---
name: code-review
description: "Perform a read-only review of a change across three independent axes: repository Standards, originating Spec fidelity, and Documentation integrity. Use when the user asks to review a branch, diff, pull request, implementation, or changes since a fixed point."
---

# Code Review

Review without modifying code, documentation, tracker work, Git state, or external
systems. Findings are the output; fixes require a separate authorized workflow.

## Pin the review range

Obtain the fixed comparison point from the user or invoking workflow. Resolve it
before review and fail early if it is invalid. Capture one exact diff command and
commit list for every reviewer. Use merge-base comparison for committed branch
work; include staged and working-tree changes when the requested review covers
uncommitted implementation.

Verify the diff is non-empty. State the fixed point, compared tip or working tree,
diff command, and commit list in the final report.

## Gather authority

Identify the originating Spec or Ticket from the user's reference, commit
messages, configured tracker, or matching repository document. If none exists,
ask whether the Spec axis should be skipped.

Locate documented repository standards and the configured project-documentation
map. If that map is missing, explain that `$setup-senler-skills` is required and
report the Documentation axis as not reviewable; do not impose default paths.

For the Documentation axis, load `$project-documentation`, its authoritative
document-role reference, and the configured candidate documents affected by the
diff. Read [references/review-axes.md](references/review-axes.md) for review-specific
checks and the smell baseline. Repository standards override judgement-call
smell advice.

## Run three independent reviews

Launch three fresh review contexts in parallel when subagents are available. Give
each the same diff and commit list but only the authority needed for its axis:

1. **Standards** - documented repository rules plus the named smell baseline.
2. **Spec** - missing or partial requirements, scope creep, and incorrect behavior
   against the originating work item.
3. **Documentation** - authoritative ownership, synchronization, granularity,
   relationships, and explained code/design gaps.

Do not let one reviewer see or rerank another reviewer's conclusions. Require
each finding to include severity, exact file/hunk, evidence, violated authority,
and a concise remediation direction. Skip issues that automated tooling already
reports more precisely.

## Classify without fixing

Classify clear documented-standard violations, clear Spec failures, and clear
missing or incorrect documentation updates as **blocking**. Classify smells,
optional refactors, debatable wording, design changes, and scope-expanding ideas
as **judgement calls** unless a documented authority makes them mandatory.

Standalone `$code-review` is always read-only, including for obvious blockers.
Do not apply patches, update Issues, stage files, commit, or launch an
implementation workflow.

## Report axes separately

Present `Standards`, `Spec`, and `Documentation` as separate sections. Preserve
severity within each axis and do not collapse them into one overall score. End
with finding counts, the worst finding per axis, and a clear list of blocking
items versus judgement calls.
