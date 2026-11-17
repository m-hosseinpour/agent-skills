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

Installs are symlinks by default, so there is one copy on disk; `--copy` puts a real file in place instead. Global installs are per agent: agents that share `~/.agents/skills` (Amp, Cline, Droid, Kilo, and others) are written there once, while agents with their own directory — `~/.claude/skills`, `~/.codex/skills` — get their own entry. `npx skills update` refreshes skills installed from this repo.

## Skills

| Skill | Use it when |
| --- | --- |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | deciding what belongs in the always-loaded global instruction file, or reorganizing it as it grows |
| [designing-persian-rtl-web-ui](skills/designing-persian-rtl-web-ui/SKILL.md) | building, changing, or checking a Persian (Farsi) web interface — RTL layout, typography, UI copy, numerals, responsive behavior, or dark mode — and before calling Persian UI work done; not RTL-only work in non-Persian interfaces |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | assessing multiple substantial, possibly independent workstreams when delegation is allowed, explicit parallel-agent requests, or a subagent running alongside the coordinator or other agents; not tiny multi-step tasks or parallel tool calls |
| [research-with-evidence](skills/research-with-evidence/SKILL.md) | multi-source or in-depth web research, evidence-backed comparisons, conflicting claims, or checking a research report's substantive claims and sources — not simple lookups, already-sufficient explanations, translation/editing without fact-checking, code-change review, or concrete software debugging |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | starting a review of a PR/MR, branch, commit range, patch, or uncommitted changes for defects, regressions, requirements, or readiness, including direct review-and-test instructions against a ticket or acceptance criteria; also before completing consequential behavior, contract, security, or persisted-data changes — not test-only runs, routine edits without a review request, unchanged-code audits, explanation-only walkthroughs, or formatting existing findings |
| [session-handoff](skills/session-handoff/SKILL.md) | preparing context for another session, agent, or person, preserving ongoing work before reset/compaction, or resuming a supplied handoff — not routine status, finished-work summaries, short delegation briefs, or author-facing review reports |
| [structured-reasoning](skills/structured-reasoning/SKILL.md) | any request requiring substantial reasoning, evidence synthesis, resolving uncertainty, planning, or meaningful trade-offs, regardless of domain or output; also explicit brainstorming, stress-testing an idea or decision, or a guided interview to clarify a plan, but not simple factual lookups or obvious mechanical tasks |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | investigating or fixing bugs, regressions, flaky tests, build/deployment failures, performance problems, or incorrect output; also explaining why a failure occurred — not failure-free explanation, feature design, or an already-verified correction with no new uncertainty |
| [targeted-proxy-access](skills/targeted-proxy-access/SKILL.md) | a page fetch fails because the site is blocked or geo-restricted — from an MCP server, a browser, or the harness's own built-in reader — or a routed domain still fails and the gateway, routed domains, or client wiring needs checking; only chosen domains go through your own VLESS/Trojan configs |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | a project instruction file (`CLAUDE.md`, `AGENTS.md`) has outgrown what a session can hold |
| [understanding-code-changes](skills/understanding-code-changes/SKILL.md) | understanding an unfamiliar PR/MR, branch, or diff in its project context — for explanation, maintenance, or orientation before review, rather than a verdict |
| [validating-completed-tasks](skills/validating-completed-tasks/SKILL.md) | validating completed work for task acceptance, initially or after prior review and revisions — whether implementation or a research/security report is correct, complete, and trustworthy, including real acceptance/edge-case tests and fix verification against earlier findings/current requirements; not defect-only or merge-readiness review without task-completion validation even if a ticket is cited, test-only execution, settled-report writing, explanation, implementation, or fixes |
| [writing-code-review-reports](skills/writing-code-review-reports/SKILL.md) | writing a code-review report from completed results supplied by others or produced in the current task, including the reporting stage of a review-and-report request, short reports in chat, zero-findings reports, editing, translation, or consolidation — not code inspection, fixes, feedback replies, or a brief findings-only reply when no report is requested |
| [writing-implementation-plans](skills/writing-implementation-plans/SKILL.md) | writing, reviewing, or updating an implementation plan; coordinating substantial cross-component or high-risk work, migrations, or multi-session handoffs; checking a potentially stale plan on resumption — not routine edits without a plan request or execution of a current settled plan |
| [writing-skills](skills/writing-skills/SKILL.md) | creating, reviewing, or improving an agent skill; capturing a repeatable workflow; diagnosing missed/unwanted loading; or changing references/helpers that affect use — not installation, applying existing skills, format explanations, or meaning-preserving mechanical edits |
| [writing-task-briefs-and-guides](skills/writing-task-briefs-and-guides/SKILL.md) | a long task description needs a concise team-facing version for estimation plus a full standalone developer guide |

### Renamed skills

The following names have changed. The rename itself preserved their descriptions and
workflows; `designing-persian-rtl-web-ui` has since narrowed its description to match
its Persian-specific guidance, excluding RTL-only work in non-Persian interfaces:

| Former name | Current name |
| --- | --- |
| `brainstorming` | `structured-reasoning` |
| `understanding-a-merge-request` | `understanding-code-changes` |
| `writing-plans` | `writing-implementation-plans` |
| `splitting-task-descriptions` | `writing-task-briefs-and-guides` |
| `proxy-tunnel` | `targeted-proxy-access` |
| `designing-persian-web-ui` | `designing-persian-rtl-web-ui` |

Use the current names in install commands, prompts, and instruction files. Existing
installations are not retargeted automatically: reinstall the renamed skills in the
same project/global scope and for the same agents, for example
`npx skills add m-hosseinpour/agent-skills --skill structured-reasoning -g`.
Check old symlinks before removing them, and preserve copied skills with local edits.

`targeted-proxy-access` keeps the gateway's `proxy-tunnel-exec` command,
`PROXY_TUNNEL_*` settings, `proxy-tunnel` service, and existing data directories.
Installed launcher/service paths may still point into the former skill folder;
follow its [upgrade guide](skills/targeted-proxy-access/references/setup.md#upgrading-after-the-skill-rename)
to refresh them. Renaming the catalog does not modify your agent configs or running services.

## How the catalog is organized

Each skill lives in `skills/<skill-name>/` with a `SKILL.md` entry point. Optional `references/` hold supporting guidance and `scripts/` hold helpers. This keeps each workflow self-contained and lets you install only what you need.

## Contributing

Suggestions, corrections, and new skills are welcome. Open an issue to discuss an idea, or send a pull request with the change and how you checked it.

When adding or rewriting a skill:

- Keep the folder name and frontmatter `name` identical.
- Use the `writing-skills` workflow in this catalog to shape and check the skill.
- Confirm the installer discovers it with `npx skills add . --list`.
- Link any new supporting files from the skill's `SKILL.md`.

If a skill is renamed, existing installs are not retargeted automatically. See [Renamed skills](#renamed-skills) for upgrade guidance.

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
