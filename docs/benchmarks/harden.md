# Evidence — harden

Status: **UNVERIFIED** (2026-09-14). Runtime depth pass complete (Phase
19); zero baseline-vs-skill trials executed — zero-spend policy, no
Codex. This page publishes no number it cannot point at.

## Primary claim

Evidence-backed hardening: threat model first, exploits closed and
re-run, theater refused (attack-surface reduction honesty).

## Boundaries

Owns: threat modeling, static/dependency/config/authz review, safe
adversarial verification, fixes with retests. Must route elsewhere:
quality → `referee`; scale resilience → `headroom`; product decisions
→ user. Must not: claim unhackable, exploit destructively, test without
authorization, print secrets, theater.

## Method

- Layer A: 5 trigger cases + exploitability-only case; bundle smoke (C-005).
- Layer B: 5 scenarios `evals/workflow/scenarios/harden.md` (HN1–HN5,
  incl. blind-spot failure and WAF-it adversarial); authored,
  unexecuted.
- Layer C: protocol `evals/outcomes/harden.md` + frozen
  `harden-tasks.json` on the `harden-notes` fixture (in-memory sqlite:
  injectable lookup, hardcoded secret, unenforced ownership) via the
  workspace grader — plain AND obfuscated injection separate real fixes
  from regex theater. Verified offline end-to-end (real exploit runs,
  all gates).

## Raw results

None yet. Pointers will land here with agent/version/model/commit/
fixture-hash/timestamp per trial, failures preserved.

## Limitations (known before first run)

- Exploit closure is not audit quality: threat-model depth and triage
  honesty stay in blind review.
- One app shape (notes CRUD); supply-chain, headers, and GenAI-surface
  findings get scenario coverage only until fixtures grow.
- Safe verification only: destructive/unauthorized testing is refused
  by the skill and untestable by the protocol alike.

## Context audit

SKILL.md ~130 lines, 1 reference (attack-surface checklist). Phase 19
added Prerequisites and Tool selection/fallback — zero new always-on cost.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill harden --agent <agent> --trials 2
scripts/eval-outcome --skill harden --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```
