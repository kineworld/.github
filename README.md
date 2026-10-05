# 勘境 · KineWorld

**让机器理解行动如何改变世界。**  
**World models for perception, planning and control.**

勘境围绕动作条件世界模型、预测表征、空间智能与规划控制开展研发。我们公开精选成果和有明确评测条件的对比数据；核心实现、模型权重、训练配方与内部研发记录采用私有管理。

## 研究进展

### PushT：同一预测器下的规划成功率提升

在 50 个配对保留场景中，姿态目标规划成功 **33/50（66%）**，覆盖率目标对照成功 **11/50（22%）**，提升 **44 个百分点**。两者使用同一预测器、传感器与每次决策预算。

这是指定模拟任务内的规划目标对照。完整评测条件、统计与逐场景结果见 **[成果说明](https://github.com/kineworld/.github/blob/main/results/pusht-2026-10.md)**；结果不外推为跨模型排行榜或真实机器人能力。

### 研发方向

- **预测表征与动作条件动力学**：围绕未来状态表征和动作影响开展模型研究。
- **规划与控制**：连接预测、候选行动和闭环反馈。
- **空间智能**：探索视觉、几何与可交互环境的结合。

## 了解勘境

**[官网 · kineworld.com](https://kineworld.com)** · **[研究成果](https://github.com/kineworld/.github/blob/main/results/pusht-2026-10.md)**

核心研发闭源。组织内保留的开源 fork 属于各自上游作者；来源与许可证继续保留，不作为勘境自研模型或性能的证明。

---

KineWorld develops action-conditioned world models, predictive representations and systems for spatial reasoning, planning and control. Selected results are public; implementation and internal research remain private.
