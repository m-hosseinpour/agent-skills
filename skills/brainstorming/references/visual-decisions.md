# Visual Decisions

Use a visual when it helps the user make a specific decision, not just because the task involves a UI. Show only enough detail to compare the relevant options. This guide needs no custom server, browser helper, or other skill.

## Choose the Smallest Useful Representation

- **Text or a comparison table:** requirements, scope, API choices, and conceptual trade-offs. A UI topic does not automatically need a mockup.
- **An inline diagram:** relationships, flows, or component boundaries. Use a format the environment can display; plain text is a valid fallback.
- **An image or wireframe:** layout, navigation, or visual hierarchy. Match fidelity to the question; do not polish a layout experiment as if it were the finished product.
- **A static HTML page:** when real wrapping, spacing, or responsive behavior affects the choice. Use the project's existing preview or the environment's supported browser/file preview. Do not add a server or install dependencies solely for this discussion.

## Preview and Feedback

1. **Name the decision.** Say what the visual will help decide and what it deliberately leaves out. Offer a mockup before spending substantial effort on it; an explicit request for one already supplies that agreement.
2. **Prepare comparable options.** Keep content, viewport, and fidelity consistent where possible. Use representative content lengths and state which widths or states matter. Explain each option's benefit and cost in chat as well as in the visual.
3. **Show it through an available channel.** Prefer an existing preview. If a file is useful, follow the project's location convention or agree on a location, then share the path. Do not assume that a browser can open local files or that a local URL is reachable by the user. Check the actual result before calling a preview ready.
4. **Ask for feedback in the conversation.** Name the options and ask a focused question. There is no automatic click-event capture; do not infer a selection or approval from a mockup's appearance or interactions.
5. **Revise only what the feedback changes.** Keep one current preview unless retaining variants helps the comparison. Summarize the chosen direction, remaining limits, and the next step. Choosing a mockup does not itself authorize production implementation.

If previewing is unavailable, report that limitation and offer an image, diagram, or text comparison. If a new service or dependency is genuinely necessary, explain the cost and get agreement rather than silently rebuilding a companion server. Starting services or exposing ports still follows the user's authorization and environment permissions.

## Keep Mockups Honest and Safe

- Label mockups as exploratory. Identify simulated behavior, missing states, and unverified responsiveness; do not present a static screen as a working feature.
- For HTML, use a complete document with a viewport meta tag. Prefer semantic elements; if controls are interactive, use native buttons, inputs, or selection controls with labels, keyboard access, and visible focus. Separate any simulated interaction from real application actions.
- Include relevant loading, empty, error, long-content, or narrow-width states when they could change the decision. Inspect rendered output at those widths before claiming it works there.
- Use synthetic or authorized content. Do not put credentials or private production data into mockups, external renderers, or image services. Prefer local assets; loading remote images, fonts, or scripts makes network requests and can disclose context.
- Mockups are not production code. Reusing one requires a separate decision about integration, behavior, accessibility, and verification. Preserve generated files unless the user authorizes removal; do not add automatic cleanup.
