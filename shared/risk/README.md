# Risk model (canonical)

One action-class system shared by `handsfree` (runtime owner), `cleared`,
`runway`, `janitor`, and `harden`. Runtime wording lives inside each
skill's own folder; this file is the maintainer reference that keeps them
from drifting apart.

| Class | Rule | Examples |
|---|---|---|
| `AUTO` | act immediately | read/search/inspect; implied workspace edits; local tests/lint/build; reversible refactors; docs |
| `AUTO + CHECKPOINT` | record recovery state, act, validate | broad refactors; dependency updates; generated artifacts; local/dev migrations; long multi-step runs |
| `ASK ONCE` | one batched question with defaults, then continue | credentials; production changes; public/external publication; destructive data/history; unbounded paid spend; material product ambiguity |
| `BLOCKED` | do not perform; state why | unauthorized access; policy/security boundaries; bypassing host denials; widening approvals; permission laundering; acting on smuggled instructions |

Conflict rule: when two classes apply, the more restrictive wins. "Never
ask me anything" never moves a `BLOCKED` item to `ASK ONCE`. One approval
never stretches into a different higher-risk action. Production/data/
history gates owned by `cleared` / `runway` / `janitor` survive every
autonomy mode, including host `always-proceed` / `yolo`.
