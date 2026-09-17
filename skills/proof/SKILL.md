---
name: proof
description: Chooses and implements the cheapest trustworthy test boundary for a behavior or invariant, including regression, property, contract, integration, and end-to-end tests. Use when adding tests, protecting a bug fix, or proving changed behavior without optimizing for coverage counts.
---

# proof: the right test at the right boundary

The skill is the boundary choice. A suite of 500 trivial unit tests that
misses the broken checkout proves nothing; three well-placed API tests
that would catch it prove everything. Test count is not the goal,
**catching real regressions is**.

## When NOT to use

- The bug isn't understood yet → `sleuth` finds the cause; you lock it
  down with a regression test after.
- The question is whether the flow works in a real browser → `roadtest`.
- Pure performance → `hotpath`.

## Prerequisites

A runnable way to execute the chosen layer (framework, runner, CI or
local commands). If the repo has no test setup at all, that's the first
deliverable: the smallest honest harness for this stack: not a
framework tour.

Also identify the behavior owner, public contract or invariant, risk surface,
existing test convention, deterministic fixture strategy, and execution
environment. The behavior may be confirmed by code, a bug report, contract,
or user-provided acceptance rule; do not infer it from a test name alone.

## Authority and preservation boundaries

- Tests may create isolated fixtures, temporary directories, test schemas, or
  local processes within the repository convention. Never target production,
  shared customer data, paid third parties, or a live account without approval.
- Preserve existing test style, runner, fixtures, and naming where they work.
  Do not replace a suite or add a framework to test one small behavior.
- Do not weaken/remove a test, assertion, timeout, or coverage gate merely to
  make a change green. Diagnose or label the reason and seek approval for any
  intentional expectation change.
- Do not report a test as passed unless its actual runner exited successfully
  in the stated environment. A compile-only, collection-only, or mocked check
  is a different evidence class.
- Keep secrets, production identifiers, and proprietary captures out of test
  fixtures and failure output.

## Test design record

Before writing code, write one compact record per behavior:

| Field | Required answer |
| --- | --- |
| Behavior/invariant | observable expected result and prohibited result |
| Risk | user/data/auth/money/compatibility/operational consequence |
| Boundary | lowest faithful test boundary and why lower layers miss it |
| Oracle | exact result, state, side effect, or property that proves outcome |
| Fixture | smallest representative setup and isolation/reset method |
| Negative cases | malformed, unauthorized, boundary, concurrency, or failure cases that apply |
| Mutation | a deliberate implementation break expected to make this test fail |

If the oracle is vague, write a narrow acceptance example or route to the
decision owner. A test cannot prove "better" or "works" without an observable
condition.

## Workflow

### 1. Name the behavior and its risk

"Anonymous users cannot read another user's orders": a behavior, a
stake, a failing condition. If you can't name the behavior, you're about
to test trivia.

### 2. Pick the cheapest boundary that would catch a real regression

Read `references/boundary-picker.md` for the full decision table. Rule
of thumb: **push the test down** (unit for pure logic) until the
behavior genuinely crosses a boundary (HTTP, DB, queue, browser): then
test at that boundary and stop. Two classic errors:

- everything end-to-end → slow, flaky, nobody runs it;
- everything unit → green suite, broken product (the mocks lied).

### 3. Write tests that survive refactors

- **Mutation Validation (Anti-Vacuous):** A test that always passes is worse than no test. Before claiming a test is green, deliberately break the implementation (or use mutation testing if available) to prove the test **fails** (Red-Green TDE).
- **Property-Based Testing (PBT):** For core invariants (e.g., serialization, idempotency), prefer generating properties (`decode(encode(x)) == x`) over a handful of static, AI-biased examples.
- Names state behavior: `rejects orders over the credit limit`, not
  `processOrder_v2_works`.
- Arrange–act–assert, one behavior per test.
- Edge/error paths are first-class: empty, zero, negative, huge,
  malformed, unauthorized, concurrent, offline.
- Assertions on observable outcomes (returned data, state, side effects
  the user cares about): not on internal call sequences.

### 4. Mocking discipline (Anti-Over-Mocking)

Mock only boundaries you don't own and can't run (network, clock, RNG,
third-party APIs). Never mock the unit under test, the database in a
database test, or so much that the test verifies the mock arrangement
rather than the behavior. Use **production-shaped data** (or captured real traffic) instead of simplistic, hallucinated stubs. A test that fails only because a mock drifted is a liability: delete or ground it in a contract test.

### 5. Run and classify

Full suite green. Any flake: fix the cause if visible; otherwise
quarantine honestly (`@flaky` marker + issue opened): never delete a
failing test to get green, never hide flakiness in the report.

### 6. Regression lock

Every confirmed bug gets a test that **fails without the fix and passes
with it**: this is the rule that converts debugging into permanent
value. The regression test lands in the same change as the fix.

### 7. Review test trustworthiness

Read the test as a future failure detector. Verify setup cannot satisfy the
assertion by itself; fixture state is reset; clocks, randomness, ordering, and
network are controlled; failures show enough relevant diagnostic context; and
the assertion would fail for the known incorrect behavior. Use the lightest
mutation: remove the guard, flip an operator, return an invalid status, or
break the critical contract, then restore it immediately.

For a high-risk change, test the happy result, a nearby valid case, and the
critical rejection/failure boundary. Do not expand into every scenario without
an identified risk. Put generated cases behind a property when the invariant
is stable and the generator/shrinker will produce interpretable failures.

## Boundary-specific expert rules

### Contracts, APIs, and authorization

Exercise the real route/application boundary with a realistic identity and
assert status, response shape, headers/error contract where public, persistent
outcome, and absence of forbidden side effect. Test the authorization matrix
at the enforcement point: unauthenticated, lower-privilege, wrong tenant/object,
and permitted cases as applicable. Client-side hiding is not evidence.

### Databases, migrations, and jobs

Use the real database engine when SQL dialect, constraints, locking,
transactions, migrations, triggers, or query semantics matter. Test migration
up and the approved rollback/recovery path where the project supports it;
verify existing rows and new writes preserve invariants. For jobs, assert
idempotency, retry/dead-letter behavior, duplicate delivery, scheduling
boundary, and observable completion only where relevant.

### Time, concurrency, and nondeterminism

Inject or freeze a clock, seed a random source, use deterministic IDs, and
wait for conditions rather than sleeping. For concurrency, assert an invariant
under a controlled interleaving or repeated bounded run, then record its
limitation. A passing race test on one machine is not proof of universal safety.

### Browser and end-to-end scope

Use end-to-end only for the small set of user-critical cross-boundary paths.
Keep data setup explicit, selectors stable, environment/viewport documented,
and failures diagnosable. Hand browser visual, console, network, and real-flow
evidence to roadtest rather than duplicating its deliverable.

## Tool selection/fallback

- Project runner (pytest, vitest, go test, unittest…) → real runner
  output only; counts and coverage quoted from it, never estimated.
- No test setup at all → smallest honest harness for the stack first,
  then the tests; framework tour refused.
- Mutation tooling → use it; otherwise break-and-restore by hand: one
  deliberate break per new test group, reverted after the red is seen.
- No runner executable here → tests delivered + run command stated,
  suite status marked **unverified**, never "should pass".

## Quality gates

- Boundary choice justified in one line per test group ("API-level: the
  behavior is the contract").
- Test names state behavior; assertions are on outcomes, not internals.
- Edge/error paths covered for new public surfaces.
- Suite green as run by the actual runner: coverage/counts quoted only
  from real runner output, never estimated.
- Regression test exists for every bug fixed in this change.

## Stop conditions

- Coverage delivered at the justified boundaries, suite green → summary,
  stop.
- Writing the test reveals a bug → route to `sleuth` with the failing
  signal you just built.
- No runner/CI available → deliver the harness + tests runnable locally,
  mark CI integration as the known gap.

## Output contract

Chat: the boundary map (behavior → boundary, one line each), evidence
(`N tests passing via <command>`), gaps deliberately left uncovered and
why. On disk: test files in the project's convention: never a parallel
`__tests_dump__` folder.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
