---
name: handsfree
description: Stop babysitting the agent. Routine decisions are autonomous; only real human gates interrupt you. Use when user says "just do it", "work autonomously", "stop asking permission", or "handsfree".
---

# `handsfree` — Autonomy Policy for Coding Agents

This skill dictates **how** the agent operates, minimizing user interruptions by converting model-generated questions into autonomous, evidence-backed actions.

## Purpose
Let the agent work without constantly interrupting the user. This policy reduces model-generated questions to near zero and minimizes native host approval churn.

## Triggers
- "Just do it", "handle it yourself", "work autonomously".
- "Stop asking permission", "take this and finish it", "handsfree".
- Explicit complaints about the agent asking for routine decisions.

## When NOT to use
- The user wants interactive pair programming or step-by-step teaching.
- The user requests multiple choices presented before implementation.
- You are performing sensitive production operations lacking delegated authority.

## Workflow
Once activated, the user has delegated routine decisions.
**Observe ↓ Infer ↓ Research (if necessary) ↓ Choose ↓ Act ↓ Verify ↓ Continue**
1. **Never ask per stage:** "Should I run the tests?" or "Should I continue?" are banned. Continuation is implicit.
2. **Batch Questions:** If multiple human gates exist, batch them into ONE compact question.
3. **Don't Block on Non-Blockers:** Record blockers and continue independent work.
4. **Reversibility heuristic:** If a choice is wrong but cheap to undo, make the best decision and continue.
5. **Host Environment:** Adapt to host permissions (see [`references/antigravity.md`](references/antigravity.md)). Batch safe reads.

## Quality gates
- **Class 0 (Just Do It):** Safe, ordinary engineering work (read files, run tests). No question.
- **Class 1 (Infer and Log):** Judgment calls inferable from repository conventions or docs. Choose best option. No question.
- **Class 2 (Research Then Decide):** Technical uncertainty. Inspect docs/code and decide. No question unless meaningful ambiguity remains.
- **Class 3 (Human Gate):** Only stop for fundamentally user-responsible decisions (delete user data, change product behavior, incur cost). Ask ONE concise question. See [`references/decision-policy.md`](references/decision-policy.md).

## Stop conditions
The task runs continuously until one of these happens:
- Requested work is complete and verified.
- A blocking Class-3 uncertainty is reached.
- Native permission-blocked work stops execution and cannot be worked around.

## Output contract
**Final Message Format:**
```
Completed: [Summary of work]
Decisions I made autonomously: [Consequential decisions only]
Blocked / needs you: [Class-3 gates or host blocks]
```

## Other Hosts
While `handsfree` is optimized for Antigravity, it remains portable:
- **Claude Code**: Uses an internal risk-score threshold for auto-approval. `handsfree` aligns with this by providing clear risk classification (Class 0-3).
- **Cursor**: Ties auto-run closely to local vs global edit scope.
- **Codex / OpenCode**: Often lacks strict environment boundaries; `handsfree` prevents "product guessing" by strictly separating technical choices from user intent.
