---
name: pilot
description: Implements an approved plan one coherent slice at a time with fresh inspection, risk-appropriate verification, diff review, and clean handoff state. Use when the user asks to execute a multi-step implementation plan or continue an existing build.
---

# pilot: fly the plan

You turn an approved plan into working code without ever accumulating more
than one unverified slice of change. The loop is the skill: inspect →
implement → fast checks → test → inspect diff → continue. Skipping the
verification steps to "move fast" is how a plan becomes a mess.

## When NOT to use

- No plan exists and the task is small and obvious → just implement it.
- No plan exists and the task is serious → `masterplan` first.
- The user is still deciding what to build → `hotseat` / `distill`.

## Prerequisites

A plan with ordered slices (`docs/plans/<slug>.md` or equivalent) and its
verification commands. If the repo defines no test/lint/build commands,
establish a baseline signal first (run what exists, note the state): you
cannot verify changes against silence.

## Authority and slice contract

Pilot executes an approved plan inside its stated scope. It may make necessary
local adjustments that preserve architecture, acceptance criteria, and action
class. Stop for a user decision when a change alters product behavior, public
contract, data risk, security posture, external effect, cost, or plan boundary.

Before each medium or high-risk slice, record outcome, confirmed files,
invariants, verification, recovery path, and dirty-tree overlap. Read
[references/execution-protocol.md](references/execution-protocol.md) for a
deviation, failed check, migration, or plan/reality mismatch.

## The loop (per slice, in order)

### 1. Inspect and classify

Read the slice's files fresh: they may have changed since planning or
since earlier slices. Restate in one line: what this slice delivers, how
you'll verify it. Then classify the slice's **risk**: low (pure
addition, no shared state), medium (touches existing behavior), high
(data, auth, money, schema, public API, infra). Risk sets the
verification floor: high-risk slices get the full gate treatment
early, not just at the end: and whether you checkpoint a **rollback
point** (commit tag or noted revert path) before starting. Checkpointing
never touches the user's uncommitted work: if the tree is dirty, use a
stash, a branch, or a noted revert path: never absorb, overwrite, or
"clean up" user changes as a side effect. If reality
contradicts the plan's assumptions → stop and report (below), don't
improvise.

Inspect current diff, repository instructions, relevant callers, config, and
existing tests before implementation. Planning evidence ages: a file changed
since planning is new input, not a minor inconvenience.

### 2. Implement

The smallest correct version of the slice. Follow repo conventions over
personal taste. **No drive-by refactors**: anything outside the slice's
file list either goes in the completion report as a follow-up or, if
load-bearing, is called out before proceeding.

Maintain one coherent intent per slice. Classify unplanned work as local
deviation, discovery need, or scope/architecture change. Only a local deviation
may proceed; record reason and changed verification immediately.

### 3. Fast checks

Lint, typecheck, build: whatever the repo defines. Must be green before
moving on. Red checks do not get deferred ("I'll fix it later").

### 4. Test at the useful boundary

Choose the cheapest test that can fail for the behavior being changed. For a
new bug or invariant, a failing test before the fix is strong evidence. A test
may legitimately pass before implementation when it characterizes existing
behavior, protects a refactor, validates generated integration code, or covers
configuration. State what failure it would catch instead of manufacturing red.

Run related existing tests. A slice is not implemented until its relevant
checks pass or the unavailable evidence is named precisely.

Slice tests prove the slice; the lasting regression strategy belongs to
`proof`: write the tests this slice needs, not the suite the project
wishes it had.

### 5. Inspect the diff

`git diff` against the slice's definition: everything planned present,
nothing extra snuck in, no debug leftovers, no secrets. Strictly review for
**hallucinated APIs or tool spoofing** (calling endpoints that don't exist
or passing fabricated arguments just to satisfy a prompt). Fix what fails
this review before continuing.

### 6. Continue

Check the slice off in the plan file. If implementation deviated from
the plan (different file, extra step, dropped step), **record the
deviation in the plan file** next to the slice: silent drift is how
plans become fiction. Keep a running **decision log** in the plan file:
each fix attempt, workaround, and judgment call as one line (what was
tried → what happened → what was decided). The log is what makes the
next session: or `sleuth`, or the reviewer: understand why the code
looks the way it does. Next slice. If a fix attempt failed twice on the
same failure → stop and report the failure mode; a third blind attempt
is how agents thrash.

### Recovery and replan boundary

On failure, preserve failing command, diff, and assumption before changing
direction. Compare to baseline when practical. A retry changes hypothesis or
diagnostic; two equivalent retries are one attempt. Return to `masterplan` only
when evidence changes architecture, acceptance criteria, public behavior, data
model, security posture, or deployment order. Otherwise record local deviation
and continue after verification.

## Parallelism

Independent slices (the plan marks them) may go to subagents: one slice
per subagent, prompt = the slice + conventions + verify commands + "report
diff and test results". Conflicting slices run sequentially. No subagent
support → sequential; the loop is identical.

## Blocked or contradictory reality

Stop and report when: a planned file doesn't exist as described, tests
that should pass can't (including failures that pre-date your slice,
verify against the baseline, don't inherit someone else's breakage as
your own or ignore it), or the slice as written can't deliver its stated
outcome. Apply the materiality test before routing back: if the fix
stays within the slice's files and the plan's architecture, record the
deviation and continue: only architecture or scope changes go back to
`masterplan` for replanning. Ping-ponging every surprise back to
planning is how execution stalls. Silent scope improvisation is the
failure mode this exists to prevent.

## The completion gate

Before any "implementation complete" claim, run the gate checklist in
`references/completion-gate.md` (read it every time: it maps change type
to required gates). Minimum for everything: a `proof`-grade full test
pass + a `referee` review (fresh-context subagent when available;
disciplined self-review otherwise). Where relevant: `roadtest` for UI
slices, `harden` for auth/data changes, `hotpath` for hot paths. Every
gate result is reported as **verified** (with evidence) or **unverified**
(with reason): the word "unverified" is mandatory, not optional polish.

## Tool selection / fallback

- Use project-native build, test, lint, migration, and browser commands.
- Delegate only independent slices when delegation is available and authorized.
- If a verification capability is missing, finish safe in-scope work and report the exact unverified boundary.
- Use narrowest deterministic check that can falsify slice claim, then broader
  gates when risk or repository policy requires them.

## Quality gates

- Every slice's verify step actually ran this session; none assumed.
- Diff inspected before every continue; no unchecked slice marked done.
- Completion report contains zero claims without evidence.
- The plan file's checkboxes reflect reality.
- Every deviation identifies whether it preserved plan or required replan.
- A blocked or unverified slice is never checked off as done.

## Stop conditions

- All slices done, gates green → completion report, stop.
- Two failed fix attempts on one slice → report and stop.
- Plan/reality contradiction → report and route back to `masterplan`.
- User interrupts → finish or safely revert the current slice, then stop.
- Recovery overwrites user work, deletes data, rewrites history, or needs new
  external authority → stop and apply relevant gate rather than force complete.

## Output contract

Completion report:

```text
── build report ───────────────────────────
slices:   3/3 done (plan docs/plans/dark-mode.md)
verified: tests 42 pass · build green · diff-reviewed per slice
          roadtest: unverified (no browser tooling this session)
gate:     referee review: 1 minor finding (naming), non-blocking
followups: theme audit for 3rd-party embeds (out of scope)
```

Evidence or it didn't happen: every green claim names the command that
proved it.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/completion-gate.md](references/completion-gate.md) before a
completion claim. Read [references/execution-protocol.md](references/execution-protocol.md)
for slice records, deviations, retries, and plan/reality mismatches.
