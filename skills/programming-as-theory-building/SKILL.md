---
name: programming-as-theory-building
description: "Use when writing, modifying, debugging, reviewing, or refactoring code where the change must preserve a recoverable theory of how real-world affairs map into program behavior."
---

# Programming as Theory Building

Use this skill when code work would otherwise become text editing detached from
the system's purpose.

## Core Idea

The valuable product of programming is the programmer's working theory: how the
program maps real-world activity into behavior, why it is shaped this way, and
how it can be changed without breaking that theory. Source code, tests, docs,
and logs are evidence for reconstructing the theory.

## Before Editing

Answer briefly:

1. **Mapping:** What workflow, rule, protocol, or invariant maps to this code?
2. **Current Theory:** Why is the current code shaped this way? Use names,
   tests, callers, data shapes, or runtime behavior as evidence.
3. **Similarity:** Which existing facility does the new demand most resemble?
4. **Boundary:** What cases are intentionally outside this program's scope?
5. **Proof:** What check would show the theory is now better supported?

## Workflow

1. Inspect the relevant code path, callers, tests, fixtures, docs, and current
   runtime behavior before editing.
2. Put the change beside the closest existing domain concept. Reuse local names,
   validators, data shapes, services, routes, and tests when they already encode
   the idea.
3. Keep the edit surgical. Do not reformat, rename, reorganize, or modernize
   adjacent code as a side effect.
4. Avoid speculative flexibility. Add an abstraction only when the current
   theory already has multiple real cases that need it.
5. Preserve invariants instead of patching around them. If the invariant is
   unclear, gather more context before changing behavior.
6. Verify the behavior that matters: reproduce a bug before fixing it, exercise
   the user-visible path for a feature, or prove behavior stayed the same for a
   refactor.

## Stop Conditions

- The change requires special cases that do not match existing names or
  boundaries.
- Two areas encode the same domain concept differently and the task depends on
  choosing between them.
- The obvious implementation is a broad rewrite or a one-caller abstraction.
- The code's purpose cannot be mapped back to the real-world activity.
- Product, domain, legal, security, or data policy decisions are needed before
  the code can be made correct.

## Review Mode

When reviewing, lead with concrete risks, regressions, misplaced behavior,
duplicated domain concepts, speculative flexibility, and missing tests. If no
issue is found, say so directly and state any residual test gap.

## Response Shape

```text
Theory: [world rule -> program location]
Changed: [what changed]
Verified: [checks run]
Risk: [meaningful residual risk]
```
