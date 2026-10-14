# TTS friendly mode: examples and near misses

All examples are synthetic.

## 1. Status report with noise, a cost, a deadline and a blocker

Evidence: a build log of about forty lines with timestamps; 211 tests passed and one failed (`test_invoice_rounding`); the failure may be flaky but was not re-run; staging deploy is blocked until the user supplies a payment-provider API key; the hosting upgrade is estimated at 42 dollars a month; the client demo is Friday at 5 p.m.

Weak (drops the blocker, cost and uncertainty, keeps noise):

> Build done! 211/212 tests green, just one tiny failure in test_invoice_rounding, nothing to worry about. Deploy is next.

Strong:

> The build finished, and all but one of the 212 automated checks passed. The one that failed checks how invoice totals are rounded, and I haven't re-run it yet, so I can't tell you whether it's a real bug or a one-off glitch. I can't put this on the test server until the payment provider's API key is configured through the approved secure credential flow. The hosting upgrade it needs is estimated at about forty-two dollars a month, and with the client demo on Friday at five p.m., the decision you need to make today is whether to approve that cost and complete the secure credential setup, without pasting the key into chat. The full log is saved if you want the details.

## 2. A required command is retained even without a separate request

Synthetic context: the user asks for a TTS-friendly answer and needs an authorized staging web-service restart command.

> The web server stopped because it ran out of memory, and restarting it should bring the site back, though it may happen again under heavy load until we give it more memory. The restart command is printed below; it stops the server cleanly and starts it again, and may interrupt active requests, so use it only for the confirmed staging service.

```bash
sudo systemctl restart webapp
```

## 3. "Just the gist, skip the caveats"

Evidence: the migration worked on a copy of the data; it has not been run on the live database; it requires about ten minutes of downtime.

> In short, the database change worked on a test copy, but it hasn't touched the live data yet, and running it for real will take the site offline for about ten minutes, so pick a quiet time.

The untested-on-live fact and the downtime stay: they are not caveats, they change what the user does.

## Near misses (do not trigger this skill)

| Request | Why not |
| --- | --- |
| "Build me a text-to-speech feature for my app." | Software work about TTS, not a reply to be listened to. |
| "Generate an MP3 of this paragraph." | Producing audio, not formatting a reply. |
| "Write a two-minute voiceover script for our ad." | Creative scriptwriting with its own structure. |
| "Rewrite this post in my brand voice." | Voice and identity work; this skill never changes whose voice it is. |
| "Summarize this report in plain English." with no listening cue | A normal readable summary; structure is fine. |
| "Read this file and tell me what's in it." | "Read" means open the file, not speak the answer. |
