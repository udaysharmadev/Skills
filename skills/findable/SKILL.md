---
name: findable
description: SEO and discoverability for public web projects — titles, metadata, canonical URLs, semantic HTML, robots, sitemaps, structured data, social previews and crawlability. Use when a site needs to be findable on search engines or social shares, when the user mentions SEO, meta tags, Open Graph, sitemap, search ranking or discoverability, before launch of a public site, or when shared links render badly. Evidence-based only — no snake-oil ranking promises.
---

# findable — be findable by humans and machines

Discoverability is engineering, not incantations: correct metadata,
semantic structure, crawlable pages, honest structured data. You audit
against verifiable checks and fix what's broken — no ranking promises,
no keyword stuffing, no snake oil.

## When NOT to use

- README/docs discoverability on GitHub → `frontpage`.
- Content quality/copy → that's writing work, `frontpage`-adjacent; you
  handle the machine layer around it.
- Private/authenticated apps — no crawling surface, say so and stop.

## Prerequisites

Detect the rendering model first — it decides everything: SSR/SSG
(full metadata control), SPA (needs prerendering or SSR for crawlers),
static (direct control). Audit the **rendered** HTML (curl/view-source
of live pages), never just the source templates — client-side-rendered
meta tags that crawlers never see are the classic invisible failure.

## Workflow

### 1. Crawl-surface audit

Walk `references/seo-checklist.md` on the real rendered pages:

- per-page uniqueness: titles, meta descriptions, canonicals;
- semantic HTML: one `h1`, heading hierarchy, real landmarks;
- `robots.txt` + `sitemap.xml`: present, accurate, submitted;
- structured data: valid, honest (schema.org — validate it);
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
  image metadata are ranking-adjacent — flag them, deep work belongs to
  `hotpath`.
- **Accessibility overlap:** semantic headings, alt text, link purpose —
  same work serves both; note the dual value.
- **Content hierarchy:** pages need a topic; a page about everything
  ranks for nothing. Flag structure problems; writing the content is
  the user's or `frontpage`'s job.

### 4. GEO/AEO (only with evidence)

AI/answer-engine discoverability is emerging and poorly standardized:
the evidence-based part is the same as good SEO (clean semantic HTML,
structured data, factual content, stable URLs). Anything beyond that —
"AI ranking hacks", secret llms.txt rituals — is presented as
unproven speculation or not at all.

## Quality gates

- Audit ran on rendered HTML of real URLs, with the commands shown.
- Every fix verified in served output (before/after evidence).
- Titles/descriptions: unique + descriptive per page, no template
  duplication across pages.
- Structured data validates and describes only what's on the page —
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
