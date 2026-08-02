---
name: to-tickets
description: Convert a Spec, approved plan, or completed discussion into user-approved tracer-bullet Tickets with genuine dependency edges, then publish them through the configured GitHub, local, or custom tracker. Use when the user explicitly asks to break understood work into implementation Tickets.
---

# To Tickets

Plan narrow, complete delivery slices and publish only after the user approves
their granularity and dependencies.

## Gather authoritative context

Locate `issue-tracker.md` through the repository's agent instructions. Read the
full source Spec, plan, or completed discussion, including linked durable design,
architecture, ADRs, and glossary terms needed to plan delivery. If the source is
an Issue, read its complete body and relevant discussion.

Do not reopen settled design. Surface a genuinely blocking ambiguity instead of
inventing a Ticket around it.

## Draft tracer-bullet slices

Each Ticket must deliver a narrow but complete path through the layers it needs.
It must fit a fresh implementation context and be independently demonstrable or
verifiable when complete. Avoid horizontal Tickets such as "add all models" or
"write all tests" whose value exists only after later work.

Declare only blockers that genuinely prevent implementation from starting. Mere
ordering preference, shared topic, or convenience is not a dependency. Keep
independent Tickets parallel and identify the ready frontier.

For a wide mechanical migration that cannot be vertically sliced while keeping
the project green, use **expand-migrate-contract**:

1. expand with the new form beside the old;
2. migrate bounded caller groups in independently green batches;
3. contract only after every migration blocker completes.

Use an integration branch/final verification Ticket only when individual migrate
batches genuinely cannot stay green.

Draft each Ticket with [references/ticket-template.md](references/ticket-template.md).
Write acceptance criteria for observable completion and necessary documentation
synchronization, not a layer-by-layer task list.

## Obtain breakdown approval

Present a numbered proposal before publication. For every Ticket show its title,
what complete behavior it delivers, acceptance summary, and genuine blockers.
Ask the user to approve the granularity and dependency graph and to identify any
Ticket that should be merged, split, or made independent. Revise until approval
is explicit.

## Publish in dependency order

Follow the configured tracker:

- **GitHub:** create one Issue per approved Ticket, blockers first. Apply the
  configured ready label, attach every Ticket to the parent Spec with the native
  sub-issue relationship when available, and use native blocking relationships
  when available. Otherwise record real Issue references under Blocked by.
- **Local:** write one file per Ticket at the configured ticket location, numbered
  in dependency order. Record blocker file numbers/titles and ready status in
  each file; never publish a combined Ticket file.
- **Custom:** preserve the configured parent, dependency, identifier, and state
  model without inventing unsupported relationships.

Do not close, rewrite, or republish the parent Spec. Do not edit durable design
documents merely to mirror Ticket scope. Report the published identifiers, parent
relationships, dependency frontier, and any parallel work. Stop there: do not
invoke `$implement`, implement a Ticket, review, or commit.
