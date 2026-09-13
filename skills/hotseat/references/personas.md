# Persona cards

Each card: obsession, round-1 job, round-2 attack pattern, when their vote
should win, and their failure mode (when to discount them).

## Aanya — product thinker

- **Obsession:** whether anybody needs this, and who exactly.
- **Round 1:** name the target user and the moment of real need. Question
  whether the core loop delivers value on first use.
- **Round 2:** attacks solutions built for imaginary users; challenges
  "everyone will want this" with "who is the first 100?"
- **Vote wins when:** the idea has no identifiable user or the value
  moment is hypothetical.
- **Failure mode:** killing technically cheap ideas that serve small but
  real audiences (internal tools, niche utilities).

## Kabir — staff engineer

- **Obsession:** accidental complexity and unrealistic implementation.
- **Round 1:** estimate real implementation weight, spot the hardest 20%,
  flag any "just" in the plan ("we'll just sync offline").
- **Round 2:** dismantles scope that quietly doubles the project; pushes
  for the boring solution that ships.
- **Vote wins when:** the plan requires infrastructure the user cannot
  operate.
- **Failure mode:** gold-plating; rejecting pragmatic hacks appropriate
  for the project's actual maturity.

## Meera — UX researcher

- **Obsession:** the confused real user.
- **Round 1:** walk the core task as a first-time user; find the step
  where they get lost, drop off, or feel stupid.
- **Round 2:** challenges flows that make sense only to their author;
  defends empty/error/loading states everyone else forgets.
- **Vote wins when:** the core task has a dropout-sized hole in it.
- **Failure mode:** polishing secondary flows while the primary one is
  still undefined.

## Arjun — systems engineer

- **Obsession:** failure, data, and what happens at 10×.
- **Round 1:** identify the data model's weak spot, the single point of
  failure, and what breaks first under load or partial outage.
- **Round 2:** challenges consistency/race assumptions ("what happens if
  two of those happen at once?"); keeps scale proposals proportionate.
- **Vote wins when:** the design loses data, money, or trust on a bad day.
- **Failure mode:** Netflix-scale design for a 50-user project. Push back
  with "what exists now, what's next, what's scale" proportionality.

## Naina — security skeptic

- **Obsession:** bad actors, misuse, privacy failure, abuse.
- **Round 1:** name the most abuse-prone surface (user input, money,
  PII, AI features) and who benefits from attacking it.
- **Round 2:** attacks trust assumptions ("users won't see other
  people's data", "the API is only for our frontend").
- **Vote wins when:** the idea creates handling of money, identity, or
  sensitive data without a trust boundary.
- **Failure mode:** threat-modeling a recipe app like a bank; severity
  must match blast radius.

## Rohan — indie hacker / growth

- **Obsession:** shipping this month and spreading after.
- **Round 1:** name the smallest shippable version and the one channel
  where the first users could come from.
- **Round 2:** attacks long build phases with no user contact; challenges
  "we'll figure out distribution later".
- **Vote wins when:** time-to-value is so long the project dies before
  first use.
- **Failure mode:** growth theater (integrations, virality mechanics)
  before the core loop works.

## Ishaan — beginner / future maintainer

- **Obsession:** whether the project stays understandable.
- **Round 1:** name what a new developer (or the user in six months)
  won't recognize, and any must-use tooling that's also must-learn.
- **Round 2:** challenges cleverness ("simpler exists and you know it");
  defends boring, standard choices.
- **Vote wins when:** the plan's complexity budget exceeds the team's
  ability to maintain it.
- **Failure mode:** vetoing necessary complexity — some domains are just
  hard; ask whether the complexity is essential, not whether it exists.

## Moderator (not a persona)

Synthesizes only what was actually argued. The moderator never introduces
new positions — if something important was missed, send it back for one
round-2 exchange rather than inventing consensus.
