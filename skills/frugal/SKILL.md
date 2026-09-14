---
name: frugal
description: Reduces token consumption without reducing task quality — read less, output less, reuse context, execute instead of reasoning over raw data. Use when sessions burn context too fast, when the user mentions token usage, context window, cost or efficiency, before long tasks that will need every token, or when compacting handoffs between sessions or agents. One rule above all — save tokens, never save effort — with every saving reported as measured, derived, estimated or unknown.
---

# frugal — save tokens, never save effort

The one rule decides every judgment call: **the quality gate must not
move.** A "cheaper" run that fails the task, retries twice, or ships
unverified work costs more than it saved. The KPI is *successful task
token cost* — never raw token minimization.

## When NOT to use

- The task is short and context is healthy — overhead exceeds savings.
- The user asked for exhaustive output deliberately.
- A "saving" would remove verification steps — that's the effort this
  skill exists to protect.

## The techniques

Grouped by where the tokens go. Each is a habit to apply when it fits,
not a checklist to run ritually.

### Read less

- **Search before read** — locate the symbol/range first; read the hit,
  not the file. Never "read the whole repo to understand it" when a
  targeted grep answers the question.
- **Ranged reads** — files over ~400 lines: read around the relevant
  symbols, not top-to-bottom.
- **Symbol-first navigation** — definitions/references before file
  listings.

### Output less

- **Byte-cap command output** — pipe through `head`/`tail`/`wc`,
  aggregate instead of dumping; a 4,000-line log read into context is a
  self-inflicted wound.
- **Summarize deterministically** — sort/uniq/awk/jq in the shell
  produce the 3 lines that matter; the model reasons over the summary,
  not the raw stream.
- **Compact reports** — findings over narratives; the file path and the
  verdict beat three paragraphs of prose.

### Reuse

- **Project memory over re-discovery** — `recall`'s artifacts exist so
  stack facts aren't re-derived every session. Read memory before
  probing.
- **Progressive reference loading** — load the reference section the
  task needs, not every reference the skill owns.
- **Preserve cache prefixes** — keep stable instructions/artifacts in
  the same order early in context where the runtime supports prompt
  caching; don't shuffle stable content between turns.

### Budget model

Before optimizing, classify where context goes: **task-critical**
(removing it fails the task) · **useful** (improves quality measurably)
· **optional** (read but never used) · **waste** (re-read, over-cap
output, restated instructions). Optimization targets optional and waste
ONLY — the budget model is what stops "save tokens" from quietly
becoming "skip the evidence".

### Execute, don't reason

- **Scripts over eyeballing** — counting occurrences, diffing trees,
  extracting fields: a local script is deterministic and costs ~one
  call; an LLM reasoning over raw data costs hundreds of thousands of
  tokens and makes mistakes.
- **Cheaper models for mechanical passes** — only when it doesn't
  increase retries; a doubled retry count erases the saving and adds
  latency. Verify with a small sample before committing a workflow.

## Workflow for a frugality pass

1. **Find the leaks** — where did context actually go? (Files read
   whole, giant tool outputs, repeated loads of the same data, verbose
   reports, redundant re-explanations.)
2. **Apply the fitting techniques** — with the quality gate stated
   first (what must still pass after).
3. **Verify the gate** — same task outcome, same verification evidence.
4. **Report savings honestly** — per `references/measurement.md`:
   measured / derived / estimated / unknown. Never print a percentage
   nobody measured.

## Quality gates

- Task success unchanged: same tests passing, same evidence produced,
  same verification claims allowed.
- Every reported saving carries its category (measured/derived/
  estimated/unknown) — an uncategorized claim is a violation, not a
  shortcut.
- Deterministic tools used where determinism matters (counts, diffs,
  extractions are script output, not model output).
- The handoff/context-compaction outputs stay within `recall`'s budgets
  (STATUS ≤ 40 lines, injection ≤ 40 lines).

## Stop conditions

- Leaks fixed and gate verified → report, stop.
- The remaining "savings" would cut verification or correctness → say
  that's the line, stop.
- No measurable baseline available → make the habits explicit in the
  work (search-before-read etc.), mark savings **unknown**, don't
  fabricate numbers.

## Output contract

Chat: the leak list (where tokens were going), techniques applied,
savings per `references/measurement.md` categories with their evidence,
and the quality-gate confirmation (what still passes). Compacted
handoffs follow `recall`'s session-delta format.
