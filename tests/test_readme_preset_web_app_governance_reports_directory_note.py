from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceReportsDirectoryNoteTest(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_reports_directory_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_REPORTS_DIRECTORY_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_REPORTS_DIRECTORY_NOTE.md").exists())
