# Security contracts

Canonical security rules for bundled scripts and the `harden` skill's audit
checklists (OWASP Top 10:2025 baseline, ASVS 5.0.0 depth).

The safe-by-default rules for contributed scripts live in
[SECURITY.md](../../SECURITY.md). The complete audit framework lives inside the
self-contained `harden` package at
`skills/harden/references/attack-surface.md`.

This directory is the extraction point for a security rule only after multiple
skills need one canonical maintainer contract. It is not a runtime dependency.
