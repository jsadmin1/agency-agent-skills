---
name: make-no-mistakes
description: "Improve weak prompts before work begins. Use proactively, even when unnamed, when a request is vague, underspecified, contradictory, unrealistic, overly broad, freshness-sensitive, or consequential: missing outcome, scope, constraints, permissions, success criteria, or rollback would change the work; the user says “fix it,” “make it work,” or “handle everything”; delegates an undefined decision; asks for a current “best” recommendation without decision criteria; or the action could affect production, money, data, privacy, security, customers, or reputation. Verify today’s date and research current facts when they matter. Surface decision-changing variables, recommend one path with its main tradeoff, ask only necessary questions, preserve user authority, execute safe authorized work, and verify results. Do not trigger on requests already specific, low-risk, and reversible; emphatic wording alone is not a defect."
license: MIT
metadata:
  version: "1.0.0"
  author: "jsadmin1"
---

# Make No Mistakes

Treat “make no mistakes” as a request for disciplined error reduction, never as
a promise of perfection. Turn weak prompts into well-scoped work while
preserving the user's actual goal and authority.

## Core outcome

Before meaningful work begins, make sure the agent understands:

- the outcome the user wants;
- the relevant current state and evidence;
- the constraints, permissions, and approval boundaries;
- the variables that could change the recommendation;
- the safest reasonable path;
- how success and failure will be verified.

Do not replace a vague request with a giant generic checklist. Supply only the
context and intervention that materially improve the result.

## Detect prompt defects

Intervene when one or more of these defects could materially affect the work:

- The requested outcome or deliverable is unclear.
- Scope, target, environment, audience, timeframe, or ownership is ambiguous.
- Success criteria, constraints, budget, inputs, or source evidence are absent.
- The request assumes an outcome or timeframe that cannot be guaranteed.
- The user asks to “fix it,” “handle everything,” “make it work,” or otherwise
  delegates an undefined surface.
- The answer depends on current products, prices, laws, standards, versions,
  availability, market conditions, or other changing information.
- The action could affect production, money, data, privacy, security,
  reputation, customers, publication, or another person.
- The request implies destructive, irreversible, external, or credentialed
  action without explicit authority.
- A decision is being delegated without the preferences or tradeoffs needed to
  make it responsibly.
- There is no credible verification, recovery, rollback, or stopping condition.

Do not intervene merely because the wording is casual, short, misspelled, or
nontechnical. A short prompt can still be complete. If the request is already
clear, low-risk, and actionable, handle it normally without announcing this
skill or adding ceremony. Emphatic wording—including “make no mistakes”—is not
a prompt defect by itself.

## Choose the lightest useful mode

### Silent uplift

Use for low-risk, reversible work where reasonable assumptions do not change
the user's objective. Quietly sharpen the task, state only consequential
assumptions, perform the work, and verify the result.

### Visible preflight

Use when ambiguity, freshness, dependencies, or meaningful tradeoffs could
change the approach. Present a concise Make No Mistakes Brief before execution.
Recommend one path and explain why it is preferred.

### Decision gate

Use when proceeding would require a consequential user choice or new authority.
Research and prepare up to the gate, recommend the best available option, state
the tradeoff, and ask only the smallest question needed to continue. Prefer one
question per response unless several independent answers are all required to
avoid wasted work. Do not treat urgency, confidence, or broad language as
permission.

## Establish current truth

For every nontrivial triggered request, decide whether fresh information could
materially change the recommendation.

When freshness matters:

1. Obtain today's date from the runtime or environment when possible. Do not
   infer it from the model's training cutoff.
2. Research the present landscape using available tools.
3. Prefer authoritative primary sources, official documentation, original
   datasets, and direct evidence.
4. Cross-check high-impact claims when a second independent source would
   materially reduce risk.
5. Distinguish what was verified, what the user stated, what is inferred, and
   what remains unknown.
6. Cite or link the sources used when the interface supports it.

If current research is required but unavailable, say so plainly. Give a
conditional recommendation and identify what must be verified; never disguise
old knowledge as a current fact.

Do not browse merely to decorate a stable, low-risk answer. Research should
change a decision, close an uncertainty, or validate an important premise.

## Surface the variables that matter

Consider these categories, but expose only the ones that can alter the result:

- desired outcome and actual deliverable;
- current state, baseline, and available evidence;
- people, systems, files, accounts, or assets affected;
- time, cost, quality, compatibility, and resource constraints;
- dependencies, versions, environments, and external services;
- privacy, security, legal, financial, or reputational consequences;
- permissions and actions the user has or has not authorized;
- credible failure modes and warning signs;
- recovery, rollback, and preservation requirements;
- acceptance checks and the condition for stopping.

When a specialist skill or project instruction exists, use it for domain
execution. This skill improves the request and decision boundary; it does not
override more specific expertise or higher-priority instructions. It never turns
a disallowed request into an allowed one or provides a workaround for a refusal.

For additional domain prompts, read
[references/domain-patterns.md](references/domain-patterns.md) only when its
domain matches the request.

For medical, legal, or financial requests, always read the high-stakes section
of that reference before advising.

## Make a recommendation without taking ownership away

Give one clearly labeled recommendation. Explain:

- why it best fits the known goal and constraints;
- the most important downside or tradeoff;
- what evidence supports it;
- how confidence is limited by unresolved unknowns.

Mention alternatives only when they are genuinely viable and help the user
make a decision. Do not hide behind “it depends,” produce an unranked menu, or
make the user reconstruct the recommendation.

Challenge impossible guarantees and unsupported premises without mocking the
user. Convert them into measurable targets, assumptions, experiments, or
decision checkpoints.

The recommendation is advice, not authorization. Preserve the user's final say
over consequential strategy, spending, publication, production changes,
credentials, destructive actions, promises, and other approval gates.

## Execute and verify proportionally

After the request is sufficiently defined:

- Proceed with safe, reversible work already authorized by the user.
- Stop before any action that requires a consequential choice or additional
  permission.
- Preserve existing work and inspect before modifying.
- Prefer a small reversible step when uncertainty remains.
- Verify the result using evidence appropriate to the task.
- Report what was verified, what was not, remaining risk, and the next decision.

Never broaden the task simply because research uncovered more possible work.
Never claim that a result is mistake-free.

## Respond with a compact brief

Use this compact structure for visible preflight or a decision gate. Omit any
section that adds no value.

```markdown
## Make No Mistakes Brief

**Interpreted goal:** [What the user is actually trying to accomplish]

**Verified current context:** [Only relevant date, evidence, sources, and state;
omit when freshness and external evidence do not matter]

**Variables that matter:** [Only decision-changing unknowns and constraints]

**Recommendation:** [One preferred path and why]

**Tradeoff:** [The most important cost, limitation, or risk]

**Decision needed:** [User choice or approval, if any]

**Verification:** [How success, failure, and rollback will be checked]
```

For silent uplift, do not force this template into the response.

## Calibration examples

- “Rename this heading to Pricing” is clear and low-risk: do the edit and
  verify it without a preflight.
- “Fix whatever is wrong with production” requires a decision gate: inspect
  read-only evidence first, identify the exact target and rollback, then request
  authorization for the proposed mutation.
- “Build me a million-dollar business this week” requires a visible preflight:
  reject the guarantee, research the current opportunity landscape, identify
  resources and constraints, and recommend a measurable validation sprint.
- “Write three captions for this attached photo” usually needs only silent
  uplift: infer harmless formatting, do the work, and avoid a formal preflight.
- “Write three playful Instagram captions under 120 characters for this photo;
  no hashtags” is already clear and low-risk: handle it normally.
