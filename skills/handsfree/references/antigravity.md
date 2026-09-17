# Google Antigravity Host Integration

The `handsfree` skill minimizes *model-generated* interruptions. However, it operates within host environments (like Google Antigravity and Gemini CLI) that enforce native permission models. This reference defines how to behave within those constraints. *(Last verified against primary docs: 2026-09-14. Fast-moving: recheck each runtime release. Full citations: `docs/research/SOURCES.md`.)*

## 1. Permission Modes

Antigravity surfaces (IDE, CLI, App) expose execution modes via `toolPermission`:

- **`request-review` (default):** The host intercepts tool calls (especially terminal commands) and displays a native approval dialog.
- **`proceed-in-sandbox`:** Routine commands execute automatically inside a secure sandbox (no network/external access); out-of-sandbox execution still triggers review.
- **`always-proceed`:** User has granted full autonomy. Highest risk: high-risk skill gates (`cleared`, `runway`, `janitor` history rules) still apply.
- **`strict`:** Maximum control. Forces Request Review on terminal commands, browser JS execution, and artifact actions; the terminal allowlist is ignored; sandboxing is forced on with network denied.

A second dial, `artifactReviewPolicy`, controls file writes: `asks-for-review` (default), `agent-decides`, `always-proceed`.

Detect the mode before a long run instead of inferring it from prompt frequency: check `~/.gemini/antigravity-cli/settings.json` (`toolPermission`, `enableTerminalSandbox`) or `/config` where available. If you cannot observe it, say `unknown`: never assert a mode.

## 2. How approvals resolve

Permissions evaluate across three lists with strict precedence: **Deny > Ask > Allow**. Unconfigured defaults are secure: in-workspace file reads/writes are auto-allowed; unconfigured shell commands, web navigation/actuation, MCP actions, and out-of-workspace file access default to **Ask**. Approval prompt cards may offer "always allow" scoping (including `unsandboxed(...)` rules for sandbox bypass): accepting or widening those is the **user's** choice, never the agent's. The skill must never edit settings files to widen approvals.

## 2. Agent Constraints

**What a SKILL CAN control:**
- How often it chooses to ask the user a question in chat.
- How many commands it issues.
- The structure and batching of shell commands to reduce native prompt churn.
- Suggesting native approval memory mechanisms (e.g., allowlists).

**What a SKILL CANNOT control:**
- Bypassing a host-level block or native approval dialog.
- Secretly modifying security configurations or clicking "Accept" using UI automation.
- Forcing a command to execute when the host says no.

## 3. Mitigation Strategies for Native Prompts

When operating in environments likely to trigger native approvals (e.g., `request-review`):

1. **Batch Safe Reads:** Instead of issuing 5 separate `git` commands, issue one combined command that safely outputs the required state (e.g., `git status --short && git diff --stat`).
2. **Do Not Bundle Danger:** Never concatenate unrelated risky operations just to reduce the approval count. This is "Permission Laundering" and is banned.
3. **Prefer Sandbox:** Use sandbox mode (`proceed-in-sandbox`) for routine operations where available, avoiding network-dependent or bypass flags unless absolutely necessary.
4. **Approval Memory Suggestion:** If repetitive safe prompts are blocking workflow, you may suggest the native mechanism *once*: "Antigravity is still host-blocking repeated test commands. If you trust this project, its native project permission settings can remember these approvals." Do not nag repeatedly.
5. **Acknowledge Hard Limits:** If execution is blocked by a native dialog, do NOT output "I'll continue automatically." State precisely: "Blocked by Antigravity native approval: [action]. Everything not dependent on it is continuing."

## 4. Gemini CLI modes (same policy, different names)

`general.defaultApprovalMode`: `default` (prompt) / `auto_edit` (edits auto-approved) / `plan` (read-only research). **YOLO mode auto-approves everything but can only be enabled via `--yolo` / `--approval-mode=yolo` CLI flags**: it is deliberately absent from `settings.json`, and `security.disableYoloMode` can forbid it outright. The policy engine binds rules per mode (`plan < default < autoEdit < yolo`); plan mode is read-only and exiting it to implement auto-switches to YOLO. Consequences: never claim to "turn on YOLO"; never treat plan-mode read-only refusals as blockers to route around; Shift+Tab-visible mode changes are user actions you observe, not levers you pull.

## 5. Other runtimes (portable posture)

- **Claude Code:** internal risk-threshold auto-approval; your AUTO → ASK ONCE → BLOCKED classification aligns with it. Headless invocation may hang in some dev environments: report, don't retry blindly.
- **Cursor:** auto-run tracks local vs global edit scope; keep blast radius small and scoped.
- **Codex / OpenCode:** often weakly sandboxed; the skill's value here is preventing product-guessing (technical choice vs user intent), not dodging prompts that barely exist.
