# Mocking boundaries

Mock only boundaries outside the owned system when deterministic real use is not
practical: external APIs, time, randomness, network services, and sometimes a
database or filesystem.

Do not mock owned classes or internal collaborators. Test them together through
the confirmed public seam. Prefer a real test database or filesystem fixture when
it is reliable and proportional.

At an external boundary, expose narrow operation-specific interfaces and inject
the dependency. Avoid generic mocks whose conditional behavior reproduces the
implementation inside test setup.
