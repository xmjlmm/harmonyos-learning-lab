# 分支迁移与重组

| 原分支 | 固定提交 | 新路径 | 原文件数 |
| --- | --- | --- | --- |
| `big_homework` | `4d9e7ab33e57c8c70cd7669e00fb6d17a3f753f0` | `archive/scaffolds/big-homework` | 8 |
| `bighomework` | `721a5b53fbba8702d0d93ee25420053a01161462` | `prototypes/farm-assistant` | 48 |
| `first` | `ef4a24c7d7ffbda3f69db008df43a87747c910a2` | `apps/farm-manager` | 59 |
| `main` | `c046da51633cf31a2618e5c183b4e6efabb07c22` | `docs/original-main-README.md` | 1 |
| `rdb_master` | `cbf7bd3f8ef9b7c2a7065a95c636f4538b4223ca` | `samples/distributed-billing` | 271 |
| `second` | `a18e7108139e5c0772a3fe6c6c857e1ed0512b59` | `samples/state-management/extended` | 39 |
| `third` | `90f7c627ec2deede937a4404f33a1ceec5ffd95b` | `samples/state-management/basic` | 39 |

## 边界与保留策略

first 才是较完整的智慧农场工程；不能按分支名误认为它只包含第一次简单作业。bighomework 是另一份未完成实现，保留独立原型。big_homework 仅含配置，归入历史骨架。

second 和 third 的页面实现、装饰器示例与路由配置存在差异，因此分别保留扩展与基础示例。重复的框架样板不跨工程去重，避免引入构建耦合。

rdb_master 作为有独立许可证的完整数据库示例保留；缓存、预览与构建产物归 archive/generated。原始顶层 README 以 README.upstream.md 保存，main 原文单独归档。

所有原文件在新树中均有原始字节副本。仅修改 3 个启动/路由文件，其修改前版本归 archive/originals，详情见迁移清单 adjustments。

本次不删除原分支、不改写历史。整理提交以原 main 为父提交，通过普通快进推送更新 main，并保留 reorganize/project-layout 分支。
