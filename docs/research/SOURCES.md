# Research sources — canonical, version-sensitive, verified

> Maintainer backbone for the v1 campaign. Every entry below was re-verified
> against the live primary source on **2026-09-14**. Runtime `SKILL.md` files
> must stay lean; this file (plus per-skill notes in this directory) is where
> citations live. If a URL rots, the `Refresh` column tells the next auditor
> what to re-check. Nothing here is pasted into runtime context.

## Antigravity + Gemini permission behavior (handsfree-critical)

| Source | Verified | What it establishes | Refresh |
|---|---|---|---|
| [Antigravity CLI settings](https://www.antigravity.google/docs/cli/settings/) | 2026-09-14 | `toolPermission`: `request-review` (default), `proceed-in-sandbox`, `strict`, `always-proceed`. `artifactReviewPolicy`: `asks-for-review` (default), `agent-decides`, `always-proceed`. Sandbox via `enableTerminalSandbox`; non-workspace access off by default. | fast-moving — recheck each release |
| [Antigravity CLI sandbox](https://antigravity.google/docs/cli/sandbox/) | 2026-09-14 | `proceed-in-sandbox` lets sandboxed commands auto-run; out-of-sandbox still prompts. Sandbox bypass requests always require approval unless an `unsandboxed(...)` allow rule matches. `enableTerminalSandbox` default `false`, `toolPermission` default `request-review`. | fast-moving |
| [Antigravity IDE settings](https://www.antigravity.google/docs/ide/settings/) | 2026-09-14 | Same four modes in IDE; strict mode forces Request Review on terminal, browser JS, and artifacts, ignores allowlist, forces sandbox with no network. | fast-moving |
| [Antigravity permissions](https://antigravity.google/docs/permissions/) | 2026-09-14 | Three lists with precedence **Deny > Ask > Allow**. Unconfigured web reads default Ask; in-workspace file reads/writes auto-allowed; other actions default Ask. Prompt cards allow scope editing (not for terminal commands). | fast-moving |
| [Gemini CLI configuration](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md) | 2026-09-14 | `general.defaultApprovalMode`: `default` / `auto_edit` / `plan` (default `default`). **YOLO is fully supported but can only be enabled via `--yolo` / `--approval-mode=yolo` CLI flags** — deliberately excluded from `settings.json` for security. `security.disableYoloMode` can forbid it. | fast-moving |
| [Gemini CLI policy engine](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md) | 2026-09-14 | Approval modes `default` / `autoEdit` / `plan` / `yolo` with hierarchy `plan < default < autoEdit < yolo`. Rules bind to modes via `modes = [...]`. Read-only tools allowed; write tools default `ask_user`; dedicated allow-rules exist per mode. Approvals granted in a stricter mode flow upward only. | fast-moving |
| [Gemini CLI plan mode](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md) | 2026-09-14 | Read-only research mode (Shift+Tab cycles Default → Auto-Edit → Plan). Exiting plan to implement auto-switches to YOLO. `plan.toml` built-in policy enforceable; user overrides in `~/.gemini/policies/`. | fast-moving |

Implication encoded in `handsfree`: a skill can eliminate **model-created**
ceremony but can never bypass **host enforcement**. Changing
`request-review` → `proceed-in-sandbox` / `always-proceed` (or Gemini
`default` → `auto_edit` / `yolo`) is a user/runtime choice the skill may
explain once, never perform or trick.

## Agent Skills format (all 28 skills)

| Source | Verified | What it establishes | Refresh |
|---|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | 2026-09-14 | Skill = directory + `SKILL.md` (YAML frontmatter + Markdown). `name`: 1–64 chars, lowercase alnum + hyphens, no leading/trailing/double hyphen, must match parent dir. `description`: 1–1024 chars, non-empty, what + when. Optional `license`, `compatibility` (≤500 chars), `metadata`, `allowed-tools`. Body unrestricted. Progressive disclosure: metadata ~100 tok → instructions <5000 tok → resources on demand. `SKILL.md` ≤500 lines. | stable — recheck yearly |
| [Microsoft Learn: Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) | 2026-09-14 | Same contract; four-stage disclosure (advertise → load → read resources → run scripts). Resources discovered from `references/` + `assets/`, scripts from `scripts/`. | stable |

## Distribution (install claims)

| Source | Verified | What it establishes | Refresh |
|---|---|---|---|
| [skills.sh docs](https://www.skills.sh/docs) | 2026-09-14 | Install via `npx skills add owner/repo`. Badge: `[![skills.sh](https://skills.sh/b/owner/repo)](https://skills.sh/owner/repo)`. CLI open source at `vercel-labs/skills`. | stable |
| [vercel-labs/skills CLI](https://github.com/vercel-labs/skills) | 2026-09-14 | Flags: `-g/--global`, `-a/--agent`, `-s/--skill`, `-l/--list`, `--copy`, `-y/--yes`, `--all` (= `--skill '*' --agent '*'`). Commands: `add/use/list/find/remove/update/init`. 70+ agents supported incl. OpenCode, Claude Code, Codex, Cursor. Project scope default (`./skills/`-style dir), global with `-g`. | fast-moving — reverify exact install command per release |

## Long-running / autonomy harness design

| Source | Verified | What it establishes | Refresh |
|---|---|---|---|
| [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 2026-09-14 | Initializer + coding agent split; one feature at a time; clean mergeable state per session; `init.sh` + progress file + git log as handoff; feature list with pass/fail gates; test-before-build to catch rot. | research — stable |
| [Anthropic: Harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) | 2026-09-14 | Context resets beat compaction for anxious models; sprint contracts (builder+evaluator agree on done); fresh-context evaluator with hard thresholds; re-simplify scaffolding on each model upgrade; evaluator load-bearing only past the model's solo boundary. | research — stable |
| [cwc-long-running-agents](https://github.com/anthropics/cwc-long-running-agents/blob/main/README.md) | 2026-09-14 | Default-FAIL contract; evidence-read gates before pass-marking; agent-maintained handoff (`PROGRESS.md` + commits); `/goal` loop vs custom wrapper. Direct model for `pilot` slice discipline + `cleared` evidence rules. | research — stable |

## Eval methodology (proof phase)

Per-skill notes cite their own core sources (debate-diversity for `hotseat`,
OWASP/ASVS for `harden`, Core Web Vitals for `polish`, WCAG 2.2 for
`friction`). The cross-skill rules live here: deterministic graders first,
structured rules second, blind qualitative rubrics only for genuinely
qualitative properties; answer keys isolated from evaluated workspaces;
held-out cases frozen before tuning; multiple trials; raw traces kept
including failures. This follows the Anthropic eval guidance already encoded
in `docs/evaluations.md` — no new claim introduced.

## Research policy

- Primary/official sources ground version-sensitive claims; community sources identify failure modes only.
- Every version-sensitive claim names its verified date; `handsfree` references must.
- Rejected-but-tempting ideas stay recorded in the per-skill note so they do not return as regressions.
- No benchmark number, install count, star count, or compatibility badge enters the README without a row in `docs/claims.md`.
