#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_SOCIAVAULT_URL = "https://api.sociavault.com/v1/posts"


def build_parser() -> argparse.ArgumentParser:
    examples = """Examples:
  python3 scripts/fetch-posts.py --provider paste --input-file data/raw-posts.jsonl
  python3 scripts/fetch-posts.py --provider sociavault --platform linkedin --handle acme --count 25
"""
    parser = argparse.ArgumentParser(
        description="Fetch posts from a local file or SociaVault and emit normalized JSONL.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--provider",
        required=True,
        choices=("sociavault", "paste"),
        help="Source provider.",
    )
    parser.add_argument("--input-file", help="Path to a local JSONL file for the paste provider.")
    parser.add_argument("--platform", help="Platform name for the SociaVault provider.")
    parser.add_argument("--handle", help="Account handle for the SociaVault provider.")
    parser.add_argument("--count", type=int, default=10, help="Number of posts to fetch.")
    return parser


def coerce_int(value: object) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def normalize_post(record: dict[str, object], fallback_platform: str = "") -> dict[str, object]:
    engagement = record.get("engagement")
    if isinstance(engagement, dict):
        engagement_map = engagement
    else:
        engagement_map = {}

    text = record.get("text") or record.get("content") or record.get("caption") or ""
    normalized = {
        "id": str(record.get("id") or record.get("post_id") or record.get("uuid") or ""),
        "date": str(record.get("date") or record.get("created_at") or record.get("timestamp") or ""),
        "platform": str(record.get("platform") or fallback_platform or ""),
        "text": str(text),
        "engagement": {
            "likes": coerce_int(engagement_map.get("likes", record.get("likes", 0))),
            "comments": coerce_int(engagement_map.get("comments", record.get("comments", 0))),
            "shares": coerce_int(engagement_map.get("shares", record.get("shares", 0))),
            "saves": coerce_int(engagement_map.get("saves", record.get("saves", 0))),
        },
        "format": str(record.get("format") or record.get("post_format") or "unknown"),
        "media_type": str(record.get("media_type") or record.get("type") or "unknown"),
    }
    return normalized


def read_jsonl(path: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON on line {line_number}: {exc.msg}") from exc
        if not isinstance(payload, dict):
            raise ValueError(f"line {line_number} is not a JSON object")
        records.append(payload)
    return records


def fetch_from_paste(args: argparse.Namespace) -> list[dict[str, object]]:
    if not args.input_file:
        raise ValueError("--input-file is required for the paste provider")
    path = Path(args.input_file)
    if not path.is_file():
        raise ValueError(f"input file not found: {path}")
    records = read_jsonl(path)
    return [normalize_post(record) for record in records]


def parse_sociavault_payload(payload: object, fallback_platform: str) -> list[dict[str, object]]:
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict):
        for key in ("posts", "data", "results", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                records = value
                break
        else:
            records = [payload]
    else:
        raise ValueError("unexpected SociaVault response shape")

    normalized: list[dict[str, object]] = []
    for item in records:
        if isinstance(item, dict):
            normalized.append(normalize_post(item, fallback_platform=fallback_platform))
    return normalized


def fetch_from_sociavault(args: argparse.Namespace) -> list[dict[str, object]]:
    missing = [name for name in ("platform", "handle") if not getattr(args, name)]
    if missing:
        raise ValueError(f"missing required argument(s) for sociavault: {', '.join('--' + item for item in missing)}")

    api_key = os.environ.get("SOCIAVAULT_API_KEY")
    if not api_key:
        raise ValueError("SOCIAVAULT_API_KEY is not set")

    base_url = os.environ.get("SOCIAVAULT_API_URL", DEFAULT_SOCIAVAULT_URL)
    query = urllib.parse.urlencode(
        {
            "platform": args.platform,
            "handle": args.handle,
            "count": args.count,
        }
    )
    request = urllib.request.Request(
        f"{base_url}?{query}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "socialskills-fetch-posts/1.0",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            raw_body = response.read().decode(charset)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").strip()
        message = f"SociaVault request failed with HTTP {exc.code}"
        if body:
            message = f"{message}: {body}"
        raise RuntimeError(message) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"SociaVault request failed: {exc.reason}") from exc

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"SociaVault returned invalid JSON: {exc.msg}") from exc

    return parse_sociavault_payload(payload, fallback_platform=args.platform)


def emit_jsonl(records: list[dict[str, object]]) -> None:
    for record in records:
        json.dump(record, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.provider == "paste":
            records = fetch_from_paste(args)
        else:
            records = fetch_from_sociavault(args)
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    emit_jsonl(records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
