# X/Twitter — Platform Deep Dive

*Last updated: March 2026*
*Sources: X open-source algorithm (GitHub, Jan 2026 xAI release), PostEverywhere analysis, Typefully analysis, Buffer data*

---

## Algorithm Architecture (January 2026 — Grok-Powered)

X open-sourced its algorithm twice: April 2023 (legacy) and January 2026 (Grok-powered via xAI). This is the only major platform with public ranking weights.

### Three-Stage Pipeline

**Stage 1: Candidate Sourcing** — Scans ~500M daily tweets, narrows to ~1,500 candidates per user:
- In-network (50%): Posts from accounts you follow, ranked by the **Real Graph** model (predicts engagement likelihood based on interaction history)
- Out-of-network (50%): Discovered via **SimClusters** (145,000 topic clusters, ~85% of out-of-network discovery) and social graph signals

**Stage 2: Neural Network Ranking** — Grok-powered transformer model (replaced the original 48M-parameter network in Jan 2026) predicts: will this user like, reply, repost, click, engage with media, spend time reading, or react negatively? Each tweet gets: `Final Score = probability of action × weighted importance factor`

**Stage 3: Heuristics & Filtering** — Diversity limits (one account can't dominate feed), blocked/muted removal, NSFW filtering, already-seen deduplication, age cutoff (hard, not gradual)

### The Three Feed Tabs
- **For You** — Algorithm-curated (default). 50/50 in-network/out-of-network blend
- **Following** — Was chronological until Nov 2025; now Grok-sorted by predicted engagement (toggle to chronological still available)
- **Explore** — Trending + breaking news

---

## Engagement Weights (From Open-Sourced Code)

Confirmed in both 2023 release and January 2026 xAI release.

| Signal | Weight | What It Means |
|--------|--------|---------------|
| Reply engaged by author | +75 | You reply AND the author engages back. **The single most powerful signal — 150x a like** |
| Reply | +13.5 | Someone replies to the tweet |
| Profile click + engagement | +12.0 | Visitor clicks profile AND likes/replies to something |
| Conversation click + engagement | +11.0 | Clicks into thread AND interacts |
| Dwell time (2+ min) | +10.0 | Reads/views for 2+ minutes |
| Bookmark | +10.0 | Saves the tweet |
| Retweet | +1.0 | Shares to their timeline |
| Like | +0.5 | **Lowest-value positive signal** |

**Simplified scoring formula** (widely cited from code):
```
Likes × 1 + Retweets × 20 + Replies × 13.5 + Profile Clicks × 12 + Link Clicks × 11 + Bookmarks × 10
```

### Negative Signals
| Signal | Impact |
|--------|--------|
| Block | Strong penalty; accumulates on TweepCred |
| Report | Major penalty (-15 to -35 on reputation) |
| Mute | Significant negative |
| "Not interested" | Reduces distribution for that content type |
| Unfollow | Negative signal on relationship score |

### TweepCred: Hidden Reputation Score
Every account has a TweepCred score (0-100) using weighted PageRank:
- Factors: account age, follower-to-following ratio, engagement quality, interactions with high-quality users
- **Critical threshold: 65.** Below 0.65, only 3 of your tweets are considered for distribution
- Premium subscribers get +4 to +16 point boost

---

## Grok-Powered Changes (January 2026)

The xAI release (`github.com/xai-org/x-algorithm`) confirmed:

- **Architecture:** Rust-based. Four components — Home Mixer (orchestration), Thunder (in-memory post storage), Phoenix (Grok-based ranking), Candidate Pipeline
- **Sentiment analysis:** Grok reads every post's tone. Positive/constructive messaging → wider distribution. Negative/combative → reduced visibility even if engagement is high
- **Promptable feeds:** Users can input natural language commands like "show me AI and startups" to customize recommendations
- **Video understanding:** Grok watches every video to match content to interested viewers

---

## Premium vs. Free: The Reach Gap

- Premium accounts get **~10x more reach per post** than free accounts (Buffer analysis)
- At least **half of free account posts see zero engagement** (Buffer)
- External links from free accounts have **zero median engagement** since March 2025
- Premium is effectively required if X is a meaningful marketing channel
- Premium also boosts TweepCred by +4 to +16 points

---

## Platform Specs

### Character Limits
| Element | Limit |
|---------|-------|
| Tweet (non-Premium) | 280 characters |
| Tweet (Premium) | 25,000 characters |
| Display name | 50 characters |
| Username | 15 characters |
| Bio | 160 characters |
| DM | 10,000 characters |
| Alt text | 1,000 characters |
| Poll option | 25 characters |

### Image Specs
| Type | Size | Ratio | Max File | Format |
|------|------|-------|----------|--------|
| Single image | 1200×675px | 16:9 | 5 MB | JPG, PNG, GIF, WEBP |
| Multi-image (up to 4) | 1200×675px | 16:9 | 5 MB each | JPG, PNG, WEBP |
| GIF | 1200×675px | 16:9 | 15 MB | GIF |
| Profile photo | 400×400px | 1:1 | 2 MB | JPG, PNG |
| Header | 1500×500px | 3:1 | 5 MB | JPG, PNG |

### Video Specs
| Type | Size | Ratio | Max | Duration | Format |
|------|------|-------|-----|----------|--------|
| Standard | 1280×720px | 16:9 | 512 MB | 0:01–2:20 | MP4 (H.264) |
| Vertical | 1080×1920px | 9:16 | 512 MB | 0:01–2:20 | MP4 (H.264) |
Premium: up to 4 hours, 8 GB.

### Polls
- 2-4 options, 25 chars/option, duration 5 min to 7 days

### Thread Mechanics
- No hard limit (practical: ~25 tweets before sharp engagement drop)
- Each tweet scored individually; engagement compounds to first tweet
- Self-replies treated as high-value engagement
- Mixed media types OK within a thread

---

## Content Format Performance (2026)

**Text-only posts outperform video by 30% on X** — the only major platform where text beats video.

| Format | Engagement | Notes |
|--------|-----------|-------|
| Text singles | Highest for quick takes | Under 275 chars sweet spot |
| Threads (5-10 tweets) | High for educational | Front-load best content (60% drop after tweet 4) |
| Images (single) | Good | 1-2 images > 4 images |
| Polls | High reply rate | Algorithm counts poll votes as engagement |
| Video | Lower than text | Works for tutorials, screen recordings |
| External links | **30-50% reach penalty** | Always put links in reply, not main tweet |

---

## Hashtags
- 1-2 niche-relevant hashtags: +21% engagement
- Multiple hashtags: **-40% reach penalty**
- Generic popular hashtags get drowned out
- Best practice: 0-1 hashtags, placed naturally

---

## Posting Strategy

### Optimal Times
| Day | Best Windows | Notes |
|-----|-------------|-------|
| Tuesday-Thursday | 8-10 AM, 12-1 PM | Highest engagement days |
| Wednesday | 9 AM | Single best window |
| Friday | 8-10 AM | Drops afternoon |
| Weekend | Lower volume, lower competition | Test for your audience |
*All times in audience's local timezone*

### Frequency
- Sweet spot: 2-3 quality posts/day including replies and threads
- Wait 30-60 minutes between tweets
- Algorithm penalizes high volume with low per-tweet engagement
- 10 high-quality tweets outperform 30 mediocre ones

### First-Hour Velocity
- Early engagement in the first 30-60 minutes is the strongest distribution signal
- Post when you can actively engage with replies
- Author reply-backs are worth +75 (150x a like)

---

## Voice Guide

- Direct, punchy, conversational
- Fragments OK, casual punctuation OK
- Contractions always ("it's" not "it is")
- Opinions encouraged — the algorithm rewards engagement, and takes generate replies
- 0-3 emoji (strategic, not decorative)
- No corporate voice — LinkedIn tone fails on X

---

## Key Gotchas

1. **Link penalty is real and severe.** 30-50% reach reduction for external links. Always use reply-link strategy.
2. **Grok sentiment matters.** Positive/constructive tone gets wider distribution even with less engagement than outrage content.
3. **Free accounts are at a massive disadvantage.** ~10x reach gap vs Premium.
4. **TweepCred threshold of 65 is a cliff.** Below it, only 3 tweets get considered for distribution.
5. **The "Following" tab is no longer chronological by default** (Nov 2025). Users must manually toggle to chronological.
6. **Duplicate detection is active.** Reposting the same content gets caught and limited.
7. **Muted keywords are a silent killer.** If your post contains commonly muted terms, it's filtered for those users before scoring even begins.
