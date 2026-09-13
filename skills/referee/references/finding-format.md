# Findings — severity, format, the quality checklist

## Severity definitions (with the line between them)

| Sev | Definition | Example |
| --- | --- | --- |
| **Blocker** | Ships a defect: data loss, security hole, broken acceptance criterion, crash on a real path | authz check missing on new endpoint |
| **Major** | Will hurt soon and shouldn't merge as-is: missing tests for new behavior, silent error swallowing, misleading naming on a core concept, perf foot-gun on a hot path | new money path has no test for the failure branch |
| **Minor** | Real but safely fixable forward: missing edge case that's unlikely, small duplication, doc drift | error message promises format the code doesn't produce |
| **Nit** | Preference and polish: naming, order, subjective style | `d` vs `durationMs` |

Judgment calls: **a preference is a nit.** Reserve major for things that
will demonstrably cost the next person time or the users something.
Nits never block; if you're listing more than a handful of nits, you're
reviewing style, not the change.

## Finding format (every finding, all four parts)

```text
<sev> <file:line> — <what is wrong>
      why it matters: <the concrete consequence>
      fix direction: <the change, one line>
```

A finding without "why it matters" is an opinion; without a fix
direction it's a complaint. Both halves or delete it.

## Quality checklist (walk per diff — skip what doesn't apply)

**Correctness**
- Logic handles the edges the behavior names: empty, zero, max, negative,
  malformed, concurrent, repeated.
- Error paths do something deliberate (typed, logged, surfaced) — no
  silent catches.
- Resource handling: files/connections/cursors closed on every path,
  including error paths.
- Concurrency: shared state identified; races either impossible
  (constraints) or handled (locking/idempotency).

**Intent & scope**
- Every acceptance criterion: met, partially met, or missing — named.
- No scope creep: refactors/rename/dead-code removal that the criteria
  didn't ask for (note as findings, however well-intentioned).
- No dead code, debug leftovers, commented-out blocks, or console
  noise introduced.

**Tests**
- New behavior has tests at the boundary that matters (proof's map).
- The tests would fail if the implementation were reverted.
- No test-only backdoors in production code (or they're documented and
  gated).

**Security**
- New inputs validated at the boundary; new object access authorized per
  resource.
- No secrets/PII in logs, errors, or test fixtures.
- Queries parameterized; no string-built SQL/commands.

**Performance** (obvious-level only; measurement belongs to hotpath)
- No N+1 in new loops over queries; no unbounded growth (arrays, maps,
  listeners).

**Conventions & clarity**
- Project conventions followed (naming, structure, patterns) — reviewer
  taste loses to house style.
- Names say what things are for; the complex part has the comment
  explaining *why* (not *what*).
- Complexity proportionate: is there a simpler version that meets the
  criteria? If yes, that's a major with a sketch.

**API/DB surface changes**
- Breaking changes flagged and versioned; migration has a down-path.

## Self-review discipline (when fresh-context is unavailable)

1. Wait for the **complete** diff — reviewing slices hides the seams.
2. Reread the written acceptance criteria before line one of code —
   memory of them is author-bias fuel.
3. Read the diff twice: once as intent-auditor, once as quality checklist.
4. For every "looks fine", ask what evidence would prove it isn't.
5. Disclose the mode; recommend a fresh-context pass before merge for
   anything touching auth, money, or data loss paths.
