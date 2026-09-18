# Contributing to KineWorld

KineWorld is a research-stage project. This file applies to every repository in the
[`kineworld`](https://github.com/kineworld) organization unless a repository ships its own
`CONTRIBUTING.md`.

短版：**先给证据，再给结论。** 不接受没有可复现依据的性能主张。

## What we welcome

| Contribution | Where it goes | What it must include |
| --- | --- | --- |
| Bug report | Issue template *Bug report* | Exact command, environment, observed vs expected output |
| Reproduction attempt (success **or** failure) | Issue template *Reproduction report* | Commit SHA, hardware, wall-clock, logs, raw numbers |
| Challenge to a published claim | Issue template *Evidence challenge* | Which claim, which artifact, what contradicts it |
| Documentation fix | Pull request | No claim changes |
| Code change | Pull request | See *Pull requests* below |

Negative results are first-class here. A careful failed reproduction is more useful to us
than a vague success report.

## Evidence rules

These apply to issues and pull requests equally.

1. **No claim without an artifact.** Every performance or capability statement must point at a
   file in the repository (`results/*.json`, a manifest, a log) that a third party can re-run.
2. **State the evidence level.** We use `E1` for a single seed / single checkpoint / single task
   run. Do not present an `E1` result as a general capability.
3. **Distinguish correlation from causation.** Observational readings are reported as
   observational. If an intervention was not performed, say so.
4. **Report uncertainty honestly.** If a result has no variance estimate, write
   `capability gap` rather than inventing an interval or a heuristic "confidence" number.
5. **Register negative results.** A falsified hypothesis gets recorded, not quietly dropped.
6. **No fabricated entities.** Do not introduce partners, customers, revenue, funding rounds,
   external replications, or expert endorsements that do not exist.

## Pull requests

- Branch from the repository's default branch. Keep the change set focused; one concern per PR.
- Do not commit secrets, credentials, model weights, datasets, or third-party user material.
  If a change needs weights or gated data, describe how to obtain them in the PR body.
- If you change a published number or claim, update the artifact that carries it (report,
  manifest, ledger row) in the same PR. A number that exists in two places is a defect.
- If you add a self-check or test, make sure it can fail. Before submitting, ask: *what defect
  would turn this red?* If you cannot answer, the check is decorative — remove it.
- Run whatever the repository provides (`unittest discover`, `check_*` scripts, CI) before
  requesting review, and paste the result.

## Forks and third-party code

Repositories that are forks of upstream projects remain governed by their upstream
contribution process and licence. Send fixes for upstream code upstream. KineWorld-specific
adaptations belong on a separate branch and must be described as adaptations, not as upstream
capability.

See [`ATTRIBUTION.md`](ATTRIBUTION.md) for the full fork list and licence status.

## Licensing of contributions

This organization has no CLA and no DCO requirement. By opening a pull request you agree that
your contribution is licensed under the licence of the repository you are contributing to.
For documentation in this `.github` repository, that is the licence stated in
[`README.md`](README.md).

## Response expectations

There is currently **one maintainer**, working on this part-time alongside research. Expect
replies in days, not hours, and expect us to ask for the raw artifact before discussing
conclusions. There is no support SLA — see [`SUPPORT.md`](SUPPORT.md).
