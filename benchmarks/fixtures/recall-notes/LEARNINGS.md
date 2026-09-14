# Learnings

## 2026-09-10 unittest needs tests/__init__.py for discover
- `python -m unittest discover -s tests` fails on 3.14 without an importable start dir; ship `tests/__init__.py`.

## 2026-09-12 pycache poisons scope checks
- Python bytecode in the workdir counts as changed files; filter it before grading.
