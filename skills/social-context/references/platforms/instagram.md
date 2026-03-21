# Instagram — Platform Deep Dive

*Last updated: March 2026*

---

## Platform Specs

### Character Limits

| Element | Limit |
|---------|-------|
| Feed post caption | 2,200 characters |
| "See more" cutoff | ~125 characters (mobile) / ~180 characters (desktop) |
| Hashtags per post | **5 maximum** (enforced limit as of early 2026) |
| Comment | 300 characters |
| Bio | 150 characters |
| Website field | 1 URL (or Linktree) |
| Username | 30 characters |
| Name field | 30 characters |
| Story text sticker | 250 characters |
| Reel caption | 2,200 characters |

### Image Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Format |
|------|-----------------|--------------|---------------|--------|
| Feed – Portrait *(recommended)* | 1080 × 1350 px | **4:5** | 30 MB | JPG, PNG |
| Feed – Square | 1080 × 1080 px | 1:1 | 30 MB | JPG, PNG |
| Feed – Landscape | 1080 × 566 px | 1.91:1 | 30 MB | JPG, PNG |
| Story | 1080 × 1920 px | 9:16 | 30 MB | JPG, PNG |
| Reel cover | 1080 × 1920 px | 9:16 | 8 MB | JPG, PNG |
| Profile photo | 320 × 320 px | 1:1 (circle crop) | - | JPG, PNG |

**Best format for feed in 2026:** 4:5 portrait (1080 × 1350 px). Takes maximum vertical screen space, proven higher engagement than square.

**Avoid 9:16 for feed posts** — Instagram crops it to 4:5, cutting top and bottom. Keep key content within the 4:5 safe zone.

### Video Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Duration | Format |
|------|-----------------|--------------|---------------|----------|--------|
| Reel | 1080 × 1920 px | 9:16 | 4 GB | 3 sec – 10 min | MP4, MOV |
| Feed video | 1080 × 1080 px | 1:1 | 4 GB | 3 sec – 60 min | MP4, MOV |
| Story video | 1080 × 1920 px | 9:16 | 4 GB | 3 sec – 60 sec | MP4, MOV |

**Reel safe zone:** Interface overlays (username, caption, buttons) cover bottom ~250 px and both side edges. Keep text and key content between 20% and 75% of the vertical frame.

**Reels under 3 minutes** are strongly recommended by Adam Mosseri himself. Longer Reels are possible but rarely optimal unless you have proven audience demand.

### Carousel Specs

- 2–10 slides per carousel (recently up to 20 in testing)
- All slides must be same aspect ratio (first slide determines crop for all)
- Max file size: 30 MB per image, 4 GB per video slide
- Mix of images and video within one carousel is supported

**Recommended carousel dimensions:** 1080 × 1350 px (4:5) for maximum feed real estate.

---

## Algorithm (2026 — Multi-Surface AI System)

### The Key Shift: Adam Mosseri's 2026 Direction

On December 31, 2025, Mosseri set the tone for 2026:

> "Authenticity itself is becoming infinitely reproducible. Because AI can now generate polished images and videos instantly, perfect content is cheap. The content that stands out is often more human and less manufactured."

**2026 Instagram rewards:** Raw over polished. Human over manufactured. Specific over generic.

### Two Tracks of Reach

**Track 1 — Connected Reach:** People who already follow you. Instagram ranks your post against all other posts in their potential feed by predicted relevance to them specifically.

**Track 2 — Unconnected Reach (Discovery):** People who don't follow you. Uses an "audition system":
1. Show post to small group of non-followers
2. If performance is strong → expand to wider non-follower audience
3. If strong again → expand further (process can repeat)
4. This is why small accounts can go viral

**Reels & Explore → Unconnected Reach (discovery)**
**Feed & Stories → Connected Reach (existing followers)**
**Search → Intent-based discovery (SEO-like)**

### Surface-by-Surface Algorithm

#### Feed
Signals ranked by weight:
- **Watch time** (videos) — how long someone spends on your post
- **Engagement velocity** — early likes, comments, shares in first 1-2 hours
- **Relationship signals** — accounts you message, comment on, interact with regularly
- **"See more" expansion rate** — whether people click to read captions
- **Saves** — strong "return value" signal
- **Profile clicks** — post → profile visit indicates strong interest
- **Negative signals** — quick scrolls past, "Not interested" taps

Limits back-to-back posts from same account and mixes recommended + followed content.

#### Reels
Primary ranking signals:
- **Completion rate** — did they watch the whole thing?
- **Rewatch rate** — strong signal of value
- **Shares/Sends** — #1 growth lever in 2026 (Instagram explicitly prioritizing this)
- **Save rate** — high value indicator
- **Likes** — positive but lower weight than saves/shares
- **Comments** — quality comments weighted over emoji-only

What does NOT get recommended:
- Watermarked videos (TikTok watermark = suppression)
- Videos below minimum resolution
- Repurposed content that feels recycled
- Lip-sync content from non-music accounts
- Political content (Instagram deprioritizing political content broadly)

#### Stories
- **Viewing history** — watch the most Stories from Account A? Account A goes first.
- **Engagement history** — likes, replies, emoji reactions on past Stories
- **Relationship closeness** — DMs, mutual follows, Facebook connection
- Stories only show from followed accounts (no discovery surface)

#### Explore
- 36+ ranking signals (most of any surface)
- Most important: likelihood to follow creator, 5+ second dwell time, 95%+ video completion
- Purely based on past behavior — what you've liked, saved, searched

#### Search (Instagram SEO)
- Now functions as a keyword-driven discovery engine
- Keyword relevance in: captions, alt text, profile name, on-screen text, spoken audio
- Hashtags help with search (though no longer primary reach driver)
- Complete captions and accurate alt text are increasingly important

### What Gets Boosted (2026)

1. **Shares/Sends** — Instagram's #1 growth signal. "Would someone DM this to a friend?"
2. **Original content** — Made for Instagram, not cross-posted from TikTok
3. **Authentic/raw aesthetic** — Mosseri explicitly signaling this
4. **Strong first-second hook** — early watch time/completion signals everything
5. **Saves** — indicates "I'll return to this" value
6. **Comments with depth** — conversation, not emoji reactions
7. **Reels under 3 minutes** — preferred length for Reels distribution
8. **Topic consistency** — "Your Algorithm" feature means niche clarity matters more

### What Gets Suppressed (2026)

1. **TikTok watermarks** — reduced distribution, Mosseri confirmed
2. **Watermarks from any competing platform**
3. **Overly polished AI content** — Mosseri signaling this trend
4. **Hashtag stuffing** — hard limit of 5 now, more was suppressed before
5. **Engagement bait** ("Comment YES if you agree")
6. **Political content** — Instagram is actively reducing distribution
7. **Recycled content** without new creative value
8. **Inconsistent niche** — confuses topic classification system

---

## Gotchas

### The Hashtag Rule Change (Critical Update)

Instagram **officially limited posts to 5 hashtags** in early 2026. Instagram Creators account confirmed this.

- Max 5 hashtags per post or Reel
- More than 5 does not get penalized with a hard error, but are ignored
- **Hashtags for reach are largely dead** — the algorithm reads your caption and audio semantically
- **Hashtags still help search** — someone searching #contentmarketing may find your post
- **Use hashtags for categorization, not reach:** 3-5 specific, relevant tags > 30 broad tags
- **In captions vs comments:** Best practice is caption. Comments hashtags have minimal effect.

### The Reels Watermark Problem

Cross-posting TikToks directly to Instagram is suppressed. This includes:
- TikTok watermark in the video
- TikTok username overlaid in the video
- TikTok-specific UI elements visible in the video

**Solution:** Before cross-posting, remove watermarks using SnapTik, SaveTok, or similar tools. Or better: post original content natively to each platform.

### The "Trial Reels" Feature (Use It)

Instagram launched Trial Reels — a feature that shows a Reel to non-followers ONLY, without publishing to your main profile.

**How to use it:**
1. Create a Reel
2. Choose "Trial" instead of "Post"
3. If it performs well with cold audiences → publish to your full profile
4. If it flops → let it die quietly (no impact on your main followers)

**This is built-in A/B testing.** Use it for: new content styles, new hook formats, new topics you're testing, new visual formats.

### Carousel First Slide = Everything

The first carousel slide determines:
- The crop/aspect ratio for ALL other slides
- Whether someone stops scrolling
- Whether they swipe to see more

**The first slide is not slide 1 of 10 — it's the cover of a book.** It should:
- State the value proposition clearly
- Create a curiosity gap
- Use bold, readable text
- Have visual contrast that stops the scroll

### Saves vs. Likes

**Saves are 10x more algorithmically valuable than likes.** They tell Instagram "this person wants to come back to this."

Content that gets saves:
- Educational content people want to reference later (tutorials, step-by-steps, checklists)
- Resource lists
- Templates and frameworks
- "How I did X" breakdowns

When you create content, ask: "Is this saveable?" Not just "is this likeable?"

### Shares/Sends Are Now #1

In 2026, Instagram's primary growth metric is shares (sends to friends via DM). Instagram explicitly announced this shift.

Ask before posting: "Would someone DM this to a friend?"

Content that gets shared:
- Relatable memes
- Practical tips someone would send a coworker
- Funny/surprising content
- Emotional content
- "You need to see this" moments

### Feed Format: 4:5 Is the Standard

- 4:5 portrait (1080 × 1350 px) takes most vertical space = most attention in feed
- Square (1:1) is clean but loses feed real estate
- Landscape (1.91:1) is the worst for engagement — appears small in feed
- **If unsure: always go 4:5**

### "Your Algorithm" Feature Impact

Users can now see and edit the topics Instagram thinks they care about, and down-rank topics they don't want.

**Implication for creators:** If your content doesn't clearly fall into a recognizable topic/niche, users can effectively opt out of seeing your content category.

**Niche consistency is now table stakes.** Jumping between unrelated topics (tech content one week, fitness content next) confuses the classification system and reduces distribution.

### Reel Covers (Profile Grid Problem)

Reels are cropped to 3:4 in the profile grid, but displayed as 9:16 in the Reels tab and full-screen.

**The gotcha:** If you set a custom Reel cover image, it displays at 1:1 in the grid. Design covers that work at BOTH 3:4 and 1:1 crops. Keep the most important visual element in the center square of your 9:16 frame.

---

## Content Strategy for Instagram

### Posting Frequency & Timing

| Format | Recommended Frequency |
|--------|----------------------|
| Feed posts (images/carousels) | 3-5 per week |
| Reels | 3-5 per week |
| Stories | 2-7 per day |
| Combined | Don't exceed 2 feed posts/day or audience fatigue sets in |

**Best times (general):** Tuesday-Friday, 9 AM-12 PM and 6-9 PM (audience's time zone)
**Stories:** Any time — Stories show in chronological order to followers
**Reels:** Timing matters less than feed posts because Reels distribution is algorithm-driven, not time-dependent

### Content Mix for Founders/SMBs

| Format | % | Purpose |
|--------|---|---------|
| Carousels | 35% | Education, authority, saves. Highest engagement per format. |
| Reels | 35% | Discovery, reach, new followers. Primary growth lever. |
| Single image posts | 15% | Brand, products, quick updates. |
| Stories | 15% | Relationship, community, behind-the-scenes. |

### What NOT to Post on Instagram

- **Watermarked TikToks** (suppression guaranteed)
- **Horizontal videos** as Reels (feels wrong, cropped, unprofessional)
- **30 hashtags** (limit is 5, stuffing was killing reach anyway)
- **Link in caption** (Instagram doesn't make links clickable in captions — use "link in bio")
- **Long wall-of-text captions** without line breaks (nobody reads these)
- **Generic motivational quotes on stock photos** (the lowest-signal content on Instagram)
- **Perfectly polished AI-generated imagery** (Mosseri specifically signaling against this)
- **Repurposed blog post screenshots** — this doesn't work as content
- **Engagement bait** ("double tap if you agree!")
- **Political content** (platform is actively downranking it)

---

## Platform-Specific Voice Guide

### Instagram Tone

Instagram rewards **visual-first, authentic, aspirational-but-accessible** content.

- **Captions support the visual** — the image/video is the hero; captions add depth
- **Personal narrative performs** — "I" stories, behind-the-scenes, process
- **Relatability over perfection** — Mosseri confirmed: raw beats polished in 2026
- **Shorter captions often beat longer** — but educational carousels with longer captions work when structured well

### Voice Calibration

| Dimension | Instagram Sweet Spot |
|-----------|---------------------|
| Formality | Casual to personal. More informal than LinkedIn, less punchy than Twitter. |
| Caption length | Short hook (first 125 chars = critical) + extended context if needed |
| Emoji usage | Moderate. 2-5 per caption. Used as visual breaks between paragraphs. |
| Hashtag usage | 3-5 specific, relevant tags in caption. No more. |
| Tone | Warm, personal, aspirational. "Here's what I'm learning" vs "Here's what you should do." |
| Story vs Feed voice | Stories: raw, conversational, real-time. Feed: more considered, polished idea. |

### Hook Patterns for Reels (First 1-3 Seconds)

- **Visual hook:** Unexpected visual that creates curiosity before any text/audio
- **Text overlay hook:** Bold statement on screen — "I made $0 my first month doing this..."
- **Audio hook:** Say the most compelling thing first — skip the intro, start with the payoff
- **Pattern interrupt:** Something visually surprising that makes people stop swiping

### CTA Patterns

- "Save this for later 🔖" (drives saves — strongest algorithm signal)
- "Send this to someone who needs it ↗️" (drives shares — #1 priority signal in 2026)
- "What would you add? Drop it below 👇" (drives comments)
- "Follow for more [topic] content" (post-Reel follow CTA)
- **Avoid:** "Like if you agree" (engagement bait, detected)

---

## Emoji Guide for Instagram

### Emoji Culture

Instagram is the most emoji-friendly of our 6 platforms. Used well, emoji:
- Break up paragraphs visually
- Signal tone and personality
- Act as visual anchors in the caption scan

**Recommended usage:** 2-5 per caption. Used as paragraph separators and emphasis, not decoration.

**Emoji that work well on Instagram:**
- ✨ (aspirational, aesthetic)
- 🙌 (celebratory, community)
- 📌 (save/reference)
- 🔖 (save CTA)
- 👇 (CTA direction)
- 💡 (insight/idea)
- → (bullet list substitute)

**Emoji that feel off on Instagram:**
- 🚀💰💯 (crypto/hustle bro energy)
- Excessive 🔥🔥🔥 in sequence
- Corporate emoji usage (📊📈 in every post)

---

*Sources: Adam Mosseri Instagram (Dec 2025 year-end statement, Jan-Feb 2026 posts), Hootsuite Instagram Algorithm Guide (2026), MeetEdgar Instagram Algorithm Updates 2026, HeyOrca Instagram Specs Guide 2026, Meta Transparency Centre (2026), Instagram Creators official account updates.*
