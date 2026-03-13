from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernanceSourceLocationAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_source_location_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_GOVERNANCE_SOURCE_LOCATION_ALIAS_NOTE.md", readme)
        self.assertIn("source_location", readme)


if __name__ == "__main__":
    unittest.main()
