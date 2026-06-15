---
name: essential-complexity
description: "Use when estimating, simplifying, refactoring, or generating code where accidental complexity can be removed but essential domain complexity must remain explicit."
---

# Essential Complexity

Use this skill when a task asks for simpler code, faster delivery, or code
generation and the main risk is confusing real domain difficulty with avoidable
implementation clutter.

## Core Idea

Brooks distinguishes essential complexity, which belongs to the problem itself,
from accidental complexity, which comes from tools, representations,
interfaces, build friction, duplication, or unnecessary machinery. Good code
generation removes accidents without hiding the domain's irreducible rules.

## Before Acting

Answer briefly:

1. **Essence:** What domain rule, state, constraint, or tradeoff is inherently
   hard?
2. **Accident:** What complexity is caused by tooling, indirection, duplication,
   ceremony, stale abstractions, or awkward representation?
3. **Separation:** Where are accidental details mixed into essential domain
   logic?
4. **Simplification:** Which accidental part can be removed without erasing the
   domain rule?
5. **Proof:** What behavior shows the domain rule is preserved while clutter is
   reduced?

## Workflow

1. Inspect the user-facing behavior, domain tests, data model, and current pain
   points before simplifying.
2. Classify complexity as essential or accidental. If unsure, state the
   uncertainty and inspect more.
3. Remove accidental complexity first: duplicated adapters, unused options,
   over-general interfaces, noisy transformations, stale compatibility paths, or
   unnecessary build/runtime steps.
4. Keep essential complexity explicit in names, invariants, tests, and errors.
5. Do not replace domain complexity with a vague framework, generic engine, or
   hidden prompt that cannot explain the business rule.
6. Verify that the important behavior still holds and that the simplified path
   is measurably easier to read, test, run, or change.

## Stop Conditions

- The requested simplification would erase a real domain distinction.
- You cannot identify which complexity is accidental.
- The change promises a dramatic improvement without a concrete mechanism.
- The task is about module volatility or human-facing notation; use
  information hiding or cognitive dimensions instead.

## Response Shape

```text
Theory: [essential complexity kept -> accidental complexity removed]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
