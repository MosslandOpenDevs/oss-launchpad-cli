from pathlib import Path
import unittest


class ReadmeWebAppGovernanceReportOutputKeyNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_report_output_key_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('report_output_key', readme)
        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_KEY_NOTE.md', readme)

    def test_note_exists_and_mentions_report_output_key(self) -> None:
        content = Path('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_KEY_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('report_output_key', content)
        self.assertIn('one reviewable result card', content)


if __name__ == '__main__':
    unittest.main()
