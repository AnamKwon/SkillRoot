# SkillRoot

Theory-grounded skills for coding agents.

This repository collects one skill per theory. Each skill translates an older
theory, paper, or design tradition into a compact agent workflow. The starting
point is Peter Naur's programming-as-theory-building frame and the public skill
layout used in `AnamKwon/programming-as-theory-building-skill`.

## Repository Rules

- Put installable skills under `skills/<skill-name>/SKILL.md`.
- Keep each skill short and procedural. Put long background notes in
  `skills/<skill-name>/references/`.
- Add one theory or skill per branch.
- Name branches with the theory or skill slug, for example
  `skill/situated-action`.
- Record research candidates in `theories/catalog.yml` before generating a
  skill.
- Cite primary papers, books, or stable publisher pages where possible.

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

Then edit:

- `skills/<theory-slug>/SKILL.md`
- `skills/<theory-slug>/references/source-notes.md`

Validate before committing:

```bash
python3 scripts/validate_skills.py
```

Commit and push:

```bash
git add skills/<theory-slug> theories/catalog.yml
git commit -m "Add <theory-slug> skill"
git push -u origin skill/<theory-slug>
```

## Seed Theory Backlog

The initial catalog includes theory candidates that can become separate skills:

- Programming as Theory Building, Peter Naur
- Situated Action, Lucy Suchman
- Reflective Practice, Donald Schön
- Sensemaking, Karl Weick
- Activity Theory and Expansive Learning, Yrjö Engeström
- Distributed Cognition, Edwin Hutchins
- Double-Loop Learning, Chris Argyris and Donald Schön
- Wicked Problems and Design Rationale, Horst Rittel and Melvin Webber

Use the catalog as a research queue, not as a claim that every candidate is
already a finished skill.

