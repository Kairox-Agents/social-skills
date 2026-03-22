# X/Twitter Algorithm Deep Dive (March 2026)

*Source: Open-sourced algorithm (GitHub, Jan 2026 xAI release), PostEverywhere analysis, Typefully breakdown*

## Architecture: Grok-Powered (January 2026)

X replaced its legacy recommendation system with Grok in October 2025 (Musk announcement), confirmed in January 2026 xAI GitHub release (`github.com/xai-org/x-algorithm`).

**Three-stage pipeline:**
1. **Candidate Sourcing** — 500M daily tweets → ~1,500 candidates per user. 50% in-network (Real Graph model), 50% out-of-network (SimClusters: 145,000 topic clusters)
2. **Grok Neural Ranking** — Rust-based codebase with Home Mixer, Thunder (in-memory storage), Phoenix (Grok ranking), Candidate Pipeline. Predicts: like, reply, repost, click, media engagement, dwell time, negative reaction
3. **Heuristics & Filtering** — Diversity limits, muted/blocked removal, duplicate detection, age cutoff (hard, not gradual)

## Confirmed Engagement Weights (Open-Source Code)

| Signal | Weight | Relative to Like |
|--------|--------|-----------------|
| Reply engaged by author | +75 | 150x |
| Reply | +13.5 | 27x |
| Profile click + engagement | +12.0 | 24x |
| Conversation click + engagement | +11.0 | 22x |
| Dwell time (2+ min) | +10.0 | 20x |
| Bookmark | +10.0 | 20x |
| Retweet | +1.0 | 2x |
| Like | +0.5 | 1x (baseline) |

**Scoring formula:** `Likes × 1 + Retweets × 20 + Replies × 13.5 + Profile Clicks × 12 + Link Clicks × 11 + Bookmarks × 10`

## Grok-Specific Changes (Jan 2026)

- **Sentiment analysis:** Grok reads every post's tone. Positive/constructive → wider distribution. Negative/combative → reduced visibility even if engagement is high
- **Video understanding:** Grok watches every video to match to interested viewers
- **Promptable feeds:** Users can enter natural language to customize recommendations
- **Following tab Grok-sorted:** Since Nov 2025, not chronological by default (toggle available)

## TweepCred (Hidden Reputation Score)

- Score 0-100, weighted PageRank
- Factors: account age, follower ratio, engagement quality, high-quality interactions
- **Threshold 65:** Below this, only 3 tweets considered for distribution
- Premium: +4 to +16 boost

## Premium vs Free Gap

- Premium accounts: **~10x more reach** (Buffer analysis)
- Free accounts: **50%+ of posts see zero engagement** (Buffer)
- External links from free accounts: **zero median engagement** since March 2025
- Premium is effectively required for meaningful X marketing

## Content Format Performance

- **Text-only beats video by 30%** — the only major platform where text wins
- External links: **30-50% reach penalty**
- 1-2 hashtags: +21% engagement; multiple: -40% penalty

## Practical Optimization Rules

1. Drive conversations — author reply-back is 150x a like
2. Post 2-3 quality times/day, 30-60 min spacing
3. Text-only outperforms video on X
4. Link in reply, never main tweet
5. 0-1 hashtags only
6. First 30-60 min engagement velocity determines distribution
7. Positive/constructive tone gets wider distribution (Grok sentiment)
8. Respond to genuine replies immediately — highest-leverage activity

## Anti-patterns

- "Like and retweet!" strategies (fundamentally inefficient — likes worth 0.5)
- External links in main tweet (30-50% reach penalty)
- Multiple hashtags (-40% penalty)
- High volume with low per-tweet engagement (algorithm penalizes)
- Negative/combative tone (Grok reduces visibility)
- Duplicate content (detection system active)
