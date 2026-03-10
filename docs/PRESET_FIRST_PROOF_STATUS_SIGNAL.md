# Preset first proof status signal

Use this note after `oss-launchpad init` when you need a short pass/hold cue for the first believable preset-specific proof.

## PASS signal

Call the first proof ready only when all of the following are true:

1. one visible proof asset exists,
2. one reproducible check asset exists,
3. both assets match the preset story,
4. the maintainer update can name them without overselling the repo.

## HOLD signal

Hold the claim if any condition is missing, especially when the scaffold only looks complete on paper.

## One-line examples

- `PASS: ai-agent scaffold already shows a prompt plus smoke eval, so the first proof is believable.`
- `HOLD: web-app scaffold has landing docs, but no visible proof/check pair is named yet.`
- `PASS: python-lib scaffold has example usage plus smoke test, so the first proof can anchor the first public commit.`

## Related docs

- `docs/PRESET_FIRST_PROOF_OUTPUTS.md`
- `docs/PRESET_FIRST_PROOF_READY_CHECK.md`
- `docs/PRESET_FIRST_PROOF_PUSH_NOTE.md`
