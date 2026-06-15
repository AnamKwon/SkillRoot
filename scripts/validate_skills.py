#!/usr/bin/env python3
"""Validate the minimal SkillRoot repository contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "theories" / "catalog.yml"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def catalog_slugs() -> set[str]:
    text = CATALOG.read_text(encoding="utf-8")
    return set(re.findall(r"^  - slug: ([a-z0-9-]+)$", text, re.MULTILINE))


def validate_skill(path: Path, slugs: set[str]) -> None:
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        fail(f"{path.relative_to(ROOT)} missing SKILL.md")

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{skill_md.relative_to(ROOT)} missing YAML frontmatter")
    if not re.search(r"^name: [a-z0-9-]+$", text, re.MULTILINE):
        fail(f"{skill_md.relative_to(ROOT)} missing valid name")
    if not re.search(r"^description: .+", text, re.MULTILINE):
        fail(f"{skill_md.relative_to(ROOT)} missing description")
    if path.name not in slugs:
        fail(f"{path.relative_to(ROOT)} has no matching catalog slug")


def main() -> int:
    if not CATALOG.exists():
        fail("theories/catalog.yml is missing")

    slugs = catalog_slugs()
    if not slugs:
        fail("theories/catalog.yml has no theory entries")

    if SKILLS.exists():
        for path in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            validate_skill(path, slugs)

    print(f"validated {len(slugs)} catalog entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

