# Trigger cases

> Case lines are bullets: an utterance in quotes, then the expected skill
> slug — or the word none. A "none" case is a negative case: no skill in
> this bundle should activate.
> Run scripts/run-evals to validate. These are fixtures, not results.

## concierge

- "I just installed this skills bundle, what now" => concierge
- "/concierge" => concierge
- "what can these skills do for this repo" => concierge
- "I want to build an attendance app, where do I start" => concierge
- "which skill should handle this" => concierge

## hotseat

- "I have an idea for a habit tracker app" => hotseat
- "should I build a subscription tracker app or is that dumb" => hotseat
- "validate my startup idea before I waste a weekend on it" => hotseat
- "thinking about adding AI chat to my portfolio site, thoughts" => hotseat
- "here's my product idea, poke holes in it" => hotseat

## spelunk

- "how does this codebase even work" => spelunk
- "where is authentication handled in this repo" => spelunk
- "I'm new to this project, walk me through it" => spelunk
- "map out this repository before we change anything" => spelunk
- "what does the payments module do" => spelunk

## scout

- "what's the best markdown parsing library for react in 2026" => scout
- "should we upgrade from react 18 to 19" => scout
- "how do I integrate stripe webhooks properly" => scout
- "does zustand still work with react server components" => scout
- "research which headless CMS fits this project" => scout

## distill

- "bro add dashboard make it good" => distill
- "make the app better" => distill
- "turn this rambling into a proper spec for the agent" => distill
- "I want notifications... like, the good kind, you know" => distill
- "write a clear task brief for adding profile pages" => distill

## masterplan

- "plan the implementation of the billing feature" => masterplan
- "give me a migration plan from mongodb to postgres" => masterplan
- "we agreed on the spec, now plan the refactor" => masterplan
- "break this epic into implementable slices" => masterplan

## recall

- "what did we decide last session" => recall
- "remember that we chose sqlite for now, not postgres" => recall
- "catch me up on where this project stands" => recall
- "save this lesson before we lose the context window" => recall
- "write a handoff summary for tomorrow" => recall

## Negative cases (must stay quiet)

- "fix the login bug, it 500s on submit" => none
- "make the button blue" => none
- "write unit tests for utils/date.ts" => none
- "review my diff before I push" => none
- "deploy this to vercel" => none
- "make this UI pretty" => none
- "clean up this mess of a repo" => none
- "why is this test flaky" => none
- "add a logout link to the navbar" => none
- "delete the unused imports in src/api.ts" => none
