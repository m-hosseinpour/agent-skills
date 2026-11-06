# Visual Decisions

Use a visual when it clarifies a specific question, relationship, or choice. Show only the detail that helps understanding or comparison. This guide needs no custom server, browser helper, or other skill.

## Choose the Smallest Useful Representation

- **Text or a comparison table:** criteria, constraints, evidence, and trade-offs when their arrangement in space adds little.
- **An inline diagram:** relationships, flows, or interacting parts. Use a format the environment can display; plain text is a valid fallback. Label uncertain or inferred links rather than presenting them as established facts.
- **An image or wireframe:** layout, navigation, or visual hierarchy. Match fidelity to the question; do not polish a layout experiment as if it were the finished product.
- **A static HTML page:** when real wrapping, spacing, or responsive behavior affects the choice. Use the project's existing preview or the environment's supported browser/file preview. Do not add a server or install dependencies solely for this discussion.

## Preview and Feedback

1. **Name the purpose.** Say what the visual will help understand or decide and what it deliberately leaves out. Offer a mockup before spending substantial effort on it; an explicit request for one already supplies that agreement.
2. **Prepare the visual for its purpose.** Show the relevant relationships or evidence without implying unsupported certainty. When comparing options, keep content, viewport, and fidelity consistent where possible, and explain each option's benefit and cost in chat as well as in the visual. For mockups, use representative content lengths and state which widths or states matter.
3. **Show it through an available channel.** Prefer an existing preview. If a file is useful, follow the project's location convention or agree on a location, then share the path. Do not assume that a browser can open local files or that a local URL is reachable by the user. Check the actual result before calling a preview ready.
4. **Use the conversation for feedback.** When a choice is needed, name the options and ask a focused question. An explanatory visual does not require an approval round. There is no automatic click-event capture; do not infer a selection or approval from a mockup's appearance or interactions.
5. **Revise only when needed.** Keep one current visual unless variants help the explanation or comparison. Summarize its relevant limits and, if a choice was made, the chosen direction and next step. Choosing a mockup does not itself authorize production implementation.

If previewing is unavailable, report that limitation and offer an image, diagram, or text comparison. If a new service or dependency is genuinely necessary, explain the cost and get agreement rather than silently rebuilding a companion server. Starting services or exposing ports still follows the user's authorization and environment permissions.

## Keep Mockups Honest and Safe

- Label mockups as exploratory. Identify simulated behavior, missing states, and unverified responsiveness; do not present a static screen as a working feature.
- For HTML, use a complete document with a viewport meta tag. Prefer semantic elements; if controls are interactive, use native buttons, inputs, or selection controls with labels, keyboard access, and visible focus. Separate any simulated interaction from real application actions.
- Include relevant loading, empty, error, long-content, or narrow-width states when they could change the decision. Inspect rendered output at those widths before claiming it works there.
- Use synthetic or authorized content. Do not put credentials or private production data into mockups, external renderers, or image services. Prefer local assets; loading remote images, fonts, or scripts makes network requests and can disclose context.
- Mockups are not production code. Reusing one requires a separate decision about integration, behavior, accessibility, and verification. Preserve generated files unless the user authorizes removal; do not add automatic cleanup.
