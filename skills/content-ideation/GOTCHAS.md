# Gotchas — Content Ideation

## 1. Generic Ideas Are Worse Than No Ideas

**What happens:** Agent generates "10 post ideas" that could apply to any brand in any industry: "Share a tip," "Post a behind-the-scenes," "Ask your audience a question."

**Why it matters:** Generic ideas produce generic content, which gets buried by every platform's algorithm. The "Only I Can Say This" filter exists for a reason — if 10 competitors could post the same idea, it's not differentiated enough.

**How to avoid:** Every idea must pass two tests: (1) Does it connect to a specific content pillar or audience pain point from config.json? (2) Could only THIS brand/person post this with credibility? If either answer is no, discard and try again.

## 2. Trendjacking After the Window Closes

**What happens:** Agent suggests jumping on a trending topic that peaked 5 days ago. The content feels dated by the time it's created and posted.

**The data:** TikTok trends have a 24-48 hour peak window. X trends move even faster (hours). LinkedIn is more forgiving (3-5 days for business trends). Reddit has no trend mechanism — evergreen value beats timely.

**How to avoid:** Check if the trend is still active before suggesting it. For TikTok, if the trending sound is more than 48 hours old, it's likely too late. For X, if it's not in Explore anymore, it's over.

## 3. The "AI Slop Idea Factory"

**What happens:** Agent generates 20 ideas rapidly, all following the same template: "X lessons from Y," "How to Z in 2026," "The mistake most [audience] make with [topic]." The ideas look productive but are actually formulaic.

**The data:** Buffer's 2025 report found content volume doubled across platforms but engagement declined on half of them. The volume problem isn't solved by more ideas — it's solved by better ideas.

**How to avoid:** Generate ideas in small batches (5-7, not 20). Use different ideation frameworks for each batch. After generating, actively prune the weakest 30%. Quality of ideas matters more than quantity.

## 4. Ignoring What Already Worked

**What happens:** Agent ideates purely from frameworks and pain points without checking what the account's top-performing posts were about. Misses the patterns hiding in existing data.

**Why it matters:** The best predictor of future engagement is past engagement patterns. If data/number posts consistently outperform opinion posts for this account, generate more data-driven ideas.

**How to avoid:** Check `data/content-log.jsonl` (if it exists) before ideating. If account-analysis has been run, reference the top-performing content patterns. Build on what works, don't just generate from scratch.

## 5. Platform-Blind Ideation

**What happens:** Agent generates great ideas but doesn't consider which platform they'll work on. A deep analytical breakdown is perfect for LinkedIn/Reddit but wrong for TikTok. A visual tutorial idea is perfect for Instagram but useless as an X text post.

**How to avoid:** Always tag ideas with best-fit platform(s). Consider format before topic — if the user needs Instagram content, generate carousel-shaped and Reel-shaped ideas, not blog-shaped ideas.
