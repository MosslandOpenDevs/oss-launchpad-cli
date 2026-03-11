from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebDemoFormResultStabilityTests(unittest.TestCase):
    def test_readme_mentions_preset_web_demo_form_result_stability(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md").exists())


if __name__ == "__main__":
    unittest.main()
