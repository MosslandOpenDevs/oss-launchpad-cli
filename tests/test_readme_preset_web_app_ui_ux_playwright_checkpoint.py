import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppUiUxPlaywrightCheckpointTests(unittest.TestCase):
    def test_readme_mentions_checkpoint_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_UI_UX_PLAYWRIGHT_CHECKPOINT.md", readme)

    def test_note_mentions_result_card_and_playwright(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_UI_UX_PLAYWRIGHT_CHECKPOINT.md").read_text(encoding="utf-8")
        self.assertIn("one stable result card", note)
        self.assertIn("reproducible Playwright checkpoint sequence", note)


if __name__ == "__main__":
    unittest.main()
