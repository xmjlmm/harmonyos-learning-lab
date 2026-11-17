# 状态管理与主题设置：扩展示例

保留父子组件状态管理和跨页面主题共享的扩展教学实现。

## 来源

原分支：`second`，固定提交：`a18e7108139e5c0772a3fe6c6c857e1ed0512b59`。

[分支迁移表](../../../docs/BRANCH-MAP.md) · [完整校验清单](../../../docs/migration-manifest.json)

## 内容与入口

- [PageA](entry/src/main/ets/pages/PageA.ets)：@State、@Prop 与 @Link。
- [PageB](entry/src/main/ets/pages/PageB.ets)：@StorageLink 主题切换。
- PageB 额外演示 @StorageProp 与装饰器说明；ChildComponent.ets 是整段注释的历史代码。

启动页已从不存在的 pages/Index 修正为 pages/PageA。PageA、PageB 均注册在 main_pages.json 中。

## 环境与运行

使用匹配工程模型的 DevEco Studio，准备 HarmonyOS 6.0.0(20) SDK。打开本目录后同步依赖、选择设备并配置自己的签名。

本目录是独立工程，不依赖其他模块的 entry、资源或依赖缓存。原 signingConfigs 为空，需要本机配置；本次不附签名材料。

## 状态与限制

主题通过 AppStorage 装饰器共享；原代码没有显式配置 PersistentStorage，不能据此宣称杀进程重启后仍保留设置。 原始页面中的“持久化”注释或文案保留，但不作为行为保证。 当前仅验证入口、路由、相对导入和资源结构，未完成 SDK 编译。
