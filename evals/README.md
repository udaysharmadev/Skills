# evals/

Evaluation assets. Nothing here may claim a number that was not
actually measured (PRD §3.4, §13).

| Directory | Purpose | Status |
| --- | --- | --- |
| `trigger/` | 206 routing cases: positive/negative, sibling-confusion, router-stress | **runner live** — `scripts/eval-trigger` |
| `adapters/` | per-agent invocation config + verification status | codex (gated: paid-agent guard) + opencode verified (live); claude unverified (headless hangs in dev env); cursor/antigravity UNAVAILABLE |
| `workflow/` | per-skill scenario specs, deterministic checks where possible | 133 scenarios authored (24 skills); evidence runner live, results ungraded by default |
| `outcomes/` | baseline-vs-skill outcome protocols + per-skill verdicts | `handsfree` protocol authored; `concierge` **executed** (MIXED); `hotseat` **executed** (PROVEN LIFT); `spelunk` + `scout` + `distill` + `masterplan` + `pilot` + `backend` + `blueprint` + `headroom` + `polish` + `friction` + `ditto` + `proof` + `roadtest` + `sleuth` + `referee` + `hotpath` + `harden` + `unslop` + `janitor` + `frontpage` protocols + graders authored, zero trials (zero-spend, no Codex) |
| `regression/` | field bugs captured as cases before fixes merge | populated as issues land |
| `fixtures/` | representative stack fixtures | superseded by `benchmarks/fixtures/` (kept for evals that want them) |
| `results/` | runner output JSONs (gitignored) | curated release evidence may be committed separately |

## Running

```bash
scripts/eval-trigger --check                          # capability table
scripts/eval-trigger --agent claude --tier smoke      # 12 measured cases
scripts/eval-trigger --suite all --agent claude --tier standard
scripts/eval-workflow --check
scripts/eval-workflow --scenario H3 --agent codex --allow-paid   # also needs ALLOW_PAID_AGENT=1 (paid-agent guard)
```

See `docs/evaluations.md` for methodology, budget tiers, and the honesty
contract. Results without provenance (agent, commit, date, invocation
status) may not be quoted anywhere.
