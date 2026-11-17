# Agent Skills for AI Coding Agents

Give your coding agent a repeatable workflow for code review, debugging, research, planning, and more. This modular collection follows the open [Agent Skills format](https://agentskills.io): install one skill, a few, or the whole catalog with the [`skills` CLI](https://github.com/vercel-labs/skills), without cloning the repository. It is designed for compatible coding tools including Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode.

Each skill focuses on a specific kind of work, so you can add a practical workflow when you need it instead of installing a one-size-fits-all bundle.

If these workflows are useful, consider starring the repository or opening an issue with what you would like to see next.

**Choose a starting point:** [review code changes](skills/reviewing-code-changes/SKILL.md) · [debug a tricky failure](skills/systematic-debugging/SKILL.md) · [research with evidence](skills/research-with-evidence/SKILL.md) · [plan implementation work](skills/writing-implementation-plans/SKILL.md) · [browse all skills](#skills)

## Get started

Install interactively, or choose a skill and agent explicitly. Skills can be installed per project or globally.

```bash
# see what is here, without installing
npx skills add m-hosseinpour/agent-skills --list

# choose the skills and agents interactively
npx skills add m-hosseinpour/agent-skills

# one skill, into this project, for OpenCode
npx skills add m-hosseinpour/agent-skills --skill reviewing-code-changes -a opencode

# several, for every agent detected in this project
npx skills add m-hosseinpour/agent-skills --skill structured-reasoning --skill writing-implementation-plans -a '*'

# everything, globally
npx skills add m-hosseinpour/agent-skills --skill '*' -g

# read a skill in a prompt without installing it
npx skills use m-hosseinpour/agent-skills@systematic-debugging
```

Installs are symlinks by default, so there is one copy on disk; `--copy` puts a real file in place instead. Global installs use each agent's configured skills directory; some agents share a directory, while others use their own. See the [`skills` CLI supported agents and install paths](https://github.com/vercel-labs/skills/blob/main/docs/agents.md). `npx skills update` refreshes skills installed from this repo.

## Skills

| Skill | What it helps with |
| --- | --- |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | Decide what belongs in always-loaded agent instructions and keep them maintainable. |
| [designing-persian-rtl-web-ui](skills/designing-persian-rtl-web-ui/SKILL.md) | Build and review Persian right-to-left web interfaces. |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | Decide when and how to delegate substantial work to parallel agents. |
| [research-with-evidence](skills/research-with-evidence/SKILL.md) | Research complex questions and produce evidence-backed findings. |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | Review code changes for defects, regressions, and requirement gaps. |
| [session-handoff](skills/session-handoff/SKILL.md) | Preserve decisions, evidence, and next steps across sessions. |
| [structured-reasoning](skills/structured-reasoning/SKILL.md) | Work through nontrivial questions, uncertainty, and trade-offs. |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | Find the cause of bugs before choosing a fix. |
| [targeted-proxy-access](skills/targeted-proxy-access/SKILL.md) | Route selected blocked domains through a user-configured proxy. |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | Shorten oversized project instructions without losing essential guidance. |
| [understanding-code-changes](skills/understanding-code-changes/SKILL.md) | Explain unfamiliar diffs in their project context. |
| [validating-completed-tasks](skills/validating-completed-tasks/SKILL.md) | Check a completed task against its requirements and real acceptance paths. |
| [writing-code-review-reports](skills/writing-code-review-reports/SKILL.md) | Turn completed review findings into a clear author-facing report. |
| [writing-implementation-plans](skills/writing-implementation-plans/SKILL.md) | Create actionable plans for implementation and migrations. |
| [writing-skills](skills/writing-skills/SKILL.md) | Create or improve reusable agent skills. |
| [writing-task-briefs-and-guides](skills/writing-task-briefs-and-guides/SKILL.md) | Turn a long task brief into an estimate-ready summary and full guide. |

## How the catalog is organized

Each skill lives in `skills/<skill-name>/` with a `SKILL.md` entry point. Optional `references/` hold supporting guidance and `scripts/` hold helpers. This keeps each workflow self-contained and lets you install only what you need.

## Contributing

Suggestions, corrections, and new skills are welcome. [Open an issue](https://github.com/m-hosseinpour/agent-skills/issues/new/choose) to discuss an idea, or send a pull request with the change and how you checked it.

When adding or rewriting a skill:

- Keep the folder name and frontmatter `name` identical.
- Use the `writing-skills` workflow in this catalog to shape and check the skill.
- Confirm the installer discovers it with `npx skills add . --list`.
- Link any new supporting files from the skill's `SKILL.md`.

## Acknowledgements

Several skills started from someone else's work, and a few still carry it. Full license texts are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

**obra/superpowers** ([MIT](https://github.com/obra/superpowers), © 2025 Jesse Vincent) — five skills began as copies from that repository and have been rewritten since:

- `structured-reasoning` (originally `brainstorming`) — began with the upstream subject; the former upstream visual-companion scripts and guide have been removed
- `systematic-debugging` — its tracing, safeguards, and waiting guides in `references/`, and helper examples in `scripts/`, have been rewritten from the original supporting files
- `writing-skills` — rewritten descendants in `references/`: `anthropic-best-practices.md`, `discipline-wording.md` (formerly `persuasion-principles.md`), `testing-skills.md` (formerly `testing-skills-with-subagents.md`), `instruction-files-testing.md` (formerly the example test plan), and `graphviz-conventions.dot`; `scripts/render-graphs.mjs` replaces the original renderer; evaluation scenarios are new
- `dispatching-parallel-agents` — the name and the subject, nothing else
- `writing-implementation-plans` (originally `writing-plans`) — the subject, nothing else

`reviewing-code-changes` also borrows a few review-process points from `requesting-code-review`.

**PR Review Canvas** ([MIT](https://github.com/projekta2/pr-review-canvas), © 2026 Alexandre Iglesias / Projekta2 Creative Studio) — `reviewing-code-changes` is built on its review checklist: `references/checklist.md` keeps the categories and item numbering, reworded, for 35 of the 51 items.

**cursor/plugins** ([MIT](https://github.com/cursor/plugins), © 2026 Cursor) — the rubric in `reviewing-code-changes/references/quality-bar.md` is distilled from its `thermo-nuclear-code-quality-review` skill, and three checklist items come from its `thermos` plugin. `understanding-code-changes` adapts the comprehension-first grouping, pseudocode, traces, callouts, and choice of representation from [its `pr-review-canvas` skill](https://github.com/cursor/plugins/tree/main/pr-review-canvas), with independently written guidance for portable Markdown and project-context investigation rather than the Canvas SDK.

**wshobson/agents** ([MIT](https://github.com/wshobson/agents), © 2024 Seth Hobson) — the language traps in `reviewing-code-changes/references/patterns.md` adapt its `code-review-excellence` skill.

**anthropics/skills** ([Apache 2.0](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt)) — `designing-persian-rtl-web-ui` is my own skill, but its anti-default guidance and copywriting section follow the `frontend-design` skill.

## License

MIT — see [LICENSE](LICENSE).
