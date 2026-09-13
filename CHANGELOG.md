# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is semantic.

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
