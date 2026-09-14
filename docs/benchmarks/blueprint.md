# Evidence — blueprint

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
09); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Produce truthful architecture views that answer real questions (diagram
truth / usefulness).

## Boundaries

Owns: question-driven view selection, code-traced nodes, validated
sources, navigable deliverable. Must route elsewhere: symbol location →
`spelunk` quick; scale decisions → `headroom` (documents the outcome);
single README sketch → inline Mermaid, no deliverable. Must not: invent
infrastructure, mix proposed with observed, ship empty placeholders,
claim rendering without rendering.

## Method

- Layer A: 5 trigger cases + proposed-marking case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/blueprint.md` (BP1–BP5,
  incl. no-render-toolchain and make-it-look-enterprise adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/blueprint.md` + frozen
  `blueprint-tasks.json` with artifact grading (validator exits, node
  resolution, infra-word scan, diagram budget). Grader verified offline
  on all five gates.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Static validation ≠ rendering; render-once evidence needs a
  mermaid-cli environment at trial time (recorded per trial).
- Infra-word scan is fixture-relative (works because fixtures own no
  infra); real repos need an allow-list drawn from their manifests.
- Usefulness (did the diagram answer the question) stays in blind review.

## Context audit

SKILL.md ~125 lines, 1 reference (question→diagram menu + patterns), 1
script (validator, both directions tested), 1 asset (HTML template).
Phase 09 added deliverable provenance + Decisions section inside existing
structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill blueprint --agent <agent> --trials 2
scripts/eval-outcome --skill blueprint --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
