# Instagram — Platform Deep Dive

*Last updated: March 2026*
*Sources: Adam Mosseri (Instagram Head) statements, Buffer (4M+ post analysis), MeetEdgar, Mirra analysis, Instagram Creators official account*

---

## Algorithm Architecture (2026)

Instagram runs **multiple separate AI systems**, not one algorithm:

| Surface | Focus | Discovery Type |
|---------|-------|----------------|
| **Feed** | Followed accounts + recommended | Connected Reach (primary) |
| **Stories** | Close friends, followed accounts | Connected Reach only |
| **Reels** | Discovery, entertainment | Unconnected Reach (primary) |
| **Explore** | New content discovery | Unconnected Reach only |
| **Search** | Keyword-driven SEO engine | Intent-based |

### Two Distribution Tracks

**Connected Reach:** People who follow you. Instagram compares your post with all other posts a follower could see and ranks by predicted relevance. Not all followers see your content equally.

**Unconnected Reach:** Non-followers. Uses an **"audition system"**: small group of non-followers → if it performs well → wider audition → can repeat multiple times. This is how small accounts go viral.

---

## Ranking Signals (2026)

### Feed Ranking (by importance)
1. **User engagement history** — What posts that specific user likes, shares, saves, comments on
2. **Post popularity** — How many people engage, how quickly, quality of engagement
3. **Creator interaction history** — How many people interacted with the creator in past few weeks
4. **Relationship history** — Consistent interactions (commenting on each other's posts)

Instagram predicts 5 actions: **time spent on post, comment, like, share, profile photo tap.** More likely + more heavily weighted action = higher ranking.

### Reels Ranking (by importance)
1. **DM shares** — **Most heavily weighted signal for Reels distribution**
2. **Completion rate** — Did they watch the whole thing?
3. **Saves** — Stronger than likes for quality signal
4. **Watch time** — Total time spent
5. **Likes** — Weakest signal

### Signal Hierarchy (2026)
| Signal | Weight | Notes |
|--------|--------|-------|
| **DM sends/shares** | Highest | Sharing via DM = strongest quality signal |
| **Saves** | Very High | Key ranking signal, especially for educational content |
| **Watch time** | Very High | Especially for Reels and video |
| **Comments (substantive)** | High | Depth matters — real conversations >> "nice!" |
| **Shares (to Stories/external)** | High | Amplification signal |
| **Likes** | **Weakest** | Now the lowest-value positive engagement signal |

---

## 6 Major 2026 Changes

### 1. Views Are Measured Differently
- View only counts when someone **actively opens, taps on, or intentionally watches** your content
- No longer counts passive scroll-past
- "Views" is now the primary metric across ALL formats (Reels, Stories, Photos, Carousels)
- Your numbers may look lower but the data is more honest

### 2. "Your Algorithm" Feature
- Users can see which topics influence their Reels recommendations and adjust them
- For creators: **content categorization matters more than ever**
- Jumping between unrelated topics makes it harder for Instagram to recommend you
- Niche clarity and consistency are increasingly important

### 3. Reels Still Dominant, But Photos Not Dead
- Reels remain the biggest discovery engine
- Meta testing Reels-first interface in some markets (not universal)
- **Carousel engagement is UP** — many creators seeing increases
- Right takeaway: format strategy follows attention, not dogma

### 4. Hashtag Limit: 5 Maximum
- Instagram now **limits posts and Reels to 5 hashtags** (Creators official account)
- Mosseri: specific hashtags > generic lists
- Hashtags help with search but **do not increase reach**
- Focus on: clear captions, relevant keywords, strong on-screen text, clear topic signals

### 5. Follower Count Matters Less Than Ever
- Algorithmic feeds replaced intentional following behavior
- Small but engaged accounts routinely outperform large passive ones
- Algorithm reads engagement signals (watch time, sends, likes per reach), not follower count
- Instagram testing replacing "Following" count with "Friends" count on profiles

### 6. Creator Tools Matter More Than Algorithm Hacks
- **Edits App:** Meta's video editing app. No boost for using it, BUT watermarks from other platforms (TikTok) reduce distribution
- **Trial Reels:** Show content to non-followers first without publishing to your profile. If it performs well → publish broadly. Mosseri specifically recommends this for 2026

---

## Content Format Performance (2026)

| Format | Engagement Rate | Notes |
|--------|----------------|-------|
| **Carousels** | **24.42%** | Nearly 4x text posts. Up to 20 slides now. Unseen slides = re-shown to same user |
| **Reels** | High reach | Primary discovery engine. Hook in first 2 seconds |
| **Text posts** | 6.67% | Improved with strong hooks |
| **Single images** | Declining | -30% vs 2024-2025 (reversed from previous years) |
| **Stories** | Followers only | Chronological. Good for engagement, not discovery |

### Carousel Power
- Up to 20 photos/videos per carousel
- When a follower doesn't swipe to the end, Instagram re-shows the carousel later, picking up with unseen slides
- Multiple chances for engagement = higher total engagement rate
- Add audio to carousels (Mosseri recommendation)

---

## Platform Specs

| Element | Limit |
|---------|-------|
| Caption | 2,200 characters |
| Caption visible (before "more") | ~125 characters |
| Hashtags | 5 maximum (2026 limit) |
| Bio | 150 characters |
| Username | 30 characters |
| Alt text | 100 characters |
| Carousel slides | 20 maximum |

### Image Specs
| Type | Size | Ratio |
|------|------|-------|
| Square | 1080×1080px | 1:1 |
| Portrait | 1080×1350px | 4:5 (recommended — takes more screen space) |
| Landscape | 1080×566px | 1.91:1 |
| Stories | 1080×1920px | 9:16 |
| Profile photo | 320×320px | 1:1 |

### Reels Specs
| Element | Spec |
|---------|------|
| Duration | Up to 3 minutes (90 seconds optimal) |
| Aspect ratio | 9:16 (vertical, full screen) |
| Resolution | 1080×1920px |
| File size | Up to 4 GB |
| Format | MP4, MOV |

---

## Mosseri's 2026 Direction: Authenticity > Polish

Adam Mosseri's end-of-2025 message set the 2026 tone:

> "Authenticity itself is becoming infinitely reproducible. Because AI tools can now generate highly polished images and videos instantly, perfect content is becoming cheap and easy to produce. The content that stands out is often more human and less manufactured."

**What this means:**
- Raw, authentic content > perfectly polished AI-generated visuals
- Instagram exploring ways to label AI content and verify real captures
- Trust shifting from "what looks real" to **who shared it**
- Lean into imperfect, human, personal content

---

## SEO Over Hashtags

Keywords are now more effective than hashtags for discovery:
- Keywords in captions → searchable
- Keywords in profile name/bio → discoverable
- On-screen text in Reels → indexed
- Alt text on images → helps with accessibility AND search
- Hashtag follows were removed — hashtags only help categorization

---

## Posting Strategy

### Optimal Times
| Day | Best Windows | Notes |
|-----|-------------|-------|
| Tuesday-Friday | 9 AM-12 PM, 6-9 PM | Feed posts |
| Reels | Timing less critical | Algorithm-driven, not time-dependent |
| Stories | Anytime | Chronological to followers |
*Times in audience's local timezone*

### Frequency
| Format | Minimum | Sweet Spot | Maximum |
|--------|---------|------------|---------|
| Feed posts | 3/week | 3-5/week | 2/day |
| Reels | 3/week | 3-5/week | 1/day |
| Stories | 2-7/day | 3-5/day | 10/day |

---

## Voice Guide

- Visual-first platform — caption supports the visual, not the other way around
- Conversational, warm, personal
- Line breaks for readability (mobile-first)
- Emoji as visual paragraph breaks (2-5 per caption)
- Save-worthy and send-worthy CTAs (strongest signals)
- No promotional language — Instagram deprioritizes obvious ads

---

## Key Gotchas

1. **DM shares are the #1 Reels signal.** Design content people want to send to friends.
2. **Saves > likes.** Bookmark-worthy content (frameworks, checklists, tutorials) gets algorithmic priority.
3. **5 hashtag limit is hard.** Don't waste them on generic tags (#love #inspo). Use specific, searchable ones.
4. **Carousels get re-shown.** Unseen slides = another chance. Design them so each slide works independently.
5. **TikTok watermarks hurt you.** Instagram reduces distribution of videos with other platforms' watermarks.
6. **Trial Reels are underused.** Test content with non-followers before publishing to your profile. Free A/B testing.
7. **Views changed meaning.** Lower numbers don't mean less reach — the metric is just more honest now.
8. **Raw > polished.** Mosseri is explicitly signaling that authentic, imperfect content beats AI-perfect visuals.
