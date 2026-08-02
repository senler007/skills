# Behavioral test quality

## Keep

- Exercise a public interface a caller or user relies on.
- Name the capability and observable outcome.
- Use independent literals, examples, or Spec criteria for expected results.
- Keep one logical behavior per test.
- Prefer integration-style coverage when it remains focused and deterministic.

## Reject

- Private-method, internal collaborator, call-count, or call-order assertions.
- Database inspection or other side channels when the public interface can verify behavior.
- Expected values computed by repeating the production algorithm.
- Snapshots of unstable prose or structure when equivalent behavior is valid.
- Horizontal batches of tests for code that does not yet exist.

A good test survives internal refactoring while failing when promised behavior changes.
