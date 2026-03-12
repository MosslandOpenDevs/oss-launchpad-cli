from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppFormResultCardReviewStartTest(unittest.TestCase):
    def test_note_exists_with_small_ui_review_loop(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_FORM_RESULT_CARD_REVIEW_START.md").read_text(encoding="utf-8")
        self.assertIn("one form", note)
        self.assertIn("one primary action", note)
        self.assertIn("one result card", note)
        self.assertIn("one validation command before push", note)


if __name__ == "__main__":
    unittest.main()
