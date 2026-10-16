# blueprint research ledger

Accessed 2026-10-14. Sources below were inspected in this upgrade; moving
documentation/branches are not evidence of installed versions or host compatibility.
No numerical default, empirical prevalence, or comparative lift is adopted.

## Source 1

Title: Usage: securityLevel

Author / Organization: Mermaid project

Publication date: Not verified; living documentation/source accessed 2026-10-14

Version: Living docs (v12.2.0 served 2026-10-16); selected template requests major 12 without exact pin

URL: https://mermaid.js.org/config/usage.html

Source type: official docs

What it establishes:
Strict rendering encodes HTML labels and disables click behavior.

What this skill adopts:
Set strict explicitly and escape other HTML substitutions.

What it does NOT establish:
Does not sanitize arbitrary template content or prove diagram truth.

Numbers taken from source:
None. Version identifiers describe source scope, not measurements.

Reverify when:
The target installed version, protocol, runtime, standard or relevant behavior changes.

## Source 2

Title: Default configuration implementation

Author / Organization: Mermaid project

Publication date: Not verified; living documentation/source accessed 2026-10-14

Version: Moving develop branch; not template installed-version evidence

URL: https://raw.githubusercontent.com/mermaid-js/mermaid/develop/packages/mermaid/src/defaultConfig.ts

Source type: implementation evidence

What it establishes:
Configuration implementation and documentation are separate surfaces; source inspected.

What this skill adopts:
Record the actual renderer separately and never treat the heuristic as a parser.

What it does NOT establish:
Inspection of this file did not verify an exact securityLevel default; no such code claim is adopted.

Numbers taken from source:
None. Version identifiers describe source scope, not measurements.

Reverify when:
The target installed version, protocol, runtime, standard or relevant behavior changes.
