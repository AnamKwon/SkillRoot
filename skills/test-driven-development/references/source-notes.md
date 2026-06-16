# Source Notes: test-driven-development

- Primary source: Test-Driven Development: By Example
- Author: Kent Beck
- Year: 2002
- URL: https://dl.acm.org/doi/10.5555/579193
- Supporting source: Test Driven Development
- Supporting URL: https://www.martinfowler.com/bliki/TestDrivenDevelopment.html

## Key Concepts

- A failing test expresses the next behavior before production code changes.
- The smallest honest implementation makes the test pass.
- Refactoring happens after green while tests preserve behavior.

## Agent Translation

Use it to choose one behavior slice, observe red, implement green, and refactor under the test.

## Common Misuse

Do not write tests that assert implementation details instead of observable behavior.

## Source Mapping

Behavior slice -> red test -> green code -> refactor proof.

## Drafting Notes

Keep the runnable skill concise. Move detailed theory reminders here, and
only load this file when the task needs source grounding or misuse checks.
