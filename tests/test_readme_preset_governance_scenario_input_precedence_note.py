from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetGovernanceScenarioInputPrecedenceNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_governance_scenario_input_precedence_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_GOVERNANCE_SCENARIO_INPUT_PRECEDENCE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_GOVERNANCE_SCENARIO_INPUT_PRECEDENCE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
