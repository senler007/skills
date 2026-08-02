# Change-oriented Spec template

Write every section in the project's configured documentation language. Keep the
Spec sufficient for planning the change without reproducing complete durable
system documentation.

## Problem Statement

Describe the current user or maintainer problem and its concrete impact.

## Desired Outcome

Describe the observable result after the change succeeds. Link the project
overview when broader product context is useful.

## Design Changes

Describe the confirmed behavioral delta. Link each relevant authoritative design
document or glossary entry. Do not restate complete system rules.

## Scope

List what this Spec includes and explicitly excludes. Separate deferred follow-up
from required work.

## User Stories

Use numbered `As a …, I want …, so that …` stories when they clarify actors and
benefits. Prefer coverage over artificial length.

## Implementation Decisions

Record the change-specific implementation delta, delivery constraints, required
migrations, and links to affected responsibilities or contracts. Synchronize
stable module responsibilities, interfaces, data contracts, and consequential
rationale to their Architecture or ADR authority, then link them here. Avoid
fragile file paths, code listings, and choices the implementer may decide safely
later.

## Testing Decisions

Name the confirmed highest practical behavioral seam, observable cases, relevant
prior art, and why lower-level implementation assertions are unnecessary.

## Acceptance Criteria

Write objective, externally verifiable completion conditions. Include required
documentation synchronization and tracker relationships where applicable.

## Further Notes

Add only context that does not belong to an authority above, such as known risks
or links to prototypes. Omit this section when empty.
