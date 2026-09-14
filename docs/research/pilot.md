# pilot — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| SWE-agent Execution Patterns (2025/2026) | Test-Driven Execution (TDE) is required to stop agents from writing vacuous tests that pass automatically, hiding hallucinated logic. | Changes the testing sequence to require a failing test (red) before implementation (green). | SKILL.md §4 |
| Agent Hallucination Mitigation Studies | The most dangerous executor hallucination is "silent scope improvisation" — patching unrelated files or weakening tests just to make the current pipeline green. | Explicitly bans scope drift and test-weakening in the completion gate. | references/completion-gate.md |
| Structural Integrity Verification | Agents often spoof tool arguments or hallucinate APIs when they get stuck. Diff inspection must specifically target these fabrications, not just look for "debug leftovers". | Upgrades the diff inspection step to explicitly hunt for spoofed APIs and hallucinated signatures. | SKILL.md §5 |

## Key new intelligence encoded

1. **Test-Driven Execution (TDE)** — mandates the Red-Green cycle. The agent must verify the test fails before writing the implementation to prevent vacuous test generation.
2. **Scope Containment Rule** — explicitly names and bans "silent scope improvisation", ensuring agents don't drift into unrelated files or modify tests simply to bypass failures.
3. **Spoofing Detection** — updates diff inspection to hunt for "tool argument spoofing" (passing fabricated arguments to satisfy an immediate prompt constraint).

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Executor agent failure modes | SWE-agent / Open SWE 2026 post-mortems |
| Neurosymbolic agent guardrails | 2026 RAG/Execution integration studies |
