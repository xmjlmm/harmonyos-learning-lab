# 分布式关系型数据库账单示例

保留 Huawei Codelab 的分布式账单工程，以及原始中英文说明、截图和 Apache 2.0 许可证。

## 来源

原分支：`rdb_master`，固定提交：`cbf7bd3f8ef9b7c2a7065a95c636f4538b4223ca`。

[分支迁移表](../../docs/BRANCH-MAP.md) · [完整校验清单](../../docs/migration-manifest.json)

## 内容与入口

- [BillHomePage](entry/src/main/ets/pages/BillHomePage.ets)：账单页面。
- `components/BillDialog.ets`：账单编辑弹窗。
- `utils/RdbManager.ets`、`viewmodel`：数据访问与页面数据模型。
- [screenshots](screenshots/)：原始效果预览。

EntryAbility 加载 pages/BillHomePage；账单支持新增、删除、编辑、查询，源码包含同步相关接口。

## 环境与运行

使用匹配工程模型的 DevEco Studio，准备 HarmonyOS 5.1.1(19) SDK。打开本目录后同步依赖、选择设备并配置自己的签名。

本目录是独立工程，不依赖其他模块的 entry、资源或依赖缓存。原 signingConfigs 为空，需要本机配置；本次不附签名材料。

## 状态与限制

跨设备验证按原 README 要求使用支持的双端设备、同一华为账号、分布式数据权限、Wi-Fi 和蓝牙条件。原说明要求 HarmonyOS / DevEco Studio / SDK 5.1.1 Release 及以上，工程当前 SDK 目标为 5.1.1(19)。缓存移出工程，需由 IDE 重新生成；本次未实测设备间同步。

## 原始说明

原 README 保存在 [README.upstream.md](README.upstream.md)，同目录资源与许可证保持原相对位置。
