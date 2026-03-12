import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'


class CliPresetsJsonResultCardFocusTests(unittest.TestCase):
    def test_presets_json_includes_result_card_focus_alias(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'oss_launchpad_cli.cli', 'presets', '--json'],
            cwd=ROOT,
            env={**dict(__import__('os').environ), 'PYTHONPATH': str(SRC)},
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        self.assertTrue(payload)
        for preset, details in payload.items():
            self.assertIn('result_card_focus', details, preset)
            self.assertEqual(details['result_card_focus'], details['first_ui_slice'])


if __name__ == '__main__':
    unittest.main()
