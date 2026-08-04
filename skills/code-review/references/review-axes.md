# Review axes

## Standards

Check every documented repository rule. Also name, rather than vaguely imply,
applicable Fowler-style smells: Mysterious Name, Duplicated Code, Feature Envy,
Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent
Change, Speculative Generality, Message Chains, Middle Man, and Refused Bequest.
Smells are judgement calls; repository rules override them.

## Spec

Check requirements that are missing or partial, behavior outside requested scope,
and implementation that claims a requirement but behaves incorrectly. Quote or
link the originating criterion for every finding. Do not treat a desirable idea
as required when the Spec does not ask for it.

## Documentation

Load `$project-documentation` and its document-role reference as the authority for
ownership boundaries. Do not duplicate or reinterpret those rules here. Then
check all of the following against the diff and configured candidate documents:

- one authoritative owner per durable fact;
- missing updates to confirmed module-guide Design or Architecture sections,
  glossary, or ADRs;
- accidental duplication of durable rules across documents or tracker work;
- synchronization after changed terms, behavior, responsibilities, or rationale;
- unapproved or unnecessary new module guides;
- explained code/design gaps against active Specs and Tickets;
- broken links or relationships among durable authorities, Specs, and Tickets;
- configured language and path casing.

An implementation gap explicitly planned by active work is not stale design.
An unexplained conflict must be surfaced rather than resolved by assumption.

## Finding shape

For each finding report axis, severity, blocking or judgement-call classification,
file and tight line range, evidence, authority, impact, and concise remediation.
Report `PASS` when an axis has no actionable findings. Report `not reviewable`
instead when required authority is unavailable.
