# social-skills

Your all-around social media and content Swiss army knife with deep expertise and high-taste curation.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](package.json)
[![Skills](https://img.shields.io/badge/skills-9-orange.svg)](#skill-reference)
[![Platforms](https://img.shields.io/badge/platforms-6-purple.svg)](#platforms)

Built for **solo creators, SMBs, and early-stage founders** who want to stop guessing and start posting with confidence.

## Platforms

X/Twitter · LinkedIn · Reddit · Instagram · TikTok · YouTube (Shorts + long-form)

## Quick Start

### 1. Install

```bash
# OpenClaw
openclaw skills add social-skills

# Or clone directly
git clone https://github.com/your-org/social-skills.git
```

### 2. Configure

Tell the agent about your brand, audience, and voice:

```
I run a B2B SaaS for project management, targeting startup founders.
My tone is direct and practical — no corporate speak.
Platforms: X, LinkedIn, Instagram.
```

The `social-context` skill creates your config automatically.

### 3. Create

```
Write me a LinkedIn post about why most PM tools are overcomplicated.
```

That's it. The agent handles hook optimization, platform formatting, AI-tell removal, and CTA selection.

## What's Inside

### Modular Skill Pack (9 skills)

Composable skills that work together or independently:

| Skill | Description | When to Use |
|-------|-------------|-------------|
| `social-context` | Brand/audience/voice configuration | First — sets up everything else |
| `social-copywriting` | Platform-native post writing | Writing any social post |
| `content-review` | Two-stage quality + compliance review | Before publishing |
| `thread-writing` | Multi-part thread/carousel creation | X threads, LinkedIn carousels |
| `content-ideation` | Idea generation with 15 frameworks | Weekly content planning |
| `content-repurposing` | Source → multi-platform adaptation | Repurposing blogs, podcasts, videos |
| `content-calendar` | Date-stamped posting schedule | Weekly/monthly planning |
| `posting-strategy` | Timing, frequency, cross-posting rules | Platform strategy decisions |
| `account-analysis` | Voice profile + engagement analysis | Studying your own or competitor accounts |

### Standalone Tool

| Tool | Description |
|------|-------------|
| `omni-viral-humanizer` | Zero-setup humanizer + optimizer for all 6 platforms. Drop in a draft, get platform-native outputs with scoring. |

## Typical Workflows

### Quick Post
```
social-context → social-copywriting → content-review → publish
```

### Weekly Planning
```
content-ideation → content-calendar → social-copywriting → content-review
```

### Repurpose a Blog Post
```
content-repurposing → social-copywriting (per platform) → content-review
```

### Account Audit
```
account-analysis → social-context (update voice profile) → posting-strategy
```

### Quick-Fire Humanize
```
omni-viral-humanizer (standalone — no setup needed)
```

## Scripts

All Python 3 stdlib — zero pip installs required.

| Script | Description | Example |
|--------|-------------|---------|
| `adapt-cross-platform.py` | Adapt text for different platforms | `python3 scripts/adapt-cross-platform.py --text "..." --source linkedin --targets x-twitter,reddit` |
| `generate-calendar.py` | Generate content calendar (MD + JSON) | `python3 scripts/generate-calendar.py --weeks 4 --platforms "x-twitter,linkedin" --pillars "educational,personal" --frequency "5,3"` |
| `content-log.py` | Track published content (add/list/stats/search) | `python3 scripts/content-log.py add --platform linkedin --format text-post --topic "..." --pillar educational --content "..."` |
| `fetch-posts.py` | Fetch posts from SociaVault or local file | `python3 scripts/fetch-posts.py --provider paste --input-file data/posts.jsonl` |
| `analyze-account.py` | Analyze engagement patterns from JSONL | `python3 scripts/analyze-account.py --input-file data/posts.jsonl` |
| `validate-skills.py` | Validate all skill YAML frontmatter | `python3 scripts/validate-skills.py` |
| `test-all.py` | Run full test suite | `python3 scripts/test-all.py` |

## Reference Files

124KB+ of opinionated, platform-specific guidance:

- **Platform references** (6 files): Algorithm signals, formatting rules, engagement patterns for each platform
- **Hook formulas** (55+): Categorized by type with platform tags and examples
- **CTA patterns**: Per-platform CTAs mapped to algorithm signals
- **Anti-patterns**: What NOT to do (AI tells, engagement bait, format mistakes)
- **Repurposing matrix**: Every source→target format pair with adaptation rules
- **Ideation frameworks** (15): Repeatable idea generation systems
- **Cross-posting rules**: Platform pair checklists and sequencing strategy

## Examples

See the `examples/` directory for full walkthroughs:

- `quick-start-test.md` — First post in 5 minutes
- `full-workflow-test.md` — Complete 6-step pipeline
- `account-analysis-test.md` — Data → analysis → voice profile
- `omni-viral-humanizer-test.md` — Full humanization with expected JSON output

Sample data: `examples/data/sample-posts.jsonl` (50 realistic posts modeled on real viral patterns)

## Architecture

```
social-context (foundation — all skills depend on this)
       ↓
  ┌────┴────┐
  ↓         ↓
Writing   Strategy
Skills    Skills
  ↓         ↓
content-review (quality gate)
```

- **Platform .md files** are the static reference layer — skills read them, not the other way around
- **social-context** is hard-gated: other skills check for config before running
- **content-review** runs a two-stage review: platform compliance → quality + voice

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Short version: PRs welcome for platform reference updates, new viral examples, and bug fixes. New skills require discussion first.

## License

MIT — see [LICENSE](LICENSE).
