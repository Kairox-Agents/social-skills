# social-skills

A full-stack agent skill pack for social media content creation, strategy, and growth.

Built on the [AgentSkills spec](https://agentskills.io). Works with Claude Code, OpenClaw, Codex, Cursor, and any AgentSkills-compatible tool.

## What's Inside

### Foundation
- **social-context** — Brand voice, audience, platforms, content pillars. Every other skill reads this first.

### Creation
- **social-copywriting** — Platform-native post writing (X, LinkedIn, Reddit, Instagram, TikTok, YouTube)
- **thread-writing** — Threads and serialized long-form content
- **content-repurposing** — Long-form → multi-platform atomization

### Strategy
- **content-ideation** — Topic and idea generation from pillars, audience, and trends
- **content-calendar** — Weekly/monthly planning in Markdown + JSON
- **posting-strategy** — Optimal timing, frequency, and cross-posting rules

### Quality
- **content-review** — Two-stage quality gate (platform compliance + taste/cringe check)

### Research
- **account-analysis** — Analyze accounts for voice DNA extraction and competitive intelligence

### Quick-Fire
- **omni-viral-humanizer** — Standalone: raw idea → humanized, algorithm-optimized posts for X + LinkedIn + TikTok in one shot

## Platform Coverage

Deep reference files (algorithm mechanics, specs, gotchas, voice guides) for:
- X/Twitter
- LinkedIn
- Reddit
- Instagram
- TikTok
- YouTube (Shorts + long-form)

## Install

### Claude Code
```bash
cp -R skills/* .claude/skills/
```

### OpenClaw
```bash
cp -R skills/* ~/.openclaw/skills/
```

### AgentSkills (universal)
```bash
cp -R skills/* .agents/skills/
```

## Design Principles

1. **Platform-deep, not platform-generic.** Separate reference files per platform with real algorithm knowledge and gotchas.
2. **Opinionated but modular.** Strong defaults, easy to override or skip skills you don't need.
3. **Gotchas-first.** Every skill and platform reference starts with what goes wrong.
4. **Hard gates.** No content generation until foundation context exists.
5. **Two-stage review.** Platform compliance + taste/quality check before publishing.
6. **Scripts that DO things.** Python (stdlib only) for calendar generation, content transformation, reporting.
7. **Persistent state.** Content log tracks everything across sessions.

## Target Users

Solo creators and SMB/early-stage startup founders who:
- Wear multiple hats
- Have 2-5 hours/week for social media
- Need to be on 3-6 platforms but can't be an expert on all
- Value quality over volume

## License

MIT
