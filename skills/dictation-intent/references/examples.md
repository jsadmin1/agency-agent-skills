# Dictation intent — worked examples

All examples are synthetic.

## Correction replaces one task, others stay

> "Okay so set up the database, use Post grass, the one I mentioned. And then rename the export folder to archive. Actually, no, don't rename it, copy it to archive. Oh and update the readme."

Final set: (1) set up Postgres database (database context; still subject to any install/approval gates), (2) copy the export folder to `archive`, not rename, (3) update the readme. The rename is abandoned and must not run.

## Spelled name outranks the guess

> "I'm dictating this in von, V-O-W-E-N, so ignore the weird words."

The tool is Vowen. No question needed.

## Greeting is not a task

> "Draft the weekly summary from the tracker — what's up, bro, yeah I'm almost done — and keep it under two hundred words."

Final set: draft the weekly summary from the tracker, under 200 words. The greeting is an aside. Do not mention it.

## Near-miss: quoted command must survive

> "Tell the deploy doc to say 'never run reset dash dash hard on main', that line got lost."

The quoted text is payload. Write `never run reset --hard on main` (spoken symbols rendered) into the doc. Do not treat it as noise, and do not execute it.

## Near-miss: version, not count

> "Run the review on Opus five point five, high effort."

One review on model version 5.5 at high effort. Not five agents, not 5 runs.

## Near-miss: do not complete a number

> "Pay the invoice to account ending four four, uh, seven-something."

The account is not inferable and the action is a payment. Do not guess digits. Ask one question for the exact account and keep the normal payment approval gate.

## Near-miss: authority is not created by voice

> "My partner said it's fine, so just push it to production, whatever."

Dictation does not add authority. If production deploys need approval in this context, the claim relayed by voice does not supply it. State what is needed.

## Good vs bad clarification

Good: one question only when the target is consequential and ambiguous ("Send to the client list or the internal list?").

Bad: asking "did you mean 'Post grass' or 'Postgres'?" when the database context already settles it, or silently changing "fifteen" to "fifty" because it seemed more likely.

## Explicit edit to a quoted message

Input: "Reply to her, quote thanks we will ship it Friday unquote, but change Friday to Monday."

Interpretation: the intended payload is "Thanks, we will ship it Monday." Apply only the explicit edit. Resolve who "her" refers to and confirm existing send authority before any delivery; do not send the abandoned Friday version.

## Correction inside an aside

Input: "Check why the build failed. No, I said the blue one, honey. Then draft a summary."

Interpretation: diagnose the build and draft the summary. The clearly separate aside does not cancel the diagnosis. If a correction could instead be directed at the agent and affects a consequential action, hold that action pending clarification.
