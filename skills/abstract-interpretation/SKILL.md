---
name: abstract-interpretation
description: "Use when reasoning about program behavior with sound approximations, static analysis, invariants, and safe over-approximations when exact execution is impossible or too expensive."
---

# Abstract Interpretation

Use this skill when you need to reason about many possible executions without
running all of them.

## Core Idea

Abstract interpretation analyzes programs by replacing concrete executions with
an abstraction that safely over-approximates possible behavior. The abstraction
must preserve the property being checked, and precision limits must be stated.

## Before Acting

Answer briefly:

1. **Property:** What safety, range, reachability, nullability, permission, or
   state property must hold?
2. **Concrete Space:** What executions or states are too many to enumerate?
3. **Abstraction:** What summary preserves the property: types, intervals,
   sets, states, effects, ownership, or permissions?
4. **Precision:** What false positives or imprecision can the abstraction
   introduce?
5. **Proof:** What static check, invariant, or targeted runtime test supports
   the conclusion?

## Workflow

1. Define the property before choosing an abstraction.
2. Identify the concrete states and transitions relevant to that property.
3. Choose the simplest abstraction that is sound enough for the decision.
4. Over-approximate possible behavior. Do not infer safety from a few sampled
   paths unless the abstraction justifies it.
5. Track joins, loops, recursion, async callbacks, or external inputs where
   precision can be lost.
6. Report uncertainty as false-positive, false-negative, or unmodeled behavior
   risk, and verify high-risk cases with focused tests when possible.

## Stop Conditions

- You cannot state the property being analyzed.
- The abstraction would hide the exact behavior that matters.
- The conclusion depends on an unsound assumption about external input or side
  effects.
- Runtime reproduction is cheap and more informative; use direct testing first.

## Response Shape

```text
Theory: [property -> abstraction -> precision limits]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
