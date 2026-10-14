---
name: knowledge-base-maintenance
description: Use when asked to assess or restore an entire knowledge base,
  process a capture backlog, refine notes into lessons or workflows, repair wiki
  integrity, or run recurring KB maintenance. Supports read-only assessment,
  full restoration, and incremental maintenance. Discover the project's own
  governance and evidence rules; ordinary single-page edits do not require a
  corpus-wide pass.
---
# Knowledge-base maintenance

Restore useful, traceable knowledge without erasing its evidence. A clean linter result is one gate, not proof that the corpus is complete or correct.

## Establish the commission

Identify the exact knowledge root and requested mode: read-only assessment, full restoration, or incremental maintenance. Separate content repair, skill installation, publication, Git operations, and external communications; permission for one does not imply the others. Respect an active planning-only instruction.

Read project governance, local agent instructions, templates, current tracking, and live Git/runtime state. Preserve unrelated changes. Identify the writer before changing shared documents. Do not launch agents or contact peers without authorization.

For OpenKnowledge, load its current project-local runtime skill and discover the MCP tools. Route in-scope Markdown and managed skills through the prescribed tools; use current schemas, not remembered tool shapes. If another KB system owns writes, honor that system instead. Never treat unavailable tooling as a reason to bypass a collaborative or conflict boundary.

## Select the mode

- **Assessment:** inventory, read, diagnose, and report. Persist reports only if authorized; do not fix content or configuration.
- **Full restoration:** review every in-scope reader document plus governing templates and configuration, then repair and refine the corpus.
- **Incremental maintenance:** review changed/new captures and the source, destination, and navigation relationships affected by them. Report that bounded denominator; do not call it a full review.

## Preserve and establish coverage

Use the project's supported preservation checkpoint before substantial changes. Inventory every directory and classify reader content, templates, managed skills, configuration, generated files, ignored material, and runtime state. Do not read secrets or runtime databases to satisfy a generic completeness slogan.

Record the inventory revision and a per-document ledger: path, reviewed content fingerprint, full-read status, role/topic, evidence status, findings, disposition, canonical destinations, and remaining checks. Read each in-scope document completely. Recover capped output in bounded chunks. Reconcile line and UTF-8 byte coverage against the same source revision, including overlaps and a final partial chunk. Check truncation in both the source tool and the orchestration output. Listings, retrieval summaries, and tool metadata do not count as body reads.

Keep machine receipts compact and inspectable. Bound command arguments and transport payloads as well as visible output; send large captured bodies through chunked data or stdin instead of one oversized shell argument. Store structured results, but emit only needed fields; enriched inventory responses can duplicate large metadata blocks. Count enumerated inputs and reconcile them against validator scope. An empty check without a known denominator is not a pass.

Persist findings and completed units after each coherent batch. Follow the host/project continuity protocol before context loss. Resume from the ledger and current revisions, not a summary alone.

## Refine by evidence and concept

Preserve raw captures and immutable sources. Normalize metadata and repair references without silently rewriting the historical account. Use separate, linked derived documents for corrections, synthesis, and generalization.

Classify every item: retain, repair, consolidate, derive, deprecate, or defer with a concrete reason. Full coverage does not mean forcing every note into a best practice.

- A **lesson** explains an observed failure or discovery, the prior belief, consequence, correction, and prevention.
- A **workflow** states prerequisites, reproducible steps, expected results, verification, failure handling, and safe stops.
- A **best practice** generalizes supported evidence while stating where it applies and what it does not establish.
- An **idea** remains a proposal until evidence supports stronger status.

Consolidate by concept, not one new article per source. Extend appropriate canonical documents and retain source-to-destination mappings. Do not smooth away disagreements: compare source authority, dates, and scope; resolve with evidence or record the unresolved conflict.

Separate full reading, current claim verification, command execution, and live delivery. Verify actionable changing guidance against current primary sources or safe local evidence. Dated incident accounts remain dated. Do not claim that matching a current doc proves the historical event or another host's runtime. Ingest evidence according to local rules and applicable rights; label excerpts and inaccessible sources honestly.

## Repair structure and relationships

Use local folder templates and schemas. Remove unfilled scaffolding from reader content without inventing the missing capture. Update existing navigation and source links when content changes. Keep knowledge reachable from the root through useful paths; do not manufacture irrelevant links to internal templates.

Validate link destinations, case, relative depth, heading fragments, source references, and attachments. Check fragments separately if the built-in auditor only checks the path. Replace legacy syntax only where project rules require it. Re-read a document before a targeted edit and heed conflict or divergence responses. Bind edits to a unique record and its context, not a repeated generic sentence. After a failed multi-file operation, inspect actual target state before retrying; neither rollback nor partial success can be assumed.

When changing templates, preserve both their menu metadata and the child-document defaults. Verify required defaults and reusable body structure after the owning tool writes. A successful response is not proof that the intended metadata layer was preserved.

Preserve append-only historical logs and immutable evidence. Disclose legitimate historical exceptions separately. Never disable a checker, weaken a schema, create empty target pages, or hide files merely to make the dashboard green.

## Verify and deliver

Read `references/acceptance.md` before final verification. Read `references/worked-cases.md` when applying the promotion rules or evaluating this skill.

Run the applicable validators against the intended scope. Inspect selected families, degradation, deferred checks, suppressions, omitted findings, and the input count. Narrow capped findings until every actionable issue is accounted for. Verify changed complex content in rendered form using the supported surface.

Reconcile new/changed documents and re-review changed revisions before closing the ledger. Resolve comments substantively and respect conflicts requiring a human; never dismiss them to clear a counter.

When authorized to deliver through Git, inspect exact scoped diffs, preserve unrelated work, verify destination/privacy, and verify the remote revision. Reconcile intended untracked or ignored attachments and receipts separately; matching committed heads cannot prove that files outside the commit were delivered. Autosave, a shadow checkpoint, and a cached tracking branch are different evidence from live remote readback. Do not force-push or rewrite history as cleanup.

Report coverage, completed refinements, validation scope, exceptions, source-preservation evidence, and actual delivery state. If a required gate remains blocked, identify it and finish independent work; do not label the entire goal complete. Do not promise continued unattended execution beyond the runtime's capabilities.
