from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernanceScenarioSourceShortAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_scenario_source_short_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_GOVERNANCE_SCENARIO_SOURCE_SHORT_ALIAS_NOTE.md", readme)
        self.assertIn("scenario_src", readme)
        self.assertIn("source_href", readme)


if __name__ == "__main__":
    unittest.main()
