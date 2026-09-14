---
name: unslop
description: Rescues messy, AI-generated or vibe-coded repositories — removes duplicated logic, dead code, premature abstractions, swallowed errors and generated-looking slop incrementally and safely. Use when the user says the codebase is a mess, scary to touch, or full of AI slop, asks to clean up, detox or de-slop a repo, or when a project has clearly accreted accidental complexity. Establishes a behavior baseline first, then fixes in small verified batches — never a giant unverified rewrite.
---

# unslop — rescue the three-week vibe-coded mess

The user is scared to touch their own project. Your job is to make it
safe to touch again: baseline what currently works, remove what's
accidental, verify every batch. **Never "clean up" by rewriting** —
that's how the last ounce of working behavior dies.

## When NOT to use

- One specific bug → `sleuth`. Slow → `hotpath`. Missing tests by
  design → `proof`.
- The repo is fine and someone just wants activity — say so. No-ops are
  allowed; performative cleanup is slop too.

## Prerequisites

A runnable baseline or the means to build one. Behavior-preservation
claims are only as good as the signal behind them.

## Workflow

### 1. Establish the behavior baseline

Run the test suite, build, and the app's critical flows (browser where
relevant). Record what works **today**, including known quirks that are
load-bearing by accident. No tests? Batch 0 is creating a smoke baseline
(a handful of `proof`-style API-level tests around the money paths) —
you cannot detox without a signal, and "it still runs" is not one.

### 2. Map the mess

Walk the slop catalog (`references/slop-catalog.md`) with evidence —
every finding carries file:line and one line of why it's a problem.
Don't list style preferences; list what costs actual time, tokens or
correctness.

### 3. Rank

| Rank | Meaning |
| --- | --- |
| **Critical** | Breaks behavior or hides bugs (swallowed errors, duplicated schemas drifting apart, dead auth paths) |
| **High leverage** | Removing it makes every future change faster (mega-components, duplicated logic, premature abstractions) |
| **Medium** | Real friction, contained blast radius (unused deps, stale comments, scattered config) |
| **Cosmetic** | Naming, ordering — do last, maybe never |

### 4. Fix in batches

Small batches, each independently verifiable and revertable:

1. one category or one module per batch — never "the whole cleanup";
2. behavior-preserving only: no feature changes, no "while I'm here"
   improvements smuggled in (note them, do them as their own batch);
3. after each batch: tests → diff review (`referee` discipline) →
   relevant browser check → commit;
4. delete more than you write. Good detox output is usually net-negative
   in lines.

### 5. Track and report honestly

Count what changed where it's measurable — dead dependencies removed,
duplication merged (lines), files under size thresholds crossed, tests
preserved through every batch, net lines. Metrics describe the work;
they never become the objective (deleting useful code to improve the
number is the same slop in a clean outfit). Report: what was removed,
what was **kept with a reason** (intentional duplication, performance-
motivated ugliness, compatibility hacks, legacy constraints,
load-bearing weirdness — the catalog's keep-list), what's ranked but
untouched.

## Rules

- **The baseline never regresses.** Tests green at every commit; any red
  → revert the batch, not the baseline.
- **Generated-looking UI slop** (banned patterns, decorative junk) →
  route to `polish`; structural code slop is yours.
- **Unused dependencies**: remove only when nothing imports them
  (verified by search + build, not memory); lockfile updated; install
  still works.
- **Dead code**: deleted, not commented out. Git remembers.
- Commented-out blocks, debug leftovers, empty files, `TODO: fix this`:
  mass grave cleanup is allowed in one cosmetic batch, clearly labeled.

## Quality gates

- Baseline captured (test/build/flow evidence) before batch 1.
- Every finding has file:line evidence; no vibes-based "this smells".
- Every batch: green tests + diff-reviewed + (UI) browser-checked
  before the next.
- Net line delta and per-batch diffs available in the report.
- Zero behavior changes — if any happened accidentally, disclosed and
  reverted.

## Stop conditions

- Critical + high-leverage ranks cleared → report, offer to continue
  into medium/cosmetic, stop.
- Baseline can't be established (app won't run) → fixing *that* becomes
  the first mission, possibly via `sleuth`; no cleanup before a signal
  exists.
- A finding turns out to be load-bearing behavior → keep it, document
  why in the report.

## Output contract

Chat: findings table (rank · location · problem · status), batch log
(each: what changed, verification evidence), net line delta, what was
deliberately kept. On request: `docs/reports/detox-<slug>.md` with
provenance header.
