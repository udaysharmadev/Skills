# generated/ — derived facts, never hand-edited truth

This directory holds files produced by `scripts/build-docs` (and future
generators: routing manifest, composition graph, benchmark dashboard) from
canonical sources (`skills/*/SKILL.md` frontmatter, `docs/claims.md`,
eval result files).

Rule: generators read truth; humans read generated files. CI fails on
drift (`git diff --exit-code` after rebuild). If a generated fact looks
wrong, fix the source and rebuild — never patch the output.
