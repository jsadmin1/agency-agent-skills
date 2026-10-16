#!/usr/bin/env python3
"""Brain-dump preservation helper: inspect, capture, chunk, verify.

Standard library only. No network, no clipboard, no cross-file search.
Offsets are Python str indices (Unicode code points) into the decoded text.

  bdp.py inspect --jsonl FILE [--tail N]
  bdp.py capture (--jsonl FILE --lines 12,14-15 | --text-file FILE --provenance TEXT)
                 --root AUTHORIZED_DIR --out DIR
                 [--conversation-id ID] [--include-nonhuman] [--sensitive-authorized]
  bdp.py chunk   --capture DIR [--target 1500]   (1..MAX_TARGET)
  bdp.py verify  --capture DIR

Exit codes: 0 ok, 1 verification failed, 2 input/capture gate, 3 sensitive gate.
"""
import argparse, datetime, hashlib, json, os, re, stat, sys

SECRET_PATTERNS = [
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"\bAKIA[0-9A-Z]{16}\b", r"\bsk-[A-Za-z0-9_-]{20,}",
    r"\bgh[pousr]_[A-Za-z0-9]{30,}", r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    r"(?i)\b(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*\S{8,}",
]
WRAPPER = re.compile(r"^\s*<([a-z][a-z0-9_-]*)>")
TYPES = {"requirement", "question", "proposal", "example", "exclusion", "aside",
         "superseded", "deferral", "conflict", "other"}
STATUSES = {"open", "needs-confirmation", "confirmed", "superseded", "deferred", "excluded"}
MAX_TARGET = 1_000_000


def sha(b):
    return hashlib.sha256(b).hexdigest()


def gate(msg, code=2):
    print("GATE: " + msg, file=sys.stderr)
    sys.exit(code)


def split_lines(data):
    """Return [(line_no, raw_bytes_without_newline, had_newline)] without losing bytes."""
    out, start, n = [], 0, 1
    while start < len(data):
        end = data.find(b"\n", start)
        if end == -1:
            out.append((n, data[start:], False))
            break
        out.append((n, data[start:end], True))
        start, n = end + 1, n + 1
    return out


def extract(obj):
    """Harness-agnostic best effort: (role, kind, [text parts], record_id, timestamp)."""
    src = obj
    for key in ("message", "payload"):
        if isinstance(obj.get(key), dict):
            src = obj[key]
            break
    role = src.get("role") or obj.get("role")
    content = src.get("content", src.get("text"))
    parts, other = [], set()
    if isinstance(content, str):
        parts.append(content)
    elif isinstance(content, list):
        for p in content:
            if isinstance(p, str):
                parts.append(p)
            elif isinstance(p, dict) and p.get("type") in ("text", "input_text") and isinstance(p.get("text"), str):
                parts.append(p["text"])
            elif isinstance(p, dict):
                other.add(p.get("type") or "unknown")
    if obj.get("isCompactSummary") or obj.get("type") == "summary":
        kind = "summary"
    elif obj.get("isMeta"):
        kind = "meta"
    elif role != "user":
        kind = "non_user"
    elif "tool_result" in other:
        kind = "tool_result"
    elif not parts:
        kind = "no_text"
    elif WRAPPER.match(parts[0]):
        kind = "injected_wrapper"
    else:
        kind = "human_text"
    rid = obj.get("uuid") or obj.get("id") or src.get("id")
    ts = obj.get("timestamp") or src.get("timestamp")
    return role, kind, parts, rid, ts, sorted(other)


def parse_selector(sel):
    lines = set()
    for piece in sel.split(","):
        piece = piece.strip()
        if "-" in piece:
            a, b = piece.split("-", 1)
            lines.update(range(int(a), int(b) + 1))
        elif piece:
            lines.add(int(piece))
    return sorted(lines)


def read_source(path):
    if not os.path.isfile(path):
        gate(f"source not found or not a file: {path}. State the limitation; ask for an export or exact supplied text.")
    with open(path, "rb") as fh:
        return fh.read()


def cmd_inspect(a):
    rows = split_lines(read_source(a.jsonl))
    for n, raw, nl in rows[-a.tail:] if a.tail else rows:
        try:
            role, kind, parts, rid, ts, other = extract(json.loads(raw.decode("utf-8")))
            text = "\n".join(parts)
            print(f"{n}\t{kind}\t{role}\t{rid}\t{ts}\tchars={len(text)}\t{text[:60]!r}")
        except (ValueError, UnicodeDecodeError, AttributeError):
            print(f"{n}\tparse_error\t-\t-\t-\tbytes={len(raw)}\tfinal_newline={nl}")


def scan_sensitive(text):
    return [p for p in SECRET_PATTERNS if re.search(p, text)]


def write_new(path, data, mode, dir_fd=None):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=dir_fd)
    with os.fdopen(fd, "wb") as fh:
        fh.write(data)
        os.fchmod(fh.fileno(), mode)


def open_destination(out, root):
    """Create OUT as a new directory strictly inside the real path of ROOT; return (dir_fd, real_path).

    Rejects '..' components, resolves every existing ancestor (symlinks included) and requires the
    result inside ROOT, then creates each missing component with mkdir + O_NOFOLLOW relative to the
    already-verified parent descriptor, so a later symlink swap cannot redirect creation."""
    if not root:
        gate("--root is required: the explicit authorized directory captures must stay inside.")
    if ".." in out.replace("\\", "/").split("/"):
        gate(f"destination contains '..': {out}. Give a direct path inside the authorized root.")
    real_root = os.path.realpath(root)
    if not os.path.isdir(real_root):
        gate(f"authorized root is not an existing directory: {root}")
    path = os.path.abspath(out)
    missing, anc = [os.path.basename(path)], os.path.dirname(path)
    while not os.path.lexists(anc):
        missing.insert(0, os.path.basename(anc))
        anc = os.path.dirname(anc)
    real_anc = os.path.realpath(anc)
    if not (real_anc == real_root or real_anc.startswith(real_root.rstrip(os.sep) + os.sep)):
        gate(f"destination resolves outside the authorized root: {out} -> {os.path.join(real_anc, *missing)} "
             f"(root {real_root}). Nothing was written.")
    try:
        fd = os.open(real_anc, os.O_RDONLY | os.O_DIRECTORY)
    except OSError as exc:
        gate(f"destination ancestor is not a usable directory: {real_anc} ({exc.strerror})")
    for i, name in enumerate(missing):
        try:
            os.mkdir(name, 0o700, dir_fd=fd)
        except FileExistsError:
            os.close(fd)
            gate(f"destination already exists: {out}. Captures are never overwritten; choose a new destination.")
        nfd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
        os.close(fd)
        fd = nfd
    return fd, os.path.join(real_anc, *missing)


def retained_scan_text(raw_lines):
    """Everything capture keeps, for the sensitivity scan: each raw line as bytes-decoded text
    (undecodable bytes replaced, so ASCII patterns still match) plus the JSON-decoded form of
    every parseable line, so escaped metadata, non-text parts and tool fields are all covered."""
    out = []
    for raw in raw_lines:
        out.append(raw.decode("utf-8", "replace"))
        try:
            out.append(json.dumps(json.loads(raw.decode("utf-8")), ensure_ascii=False))
        except (ValueError, UnicodeDecodeError):
            pass
    return "\n".join(out)


def cmd_capture(a):
    if os.path.lexists(a.out):
        gate(f"destination already exists: {a.out}. Captures are never overwritten; choose a new destination.")
    if not a.root:
        gate("--root is required: the explicit authorized directory captures must stay inside.")
    now = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")
    records, raw_out, segments, issues, conflicts = [], b"", [], [], []
    if a.jsonl:
        if not a.lines:
            gate("--lines is required with --jsonl; select the exact records, never the whole history.")
        data = read_source(a.jsonl)
        rows = {n: (raw, nl) for n, raw, nl in split_lines(data)}
        seen_raw, seen_id, texts, raw_lines = {}, {}, [], []
        for n in parse_selector(a.lines):
            if n not in rows:
                gate(f"line {n} does not exist in source ({len(rows)} lines).")
            raw, nl = rows[n]
            rec = {"line": n, "raw_sha256": sha(raw), "raw_bytes": len(raw), "source_final_newline": nl}
            raw_out += raw + b"\n"
            raw_lines.append(raw)
            if raw in seen_raw:
                rec.update(status="duplicate_event", duplicate_of_line=seen_raw[raw])
                records.append(rec)
                continue
            seen_raw[raw] = n
            try:
                obj = json.loads(raw.decode("utf-8"))
                role, kind, parts, rid, ts, other = extract(obj)
            except (ValueError, UnicodeDecodeError, AttributeError) as exc:
                rec.update(status="undecodable", error=type(exc).__name__)
                issues.append(f"line {n}: not valid JSON/UTF-8 (truncated or corrupt); raw bytes preserved, text missing")
                records.append(rec)
                continue
            rec.update(role=role, kind=kind, record_id=rid, timestamp=ts, other_part_types=other,
                       part_count=len(parts))
            if rid is not None and rid in seen_id:
                rec["id_conflict"] = {"record_id": rid, "other_line": seen_id[rid], "status": "unresolved"}
                conflicts.append({"record_id": rid, "lines": [seen_id[rid], n], "status": "unresolved",
                                  "note": "same record id, different raw payload; neither is assumed canonical"})
                issues.append(f"line {n}: record id {rid!r} also used by line {seen_id[rid]} with a different "
                              "payload; unresolved ID conflict. Reselect one representation or confirm with the user.")
            elif rid is not None:
                seen_id[rid] = n
            if kind != "human_text" and not a.include_nonhuman:
                gate(f"line {n} is '{kind}', not plain human text. Do not assume every user-role record is a "
                     "human instruction; reselect, or pass --include-nonhuman if the user confirmed it.")
            text = "\n".join(parts)
            try:
                text.encode("utf-8")
            except UnicodeEncodeError:
                rec.update(status="undecodable", error="lone_surrogate")
                issues.append(f"line {n}: text contains unpaired surrogate; raw preserved, text missing")
                records.append(rec)
                continue
            if any(t == text for t in texts):
                rec["note"] = "same text as an earlier selected record with different raw bytes; kept, review"
            texts.append(text)
            rec["status"] = "decoded"
            records.append(rec)
            segments.append((rec, text))
        source = {"type": "native_jsonl", "path": os.path.abspath(a.jsonl), "size_at_read": len(data),
                  "conversation_id": a.conversation_id, "selector": a.lines,
                  "format_note": "harness-specific JSONL; extraction is best-effort and recorded per line"}
    else:
        if not a.provenance:
            gate("--provenance is required with --text-file (who supplied it, how, when).")
        raw_out = read_source(a.text_file)
        try:
            text = raw_out.decode("utf-8")
        except UnicodeDecodeError:
            gate("supplied text is not valid UTF-8; ask for a UTF-8 export rather than guessing.")
        segments.append(({"line": None, "status": "decoded"}, text))
        source = {"type": "supplied_text", "native_record": False, "path": os.path.abspath(a.text_file),
                  "provenance": a.provenance, "raw_sha256": sha(raw_out)}
        raw_lines = [raw_out]
    if conflicts:
        source["id_conflicts"] = conflicts
    sep = "\n\n"
    combined, pos = "", 0
    for i, (rec, text) in enumerate(segments):
        if i:
            combined += sep
            pos += len(sep)
        rec["text_start"], rec["text_end"] = pos, pos + len(text)
        combined += text
        pos += len(text)
    hits = scan_sensitive(combined + "\n" + retained_scan_text(raw_lines))
    if hits and not a.sensitive_authorized:
        gate("possible secret-bearing content detected; nothing was written. Do not redact and call it verbatim. "
             "Proceed only with explicit authorization for restricted local storage (--sensitive-authorized).", 3)
    text_bytes = combined.encode("utf-8")
    fmode = 0o400  # retained originals are always owner-only
    dfd, real_out = open_destination(a.out, a.root)
    os.mkdir("original", 0o700, dir_fd=dfd)
    ofd = os.open("original", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=dfd)
    raw_name = "raw-records.jsonl" if a.jsonl else "supplied-text.bin"
    write_new(raw_name, raw_out, fmode, dir_fd=ofd)
    write_new("user-text.txt", text_bytes, fmode, dir_fd=ofd)
    manifest = {
        "schema": 1, "captured_at": now, "source": source, "records": records,
        "files": {f"original/{raw_name}": sha(raw_out), "original/user-text.txt": sha(text_bytes)},
        "text": {"unit": "unicode_code_points", "length": len(combined), "record_separator": sep if len(segments) > 1 else None,
                 "part_separator": "\n", "final_newline_added": False},
        "normalization": ["raw-records.jsonl stores each selected source line followed by one LF"] if a.jsonl else
                         ["supplied text stored byte-identical; decoded as UTF-8 without other changes"],
        "complete": not issues, "issues": issues, "id_conflicts": conflicts,
        "destination": {"authorized_root": os.path.realpath(a.root), "real_path": real_out},
        "sensitive": {"suspected": bool(hits), "authorized_local_only": bool(hits), "export_prohibited": bool(hits),
                      "scanned": "decoded user text and every retained raw byte, metadata and non-text part"},
    }
    write_new("manifest.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"), fmode, dir_fd=dfd)
    os.fchmod(ofd, 0o500)
    os.close(ofd)
    os.close(dfd)
    print(json.dumps({"out": real_out, "complete": manifest["complete"], "chars": len(combined),
                      "records": len(records), "issues": issues}, ensure_ascii=False))
    if issues:
        gate("capture is INCOMPLETE (see manifest issues); raw bytes kept. Do not summarize as if complete.")


def load_capture(d):
    with open(os.path.join(d, "manifest.json"), encoding="utf-8") as fh:
        man = json.load(fh)
    with open(os.path.join(d, "original", "user-text.txt"), "rb") as fh:
        tb = fh.read()
    return man, tb


def cmd_chunk(a):
    if not 1 <= a.target <= MAX_TARGET:
        gate(f"--target must be an integer from 1 to {MAX_TARGET}; got {a.target}.")
    man, tb = load_capture(a.capture)
    text = tb.decode("utf-8")
    path = os.path.join(a.capture, "chunk-map.json")
    if os.path.exists(path):
        gate("chunk-map.json exists; chunk maps are not regenerated over reviewed work.")
    chunks, start = [], 0
    while start < len(text):
        end = min(len(text), start + a.target)
        if end < len(text):
            window = text[start:end]
            for boundary in ("\n\n", "\n", ". ", "? ", "! "):
                k = window.rfind(boundary)
                if k > a.target // 3:
                    end = start + k + len(boundary)
                    break
        seg = text[start:end]
        chunks.append({"id": f"c{len(chunks) + 1:02d}", "start": start, "end": end,
                       "line_start": text.count("\n", 0, start) + 1, "line_end": text.count("\n", 0, max(start, end - 1)) + 1,
                       "sha256": sha(seg.encode("utf-8")), "head": seg[:40], "tail": seg[-40:]})
        start = end
    out = {"text_sha256": sha(tb), "unit": "unicode_code_points", "chunks": chunks,
           "context_rule": "review each chunk with the previous chunk's tail and the next chunk's head"}
    write_new(path, (json.dumps(out, ensure_ascii=False, indent=2) + "\n").encode("utf-8"), 0o644)
    print(f"{len(chunks)} chunks over {len(text)} code points -> {path}")


def cmd_verify(a):
    errs = []
    man, tb = load_capture(a.capture)
    for rel, want in man["files"].items():
        with open(os.path.join(a.capture, rel), "rb") as fh:
            if sha(fh.read()) != want:
                errs.append(f"frozen file changed: {rel}")
    text = tb.decode("utf-8")
    if not man.get("complete"):
        errs.append("capture marked incomplete: " + "; ".join(man.get("issues", [])))
    cm_path, lg_path = os.path.join(a.capture, "chunk-map.json"), os.path.join(a.capture, "ledger.json")
    if not os.path.exists(cm_path):
        errs.append("chunk-map.json missing")
        chunks = []
    else:
        cm = json.load(open(cm_path, encoding="utf-8"))
        chunks = cm["chunks"]
        if cm.get("text_sha256") != sha(tb):
            errs.append("chunk map was built for different text")
        pos = 0
        for c in chunks:
            if c["start"] != pos:
                errs.append(f"{c['id']}: gap or overlap at {pos}..{c['start']}")
            if sha(text[c["start"]:c["end"]].encode("utf-8")) != c["sha256"]:
                errs.append(f"{c['id']}: span hash mismatch")
            pos = c["end"]
        if pos != len(text):
            errs.append(f"chunks end at {pos}, text length {len(text)}: uncovered tail")
    items = {}
    if not os.path.exists(lg_path):
        errs.append("ledger.json missing")
    else:
        lg = json.load(open(lg_path, encoding="utf-8"))
        items = {i["id"]: i for i in lg.get("items", [])}
        reviewed = {r["chunk"] for r in lg.get("chunks_reviewed", [])}
        for c in chunks:
            if c["id"] not in reviewed:
                errs.append(f"{c['id']}: not marked reviewed in ledger")
        for r in lg.get("chunks_reviewed", []):
            for ref in r.get("items", []):
                if ref not in items:
                    errs.append(f"review of {r['chunk']} cites unknown item {ref}")
        for i in items.values():
            if i.get("type") not in TYPES:
                errs.append(f"{i['id']}: unknown type {i.get('type')}")
            if i.get("status") not in STATUSES:
                errs.append(f"{i['id']}: unknown status {i.get('status')}")
            if not i.get("evidence"):
                errs.append(f"{i['id']}: no evidence span")
            for ev in i.get("evidence", []):
                s, e = ev.get("start", -1), ev.get("end", -1)
                if not (0 <= s < e <= len(text)) or text[s:e] != ev.get("quote"):
                    errs.append(f"{i['id']}: evidence quote does not match source span {s}..{e}")
            if (i.get("type") == "superseded" or i.get("status") == "superseded") and i.get("superseded_by") not in items:
                errs.append(f"{i['id']}: superseded without a valid superseded_by item")
            if i.get("status") == "confirmed" and not i.get("confirmed_by"):
                errs.append(f"{i['id']}: confirmed without a confirmed_by reference to a later user message")
    for e in errs:
        print("FAIL: " + e)
    print(json.dumps({"chunks": len(chunks), "items": len(items), "failures": len(errs)}))
    sys.exit(1 if errs else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("inspect"); s.add_argument("--jsonl", required=True); s.add_argument("--tail", type=int, default=20)
    s = sub.add_parser("capture")
    g = s.add_mutually_exclusive_group(required=True); g.add_argument("--jsonl"); g.add_argument("--text-file")
    s.add_argument("--lines"); s.add_argument("--provenance"); s.add_argument("--out", required=True)
    s.add_argument("--root", help="explicit authorized directory; the destination must resolve inside it")
    s.add_argument("--conversation-id"); s.add_argument("--include-nonhuman", action="store_true")
    s.add_argument("--sensitive-authorized", action="store_true")
    s = sub.add_parser("chunk"); s.add_argument("--capture", required=True); s.add_argument("--target", type=int, default=1500)
    s = sub.add_parser("verify"); s.add_argument("--capture", required=True)
    a = p.parse_args()
    {"inspect": cmd_inspect, "capture": cmd_capture, "chunk": cmd_chunk, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    main()
