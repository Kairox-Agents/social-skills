# Skill Evaluation Report (v2 — Post Platform Rewrite)

## Summary
- **Skill:** social-skills (9-skill pack + 1 standalone tool)
- **Domain:** Social media content creation & strategy
- **Tier:** ✅ Expert-Reviewed (borderline Expert-Certified)
- **Overall Score:** 79/100 (↑7 from 72)
- **Verdict:** Strong install. The platform reference rewrite pushed this from "good skill pack with thin spots" to "genuinely expert-grade reference library powering well-structured skills." The remaining gap to Tier 1 is structural (missing GOTCHAS.md files, EXPERT.md, quality test cases), not content.

---

## Security Scan

**SECURITY SCAN: PASS** (unchanged from v1)
Issues: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 1 LOW

- **MEDIUM** — `scripts/fetch-posts.py:91` accepts arbitrary `--input-file` path without traversal validation.
- **LOW** — `plugin.json:5` contains author's real name. Intentional for attribution.

No changes in security posture from v1.

---

## Format & Structure

**FORMAT: PASS**
Structure score: **6/11** checks passed (unchanged)

**Required:** All pass (same as v1)

**Structural quality (unchanged gaps):**
- [x] SKILL.md < 500 lines — all 10
- [x] Third-person imperative
- [x] JIT loading — platform refs + algo deep dives loaded on demand
- [ ] Negative triggers in descriptions — still only omni-viral-humanizer
- [ ] Documentation cruft — README/CONTRIBUTING still present (human-facing, token cost)
- [ ] GOTCHAS.md — **still missing from all skills** (gotchas are inline + in platform refs)
- [ ] EXPERT.md — **still missing**
- [x] references/ directory — **now 22 files** (was 21)
- [x] scripts/ directory — 7 scripts
- [ ] tests/ directory — still no formal test directory

**New structural note:** All 6 platform references now have "Key Gotchas" sections (7-8 items each). This partially compensates for missing standalone GOTCHAS.md files. The algo deep dives now cover all 6 platforms (was 3).

---

## Slop Detection

**Hedge density: 0.04% — Excellent** (improved from 0.05%)
8 hedge words across 20,498 words. Two of the "leverage" hits are in anti-patterns telling you NOT to use "leverage." Effectively zero hedging across doubled content volume.

**Specificity ratio: 2.04 — Exceptional** (improved from 1.61)
2,034 concrete items across 998 sentences. Every two sentences average four specific numbers, named tools/people, or conditional rules.

New specificity sources:
- Named people: Mosseri, Mohan, Sachdeva (executive statements with dates)
- Named systems: 360Brew, Grok, SimClusters, TweepCred, Phoenix, Thunder, Home Mixer
- Named analysis sources: AuthoredUp, TheShieldIndex, Botdog, OutlierKit, vidIQ, SocialInsider, MagicPost
- Specific percentages: -47% YoY, -72% video, 24.42% carousel engagement, 70% completion threshold, 150x like weight

**Obvious content: ~10%** (improved from ~15%)
The platform rewrites replaced generic timing tables and "best practices" with sourced, time-stamped algorithm data. Most remaining "obvious" content is in SKILL.md process sections ("Understand the Request" interview questions).

**Max consecutive generic sentences: 2** (improved from 3)

**"You are an expert" pattern: Still borderline**
omni-viral-humanizer/SKILL.md still opens with "You are an execution-focused social content optimizer." Same assessment: backed by immediate specifics.

**Domain vocabulary vs expertise: Strongly passes**
Every major platform claim now has:
- Named source (AuthoredUp, PostEverywhere, Mosseri statement, xAI GitHub)
- Evidence quality rating (🟢/🟡/🔴)
- Date stamp
- Specific number attached

**Overall: Clean — expert-written content with research-grade sourcing**

---

## Quality Scores

| Dimension | Score | Change | Key Evidence |
|-----------|-------|--------|-------------|
| Specificity | 23/25 | ↑2 | 2,034 concrete items across 998 sentences (ratio 2.04). All 6 platforms now have sourced algo data with named systems (360Brew, Grok/SimClusters, TweepCred), specific weights (+75 reply-by-author, 5x saves, 70% completion), named analysts (AuthoredUp 3M+ posts, Buffer 4M+ posts). Instagram now has DM shares as #1 Reels signal. YouTube has 4-layer testing system. Reddit has rising→hot pipeline. Every claim has dated source. |
| Expertise Authenticity | 20/25 | ↑2 | 110 non-obvious insight references found. New: 360Brew profile audit, TweepCred threshold 65 cliff, LinkedIn saves 4-6x delayed boost, TikTok 70% completion threshold (up from 50%), YouTube Shorts decoupled from long-form, Instagram carousel re-show mechanic, Grok sentiment analysis affecting distribution. Platform gotchas sections average 7-8 items each with specific "why this matters" explanations. Still missing: first-person failure narratives ("we tried X and it cost us Y"). |
| Actionability | 17/20 | — | Unchanged. `<HARD-GATE>` pattern, two-stage review, SKILL-IO-MAP. Process enforcement is the same. |
| Completeness | 13/15 | ↑2 | All 6 platforms now have full coverage: platform specs, algo deep dive, sources with evidence ratings, gotchas sections. Instagram went from thin to 9KB. YouTube from thin to 10KB. Reddit from generic community guidelines to 10KB with ML sort expansion, rising→hot pipeline, subreddit-specific strategies. Algo deep dives for all 6 platforms in omni-viral-humanizer (was 3). Sources.md for all 6 (was 3). |
| Testability | 6/15 | ↑1 | Same structural tests. Minor improvement: the platform references now serve as implicit test criteria (e.g., "Reddit output should have 0 hashtags, 0 emoji in title" is now explicitly documented in the Reddit reference). Still no formal input→output test cases. |
| **Total** | **79/100** | **↑7** | |

---

## Tier Assignment

**Tier: ✅ Expert-Reviewed (Score: 79)**

Closer to Expert-Certified than before but still blocked by structural gaps.

**Tier 1 Checklist: 6/10** (↑1 from 5/10)

- [x] ≥5 non-obvious insights — Yes (110 references found, significantly expanded)
- [ ] GOTCHAS.md with specific failure modes — **Still missing as standalone files** (now has Key Gotchas sections in all 6 platform refs + 4 SKILL.md files)
- [x] Process enforcement — Yes, `<HARD-GATE>` in 7/10 skills
- [x] Real tooling/scripts/reference files — 7 scripts, 22 reference files, 114KB reference content
- [ ] Expert attribution — **No EXPERT.md**
- [ ] ≥3 test cases with measurable criteria — No quality-validation test cases
- [x] Makes agent BETTER — Yes, significantly (see Value Assessment)
- [x] Names specific tools/frameworks — 395 named tool/service/person references
- [x] Anti-patterns with concrete examples — Anti-patterns file + platform-specific gotchas in all 6 refs (**upgraded from partial**)
- [ ] Edge case handling and escalation criteria — Partial edge cases, no escalation

---

## Deep Analysis

### Value Assessment

**What does this skill teach an agent that it doesn't already know?**
Substantially more than baseline. The platform rewrite added knowledge Claude does not have in training:
- X's January 2026 xAI release with confirmed Grok integration and updated weights
- LinkedIn's 360Brew replacement (late 2024-2026) with 150B parameter model
- Instagram's 5-hashtag hard limit and Trial Reels feature
- TikTok's January 2026 update: 70% completion threshold, follower-first distribution
- YouTube's Shorts decoupling and February 2026 Browse overhaul
- Reddit's expanded ML-powered Best sort

**If I deleted this skill and just asked the agent the same task, how much worse would the output be?**
~45-50% worse (↑ from 35-40%). The gap widened because:
- Claude's training data likely predates the Jan 2026 xAI release, 360Brew, TikTok's completion threshold change
- The evidence quality ratings (🟢/🟡/🔴) on every claim prevent the agent from stating unverified claims with false certainty
- Platform-specific gotchas are now comprehensive enough to catch most common mistakes

**Would a domain professional learn anything from reading this?**
Yes. Even a senior social media manager would find the sourced algorithm data valuable as a reference — especially the 360Brew profile audit mechanism, TweepCred thresholds, and the specific engagement weight table from X's open-source code. The sources.md files make this verifiable, which professionals care about.

### Process Assessment (unchanged)
- `<HARD-GATE>` enforcement in 7/10 skills
- Two-stage review gate in content-review
- SKILL-IO-MAP documents data flow
- No escalation criteria

### Expertise Markers (expanded)
- ✅ Time-stamped knowledge: "January 2026 xAI release," "Late 2025 Shorts decoupling," "November 2025 Sachdeva statement," "February 2026 Browse overhaul"
- ✅ Named sources with evidence quality: Every platform claim has 🟢/🟡/🔴 rating
- ✅ Counterintuitive advice: "Text outperforms video by 30% on X" (only platform), "Don't delete underperforming LinkedIn posts — 72h saves can revive them"
- ✅ Specific numbers with context: 150x like weight, 5x saves vs likes, 70% completion threshold, -47% reach YoY, 200B daily Shorts views
- ✅ Named exceptions: "TikTok timing less critical than X/LinkedIn," "Reddit community matters more than algorithm," "Shorts and long-form are independent on YouTube"
- ✅ Decision trees: Platform-specific format performance tables, signal weight rankings
- ⚠️ Failure stories: Still absent as first-person narratives

### Anti-Expertise Markers
- ❌ "You are an execution-focused social content optimizer" (omni-viral-humanizer) — mild, backed by specifics
- No other anti-expertise markers detected. The platform rewrite eliminated the remaining generic sections.

---

## Top 3 Strengths

1. **Sourced, time-stamped algorithm data across all 6 platforms** — Every major claim has a named source, evidence quality rating, and date. X's open-source weights are from the January 2026 xAI release. LinkedIn's 360Brew data comes from AuthoredUp's 3M+ post analysis. Instagram's signals are from Buffer's 4M+ post study + Mosseri's own statements. This is research-grade sourcing that no other social media skill pack offers. (114KB across 22 reference files)

2. **Anti-patterns + AI-tell checklist as quality gate** — 30+ AI-tell words with human alternatives, 6 platform-specific cringe pattern lists, the 3-Read Test. Combined with the `<HARD-GATE>` pattern forcing config-first loading, this creates a genuine quality improvement pipeline, not just a prompt. (anti-patterns.md, ai-tell-checklist.md, 7 HARD-GATE skills)

3. **Comprehensive platform gotchas** — All 6 platform references now end with 7-8 specific "Key Gotchas" with actionable detail: "TweepCred threshold 65 is a cliff," "Don't delete LinkedIn posts — 72h saves can revive them," "TikTok watermarks on Instagram reduce distribution." These are the kind of warnings that prevent real-world mistakes. (6 platform .md files, ~50 gotchas total)

## Top 3 Issues

1. **No standalone GOTCHAS.md files** — The evaluation framework requires these for Tier 1. Gotchas are now well-covered in platform references (7-8 per platform) and inline in 4 SKILL.md files, but no standalone GOTCHAS.md exists in any skill directory. This is the single most fixable gap. **Fix:** Extract from platform refs + inline gotchas into standalone files. Add first-person failure narratives. Estimated effort: 2-3 hours. (+3-4 points)

2. **No quality-validation test cases** — Still no "given this input, the skill should produce output matching these criteria" tests. The platform references implicitly define testable criteria (Reddit: 0 hashtags, 0 emoji in title; LinkedIn: hook before 210 chars; X: no links in main tweet) but these aren't formalized as test cases. **Fix:** Create `tests/` with 5+ input/expected-output pairs covering platform compliance checks. (+4-6 points)

3. **No EXPERT.md or attribution** — With the expanded sourcing (sources.md for all 6 platforms), the raw data is well-attributed, but there's no document explaining WHO created this skill pack, what experience backs the editorial decisions, or how the algorithm data was verified. **Fix:** Add EXPERT.md with author background, methodology, and how sources were selected. (+2-3 points)

---

## Recommendations

**To reach Tier 1 (Expert-Certified, ≥85):**

1. **GOTCHAS.md for each skill** — Extract existing inline gotchas + platform ref gotchas. Add 2-3 first-person failure narratives per skill. Format: "What happened → Why it happened → How to avoid it." (+3-4 points)

2. **Quality test cases** — Minimum 5 tests:
   - Test: LinkedIn post with external link in body → content-review should flag it
   - Test: Reddit post with hashtags and emoji → should flag and remove
   - Test: X post over 280 chars (non-Premium) → should flag
   - Test: omni-viral-humanizer given generic AI draft → ai-tell score should improve
   - Test: Instagram post with 8 hashtags → should reduce to 5
   (+4-6 points)

3. **EXPERT.md** — Author, methodology, source verification process. (+2-3 points)

4. **Viral examples for Instagram, YouTube, Reddit** — omni-viral-humanizer has viral-examples.txt for X, LinkedIn, TikTok but not the other three platforms. (+1-2 points on Completeness)

**Total potential: 79 → 89-94 with these changes.**

---

## Score Comparison: v1 vs v2

| Dimension | v1 Score | v2 Score | Change | What Improved |
|-----------|----------|----------|--------|---------------|
| Specificity | 21/25 | 23/25 | +2 | 2,034 concrete items (was 822). Named sources doubled. All platforms have dated, sourced algo data |
| Expertise Authenticity | 18/25 | 20/25 | +2 | 110 non-obvious insight refs (was ~30). 6 platform gotchas sections. Named executive sources |
| Actionability | 17/20 | 17/20 | — | No change (process structure unchanged) |
| Completeness | 11/15 | 13/15 | +2 | All 6 platforms fully covered (was 3 strong + 3 thin). Algo deep dives 6/6. Sources 6/6 |
| Testability | 5/15 | 6/15 | +1 | Platform refs implicitly define testable criteria (Reddit: 0 hashtags, etc.) |
| **Total** | **72/100** | **79/100** | **+7** | |

## Comparison to Tier 1 Benchmarks

| Dimension | social-skills v2 | gstack | superpowers | pm-skills |
|-----------|-----------------|--------|-------------|-----------|
| Reference depth | **114KB, 22 files, all sourced** | Moderate | Moderate | Deep (named frameworks) |
| Process enforcement | `<HARD-GATE>` 7/10 | Role routing | Mandatory pipeline | Three-layer hierarchy |
| Evidence quality | **🟢/🟡/🔴 ratings on every claim** | None | None | None |
| GOTCHAS.md | ❌ (inline only) | ✅ | ✅ | ✅ |
| Test cases | Structural only | Quality validation | Quality validation | Framework validation |
| Non-obvious insights | **110 references** | High | High | High |

**Bottom line:** social-skills v2 has the deepest, most rigorously sourced reference content of any skill pack evaluated. Its evidence quality rating system (🟢/🟡/🔴) is unique — no other pack does this. The content is Tier 1. The structure needs GOTCHAS.md, EXPERT.md, and test cases to match.
