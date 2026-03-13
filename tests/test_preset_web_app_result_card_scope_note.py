from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PresetWebAppResultCardScopeNoteTest(unittest.TestCase):
    def test_note_keeps_first_ui_slice_narrow(self) -> None:
        doc = (ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_SCOPE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("one intro-first page, one primary form, and one reviewable result card", doc)
        self.assertIn("before adding secondary navigation", doc)

    def test_note_mentions_docs_and_playwright_proof_lane(self) -> None:
        doc = (ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_SCOPE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("Playwright path", doc)
        self.assertIn("docs/landing-page-brief.md", doc)
        self.assertIn("docs/information-architecture.md", doc)


if __name__ == "__main__":
    unittest.main()
