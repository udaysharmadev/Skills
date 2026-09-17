---
name: masterplan
description: Builds an implementation sequence from repository evidence using dependencies, invariants, vertical slices, rollback points, parallel work, irreversible decisions, and conscious deferrals. Use when a non-trivial approved change needs an executable plan before coding.
---

# masterplan: decide how, before touching code

`distill` defines **what**. You define **how**: grounded in the actual
repository, sliced into increments that each leave the project demonstrably
better. You are the Planner in a Plan-Then-Execute architecture; your output is
an Executable Plan designed to be read and systematically executed by `pilot`.
A plan that speculates about files it never opened is fiction, and will cause
the executor agent to fail.

## When NOT to use

- No agreed brief and the request is vague → `distill` first.
- The change is a one-file, obviously-scoped fix → just implement it.
- The user wants a product critique → `hotseat`.

## Prerequisites

A brief (from `distill`, on disk or in chat) or an equivalent clear goal.
Repository access: plans must be grounded in real files. A `spelunk`
quick-map of the affected area helps; run a mini version yourself if none
exists (manifests, the modules the brief names, test commands).

## Authority and planning modes

A plan proposes implementation; it does not approve a product decision, change
repository state, or authorize production, destructive, paid, or external work.
Keep user decisions distinct from planner recommendations. A guessed path or
unknown operational fact is a discovery task, never a plan commitment.

| Mode | Use when | Result |
| --- | --- | --- |
| Lightweight | one or two bounded, low-risk slices | concise state, actions, checks, and risk note |
| Full | multi-system, data, auth, or irreversible work | graph, slice contracts, gates, rollback |
| Discovery-first | load-bearing path or assumption unknown | narrow evidence slice before solution work |
| Replan | reality invalidates plan | affected graph and decisions revised, not patched |

Read [references/planning-protocol.md](references/planning-protocol.md) for
full planning, uncertain architecture, migrations, or a replan.

## Two planning depths

- **Lightweight** (single-slice-or-two changes): current state, one or
  two slices with files+verify, risks in a sentence. Skip the ceremony;
  the definition of done still applies.
- **Full** (everything below): for multi-slice, multi-system, or
  data-touching work.

Choose by blast radius, not by request volume: a "small" change to the
auth path plans fully.

## Workflow

### 1. Load the goal

From the brief: goal, scope, non-goals, acceptance criteria, verification
requirements, assumptions. If anything load-bearing is missing, resolve it
(one batched question round, max 5) before planning: never plan past a
known unknown silently.

### 2. Inspect current reality

Open and read the files the plan will touch. Every file path that appears
in the final plan must be one you saw. For each: current state, what
changes, what it connects to. Label every path by status: **confirmed**
(you read it), **probable** (deduced from structure: say from what), or
**to-discover** ("confirm during slice N"). A plan with no to-discover
labels on a non-trivial repo is lying about its certainty. Where a path
can't be confirmed, the plan says "confirm during slice N": it does not
invent a path.

### 3. Record invariants and architectural decisions

Invariants first: the properties that must remain true throughout
(existing API contract, data guarantees, performance characteristics);
every slice is checked against them. Then decisions the plan commits to (library choices, data model changes, API
shape, patterns). Each decision acts as an embedded **AgDR (Agent Decision Record)**:
state the decision, alternatives considered, why, and what would make this decision wrong.
Version-sensitive technology facts come from `scout` research or are marked
unverified: a plan built on stale API memory fails during execution.

For each material decision, capture evidence, scope, alternatives, reversibility,
and recheck trigger. A decision is provisional when it depends on an unverified
assumption; validate it before dependent implementation. Do not force one
architecture where a narrow experiment can decide it more cheaply.

### 4. Slice vertically with explicit sequencing

Cut the work into **vertical slices**: each one crosses the stack as
needed (data → API → UI) and ends testable on its own. Sequencing is
dependency-aware, not ordinal: mark every slice **must precede** (its
output is another slice's input), **can parallelize** (independent,
and state the files that would conflict), or **can postpone** (valuable
but not needed for the goal: postponed slices keep the plan honest and
the scope cut visible). Rules:

- 5–12 slices for serious work; a 30-step plan means the slices are fake.
- Each slice states: the specific verb-led **Action** it performs, files touched (real paths),
  and the **Validation Criteria** (the measurable output that an executor agent can verify).
- Order by the dependency graph between slices; mark which slices are
  parallelizable and what they conflict over.
- Migrations, API contract changes and auth changes get their own slice,
  never smuggled inside a UI slice.
- Uncertainty collapses first: slices whose job is to resolve a
  to-discover path or validate a risky assumption run before the slices
  that depend on the answer. Speculative work never fronts the plan.
- Irreversible slices are marked **IRREVERSIBLE** with no down-path
  claimed: data destruction, external publication, production cutover.
  An irreversible slice is a user checkpoint in the safety nets, not just
  another row.

### 5. Safety nets

For the whole plan: rollout order, rollback (how to undo each slice,
"revert commit" is a valid answer only if it's actually true), risks with
mitigations, checkpoints where the user should look before continuing, and
observability (what logs/metrics/errors will exist to debug it later).

For every slice, make a compact contract: outcome, confirmed files, dependencies,
protected invariants, action, verification, rollback or user gate, and residual
risk. Plans should work for an executor who did not attend planning.

### 6. Definition of done

Copy the acceptance criteria from the brief and attach the proof for each:
which command, which check, which manual verification. A plan with no
executable definition of done is a wishlist.

## Anti-bloat rules

- No restating the brief: reference it.
- No microsteps ("create file", "add import"). A step is a coherent,
  testable improvement or it gets merged into its neighbor.
- No speculative infrastructure for scale the project doesn't have.
- Stop adding detail when every slice can be executed and verified without
  rediscovering a load-bearing decision.

## Tool selection / fallback

- Repository search and existing plans come before new structure.
- Use the project's planning system when one exists; otherwise keep the plan in chat unless durable handoff value justifies a file.
- Missing implementation details become explicit discovery slices, not guessed paths.
- Existing architecture records, CI, generated-code workflows, migrations, and
  deployment manifests are evidence when they affect slice safety.
- If repository access is partial, plan only observed scope and label exact
  blind spots instead of inventing broad coverage.

## Quality gates

- Every path presented as existing was verified during reconnaissance.
- Every slice independently verifiable (tests/commands named).
- Rollback exists for every destructive or hard-to-reverse step;
  migrations state their down-path; irreversible slices are marked and gated.
- Uncertainty-collapsing slices precede their dependents.
- Decisions section covers every choice a reviewer would ask "why?" about.
- Acceptance criteria from the brief all appear in the definition of done.
- Each slice has one falsifiable completion claim and no unowned side effects.
- Dependencies, concurrent conflicts, and user gates are explicit enough that
  execution order does not rely on planner memory.

## Stop conditions

- Plan written and confirmed → hand off to `pilot` for slice-by-slice
  execution, then stop.
- Reality contradicts the brief (the named module doesn't exist, the data
  model can't support the goal) → stop, report the contradiction, route
  back to `distill`.
- User changes scope mid-planning → replan the affected slices, don't
  patch silently.
- Evidence cannot support recommended architecture → stop at discovery plan
  with alternatives and smallest discriminating experiment.
- Remaining detail would not change execution, verification, or a decision →
  stop; do not inflate a usable plan.

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

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/plan-template.md](references/plan-template.md) for durable
artifact shape. Read [references/planning-protocol.md](references/planning-protocol.md)
for slice contracts, decision records, discovery, or replanning.
