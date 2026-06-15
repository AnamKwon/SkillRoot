---
name: reflective-practice
description: "Use when designing, debugging, refactoring, or analyzing code where surprises during action should trigger reflection, reframing, and a revised next move."
---

# Reflective Practice

Use this skill when a coding move produces surprise: a test fails differently
than expected, a design no longer fits, or a user correction changes the frame.

## Core Idea

Schön's reflective practitioner reflects in action. The practitioner makes a
move, the situation talks back, and the practitioner reframes the problem while
work is still underway. This is useful for coding when routine application of a
known technique stops fitting the observed system.

## Before Acting

Answer briefly:

1. **Move:** What action did you just take or plan to take?
2. **Back-talk:** What did the code, test, log, UI, or user reveal in response?
3. **Frame:** What assumption about the problem is now questionable?
4. **Reframe:** What new framing better explains the evidence?
5. **Experiment:** What small next move tests the new frame?

## Workflow

1. Name the surprise explicitly before adding another patch.
2. Compare the surprise against the current frame: wrong invariant, wrong
   boundary, wrong user goal, wrong runtime assumption, or wrong test meaning.
3. Reframe the problem in one or two concrete sentences.
4. Make the smallest reversible experiment that would confirm or reject the new
   frame.
5. Capture what changed in the working theory through names, tests, comments, or
   final summary only where that knowledge would otherwise be lost.
6. Continue only after the situation's response is understood well enough for
   the next move.

## Stop Conditions

- You are adding patches without naming what each patch is testing.
- The same surprise repeats and the frame has not changed.
- The task needs plan adaptation to changing context more than reflective
  problem framing; consider situated action.
- The next move is irreversible and the current frame is still unstable.

## Response Shape

```text
Theory: [surprise -> revised frame]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
