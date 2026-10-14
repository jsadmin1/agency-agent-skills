# Domain Patterns

Read only the section matching the active request. These are prompts for
judgment, not mandatory checklists. Surface an item only when it can change the
recommendation, permission boundary, or verification plan.

## Software and coding

- Identify the repository, target behavior, baseline, affected interfaces, and
  success criteria.
- Inspect applicable project instructions and current version-control state.
- Preserve unrelated changes and determine whether the request authorizes a
  diagnosis, a change, or both.
- Check dependency and version assumptions against current official
  documentation when they are material.
- Define proportionate tests, failure handling, compatibility, and rollback.

## Infrastructure, databases, and production systems

- Distinguish local, development, staging, and production targets.
- Begin with read-only evidence unless mutation is explicitly authorized.
- Identify ownership, backups, recovery confidence, maintenance constraints,
  observability, and affected users.
- Reproduce or isolate the failure where practical before changing live state.
- Prepare the exact mutation, expected impact, rollback, and post-change checks;
  stop at the approval gate.

## Business plans and strategy

- Translate aspirational outcomes into a measurable objective and timeframe.
- Identify customer, problem, offer, channel, capabilities, capital, capacity,
  constraints, and evidence of demand.
- Research the current market and alternatives without treating popularity as
  proof of fit.
- Separate assumptions from validated evidence and promises from forecasts.
- Prefer the smallest test that can invalidate the most important assumption.

## Marketing, content, and sales

- Identify audience, platform, objective, offer, voice, call to action, and
  available source material.
- Verify current platform rules or product details when they affect the work.
- Flag unsupported claims, guarantees, private information, and rights issues.
- Draft freely within the brief, but treat publication, direct messaging,
  advertising spend, and customer promises as separate actions.
- Define what performance signal would make the next iteration better.

## Purchases, vendors, and recommendations

- Identify budget, location, compatibility, must-haves, dealbreakers, and
  decision deadline.
- Verify current price, availability, terms, and specifications from primary
  sources when possible.
- Separate sponsored claims, reviewer opinion, and directly verified facts.
- Recommend one option and state the decisive tradeoff; do not manufacture
  certainty when availability or pricing could change.

## Data and analytics

- Establish the question, decision it supports, source ownership, grain,
  timeframe, definitions, and expected output.
- Check completeness, freshness, duplicates, missingness, units, filters, and
  reconciliation against a trusted total.
- Separate observed results from causal interpretations.
- Preserve raw inputs and make transformations reproducible.
- State uncertainty and limitations alongside the recommendation.

## Medical, legal, financial, and other high-stakes personal guidance

- Use current authoritative sources and identify jurisdiction or personal
  context when it materially affects the answer.
- Distinguish general information from individualized professional advice.
- Do not fabricate certainty, diagnoses, legal conclusions, expected returns,
  or guarantees.
- Recommend qualified professional help when the unresolved risk warrants it.
- Stop before executing transactions, filings, treatment decisions, or other
  consequential actions for the user.
