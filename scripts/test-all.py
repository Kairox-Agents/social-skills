#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
VALIDATE_SCRIPT = ROOT / "scripts" / "validate-skills.py"
OMNI_TEST = ROOT / "omni-viral-humanizer" / "test.py"
PLATFORM_FILES = (
    "x-twitter.md",
    "linkedin.md",
    "reddit.md",
    "instagram.md",
    "tiktok.md",
    "youtube.md",
)


def run_subprocess(script_path: Path) -> bool:
    result = subprocess.run([sys.executable, str(script_path)], cwd=ROOT)
    return result.returncode == 0


def main() -> int:
    checks: list[tuple[str, bool]] = []

    checks.append(("validate-skills.py", run_subprocess(VALIDATE_SCRIPT)))
    checks.append(("omni-viral-humanizer/test.py", run_subprocess(OMNI_TEST)))

    platforms_dir = ROOT / "skills" / "social-context" / "references" / "platforms"
    for filename in PLATFORM_FILES:
        path = platforms_dir / filename
        checks.append((f"platform reference {filename}", path.is_file()))

    anti_patterns = (
        ROOT / "skills" / "social-copywriting" / "references" / "anti-patterns.md"
    )
    checks.append(("social-copywriting anti-patterns.md", anti_patterns.is_file()))

    skill_io_map = ROOT / "SKILL-IO-MAP.md"
    checks.append(("SKILL-IO-MAP.md", skill_io_map.is_file()))

    failed = 0
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"{status} {name}")
        if not passed:
            failed += 1

    print(f"Overall: {'PASS' if failed == 0 else 'FAIL'} ({len(checks) - failed}/{len(checks)} checks passed)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
