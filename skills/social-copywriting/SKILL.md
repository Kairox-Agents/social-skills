---
name: social-copywriting
description: Write platform-native social media posts. Use when the user wants to create a post, caption, or text content for X, LinkedIn, Reddit, Instagram, TikTok, or YouTube. Loads brand context from social-context, applies platform-specific voice and algorithm rules, and outputs ready-to-post copy. For threads use thread-writing. For video scripts use video-scripting.
---

# Social Copywriting

<HARD-GATE>
Before generating ANY content:
1. Load social-context/config.json (if missing, direct user to social-context skill first)
2. Load references/platforms/<target-platform>.md from social-context
3. Load references/anti-patterns.md from this skill
This applies to EVERY request regardless of perceived simplicity.
</HARD-GATE>

## Process (Follow In Order)

### 1. Understand the Request
- What platform(s)?
- What topic/idea/message?
- What format? (single post, carousel outline, caption, etc.)
- What goal? (engagement, awareness, leads, community)
- Any specific angle or constraint?

If platform is ambiguous, ask. Don't guess.

### 2. Load Context
- Brand voice from config.json
- Platform voice variant from config.json → `voice.platform_variants.<platform>`
- Platform reference file (specs, algorithm, gotchas)
- Anti-patterns checklist

### 3. Humanize
Before platform optimization, ensure the draft:
- Has no AI-tell patterns (see references/anti-patterns.md)
- Uses specific nouns, not vague abstractions
- Has a genuine opinion or point of view
- Sounds like the brand's voice, not a press release

### 4. Platform-Optimize
Apply platform-specific rules. **These are non-negotiable:**

#### X/Twitter
- Max 275 chars for singles (leave room for engagement)
- Hook in first 3-8 words
- 0-1 hashtags
- 0-3 emoji (strategic, not decorative)
- No links in main post (note: "link in reply" if needed)
- Reply-driving CTA
- Short lines, fragments OK

#### LinkedIn
- Hook in first 125 chars (before "see more" cutoff)
- 150-250 word sweet spot
- Short paragraphs (1-2 sentences each)
- 0-3 hashtags in caption
- No links in post body (note: "link in comments" if needed)
- Save-worthy or comment-worthy structure
- Professional-human tone (never corporate)

#### Reddit
- Title is 90% of success — specific, descriptive, no clickbait, NO emoji
- Body: genuine, casual, specific, no marketing language
- Zero hashtags (hashtags don't exist on Reddit)
- Zero promotional tone
- Community-first framing
- Match subreddit voice (ask which subreddit if not specified)

#### Instagram
- Caption hook in first 125 chars (before truncation)
- 3-5 hashtags maximum (hard platform limit in 2026)
- 2-5 emoji as visual paragraph breaks
- "Save this" or "Send this to a friend" CTAs (strongest signals)
- Visual description note if image/carousel needed

#### TikTok (caption only — for scripts use video-scripting)
- Caption: 60-80 chars visible in-feed, rest behind "more"
- 3-5 specific hashtags
- Search-friendly keywords in caption
- 1-3 emoji max
- Complement the video, don't repeat it

#### YouTube (description/community post)
- Title: primary keyword + hook, max 60 chars for search display
- Description: keyword in first 25 words, 150-300 words, include timestamps
- Community post: conversational, poll or question format works well

### 5. Self-Review Checklist

Before presenting output, verify:

- [ ] Brand voice matches config.json
- [ ] Platform specs respected (char limits, hashtag counts, format)
- [ ] No words from `never_use` list
- [ ] Hook is genuinely compelling (not generic)
- [ ] CTA is platform-appropriate
- [ ] No AI-tell patterns from anti-patterns.md
- [ ] Content is specific (names, numbers, examples) not vague
- [ ] Would a real human in this niche actually post this?

### 6. Output Format

For each piece of content, provide:

```
## [Platform] Post

[Ready-to-copy content]

---
**Format:** single post | carousel outline | caption
**Character count:** X/Y limit
**Hashtags:** [list]
**CTA type:** reply-driving | save-worthy | share-driving
**Link handling:** [none | in reply | in comments | in bio]
**Best posting window:** [day + time range]
**Notes:** [any platform-specific notes]
```

## Multi-Platform Requests

When user says "post this everywhere" or requests multiple platforms:

1. Generate **completely separate versions** for each platform
2. Do NOT copy-paste with minor tweaks
3. Include cross-posting notes: what stayed the same, what changed, why
4. Present in order: X → LinkedIn → Reddit → Instagram → TikTok → YouTube

## Related Skills

- **thread-writing** — For X/LinkedIn threads and long-form serialized content
- **video-scripting** — For TikTok/Reels/Shorts/YouTube scripts
- **carousel-design** — For Instagram/LinkedIn carousel slide content
- **content-repurposing** — For turning long-form content into multiple platform posts
- **content-review** — For two-stage quality review before publishing
- **content-ideation** — For generating ideas when user doesn't have a topic
- **posting-strategy** — For optimal timing and frequency guidance

## This Skill Does NOT:

- Generate video scripts (use video-scripting)
- Write full threads (use thread-writing)
- Create visual content (use social-visual-design)
- Plan content calendars (use content-calendar)
- Analyze performance (use social-analytics)

## Anti-Pattern: "It's Just a Quick Post"

Every post goes through platform adaptation. A LinkedIn post copied to Twitter will fail. A tweet expanded to LinkedIn will feel shallow. A Reddit post written in Instagram voice will get downvoted to oblivion. Even "simple" posts need platform-native treatment.
