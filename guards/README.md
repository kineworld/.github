# Guards

Two files a repository copies into its test directory, plus three lines of YAML. That is
the whole adoption. Nothing here is imported from this repository; it is a source of
copies, kept in one place so the copies cannot drift apart in intent -- and, since
`.github/workflows/python-tests.yml` now compares every caller's copies against these, so
that they cannot drift apart at all without the caller's own CI saying so. See *Keeping the
copies honest* below.

This repository is also a caller now. `world-models/labs/` holds a copy of
`check_collection.py`, and `guide-checks.yml` runs it after the suite. It was the last
repository in the organisation without one, which is the wrong way round for the repository
that publishes them -- see kineworld/.github#10.

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
not be possible. It also fails when a copy has fallen behind these files -- see below.

## Keeping the copies honest

A copy is a thing that can fall behind, and these did. Within a day of this pair being
published, four of the six copies in use were behind the originals, on both files. So
`.github/workflows/python-tests.yml` fetches these two files at `main` and compares the
copies in the caller's test directory against them, before installing anything. A drifted
copy fails the caller's own build, with a diff and the one-line command that fixes it.

What the drift cost, measured on a directory holding one good module and one unimportable
module:

| shim | result |
| --- | --- |
| the older copy | `Ran 1 test` -- the good test never runs |
| this file | `Ran 2 tests` -- `tests.Test_test_broken_import` ERROR, `tests.Test_test_good_test_alpha` ok |

Both versions passed the collection guard on a real repository, because the count still came
out right. What degraded was only what a failure could tell you: with the older shim, one
module that cannot be imported keeps every other test in the directory out of the suite
output, and the guard's count says "N invisible" without saying which module. So this was
degraded rather than silent -- but degraded is what a copy does, and there is no reason to
accept it when a `cmp` detects it.

Carriage returns are stripped on both sides before comparing. A contributor on Windows runs
with `core.autocrlf`, which rewrites their checkout; that is a property of their machine
rather than drift in the file, and reporting it as drift would send them to the wrong fix.

`load_tests.py` is compared only when the caller has a non-empty `__init__.py`. Absent and
empty are both legitimate -- absent means the directory holds no module-level `test_*`
functions, empty means the directory is a package and nothing more. Anything else has to be
this file, because a hand-rolled `load_tests` is where "collects fewer tests than the source
defines" lives.

### The copy inside this repository

The copy in `world-models/labs/` is compared against `guards/check_collection.py` by
`guide-checks.yml`, with the same `tr -d '\r'` on both sides. It does not fetch from
`raw.githubusercontent.com` the way the reusable workflow does, because here the canonical
file is already in the checkout -- which is the one advantage of being the repository the
copies come from, and worth taking: a comparison that needs no network cannot fail for
network reasons and be misread as drift, or worse, be skipped.

So there are two places a copy of this file can be compared, and the one that runs depends
on where the copy is. A caller elsewhere gets the fetch-and-compare in
`python-tests.yml`, before its dependencies are installed. This repository gets the `cmp`
in `guide-checks.yml`, first among that job's steps. Neither is a substitute for the other,
and a change to `guards/check_collection.py` has to keep both satisfied -- which is exactly
what happens, since they compare the same pair of files.

## Why the count is derived instead of stored

A stored number is a number someone has to update, and the moment they forget, the check
stops checking while still reporting success. That failure -- a check narrowing what it
looks at and still reporting success -- has appeared five times in this work, including
three times inside the checks themselves. The audit that started it is in
kineworld/.github#3.
