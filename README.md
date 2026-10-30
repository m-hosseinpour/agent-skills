# Agent Skills

A collection of [agent skills](https://agentskills.io): plain folders, each with a `SKILL.md`, in the open Agent Skills format. They install with the [`skills` CLI](https://github.com/vercel-labs/skills) and work with Claude Code, Codex, Cursor, Copilot, Gemini CLI, `dsh`, and any other agent that reads the same format — one copy of the content, installed where each agent looks.

## Install

Cloning is not required. Ask for one skill, a few, or all of them, per project or globally.

```bash
# see what is here, without installing
npx skills add m-hosseinpour/agent-skills --list

# choose the skills and agents interactively
npx skills add m-hosseinpour/agent-skills

# one skill, into this project, for OpenCode
npx skills add m-hosseinpour/agent-skills --skill reviewing-code-changes -a opencode

# several, for every agent detected in this project
npx skills add m-hosseinpour/agent-skills --skill brainstorming --skill writing-plans -a '*'

# everything, globally
npx skills add m-hosseinpour/agent-skills --skill '*' -g

# read a skill in a prompt without installing it
npx skills use m-hosseinpour/agent-skills@systematic-debugging
```

Installs are symlinks by default, so there is one copy on disk; `--copy` puts a real file in place instead. Global installs are per agent: agents that share `~/.agents/skills` (Amp, Cline, Droid, Kilo, and others) are written there once, while agents with their own directory — `~/.claude/skills`, `~/.codex/skills` — get their own entry. `npx skills update` refreshes skills installed from this repo.

## Skills

| Skill | Use it when |
| --- | --- |
| [brainstorming](skills/brainstorming/SKILL.md) | the goal, constraints, or approach are unclear and need to become a design the user can correct before building |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | deciding what belongs in the always-loaded global instruction file, or reorganizing it as it grows |
| [designing-persian-web-ui](skills/designing-persian-web-ui/SKILL.md) | building or changing a Persian (Farsi) or right-to-left web interface — direction, layout, numerals, UI copy — and before calling Persian UI work done |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | planning two or more subagents that will run at the same time |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | reviewing a diff, branch, or merge request before merge, or giving an independent second opinion |
| [splitting-task-descriptions](skills/splitting-task-descriptions/SKILL.md) | a long task description needs a concise team-facing version plus a full developer guide |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | a bug, test failure, build error, or performance problem needs a cause found before a fix |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | a project instruction file (`CLAUDE.md`, `AGENTS.md`) has outgrown what a session can hold |
| [understanding-a-merge-request](skills/understanding-a-merge-request/SKILL.md) | you have to maintain or explain someone else's change rather than judge it |
| [writing-plans](skills/writing-plans/SKILL.md) | a large, risky, or multi-session change needs a durable implementation plan before coding |
| [writing-skills](skills/writing-skills/SKILL.md) | creating a skill or making a substantive change to an existing one |

## Layout

```
skills/
└── <skill-name>/
    ├── SKILL.md      # required: name + description frontmatter, then the instructions
    ├── references/   # optional: detail the agent reads only when the skill sends it there
    └── scripts/      # optional: helpers the skill runs instead of reading
```

The format is progressive: only the frontmatter of every skill is preloaded, `SKILL.md` is read when a skill triggers, and anything else is read on demand. Keeping detail in `references/` is what makes that work.

## Working in this repo

- **The folder name is the skill name.** Frontmatter `name` must match it exactly; installers index skills by that pair.
- **Descriptions are the trigger.** Say when to use the skill, not what it contains — an agent decides to load it from the description alone.
- **Adding or rewriting a skill:** use the `writing-skills` skill in this repo, then confirm discovery with `npx skills add . --list`.
- **Changing a skill:** the installed copies are symlinks to this checkout, so an edit here — or `git pull` on a machine that installed it — is live for every agent already linking it.

## Acknowledgements

Several skills started from someone else's work, and a few still carry it. Full license texts are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

**obra/superpowers** ([MIT](https://github.com/obra/superpowers), © 2025 Jesse Vincent) — five skills began as copies of the same-named skills and have been rewritten since:

- `brainstorming` — the visual-companion scripts and `visual-companion.md`
- `systematic-debugging` — `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, `condition-based-waiting-example.ts`, `find-polluter.sh`
- `writing-skills` — `anthropic-best-practices.md`, `persuasion-principles.md`, `testing-skills-with-subagents.md`, `examples/instruction-files-testing.md`, `graphviz-conventions.dot`, `render-graphs.js`
- `dispatching-parallel-agents`, `writing-plans` — the name and the subject, nothing else

`reviewing-code-changes` also borrows a few review-process points from `requesting-code-review`.

**PR Review Canvas** ([MIT](https://github.com/projekta2/pr-review-canvas), © 2026 Alexandre Iglesias / Projekta2 Creative Studio) — `reviewing-code-changes` is built on its review checklist: `references/checklist.md` keeps the categories and item numbering, reworded, for 35 of the 51 items. `understanding-a-merge-request` is inspired by the [Cursor `pr-review-canvas` skill](https://github.com/cursor/plugins/tree/main/pr-review-canvas) (MIT, © 2026 Cursor); none of its text was copied.

**cursor/plugins** ([MIT](https://github.com/cursor/plugins), © 2026 Cursor) — the rubric in `reviewing-code-changes/references/quality-bar.md` is distilled from its `thermo-nuclear-code-quality-review` skill, and three checklist items come from its `thermos` plugin.

**wshobson/agents** ([MIT](https://github.com/wshobson/agents), © 2024 Seth Hobson) — the language traps in `reviewing-code-changes/references/patterns.md` adapt its `code-review-excellence` skill.

**anthropics/skills** ([Apache 2.0](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt)) — `designing-persian-web-ui` is my own skill, but its anti-default guidance and copywriting section follow the `frontend-design` skill.

## License

MIT — see [LICENSE](LICENSE).
