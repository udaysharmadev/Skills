# hotseat — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| ACL 2026 — Demystifying Multi-Agent Debate: The Role of Confidence and Diversity | Homogeneous LLM debate converges toward the same answer regardless of rounds; diversity at initialization is the critical variable | Added convergence detection to round-1 synthesis check | SKILL.md §round-1, §honesty rules, personas.md moderator |
| Teresa Torres, Continuous Discovery Habits (productalk.io) | Assumption testing is more efficient than idea testing; rank assumptions by kill probability and test urgency | Assumption register now includes urgency tiers | SKILL.md §synthesis §2, personas.md moderator format |
| Gary Klein, Pre-mortem technique (HBR 2007 + practical 2025 sources) | Past-tense failure framing bypasses optimism bias; independent silent generation prevents "boss effect" suppression | Full pre-mortem mode added with prospective hindsight mechanics | SKILL.md §pre-mortem section |
| Product Talk — Teresa Torres on kill criteria | Kill criteria must be specific and falsifiable; "low engagement" is not a kill criterion | Kill criteria format specified with threshold + timeframe requirement | SKILL.md §synthesis §7, personas.md moderator |

## Key new intelligence encoded

1. **ACL 2026 convergence detection** — after round 1, if ≥4 personas agree with similar reasoning, flag it as potential echo-collapse and either disclose or run sharper round 2
2. **Pre-mortem as distinct mode** — Gary Klein's prospective hindsight technique: past tense, silent independent generation, grouped by probability × severity
3. **Assumption register priority** — ranked by kill probability with urgency tiers: test before build / test during build / monitor post-launch
4. **Falsifiable kill criteria format** — must include metric, threshold, timeframe, and minimum cohort size
5. **MVP cut line with re-entry conditions** — deferred items must have a specific condition for reinstatement, not just "later"
6. **Per-persona round-2 attack angles** — each persona card now names what they specifically target in cross-examination

## Rejected ideas

| Idea | Why not adopted |
| --- | --- |
| Fixed weight/score per persona | Introduces fake quantification; judgment is more honest |
| "Audience size" field in persona verdicts | Cross-cuts all personas; addressed by Aanya's domain |
| Voting mechanism (majority vote outcome) | Collapses disagreement; synthesis is richer |

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Multi-agent debate research | ACL 2026, arxiv 2025-2026 |
| Teresa Torres assumption testing | productalk.io / Continuous Discovery Habits book |
| Gary Klein pre-mortem | HBR Nov 2007; revalidated in 2025 practitioner sources |
