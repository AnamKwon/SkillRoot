---
name: domain-driven-design
description: "Use when modeling or generating code for complex business domains where ubiquitous language, bounded contexts, aggregates, and domain behavior should shape the implementation."
---

# Domain Driven Design

Use this skill when business meaning, not technical layering, should drive the
model and code boundaries.

## Core Idea

Domain-driven design puts the heart of complex software in the domain model.
Names, boundaries, tests, and behavior should reflect the ubiquitous language
used by domain experts. Different bounded contexts may use the same word to mean
different things.

## Before Acting

Answer briefly:

1. **Language:** What domain terms must appear in code, tests, and examples?
2. **Context:** Which bounded context owns this meaning?
3. **Invariant:** Which aggregate, entity, value object, or service owns the
   rule?
4. **Translation:** Where must language cross a boundary or anti-corruption
   layer?
5. **Proof:** What domain example shows the model preserves the rule?

## Workflow

1. Inspect existing domain names, examples, tests, data shapes, and user
   language before adding classes or tables.
2. Put behavior with the domain concept that owns the invariant. Avoid anemic
   data containers plus distant procedural services when the rule has a clear
   owner.
3. Keep bounded contexts separate when the same term has different meanings.
4. Add translation at boundaries instead of leaking another context's model into
   this one.
5. Use repositories, services, factories, or events only when the current domain
   model needs them, not as default ceremony.
6. Verify with domain examples and invariant-focused tests.

## Stop Conditions

- The domain language is unknown or contested.
- The change is CRUD plumbing with no domain rule; simpler structure may be
  enough.
- The requested model crosses contexts without a translation boundary.
- The issue is mainly a module volatility or API contract problem; use
  information-hiding or design-by-contract instead.

## Response Shape

```text
Theory: [domain language/context -> code model]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
