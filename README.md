# Agent Skills for AI Coding Agents

Give your coding agent a repeatable workflow for code review, debugging, research, planning, and more. This modular collection follows the open [Agent Skills format](https://agentskills.io): install one skill, a few, or the whole catalog with the [`skills` CLI](https://github.com/vercel-labs/skills), without cloning the repository. It works with compatible coding tools including Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode.

Each skill covers one kind of work, so you add the workflows you need instead of a one-size-fits-all bundle. A skill is a folder of instructions: a `SKILL.md` entry point, plus optional references and helper scripts. Its `SKILL.md` opens with a name and a "use when …" description, and that line is what your agent matches against. Install the skills you want, and the right one loads when a task fits.

**Choose a starting point:** [review code changes](skills/reviewing-code-changes/SKILL.md) · [debug a tricky failure](skills/systematic-debugging/SKILL.md) · [research with evidence](skills/research-with-evidence/SKILL.md) · [plan implementation work](skills/writing-implementation-plans/SKILL.md) · [browse all skills](#skills)

## Get started

The `skills` CLI requires Node.js 22.20 or later. Installs go into the current project unless you pass `-g`.

```bash
# see what is here, without installing
npx skills add m-hosseinpour/agent-skills --list

# choose the skills and agents interactively
npx skills add m-hosseinpour/agent-skills

# one skill, into this project, for OpenCode
npx skills add m-hosseinpour/agent-skills --skill reviewing-code-changes -a opencode
```

Check what landed with `npx skills list` (add `-g` for global installs).

Installation makes a real copy when every selected agent shares a skills directory — a single agent always does — and keeps one copy with symlinks when the agents use different directories; `--copy` always copies. Global installs go to each agent's configured directory, which some agents share and others keep separate. See the [supported agents and install paths](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

<details>
<summary>More commands</summary>

```bash
# several, for every agent detected in this project
npx skills add m-hosseinpour/agent-skills --skill structured-reasoning --skill writing-implementation-plans -a '*'

# everything, globally
npx skills add m-hosseinpour/agent-skills --skill '*' -g

# read a skill in a prompt without installing it
npx skills use m-hosseinpour/agent-skills@systematic-debugging
```

`npx skills update` refreshes the skills you installed from this repo.

</details>

## Skills

Each link opens the skill's `SKILL.md` — the instructions your agent reads.

| Skill | What it helps with |
| --- | --- |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | Manual-only where supported. Decide what belongs in always-loaded agent instructions and keep them maintainable. |
| [designing-persian-rtl-web-ui](skills/designing-persian-rtl-web-ui/SKILL.md) | Build and review Persian right-to-left web interfaces. |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | Decide when and how to delegate substantial work to parallel agents. |
| [research-with-evidence](skills/research-with-evidence/SKILL.md) | Research complex questions and produce evidence-backed findings. |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | Review code changes for defects, regressions, and requirement gaps. |
| [session-handoff](skills/session-handoff/SKILL.md) | Preserve decisions, evidence, and next steps across sessions. |
| [structured-reasoning](skills/structured-reasoning/SKILL.md) | Work through nontrivial questions, uncertainty, and trade-offs. |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | Find the cause of bugs before choosing a fix. |
| [targeted-proxy-access](skills/targeted-proxy-access/SKILL.md) | Route selected blocked domains through a user-configured proxy. |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | Manual-only where supported. Shorten oversized project instructions without losing essential guidance. |
| [understanding-code-changes](skills/understanding-code-changes/SKILL.md) | Explain unfamiliar diffs in their project context. |
| [validating-completed-tasks](skills/validating-completed-tasks/SKILL.md) | Check a completed task against its requirements and real acceptance paths. |
| [writing-code-review-reports](skills/writing-code-review-reports/SKILL.md) | Turn completed review findings into a clear author-facing report. |
| [writing-implementation-plans](skills/writing-implementation-plans/SKILL.md) | Create actionable plans for implementation and migrations. |
| [writing-skills](skills/writing-skills/SKILL.md) | Create or improve reusable agent skills. |
| [writing-task-briefs-and-guides](skills/writing-task-briefs-and-guides/SKILL.md) | Manual-only where supported. Turn a long task brief into an estimate-ready summary and full guide. |

**Manual-only skills** are never offered for automatic selection where the harness has a control for it: `disable-model-invocation: true` covers Claude Code, Cursor, GitHub Copilot, OpenCode, DeepSeek Harness, Pi, Qwen Code, Kimi Code and Droid, `triggers: [user]` covers Devin (including Windsurf), and `agents/openai.yaml` covers Codex. Ask for one by name — `/name` in most harnesses, `/skill:name` in Pi and Kimi Code, `$name` in Codex, or by name in OpenCode and DeepSeek Harness. Gemini CLI, Cline and harnesses without that control may still offer these skills automatically.

## Contributing

Suggestions, corrections, and new skills are welcome. [Open an issue](https://github.com/m-hosseinpour/agent-skills/issues/new) to discuss an idea, or send a pull request with the change and how you checked it.

Each skill is `skills/<name>/` with a `SKILL.md` entry point; optional `references/` hold guidance read on demand and `scripts/` hold helpers, so a skill stays self-contained and you install only what you need. Repository rules — the folder name must match the frontmatter `name`, and every new file must be linked from `SKILL.md` — are in [AGENTS.md](AGENTS.md). Use the [writing-skills](skills/writing-skills/SKILL.md) workflow to shape a skill, then confirm the installer discovers it with `npx skills add . --list`.

## Acknowledgements

Several skills started from other people's work, and some still adapt parts of it. Full file-level attribution and license texts are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

- [obra/superpowers](https://github.com/obra/superpowers) (MIT, © 2025 Jesse Vincent) — `structured-reasoning`, `systematic-debugging`, `writing-skills`, `dispatching-parallel-agents`, and `writing-implementation-plans`; `reviewing-code-changes` also borrows a few review-process points
- [PR Review Canvas](https://github.com/projekta2/pr-review-canvas) (MIT, © 2026 Alexandre Iglesias / Projekta2 Creative Studio) — the review checklist behind `reviewing-code-changes`
- [cursor/plugins](https://github.com/cursor/plugins) (MIT, © 2026 Cursor) — the quality rubric in `reviewing-code-changes` and the explanation approach in `understanding-code-changes`
- [wshobson/agents](https://github.com/wshobson/agents) (MIT, © 2024 Seth Hobson) — the language traps in `reviewing-code-changes`
- [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt) (Apache 2.0) — `designing-persian-rtl-web-ui` is my own skill, but its anti-default guidance and copywriting section follow the `frontend-design` skill

The [TinyFish integration skills](https://github.com/tinyfish-io/tinyfish-web-agent-integrations) also inspired operational ideas in `research-with-evidence`: freshness and access-context checks, structured entity collection, partial-batch handling, and server-job recovery. This guidance is independently written and requires no TinyFish tools; no upstream text or code is bundled for these additions.

If these workflows are useful, consider starring the repository — it helps others find the catalog.

## License

MIT — see [LICENSE](LICENSE).
