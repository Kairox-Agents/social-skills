#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import re


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
REQUIRED_FRONTMATTER_FIELDS = ("name", "description")
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_LINES = 500
SKILL_DIR_PATTERN = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        raise ValueError("unterminated YAML frontmatter")

    fields: dict[str, str] = {}
    for raw_line in lines[1:end_index]:
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return ["missing SKILL.md"]

    content = skill_md.read_text(encoding="utf-8")
    line_count = len(content.splitlines())
    if line_count > MAX_SKILL_LINES:
        errors.append(f"SKILL.md exceeds {MAX_SKILL_LINES} lines ({line_count})")

    try:
        frontmatter = parse_frontmatter(content)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    for field in REQUIRED_FRONTMATTER_FIELDS:
        if not frontmatter.get(field):
            errors.append(f"missing frontmatter field: {field}")

    if frontmatter.get("name") and frontmatter["name"] != skill_dir.name:
        errors.append(
            f"name field mismatch: expected '{skill_dir.name}', found '{frontmatter['name']}'"
        )

    description = frontmatter.get("description", "")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"description exceeds {MAX_DESCRIPTION_LENGTH} chars ({len(description)})"
        )

    references_dir = skill_dir / "references"
    if references_dir.exists():
        if not references_dir.is_dir():
            errors.append("references exists but is not a directory")
        else:
            for path in sorted(references_dir.rglob("*")):
                if not path.exists():
                    errors.append(f"missing reference path: {path.relative_to(ROOT)}")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"FAIL skills directory not found: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(
        path
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and SKILL_DIR_PATTERN.fullmatch(path.name)
    )
    failures = 0

    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"FAIL {skill_dir.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {skill_dir.name}")

    passed = len(skill_dirs) - failures
    print(f"Summary: {passed}/{len(skill_dirs)} skills passed")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
