# Evidence — spelunk

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
03); zero baseline-vs-skill trials executed — zero-spend policy: no
paid-model runs without an explicit trial budget. This page publishes no
number it cannot point at.

## Primary claim

Build the smallest accurate mental model of an unfamiliar repository
(fact accuracy per unit of reading).

## Boundaries

Owns: mode selection (quick/deep/teach/risk-map), discovery order,
epistemic labels, budget discipline. Must route elsewhere: settled
single-file questions (just read it), fresh memory (read it instead),
empty repos (say so). Must not: read blindly, invent commands, record
secret values, cite generated/vendor code without verification.

## Method

- Layer A: 6 trigger cases + risk-map case; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/spelunk.md` (SP1–SP5);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/spelunk.md` + frozen
  `spelunk-tasks.json` (seeded fixtures, answer keys isolated).
  Harness support implemented and offline-tested: fixture workspaces +
  fact-recall/contaminant/hallucinated-path grader. Grader edge cases
  (missing fact, contaminant, invented path) verified to fail correctly
  with diagnostics — no agent involved.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Headless runners expose no tool-call/file/byte telemetry: accuracy is
  graded first; cost stays honestly labeled from duration/output size.
- Path-existence check covers extension-bearing mentions only.
- Held-out O3 shares the ts-dashboard fixture with O1 (unseen questions;
  no tuning occurs anywhere, so leakage is N/A — stated, not hidden).

## Context audit

SKILL.md ~140 lines, 1 reference (discovery checklist), 1 script
(`inventory`: manifests, ext distribution, largest files, debt, test
ratio, generated/vendor candidates, scoped churn). Phase 03 added the
trace-one-path-early step, precise-symbols-before-grep rung, and
commit/dirty provenance — all inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill spelunk --agent <agent> --trials 2
scripts/eval-outcome --skill spelunk --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
