# Plan Document Reviewer Prompt

Read after drafting a substantial or high-stakes plan when an independent reviewer is useful and delegation is available and allowed. This template does not authorize dispatch. A self-review can use the same questions when a separate reviewer is unavailable.

Provide the plan, authoritative requirements, relevant project context, and access limits. Include a spec only if one exists; otherwise identify the plan's approach section as the design record. Do not make the reviewer infer requirements from the plan itself.

```text
Review this implementation plan for material gaps and readiness. You are a
read-only reviewer, not an implementer or approver of user decisions.

Plan: [path or supplied text]
Requirements and acceptance criteria: [source or supplied text]
Design/spec: [reference if separate; otherwise the plan's approach section]
Project context: [relevant instructions, starting state, affected paths,
                 verified contracts, and available verification practices]
Access limits: [permitted inputs/tools; no edits, commits, workers, or state changes]

Check:
1. Coverage: every material requirement has a task or combined check; no hidden
   scope expansion or conflict with agreed decisions.
2. Grounding: paths, API facts, commands, and constraints have a credible basis.
   Identify unverified facts without inventing replacements. If allowed inputs
   cannot establish a fact, state the verification gap and its effect on readiness.
3. Sequence and contracts: dependencies are feasible, shared interfaces agree,
   blocked work is identified, and any claimed parallel units have settled inputs
   and nonconflicting write ownership, including indirect writes/shared state.
4. Usable tasks: an implementer with the stated context can identify the outcome,
   scope, needed inputs, and check. Do not require each task to run independently
   or assume each task will be assigned to a subagent.
5. Verification: checks name expected behavior, relevant failure cases, and combined
   acceptance, not just successful local commands. Baseline failures or unavailable
   checks are not presented as green results.
6. Risk and handoff: applicable compatibility, data, rollout, and recovery concerns
   are addressed; unresolved material decisions block the work they affect. A resume
   plan accounts for current state and affected completed work, not only pending work.
7. Useful detail: flag implementation bodies only when they unnecessarily prescribe
   routine choices or duplicate the work. Contracts, evidence, illustrative traces,
   small pseudocode sketches, and verification commands can be useful. Do not flag
   a block solely for its syntax, executability, or number of lines.

Report only material issues: what is wrong, where, evidence, the likely consequence,
and the smallest needed clarification/correction. Keep optional suggestions separate.
An explicitly blocked investigation is legitimate planning, not a placeholder defect;
dependent implementation must not be described as ready.

Output:
## Plan Review
Status: Ready | Ready for unblocked tasks only | Needs revision
Reviewed inputs and limits: [what you checked; what remains unverified]
Issues: [task/section, evidence, consequence, needed correction; or none]
Advisory suggestions: [optional; not approval gates]

Readiness does not authorize implementation, resolve user choices, or claim that
the code or proposed checks have already succeeded.
```
