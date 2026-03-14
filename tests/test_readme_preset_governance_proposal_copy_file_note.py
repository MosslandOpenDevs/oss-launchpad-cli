from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetGovernanceProposalCopyFileNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_governance_proposal_copy_file_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_GOVERNANCE_PROPOSAL_COPY_FILE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_GOVERNANCE_PROPOSAL_COPY_FILE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
