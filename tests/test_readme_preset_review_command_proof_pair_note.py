from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetReviewCommandProofPairNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_review_command_proof_pair_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_REVIEW_COMMAND_PROOF_PAIR_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_REVIEW_COMMAND_PROOF_PAIR_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
