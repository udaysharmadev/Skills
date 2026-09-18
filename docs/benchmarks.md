# Benchmarks — skill vs no skill

The credibility layer: same agent + same task + skill, versus same
agent + same task + no skill. Controlled where controllable, multiple
runs where stochastic, raw outputs recorded, cherry-picking forbidden.

## Status: empirical proof phase underway

Ten of 28 skill families have executed baseline-vs-skill trials, including
the `handsfree` grader-debugging smoke sample. Current
skill-specific verdicts are: `hotseat` PROVEN LIFT; `concierge`, `proof`,
`recall`, `spelunk`, and `scout` MIXED; `distill`, `masterplan`, and `pilot`
NO LIFT on the available evidence. Nineteen remain UNVERIFIED: `handsfree`
despite its completed smoke sample, plus 18 without completed trials. These are
not suite-wide or cross-model superiority claims.

Each result page under [`docs/benchmarks/`](benchmarks/) records agent +
version, model, date, git commit, run count, grading limits, and the observed
trial table. Raw runner outputs remain under the gitignored `evals/results/`
unless curated evidence is explicitly committed.

## Focus skills (signature, public-demo quality)

`hotseat` `polish` `unslop` `blueprint` `harden` `frugal` `frontpage`

## Fixtures

`benchmarks/fixtures/` contains 20 intentionally small repositories or files
with **seeded defects**. The answer key for each fixture lives in
the task contract or `benchmarks/answer-keys/` and is given to the grader,
never to the evaluated agent. `scripts/eval-outcome --check` verifies that
every named fixture resolves before a live run.

| Fixture | Stack | Seeds | Serves |
| --- | --- | --- | --- |
| `ts-dashboard` | TypeScript/React-style web app | swallowed errors, duplicated logic + schema, dead code, unused dep, any-casts, debug leftovers, committed secret, mega-component | `unslop` `harden` `proof` `referee` |
| `py-notes-api` | Python FastAPI-style API | validation gaps, missing tests, config sprawl, doc gaps | `backend` `proof` `frontpage` |
| `ugly-dashboard.html` | single-page vanilla UI | generic AI-UI patterns, missing states, contrast failures | `polish` `friction` |

The table is representative rather than exhaustive; the remaining fixtures
exercise release gates, UI reconstruction, UX, SEO, memory, Git hygiene,
performance, security, browser evidence, and deployment restraint.

PRD §12 names five stack categories. The current set covers TypeScript/web,
Python, and standalone HTML. Go/Rust, Java/Kotlin, and mobile remain explicit
fixture gaps; no cross-stack claim is made for them.

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
