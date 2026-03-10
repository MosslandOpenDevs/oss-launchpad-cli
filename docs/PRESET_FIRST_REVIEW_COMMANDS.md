# Preset first review commands

Use these commands right after scaffold generation when you want the smallest believable review surface for each preset.

## ai-agent

```bash
sed -n '1,80p' README.md && sed -n '1,40p' evals/README.md
```

## web-app

```bash
sed -n '1,80p' README.md && sed -n '1,40p' docs/landing-page-brief.md
```

## python-lib

```bash
sed -n '1,80p' README.md && sed -n '1,80p' docs/api-surface.md
```

## Why this exists

A generated repo feels more reviewable when maintainers can open one public-facing file and one proof-oriented file immediately, without inventing a review path from scratch.
