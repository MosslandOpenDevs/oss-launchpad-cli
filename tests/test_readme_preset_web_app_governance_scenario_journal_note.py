from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceScenarioJournalNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_scenario_journal_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_SCENARIO_JOURNAL_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_SCENARIO_JOURNAL_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
