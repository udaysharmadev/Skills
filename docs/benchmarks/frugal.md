# Evidence — frugal

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
24); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Cheaper without weaker: exact diagnostics, categorized savings,
protected verification (frugality honesty).

## Boundaries

Owns: leak finding, fitting techniques, honest savings reports,
compact handoffs. Must route elsewhere: undefined tasks → define gate
first; deliberate exhaustive output → user's call. Must not: compress
diagnostics, fabricate percentages, cut verification, minimize raw.

## Method

- Layer A: 5 trigger cases + no-skipped-verification case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/frugal.md` (FG1–FG5,
  incl. no-telemetry failure and 63-percent adversarial); authored,
  unexecuted. Signature F1–F3 remain as cross-checks.
- Layer C: protocol `evals/outcomes/frugal.md` + frozen
  `frugal-tasks.json` on the `frugal-hunt` fixture via the fact
  grader — frozen ERROR line numbers + honesty groups + compactness
  budgets. Verified offline on all gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Numbers are not process proof: whether extraction was actually cheap
  stays unmeasured headless — the line budget proxies it.
- One hunt shape (log grep); other economies (cache prefixes, model
  routing) get scenario coverage only until tasks grow.

## Context audit

SKILL.md ~140 lines, 1 reference (measurement rules). Phase 24 added
Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill frugal --agent <agent> --trials 2
scripts/eval-outcome --skill frugal --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
