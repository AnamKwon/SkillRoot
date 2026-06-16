---
name: conways-law
description: "Use when designing systems, services, packages, generated code boundaries, or ownership seams where communication paths and team structure shape architecture."
---

# Conway's Law

Use this skill when architecture, package structure, APIs, or service seams must
fit the people who will build and maintain them.

## Core Idea

Conway observed that system designs tend to mirror the communication structures
of the organizations that produce them. A technically neat boundary can fail if
ownership, review, deployment, support, or decision paths cannot sustain it.

## Before Acting

Answer briefly:

1. **Actors:** Who owns, reviews, deploys, supports, or consumes this code?
2. **Communication:** Which handoffs, approvals, or coordination paths matter?
3. **Mirror:** Does the proposed technical boundary mirror those paths, fight
   them, or intentionally reshape them?
4. **Interface:** What contract keeps cross-team coordination explicit?
5. **Proof:** What ownership, CI, deployment, or caller evidence shows the seam
   can be maintained?

## Workflow

1. Inspect current ownership signals: directories, CODEOWNERS, service names,
   package boundaries, deploy units, runbooks, review history, and issue labels.
2. Map the communication path around the change before changing the architecture.
3. Prefer boundaries that make necessary coordination explicit through APIs,
   events, schemas, docs, tests, or release contracts.
4. Avoid creating a shared module that requires constant cross-team negotiation
   unless the organization already has a clear owner for it.
5. If the desired architecture intentionally changes ownership, state that as a
   migration, not just a code refactor.
6. Verify the seam with the closest real coordination artifact: owner approval,
   contract test, deployment check, integration test, or consumer example.

## Stop Conditions

- The change needs an ownership decision the code cannot answer.
- The proposed boundary creates a shared responsibility with no accountable
  owner.
- The issue is mainly volatile implementation detail inside one module; consider
  information hiding instead.
- You cannot identify the consumers or maintainers affected by the seam.

## Response Shape

```text
Theory: [communication path -> technical boundary]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
