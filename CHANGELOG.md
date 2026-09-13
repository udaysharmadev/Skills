# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is semantic.

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
