# SocialSkills — Landscape Research & Architecture Plan

## Phase 1: Landscape Mapping

### What Exists Today

**Existing skill packs that touch social/content:**

1. **coreyhaines31/marketingskills** (33 skills) — The most relevant competitor. SaaS-focused marketing: SEO, CRO, copywriting, paid ads, email sequences, social content. Good architecture (product-marketing-context as foundation, skills cross-reference each other). BUT: social is just ONE skill (`social-content`), content creation is thin, no visual/design pipeline, no scheduling/analytics, no community management. Very CRO-heavy.

2. **alirezarezvani/claude-skills** (205 skills, 43 marketing) — Quantity over depth. 7 marketing "pods": Content (8), SEO (5), CRO (6), Channels (6), Growth (4), Intelligence (4), Sales (2). Has a `content-creator` skill. Includes Python scripts. But individual skills are surface-level — framework descriptions, not domain-deep.

3. **mcpmarket.com social-media-content-strategist** — Single skill, basic platform templates.

4. **ckm-design (already installed)** — Has social photo generation (HTML→screenshot), banner design (22 styles), platform size references. Solid visual production but NO content strategy, copywriting, scheduling, analytics, or community management.

5. **ckm-brand (already installed)** — Brand voice, guidelines, consistency. Good foundation layer but doesn't extend into social execution.

6. **phuryn/pm-skills** — PM-focused but excellent structural model: skills → commands → plugins architecture. Skills cross-reference each other. Commands chain skills. Great progressive disclosure.

7. **garrytan/gstack** — Engineering-focused but the *process* model is brilliant: Think → Plan → Build → Review → Test → Ship → Reflect. Each skill feeds the next. This "sprint" pattern is exactly what social/content needs.

### The Gap

Nobody has built the **full-stack social media & content creation skill pack**. What exists is either:
- Marketing-centric (conversion/SEO focus, social as afterthought)
- Visual-only (design/banner tools without strategy)
- Surface-level (framework lists without real domain knowledge)
- Single-purpose (one skill doing one thing)

**What's missing from ALL of them:**

| Gap | Details |
|-----|---------|
| Platform-deep knowledge | Character limits, algorithm nuances, format specs, posting cadences — the stuff that changes quarterly |
| Content pipeline | Ideation → research → draft → edit → visual → schedule → publish → analyze — as a connected flow |
| Voice/tone adaptation | Same message, 5 platforms, 5 different versions — with platform-native feel |
| Community management | Reply frameworks, crisis playbooks, engagement protocols |
| Analytics interpretation | Not just "track metrics" but "here's what these numbers mean and what to do about them" |
| Content repurposing | Long-form → social atomization (blog → thread → carousel → reels script → newsletter) |
| Visual + copy integration | Most skills are text OR visuals, never both working together |
| Gotchas/pitfalls | Real platform-specific failure modes, algorithm traps, common mistakes |

### Standards & Specs

- **AgentSkills spec** (agentskills.io) — The emerging open standard. SKILL.md + frontmatter + folder structure. Supported by Claude Code, Codex, Gemini CLI, Cursor, and others.
- **Open Plugins** (open-plugins.com) — Plugin marketplace manifest standard (plugin.json).
- **Claude Code Plugin Marketplace** — Built-in discovery/install system.
- No social-media-specific agent standard exists. We define it.

### Key Design Principles (from Thariq's article + our research)

1. **Don't state the obvious** — Focus on what pushes agents OUT of default patterns
2. **Gotchas section** — Highest-signal content; accumulate from real failures
3. **Filesystem as context engineering** — Skills are folders, not just markdown
4. **Don't over-constrain** — Info + flexibility, not rigid scripts
5. **Description is a trigger, not a summary** — WHEN to activate, not what it does
6. **Skills can have memory** — Log files, JSON, SQLite for state
7. **Scripts > instructions to write scripts** — Helper libraries over telling agent to build from scratch
8. **Progressive disclosure** — Metadata → SKILL.md → references → scripts (3-level loading)
9. **Process, not collection** — Skills should flow like a sprint (gstack pattern)

---

## Phase 2: Architecture Design

### SocialSkills Pack Structure

```
socialskills/
├── README.md
├── plugin.json                    # Open Plugins manifest
├── .plugin/plugin.json            # Claude Code marketplace manifest
│
├── foundation/                    # Always-loaded context layer
│   └── social-context/
│       ├── SKILL.md               # Brand voice + audience + platforms config
│       ├── config.json            # User's brand/platform settings (generated on first use)
│       └── references/
│           └── platform-specs.md  # Current specs (char limits, image sizes, algorithm notes)
│
├── strategy/                      # Planning & ideation
│   ├── content-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── content-pillars.md
│   │       ├── editorial-calendar.md
│   │       └── audience-research.md
│   ├── content-ideation/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── ideation-frameworks.md
│   │       └── trend-research.md
│   └── campaign-planning/
│       ├── SKILL.md
│       └── references/
│           ├── campaign-types.md
│           └── launch-playbooks.md
│
├── creation/                      # Content production
│   ├── social-copywriting/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── platform-voice.md       # How to write for each platform
│   │   │   ├── hook-formulas.md        # Proven opening patterns
│   │   │   ├── cta-patterns.md         # Call-to-action frameworks
│   │   │   ├── hashtag-strategy.md
│   │   │   └── gotchas.md              # Common copywriting failures
│   │   └── scripts/
│   │       └── adapt-cross-platform.py # Transform content across platforms
│   ├── thread-writing/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── thread-structures.md    # X/Twitter, LinkedIn, Threads patterns
│   │       └── thread-hooks.md
│   ├── carousel-design/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── carousel-frameworks.md
│   │       └── slide-patterns.md
│   ├── video-scripting/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── short-form-scripts.md   # Reels, TikTok, Shorts
│   │       ├── long-form-scripts.md    # YouTube
│   │       └── hook-patterns.md
│   ├── newsletter-writing/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── newsletter-formats.md
│   │       ├── subject-lines.md
│   │       └── growth-tactics.md
│   └── content-repurposing/
│       ├── SKILL.md                    # Long-form → atomized social content
│       ├── references/
│       │   └── repurposing-matrix.md   # What formats work from what sources
│       └── scripts/
│           └── atomize-content.py      # Split long-form into platform pieces
│
├── visual/                        # Visual content production
│   ├── social-visual-design/
│   │   ├── SKILL.md               # Bridges to ckm-design for visual execution
│   │   └── references/
│   │       ├── platform-sizes.md
│   │       ├── visual-trends.md
│   │       └── brand-consistency.md
│   └── thumbnail-design/
│       ├── SKILL.md
│       └── references/
│           └── thumbnail-patterns.md
│
├── community/                     # Engagement & community management
│   ├── community-management/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── engagement-playbook.md
│   │       ├── reply-frameworks.md
│   │       ├── crisis-response.md
│   │       └── dm-templates.md
│   ├── ugc-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── ugc-campaigns.md
│   └── influencer-outreach/
│       ├── SKILL.md
│       └── references/
│           ├── outreach-templates.md
│           └── collaboration-types.md
│
├── analytics/                     # Measurement & optimization
│   ├── social-analytics/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── metrics-glossary.md     # What each metric means + benchmarks
│   │   │   ├── platform-analytics.md   # Platform-specific metrics
│   │   │   └── reporting-templates.md
│   │   └── scripts/
│   │       └── generate-report.py
│   ├── content-audit/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── audit-framework.md
│   └── ab-testing-social/
│       ├── SKILL.md
│       └── references/
│           └── test-frameworks.md
│
├── distribution/                  # Publishing & scheduling
│   ├── posting-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── optimal-timing.md
│   │       ├── frequency-guides.md
│   │       └── cross-posting-rules.md
│   └── content-calendar/
│       ├── SKILL.md
│       └── scripts/
│           └── generate-calendar.py
│
├── growth/                        # Growth & monetization
│   ├── audience-growth/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── growth-tactics.md
│   │       └── platform-algorithms.md
│   ├── social-seo/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── social-search-optimization.md
│   └── monetization/
│       ├── SKILL.md
│       └── references/
│           ├── revenue-models.md
│           └── creator-economy.md
│
└── data/                          # Persistent state (outside skill dirs)
    ├── content-log.jsonl          # History of content created
    ├── performance-data.jsonl     # Content performance tracking
    └── brand-context.json         # User's brand/audience config
```

### Skill Flow (The Content Sprint)

Inspired by gstack's sprint model:

```
Strategy → Ideate → Create → Design → Review → Schedule → Publish → Analyze → Iterate
    │          │        │        │         │         │          │         │          │
    ▼          ▼        ▼        ▼         ▼         ▼          ▼         ▼          ▼
 content   content  social    social    copy      posting    content   social    content
 strategy  ideation copywrite visual    edit      strategy   calendar analytics  audit
                    /thread   design
                    /carousel
                    /video
                    /newsletter
```

### Foundation Layer: social-context

Every skill reads `social-context` first (like marketingskills' product-marketing-context). Contains:
- Brand voice & tone guidelines
- Target audience personas
- Active platforms & goals per platform
- Content pillars
- Competitor profiles
- Key metrics & KPIs

First-time use: agent interviews user to build config.json.

### Plugin Organization (for marketplace)

```
Plugin Name                  | Skills Included
-----------------------------|------------------------------------------
socialskills-foundation      | social-context
socialskills-strategy        | content-strategy, content-ideation, campaign-planning
socialskills-creation        | social-copywriting, thread-writing, carousel-design,
                             | video-scripting, newsletter-writing, content-repurposing
socialskills-visual          | social-visual-design, thumbnail-design
socialskills-community       | community-management, ugc-strategy, influencer-outreach
socialskills-analytics       | social-analytics, content-audit, ab-testing-social
socialskills-distribution    | posting-strategy, content-calendar
socialskills-growth          | audience-growth, social-seo, monetization
```

### Differentiation: What Makes This Not Garbage

1. **Platform-deep, not platform-generic** — Separate reference files per platform with REAL nuances (LinkedIn's algorithm favors dwell time, X rewards early engagement velocity, Instagram Reels discovery mechanics, TikTok's FYP signals)

2. **Gotchas-first design** — Every skill starts with "what goes wrong" because that's the highest-signal content. E.g.: "Don't use hashtags in LinkedIn article posts — they hurt reach. But DO use them in regular posts (3-5 max)."

3. **Connected flow** — Skills reference each other. Content-ideation knows about content-strategy pillars. Social-copywriting reads brand voice from social-context. Analytics feeds back into strategy.

4. **Scripts that DO things** — Not "here's how to analyze" but actual Python that generates reports, transforms content cross-platform, creates editorial calendars.

5. **Memory & state** — Content log tracks what's been created. Performance data enables "what's working?" analysis. Brand context persists across sessions.

6. **Bridges to visual tools** — social-visual-design skill knows about ckm-design and delegates to it. Copy + visual in one flow.

7. **Real frameworks, not Wikipedia summaries** — Hook formulas that actually work, thread structures proven by top creators, carousel patterns that drive saves.

---

## Phase 3: Priority & Build Order

### Wave 1 (Foundation + Core Creation) — Build First
1. `social-context` — Everything else depends on this
2. `social-copywriting` — Most common use case
3. `content-repurposing` — Highest leverage
4. `thread-writing` — High demand, well-defined format
5. `content-ideation` — Upstream of everything

### Wave 2 (Strategy + Distribution)
6. `content-strategy` — The "think before you create" layer
7. `posting-strategy` — When/how to publish
8. `content-calendar` — Planning tool
9. `carousel-design` — Visual-heavy, high engagement format

### Wave 3 (Analytics + Community)
10. `social-analytics` — Close the feedback loop
11. `content-audit` — Periodic review
12. `community-management` — Engagement layer
13. `video-scripting` — Growing format

### Wave 4 (Growth + Advanced)
14. `audience-growth` — Platform algorithms & growth tactics
15. `campaign-planning` — Multi-channel campaigns
16. `newsletter-writing` — Owned audience
17. `social-seo` — Search optimization
18. `ugc-strategy`, `influencer-outreach`, `monetization` — Advanced plays

---

## Open Questions

1. **Naming convention**: `socialskills-*` prefix or flat names? (I lean flat with plugin grouping)
2. **Platform coverage**: Start with X, LinkedIn, Instagram, TikTok, YouTube? Or broader?
3. **Integration with existing ckm skills**: Hard dependency or soft references?
4. **Target user**: Solo creator? Marketing team? Agency? (Affects depth vs breadth)
5. **Update cadence**: Platform specs change quarterly — how do we handle this?
