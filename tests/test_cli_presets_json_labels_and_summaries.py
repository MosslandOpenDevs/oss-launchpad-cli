from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliPresetsJsonLabelsAndSummariesTests(unittest.TestCase):
    def test_presets_json_includes_label_and_summary(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": str(SRC)},
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["web-app"]["label"], "Web App")
        self.assertIn("landing flow", payload["web-app"]["summary"])
        self.assertEqual(payload["python-lib"]["label"], "Python Lib")
        self.assertIn("importable package", payload["python-lib"]["summary"])



    def test_readme_mentions_preset_json_form_result_card_export_path_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_FORM_RESULT_CARD_EXPORT_PATH_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_FORM_RESULT_CARD_EXPORT_PATH_NOTE.md").exists())

if __name__ == "__main__":
    unittest.main()
