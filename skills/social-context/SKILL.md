---
name: social-context
description: Foundation context for all social-skills. Use FIRST before any content creation, strategy, or analysis skill. Loads brand voice, audience personas, active platforms, and content pillars. If config.json doesn't exist, runs quick-start or full-brand-audit interview to create it.
---

# Social Context — Foundation

<HARD-GATE>
Every other social-skills skill MUST load this skill's config.json before executing.
If config.json does not exist, run the setup interview below BEFORE any content work.
No exceptions. "It's just a quick post" is not an exception.
</HARD-GATE>

## Setup Interview

If `config.json` does not exist in this skill's directory, run one of these interviews:

### Quick Start (5 questions, ~2 minutes)

1. **What's your brand/company name?**
2. **What do you do in one sentence?** (e.g., "We build project management tools for remote teams")
3. **Who's your target audience?** (e.g., "Early-stage SaaS founders, 25-45, technical background")
4. **Which platforms are you active on?** (X, LinkedIn, Reddit, Instagram, TikTok, YouTube — pick all that apply)
5. **What tone fits your brand?** (e.g., "Direct and slightly irreverent" or "Professional but warm")

Generate config.json from answers. Tell the user they can run `/full-brand-audit` later to deepen it.

### Full Brand Audit (15+ questions, ~10 minutes)

Run this when user explicitly requests deeper setup or says `/full-brand-audit`.

**Identity:**
1. Brand/company name
2. One-sentence description
3. Mission/purpose (why you exist beyond making money)
4. 3-5 adjectives that describe your brand personality
5. What you are NOT (anti-positioning: "We are NOT corporate, NOT salesy, NOT generic")

**Audience:**
6. Primary audience (demographics + psychographics)
7. Secondary audience (if any)
8. What keeps your audience up at night? (pain points)
9. What does your audience aspire to? (goals)
10. Where does your audience hang out online? (specific subreddits, newsletters, communities)

**Voice:**
11. Tone spectrum: where do you fall on formal↔casual, serious↔playful, technical↔accessible?
12. Words/phrases you ALWAYS use (brand vocabulary)
13. Words/phrases you NEVER use (banned language)
14. A real person or brand whose voice is similar to yours
15. How does your voice change per platform? (or should it stay consistent?)

**Strategy:**
16. Content pillars (3-5 topics you consistently create about)
17. Primary goal per platform (growth? leads? community? thought leadership?)
18. Current posting frequency per platform
19. Competitors or accounts you admire (for reference, not copying)
20. Any existing brand guidelines, style guides, or voice docs? (load if available)

## config.json Schema

```json
{
  "brand": {
    "name": "",
    "description": "",
    "mission": "",
    "personality": [],
    "anti_positioning": []
  },
  "audience": {
    "primary": {
      "description": "",
      "demographics": "",
      "pain_points": [],
      "goals": [],
      "communities": []
    },
    "secondary": null
  },
  "voice": {
    "tone": {
      "formality": "casual|professional-casual|professional|formal",
      "energy": "calm|warm|energetic|intense",
      "humor": "none|subtle|moderate|frequent"
    },
    "always_use": [],
    "never_use": [],
    "similar_to": "",
    "platform_variants": {
      "x-twitter": "",
      "linkedin": "",
      "reddit": "",
      "instagram": "",
      "tiktok": "",
      "youtube": ""
    }
  },
  "platforms": {
    "active": [],
    "primary_goal": {},
    "posting_frequency": {}
  },
  "content_pillars": [],
  "competitors": [],
  "setup_mode": "quick-start|full-brand-audit",
  "created": "",
  "last_updated": ""
}
```

## How Other Skills Use This

Every creation skill should:

1. Read `social-context/config.json`
2. Load the relevant platform reference from `references/platforms/<platform>.md`
3. Apply brand voice and audience context to all outputs
4. Respect `never_use` words and `anti_positioning` in generated content
5. Match the `platform_variants` voice when writing for a specific platform

## Platform References

Deep platform knowledge lives in `references/platforms/`:
- `x-twitter.md` — Algorithm, specs, gotchas, voice guide, hook patterns
- `linkedin.md` — Algorithm, specs, gotchas, voice guide, hook patterns
- `reddit.md` — Algorithm, specs, gotchas, voice guide (Reddit is VERY different)
- `instagram.md` — Algorithm, specs, gotchas, Reels/carousel strategy
- `tiktok.md` — Algorithm, specs, gotchas, FYP mechanics, search SEO
- `youtube.md` — Algorithm (long-form + Shorts), specs, thumbnail strategy, SEO

Load only the platform(s) relevant to the current task.

## Skill Selection Guide

| Task | Use This Skill | Related Skills |
|------|---------------|----------------|
| "Write a LinkedIn post" | social-copywriting | social-context, content-review |
| "Create a thread for X" | thread-writing | social-context, content-review |
| "Turn this blog into social posts" | content-repurposing | social-context, social-copywriting |
| "Plan my content for next week" | content-calendar | social-context, content-ideation, posting-strategy |
| "What should I post about?" | content-ideation | social-context, content-strategy |
| "When should I post this?" | posting-strategy | social-context |
| "Review this post before I publish" | content-review | social-context |
| "Analyze this account's strategy" | account-analysis | social-context |
| "Quick — make this go viral" | omni-viral-humanizer | (standalone, no setup needed) |

## This Skill Does NOT:

- Generate content (use social-copywriting, thread-writing, etc.)
- Analyze performance (use social-analytics)
- Plan calendars (use content-calendar)
- Review content quality (use content-review)

It provides the **foundation context** that all other skills read.

## Updating Context

User can update config.json at any time by saying:
- "Update my brand voice" → re-run relevant voice questions
- "Add a new platform" → add to active platforms + set goals/frequency
- "Change my content pillars" → update pillars array
- "Full brand audit" → re-run complete interview

Always update `last_updated` timestamp when config changes.
