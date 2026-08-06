# GitHub issue tracker configuration

Use this seed for the repository's agent-facing `issue-tracker.md`. Replace every
placeholder with the confirmed repository value and omit unused guidance.

```markdown
# Issue tracker

- Mode: GitHub
- Repository: `{owner}/{repository}`
- Specs: GitHub issues labeled `{spec label, if used}`
- Tickets: GitHub issues attached to their parent Spec as sub-issues
- Ready state: `{label or project status, if used}`
- Done state: closed issue

Use the repository above for Spec, ticket, and progress state. Read the parent
Spec and the selected ticket before implementation. Preserve native sub-issue
relationships. Explicit invocation of a publishing workflow such as `$to-spec`
or `$to-tickets` authorizes the writes that workflow describes. Do not ask for a
second publication confirmation after the workflow's own required approval. For
GitHub publication, create Issues directly; do not write temporary tracker files
inside the repository.
```
