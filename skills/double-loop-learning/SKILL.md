---
name: double-loop-learning
description: "Use when debugging repeated failures, writing postmortems, changing policies, or modifying code where underlying assumptions must be revised, not only actions corrected."
---

# Double Loop Learning

Use this skill when a bug or process keeps returning and a local fix is probably
only single-loop correction.

## Core Idea

Single-loop learning corrects actions while leaving governing variables intact.
Double-loop learning questions and changes the governing assumptions, policies,
metrics, defaults, or incentives that made the failing action reasonable.

## Before Acting

Answer briefly:

1. **Error:** What failure, regression, or repeated workaround appeared?
2. **Single Loop:** What direct action would correct this instance?
3. **Governing Variable:** What assumption, metric, default, policy, or
   incentive made the bad action likely?
4. **Double Loop:** What rule or premise should change?
5. **Proof:** What future case would fail before and pass after the premise
   changes?

## Workflow

1. Fix urgent harm only as far as needed to create room for analysis.
2. Separate instance correction from governing-variable correction.
3. Inspect evidence from repeated incidents, tests, defaults, alerts, review
   comments, docs, metrics, or user behavior.
4. Name the assumption that made the failure rational inside the old system.
5. Change the narrowest governing variable: invariant, policy, threshold,
   default, validation rule, review rule, test expectation, or ownership rule.
6. Verify both loops: the current failure is corrected and the old assumption no
   longer silently permits the next one.

## Stop Conditions

- There is only one isolated failure and no evidence of a governing assumption.
- The proposed policy change is broader than the evidence supports.
- The needed governing variable is a product, legal, security, or org decision
  outside code authority.
- The issue is still ambiguous; use sensemaking before changing assumptions.

## Response Shape

```text
Theory: [single-loop fix -> governing variable changed]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
