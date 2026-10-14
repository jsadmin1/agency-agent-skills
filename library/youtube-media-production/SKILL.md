---
name: youtube-media-production
description: Produce and validate local narration, sound, generated or licensed
  visuals, captions, long-form masters, clean backgrounds, thumbnails, and
  standalone YouTube Shorts from a director-locked episode package. Use when an
  agent must run or extend the operator's own local media toolchain (for example
  FFmpeg-based rendering, local TTS, image generation, motion graphics,
  manifests and delivery packaging) while preserving separate assets,
  provenance, reproducibility, and mechanical and creative QA. This skill does
  not bundle a media pipeline. Never use it to publish.
---
# YouTube Media Production

Turn a locked episode package into local, review-ready deliverables. Do not upload, schedule, publish, change a channel, or rewrite story logic inside the edit.

This skill describes the production contract. It does not ship renderers, voice models or a pipeline; use the tools the operator already has and has validated.

## Preflight

1. Resolve the operator-supplied project root, channel, work-order ID, episode root, locked-script hash, and authorized production outputs.
2. Read the workspace/project trackers and the applicable channel bible. If the operator supplies a studio profile (roots, role ownership, required project docs, tracker paths), read it and treat live trackers as newer.
3. Run `scripts/preflight_youtube_project.py --project-root <path> --episode-root <path>`, adding `--require-doc <relative-path>` for each project document the studio treats as mandatory and `--require-tool <name>` for any tool beyond `ffmpeg`/`ffprobe`.
4. Require director-owned `SCRIPT_LOCKED`/production authorization, a rights record, an approved voice identity, and an episode-local output path. Missing or conflicting state is `STOP`.
5. Re-hash locked inputs before each expensive stage. If they drift, stop and return to story review.

## Build order

1. **Narration:** generate beat-sized segments from locked words and pronunciation/performance cues. Preserve raw takes, selected takes, narration-only WAV, compressed review audio, timestamps, model ID/revision, lawful reference, settings, and hashes.
2. **Screen-off gate:** assemble the voice-only timeline and compare it to the locked script. Fix performance or return a script defect; do not hide confusion with visuals.
3. **Sound:** build separate ambience, music/threat-pulse, effects, and narration stems. Record license/source or deterministic synthesis provenance for every sound.
4. **Visual spine:** use original, licensed, public-domain, or generated assets with recorded provenance. Keep character and location continuity. Label factual reconstructions in-frame; never fabricate evidence.
5. **Captions and overlays:** derive timings from final narration, use at most two readable lines, preserve sidecar captions, and respect the active vertical safe-zone contract.
6. **Long-form render:** create the clean silent background separately from the captioned/audio master. Use staging outputs until all QA checks pass.
7. **Standalone Shorts:** write/render only the approved independent Short recipes after the master passes. Each Short needs its own hook, complete payoff, first-frame composition, caption QA, and matching-long-form delivery field.
8. **Mechanical QA:** decode every final file; inspect streams, resolution, frame rate, pixel format, sample rate, channel layout, duration alignment, loudness, peak, silence/blank tail, captions, representative frames, and full-timeline contact sheet.
9. **Human QA:** run screen-off, phone-speaker, muted, phone-size, hook, longest-caption, climax, ending, thumbnail, rights, disclosure, and advertiser-suitability passes.
10. **Package:** finish hashes, manifests, rights, prompts, source lists, QA reports, `DELIVERY.md`, and [assets/delivery-receipt.md](assets/delivery-receipt.md).

Read [references/delivery-contract.md](references/delivery-contract.md) for the required artifact and technical contract.

## Renderer selection

- Prefer an already validated episode-local builder or a validated manifest-driven path.
- Never assume a shared renderer is generic. Inspect its CLI and configuration first.
- Preserve completed releases. A shared-source change must be backward compatible and pass the existing test suite plus a completed-episode regression check.
- Never add a new episode to a hard-coded legacy batch script merely because it is convenient.
- Use staging paths scoped by work order/run. Do not write directly into `renders/delivery/` before QA passes.

## Tool boundaries

- Use the available image-generation tool for requested original visuals; preserve prompts and generation provenance.
- Download media (for example with `yt-dlp`) only when the studio owns it or is expressly authorized to download it.
- Do not install packages, alter authentication, read secret stores, imitate a real person's voice, or use copyrighted gameplay/footage without recorded commercial rights.
- Keep model weights, caches, temporary renders, and generated bulk media local and ignored. Version lightweight scripts, prompts, manifests, rights, captions, and QA receipts.

## Completion receipt

Report the exact local paths and SHA-256 values for the master, clean background, narration-only audio, full mix, each stem, captions, each Short, thumbnail, manifests, rights record, QA report/contact sheet, and `DELIVERY.md`. Include runtime, codecs, dimensions, frame rate, sample rate, loudness, peak, decode result, unresolved findings, and requested next state. End with: `No YouTube or public publishing state was changed.`
