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
- "why is the /api/orders endpoint slow" => none
- "rename the settings page title" => none
- "add a new column to the users table" => none
- "write a migration plan for switching databases" => none
- "what should our git commit message convention be" => none
- "summarize this PR description for me" => none

## pilot

- "the plan is approved, start building" => pilot
- "execute the plan slice by slice" => pilot
- "implement slice 2 from docs/plans/dark-mode.md" => pilot
- "keep going with the implementation from where we left off" => pilot

## backend

- "add a DELETE /api/projects/:id endpoint" => backend
- "we need webhook handling for stripe events" => backend
- "the orders table needs a migration to add a status column" => backend
- "make sure users can only edit their own posts" => backend

## blueprint

- "document the architecture of this system" => blueprint
- "I need diagrams showing how the services connect" => blueprint
- "create onboarding docs explaining how the system works" => blueprint
- "draw the request flow for checkout" => blueprint

## headroom

- "will this architecture handle 100k users" => headroom
- "should we split this into microservices" => headroom
- "design the system for the new notification service" => headroom
- "sql or nosql for this workload" => headroom

## polish

- "make the landing page look professional" => polish
- "this dashboard looks so generic, fix it" => polish
- "improve the UI of the settings screen" => polish
- "our app screams AI-generated, help" => polish

## friction

- "users keep abandoning the signup form" => friction
- "the onboarding flow is confusing, audit it" => friction
- "is our app accessible? check keyboard navigation too" => friction
- "the error messages in our app are useless" => friction

## ditto

- "make it look like this [screenshot]" => ditto
- "rebuild this page from the URL I sent" => ditto
- "clone this dashboard design from the Figma export" => ditto
- "recreate the UI in this image using our stack" => ditto

## proof

- "add tests for the checkout flow" => proof
- "we need regression coverage for that bug you fixed" => proof
- "should this be a unit test or an integration test" => proof
- "improve our test suite, it misses real breakage" => proof

## roadtest

- "actually open the browser and test the signup flow" => roadtest
- "check that checkout works end to end before release" => roadtest
- "walk through the app like a user and screenshot everything" => roadtest
- "verify the UI changes in a real browser" => roadtest

## sleuth

- "this bug keeps coming back, figure out the real cause" => sleuth
- "the API randomly 500s about 1 in 20 times" => sleuth
- "debug why the sync job duplicates records" => sleuth
- "it works locally but breaks in production, why" => sleuth

## referee

- "review my diff before I merge" => referee
- "can you do a code review on this PR" => referee
- "check whether this change actually implements the spec" => referee
- "act as a reviewer for the auth refactor" => referee

## hotpath

- "the dashboard takes 5 seconds to load, fix it" => hotpath
- "profile and optimize the report generation" => hotpath
- "our bundle is huge, find out why" => hotpath
- "make the search endpoint faster, but measure it" => hotpath

## harden

- "audit our app for security issues before launch" => harden
- "we're handling payments now, check we're not doing anything stupid" => harden
- "check for injection and XSS risks in the new API" => harden
- "harden the auth flow, we store PII" => harden
