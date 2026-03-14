from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReadmePresetWebAppGovernanceReportOutputBasenameNoteTest(unittest.TestCase):
    def test_readme_mentions_report_output_basename_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_BASENAME_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_BASENAME_NOTE.md").exists())

if __name__ == "__main__":
    unittest.main()
