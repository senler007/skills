# Senler Skills

A Codex-first collection of reusable development workflow skills. The workflow
keeps tracker artifacts for delivery and project documents for durable product
knowledge, so a finished feature remains understandable after its ticket closes.

The repository currently contains:

- `setup-senler-skills` configures tracker and documentation locations for a repository.
- `project-documentation` routes confirmed decisions to one authoritative project document.
- `grilling` resolves one user decision at a time before action.
- `grill-with-docs` combines grilling with durable project-documentation synchronization.

Install any skill with a standard Codex-compatible skill installer by pointing
it at this GitHub repository and the corresponding directory under `skills/`.

Skill source is written in English. Generated project documentation follows the
configured project's language and preserves its existing paths and naming.

## Attribution

This is an independent, one-time derivative of the AI Hero skills workflow by
Matt Pocock. It is not automatically synchronized with that project. See
[`LICENSE`](LICENSE) for MIT licensing and attribution.

| Skill | Origin |
| --- | --- |
| `setup-senler-skills` | Original for this collection |
| `project-documentation` | Original for this collection |
| `grilling` | Derived from the AI Hero workflow |
| `grill-with-docs` | Substantially rewritten from the AI Hero workflow |
