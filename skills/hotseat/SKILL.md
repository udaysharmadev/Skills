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
anchor less. Research on multi-agent debate (ACL 2026) confirms that without
viewpoint diversity at the *start*, debaters converge toward the same answer
regardless of how many rounds run. Keep independence even when it feels slower.

## When NOT to use

- The idea is settled and the user wants execution → `distill`.
- The question is about a library/API/framework → `scout`.
- Mid-implementation design question ("which table structure here?") →
  answer directly; debate is overhead.
- The user wants cheerleading, not critique. Ask once; if they confirm, stop.

## Modes

| Mode | Scope | Use when |
| --- | --- | --- |
| **quick challenge** | 3 personas most relevant to the question, 1 round | a specific decision, not a whole idea |
| **full hotseat** | all 7, 2 rounds, full synthesis | validating a product/project idea |
| **technical hotseat** | Kabir, Arjun, Naina, Ishaan | architecture/implementation feasibility of a settled product idea |
| **product hotseat** | Aanya, Meera, Rohan (+Kabir if build cost is the question) | positioning, scoping, audience |
| **pre-mortem** | all 7, past-tense failure framing | idea already approved; surface risks before committing |

Pre-mortem runs differently from debate — see the pre-mortem section below.

## Prerequisites

None. Subagents upgrade fidelity: one subagent per persona in round 1 makes
independence structural rather than disciplined. Without subagents, write each
verdict fully before starting the next; never revise an earlier verdict after
reading a later one.

## The panel

| Person | Lens | Signature question |
| --- | --- | --- |
| Aanya | Product | "Does anyone actually need this, and what behavior does it replace?" |
| Kabir | Staff engineer | "What's the accidental complexity, and what will force the first rewrite?" |
| Meera | UX | "What does the confused first-time user believe — and is that belief the UI's fault?" |
| Arjun | Systems | "What happens to half-finished state when this fails midway?" |
| Naina | Security | "What can I do as an authenticated user that I shouldn't — and what if I'm the lowest-privileged user?" |
| Rohan | Growth / indie shipper | "What is the smallest thing that produces a shareable moment, and can it ship this month?" |
| Ishaan | Beginner maintainer | "What has to be true in my head before I can safely touch this?" |

Full persona cards (attack angles, what they demand, what changes their mind)
live in `references/personas.md`. Read it before round 1.

## Workflow

### 1. Frame

Restate the idea in one tight paragraph: what it is, for whom, the core
value. If critical context is missing (who uses it, where it runs, budget),
ask at most 3 questions — only ones whose answers would change the debate.

### 2. Round 1 — independent verdicts

Each persona produces, **without seeing any other persona's output**:

- what they like;
- what worries them most;
- one assumption they distrust (and why they distrust it);
- one major question that would change their view;
- one alternative to the idea as framed;
- recommendation (build / change / kill, one line why).

With subagents: one subagent per persona, prompt = persona card + framed
idea + nothing else. Without: write each verdict fully before starting the
next; never revise an earlier verdict after reading a later one.

**After all round-1 verdicts:** check for premature convergence. If more
than 4 of 7 personas recommend the same thing with similar reasoning, name
it explicitly in the synthesis — either the idea survived a genuine test
(note it) or the panel collapsed into echo (run a sharper round 2 targeting
the weakest assumption).

### 3. Round 2 — real disagreement only

Show every persona the others' round-1 verdicts. Round 2 exists **only**
where verdicts conflict or an assumption was distrust-flagged. Direct
engagement: "Kabir: Meera's onboarding concern assumes X — here's why X is
wrong, and here's the specific edge case that breaks her claim." No polite
summarizing, no repeating round 1. Maximum two exchanges per conflict.
Cap: one round 2. Endless debate is a failure mode.

### 4. Pre-mortem (alternative to debate when idea is approved)

**Do not run debate — run this instead:**

1. Announce: "It is now 18 months in the future and this product has failed.
   The failure was real and significant. Your job is to explain why."
2. Each persona generates, *in silence and independently*, 3–5 specific
   failure causes using past tense ("the onboarding converted at 8% because
   users didn't understand X until step 4, by which time 80% had left").
3. Collect and group. Prioritize by: (a) probability and (b) kill severity.
4. For each top-3 failure cause: name a concrete mitigating action to take now.

Pre-mortem surfaces risks that debate suppresses because the "we can handle
that" reflex doesn't fire when you've already accepted that you lost.

### 5. Moderated synthesis

A moderator (not any persona) synthesizes — decisions, not a transcript:

1. **Strongest version** of the idea that survived;
2. **Assumption register** — ranked by kill probability: assumption →
   who distrust it → what would resolve it → urgency (test before build /
   test in build / monitor post-launch);
3. **Rejected assumptions** (with who rejected them and why);
4. **Open questions** the user must answer before building;
5. **Product + technical decisions** to lock now;
6. **MVP cut line** — what survives in the smallest shippable version,
   what waits;
7. **Kill criteria** — what observable outcome after build would prove this
   wrong (must be specific and falsifiable: not "low engagement" but "DAU/MAU
   below 0.15 after 4 weeks with 200 active users");
8. **Top 3–5 risks** — each with a mitigation and its second-order effect.

## Honesty rules

- Personas are reasoning lenses, not people. Never fabricate user research,
  market data, or statistics — arguments must stand on stated reasoning, or
  be marked "(unverifiable without research)".
- If the panel genuinely agrees on something, say so and say why — "all 7
  personas flagged distribution as the primary risk" is valuable. Manufacturing
  conflict is as useless as suppressing it.
- If a verdict is essentially the same as another persona's, call it in the
  synthesis: "Kabir and Arjun reached the same concern by different paths —
  this is a strong signal." Don't run false diversity for seven rounds.

## Quality gates

- Every round-1 verdict is self-contained (zero references to other
  personas — check before revealing).
- The synthesis names at least **2 rejected or corrected assumptions**.
  If it can't, the debate was theater — run a sharper round 2 or say
  honestly that the idea survived unchallenged.
- Kill criteria are specific and falsifiable — not "if users don't adopt it"
  but a concrete metric with a threshold and timeframe.
- No more than 2 discussion rounds total.
- Synthesis is decision-oriented: a reader can act on it without re-reading
  the debate.

## Stop conditions

- Synthesis delivered and user's reaction captured → offer `distill` to
  convert surviving idea into a brief, then stop.
- User kills the idea → record why in the artifact, stop.
- User redirects mid-debate → follow the redirect; do not finish theater.

## Output contract

In chat: the synthesis (sections above), compact.

On disk (when debate concludes): `docs/ideas/YYYY-MM-DD-<slug>.md` with
provenance header, the frame, each persona's round-1 verdict, round-2
conflicts, and the synthesis. The synthesis section must be self-sufficient —
`recall` may later pull decisions from it.

## References

- `references/personas.md` — the seven persona cards. Read before round 1.
