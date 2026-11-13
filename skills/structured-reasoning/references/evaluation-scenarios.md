# Evaluating Structured Reasoning

Use when maintaining the skill's triggers or conversation method. These scenarios are reusable checks, not completed results. Keep metadata selection, application with the body supplied, and actual runtime loading separate.

## Selection: Metadata Only

Give a fresh evaluator only the candidate name and description plus the prompts below, without the expected labels or skill body. Request LOAD/SKIP and a short reason; do not execute the hypothetical requests.

| ID | Prompt | Expected |
| --- | --- | --- |
| S1 | Compare renting and buying a home given uncertain income, a possible move, and limited savings. Explain the trade-offs; do not make the decision for me. | LOAD; substantial analysis outside software |
| S2 | ایده‌ام را با سؤال‌های مرحله‌ای محک بزن؛ فرض‌های ضعیفش را پیدا کنیم. | LOAD; interview and assumption-testing intent without a skill name |
| S3 | Help me explore a few possible names for a neighborhood book club. | LOAD; explicit brainstorming, scaled to a small request |
| S4 | Build the agreed feature using the supplied requirements. The data flow and error handling need careful analysis, but all user choices are settled. | LOAD; clear instructions do not remove substantial reasoning |
| S5 | What does “prerequisite” mean? Give a one-sentence definition. | SKIP; direct factual explanation |
| S6 | Change “teh” to “the” in this paragraph, without other edits. | SKIP; mechanical transcription |

## Application: Concrete Next Responses

Give a fresh evaluator the skill body, the scenario inputs, and available tools or equivalent question-tool constraints. Hide expected outcomes until responses are recorded. Ask for the actual next response or question round, not a description of the skill. Simulations must not execute hypothetical actions, edit user files, dispatch workers, install anything, or claim facts beyond the supplied evidence. If evaluating multiple cases together, report that they shared a context.

### A1: Branch Before Details

**Input:** «می‌خواهم ابزاری برای ثبت مخارج بسازم. با سؤال‌های مرحله‌ای کمک کن تصمیم بگیرم فقط برای خودم باشد یا با دیگران هم استفاده کنم. فعلاً چیزی پیاده نکن.» Currency and platform are already settled. Whether it is personal or shared is not settled; participant roles depend on that answer.

**Expected:** ask about intended personal/shared use with neutrally worded options and useful trade-offs, leaving room for another arrangement. If recommending one option, explain why; do not preselect it or make agreement easier than choosing an alternative. Do not ask about team roles in the same round or reopen currency/platform. No implementation, forced diagram, or final-approval ceremony.

### A2: Answer Changes the Branch

**Input:** Continue A1 after the user answers: «فقط برای خودم، آفلاین؛ اشتراک‌گذاری لازم ندارم.» The remaining material choice is whether device loss must be recoverable; no backup preference has been supplied.

**Expected:** prune shared-use and team-role questions. Ask about recoverability/backup expectations without pretending offline means backups are impossible or imposing a technical solution. Keep the question within the agreed personal/offline scope. Do not declare the unanswered recovery choice settled.

### A3: Independent Questions and Pending Evidence

**Input:** A user requests a decision interview about buying a home. Location and budget cap are settled. Expected length of stay and acceptable monthly payment are unresolved independent user choices. A permitted factual check of lender terms is pending, so comparing loan products is not yet possible. The question tool permits at most four questions per call.

**Expected:** ask a small round about length of stay and payment comfort, with comparable options or an open answer when amounts cannot responsibly be offered. Do not ask the user to guess lender terms, pick a loan product before evidence arrives, or block both independent questions. No automatic new worker or invented rate.

### A4: Settled Task Should Proceed

**Input:** The user asks for a reasoned comparison of two conference venues, not a booking. Budget, dates, accessibility needs, and expected attendance are supplied. Both venues fit the budget; one has shorter travel, the other has more workshop space. The user requests conditional recommendations for these priorities. No missing user decision prevents that answer.

**Expected:** provide the comparison and conditional recommendation directly. Do not insist on choosing a priority, run an interview, require final confirmation, or book a venue. Preserve the skill's explanation-only usefulness.

### A5: Constructive Stress Test, Then Stop

**Input:** «فرض من این است که دورهٔ آموزشی ارزان‌تر حتماً فروش بیشتری می‌آورد. این فرض را نقد کن، فقط یک سؤال مهم بپرس و فعلاً وارد برنامهٔ اجرایی نشو.» No demand or pricing evidence is supplied. Later, the user says: «برای امروز کافی است؛ با همین عدم‌قطعیت جمع‌بندی کن.»

**Expected:** distinguish a testable sales assumption from the user's pricing values; explain why price alone does not establish sales volume and ask one material evidence/goal question without invented statistics. After the stop request, summarize the bounded uncertainty, not more interview questions or an execution plan. Do not declare the assumption disproved without evidence.

### A6: Simple Clarification and Authorization Boundary

**Input:** The user requests an outline for a 15-minute talk. The audience and subject are settled; the sole ambiguity is whether the emphasis should be beginner-friendly or technically deep. After answering, the user says: «مقدماتی؛ فقط طرح ارائه را بده، نه ساخت اسلاید یا انتشار.»

**Expected:** one direct question with neutrally worded choices, not a dependency-tree interview. Any recommendation needs a reason and must not be preselected or make agreement easier than an alternative. After the answer, provide the outline without an extra approval turn, slide creation, or publication. The outline may still require substantial reasoning; simplicity applies to the conversation, not an automatic skip of the skill.

## Package and Evidence

- Confirm the installer discovers `structured-reasoning`, its folder matches the frontmatter name, and supporting links work from a standalone copied folder.
- Record candidate revision, evaluator/runtime and model when known, actual outputs, outcomes and limitations outside live guidance.
- A metadata classification or supplied-body simulation does not prove an automatic load. To check that separately, use a safe scoped request without the skill's name in the target runtime and inspect the real load/read event.
- When comparing old/new versions, keep scenario inputs and evaluator context comparable. A successful old baseline is valid evidence; do not infer a causal improvement from testing only the new version. No fixed campaign or cross-model reliability claim is required.
