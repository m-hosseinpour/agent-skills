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
| [brainstorming](skills/brainstorming/SKILL.md) | before nontrivial implementation, even with clear requirements, or when exploring ideas or a design; skip mechanical edits and explanation-only requests, and diagnose bugs first |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | deciding what belongs in the always-loaded global instruction file, or reorganizing it as it grows |
| [designing-persian-web-ui](skills/designing-persian-web-ui/SKILL.md) | building or changing a Persian (Farsi) or right-to-left web interface — direction, layout, numerals, UI copy — and before calling Persian UI work done |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | assessing multiple substantial, possibly independent workstreams when delegation is allowed, explicit parallel-agent requests, or a subagent running alongside the coordinator or other agents; not tiny multi-step tasks or parallel tool calls |
| [proxy-tunnel](skills/proxy-tunnel/SKILL.md) | a fetch fails because the site is blocked or geo-restricted, and only that domain should go through your own VLESS/Trojan configs |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | reviewing a PR/MR, branch, patch, or uncommitted changes for defects, regressions, requirements, or readiness; also before completing consequential behavior, contract, security, or persisted-data changes — not routine edits without a review request, unchanged-code audits, explanation-only walkthroughs, or formatting existing findings |
| [splitting-task-descriptions](skills/splitting-task-descriptions/SKILL.md) | a long task description needs a concise team-facing version plus a full developer guide |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | a bug, test failure, build error, or performance problem needs a cause found before a fix |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | a project instruction file (`CLAUDE.md`, `AGENTS.md`) has outgrown what a session can hold |
| [understanding-a-merge-request](skills/understanding-a-merge-request/SKILL.md) | understanding an unfamiliar MR, branch, or diff in its project context — for explanation, maintenance, or orientation before review, rather than a verdict |
| [writing-code-review-reports](skills/writing-code-review-reports/SKILL.md) | existing review results need an author-facing handoff, revision, faithful translation, or consolidation, including zero-findings reports and the reporting stage after inspection — not code inspection, fixes, feedback replies, or a brief review reply without a requested handoff |
| [writing-plans](skills/writing-plans/SKILL.md) | writing, reviewing, or updating an implementation plan; coordinating substantial cross-component or high-risk work, migrations, or multi-session handoffs; checking a potentially stale plan on resumption — not routine edits without a plan request or execution of a current settled plan |
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

`brainstorming` is a design checkpoint for nontrivial implementation, not an automatic interview or approval gate. It checks current evidence even when requirements are clear, asks only about consequential unresolved choices, and proceeds without re-approving settled decisions when implementation is already requested. This is broader than using it only for vague requests, but does not require a design document or visual preview for every task.

For visual decisions, its optional [visual guide](skills/brainstorming/references/visual-decisions.md) uses diagrams, images, or static HTML with an existing preview tool. The former custom browser-companion server and scripts have been removed: there is no companion launch command, automatic click capture, or dedicated live-reload service. Feedback stays in the conversation. Existing `.brainstorm/` artifacts are not removed by this change.

Use a separate skill when the task has its own trigger, not merely more detail within a parent workflow. For example, `reviewing-code-changes` owns inspection and findings; `writing-code-review-reports` owns the handoff document once those results exist. A request for both uses them at successive stages; a brief review reply does not require the reporting skill.

`writing-code-review-reports` distinguishes a focused author handoff from a faithful translation/edit and a consolidation of reviewer outputs. Full translations retain requested nits and optional suggestions; composed handoffs default to material findings and all confirmed extras. It preserves code-state provenance, conflicting claims, portable verification evidence, and evidence-bounded verdicts without reopening review. Its optional [Persian guide](skills/writing-code-review-reports/references/persian-report.md) provides terminology and an adaptable template; the [consolidation guide](skills/writing-code-review-reports/references/consolidation-and-evidence.md) handles duplicates, revisions, and supplied check results. The maintainer-only [evaluation scenarios](skills/writing-code-review-reports/references/evaluation-scenarios.md) separate metadata selection from generated-report quality.

`reviewing-code-changes` also applies at a pre-completion checkpoint for consequential changes, without requiring an explicit review request or imposing a full sweep on tiny edits. It pins the comparison and relevant code state, traces affected behavior through unchanged contracts, reports evidenced findings by impact, and distinguishes missing evidence from confirmed defects. Its references are loaded at the relevant decision: [scope and evidence](skills/reviewing-code-changes/references/scope-and-evidence.md), requirements, broader risk prompts, contextual patterns, structural design, or an allowed delegated review. The optional [evaluation scenarios](skills/reviewing-code-changes/references/evaluation-scenarios.md) check metadata selection separately from application; passing an installer listing is not proof of automatic loading.

`dispatching-parallel-agents` helps assess opportunities before a worker split is chosen; loading it does not require delegation. It weighs setup and integration cost, assigns ownership of files and shared mutable resources, and covers changed contracts, partial failures, and combined verification. One subagent working alongside the coordinator counts as parallel work. Its optional [evaluation scenarios](skills/dispatching-parallel-agents/references/evaluation-scenarios.md) separate trigger discovery from coordination decisions; they are not a required dispatch ritual.

`writing-plans` focuses on a usable plan, not a complete execution framework. It checks current project evidence, bounds unresolved questions, connects task dependencies to observable checks, and updates affected completed work when a contract changes. An explicit small planning request may need only a chat checklist; a short but risky migration may need a durable plan. Its optional [plan template](skills/writing-plans/references/plan-template.md), [separate design record](skills/writing-plans/references/spec-template.md), and [read-only reviewer prompt](skills/writing-plans/references/plan-document-reviewer-prompt.md) are linked at the decisions where they help, without requiring extra documents, workers, or repeated approval. The maintainer [evaluation scenarios](skills/writing-plans/references/evaluation-scenarios.md) distinguish metadata selection from plan quality; neither installer listing nor a simulation guarantees automatic loading or successful implementation.

`understanding-a-merge-request` produces an adaptive Markdown walkthrough, not a merge verdict: it connects the change to relevant unchanged code, explains before/after behavior or responsibility shifts, and selects useful views such as flow maps, example traces, contract tables, or rollout sequences. Short explanations can stay in chat; substantial walkthroughs can be saved alongside the code. It requires no Cursor Canvas or particular hosting provider.

## Working in this repo

- **The folder name is the skill name.** Frontmatter `name` must match it exactly; installers index skills by that pair.
- **Descriptions are the trigger.** Say when to use the skill, not what it contains — an agent decides to load it from the description alone.
- **Adding or rewriting a skill:** use the `writing-skills` skill in this repo, then confirm discovery with `npx skills add . --list`.
- **Changing a skill:** the installed copies are symlinks to this checkout, so an edit here — or `git pull` on a machine that installed it — is live for every agent already linking it.

## Acknowledgements

Several skills started from someone else's work, and a few still carry it. Full license texts are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

**obra/superpowers** ([MIT](https://github.com/obra/superpowers), © 2025 Jesse Vincent) — five skills began as copies of the same-named skills and have been rewritten since:

- `brainstorming` — the name and the subject; the former upstream visual-companion scripts and guide have been removed
- `systematic-debugging` — `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, `condition-based-waiting-example.ts`, `find-polluter.sh`
- `writing-skills` — `anthropic-best-practices.md`, `persuasion-principles.md`, `testing-skills-with-subagents.md`, `examples/instruction-files-testing.md`, `graphviz-conventions.dot`, `render-graphs.js`
- `dispatching-parallel-agents`, `writing-plans` — the name and the subject, nothing else

`reviewing-code-changes` also borrows a few review-process points from `requesting-code-review`.

**PR Review Canvas** ([MIT](https://github.com/projekta2/pr-review-canvas), © 2026 Alexandre Iglesias / Projekta2 Creative Studio) — `reviewing-code-changes` is built on its review checklist: `references/checklist.md` keeps the categories and item numbering, reworded, for 35 of the 51 items.

**cursor/plugins** ([MIT](https://github.com/cursor/plugins), © 2026 Cursor) — the rubric in `reviewing-code-changes/references/quality-bar.md` is distilled from its `thermo-nuclear-code-quality-review` skill, and three checklist items come from its `thermos` plugin. `understanding-a-merge-request` adapts the comprehension-first grouping, pseudocode, traces, callouts, and choice of representation from [its `pr-review-canvas` skill](https://github.com/cursor/plugins/tree/main/pr-review-canvas), with independently written guidance for portable Markdown and project-context investigation rather than the Canvas SDK.

**wshobson/agents** ([MIT](https://github.com/wshobson/agents), © 2024 Seth Hobson) — the language traps in `reviewing-code-changes/references/patterns.md` adapt its `code-review-excellence` skill.

**anthropics/skills** ([Apache 2.0](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt)) — `designing-persian-web-ui` is my own skill, but its anti-default guidance and copywriting section follow the `frontend-design` skill.

## License

MIT — see [LICENSE](LICENSE).
