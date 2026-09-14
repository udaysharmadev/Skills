---
name: masterplan
description: Produces a serious implementation plan from an agreed brief or a clear goal — vertical slices, architectural decisions, exact files, tests, rollout, rollback and a definition of done. Use when the user asks to plan an implementation, break a feature or migration into steps, or after distill has produced a task brief and before code gets written. Inspects the real files first and never plans changes to files it has not verified exist.
---

# masterplan — decide how, before touching code

`distill` defines **what**. You define **how** — grounded in the actual
repository, sliced into increments that each leave the project demonstrably
better. A plan that speculates about files it never opened is fiction.

## When NOT to use

- No agreed brief and the request is vague → `distill` first.
- The change is a one-file, obviously-scoped fix → just implement it.
- The user wants a product critique → `hotseat`.

## Prerequisites

A brief (from `distill`, on disk or in chat) or an equivalent clear goal.
Repository access — plans must be grounded in real files. A `spelunk`
quick-map of the affected area helps; run a mini version yourself if none
exists (manifests, the modules the brief names, test commands).

## Two planning depths

- **Lightweight** (single-slice-or-two changes): current state, one or
  two slices with files+verify, risks in a sentence. Skip the ceremony;
  the definition of done still applies.
- **Full** (everything below): for multi-slice, multi-system, or
  data-touching work.

Choose by blast radius, not by request volume — a "small" change to the
auth path plans fully.

## Workflow

### 1. Load the goal

From the brief: goal, scope, non-goals, acceptance criteria, verification
requirements, assumptions. If anything load-bearing is missing, resolve it
(one batched question round, max 5) before planning — never plan past a
known unknown silently.

### 2. Inspect current reality

Open and read the files the plan will touch. Every file path that appears
in the final plan must be one you saw. For each: current state, what
changes, what it connects to. Where a path can't be confirmed, the plan
says "confirm during slice N" — it does not invent a path.

### 3. Record invariants and architectural decisions

Invariants first — the properties that must remain true throughout
(existing API contract, data guarantees, performance characteristics);
every slice is checked against them. Then decisions the plan commits to (library choices, data model changes, API
shape, patterns), each as: decision, alternatives considered, why, and
what would make this decision wrong. Version-sensitive technology facts
come from `scout` research or are marked unverified — a plan built on
stale API memory fails during implementation.

### 4. Slice vertically with explicit sequencing

Cut the work into **vertical slices** — each one crosses the stack as
needed (data → API → UI) and ends testable on its own. Sequencing is
dependency-aware, not ordinal: mark every slice **must precede** (its
output is another slice's input), **can parallelize** (independent —
and state the files that would conflict), or **can postpone** (valuable
but not needed for the goal — postponed slices keep the plan honest and
the scope cut visible). Rules:

- 5–12 slices for serious work; a 30-step plan means the slices are fake.
- Each slice states: what it delivers, files touched (real paths),
  tests added, how to verify it works right now.
- Order by the dependency graph between slices; mark which slices are
  parallelizable and what they conflict over.
- Migrations, API contract changes and auth changes get their own slice —
  never smuggled inside a UI slice.

### 5. Safety nets

For the whole plan: rollout order, rollback (how to undo each slice —
"revert commit" is a valid answer only if it's actually true), risks with
mitigations, checkpoints where the user should look before continuing, and
observability (what logs/metrics/errors will exist to debug it later).

### 6. Definition of done

Copy the acceptance criteria from the brief and attach the proof for each:
which command, which check, which manual verification. A plan with no
executable definition of done is a wishlist.

## Anti-bloat rules

- No restating the brief — reference it.
- No microsteps ("create file", "add import"). A step is a coherent,
  testable improvement or it gets merged into its neighbor.
- No speculative infrastructure for scale the project doesn't have.
- Target ≤ 150 lines for the plan document.

## Quality gates

- 100% of file paths verified to exist during step 2.
- Every slice independently verifiable (tests/commands named).
- Rollback exists for every destructive or hard-to-reverse step;
  migrations state their down-path.
- Decisions section covers every choice a reviewer would ask "why?" about.
- Acceptance criteria from the brief all appear in the definition of done.

## Stop conditions

- Plan written and confirmed → hand off to `pilot` for slice-by-slice
  execution, then stop.
- Reality contradicts the brief (the named module doesn't exist, the data
  model can't support the goal) → stop, report the contradiction, route
  back to `distill`.
- User changes scope mid-planning → replan the affected slices, don't
  patch silently.

## Output contract

`docs/plans/<slug>.md` (provenance header `<!-- generated by masterplan on
YYYY-MM-DD -->`), sections per `references/plan-template.md`:

```markdown
# Plan: <title>
## Current state → Target state
## Decisions
## Slices (ordered, with dependency notes)
## Rollout, rollback, risks, checkpoints
## Definition of done
```

Chat summary: slice list (one line each), the 2–3 decisions that matter,
total risk in one sentence.
