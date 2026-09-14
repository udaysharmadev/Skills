# Evidence — handsfree

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (v1
campaign); zero baseline-vs-skill trials executed. This page is the
pattern all 28 per-skill evidence pages will follow — it publishes no
number it cannot point at.

## Primary claim

Safe reversible work completes without needless interruption; necessary
gates still fire.

## Boundaries

Owns: model-created ceremony suppression, safe-default inference,
checkpoint/budget discipline, host-block reporting. Must route elsewhere:
release risk → `cleared`; deployment → `runway`; history surgery →
`janitor`; security findings → `harden`. Must not: widen host approvals,
skip ASK ONCE/BLOCKED gates, absorb user dirty state.

## Method

- Layer A (activation): 9 trigger cases in `evals/trigger/cases.md`;
  routing smoke results exist at bundle level, handsfree-specific
  standard-tier runs pending.
- Layer B (workflow): 5 scenarios in
  `evals/workflow/scenarios/handsfree.md` (HF1–HF5); authored, unexecuted.
- Layer C (outcome): protocol in `evals/outcomes/handsfree.md` (O1–O2);
  unexecuted.

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations

- Host behavior varies by mode and version; results pin the exact
  `toolPermission` / approval-mode observed.
- Interruption-rate baselines differ per model; lift is always relative
  to the same model without the skill, never cross-model.
- `plan`/`strict` read-only environments cap what autonomy can demonstrate.

## Context audit

SKILL.md ~150 lines, 2 references (antigravity, decision-policy), 0
scripts (justified: classification is judgment, not computation).
Frontmatter description carries the trigger signal; depth loads on demand.

## Reproduce

```bash
scripts/validate-skills            # structural contract
scripts/eval-trigger --suite all   # Layer A (when harness lands for handsfree tier)
scripts/eval-workflow --scenario HF1 --agent codex
```
