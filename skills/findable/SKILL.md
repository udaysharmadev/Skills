---
name: findable
description: Audits and improves web discoverability across crawlability, HTTP status, rendering, indexability, canonical metadata, titles, descriptions, internal links, sitemaps, robots rules, social previews, and eligible structured data. Use for technical SEO without ranking promises.
---

# findable: be findable by humans and machines

Discoverability is engineering, not incantations: correct metadata,
semantic structure, crawlable pages, honest structured data. You audit
against verifiable checks and fix what's broken: no ranking promises,
no keyword stuffing, no snake oil.

## When NOT to use

- README/docs discoverability on GitHub → `frontpage`.
- Content quality/copy → that's writing work, `frontpage`-adjacent; you
  handle the machine layer around it.
- Private/authenticated apps: no crawling surface, say so and stop.

## Prerequisites

Detect the rendering model first because crawler support varies. Google can
execute JavaScript and process rendered metadata, while some other crawlers do
not. SSR or SSG is usually more robust, but it is not universally required.
Audit both the HTTP response and rendered HTML instead of assuming either one
is what every crawler sees.

## Authority, scope, and evidence boundaries

Findable audits public discoverability surfaces. It does not promise rankings,
submit a sitemap, request indexing, change robots/CDN rules, publish content,
or create search-console accounts without explicit authority. Treat each result
as one of: observed HTTP/rendered evidence, platform/search-console evidence,
repository configuration evidence, inference, or unverified.

Never expose private URLs, credentials, tokens, customer pages, or staging
hosts in a durable public report. Do not make a private/authenticated surface
crawlable as an SEO improvement. Preserve privacy, access control, and legal
requirements over discoverability.

## URL inventory and indexability model

Inventory representative URLs by page type before touching metadata:

| Page type | Canonical candidate | Audience | Render path | Index intent | Evidence |
| --- | --- | --- | --- | --- | --- |
| Homepage | absolute URL | public | SSR/SSG/client | index/noindex | HTTP + rendered |
| Listing/detail/article | absolute URL | public | same | index/noindex | HTTP + internal link |
| Search/filter/pagination | canonical rule | public | same | conditional | query/robots evidence |
| Auth/admin/account | n/a | private | any | noindex/private | access policy |
| Preview/staging | n/a | non-public | any | noindex/auth | deployment config |

Diagnose in order: URL discovery and response status, robots/crawl access,
rendered content and metadata, canonical/indexing eligibility, internal-link
reachability, then search-engine observation where access exists. An indexed
page can still rank poorly; a perfectly authored title cannot repair an
unreachable or noindexed page.

## Metadata and structured-data decision framework

One canonical URL represents one materially equivalent public page. Parameter,
locale, pagination, alternate format, and duplicate routes need an intentional
relationship, not blanket canonicalization to the homepage. Confirm that a
canonical target is public, indexable, and semantically equivalent before
declaring it correct.

Use structured data only when its type and properties are visibly true for the
page. Validate syntax and required fields, then compare claims to rendered
content. Do not add review, product, author, event, FAQ, price, or organization
claims simply because a schema type permits them. Treat rich-result eligibility
as an outcome search engines control, not a deliverable this skill can promise.

## Tool selection/fallback

- Live URLs + curl → rendered-HTML audit; every fix verified in served
  output (before/after).
- Validator available (schema.org, card debuggers) → structured data
  and previews proven; otherwise tags resolve to real assets by hand.
- Offline / no runnable site → static audit of templates + content
  files; external checks marked unverified, never claimed 200.

## Workflow

### 1. Crawl-surface audit

Walk `references/seo-checklist.md` on the real rendered pages:

- per-page uniqueness: titles, meta descriptions, canonicals;
- semantic HTML: one `h1`, heading hierarchy, real landmarks;
- `robots.txt` + `sitemap.xml`: present, accurate, submitted;
- structured data: valid, honest (schema.org: validate it);
- social previews: Open Graph + Twitter cards rendering correctly;
- crawl traps: noindex on public pages, broken internal links, orphan
  pages, duplicate content via parameter URLs.

### 2. Fix with verification

Every fix verified against the live/rendered output:

- `curl -s <url>` shows the meta in the served HTML;
- structured data passes a validator;
- social preview renders in a card debugger (or at minimum the OG tags
  resolve to real, correctly-sized images);
- sitemap URLs all return 200 and are canonical.

### 3. The overlap checks

- **Performance overlap:** page weight, render-blocking resources and
  image metadata are ranking-adjacent: flag them, deep work belongs to
  `hotpath`.
- **Accessibility overlap:** semantic headings, alt text, link purpose,
  same work serves both; note the dual value.
- **Content hierarchy:** pages need a topic; a page about everything
  ranks for nothing. Flag structure problems; writing the content is
  the user's or `frontpage`'s job.

### 4. GEO/AEO (only with evidence)

AI/answer-engine discoverability is emerging and poorly standardized:
the evidence-based part is the same as good SEO (clean semantic HTML,
structured data, factual content, stable URLs). Anything beyond that,
"AI ranking hacks", secret llms.txt rituals: is presented as
unproven speculation or not at all.

### 5. Verify deployment and monitor the chain

After a fix, verify the exact served candidate through a normal request and
rendered output where relevant. Check status/redirect chain, canonical target,
robots directives, title/description, structured-data payload, social asset
resolution, internal links, sitemap membership, and the noindex/auth boundary
for non-public surfaces. Capture commit/environment/time.

If search-console or platform evidence exists, distinguish discovered,
crawled, indexed, and presentation/rich-result observations. Each can lag
deployment and each can fail independently. Report what must be re-crawled or
watched later, but do not treat time-delayed indexing as a failed code fix.

## Failure handling and edge cases

- **No live URL:** static audit only; label served/rendered/indexing claims
  unverified and specify the build/preview command needed.
- **Redirect/canonical conflict:** preserve the chain, identify the competing
  owner/configuration layers, and fix only after confirming desired public URL.
- **Client-only metadata:** verify actual rendered output before claiming a
  crawler sees it; route rendering architecture decisions to the appropriate
  owner.
- **Robots controlled upstream:** report exact response/header/config layer and
  request access. Do not compensate with page tags that contradict the proxy.
- **International/multi-domain site:** treat locale and hostname variants as
  separate URL relationships. Do not infer hreflang/canonical policy.
- **Structured-data validator passes but content differs:** classify as a
  correctness issue, remove/repair the misleading claim, then revalidate.

## Anti-Patterns (The Banned List)

- **Slop Content Generation**: generating 5,000 words of generic, keyword-stuffed AI text to "rank better." 2026 ranking engines penalize volume-based slop. Discoverability is earned through technical structure and actual human-valuable content, not text generation.
- **Hallucinated Structured Data**: an agent auto-generating schema.org JSON-LD that includes fake 5-star reviews, hallucinated authors, or URLs that 404. Structured data must strictly describe the verifiable reality of the page.
- **Invisible Meta Tags**: an agent appending `<meta>` tags using client-side React/Vue in a pure SPA without SSR. If you don't prerender it, the crawler won't see it, and the fix is a hallucination.

## Quality gates

- Findings separated into **confirmed technical issue** (evidence in
  rendered output), **content opportunity** (needs writing, not code),
  and **speculative growth suggestion** (labeled as such or cut). Only
  the first category gets "fix" treatment; the second gets routed
  (frontpage/user); the third never becomes a ranking promise.
- Audit ran on rendered HTML of real URLs, with the commands shown.
- Every fix verified in served output (before/after evidence).
- Titles/descriptions: unique + descriptive per page, no template
  duplication across pages.
- Structured data validates and describes only what's on the page,
  fake review stars are a penalty, not a trick.
- Zero unverifiable ranking claims in the report.

## Stop conditions

- Audit + fixes verified → report with re-crawl notes, stop.
- SPA without prerendering and no build access → report the gap and the
  exact prerender/SSR options; don't ship meta tags no crawler will see.
- Indexing blocked at a level above the code (robots at proxy/CDN,
  noindex from the platform) → name the layer, hand off.

## Output contract

Chat: findings table (page/check/status/evidence), fixes applied with
before/after verification, what needs platform-level access. On
request: `docs/reports/seo-<slug>.md` with provenance header.

## Research basis

Read [references/research.md](references/research.md) when a decision depends on
an external standard, a numerical claim, or a fast-moving practice. The ledger
records what the source supports, what it does not support, and when to reverify.
