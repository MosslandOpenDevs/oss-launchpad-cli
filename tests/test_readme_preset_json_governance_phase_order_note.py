from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernancePhaseOrderNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_phase_order_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_GOVERNANCE_PHASE_ORDER_NOTE.md", readme)
        self.assertIn("scenario-file -> report-bundle -> preset -> result-card phase order", readme)


if __name__ == "__main__":
    unittest.main()
