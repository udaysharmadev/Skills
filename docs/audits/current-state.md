# Historical current-state audit: Skills v1 campaign, Phase 0

> Superseded by the 28-skill release at commit `310dfec` on 2026-09-18.
> This is preserved evidence of the 2026-09-14 baseline, not a description of
> the current product. For current install and runtime information, use the
> repository README, generated skill index, and validators.

Frozen: 2026-09-14. Commit `96b4646` (`docs: add banner image to top of README and sync 28-skill index`).
Tree clean at freeze time. Auditor: OpenCode session (Muse Spark) under the
`SKILLS_V1_ANTIGRAVITY_EXECUTION_PROMPT.md` + `SKILLS_V1_MASTERPLAN.md` contract.

## Environment at freeze

| Fact | Value |
|---|---|
| Commit SHA | `96b46465041997ca6fdabb3f658c3e856d5bd9fd` |
| Branch | `main`, in sync with `origin/main` |
| Working tree | clean (`git status`, `git diff` empty) |
| Recent history | 20 commits visible; last 20 are skill-depth passes + `handsfree` addition + README/productization |
| Local runtimes (from `docs/compatibility.md`, measured 2026-09-14) | Codex 0.153.4 (gpt-5.6-sol) ✅ · OpenCode 1.18.30 ✅ · Claude Code 2.1.235 (headless hangs, unverified) · Cursor/Antigravity unavailable locally |
| Audit session | OpenCode + Muse Spark, darwin/arm64, python 3.14.6, bash 3.2 |

## Validators at freeze (all green)

| Check | Result |
|---|---|
| `scripts/validate-skills` | OK: 28 skill(s) valid |
| `scripts/check-names` | OK: single-word system |
| `scripts/check-links` | OK: bundled paths + local targets exist |
| `scripts/check-context` | pass with note: `hotseat` OUTLIER (~2174 tok vs ~1443 median; still far under the 5000-token spec budget — no action) |

## Inventory

- `skills/`: **28 folders**, each with `SKILL.md` + ≥1 `references/` file reachable from the body. 5 skill-owned scripts + 1 asset (`blueprint/assets/template.html`), all reachable and executable where required.
- `docs/research/`: 29 notes (28 skills + index). Every note carries a `Where encoded` trace (verified for the original 27 during productization; `handsfree` trace present but shallow — see Phase 28 gap).
- `evals/`: trigger runner + 168 routing cases in `evals/trigger/cases.md`; workflow runner + 21 authored signature-skill scenarios; raw results present locally (`evals/results/`, gitignored): Codex smoke 11/12 (0.917), OpenCode smoke 12/12 (1.0), plus ungraded H3 workflow trials.
- `benchmarks/fixtures/`: `ts-dashboard`, `py-notes-api`, `ugly-dashboard.html` with seeded defects + answer-key isolation (covers TS/web, Python, HTML; Go/Rust/Java/mobile fixtures absent — PRD §12 gap, deferred honestly).
- CI (`.github/workflows/ci.yml`): validate-skills, check-names, check-links, run-evals, build-docs drift, check-context. **Missing** (masterplan Phase 1 gap): frontmatter-strict validation, routing-manifest check, claims check, README-sync check.

## Verdicts (PASS / PARTIAL / BLOCKED / LEGACY / UNVERIFIED)

| Area | Verdict | Note |
|---|---|---|
| 28-skill runtime structure | **PASS** | 28/28 folders valid, self-contained, ≤500 lines, frontmatter names match dirs |
| Skill-file contract (PRD §8) | **PASS** | purpose, triggers, when-NOT, prerequisites/workflow, fallback, gates, stop, output, reference pointers present |
| Research provenance | **PARTIAL** | 27/27 traced; `handsfree` note exists but cites no primary URLs and references `SKILL.md` rule numbers that do not exist in the current file |
| `handsfree` vs special contract | **PARTIAL** | autonomy-governor shape present (antigravity.md + decision-policy.md are good); SKILL.md itself is 56 lines and **lacks** AUTO/AUTO+CHECKPOINT/ASK-ONCE/BLOCKED classes, checkpoint/budget/loop rules, dirty-tree preservation, host-mode detection procedure, adversarial gate ("never ask me" + destructive request), completion predicate |
| Routing/activation evidence (Layer A) | **PARTIAL** | trigger cases + live runners + Codex/OpenCode smoke results exist; `handsfree` trigger cases present (9); full 28-skill standard-tier + held-out runs not executed |
| Workflow evidence (Layer B) | **PARTIAL** | 21 scenarios authored for 7 signature skills; results ungraded by default; 21/28 skills have no authored workflow scenarios |
| Outcome evidence (Layer C) | **BLOCKED** | intentionally deferred to the proof phase; **zero** baseline-vs-skill outcome trials executed for any skill — every skill is `UNVERIFIED` at Layer C |
| Held-out + composition suites | **BLOCKED** | held-out set not frozen; bundle composition cases (multi-skill, mid-workflow, misleading, risky, long-running) not authored |
| Claims system | **BLOCKED** | no `docs/claims.md`; README currently honest (makes no benchmark claim) — must stay that way via CI |
| Benchmark docs | **PARTIAL** | `docs/benchmarks.md` + `docs/evaluations.md` describe methodology honestly; per-skill evidence pages (`docs/benchmarks/<skill>.md`) + dashboard do not exist |
| Compatibility matrix | **PARTIAL** | Codex/OpenCode measured; Claude/Cursor/Antigravity unverified/unavailable; install command verified for **27** skills pre-`handsfree` — 28-skill install **not yet reverified** |
| 27→28 staleness | **LEGACY** | tree says 28 in validators/README-index but PRD status, CONTRIBUTING ("frozen at 27"), `docs/skills/README`, `docs/scorecard`, evals coverage target, compatibility install note still say 27 |
| Context budget | **PASS** | total SKILL.md 159KB, references 114KB, frontmatter ~3525 tok always-on; only `hotseat` flagged, within spec |
| Supply-chain hygiene | **PARTIAL** | validators check executability/reachability; no path-traversal/symlink/secret/egress audit in CI; skills.sh security review pending indexing |
| Public surface | **PARTIAL** | README honest + banner present; issue forms, PR template, SECURITY, CONTRIBUTING exist; topics/social-preview/releases/pins unverified from here |

## Stale-marker scan

No live `TODO`/`FIXME`/`coming soon` in shipped skill packages (only legitimate
mentions: TODO-debt as a `spelunk` signal, placeholder-data handling in
`ditto`/`friction`/`blueprint`, "planned slice" in `pilot`). The staleness is
structural (27 vs 28), not textual — tracked as LEGACY above.

## What this audit authorizes

Phase 1 (contracts + missing validators + claims system), Phase 2 (eval
harness + held-out freeze), Phase 3/`handsfree` depth pass first (dogfood
autonomy early), then skill phases in masterplan order starting at
`concierge`. No README marketing changes and no v1.0 tag until the release
gate is genuinely met. Anything already better than the plan is preserved.
