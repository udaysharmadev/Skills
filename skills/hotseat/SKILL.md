---
name: hotseat
description: Challenges a consequential product, architecture, or feature decision through independent lenses, evidence, disagreement, premortem risks, kill criteria, and re-entry conditions. Use before committing when the user wants critique, alternatives, or a go or no-go recommendation.
---

# hotseat: put the idea in the hot seat

One LLM asked "is my idea good?" will say yes. This skill replaces that
reflex with structured disagreement: seven specialists argue the idea from
seven angles **before seeing each other's opinions**, then a moderator
synthesizes what survives.

The independence ordering is the whole trick: opinions formed in isolation
anchor less. Multi-agent debate research motivates testing independent
judgments before synthesis, but it does not prove that a fixed panel or persona
set is objectively correct. Keep independence even when it feels slower.

The panel is not user research, market sizing, security testing, or a vote.
It is a structured way to expose assumptions, choose cheap tests, preserve
dissent, and help a decision owner decide under uncertainty.

## When NOT to use

- The idea is settled and the user wants execution → `distill`.
- The question is about a library/API/framework → `scout`.
- Mid-implementation design question ("which table structure here?") →
  answer directly; debate is overhead.
- The user wants cheerleading, not critique. Ask once; if they confirm, stop.

## Modes

| Mode | Scope | Use when |
| --- | --- | --- |
| **quick challenge** | only the independent lenses that can change the decision | a specific decision, not a whole idea |
| **full hotseat** | all relevant lenses, followed by evidence-based synthesis | validating a product or project idea |
| **technical hotseat** | engineering, systems, security, and maintainer lenses | feasibility of a settled product idea |
| **product hotseat** | product, UX, delivery, and cost lenses | positioning, scoping, and audience |
| **pre-mortem** | relevant lenses using past-tense failure framing | surface risks before committing |

Pre-mortem runs differently from debate: see the pre-mortem section below.

## Prerequisites

None. Subagents upgrade fidelity: one subagent per persona in round 1 makes
independence structural rather than disciplined. Without subagents, write each
verdict fully before starting the next; never revise an earlier verdict after
reading a later one.

Collect only the context that can alter the decision: decision owner, target
user, job/problem, current alternatives, constraints, time/budget, irreversible
cost, known evidence, and decision deadline. If missing information makes a
build/kill recommendation arbitrary, ask a compact question batch or narrow to
a hypothesis challenge.

## Authority and evidence boundaries

- Personas are analytical lenses, not independent human experts, customers, or
  security assessors. Never attribute an invented opinion to a real group.
- No lens may claim a market fact, compliance requirement, benchmark, threat,
  user behavior, or technical limit without supplied or independently verified
  evidence. Mark reasoning-only conclusions as hypotheses.
- The decision owner remains responsible for a build, spend, policy, data, or
  launch decision. This skill recommends, it does not authorize.
- Preserve the original proposal and its constraints. A stronger variant may be
  proposed, but must name what it changes and costs.
- Do not use a panel to manufacture consensus for a predetermined outcome.
  Surface the constraint and write a decision memo with dissent instead.

## Decision framing and option discipline

Frame the decision as a falsifiable choice, not "is this good?" Name at least
two live options when they exist: build as proposed, reduce/resequence, choose
an alternative, delay for evidence, or stop. For each option record expected
benefit, material downside, reversible/irreversible commitments, missing
evidence, and decision owner.

The moderator may not introduce a new option after round one unless an
independent lens proposed it. A lens may challenge an assumption but must name
the observation that would change its mind. This prevents confident prose from
being mistaken for a decision framework.

## Independence protocol

Before round one, make a shared fact packet containing only the frame, supplied
evidence, constraints, and definitions. Do not include another persona's
reasoning, prior synthesis, or a preferred conclusion. Each lens must produce
its verdict from that packet. Capture it before reading another verdict.

After collection, tag every statement as **fact**, **inference**, **assumption**,
or **proposal**. Group similar concerns by premise, not wording. If two lenses
reach the same conclusion through distinct evidence, retain both paths. If they
repeat the same unsupported premise, count it once and flag false convergence.

Use the panel cards in references/personas.md conditionally: choose only lenses
whose distinctive question could change the decision in quick mode. Full mode
may use all seven, but an irrelevant persona should state "no material angle"
rather than fabricate a concern.

## The panel

| Person | Lens | Signature question |
| --- | --- | --- |
| Aanya | Product | "Does anyone actually need this, and what behavior does it replace?" |
| Kabir | Staff engineer | "What's the accidental complexity, and what will force the first rewrite?" |
| Meera | UX | "What does the confused first-time user believe: and is that belief the UI's fault?" |
| Arjun | Systems | "What happens to half-finished state when this fails midway?" |
| Naina | Security | "What can I do as an authenticated user that I shouldn't: and what if I'm the lowest-privileged user?" |
| Rohan | Growth / indie shipper | "What is the smallest thing that produces a shareable moment, and can it ship this month?" |
| Ishaan | Beginner maintainer | "What has to be true in my head before I can safely touch this?" |

Full persona cards (attack angles, what they demand, what changes their mind)
live in `references/personas.md`. Read it before round 1.

## Workflow

### 1. Frame

Restate the idea in one tight paragraph: what it is, for whom, the core
value. If critical context is missing (who uses it, where it runs, budget),
ask only the smallest batch of questions whose answers would change the debate.

### 2. Round 1: independent verdicts

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

**After all round-1 verdicts:** check for premature convergence. Agreement
without materially different evidence is not independent confirmation. Name
the convergence and run a sharper challenge against the weakest assumption.

### 3. Round 2: real disagreement only

Show every persona the others' round-1 verdicts. Round 2 exists **only**
where verdicts conflict or an assumption was distrust-flagged. Direct
engagement must identify the disputed premise and evidence that would resolve
it. Stop when another exchange would repeat positions rather than add evidence.

### 4. Pre-mortem (alternative to debate when idea is approved)

**Do not run debate: run this instead:**

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

A moderator (not any persona) synthesizes: decisions, not a transcript:

1. **Strongest version** of the idea that survived;
2. **Decision matrix**: the live options considered (build / change /
   kill / major variants) as rows, each persona's one-line verdict as
   columns. Qualitative verdicts only: no scores, no votes, no weighting
   (voting collapses disagreement: see rejected ideas in the research note);
3. **Assumption register**: ranked by kill probability: assumption →
   who distrust it → what would resolve it → urgency (test before build /
   test in build / monitor post-launch);
4. **Rejected assumptions** (with who rejected them and why);
5. **Minority objections**: dissent that survived round 2 is quoted in
   the dissenter's own terms, never smoothed into consensus. A synthesis
   with no minority section must state why (genuine agreement or
   unresolved: never imply unanimity by omission);
6. **Open questions** the user must answer before building;
7. **Product + technical decisions** to lock now;
8. **MVP cut line**: what survives in the smallest shippable version,
   what waits;
9. **Kill criteria**: what observable outcome after build would prove this
   wrong (must be specific and falsifiable: not "low engagement" but "DAU/MAU
   below 0.15 after 4 weeks with 200 active users");
10. **Top 3–5 risks**: each with a mitigation and its second-order effect.

### 6. Convert critique into a decision experiment

For each assumption marked "test before build", choose the smallest ethical,
time-bounded experiment that can split the live options. Define audience,
method, leading observation, success/failure interpretation, owner, cost,
deadline, and what decision follows each result. Prefer a prototype, technical
spike, user task, narrow data query, or documented source review to a broad
build.

Do not give a metric a threshold merely to look decisive. A useful threshold is
grounded in the product's economics, risk, or prior evidence; otherwise state
the directional decision rule and ask the owner to set the boundary.

## Failure handling and edge cases

- **Thin context:** produce only a hypothesis map and the minimum questions or
  experiments needed. Do not invent a user, budget, or market.
- **All lenses agree:** run a disconfirmation pass against the dominant premise;
  report genuine agreement only after naming why it is not repeated reasoning.
- **One lens dominates:** ensure the synthesis preserves minority objections and
  does not turn severity rhetoric into a veto without evidence.
- **Irreversible/high-risk choice:** escalate to the accountable human and
  include options, downside, and evidence gap. Do not issue a casual go signal.
- **External facts needed:** route source work to scout or perform targeted
  primary-source research, then rerun only the affected disagreement.
- **User requests a verdict without debate:** give a direct conditional
  recommendation and state that a hotseat was not performed.

## Tool selection and fallbacks

- Use independently scoped agents only when they are available and the decision
  justifies the coordination cost. Each receives the fact packet and one lens,
  never other verdicts.
- Without independent agents, serialize drafting: complete and freeze one
  verdict before reading or drafting the next. State this lower-fidelity method.
- Use targeted research only for an assumption whose result may change an
  option. Prefer primary sources and observed repository/user evidence.
- Use a compact table or issue artifact for assumptions and experiments. Avoid
  a transcript as the primary deliverable.
- If evidence cannot be collected in time, report conditional options and the
  cost of deciding now rather than silently converting uncertainty into a score.

## Honesty rules

- Personas are reasoning lenses, not people. Never fabricate user research,
  market data, or statistics: arguments must stand on stated reasoning, or
  be marked "(unverifiable without research)".
- If the panel genuinely agrees on something, say so and say why: "all 7
  personas flagged distribution as the primary risk" is valuable. Manufacturing
  conflict is as useless as suppressing it.
- If a verdict is essentially the same as another persona's, call it in the
  synthesis: "Kabir and Arjun reached the same concern by different paths,
  this is a strong signal." Don't run false diversity for seven rounds.

## Tool selection / fallback

- Use independent subagents only when available and useful; otherwise write each lens before reading the next.
- Research only claims that can change the decision.
- If evidence is unavailable, preserve disagreement and name the cheapest validating experiment.

## Quality gates

- Every round-1 verdict is self-contained (zero references to other
  personas: check before revealing).
- The synthesis names at least **2 rejected or corrected assumptions**.
  If it can't, the debate was theater: run a sharper round 2 or say
  honestly that the idea survived unchallenged.
- The synthesis carries a decision matrix (options × one-line verdicts,
  no scores) and a minority-objections section: or states explicitly why
  the latter is empty.
- Kill criteria are specific and falsifiable: not "if users don't adopt it"
  but a concrete metric with a threshold and timeframe.
- No more than 2 discussion rounds total.
- Synthesis is decision-oriented: a reader can act on it without re-reading
  the debate.
- Every material claim is labeled fact, inference, assumption, or proposal.
- The final recommendation identifies the accountable decision owner and at
  least one evidence-triggered re-entry condition.
- A lens that has no relevant distinct angle says so; it does not pad the panel.

## Stop conditions

- Synthesis delivered and user's reaction captured → offer `distill` to
  convert surviving idea into a brief, then stop.
- User kills the idea → record why in the artifact, stop.
- User redirects mid-debate → follow the redirect; do not finish theater.

## Output contract

In chat: the synthesis (sections above), compact.

On disk (when debate concludes): `docs/ideas/YYYY-MM-DD-<slug>.md` with
provenance header, the frame, each persona's round-1 verdict, round-2
conflicts, and the synthesis. The synthesis section must be self-sufficient,
`recall` may later pull decisions from it.

## References

- `references/personas.md`: the seven persona cards. Read before round 1.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
