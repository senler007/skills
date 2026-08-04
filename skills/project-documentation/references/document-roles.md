# Authoritative document roles

Use this reference to resolve boundaries. A project's configured existing files
may have different names; roles matter more than filenames.

| Role | Owns | Does not own |
| --- | --- | --- |
| Project overview | What the project is, its audience, high-level capabilities, and navigation to deeper authorities | Detailed rules, code decomposition, or work status |
| Glossary | Canonical terms and terse meanings needed for consistent discussion | Full rule explanations or implementation notes |
| Design systems | Confirmed user/player-visible behavior, flows, rules, constraints, and edge cases for large or distinct systems | Class ownership, delivery progress, or every small related rule as a separate file |
| Architecture | Code/module boundaries, runtime responsibilities, important data flow, and integration seams | Product intent, tracker status, or historical rationale better recorded in an ADR |
| ADRs | Accepted, hard-to-reverse or surprising decisions with context, alternatives, tradeoffs, and consequences | Routine choices, mutable rules, or implementation progress |
| Tracker work | Specs, tickets, acceptance criteria, dependencies, current status, and remaining work | Long-term explanation of the finished product |
| Development record | Concise completed-change summaries, key configuration, and direct validation for each modifying task | Product rules, architecture authority, plans, brainstorming, or tracker status |

## Boundary rules

- **One fact, one authority.** Consumers link to the owner and add only the
  context needed to understand the link.
- **Behavior versus implementation.** A control scheme's player-visible mapping
  and interaction rules belong in design; the input subsystem and binding flow
  belong in architecture.
- **Term versus rule.** The glossary defines a term briefly; a design document
  owns the rules that use it.
- **Target versus progress.** Design records confirmed target behavior; the
  tracker records what is not yet delivered.
- **Current structure versus rationale.** Architecture describes the resulting
  responsibility; an ADR preserves why a consequential choice was made.
- **Small versus independent.** Keep ordinary related rules together. Split out a
  design document only when the system is large or useful to understand on its own.
- **Authority versus journal.** Durable documents and the tracker own project
  truth; the development record is a dated journal that links to them rather than
  becoming another source of truth.

## Conflict check

An active Spec or ticket can temporarily explain why code and the target design
differ. Without that explanation, treat disagreement among code, design,
architecture, and glossary as an unresolved conflict—not permission to choose a
winner silently.
