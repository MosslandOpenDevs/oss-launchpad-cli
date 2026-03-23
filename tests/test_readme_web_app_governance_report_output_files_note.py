from pathlib import Path
import unittest


class ReadmeWebAppGovernanceReportOutputFilesNoteTest(unittest.TestCase):
    def test_readme_mentions_output_files_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn(
            "docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_FILES_NOTE.md",
            readme,
        )

    def test_note_exists_and_mentions_report_output_files(self) -> None:
        note = Path("docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_FILES_NOTE.md")
        self.assertTrue(note.exists())
        content = note.read_text(encoding="utf-8")
        self.assertIn("report.outputs.files", content)
        self.assertIn("result card", content)
        self.assertIn("scenario file", content)


if __name__ == "__main__":
    unittest.main()
