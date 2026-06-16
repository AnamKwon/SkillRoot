#!/usr/bin/env python3
"""Validate the SkillRoot repository contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "theories" / "catalog.yml"
README = ROOT / "README.md"
SELECTION_GUIDE = ROOT / "theories" / "selection-guide.md"

REQUIRED_SKILL_SECTIONS = [
    "Core Idea",
    "Workflow",
    "Stop Conditions",
    "Response Shape",
]
REQUIRED_SOURCE_SECTIONS = [
    "Key Concepts",
    "Agent Translation",
    "Common Misuse",
    "Source Mapping",
]


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def catalog_slugs() -> set[str]:
    text = CATALOG.read_text(encoding="utf-8")
    slugs = set(re.findall(r"^  - slug: ([a-z0-9-]+)$", text, re.MULTILINE))
    skill_names = set(re.findall(r"^    skill_name: ([a-z0-9-]+)$", text, re.MULTILINE))
    mismatches = sorted(slugs.symmetric_difference(skill_names))
    if mismatches:
        fail(f"catalog slug and skill_name must match: {', '.join(mismatches)}")
    return slugs


def quoted_yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}: \"(.+)\"$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate_agents_yaml(path: Path, skill_name: str) -> None:
    agents_yaml = path / "agents" / "openai.yaml"
    if not agents_yaml.exists():
        fail(f"{path.relative_to(ROOT)} missing agents/openai.yaml")

    text = agents_yaml.read_text(encoding="utf-8")
    for needle in [
        "interface:",
        "  display_name: ",
        "  short_description: ",
        "  default_prompt: ",
        "policy:",
        "  allow_implicit_invocation: true",
    ]:
        if needle not in text:
            fail(f"{agents_yaml.relative_to(ROOT)} missing {needle.strip()}")

    short_description = quoted_yaml_value(text, "  short_description")
    if short_description is None:
        fail(f"{agents_yaml.relative_to(ROOT)} short_description must be quoted")
    if not 25 <= len(short_description) <= 64:
        fail(f"{agents_yaml.relative_to(ROOT)} short_description must be 25-64 chars")

    default_prompt = quoted_yaml_value(text, "  default_prompt")
    if default_prompt is None:
        fail(f"{agents_yaml.relative_to(ROOT)} default_prompt must be quoted")
    if f"${skill_name}" not in default_prompt:
        fail(f"{agents_yaml.relative_to(ROOT)} default_prompt must mention ${skill_name}")


def validate_source_notes(path: Path) -> None:
    source_notes = path / "references" / "source-notes.md"
    if not source_notes.exists():
        fail(f"{path.relative_to(ROOT)} missing references/source-notes.md")

    text = source_notes.read_text(encoding="utf-8")
    for section in REQUIRED_SOURCE_SECTIONS:
        if f"## {section}" not in text:
            fail(f"{source_notes.relative_to(ROOT)} missing ## {section}")
    for label in ["Primary source:", "Author:", "Year:", "URL:"]:
        if label not in text:
            fail(f"{source_notes.relative_to(ROOT)} missing {label}")


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
    for section in REQUIRED_SKILL_SECTIONS:
        if f"## {section}" not in text:
            fail(f"{skill_md.relative_to(ROOT)} missing ## {section}")
    if "## Before Acting" not in text and "## Before Editing" not in text:
        fail(f"{skill_md.relative_to(ROOT)} missing before-action section")

    validate_source_notes(path)
    validate_agents_yaml(path, path.name)


def main() -> int:
    if not CATALOG.exists():
        fail("theories/catalog.yml is missing")
    if not README.exists():
        fail("README.md is missing")
    if not SELECTION_GUIDE.exists():
        fail("theories/selection-guide.md is missing")

    slugs = catalog_slugs()
    if not slugs:
        fail("theories/catalog.yml has no theory entries")

    if not SKILLS.exists():
        fail("skills directory is missing")

    skill_dirs = {p.name: p for p in SKILLS.iterdir() if p.is_dir()}
    missing = sorted(slugs.difference(skill_dirs))
    extra = sorted(set(skill_dirs).difference(slugs))
    if missing:
        fail(f"catalog entries missing skill directories: {', '.join(missing)}")
    if extra:
        fail(f"skill directories missing catalog entries: {', '.join(extra)}")

    for path in sorted(skill_dirs.values()):
        validate_skill(path, slugs)

    readme_text = README.read_text(encoding="utf-8")
    guide_text = SELECTION_GUIDE.read_text(encoding="utf-8")
    for slug in sorted(slugs):
        if f"skills/{slug}/SKILL.md" not in readme_text:
            fail(f"README.md missing skills/{slug}/SKILL.md")
        if f"`{slug}`" not in guide_text:
            fail(f"selection-guide.md missing `{slug}`")

    print(f"validated {len(slugs)} catalog entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
