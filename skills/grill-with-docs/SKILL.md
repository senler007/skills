---
name: grill-with-docs
description: Run a focused one-question-at-a-time design interview while synchronizing confirmed target design into configured human-readable project documentation. Use when the user explicitly asks to grill a feature, system, lifecycle, or design with project docs before specification or implementation.
---

# Grill with Docs

Combine `$grilling` with `$project-documentation`. Reach shared understanding
while leaving confirmed durable design in its authoritative human-readable home.
This is an explicit workflow: do not start it only because ordinary discussion
touches project documentation.

## Prepare the session

Locate the project-documentation configuration named by the repository's agent
instructions. If it is missing, explain that `$setup-senler-skills` must first
configure the project; do not guess a permanent document layout.

Read only the relevant module guide, glossary, ADR, active Spec or Tickets, and
implementation context. Use `$grilling` to distinguish facts that can be
discovered from decisions that belong to the user.

Identify the likely existing module guide or other authority before the first
decision question. This is provisional: do not create a new module boundary
merely because the interview topic has a convenient name.

## Grill and synchronize

Follow `$grilling` strictly: ask exactly one decision question per turn, include
a recommendation, and wait for the user's answer.

After each clear answer:

1. Separate confirmed target design from unresolved consequences and temporary
   implementation state.
2. Use `$project-documentation` to route the confirmed durable fact to exactly
   one authority.
3. Update the applicable Design or Architecture section of an existing module
   guide when the current task authorizes documentation edits. Preserve the
   project's configured language, paths, casing, terminology, and style.
4. Link other documents to that authority when a relationship must be visible;
   do not duplicate the full rule.
5. Continue with the next prerequisite decision only after the current decision
   and any authorized documentation update are settled.

Do not write alternatives, recommendations awaiting an answer, ambiguous replies,
or open questions into durable project documentation. Keep delivery scope and
progress in the configured tracker, not in module guides.

## Handle document boundaries

Prefer the relevant section of an existing module guide. If the confirmed topic
appears to need a new module guide, explain the proposed reading and maintenance
boundary and ask one explicit confirmation question before creating it. Until
the user confirms, keep the decision in the conversation and do not create an
empty or provisional document.

Use the creation and conflict rules from `$project-documentation`. In particular,
surface unexplained disagreements among code, active work, and durable documents;
never silently choose an authority.

## Stop after documentation synchronization

The workflow is complete when the user confirms shared understanding, important
decisions are reflected in their existing or explicitly approved authorities,
and remaining deferrals are named.

Summarize the confirmed design, updated module guides or other authorities, and
deferred questions. Do not automatically invoke `$to-spec`, create Tickets,
implement the design, or commit changes. The user starts the next workflow
explicitly in a new or existing conversation.
