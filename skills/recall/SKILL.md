---
name: recall
description: Maintains compact project memory as verified facts, decisions, current state, unresolved issues, and lessons with source and freshness metadata. Use for long-running work, context resets, handoffs, or when the user asks what was decided or what remains.
---

# recall: memory that respects the context window

Context loss between sessions is where vibe-coded projects go to die. This
skill fixes that with four small files and brutal editing discipline. A
memory system that injects everything every turn is a token leak, not
memory.

## Prerequisites

The four files present (or a first write to create them) plus a task
that genuinely needs past context: a decision to record, a handoff to
write, a catch-up to give. Ephemeral facts and repo-derivable trivia
never reach a write.

## Authority and operating modes

Memory is a project artifact, not an inference engine. Write only facts observed
in the repository or task, user decisions, and lessons supported by concrete
experience. Do not record credentials, private data, speculation, private
reasoning, or a decision the user has not made. When ownership is unclear,
propose the entry rather than writing it.

| Mode | Use when | Result |
| --- | --- | --- |
| Retrieve | task needs prior context | smallest current evidence set and freshness report |
| Delta | a session or milestone changed durable state | minimal verified update to appropriate files |
| Reconcile | entries conflict, drift, or duplicate | source-backed supersession or deferred conflict |
| Compact | a file no longer supports quick decisions | lossless reduction with pointers retained |

Use [references/memory-protocol.md](references/memory-protocol.md) for a
reconciliation, compaction, or write whose source is outside the current task.

## Tool selection/fallback

- `scripts/check-memory`: run after every write batch; fix missing dates,
  duplicate entries, and missing status freshness markers.
- Files contradictory or polluted → one compaction pass first; never
  write into a mess.
- No files yet → create on first write in `references/file-formats.md`
  shape; the validator confirms the shape after.

## When NOT to use

- The fact is ephemeral (current branch, WIP noise): it lives in git and
  `STATUS.md` already covers ongoing work.
- The information is derivable from the repository in seconds (a file
  path, a command): don't memorize what you can re-derive.
- The user just wants a one-off answer: memory writes are for things
  that matter next session.

## The four files

| File | Holds | Soft cap |
| --- | --- | --- |
| `PROJECT_CONTEXT.md` | Stable facts: stack, commands, conventions, services, env var **names** | compact reference |
| `DECISIONS.md` | Decisions + why + rejected alternatives, newest first | append-only decisions, superseded explicitly |
| `STATUS.md` | Current work, blockers, next steps: a snapshot, not a log | replaced each handoff |
| `LEARNINGS.md` | Expensive lessons ("X breaks under Y", "user prefers Z") | only non-obvious reusable lessons |

Exact formats: `references/file-formats.md`. All four live at the
repository root, are created on first write, and are plain markdown so
humans can read and edit them too.

## Write rules

0. **Enforce the Knowledge Hierarchy.** Fact (true until codebase changes) →
   Decision (true until context changes, explicitly modeled state machine) →
   Lesson (portable, true everywhere). Status is transient. Hypotheses stay
   out of memory entirely until they survive testing.
1. **Decisions and facts, not transcripts.** "Chose SQLite over Postgres
   because deployment is single-box": yes. "User said, then I said": no.
2. **One entry, one thing.** No essays. If it needs paragraphs, it's two
   entries or it belongs in `docs/`.
3. **Deduplicate before appending.** Read the file, update the existing
   entry if one covers it. Four near-identical entries is corruption, not
   memory.
4. **Provenance on load-bearing entries:** date + one line of why
   (`- 2026-09-14: chose SQLite: single-box deploy, no concurrency needs`).
5. **Decisions are governed state machines.** PROJECT_CONTEXT holds what
   should still be true in six months. DECISIONS models active choices as
   `[Active]` -> `[Superseded]` -> `[Deprecated]`. A durable decision captures:
   decision, reason, date/context, consequence, and what it supersedes. A
   contradiction between an old fact and a new one is a supersession (state change),
   not a coin flip.
6. **Transient state needs an expiry condition.** Use a date, milestone, or
   superseding event when staleness would mislead future work.
7. **Never write secrets**: env var names, never values; no tokens, no
   credentials, no personal data the user didn't ask to store.

## Session start (retrieval)

Read only what the task needs: `STATUS.md` always (it's tiny by design);
`PROJECT_CONTEXT.md` for anything substantial; `DECISIONS.md` /
`LEARNINGS.md` when the task touches a past decision or looks like a
repeated mistake. Load the smallest set that supports the current decision. If
the files have grown noisy, compact first, then proceed.

Check freshness before relying on a loaded entry: date, source, status, expiry
or revisit condition, and whether repository state still supports it. An entry
is a lead, not an override of current source, tests, configuration, or an
explicit user instruction. Cite stale or conflicting memory as a risk rather
than silently repeating it.

## Session delta (the handoff protocol)

Before a session ends, a context reset looms, or a major milestone lands,
write the delta:

- **STATUS.md**: replace the snapshot: done / in progress / blocked /
  next, each one line.
- **DECISIONS.md**: append any decisions made this session (with why).
- **LEARNINGS.md**: append lessons that cost real time to discover.
- **PROJECT_CONTEXT.md**: only if a stable fact actually changed.

Keep the delta to decisions and state that will matter next session. Detailed
plans, briefs, and research stay in their owning artifacts with STATUS pointing
at them.

## Compaction

When a file stops being quick to scan: merge duplicates, delete entries superseded
by newer ones (keep the newest), move narrative detail into `docs/` and
leave a one-line pointer. Never compact by summarizing everything into
vagueness: a memory that says "we made many decisions" is not memory.

### Reconciliation and failure handling

When memory conflicts with repository truth, an explicit user choice, or newer
verified evidence, do not edit history into a single claim. Mark the older
decision superseded with its replacement pointer, update the current snapshot,
and preserve enough provenance to explain the change. If neither claim can be
verified, record the conflict in STATUS with a resolving action and do not
promote either to project context.

If the validator fails, fix structure without weakening semantic record. If a
file contains sensitive material, stop copying it; minimize exposure, alert the
user to its location without repeating values, and route security handling to
`harden`.

## Quality gates

- Run the bundled validator after writes. Structural consistency is checkable;
  truth and usefulness still require judgment.
- Every write deduplicated against current file contents (you read before
  you appended).
- New content is concise and the memory files remain quick to scan.
- No secrets, no env values, no transcript-style entries.
- Every decision entry answers "why": a decision without a why can't be
  revisited intelligently later.
- Every durable entry identifies its evidence class: observed repository fact,
  explicit user decision, or verified lesson. Unsupported inference stays out
  or is a question in STATUS.
- Compaction preserves decision state, source pointers, active constraints,
  unresolved blockers, and next safe action; shorter that loses these regresses.

## Stop conditions

- Requested fact remembered (or session delta written) → confirm in one
  line, stop.
- The "memory" turns out to be repo-derivable → say so, skip the write.
- Files have grown contradictory or polluted → propose one compaction
  pass before continuing; don't write into a mess.
- Freshness cannot be established for a load-bearing entry → do not carry it
  forward as fact; name source or experiment needed to refresh it.
- Requested entry exposes secrets, personal data, or unapproved private
  material → decline that content and offer a safe pointer or redaction.

## Output contract

Writes go only to the four files above (plus pointers into `docs/`).
Confirmation in chat is one line per file touched:
`recall: DECISIONS.md +1 ( chose SQLite: single-box deploy ) · STATUS.md
snapshot updated`.

On session start, end the catch-up with a short freshness summary or name what
needs compacting.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
Read [references/file-formats.md](references/file-formats.md) before creating or
editing the four files. Read [references/memory-protocol.md](references/memory-protocol.md)
for reconciliation, source-backed compaction, or recovery from stale memory.
