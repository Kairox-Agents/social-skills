# Reddit — Platform Deep Dive

*Last updated: March 2026*
*Sources: Reddit official announcements, r/TheoryOfReddit, r/help mod statements, Reddit Engineering blog, community analysis*

---

## Algorithm Architecture (2026)

Reddit's algorithm is fundamentally different from every other social platform: **community-first, not creator-first.**

### Feed Types

| Feed | How It Works | 2026 Changes |
|------|-------------|-------------|
| **Best (default)** | ML-powered. Predicts which posts you'll find most relevant from subscribed + recommended subreddits | Now uses more aggressive recommendation via ML. Shows posts from subreddits you've never visited |
| **Hot** | Time-decayed popularity. Upvotes relative to post age | Still the most reliable sort for within-subreddit browsing |
| **New** | Chronological | No changes |
| **Rising** | Posts gaining upvotes quickly relative to their age | Critical 2-3 hour window: posts that gain momentum here reach Hot |
| **Controversial** | High ratio of upvotes to downvotes | Unchanged |
| **Top** | Highest upvoted posts over a time period | Unchanged |

### The 2026 "Best" Sort Changes
Reddit expanded its ML-powered "Best" sort significantly in late 2025/early 2026:
- Shows posts from subreddits you've never visited or subscribed to
- Uses engagement prediction to surface "relevant" content
- Many users reported seeing random unrelated subreddits in their feed
- **For creators:** Your post can now reach people who've never seen your subreddit — if it performs well

---

## How Ranking Works

### The Rising → Hot Pipeline
This is the core distribution mechanic:

1. **New post appears** in the subreddit's "New" feed
2. **Early upvotes** (first 30-60 minutes) determine if it moves to "Rising"
3. **Rising period** (2-3 hours) is the critical window — if upvotes keep coming, post moves to "Hot"
4. **Hot** = primary visibility. Most users browse Hot by default within subreddits
5. **Best** (home feed) = ML picks from Hot posts across all your subscribed (and recommended) subreddits

### Upvote Velocity > Total Upvotes
Reddit's ranking formula (originally from the Hot algorithm, open source):
- **Upvote velocity** matters more than total upvotes
- A post with 50 upvotes in 1 hour outranks a post with 200 upvotes over 12 hours
- **Time decay** is aggressive — older posts drop quickly regardless of total votes
- First hour upvote/comment velocity is the strongest signal

### Comment Activity as Ranking Signal
- Posts with more comments rank higher (signals discussion value)
- Comment depth (reply chains) > comment count
- OP (original poster) participating in comments boosts the post further
- Top-level comments that themselves generate replies are especially valuable

---

## What Matters on Reddit (2026)

| Factor | Importance | Notes |
|--------|-----------|-------|
| **Title** | Critical | 90% of whether someone clicks/upvotes. Specific > clever |
| **First hour velocity** | Very High | Upvotes + comments in first 60 minutes determine everything |
| **Comment engagement** | Very High | OP participating = significant boost |
| **Community fit** | Very High | Content that matches subreddit norms succeeds; mismatched content dies |
| **Subreddit rules compliance** | Gate | Violating rules = removal. Check AutoMod and sidebar BEFORE posting |
| **Account age/karma** | Gate | Many subreddits have minimum thresholds. Low-karma accounts are filtered |
| **Post timing** | High | Reddit's 2-3 hour rising window means timing matters more than most platforms |

### What Reddit Does NOT Use
- No "algorithm" optimizing for ad revenue on organic posts
- No "boost" or "promote" for organic content
- No follower-based distribution (followers exist but barely affect distribution)
- No hashtags. Period.
- No engagement pods (moderators detect and ban)

---

## Platform Specs

| Element | Limit |
|---------|-------|
| Title | 300 characters (shorter is better — aim for 100-150) |
| Body (text post) | 40,000 characters |
| Comment | 10,000 characters |
| Username | 20 characters |
| Subreddit name | 21 characters |
| Images | Up to 20 per post (gallery) |
| Video | Up to 15 minutes, 1 GB |
| Polls | 2-6 options, up to 7 days |
| Flair | Subreddit-specific (check before posting) |

### Image Specs
| Type | Recommended | Notes |
|------|-------------|-------|
| Image post | No strict size | Reddit auto-scales. Higher res = better |
| Thumbnail | Auto-generated from link or image | Landscape images create better thumbnails |
| Avatar | 256×256px | |

---

## Content Strategy (2026)

### What Performs Well
- **Genuine questions** that spark discussion
- **Original analysis/research** with specific data
- **Personal experiences** told honestly (not humbly-bragged)
- **Useful resources** shared without self-promotion
- **AMA-style posts** in relevant subreddits
- **Contrarian but well-reasoned takes** with evidence

### What Gets You Downvoted/Banned
- **Any promotional language** — "We're excited to announce...", "Check out my...", mentioning your product by name without context
- **Hashtags** — Reddit doesn't have hashtags. Using them marks you as a marketer
- **Emoji in titles** — Immediate credibility killer
- **Marketing voice** — Anything that sounds like a press release
- **Cross-posting to 5 subreddits simultaneously** — Spam detection + community backlash
- **Ignoring subreddit rules** — Every subreddit has unique rules. Read them.
- **Not engaging in comments** — Post and disappear = the post dies

### The Reddit Marketing Paradox
The best way to market on Reddit is to **not market on Reddit.**
- Provide genuine value → people check your profile → they find your product/project
- Answer questions in your domain → build reputation → organic discovery
- Share real numbers and experiences → build trust → people ask what you do

### Title Writing
- **Specific > clever.** "I analyzed 200 SaaS onboarding flows and the top 10% all do these 3 things" beats "You're onboarding wrong"
- **No clickbait.** Reddit users punish unfulfilled curiosity gaps
- **No emoji.** Not even one.
- **Describe what they'll get.** "Here's my full spreadsheet of..." "AMA: I've been doing X for Y years"
- **Questions work.** "Genuine question for founders: how do you handle X?"

---

## Posting Strategy

### Optimal Times
| Day | Best Windows | Notes |
|-----|-------------|-------|
| Tuesday-Thursday | 8-10 AM EST | Peak activity for business/tech subreddits |
| Mornings (any day) | Generally best | Catch rising→hot transition during business hours |
| Weekends | Lower for business subs | Higher for hobby/lifestyle subreddits |

**Critical:** Reddit's 2-3 hour rising window makes timing more important than on other platforms. Post when the subreddit's audience is waking up/online.

### Frequency
- **Comments:** Daily or near-daily (builds karma and reputation)
- **Posts:** 1-3/week per subreddit
- **Never:** Same content in the same subreddit twice
- **Never:** Same post in 5 subreddits simultaneously
- **Space out:** Don't post in the same subreddit more than once per day

---

## Voice Guide

- **Casual, genuine, peer-to-peer.** You're talking to the community, not at them
- Zero promotional tone. If it sounds like marketing, rewrite it
- Match the subreddit's tone (some are formal, most are casual)
- Self-deprecation is appreciated; humility is expected
- Specific details build credibility ("I run a $42K MRR SaaS" > "I run a successful business")
- Admit what you don't know. "I'm not sure about X, but here's what I've seen..."
- Use Reddit conventions: "EDIT:" for updates, "TL;DR:" for summaries

---

## Subreddit-Specific Behavior

Each subreddit is its own community with unique rules and culture:

### Before Posting in Any Subreddit
1. Read the sidebar/rules (every subreddit has them)
2. Read the top 10 posts to understand tone and format
3. Check for AutoModerator rules (many subs auto-remove low-karma posts)
4. Search if your topic has been posted before (reposts get removed)
5. Use appropriate flair if required

### Common Subreddit Types for B2B/Founders
| Subreddit | What Works | What Fails |
|-----------|-----------|-----------|
| r/startups | Honest experiences, failure stories, specific learnings | Product launches, promotional posts |
| r/SaaS | Technical deep dives, growth metrics, stack discussions | "Check out my app" |
| r/entrepreneur | Practical advice, revenue/growth numbers, AMAs | Motivational fluff, course promotion |
| r/smallbusiness | Specific operational advice, tool recommendations | Marketing speak |
| r/marketing | Data-backed insights, case studies | Generic "5 tips" posts |

---

## Key Gotchas

1. **Title is 90% of success.** Specific, descriptive, no clickbait, no emoji. This is non-negotiable.
2. **First hour is everything.** Reddit's rising→hot pipeline means early velocity determines total reach.
3. **Zero self-promotion tolerance.** Reddit users smell marketing instantly. Value first, always.
4. **Each subreddit is its own platform.** Rules, tone, and expectations vary wildly. Never assume.
5. **OP engagement is required.** Post and disappear = the post dies. Reply to comments, engage in discussion.
6. **Account history matters.** Redditors will check your post history. If it's all self-promotion, you'll be called out.
7. **The "Best" sort now recommends broadly.** Your post might reach people outside your subreddit — but only if it performs well within the subreddit first.
8. **Karma is a trust score, not a vanity metric.** Low karma accounts face posting restrictions in many subreddits.
