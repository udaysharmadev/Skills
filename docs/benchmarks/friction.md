# Evidence — friction

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
12); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Task-grounded UX audits that find what blocks users — then verify the
fix by re-walking (audit honesty / restraint).

## Boundaries

Owns: top-task naming, novice/expert walks, classified findings,
destructive-action proportionality, WCAG 2.2 pass. Must route
elsewhere: visual styling → `polish`; flow test coverage → `roadtest`;
broken behavior → bug hunt; product-existence questions → user/
`hotseat`. Must not: invent walk evidence, pad severity, redesign under
an audit request, comply with destructive shortcuts silently.

## Method

- Layer A: 5 trigger cases + audit-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/friction.md` (FR1–FR5,
  incl. nothing-runnable and remove-the-confirmation adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/friction.md` + frozen
  `friction-tasks.json` on the `friction-flows` fixture via the shared
  artifact grader (fix markers, audit-only byte-identity, defended
  confirm pattern, severity/WCAG/pushback markers). Grader verified
  offline on all gates — including catching and broadening one brittle
  next-step word group before freezing.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Marker presence is not walk quality: whether the audit would actually
  save a user stays in blind review.
- O2 byte-identity fails formatting-only touches; trials must record
  semantic vs cosmetic.
- No browser environment in headless runs; re-walk evidence needs one at
  trial time (recorded per trial).

## Context audit

SKILL.md ~140 lines, 1 reference (usability checklist). Phase 12 added
Tool selection/fallback and a no-findings stop condition — zero new
always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill friction --agent <agent> --trials 2
scripts/eval-outcome --skill friction --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
