# Agency Agent Skills

Reusable skills for coding agents: clearer intent, bounded autonomy, recoverable
work, source-backed knowledge and careful tool use. Each skill is a folder with
a `SKILL.md` entrypoint and any focused references or scripts it needs.

## Skills

| Skill | Job |
| --- | --- |
| [dictation-intent](skills/dictation-intent/SKILL.md) | Interpret live dictation, scoped corrections and interruptions without guessing consequential details. |
| [brain-dump-preservation](library/brain-dump-preservation/SKILL.md) | Preserve authorized evolving prompts with source provenance, chunk coverage and a reviewable readback. |
| [tts-friendly-mode](skills/tts-friendly-mode/SKILL.md) | Make replies listenable while retaining facts and exact commands. |
| [operator-mode](skills/operator-mode/SKILL.md) | Take point on the current task without silently widening authority. |
| [make-no-mistakes](library/make-no-mistakes/SKILL.md) | Improve underspecified requests with proportionate questions and verification. |
| [project-bootstrap](skills/project-bootstrap/SKILL.md) | Set up a project from an operator-supplied trusted Agent OS V5 master. |
| [rehydration-protocol](library/rehydration-protocol/SKILL.md) | Preserve verified state before resets and ownership transfers. |
| [knowledge-base-maintenance](library/knowledge-base-maintenance/SKILL.md) | Assess and maintain a source-backed knowledge base. |
| [partner-message-delivery](library/partner-message-delivery/SKILL.md) | Deliver authorized messages with recipient and outcome verification. |
| [parallels-desktop-cli](library/parallels-desktop-cli/SKILL.md) | Operate an installed Parallels CLI with scoped lifecycle safeguards. |
| [crawl4ai](library/crawl4ai/SKILL.md) | Use an operator-configured Crawl4AI service for bounded research retrieval. |
| [creator-voice](library/creator-voice/SKILL.md) | Draft against the creator's own supplied voice and factual profile. |
| [youtube-story-development](library/youtube-story-development/SKILL.md) | Develop source-backed stories and pre-production packages. |
| [youtube-media-production](library/youtube-media-production/SKILL.md) | Produce and verify media using the operator's existing production tools. |
| [youtube-studio-chrome-operator](library/youtube-studio-chrome-operator/SKILL.md) | Operate YouTube Studio with verified channel identity and release authority. |

The V5 master, Parallels, Crawl4AI, browser control, media tools and service
accounts are **not bundled**. Do not assume a skill supplies those dependencies.

`skills/` contains the everyday general-purpose sources. `library/` contains
opt-in workflows and generic public variants. The split prevents these variants
from replacing a maintainer's personalized live skills merely because the
repository is registered as a managed source. Each individual skill folder uses
the same format and can be installed separately.

## Use a skill

Choose only the skill relevant to your task. Copy its **whole folder** into the
skill-discovery directory supported by your coding agent, or use your agent's
documented skill installer. Follow that harness's own instructions for loading
new skills; an existing conversation may need a refresh or restart. Optional
`agents/openai.yaml` files are Codex UI metadata, not universal configuration.

You can also give an agent the exact `SKILL.md` path and ask it to read the skill
and the referenced files before acting. Reading instructions does not install
tools, grant permissions, connect accounts or authorize external actions.

## What these skills do not promise

These are judgment guides, not deterministic enforcement or a guarantee of
perfect results. Structural validation and simulated examples do not prove
reliability on every model, harness or operating system. Use appropriate tests
and preserve your approval, privacy, spending and production boundaries.

Skill-specific tools remain external dependencies. This repository does not
bundle private project workspaces, account information, customer records,
commercial training libraries or third-party vendor skill collections.

See [PROVENANCE.md](PROVENANCE.md) for source and review scope, and
[LICENSE](LICENSE) for the MIT grant on original material. Existing per-skill
notices remain applicable. The original make-no-mistakes repository remains
available at https://github.com/jsadmin1/make-no-mistakes.

## Maintainer workflow

Keep one reviewed source per public skill. Make changes in a scoped candidate,
check referenced files and executable helpers, test realistic near misses, and
scan the entire intended export and Git history before publishing. Never commit
personal runtime configuration or private review receipts to this repository.
