# Skill constitution

The official [Agent Skills specification](https://agentskills.io/specification)
is the structural authority.

A shipped skill must:

1. contain a valid `SKILL.md` whose name matches its directory;
2. describe what it does and when it activates in frontmatter;
3. own one clear job and name adjacent work it does not own;
4. inspect evidence before making consequential decisions;
5. distinguish observed facts, inferences, and unknowns;
6. define approval boundaries for destructive, expensive, or external actions;
7. recover deliberately after failed attempts instead of looping;
8. specify a minimum useful output and proof of completion;
9. keep optional depth in focused, one-level references;
10. work when copied alone, without a sibling or repository-only runtime file;
11. include a local research ledger with explicit limitations;
12. avoid unexplained thresholds and unsupported claims.

Scripts exist only for repeatable deterministic work. Assets exist only when a
reusable output artifact needs them. No skill depends on the experimental
`allowed-tools` field for its core workflow.
