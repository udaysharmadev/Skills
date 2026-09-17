# Execution protocol: one verified slice at a time

Use this reference for medium or high-risk work, deviations, failures, or an
interrupted implementation. Low-risk slices can use entrypoint loop.

## Slice record

Record outcome, current evidence, files touched, protected invariants,
verification, recovery path, deviations, and status: done, blocked, deferred,
or needs replan. A checkbox is evidence-backed state, not intent.

## Deviation triage

| Type | Action |
| --- | --- |
| Local implementation adjustment | record reason and verification; continue after checks |
| Unknown file or behavior | discovery before implementation continues |
| Architecture or scope change | stop and return affected slices to masterplan |
| New external, destructive, paid, or production effect | apply gate and await authorization |

## Failed-check response

1. Preserve command output, diff, and baseline comparison if available.
2. Identify a distinct hypothesis or diagnostic.
3. Repair inside active slice unless evidence requires replan.
4. Re-run relevant verification and inspect diff.
5. Stop after two unproductive attempts; report blocker.

## Interruption handoff

State active slice, changed paths, checks and results, dirty-tree overlap,
recovery path, unresolved risk, and next safe action. Never claim completion
from partial implementation.
