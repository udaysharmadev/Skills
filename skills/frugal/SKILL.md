---
name: frugal
description: Reduces context and token waste while preserving task-critical evidence, source pointers, and the same quality gate. Use when a software task is context-heavy, repetitive, expensive, or likely to exceed an agent context window.
---

# frugal: save tokens, never save effort

The one rule decides every judgment call: **the quality gate must not
move.** A "cheaper" run that fails the task, retries twice, or ships
unverified work costs more than it saved. The KPI is *successful task
token cost*: never raw token minimization.

## Prerequisites

The task to economize plus its quality gate stated first (what must
still pass after), and whatever usage signal exists (provider telemetry,
or nothing: then savings start at **unknown**). No gate → define one
before touching the workflow; optimizing an undefined task is just
skipping work with extra steps.

## Authority and operating modes

This skill reduces avoidable context, tool-output, and repeated-discovery cost;
it does not authorize cutting required investigation, verification, user-facing
detail, privacy safeguards, or a requested exhaustive deliverable. Preserve the
task's acceptance criteria and approval boundaries exactly.

Choose a mode that matches the evidence available:

| Mode | Use when | Result |
| --- | --- | --- |
| Habit pass | No reliable usage telemetry exists | targeted reads and compact output; savings remain unknown |
| Measured experiment | Comparable runs and usage fields exist | controlled before/after record |
| Workflow redesign | Repetition spans sessions or agents | reusable retrieval, handoff, or automation rule with its quality gate |
| Incident response | Context is exhausted or evidence was lost | recover critical facts first; do not optimize retrospectively |

Write a short budget record before a measured experiment. Use
[references/budget-protocol.md](references/budget-protocol.md) for sampling,
context classification, and recovery from a lossy summary.

## Tool selection/fallback

- Provider usage fields → measured comparisons, like with like.
- No telemetry → byte/line proxies (files opened, lines retrieved,
  output bytes before/after) computed deterministically, labeled
  derived: or honestly **unknown**.
- Counting/extracting → shell tools (grep/jq/awk), never model
  eyeballing; the counter runs before the claim.

## When NOT to use

- The task is short and context is healthy: overhead exceeds savings.
- The user asked for exhaustive output deliberately.
- A "saving" would remove verification steps: that's the effort this
  skill exists to protect.

## The techniques

Grouped by where the tokens go. Each is a habit to apply when it fits,
not a checklist to run ritually.

### Read less

- **Search before read**: locate the symbol/range first; read the hit,
  not the file. Never "read the whole repo to understand it" when a
  targeted grep answers the question.
- **Ranged reads**: when a full file would add substantial irrelevant context,
  read around the relevant symbols.
- **Symbol-first navigation**: definitions/references before file
  listings.

### Output less

- **Bound command output**: use `head`/`tail`/`wc` or aggregation when
  raw output would drown the evidence.
- **Summarize deterministically**: sort/uniq/awk/jq in the shell
  produce only the lines that matter; the model reasons over the summary,
  not the raw stream.
- **Compact reports**: findings over narratives; the file path and the
  verdict beat three paragraphs of prose.

### Reuse

- **Project memory over re-discovery**: `recall`'s artifacts exist so
  stack facts aren't re-derived every session. Read memory before
  probing.
- **Progressive reference loading**: load the reference section the
  task needs, not every reference the skill owns.
- **Preserve cache prefixes**: keep stable instructions/artifacts in
  the same order early in context where the runtime supports prompt
  caching; don't shuffle stable content between turns.

### Budget model

Before optimizing, classify where context goes: **task-critical**
(removing it fails the task) · **useful** (improves quality measurably)
· **optional** (read but never used) · **waste** (re-read, over-cap
output, restated instructions). Optimization targets optional and waste
ONLY: the budget model is what stops "save tokens" from quietly
becoming "skip the evidence".

For each expensive input, ask four questions: What decision could it change?
What is the narrowest deterministic retrieval that retains that fact? Can a
pointer plus range replace the payload? What verification would detect a lost
constraint? If no decision or gate needs it, it is a candidate to avoid or
defer, not a candidate to summarize from memory.

## Anti-Patterns (The Banned List)

- **Context dumping:** loading an unfiltered log or whole repository when a
  targeted query can preserve the relevant evidence. Use `rg`, `jq`, or
  `awk` to extract what matters before reading.
- **Lossy Compression**: attempting to save tokens by summarizing a stack trace into "there was a type error," destroying the exact line numbers needed to fix the bug. Never compress the diagnostic payload.
- **Chatty Reasoning**: writing three paragraphs of "Thinking out loud..." to the user before running a one-line command. Keep thoughts internal or compact.

### Execute, don't reason

- **Scripts over eyeballing**: counting occurrences, diffing trees,
  extracting fields: a local script is deterministic and costs ~one
  call; an LLM reasoning over raw data costs hundreds of thousands of
  tokens and makes mistakes.
- **Cheaper models for mechanical passes**: only when it doesn't
  increase retries; a doubled retry count erases the saving and adds
  latency. Verify with a small sample before committing a workflow.
- **Stable evidence records**: retain file paths, symbols, commands, hashes,
  and source dates rather than re-pasting whole artifacts. A pointer is useful
  only when the recipient can actually access the target.
- **Bounded retrieval with escape hatches**: start from a search hit and a
  narrow range, then widen deliberately when imports, callers, history, or
  failure output make the initial slice insufficient. A cap is a default, not
  a censor.

## Workflow for a frugality pass

1. **State the protected outcome**: identify the acceptance criterion, trusted
   sources, verification commands, and detail the user explicitly asked to see.
2. **Map the evidence path**: identify where context actually went (whole-file
   reads, giant output, duplicate discovery, stale memory, or verbose reports)
   and classify each input as task-critical, useful, optional, or waste.
3. **Select one intervention**: use search, range reads, deterministic
   extraction, stable ordering, or a reusable handoff. Do not bundle changes
   when the purpose is to measure attribution.
4. **Execute with recovery in mind**: retain source pointers and the raw
   diagnostic payload needed to widen context. Never discard unique failures,
   exact constraints, identifiers, or user decisions.
5. **Verify the same gate**: compare task outcome and verification evidence.
   If the optimized path needs a retry or misses a constraint, count the total
   cost and restore the necessary evidence.
6. **Report honestly**: use the categories in
   [references/measurement.md](references/measurement.md): measured, derived,
   estimated, or unknown. Never print a percentage nobody measured.

### Repository inspection strategy

Before reading broadly, inspect repository instructions, task-local manifests,
the narrow symbol or error, and the affected test or build command. Use search
results to choose ranges, then follow only dependencies that change the next
decision. Read a full file when its control flow, configuration, generated
boundaries, or call graph makes slicing unsafe. Frugal navigation is evidence
directed, not artificially narrow.

### Failure handling and fallbacks

| Failure | Response |
| --- | --- |
| Search has no useful hit | widen by concept, file type, or history; do not infer absence |
| A range lacks lifecycle context | read the enclosing unit and its caller or configuration path |
| Summary conflicts with source | source wins; replace the summary and record the correction |
| Optimized path causes retry | include retry cost, restore the omitted evidence, and reject the intervention if it is net-worse |
| Usage telemetry is unavailable | use deterministic proxies only when useful; label token savings unknown |
| A handoff cannot access a pointer | include the smallest decision-relevant excerpt and the access limitation |

## Quality gates

- Task success unchanged: same tests passing, same evidence produced,
  same verification claims allowed.
- Every reported saving carries its category (measured/derived/
  estimated/unknown): an uncategorized claim is a violation, not a
  shortcut.
- Deterministic tools used where determinism matters (counts, diffs,
  extractions are script output, not model output).
- Handoff and context-compaction outputs remain quick to scan and contain only
  information that can change the next action.
- Compaction preserves the current goal, user decisions, unresolved risks,
  verification state, exact source pointers, and the next safe action.
- A claimed optimization does not conceal a retry, model change, task change,
  cache-state difference, or lost evidence.

## Stop conditions

- Leaks fixed and gate verified → report, stop.
- The remaining "savings" would cut verification or correctness → say
  that's the line, stop.
- No measurable baseline available → make the habits explicit in the
  work (search-before-read etc.), mark savings **unknown**, don't
  fabricate numbers.
- The next possible reduction would make a decision depend on a stale or lossy
  summary → stop and retain the source material.
- A measured intervention is net-worse after retries or verification → revert
  the workflow change and record the negative result.

## Output contract

Chat: the leak list (where tokens were going), techniques applied,
savings per `references/measurement.md` categories with their evidence,
and the quality-gate confirmation (what still passes). Compacted
handoffs follow `recall`'s session-delta format. A measured experiment also
states comparison scope, changed variable, telemetry source, retries, outcome,
and whether the result is adopted or rejected.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/budget-protocol.md](references/budget-protocol.md) for a
measured experiment, cross-session handoff design, or recovery from a context
loss incident.
