from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PresetWebAppResultCardRecoveryLoopNoteTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_recovery_loop_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_RECOVERY_LOOP.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_RECOVERY_LOOP.md").exists())


if __name__ == "__main__":
    unittest.main()
