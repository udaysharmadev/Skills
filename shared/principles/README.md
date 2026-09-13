# Product principles (canonical)

Full prose lives in PRD §3. This is the checklist form every skill must
satisfy. Skills inline the subset they depend on.

## 1. Evidence before confidence

Never claim "everything works" because code looks reasonable. When
verification is possible, run it (tests, builds, browser flows, screenshots,
type checks, linters, scanners). When it is not possible, the output says
**unverified** in those exact words.

## 2. Universal core, runtime enhancements

No skill fundamentally requires one runtime, MCP server, framework or OS.
Every workflow follows:

**core workflow → capability detection → best available tool → fallback workflow**

A weaker runtime receives the methodology, not a refusal. No runtime may
hallucinate an action it could not perform.

## 3. Research + instructions + tools + verification

Serious skills carry four layers: methodology (SKILL.md body), references
(loaded on demand), deterministic scripts (for things an LLM should not
eyeball), and a concrete definition of done.

## 4. No AI slop

No unnecessary abstractions, no hallucinated packages, no fake benchmarks,
no decorative badges, no giant reports where a compact result is enough, no
rewriting working projects to demonstrate activity, no "best practices"
without understanding the codebase.

## 5. Research current reality

When APIs, frameworks, packages or deployment behavior can have changed,
research current primary documentation rather than trusting model memory.
That is `scout`'s whole job; other skills delegate to it by name.

## 6. Protect user control

Autonomous for reversible actions. Explicit confirmation gate for:
destructive database operations, deleting meaningful user data, history
rewrites, force pushes, production infrastructure destruction, expensive
cloud changes, high-blast-radius credential changes.
