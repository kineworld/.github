# Security Policy

## Reporting a vulnerability

**Please do not open a public issue for a security problem.**

Use GitHub's private reporting channel instead:

1. Go to the **Security** tab of the affected repository.
2. Choose **Report a vulnerability** (private vulnerability reporting).

If that option is not available on the repository, open a normal issue that says only
*"I need a private security contact for this repository"* — with no technical detail — and a
private channel will be arranged.

## Scope

| Asset | In scope | Notes |
| --- | --- | --- |
| First-party repositories — `kine-jepa`, `kine-bench`, `kine-datapipe`, `kineworld-site`, `spatial-0` | Yes | Includes code, CI workflows, and downloadable artifacts |
| `.github` repository (profile, learning guide, labs) | Yes | Includes the GitHub Actions workflows |
| Forks of upstream projects (see [`ATTRIBUTION.md`](ATTRIBUTION.md)) | No | Report to the upstream project. We do not maintain their code |
| `kineworld.com` web presence | Yes | Infrastructure and configuration issues |
| Model weights, datasets, or services we do not host | No | Report to the party that distributes them |

## What we care about most

- **Supply-chain integrity.** We pin third-party GitHub Actions to full commit SHAs. A
  workflow that references a mutable tag is treated as a defect — please report it.
- **Leaked credentials.** Committed tokens, keys, or private endpoints.
- **Evidence integrity.** Any way to make a published artifact, manifest, or self-check report
  a passing result when the underlying run did not actually pass. We consider this equal in
  severity to a code execution bug: the project's only product is trustworthy evidence.
- **Data exposure.** Anything that leaks third-party video, personal data, or unpublished
  material through a repository or an artifact.

## Out of scope

- Missing security headers, best-practice nits, and automated-scanner output with no
  demonstrated impact.
- The absence of a support SLA, or the fact that research code has rough edges.
- Vulnerabilities in upstream projects that we merely forked — send those upstream.
- Reports generated purely by a tool, with no reproduction path and no impact statement.

## Our commitments

- We will acknowledge a valid report and tell you whether it is in scope.
- We will not pursue legal action against good-faith research that respects this policy.
- We will credit you if you want credit, and stay quiet if you prefer.
- We will not claim a fix is shipped until it is actually on the default branch.

## Disclosure

Please give us a reasonable window to fix an issue before publishing details. If a report
turns out to be a false alarm, we will say so publicly rather than quietly closing it.

## No bug bounty

This is a research-stage project with no funding. There is no monetary reward for reports.
