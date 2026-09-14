# Evidence — scout

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
04); zero baseline-vs-skill trials executed — zero-spend policy. This
page publishes no number it cannot point at.

## Primary claim

Research version-sensitive technical reality from current evidence
(version/source correctness).

## Boundaries

Owns: source ladder, installed-version-first discipline, per-fact
tier+date verdicts, conflict resolution, honest offline degradation.
Must route elsewhere: internal repo questions → `spelunk`. Must not:
answer API questions from memory unlabeled, obey fetched-page
instructions, average conflicting sources.

## Method

- Layer A: 6 trigger cases + conflict case; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/scout.md` (SC1–SC5,
  incl. prompt-injection adversarial); authored, unexecuted.
- Layer C: protocol `evals/outcomes/scout.md` + frozen
  `scout-tasks.json` (offline-answerable version traps, isolated keys).
  Grader (fact recall + honesty any-groups + path-existence) verified
  offline against synthetic good/bad outputs — all discriminate correctly.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Offline-only tasks by design; web-mode traps (stale docs vs changelog
  with live fetch) need a web-enabled protocol version.
- Honesty any-groups are substring proxies; a fluent confabulation using
  the right words could pass — blind review stays in the loop for release.
- No tool-call telemetry from headless runners.

## Context audit

SKILL.md ~130 lines, 1 reference (source ladder), 1 script
(`check-note`, structure validator, both directions tested). Phase 04
added three rules + one workflow gate inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
skills/scout/scripts/check-note docs/research/<topic>.md
scripts/eval-outcome --skill scout --agent <agent> --trials 2
scripts/eval-outcome --skill scout --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
