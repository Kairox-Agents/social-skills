# SocialSkills — Comprehensive Design Document

**One-liner:** A full-stack agent skill pack for social media content creation, strategy, and growth — built on the AgentSkills spec, designed with real domain depth.

---

## 1. Executive Summary

### What We Found

The social media / content creation skill space is **crowded but shallow**. There are 10+ open source projects touching this domain, but every single one falls into predictable traps:

- **Marketing packs** (marketingskills, kostja94, alirezarezvani) treat social as one skill among 30+ marketing skills. It's an afterthought.
- **Full-stack agent apps** (langchain/social-media-agent, social-agents) are runtime applications, not portable skills. They require specific infra (LangGraph, Supabase, Arcade).
- **Design skills** (ckm-design, ckm-brand) handle visual production but zero strategy.
- **Agency agent collections** (msitarzewski/agency-agents) are persona definitions, not workflow skills with scripts and references.

### The Gap

Nobody has built a **social-media-native skill pack** that:
1. Treats social content as a first-class discipline (not a subset of "marketing")
2. Covers the full pipeline: strategy → ideation → creation → visuals → scheduling → analytics → iteration
3. Has platform-deep knowledge (not just "post to LinkedIn")
4. Includes scripts and templates that DO things
5. Uses progressive disclosure properly
6. Maintains state and memory across sessions

### Recommendation

**Build from scratch** using the AgentSkills spec. Borrow heavily from:
- **marketingskills** (Corey Haines): Foundation context pattern, skill cross-referencing, description trigger style
- **agency-agents** (msitarzewski): Deep persona/domain knowledge structure
- **gstack** (Garry Tan): Sprint-flow process model
- **langchain/social-media-agent**: Content repurposing pipeline concept, HITL review flow
- **ckm-design**: Visual production integration pattern

---

## 2. Standards & Ecosystem Map

### The Canonical Standard: AgentSkills

**Spec:** https://agentskills.io/specification  
**GitHub:** https://github.com/agentskills/agentskills  
**Maintained by:** Anthropic (open-sourced Dec 2025)  
**Adoption:** Claude Code, OpenAI Codex, Gemini CLI, Cursor, Windsurf, OpenClaw, Kilo Code, OpenCode, Augment, Antigravity (11+ tools)

**Key spec requirements:**
- Skill = directory containing `SKILL.md` with YAML frontmatter
- `name` field: lowercase, hyphens only, max 64 chars, must match directory name
- `description` field: max 1024 chars, should describe WHEN to activate
- Optional dirs: `scripts/`, `references/`, `assets/`
- Progressive disclosure: metadata (~100 tokens) → instructions (<5000 tokens) → resources (on-demand)
- `SKILL.md` should stay under 500 lines

**Frontmatter fields:**
```yaml
name: skill-name          # Required
description: "..."        # Required (trigger, not summary)
license: MIT              # Optional
compatibility: "..."      # Optional
metadata:                 # Optional
  author: org
  version: "1.0"
allowed-tools: "..."      # Optional (experimental)
```

### Installation Ecosystem

| Method | Tool |
|--------|------|
| `npx skills add` | vercel-labs/skills CLI |
| `npx skillkit install` | rohitg00/skillkit (multi-tool) |
| `/plugin marketplace` | Claude Code native |
| `git clone` + copy | Universal |
| `scripts/convert.sh` | alirezarezvani format converter (11 tools) |
| OpenClaw skill install | `openclaw skill install <url>` |

### Emerging Conventions (Not Formally Standardized)

- `.agents/skills/` as cross-tool skill directory (AgentSkills spec)
- `.claude/skills/` for Claude Code specifically
- `~/.openclaw/skills/` for OpenClaw global skills
- Product/project context files (`.agents/product-marketing-context.md`) as foundation context
- Skills reading each other by name reference (informal dependency)
- `config.json` within skill dirs for user configuration
- `data/` or `${CLAUDE_PLUGIN_DATA}` for persistent state

### Social Media Platform APIs & Limits

| Platform | API Status | Key Limits |
|----------|-----------|------------|
| X/Twitter | v2 API (paid tiers) | 280 chars, 4 images, 2:20 video |
| LinkedIn | Marketing API + basic | 3000 chars posts, 10 carousel slides |
| Instagram | Graph API (via Meta) | 2200 chars caption, 30 hashtags |
| TikTok | Content Posting API | 2200 chars, 60s-10min video |
| YouTube | Data API v3 | 100 chars title, 5000 chars desc |
| Threads | API (2024+) | 500 chars, 10 images |
| Facebook | Graph API | 63,206 chars, 10 images |
| Pinterest | API v5 | 500 char desc, 100 char title |
| Bluesky | AT Protocol (open) | 300 chars, 4 images |

---

## 3. Existing Projects — Detailed Breakdown

### 3.1 coreyhaines31/marketingskills

- **URL:** https://github.com/coreyhaines31/marketingskills
- **Stars:** High (most-referenced marketing skill pack)
- **What it is:** 33 markdown skills for Claude Code / AI agents
- **Architecture:** Foundation context (`product-marketing-context`) read by all skills. Skills cross-reference each other via "Related Skills" sections. Flat directory structure.
- **Core approach:** SaaS marketing toolkit — CRO, SEO, copywriting, growth
- **Social coverage:** ONE skill: `social-content` (~250 lines). Covers hooks, content pillars, repurposing, calendar structure, engagement strategy, analytics. Has `references/` dir with `platforms.md`, `post-templates.md`, `reverse-engineering.md`.
- **What it does well:**
  - Foundation context pattern is excellent
  - Description fields are proper triggers
  - Progressive disclosure via `references/` folder
  - Practical, not theoretical — real formulas and templates
  - Skill cross-referencing creates coherent system
- **What it does poorly:**
  - Social is 1 skill out of 33 — not deep enough
  - No platform-specific skills (LinkedIn ≠ TikTok)
  - No scripts that execute
  - No state/memory
  - No visual content pipeline
  - No thread-writing, carousel-design, or video-scripting specifics
- **Tech stack:** Pure markdown, no code
- **Activity:** Active, regularly updated

### 3.2 alirezarezvani/claude-skills

- **URL:** https://github.com/alirezarezvani/claude-skills
- **Stars:** 5,200+
- **What it is:** 205 skills across 9 domains, 268 Python tools
- **Architecture:** Skills + Agents (personas) + Commands. 7 marketing "pods": Content (8), SEO (5), CRO (6), Channels (6), Growth (4), Intelligence (4), Sales (2). Includes orchestration router.
- **Social coverage:** ~8 content skills, ~6 channel skills. Has `content-creator`, platform-specific skills for some channels.
- **What it does well:**
  - Massive scope with Python tooling
  - Multi-tool conversion (11 agents via scripts/convert.sh)
  - Persona system (Growth Marketer, Solo Founder, Startup CTO)
  - Orchestration patterns documented
  - Zero pip installs (stdlib-only Python)
- **What it does poorly:**
  - Quantity over quality — individual skills are shallow
  - Many skills feel AI-generated (generic frameworks, not battle-tested)
  - No gotchas sections
  - Social/content skills lack platform depth
  - Monolithic repo makes selective install awkward
- **Tech stack:** Markdown + Python (stdlib only)
- **Activity:** Active, last updated recently

### 3.3 kostja94/marketing-skills

- **URL:** https://github.com/kostja94/marketing-skills
- **Stars:** Growing
- **What it is:** 160+ marketing skills, heavily SEO-focused
- **Architecture:** Flat skill layout. `project-context.md` as foundation. Includes task tracker template. Skills have dependency maps.
- **Social coverage:** "Platforms" category: X, Reddit, LinkedIn, TikTok, YouTube, Medium, GitHub. Plus content category with copywriting, video, visual, translation.
- **What it does well:**
  - Largest single marketing skill collection
  - Good dependency visualization (ASCII flow diagrams)
  - Task tracker integration
  - References SkillsBench research (+16.2pp task success with curated skills)
  - "Skip intro" pattern for repeat tasks
- **What it does poorly:**
  - Overwhelmingly SEO-focused — social is bolted on
  - No scripts or automation
  - Skills feel template-generated
  - No state management
  - Platform skills are generic
- **Tech stack:** Pure markdown
- **Activity:** Active

### 3.4 zubair-trabzada/ai-marketing-claude

- **URL:** https://github.com/zubair-trabzada/ai-marketing-claude
- **Stars:** Moderate
- **What it is:** 15 marketing skills with parallel subagents, PDF report generation
- **Architecture:** Main orchestrator (`market/SKILL.md`) routes `/market` commands. 5 parallel subagents for audit. 14 sub-skills. Python scripts for analysis.
- **Social coverage:** `market-social` (30-day content calendar), `market-copy` (copywriting), `market-brand` (voice analysis).
- **What it does well:**
  - Parallel subagent execution model
  - Scoring system (6 dimensions, weighted)
  - Python scripts that DO things (page analysis, competitor scanning, calendar generation, PDF reports)
  - Slash-command interface (`/market audit <url>`)
  - Templates for emails, proposals, calendars
  - Agency use case (client proposals)
- **What it does poorly:**
  - Marketing audit focused, not content creation focused
  - Social calendar is generic (not platform-deep)
  - Requires `reportlab` pip install
  - No persistent state between sessions
  - Content quality is medium
- **Tech stack:** Markdown + Python (reportlab dependency)
- **Activity:** Recently created

### 3.5 langchain-ai/social-media-agent

- **URL:** https://github.com/langchain-ai/social-media-agent
- **Stars:** Significant (LangChain backed)
- **What it is:** Full agent application for sourcing, curating, scheduling social posts with HITL
- **Architecture:** LangGraph-based stateful agent. URL → content extraction → post generation → human review → scheduling. Supports Twitter + LinkedIn.
- **What it does well:**
  - True end-to-end pipeline (source → draft → review → publish)
  - Human-in-the-loop review flow
  - Cron-based content sourcing
  - Image selection and upload
  - Multi-source ingestion (URLs, GitHub, YouTube, Slack)
  - Post style customization
- **What it does poorly:**
  - NOT a portable skill pack — requires LangGraph, Supabase, Arcade, FireCrawl
  - Heavy infrastructure requirements
  - Only Twitter + LinkedIn
  - No content strategy or analytics layer
  - Overkill for "help me write a LinkedIn post"
- **Tech stack:** TypeScript, LangGraph, Supabase, Arcade
- **Activity:** Active (LangChain maintained)
- **Verdict:** Great execution model to borrow, wrong format for us

### 3.6 msitarzewski/agency-agents

- **URL:** https://github.com/msitarzewski/agency-agents
- **Stars:** 10,000+ (exploded March 2026)
- **What it is:** 61 AI agent persona definitions organized by department
- **Architecture:** Agent markdown files with identity, mission, workflows, deliverables, success metrics, communication style. Multi-tool install script.
- **Social coverage:** Content Marketing department includes social, copywriting, SEO, email agents. Paid Media department has PPC, creative, analytics.
- **What it does well:**
  - Deep persona definitions with personality
  - Deliverable-focused (real outputs, not frameworks)
  - Success metrics per agent
  - Multi-tool support (Cursor, Copilot, Aider, Windsurf)
  - Community-driven, fast-growing
- **What it does poorly:**
  - Personas, not skills — no scripts, references, or progressive disclosure
  - No cross-referencing or workflow chaining
  - No state or memory
  - No platform-specific depth
  - Format doesn't follow AgentSkills spec
- **Tech stack:** Pure markdown
- **Activity:** Very active (March 2026 explosion)

### 3.7 ckm-design (Installed)

- **What it is:** Comprehensive design skill covering brand, tokens, UI, logo, CIP, slides, banners, social photos, icons
- **Social coverage:** Banner design (22 styles, social/ads/web/print), social photos (HTML→screenshot, multi-platform), platform size references
- **What it does well:**
  - Actually generates visual content (not just describes it)
  - Platform-specific image sizes
  - Multiple visual styles
  - Script-driven workflow
- **What it does poorly:**
  - Zero content strategy or copywriting
  - Visual output only
  - No analytics, scheduling, or community management

### 3.8 Additional Projects Surveyed

| Project | Type | Notes |
|---------|------|-------|
| zxkane/social-agents | Claude SDK app | Platform slash commands for Twitter/Reddit/LinkedIn. Runtime app, not skills. |
| Klaudiusz321/social-media-agents | Multi-agent system | 4 specialized agents (Ad, Analytics, Content, Engagement). Chat interface. |
| harshmriduhash/Social-Media-AI-Agent | Instagram bot | Posting, liking, commenting automation. Not skill-based. |
| VoltAgent/awesome-agent-skills | Aggregator | 500+ skills catalog. Lists Typefully, Replicate, fal.ai skills relevant to content. |
| Typefully skills | Official | Social media scheduling/writing for Typefully platform. Narrow scope. |

---

## 4. Articles & Research

### Thariq Shihipar — "Lessons from Building Claude Code: How We Use Skills" (March 17, 2026)
- **Source:** https://x.com/trq212/status/2033949937936085378
- **Key takeaways for SocialSkills:**
  1. Description is a trigger — write "When the user wants to..." not "This skill does..."
  2. Gotchas section is highest-signal content — build from real failures
  3. Progressive disclosure — SKILL.md (~500 lines) → references/ → scripts/
  4. Don't state the obvious — focus on what pushes Claude OUT of defaults
  5. Skills can have memory — log files, JSON, SQLite for state
  6. Give scripts, not instructions to write scripts
  7. Config.json for first-use setup
  8. On-demand hooks for conditional behavior
  9. Measure skills with PreToolUse hooks

### Sprout Social — "2026 Social Media Content Strategy Report" (Jan 2026)
- **Source:** https://sproutsocial.com/insights/data/2026-social-media-content-strategy-report/
- 2,300 consumers + 1,200 marketers surveyed
- Key insight: Consumer expectations differ significantly by network
- Priority for social teams: content format optimization by platform

### SkillsBench Research (2025)
- **Source:** https://arxiv.org/abs/2602.12670
- Human-curated skills yield +16.2pp task success
- Vertical domains (marketing, SEO) benefit most from skills
- Validates our approach: domain depth > generic breadth

---

## 5. Pattern Analysis

### Proven Patterns (Battle-Tested)

| Pattern | Used By | Assessment |
|---------|---------|------------|
| Foundation context file | marketingskills, kostja94 | **Steal this.** Every social skill should read a shared context file first. |
| Description as trigger | marketingskills, AgentSkills spec | **Steal this.** "When the user wants to..." format. |
| Skill cross-referencing | marketingskills, alirezarezvani | **Steal this.** "Related Skills" section + inline references. |
| Progressive disclosure | AgentSkills spec, Thariq article | **Steal this.** 3-tier: metadata → SKILL.md → references/scripts. |
| Sprint flow model | gstack | **Adapt this.** Strategy → Create → Review → Ship → Analyze cycle. |
| Python scripts (stdlib-only) | alirezarezvani | **Steal this.** Zero-dependency scripts that actually execute. |
| Parallel subagents | ai-marketing-claude | **Consider this.** Good for audits and multi-platform generation. |
| Multi-tool install script | alirezarezvani, agency-agents | **Steal this.** Single `convert.sh` for 11+ agent tools. |
| Templates directory | ai-marketing-claude, kostja94 | **Steal this.** Pre-built content templates, calendar formats. |
| Persona + process | agency-agents | **Adapt this.** Domain expertise with personality, but in skill format not persona format. |

### Experimental Patterns

| Pattern | Used By | Assessment |
|---------|---------|------------|
| Slash-command interface | ai-marketing-claude | Nice UX but not portable across all agents |
| Scoring systems | ai-marketing-claude | Good for audits, overkill for content creation |
| On-demand hooks | Thariq article | Powerful but under-explored |
| HITL review flow | langchain/social-media-agent | Good concept, hard to implement as pure skill |

---

## 6. Gap Analysis — Feature Matrix

| Feature | marketing-skills (Corey) | claude-skills (Alireza) | marketing-skills (Kostja) | ai-marketing (Zubair) | agency-agents | langchain social | SocialSkills (ours) |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AgentSkills spec compliant | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Platform-specific content skills | ❌ | ❌ | Partial | ❌ | ❌ | Partial | ✅ |
| Thread writing skill | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Carousel/slide skill | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Video script skill | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Newsletter skill | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Content repurposing pipeline | Mentioned | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Hook/formula library | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Foundation context | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Cross-skill references | ✅ | ✅ | ✅ | ❌ | ❌ | N/A | ✅ |
| Executable scripts | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Persistent state/memory | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Visual content integration | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Community management | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Analytics/reporting | Mentioned | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| Crisis response playbook | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Platform algorithm deep-dives | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Gotchas/pitfalls sections | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Multi-tool support | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| Content calendar generation | Mentioned | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Audience growth tactics | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

**The whitespace:** No existing project combines platform-deep content creation skills + executable scripts + persistent state + visual integration + analytics feedback loop. That's SocialSkills.

---

## 7. Build vs Fork Recommendation

### Option A: Fork marketingskills (Corey Haines)
- **Pros:** Best foundation pattern, clean architecture, proven skill quality
- **Cons:** SaaS/CRO-focused DNA, would need to gut 30 skills and add 20+. His social-content skill is a starting point but not deep enough. Fork maintenance burden.
- **Verdict:** ❌ **Don't fork.** Borrow the patterns (foundation context, cross-referencing, trigger descriptions), build fresh.

### Option B: Fork alirezarezvani/claude-skills marketing pod
- **Pros:** Has Python tooling, multi-tool support, large community
- **Cons:** Quality is inconsistent, marketing skills are shallow, would need complete rewrite
- **Verdict:** ❌ **Don't fork.** Steal the multi-tool install script pattern, nothing else.

### Option C: Fork ai-marketing-claude (Zubair)
- **Pros:** Has scripts, subagent pattern, PDF reports
- **Cons:** Marketing audit focused, not content creation. Skills are thin.
- **Verdict:** ❌ **Don't fork.** Borrow subagent pattern for multi-platform generation.

### Option D: Build from scratch
- **Pros:** Clean architecture, social-native design, no legacy constraints, can embed all best patterns
- **Cons:** More initial work
- **Verdict:** ✅ **Build from scratch.** Borrow patterns aggressively, own the architecture.

### Specific Things to Borrow

| What | From Where | How |
|------|-----------|-----|
| Foundation context pattern | marketingskills | social-context skill reads user's brand/audience/platforms before any other skill runs |
| Trigger-style descriptions | marketingskills | "When the user wants to..." format for all description fields |
| Cross-referencing | marketingskills | "Related Skills" sections + inline "see [skill-name]" references |
| Hook formulas | marketingskills/social-content | Their hook library is good — expand it 3x |
| Content pillars framework | marketingskills/social-content | Adapt for social-native use |
| Multi-tool convert script | alirezarezvani | `scripts/convert.sh` pattern for 11+ tools |
| Python scripts (stdlib-only) | alirezarezvani | Zero-dependency scripts for calendar gen, content transformation |
| Subagent pattern | ai-marketing-claude | For multi-platform content generation from single input |
| Content repurposing pipeline | langchain/social-media-agent | Source → extract → adapt → schedule concept |
| Sprint flow process | gstack | Strategy → Create → Review → Ship → Analyze |
| Platform sizes + visual gen | ckm-design | Integration references for visual content |

---

## 8. Architecture

### Core Data Model

```
SocialSkills Pack
├── Foundation Layer
│   └── social-context (brand, audience, platforms, pillars, competitors)
│
├── Strategy Layer
│   ├── content-strategy (pillars, editorial direction)
│   ├── content-ideation (idea generation, trend research)
│   └── campaign-planning (multi-channel campaigns, launches)
│
├── Creation Layer
│   ├── social-copywriting (platform-adaptive copy)
│   ├── thread-writing (X, LinkedIn, Threads long-form)
│   ├── carousel-design (LinkedIn, Instagram slide content)
│   ├── video-scripting (Reels, TikTok, Shorts, YouTube)
│   ├── newsletter-writing (email newsletters, growth)
│   └── content-repurposing (long-form → multi-platform atomization)
│
├── Visual Layer
│   ├── social-visual-design (visual content, bridges to design tools)
│   └── thumbnail-design (YouTube, blog thumbnails)
│
├── Community Layer
│   ├── community-management (engagement, replies, DMs)
│   ├── ugc-strategy (user-generated content campaigns)
│   └── influencer-outreach (partnerships, collaborations)
│
├── Analytics Layer
│   ├── social-analytics (metrics, reporting, insights)
│   ├── content-audit (periodic review, what's working)
│   └── ab-testing-social (testing hypotheses)
│
├── Distribution Layer
│   ├── posting-strategy (timing, frequency, cross-posting)
│   └── content-calendar (planning, scheduling, batching)
│
└── Growth Layer
    ├── audience-growth (platform algorithms, tactics)
    ├── social-seo (search optimization for social)
    └── monetization (creator economy, revenue)
```

### Directory Structure

```
socialskills/
├── README.md                          # Overview, install, usage
├── LICENSE                            # MIT
├── plugin.json                        # Open Plugins manifest
├── scripts/
│   ├── install.sh                     # Universal installer
│   └── convert.sh                     # Multi-tool format converter
│
├── skills/
│   ├── social-context/                # Foundation — read by all other skills
│   │   ├── SKILL.md                   # Setup interview + context loading
│   │   ├── config.json                # User's brand/audience config (generated)
│   │   └── references/
│   │       ├── platform-specs.md      # Current platform specs & limits
│   │       ├── platform-algorithms.md # How each algorithm works (updated quarterly)
│   │       └── audience-personas.md   # Template for audience definition
│   │
│   ├── content-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── content-pillars.md     # Pillar framework + examples by niche
│   │       ├── editorial-calendar.md  # Planning frameworks
│   │       └── competitive-analysis.md
│   │
│   ├── content-ideation/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── ideation-frameworks.md # 15+ ideation methods
│   │   │   ├── trend-research.md      # How to find & ride trends
│   │   │   └── content-angles.md      # Reframing techniques
│   │   └── scripts/
│   │       └── idea-generator.py      # Generates ideas from pillars + trends
│   │
│   ├── social-copywriting/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── platform-voice.md      # How to write for EACH platform
│   │   │   ├── hook-formulas.md       # 50+ proven hook patterns
│   │   │   ├── cta-patterns.md        # Call-to-action library
│   │   │   ├── hashtag-strategy.md    # Platform-specific hashtag rules
│   │   │   ├── emoji-guide.md         # When/how to use emoji by platform
│   │   │   └── gotchas.md             # Common copywriting failures
│   │   └── scripts/
│   │       └── adapt-cross-platform.py # Transform one post → multiple platforms
│   │
│   ├── thread-writing/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── thread-structures.md   # Architecture patterns for threads
│   │       ├── thread-hooks.md        # Opening tweet/post formulas
│   │       ├── thread-transitions.md  # Between-tweet connectors
│   │       └── gotchas.md
│   │
│   ├── carousel-design/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── carousel-frameworks.md # Story arc, listicle, tutorial, etc.
│   │   │   ├── slide-patterns.md      # Visual layout patterns
│   │   │   └── gotchas.md
│   │   └── assets/
│   │       └── carousel-template.html # Base HTML template for generation
│   │
│   ├── video-scripting/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── short-form-scripts.md  # Reels/TikTok/Shorts (15s-90s)
│   │       ├── long-form-scripts.md   # YouTube (5-30min)
│   │       ├── hook-patterns.md       # First 3 seconds formulas
│   │       ├── b-roll-guides.md       # Visual storytelling cues
│   │       └── gotchas.md
│   │
│   ├── newsletter-writing/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── newsletter-formats.md  # Curated, essay, roundup, etc.
│   │       ├── subject-lines.md       # Formula library
│   │       ├── growth-tactics.md      # How to grow subscriber base
│   │       └── gotchas.md
│   │
│   ├── content-repurposing/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── repurposing-matrix.md  # Source format → output formats map
│   │   │   └── atomization-guide.md   # How to break down long-form
│   │   └── scripts/
│   │       └── atomize-content.py     # Breaks content into platform pieces
│   │
│   ├── social-visual-design/
│   │   ├── SKILL.md                   # Integrates with ckm-design if available
│   │   └── references/
│   │       ├── platform-sizes.md      # All image/video dimensions
│   │       ├── visual-trends.md       # Current design trends
│   │       ├── brand-consistency.md   # Visual brand guidelines
│   │       ├── color-psychology.md    # Colors and emotional response
│   │       └── gotchas.md
│   │
│   ├── thumbnail-design/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── thumbnail-patterns.md  # High-CTR thumbnail formulas
│   │       └── gotchas.md
│   │
│   ├── community-management/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── engagement-playbook.md # Daily engagement routines
│   │       ├── reply-frameworks.md    # How to respond to different comment types
│   │       ├── crisis-response.md     # When things go wrong
│   │       ├── dm-templates.md        # Outreach and response templates
│   │       └── gotchas.md
│   │
│   ├── ugc-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── ugc-campaigns.md       # Campaign types and execution
│   │       └── gotchas.md
│   │
│   ├── influencer-outreach/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── outreach-templates.md  # Cold outreach that works
│   │       ├── collaboration-types.md # Partnership models
│   │       └── gotchas.md
│   │
│   ├── social-analytics/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── metrics-glossary.md    # Every metric explained + benchmarks
│   │   │   ├── platform-analytics.md  # Platform-specific metrics
│   │   │   ├── reporting-templates.md # Weekly/monthly report formats
│   │   │   └── gotchas.md
│   │   └── scripts/
│   │       └── generate-report.py     # Generates formatted reports from data
│   │
│   ├── content-audit/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── audit-framework.md     # How to audit content performance
│   │       └── gotchas.md
│   │
│   ├── ab-testing-social/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── test-frameworks.md     # What to test and how
│   │       └── gotchas.md
│   │
│   ├── posting-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── optimal-timing.md      # Best posting times by platform
│   │       ├── frequency-guides.md    # How often per platform
│   │       ├── cross-posting-rules.md # What adapts vs what doesn't
│   │       └── gotchas.md
│   │
│   ├── content-calendar/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   └── calendar-frameworks.md
│   │   ├── scripts/
│   │   │   └── generate-calendar.py   # Creates formatted content calendar
│   │   └── assets/
│   │       └── calendar-template.md   # Template for content calendars
│   │
│   ├── audience-growth/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── growth-tactics.md      # Platform-specific growth plays
│   │       ├── algorithm-hacks.md     # What each algorithm rewards
│   │       └── gotchas.md
│   │
│   ├── social-seo/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── social-search.md       # TikTok search, LinkedIn SEO, etc.
│   │       └── gotchas.md
│   │
│   └── monetization/
│       ├── SKILL.md
│       └── references/
│           ├── revenue-models.md      # Sponsorships, products, services, etc.
│           ├── creator-economy.md     # Platform creator programs
│           └── gotchas.md
│
├── templates/
│   ├── social-context-template.md     # Template for foundation context
│   ├── content-calendar-template.md   # Weekly/monthly calendar
│   └── content-brief-template.md      # Brief for content pieces
│
└── data/                              # Persistent state (gitignored)
    ├── content-log.jsonl              # All content created
    ├── performance.jsonl              # Content performance tracking
    └── brand-context.json             # Cached brand context
```

### Skill Flow

```
                    ┌─────────────────┐
                    │  social-context  │ ← Foundation (read by ALL skills)
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────┐  ┌─────────────┐  ┌────────────┐
     │  content-   │  │  content-    │  │  campaign-  │
     │  strategy   │  │  ideation    │  │  planning   │
     └──────┬─────┘  └──────┬──────┘  └─────┬──────┘
            └───────────────┼────────────────┘
                            ▼
              ┌─────── CREATE ───────┐
              │                      │
     ┌────────┴──────┐      ┌───────┴────────┐
     │  Text Content  │      │ Visual Content  │
     ├───────────────┤      ├────────────────┤
     │ copywriting    │      │ visual-design   │
     │ thread-writing │      │ thumbnail       │
     │ carousel-design│      │ carousel-design │
     │ video-scripting│      └───────┬────────┘
     │ newsletter     │              │
     └───────┬───────┘              │
             │                       │
             ▼                       ▼
     ┌───────────────┐     ┌────────────────┐
     │  content-      │     │  posting-       │
     │  repurposing   │────▶│  strategy       │
     └───────────────┘     └───────┬────────┘
                                    │
                           ┌───────┴────────┐
                           │  content-       │
                           │  calendar       │
                           └───────┬────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
           ┌──────────────┐ ┌────────────┐ ┌──────────────┐
           │  community-   │ │  social-    │ │  audience-    │
           │  management   │ │  analytics  │ │  growth       │
           └──────────────┘ └──────┬─────┘ └──────────────┘
                                    │
                           ┌───────┴────────┐
                           │  content-       │
                           │  audit          │──▶ Back to Strategy
                           └────────────────┘
```

### Key Abstractions

1. **Social Context** — Persistent config that all skills read. Contains brand voice, audience, active platforms, content pillars, goals. Created via interview on first use.

2. **Content Piece** — Any unit of social content. Has: platform, format, copy, visual requirements, hashtags, CTA, scheduling notes. Skills output these.

3. **Content Log** — Append-only JSONL tracking everything created. Enables "what have I posted about?" queries and prevents repetition.

4. **Platform Adapter** — Reference files that encode platform-specific rules. Each platform gets its own reference doc with specs, algorithm notes, gotchas.

5. **Repurposing Matrix** — Maps source format → target formats with transformation rules. E.g., Blog → Thread (extract key insights), Blog → Carousel (5-slide story arc), Blog → Reel script (30s hook + value + CTA).

---

## 9. v1 Scope (MVP)

### v1 Skills (Build First)

| # | Skill | Rationale |
|---|-------|-----------|
| 1 | social-context | Foundation — everything depends on this |
| 2 | social-copywriting | Most common use case |
| 3 | thread-writing | High demand, well-defined format |
| 4 | content-ideation | Upstream of all creation |
| 5 | content-repurposing | Highest leverage — one input, many outputs |
| 6 | content-calendar | Planning tool, generates tangible output |
| 7 | posting-strategy | When/how to publish |

### v1 Non-Goals

- Video scripting (v2)
- Community management (v2)
- Analytics/reporting (v2)
- Monetization (v2)
- Multi-tool convert script (v2 — start with AgentSkills spec only)
- Visual content generation (v2 — soft-reference ckm-design)

### v1 Success Criteria

1. User can install and generate a LinkedIn post, X thread, and Instagram carousel from a single topic in under 5 minutes
2. Foundation context interview takes <2 minutes and produces useful config
3. Content repurposing turns a blog post URL into 5+ platform-specific posts
4. Skills cross-reference each other coherently
5. Every skill has a Gotchas section with ≥5 real platform-specific pitfalls
6. Scripts execute without any pip/npm installs (stdlib only)
7. Content log persists across sessions

### v2 Roadmap

- Wave 2: carousel-design, video-scripting, newsletter-writing, content-strategy, campaign-planning
- Wave 3: social-analytics, content-audit, community-management, social-visual-design
- Wave 4: audience-growth, social-seo, monetization, ugc-strategy, influencer-outreach, ab-testing-social, thumbnail-design
- Multi-tool support via convert.sh
- Plugin marketplace listing
- Automated platform spec updates (quarterly refresh script)

---

## 10. Open Questions

1. **Naming**: `socialskills` as the pack name works. Should individual skills use a prefix? (`ss-copywriting` vs just `social-copywriting`)? Spec says name must match directory name, so prefixing adds clutter but aids discoverability.

2. **Platform priority**: v1 should cover X/Twitter + LinkedIn + Instagram. Add TikTok, YouTube, Threads, Bluesky in v2?

3. **ckm-design integration**: Should `social-visual-design` hard-depend on ckm-design? Or soft-reference it ("if ckm-design is available, use it; otherwise, provide text descriptions of visual requirements")?

4. **Target user**: The architecture supports solo creators → small teams. Should v1 optimize for solo creators and add team features (approval workflows, brand compliance) in v2?

5. **Distribution**: GitHub repo + ClaHub listing? Plugin marketplace? Both?

6. **License**: MIT seems right for maximum adoption. Confirm?

7. **Content log format**: JSONL is simple and append-friendly. But should it be structured more formally? Schema:
```json
{
  "id": "uuid",
  "created": "ISO-8601",
  "platform": "linkedin",
  "format": "post",
  "topic": "...",
  "pillar": "educational",
  "content": "...",
  "hashtags": [],
  "performance": null
}
```

8. **Gotchas sourcing**: The gotchas sections are the highest-value content. Should we start with a "known gotchas" research sprint before writing skills? Or accumulate them iteratively?

9. **How opinionated?** Should skills be prescriptive ("always use exactly 3-5 hashtags on LinkedIn") or flexible ("consider hashtag usage based on your audience data")? Thariq says don't over-constrain, but marketers want playbooks.

10. **Update cadence**: Platform algorithms change quarterly. How do we handle this? Quarterly update branches? A `references/changelog.md` per platform?

---

*Research completed March 19, 2026. Sources cited inline throughout.*
