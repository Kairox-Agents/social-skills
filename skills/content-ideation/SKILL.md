---
name: content-ideation
description: Generate content ideas and topics. Use when user asks "what should I post about?", needs ideas, is stuck, or wants to brainstorm content topics. Draws from content pillars, audience pain points, trends, and proven formats. Outputs actionable ideas with platform suggestions and format recommendations.
---

# Content Ideation

<HARD-GATE>
Load social-context/config.json first.
Ideas should come from the user's content pillars, audience, and brand — not generic "10 post ideas for any brand."
</HARD-GATE>

## Process

### 1. Understand the Need
- How many ideas? (default: 10)
- For which platform(s)?
- Any specific pillar or topic area?
- Time-sensitive? (trending, seasonal, event-based?)
- What's been posted recently? (check content-log.jsonl if it exists — avoid repetition)

### 2. Ideation Frameworks

Use these frameworks in rotation. Don't default to one.

#### Pillar Rotation
For each content pillar in config.json, generate 2-3 ideas:
- One educational (teach something specific)
- One personal/narrative (share experience)
- One opinion/hot-take (take a stance)

#### Audience Pain Points
For each pain point in config.json → audience.primary.pain_points:
- "How I solved [pain point]"
- "The mistake most [audience] make with [pain point]"
- "What I wish I knew about [pain point] before [experience]"

#### Format-First
Pick an engaging format, then fill with your topics:
- Thread: "X lessons from Y"
- Carousel: "Step-by-step guide to Z"
- Contrarian post: "Why [common belief] is wrong"
- Story post: "The time I [experience] and what I learned"
- Question post: "What's your [specific question about niche topic]?"
- Before/after: "[Past state] → [Current state]. Here's how:"
- Data/number post: "We achieved [specific metric]. Here's the breakdown:"

#### Reverse Engineering
Look at what's working for competitors listed in config.json:
- What topics get their most engagement?
- What formats do they use?
- What angle could YOU bring that they don't?
- What are they NOT talking about?

#### Timeliness
- Industry news or announcements
- Seasonal relevance (Q4 planning, new year, etc.)
- Platform updates or algorithm changes
- Cultural moments relevant to the audience
- Upcoming events or launches

#### The "Only I Can Say This" Filter
The best content passes this test: "Could 10 other people in my niche write this exact post?"
If yes → make it more specific, more opinionated, or more personal.
If no → you have a good idea.

### 3. Output Format

For each idea:

```
### Idea [N]: [Title]

**Pillar:** [which content pillar]
**Format:** single post | thread | carousel | video | story
**Best platform(s):** [ranked]
**Hook direction:** [1-sentence hook concept]
**Why it works:** [1-sentence rationale]
**Difficulty:** easy | medium | hard (production effort)
```

### 4. Prioritization

After generating ideas, rank by:
1. **Relevance** to current audience needs
2. **Differentiation** from what competitors are posting
3. **Production effort** vs expected impact
4. **Platform fit** for the user's strongest platform(s)
5. **Timeliness** (time-sensitive ideas go first)

Present top 3-5 as "recommended" with brief rationale.

## Content Idea Bank

When generating ideas, optionally save to `data/idea-bank.jsonl`:

```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "title": "...",
  "pillar": "...",
  "format": "...",
  "platforms": [],
  "hook_direction": "...",
  "status": "idea|planned|created|published",
  "notes": ""
}
```

This prevents repetition across sessions and feeds into content-calendar.

## Gotchas

- **Generic ideas are worse than no ideas.** "5 tips for productivity" is not an idea — it's a template. Be specific.
- **Don't ideate without context.** Ideas disconnected from brand pillars and audience pain points waste time.
- **Trendjacking has a shelf life.** If a trend is older than 3-5 days (especially on TikTok), it may be too late.
- **Quantity ≠ quality.** 5 sharp ideas > 20 generic ones.

## Related Skills

- **content-strategy** — For defining pillars and editorial direction (upstream of ideation)
- **social-copywriting** — For turning ideas into actual posts
- **content-calendar** — For scheduling ideas into a plan
- **content-repurposing** — For expanding one idea across platforms

## This Skill Does NOT:

- Write the actual posts (use social-copywriting)
- Define content strategy (use content-strategy)
- Schedule content (use content-calendar)
