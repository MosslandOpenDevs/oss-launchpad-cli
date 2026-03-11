from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeWebDemoAssetCheckTests(unittest.TestCase):
    def test_readme_mentions_web_demo_asset_check_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_DEMO_ASSET_CHECK.md", readme)
        self.assertTrue((root / "docs" / "PRESET_WEB_DEMO_ASSET_CHECK.md").exists())


if __name__ == "__main__":
    unittest.main()
