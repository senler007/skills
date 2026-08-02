---
name: implement
description: Implement exactly the user-supplied Spec, Ticket set, or single Ticket; use TDD at confirmed seams, synchronize durable documentation, remediate clear three-axis review blockers, validate, and commit. Use only when the user explicitly asks to implement scoped work.
---

# Implement

Complete the requested scope without silently adding adjacent work.

## Resolve exact scope

Read the configured tracker and project-documentation map, then resolve the input:

- **Spec** - implement its associated approved Ticket work, respecting dependencies.
- **Ticket set** - implement exactly that set in dependency order.
- **single Ticket** - implement only that Ticket and its stated acceptance criteria.

Read full bodies, relationships, linked authorities, and relevant repository rules.
Do not pull in a blocker that is not complete; report the blocked frontier instead.
Record the pre-implementation Git fixed point for later review and preserve
unrelated user changes in the working tree.

## Agree tests and implement

Use `$tdd` where behavior warrants automated coverage. Reuse the testing seam
confirmed by the Spec; if absent, propose the highest practical stable seam and
wait for confirmation. Documentation-only or purely mechanical work need not
invent a behavioral test, but still needs proportionate validation.

Work in narrow vertical slices. Run the focused test or check during each slice,
nearby checks regularly, and the repository's required broader verification once
the requested scope is complete. Stop on unexplained failures rather than hiding
or weakening them.

## Synchronize durable outcomes

Use `$project-documentation` for confirmed implementation outcomes that affect
target design, canonical terms, module/runtime responsibilities, or an accepted
architectural decision. Update or create exactly one authoritative owner as
directed by `$project-documentation`, then link from consumers; do not duplicate
facts or turn progress into durable design. Creating a new dedicated design
document still requires user confirmation.

An implementation that intentionally has not reached confirmed target design
remains tracker progress. Surface any unexplained code/document conflict.

## Review and remediate blockers

Invoke `$code-review` against the recorded fixed point after implementation. Keep
Standards, Spec, and Documentation findings separate.

Fix clear blocking findings within the authorized scope, rerun affected focused
checks, and repeat the relevant review axis until blockers are resolved. Report,
rather than automatically apply, judgement-call refactors, scope expansion,
optional improvements, and design changes. Ask for authority when a blocker can
only be resolved by changing confirmed design or expanding scope.

## Validate and commit

Run required broad verification and confirm the diff contains only intended work.
Create a commit only when:

- requested acceptance criteria are met;
- required tests and validation pass;
- affected durable authorities are synchronized;
- no clear in-scope review blocker remains.

Use an intentional message referencing the work item. Report commit identifiers,
validation, documentation updates, resolved blockers, and remaining judgement
calls. Do not push, close tracker work, or start another workflow unless the user
also authorizes it.
