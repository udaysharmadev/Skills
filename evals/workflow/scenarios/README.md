# Workflow scenarios

Per-skill scenario specs with **deterministic assertions first**
(file exists, command exits zero, artifact shape, forbidden-claim
absence), model-graded rubrics only for genuinely qualitative
dimensions — stored rubric, blind grading, human review possible, never
described as ground truth.

| File | Skills | Scenarios | Status |
| --- | --- | --- | --- |
| `scenarios/signature-skills.md` | hotseat, polish, unslop, blueprint, harden, frugal, frontpage | 21 (happy/edge/failure each) | authored; execution wired per-agent in 0.8 |

Target coverage for v1.0 eval completeness: all 27 skills × 3 scenarios
(≥ 81). Authored ≠ executed: a scenario only counts as coverage once a
runner has executed it against a real agent and stored results.
