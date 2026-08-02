[English](README.md) | 简体中文

# Senler Skills

一套精简、以 Codex 为首要支持环境的开发工作流，用来把设计讨论转化为经过审查、
文档同步并已提交的实现。Tracker 工件负责交付过程，人类可读的项目文档负责保存
长期产品知识。

首个版本正好包含九个 Skill。

| 显式工作流 | 用途 |
| --- | --- |
| `setup-senler-skills` | 配置 Tracker、文档路径、语言和 Agent 指引 |
| `grill-with-docs` | 一次解决一个设计决策，并同步已经确认的设计 |
| `to-spec` | 把已完成的讨论发布为面向变更的 Spec |
| `to-tickets` | 发布经过确认、具有真实依赖关系的纵向切片 Ticket |
| `implement` | 实现指定范围、处理审查阻断项、验证并提交 |

| 支持性纪律 | 用途 |
| --- | --- |
| `grilling` | 每次只提出一个带推荐答案的决策问题 |
| `project-documentation` | 把每条长期事实放入唯一的权威来源 |
| `tdd` | 通过已经确认的稳定边界测试外部行为 |
| `code-review` | 分别审查 Standards、Spec 和 Documentation |

## 安装

使用 Codex 标准的 `$skill-installer`，仓库地址为：

https://github.com/senler007/skills

例如，只安装 `to-spec` 时，可以这样告诉 Codex：

```text
Use $skill-installer to install the to-spec Skill from https://github.com/senler007/skills/tree/main/skills/to-spec.
```

安装全部九个 Skill 时，可以这样说：

```text
Use $skill-installer to install all nine Skills from https://github.com/senler007/skills.
```

标准安装器会把 `skills/` 下的每个目录识别为一个独立 Skill 包。安装后重新启动
Codex，或开始一个新的 Codex 对话轮次，以便发现新安装的 Skill。

## 工作流

常规流程分为五个阶段：

1. **一次性设置**：调用 `setup-senler-skills`，记录项目真实的 Tracker 和文档布局。
2. **讨论设计**：调用 `grill-with-docs`，直到双方理解一致，长期设计文档也完成同步。
3. **编写 Spec**：调用 `to-spec`，发布已经确认的变更和测试边界。
4. **规划 Ticket**：调用 `to-tickets`，确认纵向切片的粒度和依赖关系。
5. **实现**：把一个 Spec、一组 Ticket 或单个 Ticket 交给 `implement`；它会在提交前执行 TDD、文档同步和三轴审查。

每个显式工作流都会在完成自己的输出后停止。是否进入下一阶段由用户决定，任何
工作流都不会擅自推进到另一个阶段。

## 文档权威

这套 Skill 会为每条长期事实指定唯一的权威来源，并把长期项目知识与 Tracker
进度分开。项目概览、术语表、设计、架构、ADR 和 Tracker 的详细职责边界，以
[`project-documentation` 角色说明](skills/project-documentation/references/document-roles.md)
为准。其他文档只链接到权威来源，不再维护规则副本。

## Codex 支持

Codex 是首个正式支持并完成前向测试的运行环境。Skill 指令及其引用资料使用英文
维护；生成或更新项目文档时，会遵循目标项目已经确定的语言、路径、大小写和术语。

这些 Skill 会在可行范围内保持可移植性，但首个版本不承诺兼容所有支持 Skill 的工具。

## 归属说明

本项目在很大程度上借鉴了 Matt Pocock 的 AI Hero Skills 工作流，并作为一个独立、
一次性派生版本维护。项目不会自动同步上游；后续上游变更只会以人工、主动选择的
方式引入。MIT 许可信息见 [`LICENSE`](LICENSE)。

| Skill | 来源 |
| --- | --- |
| `setup-senler-skills` | 本项目原创 |
| `project-documentation` | 本项目原创 |
| `grilling` | 派生自 AI Hero 工作流 |
| `grill-with-docs` | 基于 AI Hero 工作流大幅重写 |
| `to-spec` | 基于 AI Hero 工作流大幅重写 |
| `to-tickets` | 派生自 AI Hero 工作流 |
| `code-review` | 基于 AI Hero 工作流大幅重写 |
| `tdd` | 派生自 AI Hero 工作流 |
| `implement` | 基于 AI Hero 工作流大幅重写 |
