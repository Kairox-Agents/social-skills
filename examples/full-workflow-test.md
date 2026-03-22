# Full Workflow Test — End-to-End Pipeline

> Tests the complete content pipeline: context → ideation → writing → review → calendar → repurposing.

## Test Scenario

**Fictional brand:** Acme PM — a lightweight B2B project management SaaS for startup founders.
**Audience:** Startup founders, small team leads (5-20 people), bootstrapped preferred.
**Platforms:** X, LinkedIn, Instagram.
**Voice:** Direct, slightly irreverent, anti-enterprise, builder mentality.

---

## Step 1: Social Context Setup

**User input:**
```
Set up my social profiles. I'm building Acme PM, a simple project management tool for startups.
Target audience: startup founders and small team leads, mostly bootstrapped.
Platforms: X, LinkedIn, Instagram.
Voice: direct, builder mentality, anti-enterprise complexity. Think "engineer who explains things clearly" not "marketing department."
```

**Expected:** `social-context` creates config.json with all fields populated.

**Pass/fail criteria:**
- [ ] Config includes all 3 platforms
- [ ] Voice captures "anti-enterprise" and "builder mentality"
- [ ] Audience pain points inferred (tool overload, shipping speed, simplicity)

---

## Step 2: Generate 10 Ideas with Content Ideation

**User input:**
```
Give me 10 content ideas for this week across X, LinkedIn, and Instagram.
```

**Expected:** `content-ideation` generates ideas using frameworks from `ideation-frameworks.md`.

**Pass/fail criteria:**
- [ ] 10 distinct ideas returned
- [ ] Mix of pillars (educational, personal, opinion, behind-the-scenes)
- [ ] Each idea tagged with suggested platform and format
- [ ] No generic ideas ("5 tips for productivity") — all should have a specific angle
- [ ] At least 2 ideas leverage the contrarian/anti-enterprise voice

---

## Step 3: Write 3 Posts (X + LinkedIn + Instagram)

**User input (post 1):**
```
Write an X thread about why Gantt charts are the enemy of shipping fast.
```

**User input (post 2):**
```
Write a LinkedIn post about the moment I realized our product had too many features.
```

**User input (post 3):**
```
Write an Instagram carousel about "3 signs your PM tool is slowing you down."
```

**Expected:** `social-copywriting` generates platform-native content for each.

**Pass/fail criteria — X thread:**
- [ ] 4-8 tweets, each self-contained
- [ ] First tweet is a strong hook
- [ ] 0-1 hashtags total
- [ ] CTA in final tweet drives replies
- [ ] Anti-enterprise voice present

**Pass/fail criteria — LinkedIn post:**
- [ ] Hook in first 210 chars
- [ ] Personal story format (not listicle)
- [ ] Line breaks, short paragraphs
- [ ] 2-3 hashtags at end
- [ ] Comment-driving CTA

**Pass/fail criteria — Instagram carousel:**
- [ ] 5-8 slides outlined
- [ ] Each slide: 1 point, 10-20 words max
- [ ] Slide 1 = visual hook
- [ ] Final slide = CTA + handle
- [ ] Caption included with hashtags

---

## Step 4: Review All 3 Posts

**User input:**
```
Review all 3 posts before I publish them.
```

**Expected:** `content-review` runs two-stage review on each post.

**Pass/fail criteria:**
- [ ] Each post reviewed independently
- [ ] AI-tell check performed on each
- [ ] Platform-specific compliance verified
- [ ] Hook strength rated
- [ ] Specific improvement suggestions (not just "looks good!")
- [ ] Voice consistency checked against social-context config

---

## Step 5: Generate 2-Week Content Calendar

**User input:**
```
Generate a 2-week content calendar. X: 5 posts/week. LinkedIn: 3/week. Instagram: 3/week.
Pillars: educational, personal, opinion.
```

**Expected:** `content-calendar` (or `generate-calendar.py`) produces calendar.

**Verification command:**
```bash
python3 scripts/generate-calendar.py --weeks 2 --platforms "x-twitter,linkedin,instagram" --pillars "educational,personal,opinion" --frequency "5,3,3"
```

**Pass/fail criteria:**
- [ ] 22 entries total (5+3+3 × 2 weeks)
- [ ] Markdown + JSON output generated
- [ ] Entries spread across weekdays (not all on Monday)
- [ ] Pillar distribution roughly 40/25/20 for edu/personal/opinion
- [ ] Each entry has: date, time, platform, format, pillar, topic placeholder

---

## Step 6: Repurpose a Blog Post

**User input:**
```
Repurpose this blog post into X thread, LinkedIn post, and Instagram carousel:

"Why We Removed 60% of Our Features

Last quarter, we made the scariest decision in Acme PM's history: we removed 60% of our features.

Not deprecated. Not hidden behind settings. Removed.

Here's why: we tracked feature usage across 500 accounts. The results were brutal. 12 features accounted for 94% of daily usage. The other 31 features? Used by fewer than 3% of users, but responsible for 70% of our support tickets.

We spent 6 weeks removing features, migrating data, and personally emailing every affected user. We lost 8% of our customers. We gained 40% faster load times, 60% fewer support tickets, and our NPS went from 32 to 67.

The lesson: your product isn't what you build. It's what you keep."
```

**Expected:** `content-repurposing` generates 3 platform-native adaptations using `repurposing-matrix.md`.

**Pass/fail criteria:**
- [ ] X thread: 5-8 tweets, data points highlighted, hook tweet is compelling
- [ ] LinkedIn post: story-driven, personal voice, "see more" hook
- [ ] Instagram carousel: 5-8 slides, one insight per slide, visual direction
- [ ] All three are genuinely different — not just reformatted versions of the same text
- [ ] Each adaptation follows its platform's specific rules
- [ ] Blog-specific details (60%, 500 accounts, NPS scores) preserved where impactful
