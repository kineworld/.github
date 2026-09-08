# 09 · 一手资料与开源地图

[目录](README.md) · 上一章：[论文工作流](08-paper-workflow.md) · 下一章：[研究路线](10-research-roadmap.md)

这是**按问题选出的阅读入口**，不是“所有最强项目排名”。以下主来源于2026-09-08核对；教程整理于2026-09-09。仓库主分支、权重和许可证可能变化，执行时必须再固定版本。链接可访问不代表我们复现了它，更不代表游戏本能训练它。

## 基础与方法

| 来源 | 为什么读 | 阅读出口 |
| --- | --- | --- |
| [Python官方教程](https://docs.python.org/3/tutorial/) | 学会运行、修改和记录实验 | 能解释函数、循环、路径和异常 |
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 张量、数据、自动微分与模型保存 | 能训练并重新加载一个小网络 |
| [Dive into Deep Learning](https://d2l.ai/) | 查缺补漏，而不是从头背完 | 能解释当前实验所需的数学 |
| [Elements of Causal Inference](https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/) | 区分观察、干预及可识别性 | 说清因果结论依赖什么假设 |

## 动力学、表征与控制

| 项目 | 关注点 | 不应作出的推断 |
| --- | --- | --- |
| [World Models](https://worldmodels.github.io/) | 压缩观察、时序模型、控制组合的经典入口 | 经典实验结果适用于所有现实任务 |
| [DreamerV3](https://github.com/danijar/dreamerv3) | 在学习模型的想象中学习行为 | 想象训练完全不需要环境数据 |
| [TD-MPC2](https://github.com/nicklashansen/tdmpc2) | 潜在模型与连续控制规划 | 控制任务表现等于视觉生成表现 |
| [I-JEPA](https://github.com/facebookresearch/ijepa) | 图像中的联合嵌入预测 | 图像预训练已解决动作规划 |
| [V-JEPA 2 / 2-AC / 2.1](https://github.com/facebookresearch/vjepa2) | 视频表征、动作条件后训练等不同配置 | 任意编码器权重都能直接控制机器人 |
| [MuJoCo](https://github.com/google-deepmind/mujoco) | 可控物理环境与实验平台 | 使用物理模拟器就等于学出了世界模型 |

V-JEPA仓库核对时已包含2.1，不要只按旧教程找2的文件。以上为学习入口，并非声称V3、2或2.1永远是各自系列最新版本。新版本先读作者发布记录再加入实验。

## 空间与视频

| 项目或原始介绍 | 用来学什么 | 先检查 |
| --- | --- | --- |
| [VGGT](https://github.com/facebookresearch/vggt) | 图像到相机与几何属性 | 权重版本、尺度、显存、许可证 |
| [3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) | 空间表示与新视角渲染 | 相机数据、重建覆盖、代码使用条件 |
| [Cosmos-Predict2](https://github.com/nvidia-cosmos/cosmos-predict2) | 视频世界模型工程入口 | 模型/任务版本、硬件及数据许可 |
| [Genie 3官方介绍](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) | 分析交互世界能力声明 | 哪些是演示、哪些有公开评测与可复现实现 |
| [World Labs世界模型分类](https://www.worldlabs.ai/blog/taxonomy-of-world-models) | 比较不同功能定义 | 分类不等于能力或排名认证 |

最后两项是官方阅读材料，不在这里被当作开源项目。不要根据宣传视频推测未公开训练细节，也不要默认商业API产出可以用于蒸馏竞争模型。

## 评测入口

- [Physion](https://physion-benchmark.github.io/)：视觉物理预测。
- [Physion++](https://dingmyu.github.io/physion_v2/)：涉及隐藏物理属性推断的场景预测。
- [Physics-IQ官方仓库](https://github.com/google-deepmind/physics-iq-benchmark)：生成视频物理评测；协议和版本以该仓库及对应论文为准。

先完成[评测章节](07-evaluation.md)。如果你的模型只输出潜在向量，不能直接拿它与要求生成视频的系统在同一接口下比较；需要合法、明确的任务适配，并把新增模块与计算预算计入。

## 下载前的六项核验

```text
官方仓库与提交SHA：
代码许可证 / 权重许可证 / 数据许可证：
允许的用途、再分发与商用限制：
权重体积 / 预计下载量 / 官方硬件条件：
目标模式：推理、微调还是从零训练：
本机验证结果与停止条件：
```

“GitHub能看到代码”不等于所有资产均为宽松开源；下载模型不等于获得任意用途授权。不要复制许可证标题后就忽略附加条款。本表不提供法律意见，也不对商用资格作统一判断。

## 小显存设备怎么用这些资料？

先读结构，运行CPU实验，再挑能验证的最小配置。预先设定分辨率、帧数、批次与峰值显存测量；超出预算就停止。冻结编码器、缓存特征、减小实验规模可能降低成本，但必须记录它们改变了什么，不能拿缩小版结果冒充完整复现。

## 如何持续更新

新论文先写[论文卡](08-paper-workflow.md)，然后记录它替代了哪一项能力、可复现性怎样、许可证是否合适。没有明确问题，不因“新发布”就下载或迁移。贡献时标明核对日期；移除失效链接时保留原始出处信息，避免把项目更名误认为全新技术。
