# Ordinary imsg CLI delivery

Read only when an existing macOS `imsg` route is being considered. Command shapes below were checked with installed **0.15.10** help on 2026-10-10; no database, account, contact, message read, or live send was tested. Recheck installed help on another host/version. Do not treat this dated check as readiness on the current machine.

## Installation and permission gates

Run these read-only inspection commands before relying on the CLI:

```sh
command -v imsg
imsg --version
imsg --help
imsg send --help
HOMEBREW_NO_AUTO_UPDATE=1 brew info steipete/tap/imsg
```

If unavailable, stop or use an already-supported alternative; installation is a separate user-authorized setup task. macOS 14+ is required for the verified release's macOS build.

1. Confirm the command is available from the app or process that will actually launch it.
2. In System Settings → Privacy & Security → Full Disk Access, enable that terminal or parent app if database-backed lookup or verification is needed.
3. Save work and relaunch only the affected app or process at a safe checkpoint when the grant requires it.
4. In System Settings → Privacy & Security → Automation, allow that app to control Messages when its entry or authorized-send prompt is available.
5. Verify the intended sending account in Messages and the authorized destination before dispatch.
6. Keep SIP enabled and use ordinary `imsg send` for text/files; leave advanced bridge features out of this workflow.

Full Disk Access governs the Messages database; Automation separately governs AppleScript control of Messages. A CLI version check proves neither. Contacts permission is optional for name resolution; prefer a verified exact handle over a display name. Do not close all terminal-control-plane sessions merely to apply a grant. Do not trigger a live send just to test permission.

Direct handle sends can be accepted without database access, but chat-ID targeting and database verification require it. If access cannot be verified within current authority, label it untested. Do not query a privacy database or scrape unrelated conversations to diagnose the gate.

## Target and command shapes

These are templates, not instructions to send without authority. Replace placeholders with verified private bindings and use one target selector per call.

```sh
imsg send --to '<VERIFIED_HANDLE>' --text '<AUTHORIZED_TEXT>' --service imessage --json
imsg send --chat-id '<VERIFIED_CHAT_ID>' --text '<AUTHORIZED_TEXT>' --json
imsg send --chat-guid '<VERIFIED_CHAT_GUID>' --text '<AUTHORIZED_TEXT>' --json
imsg send --chat-identifier '<VERIFIED_CHAT_IDENTIFIER>' --text '<AUTHORIZED_TEXT>' --json
imsg send --to '<VERIFIED_HANDLE>' --file '<AUTHORIZED_FILE_PATH>' --service imessage --json
```

`--text` and `--file` can be combined when text plus one attachment is the intended unit; use separate calls for expressly ordered parts. Inspect each result before the next part. `--file` stages the file in Messages' attachment storage, so it is a sending side effect rather than a read-only test.

For arbitrary text, use an argument array rather than replacing text inside a shell template:

```python
import subprocess

# Variables come from verified private bindings and approved content.
result = subprocess.run(
    [imsg_executable, "send", "--to", verified_handle,
     "--text", authorized_text, "--service", "imessage", "--json"],
    shell=False, capture_output=True, text=True, timeout=30,
)
# Capture return code/stdout/stderr privately; resolve uncertainty before any retry.
```

A Python timeout can still mean Messages accepted the send; it does not justify resending. Avoid verbose logs that disclose unrelated contacts or content.

`--service imessage` enforces iMessage-only sending. Default `auto` may select SMS from existing history and may fall back to SMS for a text-only phone send after proven pre-dispatch iMessage target/service failure. `--no-sms-fallback` disables that automatic retry but does not force an SMS-only thread to use iMessage; use explicit `--service imessage` for iMessage exclusivity. SMS requires existing iPhone Text Message Forwarding; this skill does not change it. Group sends use the chat's existing service; omit `--service` and verify that service fits authority.

`imsg send` cannot force a particular outgoing phone number among numbers on the same Apple account. Verify the account's routing separately; if the exact required sender cannot be established, stop rather than claiming it is selectable.

## Minimal identity and result checks

Installed help also supports these bounded read shapes, to be used only when authorized identity or receipt inspection requires them:

```sh
imsg chats --limit 5 --json
imsg group --chat-id '<VERIFIED_CHAT_ID>' --json
imsg history --chat-id '<VERIFIED_CHAT_ID>' --limit 5 --start '<ATTEMPT_START_ISO8601>' --json
```

Do not treat a recent-chat list as an exhaustive identity search. `group` can inspect direct-chat identity too. Match the intended participants and service; any lookup remains private. Limit history to the attempted recipient/time window and inspect only enough to resolve that attempt; do not copy unrelated message bodies into a receipt.

The v0.15.10 send guide documents JSON success `{"status":"sent"}`. With database access, ordinary text sends check for the matching outgoing row; without it, success can mean transport acceptance only. Report the evidence basis and do not elevate an accepted send to recipient-delivered/read.

The same guide documents failure dispositions: `not_started` proves no dispatch for that attempt; `may_have_completed` and `still_in_flight` prohibit retries/fallback until resolved. Use actual returned evidence; if absent or unreadable, treat the outcome as unknown. Attachment verification can be uncertain independently of text, so verify the intended file as well. No private bridge is needed to report an ordinary send honestly.

## Official sources

- [Official imsg README](https://github.com/openclaw/imsg/blob/main/README.md).
- [Permissions and parent-process grants](https://github.com/openclaw/imsg/blob/main/docs/permissions.md).
- [Send guide pinned to verified v0.15.10](https://github.com/openclaw/imsg/blob/v0.15.10/docs/send.md).
- [Homebrew formula and caveats](https://github.com/steipete/homebrew-tap/blob/HEAD/Formula/imsg.rb).

Documentation was inspected; send outcomes and permissions were not exercised. Consult current official guidance if local behavior differs, without weakening system security.
