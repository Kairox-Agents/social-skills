---
name: content-calendar
description: Plan and generate content calendars. Use when user wants to plan their content for a week, month, or campaign period. Outputs a structured calendar with topics, formats, platforms, and timing. Generates both Markdown (human-readable) and JSON (machine-readable) formats.
---

# Content Calendar

<HARD-GATE>
Load social-context/config.json first.
Calendar should reflect the user's content pillars, platforms, and posting frequency.
</HARD-GATE>

## Process

### 1. Determine Scope
- Time period? (1 week, 2 weeks, 1 month)
- Which platforms?
- Any specific themes, launches, or events during this period?
- Content already created or planned?

### 2. Calculate Volume

From config.json → platforms.posting_frequency, determine total posts needed.

Example for a founder on 3 platforms:
```
X: 5 posts/week × 4 weeks = 20 posts
LinkedIn: 3 posts/week × 4 weeks = 12 posts
Instagram: 3 posts/week × 4 weeks = 12 posts
Total: 44 pieces of content/month
```

### 3. Apply Pillar Distribution

Distribute content across pillars from config.json. Recommended ratio:

| Pillar Type | % | Purpose |
|-------------|---|---------|
| Educational/value | 40% | Authority, saves, bookmarks |
| Personal/narrative | 25% | Connection, replies |
| Industry/opinion | 20% | Thought leadership, conversations |
| Behind-the-scenes | 10% | Humanize, community |
| Promotional | 5% | Direct business value |

### 4. Map Format Mix per Platform

Each platform should have format variety:

**X:** 60% singles, 25% threads, 15% quote tweets / polls
**LinkedIn:** 40% text posts, 35% carousels, 15% polls, 10% articles
**Instagram:** 35% carousels, 35% Reels, 20% single image, 10% Stories
**TikTok:** 70% educational/tips, 20% trending, 10% behind-scenes
**Reddit:** 50% comments, 30% text posts, 20% link/image posts
**YouTube:** 40% Shorts, 40% long-form, 20% community posts

### 5. Generate Calendar

#### Markdown Output (Primary)

```markdown
# Content Calendar — [Month Year]

## Week 1: [Date Range]

### Monday [Date]
| Time | Platform | Format | Pillar | Topic | Status |
|------|----------|--------|--------|-------|--------|
| 9:00 AM | LinkedIn | Text post | Educational | [topic] | 📝 Draft |
| 12:00 PM | X | Single | Opinion | [topic] | 💡 Idea |

### Tuesday [Date]
| Time | Platform | Format | Pillar | Topic | Status |
|------|----------|--------|--------|-------|--------|
| 8:30 AM | X | Thread | Educational | [topic] | 💡 Idea |
| 10:00 AM | Instagram | Carousel | Value | [topic] | 💡 Idea |

[...continue for each day...]

## Week 2: [Date Range]
[...]
```

Status indicators:
- 💡 Idea (topic defined, not written)
- 📝 Draft (content written, not reviewed)
- ✅ Ready (reviewed, approved)
- 📤 Published

#### JSON Output (Secondary)

Generate alongside Markdown at `data/content-calendar.json`:

```json
{
  "period": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" },
  "entries": [
    {
      "date": "YYYY-MM-DD",
      "time": "HH:MM",
      "platform": "linkedin",
      "format": "text-post",
      "pillar": "educational",
      "topic": "...",
      "hook_direction": "...",
      "status": "idea",
      "content_id": null,
      "notes": ""
    }
  ]
}
```

### 6. Repurposing Blocks

Identify 2-3 "anchor content" pieces per week that will be repurposed:
- Monday: Long-form post (blog/LinkedIn article) → repurpose into X thread + Instagram carousel + TikTok script
- Thursday: Thread → repurpose highlights into singles for other platforms

Mark these as "ANCHOR" in the calendar.

## Calendar Templates

### Solo Founder — 3 Platform Template (X + LinkedIn + Instagram)
- **Monday:** LinkedIn (educational) + X (hot take)
- **Tuesday:** X (thread from Mon's LinkedIn topic) + Instagram (carousel)
- **Wednesday:** LinkedIn (personal story) + X (engagement post)
- **Thursday:** Instagram (Reel) + X (data/number post)
- **Friday:** LinkedIn (industry commentary) + X (weekend question)

### Startup — 5 Platform Template
[Expanded version with Reddit + TikTok + YouTube]

## Gotchas

- **Don't over-plan.** A rigid calendar that ignores real-time opportunities is worse than flexible guidelines.
- **Leave gaps for reactive content.** Reserve 20% of calendar slots for trending topics and timely responses.
- **Batch creation.** Plan to write 3-5 posts in one session rather than one per day. More efficient, more consistent voice.
- **Calendar ≠ commitment.** If a planned post doesn't feel right on the day, skip it. Quality > schedule.

## Related Skills

- **content-ideation** — Feeds topics into the calendar
- **posting-strategy** — Provides timing and frequency guidance
- **social-copywriting** — Writes the actual posts from calendar topics
- **content-repurposing** — Handles anchor content → multi-platform expansion

## This Skill Does NOT:

- Write the actual content (use social-copywriting)
- Determine optimal timing (use posting-strategy)
- Generate ideas from scratch (use content-ideation)
- Publish or schedule (manual or via scheduling tools)
