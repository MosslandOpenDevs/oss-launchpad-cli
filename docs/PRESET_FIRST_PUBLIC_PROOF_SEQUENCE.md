# PRESET_FIRST_PUBLIC_PROOF_SEQUENCE

Use this after `oss-launchpad init` when the scaffold exists and you want the shortest believable path to the first public proof.

## Sequence
1. Run the preset-specific smoke command printed by `init`.
2. Open the preset's most visible proof asset (README, demo, evals, or example file).
3. Pair that visible asset with one reproducible check artifact.
4. Make one preset-specific edit that improves the proof, not the scaffold volume.
5. Re-run the same smoke command before the first push.

## Rule of thumb
Your first public proof should show one visible artifact plus one repeatable check. Do not try to prove full project maturity on day zero.

## One-line maintainer note
`First public proof is ready when one preset-specific artifact reads credibly and its paired smoke check still passes.`
