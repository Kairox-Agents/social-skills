# Quick Start Test — First Post in 5 Minutes

> Walkthrough: install skills → configure social-context → generate first LinkedIn post.

## Prerequisites
- Agent with `social-skills` pack installed
- No prior configuration needed

## Step 1: Trigger social-context Quick Start

**User input:**
```
I want to start posting on LinkedIn. I run a B2B SaaS for project management, targeting startup founders and small teams. My tone is direct and practical — I don't do corporate speak.
```

**Expected agent behavior:**
1. Agent reads `social-context/SKILL.md`
2. Detects no existing `config.json` → triggers quick-start interview
3. Extracts from user input:
   - Industry: B2B SaaS
   - Product: Project management
   - Audience: Startup founders, small teams
   - Platforms: LinkedIn (primary, explicitly stated)
   - Voice: Direct, practical, anti-corporate

**Expected output (config.json created):**
```json
{
  "brand": {
    "name": "[asks user or infers]",
    "industry": "B2B SaaS",
    "product": "Project management tool"
  },
  "audience": {
    "primary": "Startup founders and small team leads",
    "pain_points": ["project chaos", "tool overload", "shipping speed"],
    "platforms": ["linkedin"]
  },
  "voice": {
    "tone": "direct, practical",
    "avoid": ["corporate jargon", "buzzwords", "fluff"],
    "examples": []
  }
}
```

**Pass criteria:**
- [ ] Config file created without errors
- [ ] Agent asks clarifying questions only if genuinely ambiguous (not for everything)
- [ ] Voice section captures "anti-corporate" preference

## Step 2: Generate First Post

**User input:**
```
Write me a LinkedIn post about why most project management tools are overcomplicated.
```

**Expected agent behavior:**
1. Reads `social-context` config for voice/audience
2. Reads `social-copywriting/SKILL.md` + `references/hook-formulas.md`
3. Reads LinkedIn platform reference for formatting rules
4. Generates post with:
   - Strong hook in first 210 chars (before "see more" fold)
   - Personal/opinionated tone (not generic)
   - Line breaks every 1-2 sentences
   - 2-3 hashtags at end
   - Reply-driving CTA

**Example expected output:**
```
Most project management tools are built for project managers.

But most startups don't have project managers.

They have founders wearing 6 hats, trying to ship fast without drowning in Gantt charts and dependency maps nobody asked for.

Here's what I've learned building PM software for small teams:

The features people actually use? Tasks, deadlines, and "who's doing what."
That's it. Everything else is noise someone added to win an enterprise RFP.

We stripped our tool down to those 3 things. Usage went up 40%.

The best software doesn't do more. It does less, better.

What's the one feature you actually use in your PM tool? (Be honest — it's probably not the Gantt chart.)

#projectmanagement #startups #saas
```

**Pass criteria:**
- [ ] Hook lands before 210-char fold
- [ ] No AI-tell vocabulary (no "leverage", "delve", "game-changer")
- [ ] Tone matches: direct, practical, opinionated
- [ ] Includes specific details (not generic advice)
- [ ] CTA drives comments (question format)
- [ ] 2-3 hashtags at end, not scattered
- [ ] No link in main post body
- [ ] Total length: 500-2,000 chars

## Step 3: Review the Post

**User input:**
```
Review this post before I publish it.
```

**Expected agent behavior:**
1. Reads `content-review/SKILL.md`
2. Runs two-stage review:
   - Stage 1: Platform compliance (LinkedIn rules, length, formatting)
   - Stage 2: Quality + voice consistency
3. Returns actionable feedback

**Pass criteria:**
- [ ] Review catches any remaining AI tells
- [ ] Review checks hook strength
- [ ] Review validates CTA quality
- [ ] Review confirms platform-specific formatting
- [ ] Provides specific, actionable suggestions (not vague praise)
