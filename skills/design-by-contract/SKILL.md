---
name: design-by-contract
description: "Use when generating or changing APIs, classes, functions, services, or tests where responsibilities should be made explicit through preconditions, postconditions, and invariants."
---

# Design By Contract

Use this skill when reliability depends on making caller obligations and
provider guarantees explicit at code boundaries.

## Core Idea

Design by Contract models software elements as contracts. Callers must satisfy
preconditions; providers must ensure postconditions; objects or modules preserve
invariants. Contracts make responsibility explicit instead of spreading blame
across callers, callees, and tests.

## Before Acting

Answer briefly:

1. **Boundary:** Which function, class, endpoint, service, or module boundary is
   being contracted?
2. **Preconditions:** What must the caller provide or guarantee?
3. **Postconditions:** What must the provider return, change, or preserve?
4. **Invariants:** What must always remain true for the object, module, or data?
5. **Proof:** Which tests or runtime checks verify the contract at the boundary?

## Workflow

1. Inspect existing boundary behavior, validation, type hints, tests, and error
   handling before adding contract language.
2. State preconditions as caller obligations. Reject invalid inputs at the
   boundary closest to the caller.
3. State postconditions as provider guarantees. Test outputs, side effects, and
   persistence effects where they are promised.
4. State invariants as stable truths of an object, module, aggregate, or data
   model.
5. Put checks where they clarify responsibility. Do not duplicate defensive
   checks at every internal hop unless the boundary is untrusted.
6. Verify both valid and invalid contract cases.

## Stop Conditions

- The responsibility boundary is unclear.
- Contracts would duplicate existing validators without clarifying ownership.
- The proposed check encodes a policy decision that has not been decided.
- The task is about discovering the problem frame, not enforcing a known
  boundary; consider wicked problems or sensemaking.

## Response Shape

```text
Theory: [preconditions/postconditions/invariants -> code boundary]
Changed: [what changed, if anything]
Verified: [checks run]
Risk: [remaining uncertainty]
```
