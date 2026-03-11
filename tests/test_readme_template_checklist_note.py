from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeTemplateChecklistNoteTests(unittest.TestCase):
    def test_readme_mentions_template_checklist_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_TEMPLATE_CHECKLIST_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "README_TEMPLATE_CHECKLIST_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
