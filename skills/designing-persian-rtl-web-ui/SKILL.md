---
name: designing-persian-rtl-web-ui
description: Use when building or changing a Persian (Farsi) or right-to-left web interface — a page, a component, a layout, dark mode, UI copy, direction, numerals, or an existing RTL UI that needs work — and before calling Persian UI work done.
---

# Designing Persian RTL Web UI

Taste for Persian and right-to-left web interfaces. It applies on top of a project's own design language: **the project's language wins, but "no design language at all" is not an option.**

## Start from the subject, not from a template

Before choosing a look, name the subject, the audience, and the one job the screen does. The look comes from those — the industry, its materials, its own vocabulary — not from whichever layout you reached for last time.

Sketch the palette (4–6 named hex values), the typefaces and their roles, and the layout in a few lines *before* writing CSS, then reread it against the brief. If the same plan would serve any similar page, the plan is the problem, not the CSS.

## The baseline: modern product surface

Think Linear or Vercel — generous whitespace, strong typography with a real type scale, subtle shadows, crisp borders, deliberate dark mode. Confident and quiet, never decorated. **A plain unstyled page is a defect, not a default**; when in doubt err toward more visual character, not less.

This is the **floor for internal tools and dashboards**, not the answer to every brief. A marketing page, a portfolio, anything with a brand of its own gets a direction chosen for it — and when the brief states a visual direction, follow it exactly, including when it asks for one of the looks warned against below.

## On top of that: warmth, and one bold moment

Where the reader is not a specialist, each decision is a clear card in plain language with large type instead of a wall of tables and jargon, and the primary action is obvious at a glance.

Do not let everything sit at the same visual weight — the key number and the primary action carry real emphasis: a saturated accent, a larger size, a gradient reserved for the one thing that matters. **Every screen has a focal point.** Boldness means *emphasis*, not noise: avoid glassmorphism everywhere, heavy animation, neon, decoration for its own sake.

Spend that boldness in one place. Let one element be the memorable thing, keep everything around it quiet, and before finishing remove one accessory.

## Do not ship the generated-page tells

Each of these is right for some brief and a default for none:

- Accenting a single word of a headline — italic, bold, or a different colour.
- ALL-CAPS for labels, or an eyebrow label above every heading.
- Numbered markers (01 / 02 / 03) where the content is not actually a sequence.
- The same rounded card, radius and soft grey shadow repeated at every level of hierarchy.
- Gradients as decoration instead of emphasis on one element.
- Warm cream + high-contrast serif + terracotta; near-black + one acid accent — the two most common clusters.
- Monospace labels and tracked-out type pasted on as texture.

Structure carries information: a divider or a number earns its place only when it tells the reader something true about the content. The hero is the first thing seen — open with the most characteristic thing in the subject's world (a headline, an image, an animation, a live demo), and treat "big number, small label, gradient accent" as one option among many.

## Words are design content

Name things by what the person understands, not by how the system is built — they manage notifications, not webhook config. A button says what happens when it is used: "Save changes", not "Submit", and the toast that follows says "Saved". Errors state what happened and how to fix it, never apologise and never go vague. An empty screen is an invitation to act. Sentence case, plain verbs, no filler.

## Responsive is required, not optional

Design mobile-first; a phone is the common case, not the fallback. Every page works at 360px — no horizontal scroll, no tiny tap targets, tables become stacked cards or scroll containers, the primary action stays reachable. Touch targets ≥44px, primary actions low on the screen on mobile. Test at 360 / 768 / 1280 using the real flow, not a screenshot.

## Typography — set a real scale and load what you name

Load every font family the CSS names; a `font-family` naming a font that is never loaded is a silent bug that falls back to a system font. Build a type scale with real contrast — the number that matters visibly larger than headings, headings clearly larger than body, not everything at 1rem. Consider tabular figures so numeric columns align.

Choose the family for the subject rather than reaching for the same one every time: one family, or two that are clearly distinct. When type is itself the visual element, its treatment is part of the design, not a neutral vehicle.

## Persian and right-to-left

**Direction is a layout decision, made once.** Set `dir="rtl"` on the document (and `lang="fa"`) and let the layout follow it. Use logical properties — `margin-inline-start`, `padding-inline`, `inset-inline-start`, `border-start-start-radius` — instead of `left`/`right`, so one stylesheet serves both directions. Flex and grid rows already follow direction: `flex-direction: row-reverse` to fake RTL breaks the moment a component is reused in an LTR context.

**Mirror what points, not what is real.** Chevrons, back/next arrows and progress direction flip; play buttons, clocks, checkmarks, brand logos and sliders from 0 to 100 keep their orientation.

**Text and numbers need deliberate handling.** Persian digits are a product decision — pick one and keep it: Latin digits in data, tables and code fields, Persian digits in prose when the product speaks Persian. Either way use tabular figures so columns line up. Wrap LTR runs inside a sentence (URLs, English names, code, email addresses) in `<bdi>` or `dir="ltr"`, otherwise trailing punctuation jumps to the wrong end.

**The typography has to be Persian, not a Latin font with Persian glyphs.** Load a real Persian face — Vazirmatn is the safe default — and set line height generously, roughly 1.7–1.9; Latin defaults are too tight for Persian ascenders and descenders. Use the half-space (U+200C) in words that need it rather than a full space, and check that headings do not break mid-phrase when they wrap.

Check the result with real Persian content — Latin placeholder text hides every one of these problems.

## Color and motion

Design light and dark deliberately — dark mode is not an inverted afterthought. One accent means "action"; semantic tones (safe / caution / danger) stay distinguishable in both modes and for color-blind readers; check contrast rather than assuming.

Motion is subtle and fast (150–250ms on hover, focus, open/close), clarifies rather than performs, and respects `prefers-reduced-motion`. Anything the user did not trigger is one orchestrated moment — a single load sequence or reveal — not a fade-and-slide on every section.

## Before calling UI work done

Load it at phone width, run the real flow end to end, and confirm responsive and dark-mode behaviour. **A desktop screenshot proves nothing about the phone.** Where you can, look at the rendered result and critique it: a broken layout, a flat hierarchy and a font that silently fell back all look different in a picture than in the source.

When the user says a UI feels plain, the fix is usually more type-scale contrast, a real focal point and better spacing — not more colors.

---

The anti-default guidance and the copywriting section above are adapted from Anthropic's `frontend-design` skill (Apache 2.0).
