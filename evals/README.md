# evals/

Evaluation assets. Nothing in this directory may be used to claim a number
that was not actually measured (PRD §3.4, §13).

| Directory | Purpose | Status |
| --- | --- | --- |
| `trigger/` | Utterance → expected-skill cases (positive AND negative) | fixtures maintained; live runner not wired |
| `workflow/` | Did the agent follow the skill's important phases | planned with Phase 2+ skills |
| `regression/` | Bugs found in the field, captured as cases | populated as issues land |
| `fixtures/` | Representative stack fixtures (TS/web, Python, Go/Rust, JVM, mobile) | planned (PRD §12) |

## Honesty contract

- `scripts/run-evals` currently validates fixture well-formedness only.
- Until a live runner executes cases against real agents, **no trigger
  precision/recall numbers may appear in any README or doc**.
