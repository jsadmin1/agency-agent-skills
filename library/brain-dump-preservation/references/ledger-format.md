# Capture folder and ledger format

All examples are synthetic.

## Folder contents

| File | Written by | Mutable? |
| --- | --- | --- |
| `original/raw-records.jsonl` or `original/supplied-text.bin` | `capture` | No (read-only) |
| `original/user-text.txt` | `capture` (decoded exact user text) | No (read-only) |
| `manifest.json` | `capture` (source, selectors, ids, hashes, normalization, issues) | No |
| `chunk-map.json` | `chunk` | Not after review starts |
| `ledger.json` | you | Yes, append and update items |
| `synthesis.md` | you | Yes, the readable working view |

`raw-records.jsonl` holds the selected source lines exactly, each followed by one LF; a source line that had no final newline gains that LF, recorded as `source_final_newline: false`, so the original bytes are reconstructable. `user-text.txt` is the decoded user text: JSON escapes such as `\n` and `é` are decoded, a typed literal backslash-n stays a literal backslash-n, and multiple records or text parts are joined with the separators the manifest names. Offsets are Unicode code points into `user-text.txt`.

## ledger.json

```json
{
  "items": [
    {
      "id": "i01",
      "type": "proposal",
      "summary": "Export the report weekly",
      "evidence": [{"start": 0, "end": 30, "quote": "maybe we export it every week,"}],
      "status": "superseded",
      "superseded_by": "i02"
    },
    {
      "id": "i02",
      "type": "requirement",
      "summary": "Export the report daily instead of weekly",
      "evidence": [{"start": 1532, "end": 1571, "quote": "actually no, daily, not weekly, the rep"}],
      "status": "needs-confirmation"
    }
  ],
  "chunks_reviewed": [
    {"chunk": "c01", "items": ["i01"], "note": "weekly export floated"},
    {"chunk": "c02", "items": ["i02"], "note": "correction of c01 export cadence"}
  ]
}
```

- `type`: requirement, question, proposal, example, exclusion, aside, superseded, deferral, conflict, other.
- `status`: open, needs-confirmation, confirmed, superseded, deferred, excluded.
- `superseded` items (by type or status) must name an existing `superseded_by` item.
- `confirmed` requires `confirmed_by`: a pointer to the later user message that confirmed it, never your own inference.
- `quote` must equal the source text at `start..end` exactly; `verify` checks it.
- Optional fields: `related` (item ids), `question` (what to ask), `note`.

## Worked example: a correction that crosses a chunk boundary

Chunk c01 ends with "...and the export should go to the shared drive, every week." Chunk c02 opens "Wait, not the shared drive, that's public. Keep it local." Reading c02 alone loses what "it" is; reading c01 alone keeps a destination the user rejected. Review c02 with c01's tail: item i03 (destination: shared drive) becomes superseded by i04 (destination: local), both citing their own spans. The cadence ("every week") is not touched by this correction and stays as its own item.

## synthesis.md shape

```markdown
# Readback — <short title>
Source: manifest.json (sha256 of user-text.txt: ...). Not authorization to act.

## What I understand you want (needs your confirmation)
1. ... (i02, i04)
## Replaced or dropped along the way
- Weekly export -> daily (i01 -> i02)
## Deferred / asides
## Open questions and conflicts
1. ... (i07 vs i09)
```
