# Research provenance

These notes explain why each skill makes the decisions it makes. They preserve
the research pass behind the runtime instructions: the source or research
theme, the lesson that mattered, the behavior it changed, and the exact
`SKILL.md`, reference, or helper where that behavior now lives.

Research files are maintainer evidence. They do **not** load into agent context
when a skill runs. A copied skill remains self-contained; only its own
`SKILL.md`, conditional references, scripts, and assets travel with it.

## Evidence categories

Treat sources according to the claim they can support:

1. **Official truth** — standards, specifications, vendor documentation, and
   versioned source code establish current behavior.
2. **Research evidence** — papers and careful empirical work inform decision
   frameworks, with their scope and limitations preserved.
3. **Implementation patterns** — production engineering material shows how a
   sound principle survives real systems.
4. **Community failure signals** — issues and practitioner reports reveal what
   to investigate; they are not ground truth by themselves.

Each note’s **Where encoded** column is the traceability contract. If runtime
behavior changes, update that row in the same pull request. Rejected ideas stay
recorded when they are tempting enough to recur.

## Refresh policy

- Re-check fast-moving APIs, agent frameworks, standards, platform behavior,
  and security guidance before changing runtime advice.
- Prefer primary or official sources for factual claims.
- Use community reports to identify failure modes, then verify the mechanism.
- Cite only evidence that materially changed the skill; do not copy source
  text or build decorative bibliographies.
- Remove or qualify claims that cannot be supported. A precise uncertainty is
  better than a confident folk rule.
- Keep research prose here, outside runtime context. Encode only the resulting
  decision logic, restraint, tooling, or failure prevention in the skill.

## Intelligence

| Skill | Research focus |
| --- | --- |
| [`concierge`](concierge.md) | uncertainty-source routing, evidence reuse, and the cost of needless handoffs |
| [`hotseat`](hotseat.md) | viewpoint diversity, assumption testing, pre-mortems, and falsifiable kill criteria |
| [`spelunk`](spelunk.md) | outside-in discovery, churn × complexity, and cognitive debt |
| [`scout`](scout.md) | source hierarchies, API grounding, stability, and conflict resolution |
| [`distill`](distill.md) | ambiguity detection and agent-executable requirements |
| [`masterplan`](masterplan.md) | planner–executor separation, vertical slices, and compact decision records |
| [`recall`](recall.md) | governed memory, knowledge lifecycles, TTLs, and context pollution |

## Building & architecture

| Skill | Research focus |
| --- | --- |
| [`pilot`](pilot.md) | test-driven execution, scope containment, and hallucination detection |
| [`backend`](backend.md) | agent-safe boundaries, idempotency, and structured output validation |
| [`blueprint`](blueprint.md) | audience-specific C4 views, traceable models, and trust boundaries |
| [`headroom`](headroom.md) | proportional scaling, bounded agency, and avoiding premature distribution |

## Product experience

| Skill | Research focus |
| --- | --- |
| [`polish`](polish.md) | generated-UI failure patterns, semantic accessibility, and token constraints |
| [`friction`](friction.md) | agentic usability, planning visibility, escalation, and audit trails |
| [`ditto`](ditto.md) | design-system mapping and structural visual comparison |

## Proof & engineering

| Skill | Research focus |
| --- | --- |
| [`proof`](proof.md) | vacuous-test prevention, production-shaped mocks, and property testing |
| [`roadtest`](roadtest.md) | semantic locators, self-healing risks, and evidence discipline |
| [`sleuth`](sleuth.md) | hypothesis-driven debugging and trace-based observability |
| [`referee`](referee.md) | intent-first review, caller context, confidence, and review fatigue |
| [`hotpath`](hotpath.md) | measured bottlenecks, structural gains, and micro-tuning traps |
| [`harden`](harden.md) | GenAI attack surfaces, excessive agency, and exploitability-aware triage |

## Cleanup & public surface

| Skill | Research focus |
| --- | --- |
| [`unslop`](unslop.md) | AI code accretion, zombie abstractions, and behavior-preserving cleanup |
| [`janitor`](janitor.md) | atomic history, branch sprawl, and useful commit intent |
| [`frontpage`](frontpage.md) | theoretical quickstarts, hallucinated badges, and documentation fit |
| [`findable`](findable.md) | honest structured data, rendered metadata, and anti-slop discoverability |
| [`frugal`](frugal.md) | context dumping, lossy compression, and successful-task token cost |

## Shipping

| Skill | Research focus |
| --- | --- |
| [`cleared`](cleared.md) | evidence inflation, release-gate boundaries, and actionable ownership |
| [`runway`](runway.md) | live-state verification, deployed fingerprints, and proportional rollout strategy |
