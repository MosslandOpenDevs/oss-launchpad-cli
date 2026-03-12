# Preset web app result card replay lane

For preset web app work, keep one reproducible path from form input to result card proof:

1. Fill one preset JSON form path.
2. Verify the primary status/result card above the fold.
3. Verify the export/download target without branching into multiple competing actions.
4. Record the validation command or Playwright checkpoint that can replay the same path.

This keeps UI polish aligned with stable verification instead of adding extra surface area without proof.
