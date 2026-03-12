from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePresetJsonResultCardExportOwnerStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_export_owner_status_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_EXPORT_OWNER_STATUS_NOTE.md", readme)
        self.assertTrue((root / "docs" / "PRESET_JSON_RESULT_CARD_EXPORT_OWNER_STATUS_NOTE.md").exists())
