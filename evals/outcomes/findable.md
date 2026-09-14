# Outcome benchmark — findable

Status: **UNVERIFIED** — protocol + tasks frozen 2026-09-14. Zero agent
trials executed (zero-spend policy, no Codex). Numbers appear only after
live runs with full provenance.

## Design

Same site + fixture copy, same agent/model/tools; the only intended
difference is whether the `findable` runtime is in context. Baseline is
a strong SEO prompt (improve rankings, no methodology). The agent works
in a fixture copy (`benchmarks/fixtures/findable-site`: duplicate
titles, staging noindex, fake review stars, blocked robots, lying
sitemap, double headings); grading runs on the **workspace**
(deterministic greps recorded pre-cleanup, scope containment) plus
report markers, via the `pilot`-type grader. Static checks need no
browser, so this protocol grades unusually close to the real skill. 2
trials per condition per task; held-out O3 runs once per condition at
the end, never tuned against.

## Tasks (`findable-tasks.json`)

- O1 (full fix): unique titles, noindex gone, fake stars gone, OG +
  canonicals present, sitemap honest, robots referencing it.
- O2 (metadata-only restraint): metadata fixed, double-h1 structure
  provably untouched.
- O3 held-out (stuffing adversarial): "repeat 'best notes app'
  everywhere" — treatment must refuse and stay technical (phrase count
  ≤ 2).

## Grading (deterministic, pre-registered)

Workspace grader (`pilot` type, verified offline end-to-end with real
file operations; no harness change): grep exits as expected + scope
kept + report markers. Pass = all green. Known gap: greps are not
crawl truth — real-index behavior stays untested until live trials,
stated here not hidden.

## Verdict rule (pre-registered)

Treatment more evidence-honest (buckets separated, fixes verified,
snake oil refused) repeatedly → lift per the shared vocabulary.
Baseline already disciplined → NO CLEAR LIFT. Treatment stuffs,
promises rankings, or hallucinates structured data → REGRESSION.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill findable --agent <agent> --trials 2
scripts/eval-outcome --skill findable --agent <agent> --trials 1 --heldout
```

Raw traces: `evals/results/` (gitignored). Curated verdict:
`docs/benchmarks/findable.md`.
