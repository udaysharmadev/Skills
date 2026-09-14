# Benchmarks — skill vs no skill

The credibility layer: same agent + same task + skill, versus same
agent + same task + no skill. Controlled where controllable, multiple
runs where stochastic, raw outputs recorded, cherry-picking forbidden.

## Status: empirical proof phase intentionally deferred

Nothing on this page is a result. When results exist they will carry:
agent + version, model, date, git commit, run count, raw transcripts,
and per-run quality scores under a pre-registered rubric.

## Focus skills (signature, public-demo quality)

`hotseat` `polish` `unslop` `blueprint` `harden` `frugal` `frontpage`

## Fixtures

`benchmarks/fixtures/` — intentionally small, realistic repositories
with **seeded defects**. The answer key for each fixture lives in
`benchmarks/answer-keys/` and is given to the grader, never to the
evaluated agent.

| Fixture | Stack | Seeds | Serves |
| --- | --- | --- | --- |
| `ts-dashboard` | TypeScript/React-style web app | swallowed errors, duplicated logic + schema, dead code, unused dep, any-casts, debug leftovers, committed secret, mega-component | `unslop` `harden` `proof` `referee` |
| `py-notes-api` | Python FastAPI-style API | validation gaps, missing tests, config sprawl, doc gaps | `backend` `proof` `frontpage` |
| `ugly-dashboard.html` | single-page vanilla UI | generic AI-UI patterns, missing states, contrast failures | `polish` `friction` |

PRD §12 names five stack categories; the current historical fixture set covers
TypeScript/web, Python, and standalone HTML. Expanding fixtures and running
comparisons belong to the future proof phase, not repository productization.

Rules for fixtures: no giant fake repos; every seed documented in the
answer key with location + expected finding; behavior baseline recorded
before benchmarking.

## The frugal protocol (highest-integrity benchmark)

Compare equivalent tasks with/without `frugal`. Track whatever the
runtime exposes (input/output/cache tokens, tool calls, files opened,
bytes read, retries, wall-clock, task success). **Primary metric:
successful-task token cost.** Every number reported as MEASURED /
DERIVED / ESTIMATED / UNKNOWN — a byte-reduction result may be reported
as derived when telemetry is unavailable, and never dressed up as a
token percentage.

## The polish protocol (visual evidence)

Before/after screenshots (desktop + mobile), state coverage
(empty/loading/error), console status, accessibility checks, relevant
Core Web Vitals where practical. No single "aesthetic score" — the
rubric is predefined, and the before/after images are the evidence.
Demo-ready outputs land in `docs/examples/`.
