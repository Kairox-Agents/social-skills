# LinkedIn — Platform Deep Dive

*Last updated: March 2026*
*Sources: LinkedIn Engineering, AuthoredUp (3M+ post analysis), TheShieldIndex, Botdog, Mosseri/Sachdeva statements*

---

## Algorithm Architecture: 360Brew (Late 2024 → 2026)

LinkedIn replaced its entire content ranking infrastructure with **360Brew**, a single unified AI model:

- **Architecture:** Decoder-only transformer with 150 billion parameters (same family as GPT/Claude but trained entirely on LinkedIn's networking data)
- **Previous system:** Thousands of task-specific ranking models (one for feed, one for jobs, one for connections, etc.)
- **New system:** One model that understands context, expertise, and relevance across all surfaces

### Key Differences from Old Algorithm
- 360Brew **audits your profile before distributing your content** — checks if your expertise matches what you're posting about
- Generic posts matching spam patterns are deprioritized
- Engagement pods are actively detected and penalized
- Takes ~90 days of aligned posting for 360Brew to fully categorize you

---

## Ranking Signals (2026)

### Two Distribution Tracks

**Track 1: Connected Reach** — People who follow you. Instagram-style: not all followers see your content equally. 360Brew predicts who is most likely to care and engage.

**Track 2: Unconnected Reach** — People who don't follow you. Uses an "audition system": your post gets initial exposure to non-followers → if it performs well, wider audition → can repeat multiple times.

### Signal Weights (from AuthoredUp analysis of 3M+ posts)

| Signal | Impact | Notes |
|--------|--------|-------|
| **Saves/Bookmarks** | **5x more reach than a like** | The single biggest shift in 2026. Delayed saves (24-72h) are especially powerful |
| **Comment depth** | Very High | Substantive multi-reply threads >> surface "Great post!" comments |
| **Dwell time** | Very High | Time spent reading after clicking "see more" |
| **DM shares** | Very High | Sending a post via DM signals high quality |
| **Profile visits** | High | Someone visiting your profile after seeing content |
| **Likes** | Low (relative) | **Weakest positive signal** — a like is now 5x less valuable than a save |
| **Delayed engagement (24-72h)** | High | Posts receiving saves/comments days later get 4-6x more reach (360Brew sees lasting value) |

### Negative Signals
- **"Not interested" clicks** — strong negative
- **Engagement pod patterns** — detected by analyzing comment velocity, account relationship patterns, engagement timing
- **Generic comments** ("Great post!", "Totally agree!") — harm reach even if not orchestrated
- **Profile-topic mismatch** — posting about topics unrelated to your headline/experience limits reach

### Profile Audit (New in 2026)
360Brew checks before distributing your content:
- **Headline and summary** — must align with topics you post about
- **Work history** — expertise must be clear
- **Content consistency** — focused niche >> random topics
- **Network relevance** — are your connections relevant to your topics?

---

## Reach Reality Check (2026)

**Organic reach is down significantly** (AuthoredUp/TheShieldIndex data):
- Overall reach: **-47% year-on-year**
- Video content: **-72%**
- Text posts: **-34%**

### Average Impressions by Follower Count (TheShieldIndex)
| Followers | Average Impressions/Post |
|-----------|------------------------|
| 1,000-5,000 | ~500-800 |
| 5,000-10,000 | ~800-1,200 |
| 10,000-25,000 | ~1,500-3,000 |
| 25,000-50,000 | ~3,000-6,000 |

**1,000+ views on a post is above average for most account sizes.**

---

## Platform Specs

| Element | Limit |
|---------|-------|
| Post (text) | 3,000 characters |
| Article | 125,000 characters |
| Headline | 220 characters |
| Summary | 2,600 characters |
| Comment | 1,250 characters |
| Hashtags | No hard limit; 2-3 recommended |
| Document (carousel) | 300 slides max, 100 MB |

### "See More" Fold
- **First ~210 characters** are visible before the fold
- Your hook MUST land before this cutoff
- Posts that get "see more" clicks signal quality to the algorithm (dwell time starts here)

### Image Specs
| Type | Size | Ratio |
|------|------|-------|
| Single image | 1200×627px | 1.91:1 |
| Square image | 1080×1080px | 1:1 |
| Portrait | 1080×1350px | 4:5 |
| Carousel/document | 1080×1080px or 1920×1080px | 1:1 or 16:9 |

### Video Specs
- Max 10 minutes, 5 GB
- Vertical (9:16) or horizontal (16:9)
- Native upload only (YouTube links get deprioritized)
- Captions/subtitles strongly recommended

---

## Content Format Performance (2026)

| Format | Performance | Notes |
|--------|------------|-------|
| **Carousels/Documents** | Highest engagement | 24.42% engagement rate (SocialInsider). Best for B2B education |
| **Text posts with strong hooks** | High | Now outperform single images by 30%. Sweet spot: 1,300-2,000 chars |
| **Polls** | High reply rate | Good for engagement but lower save rate |
| **Single images** | Declining | **-30% vs 2024-2025.** Reversed from previous years |
| **Video** | Down significantly | **-72% reach.** Native video still beats YouTube links |
| **External links** | Lowest | Put links in first comment, never in post body |

---

## Engagement Pods: Actively Penalized

LinkedIn VP of Product Gyanda Sachdeva (Nov 2025): goal is to make engagement pods "entirely ineffective."

What's being detected:
- Comments posted through third-party scripts or browser plugins → removed from "Most Relevant" view
- Same accounts consistently engaging within minutes of posting → flagged and reach limited
- Repeat offenders → account restrictions
- Generic comment patterns (even if not orchestrated) → harm your post's reach

---

## Hashtags
- 2-3 relevant hashtags at the end of your post
- Hashtags help with search categorization, not reach amplification
- No hashtag following (deprecated)
- Quality > quantity — 3 specific >> 10 generic

---

## Posting Strategy

### Optimal Times
| Day | Best Windows | Notes |
|-----|-------------|-------|
| Tuesday | 8-10 AM | Highest engagement |
| Wednesday | 8-10 AM, 12-1 PM | Strong |
| Thursday | 8-10 AM | Strong |
| Monday | 8-10 AM | Decent but competitive |
| Friday | 8-10 AM | Lower engagement |
| Weekend | Lower volume | Personal/lifestyle content can work |
*Times in audience's local timezone*

### Frequency
- Sweet spot: 1 post per business day (Mon-Fri)
- Maximum: 1/day (multiple posts compete against each other)
- Minimum viable: 2-3/week
- Consistency matters more than volume — 90 days for 360Brew to categorize you

### Golden Hour (Still Relevant)
- First 60-90 minutes determine ~70% of reach
- Respond to every early comment quickly
- Quality of early comments matters more than quantity

---

## Voice Guide

- Professional-casual (never corporate, never bro-casual)
- Personal stories outperform corporate announcements **4:1**
- Line breaks every 1-2 sentences (readability on mobile)
- First-person voice strongly preferred
- Take positions — balanced "on one hand..." posts underperform
- Vulnerability and honest numbers build trust
- No buzzword bingo ("synergy," "paradigm shift," "disruptive")

---

## Key Gotchas

1. **360Brew replaced everything.** The old playbook is dead. What worked in 2024 may not work now.
2. **Saves are the new king.** Design content worth bookmarking — frameworks, checklists, reference material.
3. **Patience pays.** Don't delete underperforming posts — saves at 72h can revive them (4-6x boost).
4. **Profile = credibility signal.** 360Brew checks your profile before distributing your content. Mismatched profile+content = limited reach.
5. **90-day ramp.** New posting strategies take ~90 days for 360Brew to fully recognize and optimize distribution.
6. **Link-in-comments is mandatory.** External links in post body are actively penalized.
7. **Generic comments hurt you.** Even unsolicited "Great post!" comments from random accounts can reduce your post's reach.
8. **1,000 views is good.** Don't compare yourself to viral outliers — the median is lower than most people think.
