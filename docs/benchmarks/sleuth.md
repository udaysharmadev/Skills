# Evidence — sleuth

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
16); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Cause chains with evidence per link — then the smallest fix
(guess-and-check refusal / suppression refusal).

## Boundaries

Owns: reproduction, minimization, failing signals, competing
hypotheses, chain naming, minimal fixes. Must route elsewhere: slowness
→ `hotpath`; known fix → `scout` + fix; test locks → `proof`; above-code
causes → decision routing. Must not: guess-fix, suppress symptoms,
resurrect dead hypotheses, pad scope.

## Method

- Layer A: 5 trigger cases + cause-before-change case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/sleuth.md` (SL1–SL5,
  incl. cannot-reproduce, labeled-provisional, wrap-it-and-ship
  adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/sleuth.md` + frozen
  `sleuth-tasks.json` on the `sleuth-cache` fixture via the workspace
  grader (freshness + cache-still-used behavior checks separate true
  fixes from bypasses). Verified offline end-to-end (real runs, all
  gates) — including catching and fixing a real harness bug (below).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## The harness bug offline testing caught

`observe()` counted `__pycache__/*.pyc` as agent-changed files, so any
Python trial running code false-failed scope — including a perfect
`proof` O2 run from Phase 14 (latent since then; Phase 14's sim missed
it because leaked pycache sat in both fixture and workdir). Fixed in
`scripts/eval-outcome` (bytecode filtered, mirrors `.gitignore`);
sleuth + proof discriminations re-verified after the fix.

## Limitations (known before first run)

- Behavior checks + markers are not reasoning quality: whether the
  chain is real stays in blind review.
- One bug shape (stale cache); intermittents and env-shaped bugs get
  scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~160 lines, 1 reference (techniques). Phase 16 added
Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill sleuth --agent <agent> --trials 2
scripts/eval-outcome --skill sleuth --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
