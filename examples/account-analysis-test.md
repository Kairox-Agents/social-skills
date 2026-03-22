# Account Analysis Test

> Walkthrough: provide sample posts → run analysis script → generate voice profile.

## Test Data

**Input file:** `examples/data/sample-posts.jsonl` (50 synthetic posts from a fictional SaaS founder)

## Step 1: Normalize the Data

If using raw/non-normalized data, pipe through fetch-posts first:
```bash
python3 scripts/fetch-posts.py --provider paste --input-file examples/data/sample-posts.jsonl > /tmp/normalized.jsonl
```

If `sample-posts.jsonl` is already in normalized format, use directly.

## Step 2: Run Account Analysis

```bash
python3 scripts/analyze-account.py --input-file examples/data/sample-posts.jsonl
```

**Expected output (stdout):** JSON report with:
```json
{
  "total_posts": 50,
  "posting_frequency": {
    "posts_per_week": "~4-6",
    "day_of_week": { "...": "..." }
  },
  "format_distribution": {
    "single": { "count": "...", "pct": "..." },
    "thread": { "count": "...", "pct": "..." },
    "text-post": { "count": "...", "pct": "..." },
    "carousel": { "count": "...", "pct": "..." }
  },
  "content_length": {
    "avg": "...", "median": "...", "min": "...", "max": "..."
  },
  "hashtags": {
    "avg_per_post": "...",
    "top_10": [["#hashtag", "count"], "..."]
  },
  "engagement_by_format": { "...": "..." },
  "top_posts": ["..."],
  "bottom_posts": ["..."]
}
```

**Expected file output:** `data/account-analysis.md` with readable Markdown summary.

**Pass criteria:**
- [ ] JSON is valid and parseable
- [ ] All sections present (frequency, format, length, hashtags, engagement, top/bottom)
- [ ] Top 10% posts identified correctly (sorted by total engagement)
- [ ] Markdown report is human-readable

## Step 3: Generate Voice Profile (Agent Step)

**User input to agent:**
```
Analyze this account data and generate a voice profile:
[paste or reference the analysis JSON]
```

**Expected agent behavior:**
1. Agent reads `account-analysis/SKILL.md`
2. Uses the analysis data to identify patterns
3. Generates `voice-profile.md` with:

```markdown
# Voice Profile — [Account Name]

## Tone
- [Primary tone descriptors based on top-performing content]
- [What the audience responds to]

## Patterns That Work
- [Format preferences based on engagement data]
- [Content length sweet spot]
- [Hook styles that perform]
- [Hashtag usage that works]

## Patterns That Don't Work
- [Formats with low engagement]
- [Topics/angles that underperform]

## Recommended Voice Settings
- Tone: [specific descriptors]
- Avoid: [specific things to avoid]
- Posting cadence: [based on frequency analysis]
- Best formats: [ranked by engagement]

## Platform-Specific Notes
- [Platform 1]: [what works here specifically]
- [Platform 2]: [what works here specifically]
```

**Pass criteria:**
- [ ] Voice profile reflects actual data patterns (not generic advice)
- [ ] Top-performing formats highlighted
- [ ] Underperforming patterns identified
- [ ] Recommendations are specific and actionable
- [ ] Can be plugged into social-context config.json voice section
