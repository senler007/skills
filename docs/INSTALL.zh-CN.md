# 三个工作流 Skill：安装和使用

这三个 Skill 分别负责需求澄清、方案与实施、Figma 任务调度。
先用 `grilling` 或 `ask-plan-build` 处理单个任务也可以。
它们是指令与辅助文件；安装 Skill 不会自动获得 Figma 访问权、创建每日任务或开始操作项目。

## 安装

需要 Node.js/npm 和 Git。在终端执行：

```bash
npx skills add senler007/skills --skill grilling ask-plan-build figma-task-steward -a codex -g --copy
```

这条命令安装默认分支的三个 Skill 到 Codex 个人目录，不修改当前项目。
`--copy` 使用复制方式，Windows 无需创建符号链接。
只装其中一个时，在 `--skill` 后只保留它的名称。
命令使用第三方 [Vercel Skills CLI](https://github.com/vercel-labs/skills)，具体安装路径以终端输出为准。

安装完成后检查是否能用 `$grilling`、`$ask-plan-build`、`$figma-task-steward` 调用。
未出现时重启 Codex。已有同名个人修改版时先备份，再决定是否替换；不要在多个个人目录重复安装同名版本。
关于本地 Skill 的发现方式，见 [OpenAI 文档](https://learn.chatgpt.com/docs/build-skills)。

## 先试用两个独立 Skill

复制给 Codex，并换成自己的任务：

```text
使用 $grilling 帮我澄清这个功能：玩家可以保存并切换多个角色外观方案。
```

或者：

```text
使用 $ask-plan-build，为我的项目增加角色外观方案保存功能。先问清必要问题，再给出具体方案。
```

`grilling` 按决策依赖逐轮提问，`ask-plan-build` 的独立流程是一轮最多五问。
已有问答交给管家工作流时会复用，不应重新采访。具体行为以各 Skill 的 `SKILL.md` 为准。
若要求把结论写入长期项目文档，还需项目配置的 `project-documentation` Skill；本仓库提供该包，可按需另行安装。

## Figma 任务管家的首次配置

运行环境需要：

- Codex 桌面端中可用的项目、独立会话、会话消息工具；跨天自动接班还需要自动任务工具。仅有基础 CLI 或聊天界面不能假定这些能力可用。
- 已连接并授权访问目标文件的 Figma 插件，提供 Figma 工具及 `figma-use` Skill。
- 本机 Python 3.8 或更新版本，用于包内的 `scripts/ledger.py`；脚本只用 Python 标准库。
- 本仓库提供的 `grilling`、`ask-plan-build`，以及目标项目要求的文档、代码规范等 Skill。Unreal 项目另用自己的 Unreal 项目 Skill，它们不会由这条三 Skill 安装命令一并安装。

在自己的项目里准备这些真实入口，已有文件直接补充，不要复制作者的私人项目：

| 文件或位置 | 需要提供的信息 |
| --- | --- |
| `Docs/ProjectOverview.md` | 项目简介、默认 Figma 文件链接 |
| `Docs/agents/issue-tracker.md` | 项目使用的规格/任务跟踪方式；不用 GitHub Issues 就明确自己的事实来源 |
| `Docs/agents/project-docs.md` | 文档语言、项目文档位置和维护规则 |
| Figma 的 `每日安排` 页面 | 有真实标题、需求文字、验收目标及必要参考图的任务容器 |

入口准备好后，在这个项目的 Codex 会话发送：

```text
使用 $figma-task-steward 管理当前项目的 Figma「每日安排」。
允许为交给 AI 的任务创建独立 Codex 会话，并在这些会话之间发送派发、交接与完成消息。
先核查已有会话和任务归属，再逐卡开始澄清；共享项目的调查和实施遵守串行操作规则。
```

如需每天新建管家，再明确告诉 Codex 每天几点执行，由它配置每日自动任务。
安装本身不会创建自动任务，也不会自动监听 Figma 每次修改。

账本存放在个人 Codex 目录下的 `figma-task-steward/<工作区路径哈希>/state.json`。
仓库不包含作者的账本、项目路径、账户连接或会话记录。
账本用于合作会话协调，不能强制阻止人工、未登记会话或另一台机器改动项目。
完整规则见 [Figma 管家 Skill](../skills/figma-task-steward/SKILL.md)。

## 更新

安装新版前备份自己的同名修改，再运行上面的安装命令。
只更新 Skill 文件，不要删除个人 Codex 目录下的运行账本。
