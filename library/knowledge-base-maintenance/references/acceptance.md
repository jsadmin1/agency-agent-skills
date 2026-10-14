# Acceptance and coverage

Use the project's actual contracts. These checks supplement them; they do not impose one universal knowledge taxonomy or authorize publication.

## Keep distinct denominators

Track reader documents, templates, managed skill files, and other relevant assets separately. A directory listing can include all of them while the content auditor intentionally excludes templates. Reconcile the difference before making claims.

For each reader document record its path, content fingerprint, full-read status, evidence status, findings, disposition, destination links, and verification state. A changed source revision invalidates the old review until the change is inspected. New deliverables join the final inventory. Retained historical evidence can be fully reviewed without being independently corroborated.

A disposition must explain the work: an existing canonical concept was extended; a historical record was retained; a useful source supplied a new lesson; a proposal remains untested; an empty capture contains no recoverable evidence. A label such as 'reviewed' alone is insufficient.

## Validator evidence

Record validator name, selected checks, scope, input count, errors/warnings, omissions, degradation, suppression, and timestamp. Missing families were not checked. A selected family can still be degraded. Empty results can mean zero inputs, disabled checks, omitted findings, or deferred execution.

In OpenKnowledge, inspect `ran`, `fileCount`, `warnings`, omission counters, `brokenLinkSuppression`, and write-time `link-check-deferred`. Use the current tool contract when fields differ. `audit` validates links; graph tools help inspect relationships. Template orphans and reserved-log historical links require classification, not artificial repair. Heading fragments may require a separate check.

Do not assume a command's exit code proves that its intended input was processed. When building a checker, use known-good and known-bad fixtures, including zero inputs, missing target, wrong fragment, and partial output. Test behavior, not whether source code contains desired words.

## Evidence and promotion

Separate evidence classes: observed incident, user decision, independently verified artifact, current primary documentation, agent inference, and proposal. A current source must support the exact material claim, not merely share its topic. Record version/date and execution boundary.

When a historical source overclaims, preserve it and add the correction to derived guidance with clear attribution. Do not treat editing the source as independent verification. An unavailable source is a named limitation; a filename alone cannot reconstruct missing knowledge.

For exports, traverse references across the release boundary. Either include supporting sources permitted for the audience or replace private dependencies with suitable self-contained, sourced material. Checking only that files exist in the authoring KB does not prove the exported bundle is usable.

## Final gate

- All in-scope items have complete reads and meaningful dispositions; count every justified exclusion.
- All supported refinements are implemented, with source and destination mappings.
- Current reader navigation, internal paths, relevant fragments, attachments, and source references work.
- Applicable validators completed on the reconciled corpus without unexplained warnings or omissions.
- Contradictions and unsupported current claims are corrected or visibly qualified.
- Comments and conflicts are resolved substantively or reported as blockers.
- Changed complex content was checked in the intended renderer.
- Originals, unrelated changes, and immutable evidence remain recoverable.
- Any authorized remote delivery is proven by fresh destination and revision readback.

State residual limits precisely. 'No actionable defects in the reviewed scope' can be justified; 'all knowledge is correct forever' cannot. Do not silently redefine incomplete required work as an exception.
