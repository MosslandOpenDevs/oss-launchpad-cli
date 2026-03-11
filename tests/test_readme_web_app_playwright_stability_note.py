from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppPlaywrightStabilityNoteTest(unittest.TestCase):
    def test_readme_links_playwright_stability_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        rel = "docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_NOTE.md"
        self.assertIn(rel, readme)
        note = (ROOT / rel).read_text(encoding="utf-8")
        self.assertIn("one form, one result card, and one downloadable artifact", note)
        self.assertIn("replaying the last stable step", note)


if __name__ == "__main__":
    unittest.main()
