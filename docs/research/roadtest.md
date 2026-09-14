# roadtest — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Browser Automation (2025/2026) | "Silent Self-Healing" is an anti-pattern. When AI guesses locators to bypass broken semantics, it masks real application decay. | Bans silent self-healing, requiring any AI-healed locator to be formally logged as a finding for human review. | SKILL.md §Rules, references/evidence-bundle.md |
| Visual Regression Realities | Pixel-perfect matching fails on dynamic/responsive layouts. Structural DOM analysis is required, and visual tests must not be a crutch for functional logic tests. | Reinforces that evidence must capture state and assertion moments, avoiding reliance on blind pixel-diffing for functional proofs. | references/evidence-bundle.md |
| Decoupling Goal from Script | AI agents are excellent at defining the outcome (goal) but should use stable, deterministic frameworks (Playwright) via semantic locators (`getByRole`) to execute critical paths. | Forbids brittle AI-guessed XPath/CSS chains, enforcing user-centric semantic locators. | SKILL.md §Rules |

## Key new intelligence encoded

1. **Anti-Silent Healing** — ensures that the resilience of AI browser automation does not hide underlying code degradation (e.g., deleted test IDs) by forcing the agent to log every fallback.
2. **Stable Locators First** — mandates semantic, user-centric locators (`getByRole`, `data-testid`) over brittle XPath generation.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| AI self-healing automation | Playwright / Agentic testing pipelines (2026 patterns) |
