# Evidence — backend

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
08); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Build production-grade backend behavior across stacks (authz /
idempotency / transaction correctness).

## Boundaries

Owns: stack detection, failure-semantics disciplines, verification at
the right boundary. Must route elsewhere: scale decisions → `headroom`;
architecture docs → `blueprint`; unclear-cause bugs → root-cause first.
Must not: answer Node-shaped for Django, trust clients, swallow errors,
log secrets, average conflicts.

## Method

- Layer A: 5 trigger cases + idempotency-trap case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/backend.md` (BE1–BE5,
  incl. exactly-once-under-retries and trust-the-client adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/backend.md` + frozen
  `backend-tasks.json` (two stacks, workspace grading). Grader verified
  offline (constraint vs `if` discriminate correctly).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Proxies can't prove true exactly-once under concurrency or isolation
  correctness — blind review + (later) runnable race fixtures required.
- Fixture suites aren't runnable (seeded gap); executable checks are thin
  (parse/presence) until runnable fixtures exist.
- Single-turn runs can't test migration sequencing across deploys.

## Context audit

SKILL.md ~105 lines, 1 reference (checklists, section-scoped reads), 0
scripts (justified: judgment across stacks). Phase 08 added outbox,
retry-ownership, deadlock, backpressure, contract sections, and removed
a duplicated webhooks bullet — net depth up, size nearly flat.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill backend --agent <agent> --trials 2
scripts/eval-outcome --skill backend --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
