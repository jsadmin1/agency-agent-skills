# Launch and handoff checks

Use with the herdr skill. These are the facts to observe, not commands to type; take syntax from the installed CLI's `--help` at the time.

## Before creating anything

- Record the installed Herdr version and read the help for `session`, `workspace` and `agent start`.
- List existing sessions. If the chosen name is already in use by anything other than this project, stop and ask for a new name. Never fall back to a default session.
- Confirm the task explicitly authorizes launch, the peer mode, and each harness's model, effort, speed and permission choice. Missing any one means plan only.
- Leave unrelated sessions and remote-access processes untouched.

## Layout

- Main: cwd = project root, label `orchestrator`.
- Peer (paired mode): cwd = `agents/co-orchestrator`, label `co-orchestrator`. Reserved mode: a plain shell, no agent. Solo: no peer surface.
- Prefer no-focus creation. If a start times out, list agents before retrying; do not start a second copy.

## Verify before the first task

For each surface, observe and record (sanitized):

- session, workspace and pane identifiers;
- harness and, when the harness exposes one, the native conversation ID (some bind only after a first bounded message: record that transition, do not invent an ID);
- actual cwd;
- model, effort, speed and effective permissions as reported by the running client, not as requested;
- that no second client is writing the same native conversation.

Record these in the new project's agent registry. Record an explicit ownership transfer after the new main acknowledges the handoff; the former setup writer then stops modifying that project's canonical state.

## Do not

- Treat a folder, a restored workspace, or a detached client as proof an agent is running.
- Paste work into a pane that holds an unsent human draft.
- Grant broad machine or account permissions because a template mentions them.
