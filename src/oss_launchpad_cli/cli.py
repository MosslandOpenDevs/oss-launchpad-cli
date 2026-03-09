from __future__ import annotations

import argparse
import json
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
TEMPLATES_ROOT = PACKAGE_ROOT.parent.parent / "templates"
BASE_TEMPLATE_ROOT = TEMPLATES_ROOT / "base"
PRESET_TEMPLATE_ROOTS = {
    "ai-agent": TEMPLATES_ROOT / "ai-agent",
    "web-app": TEMPLATES_ROOT / "web-app",
    "python-lib": TEMPLATES_ROOT / "python-lib",
}
DEFAULT_CONTEXT = {
    "project_tagline": "Bootstrap a public repository with launch-ready documentation and reproducible project scaffolding.",
    "why_section": "Use this repository to explain the project clearly, show a runnable path, and make contribution/release expectations obvious.",
    "setup_section": "- Document install steps.\n- Add the first runnable command.\n- Keep setup instructions short and reproducible.",
}


def _load_preset_context(preset: str) -> dict[str, str]:
    if preset not in PRESET_TEMPLATE_ROOTS:
        raise ValueError(f"Unsupported preset: {preset}")
    context_path = PRESET_TEMPLATE_ROOTS[preset] / "context.json"
    with context_path.open("r", encoding="utf-8") as handle:
        preset_context = json.load(handle)
    merged = dict(DEFAULT_CONTEXT)
    merged.update(preset_context)
    return merged


def _iter_template_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def init_project(target: Path, title: str, preset: str) -> list[str]:
    created: list[str] = []
    context = _load_preset_context(preset)
    context["title"] = title

    for template_file in _iter_template_files(BASE_TEMPLATE_ROOT):
        rel_path = template_file.relative_to(BASE_TEMPLATE_ROOT)
        file_path = target / rel_path
        if file_path.exists():
            continue
        file_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = template_file.read_text(encoding="utf-8").format(**context)
        file_path.write_text(rendered, encoding="utf-8")
        if file_path.name == "run_demo.sh":
            file_path.chmod(0o755)
        created.append(rel_path.as_posix())
    return created


def main() -> None:
    parser = argparse.ArgumentParser(prog="oss-launchpad")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init", help="Initialize a public OSS launch scaffold")
    init_cmd.add_argument("directory", help="Target directory")
    init_cmd.add_argument("--title", help="Project title", default="New Project")
    init_cmd.add_argument(
        "--preset",
        choices=sorted(PRESET_TEMPLATE_ROOTS),
        default="ai-agent",
        help="Project preset to render into the scaffold",
    )

    args = parser.parse_args()

    if args.command == "init":
        target = Path(args.directory).resolve()
        target.mkdir(parents=True, exist_ok=True)
        created = init_project(target, args.title, args.preset)
        print(f"Initialized scaffold in: {target}")
        print(f"Preset: {args.preset}")
        if created:
            print("Created files:")
            for item in created:
                print(f"- {item}")
        else:
            print("No new files created.")


if __name__ == "__main__":
    main()
