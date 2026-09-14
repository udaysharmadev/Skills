# Evidence — runway

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
26); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Deploys that happened, proven on the live URL — or honestly reported
as not-deployed (flight honesty).

## Boundaries

Owns: preflight, platform-detected deploys, live verification,
rollback paths. Must route elsewhere: readiness verdicts → `cleared`;
scale/infra choices → `headroom`. Must not: fabricate deploys, skip
to prod, print secrets, invent canary theater.

## Method

- Layer A: 5 trigger cases + preflight-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/runway.md` (RW1–RW5,
  incl. no-access failure and say-it's-live adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/runway.md` + frozen
  `runway-tasks.json` on the `runway-app` fixture — file identity (no
  deploys, no created files) plus honesty markers and fabrication
  phrases. Verified offline on all gates, including catching a real
  harness gap (below).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## The harness gap offline testing caught

The workspace grader ignored `must_not` contaminants (only the fact
grader honored them), so fabrication phrases were ungradable — and
file-identity checks alone missed *created* files (a DEPLOYED.md
"passed" a no-deploy task; fixed with an entry-count gate). Both
fixed same-phase, backward-compatible: no prior pilot task declares
`must_not`, and the count gate is per-task. Full regression clean.

## Limitations (known before first run)

- Markers are not deploy skill: real fingerprint verification stays
  untested until platform trials with credentials.
- One platform shape (static + vercel.json); other targets get
  scenario coverage only until fixtures grow.

## Context audit

SKILL.md ~150 lines, 1 reference (platforms). Phase 26 added
Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill runway --agent <agent> --trials 2
scripts/eval-outcome --skill runway --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
