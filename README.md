English | [简体中文](README.zh-CN.md)

# Senler Skills

## Three Skills from the article

Clarify decisions with **grilling**, review a concrete solution with
**ask-plan-build**, or explicitly enable **figma-task-steward** to coordinate
independent task chats from a Figma task board.

| Skill | Purpose | Source |
| --- | --- | --- |
| `grilling` | Ask consequential questions in dependency order, with recommendations and tradeoffs. | [SKILL.md](skills/grilling/SKILL.md) |
| `ask-plan-build` | Ask one round of up to five questions, propose concrete changes, then implement after your response. | [SKILL.md](skills/ask-plan-build/SKILL.md) |
| `figma-task-steward` | Coordinate clarification, serial project operations, acceptance, and handover in Codex desktop. | [SKILL.md](skills/figma-task-steward/SKILL.md) |

**[中文安装和使用说明](docs/INSTALL.zh-CN.md)**

With Node.js/npm and Git installed, install only these three to your Codex user
directory using the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add senler007/skills --skill grilling ask-plan-build figma-task-steward -a codex -g --copy
```

This installs the current default branch. Back up locally edited copies before
updating the same skill. If installed skills do not appear, restart Codex.

**Figma steward prerequisites:** Codex desktop with project/chat-management tools,
a connected Figma plugin (including `figma-use`), Python 3.8+, the two companion
skills above, and project documentation pointing to your Figma file and its
`每日安排` page. Configure `Docs/ProjectOverview.md`,
`Docs/agents/issue-tracker.md`, and `Docs/agents/project-docs.md` for your own
project; use its applicable documentation/coding/Unreal skills when needed.
Installation does not configure account connections or daily automation. Enable the
workflow explicitly; it is not a live Figma watcher or an operating-system lock.
See the [setup guide](docs/INSTALL.zh-CN.md#figma-任务管家的首次配置).

## Existing Spec and Ticket workflows

The rest of this repository also retains the earlier, manually selected workflow
stages described below. Installing the three skills above does not install all
of those stages or require you to use them.

If you want to control your own project instead of letting AI turn it into a mess,
use this workflow. It makes AI ask about what it does not understand and work with
you until each feature or solution is clear. Finally, it preserves every design
decision and code structure in human-readable project documentation.

This workflow is largely inspired by AIHero, with three key changes:

- **Human-readable project docs.** Each major module keeps its durable design,
  current code structure, and maintenance map in one document people can read.
- **You control the workflow.** You decide which stage runs and when. AI does not orchestrate the project for you.
- **Create a Spec whenever you want to build or change something.** Each Spec is a small AI-written record you can read later, not a giant document trying to own the whole project.

## Set and Use

Paste this into Codex to install the nine packages used by this earlier workflow:

```text
Use $skill-installer to install setup-senler-skills, grill-with-docs, to-spec, to-tickets, implement, grilling, project-documentation, tdd, and code-review from https://github.com/senler007/skills (each is under skills/).
```

After installation, start a new Codex turn, open your project, and run:

```text
Use $setup-senler-skills to configure this project so every Skill knows where its docs and tracker live.
```

This initializes the Skills for that project and only needs to run once.

## Workflow

Use only the stages your change needs. You decide which Skill runs and when:

1. **Talk the design through** - run `$grill-with-docs` when the design is still unclear. It uses `$grilling` to clarify decisions, then writes the consolidated decisions to project docs only after you confirm the final summary.
   - **Examples:** "Help me define the full turn lifecycle." "Walk me through the item-card system and clarify its design."
2. **Create a change record** - run `$to-spec` whenever a feature or change is clear enough to build.
3. **Break it into real work (optional)** - run `$to-tickets` when the Spec needs independent slices, dependency ordering, or staged delivery, then approve the breakdown.
4. **Build exactly that scope** - run `$implement` directly with a Spec or a set of Tickets. It tests, updates docs, reviews the result, and commits.

Nothing silently starts the next stage. You stay in control.

**A small change:**

```text
You Say     :[$grill-with-docs] I need to flesh out the duel system
Communicate :Talk it through with AI...
You Say     :[$to-spec]
You Say     :[$implement]
Finally     :Finish with a complete feature ready for human acceptance testing
```

For larger work, run `[$to-tickets]` between `$to-spec` and `$implement` so you
can approve the slices and dependencies first.

## What Each Skill Does

### Explicit Workflows

These run only when you ask for them.

| Skill | What it does |
| --- | --- |
| `setup-senler-skills` | Tells the Skills where your tracker and project docs live without creating empty junk. |
| `grill-with-docs` | Uses `$grilling` to clarify decisions, gets final confirmation, then writes the consolidated decisions to the right project document in one pass. |
| `to-spec` | Creates a small record of one change instead of copying the whole project design. |
| `to-tickets` | Optionally splits larger work into complete vertical slices and waits for you to approve the plan. |
| `implement` | Implements a Spec or Ticket scope directly, runs tests and review, updates durable docs, and commits. |

### Supporting Skills

These provide discipline when the task needs it.

| Skill | What it does |
| --- | --- |
| `grilling` | Asks small groups of questions whose prerequisites are settled, with a recommendation and tradeoff for each. |
| `project-documentation` | Keeps each module's design, code structure, and maintenance map in one human-readable guide, then records completed project changes in the daily development record. |
| `tdd` | Tests behavior through stable public seams instead of testing implementation details. |
| `code-review` | Reviews Standards, Spec, and Documentation separately without changing your files. |

## Credit

Largely inspired by Matt Pocock's AIHero Skills workflow. This repository is MIT
licensed, independently maintained, and does not automatically sync upstream.
See [`LICENSE`](LICENSE).
