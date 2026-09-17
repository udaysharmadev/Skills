# blueprint research ledger

## Source 1

Title: C4 model diagrams

Author / Organization: Simon Brown

Publication date: Living documentation

Version: Current website

URL: https://c4model.com/diagrams

Source type: official docs

What it establishes:
C4 offers hierarchical architecture views and says teams need only the diagram levels that add value.

What this skill adopts:
Default to context and container views, adding component, dynamic, or deployment views only when they answer a real question.

What it does NOT establish:
It does not require all architecture evidence to live in source code or require all four levels.

Numbers taken from source:
Four core static diagram levels are defined; no project diagram count is adopted.

Reverify when:
The C4 model guidance changes.

## Architecture abstractions

Title: Abstractions

Author / Organization: C4 model

Publication date: 2026

Version: Current website

URL: https://c4model.com/abstractions

Source type: official docs

What it establishes:
A software system contains applications and data stores called containers;
containers contain components, which are implemented by code elements.

What this skill adopts:
Use consistent abstraction labels and avoid calling every folder, class, or
deployment unit a C4 component or container.

What it does NOT establish:
It does not prescribe a repository layout, cloud topology, or diagram count.

Numbers taken from source:
None.

Reverify when:
The selected architecture notation or reader needs change.

## Decision records

Title: Architectural Decision Records

Author / Organization: ADR GitHub organization

Publication date: 2026

Version: Current website

URL: https://adr.github.io/

Source type: official docs

What it establishes:
An ADR captures one architecturally significant design choice with rationale,
trade-offs, and consequences as part of a maintained decision log.

What this skill adopts:
Create ADRs only for load-bearing decisions and include alternatives,
consequences, status, authority, and supersession information.

What it does NOT establish:
It does not establish who may decide, require an ADR for every implementation
choice, or prove a proposal is accepted.

Numbers taken from source:
None.

Reverify when:
The project decision-record convention or architecture governance changes.

## Diagram-as-code limits

Title: About Mermaid

Author / Organization: Mermaid project

Publication date: 2026

Version: 12 documentation

URL: https://mermaid.js.org/intro/

Source type: official docs

What it establishes:
Mermaid renders text definitions into diagrams and supports multiple diagram
types, enabling diagrams to be versioned alongside documentation.

What this skill adopts:
Keep source-controlled Mermaid as the portable default, distinguish syntax
validation from visual rendering, and preserve source alongside HTML output.

What it does NOT establish:
It does not ensure a diagram is accurate, legible, secure for arbitrary input,
or rendered consistently by every host.

Numbers taken from source:
Version 12 is the reviewed documentation major version.

Reverify when:
Mermaid syntax, renderer, hosting environment, or security configuration
changes.
