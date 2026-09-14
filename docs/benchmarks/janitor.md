# Evidence — janitor

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
21); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Git-state honesty: quoted commands, proposals-not-commits, destruction
gated on an explicit yes (state discipline).

## Boundaries

Owns: hygiene audits, convention-matched messages, branch/tag/ignore
cleanup proposals. Must route elsewhere: code slop → `unslop`; docs →
`frontpage`; code-security impact → `harden`. Must not: force-push,
rewrite public history, delete branches, or commit unasked — ever
without recorded authorization.

## Method

- Layer A: 5 trigger cases + report-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/janitor.md` (JN1–JN5,
  incl. no-gh failure and squash-and-push adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/janitor.md` + frozen
  `janitor-tasks.json` on the `janitor-mess` fixture (deterministic
  `setup.sh` recipe — nested `.git` cannot be committed; the script
  `cd`s to its own directory first): HEAD pinned to `.baseline-sha`,
  status shape, staged-file, and branch-survival checks. Verified
  offline on all gates — including catching and fixing two real
  harness bugs (below).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## The two harness bugs offline testing caught

1. Bare dotfile tokens (`.env`) counted as hallucinated paths, so the
   required finding about the committed `.env` false-failed. Fixed:
   dot-leading tokens without `/` are names, not path claims.
2. `grade_spelunk` silently ignored `verify` commands, so git-state
   gates never ran (a committer "passed" audit tasks). Fixed: the fact
   grader now enforces verify exits when declared. Both fixes are
   backward-compatible — prior tasks declare no verify fields and no
   dotfile markers (regression re-run clean).

## Limitations (known before first run)

- State checks are not audit quality: claim grounding and triage
  honesty stay in blind review.
- Trials must run `setup.sh` from the fixture directory (the request
  says so); skipped setup fails verify by construction.
- `gh`/remote behavior untested until a networked trial environment.

## Context audit

SKILL.md ~120 lines, 1 reference (hygiene checklists). Phase 21 added
Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill janitor --agent <agent> --trials 2
scripts/eval-outcome --skill janitor --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
