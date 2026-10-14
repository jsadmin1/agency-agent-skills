---
name: rehydration-protocol
description: "Continuity protocol for surviving context compaction, a context
  reset, a harness switch or a hand-off to another agent without losing state or
  inventing it afterwards. Use when the user says 'run the rehydration
  protocol', 'can we compact', 'update tracking and hand off', 'write a
  handoff', 'prepare to restart', when a work phase closes cleanly, before a
  planned reset, or before transferring ownership of work to another agent.
  Produces, in order: updated trackers, an indexed immutable snapshot on disk,
  and a pasteable restart prompt. Works in any agent harness with lossy native
  compaction."
---
# Rehydration protocol

## Why this exists

Native compaction replaces a long session with a much shorter summary. That summary cannot carry everything that mattered. What it tends to lose: exact file paths, why a decision was made rather than just what it was, which claims were verified versus assumed, partially applied state, and the difference between "pushed" and "local only".

The next session then fills the gaps confidently. It remembers that a decision existed but not its shape, and invents the rest.

**Premise: the documents on disk are the memory, not the summary.** The summary is only a pointer into them, so the documents must carry real descriptions written for a reader with no conversational context.

## Locations

Use the project's existing conventions. If the project has none, ask once and then use:

- **Instruction file** — the project's agent instruction file (for example `AGENTS.md` or `CLAUDE.md`).
- **Trackers** — the project's timeline/status document (here called `TRACKING.md`) and its decisions or open-questions document (here called `DECISIONS.md`).
- **Snapshots** — a `rehydration/snapshots/` folder with an `INDEX.md` listing every snapshot.

Write only trackers you own. If another agent or person is the designated writer of a shared document, hand them the update instead of editing it.

## When to run it

- The user asks for it by name, or asks about compacting or restarting.
- A work phase closes cleanly: planning ends, execution begins, a project is handed off.
- Before any planned context reset or harness switch.
- Before ownership of work moves to another agent. This is mandatory regardless of context pressure, because the other agent shares no context window.

Do not wait for context pressure. A clean boundary is a better trigger than a full context window.

## The four steps, in order

### 1. Update the trackers

- Timeline tracker: add a dated, timezone-aware block at the top stating current state. Supersede stale claims explicitly; never silently rewrite dated evidence.
- Decisions tracker: fold in every decision made, ownership change and re-prioritization, and every open question that needs an answer.
- Any other project-local tracker that changed.

Capture a hash baseline before editing a shared document and re-verify it immediately before saving. If it changed underneath you, stop and report the collision rather than overwriting.

### 2. Write the snapshot, then index it

Path: `rehydration/snapshots/YYYY-MM-DD-HHMM-slug.md`. Treat it as immutable once written; corrections go in a new snapshot or a dated addendum. Add one row to `rehydration/snapshots/INDEX.md` so the next session selects a snapshot from the index instead of scanning the folder.

Required sections:

| Section | Must contain |
| --- | --- |
| Current objective | What this session was for, and whether execution started |
| Read these first | Ordered list of files, with why each matters |
| Files changed | Table: path → what changed |
| Live vs local-only | What is pushed or deployed, what exists on one disk, what is uncommitted |
| Verified state | Only what was actually inspected this session |
| Decisions made | Numbered, each with its reasoning, including overrides |
| User-stated facts | Anything the user said that corrects a stale document |
| Risks and blockers | Named, with what unblocks each |
| Exact next actions | Numbered and specific enough to execute without asking |
| Do not | Explicit prohibitions carried forward |

Label each claim as **verified**, **user-stated** or **assumed**. Never bridge a gap with a guess; the next session cannot tell the difference.

### 3. Produce the restart prompt

Output it in a copyable block for the user to paste after compaction. It points at the instruction file first, then the snapshot, then the decisions tracker, and it carries a **descriptive** summary, not a list of filenames.

```text
We just compacted a long session. Before doing any work:

1. Read <instruction file> and follow it.
2. Read the snapshot:
   <absolute path to snapshot>
3. Read the decisions tracker — this is the entry point for priorities:
   <path to DECISIONS.md>
4. Skim only the top blocks of:
   <path to TRACKING.md>

What happened last session:
<6-12 lines. What we set out to do, what was actually verified, what changed
on disk, what was decided and why, any pivots or overrides.>

What we are about to do:
<the immediate next action, concretely>

Deferred, with descriptions in the decisions tracker:
<short list — name each item and one clause on what it is>

After reading, summarize your understanding of: current objective, live vs
local-only state, standing approval gates, and the exact next action.
Do not re-plan. Do not restart from scratch.
```

### 4. Only then compact or hand off

Confirm all three artifacts exist before the reset or transfer. If any step is incomplete, say so; do not let a reset happen against a partial handoff.

## Quality bar

The test: **could a competent agent with zero conversational context resume correctly from these documents alone?** If any item would make it ask "what does that refer to", the description is too thin.

Common failures:

- Naming a decision without its reasoning, so the next session cannot defend or revisit it.
- Listing filenames as if they explain themselves.
- Recording a plan as though it were completed work.
- Omitting what is *not* done, or what is explicitly forbidden.
- Bloating with narrative. Descriptions should be dense, not long.
- Putting secrets, credentials or unnecessary personal data in trackers or snapshots.

## Harness notes

The steps are the same in every harness; only the instruction file named in step 1 differs. Harnesses with stronger native compaction may need the protocol less often for context pressure, but never skip it for a hand-off between agents.
