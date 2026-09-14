# Handsfree Autonomy Policy Research

Provenance for the `handsfree` autonomy governor. Version-sensitive claims
re-verified against primary sources on **2026-09-14**; full citation table in
[SOURCES.md](SOURCES.md). Research notes stay outside runtime context.

## 1. Host permission reality (primary sources)

| Source | Lesson | Why it matters | Where encoded |
|---|---|---|---|
| [Antigravity CLI settings](https://www.antigravity.google/docs/cli/settings/) | `toolPermission`: `request-review` (default), `proceed-in-sandbox`, `strict`, `always-proceed`; `artifactReviewPolicy`: `asks-for-review` (default), `agent-decides`, `always-proceed` | The skill must name the exact mode it observes instead of guessing; each mode changes what "keep moving" means | `references/antigravity.md` (Permission modes) |
| [Antigravity CLI sandbox](https://antigravity.google/docs/cli/sandbox/) | Sandboxed commands auto-run under `proceed-in-sandbox`; bypass always prompts unless an `unsandboxed(...)` rule matches; sandbox defaults off | Prefer sandbox-compatible commands first; never smuggle bypass flags to dodge a prompt | `references/antigravity.md` (Sandbox strategy) |
| [Antigravity IDE settings](https://www.antigravity.google/docs/ide/settings/) | Strict mode forces Request Review on terminal, browser JS, artifacts; ignores allowlist; forces network-less sandbox | In strict mode the correct behavior is to say so and work read-only, not to push harder | `references/antigravity.md` (Strict mode) |
| [Antigravity permissions](https://antigravity.google/docs/permissions/) | Precedence Deny > Ask > Allow; in-workspace file access auto-allowed; unconfigured web/command actions default Ask | Read/edit inside the workspace is the low-friction path; web + shell + out-of-workspace work is where prompts live | `SKILL.md` (AUTO class), `references/antigravity.md` (Mitigation) |
| [Gemini CLI configuration](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md) | `defaultApprovalMode`: `default` / `auto_edit` / `plan`; YOLO only via `--yolo` / `--approval-mode=yolo` flags, never `settings.json` | The skill must never claim to "enable YOLO" or edit settings to widen approvals — that is the user's CLI invocation | `references/antigravity.md` (Other runtimes) |
| [Gemini CLI policy engine](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md) | Modes `default`/`autoEdit`/`plan`/`yolo`, hierarchy `plan < default < autoEdit < yolo`; per-mode `modes = [...]` rules; writes default `ask_user` | Explains why the same task prompts on one machine and not another: mode + policy, not model mood | `references/antigravity.md` (Other runtimes) |
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
- Editing user/host settings to widen approvals — a security boundary violation, banned in `references/antigravity.md`.
- Bundling unrelated risky commands to amortize one approval ("permission laundering") — banned in `references/antigravity.md`.
