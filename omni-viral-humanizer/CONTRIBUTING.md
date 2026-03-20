# Contributing

## Principles

1. Keep `SKILL.md` concise and procedural.
2. Put platform-specific details in `references/<platform>/`.
3. Prefer verifiable claims; mark uncertain claims as estimates.
4. Avoid hype-only "growth hacks".
5. Preserve strict JSON output contract.

## Updating references

- Update quarterly or when major platform updates land.
- Add source notes inline in reference files.
- Keep examples realistic and clearly labeled as observed/synthetic.

## Release checklist

- [ ] Run `python3 test.py`
- [ ] Validate frontmatter fields in `SKILL.md`
- [ ] Confirm output schema still matches examples
- [ ] Update CHANGELOG
