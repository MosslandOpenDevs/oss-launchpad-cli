from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernanceProposalMarkdownPathNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_proposal_markdown_path_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = (ROOT / "docs" / "PRESET_JSON_GOVERNANCE_PROPOSAL_MARKDOWN_PATH_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_GOVERNANCE_PROPOSAL_MARKDOWN_PATH_NOTE.md", readme)
        self.assertIn("proposal_markdown_path", note)
        self.assertIn("scenario-file -> report-bundle -> result-card order", note)


if __name__ == "__main__":
    unittest.main()
