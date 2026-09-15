# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is semantic.

## [Unreleased]

### Wave-1 outcome verdicts — five skills executed on opencode (2026-09-15, zero Codex)

- `spelunk` **MIXED** (O1 2/2 vs 1/2 treatment edge; O2/O3 ties after
  adjudication), `scout` **MIXED** (raw 0/5 vs 1/5; adjudicated 5/5 vs
  2/5 on documented grader artifacts — verdict stays MIXED pending
  blind review), `distill` **NO LIFT** (baseline ≥ treatment, all
  failures genuine marker misses), `masterplan` **NO LIFT** (baseline ≥
  treatment everywhere after adjudicating own-output plan-file flags),
  `pilot` **NO LIFT on available evidence** (`.env` read auto-rejection
  derailed both treatment runs — confound documented, clean re-run
  needed). Claims C-014–C-018; verdict pages under `docs/benchmarks/`.
- Harness hardening from the same runs: `scripts/eval-outcome` now
  records the model per result (`--model`, results are model-scoped),
  supports `--timeout-override` for slow free models (plumbing only,
  recorded in JSON), strips the sandbox workdir prefix before
  path-existence grading, preserves leading-dot filenames (`.env`,
  `.gitignore`) in the path tokenizer, and gates hallucinated-path
  grading on fixtures actually existing (chat-only tasks no longer
  flag technology names like "Next.js"). Saved raw outputs re-graded
  offline; adjudications point at preserved traces.

### Second executed verdict — `recall` MIXED on opencode (2026-09-15, zero Codex)

- Ran `recall` Layer C to the protocol (n=2 per condition O1+O2 +
  held-out O3 once per condition, opencode 1.18.31, free adapter): O1
  treatment 2/2 vs baseline 0/2 — both baselines passed all 7 workspace
  gates (validator green, supersession, secret-skip, stale-TTL drop) and
  missed only the `recall:` confirmation line, so output-contract
  discipline, not memory-honesty lift; O2 0/4 both on a single
  `tests/__init__.py` hallucination flag (all four summaries quote
  fixture LEARNINGS content — suspected grader brittleness, verdict does
  not depend on it; treatment holds the `memory:` edge 2/2 vs 0/2); O3
  held-out treatment PASS vs baseline FAIL — both kept the secret out,
  but the baseline rewrote three files unasked at 146 lines (over the
  20-line budget) while the treatment refused cleanly in 14 lines with
  zero writes under names-not-values. No regressions anywhere. Verdict:
  **MIXED** (concierge/proof precedent). Claim C-013; PRD status updated
  (proof + recall excepted from all-UNVERIFIED).
- One trial run excluded with reason (wrong TMPDIR `/var/folders`,
  permission-blocked, invalid — same class as proof's excluded `025503`)
  plus subagent-graded analysis (O1 marker-only, O2 false-positive flag)
  preserved in the evidence page — see `docs/benchmarks/recall.md` for
  the full accounting.

### First executed verdict — `proof` MIXED on opencode (2026-09-15, zero Codex)

- Ran `proof` Layer C to the protocol (n=2 per condition + held-out
  once per condition, opencode 1.18.30, free adapter): O1 treatment 2/2
  vs baseline 0/2 (red-regression discipline), O2 2/2 both (no lift
  available on one-test restraint), O3 0/1 both (held-out honesty
  markers), no regressions anywhere. Verdict: **MIXED** (concierge
  precedent). Claim C-012; PRD status updated (proof excepted from
  all-UNVERIFIED).
- Three trial runs were excluded with reasons (harness-bug all-fail,
  pre-containment contamination, permission-blocked roleplays) — see
  `docs/benchmarks/proof.md` for the full accounting.

### Outcome trial harness hardening — from first live runs (2026-09-15, opencode only, no Codex)

- First live workspace trial (`proof`, opencode, trials=1) exposed four
  trial-validity bugs, all fixed same-day with re-verification:
  pristine-fixture commits (untracked files false-failed scope);
  workdir containment (prompt workdir pin + outer-repo change monitor
  + workdir tree, after one agent edited the real fixture);
  trial TMPDIR redirected under the repo (opencode auto-rejects /tmp
  workdirs); O2 gained an added-test gate (doing nothing passed).
- Preliminary signal only (n=1 per condition; protocols require n=2
  for verdicts, which stay UNVERIFIED): O1 treatment PASS vs baseline
  FAIL; O2 both PASS. One contaminated run-2 O1-treatment PASS
  (pre-containment) is explicitly invalid and excluded.

### Paid-agent guard — codex default-deny (2026-09-14)

- Harness defaults alone spent 186 codex sessions in one day (trigger
  sweeps + `concierge`/`hotseat` outcome trials). Added
  `scripts/eval_guard.py`: `eval-trigger`, `eval-workflow`, and
  `eval-outcome` now refuse `codex` — exit 4, nothing invoked, no
  results written — unless the human sets BOTH `--allow-paid` AND
  `ALLOW_PAID_AGENT=1` on that run. Either key alone unlocks nothing;
  automation must never set the keys itself. `--check` / `--list` /
  `--dry-run` stay ungated (they invoke nothing). Free adapters
  (`opencode`) are unaffected; authorized runs record
  `paid_guard: "authorized"` for audit. Binding semantics in
  `evals/adapters/README.md`; agent-facing rule added to AGENTS.md
  non-negotiables.

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

### v1 campaign — Skill Phase 02 `hotseat` (PROVEN LIFT, structural)

- Closed two audit gaps: scoreless decision matrix (options × one-line
  verdicts — voting stays banned) and mandatory minority-objections (or
  stated why-empty) in synthesis; mirrored in the moderator card and
  quality gates.
- Authored H4 (settled-idea restraint) + H5 (forced-consensus adversarial)
  scenarios; added hotseat-vs-distill sibling pair and a comparative-decision
  trigger case.
- Hardened `scripts/eval-outcome` after a real failure: head+tail 60K
  capture (head-only truncation was eating graded syntheses) and per-task
  timeouts (hotseat needs 600s). First broken attempt preserved, re-ran clean.
- Executed `hotseat` Layer C on codex: treatment 5/5 incl. held-out (7/7
  personas, 23–40 assumption mentions, matrix + minority throughout) vs
  baseline 0/5 structural (strong essays: MVP + numbered kills, but 1–3
  assumptions, no independence, no artifacts). Cost documented (~2× chars,
  2–5× time). Verdict: **PROVEN LIFT** on debate structure — see
  `docs/benchmarks/hotseat.md`. Claim C-011.

### v1 campaign — Skill Phase 03 `spelunk` (zero-spend: depth + protocol, no trials)

- Policy change: no paid-model runs (Codex etc.) without an explicit trial
  budget. All outcome verdicts stay honestly `UNVERIFIED` until funded runs.
- Closed four audit gaps: trace-one-execution-path-early step,
  precise-symbols-before-grep rung, commit/dirty provenance header for deep
  maps, and `inventory` manifests + generated/vendor sections with `-- .`
  churn scoping (fixed repo-wide churn leaking into subdir scans).
- Authored SP1–SP5 scenarios (incl. lying-README adversarial) and a risk-map
  trigger case; outcome protocol + frozen tasks on seeded fixtures with
  isolated answer keys (verdict UNVERIFIED).
- Extended `scripts/eval-outcome` (code only): fixture workspaces +
  fact-recall/contaminant/hallucinated-path grader, offline-tested incl.
  edge cases and concierge/hotseat regression. No agent runs used.

### v1 campaign — Skill Phase 04 `scout` (zero-spend: depth + protocol, no trials)

- Closed three audit gaps without bloating runtime: per-fact tier+date
  verdicts, SKILL.md pointer to the ladder's conflict resolution (which
  already existed, unreferenced), and a new `scripts/check-note`
  structure validator wired into the workflow (tested both directions).
- Authored SC1–SC5 scenarios (incl. prompt-injection adversarial SC5 and
  memory-only restraint SC4) plus a source-conflict trigger case.
- Outcome protocol + frozen tasks: offline-answerable version traps on
  seeded fixtures (React-19-blog vs installed 18.3.1, unpinned FastAPI,
  lodash tutorial vs zero imports). Grader gains `must_contain_any`
  honesty groups, verified offline against synthetic good/bad outputs.
  Verdict UNVERIFIED — see `docs/benchmarks/scout.md`.

### v1 campaign — Skill Phase 05 `distill` (zero-spend, no Codex: depth + protocol, no trials)

- Closed two audit gaps: repo grounding now runs before question drafting
  (questions can't target nonexistent surfaces), and every candidate
  question faces a materiality test — name both plausible answers and what
  each changes, else it becomes a numbered assumption.
- Authored DI1–DI5 scenarios (contradiction, missing-surface, tiny-brief
  restraint, scope-smuggling adversarial) plus a no-ceremony trigger case.
- Outcome protocol + frozen tasks: grounding trap (O1), 30-line tiny-brief
  budget (O2 — over-specifying is the failure), held-out login scoping
  (O3). Grader gains `max_lines`; verified offline on synthetic
  good/bloat/tiny outputs. Verdict UNVERIFIED — see
  `docs/benchmarks/distill.md`.

### v1 campaign — Skill Phase 06 `masterplan` (zero-spend, no Codex: depth + protocol, no trials)

- Closed three audit gaps: confirmed/probable/to-discover path labels
  (a plan with no to-discover labels on a non-trivial repo is now called
  dishonest), uncertainty-collapses-first sequencing, and IRREVERSIBLE
  slice marking with a user checkpoint.
- Authored MP1–MP5 scenarios (no-down-path migration, missing-module,
  plan-theater restraint, horizontal-pressure adversarial) plus an
  irreversibility trigger case.
- Outcome protocol + frozen tasks (feature slicing, migration rollback,
  held-out component split). Grader verified offline: vertical slice-plan
  passes,   horizontal phase-plan fails. Verdict UNVERIFIED — see
  `docs/benchmarks/masterplan.md`.

### v1 campaign — Skill Phase 07 `pilot` (zero-spend, no Codex: depth + protocol, no trials)

- Full audit first: all three research traces re-verified against runtime
  (no drift), PRD §8 contract checked, neighbour boundaries walked. Four
  substantive gaps closed: running decision log in the plan file,
  dirty-tree checkpoint rule (never absorb user state), replan materiality
  test (in-slice deviation → record + continue; architecture/scope →
  `masterplan`), and the slice-tests vs `proof`-suite boundary.
- Authored PI1–PI5 scenarios (pre-existing breakage, "just make it green"
  adversarial) plus a plan-reality trigger case.
- Outcome protocol + frozen tasks with **workspace grading** (changed-file
  scope + check-command exits recorded pre-cleanup): new `verify`/`scope`
  support in `scripts/eval-outcome`, offline-tested on synthetic
  observations (clean/drift/red all grade correctly) with full regression
  across all 7 grader types. Verdict UNVERIFIED — see
  `docs/benchmarks/pilot.md`.

### v1 campaign — Skill Phase 08 `backend` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all research traces verified, PRD §8 walked). Fixed a
  duplicated webhooks bullet; added transactional outbox atomicity,
  caller-owned retries with deadline propagation, lock-order +
  whole-transaction deadlock retry, backpressure-vs-circuit distinction,
  and the missing Prerequisites + Tool selection/fallback sections.
- Authored BE1–BE5 scenarios (exactly-once-under-retries, trust-the-client
  adversarial, CRUD restraint) plus an idempotency trigger case.
- Outcome protocol + frozen tasks on two stacks (Python + TypeScript
  fixtures). Workspace grader gains `must_contain_any`; verified offline
  with full 8-path regression. Verdict UNVERIFIED — see
  `docs/benchmarks/backend.md`.

### v1 campaign — Skill Phase 09 `blueprint` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (traces verified, validator self-tested both
  directions). Two deliverable gaps closed: provenance header (date +
  commit + map freshness) on the README index, and a Decisions section
  linking plan AgDRs or stating calls inline.
- Authored BP1–BP5 scenarios (proposed-vs-observed, no-render-toolchain,
  make-it-look-enterprise adversarial) plus a proposed-marking trigger.
- Outcome protocol + frozen tasks with **artifact grading**: new
  artifacts-capture + `{ROOT}`-expansion support in `scripts/eval-outcome`;
  grader gates validator exits, node-to-fixture resolution,
  forbidden-infra words (invented Kafka/CDN caught), and diagram budget —
  verified offline on all five gates with full 8-grader regression.
  Verdict UNVERIFIED — see `docs/benchmarks/blueprint.md`.

### v1 campaign — Skill Phase 10 `headroom` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (traces verified). Three reference-only additions where
  the campaign bar explicitly required more: tail-latency thinking (what
  dominates p99 for this workload), cache failure-mode design (cold
  start, stampede, outage fallback), and queue economics (lag alarms, DLQ
  retention, retention pricing). Zero new always-on cost.
- Authored HR1–HR5 scenarios (no-numbers framework, premature-monolith
  restraint, billion-user adversarial) plus a boring-brief trigger case.
- Outcome protocol + frozen tasks (tiny/growing/large workloads) with an
  endorsement-vs-mention limitation stated upfront. Offline testing caught
  and fixed a real harness crash (fact grader assumed a fixture); all
  discriminations re-verified. Verdict UNVERIFIED — see
  `docs/benchmarks/headroom.md`.

### v1 campaign — Skill Phase 11 `polish` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Three reference-only additions where the campaign bar explicitly
  required more: Tool selection/fallback section (static pass +
  unverified marking without browser tooling), a no-render stop
  condition, and a dark-theme audit bullet (contrast + elevation, not
  inversion). Zero new always-on cost.
- Authored PO1–PO5 scenarios (direction-first normal, token-constraint
  hard edge, no-render failure, subtle-mode restraint, make-it-pop
  adversarial) plus a small-tweaks trigger case.
- Outcome protocol + frozen tasks on a new `polish-dashboard` fixture
  (slop-seeded page + constraint tokens file; a directory because the
  runner copies fixture dirs) with a new artifact grader (slop-hex scan,
  token byte-identity, state markers, Direction line) — verified offline
  on all gates with full 6-grader regression;   taste/hierarchy stays in
  blind review, stated upfront. Verdict UNVERIFIED — see
  `docs/benchmarks/polish.md`.

### v1 campaign — Skill Phase 12 `friction` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions where the campaign bar explicitly
  required more: Tool selection/fallback section (walk → static +
  unverified ladder, axe as floor-not-ceiling) and a no-findings stop
  condition (cite the walks, never invent findings). Zero new always-on
  cost.
- Authored FR1–FR5 scenarios (destructive-proportionality hard edge,
  nothing-runnable failure, healthy-flow/audit-only restraint,
  remove-the-confirmation adversarial) plus an audit-only trigger case.
- Outcome protocol + frozen tasks on a new `friction-flows` fixture
  (seeded signup friction + one good typed-confirm pattern to defend)
  via the shared artifact grader (new `friction` type dispatch,
  `files_unchanged` support for audit-only restraint). Offline testing
  caught and broadened one brittle next-step word group before freezing;
  all discriminations re-verified with full 7-path regression. Marker
  presence ≠ walk quality stays in blind review, stated upfront. Verdict
  UNVERIFIED — see `docs/benchmarks/friction.md`.

### v1 campaign — Skill Phase 13 `ditto` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (both research traces verified, PRD §8 walked). One
  reference-only addition where the campaign bar explicitly required
  more: Tool selection/fallback section consolidating the four
  capability rungs (full loop → static → screenshot-only →
  description-only). Zero new always-on cost.
- Authored DT1–DT5 scenarios (single-viewport hard edge, auth-walled
  failure, placeholders-only restraint, injection-plus-secret
  adversarial) plus a placeholders-only trigger case.
- Outcome protocol + frozen tasks on a new `ditto-source` fixture
  (raw-hex styles, owned asset refs, one embedded AI directive, one fake
  secret) via the shared artifact grader (new `ditto` type dispatch, no
  new grader mechanics). Verified offline on all gates with full 7-path
  regression; visual match stays in blind review, stated upfront.
  Verdict UNVERIFIED — see `docs/benchmarks/ditto.md`.

### v1 campaign — Skill Phase 14 `proof` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  One reference-only addition where the campaign bar explicitly required
  more: Tool selection/fallback section consolidating the four
  execution rungs (real runner → minimal harness → hand mutation →
  unverified). Zero new always-on cost.
- Authored PF1–PF5 scenarios (boundary-choice hard edge, zero-harness
  failure, one-test restraint, make-CI-green adversarial) plus a
  leave-the-suite-alone trigger case.
- Outcome protocol + frozen tasks on a new `proof-cart` fixture (stdlib
  unittest — pytest not guaranteed in trial envs; green suite blind to
  a seeded double-discount bug) via the workspace grader, no harness
  change. O1 graded on genuine red (`FAILED (failures=` separates red
  from green and from erroring suites); O3 grades honesty, not suite
  color. Verified offline end-to-end with real test runs on all gates.
  Verdict UNVERIFIED — see `docs/benchmarks/proof.md`.

### v1 campaign — Skill Phase 15 `roadtest` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  No runtime gap found — the capability ladder already is the
  tool-selection section, untrusted-content and self-healing rules
  present, rung discipline in the gates. Audit recorded in research,
  zero lines added to the runtime.
- Authored RT1–RT5 scenarios (console-error-on-green hard edge,
  no-browser failure, logic-only restraint, missing-testid plus
  instructive-text adversarial) plus a drive-it-not-unit-test trigger
  case.
- Outcome protocol + frozen tasks on a new `roadtest-shop` fixture
  (fake-success checkout, unhandled rejection, dead link), chat-graded
  via the fact grader — headless trials cannot produce browser
  evidence, so ladder honesty (rung/matrix/console markers, line
  budget) is the graded object, stated upfront. Verified offline on all
  gates.   Verdict UNVERIFIED — see `docs/benchmarks/roadtest.md`.

### v1 campaign — Skill Phase 16 `sleuth` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (code + runnable path +
  evidence sources) and Tool selection/fallback (debugger → prints →
  static-unconfirmed ladder). Zero new always-on cost.
- Authored SL1–SL5 scenarios (intermittent hard edge,
  cannot-reproduce failure, labeled-provisional restraint,
  wrap-it-and-ship adversarial) plus a cause-before-change trigger case.
- Outcome protocol + frozen tasks on a new `sleuth-cache` fixture
  (stale-reads bug) via the workspace grader: freshness + cache-used
  behavior checks separate true fixes from bypasses. Offline testing
  caught and fixed a real harness bug — `__pycache__/*.pyc` counted as
  changed files false-failed every Python scope trial (latent in Phase
  14's `proof` tasks; its sim missed it) — filtered in
  `scripts/eval-outcome`, both phases re-verified after. Verdict
  UNVERIFIED — see `docs/benchmarks/sleuth.md`.

### v1 campaign — Skill Phase 17 `referee` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (complete diff + written
  criteria) and Tool selection/fallback (subagent → self-review →
  decline-to-skim ladder). Zero new always-on cost.
- Authored RF1–RF5 scenarios (signature-change hard edge,
  context-free-giant-diff failure, clean-diff restraint, hurry-up
  adversarial) plus a blockers-only trigger case.
- Outcome protocol + frozen tasks on a new `referee-change` fixture
  (3-criterion brief; change meets one, misses one, smuggles a
  refactor), chat-graded via the fact grader — review judgment has no
  executable oracle, so marker discipline (verdict, disclosure,
  intent/scope groups, 60-line budget) is the graded object, stated
  upfront. Verified offline on all gates. Verdict UNVERIFIED — see
  `docs/benchmarks/referee.md`.

### v1 campaign — Skill Phase 18 `hotpath` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (both research traces verified, PRD §8 walked). Two
  reference-only additions: Prerequisites (runnable system + one
  measurement path) and Tool selection/fallback (profiler → counters →
  unverified-hypotheses ladder). Zero new always-on cost.
- Authored HP1–HP5 scenarios (micro-tune-bait hard edge,
  unmeasurable-here failure, target-met restraint, faster-by-Friday
  adversarial) plus a no-blind-optimization trigger case.
- Outcome protocol + frozen tasks on a new `hotpath-orders` fixture
  (per-line catalog scans + cold formatting decoy) via the workspace
  grader, no harness change: deterministic scan counts + golden totals
  on two workloads (wall-clock deliberately ungraded — flaky on shared
  runners). Verified offline end-to-end with real runs on all gates:
  structural fixes pass; micro-tunes, hardcodes, drift, untouched, and
  report-less runs each fail.   Verdict UNVERIFIED — see
  `docs/benchmarks/hotpath.md`.

### v1 campaign — Skill Phase 19 `harden` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (code + runnable path +
  authorization line) and Tool selection/fallback (scanner →
  adversarial → static ladder). Zero new always-on cost.
- Authored HN1–HN5 scenarios (IDOR hard edge, blind-spot failure,
  triage-not-theater restraint, WAF-it adversarial) plus an
  exploitability-only trigger case.
- Outcome protocol + frozen tasks on a new `harden-notes` fixture
  (in-memory sqlite: injectable lookup, hardcoded secret, unenforced
  ownership) via the workspace grader, no harness change: plain AND
  comment-obfuscated injection separate parameterization from regex
  theater; legit-flow checks separate fixes from breakage. Verified
  offline end-to-end with real exploit runs on all gates. Verdict
  UNVERIFIED — see `docs/benchmarks/harden.md`.

### v1 campaign — Skill Phase 20 `unslop` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  One reference-only addition: Tool selection/fallback section
  consolidating the three signal rungs (runner → smoke-baseline →
  no-signal-no-detox). Zero new always-on cost.
- Authored UN1–UN5 scenarios (load-bearing hard edge, no-baseline
  failure, audit-only restraint, rewrite-it adversarial) plus an
  audit-first trigger case. Signature U1–U3 remain as cross-checks.
- Outcome protocol + frozen tasks on a new `unslop-shop` fixture
  (seeded duplication, dead code, zombie layer, swallowed error, debug
  leftover, plus a test-locked legacy quirk to defend) via the
  workspace grader, no harness change: suite green + slop gone + quirk
  surviving + net-negative lines + tests-untouched scope. Verified
  offline end-to-end with real runs on all gates. Verdict UNVERIFIED —
  see `docs/benchmarks/unslop.md`.

### v1 campaign — Skill Phase 21 `janitor` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (repo + conditional gh)
  and Tool selection/fallback (local → gh-probed → skip-silent
  ladder). Zero new always-on cost.
- Authored JN1–JN5 scenarios (message-from-diff hard edge, no-gh
  failure, report-only restraint, squash-and-push adversarial) plus a
  report-only trigger case.
- Outcome protocol + frozen tasks on a new `janitor-mess` fixture
  (deterministic `setup.sh` recipe — nested `.git` cannot be
  committed; the script `cd`s to its own directory): HEAD pinned,
  status shape, staged-file, and branch-survival checks, no harness
  mechanics change beyond two real bug fixes below. Offline testing
  caught and fixed two harness bugs — bare `.env`-style tokens counted
  as hallucinated paths, and the fact grader silently ignoring
  `verify` commands — both backward-compatible, full regression clean.
  Verdict UNVERIFIED —   see `docs/benchmarks/janitor.md`.

### v1 campaign — Skill Phase 22 `frontpage` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  One reference-only addition: Tool selection/fallback section
  consolidating the four verification rungs (real run → verbatim
  snippets → hand-checked links → honest v0). Zero new always-on cost.
- Authored FP1–FP5 scenarios (nothing-installable hard edge, offline
  failure, tiny-tool restraint, say-10k-users adversarial) plus a
  short-and-honest trigger case. Signature F1–F3 remain as cross-checks.
- Outcome protocol + frozen tasks on a new `frontpage-tool` fixture
  (working CLI under a slop-seeded README: broken install, fake
  badges, invented traction) via the shared artifact grader (new
  `frontpage` type dispatch, no new mechanics): invented strings gone,
  real commands present, code byte-identical, audit/refusal markers.
  Offline testing caught a real harness gap — the artifact grader never
  enforced `verify` exits, so code-touching runs "passed" docs tasks —
  fixed same-phase, backward-compatible, full regression clean.
  Verdict UNVERIFIED — see `docs/benchmarks/frontpage.md`.

### v1 campaign — Skill Phase 23 `findable` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  One reference-only addition: Tool selection/fallback section
  consolidating the three audit rungs (curl-rendered → validator →
  offline-static). Zero new always-on cost.
- Authored FD1–FD5 scenarios (SPA-no-prerender hard edge, offline
  failure, metadata-only restraint, stuff-it adversarial) plus a
  no-promises trigger case.
- Outcome protocol + frozen tasks on a new `findable-site` fixture
  (duplicate titles, staging noindex, fake review stars, blocking
  robots, lying sitemap, double headings) via the workspace grader, no
  harness change: deterministic greps separate real fixes from
  untouched, restructured-when-scoped-out, and stuffed pages. Verified
  offline end-to-end with real file operations on all gates. Verdict
  UNVERIFIED — see `docs/benchmarks/findable.md`.

### v1 campaign — Skill Phase 24 `frugal` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (task + gate + signal)
  and Tool selection/fallback (telemetry → proxies → unknown ladder).
  Zero new always-on cost.
- Authored FG1–FG5 scenarios (no-telemetry honesty, gate-missing
  failure, verification-protecting restraint, 63-percent adversarial)
  plus a no-skipped-verification trigger case. Signature F1–F3 remain
  as cross-checks.
- Outcome protocol + frozen tasks on a new `frugal-hunt` fixture (1500-line
  log, ERRORs frozen at 412/987/1330) via the fact grader, no harness
  change: exact numbers + honesty groups + compactness budgets catch
  lossy summaries, whole-log dumps, and bare percentages. Verified
  offline on all gates.   Verdict UNVERIFIED — see
  `docs/benchmarks/frugal.md`.

### v1 campaign — Skill Phase 25 `cleared` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (both research traces verified, PRD §8 walked). One
  reference-only addition: Tool selection/fallback section
  consolidating the three evidence rungs (runner → sibling-reports →
  unrunnable). Zero new always-on cost.
- Authored CL1–CL5 scenarios (green-release hard edge, unrunnable
  failure, gate-not-workshop restraint, mark-it-READY adversarial)
  plus a verdict-only trigger case.
- Outcome protocol + frozen tasks on a new `cleared-release` fixture
  (2 green + 1 red version-drift test) via the workspace grader, no
  harness change: the suite must stay red (workshop-trap detector)
  plus file identity and verdict markers. Verified offline end-to-end
  with real runs on all gates.   Verdict UNVERIFIED — see
  `docs/benchmarks/cleared.md`.

### v1 campaign — Skill Phase 26 `runway` (zero-spend, no Codex: depth + protocol, no trials)

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (cleared-fresh + build +
  access) and Tool selection/fallback (CLI → preflight-only →
  plan-only ladder). Zero new always-on cost.
- Authored RW1–RW5 scenarios (missing-env hard edge, no-access
  failure, preflight-only restraint, say-it's-live adversarial) plus a
  preflight-only trigger case.
- Outcome protocol + frozen tasks on a new `runway-app` fixture via
  the workspace grader: file identity (nothing deployed, nothing
  created — including a new entry-count gate) plus honesty markers and
  fabrication phrases. Offline testing caught two real harness gaps —
  the workspace grader ignoring `must_not`, and file-identity missing
  created files — both fixed same-phase, backward-compatible, full
  regression clean.   Verdict UNVERIFIED — see
  `docs/benchmarks/runway.md`.

### v1 campaign — Skill Phase 27 `recall` (zero-spend, no Codex: depth + protocol, no trials) — ALL 28 SKILLS COVERED

- Deep audit first (all three research traces verified, PRD §8 walked).
  Two reference-only additions: Prerequisites (files + genuine need)
  and Tool selection/fallback (validator → compact → create ladder).
  Zero new always-on cost.
- Authored RC1–RC5 scenarios (budgeted catch-up, polluted-memory
  failure, repo-derivable restraint, remember-this-key adversarial)
  plus a surgical-write trigger case.
- Outcome protocol + frozen tasks on a new `recall-notes` fixture via
  workspace + fact graders, no harness change: the skill's own
  `check-memory` runs as a verify command (duplicate titles fail it —
  proven offline), plus supersession/secret/TTL/budget gates and
  confirmation markers. Verified offline end-to-end with real file
  operations on all gates. Verdict UNVERIFIED — see
  `docs/benchmarks/recall.md`.
- Milestone: recall was the last skill without a protocol — all 28
  skills now have outcome protocols (158 scenarios across 28 skills).
  Remaining work is the funded proof phase, not more scaffolding.

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
