# 整理验证与已知问题

快照与整理日期：2026-11-17。

## 已验证的内容

- 对 7 个来源分支的当前提交逐文件读取 Git blob，并在迁移时核对 Git SHA-1。
- 465 个原文件均保留原始字节，包括移入归档的缓存、预览、构建文件和本机配置；迁移清单同时记录 SHA-256、大小、文件模式、原路径与原提交。
- 独立应用与学习示例维持各自 AppScope、entry、资源和工程配置，不跨工程抽取样板代码。
- 状态管理示例的两个 EntryAbility 启动页改为 pages/PageA，third 的 main_pages.json 增加 PageB；3 个修改前文件均归档保留。
- 复查脚本检查原文件完整性、3 处修改后的哈希、5 个源码工程的相对导入、已注册页面、显式页面引用，以及新增 Markdown 的本地链接。
- 本次执行结果：465 个原文件与 3 处修正哈希通过；检查 52 条相对导入、15 条页面引用、29 份新增 Markdown 和 48 条本地链接。原有导航与原型问题单独列出，未发现额外迁移丢失或未知引用错误。

复查命令：

```powershell
python scripts/verify_repository.py
```

## 明确保留的未完成内容

1. 农场助手原型 CropManage.ets 在 `.onClick(() => { this.is` 处截断，不能编译。
2. 同一原型的 Index 引用了未提供的 pages/Settings，数据库初始化方法存在但未找到调用。
3. big_homework 只含配置，没有完整 entry/AppScope 工程。
4. 主农场应用的天气页面有模拟延迟，DataSyncManager 中多处通知/回调被注释；不宣称真实天气或跨设备同步已完成。
5. 状态管理示例没有显式 PersistentStorage 配置。@StorageLink/@StorageProp 的共享状态不能直接当作跨进程持久化保证。
6. 主农场应用有 5 个原有路由问题：缺少 Recording、RecordDetail、WeatherDetailPage 文件，以及 ProductPage、SettingsPage 未注册为路由目标。组件组合不等于路由注册。详见 known-route-issues.json，保持原源码并在模块 README 中披露。

这些问题不是迁移造成的，已分别写入模块 README。校验脚本将主农场和原型的 8 项问题单独标为 KNOWN LEGACY ISSUE，只有列明来源文件与目标的已知路由可以作为历史问题保留；新发现的未知路由仍导致校验失败。通过校验表示迁移与有限入口修正符合基线，不代表上述业务问题已修复或通过编译。

## 验证限制

本次执行文件与结构验证，没有进行 HarmonyOS SDK 编译、设备安装或真机交互验证。没有在应用清单中发现可供使用的 DevEco Studio 窗口或已登记安装项；未为本次整理安装开发环境。现有工程不包含命令行 Hvigor wrapper。

SDK、签名、设备权限、数据库行为与多设备同步需要在匹配的 DevEco Studio 和设备环境中进一步验证。原 Codelab 的历史外链不在新增链接校验范围内。

维护提示：脚本中的原文件哈希是本次迁移基线。后续业务修改可能使基线检查报告差异，应在明确变更范围后维护校验规则，不能为了消除差异而直接删除来源记录。
