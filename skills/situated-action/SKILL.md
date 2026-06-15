---
name: situated-action
description: "Use when coding, debugging, or operating interactive workflows where plans must adapt to local context, user actions, runtime evidence, and contingencies."
---

# Situated Action

Use this skill when a coding plan is useful but cannot be treated as a script
that determines action.

## Core Idea

Suchman's situated action frame treats plans as resources for action. Real work
unfolds in local situations: user feedback, runtime behavior, logs, tools,
errors, and artifacts can make a previously sensible plan wrong or incomplete.

## Before Acting

Answer briefly:

1. **Plan:** What plan are you currently following?
2. **Situation:** What local evidence has appeared: files, tests, logs, user
   messages, runtime state, or tool output?
3. **Mismatch:** What part of the plan no longer fits the situation?
4. **Adjustment:** What is the smallest plan revision that respects the new
   evidence?
5. **Proof:** What immediate check shows the revised action is grounded?

## Workflow

1. Start with a plan only as a guide. Do not continue a checklist when local
   evidence contradicts it.
2. Inspect the current situation before applying a canned workflow: branch
   state, dirty files, failing command output, user correction, service state,
   or real UI behavior.
3. When evidence changes, revise the plan in place and explain the revised next
   step briefly.
4. Prefer reversible, observation-producing moves when the situation is
   uncertain.
5. Keep user interaction situated too: respond to the newest user message and
   current workspace, not to an older intended path.
6. Verify each adapted step with the closest available evidence before moving to
   the next dependent action.

## Stop Conditions

- The plan requires ignoring fresh evidence from the user, tests, logs, or
  runtime behavior.
- The task needs a stable module boundary theory rather than adaptive action;
  consider information hiding.
- You cannot observe the situation that the next step depends on.
- Continuing would make irreversible changes before the local situation is
  understood.

## Response Shape

```text
Theory: [plan as resource -> situated evidence]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
