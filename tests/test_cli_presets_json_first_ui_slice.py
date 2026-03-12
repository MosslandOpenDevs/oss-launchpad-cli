from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliPresetsJsonFirstUiSliceTests(unittest.TestCase):
    def test_presets_json_includes_first_ui_slice(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": str(SRC)},
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        self.assertIn("result card", payload["web-app"]["first_ui_slice"])
        self.assertIn("usage example", payload["python-lib"]["first_ui_slice"])

    def test_readme_mentions_preset_json_first_ui_slice_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_FIRST_UI_SLICE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_FIRST_UI_SLICE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
