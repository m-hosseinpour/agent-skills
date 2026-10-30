---
name: understanding-a-merge-request
description: Use when you need to understand a colleague's pull or merge request rather than judge it — when you will maintain code you did not write, when a diff is too large to hold in your head, or when someone asks you to explain what a change does and why.
---

# Understanding a Merge Request

## Overview

Understanding a change is a different job from reviewing it. A review asks *is this right?*;
this asks *what problem did they have, what did they decide, and where do I start reading?*

**Core principle:** reconstruct the author's model of the change — don't inventory their files.

You are done when you can explain the change to someone else in two minutes, and name the
questions only the author can answer.

## When to Use

- Taking over, or maintaining, a branch you did not write
- A colleague's MR you must get up to speed on before you can judge it
- A diff is larger than you can hold in your head and you do not know where to begin
- You must review it and do not yet understand it — understand first, then judge with
  `reviewing-code-changes`

**Not for:** deciding whether it is ready to merge (`reviewing-code-changes`). This skill's walkthrough is for understanding a change; use a review report only when the task is to assess findings for the author.

## 1. Get the intent before the diff

Read the description, the commit messages, the linked issue. Then write one sentence:

> The system did X; after this it does Y, because Z.

If the description is missing or says only "fixes bug", that is itself a question for the
author — do not silently invent the intent from the code.

Then get the change:

- local branch: `git diff <base>...<branch>` and `git log <base>..<branch>`
- hosted: the PR URL — `.diff` on the URL gives the patch, the API gives the body
- neither given: ask which ref. Never guess the branch, and never fall back to whatever is
  checked out.

## 2. Read the shape, not the files

What is the before → after of the *flow*? A new capability, a changed contract, a deleted
path — not five files with edits.

Name the seams: the files that only make sense read together (route → handler → client).
Boilerplate — renames, import order, moved types, formatting — is a list, not a reading item.

## 3. Read in value order

1. Entry point — where the new behaviour is reached
2. Core logic — the part that decides something
3. Wiring — what connects the two
4. Support — types, config, helpers

Say what you skipped and why. Boilerplate gets a glance for surprises, never a line-by-line
pass.

## 4. Recover the decisions

For every non-obvious choice, say what else was visible in the diff, why this one won, and
what it costs. The alternative is usually on the page: the old path, the parameter nobody
passes, the config flag nobody reads.

A decision with no visible reason is a question, not an explanation.

## 5. Find the surprises

What would trip whoever maintains this in six months?

- an ordering or retry that matters only under failure
- a value trusted from outside the boundary
- new coupling between modules that were independent
- a contract that changed without every caller changing

Tag each one — *subtle*, *breaking*, *race*, *perf*, *security* — and give one sentence of
why. Skip the untagged ones: a list where everything is a surprise has no signal.

## 6. Write the document

Markdown, in this order:

1. **What it does** — two sentences.
2. **Shape of the change** — three to five lines, before → after.
3. **Reading path** — numbered, `file:line`, and why this order.
4. **Core logic** — the part that needs prose. Pseudocode when the hunk is dense; one concrete
   input traced through the old and new path when the behaviour change is hard to predict.
5. **Decisions** — a table: decision | the alternative | what it costs.
6. **Surprises** — tagged, one line each.
7. **Questions for the author** — three to five, specific, each answerable in one message.

Write it to a file and give the reader the path — a walkthrough pasted into chat cannot be
re-read alongside the code. Write in the language of the conversation; identifiers, paths and
payloads stay in their original form.

## Rules that keep it honest

- **No verdict.** "This should have…" is a review. Here it becomes a question, or a handoff to
  `reviewing-code-changes`.
- **No line-by-line restatement.** The reader already has the diff; you are adding what the
  diff does not say.
- **Cite the intent.** PR body, commit, or line. An intent you inferred is labeled *inferred*.
- **Never let an unread file pass as read.** Name what you skipped.
- **One sentence per risk.** If you cannot say why it matters in one sentence, investigate it
  or drop it.
- **Separate what you ran from what you read.** "Verified" needs an execution you can point to;
  anything else is marked *inferred*. A document that implies execution it never did is a lie.

## Common Mistakes

| Mistake | Why it fails |
|---|---|
| Sections named after files | The reader has the diff; a file-by-file summary adds nothing |
| Intent guessed from code alone | You explain the accident as if it were intent |
| Explaining what each line does | They can read code; they need the *why* |
| No reading order | Comprehension is a path, not a pile |
| Questions that are really verdicts | "Why didn't you handle X?" is a review finding in disguise |
| Complete but long | Forty pages nobody reads; two pages read twice |

## Red Flags

- A section title is a file name.
- You cannot state the intent in one sentence.
- Paragraphs begin "This file adds…".
- There is no questions section.
- The word "should" appears.
- You did not name what you skipped.

**Any of these mean: go back to step 1, or step 2.**
