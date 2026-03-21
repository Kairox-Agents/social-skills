---
name: content-review
description: Two-stage quality gate for social content before publishing. Use when the user wants to review, check, or improve a post before posting. Stage 1 checks platform compliance (specs, format, rules). Stage 2 checks taste and quality (voice, cringe, specificity, humanness). Loads platform references and anti-patterns automatically.
---

# Content Review — Two-Stage Quality Gate

Inspired by [obra/superpowers](https://github.com/obra/superpowers) two-stage code review pattern.

## When to Use

- User says "review this post" / "check this before I post" / "is this good?"
- After social-copywriting, thread-writing, or content-repurposing generates content
- Before any content gets published

## Required Context

1. The content to review
2. The target platform
3. social-context/config.json (brand voice)
4. Platform reference from social-context/references/platforms/<platform>.md
5. social-copywriting/references/anti-patterns.md

## Stage 1: Platform Compliance Review

Check hard rules. These are pass/fail — no subjectivity.

### Universal Checks
- [ ] Character count within platform limit
- [ ] Hashtag count within platform limit
- [ ] No banned words from config.json `never_use` list
- [ ] Format matches platform norms (no hashtags on Reddit, no 30 hashtags on Instagram)
- [ ] Link handling is platform-appropriate

### X/Twitter Specific
- [ ] Single post ≤ 280 chars (non-Premium) or ≤ 25,000 (Premium)
- [ ] Thread tweets ≤ 280 chars each
- [ ] 0-1 hashtags
- [ ] External links moved to reply (not in main post)
- [ ] No engagement-bait phrasing ("Like if you agree")

### LinkedIn Specific
- [ ] Post ≤ 3,000 chars
- [ ] Hook in first ~210 chars (before "see more")
- [ ] 0-3 hashtags
- [ ] External links in comments (not in post body) for reach
- [ ] Not using engagement-bait phrasing

### Reddit Specific
- [ ] Title ≤ 300 chars
- [ ] Title is specific and descriptive (no clickbait)
- [ ] No emoji in title
- [ ] No hashtags anywhere
- [ ] No promotional language
- [ ] Subreddit specified and rules checked
- [ ] No marketing voice

### Instagram Specific
- [ ] Caption ≤ 2,200 chars
- [ ] ≤ 5 hashtags (2026 limit)
- [ ] Hook in first ~125 chars
- [ ] No non-clickable links in caption
- [ ] Image/video specs noted if visual content included

### TikTok Specific
- [ ] Caption ≤ 2,200 chars
- [ ] 3-5 hashtags (search-friendly)
- [ ] Caption keywords match video content
- [ ] No watermarks from other platforms mentioned
- [ ] Business vs personal account audio considerations noted

### YouTube Specific
- [ ] Title ≤ 60 chars for full search display
- [ ] Description has keyword in first 25 words
- [ ] Tags ≤ 500 chars total
- [ ] Thumbnail description included (if applicable)

### Stage 1 Output

```
## Platform Compliance: [PASS | FAIL]

✅ Character count: X/Y
✅ Hashtag count: X/Y
✅ Link handling: [correct]
❌ [Any failures with specific fix]

[If FAIL: specific fixes needed before Stage 2]
```

## Stage 2: Taste & Quality Review

Check subjective quality. Rate each dimension 1-5.

### Voice Match (1-5)
Does this sound like the brand described in config.json?
- Tone matches formality/energy/humor settings?
- Platform voice variant applied?
- No words from `never_use` list?
- Vocabulary and phrasing match `similar_to` reference?

### Hook Strength (1-5)
Would someone stop scrolling for this?
- First line creates curiosity, tension, or value promise?
- Specific enough to stand out? (Not "5 tips for success")
- Emotionally resonant or intellectually compelling?

### Cringe Score (1-5, where 5 = zero cringe)
Does this pass the anti-patterns check?
- No AI-tell vocabulary?
- No structural tells (perfect lists, synonym cycling)?
- No platform-specific cringe patterns?
- Would a real human post this without embarrassment?

### Specificity (1-5)
Is this concrete or abstract?
- Uses specific examples, numbers, names?
- Has a genuine opinion (not both-sides fluff)?
- Contains at least one detail that could NOT be attributed to anyone else?

### Engagement Potential (1-5)
Will this drive the platform's priority signals?
- CTA matches platform's highest-value action?
- Structure invites replies/comments/saves/shares?
- Conversation-worthy (not just "nice post" reactions)?

### Humanness (1-5)
Could this have been written by the actual person?
- Natural rhythm and pacing?
- Appropriate imperfections (fragments, casual language where expected)?
- Personal voice detectable?

### Stage 2 Output

```
## Taste & Quality Review

| Dimension | Score | Notes |
|-----------|-------|-------|
| Voice match | 4/5 | [specific note] |
| Hook strength | 3/5 | [specific note] |
| Cringe score | 5/5 | [specific note] |
| Specificity | 2/5 | [specific note] |
| Engagement potential | 4/5 | [specific note] |
| Humanness | 4/5 | [specific note] |

**Overall: X/30**

### Verdict: [SHIP | REVISE | REWRITE]

- **SHIP (24-30):** Ready to post. Minor suggestions optional.
- **REVISE (16-23):** Good foundation. Specific fixes below.
- **REWRITE (1-15):** Fundamental issues. Start over with specific direction.

### Specific Improvements:
1. [Actionable fix]
2. [Actionable fix]
3. [Actionable fix]
```

## Automatic Rewrite Offer

If verdict is REVISE or REWRITE, offer to fix it:
- "Want me to revise this with the improvements above?"
- Apply fixes and re-run Stage 2 on the revised version
- Show before/after comparison

## Batch Review

When reviewing multiple posts (e.g., a week's content calendar):
- Run Stage 1 on all posts first (fast, objective)
- Run Stage 2 only on posts that pass Stage 1
- Present a summary table with scores for all posts
- Flag the weakest post for rewrite priority

## Related Skills

- **social-copywriting** — Generates content that this skill reviews
- **thread-writing** — Generates threads that this skill reviews
- **content-repurposing** — Generates multi-platform content that this skill reviews
- **social-context** — Provides brand voice for voice-match checking

## This Skill Does NOT:

- Generate new content (use social-copywriting)
- Suggest topics (use content-ideation)
- Analyze published performance (use social-analytics)
- Handle scheduling (use posting-strategy)
