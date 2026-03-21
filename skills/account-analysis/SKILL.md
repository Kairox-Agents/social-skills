---
name: account-analysis
description: Analyze any social media account to extract voice DNA, content patterns, and strategic insights. Use when user wants to study their own account, analyze a competitor, or generate a custom voice profile. Outputs a voice-profile.md and content-playbook.md that can plug into social-context for personalized content generation.
---

# Account Analysis

## Two Modes

### Self-Analysis
Analyze the USER'S OWN account(s) to codify their voice, identify what works, and generate a personalized voice profile.

**Output:** Custom voice profile that plugs into social-context/config.json → voice section.

### Competitor Analysis
Analyze another account to understand their strategy, extract patterns, and identify gaps.

**Output:** Competitive intelligence report with actionable insights.

## Data Sourcing

### Priority Order
1. **API (SociaVault)** — Cheapest all-in-one. Set API key in config: `data.api_key` and `data.provider: "sociavault"`
2. **API (Apify)** — Fallback. More complex but Philip has experience with it.
3. **MCP Servers** — Free options for Reddit (saginawj/mcp-reddit-companion) and YouTube (stephen9412/youtube-mcp-server)
4. **Manual paste/upload** — User exports and pastes their content. Always works, no API needed.
5. **Browser extraction** — Agent reads public profile via browser tool. Fragile but free.

### Post Count
- **Development mode:** 50 posts (quick analysis, pattern detection)
- **Production mode:** 500 posts (statistically meaningful, voice DNA extraction)

Configure in skill settings or ask user.

## Analysis Dimensions

### Content Analysis
- **Posting frequency & cadence** — posts/week, time of day, day of week
- **Content format distribution** — % text, image, video, carousel, thread, link, poll
- **Content pillar mapping** — topic clusters, relative weighting
- **Hook/opening analysis** — first line patterns, hook types used
- **CTA patterns** — what actions they ask for, how often, placement
- **Content length patterns** — character/word counts by format
- **Hashtag strategy** — frequency, count per post, branded vs generic
- **Emoji usage** — frequency, types, placement

### Engagement Analysis
- **Engagement rate by format** — what types get most interaction
- **Comment-to-like ratio** — conversation quality indicator
- **Share patterns** — what gets amplified
- **Reply behavior** — do they respond? How fast? What tone?

### Voice & Style
- **Tone fingerprint** — formal↔casual, technical↔accessible, confident↔tentative
- **Vocabulary analysis** — unique phrases, repeated language, jargon level
- **Sentence structure** — short vs long, fragments vs complete
- **Personality markers** — humor style, anecdote frequency, vulnerability level
- **Platform adaptation** — how voice changes across platforms

### Strategic Analysis
- **Growth trajectory** — follower growth rate
- **Engagement trends** — improving, flat, declining
- **Best performers** — top 10% content patterns
- **Worst performers** — bottom 10% anti-patterns
- **Gap analysis** — what's missing from their strategy

## Output: Voice Profile (Self-Analysis)

Generate files that plug into social-context:

```
voice-profile/
├── voice-profile.md      # Tone, vocabulary, sentence patterns
├── content-playbook.md   # Proven patterns codified as rules
├── hook-library.md       # Top-performing hooks extracted
├── platform-tactics.md   # Platform-specific patterns observed
└── anti-patterns.md      # What doesn't work for this account
```

### voice-profile.md Schema

```markdown
# Voice Profile: [Account Name]

## Tone
- Formality: [scale 1-10 with description]
- Energy: [scale 1-10]
- Humor: [scale 1-10 with style description]
- Vulnerability: [scale 1-10]
- Technical depth: [scale 1-10]

## Vocabulary
### Signature phrases: [list of frequently used phrases]
### Avoided words: [words/phrases never used]
### Jargon level: [description]

## Sentence Patterns
- Average sentence length: [X words]
- Fragment usage: [frequency]
- Question usage: [frequency]
- Opening patterns: [most common first-word/phrase patterns]

## Personality Markers
- Uses personal anecdotes: [frequency + style]
- Humor type: [dry/self-deprecating/observational/none]
- Opinion strength: [tentative/balanced/strong/provocative]
- Engagement style: [broadcaster/conversationalist/community-builder]
```

## Output: Competitive Report (Competitor Analysis)

```markdown
# Competitive Analysis: [Account Name]

## Overview
- Platform: [X]
- Followers: [count]
- Posting frequency: [X/week]
- Primary content format: [type]

## What They Do Well
1. [specific pattern with example]
2. [specific pattern with example]
3. [specific pattern with example]

## What They Do Poorly
1. [specific gap]
2. [specific gap]

## Opportunities They're Missing
1. [gap we can exploit]
2. [gap we can exploit]

## Patterns to Study (Not Copy)
1. [specific technique worth adapting]
2. [specific technique worth adapting]

## Key Metrics
| Metric | Value | Benchmark |
|--------|-------|-----------|
| Engagement rate | X% | Industry avg: Y% |
| Posting frequency | X/week | Recommended: Y/week |
| Top format | [type] | [% of content] |
```

## Process

### 1. Collect Data
- Determine platform and account
- Choose data source (API / paste / browser)
- Fetch post count per mode setting
- Normalize data format

### 2. Analyze
- Run all analysis dimensions
- Calculate metrics
- Identify patterns and outliers
- Extract top/bottom performers

### 3. Generate Output
- Self-analysis → voice profile files
- Competitor analysis → competitive report
- Both → recommend integration with social-context

### 4. Integration
For self-analysis, offer to update social-context/config.json with:
- Extracted voice parameters
- Discovered content pillars
- Optimal posting times based on actual performance data
- Platform-specific voice variants

## Related Skills

- **social-context** — Voice profile plugs into foundation context
- **content-ideation** — Competitor gaps feed into idea generation
- **content-strategy** — Analysis informs strategic direction

## This Skill Does NOT:

- Generate content (use social-copywriting)
- Post or publish anything
- Access private account data (public posts only via API)
