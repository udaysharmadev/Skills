# Evidence — hotseat

Status: **PROVEN LIFT** (2026-09-14) — on debate-structure footprints, with
a documented cost. Raw traces in `evals/results/` (gitignored); the trial
table below is the committed record.

## Primary claim

Stress-test ideas through genuinely different independent lenses (distinct
risks, non-redundancy, decision quality).

## Boundaries

Owns: independent round-1 verdicts, disagreement-only round 2, moderated
synthesis (matrix, assumption register, minority objections, MVP cut line,
falsifiable kill criteria). Must route elsewhere: settled ideas → `distill`;
cheerleading → labeled encouragement, no panel. Must not: manufacture
conflict, vote/score, fabricate research.

## Method

- Layer A: 6 trigger cases + hotseat-vs-distill sibling pair. Bundle smoke
  (C-005) applies.
- Layer B: H1–H5 (`evals/workflow/scenarios/signature-skills.md` — H4
  restraint + H5 forced-consensus authored Phase 02); execution pending.
- Layer C: `scripts/eval-outcome --skill hotseat` + protocol
  `evals/outcomes/hotseat.md` + frozen `hotseat-tasks.json`. Baseline = a
  strong critic prompt (seven named angles + MVP + risks + falsifiable
  kills) — the skill beats a good reviewer, not a strawman. Deterministic
  proxies, pre-registered: D1 ≥5/7 persona names, D2 kill section holds a
  number, D3 MVP + ≥2 assumption mentions. Matrix/minority presence
  recorded (Phase 02 additions).

## Raw results (committed summary; full traces gitignored)

Agent: Codex 0.153.4 (model gpt-5.6-sol). Commit `0d1f039` (all runs).
Zero infra failures after the harness fix below.

| Task | Baseline (n) | Treatment (n) |
|---|---|---|
| O1 one-habit tracker | 0/2 — 32–35K-char essays, MVP ✓, numbered kills ✓, 1 assumption mention, 0 named personas | **2/2** — 7/7 personas, 23–25 assumption mentions, matrix ✓, minority ✓ |
| O2 portfolio AI chat | 0/2 — same shape (1–3 assumptions, MVP + kills ✓) | **2/2** — 7/7 personas, 25–40 assumptions, matrix ✓, minority ✓ |
| O3 held-out QR attendance | 0/1 — MVP + numbered kill ✓, 1 assumption | **1/1** — 7 personas, 36 assumptions, matrix ✓, minority ✓ |

Totals: treatment 5/5 incl. held-out; baseline 0/5 on the structural gate
while producing genuinely good unstructured critiques.

## Analysis

- The lift is structural, exactly the claim: independence footprint (7
  named verdicts formed before cross-talk), assumption depth (23–40 vs
  1–3 mentions), and decision artifacts (matrix + minority 5/5 vs 0/5).
- Baselines are strong — both conditions deliver MVP + falsifiable kills.
  The skill does not rescue bad reviewers; it converts good reviews into
  auditable debates.
- Cost (not hidden): treatment runs 70–310s vs baseline 45–70s and ~61K
  vs ~33K output chars. No EFFICIENCY LIFT claimed; for quick takes the
  `quick challenge` mode exists precisely for this reason.
- Reviewer note (non-blind, not ground truth): treatment debates show
  real cross-examination (round-2 attacks reference other personas'
  claims); baselines list angles without confrontation.

## Limitations

- n is small (5 treatment / 5 baseline incl. held-out); single agent
  (codex), single model. Opencode replication pending runner time.
- Proxies ≠ quality: persona-name counts measure structure, not wisdom.
  Blind diversity rubric still future work.
- First attempt (result file `…212658…`, preserved) was invalidated by a
  harness bug: 4000-char head-only truncation cut the graded synthesis
  and 180s timeouts killed full debates. Fixed (head+tail 60K capture,
  per-task timeout, hotseat 600s) and re-ran clean — the fix is method,
  not tuning: no skill content changed between attempts.
- Long-form cost means routine re-runs are expensive; future trials can
  use `quick challenge` for regression and full mode for release gates.

## Context audit

hotseat SKILL.md ~180 lines (~2170 tok, at but under the 1.5× median
flag), personas.md carries the depth. Phase 02 added a scoreless decision
matrix + mandatory minority-or-why-empty section (falsifiable in H5).
No new always-on cost.

## Reproduce

```bash
scripts/eval-outcome --skill hotseat --agent codex --trials 2
scripts/eval-outcome --skill hotseat --agent codex --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
