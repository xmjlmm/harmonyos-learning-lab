# 状态管理与主题设置：基础示例

保留父子组件状态管理和跨页面主题共享的基础教学实现。

## 来源

原分支：`third`，固定提交：`90f7c627ec2deede937a4404f33a1ceec5ffd95b`。

[分支迁移表](../../../docs/BRANCH-MAP.md) · [完整校验清单](../../../docs/migration-manifest.json)

## 内容与入口

- [PageA](entry/src/main/ets/pages/PageA.ets)：@State、@Prop 与 @Link。
- [PageB](entry/src/main/ets/pages/PageB.ets)：@StorageLink 主题切换。
- ChildComponent.ets 另外保留一个单独的双向绑定演示；不作为默认启动页。

启动页已从不存在的 pages/Index 修正为 pages/PageA。PageA、PageB 均注册在 main_pages.json 中。

## 环境与运行

使用匹配工程模型的 DevEco Studio，准备 HarmonyOS 6.0.0(20) SDK。打开本目录后同步依赖、选择设备并配置自己的签名。

本目录是独立工程，不依赖其他模块的 entry、资源或依赖缓存。原 signingConfigs 为空，需要本机配置；本次不附签名材料。

## 状态与限制

主题通过 AppStorage 装饰器共享；原代码没有显式配置 PersistentStorage，不能据此宣称杀进程重启后仍保留设置。 本次额外补注册原来缺失的 PageB 路由。 当前仅验证入口、路由、相对导入和资源结构，未完成 SDK 编译。
