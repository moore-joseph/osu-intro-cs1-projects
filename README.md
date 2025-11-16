# OSU CS161 - Introduction to Computer Science 1 Projects

This repository contains a collection of projects from Oregon State University's post baccalaureate Introduction to Computer Science I course.

These were originally completed as coursework and have been imported from an older student GitHub account. I am now reviewing, improving and restructuring these projects to show:

- Clean Python code and structure
- Effective use of vesion control
- Automated testing using `pytest`
- Continuous Integration via Github Actions
- Refactoring earlier work to match my current engineering practices

Each project resides in `projects/` with:
- **A single `*.py` file** -- the *refactored* version. The original student submission is preserved in Git history, not as a separate file.
- **A per-project `README.md`** -- describing the assignment and the improvements.
- **Tests in the top-level `tests/` directory** with project names like `test_project_1_*.py`, `test_project_2_*.py`, etc.
- **Two focused PRs per project**:
    - `project-n-original` -- adds the **original version as submitted**
    - `project-n-refactor` -- adds the **improved, modernized version**
