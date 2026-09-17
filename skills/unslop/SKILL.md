---
name: unslop
description: Removes accidental complexity, duplication, dead code, abstraction leakage, naming debt, and generated cruft in small behavior-preserving batches. Use when a working repository is hard to change or contains messy AI-generated code.
---

# unslop: rescue the three-week vibe-coded mess

The user is scared to touch their own project. Your job is to make it
safe to touch again: baseline what currently works, remove what's
accidental, verify every batch. **Never "clean up" by rewriting**,
that's how the last ounce of working behavior dies.

## When NOT to use

- One specific bug → `sleuth`. Slow → `hotpath`. Missing tests by
  design → `proof`.
- The repo is fine and someone just wants activity: say so. No-ops are
  allowed; performative cleanup is slop too.

## Prerequisites

A runnable baseline or the means to build one. Behavior-preservation
claims are only as good as the signal behind them.

## Authority and operating modes

This skill improves internal structure while holding the observed contract
constant. It may make small, reversible source and dependency changes after a
baseline exists. It must ask before changing a public API, persistence schema,
wire format, security policy, product behavior, generated source, or an
unowned deployment artifact. A request to "make it cleaner" is not approval
for any of those changes.

Choose one mode before editing:

| Mode | Use when | Deliverable |
| --- | --- | --- |
| Assess | Scope or safety is unclear | ranked inventory and proposed batches; no edits |
| Detox | Baseline is trustworthy | one or more behavior-preserving, reviewable batches |
| Stabilize | No suitable baseline exists | the smallest reliable signal, then return to assessment |
| Hand off | Finding changes behavior or crosses an owner boundary | evidence packet for the owning skill or team |

Record the chosen mode, baseline command or flow, protected behavior, and
excluded areas. Read the cleanup decision record in
[references/cleanup-protocol.md](references/cleanup-protocol.md) before a
batch with more than one structural change.

## Tool selection/fallback

- Project test runner + build → baseline signal; every batch re-verified
  the same way.
- No tests but runnable: first capture the minimum behavior-preservation
  evidence appropriate to the code being changed.
- Nothing runnable → fix that first (via `sleuth` if broken); no cleanup
  batch ships without a signal: "it still runs" is not one.

## Workflow

### 1. Establish the behavior baseline

Run the test suite, build, and the app's critical flows (browser where
relevant). Record what works **today**, including known quirks that are
load-bearing by accident. Without tests, establish the cheapest trustworthy
signal before touching structure. "It still runs" is not enough evidence.

Inspect repository instructions, package manifests, CI commands, generated-file
markers, recent changes around the target, and the narrow dependency path
before deciding what is dead. Search definitions, imports, dynamic loading,
templates, configuration, build entries, tests, and documentation that names
the candidate. Search absence is evidence only after these paths are relevantly
covered; it is never proof by itself in reflection-heavy or plugin systems.

### 2. Map the mess

Walk the slop catalog (`references/slop-catalog.md`) with evidence,
every finding carries file:line and one line of why it's a problem.
Don't list style preferences; list what costs actual time, tokens or
correctness.

### 3. Rank

| Rank | Meaning |
| --- | --- |
| **Critical** | Breaks behavior or hides bugs (swallowed errors, duplicated schemas drifting apart, dead auth paths) |
| **High leverage** | Removing it makes every future change faster (mega-components, duplicated logic, premature abstractions) |
| **Medium** | Real friction, contained blast radius (unused deps, stale comments, scattered config) |
| **Cosmetic** | Naming, ordering: do last, maybe never |

Rank by evidence, expected recurrence, blast radius, and reversibility. Favor a
small, high-confidence removal over a broad "cleanup" that cannot be explained
or rolled back. Deliberate duplication is acceptable when it isolates a public
boundary, versioned migration, performance path, or independent deployment.
Mark it kept rather than merging it on principle.

### 4. Fix in batches

Small batches, each independently verifiable and revertable:

1. one category or one module per batch: never "the whole cleanup";
2. behavior-preserving only: no feature changes, no "while I'm here"
   improvements smuggled in (note them, do them as their own batch);
3. after each batch: tests → diff review (`referee` discipline) →
   relevant browser check → commit;
4. delete more than you write. Good detox output is usually net-negative
   in lines.

Use this change order unless repository evidence makes another order safer:

1. Delete a proven unreachable artifact or remove a proven unused dependency.
2. Extract one repeated, stable behavior into its existing natural home.
3. Collapse a one-use wrapper only after all callers and error behavior are
   understood.
4. Split a large unit along an existing responsibility seam, preserving public
   imports and lifecycle order.

Do not combine the steps merely because they touch nearby files. A batch should
have one falsifiable claim, such as "the deprecated parser has no reachable
callers and its supported replacement passes the same fixtures." Read
[references/cleanup-protocol.md](references/cleanup-protocol.md) for the
candidate matrix, dynamic-reachability checks, and safe transformation recipes.

### 5. Track and report honestly

Count what changed where it's measurable: dead dependencies removed,
duplication merged (lines), files under size thresholds crossed, tests
preserved through every batch, net lines. Metrics describe the work;
they never become the objective (deleting useful code to improve the
number is the same slop in a clean outfit). Report: what was removed,
what was **kept with a reason** (intentional duplication, performance-
motivated ugliness, compatibility hacks, legacy constraints,
load-bearing weirdness: the catalog's keep-list), what's ranked but
untouched.

### 6. Recover without hiding evidence

If a check fails, stop the batch. Capture the failing command, relevant diff,
and the changed assumption. Revert only the batch under examination, or repair
it if the user has authorized behavior changes; do not weaken a test, suppress
an error, or broaden the cleanup to make the symptom disappear. Re-classify the
candidate as uncertain or load-bearing and report it. A failed cleanup is a
useful result when it prevents a later outage.

If the baseline was already failing, distinguish pre-existing failures from
regressions with the smallest comparison possible. Do not call a batch verified
when that distinction cannot be made.

## Rules

- **The baseline never regresses.** Tests green at every commit; any red
  → revert the batch, not the baseline. **Beware the Refactor Loop of Death:** cleaning up code without a baseline test results in a pristine, syntactically perfect codebase that does absolutely nothing correctly. No tests = no detox.
- **Generated-looking UI slop** (banned patterns, decorative junk) →
  route to `polish`; structural code slop is yours.
- **Unused dependencies**: remove only when nothing imports them
  (verified by search + build, not memory); lockfile updated; install
  still works.
- **Dead code**: deleted, not commented out. Git remembers.
- Commented-out blocks, debug leftovers, empty files, `TODO: fix this`:
  mass grave cleanup is allowed in one cosmetic batch, clearly labeled.
- Preserve source provenance: do not hand-edit generated, vendored, lockfile,
  or migration-history artifacts unless their owning workflow requires it.
- Keep error semantics intact. Consolidating duplicate code must preserve
  validation order, retry behavior, logging, cancellation, and caller-visible
  error shape unless an approved behavior change says otherwise.
- Prefer rename-only moves before semantic reshaping when the seam is unclear.
  A clearer map is a valid intermediate result; forcing the final design is not.

## Quality gates

- Baseline captured (test/build/flow evidence) before batch 1.
- Every finding has file:line evidence; no vibes-based "this smells".
- Every batch: green tests + diff-reviewed + (UI) browser-checked
  before the next.
- Net line delta and per-batch diffs available in the report.
- Zero behavior changes: if any happened accidentally, disclosed and
  reverted.
- Candidate evidence covers plausible indirect use, or the report names the
  unresolved reachability risk and leaves the candidate untouched.
- Every structural batch has a stated invariant and a verification that could
  falsify it; formatting and line-count reductions alone do not qualify.

## Stop conditions

- Critical + high-leverage ranks cleared → report, offer to continue
  into medium/cosmetic, stop.
- Baseline can't be established (app won't run) → fixing *that* becomes
  the first mission, possibly via `sleuth`; no cleanup before a signal
  exists.
- A finding turns out to be load-bearing behavior → keep it, document
  why in the report.
- The next change would require a product, compatibility, or ownership choice
  → stop with alternatives and seek the appropriate decision.
- The remaining inventory is cosmetic or lower confidence than its expected
  benefit → stop; an explicit no-change conclusion is a successful assessment.

## Output contract

Chat: findings table (rank · location · problem · status), batch log
(each: what changed, verification evidence), net line delta, what was
deliberately kept. On request: `docs/reports/detox-<slug>.md` with
provenance header. Each changed batch includes: protected invariant, candidate
evidence, change summary, verification outcome, residual risk, and a clear
verdict of shipped, reverted, deferred, or handed off.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/slop-catalog.md](references/slop-catalog.md) while classifying
findings. Read [references/cleanup-protocol.md](references/cleanup-protocol.md)
for non-trivial reachability analysis, batch design, or a failed verification.
