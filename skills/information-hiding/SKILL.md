---
name: information-hiding
description: "Use when designing or changing modules, APIs, packages, service boundaries, or generated code where likely-changing design decisions should be hidden behind stable interfaces."
---

# Information Hiding

Use this skill when code generation or refactoring needs a defensible module
boundary, not just a convenient file split.

## Core Idea

Parnas's module criterion is to hide design decisions that are likely to
change. A good boundary does not merely group processing steps; it protects
callers from volatile data structures, algorithms, policies, storage choices,
protocol details, or external service quirks.

## Before Acting

Answer briefly:

1. **Decision:** Which design decision is most likely to change?
2. **Owner:** Which existing module should own and hide that decision?
3. **Interface:** What stable operation do callers actually need?
4. **Leak:** What representation, policy, or dependency would leak if exposed?
5. **Proof:** What test or caller check shows the decision can change locally?

## Workflow

1. Inspect current callers, data shapes, tests, and dependency direction before
   changing the boundary.
2. List volatile decisions: representation, algorithm, persistence, protocol,
   vendor, caching, formatting, error mapping, or policy.
3. Put the volatile decision behind the closest existing owner. Create a new
   module only when no current owner can explain the responsibility.
4. Design the public interface around caller intent, not internal mechanics.
5. Keep internal details inaccessible except through deliberate test seams.
6. Verify by changing or substituting one hidden detail in a focused test, or by
   showing callers no longer import or construct that detail.

## Stop Conditions

- The proposed interface exists only for one speculative future caller.
- Hiding the decision would duplicate an existing owner.
- The change makes the domain rule harder to see in names or tests.
- The task is mainly about team ownership or communication paths; consider a
  Conway's Law framing instead.

## Response Shape

```text
Theory: [volatile design decision -> module that hides it]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
