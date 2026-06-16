---
name: cleanroom-software-engineering
description: "Use when generating high-reliability code where defect prevention, precise specifications, incremental development, verification, and statistically meaningful testing matter."
---

# Cleanroom Software Engineering

Use this skill when correctness should be built in through specification and
verification, not discovered mainly by debugging.

## Core Idea

Cleanroom software engineering emphasizes defect prevention: precise
specification, incremental development, correctness reasoning, disciplined
review, and statistically meaningful testing of delivered behavior. For agents,
this means slowing down before code when reliability risk is high.

## Before Acting

Answer briefly:

1. **Specification:** What precise behavior must this increment satisfy?
2. **Increment:** What is the smallest reliable increment to deliver?
3. **Correctness Argument:** Why should the design satisfy the specification?
4. **Usage Profile:** What realistic inputs or scenarios should testing sample?
5. **Proof:** What verification and execution evidence is enough for release?

## Workflow

1. Write a small behavioral specification before coding. Include inputs,
   outputs, state changes, and forbidden behavior.
2. Split work into increments that can be reviewed and verified independently.
3. Reason about correctness before running broad tests: invariants, contracts,
   state transitions, and failure modes.
4. Implement only after the specification and increment boundary are clear.
5. Review for defect prevention: missing cases, ambiguous states, invalid
   assumptions, and unverified dependencies.
6. Test against realistic usage profiles, not only convenient examples.

## Stop Conditions

- The behavior cannot be specified precisely enough to verify.
- The task is exploratory or ambiguous; use sensemaking before cleanroom
  discipline.
- The increment is too large to reason about.
- Tests are being used as a substitute for deciding what correctness means.

## Response Shape

```text
Theory: [specification/increment -> verification evidence]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
