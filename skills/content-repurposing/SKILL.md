---
name: content-repurposing
description: Transform long-form content into multiple platform-native social posts. Use when user has a blog post, article, podcast transcript, video transcript, or any long-form content and wants to atomize it into social content for multiple platforms. Highest-leverage skill — one input becomes many outputs.
---

# Content Repurposing

<HARD-GATE>
Before repurposing:
1. Load social-context/config.json
2. Load platform references for ALL target platforms
3. Load social-copywriting/references/anti-patterns.md
</HARD-GATE>

## Process

### 1. Ingest Source Content
Accept any of:
- URL (fetch and extract)
- Pasted text
- File path
- Transcript (podcast/video)

Identify the source format and length.

### 2. Extract Core Elements

From the source, extract:
- **Main thesis** (one sentence)
- **Key insights** (3-7 distinct points)
- **Supporting data/examples** (specific numbers, stories, quotes)
- **Controversial/surprising elements** (what would make someone stop scrolling)
- **Practical takeaways** (what can the reader DO with this)

### 3. Apply the Repurposing Matrix

| Source Element | X/Twitter | LinkedIn | Reddit | Instagram | TikTok | YouTube |
|---------------|-----------|----------|--------|-----------|--------|---------|
| Main thesis | Contrarian single tweet | Hook + expanded argument | Text post with evidence | Carousel slide 1 or caption hook | Video hook (3s) | Video title + description |
| Key insights | Thread (one per tweet) | Numbered insights in post | Detailed breakdown post | Carousel slides (one per slide) | Video beats | Video chapters |
| Data/examples | Screenshot + context tweet | Data-led post | Evidence-backed post | Infographic/chart carousel | On-screen text + voiceover | Screen recording |
| Controversial take | Hot take tweet | Opinion post with reasoning | Discussion prompt | Text-on-image Reel | Talking head video | Community post |
| Practical takeaway | Actionable single tweet | How-to with steps | Step-by-step guide | Save-worthy carousel | Tutorial video | How-to video |

### 4. Generate Platform Outputs

For each target platform, generate **completely independent content.** Not the same text with minor tweaks.

**Minimum output per source:**
- 2-3 X/Twitter posts (at least one thread if enough material)
- 1-2 LinkedIn posts (text or carousel outline)
- 1 Reddit post (if subreddit-appropriate)
- 1 Instagram caption + carousel outline
- 1 TikTok script outline
- 1 YouTube Shorts script OR community post

Only generate for platforms listed in config.json → platforms.active.

### 5. Cross-Reference Check
- Do any two platform outputs say the exact same thing? → Rewrite
- Does each output feel native to its platform? → If not, revise
- Is the content pillar tagged consistently across outputs?
- Are the outputs sequenced? (Which to post first for maximum impact?)

### 6. Output Format

```
## Source: [Title/URL]
**Main thesis:** [one sentence]
**Key insights extracted:** [numbered list]

---

### X/Twitter

#### Post 1 (Single)
[copy]

#### Post 2 (Thread)
[thread tweets]

---

### LinkedIn

#### Post 1 (Text)
[copy]

---

### Reddit

#### Post 1 (r/[subreddit])
**Title:** [title]
**Body:** [body]

---

[...continue for each active platform...]

---

## Posting Sequence
1. [Platform] — [content] — [why first]
2. [Platform] — [content] — [optimal timing]
3. ...

## Cross-Posting Notes
- What stayed consistent: [core message]
- What changed: [format, tone, CTA, length per platform]
- Content log entries: [JSONL for each piece]
```

### 7. Log to Content Log

Append each generated piece to `data/content-log.jsonl` with `source: "repurposed"` and `source_id` pointing to the original.

## Atomization Patterns

### Blog Post → Social
1. **Title → X hook** (rewrite as curiosity gap or hot take)
2. **Introduction → LinkedIn hook** (first paragraph adapted for "see more")
3. **Each H2 section → one X tweet or one carousel slide**
4. **Pull quotes → Instagram text-on-image**
5. **Key stat → standalone data post on any platform**
6. **Conclusion/CTA → TikTok script hook**

### Podcast/Video Transcript → Social
1. **Best 60-second clip → short-form video** (TikTok/Reels/Shorts)
2. **Key quotes → X posts**
3. **Topic summary → LinkedIn post**
4. **Q&A segments → Reddit discussion posts**
5. **List of resources mentioned → save-worthy carousel**

### Newsletter → Social
1. **Subject line → X hook**
2. **Main essay → LinkedIn post**
3. **Curated links → thread with commentary**
4. **Personal anecdote → story-format post**

## Gotchas

- **Repurposing ≠ copy-pasting.** The same text posted to X and LinkedIn will underperform on both.
- **Not everything repurposes.** A 500-word blog post might yield 2-3 social posts, not 15. Don't force it.
- **Sequence matters.** Post the "discovery" format first (Reels, TikTok) then the "depth" format (LinkedIn, blog link).
- **Attribution.** When repurposing others' content, always credit the source.

## Related Skills

- **social-copywriting** — For writing individual platform posts
- **thread-writing** — For writing threads from repurposed insights
- **content-calendar** — For scheduling repurposed content
- **content-review** — For quality-checking repurposed outputs

## This Skill Does NOT:

- Create original content from scratch (use social-copywriting or content-ideation)
- Generate visual assets (use social-visual-design)
- Analyze performance (use social-analytics)
