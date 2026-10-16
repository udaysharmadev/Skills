# polish: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/polish/references/rendered-evidence.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [Understanding Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html); read 2026-10-14; WCAG 2.2 explanatory guidance; criteria and exceptions govern scope | Test focus after scrolling, validation and sticky UI changes. | Does not establish whole-product accessibility conformance. |
| [Modal Dialog Example](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/dialog/); read 2026-10-14; Living example; not a production widget certification | Verify mobile dialog/focus behavior and name untested device combinations. | Copying an example is not evidence the target product works. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. Sticky footer entirely covers focused control.
2. Keyboard hides submit action.
3. Modal closes without focus return.
4. Long localized error breaks form width.
5. Zoom/reflow creates avoidable two-axis scroll.
6. Dark theme contrast inferred from light theme.
7. Loading indicator removes available action.
8. Status communicated by color alone.
9. Disabled button hides unresolved save.
10. Reduced motion removes essential state feedback.
11. Screenshot uses only pristine short data.
12. Global token edit breaks adjacent route.
13. Viewport emulation called device proof.
14. Style preference used to override explicit user direction.
15. Static scan called full accessibility conformance.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (polish row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| W3C WCAG 2.2 SC 2.5.8 + web.dev INP/LCP/CLS; fetched 2026-10-14, CLS resolved 2026-10-17 | SC 2.5.8 24px rule in audit reference; INP 200ms / LCP 2.5s / CLS 0.1 at p75 in workflow (https://web.dev/articles/defining-core-web-vitals-thresholds). |
