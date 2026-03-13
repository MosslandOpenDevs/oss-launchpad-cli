from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetFiveRepoRepo45ValidateStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_five_repo_repo45_validate_status_note(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_FIVE_REPO_REPO45_VALIDATE_STATUS_NOTE.md", text)
        self.assertTrue((ROOT / "docs" / "PRESET_FIVE_REPO_REPO45_VALIDATE_STATUS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
