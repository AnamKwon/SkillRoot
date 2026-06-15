---
name: stepwise-refinement
description: "Use when developing algorithms, features, or generated code by moving from a precise high-level specification to executable detail through small refinement steps."
---

# Stepwise Refinement

Use this skill when jumping directly to implementation would hide design
decisions or produce brittle code.

## Core Idea

Wirth's stepwise refinement develops a program by starting with a precise
high-level specification and successively replacing abstract operations with
more concrete ones. Each step should preserve the intent of the level above.

## Before Acting

Answer briefly:

1. **Specification:** What must the program do at the highest useful level?
2. **Abstract Operations:** Which operations can be named before implemented?
3. **Next Refinement:** Which one design decision should be made next?
4. **Preservation:** How does the refinement preserve the higher-level intent?
5. **Proof:** What test, trace, or example validates this refinement level?

## Workflow

1. Write or infer a high-level specification before adding implementation
   detail.
2. Name abstract operations in domain terms, not helper-function mechanics.
3. Refine one operation or decision at a time: data representation, algorithm,
   boundary, error handling, or iteration strategy.
4. After each refinement, check that no higher-level requirement was lost.
5. Stop refining when the remaining operations match existing library calls,
   local helpers, or straightforward code.
6. Verify with examples at the highest level and focused checks for risky
   refinements.

## Stop Conditions

- The high-level specification is unknown or contested.
- Refinement is being used to invent layers with no present need.
- A lower-level detail changes the original intent without being acknowledged.
- The task is about test-first behavioral discovery; use test-driven-development
  instead.

## Response Shape

```text
Theory: [specification -> refinement step]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
