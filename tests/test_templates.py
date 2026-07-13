from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    tomllib = None

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from oss_launchpad_cli.cli import (
    DEFAULT_CONTEXT,
    METADATA_FILENAME,
    _load_preset_context,
    _package_name_for,
    _slugify_title,
    build_commands,
    build_day_zero_docs,
    build_first_proof_assets,
    build_quickstart_docs,
    build_starter_assets,
    init_project,
)

CANONICAL_PRESETS = ["ai-agent", "python-lib", "web-app"]
CONTEXT_KEYS = sorted(DEFAULT_CONTEXT) + ["title", "title_slug", "package_name", "year", "today"]
PLACEHOLDER_PATTERN = re.compile(r"\{[a-z][a-z0-9_]*\}")


class TemplateRenderTests(unittest.TestCase):
    def test_no_placeholder_like_token_survives_rendering(self) -> None:
        for preset in CANONICAL_PRESETS:
            with tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp)
                init_project(target, "Render Check", preset)
                for path in target.rglob("*"):
                    if not path.is_file() or path.name == METADATA_FILENAME:
                        continue
                    text = path.read_text(encoding="utf-8")
                    match = PLACEHOLDER_PATTERN.search(text)
                    self.assertIsNone(
                        match,
                        f"unrendered placeholder-like token {match.group(0) if match else ''} "
                        f"in {preset}:{path.name}",
                    )

    def test_every_promised_file_exists_in_generated_scaffold(self) -> None:
        for preset in CANONICAL_PRESETS:
            with tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp)
                title = "Promise Check"
                init_project(target, title, preset)
                package_name = _package_name_for(_slugify_title(title))
                promised = (
                    build_starter_assets(preset, package_name)
                    + build_quickstart_docs(preset, package_name)
                    + build_first_proof_assets(preset, package_name)
                    + build_day_zero_docs(preset, package_name)
                )
                for rel in promised:
                    with self.subTest(preset=preset, file=rel):
                        self.assertTrue((target / rel).is_file(), f"{preset} promises missing file {rel}")

    def test_preset_contexts_load_for_all_presets_and_aliases(self) -> None:
        for preset in CANONICAL_PRESETS + ["governance-demo", "library", "agent"]:
            context = _load_preset_context(preset, "Ctx Check")
            for key in CONTEXT_KEYS:
                self.assertIn(key, context)

    def test_quoted_title_still_generates_valid_python(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, 'My "Quoted" App', "python-lib")
            for rel in target.rglob("*.py"):
                source = rel.read_text(encoding="utf-8")
                compile(source, str(rel), "exec")

    @unittest.skipIf(tomllib is None, "tomllib requires Python 3.11+")
    def test_generated_python_lib_pyproject_is_valid_and_single_sourced(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "My Library", "python-lib")
            parsed = tomllib.loads((target / "pyproject.toml").read_text(encoding="utf-8"))
            self.assertEqual(parsed["project"]["name"], "my-library")
            self.assertIn("version", parsed["project"]["dynamic"])
            self.assertEqual(
                parsed["tool"]["setuptools"]["dynamic"]["version"]["attr"],
                "my_library.__version__",
            )


class GeneratedProjectSmokeTests(unittest.TestCase):
    def _run_shell(self, command: str, cwd: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=cwd,
            env=dict(os.environ),
        )

    def test_python_lib_scaffold_passes_its_own_validation_command(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "My Library", "python-lib")
            command = build_commands("python-lib", "my_library")["smoke"].replace(
                "python3", sys.executable
            )
            result = self._run_shell(command, target)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            # Guard against the 0.1.x zero-collected-tests regression, which
            # exits 0 on Python < 3.12.
            self.assertIn("Ran 1 test", result.stderr)

    def test_ai_agent_scaffold_passes_jsonl_validation_with_multiple_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "My Agent", "ai-agent")
            with (target / "evals" / "smoke_cases.jsonl").open("a", encoding="utf-8") as handle:
                handle.write('{"id":"second-case","input":"x","expected":"y"}\n')
            command = build_commands("ai-agent", "my_agent")["validation"].replace(
                "python3", sys.executable
            )
            result = self._run_shell(command, target)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_web_app_demo_script_runs_under_bash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "My App", "web-app")
            result = self._run_shell("bash demo/run_demo.sh", target)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            self.assertIn("PLACEHOLDER", result.stderr)


if __name__ == "__main__":
    unittest.main()
