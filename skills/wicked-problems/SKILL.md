---
name: wicked-problems
description: "Use when coding for ill-structured product, policy, architecture, or planning work where defining the problem changes the solution space."
---

# Wicked Problems

Use this skill when a request looks like a coding task but the problem definition
is contested, value-laden, or changes as solutions are proposed.

## Core Idea

Rittel and Webber contrast tame problems with wicked problems: in wicked
problems, there is no final problem statement, no single stopping rule, and every
solution changes the situation. In software, product and architecture problems
often have this shape.

## Before Acting

Answer briefly:

1. **Stakeholders:** Who values different outcomes or bears different costs?
2. **Frame:** How is the problem currently being defined?
3. **Conflict:** Which criteria conflict: speed, safety, revenue, privacy,
   maintainability, fairness, migration cost, or operability?
4. **Probe:** What small solution would reveal more about the problem?
5. **Rationale:** What issue, position, argument, and decision must be recorded?

## Workflow

1. Do not pretend the task is tame if stakeholders or criteria conflict.
2. State the current problem frame and at least one competing frame.
3. Identify what each proposed code solution would make easier, harder, visible,
   or irreversible.
4. Prefer probes, prototypes, flags, reversible migrations, or narrow
   experiments when the problem definition is still changing.
5. Record design rationale in the closest existing place: ADR, issue, PR
   description, code comment, test name, or final summary.
6. Verify by showing what the chosen implementation reveals or preserves, not by
   claiming final optimality.

## Stop Conditions

- Stakeholder criteria are unknown and the next code change is hard to reverse.
- The user needs a product, legal, policy, or security decision before code can
  be correct.
- You are using wickedness as an excuse to avoid a well-bounded implementation.
- The issue has become a concrete invariant or module boundary problem; switch
  to programming-as-theory-building or information hiding.

## Response Shape

```text
Theory: [problem frame/conflict -> rationale-preserving action]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
