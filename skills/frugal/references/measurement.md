# Measurement rules: the honesty framework for savings claims

Research context (PRD §6.25): token consumption varies enormously
between agents and more tokens do not automatically mean better
outcomes: which is exactly why the KPI is **successful task token
cost**, not raw minimization.

## The four categories

| Category | Meaning | Allowed phrasing |
| --- | --- | --- |
| **Measured** | Runtime/provider-supplied usage numbers compared across runs | "input tokens: 48,200 → 21,700 (usage fields, same task, same model)" |
| **Derived** | Reduction computed from known content with an explicit tokenizer or byte/char proxy | "context bytes read: 812KB → 96KB (−88%, byte counts from file sizes)" |
| **Estimated** | Counterfactual estimate, labeled and based on stated assumptions | "estimated ~40% fewer tokens (assumes median file 300 lines, based on 12 sampled reads)" |
| **Unknown** | Cannot honestly be measured | "savings unknown: no usage telemetry this session" |

**Never** print "saved 63% of tokens" without the category and its
evidence. An uncategorized percentage is a violation of this skill, not
a rounding choice.

## Metrics worth tracking (when the runtime exposes them)

- input tokens / output tokens / cache-read / cache-write;
- context bytes read (files opened, lines retrieved);
- command-output bytes before/after capping;
- tool calls per task; retries per task;
- **task success**: the multiplier on everything: a saving that costs
  a retry is a loss.

## Baseline discipline

- Compare like with like: same task, same model, same data; state what
  differed.
- One-variable changes (cap the logs OR range-read, not both) when the
  goal is attribution; bundle when the goal is just "do the task
  cheaper": say which goal.
- Cache-prefix savings only count when the runtime actually caches,
  verify, don't assume.

## Where this skill's own budget applies

- Session handoffs and context compaction: load the smallest set of current,
  decision-relevant evidence.
- This suite's own SKILL.md files follow the Agent Skills 500-line structural
  limit, with conditional detail loaded from references.
