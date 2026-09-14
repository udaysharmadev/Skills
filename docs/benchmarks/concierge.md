# Evidence — concierge

Status: **MIXED** (2026-09-14). First skill with executed Layer C trials.
Raw traces in `evals/results/` (gitignored per policy); the trial table
below is the committed record. No number here lacks a pointer.

## Primary claim

Route any request to the smallest sufficient workflow (routing accuracy /
over-route rate).

## Boundaries

Owns: uncertainty-source routing, smallest-chain discipline, handoff
announcement, loop ceiling (same domain ≤ 2 dispatches). Must route
elsewhere: every specialist domain. Must not: execute the work itself,
re-enter mid-task, route around gates, or invent a manifest (rejected in
`docs/research/concierge.md` — judgment over static scores).

## Method

- Layer A: 8 trigger cases (`evals/trigger/cases.md` concierge block) +
  concierge-vs-handsfree sibling pair + router-stress chains + none-cases.
  Bundle smoke: Codex 11/12, OpenCode 12/12 (pre-existing, see C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/concierge.md` (C1–C5);
  authored, execution pending runner time.
- Layer C: `scripts/eval-outcome` (new harness, stdlib-only) + protocol
  `evals/outcomes/concierge.md` + frozen tasks
  `evals/outcomes/concierge-tasks.json`. Baseline = skill catalog only;
  treatment = catalog + concierge SKILL.md + references. Deterministic
  grading, pre-registered before the first run.

## Raw results (committed summary; full traces gitignored)

Agents: Codex 0.153.4 (model gpt-5.6-sol) · OpenCode 1.18.30.
Commit `3665f6c` for all runs (recorded in each result JSON).
Timeout 180s; all runs 6–17s, zero infra failures.

| Task | Agent | Baseline | Treatment |
|---|---|---|---|
| O1 "Login is broken." (need: ⊆ {spelunk,sleuth,proof,roadtest}, incl. sleuth, ≤3) | codex, n=3 (+1 smoke) | 1/4 — failures both `sleuth→backend→proof` (backend over-route) | **4/4** `spelunk→sleuth→proof` |
| O1 same | opencode, n=2 | 2/2 `sleuth` alone | 2/2 `spelunk→sleuth→proof` |
| O2 "Rename the login button…" (need: `direct`) | both, n=3+3 (+1+0 smoke) | 7/7 `direct` | 7/7 `direct` |
| O3 held-out "Stripe webhooks then implement" (need: ⊆ {scout,backend,proof}) | codex, n=1 | 1/1 `scout→backend` | 1/1 `scout→backend→proof` (= repo's documented chain) |

## Analysis

- **Strongest lift (O1/codex):** treatment 4/4 canonical chains vs baseline
  1/4; both baseline failures add `backend` to a bug triage — the exact
  over-routing the skill exists to prevent.
- **O2:** no lift available — both conditions go `direct` 7/7. Strong
  baselines already do tiny tasks right; recorded, not hidden.
- **O1/opencode caveat:** baseline's bare `sleuth` passes the
  pre-registered grader but under-routes (no orientation, no regression
  proof) while treatment gives the full chain. Kept the pre-registered
  grades untouched; logged as a protocol limitation below instead of
  re-grading after the fact.
- **Verdict MIXED:** clear lift where the baseline over-routes, none where
  it already routes well. No gate-skips observed anywhere.

## Limitations

- n is small (codex 4+4+1, opencode 2+2 per task family); stochastic
  models deserve wider CIs before any strong claim.
- Grader rewards minimalism: a one-skill subset always passes O1/O3 even
  when a fuller chain is better. Future protocol version should score
  chain completeness, not just containment.
- Routing-given-text only: no repo inspection, no multi-turn loop
  behavior, no mid-workflow re-routing measured yet (C-scenarios cover
  the spec; execution pending).
- Single model family per agent run (codex→gpt-5.6-sol); cross-model
  generality untested.

## Context audit

concierge SKILL.md 190 lines (~2050 tok, under 1.5× median), 2 references
(routing table ~150 lines, capability-degradation). Phase 01 added the
28/28 predicate table, handsfree/direct/none rows, and the loop ceiling —
all in references except a 5-line SKILL.md pointer. No new always-on cost.

## Reproduce

```bash
scripts/eval-outcome --skill concierge --agent codex --trials 3
scripts/eval-outcome --skill concierge --agent codex --trials 1 --heldout
scripts/eval-outcome --skill concierge --agent opencode --trials 2
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
