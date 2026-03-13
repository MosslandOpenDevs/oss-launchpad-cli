from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonFormResultCardValidateRecoveryNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_form_result_card_validate_recovery_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_FORM_RESULT_CARD_VALIDATE_RECOVERY_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_FORM_RESULT_CARD_VALIDATE_RECOVERY_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
