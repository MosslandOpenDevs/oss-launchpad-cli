from pathlib import Path
import unittest


class ReadmePresetJsonResultCardExportOwnerStatusRecheckNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_export_owner_status_recheck_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_RESULT_CARD_EXPORT_OWNER_STATUS_RECHECK_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
