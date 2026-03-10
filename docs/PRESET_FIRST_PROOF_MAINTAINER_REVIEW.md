# PRESET_FIRST_PROOF_MAINTAINER_REVIEW

Use this one-page review right after `oss-launchpad init` and before the first manual commit.

## Goal

Confirm that the generated scaffold already shows one believable public proof path, not just a pile of files.

## Review loop

1. Open the printed **starter assets** and confirm they match the preset story.
2. Open the printed **first proof assets** and confirm one file is visible proof while another is reproducible proof.
3. Run the printed **validation command** exactly as shown.
4. Open the printed **proof-review command** pair and check that the repository story is still honest.
5. If the proof feels too broad, keep the first manual commit smaller and narrower.

## Pass signal

A fresh scaffold feels ready when a maintainer can answer:

- What is the repo for?
- What is the first believable proof?
- Which command re-checks that proof?
- Which two files should reviewers open first?

## Fail signal

Do not oversell the scaffold if the first proof is still only structural boilerplate.
Narrow the first commit until the README, proof asset, and validation command tell the same story.
