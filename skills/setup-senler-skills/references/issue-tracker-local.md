# Local issue tracker configuration

Use this seed for projects that do not use an external tracker. Replace every
placeholder with the confirmed repository value.

```markdown
# Issue tracker

- Mode: local
- Feature root: `.scratch/<feature>/`
- Spec: `.scratch/<feature>/spec.md`
- Tickets: `.scratch/<feature>/tickets/<ticket>.md`

Keep one ticket per file. Each ticket records its parent Spec, status,
dependencies, scope, and acceptance criteria. Treat `.scratch/` as workflow
state, not durable project documentation. Do not move confirmed design knowledge
there; route it through `$project-documentation`.
```
