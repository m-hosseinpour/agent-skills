# Evaluating Writing Skills

Use when maintaining writing-skills, not during every skill-authoring task. These are reusable inputs and expected outcomes, not a record of completed checks. Selection, useful application, and package execution need separate evidence.

## Selection: Metadata Only

Give a fresh evaluator only the candidate name/description and situations, without expected labels or the body. Request LOAD/SKIP and a short reason; do not execute hypothetical tasks. Compare old/new metadata in separate evaluations where practical. Include nearby installation, instruction-editing, or debugging skills if overlap matters.

| ID | Situation | Expected |
| --- | --- | --- |
| D1 | Create an agent skill for recurring CSV cleanup. | LOAD |
| D2 | Review an existing skill for usefulness and flaws; no edits yet. | LOAD; audit only |
| D3 | Investigate why an installed skill never loads for relevant prompts. | LOAD |
| D4 | Reorganize a skill's references and repair its broken helper. | LOAD |
| D5 | Capture a completed repeatable workflow as a skill. | LOAD |
| D6 | Update a skill's decision rule after requirements change. | LOAD |
| D7 | Install an existing skill without changing content. | SKIP |
| D8 | Fix one spelling error in SKILL.md without changing meaning. | SKIP |
| D9 | Add a local project rule to AGENTS.md; no skill requested. | SKIP |
| D10 | Apply an existing debugging skill to a failing test. | SKIP |
| D11 | Faithfully translate a skill without changing meaning or structure. | SKIP |
| D12 | Explain the Agent Skills format; no authoring or audit. | SKIP |
| D13 | اسکیل موجود رو بررسی کن؛ می‌خوام بدونم واقعاً کاربردی هست و کجا باید لود بشه. | LOAD; audit only |
| D14 | این اسکیل فقط با اسم خودش لود می‌شه، تریگرش رو بهتر کن. | LOAD |
| D15 | Turn the reporting procedure we just used into reusable guidance for other agents; decide whether a skill is the right home. | LOAD; assess placement first |
| D16 | Write a user manual for the reporting feature, not agent guidance. | SKIP |

Report misses and false positives separately. For actual automatic-loading evidence, submit a safe scoped request in the target client without naming writing-skills and inspect the actual load/read event. Registration alone or a metadata simulation cannot establish runtime selection or a cross-language/model loading rate.

## Application: Decisions and Artifacts

Give a fresh evaluator the body and access to references, plus scenario facts only. Hide Expected paragraphs until grading. Ask for next actions, useful output, reference choice with reasons, checks, and limits. Simulations must not edit user work, dispatch further workers, install packages, or execute hypothetical incidents.

### B1: Audit Request Without Edit Permission

The user asks whether an existing skill is useful and why it might be missed. Its metadata says “Use when creating a reusable skill.” The body contains “also use for reviewing existing skills.” The installer lists it, but no runtime load events are supplied. A separate project instruction forces skill loading for writes, not audits.

**Expected:** identify that a body-only audit trigger cannot guide initial selection. Report a proposed metadata change and investigate whether the runtime exposes current metadata; do not claim the installer proves automatic loading, invent a loading rate, or edit merely from an audit request. Keep instructions that force loading separate from description-only evidence.

### B2: Small Settled Creation and Existing Home

The user asks to capture a repeatable CSV reconciliation step as a skill. A current CSV skill already owns that trigger and has a clear relevant reference. The requirement is a small output shape, already agreed. The project has no test framework and forbids subagents. The only approved action is proposing a draft.

**Expected:** propose extending the existing home, with a short useful output example and a proportionate navigation/application check. No near-duplicate skill, mandatory interview, plan document, framework, announcement ritual, or delegate. Apply inline guidance without depending on another installed skill; do not write files beyond the request.

### B3: Loaded but Not Useful

An invoice skill is registered and its current description is visible. Runtime logs show it loaded. Its body links every task to a large reference that mixes incompatible rounding rules; the user reports wrong reconciliation for credit notes. A shorter candidate corrects the credit-note rule but skips scanned invoices entirely. No safe invoice fixtures are provided yet.

**Expected:** distinguish application/navigation failure from trigger failure. Inspect independent requirements and focused reference branches, ask for missing material facts or sanitized fixtures, preserve valid scan behavior, and compare the changed decision with a neighboring case. Do not broaden metadata to fix a confirmed body failure or call a read-through sufficient verification.

### B4: Helper Failures and Standalone Packaging

A skill helper imports ESM from a `.js` file with no package manifest, requires Graphviz, and writes into the project's current directory. Invalid DOT exits zero; repeated graph names overwrite an output. Instructions link to a missing absolute installation path. The repository has no test framework.

**Expected:** reproduce the real failures with scoped fixtures, make module execution and resource resolution independent of install location, document prerequisites and output behavior, protect existing output, and propagate nonzero errors. Use focused disposable execution rather than scaffold a framework. Check links from a copied standalone folder and update moved-path docs/notices. Do not silently install Graphviz.

### B5: Overbearing Reference Under Pressure

The main skill says checks are proportionate. Its testing reference orders deletion of pre-test code, three pressures per test, and continuing until “bulletproof.” Its persuasion guide orders an announcement and full-suite run every time. User instructions forbid deleting existing work and say the full suite is known to fail unchanged.

**Expected:** identify conflicting rule owners and harmful examples, not just add a top disclaimer. Rewrite the reference around legitimate outcomes, relevant checks, exceptions, authorization, and a bounded stop. No deletion, forced baseline failure, fixed campaign, claimed universal reliability, or blind copying of evaluator feedback.

### B6: Successful Baseline and Unavailable Isolation

A no-skill evaluator produces a correct draft from a clear small request. The runtime also injects project instructions about naming and relative paths. Separate clean sessions are unavailable. The user asks whether the proposed skill improved behavior.

**Expected:** report the successful baseline and confounder honestly. A skill may still offer repeated navigation/reference value, but do not fabricate failure or causal improvement. Offer a bounded self-review or future comparison when suitable, not unapproved launcher workarounds or deletion of shared instructions to force isolation.

## Reference Navigation

- Structure, open format versus client behavior: **Establish the Need and Scope** → `references/anthropic-best-practices.md`.
- Legitimate discipline boundaries: **Write the Smallest Useful Guidance** → `references/discipline-wording.md`.
- Optional diagrams: the diagram decision → `references/graphviz-conventions.dot` and `scripts/render-graphs.mjs`.
- Behavior comparison: **Verify Selection, Usefulness, and the Package** → `references/testing-skills.md`.
- Always-loaded selection instructions: the same verification section → `references/instruction-files-testing.md`.
- Maintaining writing-skills itself: **Evaluating This Skill** → this file, not an ordinary authoring step.

## Helper Checks

Run the helper only against trusted fixture DOT. Derive assertions from observable behavior, not source text:

- Valid digraphs, ordinary undirected graphs, unnamed/quoted names, and repeated graph names render as separate numbered SVGs.
- CRLF, tilde fences, and longer surrounding Markdown fences are handled without treating example code as an active diagram.
- Container-indented and blockquoted DOT fences are explicitly rejected; move diagrams to the documented top-level form rather than silently skipping them.
- Invalid or unclosed DOT, unknown options, missing input/dependency, and existing output fail nonzero without replacing existing files.
- A later invalid graph causes no new output from earlier valid graphs; no-DOT input succeeds without requiring Graphviz or creating output.
- Explicit output location and a copied standalone helper work independently of the project's package configuration.

For visual claims, inspect representative rendered output, not just file existence. Keep execution fixtures and raw reports outside live guidance, with revision, inputs, results, limits, and any skipped actual-loading checks.
