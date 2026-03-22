# Skill Evaluation Report

## Summary
- **Skill:** social-skills (9-skill pack + 1 standalone tool)
- **Domain:** Social media content creation & strategy
- **Tier:** ✅ Expert-Reviewed
- **Overall Score:** 72/100
- **Verdict:** Install-worthy. Genuinely useful reference content and process enforcement, but missing GOTCHAS.md files, EXPERT.md, and formal test cases. The reference files (anti-patterns, hook formulas, platform specs) are the real differentiators — they add knowledge Claude doesn't have by default.

---

## Security Scan

**SECURITY SCAN: PASS**
Issues: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 1 LOW

- **MEDIUM** — `scripts/fetch-posts.py:91` accepts arbitrary `--input-file` path without traversal validation. A user could read any file the process can access. Acceptable for a CLI tool but worth noting for sandboxed environments.
- **LOW** — `plugin.json:5` contains author's real name ("Philip Bankier"). Intentional for open source attribution, but flagged per PII protocol.

No prompt injection, credential exposure, malicious behavior, or scope creep detected. API key correctly read from environment variable (`SOCIAVAULT_API_KEY`), not hardcoded. No `eval()`, `exec()`, `os.system()`, or `shell=True` patterns. `subprocess` usage limited to test runner with controlled paths.

---

## Format & Structure

**FORMAT: PASS**
Structure score: **6/11** checks passed

**Required (all pass):**
- [x] Valid YAML frontmatter with `name` and `description` — all 10 skills
- [x] `name` matches directory name — all 10
- [x] Description 50-1024 chars — all 10 (range: 226-393 chars)
- [x] Description reads as trigger — all include "Use when" phrasing
- [x] SKILL.md body ≥ 200 words — all 10 (range: 655-1130 words)

**Structural quality:**
- [x] SKILL.md < 500 lines — all 10 (max: 203 lines)
- [x] Third-person imperative — mostly yes ("Load config.json", "Generate files", "Apply platform-specific rules")
- [x] JIT loading — skills reference platform files and anti-patterns in subdirectories
- [ ] Negative triggers — 7/10 skills have "This Skill Does NOT" sections ✅, but only omni-viral-humanizer has negative triggers in the description itself ❌
- [ ] No documentation cruft — README.md, CONTRIBUTING.md, CHANGELOG.md present (intended for humans/GitHub, but costs tokens if loaded by agent) ⚠️
- [ ] GOTCHAS.md — **MISSING from all 10 skills**. Some skills embed gotchas inline (content-calendar has 4, thread-writing has 4, content-repurposing has 4), but no standalone files.
- [ ] EXPERT.md — **MISSING entirely**
- [x] references/ directory — present with 21 supporting files
- [x] scripts/ directory — 7 Python scripts
- [ ] tests/ directory — no formal test directory; `test-all.py` and `test.py` exist but in scripts/ and omni-viral-humanizer/

**Structural notes:** The skill pack has good structure for a v0.1.0. The `<HARD-GATE>` pattern (used in 7/10 skills) enforces process ordering. The SKILL-IO-MAP.md documenting data flow is excellent — this is rare even in Tier 1 packs. However, the absence of standalone GOTCHAS.md files is the biggest structural gap.

---

## Slop Detection

**Hedge density: 0.05% — Excellent**
Only 4 hedge words across 8,554 words of SKILL.md content: "consider" (1), "ensure" (1), "leverage" (2 — both in the anti-patterns file telling you NOT to use "leverage"). Effectively zero hedging. This is expert-level writing discipline.

**Specificity ratio: 1.61 — Excellent**
822 concrete items across 512 sentences. Nearly every sentence contains a specific number, named tool, or conditional rule. Examples:
- "Singles: punchy, under 275 chars" (omni-viral-humanizer/SKILL.md)
- "replies = 27x weight of a like" (omni-viral-humanizer/SKILL.md)
- "LinkedIn: 40% text posts, 35% carousels, 15% polls, 10% articles" (content-calendar/SKILL.md)
- "Engagement drops ~60% after tweet 4" (thread-writing/SKILL.md)

**Obvious content: ~15% of instructions add no value beyond baseline**
Most instructions are genuinely specific. The obvious portions:
- "Understand the Request" sections that list generic questions ("What platform? What topic?")
- Some "Related Skills" and "This Skill Does NOT" sections state the obvious
- Content pillar ratio recommendations (40/25/20/10/5) are common knowledge

But ~85% of instructions contain platform-specific rules, algorithm weights, or process gates that Claude wouldn't know without the skill.

**Max consecutive generic sentences: 3**
Location: `social-context/SKILL.md` lines 98-105 (the skill selection guide table — valuable for routing but each row is template-level)

**"You are an expert" pattern: No (with one exception)**
omni-viral-humanizer/SKILL.md opens with "You are an execution-focused social content optimizer" — technically hits this pattern, but the rest of the skill immediately backs it with specific rules, not vague credentials. Borderline acceptable.

**Domain vocabulary vs expertise:**
This skill pack passes the expertise test. Examples of vocabulary backed by actual expertise:
- "Reply = 27x weight" → cites algorithm source code analysis
- "First 210 chars = see more fold" → specific LinkedIn UX detail
- "Save-to-like ratio" on TikTok → specific algorithm signal
- "2-3 hour window" on Reddit → actionable timing detail
- Platform-specific anti-pattern lists with "why it's a tell" explanations

**Overall: Clean — this is not LLM-generated slop**

The content reads as genuinely expert-written. Specific numbers, opinionated rules, platform-specific gotchas, and failure modes that feel experienced rather than hypothesized.

**Worst offending sections (for transparency):**
- `social-context/SKILL.md` — "How Other Skills Use This" section is procedural boilerplate
- `content-ideation/SKILL.md` — "Understand the Need" questions are generic interview prompts
- `posting-strategy/SKILL.md` — timing tables, while specific, are widely available data

---

## Quality Scores

| Dimension | Score | Key Evidence |
|-----------|-------|-------------|
| Specificity | 21/25 | 563 specific numbers, 242 named tools, conditional rules throughout. Platform specs with pixel dimensions, character limits, algorithm weights. Anti-patterns list 30+ specific AI-tell words with alternatives. Hook formulas library has 55+ formulas with platform tags and concrete examples. Loses points: some timing data is "general best practices" level. |
| Expertise Authenticity | 18/25 | Non-obvious insights: "Reply = 27x weight of a like" (X algo), "engagement drops ~60% after tweet 4" (thread decay), "LinkedIn penalizes posts with external links" (link-in-comments pattern), "Reddit's 2-3 hour window" (rising→hot transition timing), "Save-to-like ratio" as TikTok ranking signal. Anti-patterns file has genuine "been burned by this" energy (emoji bullet pattern, broem format, specific subreddit behavior). Loses points: no GOTCHAS.md with war stories, no failure narratives, no "we tried X and it backfired." |
| Actionability | 17/20 | Clear step-by-step process in every skill with explicit ordering. `<HARD-GATE>` pattern enforces "load config first" before any content generation — this is real process enforcement, not suggestions. Content-review has a two-stage gate (compliance → quality) with pass/fail criteria and specific scoring rubric. SKILL-IO-MAP.md shows data flow. Loses points: some skills describe process without enforcing it (content-ideation's "prioritization" step is a suggestion, not a gate). |
| Completeness | 11/15 | Happy path well covered across all skills. Edge cases partially handled: content-review handles batch review, posting-strategy has anti-patterns for frequency mistakes, thread-writing handles engagement drop-off. Cross-references between skills are explicit and accurate. "This Skill Does NOT" sections in 7/10 skills. Loses points: no escalation criteria ("when to tell the user this needs a professional"), no "when to break the rules" sections, Instagram/TikTok/YouTube platform references are thinner than X/LinkedIn. |
| Testability | 5/15 | `test-all.py` validates structure (YAML frontmatter, file existence, reference completeness) — 10 checks, all passing. `omni-viral-humanizer/test.py` checks SKILL.md structure. 4 test walkthroughs in `examples/` with expected outputs. 50-post sample dataset for analysis testing. BUT: no test cases that validate output QUALITY. No "given this input, the skill should produce output matching these criteria." No skillgrade-compatible test format. |
| **Total** | **72/100** | |

---

## Tier Assignment

**Tier: ✅ Expert-Reviewed (Score: 72)**

Meets Expert-Reviewed requirements:
- ✅ Passes security + format gates
- ✅ Evidence of expert review (non-obvious insights, specific algorithm data)
- ✅ Clear process steps with hard gates

**Tier 1 Checklist (Expert-Certified): 5/10 — does NOT qualify**

- [x] ≥5 non-obvious insights — Yes (reply 27x, thread decay 60%, LinkedIn link penalty, Reddit 2-3h window, TikTok save-to-like, emoji bullet AI-tell pattern, broem anti-pattern)
- [ ] GOTCHAS.md with specific failure modes — **Missing from all skills**. Gotchas are inline in some skills but no standalone files.
- [x] Process enforcement — Yes, `<HARD-GATE>` pattern in 7/10 skills, two-stage review gate in content-review
- [x] Real tooling/scripts/reference files — 7 Python scripts, 21 reference files, 124KB+ reference content
- [ ] Expert attribution — **No EXPERT.md**
- [ ] ≥3 test cases with measurable criteria — No quality-validation test cases
- [x] Makes agent BETTER at the task — Yes, significantly (see Value Assessment below)
- [x] Names specific tools/frameworks — Extensive (SociaVault, Apify, specific platform specs, named algorithm signals)
- [ ] Anti-patterns with concrete examples — Anti-patterns file is excellent, but most individual skills lack their own
- [ ] Edge case handling and escalation criteria — Partial edge cases, no escalation criteria

**Comparison to Tier 1 benchmarks:**
- **vs gstack:** social-skills has better reference content depth but lacks gstack's real tooling integration (headless browser, smart routing). Similar process orientation.
- **vs superpowers:** superpowers has harder gates (mandatory pipeline, subagent review). social-skills has the `<HARD-GATE>` pattern but it's softer — the agent can technically skip it. superpowers' two-stage review is matched by content-review.
- **vs pm-skills:** pm-skills encodes specific named frameworks (Teresa Torres OSTs, Cagan, Savoia). social-skills encodes specific platform algorithm data instead. Comparable domain depth, different domain.

---

## Deep Analysis

### Value Assessment

**What does this skill teach an agent that it doesn't already know?**
Significantly more than baseline. Key value-adds:
1. **Algorithm weights** — Reply 27x, bookmark 10x, repost 20x on X. Claude knows "replies are important" but not the specific multipliers.
2. **Platform-specific formatting** — LinkedIn's 210-char fold, Reddit's zero-hashtag/zero-emoji rules, Instagram's 5-hashtag 2026 limit. These are specific and time-stamped.
3. **Anti-pattern detection** — The 30+ AI-tell words with alternatives is genuinely useful. Claude would generate "leverage" and "game-changer" without this guard.
4. **Process enforcement** — Config-first gates prevent the common failure mode of generating generic content without brand context.
5. **Cross-platform adaptation** — The repurposing matrix and cross-posting rules encode real knowledge about what changes between platforms.

**If I deleted this skill and just asked the agent the same task, how much worse would the output be?**
~35-40% worse. Claude can write social posts without this skill, but it would:
- Use AI-tell vocabulary freely
- Miss platform-specific formatting rules (especially Reddit and TikTok)
- Skip the config-first gate (generating generic instead of branded content)
- Not know specific algorithm signals
- Produce less diverse output (same structure every time)

**Would a domain professional learn anything from reading this?**
A junior social media manager would learn a lot. A senior practitioner would nod along with most but would find the anti-patterns list and algorithm signal weights useful as a reference. Not "yeah, obviously" — more "yeah, that's right, good collection."

### Process Assessment

- **Enforcement vs description:** The `<HARD-GATE>` pattern enforces config-first loading. Content-review enforces a two-stage gate with pass/fail before proceeding. Most other process steps are described, not enforced.
- **Hard gates:** 7/10 skills have explicit hard gates. Strongest: social-copywriting (3 required loads before any generation), content-review (Stage 1 must pass before Stage 2).
- **Chaining:** Skills chain well. SKILL-IO-MAP.md documents the flow explicitly. social-context → creation skills → content-review is a clear pipeline.
- **Failure handling:** Thread-writing handles engagement drop-off. Content-review handles rewrite offers. Content-calendar acknowledges over-planning. But no skill has explicit "when to escalate to a human" criteria.

### Expertise Markers Found
- ✅ Counterintuitive advice: "Don't thread when a single tweet works" (thread-writing gotcha), "Calendar ≠ commitment" (content-calendar)
- ✅ Specific numbers with context: "Reply = 27x", "engagement drops ~60% after tweet 4", "Reddit's 2-3 hour window"
- ✅ Named exceptions: "TikTok timing less critical than other platforms — can resurface weeks later" vs Reddit's strict 2-3h window
- ✅ Time-stamped knowledge: "Instagram 2026 limit: 5 hashtags", "Last updated: March 2026"
- ⚠️ Failure stories: Referenced but not first-person ("The last time" stories are absent)
- ✅ Decision trees: content-review's scoring rubric, SKILL-IO-MAP routing table
- ✅ Tool-specific gotchas: Reddit anti-patterns, LinkedIn broem format, TikTok watermark detection

### Anti-Expertise Markers Found
- ❌ "You are an execution-focused social content optimizer" (omni-viral-humanizer opening) — mild
- ❌ Some "Related Skills" sections are lists without guidance on when to use which — but "This Skill Does NOT" sections partially compensate
- ❌ Posting strategy timing tables are "generally available" data — not expert-exclusive knowledge
- No bullet lists restating job titles ✅
- No "best practices" without specifying which ✅
- No "consider your audience" without specifics ✅

---

## Top 3 Strengths

1. **Anti-patterns reference (references/anti-patterns.md + ai-tell-checklist.md)** — 30+ AI-tell words with specific human alternatives, platform-specific cringe patterns, the "3-Read Test." This is genuinely expert content that makes the agent measurably better. A social post processed through this checklist will read noticeably more human. (anti-patterns.md, ai-tell-checklist.md)

2. **Process enforcement via `<HARD-GATE>` pattern** — 7/10 skills enforce config-first loading before any content generation. This prevents the #1 failure mode of social content skills: generating generic "5 tips for success" content without brand context. The two-stage review gate in content-review (compliance → quality) is a genuine quality improvement over "just review it." (social-copywriting/SKILL.md lines 3-8, content-review/SKILL.md)

3. **Platform-specific algorithm data with evidence quality** — X algorithm weights (27x reply, 10x bookmark, 20x repost) sourced from open-source code analysis. LinkedIn dual-encoder ranking. TikTok save-to-like ratio. Reddit's 2-3 hour rising→hot window. This isn't "post at good times" advice — it's specific, sourced, and actionable. The omni-viral-humanizer sources.md rates evidence quality (🟢/🟡/🔴). (omni-viral-humanizer/references/*/algo-deep-dive.md, sources.md)

## Top 3 Issues

1. **No GOTCHAS.md files anywhere** — The evaluation framework explicitly requires these for Tier 1 and recommends them for Tier 2. Several skills embed gotchas inline (content-calendar has 4, thread-writing has 4), but standalone GOTCHAS.md files with experienced failure modes, war stories, and "we tried X and it backfired" narratives are completely absent. **Fix:** Extract inline gotchas into standalone files and add 3-5 more per skill from real experience. (All skill directories)

2. **No quality-validation test cases** — `test-all.py` validates structure (frontmatter, file existence) but zero tests validate output quality. No "given this LinkedIn post, content-review should flag X and score Y." No skillgrade-compatible format. The 4 example walkthroughs are close but don't have measurable pass/fail criteria. **Fix:** Add `tests/` directory with 3+ test cases per major skill: input post + expected review output, input draft + expected humanization, input config + expected calendar structure. (Missing tests/ directory)

3. **No EXPERT.md or attribution** — No documentation of who created this knowledge, what experience backs it, or how the algorithm data was sourced (except omni-viral-humanizer's sources.md, which is good). For marketplace trust, attribution matters. **Fix:** Add EXPERT.md documenting: author background, how algorithm data was gathered, which claims are from personal experience vs research. (Missing file)

---

## Recommendations

**To reach Tier 1 (Expert-Certified, ≥85 points):**

1. **Add GOTCHAS.md to every skill** — Extract inline gotchas and add 3-5 more per skill. Focus on failure modes: "We posted a LinkedIn carousel with 15 slides and engagement dropped because..." Real specificity. (+5-8 points on Expertise Authenticity and Completeness)

2. **Add quality-validation test cases** — Create `tests/` with input/expected-output pairs:
   - Test: content-review given a post with 3 AI-tells → should flag them and score ≤3/5 on Cringe
   - Test: social-copywriting given Reddit target → output should have 0 hashtags, 0 emoji in title
   - Test: omni-viral-humanizer given generic draft → humanized output should score ≤2 on AI-tell checklist
   (+5-8 points on Testability)

3. **Add EXPERT.md** — Document author credentials, how algorithm data was sourced, which insights come from personal experience vs published research. Reference the sources.md pattern from omni-viral-humanizer. (+2-3 points on Expertise Authenticity)

4. **Add negative triggers to descriptions** — Currently only omni-viral-humanizer hints at what NOT to use it for. Each description should include: "NOT for: [specific exclusions]." This prevents misactivation and is a structural quality marker. (+1-2 points on Structure)

5. **Add escalation criteria** — "When to tell the user to hire a professional" or "When this skill is insufficient." Example: "If the user needs crisis communications, brand reputation management, or legal-sensitive content, this skill is NOT appropriate — recommend a PR professional." (+2-3 points on Completeness)

6. **Thin platform references (Instagram, TikTok, YouTube)** — The X and LinkedIn algo deep dives in omni-viral-humanizer are good. Instagram, TikTok, and YouTube are thinner. Add algo deep dives and viral examples for these three platforms. (+2-3 points on Completeness)

**Total potential improvement: 72 → 85-92 with these changes.**

---

## Comparison

| Dimension | social-skills | gstack | superpowers | pm-skills |
|-----------|--------------|--------|-------------|-----------|
| Skills count | 10 | 15 | ~8 | 65 |
| Process enforcement | `<HARD-GATE>` (7/10) | Role-based routing | Mandatory pipeline | Three-layer hierarchy |
| Real tooling | 7 Python scripts | Headless browser, smart routing | Subagent pipeline | Framework templates |
| Reference depth | 124KB+ (21 files) | Moderate | Moderate | Deep (named frameworks) |
| GOTCHAS.md | ❌ Missing | ✅ Present | ✅ Present | ✅ Present |
| Test cases | Structural only | Quality validation | Quality validation | Framework validation |
| Domain specificity | High (platform algorithms) | High (YC/startup) | High (dev workflow) | High (PM frameworks) |
| Estimated tier | Expert-Reviewed | Expert-Certified | Expert-Certified | Expert-Certified |

**Bottom line:** social-skills has Tier 1-quality reference content trapped in a Tier 2 structure. The anti-patterns, hook formulas, algorithm data, and platform specs are genuinely expert-level. The gap is structural: no GOTCHAS.md, no EXPERT.md, no quality test cases. These are fixable in a focused session.
