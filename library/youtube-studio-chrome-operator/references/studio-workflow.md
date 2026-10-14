# YouTube Studio Workflow

## Channel creation and configuration

1. Resolve the intended Google account/Brand Account and confirm the exact proposed name/handle against the approved brand package.
2. Create only the authorized channel. Do not accept unexpected terms or security/identity steps without the required user handoff.
3. Record immutable channel ID, public name, handle, account mapping, creation time, and public URL.
4. Upload approved icon, banner, description, watermark, and keywords as separately authorized assets. Verify public desktop/mobile rendering.
5. Set the correct general-audience/made-for-kids default from the channel bible. Never choose an audience setting for convenience.
6. Inspect Standard, Intermediate, and Advanced feature eligibility. Do not assume verification transfers because channels share a Google account.
7. Keep the first pilot private until its channel, story/source, media, and release gates pass.

## Upload or edit preflight

Lock:

- channel ID and current signed-in account
- exact local file path, size, SHA-256, and delivery designation
- title, description, tags/keywords, playlist, language, and category where applicable
- audience setting and rationale
- altered/synthetic disclosure and rationale
- thumbnail and caption paths/hashes
- long-form/Short classification
- related long-form video ID when the approved Short workflow requires one; otherwise explicitly not applicable
- visibility or exact schedule with IANA time zone and UTC offset
- expected checks/processing state before release

## Long-form upload

1. Upload the exact delivery master, not a review proxy or clean background.
2. Enter only approved metadata.
3. Set audience and synthetic-content fields explicitly.
4. Add the approved custom thumbnail and sidecar captions when authorized/available.
5. Wait for processing and copyright/checks to reach the required state.
6. Save as private unless the same exact release record authorizes visibility/scheduling.
7. Re-open and verify server state. Record the video ID immediately.

## Short upload or edit

1. Verify the file is the standalone approved Short.
2. Set approved metadata, audience, and disclosure.
3. If a matching long-form link is required, confirm its exact target is public/unlisted and eligible. Otherwise record that the approved Short is standalone.
4. For a required link, select the exact related long-form video ID, save, re-open, and verify. Do not invent a target for an approved standalone Short.
5. Only then schedule/publish if authorized.
6. When a related-video link was required, verify its destination from the public Short page when available.

## Scheduling or immediate publication

1. Re-open the exact video and confirm processing/checks, metadata, thumbnail, captions, audience, disclosure, and relationship.
2. Set one exact visibility state. For scheduling, enter the exact date/time/zone once.
3. Save once, re-open, and verify the exact saved server state.
4. At or after publication, verify a fresh public URL. Do not infer public state from a Studio toast.

## Ambiguous response recovery

- A spinner, timeout, Wi-Fi loss, or browser disconnect does not prove failure.
- Reconnect to Chrome, obtain a fresh tab if needed, and inspect the server state read-only.
- If expected state is present, treat the mutation as successful and the release record as consumed.
- If expected state is absent, stop and return evidence. Do not upload a duplicate or click Save/Publish again without renewed authorization.
- Never delete/reupload to solve an uncertain state unless separately authorized after exact ID resolution.
