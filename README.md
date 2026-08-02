English | [简体中文](README.zh-CN.md)

# Senler Skills

If you want to control your project instead of letting AI fuck it up and leave a
mess, use this workflow. It keeps every design decision and code structure in
human-readable project documentation.

Those documents give you a clear view of the project's design and architecture,
and keep AI from crossing boundaries.

This workflow is largely inspired by AIHero, with three key changes:

- **Human-readable project docs.** Durable design and architecture stay in documents people can actually read.
- **You control the workflow.** You decide which stage runs and when. AI does not orchestrate the project for you.
- **Create a Spec whenever you want to build or change something.** Each Spec is a small AI-written record you can read later, not a giant document trying to own the whole project.

## Set and Use

Paste this into Codex to install all nine Skills:

```text
Use $skill-installer to install all nine Skills from https://github.com/senler007/skills.
```

After installation, start a new Codex turn, open your project, and run:

```text
Use $setup-senler-skills to configure this project so every Skill knows where its docs and tracker live.
```

This initializes the Skills for that project and only needs to run once.

## Workflow

You decide when to run each step:

1. **Set up once** - run `$setup-senler-skills` to connect the Skills to this project's docs and tracker.
2. **Talk the design through** - run `$grill-with-docs`. It asks one decision at a time and writes only confirmed decisions to project docs.
   - **Examples:** "Help me define the full turn lifecycle." "Walk me through the item-card system and clarify its design."
3. **Create a change record** - run `$to-spec` whenever a feature or change is clear enough to build.
4. **Break it into real work** - run `$to-tickets`, check the slices and dependencies, then approve them.
5. **Build exactly that scope** - run `$implement` with a Spec, a Ticket set, or one Ticket. It tests, updates docs, reviews the result, and commits.

Nothing silently starts the next stage. You stay in control.

## What Each Skill Does

### Explicit Workflows

These run only when you ask for them.

| Skill | What it does |
| --- | --- |
| `setup-senler-skills` | Tells the Skills where your tracker and project docs live without creating empty junk. |
| `grill-with-docs` | Asks one design question at a time and writes confirmed answers to the right project document. |
| `to-spec` | Creates a small record of one change instead of copying the whole project design. |
| `to-tickets` | Splits the change into complete vertical slices and waits for you to approve the plan. |
| `implement` | Implements only the scope you passed, runs tests and review, updates durable docs, and commits. |

### Supporting Skills

These provide discipline when the task needs it.

| Skill | What it does |
| --- | --- |
| `grilling` | Stops AI from asking ten questions at once: one decision, one recommendation, one answer. |
| `project-documentation` | Keeps each durable fact in one human-readable authority instead of duplicating it everywhere. |
| `tdd` | Tests behavior through stable public seams instead of testing implementation details. |
| `code-review` | Reviews Standards, Spec, and Documentation separately without changing your files. |

## Credit

Largely inspired by Matt Pocock's AIHero Skills workflow. This repository is MIT
licensed, independently maintained, and does not automatically sync upstream.
See [`LICENSE`](LICENSE).
