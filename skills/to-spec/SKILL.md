---
name: to-spec
description: Synthesize completed discussion and repository context into a change-oriented Spec, confirm the highest practical behavioral testing seam, and publish through the configured tracker. Use when the user explicitly asks to turn an already-understood feature or design into a Spec or PRD.
---

# To Spec

Turn existing shared understanding into a publishable change record. Do not
restart the design interview or invent answers to unresolved product decisions.

## Load configuration and context

Locate `issue-tracker.md` and `project-docs.md` through the repository's agent
instructions. If configuration is missing, ask the user to run
`$setup-senler-skills`; do not guess publication or durable-document paths.

Read the completed conversation, relevant repository state, active durable design,
glossary, architecture, ADRs, and related tracker work. Use the project's
configured documentation language and canonical terms.

If a consequential product decision is unresolved, name it and stop. Recommend a
return to `$grill-with-docs` rather than conducting a new interview inside this
workflow.

## Keep the Spec change-oriented

Use [references/spec-template.md](references/spec-template.md). Explain the
problem, desired outcome, design changes, scope, implementation decisions,
testing decisions, and acceptance criteria needed to deliver this change.

Treat durable project documents as authorities:

- link complete system rules and canonical terminology instead of copying them;
- describe only the behavioral delta needed to understand this change;
- link architecture or ADRs when they constrain implementation;
- keep status and remaining work in the tracker, not in design documents.

When confirmed discussion has not yet reached an existing authoritative document,
use `$project-documentation` to synchronize it before publication. Creating a new
dedicated design document still requires user confirmation. Never publish an
unconfirmed idea as either durable design or a Spec decision.

## Confirm the testing seam

Identify the highest practical seam that observes external behavior and is stable
across implementation refactors. Prefer an existing seam and as few seams as
possible. Use repository prior art rather than proposing a new harness by default.

If the testing seam was not already confirmed in the discussion, present the
proposal, its observable behavior, and why it is the highest practical seam. Ask
one focused confirmation question and wait. This is the only required design
confirmation in this synthesis workflow; it does not reopen settled feature
decisions.

Record the confirmed seam and important behavioral cases under Testing Decisions.
Do not specify tests that assert prompt wording, private functions, or incidental
file layout when an equivalent public behavior can be observed.

## Publish through the configured tracker

Render the complete Spec in the configured project language, verify all required
sections and links, then publish according to `issue-tracker.md`:

- **GitHub:** create one Issue in the configured repository and apply the
  configured Spec/ready label. Preserve any configured parent relationship.
- **Local:** write the Spec to the configured feature Spec path; do not place it
  among durable project documentation.
- **Custom:** use the documented system, identifiers, relationship model, and
  state conventions without inventing unsupported fields.

Use the exact confirmed content for publication. Report the resulting Issue URL
or local/custom identifier and a short link summary. Stop after publishing: do
not invoke `$to-tickets`, create tickets, implement, review, or commit.
