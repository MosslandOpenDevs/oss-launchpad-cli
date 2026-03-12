from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonFormCardScopeTests(unittest.TestCase):
    def test_readme_mentions_preset_json_form_card_scope(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_FORM_CARD_SCOPE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_FORM_CARD_SCOPE.md").exists())


if __name__ == "__main__":
    unittest.main()
