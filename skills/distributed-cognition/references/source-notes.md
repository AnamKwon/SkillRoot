# Source Notes: distributed-cognition

- Primary source: Cognition in the Wild
- Author: Edwin Hutchins
- Year: 1995
- URL: https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/
- Supporting source: The Distributed Cognition Perspective on Human Interaction
- Supporting URL: https://pages.ucsd.edu/~ehutchins/integratedCogSci/DCOG-Interaction.pdf

## Fallback Sources

- UCSD interaction paper: https://pages.ucsd.edu/~ehutchins/integratedCogSci/DCOG-Interaction.pdf

## Key Concepts

- Cognitive work can be distributed across people, artifacts, representations, and environments.
- Software operations often depend on logs, dashboards, runbooks, schemas, queues, and handoffs.
- Correctness can fail when information is represented in the wrong place or not propagated.

## Agent Translation

Use it to map information flow and update the artifact another actor depends on.

## Common Misuse

Do not fix code locally while leaving dashboards, runbooks, alerts, or schemas inconsistent.

## Source Mapping

Distributed representation -> propagation path -> whole-system verification.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
