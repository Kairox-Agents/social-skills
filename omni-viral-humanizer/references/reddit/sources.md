# Reddit Algorithm Sources

| Claim | Source | Evidence Quality | Date |
|-------|--------|-----------------|------|
| "Best" sort uses ML, expanded late 2025/early 2026 | Reddit official (AutoMod responses in r/help) | 🟢 High (official) | Jan 2026 |
| Best sort now recommends from unsubscribed subreddits | Reddit official + r/help community reports | 🟢 High (official + widespread user reports) | Jan 2026 |
| Upvote velocity > total upvotes | Reddit open-source Hot algorithm code | 🟢 High (source code, historically open) | Ongoing |
| Time decay is aggressive for Hot sort | Reddit open-source ranking code | 🟢 High (source code) | Ongoing |
| First hour velocity determines rising→hot transition | r/TheoryOfReddit analysis + community consensus | 🟡 Medium (community analysis + observable) | Ongoing |
| Comment activity boosts post ranking | Reddit ranking documentation + r/TheoryOfReddit | 🟡 Medium (documented behavior) | Ongoing |
| OP participation boosts post | Community analysis + observable behavior | 🔴 Low (anecdotal but widely reported) | Ongoing |
| 2-3 hour rising window | r/TheoryOfReddit + community analysis | 🟡 Medium (observable pattern) | Ongoing |
| Karma/account age thresholds per subreddit | Subreddit AutoModerator configurations (public) | 🟢 High (visible in subreddit rules) | Ongoing |
| No hashtags, no engagement pods, no follower-based distribution | Reddit platform design (observable) | 🟢 High (platform design) | Ongoing |

## Important Notes on Reddit Sources

Reddit's algorithm is less documented than X (open-source), LinkedIn (360Brew research), or Instagram/TikTok (exec statements). Key differences:

1. **Reddit's Hot algorithm was historically open-source** — the basic ranking formula is known
2. **The "Best" sort is ML-powered and opaque** — Reddit doesn't publish its ML model details
3. **Much of what we know comes from community analysis** on r/TheoryOfReddit and observable behavior
4. **Reddit's algorithm matters less than community behavior** — moderators and community norms have more impact on content success than any algorithm

## Primary Sources
- Reddit Help Center: https://support.reddithelp.com/
- r/TheoryOfReddit: Community analysis of Reddit mechanics
- r/help: Official Reddit support + AutoMod responses about algorithm changes
- Reddit Engineering Blog: https://www.redditinc.com/blog (infrequent algorithm details)
- Adweek: Reddit Best sort ML announcement (2021, still relevant architecture)
