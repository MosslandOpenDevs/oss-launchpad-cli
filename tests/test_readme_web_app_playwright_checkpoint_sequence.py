from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeWebAppPlaywrightCheckpointSequenceTests(unittest.TestCase):
    def test_readme_mentions_web_app_playwright_checkpoint_sequence(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINT_SEQUENCE.md", readme)
        self.assertTrue((root / "docs" / "PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINT_SEQUENCE.md").exists())


if __name__ == "__main__":
    unittest.main()
