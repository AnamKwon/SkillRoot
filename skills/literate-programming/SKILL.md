---
name: literate-programming
description: "Use when generating, reorganizing, or documenting code where human understanding, explanatory order, and executable implementation must be developed together."
---

# Literate Programming

Use this skill when the code is hard to understand in machine order and the
maintainer needs the program's story to be recoverable.

## Core Idea

Knuth's literate programming reverses the usual emphasis: write programs as
explanations for humans, with executable code arranged to support that
explanation. For coding agents, this means choosing names, examples, comments,
tests, and file organization so a maintainer can reconstruct intent.

## Before Acting

Answer briefly:

1. **Reader:** Who needs to understand this code later?
2. **Story:** What order best explains the program's intent to that reader?
3. **Code Order:** Where does execution order differ from explanation order?
4. **Synchronization:** Which comments, docs, examples, or tests must stay true
   with the code?
5. **Proof:** What read-through, test, or example shows the story and behavior
   agree?

## Workflow

1. Identify the maintainer-facing story before adding prose or reorganizing code.
2. Use names and small examples first; add comments only where code cannot carry
   the explanation alone.
3. Place explanatory comments near the decisions they explain, not in distant
   overview text that can drift.
4. Keep generated docs, examples, and tests synchronized with behavior.
5. Avoid decorative documentation. Every prose block must explain intent,
   invariant, ordering, or tradeoff that is otherwise hard to recover.
6. Verify by reading from public entry point to core behavior and running the
   example or test that represents the story.

## Stop Conditions

- The code can be made clear through names and structure without extra prose.
- The requested documentation would duplicate code facts likely to drift.
- The real issue is ambiguous behavior or missing tests; use sensemaking or
  test-driven-development first.
- Reordering for explanation would fight the repository's established layout.

## Response Shape

```text
Theory: [human explanation order -> executable code]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
