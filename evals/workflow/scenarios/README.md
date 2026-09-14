# Workflow scenarios

Per-skill scenario specs with candidate `D#` checks (deterministic where
possible) and `R#` rubrics for genuinely qualitative dimensions. Rubric
grading stays blind and reviewable; it is never described as ground truth.

| File | Skills | Scenarios | Status |
| --- | --- | --- | --- |
| `signature-skills.md` | hotseat, polish, unslop, blueprint, harden, frugal, frontpage | 21 (happy/edge/failure each) | authored; evidence runner available |
| `handsfree.md` | handsfree | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `concierge.md` | concierge | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `spelunk.md` | spelunk | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `scout.md` | scout | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `distill.md` | distill | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `masterplan.md` | masterplan | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `pilot.md` | pilot | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `backend.md` | backend | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `blueprint.md` | blueprint | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `headroom.md` | headroom | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `polish.md` | polish | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `friction.md` | friction | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `ditto.md` | ditto | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `proof.md` | proof | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `roadtest.md` | roadtest | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `sleuth.md` | sleuth | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `referee.md` | referee | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `hotpath.md` | hotpath | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `harden.md` | harden | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `unslop.md` | unslop | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `janitor.md` | janitor | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |
| `frontpage.md` | frontpage | 5 (normal/hard-edge/failure/restraint/adversarial) | authored; evidence runner available |

Target coverage for v1.0 eval completeness: all 28 skills × 3 scenarios
(≥ 84). Authored ≠ executed: a scenario only counts as coverage once a
runner has executed it against a real agent and stored results.

`scripts/eval-workflow --check` validates scenario structure. Live runs
require an explicit scenario id to prevent surprise token spend:

```bash
scripts/eval-workflow --list
scripts/eval-workflow --scenario H3 --agent codex
```

The runner preserves raw final output, input provenance, before/after
workspace manifests, and an archive of produced artifacts. It records
assertions as `ungraded`; execution alone is never reported as a pass.
