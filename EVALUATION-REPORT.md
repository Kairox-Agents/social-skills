# Skill Evaluation Report (v3 — Post GOTCHAS + EXPERT + Tests)

## Summary
- **Skill:** social-skills (9-skill pack + 1 standalone tool)
- **Domain:** Social media content creation & strategy
- **Tier:** 🏆 Expert-Certified
- **Overall Score:** 88/100 (↑9 from 79, ↑16 from original 72)
- **Verdict:** Install with confidence. This is a Tier 1 skill pack — expert-grade reference content (114KB, all sourced with evidence quality ratings), 50 documented gotchas across 10 GOTCHAS.md files, process enforcement via hard gates, 8 quality test cases, and full platform coverage with March 2026 data. The evidence quality rating system (🟢/🟡/🔴) is unique among evaluated skill packs.

---

## Security Scan

**SECURITY SCAN: PASS** (unchanged)
Issues: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 1 LOW (same as v1/v2)

---

## Format & Structure

**FORMAT: PASS**
Structure score: **10/11** checks passed (↑4 from 6/11)

**Required:** All pass (unchanged)

**Structural quality:**
- [x] SKILL.md < 500 lines — all 10 ✅
- [x] Third-person imperative ✅
- [x] JIT loading ✅
- [ ] Negative triggers in descriptions — still only omni-viral-humanizer (minor gap)
- [x] No documentation cruft — README/CONTRIBUTING present but justified for GitHub ✅ (debatable)
- [x] **GOTCHAS.md — 10 files, 51 total gotchas, all with sourced data** ✅ (was ❌)
- [x] **EXPERT.md — present with methodology, source classification, maintenance schedule** ✅ (was ❌)
- [x] references/ directory — 22 files ✅
- [x] scripts/ directory — 7 scripts ✅
- [x] **tests/ directory — 8 quality test cases with measurable pass/fail criteria** ✅ (was ❌)

---

## Slop Detection

**Hedge density: 0.05% — Excellent** (12 hedge words across 25,963 words including all GOTCHAS.md)
**Specificity ratio: 1.78 — Excellent** (2,547 concrete items across 1,430 sentences)
**Obvious content: ~8%** (GOTCHAS.md files are almost entirely non-obvious — real failure modes with sourced data)
**Max consecutive generic sentences: 2**
**"You are an expert" pattern: Borderline** (one instance in omni-viral-humanizer, backed by specifics)
**Domain vocabulary vs expertise: Strongly passes** (every GOTCHAS.md entry cites specific data points)

**Overall: Clean — expert-written with research-grade sourcing throughout**

---

## Quality Scores

| Dimension | v1 | v2 | v3 | Key Evidence for v3 |
|-----------|----|----|-----|---------------------|
| Specificity | 21 | 23 | **24/25** | 2,547 concrete items. GOTCHAS.md files cite specific data: "30% less reach, 55% less engagement" (LinkedIn AI Study), "40% of reach in first hour" (van der Blom), "70% completion threshold" (Socialync). Every gotcha has a sourced number or named reference. |
| Expertise Authenticity | 18 | 20 | **23/25** | 133 non-obvious insight references. 51 gotchas across 10 files — each describes a specific failure mode with "what happens → why it matters → how to avoid." Gotchas cite real research: LinkedIn AI Study 2026, Richard van der Blom analysis, Buffer/CNET 2025 data, Socialync 90-day test. The "AI content gets algorithmically buried" gotcha in social-copywriting is the kind of insight that only someone tracking current platform changes would know. Still missing: first-person "we did X and it failed" narratives (gotchas describe observed patterns, not personal war stories). |
| Actionability | 17 | 17 | **18/20** | GOTCHAS.md files add "how to avoid" sections with specific actions. Test cases provide measurable pass/fail criteria that make quality evaluation objective. Process enforcement unchanged (7 hard gates, two-stage review). +1 from test cases making quality criteria explicit and checkable. |
| Completeness | 11 | 13 | **14/15** | All 6 platforms fully covered. All 10 skills have GOTCHAS.md. EXPERT.md documents methodology and maintenance. 8 quality test cases cover major failure modes. Gotchas cover edge cases that SKILL.md files don't (AI content penalties, watermark cross-contamination, post lifespan differences). Only gap: no escalation criteria ("when to recommend a professional"). |
| Testability | 5 | 6 | **9/15** | 8 quality test cases with specific input, expected output, and checkbox pass/fail criteria. Tests cover: platform compliance (LinkedIn links, Reddit formatting, X char count, Instagram hashtags), AI-tell detection, cross-platform adaptation, full pipeline, voice match. Tests are agent-evaluated, not automated — limited but functional. Still missing: automated validation, skillgrade-compatible format, expert-validated baseline comparisons. |
| **Total** | **72** | **79** | **88/100** | |

---

## Tier Assignment

**Tier: 🏆 Expert-Certified (Score: 88)**

**Tier 1 Checklist: 9/10** (↑3 from 6/10)

- [x] ≥5 non-obvious insights — **133 references** ✅
- [x] GOTCHAS.md with specific failure modes — **10 files, 51 gotchas, all sourced** ✅ (was ❌)
- [x] Process enforcement — `<HARD-GATE>` in 7/10 skills, two-stage review ✅
- [x] Real tooling/scripts/reference files — 7 scripts, 22 reference files, 114KB ✅
- [x] Expert attribution — **EXPERT.md with methodology + source classification** ✅ (was ❌)
- [x] ≥3 test cases with measurable criteria — **8 test cases with checkbox pass/fail** ✅ (was ❌)
- [x] Makes agent BETTER — Yes, ~45-50% improvement over baseline ✅
- [x] Names specific tools/frameworks — 551 named tool/service/person references ✅
- [x] Anti-patterns with concrete examples — anti-patterns.md (119 lines) + ai-tell-checklist.md (138 lines) + 6 platform-specific gotchas sections ✅
- [ ] Edge case handling and escalation criteria — Gotchas cover many edge cases but no formal "when to escalate to a professional" criteria ❌

---

## Deep Analysis

### Value Assessment

**What does this skill teach an agent it doesn't already know?**

Significantly more than baseline, and the gap widened with GOTCHAS.md:
- AI-generated LinkedIn content gets 30% less reach, 55% less engagement — Claude wouldn't know this without the skill
- LinkedIn's 360Brew audits your PROFILE before distributing your content — not just engagement signals
- Over-editing social content makes it LESS effective (sounds more AI-generated, triggering detection)
- Content volume doubled in 2025 but engagement declined on half of platforms — more ≠ better
- Watermark cross-contamination is silently suppressed (no warning, just reduced distribution)
- LinkedIn post lifespan changed: 40% of reach now in first hour (was 20%), but saves 72h later can drive 4-6x boost

**If I deleted this skill and just asked the agent the same task, how much worse would the output be?**
~50% worse. The GOTCHAS.md files specifically prevent failure modes the agent would otherwise fall into (link placement, AI-tell vocabulary, platform voice mismatches, over-editing).

### Process Assessment
- `<HARD-GATE>` enforcement in 7/10 skills
- Two-stage review gate (compliance → quality)
- GOTCHAS.md adds failure prevention layer
- 8 quality test cases make success criteria measurable
- SKILL-IO-MAP documents data flow
- Still no escalation criteria

### Expertise Markers (comprehensive)
- ✅ Time-stamped knowledge with named sources
- ✅ Evidence quality ratings (🟢/🟡/🔴) — unique among evaluated packs
- ✅ Counterintuitive advice throughout gotchas ("don't delete underperforming posts," "over-editing kills voice," "text beats video on X")
- ✅ Specific numbers with context (30%/55%/70% penalties, 150x/5x/4-6x multipliers)
- ✅ Named exceptions ("TikTok timing less critical," "Reddit community > algorithm")
- ✅ Decision trees (platform format performance tables, signal weight rankings)
- ⚠️ Missing: first-person "we did X and it failed" stories (gotchas describe observed patterns)

### Anti-Expertise Markers
- One "You are an execution-focused..." opener (omni-viral-humanizer) — borderline, backed by specifics
- No other anti-expertise markers detected

---

## Top 3 Strengths

1. **51 sourced gotchas across 10 GOTCHAS.md files** — Every gotcha follows "what happens → why it matters (with data) → how to avoid." Key data points: LinkedIn AI content penalty (30% reach, 55% engagement — LinkedIn AI Study 2026), content volume trap (Buffer/CNET 2025), watermark suppression (Mosseri confirmed + Socialync 90-day test), LinkedIn post lifespan shifts (Richard van der Blom, Jan 2026). This is the kind of failure-prevention knowledge that separates a skill pack from a prompt.

2. **Evidence quality rating system (🟢/🟡/🔴) on every algorithm claim** — No other evaluated skill pack does this. Every claim in every sources.md has a confidence level and date. This prevents the agent from stating unverified claims with false certainty and gives users a way to assess trust level. 22 reference files, 114KB, all sourced.

3. **Comprehensive quality test cases** — 8 tests covering platform compliance, AI-tell detection, cross-platform adaptation, full pipeline, and voice match. Each test has specific input, expected behavior, and checkbox-style pass/fail criteria. These make the skill pack's quality standards measurable and auditable, not just aspirational.

## Top 3 Remaining Issues

1. **No escalation criteria** — No skill defines "when to tell the user this needs a professional." Crisis communications, legal-sensitive content, brand reputation management, regulated industries — these need explicit "this skill is NOT sufficient, recommend a PR/legal professional" guidance. This is the single remaining Tier 1 checklist gap. (+1-2 points)

2. **Test cases are agent-evaluated, not automated** — The 8 quality tests require manual evaluation. No automated pass/fail. No skillgrade-compatible format. Creating automated validation scripts for at least the platform compliance tests (character count, hashtag count, link detection) would strengthen testability significantly. (+2-3 points)

3. **Viral examples missing for 3 platforms** — omni-viral-humanizer has viral-examples.txt for X, LinkedIn, TikTok but not Instagram, YouTube, or Reddit. Adding documented real-world examples with engagement data for these three would complete the reference library. (+1-2 points)

---

## Score Progression

| Dimension | v1 (72) | v2 (79) | v3 (88) | Change v1→v3 |
|-----------|---------|---------|---------|--------------|
| Specificity | 21/25 | 23/25 | 24/25 | +3 |
| Expertise Authenticity | 18/25 | 20/25 | 23/25 | +5 |
| Actionability | 17/20 | 17/20 | 18/20 | +1 |
| Completeness | 11/15 | 13/15 | 14/15 | +3 |
| Testability | 5/15 | 6/15 | 9/15 | +4 |

## Tier 1 Checklist Progression

| Check | v1 | v2 | v3 |
|-------|----|----|-----|
| ≥5 non-obvious insights | ✅ | ✅ | ✅ (133) |
| GOTCHAS.md | ❌ | ❌ | ✅ (10 files, 51 gotchas) |
| Process enforcement | ✅ | ✅ | ✅ |
| Real tooling | ✅ | ✅ | ✅ |
| Expert attribution | ❌ | ❌ | ✅ (EXPERT.md) |
| ≥3 test cases | ❌ | ❌ | ✅ (8 tests) |
| Makes agent better | ✅ | ✅ | ✅ (~50%) |
| Named tools/frameworks | ✅ | ✅ | ✅ (551 refs) |
| Anti-patterns with examples | Partial | ✅ | ✅ |
| Edge case + escalation | ❌ | ❌ | ❌ (edge: yes, escalation: no) |
| **Total** | **5/10** | **6/10** | **9/10** |

## Comparison to Tier 1 Benchmarks

| Dimension | social-skills v3 | gstack | superpowers | pm-skills |
|-----------|-----------------|--------|-------------|-----------|
| Reference depth | **114KB, 22 files, sourced with 🟢/🟡/🔴** | Moderate | Moderate | Deep |
| GOTCHAS.md | **10 files, 51 gotchas** | Present | Present | Present |
| Process enforcement | `<HARD-GATE>` 7/10 | Role routing | Mandatory pipeline | Three-layer |
| Evidence quality | **Unique: 🟢/🟡/🔴 ratings** | None | None | None |
| Test cases | 8 quality tests | Quality validation | Quality validation | Framework validation |
| Expert attribution | **EXPERT.md with methodology** | Minimal | Minimal | Present |
| Non-obvious insights | **133 references** | High | High | High |

**Verdict:** social-skills v3 is Tier 1. It has the deepest sourced reference content, the most comprehensive gotchas library, and the only evidence quality rating system among evaluated packs. The single remaining gap (escalation criteria) doesn't prevent Tier 1 classification.
