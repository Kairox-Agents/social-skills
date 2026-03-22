#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LOG_PATH = DATA_DIR / "content-log.jsonl"


def build_parser() -> argparse.ArgumentParser:
    examples = """Examples:
  python3 scripts/content-log.py add --platform linkedin --format text-post --topic "Why distribution wins" --pillar educational --content "..." --hashtags "distribution,marketing" --cta "Reply with your take"
  python3 scripts/content-log.py list --last 5
  python3 scripts/content-log.py stats
  python3 scripts/content-log.py search --query "distribution"
"""
    parser = argparse.ArgumentParser(
        description="Manage an append-only content log.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Append a new content log entry.")
    add_parser.add_argument("--platform", required=True)
    add_parser.add_argument("--format", required=True)
    add_parser.add_argument("--topic", required=True)
    add_parser.add_argument("--pillar", required=True)
    add_parser.add_argument("--content", required=True)
    add_parser.add_argument("--hashtags", default="")
    add_parser.add_argument("--cta", default="")

    list_parser = subparsers.add_parser("list", help="List recent entries.")
    list_parser.add_argument("--last", type=int, default=10)

    subparsers.add_parser("stats", help="Show summary counts.")

    search_parser = subparsers.add_parser("search", help="Search content and topics.")
    search_parser.add_argument("--query", required=True)

    return parser


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_entries() -> list[dict[str, object]]:
    if not LOG_PATH.exists():
        return []

    entries: list[dict[str, object]] = []
    for raw_line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        entries.append(json.loads(line))
    return entries


def write_entry(entry: dict[str, object]) -> None:
    ensure_data_dir()
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


def print_entry(entry: dict[str, object]) -> None:
    hashtags = ", ".join(entry.get("hashtags", []))
    print(f"[{entry['timestamp']}] {entry['platform']} / {entry['format']} / {entry['pillar']}")
    print(f"ID: {entry['id']}")
    print(f"Topic: {entry['topic']}")
    print(f"CTA: {entry.get('cta', '') or '-'}")
    print(f"Hashtags: {hashtags or '-'}")
    print(f"Content: {entry['content']}")
    print("")


def print_table(counter: Counter[str], title: str) -> None:
    print(title)
    print(f"{'Value':20} Count")
    print(f"{'-' * 20} -----")
    for key, count in sorted(counter.items()):
        print(f"{key:20} {count}")
    print("")


def command_add(args: argparse.Namespace) -> int:
    hashtags = [item.strip() for item in args.hashtags.split(",") if item.strip()]
    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "platform": args.platform,
        "format": args.format,
        "topic": args.topic,
        "pillar": args.pillar,
        "content": args.content,
        "hashtags": hashtags,
        "cta": args.cta,
    }
    write_entry(entry)
    print(f"Added entry {entry['id']} to {LOG_PATH}")
    return 0


def command_list(args: argparse.Namespace) -> int:
    entries = load_entries()
    recent = entries[-args.last :] if args.last > 0 else []
    if not recent:
        print("No entries found.")
        return 0

    for entry in reversed(recent):
        print_entry(entry)
    return 0


def command_stats() -> int:
    entries = load_entries()
    if not entries:
        print("No entries found.")
        return 0

    by_platform = Counter(str(entry.get("platform", "")) for entry in entries)
    by_pillar = Counter(str(entry.get("pillar", "")) for entry in entries)
    by_format = Counter(str(entry.get("format", "")) for entry in entries)

    print(f"Total entries: {len(entries)}\n")
    print_table(by_platform, "By Platform")
    print_table(by_pillar, "By Pillar")
    print_table(by_format, "By Format")
    return 0


def command_search(args: argparse.Namespace) -> int:
    query = args.query.casefold()
    matches = [
        entry
        for entry in load_entries()
        if query in str(entry.get("topic", "")).casefold()
        or query in str(entry.get("content", "")).casefold()
    ]
    if not matches:
        print("No matches found.")
        return 0

    for entry in matches:
        print_entry(entry)
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        return command_add(args)
    if args.command == "list":
        return command_list(args)
    if args.command == "stats":
        return command_stats()
    if args.command == "search":
        return command_search(args)

    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
