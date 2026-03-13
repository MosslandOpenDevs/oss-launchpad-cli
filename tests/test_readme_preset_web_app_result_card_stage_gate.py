import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardStageGateTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_stage_gate(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_STAGE_GATE.md", readme)
        self.assertIn("web-app", readme)


if __name__ == "__main__":
    unittest.main()
