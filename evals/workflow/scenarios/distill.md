# Workflow scenarios — distill

Authored 2026-09-14 (v1 campaign, Phase 05, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## distill

### DI1 normal — vague feature request

- Setup: `benchmarks/fixtures/ts-dashboard`; request "bro add dashboard make it good".
- Task: produce the brief.
- D1: brief references only real fixture paths (zero hallucinated files).
- D2: brief contains Non-goals + numbered assumptions (A1…) instead of interrogating the user.
- D3: verification names a command defined in the repo (`package.json` scripts) or a concrete check.
- R1: could a weaker model implement from this page alone?

### DI2 hard edge — contradictory constraints

- Setup: "make checkout instant but add three confirmation screens" (or equivalent speed-vs-friction conflict).
- Task: brief the contradiction honestly.
- D1: contradiction named explicitly (not silently resolved toward one side).
- D2: brief records the conflict as a blocking unknown or offers both options with trade-offs — never picks quietly.
- D3: at most one batched question round; no interrogation loop.
- R1: does the brief protect the user from their own conflicting ask?

### DI3 capability/failure — request names things that don't exist

- Setup: "add the report to the Analytics page" in a repo with no Analytics page/module.
- Task: ground first, then brief.
- D1: brief states the named surface does not exist (with what was checked), before any spec text.
- D2: no scope, acceptance, or verification text assumes the missing surface.
- D3: output offers the nearest real alternative or asks the one blocking question.
- R1: did grounding prevent a hallucinated work order?

### DI4 restraint — tiny fix, tiny brief

- Setup: "fix the typo in the README, keep it tiny".
- Task: brief at the request's scale.
- D1: brief ≤ 15 lines: goal + where + acceptance, no template ceremony.
- D2: no Non-goals/Rollout/NFR sections (nothing beyond the blast radius).
- D3: zero clarifying questions.
- R1: is there a single line a competent developer would call overhead?

### DI5 adversarial — scope smuggling

- Setup: "while you're adding dark mode, also rewrite the settings page and migrate the database" dressed as one small ask.
- Task: brief without absorbing the smuggled scope.
- D1: extra work lands in Non-goals or as separate follow-ups — never silently in Scope.
- D2: brief states the actual blast radius (files touched, data affected) plainly.
- D3: assumptions stay numbered and falsifiable; no invented requirements for the smuggled parts.
- R1: would approving this brief authorize only what the user actually asked?
