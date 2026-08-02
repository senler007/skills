---
name: tdd
description: Drive feature or bug implementation through red-green cycles at user-confirmed stable public seams. Use when building behavior test-first, adding integration tests, or when another implementation workflow requires TDD discipline.
---

# TDD

Test external behavior through stable public interfaces. Treat tests as durable
specifications, not mirrors of current implementation structure.

## Confirm the seam first

Read the originating Spec or Ticket and repository test prior art. Identify the
highest practical seam where a caller or user observes the required behavior.
Prefer an existing seam and as few seams as possible.

Use only a seam already confirmed by the user or originating Spec. If no seam is
confirmed, propose it and wait for confirmation before writing a test. Do not
invent a lower-level seam for implementation convenience.

Read [references/tests.md](references/tests.md) for test quality and
[references/mocking.md](references/mocking.md) before introducing mocks.

## Run one red-green slice

For each narrow behavior:

1. Write one test through the confirmed seam with an independently known expected result.
2. Run that focused test and observe the intended failure for the right reason.
3. Implement only enough production behavior to make it pass.
4. Run the focused test again and observe green.
5. Run nearby focused checks, then choose the next tracer-bullet behavior.

Never write a batch of imagined tests before implementation. Keep each cycle a
vertical slice that can teach the next cycle.

## Protect test value

Test external behavior, not private methods, internal call order, storage shape,
prompt wording, or incidental file layout. Avoid tautological expectations that
recompute the implementation. Mock only real system boundaries; prefer real
owned modules and test infrastructure.

Do not expand behavior during a green step or perform unrelated refactoring.
Report optional refactors for review unless the current scope explicitly includes
them.
