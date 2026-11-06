# Authoring Patterns and Format Notes

Use when choosing a skill's structure, examples, or portability boundaries. This is a condensed adaptation of [Anthropic's authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), not a verbatim import or a second mandatory workflow. For current format constraints, consult the [Agent Skills specification](https://agentskills.io/specification); product support can differ.

## Contents

- [Format versus client behavior](#format-versus-client-behavior)
- [Choosing the instruction shape](#choosing-the-instruction-shape)
- [Descriptions and boundaries](#descriptions-and-boundaries)
- [Resource navigation](#resource-navigation)
- [Executable helpers](#executable-helpers)
- [Useful evidence](#useful-evidence)

## Format versus Client Behavior

The open format requires YAML frontmatter with `name` and `description`, followed by Markdown. The name must match the directory. Use a portable lowercase ASCII name with digits and single hyphens; no spaces, leading/trailing hyphen, or consecutive hyphens. The specification limits names to 64 characters and descriptions to 1024 characters. These are format limits, not evidence that a particular wording triggers well.

```yaml
---
name: processing-invoices
description: Use when extracting line items or reconciling totals from invoice PDFs, including scanned invoices; not for drafting invoice copy or analyzing an unrelated spreadsheet.
---
```

The specification recommends keeping the body under 500 lines and moving detailed material into focused supporting files. Treat that as an upper-bound guideline, not a target or proof of concision: a short vague skill can fail, and a technically compliant long skill can waste context.

Only add optional fields when they solve a real need, such as `compatibility` for an environment requirement or `license` for bundled material. Client-specific discovery directories, permission fields, tool names, invocation syntax, model names, and network availability are not universal format guarantees. Check the intended client's documentation or current exposed capabilities before prescribing them. Do not invent a generic MCP naming convention.

Skills are normally disclosed in stages: metadata for selection, body on activation, resources on demand. Whether and when the client refreshes metadata or automatically loads a matching skill must be observed in that client.

## Choosing the Instruction Shape

Match specificity to the failure cost and number of legitimate approaches:

| Situation | Useful guidance | Avoid |
| --- | --- | --- |
| Judgment depends on context | Decision criteria, evidence needed, valid exceptions | One mandatory answer for every case |
| Output has a stable structure | A small adaptable template and a meaningful example | A required report ceremony for tiny requests |
| Operation is fragile or destructive | Preconditions, exact supported command, authorization and recovery limits | “Run exactly this” without establishing the environment |
| Operation is deterministic and repeated | An existing or justified bundled helper | Prose that makes the agent recreate the algorithm each time |

Give the purpose before the procedure. Keep the steps that change an outcome, not general background the agent already knows. An input/output pair is useful when prose leaves a real ambiguity; it should demonstrate a decision, not introduce a new unverified rule.

## Descriptions and Boundaries

The main skill owns the trigger policy: start with `Use when...`, express user intent and observable situations, and keep workflow detail in the body. The activity named by the trigger can convey what the skill helps with without summarizing its process.

Compare realistic requests against metadata alone. Include implicit requests and nearby tasks that share vocabulary but need a different skill. For example, “reconcile these invoice totals” fits the invoice skill; “write an invoice reminder email” does not. A negative prompt about unrelated weather tells little about that boundary.

If metadata matches but the skill never loads, inspect registration, stale metadata, selection policy, and competing skills before adding more keywords. Do not compensate for a client configuration problem with an ever-broader description.

## Resource Navigation

Use supporting files only when they have a clear job:

```text
processing-invoices/
├── SKILL.md
├── references/
│   ├── reconciliation.md
│   └── evaluation-scenarios.md
└── scripts/
    └── extract-lines.py
```

A useful entry point says both when and why:

> When tax and rounding rules could explain a mismatch, read `references/reconciliation.md` from the loaded skill's directory before deciding that a total is incorrect.

The sentence above illustrates wording, not a file bundled with writing-skills. In a real `SKILL.md`, link to `references/reconciliation.md`. Keep actual links relative to their containing file and resolve commands from the loaded skill root. Do not assume the project's working directory is the skill directory.

Keep primary resources directly linked from `SKILL.md`. A reference can link to a related guide, but a long chain should not hide essential decisions. Give longer guides a contents list or split them by need. A main-body rule and its reference must agree; examples and historical snapshots are not competing instruction owners.

## Executable Helpers

State prerequisites, input arguments, output location, mutation/overwrite behavior, and how failure is reported. Use an explicit interpreter or an unambiguous module format rather than relying on the installed folder's package configuration.

- Test a representative success, malformed input, unavailable dependency, and an existing output when relevant.
- Preserve diagnostic output and nonzero failure status. Do not swallow a denied permission or replace missing required data with a made-up successful default.
- Avoid hidden writes to the working project, implicit downloads, or installation commands outside authorization.
- Use safe process argument passing rather than shell interpolation. Validate at actual trust boundaries.
- Existing helpers are not automatically more reliable than generated code; their behavior still needs checking.

For external APIs, obtain the shape from current docs or an authorized request. For copied upstream material, keep required notices and mark adaptations. The installed folder should contain its needed resources rather than rely on a parent repository remaining available.

## Useful Evidence

Check selection independently from execution quality. For application tests, require a useful artifact or decision supported by scenario facts; citing a heading is not proof of compliance or quality. A reference skill can need navigation and correctness checks even when there is no rule to bypass.

Compare old/new or without/with-skill results when practical. Keep fresh evaluator context, inputs, tool access, and expected outcomes comparable; note unavoidable confounders. Expand languages, models, and samples when the intended users or observed variability justify it, not to satisfy a fixed count.

The related official guides on [description optimization](https://agentskills.io/skill-creation/optimizing-descriptions) and [output evaluation](https://agentskills.io/skill-creation/evaluating-skills) offer more detailed experiments. Their sample counts, thresholds, CLI snippets, and workspace layouts are illustrative. Check the actual client's interface before running any example.
