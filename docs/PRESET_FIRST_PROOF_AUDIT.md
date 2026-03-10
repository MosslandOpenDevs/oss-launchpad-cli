# PRESET_FIRST_PROOF_AUDIT

Use this one-page audit right after `oss-launchpad init` and before the first manual commit.

## Goal

Make sure the generated scaffold already shows one believable proof asset and one reproducible check asset for the chosen preset.

## Audit loop

1. Run the printed `Validation command`.
2. Open the printed `Proof-review command`.
3. Confirm at least one preset-specific file reads like real project proof, not placeholder noise.
4. Confirm at least one reproducible check file can be re-run by another maintainer.

## Pass signal

The repo already looks alive enough that the first manual commit can focus on project specifics instead of fixing missing launch scaffolding.

## Fail signal

If the proof files still look generic, customize the preset starter assets before pushing the repository public.
