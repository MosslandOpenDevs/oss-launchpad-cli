import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonFormResultCardExportStackTest(unittest.TestCase):
    def test_readme_mentions_preset_json_form_result_card_export_stack(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_FORM_RESULT_CARD_EXPORT_STACK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_FORM_RESULT_CARD_EXPORT_STACK.md").exists())


if __name__ == "__main__":
    unittest.main()
