# hotseat — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Unresolved citation — v1 notes label it "ACL 2026: Demystifying Multi-Agent Debate" but no URL/DOI resolves as of 2026-10-17; treat as hypothesis, not provenance | Homogeneous LLM debate converges toward the same answer regardless of rounds; diversity at initialization is the critical variable | Convergence-detection check kept in round-1 synthesis as a cautious heuristic | SKILL.md §round-1, §honesty rules, personas.md moderator |
| Teresa Torres, Continuous Discovery Habits (productalk.io) | Assumption testing is more efficient than idea testing; rank assumptions by kill probability and test urgency | Assumption register now includes urgency tiers | SKILL.md §synthesis §2, personas.md moderator format |
| Gary Klein, Pre-mortem technique (HBR 2007 + practical 2025 sources) | Past-tense failure framing bypasses optimism bias; independent silent generation prevents "boss effect" suppression | Full pre-mortem mode added with prospective hindsight mechanics | SKILL.md §pre-mortem section |
| Product Talk — Teresa Torres on kill criteria | Kill criteria must be specific and falsifiable; "low engagement" is not a kill criterion | Kill criteria format specified with threshold + timeframe requirement | SKILL.md §synthesis §7, personas.md moderator |
| v1 campaign audit, Phase 02 (2026-09-14) | Synthesis had no decision matrix; minority dissent could smooth into consensus by omission | Options × verdicts matrix (scoreless — voting stays banned) and a mandatory minority-objections-or-why-empty section | SKILL.md §synthesis items 2+5, §quality gates; personas.md moderator |

## Key new intelligence encoded

1. **Convergence detection (cautious heuristic, provenance unresolved — see above)** — after round 1, if ≥4 personas agree with similar reasoning, flag it as potential echo-collapse and either disclose or run sharper round 2
2. **Pre-mortem as distinct mode** — Gary Klein's prospective hindsight technique: past tense, silent independent generation, grouped by probability × severity
3. **Assumption register priority** — ranked by kill probability with urgency tiers: test before build / test during build / monitor post-launch
4. **Falsifiable kill criteria format** — must include metric, threshold, timeframe, and minimum cohort size
5. **MVP cut line with re-entry conditions** — deferred items must have a specific condition for reinstatement, not just "later"
6. **Per-persona round-2 attack angles** — each persona card now names what they specifically target in cross-examination

## Rejected ideas

| Idea | Why not adopted |
| --- | --- |
| Fixed weight/score per persona | Introduces fake quantification; judgment is more honest |
| "Audience size" field in persona verdicts | Cross-cuts all personas; addressed by Aanya's domain |
| Voting mechanism (majority vote outcome) | Collapses disagreement; synthesis is richer |

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Multi-agent debate research | Du et al. 2023 (arxiv 2305.14325, verified); one v1 "ACL 2026" citation unresolved — see hypothesis note above |
| Teresa Torres assumption testing | productalk.io / Continuous Discovery Habits book |
| Gary Klein pre-mortem | HBR Nov 2007; revalidated in 2025 practitioner sources |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Independent lens packet, option discipline and bounded rounds are useful; mandatory two corrections and numerical kill criteria incentivize fabricated objections; premortem example fabricates rates.

**Concrete case and proposed change:** Permit evidence-supported zero corrections; owner-grounded thresholds or discriminating qualitative observation; label future failures hypothetical; preserve seven lenses without compulsory deployment.

**Why this change:** HS3/HS5/HS6 test useful decisions instead of objection counts and arbitrary precision.

**Historical interpretation:** Historical PROVEN LIFT label is untouched and scoped to its old debate/decision-marker tasks; new calibration behavior has no comparative run. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Two-correction quota creates unsupported objections [local rule defect].
2. Numeric kill criterion lacks economic basis [local rule conflict].
3. Hypothetical premortem rates read as data [local example defect].
4. Same unsupported premise repeated seven times [existing documented risk].
5. Serialized lenses claimed independent agents [existing fallback risk].
6. Persona opinion claimed customer research [existing prohibited risk].
7. Strong idea forced into manufactured dissent [hypothesis].
8. Unsettled buyer versus user economics omitted [hypothesis].
9. Market-size estimate invented to settle debate [existing prohibited risk].
10. Mobile game inherits SaaS metrics [hypothesis].
11. Security rhetoric becomes unsupported veto [existing documented risk].
12. Founder constraints replaced by grander product [existing documented risk].
13. Third round repeats without new evidence [existing stop risk].
14. Approved execution task reopened as debate [existing negative case].
15. User stop overridden to finish synthesis [existing interruption case].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Improving Factuality and Reasoning through Multiagent Debate](https://arxiv.org/abs/2305.14325) — Yilun Du et al.; empirical research | 2023-05-23; arXiv 2305.14325 v1 | Multiple judgments can be tested before synthesis; applied only to this skill's decision boundary | Does not validate seven fictional product personas | `skills/hotseat/SKILL.md` | Relevant source, environment or criterion changes |
| [brainstorming SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Distinguish settled work from missing product choices; applied only to this skill's decision boundary | Broad trigger/approval gate is not adopted | `skills/hotseat/SKILL.md` | Relevant source, environment or criterion changes |
| [SkillsBench](https://arxiv.org/abs/2602.12670) — Xiangyi Li et al.; empirical research | 2026-02-13; revised 2026-06-14; arXiv 2602.12670 v4 | Focused skills warrant testing against broad bundles; applied only to this skill's decision boundary | Aggregate results do not establish this skill lift | `skills/hotseat/SKILL.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/hotseat/SKILL.md` | Relevant source, environment or criterion changes |
| [Skills that never fire discussion](https://www.reddit.com/r/ClaudeAI/comments/1usls7m/anyone_else_has_a_graveyard_of_claude_code_skills/) — ProperAssociation322 and _suren on Reddit; community anecdote | Relative age only; exact date unverified; fetched post and one visible reply | Overlap and invocation count are different concerns; applied only to this skill's decision boundary | Selection bias; not measured activation evidence | `skills/hotseat/SKILL.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | HS3/HS5/HS6 test useful decisions instead of objection counts and arbitrary precision. | Local contradiction is not a live model result | `evals/workflow/scenarios/hotseat.md`; `docs/benchmarks/hotseat.md` | Content or grader change |

### Adopted and rejected

- Adopted: Permit evidence-supported zero corrections; owner-grounded thresholds or discriminating qualitative observation; label future failures hypothetical; preserve seven lenses without compulsory deployment.
- Preserved: existing workflow, valuable references and historical outcomes; narrow additions load only at relevant boundaries.
- Rejected: mandatory broad workflows, fixed counts, unscoped transport trust or stronger performance claims unsupported by task evidence.
- Competitor behavior inspected: superpowers planning/inline execution and brainstorming expose concrete interfaces and progress identity, but also mandatory subskills, per-task TDD or approval ceremonies. Adopt the useful evidence boundary; reject sibling-file dependence and unconditional ceremony. MIT license checked; no instruction text copied. skills.sh entry is discovery metadata, not a behavioral benchmark.

### Access and research limits

The skills.sh writing-plans listing and upstream SKILL.md were read; listing
summary and current upstream instructions differ, so behavior comes from the
upstream file. The GitHub issue query and supplied X post returned access
errors. A candidate mattpocock grill-me raw path returned 404; no behavior or
license claim is inferred. The initial MCP security URLs errored; the older
versioned URL redirected to the fetched 2025-11-25 security tutorial. Reddit
post and one visible reply supply anecdote only, with exact post date unknown.

This pass has focused sources and local failures. It does not complete eight
to fifteen high-quality sources or independent issue/community triangulation
for every skill. Non-English, mobile/game and long-running concurrency cases
are authored hypotheses until fixtures/runs exist. Refresh those gaps before
release claims rather than padding the bibliography.

### Verification and remaining outcome gap

- Cases: `evals/workflow/scenarios/hotseat.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| HBR premortem source checked for attribution only; horizon is own-text design choice | Fixed 18-month horizon labeled as adjustable default; facilitation wording beyond that unverified. |
