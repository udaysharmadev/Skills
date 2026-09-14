# Outcome benchmark — blueprint

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same documentation task + fixture repo, same agent/model/tools; the only
intended difference is whether the `blueprint` runtime is in context.
Baseline is a strong documentarian prompt (real files only, no invented
infra). The agent works in a fixture copy and writes `.mmd` sources under
`docs/architecture/`; grading runs on the **artifacts** (captured
pre-cleanup) plus the skill's own `validate-mermaid` exits. 2 trials per
condition per task; held-out O3 runs once per condition at the end, never
tuned against.

## Tasks (`blueprint-tasks.json`)

- O1 (ts-dashboard): component + order request-flow diagrams, validated,
  nodes real, ≤ 5 diagrams.
- O2 (py-notes-api): restraint — ≤ 2 diagrams for one app + SQLite.
- O3 held-out (ts-dashboard): failure-path view (validation error,
  network error, swallowed errors) with real nodes.

## Grading (deterministic, pre-registered)

Deliverable grader (`blueprint` type): ≥ 1 `.mmd` produced; bundled
validator exits 0 on all of them; every path-like node label resolves to
a real fixture file; no forbidden-infra words (fixtures own no infra —
any Kafka/CDN/replica fails); diagram count within budget; required
content markers present. Verified offline: grounded set passes;
Kafka/CDN set, 7-diagram set, and invalid-syntax set each fail on the
right gate; empty set fails as missing.

## Verdict rule (pre-registered)

Treatment more truthful/restrained repeatedly → lift per the shared
vocabulary. Baseline already honest → NO CLEAR LIFT. Treatment invents
infra or decorates → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill blueprint --agent <agent> --trials 2
scripts/eval-outcome --skill blueprint --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/blueprint.md`.
