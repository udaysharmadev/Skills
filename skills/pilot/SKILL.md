---
name: pilot
description: Executes an approved implementation plan slice by slice with a strict inspect-implement-verify loop. Use when a plan exists (from masterplan or equivalent), the user approves building it, or asks to implement a feature in controlled increments. Runs fast checks after every slice, inspects diffs before continuing, delegates independent slices to subagents when available, and refuses to declare completion while required verification gates remain unverified.
---

# pilot — fly the plan

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
establish a baseline signal first (run what exists, note the state) — you
cannot verify changes against silence.

## The loop (per slice, in order)

### 1. Inspect and classify

Read the slice's files fresh — they may have changed since planning or
since earlier slices. Restate in one line: what this slice delivers, how
you'll verify it. Then classify the slice's **risk**: low (pure
addition, no shared state), medium (touches existing behavior), high
(data, auth, money, schema, public API, infra). Risk sets the
verification floor — high-risk slices get the full gate treatment
early, not just at the end — and whether you checkpoint a **rollback
point** (commit tag or noted revert path) before starting. Checkpointing
never touches the user's uncommitted work: if the tree is dirty, use a
stash, a branch, or a noted revert path — never absorb, overwrite, or
"clean up" user changes as a side effect. If reality
contradicts the plan's assumptions → stop and report (below), don't
improvise.

### 2. Implement

The smallest correct version of the slice. Follow repo conventions over
personal taste. **No drive-by refactors** — anything outside the slice's
file list either goes in the completion report as a follow-up or, if
load-bearing, is called out before proceeding.

### 3. Fast checks

Lint, typecheck, build — whatever the repo defines. Must be green before
moving on. Red checks do not get deferred ("I'll fix it later").

### 4. Test (Test-Driven Execution)

Enforce strict **Test-Driven Execution (TDE)**. If adding new logic:
1. Write the test first.
2. Run it and verify it **FAILS** (red). A test that passes before implementation is a hallucinated/vacuous test.
3. Write the implementation code.
4. Run the test and verify it **PASSES** (green).

Run related existing tests (module-level). A slice is not "implemented" until its tests pass correctly.

Slice tests prove the slice; the lasting regression strategy belongs to
`proof` — write the tests this slice needs, not the suite the project
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
deviation in the plan file** next to the slice — silent drift is how
plans become fiction. Keep a running **decision log** in the plan file:
each fix attempt, workaround, and judgment call as one line (what was
tried → what happened → what was decided). The log is what makes the
next session — or `sleuth`, or the reviewer — understand why the code
looks the way it does. Next slice. If a fix attempt failed twice on the
same failure → stop and report the failure mode; a third blind attempt
is how agents thrash.

## Parallelism

Independent slices (the plan marks them) may go to subagents — one slice
per subagent, prompt = the slice + conventions + verify commands + "report
diff and test results". Conflicting slices run sequentially. No subagent
support → sequential; the loop is identical.

## Blocked or contradictory reality

Stop and report when: a planned file doesn't exist as described, tests
that should pass can't (including failures that pre-date your slice —
verify against the baseline, don't inherit someone else's breakage as
your own or ignore it), or the slice as written can't deliver its stated
outcome. Apply the materiality test before routing back: if the fix
stays within the slice's files and the plan's architecture, record the
deviation and continue — only architecture or scope changes go back to
`masterplan` for replanning. Ping-ponging every surprise back to
planning is how execution stalls. Silent scope improvisation is the
failure mode this exists to prevent.

## The completion gate

Before any "implementation complete" claim, run the gate checklist in
`references/completion-gate.md` (read it every time — it maps change type
to required gates). Minimum for everything: a `proof`-grade full test
pass + a `referee` review (fresh-context subagent when available;
disciplined self-review otherwise). Where relevant: `roadtest` for UI
slices, `harden` for auth/data changes, `hotpath` for hot paths. Every
gate result is reported as **verified** (with evidence) or **unverified**
(with reason) — the word "unverified" is mandatory, not optional polish.

## Quality gates

- Every slice's verify step actually ran this session; none assumed.
- Diff inspected before every continue; no unchecked slice marked done.
- Completion report contains zero claims without evidence.
- The plan file's checkboxes reflect reality.

## Stop conditions

- All slices done, gates green → completion report, stop.
- Two failed fix attempts on one slice → report and stop.
- Plan/reality contradiction → report and route back to `masterplan`.
- User interrupts → finish or safely revert the current slice, then stop.

## Output contract

Completion report:

```text
── build report ───────────────────────────
slices:   3/3 done (plan docs/plans/dark-mode.md)
verified: tests 42 pass · build green · diff-reviewed per slice
          roadtest: unverified (no browser tooling this session)
gate:     referee review — 1 minor finding (naming), non-blocking
followups: theme audit for 3rd-party embeds (out of scope)
```

Evidence or it didn't happen — every green claim names the command that
proved it.
