# omni-viral-humanizer

One unified AgentSkill for **X + LinkedIn + TikTok**.

It takes a raw idea/draft/topic, **humanizes it first**, then outputs platform-native versions for the requested platform (`X`, `LinkedIn`, `TikTok`, or `all three`).

## What it outputs

- Ready-to-post copy/script variants
- Platform-specific analysis
- Suggested posting windows
- Media prompts
- Engagement score (heuristic)
- Cross-post adaptation notes

## Why this exists

Most "viral" prompts produce generic slop. This skill is designed around:

1. Humanization layer first
2. Platform-specific optimization second
3. Strict output contract (JSON + readable Markdown)
4. Reusable references and templates

## Install (AgentSkills layout)

```bash
mkdir -p .agents/skills
cp -R omni-viral-humanizer .agents/skills/
```

Or tool-specific:
- Claude Code: `.claude/skills/omni-viral-humanizer`
- OpenClaw: `~/.openclaw/skills/omni-viral-humanizer`

## Usage examples

- "Turn this idea into an X post"
- "Humanize this and optimize for LinkedIn"
- "Make this TikTok-ready"
- "Do all three"

## Notes

- References are intentionally split by platform.
- Claims are based on March 2026 desk research and should be revalidated quarterly.
