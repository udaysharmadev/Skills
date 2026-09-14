# frugal — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Engineering Anti-Patterns (2025/2026) | "Context Dumping" degrades model reasoning ("Lost in the Middle") and burns tokens unnecessarily when standard CLI tools could have filtered the data first. | Bans "Context Dumping (Blind Ingestion)", enforcing the use of `grep`, `jq`, and `awk` before reading data into the window. | SKILL.md §Banned List |
| Lossy Compression in Memory | Aggressively summarizing logs or traces to save tokens destroys the exact structural identifiers (line numbers, IDs) needed to actually solve the problem. | Bans "Lossy Compression," establishing that diagnostic payloads must never be destructively summarized. | SKILL.md §Banned List |
| Chatty Reasoning overhead | Outputting extensive "thinking" paragraphs directly to the user wastes output tokens and clutters the session. | Bans "Chatty Reasoning", forcing compactness. | SKILL.md §Banned List |

## Key new intelligence encoded

1. **ContextOps / Context Engineering** — shifts the paradigm from "infinite context" to "selective injection," recognizing that large context windows are a liability if filled with noise.
2. **Preservation of Diagnostics** — creates a hard boundary on token optimization: you may compact prose, but you may never compress a stack trace.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM Context Limits | "Lost in the Middle" degradation benchmarks (2026) |
