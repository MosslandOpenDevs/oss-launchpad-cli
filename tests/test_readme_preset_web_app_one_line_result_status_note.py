from __future__ import annotations

import unittest
from pathlib import Path


class ReadmePresetWebAppOneLineResultStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_one_line_result_status_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_ONE_LINE_RESULT_STATUS_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
