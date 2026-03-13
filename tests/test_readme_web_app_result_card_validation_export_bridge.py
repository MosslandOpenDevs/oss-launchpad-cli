from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardValidationExportBridgeTests(unittest.TestCase):
    def test_readme_mentions_validation_export_bridge(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_VALIDATION_EXPORT_BRIDGE.md", readme)

    def test_note_mentions_validation_command_and_export_path(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_VALIDATION_EXPORT_BRIDGE.md").read_text(encoding="utf-8")
        self.assertIn("validation command", note)
        self.assertIn("export path", note)


if __name__ == "__main__":
    unittest.main()
