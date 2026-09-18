# Governance

This document describes how decisions are actually made in the `kineworld` organization. It is
deliberately short, because the organization is deliberately small.

## Current structure

**KineWorld is a single-maintainer, research-stage organization.** There is one owner. There are
no other maintainers, no reviewers, no committee, and no separate research or engineering team.

This is stated plainly because repositories elsewhere often imply a team by using plural pronouns.
If a document here says "we", it refers to one person plus whoever is contributing in that thread.

## Decision rights

| Decision | Made by | Constraint |
| --- | --- | --- |
| Merging a pull request | The owner | Change must not weaken evidence rules (see below) |
| Publishing a new result | The owner | Requires a committed artifact + manifest |
| Changing a published claim | The owner | Requires a visible correction note, never a silent edit |
| Archiving or renaming a repository | The owner | — |
| Forking an upstream project | The owner | Must be recorded in [`ATTRIBUTION.md`](ATTRIBUTION.md) with its licence |
| Adding a maintainer | The owner | Not currently planned |

There is no voting process and no appeal body. If that becomes necessary, this file will say so.

## Evidence gate

The following rules are project-level and are **not** overridable by convenience, deadlines,
or how good a result looks:

1. A claim without a committed artifact is not a result.
2. Observational readings are labelled observational; causal language requires an intervention.
3. Single-seed / single-checkpoint / single-task results are labelled `E1` and are not presented
   as general capability.
4. Where variance is not measured, the honest entry is `capability gap`, not an invented interval.
5. Negative and falsified results are registered, not deleted.
6. Corrections are applied in place with a visible note. Silent rewrites of published numbers are
   treated as a defect.
7. Numbers that appear in prose must be machine-checked against the artifact, not transcribed by
   hand.

A pull request that violates the gate is rejected regardless of who opened it.

## Fork policy

Upstream code may be forked for study and adaptation. Forking does **not**:

- transfer authorship, licence, or credit,
- imply cooperation, endorsement, or partnership with the upstream authors,
- mean the code is running here, or has been verified here.

Every fork keeps its upstream history, `LICENSE`, and `NOTICE` files. KineWorld-specific changes
go on a separate branch and are described as adaptations. Repositories that have been forked and
not otherwise touched must not appear in any list of implemented capabilities.

## Claims about the organization itself

The organization does not publish, and will not publish, any of the following unless it is
literally true:

- named partners, customers, or users,
- revenue, funding, or valuation,
- external replications or third-party verification,
- expert or institutional endorsements,
- benchmark leadership or ranking positions,
- a headcount or team that does not exist.

Where a status is unknown or unverified, the published word is "unverified", not "in progress".

## Changing this document

Open a pull request or an issue. Because there is one decision-maker, expect a direct answer
rather than a discussion process.
