---
name: cognitive-dimensions
description: "Use when creating or changing APIs, DSLs, config formats, prompts, schemas, CLIs, or code structures that humans must read, write, debug, and modify."
---

# Cognitive Dimensions

Use this skill when generated code creates a notation that people will use:
method names, options, schemas, config files, workflows, prompts, or UI labels.

## Core Idea

Cognitive dimensions are a vocabulary for evaluating notations by the cognitive
work they impose. For code generation, the notation is often the public API,
configuration shape, command syntax, prompt format, or component structure a
human must understand and change later.

## Before Acting

Answer briefly:

1. **Notation:** What will the human read, write, scan, or edit?
2. **Task:** Is the human exploring, configuring, debugging, extending, or
   repeatedly operating it?
3. **Dimensions:** Which dimensions matter most: viscosity, visibility, hidden
   dependencies, premature commitment, error-proneness, consistency, or role
   expressiveness?
4. **Tradeoff:** Which dimension gets worse if another gets better?
5. **Proof:** What example use, test fixture, or review pass shows the notation
   is easier for the real task?

## Workflow

1. Identify the notation surface before optimizing implementation internals.
2. Inspect real examples of use: current call sites, config files, prompts,
   schema instances, command invocations, or docs.
3. Check at least five dimensions:
   - **Viscosity:** how hard it is to make a small change.
   - **Visibility:** how easily needed information can be found.
   - **Hidden dependencies:** what changes elsewhere without being obvious.
   - **Premature commitment:** what decisions must be made too early.
   - **Error-proneness:** what mistakes the notation invites.
4. Improve the notation for the user's task, not just the generator's ease.
5. Keep tradeoffs explicit. Do not pretend a notation can maximize every
   dimension at once.
6. Verify with one realistic before/after example or a fixture that exercises
   the human-facing surface.

## Stop Conditions

- No human-facing notation is being created or changed.
- The proposed change improves one dimension while quietly breaking the user's
  main task.
- The issue is primarily domain volatility or module ownership; use
  information hiding or Conway's Law instead.

## Response Shape

```text
Theory: [notation surface -> cognitive dimensions checked]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
