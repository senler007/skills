English | [简体中文](README.zh-CN.md)

# Senler Skills

A focused Codex-first workflow for turning design discussion into reviewed,
documented, and committed implementation. Tracker artifacts own delivery work;
human-readable project documents preserve durable product knowledge.

The first release contains exactly nine Skills.

| Explicit workflow | Purpose |
| --- | --- |
| `setup-senler-skills` | Configure tracker, documentation paths, language, and agent guidance |
| `grill-with-docs` | Resolve one design decision at a time and synchronize confirmed design |
| `to-spec` | Publish completed discussion as a change-oriented Spec |
| `to-tickets` | Publish approved tracer-bullet Tickets with genuine dependencies |
| `implement` | Implement the requested scope, review blockers, validate, and commit |

| Supporting discipline | Purpose |
| --- | --- |
| `grilling` | Keep interviews to one recommended decision question at a time |
| `project-documentation` | Route each durable fact to one authoritative owner |
| `tdd` | Test external behavior through confirmed stable seams |
| `code-review` | Review Standards, Spec, and Documentation independently |

## Installation

Use Codex's standard `$skill-installer` with the public repository:

https://github.com/senler007/skills

For example, to install `to-spec`, ask Codex:

```text
Use $skill-installer to install the to-spec Skill from https://github.com/senler007/skills/tree/main/skills/to-spec.
```

To install the complete collection, ask:

```text
Use $skill-installer to install all nine Skills from https://github.com/senler007/skills.
```

The standard installer accepts each directory under `skills/` as an individual
package. Restart or begin a new Codex turn after installation so newly installed
Skills are discovered.

## Workflow

The normal five-stage flow is:

1. **Setup once** - invoke `setup-senler-skills` to record the project's real tracker and document map.
2. **Grill** - invoke `grill-with-docs` until shared understanding and durable design agree.
3. **Specify** - invoke `to-spec` to publish the approved change and testing seam.
4. **Plan Tickets** - invoke `to-tickets` and approve vertical slices and dependency edges.
5. **Implement** - invoke `implement` for a Spec, Ticket set, or single Ticket; it uses TDD, documentation synchronization, and three-axis review before committing.

Each explicit workflow stops after its own output. The user starts the next stage;
no workflow silently advances into another.

## Documentation authority

The collection gives every durable fact one authoritative owner and keeps
long-lived project knowledge separate from tracker progress. See the
[`project-documentation` role reference](skills/project-documentation/references/document-roles.md)
for the authoritative boundaries among project overview, glossary, design,
architecture, ADRs, and tracker work. Other documents link to those authorities
instead of maintaining copies of their rules.

## Codex support

Codex is the first supported and forward-tested environment. Skill instructions
and bundled references are maintained in English. Generated or updated project
documentation follows the configured project's existing language, paths, casing,
and terminology.

The Skills remain portable where practical, but this release does not claim full
compatibility with every Skill-capable tool.

## Attribution

This is an independent, one-time derivative of the AI Hero skills workflow by
Matt Pocock. It has no automatic upstream synchronization; later upstream changes
are adopted manually and intentionally. See [`LICENSE`](LICENSE) for MIT licensing.

| Skill | Origin |
| --- | --- |
| `setup-senler-skills` | Original for this collection |
| `project-documentation` | Original for this collection |
| `grilling` | Derived from the AI Hero workflow |
| `grill-with-docs` | Substantially rewritten from the AI Hero workflow |
| `to-spec` | Substantially rewritten from the AI Hero workflow |
| `to-tickets` | Derived from the AI Hero workflow |
| `code-review` | Substantially rewritten from the AI Hero workflow |
| `tdd` | Derived from the AI Hero workflow |
| `implement` | Substantially rewritten from the AI Hero workflow |
