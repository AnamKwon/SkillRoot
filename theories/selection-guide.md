# Theory Skill Selection Guide

Use this guide before loading a specific skill when several theories could apply.
Prefer the primary skill when it names the current problem directly; use the
alternatives when the stop conditions in that skill point elsewhere.

| Situation | Primary Skill | Alternatives |
| --- | --- | --- |
| Preserve domain-program mapping while editing code | `programming-as-theory-building` | domain-driven-design, information-hiding |
| Choose a module or API boundary | `information-hiding` | design-by-contract, conways-law |
| Align architecture with teams or ownership | `conways-law` | activity-theory, distributed-cognition |
| Model complex business rules | `domain-driven-design` | programming-as-theory-building |
| Specify API obligations and guarantees | `design-by-contract` | cleanroom-software-engineering |
| Implement behavior test-first | `test-driven-development` | cleanroom-software-engineering, stepwise-refinement |
| Refine a high-level algorithm | `stepwise-refinement` | structured-programming |
| Reason about many possible executions | `abstract-interpretation` | structured-programming |
| Simplify without erasing domain rules | `essential-complexity` | domain-driven-design |
| Improve human-facing APIs or configs | `cognitive-dimensions` | literate-programming |
| Clarify code for maintainers | `literate-programming` | programming-as-theory-building |
| Untangle messy incidents or failures | `sensemaking` | reflective-practice, double-loop-learning |
| Adapt a plan after new evidence | `situated-action` | reflective-practice |
| Reframe a surprising debug result | `reflective-practice` | sensemaking |
| Prevent repeated failures | `double-loop-learning` | sensemaking |
| Analyze workflow-level contradictions | `activity-theory` | distributed-cognition |
| Trace operational knowledge across artifacts | `distributed-cognition` | activity-theory |
| Handle contested product or architecture work | `wicked-problems` | sensemaking |
| Use a recurring design solution | `design-patterns` | information-hiding, domain-driven-design |
| Build high-reliability increments | `cleanroom-software-engineering` | design-by-contract |
| Refactor tangled control flow | `structured-programming` | test-driven-development |

## Boundary Rules

- If the problem is ambiguous, start with `sensemaking` before choosing a design theory.
- If fresh evidence invalidates the plan, switch to `situated-action` before continuing.
- If a code change is already well bounded, prefer `programming-as-theory-building` and only add a specialized skill for the dominant force.
- If a skill would introduce ceremony for one caller, choose the simpler alternative named in its stop conditions.
