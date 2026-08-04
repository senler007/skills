# Authoritative document roles

Use this reference to resolve ownership. Existing files may have different names;
roles matter more than filenames.

| Role | Owns | Does not own |
| --- | --- | --- |
| Project overview | Project identity, audience, high-level capabilities, and navigation | Detailed module rules, code decomposition, or work status |
| Glossary | Canonical terms and terse meanings | Full rules or implementation notes |
| Module guide | Fast module orientation plus clearly labeled Design section, Architecture section, Maintenance Map, change recipes, and stable validation | Unrelated modules, tracker progress, current test results, or release status |
| ADRs | Accepted consequential decisions with context, alternatives, tradeoffs, and consequences | Routine choices, mutable rules, or implementation progress |
| Tracker work | Specs, Tickets, acceptance criteria, dependencies, current state, validation evidence, and remaining work | Long-term explanation of the finished module |
| Development record | Concise dated summaries of completed changes and direct validation | Product rules, architecture authority, plans, or tracker status |

## Boundary rules

- **One fact, one authority.** Consumers link to the owner.
- **Module front door.** A large or independently understandable module uses one
  discoverable guide for both reader orientation and maintainer navigation.
- **Design section versus Architecture section.** User-visible behavior and rules
  belong in Design; current code ownership, data flow, assets, configuration, and
  integration belong in Architecture. Both may live in the same module guide.
- **Target versus progress.** The module guide records confirmed target behavior
  and stable implementation facts; the tracker records what has shipped, passed,
  failed, or remains.
- **Current structure versus rationale.** The Architecture section describes the
  current responsibility; an ADR preserves why a consequential choice was made.
- **Small versus independent.** Keep tiny related rules together. A new module
  guide requires explicit human confirmation that the boundary deserves its own
  long-lived document.
- **Authority versus journal.** Durable documents and the tracker own project
  truth; the development record links to them rather than becoming another source.

## Conflict check

An active Spec or Ticket can temporarily explain why implementation and target
design differ. Without that explanation, treat disagreement among code, module
guides, glossary, ADRs, and tracker work as unresolved.
