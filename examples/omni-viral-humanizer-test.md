# Omni Viral Humanizer Test

> Input a raw draft → get humanized + optimized output for X, LinkedIn, TikTok.

## Test Input

**Raw draft:**
```
Most startups fail at content marketing because they copy what big companies do. Big companies have brand awareness, distribution channels, and dedicated content teams. Startups have none of that. So when a startup copies HubSpot's content strategy, they're playing a game they can't win. Instead, startups should focus on what they DO have: the founder's authentic voice, speed of execution, and willingness to share real numbers.
```

**User instruction:**
```
Humanize this and optimize for X, LinkedIn, and TikTok. My audience is startup founders.
```

## Expected Behavior

1. Agent loads `omni-viral-humanizer/SKILL.md`
2. Loads `references/humanization/ai-tell-checklist.md`
3. Loads algo deep-dives + viral examples for X, LinkedIn, TikTok
4. Runs humanization pass first
5. Creates platform-specific variants
6. Returns JSON + Markdown

## Expected JSON Output (Structure)

```json
{
  "input": {
    "platform_request": "x, linkedin, tiktok",
    "topic": "Why startups shouldn't copy big company content strategy",
    "audience": "Startup founders"
  },
  "humanization_report": {
    "issues_found": [
      "No personal details or specific examples",
      "Reads like a blog paragraph, not social content",
      "'distribution channels' is corporate-speak"
    ],
    "fixes_applied": [
      "Added specific company example (HubSpot → concrete reference)",
      "Shortened sentences, added fragments",
      "Replaced 'distribution channels' with 'built-in audience'",
      "Added opinion/personality"
    ],
    "ai_tell_score_before": "5/10",
    "ai_tell_score_after": "2/10"
  },
  "humanized_base": "...",
  "platform_outputs": {
    "x": {
      "variants": [
        {
          "type": "single",
          "text": "Startups copying HubSpot's content strategy is like a garage band copying Taylor Swift's tour plan.\n\nYou don't have the audience, the team, or the budget.\n\nWhat you DO have: a founder who can be real. That's your unfair advantage. Use it."
        },
        {
          "type": "thread",
          "tweets": [
            "Most startups fail at content marketing. Not because they're bad at it — because they're copying the wrong playbook.",
            "Big companies like HubSpot have: ↳ millions in brand awareness ↳ 50-person content teams ↳ built-in distribution from day 1",
            "Startups have: ↳ a founder ↳ a laptop ↳ real stories nobody else can tell",
            "When you copy a big company's strategy with a startup's resources, you lose. Every time.",
            "What actually works for startups: 1. Founder's voice (not brand voice) 2. Real numbers (not case studies) 3. Speed (publish in hours, not weeks)",
            "The founder who shares their real revenue journey will outperform a $200K content budget.\n\nBecause authenticity is the one thing money can't buy.\n\nWhat's your unfair content advantage? Reply below."
          ]
        }
      ],
      "analysis": {
        "hook_strength": "strong",
        "engagement_score": "8.2/10",
        "score_breakdown": {
          "hook_quality": "8/10 (weight: 30%)",
          "platform_fit": "9/10 (weight: 25%)",
          "interaction_potential": "8/10 (weight: 25%)",
          "clarity_specificity": "8/10 (weight: 20%)"
        },
        "signals_hit": ["reply potential", "contrarian framing", "no external link"],
        "platform_specific_warnings": [],
        "recommended_window": "Tue-Thu 08:30-10:00 local",
        "media_prompt": "None needed — text-native format",
        "a_b_test_suggestion": "Test single tweet vs thread — single may outperform if the 'garage band' analogy is strong enough alone",
        "notes": "Final thread tweet drives replies with a direct question"
      }
    },
    "linkedin": {
      "variants": [
        {
          "type": "text-post",
          "text": "I spent 6 months copying HubSpot's content strategy.\n\nBlog posts. SEO playbooks. Gated ebooks.\n\nResult? 47 blog posts. 200 total visitors. Zero customers.\n\nHere's what I learned:\n\nBig companies play a different game. They have brand awareness, dedicated teams, and distribution baked into their name. When HubSpot publishes a blog post, 100K people see it because they're HubSpot.\n\nWhen a startup publishes the same blog post, 12 people see it. And 8 of them are your mom's friends.\n\nWhat actually works for startups:\n\n→ The founder's real voice (not a brand guidelines doc)\n→ Actual numbers (our MRR, our churn, our mistakes)\n→ Speed — publish today, not after 3 rounds of approval\n\nThe startups winning at content right now aren't out-producing big companies. They're out-authenticating them.\n\nYour unfair advantage isn't budget. It's that you can be real.\n\nWhat's one piece of content you created that felt genuinely YOU? Drop it below.\n\n#startups #contentmarketing #founders"
        }
      ],
      "analysis": {
        "hook_strength": "strong",
        "engagement_score": "8.5/10",
        "score_breakdown": {
          "hook_quality": "9/10 (weight: 30%)",
          "platform_fit": "8/10 (weight: 25%)",
          "interaction_potential": "9/10 (weight: 25%)",
          "clarity_specificity": "8/10 (weight: 20%)"
        },
        "signals_hit": ["dwell-time story", "see-more hook", "comment prompt", "save-worthy framework"],
        "platform_specific_warnings": [],
        "recommended_window": "Tue-Thu 08:00-11:00 local",
        "media_prompt": "Optional: screenshot of analytics showing the 47-post/200-visitor result",
        "a_b_test_suggestion": "Test opening with the HubSpot copy story vs opening with 'The startups winning at content right now aren't out-producing big companies'",
        "notes": "Personal failure story → lesson → actionable framework → question CTA"
      }
    },
    "tiktok": {
      "variants": [
        {
          "type": "short-video-script",
          "duration_target": "55-65s",
          "script": [
            "[HOOK - 3s] I copied HubSpot's content strategy for 6 months. Here's what happened.",
            "[BEAT 1 - 15s] I did everything they say to do. Blog posts, SEO, gated content. 47 pieces of content later? 200 visitors. Zero customers.",
            "[BEAT 2 - 20s] Here's the thing nobody tells you. Big companies aren't winning because of their content strategy. They're winning because they're already famous. When HubSpot hits publish, 100K people see it. When you hit publish? Your mom. Maybe.",
            "[BEAT 3 - 15s] What actually works for startups? Three things. Your real voice — not some brand guidelines doc. Real numbers — show your revenue, your failures. And speed — stop waiting for approval from nobody.",
            "[CTA - 5s] What's the one piece of content you made that felt genuinely you? Tell me in the comments."
          ],
          "caption": "stop copying hubspot's content strategy 💀 it's not built for you #startup #contentmarketing #founders #buildinpublic"
        }
      ],
      "analysis": {
        "hook_strength": "strong",
        "engagement_score": "8.0/10",
        "score_breakdown": {
          "hook_quality": "8/10 (weight: 30%)",
          "platform_fit": "8/10 (weight: 25%)",
          "interaction_potential": "8/10 (weight: 25%)",
          "clarity_specificity": "8/10 (weight: 20%)"
        },
        "signals_hit": ["3s hook", "story structure", "completion-friendly pacing", "comment CTA mid-appropriate"],
        "platform_specific_warnings": ["Consider adding a visual element (screen recording, whiteboard) to boost retention"],
        "recommended_window": "Tue-Thu 16:00-20:00 local",
        "media_prompt": "Talking head with jump cuts. Consider green-screening a HubSpot blog post in the background for beat 1.",
        "a_b_test_suggestion": "Test POV format ('POV: you just copied a big company content strategy') vs direct storytelling",
        "notes": "Script written in spoken language. Casual tone matches TikTok. CTA placed at end but could also work spoken at beat 3."
      }
    }
  },
  "cross_posting_notes": [
    "Core argument consistent: startups should leverage authenticity, not copy enterprise playbooks",
    "X: compressed to single insight or expanded to structured thread. No story framing.",
    "LinkedIn: full story arc with personal failure → lesson → framework. Longer form.",
    "TikTok: spoken-language rewrite with visual hooks. Story structure but faster pacing.",
    "Test: which platform responds best to the 'I copied HubSpot' personal failure angle vs the abstract argument"
  ]
}
```

## Pass Criteria

### Humanization
- [ ] AI-tell report identifies at least 2 issues in the original
- [ ] "distribution channels" flagged and replaced
- [ ] AI-tell score decreases after humanization
- [ ] Humanized base has personal voice added

### Platform Differentiation
- [ ] X version is SHORT — single tweet ≤280 chars or thread with punchy tweets
- [ ] LinkedIn version is STORY-DRIVEN — personal narrative with "see more" hook
- [ ] TikTok version is SPOKEN — reads naturally when said aloud
- [ ] All three are genuinely different — not resized versions of the same text

### Platform Rules
- [ ] X: 0-1 hashtags, no external link, reply-driving CTA
- [ ] LinkedIn: hook before 210 chars, 2-3 hashtags at end, comment-driving CTA
- [ ] TikTok: hook in first 3 seconds, lowercase casual caption, 3-5 hashtags

### Quality
- [ ] No AI-tell vocabulary in any output
- [ ] Specific examples present (HubSpot, real numbers)
- [ ] Each variant has a clear CTA targeting the platform's key signal
- [ ] A/B test suggestions are actionable and platform-aware
- [ ] Engagement scores include breakdown and are defensible
