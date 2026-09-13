---
name: hotseat
description: Runs a structured multi-persona debate that stress-tests a product or project idea before any code is written. Use whenever the user brings an idea ("I want to build an attendance app"), asks whether they should build something, wants feedback or validation of a concept, or says words like idea, side project, MVP, startup, feature pitch, or "thoughts on this". Seven independent specialists critique the idea from product, engineering, UX, systems, security, growth and beginner perspectives, then a moderator synthesizes decisions, MVP scope and risks.
---

# hotseat — put the idea in the hot seat

One LLM asked "is my idea good?" will say yes. This skill replaces that
reflex with structured disagreement: seven specialists argue the idea from
seven angles **before seeing each other's opinions**, then a moderator
synthesizes what survives.

The independence ordering is the whole trick — opinions formed in isolation
anchor less. Keep it even when it feels slower.

## When NOT to use

- The idea is settled and the user wants execution → `distill`.
- The question is about a library/API/framework → `scout`.
- Mid-implementation design question ("which table structure here?") →
  answer it directly; a full debate is overhead.
- The user wants cheerleading, not critique. Ask once; if they confirm,
  stop.

## Prerequisites

None. Subagents (if available) upgrade fidelity: spawn the seven round-1
passes as parallel subagents so independence is structural rather than
disciplined. Without subagents, sequential passes work — follow the
anti-anchoring rules below exactly.

## The panel

| Person | Lens | Signature question |
| --- | --- | --- |
| Aanya | Product | "Does anyone actually need this?" |
| Kabir | Staff engineer | "What's the accidental complexity here?" |
| Meera | UX | "What does the confused first-time user do?" |
| Arjun | Systems | "How does this fail at 10× scale or on a bad day?" |
| Naina | Security | "How does a bad actor abuse this?" |
| Rohan | Growth / indie shipper | "Can this ship this month and spread?" |
| Ishaan | Beginner maintainer | "Will I understand this code in six months?" |

Full persona cards (what each attacks in each round, when their vote wins)
live in `references/personas.md`. Read it before round 1 — the cards are
what make the voices distinct instead of seven echoes of the model.

## Workflow

### 1. Frame

Restate the idea in one tight paragraph: what it is, for whom, the core
value. If critical context is missing (who uses it, where it runs, budget),
ask at most 3 questions — only ones whose answers would change the debate.

### 2. Round 1 — independent verdicts

Each persona produces, **without seeing any other persona's output**:

- what they like;
- what worries them;
- one assumption they distrust;
- one major question;
- one alternative;
- recommendation (build / change / kill, one line why).

With subagents: one subagent per persona, prompt = persona card + framed
idea, nothing else. Without: write each verdict fully before starting the
next; never revise an earlier verdict after reading a later one.

### 3. Round 2 — real disagreement only

Show every persona the others' round-1 verdicts. Round 2 exists **only**
where verdicts conflict or an assumption got distrusted. Direct engagement
("Kabir: Meera's onboarding worry assumes X — here's why X is wrong") —
no polite summarizing, no repeating round 1. Maximum two exchanges per
conflict. Cap: one round 2. Endless fake debate is a failure mode.

### 4. Moderated synthesis

A moderator (not any persona) synthesizes:

1. **Strongest version** of the idea that survived;
2. **Rejected assumptions** (with who rejected them and why);
3. **Open questions** the user must answer;
4. **Product decisions** to lock;
5. **Technical decisions** to lock;
6. **MVP** — the smallest lovable version;
7. **Later** — explicitly deferred ideas;
8. **Risks** — top 3–5, each with a mitigation.

## Honesty rules

- Personas are reasoning lenses, not people. Never fabricate user research,
  market data or statistics to support a persona's view — arguments must
  stand on stated reasoning, or be marked "(unverifiable without research)".
- If the panel genuinely agrees on something, say so — manufacturing
  conflict is as useless as suppressing it.

## Quality gates

- Every round-1 verdict is self-contained (zero references to other
  personas — check before revealing).
- The synthesis names at least **2 rejected or corrected assumptions**.
  If it can't, the debate was theater — run a sharper round 2 or say
  honestly that the idea survived unchallenged and why.
- No more than 2 discussion rounds total.
- The synthesis is decision-oriented: a reader can act on it without
  re-reading the debate.

## Stop conditions

- Synthesis delivered and the user's reaction captured → offer `distill`
  to convert the surviving idea into a brief, then stop.
- User kills the idea → record why in the artifact, stop.
- User redirects mid-debate → follow the redirect; do not finish theater.

## Output contract

In chat: the synthesis (8 sections above), compact.

On disk (when the debate concludes): `docs/ideas/YYYY-MM-DD-<slug>.md` with
provenance header, the frame, each persona's round-1 verdict, round-2
conflicts, and the synthesis. This is your artifact — `recall` may later
pull the decisions from it, so keep the synthesis section self-sufficient.

## References

- `references/personas.md` — the seven persona cards. Read before round 1.
