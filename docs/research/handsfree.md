# Handsfree Autonomy Policy Research

This document synthesizes research into coding agent permission models, host runtimes (specifically Google Antigravity 2026), and human-in-the-loop interruption behaviors, to establish the foundational rules for the `handsfree` autonomy skill.

## 1. Google Antigravity (2026) Permission Model

Antigravity currently implements multiple execution environments (CLI, IDE, Desktop App) with varying permission behaviors. 

| Source | Lesson | Why it matters | Where encoded |
|--------|--------|----------------|---------------|
| Antigravity Docs | Supports `request-review`, `proceed-in-sandbox`, `always-proceed`, `strict` modes. | The agent cannot bypass host-level blockades. If in `request-review`, batching commands is critical. | `references/antigravity.md` (Permission Modes) |
| Antigravity CLI | CLI environments have session vs. project memory for approvals. | Agents should suggest native memory features instead of nagging. | `SKILL.md` (Rule 17) |
| Antigravity Sandbox | Standard mode allows read/write within workspace without network; bypass requires manual approval. | Minimize network-dependent commands unless absolutely necessary. Rely on sandbox tools first. | `references/antigravity.md` (Sandbox) |
| GitHub Issues | Frequent complaints about "Approval Fatigue" when agents run 10 git commands. | Need to batch safe reads into single, atomic shell scripts or native API calls. | `SKILL.md` (Rule 16) |

## 2. Industry Permission Models

| Source | Lesson | Why it matters | Where encoded |
|--------|--------|----------------|---------------|
| Claude Code | Utilizes an auto-approval threshold based on risk score. | Risk-based classification (Autonomy Ladder) is industry standard for reducing interruptions. | `SKILL.md` (Rule 6) |
| Cursor | Auto-run behavior is tied closely to edit scope (local vs global). | Blast radius is a secondary metric for autonomy. | `SKILL.md` (Rule 8) |
| Codex / OpenCode | Unrestricted execution often leads to "Product Guessing" when intent is missing. | The agent must distinguish between "technical choice" and "user product intent". | `SKILL.md` (Rule 9) |

## 3. Human-in-the-Loop & Interruption Cost

| Source | Lesson | Why it matters | Where encoded |
|--------|--------|----------------|---------------|
| HCI Research | Alert fatigue reduces review quality to near zero. | Batching human-gate questions into a single interaction preserves user attention. | `SKILL.md` (Rule 13) |
| Agentic Workflow Papers | Non-blocking execution allows parallel progress while waiting for input. | Agent should continue independent tasks rather than blocking entirely on a single question. | `SKILL.md` (Rule 14) |
| Software Engineering Reversibility | "Reversible actions deserve autonomy" (e.g., local refactor vs DB drop). | Reversibility is the primary heuristic for whether to ask. | `SKILL.md` (Rule 7) |

## 4. Key Takeaways for `handsfree`

1. **User Intent vs Technical Choice:** Technical uncertainty is the agent's problem (solve via research). User intent ambiguity requires escalation.
2. **Reversibility over Risk:** If a technical decision is wrong but cheap to undo, just do it.
3. **Do not fight the host:** The skill minimizes *model-generated* questions. It minimizes *host-generated* prompts by writing efficient, batched commands, but it never attempts to hack or bypass host security.
4. **Continue Implicitly:** "Should I run the tests?" is banned. Run them.
