# Maintainer evaluation evidence

> This material is optional maintainer evidence, not part of installation or
> normal skill use. It records historical methodology and results without any
> claim that the bundle is benchmark-superior.

How the suite measures itself. Honesty rules from the PRD bind every
number shown anywhere: `measured` / `derived` / `estimated` / `unknown`
— never blurred.

## Trigger evals (running)

```bash
scripts/eval-trigger --check                      # capability table
scripts/eval-trigger --agent claude --tier smoke  # 12 cases, measured
scripts/eval-trigger --suite all --agent claude --tier standard
```

- **Suites:** `evals/trigger/cases.md` (173 positive/negative +
  direct-route cases), `sibling-confusion.md` (24 adjacency cases),
  `router-stress.md` (14 adversarial/multi-skill/degraded cases)
  = 211 total.
- **Method:** routing-given-metadata (see `evals/adapters/README.md`).
  Measures routing decisions, not in-runtime auto-activation — that
  limitation is stated wherever results are quoted.
- **Metrics:** precision, recall, F1 (single-slug cases), accuracy
  (all cases incl. chains, exact-match for chains — a documented
  limitation), per-skill confusion, top confusion pairs.
- **Provenance:** every result JSON records schema version, timestamp,
  git commit, agent + version + model (where the runtime exposes it),
  invocation-verified flag, runs, and raw per-case output. Results run
  in a neutral temp cwd — the answer key is not placed in its prompt or cwd.
  This is contamination resistance, not a filesystem/network security
  boundary. Results land in `evals/results/` (gitignored);
  curated release evidence may be committed separately.

## Workflow evals (evidence runner available)

`evals/workflow/scenarios/` — per-skill scenario specs with candidate
checks labeled `D#` (deterministic where possible) and qualitative rubrics
labeled `R#`. Coverage status is
tracked in that directory's README — authored ≠ executed, and we don't
conflate the two.

```bash
scripts/eval-workflow --check
scripts/eval-workflow --list
scripts/eval-workflow --scenario H3 --agent codex
```

Live workflow runs require an explicit scenario id. The evaluated agent
receives setup, task and skill instructions, but not assertions or answer
keys. Each result records raw final output, skill-package hashes, workspace
manifests, an artifact archive and agent/version/model provenance. Assertions stay `ungraded`
until a deterministic or human grader evaluates them; an executed trial is
not automatically a passing trial. This task/trial/grader separation and
evidence-first design follows current guidance from
[Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
and the UK AI Security Institute's [Inspect log model](https://inspect.aisi.org.uk/eval-logs.html).

## Outcome benchmarks (proof phase underway)

The outcome harness contains 83 validated tasks across all 28 skills. Ten
skill families have executed trials: `hotseat` has a measured lift on its
pre-registered debate-structure proxies; five verdicts are MIXED; three show
NO LIFT on the available evidence. The `handsfree` smoke sample exposed a
grader defect and remains UNVERIFIED, alongside 18 unexecuted families. See
[`docs/benchmarks.md`](benchmarks.md) and the per-skill pages; no verdict may be
generalized beyond its recorded task, agent, model, and grader.

`scripts/eval-outcome --check` validates task structure, fixture references,
held-out coverage, verify-command shape, and artifact-glob shape without
invoking an agent.

The `outcome/2` runner checkpoints each completed trial, including invocation
errors. New records also snapshot the selected task contracts in
`task_contracts`, preserving their requests, commands, and expectations.
External checker implementations still require the corresponding versioned
checkout; the command snapshot alone does not freeze those files.
`EO_MAX_CONSEC` stops after a configured number of consecutive errors
with exit 5 and an `aborted` result containing partial evidence. Completed runs
with invocation errors exit 2; measured task failures alone do not indicate a
runner failure. Zero trials, invalid timeouts, and unknown skills are rejected
before invoking an agent.

Grading requires a successful invocation and every declared verification
command to meet the exit status in the task contract. File scope uses complete
path components. Outer-repository content changes fail grading, including
changes to already-dirty files. This is after-the-fact detection, not an OS
sandbox. Artifact collection rejects symlink escapes and files over its
20,000-character capture limit, so truncated evidence cannot earn a pass.
Treatment workspaces include the complete skill package for local helper use.
Historical results retain their original schema and grading provenance.

## Budget controls

`--tier smoke|standard|release` (12/40/all), `--max-cases`, `--runs`,
`--timeout`, `--dry-run`. CI runs only deterministic checks. Live agent evals
require an explicitly installed and authenticated local CLI, and are never
started by CI. Never unexpectedly spend token budgets.

## Regression process

issue → minimal reproduction → regression case in `evals/regression/`
→ fix → case passes → case stays. The suite gets harder to break over
time.

Run `scripts/test-regressions` for deterministic runner and helper regressions.
These tests use temporary fixture copies and fake local agent commands; they
do not invoke model providers or measure skill effectiveness.
