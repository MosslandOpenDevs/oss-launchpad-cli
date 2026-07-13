from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from oss_launchpad_cli.cli import (
    PRESET_ALIASES,
    build_preset_metadata,
    build_presets_payload,
)

CANONICAL_PRESETS = ["ai-agent", "python-lib", "web-app"]
COMMAND_KEYS = [
    "smoke",
    "validation",
    "customize_first",
    "starter_review",
    "day_zero_review",
    "first_pr",
    "proof_review",
    "first_issue",
    "first_release",
]


def run_cli(*args: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(SRC))
    return subprocess.run(
        [sys.executable, "-m", "oss_launchpad_cli.cli", *args],
        capture_output=True,
        text=True,
        env=env,
    )


class PresetMetadataTests(unittest.TestCase):
    def test_payload_has_versioned_schema_with_presets_and_aliases(self) -> None:
        payload = build_presets_payload(CANONICAL_PRESETS)
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(sorted(payload["presets"]), CANONICAL_PRESETS)
        self.assertEqual(payload["aliases"], dict(sorted(PRESET_ALIASES.items())))

    def test_each_preset_exposes_stable_fields(self) -> None:
        for preset in CANONICAL_PRESETS:
            details = build_preset_metadata(preset)
            with self.subTest(preset=preset):
                self.assertEqual(details["preset_key"], preset)
                self.assertTrue(details["label"])
                self.assertTrue(details["summary"])
                self.assertTrue(details["first_ui_slice"])
                self.assertTrue(details["ui_ux_lane"])
                self.assertTrue(details["playwright_lane"])
                self.assertTrue(details["playwright_recovery_lane"])
                self.assertIsInstance(details["starter_assets"], list)
                self.assertIsInstance(details["quickstart_docs"], list)
                self.assertIsInstance(details["first_proof_assets"], list)
                self.assertIsInstance(details["day_zero_docs"], list)
                self.assertEqual(sorted(details["commands"]), sorted(COMMAND_KEYS))
                self.assertTrue(details["next_steps"])

    def test_legacy_duplicate_keys_are_gone(self) -> None:
        details = build_preset_metadata("web-app")
        for legacy_key in [
            "preset_count",
            "result_card_focus",
            "report_download_checkpoint",
            "proof_scope",
            "primary_action",
            "smoke_command",
            "validation_command",
            "proof_validation_command",
            "result_card_validation_command",
            "setup_command",
            "result_card_setup_command",
            "customize_first_command",
        ]:
            self.assertNotIn(legacy_key, details)

    def test_python_lib_commands_render_package_name(self) -> None:
        details = build_preset_metadata("python-lib", package_name="my_lib")
        self.assertIn("src/my_lib/__init__.py", details["commands"]["customize_first"])
        self.assertNotIn("{package_name}", json.dumps(details))

    def test_python_lib_smoke_keeps_pythonpath_for_each_chained_command(self) -> None:
        smoke = build_preset_metadata("python-lib")["commands"]["smoke"]
        first, second = smoke.split("&&")
        self.assertIn("PYTHONPATH=src", first)
        self.assertIn("PYTHONPATH=src", second)

    def test_day_zero_docs_include_license(self) -> None:
        for preset in CANONICAL_PRESETS:
            self.assertIn("LICENSE", build_preset_metadata(preset)["day_zero_docs"])

    def test_ai_agent_jsonl_commands_validate_line_by_line(self) -> None:
        commands = build_preset_metadata("ai-agent")["commands"]
        for key in ("smoke", "validation"):
            self.assertIn("--json-lines", commands[key])

    def test_web_app_demo_commands_use_bash(self) -> None:
        commands = build_preset_metadata("web-app")["commands"]
        for key in ("smoke", "validation"):
            self.assertTrue(commands[key].startswith("bash demo/run_demo.sh"), commands[key])


class PresetsCommandTests(unittest.TestCase):
    def test_text_output_lists_all_presets(self) -> None:
        result = run_cli("presets")
        self.assertEqual(result.returncode, 0, result.stderr)
        for preset in CANONICAL_PRESETS:
            self.assertIn(f"{preset}:", result.stdout)
        self.assertIn("first_ui_slice:", result.stdout)
        self.assertIn("starter_assets:", result.stdout)

    def test_json_output_parses_and_matches_schema(self) -> None:
        result = run_cli("presets", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(sorted(payload["presets"]), CANONICAL_PRESETS)
        self.assertIn("aliases", payload)

    def test_single_preset_filter_accepts_alias(self) -> None:
        result = run_cli("presets", "--json", "--preset", "library")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(list(payload["presets"]), ["python-lib"])


if __name__ == "__main__":
    unittest.main()
