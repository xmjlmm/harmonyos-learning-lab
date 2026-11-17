# 早期大作业工程骨架

原 big_homework 分支只有工程级配置和旧 README，是后续作业的早期骨架。

## 来源

原分支：`big_homework`，固定提交：`4d9e7ab33e57c8c70cd7669e00fb6d17a3f753f0`。

[分支迁移表](../../../docs/BRANCH-MAP.md) · [完整校验清单](../../../docs/migration-manifest.json)

## 内容与入口

保留 build-profile.json5、oh-package.json5、锁文件、Hvigor 与 linter 配置。原 local.properties 属于本机文件，单独归档。

没有 EntryAbility、页面或完整 entry 模块。

## 环境与运行

配置声明 HarmonyOS 6.0.0(20)，但缺少 entry、AppScope 和源码，不作为可导入运行的完整工程。仅供对照配置。

## 状态与限制

不能作为完整工程构建。不要从其他项目随意拼入 entry 来冒充原工程；需要完整应用时使用 apps/farm-manager，或参考独立农场助手原型。

## 原始说明

原 README 保存在 [README.upstream.md](README.upstream.md)，同目录资源与许可证保持原相对位置。
