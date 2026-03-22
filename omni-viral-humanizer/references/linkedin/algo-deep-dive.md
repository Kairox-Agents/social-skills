# LinkedIn Algorithm Deep Dive (March 2026)

*Sources: AuthoredUp (3M+ post analysis), TheShieldIndex, Botdog, LinkedIn VP Gyanda Sachdeva statements*

## Architecture: 360Brew

LinkedIn replaced its entire ranking infrastructure with **360Brew** — a decoder-only transformer with 150 billion parameters, trained entirely on LinkedIn's networking data.

- Replaced thousands of task-specific models with one unified AI system
- Understands context, expertise, and relevance in ways the old algorithm couldn't
- **Audits your profile before distributing your content** — expertise-topic match required
- Generic posts matching spam patterns are actively deprioritized
- Takes ~90 days of aligned posting for 360Brew to fully categorize a creator

## Signal Weights (AuthoredUp, 3M+ posts)

| Signal | Impact | Notes |
|--------|--------|-------|
| **Saves/Bookmarks** | 5x more reach than a like | The single biggest signal shift in 2026 |
| **Comment depth** | Very high | Multi-reply threads >> surface-level reactions |
| **Dwell time** | Very high | Time reading after "see more" click |
| **DM shares** | Very high | Sending post via DM = strong quality signal |
| **Delayed engagement (24-72h)** | 4-6x boost | Late saves/comments signal lasting value |
| **Profile visits** | High | Post → profile visit = authority signal |
| **Likes** | Low (relative) | 5x less valuable than a save |

## Key Changes in 2026

### 1. Saves Drive Distribution
Posts receiving saves drive 5x more reach than likes, 2x more than comments. Posts that receive saves 24-72 hours after publishing perform 4-6x better (360Brew sees late engagement as lasting value signal).

### 2. Engagement Pods Are Penalized
LinkedIn VP Sachdeva (Nov 2025): goal to make pods "entirely ineffective."
- Comments via third-party scripts removed from "Most Relevant" view
- Same accounts engaging within minutes → flagged + reach limited
- Generic comments ("Great post!") harm reach even if not orchestrated

### 3. Profile-Content Alignment Required
360Brew checks profile before distributing content:
- Headline/summary alignment with posted topics
- Work history and demonstrated expertise
- Posting consistency in a focused niche
- Network relevance to topics

### 4. Reach Is Down Significantly
AuthoredUp/TheShieldIndex data:
- Overall reach: **-47% year-on-year**
- Video content: **-72%**
- Text posts: **-34%**
- 1,000+ views = above average for 5K-10K follower accounts

### 5. Format Rankings Changed
- **Carousels:** Still highest engagement (24.42%)
- **Text posts:** Now outperform single images by 30%
- **Single images:** Declining (-30% vs 2024-2025)
- **Video:** Significant decline (-72%)
- **External links:** Lowest (must use link-in-comments)

## Practical Optimization Rules

1. Design content worth saving — frameworks, checklists, reference material
2. First 210 chars must force "see more" click (dwell time starts here)
3. Use personal stories (4:1 outperformance vs corporate announcements)
4. Links in first comment, never in post body (reach penalty)
5. 2-3 hashtags at end, never stuffing
6. Don't delete "underperforming" posts — 72-hour saves can revive them
7. Align profile with content topics (360Brew audits this)
8. Respond to comments quickly — comment thread depth is a strong signal

## Anti-patterns

- External links in post body (active reach penalty)
- Engagement pod behavior (detected and penalized)
- Generic comments from connections (harms post reach)
- Profile-content topic mismatch (limits distribution)
- Corporate press-release voice
- Engagement bait ("comment YES")
- Buzzword stacking
- Posting about random, unrelated topics (consistency needed for 90-day categorization)
