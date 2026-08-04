# Architecture content contract

Treat Architecture as a human-readable **code atlas**. It describes the current,
stable production structure so a person or AI can understand the system, locate
the right implementation unit, follow important runtime paths, and avoid crossing
ownership or dependency boundaries.

Architecture answers four questions:

1. **Where?** Where does a responsibility live?
2. **What?** What is each production unit's single core responsibility?
3. **How does it flow?** How do important intents, commands, events, and state move?
4. **Who owns what?** Who owns state, which entry points are public, and which
   dependency directions are allowed or forbidden?

Do not add a mandatory document-boundary section. Make the content itself clear
enough that readers can identify its purpose and navigate it immediately.

## Contents

- [Required reading order](#required-reading-order)
- [One-minute module map](#1-one-minute-module-map)
- [Key data flows](#2-key-data-flows)
- [Production Unit Index](#3-production-unit-index)
- [Complex-module Deep Dives](#4-complex-module-deep-dives)
- [Keep other concerns in their authorities](#keep-other-concerns-in-their-authorities)
- [Maintain the atlas with the code](#maintain-the-atlas-with-the-code)

## Required reading order

Keep these four layers in this order:

1. **One-minute module map**
2. **Key data flows**
3. **Production Unit Index**
4. **Complex-module Deep Dives**

Use only the layers the project actually needs, but never put detailed units
before the module map or key flows needed to understand them.

## 1. One-minute module map

Usually show 5-12 real, stable production boundaries that a reader can locate in
the repository. Use fewer in a small system and never invent modules to reach a
quota. Prefer actual packages, source directories, runtime modules, feature
folders, subsystems, plugins, or equivalent ownership boundaries over conceptual
layers that exist only in prose.

Use a compact table:

| Module | One-sentence responsibility | Public entry point | Code location |
| --- | --- | --- | --- |
| `<stable name>` | `<single core responsibility>` | `<supported caller-facing seam>` | `<exact path>` |

Every module must have a stable name, one core responsibility, a supported entry
point, and an exact code location. If a proposed module has none of these, treat
it as a concept or flow rather than inventing a module boundary.

Add one small dependency diagram only when the table cannot show the permitted
direction clearly. Use exact module names and label important relationships.

## 2. Key data flows

Document only flows that cross production boundaries, establish state ownership,
or are easy to implement incorrectly. Do not transcribe ordinary calls.

Use this skeleton:

```text
Trigger
-> public entry point
-> authoritative handler and state owner
-> result consumers
```

For each flow:

- use exact names from the Production Unit Index;
- label arrows as intent, command, event, or state;
- identify the step that mutates authoritative state;
- keep the normal path to roughly 5-9 nodes and split longer flows;
- prefer compact text or a small Mermaid diagram over detailed UML;
- omit methods and line-by-line implementation details.

## 3. Production Unit Index

Index every stable production unit needed to locate and safely change the system.
Group entries by their real repository paths. Depending on the project, units can
include classes, modules, subsystems, components, behavior-bearing Blueprints or
assets, services, packages, plugins, or Verse devices.

Treat a paired header and implementation file as one unit. Include exact names
and paths so both humans and tools can search for them. Exclude tests, generated
output, build output, temporary code, experiments, and passive content assets
that carry no architectural responsibility.

Give every unit exactly one sentence describing its single core responsibility.
Do not list methods, members, implementation steps, or speculative future work.
If the responsibility cannot be stated without joining unrelated jobs, first
consider splitting the production unit instead of lengthening its description.

The index is complete for stable production units but shallow by design. Link a
unit to a Deep Dive only when its behavior meets the criteria below.

## 4. Complex-module Deep Dives

Create a Deep Dive because a unit is difficult or risky to understand, not merely
because it is important or large. A Deep Dive is justified when at least one is
true:

- it owns a complex lifecycle or state machine;
- it involves networking, concurrency, asynchronous work, or prediction;
- it coordinates several production modules;
- its state ownership or dependency direction is non-obvious;
- it protects important invariants;
- its failure, interruption, recovery, or destruction behavior is complex;
- humans or AI have repeatedly misunderstood or modified it across a boundary.

Use only the relevant parts of this structure and omit empty headings:

```markdown
### <Production unit>

**One-sentence mental model**
<What role does this unit play in the system?>

**Public entry points**
<How should other units interact with it?>

**State ownership**
<What does it own, and what explicitly belongs elsewhere?>

**Collaboration and dependencies**
<Who calls it, what it calls, and which reverse dependencies are forbidden?>

**Key flows and invariants**
<What is easy to misunderstand, and what must remain true?>

**Failure and recovery**
<How do failure, timeout, interruption, disconnect, or destruction finish safely?>
```

Link to Design and ADR authorities rather than repeating their explanations. The
implementation remains the authority for ordinary methods and low-level detail.

## Keep other concerns in their authorities

Architecture describes current stable implementation structure and runtime
collaboration. Route other information elsewhere:

- product behavior and rules -> Design;
- reasons and meaningful tradeoffs -> ADR;
- a proposed change and its acceptance criteria -> Spec;
- delivery dependencies and current work -> Tickets or tracker;
- tests, validation evidence, and completed-task summaries -> development record
  or the repository's verification surfaces.

Do not keep implementation order, task status, exhaustive test lists, temporary
migration state, or copied product rules in Architecture.

## Maintain the atlas with the code

Update Architecture in the same task when a stable production unit is added,
removed, moved, renamed, split, or given a different responsibility; when a
public entry point or dependency direction changes; or when a key flow gains a
different state owner.

Prefer discovering names and paths from repository tooling rather than memory.
Keep prose human-reviewed: generated inventories can find drift, but they do not
decide responsibilities, ownership, or permitted dependencies.
