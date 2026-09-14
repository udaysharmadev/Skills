# Evidence — unslop

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
20); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Rescue without rewrite: baseline first, ranked batches verified,
quirks kept with reasons (detox honesty).

## Boundaries

Owns: behavior baselines, slop mapping/ranking, batched behavior-
preserving cleanup, kept-lists. Must route elsewhere: single bugs →
`sleuth`; slowness → `hotpath`; missing tests → `proof`; UI slop →
`polish`. Must not: giant rewrites, behavior drift, test gaming,
performative cleanup, invented findings.

## Method

- Layer A: 5 trigger cases + audit-first case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/unslop.md` (UN1–UN5,
  incl. no-baseline failure and rewrite-it adversarial); authored,
  unexecuted. Signature U1–U3 remain as cross-checks.
- Layer C: protocol `evals/outcomes/unslop.md` + frozen
  `unslop-tasks.json` on the `unslop-shop` fixture via the workspace
  grader — suite green + slop gone + quirk surviving + net-negative
  lines + tests-untouched scope. Verified offline end-to-end (real
  runs, all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Greps are not taste: batch quality and ranking honesty stay in blind
  review.
- One repo shape (small Python module); mega-component splits and
  dependency pruning get scenario coverage only until fixtures grow.
- Baseline-protection is scope-shaped: an agent rewriting tests AND
  code consistently could still pass — blind review watches for it.

## Context audit

SKILL.md ~125 lines, 1 reference (slop catalog). Phase 20 added Tool
selection/fallback consolidating the three signal rungs — zero new
always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill unslop --agent <agent> --trials 2
scripts/eval-outcome --skill unslop --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
