# Compact Design Record

Read when the project already maintains a design/spec or a separate record has a distinct audience or purpose. A handoff alone does not require two documents: keep the approach in the plan when that is sufficient. Follow project conventions and keep only relevant headings.

The sections capture: the problem and observable result; what is included and excluded; who uses the change and the important scenarios; the chosen approach and cross-component interfaces; relevant data and failure behavior; project or compatibility limits; checkable conditions for completion; and any remaining decision with its owner and needed-by date. Omit data, scenarios, constraints, or open decisions when they do not apply.

```markdown
# [Change] — Design

## Problem and outcome
## Goals and non-goals
## Users and scenarios
## Approach and important interfaces
## Data and failure behavior
## Constraints
## Acceptance criteria
## Open decisions (owner and needed-by date)
```

Record decisions, not a transcript of the discussion. The plan should refer to this document rather than duplicate its contents. Identify the authoritative source for each shared contract or decision. An open material decision blocks the dependent implementation; listing an owner or date does not make the design settled.
