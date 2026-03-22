# Contributing to social-skills

Thanks for your interest. This project is curated — we value quality over quantity.

## What We Accept

### Always Welcome
- **Platform reference updates**: Algorithm changes, new engagement data, updated best practices
- **Viral examples**: Real posts with engagement data and "why it worked" analysis
- **Bug fixes**: Script issues, validation errors, broken references
- **Typo/clarity fixes**: In any documentation or reference file

### Discuss First (Open an Issue)
- **New skills**: Propose the skill, its inputs/outputs, and why existing skills don't cover it
- **New platforms**: Must include algorithm reference, viral examples, and sources.md
- **Major script changes**: Discuss the approach before building
- **Architecture changes**: Anything that affects how skills compose

### Not Accepted
- Skills that require pip/npm installs (stdlib only)
- Platform references without evidence quality ratings
- Viral examples without engagement data or "why it worked" analysis
- AI-generated content in reference files (the irony is not lost on us)

## How to Add/Update Platform References

1. Check the existing file in `skills/social-context/references/platforms/<platform>.md`
2. Every algorithm claim must include:
   - Source (link, document name, or "community consensus")
   - Evidence quality: 🟢 High (official) | 🟡 Medium (credible analysis) | 🔴 Low (anecdotal)
   - Date of the information
3. If a claim is outdated, mark it with `⚠️ OUTDATED` and add the current information

## How to Add Viral Examples

1. Find the right file: `omni-viral-humanizer/references/<platform>/viral-examples.txt`
2. Each example must include:
   - Post text (or script summary for video)
   - Author type (not necessarily the name — e.g., "SaaS founder, ~15K followers")
   - Format
   - Engagement metrics (mark estimates with ~)
   - Date
   - "Why it worked" analysis (2-5 bullet points)
3. Prefer real public posts. If using patterns/composites, note that clearly.

## How to Add a New Skill

1. **Open an issue** describing the skill's purpose, inputs, outputs, and relationship to existing skills
2. Once approved, create the skill directory:
   ```
   skills/<skill-name>/
   ├── SKILL.md          # Required: YAML frontmatter + instructions
   └── references/       # Optional: supporting reference files
   ```
3. SKILL.md must have valid YAML frontmatter with `name` and `description`
4. `name` must match the directory name
5. `description` must be ≤ 1024 chars and function as a trigger (not just a summary)
6. Update `SKILL-IO-MAP.md` with the new skill's inputs and outputs
7. Run `python3 scripts/validate-skills.py` — must pass
8. Run `python3 scripts/test-all.py` — must pass

## PR Process

1. Fork and create a feature branch
2. Make your changes
3. Run `python3 scripts/test-all.py` — all checks must pass
4. Submit PR with:
   - What you changed and why
   - Evidence/sources for any new claims
   - Screenshots of test results
5. Maintainer reviews within 1 week

## Code Style

- Python scripts: stdlib only, argparse for CLI, type hints encouraged
- Reference files: Markdown with tables for structured data
- SKILL.md files: Follow the AgentSkills spec (https://agentskills.io/specification)

## Quarterly Maintenance

Every 3 months, someone should:

1. **Review platform references** — algorithm claims older than 6 months get marked for review
2. **Update viral examples** — replace oldest examples with fresh ones
3. **Check sources.md** — verify links still work, update dates
4. **Run full test suite** — ensure nothing has drifted
5. **Update CHANGELOG.md** — document what changed

## Questions?

Open an issue. We're friendly.
