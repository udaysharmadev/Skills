# Evaluations

How the suite measures itself. Honesty rules from the PRD bind every
number shown anywhere: `measured` / `derived` / `estimated` / `unknown`
— never blurred.

## Trigger evals (running)

```bash
scripts/eval-trigger --check                      # capability table
scripts/eval-trigger --agent claude --tier smoke  # 12 cases, measured
scripts/eval-trigger --suite all --agent claude --tier standard
```

- **Suites:** `evals/trigger/cases.md` (134 positive/negative +
  direct-route cases), `sibling-confusion.md` (20 adjacency cases),
  `router-stress.md` (14 adversarial/multi-skill/degraded cases)
  = 168 total.
- **Method:** routing-given-metadata (see `evals/adapters/README.md`).
  Measures routing decisions, not in-runtime auto-activation — that
  limitation is stated wherever results are quoted.
- **Metrics:** precision, recall, F1 (single-slug cases), accuracy
  (all cases incl. chains, exact-match for chains — a documented
  limitation), per-skill confusion, top confusion pairs.
- **Provenance:** every result JSON records schema version, timestamp,
  git commit, agent + version + model (where the runtime exposes it),
  invocation-verified flag, runs, and raw per-case output. Results run
  in a neutral temp cwd — the evaluated agent cannot read the answer key. Results land in `evals/results/` (gitignored);
  curated release evidence may be committed separately.

## Workflow evals (authored; execution wired in 0.8)

`evals/workflow/scenarios/` — per-skill scenario specs with
deterministic assertions first (file exists, command exits zero,
artifact shape, forbidden-claim absence), model-graded rubrics only
where the dimension is genuinely qualitative. Coverage status is
tracked in that directory's README — authored ≠ executed, and we don't
conflate the two.

## Outcome benchmarks (0.8)

Skill-vs-no-skill comparisons on seeded fixtures
(`benchmarks/`) — see `docs/benchmarks.md`.

## Budget controls

`--tier smoke|standard|release` (12/40/all), `--max-cases`, `--runs`,
`--timeout`, `--dry-run`. CI runs only the deterministic checks; live
agent evals are manual dispatch (`workflow_dispatch`) with explicit
secrets. Never unexpectedly spend token budgets.

## Regression process

issue → minimal reproduction → regression case in `evals/regression/`
→ fix → case passes → case stays. The suite gets harder to break over
time.
