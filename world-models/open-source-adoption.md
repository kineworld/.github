# KineWorld 开源复用入口

更新：2026-09-09。这里区分上游开源项目、KineWorld 的工程适配和闭源服务。Fork 不代表原创、合作背书或已经运行成功。

## 已复制到组织的上游代码

| 项目 | KineWorld Fork | 原始项目 | 代码许可证 | 用途与当前状态 |
| --- | --- | --- | --- | --- |
| MIRA | [kineworld/mira](https://github.com/kineworld/mira) | [mira-wm/mira](https://github.com/mira-wm/mira) | Apache-2.0 | 动作条件、多玩家世界模型研究；仅完成 Fork，尚未本地复现 |
| Spark | [kineworld/spark](https://github.com/kineworld/spark) | [sparkjsdev/spark](https://github.com/sparkjsdev/spark) | MIT | THREE.js 的3D高斯渲染器；仅完成 Fork，不代表已接入产品 |
| V-JEPA 2 | [kineworld/vjepa2](https://github.com/kineworld/vjepa2) | [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2) | 主要 MIT，部分 Apache-2.0 | 视频隐空间预测研究；本次仅归档上游代码 |
| DreamerV3 | [kineworld/dreamerv3](https://github.com/kineworld/dreamerv3) | [danijar/dreamerv3](https://github.com/danijar/dreamerv3) | MIT | 学习世界模型并用于策略学习；不是照片转3D |
| Wan2.2 | [kineworld/Wan2.2](https://github.com/kineworld/Wan2.2) | [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | Apache-2.0 | 视频生成基线；不能等同于可下载3D或真实物理模拟 |
| TRELLIS.2 | [kineworld/TRELLIS.2](https://github.com/kineworld/TRELLIS.2) | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | MIT | 3D资产生成候选；不保证任意整屋场景重建 |
| gsplat | [kineworld/gsplat](https://github.com/kineworld/gsplat) | [nerfstudio-project/gsplat](https://github.com/nerfstudio-project/gsplat) | Apache-2.0 | 高斯光栅化与训练基础设施 |
| Nerfstudio | [kineworld/nerfstudio](https://github.com/kineworld/nerfstudio) | [nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio) | Apache-2.0 | NeRF与场景重建工程框架 |
| COLMAP | [kineworld/colmap](https://github.com/kineworld/colmap) | [colmap/colmap](https://github.com/colmap/colmap) | BSD，依赖单独许可 | 多视图相机位姿、结构恢复 |
| Open3D | [kineworld/Open3D](https://github.com/kineworld/Open3D) | [isl-org/Open3D](https://github.com/isl-org/Open3D) | MIT | 点云与网格处理、几何检查 |
| viser | [kineworld/viser](https://github.com/kineworld/viser) | [viser-project/viser](https://github.com/viser-project/viser) | Apache-2.0 | Python侧交互式3D调试与可视化 |
| glTF Transform | [kineworld/glTF-Transform](https://github.com/kineworld/glTF-Transform) | [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform) | MIT | glTF/GLB处理与优化，不负责创造缺失几何 |
| Physics-IQ | [kineworld/physics-IQ-benchmark](https://github.com/kineworld/physics-IQ-benchmark) | [google-deepmind/physics-IQ-benchmark](https://github.com/google-deepmind/physics-IQ-benchmark) | 软件 Apache-2.0；其他材料 CC-BY-4.0 | 物理视频评测工具；Fork不代表上榜或官方背书 |
| VBench | [kineworld/VBench](https://github.com/kineworld/VBench) | [Vchitect/VBench](https://github.com/Vchitect/VBench) | Apache-2.0 | 视频质量多维评测，不是完整世界模型能力证明 |

上述许可证栏说明仓库主体代码，并非依赖、权重、训练数据和示例素材的统一商用许可。本次新增12个 Fork，加上先前 MIRA 与 Spark 共14个。均未通过本次操作完成运行或产品接入。

## 当前优先级

- **产品交付优先**：Spark、glTF Transform、Open3D；先检查现有产品是否已经使用，避免重复接入。
- **重建与生成候选**：gsplat、Nerfstudio、COLMAP、TRELLIS.2；输入要求、资产/场景区别和资源占用各不相同，按任务选择，不全部堆入运行环境。
- **研究参考**：V-JEPA 2、DreamerV3、MIRA、Wan2.2；先确定实验问题，再选择基线。
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

## 适配与验收顺序

1. 保留上游历史、LICENSE、NOTICE（如有）和作者信息；修改文件明确记录改动。
2. 固定上游提交版本；检查依赖、权重与数据的分别许可。
3. 先运行上游最小示例，记录环境、时间、显存与失败情况；未经许可或预算确认不下载受限数据、不调用收费服务。
4. 在独立分支做小规模适配，通过检查再合并。不把第三方密钥、成员信息或用户素材放进仓库。
5. 对外分别展示“上游能力”“勘境改动”“本机验证结果”，没有运行证据的状态保持待验证。

当前没有通过这些 Fork 获得新榜单成绩或证明产品质量。官网部署独立推进，本次不修改域名解析。

[返回学习指南](README.md)
