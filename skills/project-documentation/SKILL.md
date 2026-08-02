---
name: project-documentation
description: Keep a project's durable human-readable documentation clear and authoritative. Use when confirmed feature decisions, terminology, architecture, ADRs, or tracker outcomes need routing or updating; when deciding where a rule belongs; or when code and documentation appear inconsistent.
---

# Project Documentation

Maintain human-readable project knowledge alongside the tracker workflow. This
skill may activate implicitly, but it writes only confirmed decisions and settled
outcomes—not brainstorming, temporary implementation state, or guesses.

## Load the project's map

Find the project-documentation configuration named by the repository's agent
instructions. If it is missing, explain that `$setup-senler-skills` should be run;
do not silently impose this skill's default paths.

Read only the configuration and candidate authoritative documents needed for the
current fact. Follow their established path casing, language, terminology, and
style. Load [references/document-roles.md](references/document-roles.md) when the
target role or a boundary between roles is unclear.

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

- project identity and navigation → project overview;
- canonical term and short meaning → glossary;
- confirmed player-visible behavior and rules for a large or distinct system → design document;
- code/module/runtime responsibility → architecture;
- hard-to-reverse or surprising decision with a real tradeoff → ADR;
- goals, acceptance criteria, dependencies, status, and remaining delivery work → tracker.

Link from consumers to the authority rather than copying the rule. A design
document may explain behavior while architecture explains how code realizes it;
neither should absorb the other's detail.

## Maintain design documents deliberately

Prefer a section in an existing design document for small, closely related
rules. Create a dedicated design document only for a large or independently
understandable system. A dedicated document should stay human-oriented and use
these conceptual sections when relevant:

1. **Overview** — purpose and player-facing mental model.
2. **Design** — interactions, flow, and important choices.
3. **Rules** — confirmed constraints and edge cases.
4. **Related Material** — links to tracker work, architecture, ADRs, or other authorities.

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

## Report the maintenance result

State which authority was updated, what confirmed knowledge it now owns, and
which documents merely link to it. If no write was appropriate, say why. Keep
generated documentation in the project's configured language even though this
skill source is English.
