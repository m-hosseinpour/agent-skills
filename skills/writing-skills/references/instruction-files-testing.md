# Testing Instruction Files That Select Skills

Use when an always-loaded instruction file is being changed to improve relevant skill use. This is an illustrative experiment adapted from the original variant test plan—not completed evidence and not a default instruction-file policy.

## Question and Controls

Does the candidate instruction help the target client load a relevant, registered skill without loading unrelated skills or imposing a library sweep on simple work?

Use a fresh, scoped test session with the same skill catalog, metadata, task facts, tools, and permissions for each variant. The catalog must contain a genuinely useful skill for positive cases. Use the client's actual mechanism for presenting/loading skills; do not assume a home-directory path or an invented category layout.

Do not edit global user instructions or installed skills merely to test a variant. Use an approved fixture or supported isolated configuration; if isolation is unavailable, label the confounder and limit the conclusion.

## Candidate Variants

- **Baseline:** the client's normal skill exposure and instructions, unchanged.
- **Focused cue:** “Use relevant available skills when the task matches their descriptions. Loading a skill does not authorize actions or require optional resources.”
- **Boundary-aware cue:** the focused cue plus “Skip unrelated skills and mechanical work unless a specialized skill is explicitly requested. Resolve resource paths from the loaded skill's directory.”

These are hypotheses to compare, not a required winning variant. Stronger instructions can increase irrelevant loading, reading cost, and workflow rigidity.

## Scenarios

| Situation | Useful outcome |
| --- | --- |
| Diagnose a failing authentication flow under a deadline; a registered debugging skill fits | Load it, gather sanitized causal evidence, and propose authorized verification |
| A skill is requested for a reusable reporting workflow, without naming an authoring skill | Load the authoring skill, check an existing home, and produce appropriately sized guidance |
| Correct one supplied spelling error, with no behavior change | Avoid forcing an unrelated skill or a full audit |
| Install an existing skill with content unchanged | Use the client's supported installation flow; do not trigger an authoring workflow just because “skill” appears |
| Repeatedly wrong runtime selection despite matching metadata | Inspect registration/current metadata and real load events before changing the entire library |
| A relevant guide exists but user instructions forbid delegation | Apply inline guidance or disclose limits; do not spawn an evaluator to satisfy the guide |

Vary positive and near-miss wording, including the actual user's language. Include implicit requests, not just prompts that tell the agent to “load a skill.” Do not present fictional emergencies as real or execute hypothetical deployments.

## Protocol and Evidence

1. Establish expected behavior from the task and available catalog, before viewing outputs.
2. Run each selected variant in fresh context using the supported client interface. Observe actual skill-tool/file-read events when checking real loading; a declared intention is not a load.
3. Record missed relevant loads, unwanted loads, needed versus needless reference reads, useful task results, and extra burden. Repeat when variability matters, not by an automatic fixed count.
4. Review failures for instruction priority, registration, stale metadata, trigger ambiguity, or resource navigation before adding emphasis.
5. Check fresh near-misses after revision so wording is not tuned only to the original positive prompts.

Retain actual inputs, candidate revision, event evidence, decisions/artifacts, and confounders outside live instructions. A metadata-only classification is a simulation; one observed load establishes only that request in that environment. No expected compliance percentages or predetermined winning variant are assumed.
