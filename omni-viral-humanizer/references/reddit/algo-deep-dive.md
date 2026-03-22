# Reddit Algorithm Deep Dive (March 2026)

*Sources: Reddit Engineering, r/TheoryOfReddit, r/help mod statements, Reddit open-source ranking code*

## Architecture: Community-First, Not Creator-First

Reddit's ranking is fundamentally different from every other platform. There is no "creator" optimization — there's only community and content.

### Feed Types
- **Best (default):** ML-powered since 2021, significantly expanded late 2025/early 2026. Now recommends posts from subreddits you've never visited based on engagement prediction
- **Hot:** Time-decayed popularity (upvotes relative to post age). Most reliable within-subreddit sort
- **Rising:** Posts gaining upvotes quickly. The critical 2-3 hour gateway
- **New:** Chronological
- **Top:** Highest upvoted over time period

### 2026 "Best" Sort Expansion
Reddit's ML-powered Best sort now aggressively surfaces content from subreddits users haven't subscribed to. Your post can reach people outside your subreddit — but only if it performs well within the subreddit first.

## The Rising → Hot Pipeline

This is Reddit's core distribution mechanic:

1. Post appears in "New"
2. Early upvotes (first 30-60 min) → moves to "Rising"
3. Rising period (2-3 hours) → critical window. Sustained upvotes → "Hot"
4. Hot = primary visibility (most users browse this)
5. Best (home feed) = ML picks from Hot across subscribed + recommended subreddits

### Upvote Velocity > Total Upvotes
- 50 upvotes in 1 hour outranks 200 upvotes over 12 hours
- Time decay is aggressive — older posts drop quickly
- First hour is everything

## Signal Weights

| Signal | Weight | Notes |
|--------|--------|-------|
| First-hour upvote velocity | **Highest** | Determines if post escapes New → Rising → Hot |
| Comment activity | Very High | More comments = higher ranking (discussion value) |
| Comment depth | High | Reply chains > top-level comment count |
| OP participation | High | Creator engaging in comments boosts the post |
| Upvote-to-downvote ratio | High | Low ratio = controversial or off-topic |
| Community fit | Gate | Mismatched content gets downvoted/removed |
| Account karma/age | Gate | Many subreddits filter low-karma accounts |

### Negative Signals
- Downvotes (directly reduce visibility)
- Reports (trigger mod review, potential removal)
- Spam detection (cross-posting to many subreddits, promotional patterns)
- Low karma/new account (filtered in many subreddits)

## What Reddit Does NOT Use
- No follower-based distribution (followers exist but barely affect reach)
- No "boost" or "promote" for organic content
- No hashtags (they don't exist on Reddit)
- No engagement pod mechanics (moderators detect and ban)
- No creator reputation score (karma is trust, not reach multiplier)

## Practical Optimization Rules

1. Title is 90% of success — specific, descriptive, no clickbait, NO emoji
2. First hour velocity determines everything — post when the subreddit's audience is active
3. Engage in comments — OP participation is a significant ranking boost
4. Match the subreddit's voice and rules — every sub is its own community
5. Zero self-promotion — provide value, let people discover you organically
6. Search before posting — reposts get removed
7. Use appropriate flair if the subreddit requires it
8. Best timing: Tuesday-Thursday 8-10 AM EST for business/tech subs

## Anti-patterns

- Any promotional language ("We're excited to announce...")
- Hashtags (don't exist on Reddit)
- Emoji in titles (credibility killer)
- Marketing voice of any kind
- Cross-posting same content to 5+ subreddits
- Post-and-disappear (no comment engagement)
- Ignoring subreddit-specific rules
- Low-effort posts ("thoughts?" with no substance)
- "Thanks for the gold, kind stranger!" (dated)
