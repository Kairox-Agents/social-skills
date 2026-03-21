# social-skills — Completion Plan

## Overview

**Current state:** 9 SKILL.md files + 6 platform references + anti-patterns + omni-viral-humanizer scaffold. All committed. No executable scripts, no test harness, no real viral examples, no hook formula library.

**Target state:** Production-ready skill pack that can be installed, tested end-to-end, and demonstrated with real usage examples.

**Workflow:** I (Claude/OpenClaw) serve as researcher, planner, and judge. Codex CLI executes each phase via codex-handoff. I review results after each phase.

---

## Phase 1: Repository Structure & Tooling

### 1.1 Create top-level package structure
- Create `package.json` with name `social-skills`, version `0.1.0`, MIT license
- Scripts: `"test": "python3 scripts/test-all.py"`, `"validate": "python3 scripts/validate-skills.py"`
- No npm dependencies (Python stdlib only for scripts)

### 1.2 Create validation script — `scripts/validate-skills.py`
- Walk `skills/` directory
- For each subdirectory: verify `SKILL.md` exists and has valid YAML frontmatter (`name`, `description`)
- Verify `name` field matches directory name
- Verify `description` is ≤ 1024 chars
- Verify SKILL.md is ≤ 500 lines
- Verify all `references/` files referenced in SKILL.md actually exist
- Print PASS/FAIL per skill + summary

### 1.3 Create test harness — `scripts/test-all.py`
- Run `validate-skills.py` first
- Run `omni-viral-humanizer/test.py`
- Verify all platform reference files exist in `skills/social-context/references/platforms/`
- Verify `anti-patterns.md` exists in `skills/social-copywriting/references/`
- Verify `SKILL-IO-MAP.md` exists at root
- Print overall PASS/FAIL

### 1.4 Create `.gitignore`
- `__pycache__/`, `*.pyc`, `.DS_Store`, `data/*.jsonl`, `data/*.json` (user-generated state files)
- Do NOT ignore `skills/*/references/` or `examples/`

## Phase 2: Python Scripts (stdlib only)

### 2.1 Create `scripts/adapt-cross-platform.py`
- Input: a piece of text content + source platform + target platform(s)
- Output: adapted versions with platform-specific formatting applied
- Uses the character limits and rules from platform reference files (hardcoded constants, not file parsing)
- Handles: character truncation with warning, hashtag count validation, emoji count check
- Prints JSON output with `platform`, `adapted_text`, `char_count`, `warnings[]`
- Zero external dependencies

### 2.2 Create `scripts/generate-calendar.py`
- Input: number of weeks, platforms (comma-separated), pillars (comma-separated), posts-per-week-per-platform
- Output: Markdown calendar file + JSON calendar file
- Uses the pillar distribution ratios from content-calendar SKILL.md (40% educational, 25% personal, 20% opinion, 10% BTS, 5% promotional)
- Generates date-stamped entries with platform, format, pillar, and placeholder topic
- Writes to `data/content-calendar.md` and `data/content-calendar.json`
- Zero external dependencies

### 2.3 Create `scripts/content-log.py`
- Manages the append-only content log at `data/content-log.jsonl`
- Subcommands: `add` (append entry), `list` (show recent N entries), `stats` (summary by platform/pillar/format), `search` (keyword search)
- Uses the per-platform content schemas from DECISIONS.md
- Zero external dependencies

### 2.4 Create `scripts/fetch-posts.py`
- Pluggable data fetcher for account-analysis
- Provider abstraction: `sociavault`, `apify`, `paste` (manual paste/file input)
- `sociavault` provider: REST API calls using urllib (no requests library)
- `paste` provider: reads from a local JSON/JSONL file
- Input: provider, platform, account handle, post count
- Output: normalized JSONL with `{id, date, platform, text, engagement{likes,comments,shares,saves}, format, media_type}`
- API key read from environment variable `SOCIAVAULT_API_KEY` or `APIFY_API_KEY`
- Zero external dependencies (urllib.request for HTTP)

### 2.5 Create `scripts/analyze-account.py`
- Input: JSONL file from fetch-posts.py
- Runs analysis dimensions from account-analysis SKILL.md:
  - Posting frequency (posts/week, day-of-week distribution, time-of-day)
  - Format distribution (% by format type)
  - Content length stats (avg, median, min, max characters)
  - Hashtag analysis (avg count, most common)
  - Engagement stats (avg likes/comments/shares by format)
  - Top 10% and bottom 10% posts by engagement
- Output: JSON report + summary Markdown
- Zero external dependencies

## Phase 3: Hook Formula Library & Reference Files

### 3.1 Create `skills/social-copywriting/references/hook-formulas.md`
- 50+ hook formulas organized by type: curiosity, story, value, contrarian, question, data, personal
- Each formula tagged with best platform(s)
- Each formula includes one concrete example
- Sourced from the platform reference files' hook sections + expanded

### 3.2 Create `skills/social-copywriting/references/cta-patterns.md`
- CTA patterns organized by platform
- Each CTA tagged with which algorithm signal it targets (replies, saves, shares, bookmarks)
- Anti-CTAs section (what NOT to say as a CTA per platform)

### 3.3 Create `skills/content-repurposing/references/repurposing-matrix.md`
- Complete source→target format mapping
- For each combination: what to extract, how to adapt, expected output length
- Sources: blog post, podcast transcript, video transcript, newsletter, presentation
- Targets: X single, X thread, LinkedIn post, LinkedIn carousel, Reddit post, Instagram caption, Instagram carousel, TikTok script, YouTube Short script, YouTube community post

### 3.4 Create `skills/content-ideation/references/ideation-frameworks.md`
- 15 ideation frameworks with step-by-step instructions
- Includes: pillar rotation, pain point mining, format-first, reverse engineering, 10x headlines, audience questions, trend jacking, contrarian angles, case study mining, number posts, before/after, behind-the-scenes, industry commentary, prediction posts, reaction posts

### 3.5 Create `skills/posting-strategy/references/cross-posting-rules.md`
- Platform-by-platform adaptation checklist
- What changes between each platform pair (X→LinkedIn, X→Reddit, LinkedIn→Instagram, etc.)
- Sequencing strategy (which platform first, spacing, timing)

## Phase 4: omni-viral-humanizer Completion

### 4.1 Populate `references/x/viral-examples.txt` with 5 real examples
- Each example: post text, format, approximate engagement metrics, date, "why it worked" analysis
- Focus on founder/startup accounts from March 2025-2026
- Mark any estimated metrics clearly

### 4.2 Populate `references/linkedin/viral-examples.txt` with 5 real examples
- Same structure as X examples
- Include mix: text post, carousel, founder story, data post, industry commentary

### 4.3 Populate `references/tiktok/viral-examples.txt` with 5 real examples
- Each: script summary, caption, format, approximate metrics, "why it worked"
- Focus on business/founder TikTok accounts

### 4.4 Create `references/humanization/ai-tell-checklist.md`
- Extract and expand from social-copywriting/references/anti-patterns.md
- Add platform-specific AI-tell patterns
- Add positive examples ("instead of X, write Y")

### 4.5 Upgrade `SKILL.md` to full v1.3 clarity
- Add Reddit, Instagram, YouTube sections to platform optimization rules
- Add per-platform scoring model (from PLAN.md)
- Ensure output JSON schema covers all 6 platforms
- Add `platform_specific_warnings` and `a_b_test_suggestion` fields

### 4.6 Create `references/*/sources.md` for each platform
- Every major algorithm claim linked to a source URL or document
- Date-stamped for freshness tracking

## Phase 5: End-to-End Testing Examples

### 5.1 Create `examples/quick-start-test.md`
- Walkthrough: install skills → run social-context quick-start interview → generate first post
- Include exact user input and expected agent output
- Platform: LinkedIn (most common first-time use case)

### 5.2 Create `examples/full-workflow-test.md`
- Complete pipeline test:
  1. Set up social-context (quick-start for "Acme SaaS, B2B project management, targeting startup founders")
  2. Generate 10 ideas with content-ideation
  3. Pick 3 ideas, write posts for X + LinkedIn + Instagram with social-copywriting
  4. Run content-review on all 3 posts
  5. Generate a 2-week content calendar
  6. Repurpose a sample blog post into multi-platform content
- Include exact inputs, expected outputs, and pass/fail criteria for each step

### 5.3 Create `examples/account-analysis-test.md`
- Walkthrough: provide 50 sample posts (synthetic) → run analysis → generate voice profile
- Include sample input data file (`examples/data/sample-posts.jsonl`)
- Include expected analysis output format
- Include expected voice-profile.md output

### 5.4 Create `examples/omni-viral-humanizer-test.md`
- Input: "Most startups fail at content marketing because they copy what big companies do"
- Expected output: humanized + optimized for X, LinkedIn, TikTok
- Include exact JSON + Markdown expected output format
- Pass criteria: all three platforms genuinely different, no AI-tells, platform rules respected

### 5.5 Create `examples/data/sample-posts.jsonl`
- 50 synthetic but realistic posts from a fictional SaaS founder
- Mix of platforms: X (20), LinkedIn (15), Instagram (10), Reddit (5)
- Mix of formats: singles, threads, carousels, text posts
- Varying engagement levels (some hits, some misses)
- Used by account-analysis-test and fetch-posts paste provider

## Phase 6: Documentation & Distribution

### 6.1 Finalize `README.md`
- Add "Quick Start" section with 3-step install
- Add "Full Workflow" section pointing to examples
- Add "Skill Reference" table with every skill, description, and when to use
- Add "Scripts" section documenting all Python scripts with usage examples
- Add "Contributing" section
- Add badges (license, version)

### 6.2 Create `CONTRIBUTING.md`
- How to add a new skill
- How to update platform references
- How to add viral examples
- PR process and review criteria
- Quarterly maintenance checklist

### 6.3 Create `CHANGELOG.md`
- v0.1.0 entry documenting everything built

### 6.4 Create `plugin.json` (AgentSkills marketplace manifest)
- Name, description, version, author, license, skills list, tags
- Install instructions for each platform

### 6.5 Create `openclaw.yaml` (OpenClaw manifest)
- Skill listing for OpenClaw discovery

## Phase 7: Integration Testing & Final Validation

### 7.1 Run `scripts/validate-skills.py` — must pass
- All 9 skills valid frontmatter
- All referenced files exist
- No SKILL.md over 500 lines

### 7.2 Run `scripts/test-all.py` — must pass
- Validation + structure checks

### 7.3 Run `scripts/generate-calendar.py` with test params — verify output
- `python3 scripts/generate-calendar.py --weeks 2 --platforms "x,linkedin,instagram" --pillars "educational,personal,opinion" --frequency "5,3,3"`
- Verify Markdown output is well-formatted
- Verify JSON output is valid and matches schema

### 7.4 Run `scripts/content-log.py add` + `list` + `stats` — verify CRUD
- Add 5 test entries
- List recent 3
- Show stats summary

### 7.5 Run `scripts/analyze-account.py` on sample data — verify output
- Input: `examples/data/sample-posts.jsonl`
- Verify JSON report has all analysis dimensions
- Verify Markdown summary is readable

### 7.6 Manual skill activation test
- Install skills into a test `.agents/skills/` directory
- Verify each SKILL.md loads correctly
- Verify platform references load on demand
- Verify cross-skill references work (social-copywriting can find social-context)

## Verification (All Phases)

After all phases complete:
- `python3 scripts/test-all.py` passes
- `python3 omni-viral-humanizer/test.py` passes
- All example walkthroughs are complete and accurate
- `git status` shows clean working tree
- Total file count: ~60+ files
- Total lines: ~10,000+
- README accurately describes all contents

---

## Codex Handoff Sequence

| Phase | Handoff To | Estimated Complexity | Dependencies |
|-------|-----------|---------------------|-------------|
| Phase 1 | Codex | Low | None |
| Phase 2 | Codex | Medium | Phase 1 |
| Phase 3 | Codex (with my reference content) | Medium | Phases 1-2 |
| Phase 4 | Codex (with my research) | Medium | Phases 1-3 |
| Phase 5 | Codex | Medium-High | Phases 1-4 |
| Phase 6 | Codex | Low | Phases 1-5 |
| Phase 7 | Codex (I review results) | Low | Phases 1-6 |

**My role at each phase:**
- Before: provide detailed plan + any reference content needed
- During: Codex executes
- After: review diff, run tests, judge quality, build correction prompt if needed
