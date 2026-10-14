---
name: project-bootstrap
description: "Use when the user asks to create a new dedicated project home from
  an existing Agent OS V5 master, with specialized agent instructions, tracking,
  a project wiki and requested Herdr session. Examples: 'new project folder and
  session', 'bootstrap this project', or 'set up its orchestrator and peer'.
  Requires an operator-provided trusted V5 master; none is bundled. Not for
  migrating an existing project, merely operating an existing session, creating
  a compaction handoff, or general wiki editing."
---
# Project bootstrap (Agent OS V5)

Turn a separately supplied, verified Agent OS V5 master into a specialized project home and, when authorized, its working session. The included helper only performs the collision-safe copy. **You, the agent, complete the remaining steps in the same task**; do not hand the user another first-run prompt when their current commission already authorizes setup.

Prerequisites: an operator-provided compatible V5 master, filesystem access, and the installed orchestration/wiki tools requested by the user. This repository does not bundle the master, install those tools, or grant account access. Read `references/v5-baseline.md` and the actual master's instructions. Do not silently substitute another kit, relabel an older release, or execute an untrusted downloaded template.

## 1. Resolve the task and preserve existing work

Extract the project purpose, display name, slug, destination parent, master path, peer mode (paired, reserved, solo), and requested runtime settings. Reuse choices already provided. Ask only for a missing choice that changes ownership, cost, safety or outcome.

Inspect source/destination access and the named session. Preserve unrelated projects and processes. An existing same-project home is a reconciliation, not permission to overwrite or create duplicate conversations; inspect its tracker and resume the exact existing identities. An unrelated collision requires a different target. Stop on denied filesystem access rather than bypass privacy controls.

Record the trusted master version and hashes, and the current task's authority. Keep the outer Agent OS non-Git; only explicitly requested inner code repositories or wiki-owned initialization may use Git.

## 2. Stamp and specialize

Run the bundled helper from this skill's directory, with explicit operator paths:

```sh
python3 -B scripts/bootstrap.py stamp --source MASTER --dest PARENT/SLUG --name "Display Name" --slug SLUG
```

Inspect the dry-run, then repeat with `--apply` if the target and authority match. The helper changes only three identity fields. It refuses existing targets, nesting and symlinks; choose real paths (on macOS, `/tmp` and `/var` are aliases) and do not bypass a refusal by hand-copying.

Now complete the project-specific work yourself:

- Specialize root `AGENTS.md`, root `README.md` and `workspace.json` with the actual mission, inputs, scope, allowed tools, owners, stop conditions and verification requirements. Do not merely replace a project name.
- Main runs at the root; its ledger is `agents/orchestrator`. A paired peer runs from its real `agents/co-orchestrator` home with its own `AGENTS.md`, `CLAUDE.md` importing its instructions where that harness is selected, role/SOP, tracking, receipts, inbox/outbox and indexed snapshots. No root `CLAUDE.md`, recursive peer commissioning or duplicate root writers.
- Reserved mode creates a peer workspace as a shell only; solo mode launches no peer. A dormant peer template in the kit is not a running agent.
- Record peer mode and requested settings, but leave runtime verification and launch status pending until observed. Replace conflicting legacy topology only in the new copy.
- Give each owned scaffold directory a useful README; exclude generated caches and tool-managed internals. Parameterize customer identity and paths; never borrow private accounts or histories from another project.

## 3. Establish the requested knowledge workflow

Use the installed OpenKnowledge discovery/authoring workflow, not guessed flags. Initialize only `knowledge/project`, never the outer Agent OS. If the current task authorizes wiki setup, carry it out; stop only for a genuine installation, authentication or shared-config gate.

Give agents a knowledge map: read relevant indexed pages before work; preserve sources; mark research provisional; promote reviewed findings to articles/SOPs; maintain indexes and logs. Shared private knowledge is opt-in and scoped; a symlink is not an access control.

Verify actual index reading and one harmless write/readback through the supported API for each intended role. A directory, marker or successful initializer is not proof of a working wiki. Do not bypass a failed Markdown transport with unsynchronized writes.

## 4. Create the requested session within existing authority

Read the installed Herdr/orchestration skill and current CLI help. The helper's `herdr-plan` is a read-only hint, not authoritative current syntax.

If launch is explicitly authorized in this task, create/reuse the exact named session and requested workspaces now using the host's standardized launch tooling. If it is not, prepare the plan and report that gate. Do not ask again for authority already clearly given.

Use no-focus creation where supported. Verify actual model, effort, speed, permissions, cwd and native identity. Full technical access is not wider task authority. Do not change shared security settings or silently substitute unavailable models. A partial launch requires inspecting existing state before retrying.

## 5. Verify, review and hand off

Use `references/handoff-checks.md`. Check README coverage, specialized instructions, references/symlinks, real ownership boundaries, privacy and actual wiki/session behavior. Run the trusted kit's working-copy verifier; its pristine release manifest is provenance, not a runtime acceptance certificate.

Use the requested peer for one substantive setup review and at most one corrective follow-up. If no peer was requested or available, report that review limitation instead of manufacturing acceptance.

Write dated task tracking, an immutable indexed snapshot and a concise verification receipt containing completed/held checks, actual identities, current Git/publication state and exact next action. Follow the applicable rehydration protocol. Send the new main an attributed handoff from the setup agent, not a forged user instruction; it reads, acknowledges and waits at the commissioned stop condition. Transfer root writer ownership explicitly.

Return the canonical path, verified `cd` and attach commands, remaining gates and next step. Do not begin product implementation merely because the new environment exists.
