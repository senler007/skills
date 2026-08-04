# Project documentation configuration

Use this seed for the repository's agent-facing `project-docs.md`. It is a path
map and consumer contract, not a second copy of project knowledge. Replace every
placeholder and omit roles the project intentionally does not maintain.

```markdown
# Project documentation

- Language: `{project documentation language}`
- Project overview: `{existing or proposed path}`
- Glossary: `{existing or proposed path}`
- Design directory: `{existing or proposed path}`
- Architecture: `{existing or proposed path}`
- ADR directory: `{existing or proposed path}`
- Development records: `{existing or proposed YYYY-MM-DD path}`
- Tracker configuration: `{path to issue-tracker.md}`

Use `$project-documentation` to route confirmed durable knowledge. Preserve these
paths and their existing casing. One fact has one authoritative owner; other
documents link to it instead of restating it. Update an existing authority only
after the decision is confirmed. Ask before creating a new design document, and
never create empty documents as placeholders. After a task actually changes the
project, use `$project-documentation` to update the configured daily development
record once; read-only tasks do not create a record.
```
