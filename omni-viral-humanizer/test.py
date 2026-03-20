#!/usr/bin/env python3
"""Basic contract checks for omni-viral-humanizer skill."""
from pathlib import Path

ROOT = Path(__file__).parent
required = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "references/x/algo-deep-dive.md",
    "references/x/viral-examples.txt",
    "references/linkedin/algo-deep-dive.md",
    "references/linkedin/viral-examples.txt",
    "references/tiktok/algo-deep-dive.md",
    "references/tiktok/viral-examples.txt",
    "templates/viral-templates.md",
    "examples/before-after.md",
    "examples/sample-input-output.json",
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    raise SystemExit(f"Missing required files: {missing}")

skill = (ROOT / "SKILL.md").read_text()
for token in ["name:", "description:", "## Output Contract", "platform_outputs"]:
    if token not in skill:
        raise SystemExit(f"SKILL.md missing token: {token}")

print("PASS: omni-viral-humanizer structure looks valid")
