from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PresetWebAppGovernanceResultCardExportOneCtaNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_result_card_export_one_cta_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_EXPORT_ONE_CTA_NOTE.md", readme)

    def test_note_mentions_one_primary_cta_and_export_ready_result_card(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_EXPORT_ONE_CTA_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("one primary CTA", note)
        self.assertIn("export-ready result card", note)

if __name__ == "__main__":
    unittest.main()
