#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MARKDOWN_PATH = DATA_DIR / "content-calendar.md"
JSON_PATH = DATA_DIR / "content-calendar.json"

DEFAULT_RATIOS = {
    "educational": 0.40,
    "personal": 0.25,
    "opinion": 0.20,
    "behind-the-scenes": 0.10,
    "promotional": 0.05,
}

PLATFORM_FORMATS = {
    "x-twitter": ("single", "thread"),
    "linkedin": ("text-post", "carousel"),
    "instagram": ("carousel", "reel"),
    "reddit": ("text-post",),
    "tiktok": ("short-video",),
    "youtube": ("short", "long-form"),
}

PLATFORM_TIMES = {
    "x-twitter": ("08:30", "12:15", "17:45"),
    "linkedin": ("09:00", "13:00", "16:30"),
    "instagram": ("10:00", "14:30", "18:30"),
    "reddit": ("11:00", "15:00", "19:00"),
    "tiktok": ("12:00", "18:00", "20:00"),
    "youtube": ("09:30", "15:30", "19:30"),
}


def build_parser() -> argparse.ArgumentParser:
    examples = """Examples:
  python3 scripts/generate-calendar.py --weeks 4 --platforms "x-twitter,linkedin,instagram" --pillars "educational,personal,opinion" --frequency "5,3,3"
  python3 scripts/generate-calendar.py --weeks 2 --platforms "x-twitter,linkedin" --pillars "educational,opinion" --frequency "4,2"
"""
    parser = argparse.ArgumentParser(
        description="Generate a multi-week content calendar.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--weeks", required=True, type=int, help="Number of weeks to plan.")
    parser.add_argument("--platforms", required=True, help="Comma-separated platform list.")
    parser.add_argument("--pillars", required=True, help="Comma-separated primary content pillars.")
    parser.add_argument(
        "--frequency",
        required=True,
        help="Comma-separated weekly post counts matching the platforms list.",
    )
    return parser


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def expand_pillars(requested: list[str]) -> list[str]:
    ordered = []
    for pillar in requested + list(DEFAULT_RATIOS):
        if pillar not in ordered:
            ordered.append(pillar)
    return ordered


def allocate_by_ratio(total: int, pillars: list[str]) -> list[str]:
    ratios = {pillar: DEFAULT_RATIOS.get(pillar, 0.0) for pillar in pillars}
    ratio_sum = sum(ratios.values())
    if ratio_sum == 0:
        equal_share = 1 / len(pillars)
        ratios = {pillar: equal_share for pillar in pillars}
        ratio_sum = 1.0

    normalized = {pillar: ratios[pillar] / ratio_sum for pillar in pillars}
    raw_counts = {pillar: total * normalized[pillar] for pillar in pillars}
    counts = {pillar: int(raw_counts[pillar]) for pillar in pillars}
    remaining = total - sum(counts.values())

    remainders = sorted(
        pillars,
        key=lambda pillar: (raw_counts[pillar] - counts[pillar], normalized[pillar]),
        reverse=True,
    )
    for pillar in remainders[:remaining]:
        counts[pillar] += 1

    sequence: list[str] = []
    for pillar in pillars:
        sequence.extend([pillar] * counts[pillar])

    return sequence


def evenly_spaced_day_indexes(posts_per_week: int) -> list[int]:
    if posts_per_week <= 1:
        return [0]
    indexes = []
    for i in range(posts_per_week):
        value = round(i * 6 / (posts_per_week - 1))
        while value in indexes and value < 6:
            value += 1
        while value in indexes and value > 0:
            value -= 1
        indexes.append(value)
    return sorted(indexes)


def topic_placeholder(pillar: str, platform: str, counter: int) -> str:
    return f"[{pillar} topic {counter} for {platform}]"


def generate_entries(
    weeks: int,
    platforms: list[str],
    frequencies: list[int],
    pillars: list[str],
) -> list[dict[str, object]]:
    total_posts = weeks * sum(frequencies)
    pillar_sequence = allocate_by_ratio(total_posts, pillars)
    pillar_index = 0
    entries: list[dict[str, object]] = []
    platform_counters = defaultdict(int)

    start = date.today()

    for week_index in range(weeks):
        week_start = start + timedelta(days=week_index * 7)
        for platform, posts_per_week in zip(platforms, frequencies):
            day_indexes = evenly_spaced_day_indexes(posts_per_week)
            formats = PLATFORM_FORMATS.get(platform, ("post",))
            times = PLATFORM_TIMES.get(platform, ("09:00",))

            for post_index, day_index in enumerate(day_indexes):
                current_date = week_start + timedelta(days=day_index)
                pillar = pillar_sequence[pillar_index]
                pillar_index += 1
                platform_counters[(platform, pillar)] += 1
                fmt = formats[post_index % len(formats)]
                time_value = times[post_index % len(times)]

                notes = ""
                if post_index == 0 and fmt in {"thread", "carousel", "long-form"}:
                    notes = "ANCHOR"

                entries.append(
                    {
                        "date": current_date.isoformat(),
                        "time": time_value,
                        "platform": platform,
                        "format": fmt,
                        "pillar": pillar,
                        "topic": topic_placeholder(
                            pillar, platform, platform_counters[(platform, pillar)]
                        ),
                        "hook_direction": f"Lead with a clear {pillar} angle for {platform}.",
                        "status": "idea",
                        "content_id": None,
                        "notes": notes,
                    }
                )

    entries.sort(key=lambda item: (item["date"], item["time"], item["platform"]))
    return entries


def format_time(value: str) -> str:
    hour, minute = value.split(":")
    hour_int = int(hour)
    suffix = "AM" if hour_int < 12 else "PM"
    hour_12 = hour_int % 12 or 12
    return f"{hour_12}:{minute} {suffix}"


def write_markdown(entries: list[dict[str, object]], weeks: int) -> None:
    lines = [f"# Content Calendar - {date.today():%B %Y}", ""]
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)

    start = date.today()
    for entry in entries:
        entry_date = date.fromisoformat(str(entry["date"]))
        week_number = ((entry_date - start).days // 7) + 1
        grouped[week_number].append(entry)

    for week_number in range(1, weeks + 1):
        week_entries = grouped.get(week_number, [])
        if not week_entries:
            continue
        first = date.fromisoformat(str(week_entries[0]["date"]))
        last = date.fromisoformat(str(week_entries[-1]["date"]))
        lines.append(f"## Week {week_number}: {first.isoformat()} to {last.isoformat()}")
        lines.append("")
        lines.append("| Day | Date | Time | Platform | Format | Pillar | Topic | Status |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for entry in week_entries:
            entry_date = date.fromisoformat(str(entry["date"]))
            lines.append(
                "| {day} | {date} | {time} | {platform} | {format} | {pillar} | {topic} | {status} |".format(
                    day=entry_date.strftime("%A"),
                    date=entry["date"],
                    time=format_time(str(entry["time"])),
                    platform=entry["platform"],
                    format=entry["format"],
                    pillar=entry["pillar"],
                    topic=entry["topic"],
                    status=entry["status"],
                )
            )
        lines.append("")

    MARKDOWN_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.weeks <= 0:
        parser.error("--weeks must be greater than 0")

    platforms = parse_csv(args.platforms)
    requested_pillars = parse_csv(args.pillars)
    frequencies = [int(item) for item in parse_csv(args.frequency)]

    if not platforms:
        parser.error("at least one platform is required")
    if not requested_pillars:
        parser.error("at least one pillar is required")
    if len(platforms) != len(frequencies):
        parser.error("--platforms and --frequency must have the same number of items")
    if any(freq <= 0 for freq in frequencies):
        parser.error("all frequency values must be greater than 0")

    pillars = expand_pillars(requested_pillars)
    entries = generate_entries(args.weeks, platforms, frequencies, pillars)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_markdown(entries, args.weeks)

    payload = {
        "period": {
            "start": date.today().isoformat(),
            "end": (date.today() + timedelta(days=args.weeks * 7 - 1)).isoformat(),
        },
        "entries": entries,
    }
    JSON_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(
        f"Generated {len(entries)} entries across {args.weeks} week(s) "
        f"for {len(platforms)} platform(s)."
    )
    print(f"Markdown: {MARKDOWN_PATH}")
    print(f"JSON: {JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
