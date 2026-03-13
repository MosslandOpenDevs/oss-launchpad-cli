from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceReportBundleEntryNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_report_bundle_entry_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = (ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_REPORT_BUNDLE_ENTRY_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_REPORT_BUNDLE_ENTRY_NOTE.md", readme)
        self.assertIn("scenario file entry", note)
        self.assertIn("result card", note)
        self.assertIn("report bundle", note)
        self.assertIn("UI/UX-first", note)
        self.assertIn("Playwright", note)


if __name__ == "__main__":
    unittest.main()
