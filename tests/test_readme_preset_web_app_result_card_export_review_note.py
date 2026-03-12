from pathlib import Path
import unittest


class ReadmePresetWebAppResultCardExportReviewNoteTests(unittest.TestCase):
    def test_readme_mentions_export_review_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_REVIEW_NOTE.md", readme)
        self.assertTrue((root / "docs" / "PRESET_WEB_APP_RESULT_CARD_EXPORT_REVIEW_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
