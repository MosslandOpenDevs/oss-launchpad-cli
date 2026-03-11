from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeWebAppResultCardDownloadCheckNoteTests(unittest.TestCase):
    def test_readme_keeps_result_card_download_check_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_CHECK.md", readme)
        note = root / "docs" / "PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_CHECK.md"
        self.assertTrue(note.exists())
        content = note.read_text(encoding="utf-8")
        self.assertIn("download or handoff target", content)


if __name__ == "__main__":
    unittest.main()
