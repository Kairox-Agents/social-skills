# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-03-22

### Added

#### Skills (9 modular skills)
- `social-context` — Brand/audience/voice configuration with quick-start interview
- `social-copywriting` — Platform-native post writing with anti-patterns reference
- `content-review` — Two-stage review (platform compliance + quality/voice)
- `thread-writing` — Multi-part thread and carousel creation
- `content-ideation` — Idea generation with 15 repeatable frameworks
- `content-repurposing` — Source-to-multi-platform content adaptation
- `content-calendar` — Date-stamped posting schedule generation
- `posting-strategy` — Timing, frequency, cross-posting strategy
- `account-analysis` — Voice DNA extraction and engagement pattern analysis

#### Standalone Tool
- `omni-viral-humanizer` v1.3 — Zero-setup humanizer + optimizer for 6 platforms
  - AI-tell checklist with vocabulary, structural, and tone pattern detection
  - Per-platform scoring model (hook 30%, platform-fit 25%, interaction 25%, clarity 20%)
  - A/B test suggestions and humanization reports
  - Viral examples for X, LinkedIn, TikTok with "why it worked" analysis
  - Sources.md with evidence quality ratings for all algorithm claims

#### Platform References (124KB+)
- X/Twitter algorithm reference (reply 27x, bookmark 10x, repost 20x weights)
- LinkedIn algorithm reference (dual encoder, golden hour, dwell time signals)
- Reddit community and moderation guidelines
- Instagram save/carousel/reel optimization
- TikTok completion rate and save-to-like ratio signals
- YouTube thumbnail/title CTR and retention patterns

#### Reference Libraries
- Hook formulas (55+ formulas, 7 categories, platform-tagged)
- CTA patterns (per-platform, mapped to algorithm signals)
- Anti-patterns (AI tells, engagement bait, format mistakes)
- Repurposing matrix (every source→target format pair)
- Ideation frameworks (15 repeatable systems)
- Cross-posting rules (platform pair checklists)

#### Python Scripts (stdlib only)
- `adapt-cross-platform.py` — Multi-platform text adaptation with warnings
- `generate-calendar.py` — Content calendar generation (Markdown + JSON)
- `content-log.py` — Append-only content tracking (add/list/stats/search)
- `fetch-posts.py` — Post fetching from SociaVault API or local JSONL
- `analyze-account.py` — Engagement analysis with Markdown report
- `validate-skills.py` — Skill YAML frontmatter validation
- `test-all.py` — Full test suite

#### Documentation & Examples
- End-to-end test walkthroughs (quick-start, full-workflow, account-analysis, omni-viral-humanizer)
- 50-post sample dataset modeled on real viral patterns
- SKILL-IO-MAP.md documenting skill input/output relationships
- CONTRIBUTING.md with PR process and maintenance checklist
