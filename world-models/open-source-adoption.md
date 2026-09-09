# KineWorld 开源复用入口

更新：2026-09-09。这里区分上游开源项目、KineWorld 的工程适配和闭源服务。Fork 不代表原创、合作背书或已经运行成功。

## 已复制到组织的上游代码

| 项目 | KineWorld Fork | 原始项目 | 代码许可证 | 用途与当前状态 |
| --- | --- | --- | --- | --- |
| MIRA | [kineworld/mira](https://github.com/kineworld/mira) | [mira-wm/mira](https://github.com/mira-wm/mira) | Apache-2.0 | 动作条件、多玩家世界模型研究；仅完成 Fork，尚未本地复现 |
| Spark | [kineworld/spark](https://github.com/kineworld/spark) | [sparkjsdev/spark](https://github.com/sparkjsdev/spark) | MIT | THREE.js 的3D高斯渲染器；仅完成 Fork，不代表已接入产品 |

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
