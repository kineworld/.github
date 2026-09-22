# Attribution and provenance

This organization hosts two kinds of repositories, and they must not be confused:

1. **First-party work** produced by KineWorld.
2. **Forks of upstream open-source projects**, copied here for study and adaptation.

A repository appearing under `github.com/kineworld` is **not** a claim of authorship. For forks,
all authorship, copyright, and licence terms belong to the upstream project.

## First-party repositories

| Repository | What it is | Status |
| --- | --- | --- |
| [`KineJing`](https://github.com/kineworld/KineJing) | Model integration, CPU baseline and trained small latent dynamics | See model card and evidence |
| [`kine-jepa`](https://github.com/kineworld/kine-jepa) | Compact, action-conditioned latent world models | Research stage |
| [`kine-bench`](https://github.com/kineworld/kine-bench) | Evaluation and evidence gating for world-model planning claims | Research stage |
| [`kine-datapipe`](https://github.com/kineworld/kine-datapipe) | Turning video and simulation into world-model training data | Research stage |
| [`kineworld-site`](https://github.com/kineworld/kineworld-site) | Public web presence for kineworld.com | In progress |
| `spatial-0` *(private — not linked)* | Evidence-bound spatial reconstruction | Paused checkpoint |
| `kineworld-knowledge` *(private — not linked)* | Shared knowledge base, task records, and AI work coordination | Maintained |
| [`.github`](https://github.com/kineworld/.github) | Organization profile, community files, and the world-model learning guide | Maintained |

Capability claims for first-party work are limited to what is backed by committed artifacts in
the relevant repository. Current evidence is internal and research-stage.

## Forked upstream projects

**Canonical table:** [world-models/open-source-adoption.md](world-models/open-source-adoption.md)

That document is the single source of truth for the fork list. It records, for each project, the
upstream repository, the code licence, the intended use, and the verification status. It is kept
there rather than duplicated here so that the two cannot drift apart.

Forks are real GitHub forks: they retain upstream history, authors, commits, and licence files.

### What a fork here does and does not mean

| It does mean | It does not mean |
| --- | --- |
| We read this project and considered it relevant | We wrote it |
| The code is available to us to study and adapt | It is running in our pipeline |
| The licence permits the copy we made | The licence permits every bundled weight, dataset, or sample |
| We may select it as a baseline later | We have reproduced, beaten, or validated it |

### Licence caveat

A repository's `LICENSE` file covers the repository's **code**. It does not automatically cover
its dependencies, model weights, training data, or example media, each of which may carry separate
terms. Where the licence of a bundled asset is unclear, treat it as **not** usable for commercial
purposes until verified at the original source.

Two concrete cases in this organization:

- `CODE_OF_CONDUCT.md` is adapted from Contributor Covenant 2.1. Its authors release that text
  under CC BY 4.0 and require attribution, which the file carries; the MIT licence at the root of
  this repository does not relicense it.
- `spatial-0` ships no blanket `LICENSE`, deliberately: its components carry different terms,
  including non-commercial ones, and `docs/LICENSE_AUDIT.md` classifies them one by one. A single
  file at the root would assert more than is true.

## Reporting an attribution problem

If a repository here misattributes your work, omits a required notice, or uses material it should
not, open an issue in this repository and it will be corrected or removed. Attribution problems
are treated as defects, not as a difference of opinion.

## Claims we are not making

- No fork here has produced a benchmark result, a ranking, or a product capability.
- No fork here implies cooperation with, or endorsement by, its upstream authors.
- Nothing in this organization should be read as a claim over third-party intellectual property.
