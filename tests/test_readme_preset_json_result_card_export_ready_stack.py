from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOC = ROOT / "docs" / "PRESET_JSON_RESULT_CARD_EXPORT_READY_STACK.md"


def test_readme_mentions_preset_json_result_card_export_ready_stack() -> None:
    readme = README.read_text(encoding="utf-8")

    assert "docs/PRESET_JSON_RESULT_CARD_EXPORT_READY_STACK.md" in readme
    assert DOC.exists()
