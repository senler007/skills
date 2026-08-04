# 项目文档

- 文档语言：简体中文
- 项目说明：`README.md`
- 中文项目说明：`README.zh-CN.md`
- 模块文档与行为：各 `skills/<skill-name>/SKILL.md` 及其 `references/`
- ADR 与术语表：当前不维护
- 开发记录：`docs/DevelopmentRecord/YYYY-MM-DD.md`
- Tracker 配置：`docs/agents/issue-tracker.md`

使用 `$project-documentation` 归档已确认的长期知识，并保持上述路径及大小写不变。一项事实只由一个权威来源维护，其他文档只链接，不重复说明。实现过程中可以同步已有模块文档；创建新的模块文档边界必须先由人明确确认。不要创建空占位文档。只有任务确实修改仓库后，才创建或更新当天开发记录。
