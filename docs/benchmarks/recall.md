# Evidence — recall

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
27); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Memory that serves next session: supersessions not duplicates, secrets
never stored, budgets kept, validator green (memory honesty).

## Boundaries

Owns: four-file writes, session deltas, budgeted catch-ups,
compaction. Must route elsewhere: ephemeral trivia → git; derivable
facts → re-derive; approach questions → conversation. Must not: store
secrets, duplicate decisions, dump transcripts, write into a mess.

## Method

- Layer A: 6 trigger cases + surgical-write case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/recall.md` (RC1–RC5,
  incl. polluted-memory failure and remember-this-key adversarial);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/recall.md` + frozen
  `recall-tasks.json` on the `recall-notes` fixture — the skill's own
  `check-memory` runs as a verify command, plus supersession/secret/
  TTL/budget gates and confirmation markers. Verified offline
  end-to-end (real file operations, all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Milestone

Recall was the last skill without an outcome protocol: all 28 skills
now have one (`concierge` MIXED and `hotseat` PROVEN LIFT executed;
the rest UNVERIFIED, zero trials). The v1 campaign's per-skill build
is complete; what remains is the proof phase (funded trials), not
more scaffolding.

## Limitations (known before first run)

- Structural health is not memory quality: whether the delta serves
  next session stays in blind review.
- One memory shape (four files + one brief); compaction-at-scale and
  multi-project memories get scenario coverage only until fixtures
  grow.

## Context audit

SKILL.md ~140 lines, 1 reference (file formats), 1 script
(check-memory). Phase 27 added Prerequisites and Tool
selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill recall --agent <agent> --trials 2
scripts/eval-outcome --skill recall --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
