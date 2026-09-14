# Outcome benchmark — hotseat

Status: protocol + tasks frozen 2026-09-14; trials execute via
`scripts/eval-outcome --skill hotseat`. Numbers appear only with full
provenance.

## Design

Same idea, same agent/model; the only intended difference is whether the
`hotseat` runtime (SKILL.md + persona cards) is in context. Baseline is a
strong critic prompt (seven named angles + MVP + risks + falsifiable kill
criteria) — the skill must beat a good reviewer, not a strawman.
2 trials per condition per task (full debates are long); held-out idea O3
runs once per condition at the end, never tuned against.

## Tasks (`hotseat-tasks.json`)

- O1: one-habit tracker. O2: AI chat on a portfolio site.
- O3 held-out: QR attendance app.

## Grading (deterministic proxies, pre-registered)

- D1: ≥5 of 7 persona names present (independence footprint).
- D2: kill section contains a number (falsifiability footprint).
- D3: MVP present + ≥2 "assum" mentions (register footprint).
- Pass = D1 & D2 & D3. Recorded but non-gating: decision-matrix and
  minority-section presence (Phase 02 additions), assumption count,
  persona count — for baseline/treatment comparison.
- Reviewer rubric (labeled non-blind): genuine diversity vs echo,
  decision usefulness. Never presented as ground truth.

## Verdict rule (pre-registered)

Treatment beats baseline repeatedly on pass rate + diversity footprints
→ lift (PROVEN/CONSISTENCY per the shared vocabulary). Baseline already
at ceiling → NO CLEAR LIFT. Treatment worse → REGRESSION.

## Reproduce

```bash
scripts/eval-outcome --skill hotseat --agent codex --trials 2
scripts/eval-outcome --skill hotseat --agent codex --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/hotseat.md`.
