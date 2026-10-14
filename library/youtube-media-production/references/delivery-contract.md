# Delivery Contract

## Episode package

Preserve at minimum:

```text
episode-root/
  brief.md
  storyboard.md
  script.locked.md
  script_segments.json
  rights.json
  production_manifest.json
  prompts/
  audio/raw/
  audio/selected/
  audio/stems/
  audio/master/
  visuals/source/
  visuals/overlays/
  renders/staging/
  renders/review/
  renders/delivery/
  renders/qa/
  shorts/
  qc/
  DELIVERY.md
```

Use the applicable channel contract when names differ. Never delete or overwrite accepted assets without preserving their provenance/hash.

## Example vertical delivery baseline

Confirm against the current channel contract and platform requirements before use.

- Canvas: 1080x1920 native 9:16
- Frame rate: 30 fps
- Video: H.264 High, yuv420p
- Audio: AAC stereo, 48 kHz
- Master audio target: approximately -14 to -16 LUFS integrated, no higher than -1 dBTP
- Shorts: independently edited 45-90 second complete units unless current platform/brief requirements specify a narrower band

For any 16:9 commission, create a separate 1920x1080 edit from source assets. Never auto-crop the finished vertical master.

## Required QA evidence

- Full FFmpeg decode with zero errors for every delivery file
- FFprobe stream report and exact duration alignment
- Audio loudness and peak report
- First frame, hook, longest caption, midpoint, climax, CTA, and final frame
- Full-timeline contact sheet
- Screen-off, phone-speaker, muted, and phone-size review
- Caption truncation/safe-zone review
- Rights, disclosure, synthetic/reconstruction label, and advertiser review
- File sizes and SHA-256 hashes

`PASS` requires evidence from the final delivery bytes, not a proxy or intermediate.
