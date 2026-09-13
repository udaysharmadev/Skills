# evals/

Evaluation assets. Nothing here may claim a number that was not
actually measured (PRD §3.4, §13).

| Directory | Purpose | Status |
| --- | --- | --- |
| `trigger/` | 168 routing cases: positive/negative, sibling-confusion, router-stress | **runner live** — `scripts/eval-trigger` |
| `adapters/` | per-agent invocation config + verification status | codex + opencode verified (live); claude unverified (headless hangs in dev env); cursor/antigravity UNAVAILABLE |
| `workflow/` | per-skill scenario specs, deterministic assertions first | 21 scenarios authored (7 signature skills); execution wired 0.8 |
| `regression/` | field bugs captured as cases before fixes merge | populated as issues land |
| `fixtures/` | representative stack fixtures | superseded by `benchmarks/fixtures/` (kept for evals that want them) |
| `results/` | runner output JSONs (gitignored) | curated release evidence may be committed separately |

## Running

```bash
scripts/eval-trigger --check                          # capability table
scripts/eval-trigger --agent claude --tier smoke      # 12 measured cases
scripts/eval-trigger --suite all --agent claude --tier standard
```

See `docs/evaluations.md` for methodology, budget tiers, and the honesty
contract. Results without provenance (agent, commit, date, invocation
status) may not be quoted anywhere.
