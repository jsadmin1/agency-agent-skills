---
name: partner-message-delivery
description: Use when asked to send, deliver, notify, or hand off an authorized
  message or agent prompt to a named partner through Slack, iMessage, or
  WhatsApp, including verified fallback and delivery receipts. Complements
  voice/writing and platform-specific skills; mentioning a partner or requesting
  a draft does not authorize sending.
---
# Partner message delivery

Carry out an already-authorized partner message or handoff, verify the destination, and report only the delivery state actually observed. Use available voice/writing skills for wording and platform skills for channel mechanics; this skill owns routing and delivery evidence.

## Establish the boundary

- Read the current instruction and existing explicit authority: recipient, purpose, payload, attachments, and channel restrictions. Do not ask again when these are already authorized and unchanged.
- A named partner, a discussion about contacting them, or a draft request does not authorize a send. Keep draft work local until sending is explicitly instructed.
- Honor explicit channel-only restrictions. When the user has authorized flexible delivery or a standing fallback preference, treat a named primary channel as a preference and try a verified alternative within that authority; do not ask again merely because the primary route is unavailable. Otherwise, do not silently substitute another channel for a specifically requested one.
- Failed authentication or a missing contact does not authorize new access, signup, account changes, permission changes, or installation. Report the smallest blocker when no existing route is ready.

## Choose and verify one route

1. Select an existing supported connector or CLI for Slack, iMessage, or WhatsApp; use available native UI only when necessary. Do not install unknown clients or create accounts.
2. Verify the live sending workspace/account and recipient against trusted task bindings or user-confirmed identity. Display names alone and geographic guesses are insufficient; inspect only the minimum authorized identity data.
3. Verify conversation membership and audience: a private channel without the partner is not delivery to them, and a group must not expose the payload to unauthorized people. Recheck the destination immediately before submission.
4. For iMessage CLI use, read `references/imessage-cli.md`; installation, database access, Automation permission, and send readiness are separate facts.
5. Distinguish the partner human from their agent. Use a verified agent endpoint only within authority; otherwise send to the authorized human for relay and report agent execution unconfirmed.
6. Identify the actual sending agent when using a human account, for example “Sent by <SENDING_AGENT> on behalf of the account owner.” Keep attribution truthful and consistent with the authorized payload; do not impersonate the human.

Use one primary route and normally at most one fallback. An additional route needs a concrete reason within the existing commission. Do not shotgun-send across apps. A separately requested multi-channel notification is a deliberate exception, with separate receipts per route.

## Prepare the handoff

- Preserve the authorized text, attachment order, and intended audience. Verify actual files, their sharing scope, platform limits, and recipient access to links; a local path is not an accessible attachment.
- Do not send sensitive attachments through a fallback unless the same recipient, audience, and data scope remain authorized there. Do not widen permissions to make a link work.
- When both are needed, prepare a short human status update and a separate copyable agent prompt. State what is verified, what the partner should do, and any stop boundary; delivery does not prove execution.
- Use `SEND`, `--- START ---`, and `--- END ---` when the requested copy/paste protocol calls for them; use `/goal` only for a genuinely durable, resumable task. Small messages need no goal wrapper.
- Compose multiline UI text safely: determine whether newline submits first, use a safe compose/paste mechanism, inspect the complete text and attachments, then perform the final send. Do not type an untested multiline payload into a live composer.
- For CLI calls, prefer argument arrays with shell execution disabled; otherwise use proper shell quoting. Never interpolate message text into shell code, command substitutions, or executable templates.

## Own the attempt and resolve uncertainty

- In multi-agent or terminal-control-plane work, assign one named sender before sending. Coordinate through an existing private task record or exclusive claim, keyed to verified recipient, payload/attachment digest, and task; other agents must observe that ownership before attempting delivery.
- Keep aliases and exact contacts in existing private routing state, outside the public skill. Store only the minimum receipt needed for deduplication: owner, task/content key, route, attempt time, returned identifier, observed state, and evidence location. Do not store credentials.
- If the primary route fails provably before dispatch, try the single verified fallback within authority. Log why it was safe to switch.
- A timeout, missing response, nonzero exit, lost acknowledgement, or partial upload may have side effects. Inspect prior send status in the intended conversation or provider receipt before retrying or switching routes; an error label alone is not proof of non-delivery.
- If status is still unknown or work is in flight, record outcome unknown and stop; do not retry, use another app, or send later parts of the handoff. If some ordered parts succeeded, resume only confirmed missing parts after resolving the uncertain attempt.
- A provider-accepted submission is enough to prohibit a duplicate even when stronger confirmation is unavailable. Stop after a verified send, except the separately authorized multi-channel notification; report limited evidence honestly.
- No daemon, continuous polling, new credential storage, or auto-send wrapper belongs in this workflow. Use bounded checks already supported by the channel.

## Report the observed state

| State | Required evidence |
| --- | --- |
| Prepared | Payload and artifacts ready locally; nothing submitted |
| Submitted | Provider/transport accepted the request; stronger confirmation unavailable |
| Sent | Matching outgoing record or explicit channel send confirmation, with its limits stated |
| Delivered | Provider or UI shows recipient delivery |
| Read | Provider or UI shows a read indicator; do not infer from “sent” |
| Recipient-acknowledged | Recipient explicitly acknowledges this handoff |
| Agent-executed | Evidence from the agent's actual work or verified runtime receipt |

Do not infer one state from another or claim every channel supports every state. Report text and each attachment separately if their evidence differs. Include actual route, sending agent, observed state, private evidence pointer, and blocker/next action if any; omit private routing details from public artifacts.

## Synthetic examples

Good: “Send the approved update to <PARTNER>; any existing verified channel is fine.” Slack rejects before dispatch. The verified iMessage route receives one attempt. Report the observed outgoing status and that recipient read/agent execution remain unconfirmed.

Bad: “Draft a note for <PARTNER>.” The agent sends it, retries on WhatsApp after an ambiguous timeout, and says the partner's agent completed the work.
