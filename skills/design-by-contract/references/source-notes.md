# Source Notes: design-by-contract

- Primary source: Applying Design by Contract
- Author: Bertrand Meyer
- Year: 1992
- URL: https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf
- Supporting source: Design by Contract
- Supporting URL: https://www.eiffel.com/values/design-by-contract/

## Key Concepts

- A software boundary is a contract between caller obligations and provider guarantees.
- Preconditions, postconditions, and invariants assign responsibility clearly.
- Checks are most useful where they clarify trusted and untrusted boundaries.

## Agent Translation

Use it to state obligations and guarantees, then test valid and invalid contract cases.

## Common Misuse

Do not scatter defensive checks everywhere when one boundary contract would be clearer.

## Source Mapping

Boundary -> preconditions/postconditions/invariants -> contract tests.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
