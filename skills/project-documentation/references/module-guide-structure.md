# Module guide structure and quality bar

Use one human-readable module guide for each large or independently
understandable module. Co-locate its design, current architecture, maintenance
map, and stable validation knowledge. Adapt headings to the project's language
and style, and omit sections that have nothing useful to say.

## 1. Module at a glance

Open with a short explanation of what the module is, what the user or player can
do because it exists, its main capabilities, and its current boundaries. A new
reader should understand the module before opening code.

## 2. Design

Describe confirmed user-visible flows, interactions, feedback, rules,
constraints, and important edge cases. Keep implementation identifiers out
unless they are also canonical product terms.

## 3. Architecture

Describe the current implementation only as deeply as maintainers need:

- public entry points and callers;
- modules, source files, classes, components, or assets, each with a one-sentence
  responsibility;
- runtime state and data ownership;
- lifecycle and important data flow;
- authority, validation gates, external integrations, and fallback behavior.

Prefer a compact flow or responsibility table when clearer than prose. If a
stable production unit cannot be described with one coherent responsibility,
document the current truth and flag a possible split instead of hiding several
unrelated jobs inside a long description.

Architecture is a section of the module guide, not a standalone project
document.

## 4. Maintenance map

Name exact change points and downstream readers. A compact table often works:

| Concern | Change here | Read or used by | Contract | How to verify |
| --- | --- | --- | --- | --- |
| Entry or UI | file, asset, and function | runtime owner | call and cleanup behavior | visible flow |
| Configuration | field or table | exact reader | units, defaults, valid range | configuration check |
| Asset or material | asset path, slot, parameter | assignment or override code | default and override rules | visual check |
| Persistence or network | schema or API | writer and reader | authority and isolation | integration check |

Include only applicable rows, but inspect code, assets, configuration, generated
bindings, and editor-owned state instead of documenting source files alone. Mark
an inaccessible binary detail as a known gap and give the shortest discovery
procedure; never guess.

## 5. Common change recipes

Document frequent maintenance tasks as short ordered recipes. Each recipe should
identify the first edit point, downstream readers, invariants that must remain
true, and the smallest reliable validation.

## 6. Stable validation

Record repeatable ways to verify the module: automated tests, build targets,
editor checks, or a concise manual scenario. Keep current pass/fail results,
commit status, release status, and remaining work in the tracker or configured
development record instead of the module guide.

## 7. Related material

Link the project overview, relevant ADRs, deeper authorities when the project
already has them, and active tracker work. Summarize only enough context to make
the links understandable; do not copy their content.
