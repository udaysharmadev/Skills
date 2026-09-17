# SEO checklist: verify on rendered HTML, per page type

Commands assume `curl -s <url>`; the rendered/deferred HTML matters more
than the template.

## Per-page metadata

| Check | Good | Broken tell |
| --- | --- | --- |
| Title | unique, descriptive, and checked in target result surfaces | every page: "Home: MyApp" |
| Meta description | unique and useful to searchers | missing, or one description site-wide |
| Canonical | absolute, self-referencing, protocol+host exact | missing; canonical to homepage everywhere |
| Open Graph | og:title, og:description, og:image (1200×630), og:url | absent; image 404s; relative URL |
| Twitter card | summary_large_image + matching tags | absent |
| Robots meta | index,follow on public pages | noindex left from staging (the classic) |

## Structure

- Exactly one `h1` per page stating the topic; `h2`/`h3` form a real
  outline, not a styling ladder.
- Semantic landmarks: `header/nav/main/article/footer`; lists are
  `<ul>`, not div stacks.
- Links: descriptive anchors ("read the migration guide", never
  "click here"); no orphan pages (every public page reachable from
  internal links); no broken internal links.
- Images: descriptive alt; width/height set (CLS); modern formats where
  cheap.

## Crawlability

- `robots.txt`: exists, doesn't block public paths, sitemap referenced.
- `sitemap.xml`: only canonical 200s, lastmod honest, size limits
  respected.
- Duplicate content: parameter URLs (utm, sort, page) canonicalized;
  trailing-slash/case variants resolve to one canonical.
- Avoid unnecessary redirect chains; no soft-404s (successful status with
  not-found content).
- Staging environments: noindex + auth: they must never be crawlable.

## Structured data (schema.org)

- Types that match reality: Organization, WebSite (+ SearchAction if a
  search exists), Article/BlogPosting for posts, Product with offers for
  products, BreadcrumbList for deep sites, FAQPage for actual FAQs.
- Validates (Rich Results Test / validator.schema.org); required
  properties present; **describes only content actually on the page**.
- **Anti-Hallucination Check:** Verify the JSON-LD does not contain fake 5-star `AggregateRating` reviews, hallucinated authors, or URLs that 404. Fabricating schema data is an anti-pattern.
- JSON-LD in the served HTML (not injected client-side only).

## Performance & accessibility overlap (flag, don't deep-dive)

- LCP image not lazy-loaded; hero under 2.5s budget → `hotpath`.
- Render-blocking chains and uncompressed assets → `hotpath`.
- Alt text, heading order, link purpose → `friction`; dual-value work
  gets done once, credited twice.

## GEO/AEO (answer engines): evidence-based only

What's defensible: stable URLs, semantic HTML, structured data, factual
self-contained content, clear headings that answer questions. What
isn't: "llms.txt will boost your rank", keyword-stuffed "AI summaries",
any claim of guaranteed AI citations. Present the defensible part as
standard good practice; decline the rest as unproven.
