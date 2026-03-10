# Preset first-proof status examples

Copy-ready short status lines for maintainers who want to report the first believable proof after `oss-launchpad init`.

## Why this exists

The generated scaffold prints proof commands and review commands, but maintainers still need a concise way to describe what changed without overselling maturity.

## Pattern

```text
<preset>: <visible proof asset> updated, <check asset> passed, first public proof is now believable.
```

## Examples

- `ai-agent: prompts/system.txt updated, eval smoke JSON validated, first public proof is now believable.`
- `web-app: landing-page brief updated, demo shell flow reviewed, first public proof is now believable.`
- `python-lib: api-surface doc updated, unittest smoke passed, first public proof is now believable.`

## Keep it honest

Use these lines only when:

1. one visible preset asset changed,
2. one reproducible check passed, and
3. the diff is still small enough to review quickly.

If any of those are missing, report the missing proof instead of claiming readiness.
