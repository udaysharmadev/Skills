# Outcome benchmark — spelunk

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy: no Codex/payed-model runs without an
explicit trial budget). The harness support (fixture workspaces,
fact-recall grader) is implemented and offline-tested; numbers appear only
after live runs with full provenance.

## Design

Same fixture repo, same agent/model/tools; the only intended difference is
whether the `spelunk` runtime (SKILL.md + discovery checklist) is in
context. Baseline is a strong explorer prompt (read-before-claim, exact
paths, no guessing) — the skill must beat good exploration, not tourism.
The agent works inside a copy of a seeded fixture with a known answer key
(`benchmarks/answer-keys/`, never shown to the agent). 2 trials per
condition per task; held-out questions O3 run once per condition at the
end, never tuned against (no tuning occurs at all — failures only change
the skill via the normal review path, then re-run).

## Tasks (`spelunk-tasks.json`)

- O1 (ts-dashboard): test command + Order-type sites + unused deps + fetch site.
- O2 (py-notes-api): entry point + declared stack + unused deps + test setup.
- O3 held-out (ts-dashboard, unseen questions): swallowed errors + dead date code + CSV export.

## Grading (deterministic, pre-registered)

Per task: `must_contain` recall (all substrings present), zero
`must_not` contaminants, and **every code path mentioned resolves to a
real fixture file** (hallucinated-path check). Pass = 1.0 recall + clean.
Recorded alongside: duration, output size. Tool-call/file/byte counts are
not exposed by headless runners — accuracy first, cost honest-labeled
(`scripts/eval-outcome` records what the runtime exposes).

## Verdict rule (pre-registered)

Treatment more accurate (higher recall, fewer hallucinations) repeatedly
→ lift (PROVEN/CONSISTENCY per the shared vocabulary). Baseline already
perfect → NO CLEAR LIFT. Treatment worse → REGRESSION. Efficiency
(EFFICIENCY LIFT) only if success is held constant and cost is MEASURED.

## Reproduce (requires an explicit trial budget — see policy)

codex additionally requires the paid-agent guard keys (`--allow-paid` +
`ALLOW_PAID_AGENT=1`, set only by the human authorizing that run — see
`evals/adapters/README.md`).

```bash
scripts/eval-outcome --skill spelunk --agent <agent> --trials 2 [--allow-paid]
scripts/eval-outcome --skill spelunk --agent <agent> --trials 1 --heldout [--allow-paid]
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/spelunk.md`.
