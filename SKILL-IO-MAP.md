# Skill I/O Map

How data flows between skills. Each skill declares what it reads and writes.

```
SKILL                  READS                                    WRITES
─────────────────────  ───────────────────────────────────────  ─────────────────────────────────
social-context         User interview answers                   config.json, brand-context.json
content-ideation       config.json, data/idea-bank.jsonl        data/idea-bank.jsonl
social-copywriting     config.json, platform refs, anti-pats    Content + data/content-log.jsonl
thread-writing         config.json, platform refs, anti-pats    Threads + data/content-log.jsonl
content-repurposing    config.json, platform refs, source URL   Multi-platform content + log
content-calendar       config.json, idea-bank, posting-strat    data/content-calendar.json + .md
posting-strategy       config.json                              Timing recommendations
content-review         config.json, platform refs, anti-pats    Review verdict + score
account-analysis       API data or pasted posts                 voice-profile/, competitive report
```

## Dependency Graph

```
                    ┌─────────────────┐
                    │  social-context  │ ← Foundation (HARD GATE)
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
   content-ideation    account-analysis    posting-strategy
          │                  │
          ▼                  │
   content-calendar          │
          │                  │
          ▼                  ▼
   ┌──────────────── CREATION ──────────────────┐
   │ social-copywriting                          │
   │ thread-writing                              │
   │ content-repurposing                         │
   └─────────────────┬──────────────────────────┘
                     ▼
              content-review ← Quality gate
                     │
                     ▼
                  PUBLISH
```
