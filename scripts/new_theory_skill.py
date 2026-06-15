#!/usr/bin/env python3
"""Create a theory skill skeleton from theories/catalog.yml."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "theories" / "catalog.yml"
TEMPLATE = ROOT / "templates" / "theory-skill" / "SKILL.md.template"


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_catalog_blocks() -> dict[str, str]:
    text = CATALOG.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^  - slug: ([a-z0-9-]+)\n", text, re.MULTILINE))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[start:end]
    return blocks


def scalar(block: str, key: str) -> str:
    match = re.search(rf"^    {re.escape(key)}: \"?([^\n\"]+)\"?$", block, re.MULTILINE)
    if not match:
        die(f"catalog entry missing {key!r}")
    return match.group(1)


def list_values(block: str, key: str) -> list[str]:
    match = re.search(rf"^    {re.escape(key)}:\n((?:      - .+\n)+)", block, re.MULTILINE)
    if not match:
        return []
    return [line.strip()[2:].strip('"') for line in match.group(1).splitlines()]


def nested_scalar(block: str, section: str, key: str) -> str:
    pattern = rf"^    {re.escape(section)}:\n(?:      .+\n)*?      {re.escape(key)}: \"?([^\n\"]+)\"?"
    match = re.search(pattern, block, re.MULTILINE)
    if not match:
        return ""
    return match.group(1)


def render(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        die("usage: new_theory_skill.py <theory-slug>")

    slug = argv[1]
    blocks = read_catalog_blocks()
    if slug not in blocks:
        die(f"unknown theory slug {slug!r}")

    block = blocks[slug]
    skill_name = scalar(block, "skill_name")
    agent_use = scalar(block, "agent_use")
    title = nested_scalar(block, "primary_source", "title") or skill_name.replace("-", " ").title()
    author = nested_scalar(block, "primary_source", "author")
    year = nested_scalar(block, "primary_source", "year")
    url = nested_scalar(block, "primary_source", "url")
    focus = list_values(block, "draft_focus")

    skill_dir = ROOT / "skills" / skill_name
    references_dir = skill_dir / "references"
    if skill_dir.exists():
        die(f"{skill_dir.relative_to(ROOT)} already exists")

    references_dir.mkdir(parents=True)
    workflow = "\n".join(f"{index}. {item}" for index, item in enumerate(focus, start=1))
    if not workflow:
        workflow = "1. Inspect the situation.\n2. Apply the theory cautiously.\n3. Verify the result."

    skill_text = render(
        TEMPLATE.read_text(encoding="utf-8"),
        {
            "skill_name": skill_name,
            "agent_use": agent_use,
            "title": skill_name.replace("-", " ").title(),
            "theory_label": title,
            "core_idea": f"Start from {author}'s {year} work, then adapt only the parts that directly guide agent behavior.",
            "workflow": workflow,
        },
    )

    source_notes = [
        f"# Source Notes: {skill_name}",
        "",
        f"- Primary source: {title}",
        f"- Author: {author}",
        f"- Year: {year}",
        f"- URL: {url}",
        "",
        "## Drafting Notes",
        "",
        "Summarize only the concepts needed for agent behavior. Do not turn the skill",
        "into a literature review.",
        "",
    ]

    (skill_dir / "SKILL.md").write_text(skill_text, encoding="utf-8")
    (references_dir / "source-notes.md").write_text("\n".join(source_notes), encoding="utf-8")

    print(f"created {skill_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

