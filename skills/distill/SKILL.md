---
name: distill
description: Turns vague, underspecified requests into execution-grade task briefs. Use when the user gives a sloppy or one-line feature request ("bro add dashboard make it good"), before planning implementation work, when requirements are ambiguous or contradictory, or when asked to write a prompt, spec or brief for a coding task. Produces goal, scope, non-goals, acceptance criteria, edge cases and verification requirements — enough to remove ambiguity, never an encyclopedia.
---

# distill — weak request in, sharp brief out

A great brief removes ambiguity. It does not add volume. Your output should
be executable by a weaker model without access to this conversation — every
fact it needs is on the page, and nothing on the page is filler.

## When NOT to use

- The idea hasn't survived critique yet → `hotseat` first.
- The request is already precise (goal, scope, and definition of done are
  unambiguous) → skip straight to planning.
- The task is a small mechanical fix ("rename this variable") → just do it.

## Prerequisites

The triggering request. A quick look at the repository for context (what
exists, what conventions apply) — lighter than a `spelunk` pass; read only
what the request names or obviously touches.

## Scale the brief to the request

| Request type | Brief shape |
| --- | --- |
| **tiny task** (button rename, copy fix) | goal + acceptance criterion + where — 5–10 lines, no template ceremony |
| **feature** | full template below |
| **large feature / migration** | full template + NFRs, rollout constraints, backward-compatibility and data-migration notes |
| **bug/change request** | reproduction facts + expected behavior + scope guard (what NOT to fix along the way) |
| **greenfield product** | full template + target user + success metric; defer tech choices to `masterplan` unless the user named them |

A brief for a button rename that mentions "non-goals" and "rollout" is
enterprise cosplay — match depth to blast radius.

## Workflow

### 1. Extract the goal

Restate the request as one sentence: *what* will be true after the work
that isn't true now, *for whom*. If you cannot write this sentence, that's
a clarifying question, not a brief.

### 2. Ground in the repo first (lightly)

Before drafting a single question, confirm the surfaces the brief touches
actually exist: the page/module named, the data involved, the commands
available. Briefs referencing nonexistent files are how hallucinated work
starts. Most "ambiguities" die here — what remains is genuinely missing.

### 3. Ambiguity detection (max 5 questions)

Actively scan the request for linguistic, semantic, and functional
ambiguities. List what's genuinely blocking:
- Undefined boundaries ("make it fast" → what is the target metric?)
- Contradictory constraints
- Missing definitions of "good" or failure states

For each candidate question, apply the materiality test: name the two most
plausible answers and what each would change about implementation, security,
data handling, or UX. If nothing material changes, it is not a question —
it becomes an explicit numbered assumption in the brief.

Ask **only blocking questions, max 5, in one batch**. Anything non-blocking
becomes an explicit numbered assumption in the brief. Never run a
back-and-forth interrogation.

### 4. Write the brief

Use the template in `references/brief-template.md` (it includes a filled
example). Core sections:

- goal (one sentence) + user outcome;
- context: relevant existing pieces, with file paths;
- constraints and conventions to respect;
- scope: what's in;
- non-goals: what's explicitly out (as valuable as scope);
- agent-executable specifications: statements another agent can objectively verify without human judgment;
- edge cases: empty/loading/error/malformed states worth handling;
- non-functional requirements **only when they bite** (performance
  budget, accessibility bar, i18n, security constraint) — omitted means
  "nothing beyond the project's existing bar";
- backward compatibility / migration notes when existing data or users
  are affected;
- UX expectations (only if user-facing);
- verification: how "done" gets **proven** — which commands must pass,
  what a human/browser check confirms;
- known unknowns + numbered assumptions.

### 5. One-pass confirmation

Show the brief. Ask for corrections once, integrate, done. Don't loop on
polish — downstream skills (`masterplan`) will surface anything structural.

## Anti-bloat rules

- Every line must remove ambiguity or it gets deleted.
- No restating general knowledge ("React is a component library") — the
  reader is a coding agent, not a student.
- No invented requirements the user never implied. Suggestions go in a
  clearly-marked "suggestions (non-binding)" list, max 3.
- Target ≤ 120 lines; a tight brief beats an impressive one.

## Quality gates

- A reader who never saw this chat could implement without guessing on
  scope — test your draft against this before showing it.
- Every agent-executable specification is objectively checkable by another agent without human intervention.
- The verification section names real commands/checks (that exist in this
  repo or are standard).
- Assumptions are numbered and falsifiable ("A1: single-user, no roles").

## Stop conditions

- User confirms the brief → hand off to `masterplan` (or implement
  directly if the task is small), then stop.
- The request reveals an unsettled product decision → stop and route back
  to `hotseat` for that decision.

## Output contract

In chat: the brief. On disk (when the task will span sessions or feed
planning): `docs/briefs/<slug>.md` with provenance header
(`<!-- generated by distill on YYYY-MM-DD -->`).

`<slug>`: kebab-case, ≤ 5 words from the task title.
