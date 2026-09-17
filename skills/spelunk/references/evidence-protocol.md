# Discovery evidence protocol

Use this for deep maps, risk maps, monorepos, or work that a later planner or
debugger will rely on. Quick answers need only the relevant observed path.

## Evidence record

| Field | Capture |
| --- | --- |
| Question and target | decision to support and app/package boundary |
| Provenance | repository root, commit or tree state, and check date |
| Observed paths | manifests, entrypoints, configuration, symbols, tests read |
| Traced path | one real route, command, or lifecycle with symbol anchors |
| Inferences | conclusion plus observed evidence supporting it |
| Unknowns | missing runtime, ownership, generated, or external evidence |
| Recheck trigger | commit, package, config, or task change that invalidates map |

## Monorepo routing

Identify workspace manager, package graph, target app, shared packages, and
deployment ownership. Follow only dependencies that change the target behavior.
Report sibling packages as not covered unless read; do not generalize one app's
scripts or patterns to the whole repository.

## Risk-map evidence

A hotspot needs an observed complexity signal, churn signal when Git is
available, trust boundary, test gap, or contradiction. Churn alone is not a
defect. Name the likely owning skill and the evidence gap before recommending a
change.

## Handoff rule

Give next worker source paths, symbols, command definitions, active unknowns,
and the next narrow read. Do not paste inventory output or turn a map into an
implementation plan.
