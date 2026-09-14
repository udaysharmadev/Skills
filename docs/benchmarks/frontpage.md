# Evidence — frontpage

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
22); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

READMEs from verified reality: researched code, executed snippets,
audited claims, fabrication refused (documentation honesty).

## Boundaries

Owns: research, structure choice, tested snippets, claims audits,
proportional READMEs. Must route elsewhere: messy code → `unslop`;
architecture docs → `blueprint`; repo hygiene → `janitor`. Must not:
invent numbers/badges/users, bloat small tools, touch code on a docs
task, narrate diffs instead of intent.

## Method

- Layer A: 5 trigger cases + short-and-honest case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/frontpage.md`
  (FP1–FP5, incl. nothing-installable and say-10k-users adversarial);
  authored, unexecuted. Signature F1–F3 remain as cross-checks.
- Layer C: protocol `evals/outcomes/frontpage.md` + frozen
  `frontpage-tasks.json` on the `frontpage-tool` fixture via the
  shared artifact grader — invented strings gone, real commands
  present, code byte-identical, audit/refusal markers. Verified
  offline on all gates, including catching a real harness gap (below).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## The harness gap offline testing caught

The shared artifact grader (`grade_polish`, also serving polish /
friction / ditto tasks) never enforced `verify`-command exits — a
code-touching run "passed" docs tasks. Fixed alongside this phase
(same pattern as the Phase 21 fact-grader fix); all prior artifact
tasks declare no `verify` fields, so the fix is backward-compatible
(full regression re-run clean).

## Limitations (known before first run)

- Markers are not documentation quality: whether the page would
  onboard a user stays in blind review.
- One tool shape (tiny CLI); bundle/complex-project READMEs get
  scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~135 lines, 1 reference (README blueprint). Phase 22 added
Tool selection/fallback consolidating the four verification rungs —
zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill frontpage --agent <agent> --trials 2
scripts/eval-outcome --skill frontpage --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
