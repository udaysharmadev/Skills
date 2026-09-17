# Completion gate: what must be verified before "done"

The gate maps the **type of change** to the **required verification**.
Report every applicable row as verified (with evidence) or unverified
(with reason). Any unverified required gate means the report says
"complete with unverified items", never a bare "complete".

## Gate matrix

| Change touches | Required gates |
| --- | --- |
| Anything | full test suite · build · lint/types · diff self-review |
| UI / user-visible behavior | browser walk of the changed flows (`roadtest`) · responsive check · console clean |
| Auth, sessions, permissions, payments, PII | security review pass (`harden`, scoped to the changed surface) |
| Data model / migrations | migration up **and** down tested · data-preservation check on a copy |
| Public API contract | consumer check: existing callers updated or compatible · versioning/deprecation noted |
| Performance-sensitive path | before/after benchmark with numbers, or an explicit "not measured" |
| Background jobs / queues | idempotency check · retry behavior exercised |
| Docs / README claims | claims match reality (commands actually run) |

## Evidence format

One line per gate:

```text
verified:   npm test: 42 passing, 0 skipped (run 2026-09-14 14:02)
unverified: browser flow: no browser automation available this session
```

## Self-review without subagents

When no fresh-context reviewer is available, do a disciplined second pass
instead of skipping review:

1. Wait until the full diff exists (don't review slice-by-slice only).
2. Read the diff **as the reviewer**, against the plan's acceptance
   criteria: list what you'd flag.
3. Fix blockers/majors. Nits go in the report as findings, un-fixed is
   fine.
4. Say in the report that review was self-review (fresh-context review
   unavailable): honesty about the review's weakness is part of the gate.

## Non-negotiables

- "Tests pass" without having run them = fabrication. Never.
- **Scope containment:** Never modify a test simply to make it pass (unless the test was fundamentally broken). Do not touch files outside the planned slice without explicit authorization (this is "silent scope improvisation" and causes severe agent drift).
- An unverified gate is reported in those words, with the reason.
- Gate results never get bulked up to look complete ("everything works"
  is not evidence; command output is).
