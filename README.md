# harmonyos-learning-lab

HarmonyOS / ArkTS 移动应用开发学习与课程项目合集，原仓库名为 `devstudio`。将分支中的独立工程集中到主分支，以完整工程为边界维护。

## 项目导航

| 内容 | 来源分支 | 定位与状态 |
| --- | --- | --- |
| [智慧农场管理](apps/farm-manager/README.md) | `first` | 主要课程应用；保留原有详情页面和路由缺口，见模块说明 |
| [状态管理扩展示例](samples/state-management/extended/README.md) | `second` | @State / @Prop / @Link / @StorageLink / @StorageProp 与主题设置 |
| [状态管理基础示例](samples/state-management/basic/README.md) | `third` | 父子状态绑定与跨页主题共享；保留独立实现 |
| [分布式账单](samples/distributed-billing/README.md) | `rdb_master` | 关系型数据库增删改查与设备间同步 Codelab |
| [智慧农场助手原型](prototypes/farm-assistant/README.md) | `bighomework` | 原始源码不完整，不能直接编译 |
| [早期工程骨架](archive/scaffolds/big-homework/README.md) | `big_homework` | 只有配置文件，不是完整应用 |

## 如何打开

分别用 DevEco Studio 打开上表中的**具体工程目录**。仓库根目录只负责导航，没有统一 Hvigor 构建入口；不同工程不共享 entry、AppScope、签名配置或依赖目录。

- 农场应用、状态管理示例和农场原型：工程声明 HarmonyOS **6.0.0(20)**，Hvigor 模型版本 6.0.0。
- 分布式账单：工程声明 HarmonyOS **5.1.1(19)**，Hvigor 模型版本 5.1.1；设备要求详见模块与原始说明。
- 在各工程内同步依赖、选择 SDK 和设备、配置本机签名后再构建。未安装对应 SDK 时，先通过 IDE 准备环境。
- `first`、`second`、`third` 使用相同示例 bundleName，不建议直接在同一设备并行安装；需要并行安装时，分别配置独立 bundleName 与匹配签名。

## 整理说明

保留原有 7 个分支及历史，未删除业务文件。将缓存、预览产物和本机配置移入 [归档](archive/README.md)，避免混入可维护源码。仅修复状态管理示例的启动页和路由注册，修改前文件仍完整保留。

- [分支与新目录映射](docs/BRANCH-MAP.md)
- [环境与使用流程](docs/GETTING-STARTED.md)
- [验证报告与已知问题](docs/VALIDATION.md)
- [原文件校验清单](docs/migration-manifest.json)
- [维护约定](CONTRIBUTING.md)
- [来源与许可证](NOTICE.md)

在根目录运行 `python scripts/verify_repository.py` 可复查文件保留情况、迁移修正、相对导入、页面路由和新增文档链接。结构检查通过不等于完成 HarmonyOS 真机或编译验证。
