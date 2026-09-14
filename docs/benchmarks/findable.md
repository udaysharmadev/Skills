# Evidence — findable

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
23); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Technical discoverability without snake oil: verified metadata,
honest structure data, crawlable surfaces (SEO honesty).

## Boundaries

Owns: metadata, semantic structure, robots/sitemaps, structured-data
honesty, previews. Must route elsewhere: copywriting → user/
`frontpage`; perf depth → `hotpath`; README/GitHub → `frontpage`;
private apps → stop. Must not: promise rankings, stuff keywords,
hallucinate structured data, ship invisible meta.

## Method

- Layer A: 5 trigger cases + no-promises case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/findable.md` (FD1–FD5,
  incl. offline failure and stuff-it adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/findable.md` + frozen
  `findable-tasks.json` on the `findable-site` fixture via the
  workspace grader — deterministic greps (unique titles, noindex gone,
  fake stars gone, OG/canonical present, honest sitemap, structure
  untouched where scoped). Verified offline end-to-end (real file
  operations, all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Greps are not crawl truth: real-index behavior stays untested until
  live trials with served URLs.
- One site shape (two static pages); SPA/SSR rendering-model findings
  get scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~115 lines, 1 reference (SEO checklist). Phase 23 added Tool
selection/fallback consolidating the three audit rungs — zero new
always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill findable --agent <agent> --trials 2
scripts/eval-outcome --skill findable --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
