from pathlib import Path


def test_readme_mentions_preset_governance_proposal_file_alias_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_GOVERNANCE_PROPOSAL_FILE_ALIAS_NOTE.md" in readme
