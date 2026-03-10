# Preset first proof keep-or-trim guide

Use this guide when the first manual commit after `oss-launchpad init` feels too large.

## Goal

Keep the first preset-specific proof believable, reviewable, and small enough for a public repo.

## Keep

Keep changes that clearly support the first believable proof pair:

- one visible proof asset,
- one reproducible check asset,
- one README or launch-plan note that explains the proof.

## Trim

Trim changes that make the diff look like roadmap inflation:

- unrelated refactors,
- multiple new workflows at once,
- placeholder-heavy docs that do not support the first proof,
- broad cleanup with no obvious launch-readiness value.

## Default rule

If a file does not strengthen the first believable proof, leave it for the next commit.
