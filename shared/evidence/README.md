# Evidence vocabulary (canonical)

One label set for all 28 skills. Maintainer contract for humans and
tooling; skills inline the rows they depend on, never link here at runtime.

## Result labels (exact strings)

| Label | Meaning |
|---|---|
| `PROVEN LIFT` | skill beats the same-model baseline on the outcome task, repeatedly, with deterministic or blind-graded evidence |
| `CONSISTENCY LIFT` | same mean outcome, lower variance / fewer failure modes across trials |
| `EFFICIENCY LIFT` | equivalent successful outcome at lower measured cost (tokens, calls, time) |
| `MIXED` | lift on some tasks/trials, none or negative on others — details in the evidence page |
| `NO CLEAR LIFT` | strong baseline already does the task; useful information, not hidden |
| `REGRESSION` | skill makes outcomes worse (e.g. fewer questions via skipped gates) — preserved, never deleted |
| `UNVERIFIED` | no executed baseline-vs-skill comparison yet; the only honest default |

## Trial record (minimum fields per executed trial)

Case, condition (baseline/treatment), skill version/commit, fixture hash,
agent/version, model/config, timestamp, duration, tool calls,
files read/changed, token/cache telemetry when exposed, validator results,
artifacts, score/rubric, raw trace pointer, limitations.

## Grader preference

Deterministic checks (tests, builds, artifacts, seeded defects,
forbidden-path checks) → structured rules → blind qualitative A/B rubrics
only for genuinely qualitative properties → human review. Answer keys live
outside evaluated workspaces. Held-out cases stay frozen and separate from
tuning. Failures are preserved.
