# Budget protocol: reduce waste without deleting decision evidence

Use this reference for measured savings, a repeated workflow, a compact handoff,
or recovery after context loss. For a one-off task, apply the entrypoint rules
directly and keep moving.

## Budget record

Create this record before a measurement claim:

| Field | Capture |
| --- | --- |
| Task and quality gate | same acceptance criteria and verification for both paths |
| Compared runs | model, tool access, data, cache state, and task differences |
| Suspected leak | whole file, tool output, duplicate reading, report verbosity, or repeated discovery |
| Intervention | one named change, or an explicit bundled redesign |
| Preserved evidence | paths, ranges, command output, identifiers, and raw diagnostics retained |
| Outcome | success, retry count, verification result, and measured or derived usage |

Do not compare runs with materially different tasks, data, permissions, or
models as though the delta came from the intervention.

## Classify context before compacting it

| Class | Treatment |
| --- | --- |
| Task-critical | retain the source or a reversible pointer plus exact decision facts |
| Useful | retain when it materially changes quality; otherwise point to it |
| Optional | defer until a concrete question needs it |
| Waste | avoid re-reading, duplicate narration, and unbounded output |

Never compact away a user decision, approval boundary, failing assertion,
security constraint, migration state, exact identifier, or evidence that would
change the next action.

## Handoff payload

A compact handoff should contain only:

1. objective and current state;
2. decisions and constraints made by the user or repository;
3. changed files or source pointers with line or symbol anchors;
4. commands run and observed results, including failures;
5. unresolved risks and the next safe action.

If the next worker cannot open a source, include the minimum exact excerpt
needed for its next decision and state that access limitation. Do not pretend a
path is evidence in an environment where it cannot be read.

## Context-loss recovery

1. Stop proposing changes from memory.
2. Reopen the task contract, current diff, repository instructions, and last
   verification output.
3. Reconstruct only the decision-relevant chain using stable paths and symbols.
4. Mark anything not re-established as an assumption.
5. Resume with a targeted retrieval plan; do not reload the whole repository as
   a reflex.

## Claim examples

- Measured: input usage fell from a provider-reported value to another on the
  same task and model; the same test command passed in both runs.
- Derived: bounded command output reduced captured bytes, with command and
  byte counts recorded. This is not automatically a token result.
- Unknown: search-first navigation was used, but telemetry and a comparable
  baseline were unavailable. No percentage is reported.

An intervention that causes a retry, omits an important constraint, or weakens
verification is a negative result even if one individual prompt was shorter.
