# Source Notes: structured-programming

- Primary source: Notes on Structured Programming
- Author: Edsger W. Dijkstra
- Year: 1970
- URL: https://www.cs.utexas.edu/~EWD/ewd02xx/EWD249.PDF
- Supporting source: Notes on Structured Programming
- Supporting URL: https://pure.tue.nl/ws/files/2408738/252825.pdf

## Key Concepts

- Programs should be composed from control structures that support reasoning.
- Blocks need clear entry, effect, and continuation.
- The goal is tractable correctness, not style purity.

## Agent Translation

Use it to inspect branches, loops, state changes, and exits before refactoring control flow.

## Common Misuse

Do not force awkward nesting when a guard clause clarifies invalid cases.

## Source Mapping

Control shape -> block reasoning -> branch/loop verification.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
