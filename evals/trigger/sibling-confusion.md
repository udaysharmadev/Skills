# Sibling-confusion cases

Pairs of skills whose jobs are adjacent — the router must pick by the
user's *intent words*. Format matches cases.md (run via
`scripts/eval-trigger --suite sibling-confusion`).

> One expected slug per line; the sibling that must NOT win is the other
> member of the pair.

## polish vs friction

- "the signup form confuses people and they abandon it" => friction
- "this page looks like a 2009 government website" => polish

## spelunk vs blueprint

- "where in the codebase do we handle refunds" => spelunk
- "generate architecture docs for the new team" => blueprint

## distill vs masterplan

- "here's what I want, roughly: notifications that don't annoy people" => distill
- "the spec is agreed, figure out the build order" => masterplan

## proof vs roadtest

- "add tests so the next refactor doesn't break payments" => proof
- "click through the whole purchase flow in a real browser" => roadtest

## sleuth vs referee

- "the export job silently produces empty files sometimes" => sleuth
- "look over my branch before I open the PR" => referee

## harden vs cleared

- "we're handling card data now, find the holes" => harden
- "can we launch on friday, give me a real answer" => cleared

## backend vs headroom

- "implement pagination on the orders endpoint" => backend
- "will postgres still cut it when we hit 50k users" => headroom

## janitor vs frontpage

- "half our branches are merged but never deleted" => janitor
- "the readme still describes the v0 API" => frontpage

## pilot vs concierge

- "execute slice 3 of the dark mode plan" => pilot
- "just installed the bundle, what can it do here" => concierge

## scout vs spelunk

- "does drizzle still support the $dynamic API in 0.44" => scout
- "find where drizzle is configured in this repo" => spelunk
