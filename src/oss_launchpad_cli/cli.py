"""oss-launchpad-cli -- scaffold launch-ready public OSS repositories."""

from __future__ import annotations

import argparse
import dataclasses
import datetime
import hashlib
import json
import keyword
import re
import unicodedata
from pathlib import Path

from oss_launchpad_cli import __version__

PACKAGE_ROOT = Path(__file__).resolve().parent
TEMPLATES_ROOT = PACKAGE_ROOT / "templates"
BASE_TEMPLATE_ROOT = TEMPLATES_ROOT / "base"
PRESET_TEMPLATE_ROOTS = {
    "ai-agent": TEMPLATES_ROOT / "ai-agent",
    "web-app": TEMPLATES_ROOT / "web-app",
    "python-lib": TEMPLATES_ROOT / "python-lib",
}

METADATA_FILENAME = ".oss-launchpad.json"

PRESET_ALIASES = {
    "agent": "ai-agent",
    "app": "web-app",
    "site": "web-app",
    "website": "web-app",
    "frontend": "web-app",
    "landing": "web-app",
    "landing-page": "web-app",
    "showcase": "web-app",
    "web-demo": "web-app",
    "governance-demo": "web-app",
    "dao-demo": "web-app",
    "lib": "python-lib",
    "library": "python-lib",
}

PRESET_SUMMARIES = {
    "ai-agent": "Best when the first believable proof is a prompt, eval, and runnable agent contract.",
    "web-app": "Best when the first believable proof is a landing flow, UI checklist, and demo script.",
    "python-lib": "Best when the first believable proof is an importable package, smoke test, and usage example.",
}

PRESET_FIRST_UI_SLICE = {
    "ai-agent": "System prompt + eval contract + first runnable demo brief.",
    "web-app": "One form, one primary action, and one reviewable result card.",
    "python-lib": "One import path, one smoke test, and one usage example.",
}

PRESET_UI_UX_LANE = {
    "ai-agent": "Lead with the smallest believable workflow proof before layering extra controls or dashboards.",
    "web-app": "Lead with intro-first messaging, one form, one primary action, and one reviewable result card before adding secondary navigation.",
    "python-lib": "Lead with the clearest import/use path before widening advanced API surface or packaging detail.",
}

PRESET_PLAYWRIGHT_LANE = {
    "ai-agent": "Keep the first prompt/eval proof deterministic before widening the demo surface.",
    "web-app": "Keep browser proof limited to one form, one primary action, and one stable result card before widening flows.",
    "python-lib": "Keep smoke proof focused on one import path and one stable usage example before adding matrix coverage.",
}

PRESET_PLAYWRIGHT_RECOVERY_LANE = {
    "ai-agent": "Re-run the smallest deterministic eval path before widening agent-demo automation.",
    "web-app": "Recover with the smallest form -> primary action -> result-card replay before widening browser flows.",
    "python-lib": "Recover with one import path and one smoke example before adding broader matrix checks.",
}

# Rendered with {package_name} where the command depends on the import path.
PRESET_COMMAND_TEMPLATES = {
    "ai-agent": {
        "smoke": "python3 -m json.tool --json-lines < evals/smoke_cases.jsonl >/dev/null",
        "validation": "python3 -m json.tool --json-lines < evals/smoke_cases.jsonl >/dev/null",
        "customize_first": "sed -n '1,80p' prompts/system.txt && sed -n '1,80p' evals/README.md",
        "starter_review": "sed -n '1,80p' README.md && sed -n '1,80p' prompts/system.txt",
        "day_zero_review": "sed -n '1,120p' README.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "first_pr": "sed -n '1,120p' docs/agent-demo-brief.md && sed -n '1,120p' evals/README.md",
        "proof_review": "sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "first_issue": "sed -n '1,120p' docs/agent-demo-brief.md && sed -n '1,120p' evals/README.md",
        "first_release": "sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md",
    },
    "web-app": {
        "smoke": "bash demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md",
        "validation": "bash demo/run_demo.sh >/dev/null && sed -n '1,20p' docs/landing-page-brief.md",
        "customize_first": "sed -n '1,80p' docs/landing-page-brief.md && sed -n '1,80p' docs/ui-ux-checklist.md",
        "starter_review": "sed -n '1,80p' README.md && sed -n '1,80p' docs/landing-page-brief.md",
        "day_zero_review": "sed -n '1,120p' README.md && sed -n '1,120p' docs/landing-page-brief.md",
        "first_pr": "sed -n '1,120p' docs/landing-page-brief.md && sed -n '1,120p' docs/information-architecture.md",
        "proof_review": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md",
        "first_issue": "sed -n '1,120p' docs/ui-ux-checklist.md && sed -n '1,120p' docs/information-architecture.md",
        "first_release": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md",
    },
    "python-lib": {
        "smoke": "PYTHONPATH=src python3 -m unittest tests/test_smoke.py && PYTHONPATH=src python3 examples/basic_usage.py",
        "validation": "PYTHONPATH=src python3 -m unittest tests/test_smoke.py",
        "customize_first": "sed -n '1,80p' src/{package_name}/__init__.py && sed -n '1,80p' docs/api-surface.md",
        "starter_review": "sed -n '1,80p' README.md && sed -n '1,80p' src/{package_name}/__init__.py",
        "day_zero_review": "sed -n '1,120p' README.md && sed -n '1,120p' examples/basic_usage.py",
        "first_pr": "sed -n '1,120p' examples/basic_usage.py && sed -n '1,120p' docs/api-surface.md",
        "proof_review": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' examples/basic_usage.py",
        "first_issue": "sed -n '1,120p' docs/api-surface.md && sed -n '1,120p' tests/test_smoke.py",
        "first_release": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/api-surface.md",
    },
}

PRESET_STARTER_ASSETS = {
    "ai-agent": [
        "prompts/system.txt",
        "evals/README.md",
        "evals/smoke_cases.jsonl",
        "docs/agent-demo-brief.md",
    ],
    "web-app": [
        ".env.example",
        "docs/ui-ux-checklist.md",
        "docs/landing-page-brief.md",
        "docs/information-architecture.md",
        "demo/run_demo.sh",
    ],
    "python-lib": [
        "pyproject.toml",
        "src/{package_name}/__init__.py",
        "tests/test_smoke.py",
        "examples/basic_usage.py",
        "docs/api-surface.md",
    ],
}

PRESET_QUICKSTART_DOCS = {
    "ai-agent": ["README.md", "prompts/system.txt", "evals/README.md", "docs/agent-demo-brief.md"],
    "web-app": ["README.md", ".env.example", "docs/landing-page-brief.md", "docs/ui-ux-checklist.md"],
    "python-lib": ["README.md", "src/{package_name}/__init__.py", "examples/basic_usage.py", "docs/api-surface.md"],
}

PRESET_FIRST_PROOF_ASSETS = {
    "ai-agent": ["docs/agent-demo-brief.md", "evals/smoke_cases.jsonl", "demo/run_demo.sh"],
    "web-app": ["docs/landing-page-brief.md", "docs/ui-ux-checklist.md", "demo/run_demo.sh"],
    "python-lib": ["examples/basic_usage.py", "tests/test_smoke.py", "docs/api-surface.md"],
}

COMMON_DAY_ZERO_DOCS = [
    "README.md",
    "LICENSE",
    "docs/launch-plan.md",
    "docs/launch-scorecard.md",
    "RELEASE_CHECKLIST.md",
]

PRESET_DAY_ZERO_DOCS = {
    "ai-agent": ["docs/agent-demo-brief.md", "evals/README.md"],
    "web-app": ["docs/landing-page-brief.md", "docs/ui-ux-checklist.md", "docs/information-architecture.md", "demo/run_demo.sh"],
    "python-lib": ["docs/api-surface.md", "examples/basic_usage.py", "tests/test_smoke.py"],
}

COMMON_NEXT_STEPS = [
    "Review README.md and replace placeholder setup commands with the first real local run.",
    "Confirm LICENSE matches how you intend to publish the project.",
    "Fill docs/launch-plan.md with the launch audience, proof assets, and release scope.",
    "Complete docs/launch-scorecard.md so the first public announcement has a visible readiness checklist.",
    "Review RELEASE_CHECKLIST.md before the first tag so launch steps and public proof stay aligned.",
    "Replace demo/run_demo.sh placeholder output with the real walkthrough command.",
]

PRESET_NEXT_STEPS = {
    "ai-agent": [
        "Update prompts/system.txt with the first system prompt or agent contract.",
        "Add a real evaluation command under evals/README.md before the first public release.",
    ],
    "web-app": [
        "Fill .env.example with the minimum local variables required to boot the app.",
        "Review docs/information-architecture.md alongside docs/landing-page-brief.md before the first UI implementation.",
        "Replace docs/ui-ux-checklist.md examples with the actual landing-page and happy-path UX checks.",
    ],
    "python-lib": [
        "Implement the first public API in src/{package_name}/__init__.py.",
        "Run the printed validation command after wiring the package import path.",
    ],
}

DEFAULT_CONTEXT = {
    "project_tagline": "Bootstrap a public repository with launch-ready documentation and reproducible project scaffolding.",
    "why_section": "Use this repository to explain the project clearly, show a runnable path, and make contribution/release expectations obvious.",
    "setup_section": "- Document install steps.\n- Add the first runnable command.\n- Keep setup instructions short and reproducible.",
}

# Templates may contain literal braces (JSON, shell, CI syntax); only known
# context keys are substituted and everything else is left untouched.
_PLACEHOLDER_RE = re.compile(r"\{([a-z][a-z0-9_]*)\}")


@dataclasses.dataclass
class InitResult:
    created: list[str]
    skipped: list[str]
    previous_preset: str | None = None
    untouched: list[str] = dataclasses.field(default_factory=list)
    customized: list[str] = dataclasses.field(default_factory=list)


def _render_text(text: str, context: dict[str, str]) -> str:
    return _PLACEHOLDER_RE.sub(
        lambda match: str(context.get(match.group(1), match.group(0))),
        text,
    )


def _sanitize_title(title: str) -> str:
    cleaned = re.sub(r"[\x00-\x1f\x7f]+", " ", title).strip()
    return cleaned or "New Project"


def _ascii_slug(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.strip().lower()).strip("-")


def _slugify_title(title: str) -> str:
    return _ascii_slug(title) or "new-project"


def _package_name_for(title_slug: str) -> str:
    package_name = title_slug.replace("-", "_")
    if not package_name.isidentifier() or keyword.iskeyword(package_name):
        package_name = f"pkg_{package_name}"
    return package_name


def _resolve_preset_name(preset: str) -> str:
    return PRESET_ALIASES.get(preset, preset)


def _fill(entries, package_name: str):
    context = {"package_name": package_name}
    if isinstance(entries, dict):
        return {key: _render_text(value, context) for key, value in entries.items()}
    return [_render_text(entry, context) for entry in entries]


def build_commands(preset: str, package_name: str) -> dict[str, str]:
    return _fill(PRESET_COMMAND_TEMPLATES[preset], package_name)


def build_starter_assets(preset: str, package_name: str) -> list[str]:
    return _fill(PRESET_STARTER_ASSETS[preset], package_name)


def build_quickstart_docs(preset: str, package_name: str) -> list[str]:
    return _fill(PRESET_QUICKSTART_DOCS[preset], package_name)


def build_first_proof_assets(preset: str, package_name: str) -> list[str]:
    return _fill(PRESET_FIRST_PROOF_ASSETS[preset], package_name)


def build_day_zero_docs(preset: str, package_name: str) -> list[str]:
    return COMMON_DAY_ZERO_DOCS + _fill(PRESET_DAY_ZERO_DOCS[preset], package_name)


def build_next_steps(preset: str, package_name: str) -> list[str]:
    commands = build_commands(preset, package_name)
    return (
        [
            f"Smoke command: {commands['smoke']}",
            f"Validation command: {commands['validation']}",
            f"Customize-first command: {commands['customize_first']}",
        ]
        + COMMON_NEXT_STEPS
        + _fill(PRESET_NEXT_STEPS[preset], package_name)
    )


def build_preset_metadata(preset: str, package_name: str = "sample_project") -> dict:
    return {
        "preset_key": preset,
        "label": preset.replace("-", " ").title(),
        "summary": PRESET_SUMMARIES[preset],
        "first_ui_slice": PRESET_FIRST_UI_SLICE[preset],
        "ui_ux_lane": PRESET_UI_UX_LANE[preset],
        "playwright_lane": PRESET_PLAYWRIGHT_LANE[preset],
        "playwright_recovery_lane": PRESET_PLAYWRIGHT_RECOVERY_LANE[preset],
        "starter_assets": build_starter_assets(preset, package_name),
        "quickstart_docs": build_quickstart_docs(preset, package_name),
        "first_proof_assets": build_first_proof_assets(preset, package_name),
        "day_zero_docs": build_day_zero_docs(preset, package_name),
        "commands": build_commands(preset, package_name),
        "next_steps": build_next_steps(preset, package_name),
    }


def build_presets_payload(presets: list[str]) -> dict:
    return {
        "schema_version": 1,
        "presets": {preset: build_preset_metadata(preset) for preset in presets},
        "aliases": dict(sorted(PRESET_ALIASES.items())),
    }


def _load_preset_context(preset: str, title: str) -> dict[str, str]:
    preset = _resolve_preset_name(preset)
    if preset not in PRESET_TEMPLATE_ROOTS:
        raise ValueError(f"Unsupported preset: {preset}")
    context_path = PRESET_TEMPLATE_ROOTS[preset] / "context.json"
    with context_path.open("r", encoding="utf-8") as handle:
        preset_context = json.load(handle)
    title = _sanitize_title(title)
    title_slug = _slugify_title(title)
    today = datetime.date.today()
    merged = dict(DEFAULT_CONTEXT)
    merged.update(preset_context)
    merged.update(
        {
            "title": title,
            "title_slug": title_slug,
            "package_name": _package_name_for(title_slug),
            "year": str(today.year),
            "today": today.isoformat(),
        }
    )
    return merged


def _iter_template_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.name != "context.json"
        # pip byte-compiles .py template files after installation; the
        # resulting __pycache__ artifacts are not part of the scaffold.
        and "__pycache__" not in path.parts
        and path.suffix not in {".pyc", ".pyo"}
    )


def _render_template_group(
    target: Path, template_root: Path, context: dict[str, str]
) -> tuple[list[str], list[str]]:
    created: list[str] = []
    skipped: list[str] = []
    resolved_target = target.resolve()
    for template_file in _iter_template_files(template_root):
        rel_path = template_file.relative_to(template_root)
        rendered_rel_path = Path(_render_text(rel_path.as_posix(), context))
        file_path = target / rendered_rel_path
        # Symlinks inside the target must not redirect writes outside it.
        if not file_path.resolve().is_relative_to(resolved_target):
            raise ValueError(
                f"Refusing to write outside the target directory: {rendered_rel_path.as_posix()} "
                "resolves through a symlink that leaves the scaffold root."
            )
        if file_path.exists():
            skipped.append(rendered_rel_path.as_posix())
            continue
        file_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = _render_text(template_file.read_text(encoding="utf-8"), context)
        if file_path.suffix == ".py":
            try:
                compile(rendered, rendered_rel_path.as_posix(), "exec")
            except SyntaxError as error:
                raise ValueError(
                    f"Rendered template is not valid Python "
                    f"({rendered_rel_path.as_posix()}): {error}"
                ) from None
        file_path.write_text(rendered, encoding="utf-8")
        if file_path.suffix == ".sh":
            file_path.chmod(0o755)
        created.append(rendered_rel_path.as_posix())
    return created, skipped


def _file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_scaffold_metadata(target: Path) -> dict | None:
    meta_path = target / METADATA_FILENAME
    if not meta_path.is_file():
        return None
    try:
        loaded = json.loads(meta_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    return loaded if isinstance(loaded, dict) else None


def init_project(target: Path, title: str, preset: str) -> InitResult:
    preset = _resolve_preset_name(preset)
    title = _sanitize_title(title)
    context = _load_preset_context(preset, title)
    previous = _load_scaffold_metadata(target)
    created, skipped = _render_template_group(target, BASE_TEMPLATE_ROOT, context)
    preset_created, preset_skipped = _render_template_group(
        target, PRESET_TEMPLATE_ROOTS[preset], context
    )
    created.extend(preset_created)
    skipped.extend(preset_skipped)

    files = dict((previous or {}).get("files") or {})
    for rel in created:
        files[rel] = _file_digest(target / rel)
    untouched: list[str] = []
    customized: list[str] = []
    for rel in skipped:
        recorded = files.get(rel)
        if recorded is None:
            continue
        if _file_digest(target / rel) == recorded:
            untouched.append(rel)
        else:
            customized.append(rel)

    metadata = {
        "generator": "oss-launchpad-cli",
        "generator_version": __version__,
        "preset": preset,
        "title": title,
        "files": files,
    }
    (target / METADATA_FILENAME).write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    return InitResult(
        created=created,
        skipped=skipped,
        previous_preset=(previous or {}).get("preset"),
        untouched=untouched,
        customized=customized,
    )


def _list_presets() -> list[str]:
    return sorted(PRESET_TEMPLATE_ROOTS)


def _list_preset_choices() -> list[str]:
    return sorted(set(_list_presets()) | set(PRESET_ALIASES))


def _print_section(header: str, items: list[str]) -> None:
    print(header)
    for item in items:
        print(f"- {item}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="oss-launchpad")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init", help="Initialize a public OSS launch scaffold")
    init_cmd.add_argument("directory", help="Target directory")
    init_cmd.add_argument("--title", help="Project title", default="New Project")
    init_cmd.add_argument(
        "--preset",
        choices=_list_preset_choices(),
        default="ai-agent",
        metavar="{" + ",".join(_list_presets()) + "}",
        help="Project preset to render into the scaffold (canonical presets shown; common aliases such as 'app', 'site', or 'library' are also accepted)",
    )

    presets_cmd = sub.add_parser("presets", help="List scaffold presets and starter assets")
    presets_cmd.add_argument("--json", action="store_true", help="Print preset metadata as JSON")
    presets_cmd.add_argument(
        "--preset",
        choices=_list_preset_choices(),
        metavar="{" + ",".join(_list_presets()) + "}",
        help="Show metadata for one preset only (aliases accepted)",
    )

    args = parser.parse_args()

    if args.command == "presets":
        preset_names = [_resolve_preset_name(args.preset)] if args.preset else _list_presets()
        payload = build_presets_payload(preset_names)
        if args.json:
            print(json.dumps(payload, indent=2))
            return
        for preset, details in payload["presets"].items():
            print(f"{preset}: {details['summary']}")
            print(f"  first_ui_slice: {details['first_ui_slice']}")
            print(f"  ui_ux_lane: {details['ui_ux_lane']}")
            print(f"  smoke_command: {details['commands']['smoke']}")
            print(f"  validation_command: {details['commands']['validation']}")
            _print_section("  starter_assets:", details["starter_assets"])
            _print_section("  quickstart_docs:", details["quickstart_docs"])
        return

    if args.command == "init":
        resolved_preset = _resolve_preset_name(args.preset)
        title = _sanitize_title(args.title)
        target = Path(args.directory).resolve()
        try:
            target.mkdir(parents=True, exist_ok=True)
        except (FileExistsError, NotADirectoryError):
            parser.error(f"target path exists and is not a directory: {target}")
        try:
            result = init_project(target, title, resolved_preset)
        except ValueError as error:
            parser.error(str(error))
        title_slug = _slugify_title(title)
        package_name = _package_name_for(title_slug)
        print(f"Initialized scaffold in: {target}")
        print(f"Preset: {resolved_preset}")
        print(f"Title slug: {title_slug}")
        if not _ascii_slug(title):
            print(
                "Warning: the title could not be converted to an ASCII slug, so the generic "
                "'new-project' slug is used. Pass an ASCII --title to control the slug."
            )
        if result.previous_preset and result.previous_preset != resolved_preset:
            print(
                f"Warning: this directory was previously scaffolded with the "
                f"'{result.previous_preset}' preset; mixing presets in one directory "
                "produces an inconsistent scaffold."
            )
        if resolved_preset == "python-lib":
            print(f"Package import path: {package_name}")
        if result.created:
            _print_section(f"Created {len(result.created)} file(s):", result.created)
        else:
            print("No new files created.")
        if result.skipped:
            drift = ""
            if result.untouched or result.customized:
                drift = (
                    f" ({len(result.customized)} customized, "
                    f"{len(result.untouched)} untouched since generation)"
                )
            print(f"Skipped {len(result.skipped)} existing file(s), never overwritten{drift}.")
        print(f"Scaffold state recorded in {METADATA_FILENAME}.")
        _print_section(
            "Starter assets to customize first:",
            build_starter_assets(resolved_preset, package_name),
        )
        _print_section("Day-zero docs to open:", build_day_zero_docs(resolved_preset, package_name))
        _print_section("Next steps:", build_next_steps(resolved_preset, package_name))


if __name__ == "__main__":
    main()
