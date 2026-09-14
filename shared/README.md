# shared/ — canonical contracts

This directory is the **canonical source** for the bundle's cross-cutting
contracts: principles, naming, artifact conventions, capability tiers.

## The self-containment rule

Everything here is for **humans and repo tooling**. At runtime, a skill
folder is copied alone into a user's repository (`npx skills add`), so:

- a `SKILL.md` must never point at `../../../shared/...`;
- each skill **inlines** the parts of these contracts it depends on;
- cross-skill cooperation happens by **slug name** ("hand off to `scout`"),
  never by file path.

When a contract here changes, update the skills that inline it in the same
PR. `scripts/validate-skills` cannot catch drift in prose — reviewers must.

## Contents

| Directory | Contract |
| --- | --- |
| `principles/` | The six product principles every skill must honor |
| `terminology/names.md` | Naming system, collision watchlist, pre-approved alternates |
| `terminology/artifacts.md` | Which skill owns which file on disk |
| `capability-map/` | Capability tiers, detection order, fallback ladder |
| `report-schemas/` | Reserved extraction point for output shapes shared by multiple skills |
| `security/` | Cross-skill security contract boundary; current rules link to their canonical owners |
