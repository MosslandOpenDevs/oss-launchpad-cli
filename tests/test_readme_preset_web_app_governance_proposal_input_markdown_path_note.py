import unittest
from pathlib import Path


class ReadmePresetWebAppGovernanceProposalInputMarkdownPathNoteTest(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_proposal_input_markdown_path_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        note = (root / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_PROPOSAL_INPUT_MARKDOWN_PATH_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_PROPOSAL_INPUT_MARKDOWN_PATH_NOTE.md', readme)
        self.assertIn('proposal_input_markdown_path', note)
        self.assertIn('result card', note)


if __name__ == '__main__':
    unittest.main()
