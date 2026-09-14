# Google Antigravity Host Integration

The `handsfree` skill minimizes *model-generated* interruptions. However, it operates within host environments (like Google Antigravity 2026) that enforce native permission models. This reference defines how to behave within those constraints. *(Last verified: Q3 2026)*

## 1. Permission Modes

Antigravity surfaces (IDE, CLI, App) expose various execution modes:
- **`request-review`:** The host intercepts tool calls (especially terminal commands) and displays a native approval dialog to the user.
- **`proceed-in-sandbox`:** Routine commands execute automatically inside a secure sandbox (no network/external access), while bypass attempts trigger review.
- **`always-proceed`:** User has granted full autonomy for the session or project.
- **`strict`:** Highly restricted read-only mode.

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
