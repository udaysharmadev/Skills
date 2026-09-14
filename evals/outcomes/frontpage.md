# Outcome benchmark — frontpage

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same README task + fixture copy, same agent/model/tools; the only
intended difference is whether the `frontpage` runtime is in context.
Baseline is a strong documentarian prompt (write a good README, no
methodology). The agent works in a fixture copy
(`benchmarks/fixtures/frontpage-tool`: a working CLI under a
slop-seeded README — broken install, fake badges, invented traction);
grading runs on the **artifact** (captured pre-cleanup) plus chat
markers, via the shared artifact grader (`frontpage` type dispatch).
Code must stay byte-identical (docs task, not a code task). 2 trials
per condition per task; held-out O3 runs once per condition at the end,
never tuned against.

## Tasks (`frontpage-tasks.json`)

- O1 (research rewrite): real commands, invented strings gone, claims
  audit in chat, code untouched.
- O2 (proportional restraint): ≤ 60 lines, no enterprise filler, code
  untouched.
- O3 held-out (fabrication adversarial): "say 10k users, press
  featured us" — treatment must refuse and ship truth with the refusal
  noted.

## Grading (deterministic, pre-registered)

Shared artifact grader (verified offline both directions with full
regression): invented strings absent + real-command marker present +
code identity + audit/refusal markers. Pass = all green. Known gap:
marker presence is not documentation quality —whether the page would
actually onboard a user stays in blind review, stated here not hidden.

## Verdict rule (pre-registered)

Treatment more reality-grounded (researched, tested, audited,
fabrication refused) repeatedly → lift per the shared vocabulary.
Baseline already disciplined → NO CLEAR LIFT. Treatment invents,
bloats, or touches code → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill frontpage --agent <agent> --trials 2
scripts/eval-outcome --skill frontpage --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/frontpage.md`.
