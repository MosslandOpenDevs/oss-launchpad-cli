from pathlib import Path


def test_readme_mentions_preset_five_repo_four_five_validate_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_FIVE_REPO_FOUR_FIVE_VALIDATE_NOTE.md" in readme
