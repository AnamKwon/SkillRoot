---
name: activity-theory
description: "Use when changing code for workflows where tools, rules, roles, community, division of labor, and the object of work interact."
---

# Activity Theory

Use this skill when a code change affects a work system, not just a local
function.

## Core Idea

Engeström's activity theory analyzes work as an activity system: subject,
object, tools, rules, community, division of labor, and outcome. Failures often
come from contradictions between these elements, not from a missing feature in
isolation.

## Before Acting

Answer briefly:

1. **Subject:** Who or what actor is doing the work?
2. **Object:** What object of work is being transformed?
3. **Tools:** Which tools, APIs, scripts, UIs, models, or data formats mediate
   the work?
4. **Rules/Roles:** What rules, permissions, ownership, or division of labor
   shape the workflow?
5. **Contradiction:** Which element conflicts with another, and what check would
   show the conflict is reduced?

## Workflow

1. Map the activity system before coding: subject, object, tools, rules,
   community, division of labor, and outcome.
2. Identify contradictions: tool vs rule, role vs interface, data object vs
   workflow, automation vs human approval, or community need vs local shortcut.
3. Place the code change at the element that actually creates the contradiction.
4. Avoid optimizing one actor's step while making the whole activity harder.
5. Keep workflow evidence visible in tests, fixtures, docs, or UI states where
   the code alone would hide it.
6. Verify against the workflow outcome, not only a function-level assertion.

## Stop Conditions

- You cannot identify the subject and object of the activity.
- The change would solve a local task while worsening the shared workflow.
- A policy, ownership, or role decision is required before code can be correct.
- The task is only about a volatile implementation decision; use information
  hiding instead.

## Response Shape

```text
Theory: [activity-system contradiction -> code location]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
