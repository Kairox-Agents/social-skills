# LinkedIn — Platform Deep Dive

*Last updated: March 2026*

---

## Platform Specs

### Character Limits

| Element | Limit |
|---------|-------|
| Personal post | 3,000 characters |
| Company page post | 700 characters |
| Article title | 100 characters |
| Article body | 125,000 characters |
| Newsletter title | 64 characters |
| Comment | 1,250 characters |
| Headline (profile) | 220 characters |
| About/Summary | 2,600 characters |
| "See more" cutoff | ~210 characters (~3-4 lines) |

### Image Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Format |
|------|-----------------|--------------|---------------|--------|
| Feed image (square) | 1200 × 1200 px (or 1080 × 1080) | 1:1 | 5 MB | JPG, PNG, GIF (static) |
| Feed image (landscape) | 1200 × 628 px | 1.91:1 | 5 MB | JPG, PNG |
| Feed image (vertical) | 1080 × 1350 px | 4:5 | 5 MB | JPG, PNG |
| Link preview image | 1200 × 627 px | 1.91:1 | 5 MB | JPG, PNG |
| Article cover image | 1200 × 644 px | 1.86:1 | 10 MB | JPG, PNG |
| Profile photo | 400 × 400 px | 1:1 (circle crop) | 8 MB | JPG, PNG |
| Personal banner | 1584 × 396 px | 4:1 | 8 MB | JPG, PNG |
| Company page logo | 300 × 300 px | 1:1 | 4 MB | JPG, PNG |
| Company page cover | 1128 × 191 px | ~6:1 | 4 MB | JPG, PNG |

**Multi-image posts:** Up to 20 images. Use same aspect ratio across all images — LinkedIn's auto-collage builder crops unpredictably when mixing orientations. Four square (1:1) images create the cleanest grid.

**Vertical image note:** You CAN upload 9:16 images, but LinkedIn crops them to 4:5 in the feed. Keep key content within 1080 × 1350 px frame.

### Video Specs

| Type | Recommended Size | Aspect Ratio | Max File Size | Duration | Format |
|------|-----------------|--------------|---------------|----------|--------|
| Native video (landscape) | 1920 × 1080 px | 16:9 | 5 GB | 3 sec – 10 min | MP4 |
| Native video (portrait) | 1080 × 1920 px | 9:16 | 5 GB | 3 sec – 10 min | MP4 |
| Native video (square) | 1920 × 1920 px | 1:1 | 5 GB | 3 sec – 10 min | MP4 |

**LinkedIn Live:** Separate feature, requires application/approval.

### Document/Carousel Specs

| Element | Limit |
|---------|-------|
| Max pages | 300 pages |
| Max file size | 100 MB |
| Formats | PDF, PPT, PPTX, DOC, DOCX |
| Recommended slide size (square) | 1080 × 1080 px |
| Recommended slide size (vertical) | 1080 × 1350 px |

**Carousel = Document post.** Upload a PDF with slides. Each page becomes a swipeable slide. This is LinkedIn's highest-engagement native format.

### Polls

- 2–4 options
- 30 characters per option
- Duration: 1 day, 3 days, 1 week, or 2 weeks

### Newsletter

- Available for Creator Mode profiles and company pages
- Title: 64 characters
- Subscribers receive notification for each issue
- Separate distribution from feed posts (email notification to subscribers)

---

## Algorithm (2026 LLM-Powered Update)

### Architecture Overview

LinkedIn fundamentally rebuilt its feed algorithm in 2025-2026, replacing engagement-history-based ranking with **LLM-powered semantic understanding**:

- **Unified LLM-Based Retrieval:** Uses dual encoder architecture to transform user profiles and posts into dense vector embeddings. Matches content semantically — the algorithm understands that "electrical engineering" and "small modular reactors" are related topics, even without keyword overlap.
- **Generative Recommender (GR) Model:** Transformer with causal attention that processes a user's entire interaction history as a chronological sequence. Understands how interests EVOLVE over time, not just static preferences.
- **Real-time adaptation:** When a user engages with new topics, the feed updates "almost immediately" — not in batch processing cycles.

### The Three-Stage Ranking Pipeline

#### Stage 1: Quality Classification

Every post is classified before ranking:
- **Spam** → Removed entirely
- **Low quality** → Deprioritized before ranking begins
- **High quality ("Clear")** → Proceeds to engagement testing

**What triggers low-quality classification in 2026:**
- Engagement bait ("Comment YES if you agree")
- Overly promotional copy without standalone value
- Excessive tags/hashtags/emojis (looks spammy)
- External links in post body
- Overposting in short windows
- "Overly AI-sounding phrasing" — repetitive, generic, unnatural cadence
- Video-text mismatch (video unrelated to accompanying text)
- Recycled thought leadership (old content reposted without new insight)

#### Stage 2: Engagement Testing ("Golden Hour")

Posts that pass quality gates are shown to a small initial audience (subset of your connections). The algorithm watches the first ~60 minutes for:

**High-value signals:**
- **Thoughtful comments** that add context or start a thread (MOST powerful visible signal)
- **Dwell time** — how long someone spends reading (hidden but extremely important)
- **"See more" expansion rate** — whether people click to read the full post
- **Saves** — strong value indicator, especially for educational content
- **Profile clicks** — clicking to your profile after reading
- **Thread depth** — back-and-forth replies, not one-off comments

**Low-value signals:**
- Likes/reactions alone (weakest signal)
- "Great post!" comments
- Emoji-only replies
- Engagement from the same small group (pod detection)

#### Stage 3: Personalization & Network Scaling

If the post performs well, distribution expands based on three signals:

1. **Connection strength ("Who you know")** — First-degree connections and frequent interactors get priority. Relationship signals matter more than follower count.
2. **Topic relevance ("What you talk about")** — LLM semantic matching against user interest profiles. Hashtags play a SMALLER role — the algorithm reads your actual text.
3. **Engagement probability ("Will this person care?")** — Per-user prediction based on their history, content type preferences, and topic engagement patterns.

**Key implication:** Distribution is "precision delivery to people most likely to care," not broadcast to all followers.

### What Gets Boosted

1. **Subject-matter expertise** — Consistent posting within a defined topical area, demonstrated knowledge, engagement from relevant professionals. Specialists beat generalists.
2. **Meaningful conversations** — Substantive comments with back-and-forth threads. Three thoughtful comments > 100 fire emoji reactions.
3. **Dwell time** — Posts that hold attention (well-structured, scannable, narrative-driven). A text post that gets read fully can outperform a post with more likes.
4. **Saves** — "Bookmark" signal indicates high value. Educational content benefits most.
5. **Native formats** — Content that keeps users on-platform (text, images, carousels, native video) over external links.
6. **Document/carousel posts** — Extended dwell time from slide-by-slide interaction sends strong quality signal.
7. **Profile actions** — Profile clicks after reading indicate genuine interest in the author.

### What Gets Suppressed

1. **Engagement bait** — "Comment YES," "Tag someone who needs this," "Double tap if this resonates" — actively filtered as low quality.
2. **External links** — Links in post body suppress distribution. LinkedIn wants users on-platform. (See Gotchas for workarounds.)
3. **Engagement pods** — LinkedIn actively works to neutralize pod behavior and detect automated comment tools.
4. **Generic AI content** — Templated, predictable content without genuine insight is deprioritized regardless of production method.
5. **Recycled content** — Repurposed content that adds nothing new.
6. **Video-text mismatch** — Video unrelated to accompanying text, designed to game impressions.
7. **Overposting** — Multiple posts in short windows dilute per-post distribution.

### Time Dynamics

- **"Golden Hour"** — First 60 minutes critical for engagement testing
- **Extended visibility:** LinkedIn posts can surface days or even weeks later if the algorithm determines continued relevance (unlike X where posts die in 24 hours)
- **Dwell time is uniquely powerful on LinkedIn** — a hidden signal that can boost a text-only post with zero likes if people actually READ it
- The GR model tracks evolving interests — recent behavior weighs more than historical patterns

---

## Gotchas

### The Link Problem

External links suppress distribution on LinkedIn (the platform wants users to stay). This is the single most common mistake founders make.

**Workarounds that work:**
- Post valuable content natively in the text → add link in the FIRST COMMENT
- Write "Link in comments 👇" at the end of your post
- For blog posts: extract the key insights into the post text, make it complete. Link is a bonus, not the point.
- Use document/carousel format to present the content natively

**What doesn't work:**
- Link shorteners (doesn't bypass detection)
- Editing the post to add a link later (still affects distribution)
- Hiding links in image alt text (doesn't help distribution)

### Hashtag Confusion (LinkedIn-Specific)

- **Hashtags role has diminished significantly in 2026.** The LLM reads your actual text semantically — it doesn't need hashtags to categorize.
- **0-3 hashtags:** Acceptable. Helps with categorization but NOT the primary discovery mechanism.
- **4-5 hashtags:** Diminishing returns.
- **6+ hashtags:** Looks spammy, can trigger low-quality classification.
- **In articles:** Do NOT use hashtags in LinkedIn article bodies — they actively hurt reach.
- **In carousel posts:** Skip hashtags entirely. The document content speaks for itself.
- **Trending hashtags:** Less powerful than on X. LinkedIn doesn't have a "trending" culture the same way.

### The "See More" Trap

- LinkedIn truncates posts at ~210 characters (3-4 lines)
- If nobody clicks "see more," the algorithm interprets this as low-interest content
- **Your first 210 characters ARE the post** — they determine whether anyone reads the rest
- **Hook formulas that drive "see more" clicks:** Curiosity gaps, bold claims, specific numbers, contrarian takes
- **Anti-pattern:** Starting with "I'm excited to announce..." or "Happy to share..." — generic openers that don't compel expansion

### Carousel vs Regular Post

- **Carousels consistently get 2-3x engagement** vs single images and often beat video
- **Why:** Extended dwell time (swiping through slides), each slide is a micro-engagement moment
- **Sweet spot:** 8-12 slides. Under 5 feels incomplete. Over 15 loses most readers.
- **First slide = hook.** Think of it as a book cover. Bold text, clear value proposition, visual intrigue.
- **Last slide = CTA.** "Follow for more," "Save this for later," "What would you add? Comment below."
- **Gotcha:** Uploading a PDF with complex layouts can render poorly. Simple, bold text + clean graphics > complex designs.

### Company Page vs Personal Profile

- **Personal profiles get 5-10x more organic reach** than company pages (700 char limit vs 3000 chars is part of it)
- **Company page content feels corporate.** Personal profile content feels human. The algorithm and the audience both prefer human.
- **Strategy:** Founder posts on personal profile > company page posts for organic reach. Use company page for events, job posts, and formal announcements.
- **Employee advocacy:** Employees sharing company content from personal profiles dramatically outperforms company page posting.

### Editing Posts

- You CAN edit LinkedIn posts after publishing
- **Gotcha:** Editing within the first hour can disrupt the golden-hour engagement testing
- Some creators report editing kills reach. Others see no impact. Safest: proofread before posting.
- Adding a link via edit AFTER the initial engagement window is a viable workaround for the link suppression issue

### Post Frequency

- **Sweet spot:** 1 post per business day (5/week) for founders
- **Minimum for visibility:** 2-3 posts per week
- **Maximum before diminishing returns:** 1 post per day (multiple posts per day compete against each other due to author diversity limits)
- **Weekend posting:** Lower competition, but also lower audience. Test for your niche.
- **Consistency matters more than volume.** 3 posts/week for 6 months > daily posting for 2 months then silence.

### AI Content Detection

LinkedIn's LLM-powered quality filter specifically identifies:
- Repetitive template structures
- Generic advice without personal context
- Predictable phrasing patterns
- Content that "could apply to anyone"

**How to use AI without triggering detection:**
- Use AI for structure/outline, add personal stories and specific examples
- Inject your actual opinions and controversial takes
- Reference specific projects, numbers, or experiences
- Read it aloud — if it sounds like a press release, rewrite it

---

## Content Strategy for LinkedIn

### Optimal Posting Frequency & Timing

- **Best days:** Tuesday, Wednesday, Thursday
- **Best times:** 8-10 AM, 12-1 PM (audience's time zone). Weekday mornings perform best.
- **Monday:** Decent but competitive. People are catching up.
- **Friday:** Lower engagement as people wind down.
- **Weekend:** Lower volume (less competition) but smaller audience. Can work for lifestyle/personal content.

### Content Mix for Founders/SMBs

| Content Type | % of Posts | Purpose |
|-------------|-----------|---------|
| Value/educational (frameworks, how-tos, lessons) | 35% | Build authority, generate saves |
| Personal narrative/journey | 25% | Build connection, generate comments |
| Industry insight/commentary | 20% | Establish thought leadership |
| Behind-the-scenes/building-in-public | 10% | Humanize brand |
| Promotional/product updates | 5% | Direct business value |
| Engagement posts (questions, polls) | 5% | Drive conversations |

### Post Text Length Sweet Spot

- **Optimal for engagement:** 150-250 words (800-1200 characters)
- **Short posts (<100 words):** Can work for bold takes or questions but miss dwell time signal
- **Long posts (300+ words):** Work if structured well with line breaks. Risk losing readers if dense.
- **The real rule:** Make it as long as it needs to be, not longer. Every sentence should earn its place.

### Carousel Strategy

- **When to use:** Teaching, step-by-step guides, frameworks, listicles, data breakdowns, storytelling
- **Ideal length:** 8-12 slides
- **Slide structure:** One idea per slide. Bold headline + supporting detail + visual.
- **Design:** Simple backgrounds, large readable text, consistent brand colors. Don't over-design.
- **First slide:** Hook (the value proposition). "7 frameworks that changed how I hire."
- **Last slide:** CTA + author info. "Save this. Follow for more. What would you add?"
- **PDF format:** Export as PDF, upload as document post. This IS the carousel.

### What NOT to Write on LinkedIn

- "I'm humbled and honored to announce..." (LinkedIn's most hated opener)
- "Agree? 🙏" (engagement bait, detected and suppressed)
- Motivational quotes without personal context ("Success is a journey, not a destination")
- "Day 1 at my new role!" without any actual insight
- Buzzword bingo: synergy, leverage, paradigm shift, game-changer, disruptive
- Humble-bragging disguised as gratitude ("So grateful for this Forbes feature...")
- Generic "5 tips for success" content that could apply to anyone
- Corporate press release reposts
- Cross-posted tweets without any adaptation (different platform, different voice)

---

## Platform-Specific Voice Guide

### LinkedIn Tone

LinkedIn rewards **professional but human, substantive, and specific** content. The platform's culture values:

- **Substance** — Every post should contain a genuine insight, lesson, or perspective. "Fluff" is death on LinkedIn.
- **Specificity** — "Revenue grew 40% in Q2" > "We had a great quarter." Numbers, examples, and concrete details.
- **Narrative** — Stories perform better than bullet points on LinkedIn. Beginning-middle-end structure.
- **Vulnerability (professional)** — Failures and lessons learned resonate deeply. "What I got wrong about hiring" > "How to hire great people."
- **Authority without arrogance** — Confident expertise, not lecturing. "Here's what I've seen work" > "You must do this."

### Voice Calibration

| Dimension | LinkedIn Sweet Spot |
|-----------|---------------------|
| Formality | Professional-casual. Not corporate, not Twitter-casual. Think "smart conversation at an industry dinner." |
| Sentence length | Mix short and medium. One-sentence paragraphs for emphasis. Never walls of text. |
| Emoji usage | 0-3 per post. Use as visual markers, not decoration. ✅→📊🔑 are common. Never 🚀💰🔥 |
| Hashtag usage | 0-3 per post. Never in articles/carousels. |
| Paragraphs | Short. 1-2 sentences each. White space is your friend on mobile. |
| Personal pronouns | "I" for personal posts. "We" for company/team stories. Never "one" or passive voice. |
| Jargon | Industry-appropriate. B2B/SaaS audience expects business language. Don't over-explain basics. |
| Controversy | Encouraged (professional controversy). LinkedIn rewards takes, not blandness. But stay professional. |

### Hook Patterns That Work on LinkedIn

**Curiosity gap:**
- "Most founders get this completely wrong about [topic]."
- "I've reviewed 500+ [things]. Here's what separates the top 1%."
- "This one change increased our [metric] by [specific number]."

**Story:**
- "2 years ago, I [past state]. Last month, I [current state]. Here's what changed:"
- "I almost fired my best employee. Here's why I'm glad I didn't."
- "The worst advice I ever received as a founder:"

**Value/Framework:**
- "The [name] framework for [outcome] (steal this):"
- "After [experience], here are [number] things I'd tell myself:"
- "If you're struggling with [pain], read this:"

**Contrarian:**
- "[Common practice] is killing your [outcome]. Here's what to do instead."
- "Unpopular opinion: [bold statement]. Let me explain."
- "I stopped [common practice] 6 months ago. Revenue went up [%]."

**Question:**
- "What's the most underrated skill for [role]? I'll start: [your answer]."
- "Would you rather [option A] or [option B]? (Genuinely curious)"
- "What's one piece of advice you wish you'd ignored?"

### CTA Patterns

- "Save this for when you need it 🔖" (drives saves — strong algorithm signal)
- "What would you add? Drop it in the comments." (drives substantive comments)
- "If this resonated, share it with someone who needs to hear it." (drives shares)
- "Follow for more [your niche] insights." (profile follow CTA)
- **Avoid:** "Like if you agree" "Comment YES" "Tag someone" (engagement bait, suppressed)

---

## Emoji & Formatting Guide for LinkedIn

### Emoji Rules

- **0-3 emoji per post** — More looks unprofessional
- **Best uses:** Section markers (✅, ❌, →, 📌, 💡), bullet points (▸ or •), CTAs (🔖, 👇)
- **Never as subject matter:** "🚀 Our company just 💰 raised..." — this isn't Twitter
- **In carousels:** Skip emoji. Let the design speak.
- **Good LinkedIn emoji:** ✅ ❌ → 📊 🔑 📌 💡 🔖 👇 ⚡
- **Bad LinkedIn emoji:** 🚀💰🔥😂🙏💪🤷 in any professional context

### Formatting Best Practices

- **Line breaks are essential.** Single empty line between every 1-2 sentence paragraph.
- **First 210 characters = the hook.** Treat this as a separate creative challenge.
- **One idea per paragraph.** LinkedIn is read on phones. Dense paragraphs lose readers.
- **Bold/italic:** Not supported in regular posts. Use CAPS or spacing for emphasis.
- **Numbered lists:** Work great for frameworks and step-by-step content.
- **Bullet points:** Use Unicode characters (→, ▸, •, ✦) since markdown bullets don't render.

### The LinkedIn-to-Twitter Adaptation Trap

**These are different platforms with different cultures.** Direct cross-posting fails.

| Dimension | LinkedIn | X/Twitter |
|-----------|----------|-----------|
| Tone | Professional-casual | Casual-sharp |
| Length | 150-250 words | 280 chars (or thread) |
| Structure | Narrative paragraphs | Punchy one-liners |
| Emoji | Functional/markers | Personality/decoration |
| Hashtags | 0-3, decreasing importance | 0-1, nearly irrelevant |
| Humor | Subtle, professional | Witty, irreverent |
| Vulnerability | Professional failures | Personal + professional |
| Self-promotion | Acceptable when value-wrapped | Less tolerated |
| Posting time | Business hours | Anytime |

---

*Sources: LinkedIn Engineering blog (LLM-powered feed update 2026), ALM Corp algorithm analysis (March 2026), SourceGeek algorithm guide (2026), Postiv.ai specs guide (2026), SocialBee algorithm breakdown (2026), HeyOrca LinkedIn specs (2026), Sprout Social 2026 benchmarks.*
