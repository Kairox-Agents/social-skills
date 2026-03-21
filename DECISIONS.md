# SocialSkills — Consolidated Decisions

*Updated: March 19, 2026*

---

## Confirmed Decisions

| # | Question | Decision |
|---|----------|----------|
| 1 | Skill naming | **Flat** (e.g., `social-copywriting`, not `ss-copywriting`) |
| 2 | Pack name | **`social-skills`** (hyphenated per AgentSkills spec) |
| 3 | Repo structure | **Monorepo** — social-skills pack only for now. PM and dev packs later. |
| 4 | License | **MIT** |
| 5 | Install locations | Support `.agents/skills/` (AgentSkills spec), `.claude/skills/` (Claude Code), `~/.openclaw/skills/` (OpenClaw). Install docs for all three. |
| 6 | Context interview | **Both modes**: quick start (5 questions) AND full brand audit (15+). User chooses. |
| 7 | Multi-brand | **Single brand for v1.** Multi-brand in v2. |
| 8 | Account analysis output | **C — Full custom skill generation.** Analyzes account → generates personalized skill with voice DNA, patterns, hook library. |
| 9 | Data sourcing | **Cheapest 3rd party API** (see API research below) |
| 10 | Competitor vs self analysis | **Two separate skills** |
| 11 | Analysis dimensions | See refined list below |
| 12 | Voice DNA output format | Confirmed — plugs into social-context as override |
| 13 | Post count | **Dev mode: 50 posts, Production mode: 500 posts** |
| 14 | Platform-specific skills | **Yes — each platform gets deep coverage**, design to be determined (see below) |
| 15 | YouTube scope | **Both Shorts AND long-form** |
| 16 | Platform update cadence | See recommendation below |
| 17 | Per-platform voice variants | **Yes** — social-context supports voice variants per platform |
| 18 | Taste/quality enforcement | Anti-patterns + taste tiers + cringe detector + curated examples. Iterative improvement. |
| 19 | Voice opinionation level | **Very opinionated** with platform-specific guidance (emoji/hashtag rules differ per platform) |
| 20 | Content length guidance | **Very opinionated**, data-backed, per-platform |
| 21 | Script language | **Python (stdlib) + Markdown output** |
| 22 | Content log schema | **Per-platform schemas** (see below) |
| 23 | Calendar output | See top 3 analysis below |
| 24 | Distribution | **All**: GitHub + ClaHub + OpenClaw registry + `npx skills add` |
| 25 | Plugin grouping | See recommendation below |
| 26 | Contribution model | **Curated until v1 is solid** |

---

## Platforms (v1)

1. **X/Twitter**
2. **LinkedIn**
3. **Reddit**
4. **Instagram**
5. **TikTok**
6. **YouTube** (Shorts + long-form)

---

## Target User

**Solo creators AND SMBs/early-stage startup founders.**

Design for someone who:
- Wears multiple hats (founder = marketer = content creator)
- Has 2-5 hours/week for social media
- Needs to be on 3-6 platforms but can't be an expert on all of them
- Values quality over volume
- Wants to build a real audience, not just "post content"

---

## Account Analysis Feature — Data API Research

### Pricing Comparison (for scraping social media posts)

| Provider | Model | Twitter | Instagram | LinkedIn | TikTok | Reddit | YouTube | All 6 Platforms |
|----------|-------|---------|-----------|----------|--------|--------|---------|----------------|
| **SociaVault** | Pay-per-credit, never expire | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **$29 for 6K credits** (~6K API calls) |
| **TwitterAPI.io** | Pay-per-use | ✅ ($0.15/1K) | ❌ | ❌ | ❌ | ❌ | ❌ | Twitter only |
| **Apify** | Subscription + compute | ✅ | ✅ | ⚠️ (often broken) | ✅ | ✅ | ✅ | **$49/mo + variable compute** |
| **Bright Data** | Enterprise | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **$500+/mo** |
| **Data365** | Subscription | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | **$300+/mo** |
| **PhantomBuster** | Subscription (time-based) | ⚠️ | ✅ | ✅ | ⚠️ | ❌ | ❌ | **$69+/mo** |
| **RapidAPI marketplace** | Per-API varies | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | **$10-100/mo per API** |

### MCP Servers (Free/Open Source options)

| MCP Server | Platform | Notes |
|------------|----------|-------|
| Xpoz MCP | Twitter, Instagram, TikTok | Remote-only, 1.5B+ posts indexed, no install needed |
| stickerdaniel/linkedin-mcp-server | LinkedIn | Profiles, companies, jobs |
| saginawj/mcp-reddit-companion | Reddit | Natural language Reddit interaction |
| stephen9412/youtube-mcp-server | YouTube | Video, channel, playlist management |
| rafaljanicki/x-twitter-mcp-server | Twitter | Tweet management, user engagement |
| TuliEscobar/mcp-linkedin | LinkedIn | Unofficial API access |

### Recommendation

**Primary: SociaVault** — Cheapest all-in-one option for our use case.

- $29 gets 6,000 credits (covers ~6K API calls)
- All 6 of our platforms supported
- Credits never expire
- Unified JSON format across platforms
- Simple REST API (no Actor configs like Apify)
- For 500-post production analysis across 6 platforms: ~500 credits per account × 6 platforms = ~3,000 credits = one $29 pack

**Fallback: Apify** (Philip already has experience with it)
- Good for complex automation beyond simple data fetch
- Variable compute costs make it less predictable
- Community Actors break when platforms update

**Free supplement: MCP servers** for platforms where they work well
- Reddit MCP + YouTube MCP are solid free options
- Twitter MCP servers exist but reliability varies

**Architecture**: The account-analysis skill should have a **pluggable data layer** — a `scripts/fetch_posts.py` that abstracts the API provider. User configures their API key in `config.json`. Skill works with SociaVault by default, Apify as fallback, raw paste/upload as no-API option.

---

## Calendar Output — Top 3 Options

| Format | Pros | Cons |
|--------|------|------|
| **1. Markdown table** | Universal, readable in any editor, version-controllable, renders in GitHub/chat | Not importable to calendar apps, less structured |
| **2. JSON** | Machine-readable, can feed other scripts, structured | Not human-friendly for glancing at |
| **3. ICS (iCalendar)** | Importable to Google Calendar/Apple Calendar/Outlook, actual reminders | Overkill for content planning, less editable |

**Pick: Markdown as primary, JSON as secondary.**

Reasoning: The content calendar is a planning document, not a scheduling system. Founders look at it, edit it, share it. Markdown is the most versatile — it renders in editors, chat, GitHub, anywhere. JSON is generated alongside for scripts that want to consume it programmatically (e.g., a future scheduling integration). ICS is a nice v2 add-on but not essential for planning.

The script generates both: `content-calendar.md` + `content-calendar.json`

---

## Plugin Grouping — Recommendation

**Two-tier approach:**

1. **`social-skills`** (the full pack) — install everything at once. This is the default and what most people want.
2. **Individual skill install** — `npx skills add social-skills --skill social-copywriting thread-writing` for cherry-picking.

No sub-packs (socialskills-core, socialskills-visual, etc.) in v1. Reason: it adds complexity for users without clear benefit. The AgentSkills progressive disclosure model means unused skills only cost ~100 tokens each in the skill catalog. Cherry-picking individual skills covers the "I only want 3 of these" use case.

Revisit sub-packs in v2 if the pack grows past 25 skills.

---

## Platform Update Cadence — Recommendation

**Quarterly manual update with community assist.**

Implementation:
- Each platform reference file (`references/platform-specs.md`, `references/platform-algorithms.md`) has a `last_updated:` field
- Quarterly update PR cycle (Jan, Apr, Jul, Oct)
- `scripts/check-freshness.py` — flags references older than 90 days with a warning when skills load
- Community can submit update PRs to platform reference files (lower bar than new skill PRs)
- Changelog in `references/changelog.md` per platform

This is pragmatic. Automated scraping of platform changes is fragile and over-engineered for v1. Manual quarterly updates with a freshness check script catches staleness.

---

## Platform Design Architecture

**Decision needed: How to handle platform depth?**

Each platform (X, LinkedIn, Reddit, Instagram, TikTok, YouTube) has massive nuance. Options:

**Option A: One reference file per platform inside each skill**
```
social-copywriting/
├── SKILL.md
└── references/
    ├── x-twitter.md
    ├── linkedin.md
    ├── reddit.md
    ├── instagram.md
    ├── tiktok.md
    └── youtube.md
```
Pro: Platform knowledge lives next to the skill that uses it.
Con: Duplicates platform info across skills (posting-strategy also needs platform timing data).

**Option B: Shared platform references in social-context**
```
social-context/
├── SKILL.md
└── references/
    ├── platforms/
    │   ├── x-twitter.md
    │   ├── linkedin.md
    │   ├── reddit.md
    │   ├── instagram.md
    │   ├── tiktok.md
    │   └── youtube.md
    └── platform-specs.md  (quick reference table)
```
Pro: Single source of truth. All skills read from social-context.
Con: Deep platform references in a "context" skill feels odd.

**Option C: Hybrid — shared specs in social-context, skill-specific platform guidance in each skill**
```
social-context/references/platforms/     → specs, limits, algorithms (facts)
social-copywriting/references/           → how to WRITE for each platform (application)
posting-strategy/references/             → WHEN/HOW to post per platform (application)
```
Pro: Facts in one place, application knowledge where it's used.
Con: More files, but follows progressive disclosure properly.

**Recommendation: Option C (Hybrid).** This is how the best skill packs work — shared reference data + skill-specific application guidance. Philip, does this feel right?

---

## Refined Account Analysis Dimensions

For analyzing a social media account (self or competitor):

### Content Analysis
- **Posting frequency & cadence** — posts/week, time of day, day of week patterns
- **Content format distribution** — % text, image, video, carousel, thread, link, poll
- **Content pillar/topic mapping** — what subjects they cover, relative weighting
- **Hook/opening analysis** — first line patterns, hook types used, most effective hooks
- **CTA patterns** — what actions they ask for, how often, placement
- **Content length patterns** — character counts, word counts by format
- **Hashtag strategy** — frequency, count per post, branded vs generic, platform-specific usage
- **Emoji usage** — frequency, types, placement patterns

### Engagement Analysis
- **Engagement rate by format** — what content types get most interaction
- **Comment-to-like ratio** — indicator of conversation quality
- **Share/repost patterns** — what gets amplified
- **Save rate** (where visible) — what people bookmark
- **Reply behavior** — do they respond to comments? How fast? What tone?

### Voice & Style
- **Tone fingerprint** — formal ↔ casual, technical ↔ accessible, confident ↔ tentative
- **Vocabulary analysis** — unique phrases, repeated language, jargon level
- **Sentence structure** — short punchy vs long flowing, fragments vs complete
- **Personality markers** — humor style, personal anecdotes frequency, vulnerability level
- **Platform adaptation** — how voice changes across platforms

### Strategic Analysis
- **Growth trajectory** — follower/subscriber growth rate over time
- **Engagement trends** — improving, flat, declining
- **Content evolution** — how their approach has changed
- **Gap analysis** — what's missing from their strategy
- **Best performers** — top 10% content analyzed for common patterns
- **Worst performers** — bottom 10% to identify what doesn't work

### Visual Analysis (where applicable)
- **Color palette** — dominant colors, brand consistency
- **Text-on-image patterns** — font styles, overlay usage
- **Face/people presence** — selfies, team photos, illustrations, abstract
- **Visual consistency score** — does the feed have a cohesive look?

---

## Per-Platform Content Schemas

### X/Twitter
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "x-twitter",
  "format": "tweet|thread|quote-tweet|reply|poll",
  "content": {
    "text": "...",
    "thread_posts": ["...", "..."],
    "media_descriptions": ["alt text for images"],
    "poll_options": []
  },
  "hashtags": [],
  "mentions": [],
  "cta": "...",
  "hook_type": "curiosity|story|value|contrarian|question",
  "char_count": 280,
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "scheduling": {
    "optimal_time": "...",
    "day_of_week": "..."
  },
  "performance": null,
  "notes": ""
}
```

### LinkedIn
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "linkedin",
  "format": "post|article|carousel|poll|newsletter|document",
  "content": {
    "text": "...",
    "carousel_slides": [],
    "article_title": null,
    "article_body": null,
    "document_title": null
  },
  "hashtags": [],
  "mentions": [],
  "cta": "...",
  "hook_type": "...",
  "char_count": 3000,
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "scheduling": {
    "optimal_time": "...",
    "day_of_week": "..."
  },
  "performance": null,
  "notes": ""
}
```

### Reddit
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "reddit",
  "format": "text-post|link-post|image-post|poll|comment|ama",
  "content": {
    "title": "...",
    "body": "...",
    "link_url": null,
    "subreddit": "...",
    "flair": null
  },
  "cta": "...",
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "subreddit_rules_checked": false,
  "self_promotion_ratio": "...",
  "performance": null,
  "notes": ""
}
```

### Instagram
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "instagram",
  "format": "feed-post|carousel|reel|story|guide|collab",
  "content": {
    "caption": "...",
    "carousel_slides": [],
    "reel_script": null,
    "story_frames": [],
    "visual_description": "...",
    "alt_text": "..."
  },
  "hashtags": [],
  "mentions": [],
  "location_tag": null,
  "cta": "...",
  "hook_type": "...",
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "scheduling": {
    "optimal_time": "...",
    "day_of_week": "..."
  },
  "performance": null,
  "notes": ""
}
```

### TikTok
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "tiktok",
  "format": "video|carousel|photo|story",
  "content": {
    "script": "...",
    "hook_text": "...",
    "on_screen_text": [],
    "caption": "...",
    "sound_suggestion": null,
    "visual_description": "...",
    "duration_seconds": 30
  },
  "hashtags": [],
  "mentions": [],
  "cta": "...",
  "hook_type": "...",
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "trend_reference": null,
  "performance": null,
  "notes": ""
}
```

### YouTube
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "youtube",
  "format": "short|long-form|community-post|live",
  "content": {
    "title": "...",
    "description": "...",
    "script": "...",
    "hook_text": "...",
    "chapters": [],
    "tags": [],
    "thumbnail_description": "...",
    "end_screen_cta": "...",
    "duration_seconds": null
  },
  "cta": "...",
  "hook_type": "...",
  "topic": "...",
  "pillar": "...",
  "source": "original|repurposed",
  "source_id": null,
  "seo_keywords": [],
  "performance": null,
  "notes": ""
}
```

---

## Next Step: Research Sprint Plan

See `RESEARCH-SPRINT.md` for the full plan.
