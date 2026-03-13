from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetRepo45PhaseOneStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_status_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = (ROOT / "docs" / "PRESET_REPO45_PHASE_ONE_STATUS_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_REPO45_PHASE_ONE_STATUS_NOTE.md", readme)
        self.assertIn("repo 4", note)
        self.assertIn("repo 5", note)
        self.assertIn("scenario-file -> report-bundle phase-one work", note)


if __name__ == "__main__":
    unittest.main()
