# Preset first release checklist

Use this checklist before cutting the first public release for a generated preset repository.

## Minimum proof

1. Run the preset init command and confirm scaffold files are created.
2. Run the preset smoke command from the generated README.
3. Confirm the generated repo has at least one customization note beyond the default scaffold.
4. Record the exact command/output pair in the pull request or release notes.

## Release note sentence

`Validated the <preset> preset by rerunning init, executing the documented smoke command, and checking the generated proof assets.`

## Scope warning

Do not advertise a preset as release-ready when the generated README still points to placeholder commands or missing proof assets.
