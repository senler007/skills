---
name: project-documentation
description: Keep durable project documentation authoritative and maintain the configured daily development record. Use when confirmed feature decisions, terminology, architecture, ADRs, or tracker outcomes need routing or updating; when deciding where a rule belongs; when code and documentation appear inconsistent; or after a task actually changes code, docs, configuration, assets, Git/Editor state, or settles a durable decision.
---

# Project Documentation

Maintain human-readable project knowledge alongside the tracker workflow and one
concise daily record of completed changes. This skill may activate implicitly,
but durable authorities receive only confirmed decisions and settled outcomes.

## Load the project's map

Find the project-documentation configuration named by the repository's agent
instructions. It must map both authoritative document roles and the development
record path. If either configuration or the record path is missing, explain that
`$setup-senler-skills` should be run; do not silently impose default paths.

Read only the configuration and candidate authoritative documents needed for the
current fact. Follow their established path casing, language, terminology, and
style. Load [references/document-roles.md](references/document-roles.md) when the
target role or a boundary between roles is unclear.

Load [references/architecture.md](references/architecture.md) whenever creating,
restructuring, or materially updating an Architecture document. Do not impose
that contract on Design, ADR, Spec, or development-record documents.

## Decide whether the fact is durable

Write documentation only when the information is confirmed and will help a
future human understand the project after the current task closes. Typical
durable facts include accepted behavior, canonical terminology, stable code or
runtime responsibilities, and architectural decisions with meaningful tradeoffs.

Do not persist:

- tentative ideas or unresolved alternatives;
- ticket progress, test output, or short-lived implementation details in project docs;
- information already owned authoritatively elsewhere;
- a documentation change during a read-only request.

When confirmation is unclear, summarize the candidate fact and ask before
writing it.

## Route to one authority

Choose exactly one authoritative owner for each fact:

- project identity and navigation -> project overview;
- canonical term and short meaning -> glossary;
- confirmed player-visible behavior and rules for a large or distinct system -> design document;
- code/module/runtime responsibility -> architecture;
- hard-to-reverse or surprising decision with a real tradeoff -> ADR;
- goals, acceptance criteria, dependencies, status, and remaining delivery work -> tracker.

Link from consumers to the authority rather than copying the rule. A design
document may explain behavior while architecture explains how code realizes it;
neither should absorb the other's detail.

The development record is not another authority. It briefly reports completed
work and links to an authority when needed; it does not own product rules,
architecture, delivery scope, or progress state.

## Maintain design documents deliberately

Prefer a section in an existing design document for small, closely related
rules. Create a dedicated design document only for a large or independently
understandable system. A dedicated document should stay human-oriented and use
these conceptual sections when relevant:

1. **Overview** - purpose and player-facing mental model.
2. **Design** - interactions, flow, and important choices.
3. **Rules** - confirmed constraints and edge cases.
4. **Related Material** - links to tracker work, architecture, ADRs, or other authorities.

These are conceptual responsibilities, not a reason to add empty headings. Ask
for explicit confirmation before creating any new design document. Updating an
existing authoritative document after a decision has been confirmed needs no
second permission when the current task authorizes edits.

## Reconcile inconsistencies

When code and durable documentation differ:

1. Check the active Spec and tickets.
2. If they explicitly describe an in-progress transition, treat the discrepancy
   as expected and keep progress in the tracker.
3. Otherwise, surface the exact conflict. Ask which behavior is authoritative
   unless the current conversation has already confirmed it.
4. After authority is confirmed, update the authoritative document and the
   implementation only to the extent authorized by the current task. If fixing
   the implementation or creating tracker work needs additional authorization,
   ask for that action rather than re-asking the settled design question.

Never quietly rewrite documentation to match code, or code to match
documentation, when intent is unexplained.

## Maintain the daily development record

After a task actually changes code, documentation, configuration, assets,
Git/Editor state, or settles a durable decision, update the configured record
once before reporting completion. Never create or update it for a read-only task.

Use the configured language, path, and local date. Reuse the day's existing file
and append without overwriting earlier work. Preserve user-written goal text and
merge one conversation task into one concise actual-implementation section.
Follow an existing project template; when the day's file is absent, create only
the minimal date, goal, and actual-implementation structure required by that
project.

Record actual results, key configuration, and direct validation. Include a small
diagram only when architecture or data flow changed. Do not record plans,
brainstorming, guesses, per-message chronology, secrets, or tracker status that
already belongs in the configured tracker.

## Report the maintenance result

State which authority was updated, what confirmed knowledge it now owns, which
documents merely link to it, and which daily development record was updated. If
no write was appropriate, say why. Keep generated documentation in the project's
configured language even though this skill source is English.
