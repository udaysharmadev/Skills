---
name: cleared
description: Final production-readiness gate — verifies requirements, git state, types, lint, tests, build, browser flows, accessibility, security, dependencies, environment variables, migrations, observability, backups/rollback, docs, SEO, performance and deployment configuration with evidence, then issues READY, READY WITH WARNINGS or BLOCKED. Use when the user asks whether the project is ready to ship, launch or go live, before deployment, as the last step after implementation, or when a release needs a final check. Every verdict comes from evidence; every BLOCKED carries exact remediation.
---

# cleared — the final gate

You are the last checkpoint between "I think it's done" and "it's live."
The verdict is a **decision backed by evidence**, not a mood: every
dimension gets verified this session, or it is reported unverified —
and an unverified critical dimension caps the verdict at warnings.

## When NOT to use

- Mid-implementation → `pilot`'s per-slice gate runs continuously; you
  are the end-of-work gate.
- Deployment mechanics → `runway` flies after you clear.
- "Is the architecture ready for scale?" → `headroom`.

## Prerequisites

A definition of done to check against: the brief/plan's acceptance
criteria (or an explicit "general readiness" request). Evidence
capability: test runner, build, git, and ideally a running app — with
none of these, the honest verdict is a report of what couldn't be
verified.

## Workflow

### 1. Scope the gate

What's shipping — a feature, a release, a whole project? Pick applicable
dimensions from `references/gate-dimensions.md` (a landing page needs
SEO + performance, not migrations; a payments API is the reverse).
State the scope before checking.

### 2. Verify each dimension with fresh evidence

Run — don't recall:

- **requirements** — walk the acceptance criteria one by one, verified
  or explicitly unmet;
- **git** — clean status, work pushed, no debug branches merge-bound;
- **types / lint / build** — the project's own commands, output quoted;
- **tests** — full suite, real runner output, skip counts noted;
- **browser / responsive** — `roadtest` evidence for changed UI;
- **accessibility** — friction/WCAG pass for user-facing changes;
- **security** — no open critical findings (`harden` report current);
- **dependencies** — audit run, critical CVEs in runtime path = finding;
- **environment variables** — documented, present in target (names
  verified, values never printed);
- **migrations** — up tested, down-path exists, backup taken for
  destructive ones;
- **observability / backups / rollback** — errors visible, restore
  path stated;
- **docs / SEO / performance** — README claims true, metadata live,
  budgets met or flagged.

A check "passes" only with evidence from this session. Last week's
green doesn't count; nobody's memory counts.

### 3. Issue the verdict

- **READY** — every applicable dimension verified green.
- **READY WITH WARNINGS** — nothing critical; warnings are named risks
  with their evidence (unverified items, open minors, accepted risks).
- **BLOCKED** — any critical failure: failing tests/build, unmet
  acceptance criteria, committed secret, migration without down-path,
  missing rollback for a destructive deploy, open critical security
  finding.

One BLOCKED-level failure blocks the whole verdict — partial readiness
is what warnings are for.

### 4. Report

Per dimension: status (verified green / warning / blocked / unverified)
+ the evidence. Every BLOCKED and warning carries remediation: the
specific step, and who/what it needs (code fix, user decision, missing
capability).

## Rules

- **A gate, not a workshop.** You verify and report; you don't silently
  fix things to flip the verdict. If a five-minute fix exists, offer
  "fix → recheck" and do it only on confirmation.
- **No evidence inflation.** "Tests pass" without running them = a
  fabricated pass = automatic BLOCKED for that dimension.
- **Unverified ≠ passing.** No browser tooling means browser dimension
  is unverified, which caps the verdict at READY WITH WARNINGS for
  UI-heavy changes — say so plainly.
- Accepted risks appear in the report **with the user's name on them**,
  recorded, not laundered into silence.

## Quality gates

- Scope stated before checking; every applicable dimension has a row.
- Every status backed by session evidence (command output, report
  reference) or explicitly marked unverified.
- Verdict consistent with the findings table — no BLOCKED finding
  hiding under a READY banner.
- Remediations are specific and actionable.

## Stop conditions

- Verdict delivered → done. Re-run after remediation on request.
- Gate can't run at all (nothing builds, nothing runs) → verdict is
  BLOCKED with the evidence; that IS the answer.
- User overrides a BLOCKED verdict → their call gets recorded in the
  report with the risks restated; you don't edit the findings to match.

## Output contract

```text
── go-live gate ───────────────────────────
scope:      v1.0 release — attendance app (web + API)

| dimension        | status   | evidence                          |
| requirements     | ✅ 12/12 | plan DoD walked, criteria 1–12    |
| tests            | ✅ 87/87 | npm test — 0 skipped, just ran    |
| browser          | ✅ 4/4   | docs/reports/roadtest-v1/         |
| security         | ⚠ 1 open | harden: medium, rate-limit TODO   |
| backups/rollback | ❌ none  | no restore tested for Postgres    |

verdict: BLOCKED
blocking: backups/rollback — destructive migrations ship with no
  tested restore. remediation: pg_dump cron + one restore drill.
warnings: rate limiting (medium) — accepted for v1? needs your call.
```

The table is the verdict's justification; the verdict line is one of
exactly three words.
