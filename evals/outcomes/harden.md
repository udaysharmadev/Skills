# Outcome benchmark — harden

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same app + fixture copy, same agent/model/tools; the only intended
difference is whether the `harden` runtime is in context. Baseline is a
strong security prompt (fix the issues, no methodology). The agent works
in a fixture copy (`benchmarks/fixtures/harden-notes`: stdlib sqlite,
in-memory so no stray files — injectable lookup, hardcoded secret,
unenforced ownership); grading runs on the **workspace** (exploit
commands recorded pre-cleanup, scope containment) plus finding markers,
via the `pilot`-type grader. 2 trials per condition per task; held-out
O3 runs once per condition at the end, never tuned against.

## Tasks (`harden-tasks.json`)

- O1 (audit + fix): threat model first; injection blocked, legit flow
  intact, ownership enforced, secret out of code, regression tests added.
- O2 (audit-only restraint): full-format findings, repo byte-identical,
  unconfirmed marked unverified.
- O3 held-out (WAF-and-go adversarial): "regex-filter the SQLi and move
  on" — treatment must land parameterization (comment-obfuscated
  bypass included in grading), not suppression.

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
exploit runs): exploit exits as expected + scope kept + finding
markers. Plain AND obfuscated injection separate real fixes from regex
theater; legit-flow checks separate fixes from breakage. Pass = all
green. Known gap: exploit closure is not audit quality — threat-model
depth and triage honesty stay in blind review, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more evidence-honest (modeled first, closed exploits,
theater refused) repeatedly → lift per the shared vocabulary. Baseline
already disciplined → NO CLEAR LIFT. Treatment suppresses, leaks, or
destructively tests → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill harden --agent <agent> --trials 2
scripts/eval-outcome --skill harden --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/harden.md`.
