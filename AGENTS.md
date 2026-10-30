# Repository rules

This repo is a catalog of agent skills, not an application. Each folder under `skills/` is one skill.

- **Folder name equals frontmatter `name`.** Installers index skills by that pair; a mismatch makes the skill undiscoverable.
- **`skills/<name>/SKILL.md` is the only required file.** Put detail the agent should read on demand in `references/`; put helper code in `scripts/`.
- **Write or rewrite skills with the `writing-skills` skill**, and keep descriptions as triggers ("use when …") rather than summaries.
- **Verify before committing:** `npx skills add . --list` must discover the skill, and any new files must be referenced from `SKILL.md` (or be runtime artifacts the skill creates).
- **Do not commit secrets or machine-specific absolute paths.** Skills are copied into other people's agents, so they must work from the skill folder alone.
