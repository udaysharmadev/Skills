# Skill maturity scorecard

The 28 skills are **implementation-complete**. Empirical outcome benchmarking
is a separate future proof phase. This scorecard therefore keeps implementation
maturity, research depth, tooling, documentation, and evaluation evidence
separate instead of lowering a finished runtime because an intentionally
deferred benchmark has not run—or inflating everything to 100%.

Status vocabulary:

- **Complete** — the runtime contract, boundaries, workflow, fallbacks, quality
  gates, stop conditions, and output are present.
- **Traced** — research lessons were checked against their named runtime files.
- **Justified N/A** — no helper or asset improves the skill enough to warrant
  another moving part.
- **Deferred** — empirical outcome comparison belongs to the proof phase.

| Skill | Implementation | Research | Tooling | Documentation | Evaluation status |
| --- | --- | --- | --- | --- | --- |
| `concierge` | Complete | Traced | Justified N/A | Complete | **MIXED** — codex O1 4/4 vs baseline 1/4; O2/O3 no lift available; see `docs/benchmarks/concierge.md` |
| `hotseat` | Complete | Traced | Justified N/A | Complete | **PROVEN LIFT** — 5/5 structural passes vs 0/5 baseline (strong-critic baseline); cost documented; see `docs/benchmarks/hotseat.md` |
| `spelunk` | Complete | Traced | `inventory` extended (manifests, generated/vendor, scoped churn) | Complete | Protocol + fixture grader authored; outcome UNVERIFIED (zero-spend) |
| `scout` | Complete | Traced | `check-note` structure validator (both directions tested) | Complete | Protocol + offline-trap tasks authored; outcome UNVERIFIED (zero-spend) |
| `distill` | Complete | Traced | Justified N/A | Complete | Protocol + scale-budget tasks authored; outcome UNVERIFIED (zero-spend) |
| `masterplan` | Complete | Traced | Justified N/A | Complete | Protocol + groundedness tasks authored; outcome UNVERIFIED (zero-spend) |
| `recall` | Complete | Traced | `check-memory` syntax-tested | Complete | Outcome proof deferred |
| `pilot` | Complete | Traced | Justified N/A | Complete | Protocol + workspace grader authored; outcome UNVERIFIED (zero-spend) |
| `backend` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `blueprint` | Complete | Traced | `validate-mermaid` syntax-tested; HTML asset present | Complete | Outcome proof deferred |
| `headroom` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `polish` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `friction` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `ditto` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `proof` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `roadtest` | Complete | Traced | `test-matrix` smoke-tested | Complete | Outcome proof deferred |
| `sleuth` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `referee` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `hotpath` | Complete | Traced | `measure-report` smoke-tested | Complete | Outcome proof deferred |
| `harden` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `unslop` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `janitor` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `frontpage` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `findable` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `frugal` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `cleared` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `runway` | Complete | Traced | Justified N/A | Complete | Outcome proof deferred |
| `handsfree` | Complete | Traced (primary host sources, verified 2026-09-14) | Justified N/A | Complete | 5 workflow scenarios + outcome protocol authored; outcome proof deferred |

## What the final audit verified

- 28/28 `SKILL.md` files exist; frontmatter names match folders.
- 28/28 define scope boundaries, failure behavior, verification/completion, and
  an output contract.
- 28/28 have a research provenance note and at least one reachable reference.
- Every `SKILL.md` reference is linked from the runtime workflow and resolves.
- Five scripts are executable, syntax-valid, and wired to the skill that owns
  them; the one asset is referenced by `blueprint`.
- No stale `(planned)` language, sibling filesystem dependency, or hardcoded
  runtime requirement remains in the 28 skill packages.
- The research **Where encoded** rows were checked against current runtime
  content; one unsupported numeric over-routing claim was removed while
  preserving the evidence-backed restraint.

## Separation from proof

Existing routing results, workflow evidence infrastructure, and benchmark
fixtures remain documented under [evaluations](evaluations.md) and
[benchmarks](benchmarks.md). They are not used here to claim comparative
quality, cross-model superiority, or benchmark performance.
