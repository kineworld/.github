"""Fail if the standard runner cannot see every test in ``tests/``.

**This is the organisation-level copy.** Copy it into a repository as
``tests/check_collection.py`` and call it from CI -- that is exactly what
``.github/workflows/python-tests.yml`` in this repository expects to find, and it
refuses to run a suite without it.

Why it exists: four self-authored repositories in this organisation hold test
functions that no job will ever execute, in three different shapes (no workflow at
all; a workflow that runs one named module instead of discovering; a suite whose tests
the loader cannot see). The audit is in kineworld/.github#3.

Why it derives the expected count with :mod:`ast` instead of storing a number: a
hand-maintained count drifts out of date and then silently stops checking, which is the
same class of mistake as the defect this guards against.

    python tests/check_collection.py
"""

import ast
import pathlib
import sys
import unittest

TESTS_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = TESTS_DIR.parent


def count_tests_in(path):
    """Return the number of test functions a file appears to define."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    count = 0
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith("test_"):
                count += 1
        elif isinstance(node, ast.ClassDef):
            for inner in node.body:
                if isinstance(inner, ast.FunctionDef) and inner.name.startswith("test_"):
                    count += 1
    return count


def discover():
    """Collect the suite the same way CI does, for this layout.

    A package directory (one with ``__init__.py``) must be discovered with an explicit
    top-level directory; without one, ``discover`` treats it as a set of top-level
    modules, never imports it as a package, and a package-level ``load_tests`` would not
    run. A plain directory must be discovered WITHOUT a top-level directory, because
    ``discover`` raises ``ImportError`` when the start directory is not importable.

    Repositories that already keep every test inside a ``TestCase`` have no
    ``__init__.py`` and are fine either way; this picks the form their CI would use.
    """
    if (TESTS_DIR / "__init__.py").exists():
        return unittest.TestLoader().discover(str(TESTS_DIR), top_level_dir=str(REPO_ROOT))
    return unittest.TestLoader().discover(str(TESTS_DIR))


def main():
    files = sorted(TESTS_DIR.glob("test_*.py"))
    if not files:
        raise SystemExit("no tests/test_*.py files found")

    expected = sum(count_tests_in(f) for f in files)

    sys.path.insert(0, str(REPO_ROOT))
    collected = discover().countTestCases()

    print("%d test files | %d test functions in source | %d collected by unittest"
          % (len(files), expected, collected))

    if collected != expected:
        missing = expected - collected
        raise SystemExit(
            "the runner collected %d tests but the source defines %d (%d invisible). "
            "A test that does not run cannot fail. If the invisible tests are written as "
            "module-level functions, see kineworld/kine-jepa#4 for the load_tests fix."
            % (collected, expected, missing)
        )

    print("ok: every test in tests/ is visible to the runner")


if __name__ == "__main__":
    main()
