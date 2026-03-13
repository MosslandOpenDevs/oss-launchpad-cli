import json
import subprocess
import sys


def test_presets_json_includes_result_card_setup_command_alias() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
        check=True,
        capture_output=True,
        text=True,
    )

    payload = json.loads(completed.stdout)
    for details in payload.values():
        assert details["result_card_setup_command"] == details["setup_command"]
        assert details["result_card_setup_command"] == details["customize_first_command"]
