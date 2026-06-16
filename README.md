# SkillRoot

Theory-grounded skills for coding agents.

This repository collects one skill per theory. Each skill translates a
software, organizational, design, or cognition theory into a compact agent
workflow with source notes and UI metadata.

## Repository Rules

- Put installable skills under `skills/<skill-name>/SKILL.md`.
- Keep each skill short and procedural. Put source grounding and misuse notes in `skills/<skill-name>/references/source-notes.md`.
- Add one theory or skill per branch, then merge through `main` after validation.
- Record research candidates in `theories/catalog.yml` before generating a skill.
- Keep `agents/openai.yaml` in sync with `SKILL.md` for every skill. This file is
  SkillRoot/Codex skill UI metadata, not an OpenAI API, Assistants, Agents SDK,
  or Custom GPT manifest.
- Cite primary papers, books, or stable publisher pages where possible, and add fallback sources when the primary URL is fragile.

## Current Skills

| Skill | Focus | Source |
| --- | --- | --- |
| [Abstract Interpretation](skills/abstract-interpretation/SKILL.md) | Sound static reasoning with approximations | Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints |
| [Activity Theory](skills/activity-theory/SKILL.md) | Workflow change through activity systems | Learning by Expanding: An Activity-Theoretical Approach to Developmental Research |
| [Cleanroom Engineering](skills/cleanroom-software-engineering/SKILL.md) | Defect prevention with precise specs | Cleanroom Software Engineering |
| [Cognitive Dimensions](skills/cognitive-dimensions/SKILL.md) | Ergonomic checks for code notations | Cognitive Dimensions of Notations: Design Tools for Cognitive Technology |
| [Conway's Law](skills/conways-law/SKILL.md) | Architecture shaped by communication paths | How Do Committees Invent? |
| [Design by Contract](skills/design-by-contract/SKILL.md) | Explicit caller and provider obligations | Applying Design by Contract |
| [Design Patterns](skills/design-patterns/SKILL.md) | Apply patterns only when forces match | Design Patterns: Elements of Reusable Object-Oriented Software |
| [Distributed Cognition](skills/distributed-cognition/SKILL.md) | Trace knowledge across people and tools | Cognition in the Wild |
| [Domain-Driven Design](skills/domain-driven-design/SKILL.md) | Model code around domain language | Domain-Driven Design: Tackling Complexity in the Heart of Software |
| [Double-Loop Learning](skills/double-loop-learning/SKILL.md) | Revise assumptions behind repeated failures | Double Loop Learning in Organizations |
| [Essential Complexity](skills/essential-complexity/SKILL.md) | Separate domain essence from accidents | No Silver Bullet: Essence and Accidents of Software Engineering |
| [Information Hiding](skills/information-hiding/SKILL.md) | Hide volatile decisions behind interfaces | On the Criteria To Be Used in Decomposing Systems into Modules |
| [Literate Programming](skills/literate-programming/SKILL.md) | Align human explanation with code behavior | Literate Programming |
| [Programming as Theory Building](skills/programming-as-theory-building/SKILL.md) | Preserve program theory while changing code | Programming as Theory Building |
| [Reflective Practice](skills/reflective-practice/SKILL.md) | Reframe coding surprises during action | The Reflective Practitioner: How Professionals Think in Action |
| [Sensemaking](skills/sensemaking/SKILL.md) | Build plausible stories from messy cues | Sensemaking in Organizations |
| [Situated Action](skills/situated-action/SKILL.md) | Adapt plans to local runtime evidence | Plans and Situated Actions: The Problem of Human-Machine Communication |
| [Stepwise Refinement](skills/stepwise-refinement/SKILL.md) | Refine specs into code one decision at a time | Program Development by Stepwise Refinement |
| [Structured Programming](skills/structured-programming/SKILL.md) | Keep control flow reasoned and tractable | Notes on Structured Programming |
| [Test-Driven Development](skills/test-driven-development/SKILL.md) | Drive behavior through red-green-refactor | Test-Driven Development: By Example |
| [Wicked Problems](skills/wicked-problems/SKILL.md) | Probe contested product and architecture work | Dilemmas in a General Theory of Planning |

## Choose A Skill

Start with [the selection guide](theories/selection-guide.md) when multiple
skills could apply. The guide maps common coding situations to the most
likely theory and alternatives.

## Add A Theory Skill

Create a branch for the theory:

```bash
git switch main
git pull --ff-only
git switch -c skill/<theory-slug>
```

Generate the skill skeleton from the catalog:

```bash
python3 scripts/new_theory_skill.py <theory-slug>
```

Synchronize generated docs and metadata:

```bash
python3 scripts/sync_skill_artifacts.py
```

When adding or materially changing a skill, update the `SKILL_DATA` entry in
`scripts/sync_skill_artifacts.py` at the same time. That script is the source of
truth for generated `agents/openai.yaml`, enriched `source-notes.md`, README
rows, and the selection guide.

Validate before committing:

```bash
python3 scripts/validate_skills.py
```

Commit and push:

```bash
git add skills/<theory-slug> theories/catalog.yml README.md theories/selection-guide.md
git commit -m "Add <theory-slug> skill"
git push -u origin skill/<theory-slug>
```
