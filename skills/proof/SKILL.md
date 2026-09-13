---
name: proof
description: Chooses the right test boundary and builds regression protection — test behavior, not implementation trivia. Use when writing or improving tests, after fixing a bug (reproduce it as a test first), before merging or refactoring, when the user mentions testing, coverage, unit/integration/e2e tests or flaky tests, or asks whether something is actually tested. Works at any layer — unit, component, integration, contract, API, database, end-to-end, browser — and refuses to maximize test count for its own sake.
---

# proof — the right test at the right boundary

The skill is the boundary choice. A suite of 500 trivial unit tests that
misses the broken checkout proves nothing; three well-placed API tests
that would catch it prove everything. Test count is not the goal —
**catching real regressions is**.

## When NOT to use

- The bug isn't understood yet → `sleuth` finds the cause; you lock it
  down with a regression test after.
- The question is whether the flow works in a real browser → `roadtest`.
- Pure performance → `hotpath`.

## Prerequisites

A runnable way to execute the chosen layer (framework, runner, CI or
local commands). If the repo has no test setup at all, that's the first
deliverable: the smallest honest harness for this stack — not a
framework tour.

## Workflow

### 1. Name the behavior and its risk

"Anonymous users cannot read another user's orders" — a behavior, a
stake, a failing condition. If you can't name the behavior, you're about
to test trivia.

### 2. Pick the cheapest boundary that would catch a real regression

Read `references/boundary-picker.md` for the full decision table. Rule
of thumb: **push the test down** (unit for pure logic) until the
behavior genuinely crosses a boundary (HTTP, DB, queue, browser) — then
test at that boundary and stop. Two classic errors:

- everything end-to-end → slow, flaky, nobody runs it;
- everything unit → green suite, broken product (the mocks lied).

### 3. Write tests that survive refactors

- Names state behavior: `rejects orders over the credit limit`, not
  `processOrder_v2_works`.
- Arrange–act–assert, one behavior per test.
- Edge/error paths are first-class: empty, zero, negative, huge,
  malformed, unauthorized, concurrent, offline.
- Assertions on observable outcomes (returned data, state, side effects
  the user cares about) — not on internal call sequences.

### 4. Mocking discipline

Mock only boundaries you don't own and can't run (network, clock, RNG,
third-party APIs). Never mock the unit under test, the database in a
database test, or so much that the test verifies the mock arrangement
rather than the behavior. A test that fails only because a mock drifted
is a liability — delete or ground it in a contract test.

### 5. Run and classify

Full suite green. Any flake: fix the cause if visible; otherwise
quarantine honestly (`@flaky` marker + issue opened) — never delete a
failing test to get green, never hide flakiness in the report.

### 6. Regression lock

Every confirmed bug gets a test that **fails without the fix and passes
with it** — this is the rule that converts debugging into permanent
value. The regression test lands in the same change as the fix.

## Quality gates

- Boundary choice justified in one line per test group ("API-level: the
  behavior is the contract").
- Test names state behavior; assertions are on outcomes, not internals.
- Edge/error paths covered for new public surfaces.
- Suite green as run by the actual runner — coverage/counts quoted only
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
why. On disk: test files in the project's convention — never a parallel
`__tests_dump__` folder.
