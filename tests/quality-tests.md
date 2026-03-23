# Quality Test Cases

These test cases validate output QUALITY, not just structure. Each test has a specific input, expected behavior, and measurable pass/fail criteria.

---

## Test 1: LinkedIn Link Placement

**Skill under test:** content-review (Stage 1)
**Input:**
```
Platform: LinkedIn
Post: "We just shipped async standups. Here's why it matters for remote teams: https://flowpm.io/async-standups

Your morning standup doesn't need to be a meeting. It needs to be a message.

What's your standup process? #remotework #saas #startups"
```

**Expected:** Stage 1 FAIL — link in post body flagged
**Pass criteria:**
- [ ] Flags external link in post body
- [ ] Recommends moving link to first comment
- [ ] Does NOT pass to Stage 2 until link is moved

---

## Test 2: Reddit Platform Compliance

**Skill under test:** content-review (Stage 1)
**Input:**
```
Platform: Reddit (r/startups)
Title: 🚀 Check out FlowPM — We're Revolutionizing Project Management! 💪
Body: "Hey #startups community! We're excited to share our latest product update. FlowPM is the #1 project management tool for small teams. #saas #buildinpublic"
```

**Expected:** Stage 1 FAIL — multiple violations
**Pass criteria:**
- [ ] Flags emoji in title (🚀 💪)
- [ ] Flags hashtags in body (#startups, #saas, #buildinpublic)
- [ ] Flags promotional language ("Check out," "We're excited to share," "#1")
- [ ] Flags marketing voice
- [ ] Recommends complete rewrite with Reddit-native tone

---

## Test 3: X Character Count (Non-Premium)

**Skill under test:** content-review (Stage 1)
**Input:**
```
Platform: X (non-Premium account)
Post: "The best project management tool isn't a tool at all — it's a shared understanding of what matters most this week, communicated clearly to every person on the team, reinforced daily through brief check-ins that respect everyone's time and attention. That's it. That's the whole framework."
```

**Expected:** Stage 1 FAIL — over 280 characters
**Pass criteria:**
- [ ] Counts characters correctly (this is 293 chars)
- [ ] Flags as over the 280 character limit
- [ ] Suggests trimming or splitting into thread

---

## Test 4: AI-Tell Detection

**Skill under test:** social-copywriting (humanization step) or omni-viral-humanizer
**Input:**
```
"In today's fast-paced digital landscape, it's important to leverage cutting-edge tools that unlock your team's full potential. Navigate the complexities of project management with our comprehensive, robust platform that fosters seamless collaboration and drives groundbreaking results."
```

**Expected:** Flagged as heavily AI-generated
**Pass criteria:**
- [ ] Identifies ≥5 AI-tell vocabulary words ("landscape," "leverage," "cutting-edge," "unlock," "navigate," "complexities," "comprehensive," "robust," "fosters," "seamless," "groundbreaking")
- [ ] AI-tell score ≥ 7/10 (heavily AI)
- [ ] Provides specific human alternatives for each flagged word
- [ ] Rewritten version contains 0 AI-tell vocabulary words
- [ ] Rewritten version includes specific details (not vague abstractions)

---

## Test 5: Instagram Hashtag Limit

**Skill under test:** content-review (Stage 1)
**Input:**
```
Platform: Instagram
Caption: "3 signs your PM tool is slowing you down 👇

1. You spend more time updating the tool than doing the work
2. Your team has 'workarounds' for basic things  
3. Nobody opens it unless someone's watching

#projectmanagement #startup #saas #productivity #buildinpublic #tech #remotework #founder #smallbusiness #growth"
```

**Expected:** Stage 1 FAIL — too many hashtags
**Pass criteria:**
- [ ] Counts 10 hashtags
- [ ] Flags as exceeding the 5-hashtag limit (2026 Instagram rule)
- [ ] Recommends keeping the 5 most relevant hashtags
- [ ] Does NOT recommend 30 hashtags (outdated advice)

---

## Test 6: Cross-Platform Adaptation

**Skill under test:** social-copywriting (multi-platform) or content-repurposing
**Input:**
```
Source: LinkedIn post about bootstrapping to $42K MRR
Target platforms: X, Reddit, Instagram
```

**Expected:** Three completely different versions
**Pass criteria:**
- [ ] X version: ≤280 chars (or thread), punchy tone, 0-1 hashtags, no link in main post
- [ ] Reddit version: 0 hashtags, 0 emoji in title, no promotional language, specific descriptive title, casual/genuine tone
- [ ] Instagram version: ≤5 hashtags, hook in first 125 chars, visual direction note
- [ ] No two versions share more than 30% identical text
- [ ] Each version uses platform-appropriate CTA (X: reply-driving, Reddit: discussion question, Instagram: save/send)

---

## Test 7: Omni-Viral-Humanizer Full Pipeline

**Skill under test:** omni-viral-humanizer
**Input:**
```
Topic: "Why most startups fail at content marketing"
Platform: all
```

**Expected:** Valid JSON output with all 6 platforms
**Pass criteria:**
- [ ] humanization_report present with issues_found and fixes_applied
- [ ] ai_tell_score_after < ai_tell_score_before (humanization improved it)
- [ ] platform_outputs contains entries for x, linkedin, tiktok, reddit, instagram, youtube
- [ ] Each platform output has engagement_score, score_breakdown with 4 weighted dimensions
- [ ] No two platform outputs share >30% identical text
- [ ] Reddit output has 0 hashtags, 0 emoji
- [ ] X output respects 280 char limit for singles
- [ ] LinkedIn output has hook before 210 chars
- [ ] TikTok output has script with hook in first 3 seconds
- [ ] YouTube output has title under 60 chars
- [ ] cross_posting_notes present and non-empty

---

## Test 8: Voice Match After Config

**Skill under test:** social-copywriting
**Input:**
```
Config: { voice: { tone: { formality: "casual", energy: "energetic", humor: "frequent" }, never_use: ["synergy", "leverage", "disruptive"], similar_to: "Sahil Lavingia" } }
Platform: X
Topic: "Why we killed 14 features"
```

**Expected:** Output matches configured voice
**Pass criteria:**
- [ ] Tone is casual (contractions, fragments, informal language)
- [ ] Energy is high (direct statements, not passive constructions)
- [ ] Humor present (at least one moment of levity or self-deprecation)
- [ ] Contains 0 words from never_use list
- [ ] Reads like it could be from Sahil Lavingia's feed (direct, opinionated, specific numbers)
- [ ] Does NOT read like a corporate press release

---

## How to Run These Tests

These are agent-evaluated tests, not automated scripts. To run:

1. Present the input to the skill being tested
2. Compare the output against the pass criteria checkboxes
3. All checkboxes must be checked for the test to pass
4. If a test fails, note which specific criteria failed

For automated structural validation, use `python3 scripts/test-all.py`.
