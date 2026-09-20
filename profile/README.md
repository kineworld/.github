# KineWorld

**Action-conditioned world models for physical intelligence.**

KineWorld is a research-stage company in Hefei, China. We study compact, non-LLM world models that learn predictive state representations for planning and control. Every capability claim is tied to inspectable experiments, artifacts, and explicit limitations.

KineWorld is currently a **single-maintainer, part-time organization**. No partners, customers, revenue, or external replications are claimed anywhere in these repositories.

- Website: [kineworld.com](https://kineworld.com)
- Model research: [kine-jepa](https://github.com/kineworld/kine-jepa)
- Evaluation and evidence: [kine-bench](https://github.com/kineworld/kine-bench)
- Data pipeline: [kine-datapipe](https://github.com/kineworld/kine-datapipe)

Current evidence is internal and research-stage. We are actively seeking independent reproduction and technical collaboration.

## What is in this organization

Two kinds of repositories live here, and they should not be confused.

**First-party work** — [`kine-jepa`](https://github.com/kineworld/kine-jepa) · [`kine-bench`](https://github.com/kineworld/kine-bench) · [`kine-datapipe`](https://github.com/kineworld/kine-datapipe) · [`kineworld-site`](https://github.com/kineworld/kineworld-site) · [`spatial-0`](https://github.com/kineworld/spatial-0)

**Forks of upstream open-source projects** — repositories kept here for study and adaptation. These retain their upstream authors, history, and licences. Being hosted here is **not** a claim of authorship, and does not mean the code is running in our pipeline, has been reproduced, or is endorsed by its authors.

← The full list, with upstream source, licence, intended use, and verification status, is in **[ATTRIBUTION.md](https://github.com/kineworld/.github/blob/main/ATTRIBUTION.md)**.

## Working with this organization

| Document | Use it for |
| --- | --- |
| [CONTRIBUTING.md](https://github.com/kineworld/.github/blob/main/CONTRIBUTING.md) | Evidence rules, pull request requirements, what we accept |
| [SECURITY.md](https://github.com/kineworld/.github/blob/main/SECURITY.md) | Private vulnerability reporting, and what counts as in scope |
| [SUPPORT.md](https://github.com/kineworld/.github/blob/main/SUPPORT.md) | What we can and cannot help with — including an explicit list of what we do not do |
| [GOVERNANCE.md](https://github.com/kineworld/.github/blob/main/GOVERNANCE.md) | Who decides what, and the evidence gate that cannot be overridden |
| [ATTRIBUTION.md](https://github.com/kineworld/.github/blob/main/ATTRIBUTION.md) | Fork provenance, licensing, and how to report an attribution problem |
| [CODE_OF_CONDUCT.md](https://github.com/kineworld/.github/blob/main/CODE_OF_CONDUCT.md) | Contributor Covenant 2.1 |

**Reproduction attempts are the most useful thing you can send us** — including failed ones. Use the *Reproduction report* or *Evidence challenge* issue template. A challenge that holds up results in a visible, in-place correction rather than a quiet edit.

## 世界模型开放学习指南 · World Model Learning Guide

从零基础直觉到数学、JEPA、动力学、3D、多模态、因果、评测与独立研究。包含11章中文教程、术语表、练习答案和两个无需显卡的CPU实验。

**[开始学习 →](https://github.com/kineworld/.github/blob/main/world-models/README.md)**

An evidence-first Chinese learning path with a CPU-only experiment. Educational material, not a claim of model leadership or a guarantee of expertise.

## 感谢开源贡献 · Thank you to the open-source community

勘境感谢世界模型、视觉、几何与评测项目的原作者和贡献者。你们公开研究成果、代码与复现方法的开源精神，让我们能够站在已有成果之上继续探索。我们保留来源、署名、许可证和引用，以提交与实验记录说明勘境的新增工作。

**[世界模型项目、勘境改动与验证状态](https://github.com/kineworld/.github/blob/main/world-models/open-source-adoption.md)** · **[KineJing 训练与集成](https://github.com/kineworld/KineJing)**

Current changes cover CausalWM decoding, V-JEPA checkpoint loading, Wan input validation, Dreamer environment options, JEPA-WMs local predictor weights, OpenDW statistics, and Cosmos evaluation. Engineering tests do not establish model-quality or leaderboard gains. Thank you to all upstream authors for making this work possible.
