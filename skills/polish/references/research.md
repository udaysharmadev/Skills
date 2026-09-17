# polish research ledger

## Source 1

Title: Web Content Accessibility Guidelines (WCAG) 2.2

Author / Organization: W3C

Publication date: 2023-10-05

Version: W3C Recommendation

URL: https://www.w3.org/TR/WCAG22/

Source type: standard

What it establishes:
WCAG 2.2 defines testable accessibility success criteria for web content.

What this skill adopts:
Treat keyboard, focus, contrast, reflow, target size, and motion as product-quality constraints where applicable.

What it does NOT establish:
It does not define visual taste or mandate a particular design style.

Numbers taken from source:
Any criterion number or threshold must be cited with its documented exceptions.

Reverify when:
W3C publishes a newer Recommendation or erratum.

## Accessible interaction patterns

Title: ARIA Authoring Practices Guide: Patterns

Author / Organization: W3C Web Accessibility Initiative

Publication date: 2026

Version: Current guide

URL: https://www.w3.org/WAI/ARIA/apg/patterns/

Source type: official docs

What it establishes:
Common widgets require defined keyboard interaction, focus management, and
semantic roles/states. Native elements are preferable where they provide the
needed behavior.

What this skill adopts:
Inspect keyboard paths and semantics for changed controls and overlays. Treat
custom controls as behavior and semantics work, not visual replacements.

What it does NOT establish:
It does not prescribe a visual system, page layout, or custom component library.

Numbers taken from source:
None.

Reverify when:
A changed interface adds a custom composite widget or the guide materially
changes.

## Layout stability

Title: Optimize Cumulative Layout Shift

Author / Organization: web.dev

Publication date: 2026

Version: Current article

URL: https://web.dev/articles/optimize-cls

Source type: official docs

What it establishes:
Unexpected layout movement is a user-experience problem and can be reduced by
reserving space and avoiding late visual changes.

What this skill adopts:
Verify layout stability around images, fonts, banners, asynchronous content, and
skeletons after a visual change.

What it does NOT establish:
It does not guarantee a Core Web Vitals result in a different environment or
make every animated layout change incorrect.

Numbers taken from source:
No numerical performance target is adopted.

Reverify when:
The rendering path, asset strategy, or performance guidance changes.

## Interaction responsiveness

Title: Optimize Interaction to Next Paint

Author / Organization: web.dev

Publication date: 2026

Version: Current article

URL: https://web.dev/articles/optimize-inp

Source type: official docs

What it establishes:
Interaction responsiveness includes input delay, processing time, and rendering
delay, and must be measured in context.

What this skill adopts:
Inspect changed interaction handlers and report measurement conditions rather
than treating visual smoothness as evidence of responsiveness.

What it does NOT establish:
It does not select a framework or prove field performance from a local trace.

Numbers taken from source:
No numerical target is adopted.

Reverify when:
Interaction architecture, measurement tooling, or performance guidance changes.

## Motion preference

Title: prefers-reduced-motion

Author / Organization: MDN Web Docs

Publication date: 2026

Version: Current reference

URL: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

Source type: official docs

What it establishes:
The media feature exposes a user preference to minimize non-essential motion.

What this skill adopts:
Verify that changed motion has an understandable reduced-motion alternative.

What it does NOT establish:
It does not define every user's motion needs or make all animation harmful.

Numbers taken from source:
None.

Reverify when:
Motion implementation or browser/platform support changes.
