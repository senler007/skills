---
name: grilling
description: Stress-test a plan or design through questions ordered by decision dependencies. Use when the user asks to be grilled or to challenge a design.
---

Model the unresolved design as a decision tree. In each round, ask a small group
of questions whose prerequisites are settled, with a recommendation and its
tradeoff for each. Let the answers determine the next round; do not ask dependent
questions together or reopen decisions without conflicting evidence.

Resolve discoverable facts from the project before asking the user. Focus on
choices that change the outcome, scope, or costly commitments. Finish when the
material decisions are resolved, not when every hypothetical branch is explored.

If the user asks to preserve the design in project docs, read the relevant
existing authorities first. Keep the interview out of those files until the user
confirms a consolidated decision summary, then use `$project-documentation` to
write the confirmed decisions once. A revised summary needs confirmation of the
changed decisions.
