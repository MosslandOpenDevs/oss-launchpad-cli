# Preset first proof hold boundary

Use this note when a generated scaffold looks promising, but the first public proof still should not be pushed yet.

## Hold the push when

- the visible proof asset exists but still reads like placeholder content,
- the reproducible check asset has not been run yet,
- launch docs describe intent but not evidence,
- the first diff is already mixing multiple proof stories.

## Safe maintainer update

- `Scaffold is generated, but first proof is still on hold until one visible asset and one reproducible check asset are both real.`
- `Preset files exist, but public proof stays blocked until the first proof pair is customized and rechecked.`

## Fast review loop

1. open the preset's visible proof asset,
2. open the paired check asset,
3. confirm both are customized beyond placeholder state,
4. rerun the preset validation command,
5. only then use the repo-push checklist.

## Related docs

- `docs/PRESET_FIRST_PROOF_READY_CHECK.md`
- `docs/PRESET_FIRST_PROOF_SCOPE_CHECK.md`
- `docs/PRESET_FIRST_PROOF_REPO_PUSH_CHECK.md`
