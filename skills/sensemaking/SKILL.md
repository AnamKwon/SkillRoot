---
name: sensemaking
description: "Use when debugging ambiguous incidents, failing systems, legacy code, or messy project context where plausible interpretation must precede code changes."
---

# Sensemaking

Use this skill when the problem is not yet clear enough for a direct fix.

## Core Idea

Weick's sensemaking frame treats understanding as ongoing, social, cue-driven,
retrospective, and oriented toward plausible action. In coding work, this means
collecting enough cues to form a testable story before changing the system.

## Before Acting

Answer briefly:

1. **Cues:** What concrete signals are available: errors, logs, diffs, tests,
   traces, user reports, metrics, or code comments?
2. **Story:** What plausible explanation connects those cues?
3. **Identity/Role:** Whose perspective matters: user, operator, maintainer,
   reviewer, service owner, or downstream consumer?
4. **Test:** What observation would strengthen or weaken the story?
5. **Action:** What small action can improve understanding or reduce harm?

## Workflow

1. Gather cues before naming the root cause. Prefer primary evidence over
   inherited explanations.
2. Build a short narrative that links cues to a plausible failure mode or design
   issue.
3. Treat the narrative as provisional. Ask what evidence would make it wrong.
4. Use small diagnostic actions before broad fixes: reproduce, isolate, inspect
   call paths, compare versions, add temporary logging, or run a targeted test.
5. Update the story when new evidence appears. Do not force new cues into the
   first explanation.
6. Only implement a fix when the narrative points to a concrete invariant,
   boundary, dependency, or user workflow.

## Stop Conditions

- The proposed fix is based on a label like "race condition" or "cache issue"
  without supporting cues.
- The evidence supports multiple plausible stories and the next action would be
  high blast radius.
- The task is no longer ambiguous and now needs module design, notation design,
  or simplification theory instead.

## Response Shape

```text
Theory: [cues -> plausible working story]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
