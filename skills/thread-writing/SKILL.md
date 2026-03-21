---
name: thread-writing
description: Write platform-native threads and serialized long-form posts for X, LinkedIn, or Threads. Use when user wants a thread, multi-part post, or long-form serialized content. Handles thread architecture, per-tweet optimization, transition hooks, and engagement drop-off mitigation.
---

# Thread Writing

<HARD-GATE>
Before generating any thread:
1. Load social-context/config.json
2. Load platform reference for target platform
3. Load social-copywriting/references/anti-patterns.md
</HARD-GATE>

## Process

### 1. Determine Thread Type

| Type | Best For | Sweet Spot |
|------|----------|------------|
| **Listicle** | Tips, lessons, tools | 5-8 tweets/posts |
| **Story arc** | Personal narrative, case study | 6-10 tweets/posts |
| **Problem-solution** | How-to, framework | 5-7 tweets/posts |
| **Contrarian breakdown** | Hot take with evidence | 5-8 tweets/posts |
| **Case study** | Deep analysis of one example | 7-12 tweets/posts |

### 2. Thread Architecture

**Every thread follows this skeleton:**

```
Tweet 1: HOOK (this determines everything — 90% of impressions)
Tweet 2: CONTEXT (why this matters, what's at stake)
Tweet 3-N: VALUE (the meat — one idea per tweet)
Tweet N+1: SYNTHESIS (what it all means)
Tweet N+2: CTA (drive action — reply, repost, bookmark, follow)
```

### 3. Platform-Specific Rules

#### X/Twitter Threads
- Each tweet: max 280 chars (non-Premium)
- Thread length sweet spot: 5-10 tweets
- Engagement drops ~60% after tweet 4 — front-load your best content
- Use numbering (1/, 2/, etc.) so readers know position
- Each tweet should be self-contained and valuable alone
- Do NOT pad with filler tweets to reach a number
- Cliffhanger between tweets: end tweet mid-thought to pull readers forward
- Last tweet: strong CTA + "Follow @handle for more [topic]"
- No hashtags in threads (looks spammy)
- 🧵 emoji in tweet 1 is sufficient thread indicator

#### LinkedIn Long-Form Posts (Thread-Style)
- Single post format (not multi-post thread)
- Use line breaks + numbered sections to create thread-like flow
- Sweet spot: 150-300 words
- First 210 chars = hook (before "see more")
- Each section: one insight + one proof point
- End with a save-worthy or comment-driving CTA

### 4. Hook Formulas for Threads

**Curiosity gap:**
- "I [did something] for [time period]. Here's what nobody told me:"
- "After [experience], I'd change [number] things:"
- "[Common belief] is wrong. Here's the evidence:"

**Story hook:**
- "Last [time], I [unexpected event]. Here's what happened:"
- "I almost [dramatic outcome]. Thread on what saved me:"

**Value promise:**
- "[Number] [things] that [outcome] (from [experience]):"
- "The [framework/method] that changed how I [activity]:"

**Contrarian:**
- "Everyone says [common advice]. They're wrong. Here's why:"
- "Stop [popular practice]. I stopped [timeframe] ago. Results:"

### 5. Transition Techniques (Between Tweets)

- **Cliffhanger:** End with "But then..." or "What happened next changed everything."
- **Question:** End tweet with a question the next tweet answers
- **Contrast:** "That was the theory. Here's what actually happened:"
- **Numbering:** "1/ ... 2/ ... 3/ ..." (clearest, most scannable)
- **Promise:** "The biggest mistake? Coming in the next tweet."

### 6. Self-Review

- [ ] Tweet 1 hook would stop YOUR scroll
- [ ] Each tweet makes sense standalone (someone might quote-tweet just one)
- [ ] No filler tweets (every tweet earns its place)
- [ ] Engagement drop-off mitigated (best content in tweets 1-4)
- [ ] CTA is specific (not generic "thoughts?")
- [ ] Thread length justified (not padded, not cramped)
- [ ] Anti-patterns check passed

## Gotchas

- **Thread engagement drops steeply.** Tweet 1 gets ~100% impressions. Tweet 5 gets ~30-40%. Tweet 10 gets ~10-15%. Plan accordingly.
- **Don't thread when a single tweet works.** A punchy 280-char single post often outperforms a thin 5-tweet thread.
- **Each tweet competes independently.** A great thread with a weak tweet 1 dies. A mediocre thread with a killer tweet 1 survives.
- **Never use "continued..." as a tweet.** Every tweet must deliver value.

## Related Skills

- **social-copywriting** — For single posts (not threads)
- **content-repurposing** — Can output thread format from long-form content
- **content-review** — Review thread quality before posting

## This Skill Does NOT:

- Write single posts (use social-copywriting)
- Write video scripts (use video-scripting)
- Create visual content (use social-visual-design)
