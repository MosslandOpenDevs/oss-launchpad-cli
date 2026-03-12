from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePresetJsonCatalogOwnerNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_catalog_owner_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_CATALOG_OWNER_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
