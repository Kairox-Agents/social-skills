# Reddit — Platform Deep Dive

*Last updated: March 2026*

---

## ⚠️ Reddit Is Not Like Other Platforms

**Stop. Read this first.**

Reddit is fundamentally different from every other social media platform. The rules, instincts, and strategies that work on X, LinkedIn, Instagram, and TikTok will **actively destroy you** on Reddit.

Key differences:
- **Community-first, not creator-first.** Subreddits are communities, not your audience. You are a guest.
- **Anti-promotional by DNA.** Users detect and punish marketing with extreme prejudice.
- **Anonymity is the norm.** Personal brand means nothing. Content quality is everything.
- **Follower count is irrelevant.** Distribution is 100% algorithmic and community-based.
- **Downvotes exist.** And they HURT. Early downvotes can bury your content permanently.
- **Each subreddit is a different country.** What works in r/startups will get you banned in r/entrepreneur.

**If you approach Reddit like Twitter or LinkedIn, you will fail. Spectacularly.**

---

## Platform Specs

### Character Limits

| Element | Limit |
|---------|-------|
| Post title | 300 characters |
| Text post body | 40,000 characters |
| Comment | 10,000 characters |
| Flair text | Varies by subreddit (typically 64 chars) |
| Username | 20 characters (set at creation, cannot change) |
| Subreddit name | 21 characters |

### Post Types

| Type | Notes |
|------|-------|
| Text post | Title + body text. Markdown formatting. Most common for discussions. |
| Link post | Title + URL. Cannot have body text AND link simultaneously. |
| Image post | Up to 20 images. Gallery view for multiple images. |
| Video post | Up to 15 minutes, 1 GB. Native player. |
| Poll | 2-6 options, 1-7 day duration. |
| Crosspost | Shares an existing post to another subreddit. Proper etiquette for sharing across communities. |

### Image Specs

| Type | Recommended | Max File Size | Format |
|------|------------|---------------|--------|
| Image post | 1200 × 628 px minimum | 20 MB | JPG, PNG, GIF |
| Gallery (multi-image) | Up to 20 images | 20 MB each | JPG, PNG, GIF |
| Banner (subreddit) | 4000 × 192 px (desktop) | 5 MB | JPG, PNG |
| Avatar | 256 × 256 px | 1 MB | JPG, PNG |

### Video Specs

| Type | Specs |
|------|-------|
| Duration | Up to 15 minutes |
| Max file size | 1 GB |
| Aspect ratios | 16:9, 4:3, 1:1 |
| Resolution | Up to 1080p |
| Format | MP4, MOV |
| GIF uploads | Up to 100 MB (auto-converted to video) |

### Markdown Formatting

Reddit uses a Markdown variant:
- **Bold:** `**text**`
- *Italic:* `*text*`
- ~~Strikethrough:~~ `~~text~~`
- `Code:` `` `code` ``
- Block quotes: `> text`
- Headings: `# H1`, `## H2`, `### H3`
- Lists: `- item` or `1. item`
- Links: `[text](url)`
- Spoiler: `>!text!<`
- Superscript: `^text`
- Tables: Pipe-separated markdown tables

---

## Algorithm

### Core Architecture

Reddit does NOT use a single unified algorithm. It uses **multiple ranking systems** that interact:

1. **Hot** — Default feed. Combines score (upvotes minus downvotes) with time decay. Newer posts with positive votes rise; older posts fall regardless of total score.
2. **Best** — Default for comments. Uses Wilson score confidence interval — ranks by probability that a post is good, not by raw vote count.
3. **New** — Purely chronological. No algorithmic ranking.
4. **Top** — Raw score ranking within time period (hour, day, week, month, year, all time).
5. **Rising** — Posts gaining momentum but not yet "hot."
6. **Controversial** — Posts with roughly equal upvotes and downvotes.

### The Six Core Ranking Signals

| Signal | Weight | Description |
|--------|--------|-------------|
| **Engagement velocity** | Very High | How quickly upvotes, comments, and interactions come in the FIRST 2-3 hours. This is THE dominant signal. |
| **Vote ratio (confidence scoring)** | High | Uses Wilson score. 10 upvotes / 0 downvotes often outranks 50 upvotes / 15 downvotes. Clean approval > raw volume. |
| **Comment velocity** | Very High | Speed and quality of early comments. Comments weighted ~1.8× more than upvotes. |
| **Time decay** | Very High | Exponential decay. Post scoring power halves roughly every 6-12 hours. First 2-3 hours determine everything. |
| **Community alignment** | High | Fit with subreddit norms, tone, rules, flair. Misalignment triggers downvotes and reports. |
| **Account trust** | Medium | Karma, account age, diverse posting history, subreddit-specific reputation. |

### Engagement Velocity Formula (Simplified)

```
Score = (upvotes × time_multiplier + comments × 1.8 + awards × 3) / (hours_since_post^1.5 + downvote_penalty)
```

**Key insight:** The time multiplier decreases EXPONENTIALLY. A post under 2 hours old gets massive scoring boosts. After 6 hours, significant velocity penalties apply. **You have a 2-3 hour window to prove your content's worth.** Miss it, and even exceptional content dies.

### Hidden Behavioral Signals

| Signal | Effect | Notes |
|--------|--------|-------|
| **Dwell time** | Positive | How long users read your post. Strongest silent approval signal. |
| **Saves** | Positive | Indicates long-term usefulness. Guides and tutorials get high saves. |
| **"See more" expansion** | Positive | Users clicking to read full text of long posts. |
| **Hides** | Negative | Users actively hiding your post. Signals rejection. |
| **Reports** | Very Negative | Can remove post from feeds instantly. |
| **Cross-community engagement** | Positive | Engagement from users across different subreddits signals broader appeal for r/all promotion. |

### The Path to r/all

1. Post gains rapid engagement in home subreddit
2. Rises to top of subreddit's "hot" feed
3. If engagement continues from diverse users (not just subreddit regulars), signals broader appeal
4. Algorithm promotes to r/popular and r/all candidate pool
5. Further engagement from these wider audiences creates snowball effect

**Reality:** Most posts never leave their subreddit. That's fine. Subreddit-level success is the real goal for founders/SMBs.

---

## Gotchas (This Section Is Critical)

### The Self-Promotion Death Sentence

**Reddit's de facto self-promotion rules:**
- Maximum 10% of your activity should be self-promotional (the "10:1 rule")
- Many subreddits enforce this explicitly. Some are even stricter.
- "Self-promotion" includes: linking to your product, your blog, your YouTube channel, your newsletter
- **Even mentioning your company name** can trigger suspicion if your account history shows a pattern

**What actually works for founders/SMBs:**
- Be a genuine community member FIRST (weeks/months of helpful comments before ANY self-promotion)
- Share genuine value with NO link. If your advice is good enough, people will check your profile.
- When asked "what tool do you use?" — THEN it's acceptable to mention your product (organically, in context)
- AMA format (with moderator pre-approval) for legitimate companies

**What gets you killed:**
- New account → posts about their product → instant downvotes, reports, ban
- "I built this tool that..." (even if genuine, looks promotional)
- Linking to your own blog/content without substantial in-post value
- Having a post history that's exclusively about your company
- Sock puppet accounts commenting "great tool!" on your own posts (Reddit detects this)

### Subreddit Culture Varies WILDLY

Each subreddit is a different country with different laws. What works in one can get you banned in another.

| Subreddit Type | Culture | What Works | What Doesn't |
|----------------|---------|------------|--------------|
| r/startups | Builder-friendly, data-driven | Revenue breakdowns, failure post-mortems, genuine asks | "I made $10K MRR" humble-brags without detail |
| r/entrepreneur | Skeptical, anti-guru | Practical tactical advice, specific numbers | Generic motivational content, course promotion |
| r/SaaS | Technical, metric-focused | Churn analysis, technical architecture decisions | "Check out my SaaS" posts |
| r/smallbusiness | Practical, resource-sharing | Tax advice, vendor reviews, operational tips | Anything that smells like marketing |
| r/marketing | Professional, strategy-focused | Case studies, campaign analysis | Self-promotion of marketing tools |
| r/technology | News-focused, skeptical of hype | Genuine tech news, in-depth analysis | Startup launch announcements |

**Before posting in ANY subreddit:**
1. Read the rules (sidebar)
2. Read the last 50 posts — what gets upvoted? What gets removed?
3. Read the comments on top posts — what's the tone?
4. Lurk for at least a week
5. Comment helpfully on 10+ posts before making your own

### The Downvote Death Spiral

- **Early downvotes are catastrophic.** A few downvotes in the first 30 minutes can kill a post permanently.
- The Wilson score confidence interval means a post at -2 has almost zero chance of recovery.
- **Why this matters:** On Reddit, you can't just "try again" with the same content. Reposting the same thing looks like spam.
- **Prevention:** Don't post until you understand the subreddit's norms. Test with comments first.

### Authenticity Detection (Reddit Users Are Brutal)

Reddit users have developed razor-sharp instincts for detecting:
- **Corporate accounts** — Professional bio, post history is only about one company, polished language
- **AI-generated content** — Generic structure, "As a [role], I can tell you...", overly balanced perspectives
- **Astroturfing** — Multiple accounts commenting on the same posts, suspiciously positive reception
- **Disguised ads** — "I just discovered this amazing tool!" from a new account

**How to pass the authenticity test:**
- Have a genuine post history across multiple subreddits
- Use casual language appropriate to the community
- Have opinions. Reddit respects strong opinions with reasoning.
- Admit when you don't know something
- Engage in conversations, not broadcasts

### The Title Is Everything

On Reddit, **the title determines 90% of your post's success.** You cannot edit titles after posting.

**Title rules:**
- Be specific and descriptive (not clickbaity)
- Match subreddit norms (some expect [tags], some expect questions, some expect statements)
- Don't ALL CAPS (except where community norms allow it)
- Don't use emoji in titles (most subreddits view this negatively)
- Front-load the value proposition

**Good titles:**
- "After 2 years of bootstrapping, here's our actual P&L breakdown (SaaS, B2B, $40K MRR)"
- "What's the most underrated business book you've read? Looking for ops-focused recommendations."
- "I interviewed 50 YC founders about their hiring mistakes. Here's what I learned."

**Bad titles:**
- "🚀 Check out my new startup!" (promotional, emoji, vague)
- "This changed my life" (vague, clickbaity)
- "Thoughts?" (lazy, no context)

### Timing

- **Best times:** Tuesday-Thursday, 8-10 AM EST (peak Reddit activity for business subreddits)
- **Weekends:** Lower activity in business subreddits, but higher in hobby/lifestyle ones
- **Critical window:** First 2-3 hours determine everything. Post when your target subreddit is most active.
- **Don't post at night** (US time zones) unless your audience is global

### Account Health Matters

- **Karma:** Minimum karma requirements vary by subreddit. Build karma through genuine participation.
- **Account age:** Some subreddits require accounts to be 30+ days old. Some require 90+ days.
- **Diverse activity:** Accounts that only post in one subreddit look suspicious.
- **Comment karma is easier to build** than post karma. Start by commenting.

---

## Content Strategy for Reddit

### The Anti-Marketing Marketing Strategy

Reddit is the ONLY major platform where the best marketing strategy is to **not market.**

**The framework:**
1. **Be helpful** — Answer questions in your niche subreddits. Genuinely help people.
2. **Be present** — Regular, consistent participation. Not hit-and-run posting.
3. **Be transparent** — If you have a product, put it in your bio. When asked directly, be honest.
4. **Be patient** — Reddit reputation builds over months, not days.
5. **Let people come to you** — Great advice → profile curiosity → organic discovery

### Content Types That Work on Reddit

| Content Type | Engagement Level | Notes |
|-------------|-----------------|-------|
| **Detailed how-to guides** | Very High | Step-by-step, actionable, specific. The more detail, the better. |
| **Data/analysis posts** | Very High | Numbers, charts, real data. Reddit loves evidence. |
| **Personal failure stories** | High | Authentic post-mortems. "I lost $50K doing X. Here's why." |
| **Ask for advice** | High | Genuine asks get genuine responses. Reddit wants to help. |
| **AMA (Ask Me Anything)** | High | When done right (with substance). Coordinate with mods first. |
| **Resource lists** | Medium-High | Curated, opinionated lists. Not generic "top 10" SEO content. |
| **Questions** | Medium | Simple, specific questions that invite discussion. |
| **News commentary** | Medium | Your take on industry news. Add analysis, not just a link. |
| **Link posts** | Low | Unless the linked content is genuinely exceptional and relevant. |
| **Self-promotional** | Very Low | Almost always fails unless you've built community trust first. |

### Content Mix for Founders/SMBs on Reddit

| Activity | % of Time | Purpose |
|---------|-----------|---------|
| Commenting on others' posts | 60% | Build karma, reputation, relationships |
| Text posts (valuable content) | 20% | Share insights, ask questions, contribute |
| Responding to comments on your posts | 15% | Engage in discussions |
| Subtle self-reference (when relevant) | 5% | Only when naturally appropriate |

### Posting Frequency

- **Comments:** Daily or multiple times daily (the backbone of Reddit presence)
- **Posts:** 1-3 per week across relevant subreddits (not the same subreddit every day)
- **Never:** Multiple posts per day to the same subreddit (looks like spam)
- **Cadence:** Irregular is fine. Reddit doesn't reward consistency the way X/LinkedIn do.

---

## Platform-Specific Voice Guide

### Reddit Tone

Reddit rewards **knowledgeable, casual, honest, and slightly self-deprecating** content.

- **No corporate voice.** Ever. Reddit can smell corporate content and will reject it.
- **No motivational fluff.** "Just work hard and believe in yourself" gets downvoted to oblivion.
- **Specificity wins.** "We grew from $5K to $40K MRR in 14 months by switching from outbound to content marketing" > "We grew our startup using content marketing."
- **Self-deprecation works.** "I completely botched our first launch. Here's what went wrong."
- **Strong opinions are respected** (if backed by reasoning). "WordPress is the worst choice for SaaS landing pages and here's why" gets engagement.
- **Humor travels.** Reddit appreciates wit. Not forced jokes — genuine cleverness.

### Voice Calibration

| Dimension | Reddit Sweet Spot |
|-----------|-------------------|
| Formality | Casual. Think "talking to a smart friend." Contractions, informal phrasing. |
| Sentence length | Mix. Short for impact, longer for explanation. |
| Emoji usage | **Almost never.** 0-1 per post maximum. Many subreddits view emoji negatively. |
| Hashtag usage | **Never.** Hashtags do not exist on Reddit. Using them marks you as a lost marketer. |
| Formatting | Markdown-heavy. Headers, bullets, bold, code blocks. Well-formatted posts perform better. |
| Jargon | Subreddit-appropriate. Use community vocabulary. |
| Personal pronouns | "I" is default. Reddit is personal. Avoid "we" unless clearly referencing a team. |
| Vulnerability | High value. Admit mistakes, share failures, be real. |
| Humor | Encouraged. Self-deprecating > sarcastic > puns. Never forced. |

### What NOT to Write on Reddit

- **Hashtags.** Not a thing here. Instant credibility loss.
- **Emoji-heavy text.** "🚀💰 Just launched our amazing product! 🎉" — this is how you get -50 karma.
- **LinkedIn tone.** "I'm thrilled to announce..." — not here.
- **Twitter tone.** Hot takes without substance. Reddit wants the reasoning.
- **Generic advice.** "Work smarter, not harder." This isn't Instagram.
- **"Check out my..." anything.** Unless someone asked.
- **Clickbait titles.** "You won't believe what happened when I..."
- **Cross-posted content from other platforms** without adaptation. Reddit users can tell.
- **"Edit: Thanks for the gold, kind stranger!"** — This used to be charming. It's now cringe.
- **AI-generated comments.** Reddit communities are actively hostile to detected AI content.

### CTA Patterns (Reddit-Specific)

CTAs on Reddit must be **invisible or community-oriented:**
- "Has anyone else experienced this?" (invites discussion naturally)
- "What am I missing?" (invites helpful comments)
- "I'd love to hear from people who've tried [approach]" (invites experience-sharing)
- "Happy to answer questions if anyone's curious about the details." (invites engagement without pushing)
- **Never:** "Follow me for more" "Subscribe to my newsletter" "Check out my product"

---

## Reddit-Specific Strategies for Founders

### The "Build in Public" Reddit Edition

Reddit is one of the BEST platforms for building in public — but the format is completely different from X/Twitter.

**What works:**
- Monthly/quarterly update posts with real numbers (revenue, users, churn, costs)
- Specific problem → solution narratives ("How we reduced churn from 8% to 3%")
- "I made a mistake" posts (failure analysis with lessons)
- Tool/stack posts ("Our tech stack and why we chose each piece")
- "Would you use this?" validation posts (genuine, not disguised launches)

**What doesn't work:**
- Daily updates (too frequent, too self-focused)
- Vanity metrics ("We hit 10K users!!" without context or lessons)
- Disguised product launches ("I built this thing, what do you think?" from a new account)

### Subreddit Strategy for Startups

**Tier 1 (Active participation, multiple times/week):**
- 2-3 subreddits directly relevant to your industry
- Your customer's subreddits (where your users hang out)

**Tier 2 (Regular participation, weekly):**
- r/startups, r/SaaS, r/entrepreneur (pick 1-2)
- Industry news subreddits

**Tier 3 (Occasional, when relevant):**
- r/technology, r/business
- Regional subreddits (if location-relevant)

**Key rule:** Go DEEP in a few communities rather than WIDE across many. Reddit rewards depth.

### Google + Reddit SEO

Reddit posts now appear prominently in Google search results. This means:
- A helpful Reddit post can rank for years and drive continuous organic traffic
- Answering common questions in your niche → free, long-term SEO
- Reddit comments on popular threads also rank in Google
- **This is the real ROI of Reddit for founders** — not viral posts, but steady search traffic from genuinely helpful content

---

## Anti-Patterns & Cringe Detector

### Instant Red Flags

- Account is <30 days old and posting about a product
- Post history is 100% about one company/topic
- Username matches a brand name
- Responding to every critical comment defensively
- Using marketing language ("innovative," "disrupting," "game-changing")
- Perfect grammar and formatting from a new account (signals AI/corporate)
- Posting the same content to multiple subreddits simultaneously

### Tone Anti-Patterns

- "As a [founder/CEO/expert], I..." — Nobody cares about your title on Reddit
- "We're excited to share..." — This isn't a press release
- "EDIT: Wow, this blew up!" — Don't meta-comment on your post's success
- "Just wanted to put this out there..." — Passive, not confident
- Any use of "leverage," "synergy," "disrupting" — Instant eye-roll

---

*Sources: UpvoteMax algorithm analysis (2026), The Reddit Marketing Agency algorithm breakdown (Dec 2025), Reddit official documentation, r/modhelp community guidance, Conbersa.ai Reddit algorithm analysis (2026).*
