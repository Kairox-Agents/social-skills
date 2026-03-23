# Gotchas — Account Analysis

## 1. Vanity Metrics vs. Business Metrics

**What happens:** Analysis focuses on likes and follower count as success indicators. A post with 500 likes and 0 saves looks "successful." A post with 50 likes and 30 saves looks "weak." But the second post generated 3x more reach under LinkedIn's 360Brew (saves = 5x reach multiplier vs likes).

**The data:** AuthoredUp analysis of 3M+ LinkedIn posts found saves drive 5x more reach than likes. On Instagram, DM shares are the most heavily weighted signal for Reels distribution (Buffer, 4M+ posts). Likes are the weakest positive signal on both platforms.

**How to avoid:** Weight analysis toward save rate, comment depth, DM shares, and profile visits — not likes. Report likes but don't rank content quality by them.

## 2. Small Sample Size Analysis

**What happens:** User provides 15 posts for analysis. Agent extracts "patterns" and "insights" from a sample too small to be statistically meaningful.

**Why it matters:** 15 posts can't tell you if carousels outperform text posts for your specific account. One carousel might have gone viral for reasons unrelated to format. You need 50+ posts per format type for reliable format-level insights.

**How to avoid:** In development mode (50 posts), clearly label all insights as "directional, not conclusive." In production mode (500+ posts), confidence increases significantly. Always note the sample size.

## 3. Competitor Analysis Becomes Copycat Strategy

**What happens:** Agent analyzes a competitor's top posts, extracts their patterns, and recommends copying their approach. User starts sounding like a clone of the competitor.

**Why it matters:** What works for Account A won't necessarily work for Account B. Their audience relationship, brand equity, and content history are different. The point is to understand patterns, not replicate content.

**How to avoid:** Frame competitor insights as "patterns to study, not copy." Always filter through the user's own voice profile and brand positioning. Recommend adapting the PATTERN (e.g., "data-driven posts work well") not the CONTENT (e.g., "post about the same topics").

## 4. Ignoring Platform-Specific Metrics

**What happens:** Agent analyzes engagement as a single number (likes + comments + shares) across all platforms. But a 2% engagement rate means very different things on LinkedIn vs TikTok vs Reddit.

**The data:**
- LinkedIn average impressions for 5K-10K follower accounts: ~800-1,200 per post (TheShieldIndex 2026). Getting 1,000+ views is above average.
- TikTok completion rate threshold: 70%+ for viral distribution (Socialync, Jan 2026). Likes are secondary.
- Reddit: upvote velocity in first hour matters more than total upvotes.

**How to avoid:** Use platform-specific benchmarks when analyzing. Don't compare raw engagement numbers across platforms.

## 5. Voice Profile Overfitting

**What happens:** Agent extracts a voice profile from 50 posts that includes every quirk, every phrase, every formatting pattern. The resulting voice profile is so specific that it constrains future content too tightly.

**Why it matters:** Voice evolves. A voice profile extracted from 6 months of posts captures a moment in time, not a permanent identity. Over-fitting to past patterns prevents natural voice evolution.

**How to avoid:** Extract 3-5 core voice characteristics (tone, vocabulary level, opinion strength, humor style) rather than 20 micro-patterns. Update the voice profile every 90 days as the creator evolves.
