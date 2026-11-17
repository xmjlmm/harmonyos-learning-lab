# 维护约定

完整应用放 apps，独立概念示例放 samples，未完成项目放 prototypes，旧工程与产物放 archive。每个模块 README 需说明用途、入口、SDK、运行条件和验证状态。

不要把长期分支作为资料的唯一入口。后续改动使用 feature/<模块>/<主题> 等短期分支，合入 main 后由目录导航检索。已有课程分支作为来源历史保留。

独立工程中的公共样板代码即使内容一致，也不跨工程合并，以免破坏 DevEco Studio 工程边界。尚未验证的示例不应标记为可运行；修复历史代码后保留变更说明。

不再提交 .idea、.hvigor、.preview、build、oh_modules、node_modules 与本机 local.properties。archive 中已有文件是迁移基线，修改需要同时说明对完整性校验的影响。
