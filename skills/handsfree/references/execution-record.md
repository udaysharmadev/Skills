# Execution record: autonomy with recoverable evidence

Use this reference for checkpointed work, ASK ONCE gates, retries, host denials,
or scope changes. Routine AUTO work needs no extra artifact.

## Minimal record

| Field | Capture |
| --- | --- |
| Requested outcome | user-facing result and acceptance signal |
| Current mode | focused, checkpointed, gate management, or recovery |
| Action class | AUTO, AUTO + CHECKPOINT, ASK ONCE, or BLOCKED |
| Evidence | repository state, command output, or user authorization supporting class |
| Protected state | dirty work, data, public contract, or other invariant |
| Verification | command or observation that demonstrates result |
| Recovery | reversible path, or gate/blocker if none is safe |

## Scope-change rule

Classify every discovered task as one of three outcomes:

- In scope: necessary to the requested result and no stricter action class.
- Deferred: useful but not necessary; report it as a follow-up.
- Gate: changes product behavior, external state, cost, security, or risk;
  collect it in the one ASK ONCE packet.

Similarity to the original task is not enough. The new work must be necessary
to complete the original outcome safely.

## Recovery loop

1. Stop the affected branch and preserve current evidence.
2. Identify whether failure predates the action, follows it, or is unknown.
3. Choose one different low-risk diagnostic or rollback allowed by the action
   class.
4. Verify the new state. If it yields no new evidence, stop with blocker.
5. Do not erase user work, force state, alter permissions, or spend money as a
   recovery shortcut.

## Gate packet

One ASK ONCE question contains exact action, target, external or destructive
effect, alternatives, recommended default, and what independent work continues.
An approval covers only that action and target. Reclassify any expanded scope.

## Completion record

Report verified outcome, consequential autonomous decisions, checkpoints,
remaining uncertainty, and pending or blocked gates. Do not label an unrun
test, inaccessible system, or unresolved regression as verified.
