from pathlib import Path


def test_readme_mentions_preset_five_repo_repo45_one_line_gate_note() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_FIVE_REPO_REPO45_ONE_LINE_GATE_NOTE.md" in text
