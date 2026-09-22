# Guards

Two files a repository copies into its test directory, plus three lines of YAML. That is
the whole adoption. Nothing here is executed from this repository; it is a source of
copies, kept in one place so the copies cannot drift apart in intent.

## The pair

| file | goes to | what it does |
| --- | --- | --- |
| `check_collection.py` | `<test-dir>/check_collection.py` | Fails if the standard runner cannot see every test in that directory. Derives the expected count from the source with `ast`, so there is no number to keep up to date. |
| `load_tests.py` | `<test-dir>/__init__.py` | Implements the documented `load_tests` protocol, so `test_*` functions written at module level are collected instead of passed over. Only needed by a directory that has any. |

Copy `load_tests.py` **as** `__init__.py`. With one caveat: a directory that is a package
must be discovered with an explicit top-level dir (`-t .`), or `discover` never imports it
and `load_tests` is never reached. `check_collection.py` and
`.github/workflows/python-tests.yml` branch on the same rule, so the guard, a local run and
CI cannot disagree about what "collected" means.

`check_collection.py` is required by the workflow. `load_tests.py` is not required by
anything -- a directory whose tests are all inside `TestCase` classes does not need it. It
is here because the repositories that do need it should not each invent their own.

### The boundary, stated rather than left implicit

Both files count only `test_*.py`, which is the same set `unittest discover` loads. A
`test_*` function in a file called `checks.py` is therefore invisible to the guard *and*
never run by CI. That is a real blind spot, and it is deliberate only in the sense that the
guard's scope equals the runner's scope -- which is the property that lets the two numbers
be compared at all. Widening one without the other would make them disagree. Widening both
means changing the discovery pattern in the workflow as well.

## Adoption

```yaml
# .github/workflows/tests.yml
jobs:
  tests:
    uses: kineworld/.github/.github/workflows/python-tests.yml@main
    with:
      install: "-r requirements.txt"
```

Then copy the file or files above that apply. The workflow **fails** when
`check_collection.py` is absent, deliberately: a job that runs a suite without proving the
suite ran is the exact failure mode all of this exists to prevent, so partial adoption must
not be possible.

## Why the count is derived instead of stored

A stored number is a number someone has to update, and the moment they forget, the check
stops checking while still reporting success. That failure -- a check narrowing what it
looks at and still reporting success -- has appeared five times in this work, including
three times inside the checks themselves. The audit that started it is in
kineworld/.github#3.
