---
name: grilling
description: Stress-test a plan, decision, feature, or design through a relentless one-question-at-a-time interview. Use when the user asks to be grilled, interrogated, challenged, or wants to resolve ambiguities and reach shared understanding before acting.
---

# Grilling

Interview the user until the important decisions, dependencies, and edge cases are
understood. Do not implement the subject of the interview.

## Discover before asking

Inspect the available repository, documents, tracker context, and tools before
asking a question whose answer may already be discoverable. Look up facts such
as current behavior, file locations, existing terminology, framework support,
and documented constraints.

Keep decisions with the user. Do not turn a design choice into a factual claim
merely to avoid asking it.

## Resolve one decision at a time

Maintain an internal decision tree and work from prerequisite decisions toward
dependent ones. On every turn:

1. Explain the current ambiguity or tradeoff briefly.
2. Ask exactly one decision question.
3. Give a recommended answer and the reason it best fits the known constraints.
4. Wait for the user's answer before continuing.

Do not bundle several questions into a list. If a user's answer exposes another
branch, record it for a later turn instead of asking immediately. Challenge
contradictions, vague words, missing failure behavior, and unstated ownership
rather than accepting them as shared understanding.

Treat a decision as confirmed only when the user's answer is clear. When an
answer is ambiguous, restate the interpretation and use the next single question
to confirm it.

## Finish at shared understanding

Continue until consequential branches are resolved, discoverable facts have
been checked, rules and terms no longer conflict, and any intentionally deferred
questions are named with their impact.

Then summarize the shared understanding, the important decisions, and any
explicitly deferred items. Ask the user to confirm the session is complete if
that has not already been made clear. Stop there: do not implement, create a
Spec, create tickets, or begin another workflow automatically.
