# Planning protocol: make execution independent of planner memory

Use this for full plans, high-risk slices, or replanning. Lightweight plans can
stay in the entrypoint format.

## Decision record

For a material choice, record decision, evidence, scope, alternatives,
consequence, reversibility, owner, and recheck trigger. Mark unverified premise
and create its discovery slice before actions that depend on it.

## Slice contract

| Field | Required content |
| --- | --- |
| Outcome | one observable behavior or state change |
| Evidence | confirmed files, existing behavior, dependency context |
| Action | coherent work, not microsteps |
| Invariants | contracts, data, security, compatibility, or operations preserved |
| Verification | command, test, observation, or explicit unavailable boundary |
| Recovery | reversible action, migration path, or user checkpoint |
| Dependencies | prerequisite slice, conflict, and postponed work |

## Replan rule

Replan when assumption changes architecture, public behavior, data model,
security posture, deployment order, cost, or acceptance criteria. A local file
adjustment preserving these is an execution deviation. Never use a replan to
conceal scope expansion.

## Discovery-first examples

- Validate installed library capability before designing around it.
- Map migration and deployment sequence before proposing data change.
- Trace authorization boundary before adding protected route.

Discovery ends with evidence and decision, not endless research.
