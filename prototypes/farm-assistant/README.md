# 智慧农场助手早期原型

较早的智慧农场助手原型；与 apps/farm-manager 是不同实现，不进行源码拼接。

## 来源

原分支：`bighomework`，固定提交：`721a5b53fbba8702d0d93ee25420053a01161462`。

[分支迁移表](../../docs/BRANCH-MAP.md) · [完整校验清单](../../docs/migration-manifest.json)

## 内容与入口

- `model/DataModel.ets`：作物、任务、天气与设置模型。
- `model/RdbManager.ets`：本地数据库方法。
- `components`：作物、天气和统计卡片。
- [Index](entry/src/main/ets/pages/Index.ets)、[CropManage](entry/src/main/ets/pages/CropManage.ets)：原型页面。

配置启动 pages/Index，注册 Index 与 CropManage。

## 环境与运行

使用匹配工程模型的 DevEco Studio，准备 HarmonyOS 6.0.0(20) SDK。打开本目录后同步依赖、选择设备并配置自己的签名。

本目录是独立工程，不依赖其他模块的 entry、资源或依赖缓存。原 signingConfigs 为空，需要本机配置；本次不附签名材料。

## 状态与限制

**不能直接编译运行。** CropManage.ets 在 `.onClick(() => { this.is` 处被截断；Index 跳转的 pages/Settings 未提供；RdbManager.initRdbStore 有定义但没有在源码中找到初始化调用。保留原始代码作为未完成原型，不编造缺失业务。建议从 apps/farm-manager 阅读主要应用。
