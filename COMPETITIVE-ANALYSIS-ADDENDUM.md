# Competitive Analysis Addendum — New References

*Added March 19, 2026*

---

## 1. obra/superpowers — The Gold Standard for Process Skill Packs

**URL:** https://github.com/obra/superpowers  
**By:** Jesse Vincent (Prime Radiant)  
**Stars:** Very high, official Claude plugin marketplace listing  
**License:** MIT

### What It Is

A complete software development workflow for coding agents, built as composable skills. Not a collection of tips — a **mandatory process pipeline** where each skill triggers automatically and chains into the next.

### Architecture (This Is What We Should Steal)

```
brainstorming → writing-plans → subagent-driven-development → code-review → finishing
     ↓               ↓                    ↓                        ↓            ↓
  Spec doc    Implementation plan    Fresh subagent/task       2-stage review   Merge/PR
```

**Key design patterns:**

1. **Hard gates.** Skills have `<HARD-GATE>` blocks that prevent skipping steps. Brainstorming won't let you write code until the spec is approved. We need this — "Don't generate social content until foundation context is configured."

2. **Mandatory checklists.** Each skill has a numbered checklist that MUST be completed in order. Steps are marked with `- [ ]` syntax. Agent tracks completion.

3. **Subagent delegation.** Each task gets a fresh subagent with precisely crafted context (never session history). Two-stage review: spec compliance first, then quality. This is how we should do multi-platform content generation — dispatch a subagent per platform with platform-specific context.

4. **Model selection guidance.** "Use the least powerful model that can handle each role." Mechanical tasks → cheap model. Creative tasks → capable model. We should do this for content generation vs. analytics.

5. **Prompt templates as files.** `implementer-prompt.md`, `spec-reviewer-prompt.md`, `code-quality-reviewer-prompt.md` — separate files for each subagent dispatch. Not inline instructions.

6. **Process flow diagrams.** Graphviz `dot` syntax for showing decision trees and workflows. Clean, readable, version-controllable.

7. **Anti-pattern sections.** "This is too simple to need a design" is called out as an anti-pattern with explanation. Every project goes through the process. We need this for content: "This post is too simple to need platform adaptation" — no it isn't.

8. **Incremental validation.** Present design in sections, get approval after each section. For us: show content strategy in chunks, validate each content pillar before proceeding.

### What Makes It Excellent

- Skills are **mandatory workflows, not suggestions.** The agent checks for relevant skills before any task.
- Skills **chain automatically.** Brainstorming invokes writing-plans. Writing-plans invokes subagent-driven-development. No manual routing needed.
- **Two-stage review** ensures both correctness (does it match the spec?) and quality (is it well-crafted?). For social content: platform compliance review + taste/quality review.
- **YAGNI/DRY/TDD principles** are the foundation. We need equivalent principles for content: "One idea per post" / "Never repeat the same hook twice" / "Test with Trial Reels before publishing to main grid."

### What We Should Borrow (Specific)

| Pattern | From Superpowers | Our Adaptation |
|---------|-----------------|----------------|
| Hard gate before implementation | `<HARD-GATE>` in brainstorming | `<HARD-GATE>` in social-copywriting: "Do NOT generate content until social-context config exists and is loaded" |
| Mandatory checklist per skill | Numbered steps with `- [ ]` | Every creation skill has a checklist: audience → platform → format → hook → body → CTA → review |
| Subagent per task | Fresh subagent dispatched per implementation task | Fresh subagent dispatched per platform adaptation (one subagent per platform version) |
| Two-stage review | Spec compliance → code quality | Platform compliance → taste/quality review |
| Prompt templates as files | `implementer-prompt.md` | `platform-adapter-prompt.md`, `content-reviewer-prompt.md`, `taste-checker-prompt.md` |
| Process flow diagrams | Graphviz dot syntax | Same — visual workflow documentation |
| Anti-pattern sections | "Too simple to need a design" | "Too simple to need platform adaptation" |
| Model selection guidance | Cheap for mechanical, capable for creative | Cheap for formatting/specs, capable for creative writing |
| Plan → execute separation | Design doc is separate from implementation | Content brief is separate from content creation |

---

## 2. track-forge/openclaw-skill-social-ops — The Social Ops Pioneer

**URL:** https://github.com/track-forge/openclaw-skill-social-ops  
**By:** Track Forge  
**License:** Apache 2.0

### What It Is

A role-based social media operations framework for OpenClaw agents. 6 specialized roles (Scout, Researcher, Content Specialist, Responder, Poster, Analyst) with bounded authority and handoff protocols.

### Architecture

```
Scout → Responder (reply-worthy threads → responses)
Scout → Content Specialist (opportunities → lane strategy)
Researcher → Guidance for Content Specialist
Content Specialist → Writer → Poster
Poster → Done logs
Analyst → Strategy adjustments
```

### Honest Assessment (Philip said "proceed skeptically")

**What's genuinely good:**

1. **Role separation with bounded authority.** Scout detects but never acts. Content Specialist strategizes but never posts. Poster publishes but never ideates. This prevents the common failure mode of an AI agent doing everything at once poorly.

2. **Role I/O map.** `ROLE-IO-MAP.md` documents what each role reads and writes. Clean data contracts between roles.

3. **Cron-driven execution.** Each role runs on a schedule via OpenClaw crons. Scout runs frequently, Analyst runs weekly. This is a real operational model.

4. **Lane-based content strategy.** Content organized into "lanes" (content pillars) with cadence targets, format types, and status tracking.

5. **State management.** Logs per role, per day. Content pipeline state tracked in filesystem.

6. **Environment variable configuration.** `SOCIAL_OPS_DATA_DIR` for portable state location.

**What's weak/concerning:**

1. **Platform-agnostic to a fault.** Built for "Moltbook" (a niche platform). Claims adaptability to Twitter/Reddit/Discord but has ZERO platform-specific knowledge. No algorithm insights, no character limits, no gotchas. This is a framework without content.

2. **No actual domain expertise.** The roles are well-structured but contain no social media knowledge. The Scout knows HOW to scout but not WHAT to look for on Twitter vs Reddit. The Content Specialist manages lanes but has no understanding of what makes good LinkedIn content vs TikTok content.

3. **Agent-as-influencer focused.** Designed for an AI agent building its own social presence, not a human creator using an AI assistant. Different use case than ours.

4. **Cadence over quality.** "~14 posts per week" as a target without any discussion of quality, platform fit, or audience fatigue.

5. **No taste layer.** No anti-patterns, no "what not to do," no cringe detection. Just process.

6. **No scripts.** Pure markdown. No Python, no automation beyond the cron scheduling.

7. **Very early stage.** Clear rough edges, some references to "Moltbook-specific" features that don't translate.

### What We Should Borrow

| Pattern | Assessment |
|---------|------------|
| Role separation (Scout, Researcher, Content Specialist, Responder, Poster, Analyst) | **Good concept, needs our domain expertise injected.** These map roughly to our skills: content-ideation (Scout), content-strategy (Content Specialist), social-copywriting (Writer), community-management (Responder), social-analytics (Analyst). |
| Role I/O map | **Steal this.** Document what each skill reads and writes. Clean data contracts. |
| Cron-driven execution | **Good for OpenClaw users.** Include cron setup instructions in our skills. |
| Lane-based content pillars | **Already in our design.** Content pillars as a concept is standard; their file-based tracking is clean. |
| Bounded authority | **Steal this principle.** Each skill states what it does AND what it explicitly does NOT do. |
| Daily log format | **Adapt.** Our content log is JSONL (structured) not markdown (readable). Consider both. |

---

## 3. rohunvora/x-research-skill — The Research Tool

**URL:** https://github.com/rohunvora/x-research-skill  
**By:** Rohun Vora  
**License:** MIT

### What It Is

A CLI tool wrapping the X API for search, profile monitoring, and research. Designed for Claude Code and OpenClaw.

### Architecture

TypeScript (Bun) CLI with: search, profile lookup, thread following, watchlist monitoring, file-based caching, cost tracking.

### Honest Assessment

**What's genuinely good:**

1. **Cost transparency.** Every search shows what it cost. Quick mode exists to minimize API spending. This is excellent UX for a paid API wrapper.

2. **File-based caching.** 15-min default TTL, 1-hour in quick mode. Prevents repeat API charges. Simple and effective.

3. **Watchlist feature.** Track specific accounts over time. Good for competitive monitoring.

4. **Cost breakdown in README.** Per-operation cost table. Users know exactly what they're paying.

5. **Quick mode.** `--quick` forces single page, extends cache, adds noise filters. Designed for pulse checks, not deep research.

6. **Well-documented CLI.** Clear flags, examples, expected output.

**What's weak:**

1. **Twitter/X only.** No other platform support.

2. **Read-only.** Can't post, reply, or engage. Research only.

3. **Requires X API Bearer Token + Bun runtime.** Not zero-dependency.

4. **Only recent search (7 days).** Full-archive coming but not implemented.

5. **No analysis.** Fetches data but doesn't analyze patterns, voice, or strategy. That's on the agent to do.

### Relevance to SocialSkills

This is a **complementary tool**, not a competitor. It solves a specific problem (fetching X data for research) that our account-analysis feature needs.

**Integration options:**
- Reference as an optional dependency for our `account-analysis` skill
- Our `fetch_posts.py` could use the same caching pattern
- Watchlist concept maps to our competitor monitoring feature

---

## Updated Architecture Implications

### The Superpowers Process Model for Social Content

Adapting superpowers' process to our domain:

```
┌──────────────────────────────────────────────────────────────┐
│                    CONTENT CREATION PROCESS                    │
│                                                                │
│  ① STRATEGY (brainstorming equivalent)                        │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ social-context [HARD GATE: must exist before anything]  │  │
│  │ content-strategy [define pillars, audience, goals]      │  │
│  │ content-ideation [generate ideas from pillars + trends] │  │
│  └────────────────────────┬────────────────────────────────┘  │
│                           ▼                                    │
│  ② PLANNING (writing-plans equivalent)                        │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ content-calendar [plan what, when, where]               │  │
│  │ posting-strategy [timing, frequency, cross-posting]     │  │
│  │ content-brief [per-piece spec: audience, platform,      │  │
│  │                 format, key message, hook direction]     │  │
│  └────────────────────────┬────────────────────────────────┘  │
│                           ▼                                    │
│  ③ CREATION (subagent-driven-development equivalent)          │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ social-copywriting [generate platform-native content]   │  │
│  │   └→ Dispatch per-platform subagent with:               │  │
│  │       • Platform reference file                         │  │
│  │       • Brand voice from social-context                 │  │
│  │       • Content brief                                   │  │
│  │       • Anti-patterns list                              │  │
│  │ thread-writing [threads/long-form]                      │  │
│  │ carousel-design [slide content]                         │  │
│  │ video-scripting [short + long form scripts]             │  │
│  │ newsletter-writing [email content]                      │  │
│  │ content-repurposing [long-form → multi-platform]        │  │
│  │   └→ Dispatch atomization subagent:                     │  │
│  │       • Source content                                  │  │
│  │       • Repurposing matrix                              │  │
│  │       • Per-platform specs                              │  │
│  └────────────────────────┬────────────────────────────────┘  │
│                           ▼                                    │
│  ④ REVIEW (code-review equivalent)                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Stage 1: Platform compliance review                     │  │
│  │   • Character limits respected?                         │  │
│  │   • Hashtag count within platform rules?                │  │
│  │   • Format matches platform norms?                      │  │
│  │   • CTA is platform-appropriate?                        │  │
│  │                                                         │  │
│  │ Stage 2: Taste/quality review                           │  │
│  │   • Does it pass the cringe detector?                   │  │
│  │   • Would a real human post this?                       │  │
│  │   • Is the hook genuinely compelling?                   │  │
│  │   • Does it match brand voice?                          │  │
│  │   • Is it specific enough (no generic advice)?          │  │
│  │   • Does it avoid known anti-patterns?                  │  │
│  └────────────────────────┬────────────────────────────────┘  │
│                           ▼                                    │
│  ⑤ DISTRIBUTION (finishing-branch equivalent)                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Log to content-log.jsonl                                │  │
│  │ Schedule or publish                                     │  │
│  │ Update content calendar                                 │  │
│  └────────────────────────┬────────────────────────────────┘  │
│                           ▼                                    │
│  ⑥ ANALYSIS (feedback loop)                                   │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ social-analytics [measure performance]                  │  │
│  │ content-audit [what worked, what didn't]                │  │
│  │ → Feeds back into content-strategy and content-ideation │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### New Design Elements (Borrowed from Superpowers)

1. **Hard gates in every creation skill:**
```markdown
<HARD-GATE>
Do NOT generate content until:
1. social-context config.json exists and has been loaded
2. Platform reference for the target platform has been read
3. Content brief or topic has been defined
This applies to EVERY content request regardless of perceived simplicity.
</HARD-GATE>
```

2. **Anti-pattern sections in every skill** (like superpowers' "This is too simple to need a design"):
```markdown
## Anti-Pattern: "It's Just a Quick Post"
Every post goes through platform adaptation. A LinkedIn post copied to Twitter will fail.
A tweet expanded to LinkedIn will feel shallow. Even "simple" posts need platform-native treatment.
```

3. **Prompt template files for subagent dispatch:**
```
skills/social-copywriting/
├── SKILL.md
├── prompts/
│   ├── platform-adapter-prompt.md    # Subagent: adapt content to specific platform
│   ├── content-reviewer-prompt.md    # Subagent: platform compliance check
│   └── taste-checker-prompt.md       # Subagent: quality/cringe check
└── references/
    └── ...
```

4. **Bounded authority declarations** (from social-ops):
```markdown
## This Skill Does NOT:
- Generate visual content (use social-visual-design)
- Schedule or publish posts (use posting-strategy)
- Analyze performance (use social-analytics)
- Create content calendars (use content-calendar)
```

5. **Role I/O map** (from social-ops, adapted):
```
SKILL-IO-MAP.md
social-context      READS: user interview  WRITES: config.json, brand-context.json
content-ideation    READS: config.json, trend data  WRITES: ideas backlog
social-copywriting  READS: config.json, content brief, platform reference  WRITES: content pieces to content-log.jsonl
content-repurposing READS: source content, repurposing matrix  WRITES: multiple content pieces to content-log.jsonl
social-analytics    READS: content-log.jsonl, performance data  WRITES: analytics reports, strategy recommendations
```

---

## Revised v1 Skill List (Post-Superpowers Influence)

Adding **review and process skills** that superpowers makes clear are essential:

| # | Skill | Type |
|---|-------|------|
| 1 | social-context | Foundation (HARD GATE) |
| 2 | social-copywriting | Creation + per-platform subagent dispatch |
| 3 | thread-writing | Creation (long-form) |
| 4 | content-ideation | Strategy |
| 5 | content-repurposing | Creation (highest leverage) |
| 6 | content-calendar | Planning |
| 7 | posting-strategy | Distribution |
| 8 | **content-review** *(NEW)* | Quality gate — two-stage review (platform compliance + taste) |
| 9 | **account-analysis** *(NEW, was v2)* | Research — analyze accounts, generate voice DNA |

Content-review is the superpowers-inspired addition. It's the quality gate that prevents AI slop from getting published.

---

## Summary: What Changed

The three new references shift our design in important ways:

1. **Superpowers gives us the PROCESS model.** Our skills weren't just missing content — they were missing mandatory gates, checklists, subagent dispatch patterns, and review loops. Now every creation skill will have hard gates, anti-patterns, and two-stage review.

2. **Social-ops gives us ROLE BOUNDARIES.** Each skill now explicitly declares what it does AND does not do. Plus role I/O map and cron-driven execution patterns.

3. **x-research-skill gives us the DATA LAYER pattern.** Cost-transparent API access, caching, watchlist monitoring. Our account-analysis skill should follow this exact pattern.

4. **The biggest gap we now fill that NO existing project does:** Platform-deep domain knowledge (our 2,328-line platform reference files) + superpowers-quality process design + social-ops role separation. That's the combination nobody has.
