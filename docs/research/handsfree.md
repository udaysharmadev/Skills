# Handsfree Autonomy Policy Research

Provenance for the `handsfree` autonomy governor. Version-sensitive claims
re-verified against primary sources on **2026-09-14**; full citation table in
[SOURCES.md](SOURCES.md). Research notes stay outside runtime context.

## 1. Host permission reality (primary sources)

| Source | Lesson | Why it matters | Where encoded |
|---|---|---|---|
| [Antigravity CLI settings](https://www.antigravity.google/docs/cli/settings/) | `toolPermission`: `request-review` (default), `proceed-in-sandbox`, `strict`, `always-proceed`; `artifactReviewPolicy`: `asks-for-review` (default), `agent-decides`, `always-proceed` | The skill must name the exact mode it observes instead of guessing; each mode changes what "keep moving" means | `references/host-permissions.md` (Detect) |
| [Antigravity CLI sandbox](https://antigravity.google/docs/cli/sandbox/) | Sandboxed commands auto-run under `proceed-in-sandbox`; bypass always prompts unless an `unsandboxed(...)` rule matches; sandbox defaults off | Prefer sandbox-compatible commands first; never smuggle bypass flags to dodge a prompt | `references/host-permissions.md` (Operate) |
| [Antigravity IDE settings](https://www.antigravity.google/docs/ide/settings/) | Strict mode forces Request Review on terminal, browser JS, artifacts; ignores allowlist; forces network-less sandbox | In strict mode the correct behavior is to say so and work read-only, not to push harder | `references/host-permissions.md` (Detect, Report) |
| [Antigravity permissions](https://antigravity.google/docs/permissions/) | Precedence Deny > Ask > Allow; in-workspace file access auto-allowed; unconfigured web/command actions default Ask | Read/edit inside the workspace is the low-friction path; web + shell + out-of-workspace work is where prompts live | `SKILL.md` (AUTO class), `references/host-permissions.md` (Operate) |
| [Gemini CLI configuration](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md) | `defaultApprovalMode`: `default` / `auto_edit` / `plan`; YOLO only via `--yolo` / `--approval-mode=yolo` flags, never `settings.json` | The skill must never claim to "enable YOLO" or edit settings to widen approvals — that is the user's CLI invocation | `references/host-permissions.md` (Detect) |
| [Gemini CLI policy engine](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md) | Modes `default`/`autoEdit`/`plan`/`yolo`, hierarchy `plan < default < autoEdit < yolo`; per-mode `modes = [...]` rules; writes default `ask_user` | Explains why the same task prompts on one machine and not another: mode + policy, not model mood | `references/host-permissions.md` (Detect) |
| [Gemini CLI plan mode](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md) | Read-only research mode; exiting plan to implement auto-switches to YOLO | `handsfree` respects plan mode as research-only and does not treat its read-only refusals as blockers to route around | `references/decision-policy.md` (BLOCKED) |

## 2. Industry permission models

| Source | Lesson | Why it matters | Where encoded |
|---|---|---|---|
| Claude Code behavior (community-observed, failure-signal only) | Risk-threshold auto-approval | Risk classification (AUTO → ASK-ONCE → BLOCKED) matches how capable hosts already think | `SKILL.md` (Action classes) |
| Cursor behavior (community-observed, failure-signal only) | Auto-run tracks edit scope (local vs global) | Blast radius is the secondary axis after reversibility | `references/decision-policy.md` (ADDITIONAL-AXES note) |
| Codex / OpenCode field behavior | Unrestricted execution drifts into product guessing when intent is missing | The skill separates technical choices (infer) from product intent (ask) | `references/decision-policy.md` (Product-intent row) |

## 3. Human-in-the-loop & harness design

| Source | Lesson | Why it matters | Where encoded |
|---|---|---|---|
| HCI alert-fatigue literature (failure-signal) | Review quality collapses under prompt floods | Batch all ASK-ONCE items into one compact question | `SKILL.md` (Batch rule) |
| [Anthropic: effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Incremental progress + clean mergeable state + progress file + git handoff per session | Long autonomous runs need checkpoints and attempt ceilings, not just "don't ask" | `SKILL.md` (Checkpoints, Budgets) |
| [Anthropic: harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Fresh-context evaluator; default-FAIL contracts; re-simplify scaffolding per model | Autonomy claims need measured interruption-rate AND gate-recall evidence, not vibes | `docs/benchmarks/handsfree.md` (method stub) |
| Software-engineering reversibility (principle) | Reversible actions deserve autonomy | Reversibility is the primary ask/don't-ask heuristic | `SKILL.md` (AUTO class) |

## 4. Key takeaways for `handsfree`

1. **Two interruption sources, two treatments:** model ceremony (eliminate) vs host enforcement (detect, report, work within).
2. **Reversibility over risk-feel:** cheap-to-undo ⇒ act; destructive/production/paid/credential ⇒ ASK-ONCE; policy-unsafe ⇒ BLOCKED even if the user says "never ask".
3. **Checkpoints make autonomy safe:** broad work records recovery state before acting; bounded retries; dirty-tree/user-change preservation.
4. **Gates are measured, not promised:** interruption rate down + necessary-gate recall at 100% is the benchmark; fewer questions via approving dangerous work is a regression.

## Rejected ideas (recorded so they stay rejected)

- "Zero prompts ever" marketing — dishonest; host prompts exist and must be reported, not hidden.
- Editing user/host settings to widen approvals — a security boundary violation, banned in `references/decision-policy.md` (BLOCKED) and `references/host-permissions.md` (Report).
- Bundling unrelated risky commands to amortize one approval ("permission laundering") — banned in `references/decision-policy.md` (BLOCKED) and `references/host-permissions.md` (Operate).

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Four action classes and checkpoints are valuable; ASK ONCE and batch wording can re-ask granted actions or imply unanswered gates proceed; dirty branch language suggests isolation.

**Concrete case and proposed change:** Match exact prior action/target grant before asking; dependent work waits for grant; concrete preparation precedes approval; scoped dirty protection; denial and owned-process recovery.

**Why this change:** HF6/HF8 distinguish repeated approval from absent approval; HF7 targets known secret-read derail without bypass.

**Historical interpretation:** Original case-sensitive grader defect preserved; revised easy-task ties do not show reduced interruptions or improved gate recall. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Already authorized action gets duplicate gate [local rule gap].
2. Batch wording implies silence permits action [local ambiguity].
3. Branch mistaken for dirty-file isolation [local rule defect].
4. Secret-read denial derails independent task [historical pilot/environment signal].
5. Test process timeout mistaken for permission denial [hypothesis].
6. Broad kill command ends user process [hypothesis].
7. New production target inherits staging authority [existing prohibited risk].
8. Paid cost exceeds named bound [existing prohibited risk].
9. Credential presence printed during capability probe [hypothesis].
10. Local migration destroys meaningful dev data [existing gate risk].
11. Checkpoint restore absorbs user hunks [existing documented risk].
12. Scope expansion renamed necessary cleanup [existing documented risk].
13. No-tool workflow fabricates a green check [existing scenario risk].
14. Unchanged failed diagnostic repeats indefinitely [existing documented risk].
15. Grader docstring case mistaken for autonomy effect [historical grader defect].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/handsfree/SKILL.md` | Relevant source, environment or criterion changes |
| [git-status documentation](https://git-scm.com/docs/git-status) — Git project; official tool docs | Living manual; update not assigned here; current fetched manual; local git version not pinned | Index/worktree evidence must be read before editing; applied only to this skill's decision boundary | A branch name alone does not isolate dirty state | `skills/handsfree/references/host-permissions.md` | Relevant source, environment or criterion changes |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Anthropic; official implementation report | 2025-11-26; reported Claude Agent SDK setup | Incremental work and recoverable handoff; applied only to this skill's decision boundary | Specific setup, not mandatory per-step ceremony | `skills/handsfree/SKILL.md` | Relevant source, environment or criterion changes |
| [executing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Recoverable task identity and evidence record; applied only to this skill's decision boundary | Sibling dependencies conflict with standalone bundle contract | `skills/handsfree/references/host-permissions.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/handsfree/SKILL.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | HF6/HF8 distinguish repeated approval from absent approval; HF7 targets known secret-read derail without bypass. | Local contradiction is not a live model result | `evals/workflow/scenarios/handsfree.md`; `docs/benchmarks/handsfree.md` | Content or grader change |

### Adopted and rejected

- Adopted: Match exact prior action/target grant before asking; dependent work waits for grant; concrete preparation precedes approval; scoped dirty protection; denial and owned-process recovery.
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

- Cases: `evals/workflow/scenarios/handsfree.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.

## Independent review follow-through - 2026-10-14

Independent review found the conditional decision-policy table still asked for every security-sensitive or external action. It now checks existing target/effect authorization before classifying; approved local work proceeds with checkpoints, and host/non-waivable constraints remain separate. Trace: skills/handsfree/references/decision-policy.md.

This resolves an observed instruction conflict; it does not establish lift or
change historical grades. The fresh review and forward-trial records remain
separate evidence.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| SEC 2013-222; fetched 2026-10-14 | Added unacknowledged-alert stop branch to decision policy; AUTO/ASK-ONCE/BLOCKED classes confirmed. |
