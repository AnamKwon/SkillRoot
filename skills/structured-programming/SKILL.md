---
name: structured-programming
description: "Use when writing or refactoring control flow where reasoning should remain tractable through clear sequencing, selection, repetition, and decomposed program structure."
---

# Structured Programming

Use this skill when complex control flow makes code hard to reason about,
review, or test.

## Core Idea

Structured programming keeps reasoning tractable by building programs from
well-structured control constructs and decomposed blocks with clear entry,
exit, and effect. The goal is not style purity; it is making correctness easier
to reason about.

## Before Acting

Answer briefly:

1. **Control Shape:** What sequence, selection, repetition, or recursion is
   needed?
2. **Entry/Exit:** What are the clear entry and exit conditions for each block?
3. **State:** Which state changes across the block?
4. **Reasoning Risk:** Where do flags, jumps, early exits, callbacks, or shared
   mutation make reasoning harder?
5. **Proof:** What test or trace shows each block preserves its intended effect?

## Workflow

1. Inspect the existing control flow before changing it: branches, loops,
   exceptions, callbacks, async paths, and shared state.
2. Prefer explicit structure: sequence for ordered work, selection for real
   alternatives, repetition for bounded iteration, and small functions for
   separable blocks.
3. Reduce control flags, hidden fallthrough, duplicated exits, and state changes
   that span too many branches.
4. Keep each block's precondition, effect, and continuation understandable.
5. Preserve useful guard clauses when they clarify invalid cases; do not force
   awkward nesting for style.
6. Verify by testing representative branch and loop cases, including boundary
   conditions.

## Stop Conditions

- Refactoring control flow would obscure domain intent.
- The complexity is essential domain branching, not accidental structure.
- The code is event-driven or distributed and needs an information-flow theory
  first.
- You cannot run or inspect enough cases to prove behavior stayed equivalent.

## Response Shape

```text
Theory: [control-flow shape -> reasoned blocks]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
