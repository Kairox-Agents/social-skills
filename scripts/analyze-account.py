#!/usr/bin/env python3
"""Analyze a normalized JSONL posts file and produce engagement/content reports."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
REPORT_PATH = DATA_DIR / "account-analysis.md"

HASHTAG_RE = re.compile(r"(?<!\w)#[A-Za-z0-9_]+")


def build_parser() -> argparse.ArgumentParser:
    examples = """Examples:
  python3 scripts/analyze-account.py --input-file data/normalized-posts.jsonl
  python3 scripts/fetch-posts.py --provider paste --input-file data/raw.jsonl | python3 scripts/analyze-account.py --input-file -
"""
    parser = argparse.ArgumentParser(
        description="Analyze an account's posts from normalized JSONL.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input-file",
        required=True,
        help="Path to normalized JSONL (use '-' for stdin).",
    )
    return parser


def load_posts(path_str: str) -> list[dict]:
    lines = []
    if path_str == "-":
        lines = sys.stdin.read().splitlines()
    else:
        p = Path(path_str)
        if not p.is_file():
            print(f"Error: file not found: {p}", file=sys.stderr)
            sys.exit(1)
        lines = p.read_text(encoding="utf-8").splitlines()

    posts = []
    for i, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        try:
            posts.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Warning: skipping invalid JSON on line {i}: {e.msg}", file=sys.stderr)
    return posts


def total_engagement(post: dict) -> int:
    eng = post.get("engagement", {})
    return sum(
        int(eng.get(k, 0)) for k in ("likes", "comments", "shares", "saves")
    )


def analyze(posts: list[dict]) -> dict:
    if not posts:
        return {"error": "no posts to analyze"}

    n = len(posts)

    # --- Posting frequency ---
    dates = []
    dow_counter: Counter = Counter()
    for p in posts:
        d = p.get("date", "")
        if not d:
            continue
        try:
            parsed = date.fromisoformat(d[:10])
            dates.append(parsed)
            dow_counter[parsed.strftime("%A")] += 1
        except ValueError:
            pass

    posts_per_week = 0.0
    if len(dates) >= 2:
        span_days = (max(dates) - min(dates)).days or 1
        posts_per_week = round(n / (span_days / 7), 2)
    elif dates:
        posts_per_week = float(n)

    # --- Format distribution ---
    fmt_counter: Counter = Counter()
    for p in posts:
        fmt_counter[p.get("format", "unknown")] += 1
    format_dist = {
        k: {"count": v, "pct": round(v / n * 100, 1)}
        for k, v in fmt_counter.most_common()
    }

    # --- Content length ---
    lengths = [len(p.get("text", "")) for p in posts]
    length_stats = {
        "avg": round(mean(lengths), 1),
        "median": round(median(lengths), 1),
        "min": min(lengths),
        "max": max(lengths),
    }

    # --- Hashtags ---
    all_tags: list[str] = []
    tag_counts_per_post: list[int] = []
    for p in posts:
        tags = HASHTAG_RE.findall(p.get("text", ""))
        tag_counts_per_post.append(len(tags))
        all_tags.extend(t.lower() for t in tags)
    tag_counter = Counter(all_tags)
    hashtag_stats = {
        "avg_per_post": round(mean(tag_counts_per_post), 2) if tag_counts_per_post else 0,
        "top_10": tag_counter.most_common(10),
    }

    # --- Engagement by format ---
    eng_by_fmt: dict[str, list[dict]] = defaultdict(list)
    for p in posts:
        eng_by_fmt[p.get("format", "unknown")].append(p.get("engagement", {}))

    engagement_by_format = {}
    for fmt, engs in eng_by_fmt.items():
        engagement_by_format[fmt] = {
            "avg_likes": round(mean(int(e.get("likes", 0)) for e in engs), 1),
            "avg_comments": round(mean(int(e.get("comments", 0)) for e in engs), 1),
            "avg_shares": round(mean(int(e.get("shares", 0)) for e in engs), 1),
        }

    # --- Top / bottom by engagement ---
    ranked = sorted(posts, key=total_engagement, reverse=True)
    top_n = max(1, n // 10)
    top_posts = [
        {"id": p.get("id", ""), "text": p.get("text", "")[:120], "total_eng": total_engagement(p)}
        for p in ranked[:top_n]
    ]
    bottom_posts = [
        {"id": p.get("id", ""), "text": p.get("text", "")[:120], "total_eng": total_engagement(p)}
        for p in ranked[-top_n:]
    ]

    return {
        "total_posts": n,
        "posting_frequency": {
            "posts_per_week": posts_per_week,
            "day_of_week": dict(dow_counter.most_common()),
        },
        "format_distribution": format_dist,
        "content_length": length_stats,
        "hashtags": hashtag_stats,
        "engagement_by_format": engagement_by_format,
        "top_posts": top_posts,
        "bottom_posts": bottom_posts,
    }


def write_markdown(report: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# Account Analysis Report", ""]

    lines.append(f"**Total posts analyzed:** {report['total_posts']}")
    lines.append("")

    # Frequency
    freq = report["posting_frequency"]
    lines.append("## Posting Frequency")
    lines.append(f"- Posts per week: **{freq['posts_per_week']}**")
    if freq["day_of_week"]:
        lines.append("- Day distribution:")
        for day, count in freq["day_of_week"].items():
            lines.append(f"  - {day}: {count}")
    lines.append("")

    # Format
    lines.append("## Format Distribution")
    for fmt, info in report["format_distribution"].items():
        lines.append(f"- {fmt}: {info['count']} ({info['pct']}%)")
    lines.append("")

    # Length
    cl = report["content_length"]
    lines.append("## Content Length (chars)")
    lines.append(f"- Avg: {cl['avg']} | Median: {cl['median']} | Min: {cl['min']} | Max: {cl['max']}")
    lines.append("")

    # Hashtags
    ht = report["hashtags"]
    lines.append("## Hashtags")
    lines.append(f"- Avg per post: {ht['avg_per_post']}")
    if ht["top_10"]:
        lines.append("- Top 10:")
        for tag, count in ht["top_10"]:
            lines.append(f"  - {tag}: {count}")
    lines.append("")

    # Engagement
    lines.append("## Engagement by Format")
    for fmt, stats in report["engagement_by_format"].items():
        lines.append(f"- **{fmt}**: likes {stats['avg_likes']} / comments {stats['avg_comments']} / shares {stats['avg_shares']}")
    lines.append("")

    # Top posts
    lines.append("## Top Posts (by total engagement)")
    for p in report["top_posts"]:
        lines.append(f"- [{p['id']}] ({p['total_eng']} eng) {p['text']}")
    lines.append("")

    lines.append("## Bottom Posts (by total engagement)")
    for p in report["bottom_posts"]:
        lines.append(f"- [{p['id']}] ({p['total_eng']} eng) {p['text']}")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    posts = load_posts(args.input_file)
    report = analyze(posts)
    write_markdown(report)
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    print(f"\nMarkdown report: {REPORT_PATH}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
