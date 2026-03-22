#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata


PLATFORMS = (
    "x-twitter",
    "linkedin",
    "reddit",
    "instagram",
    "tiktok",
    "youtube",
)

HASHTAG_PATTERN = re.compile(r"(?<!\w)#[A-Za-z0-9_]+")
HOOK_PATTERN = re.compile(
    r"(^\s*(how|why|what|when|stop|start|the|i|we|most|if|your)\b)|[:?!]",
    re.IGNORECASE,
)


def build_parser() -> argparse.ArgumentParser:
    examples = """Examples:
  python3 scripts/adapt-cross-platform.py --text "Hot take: consistency beats hacks. #growth #marketing 🚀🔥🙂" --source linkedin --targets x-twitter,reddit
  python3 scripts/adapt-cross-platform.py --text "3 lessons from shipping every week" --source x-twitter --targets linkedin,instagram,youtube
"""
    parser = argparse.ArgumentParser(
        description="Adapt social post text for multiple platforms.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--text", required=True, help="Source content to adapt.")
    parser.add_argument(
        "--source",
        required=True,
        choices=PLATFORMS,
        help="Original platform for the input text.",
    )
    parser.add_argument(
        "--targets",
        required=True,
        help="Comma-separated target platforms.",
    )
    return parser


def parse_targets(raw_targets: str) -> list[str]:
    targets = [item.strip() for item in raw_targets.split(",") if item.strip()]
    invalid = [item for item in targets if item not in PLATFORMS]
    if not targets:
        raise ValueError("at least one target platform is required")
    if invalid:
        raise ValueError(f"invalid target platform(s): {', '.join(invalid)}")
    return targets


def is_emoji(char: str) -> bool:
    if not char:
        return False
    category = unicodedata.category(char)
    if category == "So":
        return True
    codepoint = ord(char)
    emoji_ranges = (
        (0x1F300, 0x1FAFF),
        (0x2600, 0x27BF),
    )
    return any(start <= codepoint <= end for start, end in emoji_ranges)


def limit_emojis(text: str, max_emojis: int) -> str:
    kept = 0
    output: list[str] = []
    for char in text:
        if is_emoji(char):
            if kept < max_emojis:
                output.append(char)
                kept += 1
            continue
        output.append(char)
    return "".join(output)


def remove_all_emojis(text: str) -> str:
    return "".join(char for char in text if not is_emoji(char))


def limit_hashtags(text: str, max_hashtags: int) -> str:
    kept = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal kept
        kept += 1
        return match.group(0) if kept <= max_hashtags else ""

    cleaned = HASHTAG_PATTERN.sub(replace, text)
    return normalize_spacing(cleaned)


def remove_all_hashtags(text: str) -> str:
    return normalize_spacing(HASHTAG_PATTERN.sub("", text))


def normalize_spacing(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def first_segment(text: str) -> str:
    return text.splitlines()[0].strip() if text.splitlines() else text.strip()


def has_hook(text: str) -> bool:
    preview = text[:210].strip()
    return bool(HOOK_PATTERN.search(preview))


def adapt_text(text: str, platform: str) -> dict[str, object]:
    warnings: list[str] = []
    adapted = text

    if platform == "x-twitter":
        if len(adapted) > 275:
            warnings.append("content exceeded 275 characters and was truncated")
            adapted = adapted[:275].rstrip()
        adapted = limit_hashtags(adapted, 1)
        adapted = limit_emojis(adapted, 3)
    elif platform == "linkedin":
        if len(adapted) > 3000:
            warnings.append("content exceeds LinkedIn's 3000 character limit")
        if not has_hook(adapted):
            warnings.append("no obvious hook detected in the first 210 characters")
        adapted = limit_hashtags(adapted, 3)
    elif platform == "reddit":
        title_portion = first_segment(adapted)
        if len(title_portion) > 300:
            warnings.append("title-like opening exceeds 300 characters")
        adapted = remove_all_hashtags(adapted)
        adapted = remove_all_emojis(adapted)
    elif platform == "instagram":
        if len(adapted) > 2200:
            warnings.append("content exceeds Instagram's 2200 character limit")
        adapted = limit_hashtags(adapted, 5)
    elif platform == "tiktok":
        if len(adapted) > 2200:
            warnings.append("content exceeds TikTok's 2200 character limit")
        adapted = limit_hashtags(adapted, 5)
    elif platform == "youtube":
        if len(first_segment(adapted)) > 100:
            warnings.append("title portion exceeds 100 characters")

    adapted = normalize_spacing(adapted)
    return {
        "platform": platform,
        "text": adapted,
        "char_count": len(adapted),
        "warnings": warnings,
    }


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        targets = parse_targets(args.targets)
    except ValueError as exc:
        parser.error(str(exc))

    result = {
        "adaptations": [adapt_text(args.text, target) for target in targets],
    }
    json.dump(result, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
