from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_SOURCE_PATH_REPORT_BASENAME_NOTE.md"


class ReadmePresetWebAppGovernanceSourcePathReportBasenameNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_SOURCE_PATH_REPORT_BASENAME_NOTE.md", text)

    def test_note_mentions_source_path_and_report_basename(self) -> None:
        text = NOTE.read_text(encoding="utf-8")
        self.assertIn("scenario source path", text)
        self.assertIn("report basename", text)


if __name__ == "__main__":
    unittest.main()
