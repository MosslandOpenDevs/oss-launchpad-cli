# Preset first proof review exit

Use this page after the generated scaffold has been customized once and before the first public proof commit.

## Exit checks

1. **Visible proof asset** — one preset-specific file already looks believable to a public reader.
2. **Reproducible check asset** — one command or test proves the proof asset is real.
3. **README alignment** — the generated README still points to the same proof path.
4. **Scope honesty** — the diff stays narrow enough to review quickly.

## Pass / hold rule

- **Pass** when all four checks are true.
- **Hold** when the diff still feels like scaffold churn instead of a first believable proof.

## Example framing

- `ai-agent`: prompt file + smoke eval case
- `web-app`: landing-page brief + UI checklist
- `python-lib`: API surface note + smoke test
