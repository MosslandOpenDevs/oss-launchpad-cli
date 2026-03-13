from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernancePhaseOneResultCardHandoffTests(unittest.TestCase):
    def test_readme_mentions_handoff_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_GOVERNANCE_PHASE_ONE_RESULT_CARD_HANDOFF.md", readme)

    def test_handoff_doc_mentions_scenario_file_and_markdown_html_report(self) -> None:
        doc = (ROOT / "docs" / "PRESET_JSON_GOVERNANCE_PHASE_ONE_RESULT_CARD_HANDOFF.md").read_text(encoding="utf-8")
        self.assertIn("scenario-file input support", doc)
        self.assertIn("markdown/html report generation", doc)


if __name__ == "__main__":
    unittest.main()
