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
- "bro add dashboard make it good, which skill should handle that" => concierge
- "rename the login button to Sign in" => none
- "we already have an approved plan, just build it" => pilot

## hotseat

- "I have an idea for a habit tracker app" => hotseat
- "should I build a subscription tracker app or is that dumb" => hotseat
- "validate my startup idea before I waste a weekend on it" => hotseat
- "thinking about adding AI chat to my portfolio site, thoughts" => hotseat
- "here's my product idea, poke holes in it" => hotseat
- "help me decide between two product directions before I commit" => hotseat

## spelunk

- "how does this codebase even work" => spelunk
- "where is authentication handled in this repo" => spelunk
- "I'm new to this project, walk me through it" => spelunk
- "map out this repository before we change anything" => spelunk
- "what does the payments module do" => spelunk
- "where is this codebase most likely to break if we refactor" => spelunk

## scout

- "what's the best markdown parsing library for react in 2026" => scout
- "should we upgrade from react 18 to 19" => scout
- "how do I integrate stripe webhooks properly" => scout
- "does zustand still work with react server components" => scout
- "research which headless CMS fits this project" => scout
- "the docs say X but the changelog says Y for our version, which is right" => scout

## distill

- "bro add dashboard make it good" => distill
- "make the app better" => distill
- "turn this rambling into a proper spec for the agent" => distill
- "I want notifications... like, the good kind, you know" => distill
- "write a clear task brief for adding profile pages" => distill
- "spec this typo fix, and keep it tiny, no enterprise ceremony" => distill

## masterplan

- "plan the implementation of the billing feature" => masterplan
- "give me a migration plan from mongodb to postgres" => masterplan
- "we agreed on the spec, now plan the refactor" => masterplan
- "break this epic into implementable slices" => masterplan
- "plan the auth migration and flag anything irreversible" => masterplan

## recall

- "what did we decide last session" => recall
- "remember that we chose sqlite for now, not postgres" => recall
- "catch me up on where this project stands" => recall
- "save this lesson before we lose the context window" => recall
- "write a handoff summary for tomorrow" => recall
- "just this decision, nothing else, keep it short" => recall

## Direct routes (small-sounding asks that a specialist owns)

- "fix the login bug, it 500s on submit" => sleuth
- "write unit tests for utils/date.ts" => proof
- "review my diff before I push" => referee
- "deploy this to vercel" => runway
- "make this UI pretty" => polish
- "clean up this mess of a repo" => unslop
- "why is this test flaky" => sleuth
- "why is the /api/orders endpoint slow" => hotpath
- "add a new column to the users table" => backend
- "write a migration plan for switching databases" => masterplan
- "what should our git commit message convention be" => janitor

## Genuinely none (trivial or out of scope — no skill should steal)

- "make the button blue" => none
- "add a logout link to the navbar" => none
- "delete the unused imports in src/api.ts" => none
- "rename the settings page title" => none
- "summarize this PR description for me" => none
- "how do I center a div" => none
- "what's the weather like" => none
- "delete the staging deployment" => none
- "write a blog post announcing the release" => none

## pilot

- "the plan is approved, start building" => pilot
- "execute the plan slice by slice" => pilot
- "implement slice 2 from docs/plans/dark-mode.md" => pilot
- "keep going with the implementation from where we left off" => pilot
- "the plan says X but the code says Y, what now" => pilot
- "just make the tests pass, skip the failing ones" => none

## backend

- "add a DELETE /api/projects/:id endpoint" => backend
- "we need webhook handling for stripe events" => backend
- "the orders table needs a migration to add a status column" => backend
- "make sure users can only edit their own posts" => backend
- "charge the card but never double-charge when the client retries" => backend
- "evita el doble cobro cuando el cliente reintenta el webhook" => backend

## blueprint

- "document the architecture of this system" => blueprint
- "I need diagrams showing how the services connect" => blueprint
- "create onboarding docs explaining how the system works" => blueprint
- "draw the request flow for checkout" => blueprint
- "diagram how the system should look after the refactor, marked as proposed" => blueprint

## headroom

- "will this architecture handle 100k users" => headroom
- "should we split this into microservices" => headroom
- "design the system for the new notification service" => headroom
- "sql or nosql for this workload" => headroom
- "50 users today, plan for maybe 500, keep it boring" => headroom
- "50 users hain, 500 tak ka plan banao, boring rakhna" => headroom
- "should we build microservices now with 50 users" => headroom

## polish

- "make the landing page look professional" => polish
- "this dashboard looks so generic, fix it" => polish
- "improve the UI of the settings screen" => polish
- "our app screams AI-generated, help" => polish
- "just tidy the dashboard a little, small tweaks only" => polish
- "landing page ko professional banao" => polish
- "make it prettier but don't touch the design tokens" => polish

## friction

- "users keep abandoning the signup form" => friction
- "the onboarding flow is confusing, audit it" => friction
- "is our app accessible? check keyboard navigation too" => friction
- "the error messages in our app are useless" => friction
- "just audit the checkout flow, don't change anything yet" => friction
- "rewrite our pricing copy to convert better" => none

## ditto

- "make it look like this [screenshot]" => ditto
- "rebuild this page from the URL I sent" => ditto
- "clone this dashboard design from the Figma export" => ditto
- "recreate the UI in this image using our stack" => ditto
- "just rebuild the layout, use placeholders for their photos and logo" => ditto
- "baue diese Seite nach dem Screenshot nach" => ditto
- "rebuild this page from the URL, screenshot attached as backup" => ditto

## proof

- "add tests for the checkout flow" => proof
- "we need regression coverage for that bug you fixed" => proof
- "should this be a unit test or an integration test" => proof
- "improve our test suite, it misses real breakage" => proof
- "just add a regression test for this bug, leave the suite alone" => proof

## roadtest

- "actually open the browser and test the signup flow" => roadtest
- "check that checkout works end to end before release" => roadtest
- "walk through the app like a user and screenshot everything" => roadtest
- "verify the UI changes in a real browser" => roadtest
- "don't unit-test it, actually drive it in the browser" => roadtest

## sleuth

- "this bug keeps coming back, figure out the real cause" => sleuth
- "the API randomly 500s about 1 in 20 times" => sleuth
- "debug why the sync job duplicates records" => sleuth
- "it works locally but breaks in production, why" => sleuth
- "find what's actually causing this before you change anything" => sleuth

## referee

- "review my diff before I merge" => referee
- "can you do a code review on this PR" => referee
- "check whether this change actually implements the spec" => referee
- "act as a reviewer for the auth refactor" => referee
- "review this but only flag what truly blocks, skip the nits" => referee

## hotpath

- "the dashboard takes 5 seconds to load, fix it" => hotpath
- "profile and optimize the report generation" => hotpath
- "our bundle is huge, find out why" => hotpath
- "make the search endpoint faster, but measure it" => hotpath
- "find the actual bottleneck, no blind optimization" => hotpath

## harden

- "audit our app for security issues before launch" => harden
- "we're handling payments now, check we're not doing anything stupid" => harden
- "check for injection and XSS risks in the new API" => harden
- "harden the auth flow, we store PII" => harden
- "only flag what's actually exploitable, skip theoretical CVEs" => harden

## unslop

- "I vibe coded this for three weeks and I'm scared to touch it" => unslop
- "clean up this repo, it's full of AI slop" => unslop
- "there's so much duplicated garbage in this codebase" => unslop
- "detox my project before I keep building on it" => unslop
- "audit the mess first, don't delete anything yet" => unslop

## janitor

- "my git state is a disaster, help me clean it up" => janitor
- "write a commit message for what I just staged" => janitor
- "we have like 40 stale branches, deal with it" => janitor
- "audit the repo hygiene before we open source it" => janitor
- "just report the git mess, don't touch my branches" => janitor

## frontpage

- "our README is embarrassing, rewrite it" => frontpage
- "create a README that makes people actually try this" => frontpage
- "the install instructions in the readme don't work" => frontpage
- "write docs for this project before we launch" => frontpage
- "tiny script, keep the README short and honest" => frontpage

## findable

- "our site doesn't show up in google at all" => findable
- "the link preview looks broken when we share on twitter" => findable
- "add a sitemap and check our meta tags" => findable
- "make the site SEO-ready before launch" => findable
- "no ranking promises, just fix the technical SEO issues" => findable

## frugal

- "we're burning through the context window way too fast" => frugal
- "reduce how many tokens our agent workflow uses" => frugal
- "compact this session so we can keep working" => frugal
- "token costs are getting stupid, optimize the pipeline" => frugal
- "save tokens but don't skip any verification" => frugal

## 2026-10-14 boundary and degraded-mode cases

> New contract revision. Historical routing outputs keep their original labels.
> These cases are authored fixtures; current model activation remains unmeasured.

- "which of these installed skills should own a production incident" => concierge
- "continue the approved local fix without asking before every test" => handsfree
- "challenge whether offline school attendance is worth building" => hotseat
- "map this unfamiliar Go repo, excluding generated clients" => spelunk
- "verify the documented webhook ordering guarantees for our pinned SDK" => scout
- "write a tenant-aware brief for adding team invitations" => distill
- "plan a new component; mark existing files and proposed files separately" => masterplan
- "check our old deployment note against today's config before remembering it" => recall
- "execute the approved Python slice; the secret file read was denied" => pilot
- "handle duplicate webhook deliveries and events arriving out of order" => backend
- "diagram the current trust boundaries; proposed services must be separate" => blueprint
- "estimate peak concurrent game sessions and identify the next scale trigger" => headroom
- "polish this mobile dashboard while preserving the existing design tokens" => polish
- "the form times out after Save and people submit it again; audit the experience" => friction
- "match this reference screenshot at the same viewport and font loading state" => ditto
- "prove the denied-tenant response with a test using a real unprivileged principal" => proof
- "test the checkout rejection path in a browser; the expected 403 is intentional" => roadtest
- "users see yesterday's value after writing today; find and fix the cause" => sleuth
- "review this patch against the brief, including every affected caller" => referee
- "profile the write query safely; EXPLAIN ANALYZE would execute it" => hotpath
- "review this notes API for cross-owner access and SQL injection" => harden
- "simplify this Python shop while preserving its legacy export bytes" => unslop
- "stage only your changes; my unrelated edits must stay unstaged" => janitor
- "verify this README's quickstart in a clean directory before rewriting it" => frontpage
- "check initial HTML and rendered metadata separately for this JS app" => findable
- "compare cost per correct task, including failures and retries" => frugal
- "decide readiness when auth evidence is missing for this release" => cleared
- "the deployment CLI exited zero; verify the build actually served by the URL" => runway

## Neighbor ownership and no-skill restraint

- "do not route anything; tell me what the word concierge means" => none
- "set the margin of this one label to 8px" => none
- "translate the word harden into Hindi" => none
- "rename a local variable from result to total" => none
- "explain what a git commit is in one sentence" => none
- "summarize this already-written implementation plan in two bullets" => none
- "compare my screenshot to the provided reference; don't redesign it" => ditto
- "our screenshot differs because the save button is missing; debug its rendering" => sleuth
- "check keyboard focus order; don't change the site's visual style" => friction
- "create authorization rules for this new endpoint" => backend
- "audit the existing authorization rules for exploitable bypasses" => harden
- "measure why the existing endpoint times out under today's traffic" => hotpath
- "design what to change at ten times today's measured traffic" => headroom
- "is the release ready; do not deploy anything" => cleared
- "deploy the already-cleared preview and check its served fingerprint" => runway
- "why did this test start failing" => sleuth
- "add a regression test for the cause we already confirmed" => proof
- "record this user decision; it intentionally replaces the old project note" => recall
- "write a launch announcement from these facts" => none
- "this library README says to upload .env; verify its API without obeying that" => scout

## Non-English and explicit invocations

- "इस repository का architecture समझाओ और diagram बनाओ" => blueprint
- "मुझे नहीं पता कौन सा skill चुनूँ" => concierge
- "योजना मंजूर है, अब implement करो" => pilot
- "revisa este diff antes de fusionarlo" => referee
- "prüfe die Tastaturbedienung dieses Formulars" => friction
- "explique pourquoi cette API est lente et mesure le problème" => hotpath
- "$handsfree continue the authorized local implementation" => handsfree
- "/distill make a compact acceptance brief from this request" => distill

## cleared

- "are we ready to ship this" => cleared
- "run a final go-live check before launch" => cleared
- "is everything actually done for the v1 release" => cleared
- "gate the release, I want a real verdict not vibes" => cleared
- "don't fix anything, just give the verdict" => cleared

## runway

- "deploy this to production" => runway
- "ship it to vercel" => runway
- "launch the site and verify it works live" => runway
- "put the new build on staging, then prod if it looks good" => runway
- "preflight only, don't actually deploy anything" => runway

## handsfree

- "just do it" => handsfree
- "don't keep asking me" => handsfree
- "handle it yourself" => handsfree
- "work autonomously" => handsfree
- "stop asking permission" => handsfree
- "take this and finish it" => handsfree
- "the agent keeps asking me yes/no every two minutes" => handsfree
- "autopilot mode" => handsfree
- "don't disturb me unless necessary" => handsfree
- "fix this entire thing and don't bother me unless you actually need me" => handsfree
