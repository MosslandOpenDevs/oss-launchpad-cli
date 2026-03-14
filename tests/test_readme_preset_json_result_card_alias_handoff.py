from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePresetJsonResultCardAliasHandoffTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_alias_handoff_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_ALIAS_HANDOFF.md", readme)
        self.assertTrue((root / "docs" / "PRESET_JSON_RESULT_CARD_ALIAS_HANDOFF.md").exists())


if __name__ == "__main__":
    unittest.main()
