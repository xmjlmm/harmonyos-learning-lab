# 智慧农场管理应用

较完整的智慧农场课程应用，保留农产品与生长记录管理、统计、天气展示和设置等功能。

## 来源

原分支：`first`，固定提交：`ef4a24c7d7ffbda3f69db008df43a87747c910a2`。

[分支迁移表](../../docs/BRANCH-MAP.md) · [完整校验清单](../../docs/migration-manifest.json)

## 内容与入口

- `entry/src/main/ets/pages`：MainPage、HomePage、ProductPage、RecordPage、WeatherPage、SettingsPage。
- `components`：农场、产品、记录、天气与公共布局组件。
- `database/FarmDatabase.ets`：本地关系型数据库。
- `model`、`manager`、`utils`：数据模型、通知协调和工具函数。

入口为 [EntryAbility](entry/src/main/ets/entryability/EntryAbility.ets)，加载 [MainPage](entry/src/main/ets/pages/MainPage.ets)。页面间主要通过组件组合展示，main_pages.json 仅注册 MainPage。

## 环境与运行

使用匹配工程模型的 DevEco Studio，准备 HarmonyOS 6.0.0(20) SDK。打开本目录后同步依赖、选择设备并配置自己的签名。

本目录是独立工程，不依赖其他模块的 entry、资源或依赖缓存。原 signingConfigs 为空，需要本机配置；本次不附签名材料。

## 状态与限制

**原工程仍有未完成的导航流程。** ProductPage 指向缺失的 Recording，RecordPage 指向缺失的 RecordDetail；WeatherPage 指向缺失的 WeatherDetailPage。另有对 ProductPage、SettingsPage 的 router 跳转，但 main_pages.json 未注册这些目标。MainPage 内的组件切换与 router 跳转是两种不同路径，不能将组件切换可见等同于路由完整。具体问题记录在 [已知路由清单](../../docs/known-route-issues.json)，本次保留原源码并明确披露，不编造缺失详情页面。

天气页面含模拟 API 延迟，不代表已接入真实气象服务；DataSyncManager 部分通知和回调语句仍为注释。代码中“已同步”等展示文案不能视为跨设备同步验证结果。首次初始化会在空数据库中添加示例农产品。未进行 SDK 编译与真机验收。
