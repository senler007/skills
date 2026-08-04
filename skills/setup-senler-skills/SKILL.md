---
name: setup-senler-skills
description: Configure a repository to use the Senler skills workflow. Use when the user explicitly asks to set up Senler skills, choose a GitHub/local/custom issue tracker, or establish project-documentation paths and agent guidance.
---

# Setup Senler Skills

Configure the repository once without replacing conventions that already work.
This skill is explicit-only: never run it merely because another workflow skill
is being used.

## Inspect the repository

Read only enough context to locate:

- the repository root and Git remote;
- existing agent instruction files such as `AGENTS.md` or `CLAUDE.md`;
- existing project, glossary, design, architecture, ADR, and tracker documentation;
- any existing daily development-record convention;
- the established documentation directory casing and project language.

Existing paths, casing, terminology, and language take precedence over the
defaults in this skill. Do not create parallel files for roles that already have
an authoritative owner.

## Confirm the configuration

Summarize what was found, then confirm choices that cannot be inferred safely:

1. **Tracker mode.** Recommend GitHub when the Git remote identifies a GitHub
   repository; otherwise recommend local. Also support a custom tracker.
2. **Agent instruction file.** Update an existing instruction file. If none
   exists, ask before creating one and recommend `AGENTS.md` for Codex-first use.
3. **Project-document locations.** Reuse existing owners. For missing roles,
   propose `PROJECT.md`, `docs/Glossary.md`, `docs/Design/`,
   `docs/Architecture.md`, and `docs/adr/`, adapting directory casing to the
   repository.
4. **Development record.** Reuse an existing dated task journal. When none exists,
   propose `docs/DevelopmentRecord/YYYY-MM-DD.md`, adapting directory casing to
   the repository.
5. **Document language.** Infer it from durable project documentation and ask
   only when mixed usage leaves the answer ambiguous.

Show the exact files and substantive configuration before writing, then wait for
the user's explicit approval. Do not create empty project, glossary,
architecture, ADR, or design documents during setup.

## Write the configuration

Use the applicable tracker reference:

- GitHub: [references/issue-tracker-github.md](references/issue-tracker-github.md)
- Local: [references/issue-tracker-local.md](references/issue-tracker-local.md)
- Custom: [references/issue-tracker-custom.md](references/issue-tracker-custom.md)

Create or update two small agent-facing configuration files in the repository's
existing agent-documentation directory. Prefer `docs/agents/` only when the
repository has no established location:

- `issue-tracker.md`, based on the selected tracker reference;
- `project-docs.md`, based on
  [references/project-docs.md](references/project-docs.md).

Add a concise `## Senler skills` section to the confirmed agent instruction file.
It should tell future agents where those two configurations live and to follow
them, including the configured daily development record. Merge with an existing
section instead of duplicating it.

Record actual repository-specific values, not unresolved placeholders. Avoid
copying the detailed document-role rules into multiple files; the configuration
should map roles to paths and defer maintenance behavior to
`$project-documentation`.

## Finish

Use `$project-documentation` to record the completed setup in the configured
development record.

Report the tracker mode, configuration files, instruction file, document
language, development-record path, reused authorities, and proposed-but-uncreated
document paths. Call out any ambiguity left for the user. Do not start a Spec or
create tracker work as a side effect of setup.
