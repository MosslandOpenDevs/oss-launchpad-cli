from pathlib import Path
import unittest


class ReadmePresetWebAppResultCardReplayReadyNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_replay_ready_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_REPLAY_READY_NOTE.md", readme)
        self.assertTrue((root / "docs" / "PRESET_WEB_APP_RESULT_CARD_REPLAY_READY_NOTE.md").exists())
