# KineWorld 开源复用入口

更新：2026-09-20。这里区分上游开源项目、KineWorld 的工程适配和闭源服务。Fork 不代表原创、合作背书或已经运行成功。

## 致谢：感谢开源精神

勘境感谢 Aether AI、Meta FAIR 与 JEPA-WMs 作者、Alibaba Wan 团队、NVIDIA Cosmos 团队、Dexmal / OpenDW 作者、Danijar Hafner，以及 MIRA、Microsoft TRELLIS、World Labs Spark 和下列几何、数据、评测项目的所有贡献者。

感谢你们愿意公开研究成果、代码与复现方法，让更多研究者和小团队能够学习、验证并继续探索。勘境的工作建立在这些贡献之上：原始贡献归属原作者，保留提交历史、许可证和引用；新增工作以可检查的改动、测试和实验记录说明。

We thank the original authors and the open-source community for sharing their research and tools. We preserve attribution and licenses, document our changes, and report their validation limits.

## 组织内的上游代码与改进状态

| 项目 | KineWorld Fork | 原始项目 | 代码许可证 | 用途与当前状态 |
| --- | --- | --- | --- | --- |
| CausalWM | [kineworld/KineJing-CausalWM](https://github.com/kineworld/KineJing-CausalWM) | [AetherLabsAI/CausalWM](https://github.com/AetherLabsAI/CausalWM) | LTX-2 Community License | 新增可选分块 VAE 解码与 CPU 累积；[验证边界](https://github.com/kineworld/KineJing-CausalWM/blob/main/KINEJING.md)；完整权重未运行 |
| Cosmos 3 | [kineworld/cosmos](https://github.com/kineworld/cosmos) | [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | OpenMDW-1.1 | 修复运动平滑度评测接受非有限分数的问题；[改动与测试](https://github.com/kineworld/cosmos/blob/main/KINEWORLD.md)；未复现模型分数 |
| JEPA-WMs | [kineworld/jepa-wms](https://github.com/kineworld/jepa-wms) | [facebookresearch/jepa-wms](https://github.com/facebookresearch/jepa-wms) | CC-BY-NC-4.0；组件另有许可 | 非商用研究路径；新增本地预测器权重入口与未知参数报错；[改动与测试](https://github.com/kineworld/jepa-wms/blob/main/KINEWORLD.md) |
| OpenDW / DW05 | [kineworld/OpenDW](https://github.com/kineworld/OpenDW) | [dexmal/opendw](https://github.com/dexmal/opendw) | Apache-2.0 | 动作归一化改用 float64 与稳定方差合并，拒绝无效输入；[改动与测试](https://github.com/kineworld/OpenDW/blob/main/KINEWORLD.md)；未重训模型 |
| MIRA | [kineworld/mira](https://github.com/kineworld/mira) | [mira-wm/mira](https://github.com/mira-wm/mira) | Apache-2.0 | 动作条件、多玩家世界模型研究；仅完成 Fork，尚未本地复现 |
| Spark | [kineworld/spark](https://github.com/kineworld/spark) | [sparkjsdev/spark](https://github.com/sparkjsdev/spark) | MIT | THREE.js 的3D高斯渲染器；仅完成 Fork，不代表已接入产品 |
| V-JEPA 2 | [kineworld/vjepa2](https://github.com/kineworld/vjepa2) | [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2) | 主要 MIT，部分 Apache-2.0 | 修复 localhost 权重地址，增加显式本地权重加载；[改动与测试](https://github.com/kineworld/vjepa2/blob/main/KINEWORLD.md)；未运行完整模型 |
| DreamerV3 | [kineworld/dreamerv3](https://github.com/kineworld/dreamerv3) | [danijar/dreamerv3](https://github.com/danijar/dreamerv3) | MIT | 隔离环境构造的可变配置，保留重复构造时的种子设置；[改动与测试](https://github.com/kineworld/dreamerv3/blob/main/KINEWORLD.md)；未复现完整策略训练 |
| Wan2.2 | [kineworld/Wan2.2](https://github.com/kineworld/Wan2.2) | [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | Apache-2.0 | 增加模型加载前的帧数约束检查；[改动与测试](https://github.com/kineworld/Wan2.2/blob/main/KINEWORLD.md)；未运行完整生成权重 |
| TRELLIS.2 | [kineworld/TRELLIS.2](https://github.com/kineworld/TRELLIS.2) | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | MIT | 3D资产生成候选；不保证任意整屋场景重建 |
| gsplat | [kineworld/gsplat](https://github.com/kineworld/gsplat) | [nerfstudio-project/gsplat](https://github.com/nerfstudio-project/gsplat) | Apache-2.0 | 高斯光栅化与训练基础设施 |
| Nerfstudio | [kineworld/nerfstudio](https://github.com/kineworld/nerfstudio) | [nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio) | Apache-2.0 | NeRF与场景重建工程框架 |
| COLMAP | [kineworld/colmap](https://github.com/kineworld/colmap) | [colmap/colmap](https://github.com/colmap/colmap) | BSD，依赖单独许可 | 多视图相机位姿、结构恢复 |
| Open3D | [kineworld/Open3D](https://github.com/kineworld/Open3D) | [isl-org/Open3D](https://github.com/isl-org/Open3D) | MIT | 点云与网格处理、几何检查 |
| viser | [kineworld/viser](https://github.com/kineworld/viser) | [viser-project/viser](https://github.com/viser-project/viser) | Apache-2.0 | Python侧交互式3D调试与可视化 |
| glTF Transform | [kineworld/glTF-Transform](https://github.com/kineworld/glTF-Transform) | [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform) | MIT | glTF/GLB处理与优化，不负责创造缺失几何 |
| Physics-IQ | [kineworld/physics-IQ-benchmark](https://github.com/kineworld/physics-IQ-benchmark) | [google-deepmind/physics-IQ-benchmark](https://github.com/google-deepmind/physics-IQ-benchmark) | 软件 Apache-2.0；其他材料 CC-BY-4.0 | 物理视频评测工具；Fork不代表上榜或官方背书 |
| VBench | [kineworld/VBench](https://github.com/kineworld/VBench) | [Vchitect/VBench](https://github.com/Vchitect/VBench) | Apache-2.0 | 视频质量多维评测，不是完整世界模型能力证明 |

上述许可证栏说明仓库主体代码，并非依赖、权重、训练数据和示例素材的统一商用许可。本批新增 Cosmos、JEPA-WMs、OpenDW，并纳入此前的 CausalWM 派生项目。上表逐项标注实改、测试和仍未验证的范围；其余项目保持参考状态。

## 当前优先级

- **产品交付优先**：Spark、glTF Transform、Open3D；先检查现有产品是否已经使用，避免重复接入。
- **重建与生成候选**：gsplat、Nerfstudio、COLMAP、TRELLIS.2；输入要求、资产/场景区别和资源占用各不相同，按任务选择，不全部堆入运行环境。
- **当前模型改进主线**：CausalWM、Cosmos、V-JEPA、JEPA-WMs、OpenDW、DreamerV3、Wan2.2；本批工程与数值修复已建立独立测试，接下来需要完整权重与同条件效果验证。MIRA 保持参考状态。
- **验证工具**：Physics-IQ、VBench、viser；基准数据权限和评测协议单独核实，开发与测试分离。

Fork 保留上游作者、历史及许可证。对这些项目的选择表示与本项目方向有关，不是“全球最强”排名。没有运行证据的项目不得出现在已实现功能列表中。

### MIRA 可以做什么

上游发布的是 Rocket League 场景中的多人交互世界模型，不是通用照片转3D服务。复现前还需核实权重获取方式、数据与权重许可、硬件要求。不能因为代码开放，就认定所有素材都可商用或可再训练；也尚未验证12GB显存笔记本运行效果。

### Spark 可以做什么

Spark 负责显示已有的3D高斯场景，不负责从照片生成场景，也不自动将高斯转换成高质量通用GLB网格。原始项目由 World Labs 开发，详见[官方文档](https://sparkjs.dev/)。

## 没有复制的能力

- [Atlas](https://www.worldlabs.ai/blog/atlas)：本次未取得可复制的模型代码或权重。公开演示不等于开源授权。
- [Marble / World API](https://platform.worldlabs.ai/)：服务接入与模型拥有权不同；付费、输出使用、再训练及署名遵循实际服务条款，不能假设允许蒸馏。
- [Runway GWM Worlds 2](https://runway.com/research/introducing-gwm-worlds-2)：研究预览不等于可移植的开源实现；仅保留官方入口。

## 勘境自有实验入口

[KineJing](https://github.com/kineworld/KineJing) 已完成真实 DINOv2 推理及小型动作条件特征预测器训练，详见[模型卡](https://github.com/kineworld/KineJing/blob/main/docs/DYNAMICS_MODEL_CARD.md)。DINOv2 原始贡献来自 [Meta](https://github.com/facebookresearch/dinov2)，上游权重没有随勘境检查点重新分发。该小模型输出特征，没有 RGB 解码器，不是上述大模型的联合训练或新的基础大模型。

## 适配与验收顺序

1. 保留上游历史、LICENSE、NOTICE（如有）和作者信息；修改文件明确记录改动。
2. 固定上游提交版本；检查依赖、权重与数据的分别许可。
3. 先运行上游最小示例，记录环境、时间、显存与失败情况；未经许可或预算确认不下载受限数据、不调用收费服务。
4. 在独立分支做小规模适配，通过检查再合并。不把第三方密钥、成员信息或用户素材放进仓库。
5. 对外分别展示“上游能力”“勘境改动”“本机验证结果”，没有运行证据的状态保持待验证。

当前没有通过这些 Fork 获得新榜单成绩或证明产品质量。官网部署独立推进，本次不修改域名解析。

[返回学习指南](README.md)
