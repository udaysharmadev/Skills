---
name: recall
description: Persistent, high-signal project memory kept in four root files (PROJECT_CONTEXT.md, DECISIONS.md, STATUS.md, LEARNINGS.md). Use when the user says "remember this", asks what was decided last session or to catch them up, when a decision or expensive lesson should outlive the conversation, before ending a session or a context reset, or when starting work in a repository that has these memory files. Stores decisions and facts, never transcript dumps, under a strict context budget.
---

# recall — memory that respects the context window

Context loss between sessions is where vibe-coded projects go to die. This
skill fixes that with four small files and brutal editing discipline. A
memory system that injects everything every turn is a token leak, not
memory.

## When NOT to use

- The fact is ephemeral (current branch, WIP noise) — it lives in git and
  `STATUS.md` already covers ongoing work.
- The information is derivable from the repository in seconds (a file
  path, a command) — don't memorize what you can re-derive.
- The user just wants a one-off answer — memory writes are for things
  that matter next session.

## The four files

| File | Holds | Soft cap |
| --- | --- | --- |
| `PROJECT_CONTEXT.md` | Stable facts: stack, commands, conventions, services, env var **names** | ~100 lines |
| `DECISIONS.md` | Decisions + why + rejected alternatives, newest first | ~200 lines |
| `STATUS.md` | Current work, blockers, next steps — a snapshot, not a log | ~40 lines |
| `LEARNINGS.md` | Expensive lessons ("X breaks under Y", "user prefers Z") | ~100 lines |

Exact formats: `references/file-formats.md`. All four live at the
repository root, are created on first write, and are plain markdown so
humans can read and edit them too.

## Write rules

0. **Know what kind of knowledge you are writing.** Stable fact ·
   decision · temporary status · hypothesis · lesson · constraint ·
   preference · open question · superseded fact — each lives in its home
   file (facts/constraints → PROJECT_CONTEXT, decisions/supersessions →
   DECISIONS, status/open questions → STATUS, lessons → LEARNINGS), and
   hypotheses stay out of memory entirely until they survive testing.
1. **Decisions and facts, not transcripts.** "Chose SQLite over Postgres
   because deployment is single-box" — yes. "User said, then I said" — no.
2. **One entry, one thing.** No essays. If it needs paragraphs, it's two
   entries or it belongs in `docs/`.
3. **Deduplicate before appending.** Read the file, update the existing
   entry if one covers it. Four near-identical entries is corruption, not
   memory.
4. **Provenance on load-bearing entries:** date + one line of why
   (`- 2026-09-14 — chose SQLite: single-box deploy, no concurrency needs`).
5. **Distinguish stable from temporary.** PROJECT_CONTEXT holds what
   should still be true in six months; everything else goes in STATUS.
   A durable decision captures: decision, reason, date/context,
   consequence, and what it supersedes (mark the old entry
   `*(superseded YYYY-MM-DD by: X)*` — never delete history, supersede
   it). A contradiction between an old fact and a new one is a
   supersession, not a coin flip.
6. **Stale entries get flagged or deleted**, not left to poison future
   sessions: mark `(stale as of YYYY-MM-DD — verify)` or remove.
7. **Never write secrets** — env var names, never values; no tokens, no
   credentials, no personal data the user didn't ask to store.

## Session start (retrieval)

Read only what the task needs: `STATUS.md` always (it's tiny by design);
`PROJECT_CONTEXT.md` for anything substantial; `DECISIONS.md` /
`LEARNINGS.md` when the task touches a past decision or looks like a
repeated mistake. Injection budget: **≤ 40 lines total**. If the files
have grown past their caps, compact first (below), then proceed.

## Session delta (the handoff protocol)

Before a session ends, a context reset looms, or a major milestone lands,
write the delta:

- **STATUS.md**: replace the snapshot — done / in progress / blocked /
  next, each one line.
- **DECISIONS.md**: append any decisions made this session (with why).
- **LEARNINGS.md**: append lessons that cost real time to discover.
- **PROJECT_CONTEXT.md**: only if a stable fact actually changed.

The delta is ≤ 25 lines of new content. If more happened, the extra detail
belongs in `docs/` artifacts (plans, briefs, research notes) with STATUS
pointing at them.

## Compaction

When a file exceeds its cap: merge duplicates, delete entries superseded
by newer ones (keep the newest), move narrative detail into `docs/` and
leave a one-line pointer. Never compact by summarizing everything into
vagueness — a memory that says "we made many decisions" is not memory.

## Quality gates

- Run the bundled validator after writes: `scripts/check-memory` (caps,
  dated entries, duplicates, STATUS staleness, dump smell) — structural
  health is checkable; truth is not, and stays with you.
- Every write deduplicated against current file contents (you read before
  you appended).
- New content within the session-delta budget; files within soft caps
  after compaction.
- No secrets, no env values, no transcript-style entries.
- Every decision entry answers "why" — a decision without a why can't be
  revisited intelligently later.

## Stop conditions

- Requested fact remembered (or session delta written) → confirm in one
  line, stop.
- The "memory" turns out to be repo-derivable → say so, skip the write.
- Files have grown contradictory or polluted → propose one compaction
  pass before continuing; don't write into a mess.

## Output contract

Writes go only to the four files above (plus pointers into `docs/`).
Confirmation in chat is one line per file touched:
`recall: DECISIONS.md +1 ( chose SQLite — single-box deploy ) · STATUS.md
snapshot updated`.

On session start, the catch-up is ≤ 40 lines and ends with `memory: N
entries, oldest from YYYY-MM-DD, all within caps` — or names what needs
compacting.
