# Memory protocol: preserve facts without preserving noise

Use this reference for a conflict, compaction, or durable write supported by a
different artifact. Routine session deltas should stay in the entrypoint flow.

## Eligibility test

Record an item only if it changes a future decision and is not cheaper or safer
to re-derive. Classify it before writing:

| Class | Destination | Evidence needed |
| --- | --- | --- |
| Stable repository fact | PROJECT_CONTEXT | current source path, command, or owner confirmation |
| Explicit durable choice | DECISIONS | chooser, why, alternatives, and revisit trigger |
| Current work state | STATUS | observed state, blocker, next action, and expiry |
| Expensive reusable lesson | LEARNINGS | symptom, cause, source, and prevention |
| Hypothesis or rumor | do not persist as fact | keep in current investigation only |

## Reconciliation record

When entries disagree, collect old entry, new evidence, applicable scope, and
decision impact. Prefer explicit current user instruction, then current
repository behavior or authoritative configuration, then dated historical
memory. Mark a decision superseded instead of deleting rationale. If scope is
unclear, put question in STATUS with an owner and resolving action.

## Compaction invariants

Keep active decisions and reasons, supersession pointers, active constraints,
source paths for non-obvious facts, unresolved blockers, and next actions.
Remove transcripts, repeated wording, repository-trivial facts, expired
snapshots, and duplicated lessons. Replace detail with an accessible pointer,
not a vague summary.

## Safe handoff check

Before ending a task, a worker should answer: what outcome is being pursued,
what changed, what is verified, what is blocked, what constraints are active,
and what is the next safe action. Add only missing decision-relevant entries;
do not paste the session transcript.
