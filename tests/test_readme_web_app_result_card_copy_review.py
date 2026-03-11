from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardCopyReviewTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_copy_review(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md").exists())


if __name__ == "__main__":
    unittest.main()
