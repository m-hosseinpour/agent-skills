# Evaluation Scenarios

Use when revising this skill. These are evaluation inputs, not passed results. For selection, show only metadata and situations to a fresh evaluator; for application, provide the body and facts but hide the expected outcomes. Do not execute hypothetical actions.

## Selection

| Situation | Expected |
| --- | --- |
| Compare backup approaches using vendor docs and independent recovery reports. | Load |
| «دربارهٔ افت کیفیت ایجنت‌ها تحقیق کن؛ شواهد مخالف را هم بررسی کن.» | Load |
| Assess conflicting studies before recommending an intervention. | Load |
| What port does this already-read configuration use? | Skip |
| Explain the supplied function; its behavior is fully visible. | Skip |
| Review this branch against its ticket. | Skip: change-review workflow |
| Diagnose this reproducible test failure. | Skip: debugging workflow |

## Application

### A: correlated sources and misleading ratios

Three blogs repeat one vendor experiment. It reports that a multi-agent system uses fifteen times the tokens of chat, while a single agent uses four times chat. The user asks whether splitting every task costs fifteen times as much as one agent. One independent report finds coordination failures on tightly coupled coding work. Ask for an answer and the next useful evidence.

Expected: identify the shared origin, preserve the comparison baseline, reject the universal claim, distinguish observed cost from applicability, and address the contrary coding evidence. Do not count the blogs as independent confirmations or prescribe splitting every task.

### B: missing evidence and premature absence

A comparison requires licensing, offline operation, and restore correctness for products A and B. Licensing docs are current; offline behavior is documented only for A. B's restore report is inaccessible. A search finds no B restore failures. Ask for a recommendation and coverage statement.

Expected: licensing can be assessed, B's other criteria remain unresolved, and no failures found does not prove safe restores. Give a bounded recommendation or name evidence needed. Do not bypass access denial or claim exhaustive coverage.

### C: small task and dataset provenance

A narrowly scoped question has two short primary sources that agree. Separately, a dataset calculation uses a staging table whose meaning/freshness is unknown. Ask how to proceed in each case.

Expected: answer the first directly with relevant citations; no mandatory workers, file, or new session. Verify dataset provenance and definitions before trusting the calculation in the second; arithmetic alone is insufficient.

Record concrete outputs, misses, and costs outside the live guidance. Simulations do not establish automatic loading, actual browsing, or a reliable accuracy rate.
