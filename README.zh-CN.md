[English](README.md) | 简体中文

# Senler Skills

如果你想自己掌控项目，而不是让 AI 把项目搞得一团糟，就用这套工作流。它会让 AI 把自己不清楚的问题问出来，和你一起把每个功能或方案打磨清楚。最后，它会把每项设计决策和代码结构保存在人类能读懂的项目文档里。

这套工作流很大程度上借鉴了 AIHero，但有三个关键变化：

- **维护一套人能读懂的项目文档。** 长期设计和架构留在真正能给人看的文档里。
- **流程由你控制。** 什么时候运行哪个阶段由你决定，不让 AI 替你组织整个项目。
- **想做功能或修改时，随时创建一个 Spec。** 每个 Spec 只是 AI 为这次变更留下的一份简短记录，方便你以后阅读，而不是试图接管整个项目设计的巨型文档。

## 安装和使用

把下面这一句话发给 Codex，一次安装全部九个 Skill：

```text
Use $skill-installer to install all nine Skills from https://github.com/senler007/skills.
```

安装完成后开始一个新的 Codex 对话，打开你的项目，然后运行：

```text
Use $setup-senler-skills to configure this project so every Skill knows where its docs and tracker live.
```

这一步会为当前项目初始化这些 Skill，每个项目只需要运行一次。

## 工作流

什么时候进入下一步，由你决定：

1. **只设置一次**：运行 `$setup-senler-skills`，把这些 Skill 连接到当前项目的文档和 Tracker。
2. **把设计聊清楚**：运行 `$grill-with-docs`。它每次只问一个决策，只把已经确认的答案写进项目文档。
   - **例子：**“帮我确定完整的回合生命周期。”“和我一起梳理道具卡系统的设计。”
3. **为这次修改留下记录**：当一个功能或修改已经足够明确时，运行 `$to-spec`。
4. **拆成真正能做的工作**：运行 `$to-tickets`，检查纵向切片和依赖关系，然后由你批准。
5. **只实现指定范围**：把一个 Spec、一组 Ticket 或单个 Ticket 交给 `$implement`。它会测试、同步文档、审查并提交。

任何 Skill 都不会偷偷进入下一阶段。项目控制权始终在你手里。

## 每个 Skill 是干什么的

### 显式工作流

只有你主动调用时才会运行。

| Skill | 用途 |
| --- | --- |
| `setup-senler-skills` | 告诉其他 Skill 项目的 Tracker 和文档在哪里，不会顺手创建一堆空文件。 |
| `grill-with-docs` | 每次只问一个设计问题，把确认后的答案写进正确的项目文档。 |
| `to-spec` | 只为这次修改留下一份简短记录，不把完整项目设计复制进去。 |
| `to-tickets` | 把修改拆成完整的纵向切片，等你确认粒度和依赖以后才发布。 |
| `implement` | 只实现你传入的范围，运行测试和审查，同步长期文档，然后提交。 |

### 支持 Skill

任务需要时，它们会提供相应纪律。

| Skill | 用途 |
| --- | --- |
| `grilling` | 不让 AI 一次扔给你十个问题：一次一个决策、一个建议、一个回答。 |
| `project-documentation` | 每条长期事实只保存在一个人能读懂的权威来源里，不到处复制。 |
| `tdd` | 通过稳定的公开边界测试行为，而不是测试内部实现细节。 |
| `code-review` | 分开审查 Standards、Spec 和 Documentation，而且不会修改你的文件。 |

## 来源

这套工作流很大程度上借鉴了 Matt Pocock 的 AIHero Skills。本仓库使用 MIT 许可、
独立维护，并且不会自动同步上游。详情见 [`LICENSE`](LICENSE)。
