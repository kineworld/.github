# 勘境 · KineWorld

**让机器理解行动如何改变世界。**  
**World models for perception, planning and control.**

勘境围绕动作条件世界模型、预测表征、空间智能与规划控制开展研发。我们公开精选成果和有明确评测条件的对比数据；核心实现、模型权重、训练配方与内部研发记录采用私有管理。

## 研究进展

**[查看全部已核验对比成果](https://github.com/kineworld/.github/blob/main/results/README.md)**

| 成果 | 具体对比 | 条件 |
| --- | --- | --- |
| PushT 规划 | **66% vs 22% 成功率，+44 个百分点** | 50 对场景，同预测器与每次决策预算 |
| 固定动作集合的 JEPA 对照 | **位置误差降低 96.44%，归一化遗憾降低 92.42%** | 对本地 JEPA-WM 任务读出头三种子均值；开发集，额外物理先验 |
| Physion++ 接触任务适配 | **AUROC 0.67706 vs 0.56716，准确率 +9.00 个百分点** | 同一 V-JEPA-2 表征上的读出比较；额外训练监督，已发布测试集复评 |
| KineJing 特征预测 | **特征 MSE 降低 15.75%** | 对首帧保持，本地 10 回合评估 |
| CNN 视觉前端 | **一步位置预测误差降低 22.48%** | 对颜色特征前端，50 场景，相同动力学 |

具体方法、样本数、统计范围和更多位置预测/几何结构对照见成果汇总；不将特定指标优势表述为全面领先。

### PushT：同一预测器下的规划成功率提升

在 50 个配对保留场景中，姿态目标规划成功 **33/50（66%）**，覆盖率目标对照成功 **11/50（22%）**，提升 **44 个百分点**。两者使用同一预测器、传感器与每次决策预算。

这是指定模拟任务内的规划目标对照。完整评测条件、统计与逐场景结果见 **[成果说明](https://github.com/kineworld/.github/blob/main/results/pusht-2026-10.md)**；结果不外推为跨模型排行榜或真实机器人能力。

### 研发方向

- **预测表征与动作条件动力学**：围绕未来状态表征和动作影响开展模型研究。
- **规划与控制**：连接预测、候选行动和闭环反馈。
- **空间智能**：探索视觉、几何与可交互环境的结合。

## 了解勘境

**[官网 · kineworld.com](https://kineworld.com)** · **[全部研究成果](https://github.com/kineworld/.github/blob/main/results/README.md)**

核心研发闭源。组织内保留的开源 fork 属于各自上游作者；来源与许可证继续保留，不作为勘境自研模型或性能的证明。

---

KineWorld develops action-conditioned world models, predictive representations and systems for spatial reasoning, planning and control. Selected results are public; implementation and internal research remain private.
