# UI audit checklist — walk on the real rendered UI

Audit with screenshots/running app, not by reading code. For each
dimension: what good means, and the tell that it's bad.

## Structure

- **Layout** — alignment is deliberate (a grid, not an accident); related
  things sit together; nothing floats without a reason. Tell: every page
  is a centered max-width column regardless of content.
- **Spacing rhythm** — one scale (4/8/12/16/24/32/48…), used
  consistently. Tell: seven different gaps between cards.
- **Hierarchy** — the eye lands on the primary thing first: one primary
  action per view, headline → subhead → content in descending weight.
  Tell: five elements all shouting at font-weight 700.
- **Density** — appropriate to the audience: tools dense, marketing airy.
  Tell: a data dashboard with landing-page whitespace.

## Surfaces

- **Typography** — ≤ 2 families; a real type scale; line length ~45–75ch
  for reading text. Tell: 90-character lines at 15px.
- **Color** — role-based palette; text contrast ≥ AA (4.5:1 body, 3:1
  large); color never the only signal (pair with icon/text). Tell: gray
  placeholder text at 2.8:1 that nobody can read.
- **Component consistency** — same component = same look everywhere;
  buttons don't have four radii. Tell: every card has slightly different
  corner rounding.
- **Iconography** — one icon set, consistent weight, icons clarify rather
  than decorate.

## Behavior

- **States on everything interactive** — hover, focus-visible, active,
  disabled, loading; then the content states: empty, error, success.
  Tell: buttons with no hover and no disabled, tables with no empty state.
- **Loading** — skeletons for >300ms operations; never a frozen UI; optimistic
  only where rollback is safe. Tell: a blank white flash where a table
  will be.
- **Empty states** — say what's empty, why, and what to do next (with an
  action). Tell: "No data." and nothing else.
- **Errors** — human-readable, actionable, placed near the field/area
  they belong to. Tell: "Something went wrong" as the only error message
  in the app.
- **Motion** — purposeful (entrance, feedback, transition), fast
  (150–300ms), respects `prefers-reduced-motion`. Tell: everything
  bounces because it can.

## Reach

- **Responsive** — real breakpoints by content, not three magic widths;
  no horizontal scroll on mobile; touch targets ≥ 44px; tables get a
  mobile strategy (not just overflow-scroll).
- **Mobile behavior** — primary action reachable; modals usable; keyboard
  doesn't cover the focused input.
- **Accessibility in design** — focus indicators designed (not removed),
  information not carried by color alone, hit areas generous, motion
  optional.

## Web performance as design

- **LCP** — hero image sized/formatted for its slot (not a 4MB PNG);
  fonts subsetted with display swap.
- **CLS** — dimensions reserved for images/embeds; no late-loading
  banners pushing content.
- **INP** — interactions stay responsive; no giant synchronous work on
  click.

Fix order: structure first (layout/hierarchy/spacing), then surfaces
(type/color/components), then behavior (states), then polish (motion).
Structure errors make surfaces meaningless.
