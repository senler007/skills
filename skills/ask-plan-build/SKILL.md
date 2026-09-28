---
name: ask-plan-build
description: Ask one round of up to five questions, propose a solution, then implement after the user's response. Use when the user requests this ask-plan-build planning and implementation workflow.
---

## Ask

Read relevant task context without starting implementation. Ask up to five
task-specific questions together, numbered consecutively from 1, one distinct
question per number. Ask only what is needed; do not fill the quota. This is the
only interview round for the task.

Wait until the asked items are answered or the user explicitly delegates the
remaining choices. For partial answers, refer back only to the unanswered items;
do not introduce another question round.

## Propose

Synthesize the answers into your own recommended solution: intended behavior,
key choices, implementation steps, and verification. State assumptions for
delegated choices. Inspect the relevant implementation before proposing changes
so the user can review a concrete change list, not just broad goals such as
"refactor the weapon" or "adjust animations."

Include the following detail where it applies:

- **Files and assets:** List the specific paths to create, modify, move, rename,
  or delete. For each, explain what changes, why it is needed, and the resulting
  behavior. Related files may be grouped only if each path and its role remain
  clear. Include configuration, references, and documentation affected by the
  change, not only source code.
- **Implementation:** Identify the relevant classes, functions, components, or
  data fields and explain how their responsibilities or interactions change.
  Describe meaningful before/after behavior and the order of dependent steps.
- **Animations and other content:** Name the actual assets and paths involved,
  including assets whose use changes without editing the asset itself. For
  animation work, explain which motions change and how: reuse or replacement,
  playback triggers, sequencing, blending, timing, notifies, slots, or bindings,
  as relevant. Distinguish editing animation content from changing the code or
  Blueprint that plays it. For example, a weapon refactor should identify the
  affected equip, fire, or reload animations and their planned changes when
  those motions are in scope.
- **Verification:** Connect checks to the proposed behavior, including visible
  or interactive outcomes for animation and UI changes. Identify any required
  manual verification or unavailable validation.

Use enough detail for the user to understand what they are agreeing to without
reading the implementation. Scale the explanation to the task; do not add
unrelated changes or boilerplate categories. Do not invent asset names, paths,
or parameter values. Mark unresolved details explicitly, explain how they will
be determined, and distinguish confirmed targets from conditional changes.

Present the plan and wait for the user's response before implementing.

## Build

After the response, incorporate actionable corrections and implement the plan
without another confirmation. If the user instead rejects the plan, asks a
question or requests a rewritten proposal, or postpones implementation, address
that request and remain at the proposal stage until they respond again.

Complete the implementation and relevant validation, then report the result.
