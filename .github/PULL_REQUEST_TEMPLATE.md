<!--
PR title: use a Conventional-Commits-style prefix, e.g. "docs: ...", "fix: ...", "feat: ...".
Keep one concern per pull request.
-->

## What this changes

<!-- One or two sentences. What is different after this PR? -->

## Why

<!-- The reason this is correct. Link the issue, claim, or artifact this follows from. -->

## Which repository and branch

<!-- e.g. kineworld/kine-jepa, branch feat/xyz -->

## Evidence gate

The rules in [GOVERNANCE.md](https://github.com/kineworld/.github/blob/main/GOVERNANCE.md) are
not overridable. Tick what applies:

- [ ] This PR makes **no** claim about capability, performance, or accuracy — it is documentation, tooling, or refactoring.
- [ ] This PR **does** make or change a claim, and I have committed the artifact that supports it.
- [ ] Any claim added is labelled with its evidence level (`E1` = single seed / checkpoint / task).
- [ ] Observational readings are described as observational; causal language is used only where an intervention was performed.
- [ ] Where variance is not measured, the text says `capability gap` rather than stating an interval.
- [ ] Any number changed in prose was re-checked against the artifact, not transcribed by hand.
- [ ] Negative or falsified results produced by this change are registered, not omitted.

## Checks

- [ ] Every number in prose matches the artifact it cites.
- [ ] No number, statistic, or claim now exists in two places with different values.
- [ ] New or changed self-checks can actually fail — I can name the defect that would turn each one red.
- [ ] No secrets, credentials, private endpoints, model weights, gated datasets, or third-party user material are included.
- [ ] Third-party Actions are pinned to a full commit SHA (not a tag or branch).
- [ ] Attribution is intact: upstream `LICENSE` / `NOTICE` / author credits are unchanged.
- [ ] Nothing here introduces a partner, customer, revenue figure, funding round, external replication, or endorsement that does not exist.

## How this was verified

<!--
Paste the actual commands and their results. "I ran the test suite" is not verification.
e.g.
$ python -m unittest discover -s world-models/labs -p 'test_*.py' -v
Ran 12 tests ... OK
-->

```text

```

## Not verified / known gaps

<!--
Say what you did not check, and what a reviewer should be suspicious of.
Leaving this empty is taken to mean "everything relevant was checked".
-->
