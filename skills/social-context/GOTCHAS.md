# Gotchas — Social Context

## 1. The "Quick Post" Bypass

**What happens:** User says "just write me a quick tweet" and the agent skips loading config.json. The resulting content sounds generic — no brand voice, no audience targeting, wrong tone.

**Why it matters:** Every post represents the brand. A casual tweet in corporate voice (or vice versa) is worse than no tweet at all. The `<HARD-GATE>` exists for this reason.

**How to avoid:** Never skip config.json loading, even for "quick" requests. If config.json doesn't exist yet, run the quick-start interview (5 questions, 2 minutes) before generating anything.

## 2. Platform Voice Variants Get Ignored

**What happens:** Agent loads brand voice but applies the same tone across all platforms. LinkedIn gets Twitter slang. Reddit gets promotional language. Instagram gets corporate copy.

**Why it matters:** Each platform has a different culture. What builds trust on LinkedIn (professional vulnerability) gets downvoted on Reddit (sounds like humble-bragging). What works on X (punchy fragments) feels shallow on LinkedIn.

**How to avoid:** Always check `voice.platform_variants` in config.json. If empty, prompt the user to define how their voice changes per platform.

## 3. The "Never Use" List Gets Stale

**What happens:** User sets up `never_use` words once and never updates them. Over time, the brand evolves but the banned words list doesn't, OR new AI-tell words emerge that aren't on the list.

**How to avoid:** Prompt for `never_use` review every 90 days. Cross-reference with ai-tell-checklist.md periodically.

## 4. Audience Assumptions vs. Reality

**What happens:** User describes their audience as "startup founders" but their actual engaged audience (based on analytics) is "marketing managers at mid-size companies." Content targeting mismatches tank engagement.

**Why it matters:** What you THINK your audience is and what analytics SHOW your audience is are often different. Building content for the wrong persona wastes effort.

**How to avoid:** When account-analysis data is available, compare it against config.json audience settings. Flag mismatches. Update config based on real engagement data, not assumptions.

## 5. Over-Configured Brand Voice

**What happens:** User goes through full brand audit and creates an extremely detailed voice config (15 personality adjectives, 50 banned words, 8 similar-to references). The agent then writes stilted content trying to satisfy every constraint simultaneously.

**Why it matters:** Too many constraints produce worse output than too few. The agent optimizes for constraint satisfaction instead of genuine quality.

**How to avoid:** Limit personality adjectives to 3-5. Keep `never_use` to high-impact words only. Use 1-2 `similar_to` references max. Simplicity > comprehensiveness.
