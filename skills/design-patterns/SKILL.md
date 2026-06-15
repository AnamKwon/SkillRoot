---
name: design-patterns
description: "Use when applying recurring design solutions only when a present code problem matches a known force, tradeoff, and collaboration structure."
---

# Design Patterns

Use this skill when a recurring design problem is present and a pattern may
explain the collaboration better than ad hoc structure.

## Core Idea

Design patterns name recurring solutions in context. A pattern is justified by a
problem, forces, participants, collaborations, and consequences. Pattern names
should clarify design communication, not decorate simple code with ceremony.

## Before Acting

Answer briefly:

1. **Problem:** What recurring design problem exists now?
2. **Forces:** What forces conflict: variability, coupling, lifecycle, creation,
   ownership, performance, testability, or extension?
3. **Candidate:** Which local or known pattern matches those forces?
4. **Consequence:** What complexity does the pattern add or remove?
5. **Proof:** What code example, test, or caller change shows the pattern helps?

## Workflow

1. Inspect existing local idioms before importing a textbook pattern.
2. Identify the problem and forces before naming a pattern.
3. Prefer the simplest structure that satisfies the forces. A named pattern is
   useful only when it improves communication or changeability now.
4. Use framework-native patterns when they already encode the collaboration.
5. Keep participants and responsibilities explicit in names and tests.
6. Verify the consequence: less duplication, clearer extension point, simpler
   test, safer construction, or reduced coupling.

## Stop Conditions

- The pattern is being chosen before the problem and forces are known.
- A simpler function, module, or data structure solves the present case.
- The pattern adds abstract participants for one caller.
- The issue is domain language or bounded context, not recurring collaboration;
  use domain-driven-design instead.

## Response Shape

```text
Theory: [recurring problem/forces -> chosen pattern or simpler alternative]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
