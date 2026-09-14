# Claim record schema (canonical)

Every public quantitative or compatibility statement in `docs/claims.md`
carries exactly these fields. `scripts/check-claims` enforces presence;
reviewers enforce honesty.

| Field | Values / format |
|---|---|
| id | `C-###`, stable |
| statement | the exact public sentence |
| class | `FACT` · `MEASURED` · `DERIVED` · `ESTIMATED` · `TARGET` · `UNVERIFIED` |
| evidence | repo path to the proof (result file, log, screenshot) or `—` with a reason |
| verified | `YYYY-MM-DD` or `—` |
| reproduce | command/procedure, or `—` with a reason |
| stale-if | expiration condition (new release, new model version, 90 days for fast-moving modes) |

Class semantics: `FACT` = true by inspection (file exists, command runs).
`MEASURED` = runtime/provider telemetry from a real run. `DERIVED` =
computed from measured inputs via a stated method (e.g. byte proxy for
tokens — never dressed up as measured). `ESTIMATED` = counterfactual,
clearly labeled. `TARGET` = goal, never phrased as achievement.
`UNVERIFIED` = researched or asserted, not yet executed here.
