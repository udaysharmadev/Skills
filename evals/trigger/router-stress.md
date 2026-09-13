# Router stress cases

Adversarial/multi-skill routing. Expected values are ordered workflows
(arrow chains) or `none`. These exercise concierge's "smallest
sufficient workflow" rule under pressure — the router fails if it
routes to one skill when several are needed, or to a chain longer than
necessary.

> Chains are expected as ordered slug sequences; the eval accepts
> reasonable order variations only via exact match today (documented
> limitation).

## Multi-skill routes

- "make the app prettier and also users keep abandoning checkout" => friction→polish→roadtest
- "research the correct stripe webhook approach and then implement it" => scout→backend→proof
- "this repo is a mess and auth randomly fails in production" => spelunk→sleuth→proof
- "I have an app idea, help me scope an mvp then plan it" => hotseat→distill→masterplan
- "the dashboard is slow and the readme is embarrassing" => hotpath→frontpage
- "add oauth login, make sure it's tested and secure" => backend→proof→harden

## Direct specialist requests (route straight there)

- "use the harden checklist on src/auth" => harden
- "ask the hotseat panel about my pricing idea" => hotseat
- "write the commit message for my staged changes" => janitor

## No-skill routes (nothing here should steal these)

- "remind me to call the dentist tomorrow" => none
- "what's the capital of Australia" => none
- "translate this paragraph to German" => none

## Degraded-capability routes

> Run with capabilities disabled (no browser, no web). The expected
> skill should still route — its own fallback honesty is what is under
> test, not the routing.

- "walk the checkout flow in a browser" => roadtest
- "research the newest react version" => scout
