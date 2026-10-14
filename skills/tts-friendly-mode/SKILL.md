---
name: tts-friendly-mode
description: Use when the user asks for 'TTS mode', a 'TTS-friendly' reply,
  'make this speakable', 'say it in plain English for audio', or says they will
  listen to the answer rather than read it; also when they ask to keep or turn
  off that mode. Not for audio generation, TTS software, voiceovers, brand-voice
  writing, or an ordinary readable summary without a listening cue.
---
# TTS friendly mode

The user is going to hear this answer through a text-to-speech voice, often while doing something else. Rewrite the presentation so it sounds right spoken aloud. Do not change the substance, the facts, your confidence, or whose voice it is.

## When it applies and for how long

- An explicit mode request such as "TTS mode" stays active until the user turns it off. A clearly one-off request such as "make this reply TTS-friendly" applies only to that reply. Preserve the mode preference in the host's authorized task/session continuity when needed; do not create a permanent global preference silently.
- Turn the mode off when the user says so. A later explicit request for a table, file, diff or another conflicting format overrides presentation for that reply, without silently turning off the ongoing mode.
- Files you write to disk keep their normal structure. This mode governs the spoken reply only.

## What to produce

Use one coherent paragraph of several complete sentences, in plain everyday words, unless the current user's explicit request or higher-priority host instructions require a different structure. Lead with the outcome or the answer, then what the user needs to know or decide.

Keep, every time, anything that would change what the user decides or does next: the result, required actions and who must take them, blockers, costs and spending, deadlines and dates, risks, and how sure you are. If something was not verified, say so in words ("I haven't confirmed that yet"). Shortening is never a reason to drop one of these.

Remove what only helps a reader scanning a screen: headings, bullets, numbered lists, tables, bold, emoji, and decorative structure. Remove log noise that changes nothing. Keep exact identifiers, paths, dates and values whenever the user needs them to identify a target or take the next action; place copy-sensitive text below the spoken paragraph rather than silently dropping it.

Write for the ear:

- Explain a technical term in a few plain words the first time, or replace it. Keep the user's own names for things.
- Say numbers, money, dates and symbols the way a person would: "thirty dollars a month", "Friday at five p.m.", "about half". Avoid slashes, arrows, ampersands and raw paths, which voices read badly.
- Enumerate in sentences: "there are two problems: first X, and second Y."
- Use sentences of ordinary length. One paragraph is not one giant sentence; a run-on is as hard to follow aloud as a wall of bullets.
- Match the facts' tone. No hype, forced cheerfulness, or reassurance the evidence does not support, and no extra hedging the evidence does not require.

## When it will not fit

Plain-language shortening need not repeat every raw log line. It must retain every decision-critical fact, including all blockers, costs, deadlines, required actions and uncertainty. Use additional sentences rather than omit them. Offer a linked detailed artifact for supporting evidence, not as a replacement for what the user needs to decide.

## Exact code and commands

Never drop a command or exact text the user must run or copy, even if they did not separately ask for it. Put each required command or copy-sensitive item in an appropriately labeled code block after the paragraph. Say what it does and that it is printed below, so the spoken portion stands alone. Do not spell long commands aloud in the paragraph. Describe purely illustrative commands in words when their exact bytes are unnecessary. Formatting never authorizes the action described.

## When tempted

| The thought | What to do instead |
| --- | --- |
| "They asked for short, so I can drop the cost." | Short means fewer words, not fewer decisions. Say the cost in one clause. |
| "The caveat sounds negative; I'll leave it out." | An unverified result read aloud as done is a false statement. Keep the uncertainty. |
| "I'll keep the bullets; it's clearer." | Bullets are read as symbols or flattened. Use "first, second, and finally." |
| "Everyone knows what idempotent means." | Say "safe to run twice" instead. |
| "I'll pack it all into one long sentence to keep one paragraph." | Split into normal sentences; the paragraph rule is about structure, not sentence count. |
| "They're listening, so the required command is useless." | Keep the exact command below the paragraph; audio cannot replace executable text. |
| "I'll sound upbeat so it's pleasant to hear." | Tone follows the evidence. Bad news is said plainly and calmly. |

For worked examples and near misses, read `references/examples.md` when the case is unclear.
