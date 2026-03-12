from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetFiveRepoCommitGateNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_five_repo_commit_gate_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_FIVE_REPO_COMMIT_GATE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_FIVE_REPO_COMMIT_GATE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
