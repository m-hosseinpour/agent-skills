---
name: writing-skills
description: Use when creating a reusable skill or making a substantive change to an existing skill's purpose, trigger, or guidance.
---

# Writing Skills

A skill is a reusable guide to a technique, judgment, or reference. It should be easy to find, useful when loaded by itself, and no more demanding than the problem it addresses.

## Before Writing

1. Check whether an existing skill or instruction already covers the need. Improve a clear existing home instead of creating a near-duplicate.
2. Decide whether the content is a reusable technique, a project-specific rule, a reference, or a mechanical check. Put it in the right place: skill, project instructions, reference file, or automation.
3. Define the trigger: what observable situation should cause an agent to load this skill? If agents cannot tell they need help, keep essential guidance in always-loaded instructions instead.
4. Establish the intended behavior and any important exceptions before drafting. Do not turn an unsettled design into a procedure.

## Write for Discovery and Use

- Use a short, specific name and a description that starts with `Use when...` and names detectable situations, symptoms, or tasks. Describe when to load it, not the workflow inside it.
- Keep essential decisions and steps in `SKILL.md`; put long tables, examples, templates, and optional references in supporting files.
- Make each skill self-contained enough to work when loaded alone. Supporting-file links should be optional and explain what extra value they provide.
- State the purpose first. Use concrete words, ordered steps for processes, and only examples that clarify a real choice.
- Include when not to use the skill when the boundary is easy to confuse.
- Prefer a positive recipe or a required output shape for formatting problems. Use strong prohibitions only when there is evidence that agents repeatedly break an important rule under pressure.
- If a rule can be enforced mechanically, automate it instead of adding more prose.

## Check Quality Proportionately

Match the check to the guidance and the cost of failure:

- For consequential behavior guidance with repeated failures, compare a realistic case with and without the skill when practical. Use more than one sample only when results vary or the failure cost warrants it.
- For a reference, check that a representative reader can find and apply the needed information if it will be used often.
- For routine, low-risk edits, self-review may be enough.

A read-through is not a behavior test. State honestly what kind of check was done, and revise wording when a check exposes ambiguity. Do not discard a useful draft solely because it was written before testing.

## Common Traps

- A workflow summary in the description can become a shortcut that causes the body to be skipped.
- A vague trigger leaves the skill undiscovered; an overly broad trigger makes it load for unrelated work.
- A skill that depends on another unconditionally may fail when used alone.
- A long checklist or fixed number of test runs does not itself prove quality.
- A reference that duplicates rules without owning or clarifying them creates competing sources of truth.

## Supporting References

Open these only when the task needs them:

- `anthropic-best-practices.md` — imported Anthropic authoring guide; read when designing a new skill's structure or wording. Its evaluation checklist is illustrative and model-specific, not a gate for this runtime.
- `testing-skills-with-subagents.md` — deeper pressure-testing method; open when a consequential discipline skill needs it, and scale its sample counts to the failure cost. Its example test plan is `examples/instruction-files-testing.md`.
- `persuasion-principles.md` — why authority, commitment, and scarcity wording works; open when shaping discipline guidance for use under pressure.
- `graphviz-conventions.dot` — Graphviz style for a decision flowchart; use when a small flowchart is genuinely clearer than prose.
- `render-graphs.js` — render a skill's Graphviz diagrams to SVG; run it when you need to inspect or show a diagram.

A supporting file that neither this body nor a named guide references is effectively absent. Name its entry point or remove it.
