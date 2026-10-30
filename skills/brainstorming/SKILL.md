---
name: brainstorming
description: Use when the goal, constraints, or approach are genuinely unclear, or when the user asks to explore a design before implementation.
---

# Brainstorming

Help turn an unclear request into a design the user can recognize and correct. This skill is self-contained: use it without assuming that global instructions are available.

## When to Use

Use when a consequential choice is still open: what the user wants, who it serves, what counts as success, or which approach fits. Do not load it for a clear, bounded request or a mechanical edit.

## Conversation

1. Read the relevant files and context before asking about facts they can answer.
2. Ask one focused question at a time when an answer could change the result. Say why the answer matters when that is not obvious.
3. Understand the goal, constraints, success criteria, and what would make the result unacceptable. Separate what the user decided from your proposals.
4. When the goal is clear, offer two or three viable approaches with trade-offs and recommend one. If there is only one sensible approach, explain why.
5. Summarize the agreed design in proportion to the work and invite correction.

For a quick feasibility question, propose the cheapest useful probe and return findings; label any prototype as disposable. Keeping a prototype is a separate decision.

## Approval and Handoff

For consequential work, get the user's approval of the design before implementation. A clear, bounded task needs no design ceremony; follow the user's request and normal project practice.

A written design is optional. Use one when another person will implement or maintain the work, decisions need a durable record, or the project already keeps design docs. Capture the problem, outcome, goals and non-goals, important interfaces, constraints, and acceptance criteria; omit sections that do not apply. A plan is useful for multi-step, multi-session, or delegated work, not as a mandatory next artifact for every design.

When a visual choice is genuinely easier to understand by seeing it, offer a mockup or diagram; otherwise keep the discussion in text. If the user accepts, read `visual-companion.md` first; it explains the local browser companion and uses the server files under `scripts/` (`start-server.sh`, `stop-server.sh`, `server.cjs`, `helper.js`, `frame-template.html`). Do not start that server before the user agrees.

## Scope and Simplicity

- Start with the smallest useful outcome; exclude features that do not serve the stated goal.
- If the request contains independent projects, name them and agree which to tackle first.
- If new information changes an approved design, explain the change and get approval for the changed decision, not for unchanged details again.
- Do not turn a clear request into an interview, a document, or a plan merely because this skill was loaded.
