# Source Notes: stepwise-refinement

- Primary source: Program Development by Stepwise Refinement
- Author: Niklaus Wirth
- Year: 1971
- URL: https://dl.acm.org/doi/10.1145/362575.362577
- Supporting source: Public copy of Program Development by Stepwise Refinement
- Supporting URL: https://pascal.hansotten.com/uploads/wirth/StepwiseRefinement.pdf

## Fallback Sources

- Public copy PDF: https://pascal.hansotten.com/uploads/wirth/StepwiseRefinement.pdf

## Key Concepts

- Start from a precise high-level specification.
- Replace abstract operations with concrete ones one decision at a time.
- Each refinement must preserve the intent of the level above.

## Agent Translation

Use it to name abstract operations, refine one decision, and verify preservation at each level.

## Common Misuse

Do not invent layers or helper abstractions that are not required by the current refinement.

## Source Mapping

Specification -> abstract operation -> refinement -> preservation check.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
