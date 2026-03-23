# Gotchas — Social Copywriting

## 1. AI-Generated Content Gets Algorithmically Buried

**What happens:** Agent generates clean, well-structured posts using AI-typical patterns (em dashes, "delve," "I'm thrilled to announce," perfect parallel lists). The platform algorithm detects these patterns and reduces distribution.

**The data:** LinkedIn AI-generated content sees 30% less reach and 55% less engagement than human-written posts. AI-generated images get 70% fewer clicks. 54% of LinkedIn posts are now AI-generated, making detection easier. (Source: LinkedIn AI Study 2026, via Slop Corporation analysis, Feb 2026)

**Why it matters:** The irony of using AI to write social content is that platforms are actively penalizing AI-sounding content. The humanization step isn't optional polish — it's a distribution requirement.

**How to avoid:** Always run anti-patterns.md and ai-tell-checklist.md checks. Add specific personal details, imperfections, and opinions that AI doesn't generate by default.

## 2. The Same Content Cross-Posted Without Adaptation

**What happens:** Agent copies the LinkedIn post to X with minor trimming, or pastes the X tweet into Instagram with hashtags appended.

**The data:** Cross-platform watermarks are actively suppressed (Mosseri confirmed TikTok watermarks reduce Instagram distribution). But even without watermarks, identical text underperforms because each platform's algorithm optimizes for different signals — LinkedIn rewards dwell time and saves, X rewards replies, Instagram rewards DM shares.

**How to avoid:** Generate completely independent versions for each platform. Use content-repurposing's matrix, not copy-paste.

## 3. Link Placement Kills Reach on X and LinkedIn

**What happens:** Agent puts a URL in the main post body on X or LinkedIn because it seems natural.

**The data:**
- **X:** 30-50% reach penalty for external links in main tweet. Free accounts with links have zero median engagement since March 2025. (Source: PostEverywhere, from open-source algorithm code)
- **LinkedIn:** External links in post body are deprioritized by 360Brew. (Source: AuthoredUp analysis, Botdog writeup)

**How to avoid:** X: Link in self-reply, not main tweet. LinkedIn: Link in first comment, not post body. Always note the link handling approach in the output metadata.

## 4. Reddit Marketing Voice = Instant Death

**What happens:** Agent writes a Reddit post using the same tone as LinkedIn or Instagram. Uses hashtags, promotional language, emoji in title, or any variation of "Check out my product."

**The data:** Reddit users routinely check post history. Brand accounts with obvious self-promotion get called out, downvoted, and banned. Even indirect promotion ("I happened to build something that solves this...") gets flagged. (Source: r/GrowthHacking, r/AskMarketing — multiple documented ban stories, Mar 2026)

**How to avoid:** Reddit requires a completely different voice. No hashtags, no emoji in titles, no promotional language. Lead with genuine value. If the user's product is relevant, mention it only after providing substantial standalone value.

## 5. The "Content Volume Trap"

**What happens:** Agent generates 5+ posts per day because "consistency is key." Quality drops, engagement per post drops, and the algorithm actually penalizes the account.

**The data:**
- **LinkedIn:** Posting twice within 24 hours consistently reduced reach (Richard van der Blom data, Jan 2026). Posts compete against each other.
- **X:** Algorithm penalizes high post volumes with low per-tweet engagement. 10 quality tweets outperform 30 mediocre ones. (Source: PostEverywhere FAQ)
- **Buffer 2025 data:** Posts doubled across most platforms but half saw engagement DECLINE. More content ≠ more engagement. (Source: CNET reporting on Buffer data, Mar 2026)

**How to avoid:** Quality > quantity. Follow platform-specific frequency guidelines. LinkedIn: max 1/day. X: 2-3/day max. Never generate filler content to hit a number.

## 6. Hooks That Create Expectations the Post Can't Deliver

**What happens:** Agent writes a killer hook — "This one insight changed everything about how I run my business" — but the actual content is a generic tip that doesn't match the dramatic setup.

**Why it matters:** On YouTube, high CTR + low satisfaction = algorithmic penalty (confirmed by YouTube, vidIQ analysis). The same principle applies to all platforms: if you hook people and then disappoint them, you train the algorithm AND your audience to ignore you.

**How to avoid:** Write the content first, THEN write the hook that accurately represents what follows. The hook should be the most interesting true thing you can say about the content, not the most clickable thing you can imagine.
