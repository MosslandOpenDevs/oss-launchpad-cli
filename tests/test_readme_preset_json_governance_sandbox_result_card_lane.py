from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernanceSandboxResultCardLaneTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_result_card_lane(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_GOVERNANCE_SANDBOX_RESULT_CARD_LANE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_GOVERNANCE_SANDBOX_RESULT_CARD_LANE.md").exists())


if __name__ == "__main__":
    unittest.main()
