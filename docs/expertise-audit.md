# Historical expertise audit: v0.8.6

> This is the snapshot taken at the end of the Deep Intelligence Pass. Its
> implementation gaps were reconciled during the productization pass; use the
> [current scorecard](scorecard.md) for present status. Evaluation limitations
> below remain historical evidence and are intentionally deferred, not runtime
> defects.

Per-skill maturity table (before = pre-pass scorecard, after = post-pass
re-score). Scores stay honest: **Evaluation evidence remains the capped
dimension** (trigger evals measured; workflow trials may run locally, but
no graded workflow/outcome evidence is published — work for the deferred proof
phase). No score was
inflated past what behavior demonstrates; that is why nothing crosses 92 yet.

| Skill | Before | After | Biggest upgrade | Evidence | Remaining limitation |
| --- | --- | --- | --- | --- |---|
| concierge | 86 | 91 | Intent × lifecycle routing layer | routing table covers 22 patterns; smoke evals stable | multi-skill chains not yet eval-measured |
| hotseat | 77 | 89 | Personas as decision frameworks + 5 modes | distinct optimize-for/bias/mind-changers per card | no debate-quality eval (rubric unrun) |
| spelunk | 87 | 90 | `scripts/inventory` + risk-map mode + epistemic labels | script tested on this repo | recon quality unmeasured vs baseline |
| scout | 82 | 88 | Conflict resolution + API stability + alternatives method | source-ladder rules | no research-quality eval |
| distill | 80 | 87 | Request-type scaling; NFRs-when-they-bite | template synced with SKILL.md | brief quality unmeasured |
| masterplan | 85 | 90 | Invariants + must-precede/parallelize/postpone | template + SKILL.md consistent | plan quality unmeasured |
| recall | 85 | 91 | Knowledge taxonomy + supersedes + `scripts/check-memory` | validator run on fixtures | multi-session stress test pending |
| pilot | 88 | 90 | Risk classification, deviation recording | gate matrix unchanged (already strong) | workflow eval unexecuted |
| backend | 85 | 89 | Circuit breaking, multi-tenancy invariant, storage | checklists extended | stack-specific refs pending; no eval |
| blueprint | 82 | 89 | `scripts/validate-mermaid` + component reasoning + template sections | validator catches seeded bad diagram | render test (mermaid-cli) not wired |
| headroom | 85 | 89 | Capacity-estimation arithmetic + hot keys/shedding | dimensions.md | no worked measured example yet |
| polish | 82 | 88 | Six modes + principled anti-slop + dark-mode surface | mode table bounds diffs | visual benchmark not run |
| friction | 83 | 89 | Concern classification + scent/load/trust/i18n | dimension list | no before/after task walks recorded |
| ditto | 82 | 88 | Nine-dimension fidelity framework | per-dimension reporting rule | fidelity claims unmeasured |
| proof | 88 | 91 | Flaky ladder + property-based guidance | boundary-picker extended | no suite-quality eval |
| roadtest | 83 | 90 | `scripts/test-matrix` + deep-links/refresh/auth walks | generator tested | browser-run evidence pending |
| sleuth | 85 | 90 | Hypothesis table + five-part causal chain | format in SKILL.md | debugging eval unrun |
| referee | 85 | 89 | Confidence field + honest empty review | finding format extended | fresh-context mode unmeasured |
| hotpath | 85 | 90 | `scripts/measure-report` enforcing honesty | NOISE verdict on sub-threshold | no real benchmark pair run |
| harden | 86 | 90 | Six modes + attack-precondition field | finding format extended | seeded-fixture detection unrun |
| unslop | 84 | 88 | Measurable effects + first-class keep-list | report contract | rescue benchmark unrun |
| janitor | 83 | 87 | Templates/CODEOWNERS/deps-automation checks | remote audit list | gh-dependent; unmeasured |
| frontpage | 83 | 88 | Verbatim snippet re-runs + reader-question order | verification rules | claims-audit eval unrun |
| findable | 82 | 86 | Confirmed/opportunity/speculative separation | quality gates | rendered-HTML eval unrun |
| frugal | 85 | 90 | Budget model gating what may be optimized | model in SKILL.md | token benchmark unrun |
| cleared | 88 | 91 | Per-dimension risk + owner/action | gate table | no release-gate eval |
| runway | 83 | 88 | Strategy-by-platform + CDN fingerprint rule | deploy section | deploy eval impossible locally |

**Median: 84.5 → 89. Range: 86–91. Zero skills below 70.**

## Cross-skill audit (mechanical, all green)

- 27/27 skills carry "When NOT to use" + "Output contract" sections.
- 5/5 bundled scripts compile, parse, and are executable; each wired into
  its skill's workflow with a stated when-to-run.
- No routing chain exceeds 5 hops; no loops (chains are DAGs rooted at
  concierge).
- No skill writes an artifact owned by another (checked against
  `shared/terminology/artifacts.md`).
- Gates (`cleared`, `referee`) are read-only — they report, never mutate.

## The seven questions (short form)

1. Embarrassing professional omission? — Per-skill "remaining limitation"
   column; the systemic one is missing graded workflow evals.
2. Knowledge beyond generic LLM ability? — Yes where it counts: decision
   frameworks (hotseat personas, proof boundary table, headroom capacity
   arithmetic, frugal budget model), failure ladders (sleuth, unslop),
   honesty scripts (measure-report NOISE, validate-mermaid).
3. Better decisions, not longer responses? — Context median +148 tokens
   for the whole pass; depth went to references (85→94KB) loaded on demand.
4. Knows when NOT to act? — Every skill's exclusions section + gates'
   read-only rule + harden's authorization refusals.
5. Can verify its work? — 5 deterministic scripts + evidence-or-unverified
   language enforced in output contracts.
6. Fails honestly when tooling absent? — roadtest rungs, scout offline
   mode, ditto fidelity ladder, all unchanged and load-bearing.
7. Install individually? — Honest answer: 10 skills are individually
   compelling today (concierge, masterplan, recall, proof, sleuth, harden,
   hotpath, referee, unslop, frontpage); the rest are strong within the
   bundle but their solo value rests on evals not yet run. Not gaming
   this to "yes × 27".

## Research summary

The Deep Intelligence edits added domain decision frameworks. The subsequent
commits added one provenance note per skill under `docs/research/`; the
[research index](research/README.md) is now the durable entry point and its
**Where encoded** rows were checked against runtime files during productization.

The workflow-evaluation layer was checked against current primary guidance:

- [Anthropic's agent-evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  materially reinforced the task/trial/grader separation and preservation of
  raw evidence.
- The UK AI Security Institute's [Inspect log documentation](https://inspect.aisi.org.uk/eval-logs.html)
  informed provenance-rich, inspectable result records.

## New tooling

Phase 8 added five skill-bundled deterministic helpers: `spelunk` inventory,
`recall` check-memory, `blueprint` validate-mermaid, `roadtest` test-matrix,
and `hotpath` measure-report. This continuation adds project-level
`scripts/eval-workflow`: a standard-library-only, explicit-one-scenario
evidence runner with no surprise batch spend. It copies the full selected
skill package, preserves progressive disclosure, hides assertions and answer
keys, archives produced artifacts, and records dirty-tree provenance.

## Evaluation results

- Trigger routing, measured 2026-09-14: Codex smoke 11/12 (0.9167),
  OpenCode smoke 12/12 (1.0), and Codex sibling confusion 20/20 (1.0).
- Workflow runner structure: 21 scenarios across 7 signature skills pass the
  deterministic format check.
- H3 (`hotseat` cheerleading failure mode): one final Codex/gpt-5.6-sol trial
  executed successfully after two exploratory successful trials and one
  sandbox invocation error. The final raw output and artifact bundle are
  stored locally; grading remains formally `ungraded`, so no workflow pass
  rate is claimed.
- Outcome benchmarks remain unexecuted.

## Context impact

`SKILL.md` median moved from 1,204 to approximately 1,352 derived tokens
(+148); references moved from about 85KB to 94KB. The workflow runner adds no
always-on skill context and supplies only `SKILL.md` initially; references,
scripts and assets remain available on demand in the isolated workspace.

## Cross-stack and cross-agent status

- Fixtures exist for TypeScript/web, Python and a standalone HTML UI. Go/Rust,
  JVM and mobile fixtures remain missing; no Phase 8 cross-stack behavioral
  run is published.
- Codex and OpenCode routing are measured. Codex workflow invocation is now
  exercised for H3. Claude Code remains blocked by a local headless hang;
  Cursor and Antigravity are unavailable locally.
- A fresh-context review of the workflow-runner slice found eight concrete
  issues; artifact durability, adversarial setup loss, H3 test validity,
  dirty-tree provenance, skill-package completeness, progressive disclosure,
  evidence wording and sandbox claims were corrected before this audit.

## Verdict

**MOST PROFESSIONAL — ALL 27 NEED GRADED EVALUATIONS TO CROSS 92.**

The expertise pass closed the domain-judgment gap (decision frameworks,
failure awareness, deterministic tooling); what separates every skill
from the professional band is the same single dimension: measured
behavioral evidence (workflow + outcome evals need graded, repeatable runs;
the evidence runner is now available).
