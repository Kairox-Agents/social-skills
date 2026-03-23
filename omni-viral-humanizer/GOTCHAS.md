# Gotchas — Omni Viral Humanizer

## 1. Humanization Is a Distribution Requirement, Not Optional Polish

**What happens:** User says "just optimize it for LinkedIn, skip the humanization step." Agent produces a well-structured, algorithm-aware post that sounds AI-generated. LinkedIn's 360Brew buries it.

**The data:** LinkedIn AI-generated content: 30% less reach, 55% less engagement. AI-generated images: 70% fewer clicks. 54% of LinkedIn posts are now AI-generated, making AI patterns easier to detect. (Source: LinkedIn AI Study 2026, Feb 2026)

Instagram CEO Mosseri's end-of-2025 message: "AI tools can now generate highly polished images and videos instantly. The content that stands out is often more human and less manufactured."

Buffer 2025 data: Content volume doubled across most platforms. Engagement declined on half. The flood of AI content made human-sounding content more valuable, not less.

**How to avoid:** The humanization step (ai-tell-checklist.md) runs BEFORE platform optimization. It's not a nice-to-have — it's the first gate. Skip it and everything downstream underperforms.

## 2. Over-Optimizing for One Signal

**What happens:** Agent optimizes a LinkedIn post entirely for saves (because saves = 5x reach). The post becomes a reference-heavy list with no personality. It gets saved but no comments — and comment depth is also a strong signal.

**Why it matters:** Platform scoring has multiple signals. Optimizing for one at the expense of others produces unbalanced content. The scoring model weights four dimensions for a reason: hook (30%), platform-fit (25%), interaction (25%), clarity (20%).

**How to avoid:** Check all four scoring dimensions before finalizing. A post that scores 9/10 on platform-fit but 3/10 on interaction potential isn't optimized — it's lopsided.

## 3. The "All Platforms" Trap

**What happens:** User says "optimize for all platforms." Agent produces 6 platform variants. User posts all 6 the same day. The three weakest variants dilute the brand's perceived quality.

**Why it matters:** Not every idea works on every platform. A detailed analysis post might be excellent for LinkedIn and Reddit but terrible for TikTok. Forcing it into all 6 platforms produces 3 strong variants and 3 mediocre ones.

**How to avoid:** When scoring reveals a variant below 6.0/10, flag it and recommend not posting it rather than forcing a weak adaptation. It's better to post on 3 platforms well than 6 platforms poorly.

## 4. Fabricated Engagement Predictions

**What happens:** Agent assigns confident engagement scores (8.5/10) without being honest about uncertainty. The scoring model is a quality heuristic, not a crystal ball.

**Why it matters:** Users may make posting decisions based on scores. If the score says 8.5/10 and the post gets 10% of expected engagement, trust in the tool drops permanently.

**How to avoid:** Hard Rule #3 exists for this reason: "No fake certainty." Scores are quality assessments against known algorithm signals, not engagement predictions. Below 7.0 = needs improvement. Above 8.0 = well-optimized for known signals. Not "will go viral."

## 5. Viral Examples Become Templates

**What happens:** Agent reads viral-examples.txt and produces content that mirrors the examples too closely. The output sounds like a pattern-matched remix of existing viral posts rather than original content.

**Why it matters:** Viral examples illustrate WHY certain patterns work (algorithm signals hit, audience psychology triggered). They're not templates to fill in. A post that sounds like a remix of 3 viral posts reads as formulaic — which is itself an AI-tell.

**How to avoid:** Extract the PRINCIPLE from viral examples ("vulnerability + specific numbers = engagement"), not the STRUCTURE ("I was [bad state]. Now I [good state]. Here's how:"). Apply the principle with the user's own voice and story.
