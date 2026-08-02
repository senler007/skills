# Custom issue tracker configuration

Use this seed when the project has a tracker other than GitHub or local files.
Describe its actual tools and identifiers in plain language; do not invent a
schema the tracker does not support.

```markdown
# Issue tracker

- Mode: custom
- System: `{name}`
- Project or workspace: `{identifier}`
- Spec location: `{how to find a Spec}`
- Ticket location: `{how to find a ticket}`
- Parent/child relationship: `{supported representation}`
- Ready state: `{state}`
- Done state: `{state}`

Use `{tool or access method}` for tracker reads and authorized writes. Before
implementation, read `{required context}`. Follow `{repository-specific rules}`.
```
