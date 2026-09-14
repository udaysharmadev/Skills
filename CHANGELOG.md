# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is semantic.

## [Unreleased]

### v1 campaign — Phase 0 truth-freeze, Foundation Phase 1, `handsfree` depth

- Added `docs/audits/current-state.md`: frozen truth at `96b4646` with
  PASS / PARTIAL / BLOCKED / LEGACY / UNVERIFIED verdicts. Layer C outcome
  evidence is `UNVERIFIED` for all 28 skills; no benchmark claim is made.
- Added `docs/research/SOURCES.md`: version-verified primary citations
  (Antigravity modes, Gemini CLI approval/policy engine, Agent Skills spec,
  skills.sh CLI, Anthropic harness work), all re-verified 2026-09-14.
- Rewrote `docs/research/handsfree.md` against primary URLs with exact
  `Where encoded` traces; recorded rejected ideas (zero-prompt marketing,
  settings widening, permission laundering).
- Deepened `skills/handsfree/` to the autonomy-governor contract:
  AUTO / AUTO+CHECKPOINT / ASK ONCE / BLOCKED classes, checkpoint and
  retry budgets, dirty-tree preservation, host-mode detection, adversarial
  gate ("never ask me" never waives BLOCKED), completion predicate.
- Added canonical contracts `shared/evidence/`, `shared/risk/`,
  `shared/schemas/claim.md`, `shared/generated/` (maintainer-side only;
  runtime self-containment unchanged).
- Added `docs/claims.md` (9 rows: FACT/MEASURED/DERIVED/UNVERIFIED) and
  validators `validate-frontmatter`, `check-claims`, `check-readme-sync`,
  all wired into CI.
- Authored `handsfree` evidence scaffolding, all `UNVERIFIED`: 5 workflow
  scenarios (HF1–HF5), outcome protocol (O1–O2) in `evals/outcomes/`,
  evidence page `docs/benchmarks/handsfree.md`.
- Cleared 27→28 staleness across PRD, CONTRIBUTING, scorecard (new
  `handsfree` row), skill guides, research index, evals targets, and the
  compatibility install note (28-skill install re-verification tracked as
  C-004, still pending).

### v1 campaign — Skill Phase 01 `concierge` (first executed outcome evidence)

- Closed three audit gaps without touching the rejected manifest idea:
  28/28 completion-predicate table, `handsfree` / direct / none pattern
  rows, and a loop ceiling (same domain ≤ 2 dispatches) in
  `skills/concierge/`.
- Added `scripts/eval-outcome`: stdlib-only baseline-vs-treatment runner
  with deterministic grading, provenance, and gitignored raw traces.
- Executed `concierge` Layer C: codex O1 treatment 4/4 vs baseline 1/4
  (failures = `backend` over-route), O2 direct 7/7 both, held-out O3 both
  pass with treatment matching the documented chain; opencode replication
  2/2 both on O1 (baseline minimal, treatment full). Verdict: **MIXED** —
  see `docs/benchmarks/concierge.md`. Claim C-010.

## [0.9.0] — 2026-09-14

### Productization and documentation

- Completed a folder-by-folder audit of all 27 skills, their research
  traceability, references, scripts, assets, capability fallbacks, and output
  contracts; corrected the remaining unsupported research wording and helper
  documentation drift.
- Rebuilt the root README as the product landing page with an above-the-fold
  install path, lifecycle model, grouped skill catalog, concrete differentiators,
  natural-language examples, progressive-disclosure architecture, research,
  compatibility, and trust guidance.
- Added a documentation home, beginner skill chooser, workflow recipes,
  human-facing 27-skill guide, and grouped research provenance index.
- Expanded the repository architecture documentation around discovery,
  routing, progressive disclosure, capability fallbacks, handoffs, artifact
  ownership, memory, provenance, and deterministic helpers.
- Replaced the stale scorecard with current implementation, research, tooling,
  documentation, and evaluation statuses kept as separate dimensions.
- Added two focused issue forms and a concise pull request template; updated
  contribution and security guidance for research-backed behavior changes.
- Extended local-link validation across public Markdown and made the generated
  skill index follow lifecycle order.

Empirical outcome benchmarking remains intentionally deferred to the proof
phase. This release makes no comparative performance claim and is not v1.0.

## [0.8.6] — 2026-09-14

### Phase 8 evaluation recovery

- Added `scripts/eval-workflow`, a standard-library evidence runner that
  requires explicit scenario selection before live agent invocation, hides
  assertions from the evaluated agent, records dirty-tree provenance and
  archives produced artifacts. Results remain ungraded until a real grader
  evaluates them.
- Made all 21 signature-skill scenarios independently runnable by separating
  setup/task input from hidden checks; corrected the ambiguous single-turn
  `hotseat` cheerleading scenario.
- Extended deterministic eval validation to workflow scenario structure and
  corrected documentation that previously claimed execution was already
  wired.
- Executed one final Codex/gpt-5.6-sol H3 trial. Raw evidence is stored
  locally; no workflow pass rate is claimed.
- Fresh-context review found and resolved artifact-durability, setup parsing,
  provenance, full-skill-package, progressive-disclosure and evidence-wording
  issues. `shellcheck` was unavailable locally and remains unverified.

## [0.8.5] — 2026-09-14

### Phase 8, Batch E — cleanup & public-quality depth

- **unslop**: measurable-effects tracking (deps removed, duplication
  merged, tests preserved) explicitly subordinated to judgment; the
  keep-list (intentional duplication, compatibility hacks, load-bearing
  weirdness) promoted to first-class report content.
- **janitor**: remote audit extended — issue/PR templates, CODEOWNERS,
  dependency automation, changelog/release-notes quality; description
  typo fixed.
- **frontpage**: snippet verification re-runs the README text verbatim;
  anchor/code-fence checks; the reader-question order (why care → what
  is it → see it → try it → trust it → deeper) and stated-limitations
  rule.
- **findable**: findings classified as confirmed issue / content
  opportunity / speculative suggestion — only confirmed issues get fix
  treatment.
- **frugal**: the budget model (task-critical / useful / optional /
  waste) — optimization targets optional and waste only, which is what
  stops token-saving from becoming evidence-skipping.

### Phase 8, Batch F — release & operations depth

- **cleared**: every dimension row carries status, evidence, risk and
  owner/action; "not checked" formally not-pass.
- **runway**: deployment-strategy selection follows platform and risk
  (rolling default; blue/green/canary only where supported and risky);
  CDN/cache state in verification (fingerprint through the public URL);
  anti-enterprise-cosplay rule stated.

Context: SKILL.md median 1204 → 1352 tokens across the expertise pass —
+148 median, every addition decision-bearing; references +9KB.

## [0.8.4] — 2026-09-14

### Phase 8, Batch D — proof & engineering-quality depth

- **proof**: flaky-test diagnosis ladder (shared state → timing → real
  races → unordered data → external), property-based testing guidance
  (where invariants earn generators).
- **sleuth**: hypothesis-tracking table (evidence for/against, next
  discriminating experiment); five-part causal chain — symptom,
  mechanism, root cause, trigger, contributing condition; workaround
  explicitly distinguished from root-cause fix.
- **referee**: five-part findings (adds `confidence: certain | likely |
  possible` with what would confirm possibles); the honest empty review
  documented as a valid verdict.
- **harden**: six scoped modes (quick review, feature threat model,
  full audit, pre-release, auth/authz review, API review); findings
  gain the `attack precondition` field — what the attacker actually
  needs.
- **roadtest**: `scripts/test-matrix` — decide paths × viewports × state
  checks before walking; deep-link, refresh-mid-flow and authenticated
  sessions added; screenshot discipline rule.
- **hotpath**: `scripts/measure-report` — delta computation that
  enforces honesty (conditions required, sub-threshold labeled NOISE,
  no invented percentages); measurement-quality rules inlined.

## [0.8.3] — 2026-09-14

### Phase 8, Batch C — design & UX depth

- **polish**: six contextual modes bounding the diff (subtle polish /
  full redesign / dashboard / landing page / mobile-first /
  design-system cleanup); anti-slop rules nuanced to their actual
  principle (ban the default decoration, not the technique); dark mode
  as a separate design surface with its own contrast checks.
- **friction**: findings classified by concern (usability /
  accessibility / visual design / conversion-product) with different
  owners and fix paths; information scent, cognitive load,
  progressive-disclosure, trust-signal and i18n dimensions added.
- **ditto**: fidelity measured across nine named dimensions (structure,
  geometry, typography, color, spacing, assets, responsive, interaction,
  states) reported per-dimension; multi-reference input (desktop+mobile
  pairs upgrade responsive from inferred to observed).

## [0.8.2] — 2026-09-14

### Phase 8, Batch B — building & architecture depth

- **pilot**: per-slice change-risk classification (low/medium/high by
  blast radius — data/auth/money/schema/infra) setting the verification
  floor; rollback points before high-risk slices; plan-deviation
  recording in the plan file; pre-existing test failures distinguished
  from self-caused ones.
- **backend**: circuit-breaker behavior for failing dependencies;
  multi-tenancy as a data-layer invariant (tenant scoping from the
  authenticated principal, never a client id; RLS or checked
  repository layer); storage/files section (server-side validation,
  private-by-default object storage, signed URLs, streaming).
- **blueprint**: per-component architecture reasoning in the README
  (responsibility, boundary, dependency direction, data owned, failure
  mode, security boundary); `scripts/validate-mermaid` — static syntax
  checker for .mmd sources (diagram type, balanced delimiters, duplicate
  node ids, empty labels, tabs); HTML template gains Decisions and
  Glossary sections.
- **headroom**: explicit capacity-estimation arithmetic method (peak
  factor, fan-out, storage growth, headroom rule); traffic-pattern and
  durability dimensions; hot keys; load shedding with a shed-order
  decision.

## [0.8.1] — 2026-09-14

### Phase 8, Batch A — core intelligence depth

- **Maturity scorecard** (`docs/scorecard.md`): all 27 skills scored on
  the 11-dimension rubric (median 84.5 — honest "strong", not yet
  "professional"; gaps named per skill).
- **concierge**: intent × lifecycle routing layer (fix vs audit vs
  redesign vs teach vs research), evidence-reuse rules, gate-conflict
  and mid-workflow handling — smallest-sufficient-workflow made explicit.
- **hotseat**: persona cards rebuilt as distinct decision frameworks
  (what each optimizes for, their bias, the question only they ask,
  evidence they demand, red flags, what changes their mind); five modes
  (quick challenge / full / technical / product / pre-mortem); synthesis
  now converges via assumption register, MVP cut line, kill criteria.
- **spelunk**: `scripts/inventory` — one deterministic invocation
  replaces ~15 look-around calls (file distribution, largest files,
  TODO debt, test/source ratio, churn hotspots); risk-map mode;
  observed/inferred/unknown labeling.
- **scout**: conflict-resolution rules (recency × authority), outdated-
  advice detection, API stability classification, alternatives
  comparison with explicit criteria and a stated decision rule.
- **distill**: brief depth scaled to request type (tiny task →
  greenfield); non-functional requirements included only when they bite;
  backward-compatibility/migration notes when data is affected.
- **masterplan**: two planning depths (lightweight vs full, chosen by
  blast radius); invariants recorded before decisions; sequencing
  upgraded to must-precede / can-parallelize / can-postpone.
- **recall**: knowledge-type taxonomy (fact/decision/status/hypothesis/
  lesson/constraint/preference/superseded); decision entries capture
  consequence + supersedes; `scripts/check-memory` — structural
  consistency validator (caps, dated entries, duplicates, STATUS
  staleness, dump smell).

Context cost: SKILL.md median 1204 → 1212 tokens (+8; depth went into
references/scripts, per progressive disclosure).

### Review status for this batch

Independent fresh-context review **unavailable** (reviewer quota
exhausted). A structured self-review was run instead — disclosed per the
referee self-review contract — and fixed 5 findings before commit (dead
logic in the inventory script, extension-extraction bug, stale
"(planned)" reference, template/SKILL.md drift in distill, pronoun
error). Trigger evals show no regression (codex smoke 0.917, same known
confusion). A fresh-context review of Batch A should run before v1.0.

## [0.7.0] — 2026-09-14

### Added

- **Measured evaluation layer** (`scripts/eval-trigger`): portable
  trigger-eval harness with capability-detecting agent adapters
  (UNAVAILABLE/UNVERIFIED semantics, stdin-safe invocation), 168 cases
  across three suites (`cases`, `sibling-confusion`, `router-stress`),
  provenance-stamped JSON results, budget tiers (smoke/standard/release)
  and dry-run mode.
- **First measured results** (raw JSON committed under `evals/results/`):
  stratified routing smoke (12 cases, 12 distinct skills + a negative) —
  Codex (gpt-5.6-sol) accuracy 0.917 (sole miss: a trivial-styling
  request routed to `polish`), OpenCode 1.0; sibling-confusion suite
  20/20 on Codex. Harness fixes from independent review: neutral
  working directory (answer-key contamination impossible), chain cases
  counted in accuracy, annotation-tolerant answer parsing,
  agent-version + model provenance, stratified tier sampling.
- **Installation evidence**: `npx skills add udaysharmadev/Skills --all`
  verified against the public skills CLI — all 27 skills installed into
  a clean directory.
- **Context-footprint audit** (`scripts/check-context`): median ≈1,190
  tokens per SKILL.md, zero outliers, all files within the 500-line
  contract.
- **Benchmark fixtures with private answer keys**: `ts-dashboard`
  (10 seeded issues), `py-notes-api` (5 seeds), `ugly-dashboard.html`
  (polish target) + baselines (`benchmarks/`).
- **Workflow scenarios**: 21 specs across the 7 signature skills
  (happy/edge/failure), deterministic assertions first.
- **CI** (`.github/workflows/ci.yml`): deterministic checks on every
  PR; live agent evals manual-dispatch only.
- **Docs**: evaluations, benchmarks, cross-agent compatibility matrix
  (fill-by-evidence semantics), cross-skill handoff contract, name
  collision audit (sampled, honestly scoped), brand options.

### Changed

- `hotseat` personas restored to the original product intent (Aanya,
  Kabir, Meera, Arjun, Naina, Rohan, Ishaan) across SKILL.md, persona
  cards and PRD — reasoning lenses unchanged.
- Stale "planned" references removed from shipped skills; README rebuilt
  from verified facts only (frontpage methodology, dogfooded).
- Prompt-injection defenses made explicit in all content-consuming
  skills (scout, janitor, frontpage, roadtest; ditto already had them).

## [0.6.0] — 2026-09-14

### Added

- Phase 6 "Shipping" skills — the suite is complete at 27:
  `cleared` (evidence-based go-live gate — READY / READY WITH WARNINGS /
  BLOCKED with per-dimension weights and remediation), `runway`
  (platform-agnostic deployment — preflight, preview-first, version
  fingerprint, smoke tests, logs, HTTPS checks and a named rollback
  path; Vercel first-class, Docker/VPS/static/k8s/mobile in references).
- `concierge` routing covers the full suite; trigger cases (132).

## [0.5.0] — 2026-09-14

### Added

- Phase 5 "Cleanup & public surface" skills: `unslop` (behavior-
  baselined repo detox with a slop catalog and batch protocol), `janitor`
  (git/GitHub hygiene with authorization-gated destructive ops),
  `frontpage` (claims-audited README generation with executed
  quickstarts), `findable` (rendered-HTML SEO verification, anti-snake-
  oil stance), `frugal` (token efficiency with the measured/derived/
  estimated/unknown honesty framework).
- Artifact ownership complete for all 27 skills; trigger cases (120).

## [0.4.0] — 2026-09-14

### Added

- Phase 4 "Proof" skills: `proof` (boundary-choice testing with the
  boundary picker), `roadtest` (browser QA with evidence bundles and a
  three-rung capability ladder), `sleuth` (root-cause discipline with
  hypothesis playbook), `referee` (two-axis review, fresh-context
  preferred, nit-never-blocks), `hotpath` (measure-change-measure with
  per-layer tooling), `harden` (OWASP Top 10:2025 audit with
  severity + confidence finding format, safe-adversarial rules).
- `pilot`'s completion gate and `concierge`'s routing table now
  reference the shipped Proof skills directly.
- Artifact ownership for evidence/report bundles; trigger cases (100).

## [0.3.0] — 2026-09-14

### Added

- Phase 3 "Experience" skills: `polish` (anti-slop UI design with a
  full audit checklist and Core Web Vitals awareness), `friction` (UX
  audit — task walks, WCAG 2.2 anchors, severity-ranked findings),
  `ditto` (UI recreation with a mandatory compare-correct loop and an
  untrusted-content protocol for third-party pages).
- Trigger cases for all three (74 total).

## [0.2.0] — 2026-09-14

### Added

- Phase 2 "Building" skills: `pilot` (slice-by-slice plan execution with a
  completion gate), `backend` (universal server-side specialist),
  `blueprint` (architecture analysis with Mermaid + HTML deliverable),
  `headroom` (Now/Next/Scale design with trigger metrics).
- `blueprint` ships an HTML template asset (`assets/template.html`) with
  light/dark themes, zoomable diagrams and print support.
- Trigger cases for all four new skills (60 total).

## [0.1.0] — 2026-09-14

### Added

- Phase 0 foundation: repository scaffold, skill-file contract, shared
  contracts (principles, terminology, capability map), validator scripts
  (`validate-skills`, `check-names`, `check-links`, `build-docs`) and trigger
  eval fixtures.
- Phase 1 "Intelligence" skills: `concierge`, `hotseat`, `spelunk`, `scout`,
  `distill`, `masterplan`, `recall`.
- Product definition: [PRD.md](PRD.md) covering the full 27-skill v1 target,
  naming system and build sequence.
