from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from oss_launchpad_cli import __version__
from oss_launchpad_cli.cli import (
    METADATA_FILENAME,
    _package_name_for,
    _render_text,
    _sanitize_title,
    _slugify_title,
    init_project,
)


def run_cli(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(SRC))
    return subprocess.run(
        [sys.executable, "-m", "oss_launchpad_cli.cli", *args],
        capture_output=True,
        text=True,
        env=env,
        cwd=cwd,
    )


class SlugifyTests(unittest.TestCase):
    def test_falls_back_for_punctuation_only_titles(self) -> None:
        self.assertEqual(_slugify_title("***"), "new-project")
        self.assertEqual(_slugify_title("  ---  "), "new-project")

    def test_collapses_mixed_separators_into_single_dashes(self) -> None:
        self.assertEqual(_slugify_title("My_Library v2"), "my-library-v2")
        self.assertEqual(_slugify_title(" Agent---CLI   Demo "), "agent-cli-demo")

    def test_transliterates_accented_characters(self) -> None:
        self.assertEqual(_slugify_title("Café Über"), "cafe-uber")

    def test_falls_back_for_non_latin_titles(self) -> None:
        self.assertEqual(_slugify_title("한국어 프로젝트"), "new-project")


class SanitizeTitleTests(unittest.TestCase):
    def test_strips_control_characters(self) -> None:
        self.assertEqual(_sanitize_title("My\nProject\t v1"), "My Project  v1")

    def test_empty_title_falls_back_to_default(self) -> None:
        self.assertEqual(_sanitize_title("\n\t"), "New Project")


class PackageNameTests(unittest.TestCase):
    def test_plain_slug_maps_to_underscored_identifier(self) -> None:
        self.assertEqual(_package_name_for("my-library-v2"), "my_library_v2")

    def test_digit_leading_slug_gets_pkg_prefix(self) -> None:
        self.assertEqual(_package_name_for("3d-render-kit"), "pkg_3d_render_kit")

    def test_python_keyword_gets_pkg_prefix(self) -> None:
        self.assertEqual(_package_name_for("class"), "pkg_class")


class RenderTextTests(unittest.TestCase):
    def test_replaces_known_context_keys(self) -> None:
        self.assertEqual(_render_text("Hello {title}!", {"title": "World"}), "Hello World!")

    def test_leaves_literal_braces_untouched(self) -> None:
        context = {"title": "World"}
        self.assertEqual(_render_text('{"json": true}', context), '{"json": true}')
        self.assertEqual(_render_text("${SHELL_VAR} and ${{ ci.expr }}", context), "${SHELL_VAR} and ${{ ci.expr }}")
        self.assertEqual(_render_text("unknown {not_a_key} stays", context), "unknown {not_a_key} stays")


class InitProjectTests(unittest.TestCase):
    def test_creates_base_scaffold_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = init_project(target, "Sample Agent", "ai-agent")
            self.assertEqual(result.skipped, [])
            for expected in [
                "README.md",
                "LICENSE",
                ".gitignore",
                ".editorconfig",
                "CONTRIBUTING.md",
                "CHANGELOG.md",
                "RELEASE_CHECKLIST.md",
                ".github/ISSUE_TEMPLATE/bug_report.md",
                ".github/ISSUE_TEMPLATE/feature_request.md",
                ".github/pull_request_template.md",
                "benchmark/README.md",
                "demo/run_demo.sh",
                "docs/launch-plan.md",
                "docs/launch-scorecard.md",
            ]:
                self.assertIn(expected, result.created)
                self.assertTrue((target / expected).is_file(), expected)

    def test_renders_title_and_dates_into_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "Sample Agent", "ai-agent")
            readme = (target / "README.md").read_text(encoding="utf-8")
            self.assertIn("# Sample Agent", readme)
            self.assertNotIn("{title}", readme)
            license_text = (target / "LICENSE").read_text(encoding="utf-8")
            self.assertIn("MIT License", license_text)
            self.assertIn(str(datetime.date.today().year), license_text)
            changelog = (target / "CHANGELOG.md").read_text(encoding="utf-8")
            self.assertIn(datetime.date.today().isoformat(), changelog)

    def test_marks_demo_shell_script_executable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "Demo", "web-app")
            mode = (target / "demo" / "run_demo.sh").stat().st_mode
            self.assertTrue(mode & 0o111)

    def test_existing_files_are_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "README.md").write_text("custom readme\n", encoding="utf-8")
            result = init_project(target, "Sample", "web-app")
            self.assertNotIn("README.md", result.created)
            self.assertIn("README.md", result.skipped)
            self.assertEqual((target / "README.md").read_text(encoding="utf-8"), "custom readme\n")

    def test_second_run_creates_nothing_and_reports_all_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            first = init_project(target, "Sample", "python-lib")
            second = init_project(target, "Sample", "python-lib")
            self.assertEqual(second.created, [])
            self.assertEqual(sorted(second.skipped), sorted(first.created))

    def test_rejects_unknown_preset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                init_project(Path(tmp), "Sample", "not-a-preset")

    def test_refuses_to_write_through_symlink_escaping_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outside = Path(tmp) / "outside"
            outside.mkdir()
            target = Path(tmp) / "target"
            target.mkdir()
            (target / "docs").symlink_to(outside)
            with self.assertRaises(ValueError):
                init_project(target, "Sample", "web-app")
            self.assertEqual(list(outside.iterdir()), [])


class ScaffoldMetadataTests(unittest.TestCase):
    def test_init_writes_metadata_with_preset_and_file_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = init_project(target, "Sample", "web-app")
            meta = json.loads((target / METADATA_FILENAME).read_text(encoding="utf-8"))
            self.assertEqual(meta["preset"], "web-app")
            self.assertEqual(meta["title"], "Sample")
            self.assertEqual(meta["generator_version"], __version__)
            self.assertEqual(sorted(meta["files"]), sorted(result.created))

    def test_rerun_classifies_customized_and_untouched_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            first = init_project(target, "Sample", "web-app")
            (target / "README.md").write_text("customized\n", encoding="utf-8")
            second = init_project(target, "Sample", "web-app")
            self.assertIn("README.md", second.customized)
            self.assertNotIn("README.md", second.untouched)
            self.assertEqual(
                sorted(second.untouched),
                sorted(set(first.created) - {"README.md"}),
            )

    def test_rerun_reports_previous_preset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            init_project(target, "Sample", "web-app")
            result = init_project(target, "Sample", "ai-agent")
            self.assertEqual(result.previous_preset, "web-app")


class CliProcessTests(unittest.TestCase):
    def test_version_flag_prints_package_version(self) -> None:
        result = run_cli("--version")
        self.assertEqual(result.returncode, 0)
        self.assertIn(__version__, result.stdout)

    def test_init_prints_summary_and_creates_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            result = run_cli("init", str(target), "--title", "My Lib", "--preset", "python-lib")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Preset: python-lib", result.stdout)
            self.assertIn("Title slug: my-lib", result.stdout)
            self.assertIn("Package import path: my_lib", result.stdout)
            self.assertIn("Created", result.stdout)
            self.assertIn("Next steps:", result.stdout)
            self.assertTrue((target / "src" / "my_lib" / "__init__.py").is_file())

    def test_init_accepts_alias_and_reports_canonical_preset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            result = run_cli("init", str(target), "--title", "Demo", "--preset", "governance-demo")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Preset: web-app", result.stdout)
            self.assertTrue((target / ".env.example").is_file())

    def test_rerun_reports_no_new_files_and_skip_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            first = run_cli("init", str(target), "--title", "Demo", "--preset", "web-app")
            self.assertEqual(first.returncode, 0, first.stderr)
            second = run_cli("init", str(target), "--title", "Demo", "--preset", "web-app")
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("No new files created.", second.stdout)
            self.assertIn("Skipped", second.stdout)
            self.assertIn("untouched since generation", second.stdout)

    def test_rerun_with_other_preset_warns_about_mixing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            run_cli("init", str(target), "--title", "Demo", "--preset", "web-app")
            result = run_cli("init", str(target), "--title", "Demo", "--preset", "ai-agent")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("previously scaffolded with the 'web-app' preset", result.stdout)

    def test_non_ascii_title_prints_slug_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            result = run_cli("init", str(target), "--title", "한국어 프로젝트", "--preset", "web-app")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Title slug: new-project", result.stdout)
            self.assertIn("Warning:", result.stdout)

    def test_title_that_legitimately_slugs_to_new_project_does_not_warn(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "proj"
            result = run_cli("init", str(target), "--title", "NEW PROJECT", "--preset", "web-app")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Title slug: new-project", result.stdout)
            self.assertNotIn("Warning: the title could not be converted", result.stdout)

    def test_target_path_that_is_a_file_fails_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            blocker = Path(tmp) / "blocker"
            blocker.write_text("not a directory\n", encoding="utf-8")
            result = run_cli("init", str(blocker), "--title", "Demo", "--preset", "web-app")
            self.assertEqual(result.returncode, 2)
            self.assertIn("not a directory", result.stderr)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
