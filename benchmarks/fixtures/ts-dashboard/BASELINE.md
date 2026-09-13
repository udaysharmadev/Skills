# Baseline — behavior of the fixture BEFORE any benchmark run

Fixture: ts-dashboard @ seeded state. Recorded 2026-09-14.

## What "working" means here

This is a benchmark fixture, not a product: it is intentionally broken in
seeded ways. The baseline records the seeded state so a benchmark run
must (a) fix the seeded defects without (b) breaking anything that was
working, and (c) be incremental.

## Seeded baseline

- Build/typecheck: expected to fail or produce strict-mode errors in
  several files (seeded `any` usage means it depends on tsconfig strict
  flag — fixtures/ts-dashboard has no tsconfig on purpose; graders
  evaluate detection, not the build).
- Tests: none exist ("test": "vitest run" with no tests — seeded gap).
- Runtime: no install attempted in-repo; the fixture is source-only by
  design (no node_modules in git).

## Grader note

The evaluated agent should:
1. detect the seeded issues (answer key: benchmarks/answer-keys/ts-dashboard.json),
2. verify every finding with location evidence,
3. remediate incrementally with a behavior-preserving batch protocol,
4. add tests for money-adjacent logic it touches,
5. never rewrite wholesale.

Scoring dimensions: detection recall / false positives / evidence
quality / remediation correctness / incrementality.
