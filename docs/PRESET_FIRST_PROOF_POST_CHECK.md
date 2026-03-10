# Preset first-proof post check

Use this short check before posting or pushing the first believable preset-specific proof.

## Pass conditions

1. One visible proof asset changed (`README`, demo brief, landing brief, or API surface note).
2. One reproducible check asset is still runnable (`tests/test_smoke.py`, `evals/smoke_cases.jsonl`, or demo command output).
3. The claimed proof stays preset-scoped instead of sounding like the whole project is feature-complete.
4. The diff is small enough for a stranger to review in one pass.

## One-line status template

`First proof ready: one visible preset asset plus one reproducible check asset are updated and still reviewable.`
