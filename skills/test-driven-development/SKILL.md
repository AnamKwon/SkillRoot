---
name: test-driven-development
description: "Use when implementing behavior where tests should drive design through a red-green-refactor loop and protect the emerging behavior."
---

# Test Driven Development

Use this skill when the next code change should be driven by an executable
behavior example instead of implementation speculation.

## Core Idea

Test-driven development works in small loops: write a failing test for the next
behavior, write the smallest code that passes, then refactor with tests green.
The tests are not just checks after the fact; they shape design pressure.

## Before Acting

Answer briefly:

1. **Behavior:** What observable behavior should exist next?
2. **Red:** What failing test or executable example captures it?
3. **Green:** What is the smallest implementation that can pass honestly?
4. **Refactor:** What duplication, naming, or design pressure appears after
   green?
5. **Proof:** Which test command shows red became green and stayed green?

## Workflow

1. Choose one behavior slice small enough for a short loop.
2. Write or identify a failing test before changing production code when
   practical.
3. Run the test and confirm it fails for the expected reason.
4. Implement the smallest honest code that makes the test pass.
5. Run the focused test, then the nearest relevant suite.
6. Refactor only after green. Keep behavior unchanged and rerun tests.
7. Repeat with the next behavior slice.

## Stop Conditions

- The behavior is not understood well enough to express as a test; use
  sensemaking first.
- The current task is pure exploration, migration plumbing, or generated
  artifact work where a test-first loop would be fake.
- A broad refactor is being attempted before a green safety net exists.
- The test would assert implementation details instead of observable behavior.

## Response Shape

```text
Theory: [red behavior -> green implementation -> refactor]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
