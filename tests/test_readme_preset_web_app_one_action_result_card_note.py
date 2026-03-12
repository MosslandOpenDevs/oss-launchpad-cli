from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppOneActionResultCardNoteTest(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_ONE_ACTION_RESULT_CARD_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_ONE_ACTION_RESULT_CARD_NOTE.md").exists())

    def test_note_mentions_primary_action_and_result_card(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_ONE_ACTION_RESULT_CARD_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("primary action", note)
        self.assertIn("result card", note)
        self.assertIn("oss-launchpad presets --json --preset web-app", note)


if __name__ == "__main__":
    unittest.main()
