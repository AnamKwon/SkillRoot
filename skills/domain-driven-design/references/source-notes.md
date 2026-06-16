# Source Notes: domain-driven-design

- Primary source: Domain-Driven Design: Tackling Complexity in the Heart of Software
- Author: Eric Evans
- Year: 2003
- URL: https://www.domainlanguage.com/ddd/
- Supporting source: Domain-Driven Design
- Supporting URL: https://www.oreilly.com/library/view/domain-driven-design-tackling/0321125215/

## Key Concepts

- The domain model should use the language of the business domain.
- Bounded contexts protect different meanings of the same term.
- Aggregates and domain concepts should own the invariants they enforce.

## Agent Translation

Use it to name concepts from domain examples, place behavior with invariant owners, and translate across contexts.

## Common Misuse

Do not add DDD tactical patterns as ceremony when CRUD or simple data transformation is enough.

## Source Mapping

Domain language -> bounded context -> invariant owner -> domain example.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
