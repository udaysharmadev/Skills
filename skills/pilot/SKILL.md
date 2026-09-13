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

### 1. Inspect

Read the slice's files fresh — they may have changed since planning or
since earlier slices. Restate in one line: what this slice delivers, how
you'll verify it. If reality contradicts the plan's assumptions → stop and
report (below), don't improvise.

### 2. Implement

The smallest correct version of the slice. Follow repo conventions over
personal taste. **No drive-by refactors** — anything outside the slice's
file list either goes in the completion report as a follow-up or, if
load-bearing, is called out before proceeding.

### 3. Fast checks

Lint, typecheck, build — whatever the repo defines. Must be green before
moving on. Red checks do not get deferred ("I'll fix it later").

### 4. Test

Run the slice's new tests plus related existing tests (module-level, not
necessarily the whole suite — full suite runs at the gate). A slice is not
"implemented" until its tests pass.

### 5. Inspect the diff

`git diff` against the slice's definition: everything planned present,
nothing extra snuck in, no debug leftovers, no secrets. Fix what fails
this review before continuing.

### 6. Continue

Check the slice off in the plan file. Next slice. If a fix attempt failed
twice on the same failure → stop and report the failure mode; a third
blind attempt is how agents thrash.

## Parallelism

Independent slices (the plan marks them) may go to subagents — one slice
per subagent, prompt = the slice + conventions + verify commands + "report
diff and test results". Conflicting slices run sequentially. No subagent
support → sequential; the loop is identical.

## Blocked or contradictory reality

Stop and report when: a planned file doesn't exist as described, tests
that should pass can't, or the slice as written can't deliver its stated
outcome. Route back to `masterplan` for replanning the affected slices.
Silent scope improvisation is the failure mode this exists to prevent.

## The completion gate

Before any "implementation complete" claim, run the gate checklist in
`references/completion-gate.md` (read it every time — it maps change type
to required gates). Minimum for everything: `proof`-style full test pass +
a review pass (`referee` when shipped; fresh-context subagent review if
available; disciplined self-review otherwise). Where relevant: browser
verification for UI slices, security review for auth/data changes,
performance checks for hot paths. Every gate result is reported as
**verified** (with evidence) or **unverified** (with reason) — the word
"unverified" is mandatory, not optional polish.

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
