# TikTok — Platform Deep Dive

*Last updated: March 2026*

---

## Platform Specs

### Character Limits

| Element | Limit |
|---------|-------|
| Caption | 2,200 characters |
| Bio | 80 characters |
| Username | 24 characters |
| Display name | 30 characters |
| Comment | 150 characters |
| On-screen text sticker | Varies by sticker type |

**Caption note:** While 2,200 chars is the max, most of the caption is truncated behind a "more" tap. The first ~60-80 characters appear in-feed. Treat that as your hook + keyword injection zone.

### Video Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Duration | Format |
|------|-----------------|--------------|---------------|----------|--------|
| Standard video | 1080 × 1920 px | **9:16** | 287.6 MB (iOS) / 72 MB (Android) | 3 sec – 10 min | MP4, MOV |
| Square video | 1080 × 1080 px | 1:1 | 287.6 MB | 3 sec – 10 min | MP4, MOV |
| Horizontal video | 1920 × 1080 px | 16:9 | 287.6 MB | 3 sec – 10 min | MP4, MOV |

**Always use 9:16.** Square and horizontal feel foreign and get lower completion rates. TikTok was built for full-screen vertical.

**Export settings for best quality:**
- Resolution: 1080p (4K uploads get compressed anyway)
- Codec: H.264 (H.265 has compatibility issues on older Android)
- Frame rate: 30fps or 60fps (60fps for fast-moving content)

**Safe zone:** TikTok UI overlays the bottom ~250 px (username, caption, buttons) and ~30 px from each side edge. Keep text, logos, and important visuals in the center 70% of the frame.

### Carousel/Photo Posts

| Element | Spec |
|---------|------|
| Recommended size | 1080 × 1920 px (9:16) |
| Max images | 2-10 |
| Max file size | 5 MB per image |
| Formats | JPG, PNG |
| Auto-advances | Yes, with music |

TikTok photo carousels are a growing format — auto-advance with audio gives them Reel-like energy without video production overhead.

### Audio & Sound

- Music from TikTok's licensed sound library: free for personal accounts, restricted for business accounts
- **Business accounts cannot use most trending sounds** (copyright restrictions) — this is a major strategic consideration
- Original audio: upload your own, can become "trends" if others use it
- Voiceover: built-in AI voice or record your own
- Creator Rewards Program (monetization) requires original audio or licensed content

---

## Algorithm (FYP — For You Page)

### What Makes TikTok Different

TikTok's FYP algorithm is the most democratic of any major platform:

- **Follower count is NOT a ranking signal.** A new account's first video can go viral.
- **Previous video performance is NOT a ranking signal.** Each video is evaluated independently.
- **The algorithm tests every piece of content.** Nothing is dead on arrival.
- Content can go viral **weeks or months after posting** if a new viewer cluster discovers it.

This is fundamentally different from X, LinkedIn, Instagram, and YouTube where account authority matters significantly.

### The Three Pools of Ranking Signals

#### 1. Engagement Signals (Highest Weight)

| Signal | Weight | Notes |
|--------|--------|-------|
| **Shares** | Very High | Distributes content beyond FYP; strongest quality signal |
| **Saves/Favorites** | Very High | "Return to this later" indicator |
| **Comments** | High | Conversation signal; length and quality considered |
| **Likes** | Medium | Still matters, but lower than shares/saves |
| **Profile visits** | Medium | Post → profile visit = strong author interest signal |
| **Follows from post** | High | New follower from a specific video = that video is performing |

#### 2. Watch Behavior Signals (The Real Algorithm)

| Signal | Weight | Notes |
|--------|--------|-------|
| **Completion rate** | Critical | Did they watch to the end? Most important signal. |
| **Loop rate** | Very High | Did it play again automatically? Rewatches signal deep engagement. |
| **Watch time** | Very High | Total seconds watched across all views |
| **Swipe-away rate** | Very High (negative) | Swiping off = strong rejection signal |
| **Average view duration** | High | Combined with completion rate |
| **"Not interested" taps** | High (negative) | Explicit rejection signal |

**The brutal truth:** The first 1-3 seconds determine everything. If viewers swipe away immediately, TikTok stops pushing the video. If they watch to the end and loop, TikTok amplifies it massively.

#### 3. Video Information Signals

| Signal | Notes |
|--------|-------|
| Caption keywords | Algorithm reads captions semantically; keyword-rich captions improve classification |
| Hashtags | Help categorize content; use 3-5 relevant tags |
| Sounds/music | Trending sounds give distribution boost; algorithm knows what's trending |
| On-screen text | Read and analyzed by algorithm; contributes to search indexing |
| Spoken words (auto-caption) | Transcribed and indexed for search matching |
| Visual content | Computer vision analyzes what's in the video |

### The Distribution Model

**Every video goes through a testing sequence:**

1. **Micro-audience test:** Shown to ~300-500 users who match the inferred topic
2. **Performance scoring:** Watch time, completion, shares measured
3. **If passes threshold:** Shown to ~3,000-5,000 users
4. **If passes again:** Shown to ~30,000-50,000 users
5. **If passes again:** Pushed to hundreds of thousands or millions
6. **Each stage uses fresh scoring** — past account performance doesn't carry forward

**This is why:** A mediocre video from a large account can die at stage 1. An exceptional video from a zero-follower account can hit stage 5.

### What Gets Boosted

1. **Videos that get rewatched** — loop rate is TikTok's purest quality signal
2. **Trending sounds** — personal accounts can use licensed trending audio; gives distribution boost
3. **Trending hashtags** — #[challenge] or trending topics get extra test pool exposure
4. **Content over 60 seconds** — Creator Rewards Program now rewards longer retention; algorithm has shifted
5. **Original sounds** — If your audio goes viral (others use it), your original video gets massive re-exposure
6. **TikTok search optimization** — With 41% of Gen Z using TikTok as primary search engine, searchable content performs long-term
7. **Interactive content** — Duets and Stitches that reference your video boost your original's exposure

### What Gets Suppressed

1. **Watermarks from other platforms** — Instagram, YouTube Shorts logos suppress distribution
2. **Early swipe-away behavior** — If first batch swipes fast, distribution stops immediately
3. **Low video quality** — Blurry, pixelated, or poorly-lit content gets fewer impressions
4. **Duplicate content** — Reposting your own videos is detected and suppressed
5. **Already-watched content** — TikTok won't show you a video you've already seen
6. **Spam signals** — Rapid-fire posting without engagement
7. **Business account + copyrighted music** — Using restricted audio blocks distribution

---

## TikTok Search (The New SEO Frontier)

**TikTok is now a search engine.** 41% of Gen Z use it as their primary search tool. Google now shows TikTok videos in its search results.

### How TikTok Search Works

- Users search keywords in the search bar
- TikTok surfaces videos where those keywords appear in:
  - Caption
  - On-screen text
  - Spoken words (auto-transcribed)
  - Hashtags
  - Account name/bio

### TikTok SEO Strategy

1. **Say your keywords out loud** — TikTok transcribes spoken audio. Saying "how to write LinkedIn posts" in your video gets indexed for that search.
2. **Put keywords on screen** — Text overlays are read by the algorithm
3. **Include keywords in your caption** — The first 60-80 characters matter most
4. **Use 3-5 specific hashtags** — More specific beats more popular (e.g., #linkedintips beats #socialmedia)
5. **Think in search terms** — Title your video like a search query: "How to write LinkedIn posts that actually get engagement" not "LinkedIn tips 🔥"

---

## Gotchas

### Business Account Audio Restriction (Career-Ending Mistake)

**Personal accounts** can use any sound in TikTok's library, including trending licensed music.

**Business accounts** are restricted to TikTok's Commercial Music Library (much smaller, no trending songs).

**This is huge.** Trending audio gives significant distribution boosts. Business accounts can't access 90% of trending sounds.

**Workaround options:**
- Use original audio (record your own, use voiceover)
- Use royalty-free music from the Commercial Music Library
- Use trending sounds creatively via Duet/Stitch (different rules than original posts)
- Build your OWN original sound into a trend

**The real takeaway:** If you're a founder/SMB, consider whether a business account is worth the audio restriction. Many creators use personal accounts with a business profile handle (@yourbrand) to keep audio access.

### The Cross-Posting Suppression

**TikTok watermarks on content cross-posted to other platforms:**
- Instagram suppresses TikTok watermarks
- YouTube Shorts suppresses TikTok watermarks

**Reverse is also true:**
- TikTok suppresses videos that look like repurposed Instagram Reels or YouTube Shorts

**Solution:** Export videos without watermarks. Different caption strategy per platform. Native posting performs best everywhere.

### Posting Frequency Trap

**More is not more on TikTok.** Posting 5 times a day can actually hurt your channel because:
- Each video competes with your others for the same audience pool
- Low-performing videos in rapid succession can lower your account's overall quality score
- Followers see repetitive content and engage less

**Recommended:** 1-3 videos per day maximum. Quality > quantity. One exceptional video per week beats 7 mediocre ones.

### The First 3 Seconds Are Everything

Unlike YouTube (where you have 30 seconds to hook) or LinkedIn (where readers expand text), on TikTok you have **under 3 seconds** before swipe-away behavior kicks in.

**Patterns that work:**
- Start mid-action (not with intro, logo, or title card)
- Text overlay of the punchline immediately
- Something visually unexpected in frame 1
- Speaking directly to camera with a bold claim
- "Here's the thing nobody tells you about [topic]" — spoken immediately

**What gets swiped:**
- "Hey guys! Welcome back to my channel!"
- Slow zooms or transitions before any content
- Logo animations at the start
- Any intro longer than 1 second

### Duration Sweet Spot in 2026

TikTok has been pushing longer content (1+ minute) via Creator Rewards Program incentives. The algorithm has shifted accordingly:

- **15-30 seconds:** Still works for meme-format and trending audio content. Lower RPM.
- **60-90 seconds:** Sweet spot for educational/founder content. Higher retention signal. Better monetization.
- **3-10 minutes:** For established creators with proven retention. Risky for accounts under 10K followers.

**Recommendation for founders/SMBs:** Target 60-90 seconds. Long enough to deliver real value, short enough to maintain completion rates.

### Trend Timing: Too Late Is Dead

TikTok trends have a very short half-life:
- **Day 1-3:** Early adopters. Small reach but if you're first, high upside.
- **Day 4-7:** Peak trend. Highest reach potential. Jump now or miss it.
- **Day 8-14:** Trend fatigue. Lower reach even if the video is good.
- **Day 15+:** Dead. Cringe to post now.

**How to spot trends early:** Open TikTok's Discover page daily. Check what sounds are rising (not already peaked). Check Creative Center (business.tiktok.com/creator/trends).

### The "Silence Is Fine" Myth

Many TikTok creators post without spoken audio (just on-screen text + background music). This is fine for some niches.

**But:** Spoken audio is transcribed and indexed for search. If you never speak in your videos, you miss TikTok SEO entirely. For founder/SMB content, voiceover or speaking to camera is almost always better than silent text posts.

---

## Content Strategy for TikTok

### Posting Frequency & Timing

- **Recommended:** 1-3 videos per day
- **Minimum for growth:** 1 video per day (consistency signals matter to the algorithm)
- **Best times (general):** Afternoon (2-5 PM) and evening (7-9 PM) in audience's time zone
- **Reality:** Because TikTok can resurface content weeks later, timing matters LESS than on X or LinkedIn. Quality content finds its audience.

### Content Mix for Founders/SMBs

| Type | % | Examples |
|------|---|---------|
| Educational/how-to | 40% | "How I got our first 100 customers" "3 mistakes founders make with hiring" |
| Behind-the-scenes | 25% | Office/WFH setup, team moments, product building process |
| Trending format + your niche | 20% | Putting your spin on a trending sound/format |
| Direct value (tips, lists) | 10% | Quick-fire advice in 60-90 seconds |
| Brand/product | 5% | Show don't tell — demonstrate value, don't advertise |

### What NOT to Do on TikTok

- Start videos with intros, logos, or "welcome back" (immediate swipe)
- Use restricted sounds on business accounts (breaks distribution)
- Post watermarked content from other platforms
- Copy-paste LinkedIn posts as text-on-screen without adaptation
- Ignore trending sounds when they're genuinely relevant
- Post 10 videos a day to try to "beat the algorithm"
- Over-produce (polished corporate video ≠ authenticity)
- Post silent text videos without any audio strategy
- Use all-caps captions (reads as spam)
- Use 30+ hashtags (3-5 is the standard)

---

## Platform-Specific Voice Guide

### TikTok Tone

TikTok rewards **fast, direct, authentic, entertaining, educational**. The platform's culture values:

- **Speed** — Get to the point in under 3 seconds
- **Energy** — Even calm content needs to feel alive and purposeful
- **Authenticity over production** — iPhone in good light > expensive camera in bad lighting
- **Personality** — Dry, corporate content dies. Have a perspective. Be someone.
- **Specificity** — "I grew my newsletter from 0 to 10K in 90 days" > "I grew my newsletter fast"

### Voice Calibration

| Dimension | TikTok Sweet Spot |
|-----------|-------------------|
| Formality | Casual to very casual. Contractions, informal phrasing, actual personality. |
| Pacing | Fast. No wasted seconds. Every sentence should earn its place. |
| Emoji in caption | 1-3 max. Used for visual anchoring, not decoration. |
| Hashtags | 3-5 specific, relevant. One can be trending if genuinely applicable. |
| Spoken style | Conversational, direct, like explaining to a smart friend. Not scripted-sounding. |
| Length (spoken) | Short sentences. Pause for emphasis. Don't rush — pace, not speed. |
| Humor | High value. Self-deprecating > sarcastic. Relatability wins. |
| Professionalism | Lower than LinkedIn, but professional content can work if personality is there. |

### Hook Patterns (First 3 Seconds)

**Text overlay (on-screen):**
- "The mistake that cost me $50K"
- "Nobody tells founders this about [topic]"
- "POV: You just [relatable situation]"
- "I tested [X]. Here's what happened."

**Spoken:**
- "Here's the thing nobody talks about with [topic]:"
- "I wish someone told me this before I [did thing]:"
- "Stop doing [common practice]. Here's why:"
- "This one change [made a specific measurable difference]:"

**Visual:**
- Start mid-action (showing, not telling)
- Reaction to something (creates curiosity about what they're reacting to)
- Before/after (show the result first)

### CTA Patterns

- "Save this for later 📌" (saves = strong signal)
- "Share with a founder who needs this" (shares = strongest signal)
- "Comment [word] if you want part 2" (comment volume signal; be specific, not "yes/no")
- "Follow for more [specific content type]"
- **Avoid:** "Like and subscribe" energy — feels YouTube-era, not TikTok-native

---

## Emoji Guide for TikTok

### TikTok Emoji Culture

TikTok has the most unique emoji culture of all 6 platforms. Platform-specific emoji meanings:

- 💀 = "I'm dying/this is too funny" (not literal death)
- 🧍 = "I'm just standing here awkwardly relating to this"
- 👁👄👁 = Shocked/witnessing something
- 🫡 = Respectful, "I understand"
- 🤌 = Chef's kiss / perfection (imported from Italian internet)
- ✨ = Aesthetic, aspirational
- 📌 = Save this, bookmark

**In captions:** 1-3 emoji. Used as visual punctuation. TikTok users scroll fast — emoji signal tone quickly.

**In comments:** React with relevant emoji when engaging — it's culturally normal.

**Avoid in captions:** 🚀💰🔥💪🙏 in sequence (startup cringe culture that doesn't translate to TikTok)

---

*Sources: Sprout Social TikTok Algorithm Guide (2026), HeyOrca TikTok Specs (2026), TikTok Newsroom official documentation, Wordstream TikTok Algorithm Guide (2026), TikTok Creator Portal, Darkroom Agency TikTok breakdown (2026), Go-Viral.app algorithm analysis (2026).*
