# Lightweight change Spec template

Write every section in the project's configured documentation language. Keep the
Spec sufficient to build the change without copying the project's complete
long-lived design.

## Goal

State the current problem and the observable result this change should produce.
Explain the impact in enough detail for a reader to understand why the work
exists.

## Change

Describe the confirmed behavioral and maintenance delta. Link authoritative
module guides, glossary entries, or ADRs instead of reproducing them.

Optional detail such as user stories, implementation constraints, migrations,
risks, or consequential decisions belongs here only when it removes real
ambiguity. Leave safe implementation choices to the implementer.

## Scope

List what is included and explicitly excluded. Separate required work from
deferred follow-up. Keep the boundary small enough to review as one change.

## Acceptance & Testing

Write objective completion criteria. Name the confirmed highest practical
behavioral testing seam, observable cases, relevant prior art, and required
documentation synchronization. Prefer public behavior over private functions,
prompt wording, or incidental file layout.
