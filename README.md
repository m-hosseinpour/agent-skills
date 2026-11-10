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
| [brainstorming](skills/brainstorming/SKILL.md) | any request requiring substantial reasoning, evidence synthesis, resolving uncertainty, planning, or meaningful trade-offs, regardless of domain or output; also explicit brainstorming, but not simple factual lookups or obvious mechanical tasks |
| [curating-global-instructions](skills/curating-global-instructions/SKILL.md) | deciding what belongs in the always-loaded global instruction file, or reorganizing it as it grows |
| [designing-persian-web-ui](skills/designing-persian-web-ui/SKILL.md) | building or changing a Persian (Farsi) or right-to-left web interface — direction, layout, numerals, UI copy — and before calling Persian UI work done |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | assessing multiple substantial, possibly independent workstreams when delegation is allowed, explicit parallel-agent requests, or a subagent running alongside the coordinator or other agents; not tiny multi-step tasks or parallel tool calls |
| [proxy-tunnel](skills/proxy-tunnel/SKILL.md) | a fetch fails because the site is blocked or geo-restricted, and only that domain should go through your own VLESS/Trojan configs |
| [research-with-evidence](skills/research-with-evidence/SKILL.md) | multi-source research, evidence-backed comparisons, conflicting claims, or recommendations dependent on external evidence — not simple lookups, already-sufficient explanations, code-change review, or concrete software debugging |
| [reviewing-code-changes](skills/reviewing-code-changes/SKILL.md) | starting a review of a PR/MR, branch, commit range, patch, or uncommitted changes for defects, regressions, requirements, or readiness, including direct review-and-test instructions against a ticket or acceptance criteria; also before completing consequential behavior, contract, security, or persisted-data changes — not test-only runs, routine edits without a review request, unchanged-code audits, explanation-only walkthroughs, or formatting existing findings |
| [session-handoff](skills/session-handoff/SKILL.md) | preparing context for another session, agent, or person, preserving ongoing work before reset/compaction, or resuming a supplied handoff — not routine status, finished-work summaries, short delegation briefs, or author-facing review reports |
| [splitting-task-descriptions](skills/splitting-task-descriptions/SKILL.md) | a long task description needs a concise team-facing version plus a full developer guide |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | investigating or fixing bugs, regressions, flaky tests, build/deployment failures, performance problems, or incorrect output; also explaining why a failure occurred — not failure-free explanation, feature design, or an already-verified correction with no new uncertainty |
| [trimming-project-instructions](skills/trimming-project-instructions/SKILL.md) | a project instruction file (`CLAUDE.md`, `AGENTS.md`) has outgrown what a session can hold |
| [understanding-a-merge-request](skills/understanding-a-merge-request/SKILL.md) | understanding an unfamiliar MR, branch, or diff in its project context — for explanation, maintenance, or orientation before review, rather than a verdict |
| [writing-code-review-reports](skills/writing-code-review-reports/SKILL.md) | writing a code-review report from completed results supplied by others or produced in the current task, including the reporting stage of a review-and-report request, short reports in chat, zero-findings reports, editing, translation, or consolidation — not code inspection, fixes, feedback replies, or a brief findings-only reply when no report is requested |
| [writing-plans](skills/writing-plans/SKILL.md) | writing, reviewing, or updating an implementation plan; coordinating substantial cross-component or high-risk work, migrations, or multi-session handoffs; checking a potentially stale plan on resumption — not routine edits without a plan request or execution of a current settled plan |
| [writing-skills](skills/writing-skills/SKILL.md) | creating, reviewing, or improving an agent skill; capturing a repeatable workflow; diagnosing missed/unwanted loading; or changing references/helpers that affect use — not installation, applying existing skills, format explanations, or meaning-preserving mechanical edits |

## Layout

```
skills/
└── <skill-name>/
    ├── SKILL.md      # required: name + description frontmatter, then the instructions
    ├── references/   # optional: detail the agent reads only when the skill sends it there
    └── scripts/      # optional: helpers the skill runs instead of reading
```

The format is progressive: only the frontmatter of every skill is preloaded, `SKILL.md` is read when a skill triggers, and anything else is read on demand. Keeping detail in `references/` is what makes that work.

`brainstorming` is a domain-independent thinking checkpoint for any nontrivial request, not only implementation or design. Complexity comes from the reasoning, evidence, uncertainty, constraints, and consequences involved, not from the subject or output format. Substantial explanations and investigations qualify even when no action is requested. Loading does not require an interview, approval gate, plan, or process preamble: ask only for user input that could change the result, use relevant specialized methods alongside it, and keep recommendations separate from permission to act. Simple direct answers and obvious mechanical tasks do not need the checkpoint unless brainstorming is explicitly requested.

`systematic-debugging` keeps diagnosis separate from speculative repair, explanation-only requests, and authorized incident mitigation. Its optional guides are linked at the relevant decision: [root-cause tracing and test order](skills/systematic-debugging/references/root-cause-tracing.md), [condition-based waiting](skills/systematic-debugging/references/condition-based-waiting.md), and [distinct boundary safeguards](skills/systematic-debugging/references/defense-in-depth.md). Helpers now live in `scripts/`: the dependency-free waiting example replaces the former project-specific imports; the polluter scan requires an explicit runner after `--` as separate arguments, for example `bash <skill-dir>/scripts/find-polluter.sh 'unexpected.db' 'tests/**/test_*.py' -- uv run pytest '{}'`. It preserves output/status and artifacts, but does not isolate tests or reproduce every shared-process failure. The maintainer [evaluation scenarios](skills/systematic-debugging/references/evaluation-scenarios.md) separate metadata selection from behavior; neither installer discovery nor a simulation guarantees automatic loading.

For visual understanding or comparison, brainstorming's optional [visual guide](skills/brainstorming/references/visual-decisions.md) uses diagrams, images, or static HTML with an existing preview tool. The former custom browser-companion server and scripts have been removed: there is no companion launch command, automatic click capture, or dedicated live-reload service. Feedback stays in the conversation. Existing `.brainstorm/` artifacts are not removed by this change.

Use a separate skill when the task has its own trigger, not merely more detail within a parent workflow. For example, `reviewing-code-changes` owns inspection and findings; `writing-code-review-reports` owns a requested code-review report once those results exist, whether supplied by others or produced in the current task. A request for both uses them at successive stages: before drafting the report, load the reporting skill if available and not already loaded. A requested report may be short and delivered in chat; a brief findings-only reply when no report is requested does not require the reporting skill or a report file.

`writing-code-review-reports` distinguishes a focused author handoff from a faithful translation/edit and a consolidation of reviewer outputs. Full translations retain requested nits and optional suggestions; composed handoffs default to material findings and all confirmed extras. It preserves code-state provenance, conflicting claims, portable verification evidence, and evidence-bounded verdicts without reopening review. Its optional [Persian guide](skills/writing-code-review-reports/references/persian-report.md) provides terminology and an adaptable template; the [consolidation guide](skills/writing-code-review-reports/references/consolidation-and-evidence.md) handles duplicates, revisions, and supplied check results. The maintainer-only [evaluation scenarios](skills/writing-code-review-reports/references/evaluation-scenarios.md) separate metadata selection from generated-report quality.

`reviewing-code-changes` also applies at a pre-completion checkpoint for consequential changes, without requiring an explicit review request or imposing a full sweep on tiny edits. It pins the comparison and relevant code state, traces affected behavior through unchanged contracts, reports evidenced findings by impact, and distinguishes missing evidence from confirmed defects. Its references are loaded at the relevant decision: [scope and evidence](skills/reviewing-code-changes/references/scope-and-evidence.md), requirements, broader risk prompts, contextual patterns, structural design, or an allowed delegated review. The optional [evaluation scenarios](skills/reviewing-code-changes/references/evaluation-scenarios.md) check metadata selection separately from application; passing an installer listing is not proof of automatic loading.

Its optional [test-design guide](skills/reviewing-code-changes/references/test-design.md) helps choose independent expectations and checks that expose a realistic mistake through the shipped path. A reviewer preserves the implementation, but may create verification artifacts within explicitly authorized paths/environments; neither shell nor a scratch checkout makes external side effects safe. A general-purpose agent can use the skill: the [reviewer brief](skills/reviewing-code-changes/references/reviewer-brief.md) requests the method explicitly and passes write boundaries, evidence locators, code state, and coverage limits. A dedicated reviewer profile is optional, not a loading guarantee. [Review patterns](skills/reviewing-code-changes/references/patterns.md) also check actual dependency/API versions and resource ownership for generated code; no separate full audit or line-count threshold is required merely because AI wrote it.

`research-with-evidence` tracks material subquestions, source fitness, traceable claims, conflicting evidence, and coverage limits before giving an evidence-bounded answer. Search and interpretation can alternate; neither a fixed two-stage workflow nor a file or worker is mandatory. Large data should be calculated with appropriate tools after checking provenance. Use a message for short evidence and an indexed artifact only when volume or reuse warrants it. Its [evaluation scenarios](skills/research-with-evidence/references/evaluation-scenarios.md) cover correlated sources, misleading ratios, access gaps, and small-task overhead.

`session-handoff` preserves user decisions, observed state, hypotheses, evidence/versioned checks, unresolved issues, and the next authorized move. It reuses an existing progress record or a concise message rather than requiring a new document. On resume, check only current facts that could change the action, retain valid evidence, and recover critical detail from original sources rather than laundering guesses through a summary. Its [evaluation scenarios](skills/session-handoff/references/evaluation-scenarios.md) cover stale checks, pending reviewers, worker ownership, and poisoned summaries. These simulations do not prove actual loading or cross-client reliability.

`dispatching-parallel-agents` helps assess opportunities before a worker split is chosen; loading it does not require delegation. It weighs setup and integration cost, assigns ownership of files and shared mutable resources, and covers changed contracts, partial failures, and combined verification. One subagent working alongside the coordinator counts as parallel work. Its optional [evaluation scenarios](skills/dispatching-parallel-agents/references/evaluation-scenarios.md) separate trigger discovery from coordination decisions; they are not a required dispatch ritual.

`writing-plans` focuses on a usable plan, not a complete execution framework. It checks current project evidence, bounds unresolved questions, connects task dependencies to observable checks, and updates affected completed work when a contract changes. An explicit small planning request may need only a chat checklist; a short but risky migration may need a durable plan. Its optional [plan template](skills/writing-plans/references/plan-template.md), [separate design record](skills/writing-plans/references/spec-template.md), and [read-only reviewer prompt](skills/writing-plans/references/plan-document-reviewer-prompt.md) are linked at the decisions where they help, without requiring extra documents, workers, or repeated approval. The maintainer [evaluation scenarios](skills/writing-plans/references/evaluation-scenarios.md) distinguish metadata selection from plan quality; neither installer listing nor a simulation guarantees automatic loading or successful implementation.

`writing-skills` separates selecting the right skill, getting a useful result after loading, and validating its standalone package. References are linked at the relevant decision: [authoring/format notes](skills/writing-skills/references/anthropic-best-practices.md), [discipline wording](skills/writing-skills/references/discipline-wording.md), [behavior testing](skills/writing-skills/references/testing-skills.md), and the optional [instruction-file experiment](skills/writing-skills/references/instruction-files-testing.md). The former long imported guides have been condensed or rewritten; no fixed pressure campaign, destructive test-first example, or “bulletproof” claim is required. Its [evaluation scenarios](skills/writing-skills/references/evaluation-scenarios.md) are maintainer inputs, not passed-test evidence or routine authoring steps. Installer discovery and metadata simulations do not prove automatic loading.

For optional Graphviz previews, run `node <writing-skills-dir>/scripts/render-graphs.mjs <target-skill-dir> [--output-dir <new-directory>]` with Node.js and Graphviz `dot` available, one graph per top-level `dot` fence (at most three leading spaces, not list-contained or blockquoted). Unsupported indented/quoted fences fail explicitly. The former root-level `render-graphs.js` and `--combine` mode are replaced: independent graphs stay separate, numbered SVGs default to the target's `diagrams/`, existing outputs are not overwritten, and errors exit nonzero. Render only trusted DOT; this helper does not sandbox Graphviz or sanitize generated SVG for publication. A [bundled license notice](skills/writing-skills/references/license-notice.md) preserves attribution when only this skill folder is installed.

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
- `systematic-debugging` — its tracing, safeguards, and waiting guides in `references/`, and helper examples in `scripts/`, have been rewritten from the original supporting files
- `writing-skills` — rewritten descendants in `references/`: `anthropic-best-practices.md`, `discipline-wording.md` (formerly `persuasion-principles.md`), `testing-skills.md` (formerly `testing-skills-with-subagents.md`), `instruction-files-testing.md` (formerly the example test plan), and `graphviz-conventions.dot`; `scripts/render-graphs.mjs` replaces the original renderer; evaluation scenarios are new
- `dispatching-parallel-agents`, `writing-plans` — the name and the subject, nothing else

`reviewing-code-changes` also borrows a few review-process points from `requesting-code-review`.

**PR Review Canvas** ([MIT](https://github.com/projekta2/pr-review-canvas), © 2026 Alexandre Iglesias / Projekta2 Creative Studio) — `reviewing-code-changes` is built on its review checklist: `references/checklist.md` keeps the categories and item numbering, reworded, for 35 of the 51 items.

**cursor/plugins** ([MIT](https://github.com/cursor/plugins), © 2026 Cursor) — the rubric in `reviewing-code-changes/references/quality-bar.md` is distilled from its `thermo-nuclear-code-quality-review` skill, and three checklist items come from its `thermos` plugin. `understanding-a-merge-request` adapts the comprehension-first grouping, pseudocode, traces, callouts, and choice of representation from [its `pr-review-canvas` skill](https://github.com/cursor/plugins/tree/main/pr-review-canvas), with independently written guidance for portable Markdown and project-context investigation rather than the Canvas SDK.

**wshobson/agents** ([MIT](https://github.com/wshobson/agents), © 2024 Seth Hobson) — the language traps in `reviewing-code-changes/references/patterns.md` adapt its `code-review-excellence` skill.

**anthropics/skills** ([Apache 2.0](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt)) — `designing-persian-web-ui` is my own skill, but its anti-default guidance and copywriting section follow the `frontend-design` skill.

## License

MIT — see [LICENSE](LICENSE).
