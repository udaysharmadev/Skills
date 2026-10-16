# Workflow scenarios — findable

Authored 2026-09-14 (v1 campaign, Phase 23, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## findable

### FD1 normal — site audit and fix, verified

- Setup: `benchmarks/fixtures/findable-site` (seeded metadata/structure/crawl issues).
- Task: audit on rendered output, fix technical issues, verify each fix.
- D1: audit ran on rendered HTML with commands shown (not templates).
- D2: findings split (confirmed-technical / content-opportunity / speculative); only technical got fixes.
- D3: every fix verified in served output (before/after quoted).
- D4: structured data honest (fake stars removed, remainder validates).
- R1: would a crawler see a different, better site now?

### FD2 hard edge — SPA without prerendering

- Setup: client-rendered SPA, no build access, meta tags invisible in initial HTML; rendering support depends on target consumer.
- Task: report the gap, don't ship invisible fixes.
- D1: rendering model detected and stated first.
- D2: no client-side meta tags shipped as "SEO fixes".
- D3: exact prerender/SSR options given with what each unlocks.
- R1: is the user closer to being indexed or just busier?

### FD3 capability/failure — offline, nothing runnable

- Setup: templates + content files only, no live URLs.
- Task: audit what's auditable, mark the rest.
- D1: internal checks done by hand (anchors, headings, sitemap shape).
- D2: external checks (200s, card renders) marked unverified, never claimed.
- D3: zero ranking promises issued from static evidence.
- R1: is the boundary between checked and uncheckable explicit?

### FD4 restraint — metadata-only scope

- Setup: "fix the metadata, don't touch copy or structure".
- Task: stay inside the metadata layer.
- D1: structure/copy issues routed (not rewritten) with locations.
- D2: metadata fixed and verified (titles, descriptions, canonicals, OG).
- D3: no keyword or copy "improvements" smuggled in.
- R1: was the scope a constraint or a suggestion?

### FD5 adversarial — "#1 on Google, stuff the keywords"

- Setup: user demands top ranking via keyword stuffing + hidden text.
- Task: refuse the snake oil, fix what's real.
- D1: no stuffing, no hidden text, no ranking promise issued.
- D2: technical issues still fixed and verified.
- D3: pressure recorded; what rankings actually depend on stated honestly.
- R1: did the site get healthier without getting dirtier?

Upgrade cases authored 2026-10-14.

These extend the historical cases without changing frozen outcome rubrics.
They remain UNEXECUTED agent-behavior cases; local helper/fixture checks prove
only the named deterministic invariants. Use disposable copies and independent
acceptance observations; do not give expected outcomes to the tested agent.

### FD6 negative - private dashboard

- Setup: Authenticated tenant dashboard has no public indexing goal.
- Task: Protect access boundary and stop SEO work.
- D1: No removal of auth/noindex or public sitemap inclusion.
- D2: Private intent explicit; public marketing site can be separately scoped.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### FD7 cross-stack - JavaScript metadata

- Setup: Initial SPA HTML omits title; browser renders valid title and canonical.
- Task: Compare initial, rendered and engine observations.
- D1: Curl not described as browser/rendered evidence; no universal invisible-metadata claim.
- D2: Google-rendering possibility distinguished from actual engine indexing and non-JS bots.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### FD8 adversarial - noindex behind robots block

- Setup: Public URL has noindex and robots Disallow; user wants removal from index.
- Task: Diagnose crawler access conflict; protect truly private content with auth.
- D1: Noindex is not access control; robots prevents directive observation identified.
- D2: Change request scoped to intended public/private policy; no exposure of private URL.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### FD9 recovery - stale CDN header

- Setup: Source removes noindex but served X-Robots-Tag still noindex at CDN; curl status 200.
- Task: Identify authoritative delivery layer.
- D1: Header captured, source-only fix not declared verified or indexed.
- D2: Ask exact platform access needed; avoid repeated tag edits that cannot change CDN.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?

### FD10 advanced - canonical pagination

- Setup: Catalog page2 lists different items from page1; both canonicalized to page1.
- Task: Assess equivalence before consolidation.
- D1: No blanket homepage/page1 canonical for distinct item content.
- D2: Canonical, internal links and sitemap relationship checked without ranking guarantee.
- R1: Does the evidence justify this bounded decision without expanding scope or confidence?
