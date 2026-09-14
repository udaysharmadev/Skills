# Outcome benchmark — sleuth

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same bug + fixture copy, same agent/model/tools; the only intended
difference is whether the `sleuth` runtime is in context. Baseline is a
strong debugger prompt (fix the bug, no methodology). The agent works
in a fixture copy (`benchmarks/fixtures/sleuth-cache`: reads go stale
after writes — `set` never invalidates); grading runs on the
**workspace** (behavior-check exits recorded pre-cleanup, scope
containment) plus cause-chain markers, via the `pilot`-type grader. 2
trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`sleuth-tasks.json`)

- O1 (full chain): reproduce → hypotheses → chain → smallest fix +
  regression test. Freshness AND cache-still-used checks must pass
  (bypass is not a fix).
- O2 (diagnose-only restraint): chain reported, repo byte-identical.
- O3 held-out (ship-fastest adversarial): "wrap it, bypass it, retry
  it" — treatment must root-cause (or explicit provisional), not
  suppress.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
runs): check exits as expected + scope kept + chain markers present.
The two behavior checks separate true fixes from bypasses (fresh but
uncached) and from untouched code (cached but stale). Pass = all green.
Known gap: markers are not reasoning quality — whether the chain is
real stays in blind review, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more cause-honest (chain evidenced, hypotheses killed on
data, suppression refused) repeatedly → lift per the shared vocabulary.
Baseline already disciplined → NO CLEAR LIFT. Treatment guess-fixes,
suppresses, or pads scope → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill sleuth --agent <agent> --trials 2
scripts/eval-outcome --skill sleuth --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/sleuth.md`.
