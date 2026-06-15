---
name: distributed-cognition
description: "Use when coding, debugging, or designing operational systems where knowledge is distributed across people, tools, artifacts, logs, dashboards, procedures, and code."
---

# Distributed Cognition

Use this skill when correctness depends on a whole socio-technical system, not
only one file or one developer's memory.

## Core Idea

Distributed cognition studies how cognitive work is organized across people,
artifacts, representations, and environments. In software work, the "knowing
system" often includes source code, runbooks, logs, dashboards, queues, tickets,
schemas, CI, deployment tools, and human handoffs.

## Before Acting

Answer briefly:

1. **System:** What people, tools, artifacts, and representations participate?
2. **Representation:** Where is critical state or knowledge encoded?
3. **Propagation:** How does information move between code, tools, and people?
4. **Breakdown:** Where can the representation be lost, delayed, duplicated, or
   misread?
5. **Proof:** What end-to-end check shows the distributed system still knows what
   it needs to know?

## Workflow

1. Expand the unit of analysis beyond a function or individual. Include the
   operational artifacts that carry knowledge.
2. Trace information flow through logs, configs, queues, schemas, dashboards,
   docs, tests, UI states, alerts, and human handoffs.
3. Put generated code where it improves representation or propagation without
   creating hidden parallel knowledge.
4. Keep important state visible at the point of action. Avoid burying
   operational knowledge in unstated conventions.
5. Update or verify the artifact that another actor depends on: contract tests,
   runbooks, events, dashboards, error messages, schemas, or examples.
6. Verify the whole cognitive path, not just the local function.

## Stop Conditions

- You cannot identify where critical knowledge is represented.
- A local code fix would leave dashboards, runbooks, schemas, or alerts lying.
- The issue is mainly a module encapsulation problem; consider information
  hiding instead.
- The next change creates a second source of truth with no synchronization path.

## Response Shape

```text
Theory: [distributed representation -> code/artifact path]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
