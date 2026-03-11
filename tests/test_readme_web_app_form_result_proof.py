from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppFormResultProofTests(unittest.TestCase):
    def test_readme_mentions_web_app_form_result_proof(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FORM_RESULT_PROOF.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_FORM_RESULT_PROOF.md").exists())


if __name__ == "__main__":
    unittest.main()
