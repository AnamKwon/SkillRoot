# Source Notes: information-hiding

- Primary source: On the Criteria To Be Used in Decomposing Systems into Modules
- Author: David L. Parnas
- Year: 1972
- URL: https://dl.acm.org/doi/10.1145/361598.361623
- Supporting source: Public copy of On the Criteria To Be Used in Decomposing Systems into Modules
- Supporting URL: https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf

## Fallback Sources

- Public copy PDF: https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf

## Key Concepts

- Modules should hide design decisions likely to change.
- The interface should express stable caller intent rather than internal mechanics.
- A good boundary protects callers from representation, policy, algorithm, or vendor churn.

## Agent Translation

Use it to identify volatile decisions and place them behind the closest existing owner.

## Common Misuse

Do not create broad abstractions for a speculative future caller.

## Source Mapping

Volatile decision -> owning module -> stable interface -> caller proof.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
