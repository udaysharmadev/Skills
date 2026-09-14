---
name: referee
description: Independent code and diff review along two axes — did the code solve the stated intent, and is the engineering quality sound. Use when the user asks to review code, a diff, a PR or a change, before merging, or as the completion gate after implementation work. Produces only actionable findings ranked blocker, major, minor, nit — nits never block. Prefers a fresh-context reviewer when subagents are available and always discloses which kind of review ran.
---

# referee — review like you didn't write it

Two axes, in order: **Intent** — did this actually solve the requested
problem, completely, without extras? Then **quality** — is it correct,
maintainable, safe, proportionate? A beautiful implementation of the
wrong thing fails. Independence is the product: you review what the diff
does, not what its author intended it to do.

## Prerequisites

The complete diff plus the written acceptance criteria (brief, plan, or
issue) it claims to satisfy. Criteria missing or diff sliced → ask for
them first; reviewing intent against memory is author-bias with extra
steps.

## Tool selection/fallback

- Subagent support + non-trivial change → fresh-context review (diff +
  criteria only, no author commentary); disclose the mode.
- No subagents, or trivial diff → structured self-review per
  `references/finding-format.md` (complete diff, criteria re-read,
  hunt what you'd flag in someone else's code); disclose plus its weakness.
- Neither time nor context for the full pass → decline to skim: state
  the minimum needed (split, brief, criteria) rather than fake depth.

## When NOT to use

- Mid-slice debugging → `sleuth` owns the live loop; review comes when
  the diff exists.
- Architecture decisions → `headroom`; test strategy → `proof`.
- The author is asking questions ("is this approach reasonable?") —
  that's a conversation, not a review; answer it.

## Review modes (disclose which ran)

**Fresh-context (preferred):** a subagent receives the diff + the
brief/plan/acceptance criteria — nothing else. No author commentary, no
"here's why I did it". If subagents are available and the change is
non-trivial, use this; say `review type: fresh-context`.

**Structured self-review:** no subagent available. The author reviewing
own work is attached to it, so the checklist in
`references/finding-format.md` runs mechanically: wait for the complete
diff, review against the written acceptance criteria (not memory of
them), and hunt specifically for what you'd flag in someone else's code.
Say `review type: self-review` — the disclosure is mandatory.

## Workflow

### 1. Frame

What was requested (brief/plan/issue), what the diff claims to do, scope
(size, files, risk areas). If the diff claims things it doesn't contain
or contains things never requested — that's already a finding.

### 2. Intent pass

Against the acceptance criteria, one by one: solved, partially solved,
or missing? Anything in the diff that serves no criterion (scope creep,
drive-by refactors, dead code introduced)? The intent pass produces
blockers faster than any quality check.

### 3. Quality pass

Walk the diff: correctness (logic, edge cases, error paths, concurrency),
tests (exist? right boundary? would they catch a revert?), security
(input handling, authz on new surfaces), performance (obvious only —
hotpath owns measurement), conventions (project style wins over taste),
complexity (could this be simpler without losing anything?).

### 4. Findings

Only actionable items — each with location, problem, why it matters, and
a fix direction (see format reference). No "consider...", no style
opinions with a rule behind them already, no praise padding. Findings
you can't act on get deleted, not softened.

### 5. Verdict

- **approve** — nothing above minor;
- **approve with findings** — majors exist but are safe to fix forward;
- **request changes** — any blocker.

Nits never affect the verdict. State which mode ran, the diff scope
covered, and anything explicitly not reviewed ("docs/" skipped).

## Anti-Patterns (The Banned List)

- **Context Starvation (Isolation Review)** — reviewing a file in a vacuum without checking its callers. If a function signature changes, you must use codebase search tools to verify that all upstream callers were updated. A review that misses broken downstream systems is a failed review.
- **LGTM Syndrome (Rubber-Stamping)** — approving AI-generated code just because it is syntactically clean and has no linter errors. AI code often looks perfect but solves the wrong problem. The Intent Pass must break this illusion of safety.
- **Nit-Picking / AI Pedantry** — filling a review with 15 stylistic opinions that don't affect correctness or performance. Keep the noise down; nits are collapsed.

## Quality gates

- Every finding: file:line location + why it matters + fix direction.
- Intent checked criterion-by-criterion against the actual written
  criteria.
- Severity honest — a preference is a nit, not a major; severity
  inflation is how reviews get ignored.
- Review type disclosed; self-review explicitly names its weakness.
- Zero non-actionable findings.

## Stop conditions

- Verdict delivered → done.
- Diff unreviewably large or context-free → say what's needed (split,
  brief, running app), don't skim and pretend.
- Findings reveal the change solves the wrong problem → verdict
  `request changes` with the intent finding; route back to
  `distill`/`masterplan`.

## Output contract

```text
review type: fresh-context | self-review
scope: 14 files, +312/−87 — auth middleware + tests

verdict: request changes

| Sev | Location | Finding | Fix direction |
| --- | --- | --- | --- |
| blocker | auth.ts:41 | role check happens after query — data leaks for !owner | check ownership in the query WHERE |
| major | auth.test.ts | no test for revoked-token path | add API-level test |
| nit | naming.ts:8 | `d` → `durationMs` | rename |

intent: 4/5 criteria met — "session revocation" missing (see major)
not reviewed: public/ assets
```

Findings table is the whole report; no essay, no restating the diff.
