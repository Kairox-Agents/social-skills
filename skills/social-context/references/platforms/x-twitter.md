# X/Twitter — Platform Deep Dive

*Last updated: March 2026*

---

## Platform Specs

### Character Limits

| Element | Limit |
|---------|-------|
| Tweet (non-Premium) | 280 characters |
| Tweet (Premium) | 25,000 characters |
| Display name | 50 characters |
| Username (@handle) | 15 characters |
| Bio | 160 characters |
| DM | 10,000 characters |
| Alt text | 1,000 characters |
| List name | 25 characters |
| List description | 100 characters |
| Poll option | 25 characters |

### Image Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Format |
|------|-----------------|--------------|---------------|--------|
| Single image | 1200 × 675 px | 16:9 | 5 MB | JPG, PNG, GIF, WEBP |
| Multi-image (up to 4) | 1200 × 675 px | 16:9 | 5 MB each | JPG, PNG, WEBP |
| GIF | 1200 × 675 px | 16:9 | 15 MB | GIF |
| Profile photo | 400 × 400 px | 1:1 | 2 MB | JPG, PNG |
| Header/banner | 1500 × 500 px | 3:1 | 5 MB | JPG, PNG |

**Supported aspect ratios:** 1:1, 4:5, 16:9, 1.91:1. Preview crop favors 1.91:1 landscape. Keep important elements centered to avoid crop.

### Video Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Duration | Format |
|------|-----------------|--------------|---------------|----------|--------|
| Standard video | 1280 × 720 px | 16:9 | 512 MB | 0:01–2:20 | MP4 (H.264) |
| Vertical video | 1080 × 1920 px | 9:16 | 512 MB | 0:01–2:20 | MP4 (H.264) |

**Premium users:** Videos can be up to 4 hours, 8 GB.

### Polls

- 2–4 options
- 25 characters per option
- Duration: 5 minutes to 7 days
- Cannot add images/video to polls

### Thread Mechanics

- No hard limit on thread length (practical limit: ~25 tweets before engagement drops sharply)
- Each tweet in a thread is scored individually but engagement compounds back to the first tweet
- Adding to an existing thread bumps the original tweet's visibility score slightly
- Self-replies within threads function as high-value reply engagement (the algorithm treats them similarly to conversations)
- Thread tweets can contain different media types (mix text, images, video)
- Threads can be created all at once or built incrementally

### Link Previews (Cards)

- Auto-generated from Open Graph meta tags
- Card image: 1200 × 628 px (1.91:1 aspect ratio)
- Title: pulled from `og:title`
- Description: pulled from `og:description`
- **Critical:** Link preview cards are subject to severe algorithmic suppression (see Algorithm section)

---

## Algorithm (January 2026 Grok Update)

### Architecture Overview

X replaced its legacy recommendation system in January 2026 with a **Grok-powered transformer model** that:
- Processes ~5 billion ranking decisions per day
- Completes each ranking in under 1.5 seconds
- **Reads the text** of your tweets (semantic understanding, not just engagement counting)
- **Watches video content** to understand context
- Matches content semantically against user interest profiles

Open-sourced codebase: 62.9% Rust, 37.1% Python (Apache 2.0 license).

### Two Feeds

| Feed | Type | Content Source | User Time |
|------|------|---------------|-----------|
| **For You** | Algorithmic | ~50% followed accounts + ~50% discovered | ~75-80% |
| **Following** | Chronological | Only followed accounts | ~20-25% |

**For You** is where discovery happens. Optimize for this feed.

### The Ranking Pipeline

1. **Candidate Generation** — Tweet shown to 5–15% of followers (the "test audience")
2. **Initial Scoring** — First 30–60 minutes of engagement measured using weighted signals
3. **Expansion or Suppression** — Above threshold? Expand to more followers, then non-followers matching topic interest. Below threshold? Distribution stops.
4. **Continuous Re-Scoring** — Late engagement bursts (e.g., large account retweets) can re-expand distribution
5. **Feed Mixing** — Top candidates selected for "For You" feed via hard cutoff (rank 20 shown, rank 21 not — small improvements in score matter enormously)

### Engagement Weights

**These are the numbers that matter. Not all engagement is equal.**

| Action | Weight (vs. a Like) | Notes |
|--------|:-------------------:|-------|
| Like | 1× | Baseline |
| Bookmark | 10× | Strong "save for later" signal |
| Profile click | 12× | Indicates genuine interest in author |
| Repost/Retweet | 20× | Distribution amplifier |
| Quote tweet | 25× | Adds unique commentary |
| Reply | 27× | Conversation signal |
| **Reply + author reply back** | **150×** | **Highest-weighted signal. This is the game.** |
| Video watch time | Variable (high) | Proportional to % watched |

**Key insight:** A single reply-then-author-reply-back interaction is worth more than 150 likes. This is why replying to every comment on your posts is the highest-ROI activity on X.

### What Gets Boosted

1. **Engagement velocity** — How fast engagement comes in the first 30-60 minutes. 10 replies in 15 minutes >>> 10 replies over 24 hours.
2. **Replies and conversations** — Reply weight (27×) and author-reply-back (150×) dominate all other signals.
3. **Native video** — Actively promoted as X competes with TikTok/YouTube Shorts. ~10× more engagement than text-only.
4. **Images and GIFs** — Moderate boost. Visual content increases dwell time and stops the scroll.
5. **Premium status** — Premium subscribers receive 4–8× distribution boost over non-Premium accounts.
6. **Content quality (Grok assessment)** — Originality, substantiveness, and topical relevance are evaluated by the Grok model directly.
7. **Account health** — Consistent posting, engagement ratio (create + engage, not just broadcast), and high follower engagement rate all compound.
8. **In-network engagement** — Posts from accounts a user follows get prioritized over out-of-network discovery.

### What Gets Suppressed

1. **External links** — **This is the biggest factor in 2026.** External links receive near-zero median engagement from non-Premium accounts. The algorithm actively suppresses links because X wants users to stay on the platform.
2. **Engagement farming** — "Like if you agree, RT if you disagree" is detected and suppressed.
3. **Hashtag overuse** — More than 1-2 hashtags triggers spam detection. Zero hashtags is fine.
4. **Rapid-fire posting** — 10 tweets in 5 minutes looks like spam. Space content with natural intervals.
5. **Low-effort content** — "Good morning!" or single emoji tweets are deprioritized.
6. **Blocks, mutes, reports** — Carry negative weight in scoring. Content that triggers these signals gets reduced distribution across the board.
7. **Duplicate content** — Reposting the same content (even slightly varied) is detected and limited.

### Time Decay

- A tweet loses approximately **half its visibility score every 6 hours**
- After 24 hours, algorithmic distribution is minimal
- Hard age cutoff exists (exact threshold undisclosed) — beyond this, a tweet is completely ineligible for "For You"
- Threads extend the decay window slightly because new replies/additions bump the score
- **Implication:** Post when your audience is online. A great tweet at 3 AM dies before anyone sees it.

### Author Diversity Scoring

The algorithm **limits how many of your posts appear in any single user's feed at once.** Even if every post scores well, the system throttles per-author density.

- Space out important posts (don't post 3 bangers back-to-back)
- Each post must earn its own distribution independently
- Diminishing returns on high-frequency posting

---

## Gotchas

### The Link Penalty (Most Important Gotcha)

External links are algorithmically murdered in 2026. The platform wants you on X, not clicking away.

**Workarounds that work:**
- Post the valuable content natively in the tweet → link in the first reply
- Write a text-only tweet explaining what the linked content covers → link in follow-up
- For blog posts, extract key insights into a thread → link at the end
- Long-form Premium posts (25K chars) as alternative to linking out

**What doesn't work:**
- Link shorteners (doesn't bypass detection)
- Links in quote tweets (still suppressed)
- Editing a tweet to add a link after initial engagement (disrupts ranking)

### Hashtag Confusion

- **0-1 hashtags:** Optimal. The Grok model reads your tweet semantically — it doesn't need hashtags to categorize content.
- **2 hashtags:** Acceptable. Small boost to discoverability in hashtag search.
- **3+ hashtags:** Actively penalized. Triggers spam detection.
- **Hashtags in threads:** Even worse. Makes threads look spammy.
- **Trending hashtags:** Only use if genuinely relevant. Hijacking trends without relevance triggers "not interested" signals.

### Thread Engagement Drop-Off

- Average reader drops off after tweet 3-4 in a thread
- Tweet 1 gets ~100% of impressions; tweet 5 gets ~30-40%; tweet 10 gets ~10-15%
- **Solutions:** Make every tweet self-contained and valuable (not "continued..."). Use numbered lists ("3/7") so readers know where they are. Front-load the best content.
- Don't pad threads. A 7-tweet thread with all value > a 15-tweet thread with filler.

### Quote Tweet vs Repost

- **Quote tweets** (25× weight) generate more conversation but can steal engagement from the original author
- **Reposts** (20× weight) are simpler and distribute the original content
- **For building relationships:** Repost established creators (generous), quote-tweet peers (adds value)
- **For your own reach:** Quote-tweeting large accounts is one of the fastest growth tactics (their audience sees your commentary)

### Premium vs Non-Premium Reality

- Premium: ~$8/month for 4-8× distribution boost. The single highest-ROI investment on X.
- Non-Premium accounts CAN still grow but need significantly higher engagement rates to achieve the same reach.
- Premium also unlocks: 25K character posts, longer video, edit button, reduced ads, analytics, creator revenue sharing.
- **Gotcha:** Premium doesn't fix bad content. It amplifies whatever you post — including bad posts.

### AI Content Detection

- Grok-powered algorithm can identify generic AI-generated content
- AI content isn't explicitly penalized, but generic AI output scores low on "originality" and "substantiveness" quality signals
- **Anti-patterns to avoid:** Generic listicles with no personal angle, "here's the thing" openers, overly formal corporate tone, threads that read like ChatGPT bullet points
- **What works:** Use AI for ideation/drafting, then inject personal voice, specific examples, and genuine opinions

### Timing Myths vs Reality

**Real optimal posting windows:**
- Weekdays 8-10 AM (audience's time zone) — morning scroll
- Weekdays 12-1 PM — lunch browsing
- Wednesday at 9 AM — highest-engagement single window across all data

**The myth:** "There's a perfect time to post." Reality: YOUR optimal time depends on YOUR audience's time zone and habits. Use analytics to find it.

**The real rule:** Don't post when your audience is asleep. Time decay is too steep to survive a dead first hour.

### The "Deletweeting" Trap

Deleting and immediately reposting the same tweet (hoping for a fresh start) can trigger spam detection. If a tweet underperforms, let it go. Post new content.

### Editing Posts

- Premium users can edit tweets within 1 hour of posting
- Editing does NOT reset engagement or give algorithmic re-boost
- Editing CAN negatively impact distribution if done during the critical first-hour window (the algorithm may briefly deprioritize while reassessing)
- Use editing for typo fixes, not content overhauls

---

## Content Strategy for X/Twitter

### Optimal Posting Frequency

- **Minimum for algorithmic presence:** 1 tweet/day
- **Growth sweet spot:** 2-5 tweets/day
- **Maximum before diminishing returns:** ~10 tweets/day (beyond this, per-tweet engagement dilutes and spam signals increase)
- **Threads:** 1-3 per week for founders/thought leaders
- **Consistency matters more than volume.** Daily mediocre > sporadic brilliant.

### Content Mix for Founders/SMBs

| Content Type | % of Posts | Purpose |
|-------------|-----------|---------|
| Value/educational | 40% | Build authority, generate saves/bookmarks |
| Personal insights/stories | 25% | Build connection, generate replies |
| Industry commentary/hot takes | 20% | Generate conversations, increase reply weight |
| Behind-the-scenes/building-in-public | 10% | Humanize, create narrative |
| Promotional | 5% | Direct business value (keep this low!) |

### Thread Strategy

**When to thread vs single tweet:**
- **Thread:** When you have 3+ distinct points, a story to tell, or a step-by-step process
- **Single tweet:** Hot takes, questions, quick insights, observations
- **Thread lengths that work:** 5-10 tweets is the sweet spot. Under 5 feels incomplete. Over 12 loses most readers.

**Thread structures that perform:**
1. **Listicle:** "7 things I learned..." — numbered, scannable
2. **Story arc:** Setup → conflict → resolution → lesson
3. **Problem-solution:** Pain point → agitation → fix → steps
4. **Contrarian take:** "Everyone says X. They're wrong. Here's why..."
5. **Case study/breakdown:** Analyze a real example in detail

### Engagement Routine (15-20 min/day)

**Before posting (10 min):**
1. Reply thoughtfully to 5-10 posts in your niche (warms up algorithmic presence)
2. Not "great post!" — add genuine insight, a related experience, or a thoughtful question

**After posting (10 min, within first hour):**
1. Reply to EVERY comment on your post (150× weight per conversation)
2. Ask follow-up questions to keep conversations going
3. Like replies even when you don't have a substantive response

### What NOT to Write on X

- Generic motivational quotes without personal context
- "Day 47 of building my startup" with no actual insight
- Thread hooks that promise "secrets" and deliver obvious advice
- Copy-paste from LinkedIn (tone is completely wrong)
- Excessive use of 🚀💰🔥 (reads as crypto bro / engagement farmer)
- "Agree?" as a CTA (engagement farming, may be suppressed)
- Long tweets that could be threads (wall of text on mobile)
- Scheduling 20 tweets at perfectly even intervals (looks automated)

---

## Platform-Specific Voice Guide

### X/Twitter Tone

X rewards **sharp, opinionated, slightly informal** content. The platform's culture values:

- **Brevity** — Say more with less. Even Premium users with 25K chars should usually stay under 280.
- **Personality** — Bland corporate voice dies on X. Have opinions. Be specific.
- **Directness** — No throat-clearing. No "I just wanted to share..." Lead with the point.
- **Wit** — Humor travels on X better than any other platform. Don't force it, but if you're naturally funny, lean in.
- **Authenticity over polish** — Typos are forgivable. Inauthenticity is not.

### Voice Calibration

| Dimension | X/Twitter Sweet Spot |
|-----------|---------------------|
| Formality | Casual to conversational (never corporate) |
| Sentence length | Short. Punchy. Fragments OK. |
| Emoji usage | Sparingly. 0-2 per tweet. Never 🚀💰🔥 in sequence. |
| Hashtag usage | 0-1 per tweet. Never in threads. |
| Capitalization | Sentence case normally. ALL CAPS sparingly for emphasis (not entire tweets). |
| Personal pronouns | "I" and "you" — direct, personal. Avoid "one" or "we" (unless genuinely plural). |
| Technical jargon | Match your niche. Startup Twitter expects "ARR," "TAM," "PMF" without explanation. |
| Vulnerability | High value. "I failed at X" resonates more than "I succeeded at Y." |

### Hook Patterns That Work on X

**Curiosity:**
- "I was wrong about [thing everyone believes]."
- "Nobody talks about [hidden problem]."
- "[Bold claim] — and I have the data to prove it."

**Story:**
- "Last week, [unexpected thing happened]."
- "I almost [major mistake]. Here's what saved me."
- "3 years ago: [past state]. Today: [current state]. The difference?"

**Value:**
- "How to [achieve outcome] (without [common pain]):"
- "[Number] things I wish I knew before [experience]:"
- "The [framework/tool/approach] that changed how I [activity]:"

**Contrarian:**
- "[Common advice] is wrong. Here's why."
- "Unpopular opinion: [bold statement]."
- "Stop [popular practice]. Do this instead:"

**Question:**
- "What's the most underrated [thing in your niche]?"
- "Hot take: [statement]. Agree or disagree?"
- "If you could only [constraint], what would you choose?"

### CTA Patterns

- "What's your experience with this?" (invites replies — 27× weight)
- "Bookmark this for later 🔖" (10× weight)
- "Tag someone who needs to see this" (drives reposts — 20× weight)
- "What would you add?" (conversational, high-value)
- **Avoid:** "Like if you agree" "RT if you disagree" (engagement farming detection)

---

## Case Study Accounts (Founders/Builders on X)

### Patterns from Top-Performing Founder Accounts

**Common traits across accounts with strong X growth:**

1. **Post daily** — Minimum 1/day, most do 2-5/day
2. **Thread weekly** — 1-3 high-value threads per week drive the majority of growth
3. **Reply aggressively** — Reply to their own comments AND to other accounts in their niche
4. **Mix formats** — Text, images, threads, occasional video. Never just one format.
5. **Build in public** — Revenue numbers, user milestones, failures, learnings. Transparency builds audience.
6. **Have a niche** — "Startup founder" is too broad. "Solo founder building a B2B SaaS while raising kids" is a narrative.
7. **Strong opinions loosely held** — Take stances, but update them publicly when new info arrives.
8. **No link spam** — Top accounts rarely include links in main tweets. Value goes in the tweet, link goes in the reply.

### What Differentiates Great from Good

| Good Accounts | Great Accounts |
|--------------|----------------|
| Share information | Share opinions WITH information |
| Post consistently | Post consistently AND engage in comments |
| Write threads | Write threads with narrative structure |
| Use hooks | Use hooks that are SPECIFIC, not generic |
| Share wins | Share wins AND losses with equal candor |
| Build audience | Build community (know regulars, inside jokes) |

---

## Emoji & Formatting Guide for X

### Emoji Rules

- **0-2 emoji per tweet** — More looks spammy
- **Use as punctuation, not decoration:** ✅ "Just shipped v2.0 🚢" ❌ "Just 🔥 shipped 💯 v2.0 🚀🚀🚀"
- **Audience-appropriate:** Tech Twitter tolerates fewer emoji than lifestyle/creator Twitter
- **Thread formatting:** Use emoji as bullet points sparingly (→ or • work better)
- **Forbidden pattern:** 🚀💰🔥🙏💪 in any combination (reads as engagement farmer)
- **Good emoji for founders:** 🧵 (thread), 🔖 (bookmark CTA), 📊 (data), 🏗️ (building), ↓ (thread continuation)

### Line Breaks & Formatting

- Single line breaks create visual breathing room on mobile
- Double line breaks create clear paragraph separation
- **Numbered lists work:** "1/ First point" format for mini-threads within a single tweet
- **ALL CAPS:** One word for emphasis. Never entire sentences.
- **Asterisks for emphasis:** *word* doesn't render as bold, but "WORD" or ~word~ can add emphasis
- **→ arrows** work well as bullet points in threads

---

*Sources: X open-sourced algorithm (github.com/xai-org/x-algorithm), Wallaroo Media analysis (Jan 2026), Typefully algorithm breakdown (Jan 2026), OpenTweet complete breakdown (Feb 2026), HeyOrca specs guide (2026), Sprout Social Twitter algorithm analysis (Feb 2026), Tweet Archivist thread masterclass (2026).*
