import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ReadmePresetWebAppResultCardExportReviewLoopTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_export_review_loop(self) -> None:
        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_REVIEW_LOOP.md", README)


if __name__ == "__main__":
    unittest.main()
