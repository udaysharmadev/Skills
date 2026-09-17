---
name: cleared
description: Issues an evidence-backed READY, READY WITH WARNINGS, or BLOCKED verdict using only release dimensions relevant to the artifact and its risks. Use before shipping, merging, publishing, or declaring a software task complete.
---

# cleared: the final gate

You are the last checkpoint between "I think it's done" and "it's live."
The verdict is a **decision backed by evidence**, not a mood: every
dimension gets verified this session, or it is reported unverified,
and an unverified critical dimension caps the verdict at warnings.

## When NOT to use

- Mid-implementation → `pilot`'s per-slice gate runs continuously; you
  are the end-of-work gate.
- Deployment mechanics → `runway` flies after you clear.
- "Is the architecture ready for scale?" → `headroom`.

## Prerequisites

A definition of done to check against: the brief/plan's acceptance
criteria (or an explicit "general readiness" request). Evidence
capability: test runner, build, git, and ideally a running app: with
none of these, the honest verdict is a report of what couldn't be
verified.

Identify artifact version/commit, audience, target environment, release owner,
rollback owner, criticality, change classes (data/auth/money/public API/UI),
and any explicit acceptance of risk. A release gate cannot infer who may accept
an unresolved risk or whether a warning is acceptable.

## Gate authority and evidence discipline

- This skill audits and reports. It does not merge, publish, deploy, bypass a
  branch rule, accept risk, rewrite history, or silently fix a finding.
- Fresh means evidence collected against the exact candidate commit and target
  configuration during this gate, or a cited immutable artifact demonstrably
  bound to that candidate. A prior green run is context, not current proof.
- Separate **verified**, **warning**, **blocked**, **unverified**, and
  **not applicable**. "Not applicable" needs a scope reason, not convenience.
- Preserve raw command/artifact references and summarize their relevant result;
  do not copy secrets, tokens, private endpoints, or customer data into the
  report.
- Risk acceptance must name the accountable human/role, specific risk, expiry or
  re-review trigger, and compensating control. It changes an eligible warning,
  never a hard safety or contractual blocker without explicit policy authority.
- A clean working tree is not evidence that the candidate is pushed, reviewed,
  reproducible, or deployable. Check each claim independently.

## Gate plan and applicability decision

Before running commands, make a compact plan:

| Question | Required answer |
| --- | --- |
| Candidate | commit/tag/artifact and target environment |
| Scope | feature/release/repository; included and excluded surfaces |
| Definition of done | source and individually testable criteria |
| Change risk | data, auth, money, API, UI, dependency, deployment, docs |
| Applicable dimensions | selected from gate-dimensions with rationale |
| Evidence plan | command/artifact, owner, freshness, expected pass condition |
| Escalation | what blocks, who decides warning/risk acceptance |

Apply dimensions proportionately but conservatively. A changed schema makes
migration and recovery relevant; a public UI makes browser/accessibility and
metadata relevant; a library release makes package artifact, compatibility, and
consumer-facing docs relevant. If the claim cannot be scoped safely, include it
as unverified rather than excluding it.

## Tool selection/fallback

- Project runner/build/git → fresh session evidence per dimension;
  outputs quoted, never recalled.
- Sibling reports available (roadtest bundle, harden findings, proof
  suite) → cite as evidence with paths; stale reports count as
  unverified, not green.
- Nothing runnable → the gate still runs: every dimension marked
  unverified-or-blocked with the missing capability named; hallucinated
  passes are automatic BLOCKEDs.

## Workflow

### 1. Scope the gate

What's shipping: a feature, a release, a whole project? Pick applicable
dimensions from `references/gate-dimensions.md` (a landing page needs
SEO + performance, not migrations; a payments API is the reverse).
State the scope before checking.

### 2. Verify each dimension with fresh evidence

Each dimension row carries: **status** (verified green / warning /
blocked / unverified), **evidence**, **risk if unresolved**, and
**owner/action**: who fixes what by when. "Not checked" is not pass;
it is unverified and caps the verdict. Run: don't recall:

- **requirements**: walk the acceptance criteria one by one, verified
  or explicitly unmet;
- **git**: clean status, work pushed, no debug branches merge-bound;
- **types / lint / build**: the project's own commands, output quoted;
- **tests**: full suite, real runner output, skip counts noted;
- **browser / responsive**: `roadtest` evidence for changed UI;
- **accessibility**: friction/WCAG pass for user-facing changes;
- **security**: no open critical findings (`harden` report current);
- **dependencies**: audit run, critical CVEs in runtime path = finding;
- **environment variables**: documented, present in target (names
  verified, values never printed);
- **migrations**: up tested, down-path exists, backup taken for
  destructive ones;
- **observability / backups / rollback**: errors visible, restore
  path stated;
- **docs / SEO / performance**: README claims true, metadata live,
  budgets met or flagged.

A check "passes" only with evidence from this session. Last week's
green doesn't count; nobody's memory counts.

### 3. Issue the verdict

- **READY**: every applicable dimension verified green.
- **READY WITH WARNINGS**: nothing critical; warnings are named risks
  with their evidence (unverified items, open minors, accepted risks).
- **BLOCKED**: any critical failure: failing tests/build, unmet
  acceptance criteria, committed secret, migration without down-path,
  missing rollback for a destructive deploy, open critical security
  finding.

One BLOCKED-level failure blocks the whole verdict: partial readiness
is what warnings are for.

### 4. Report

Per dimension: status (verified green / warning / blocked / unverified)
+ the evidence. Every BLOCKED and warning carries remediation: the
specific step, and who/what it needs (code fix, user decision, missing
capability).

### 5. Reconcile and close

Cross-check the verdict against the evidence table and report scope. Confirm
that all acceptance criteria have a matching row, findings reference an
artifact/command, warning owners exist, and no RELEASE/READY label is stronger
than the weakest applicable critical dimension. Keep a rerun separate: record
the changed candidate/evidence and whether it resolves, changes, or leaves each
prior finding.

## Failure handling and edge cases

- **Commands cannot run:** capture the command, failure, environment limitation,
  and affected dimensions. Mark unverified or blocked based on release risk;
  never replace it with static confidence.
- **Conflicting evidence:** preserve both sources, verify candidate identity and
  timestamps, then seek the narrowest authoritative check. Do not average a
  passing local test and failing CI into a warning.
- **Partial release:** scope only the shipped artifact but include every shared
  dependency, migration, feature flag, and rollback surface that it can affect.
- **Emergency release:** use the same evidence table, explicitly identify
  deferred checks and authority, then schedule a time-bounded follow-up. Speed
  changes evidence availability, not reality.
- **Third-party dependency or provider unavailable:** record provider-bound
  verification as unverified and evaluate whether that dependency is critical
  to the release path.
- **Risk owner absent:** do not convert the finding to accepted risk. Leave it
  warning or blocked according to the dimension weight.

## Anti-Patterns (The Banned List)

- **The Workshop Trap (Silently Fixing)**: a gate is a gate, not a workshop. Do not silently fix failing tests or lint errors to flip the verdict. If a five-minute fix exists, offer "fix → recheck" and do it only on confirmation.
- **Evidence Inflation (Hallucinated Passes)**: saying "Tests pass" because the code looks good, without actually running `npm test`. A fabricated pass = automatic BLOCKED for that dimension. Unverified ≠ passing.
- **Laundering Risk**: omitting accepted risks or warnings from the final report to make it look cleaner. Accepted risks must appear in the report with the user's name on them, recorded explicitly.

## Quality gates

- Scope stated before checking; every applicable dimension has a row.
- Every status backed by session evidence (command output, report
  reference) or explicitly marked unverified.
- Verdict consistent with the findings table: no BLOCKED finding
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
scope:      v1.0 release: attendance app (web + API)

| dimension        | status   | evidence                          |
| requirements     | ✅ 12/12 | plan DoD walked, criteria 1–12    |
| tests            | ✅ 87/87 | npm test: 0 skipped, just ran    |
| browser          | ✅ 4/4   | docs/reports/roadtest-v1/         |
| security         | ⚠ 1 open | harden: medium, rate-limit TODO   |
| backups/rollback | ❌ none  | no restore tested for Postgres    |

verdict: BLOCKED
blocking: backups/rollback: destructive migrations ship with no
  tested restore. remediation: pg_dump cron + one restore drill.
warnings: rate limiting (medium): accepted for v1? needs your call.
```

The table is the verdict's justification; the verdict line is one of
exactly three words.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
