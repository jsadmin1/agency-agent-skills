# V5 baseline facts

Rely on these only after re-reading the master's own `VERSION.json` and `README.md`; the master may have been replaced since this skill was written.

## What V5 is

- Product `Agent OS`, release `5.0.0`, stage `portable-workspace-kit`, `runtime_installed: false`.
- A folder kit copied once per project. The original master stays untouched.
- Layout: root `AGENTS.md` (main), `ops/` (canonical project state), `agents/orchestrator/` (main's ledger), `agents/co-orchestrator/` (peer home, with `CLAUDE.md` and `AGENTS.md`), `agents/workers/`, `work/`, `knowledge/`, `rehydration/snapshots/`, `templates/`, `prompts/FIRST-RUN.md`, `scripts/` (offline helpers), `workspace.json`.
- `workspace.json` ships with an empty project identity, `setup.status: unconfigured`, `launch_authorized: false`, and unset runtime models and permissions.
- `scripts/verify.py --release` checks a pristine master; plain `verify.py` checks a configured copy.

## What V5 does not include

Accounts, credentials, installed CLIs, live sessions, a hosted service, shared customer knowledge, or a promise of autonomous operation. No V5 command installs software, starts an agent, contacts a provider, or initializes Git. Live multi-agent operation and non-macOS runtime need target-machine verification.

## Claims you must not make

- That an installer or setup wizard exists for V5. A future installer is not built.
- That stamping a copy configured models, permissions, or a running session.
- That a different kit's layout or a recursively nested peer applies here. Follow the inspected V5 master, with main at the root.
- That a passing `verify.py` proves accounts, tools, or agents are connected.

## Provenance of this skill

Authored against a local V5 master whose `VERSION.json` SHA-256 was `651951f53a6a08542e0c1852a862078ef1a08c5ae4cbca483612db9e4ad93d08` and `MANIFEST.sha256` SHA-256 was `07f366a68798fe341675fdc1116182d8ea8a05dfcf8e90bee9b849acdc799959`. No V5 files are bundled; the script copies from the user's own master. A differing hash is not an error, but re-read the master's README before trusting the facts above.

## Distribution prerequisite

The V5 master is not distributed with this skill. The operator must supply a trusted compatible kit. The local helper does not download one or prove its provenance; establish that before running any code from it. The historical hashes above identify one development baseline, not a universal latest version.
