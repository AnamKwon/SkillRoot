# Source Notes: abstract-interpretation

- Primary source: Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints
- Author: Patrick Cousot and Radhia Cousot
- Year: 1977
- URL: https://www.di.ens.fr/~cousot/publications.www/CousotCousot-POPL-77-ACM-p238--252-1977.pdf
- Supporting source: Patrick Cousot publications on abstract interpretation
- Supporting URL: https://pcousot.github.io/publications.html

## Key Concepts

- Concrete executions are replaced by an abstraction that safely over-approximates behavior.
- The abstraction is only useful when it preserves the property under analysis.
- Precision loss must be reported as false-positive, false-negative, or unmodeled-behavior risk.

## Agent Translation

Use it to choose a property, define the abstract state, trace joins and loops, and state precision limits before claiming safety.

## Common Misuse

Do not use a few sampled executions as if they were a sound abstraction.

## Source Mapping

Property -> abstraction -> precision limits -> focused verification.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
