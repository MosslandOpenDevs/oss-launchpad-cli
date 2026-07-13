from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from oss_launchpad_cli.cli import (
    PRESET_ALIASES,
    PRESET_TEMPLATE_ROOTS,
    _list_preset_choices,
    _list_presets,
    _resolve_preset_name,
)

EXPECTED_ALIASES = {
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


class AliasTests(unittest.TestCase):
    def test_alias_table_matches_documented_set(self) -> None:
        self.assertEqual(PRESET_ALIASES, EXPECTED_ALIASES)

    def test_every_alias_resolves_to_a_canonical_preset(self) -> None:
        for alias, expected in PRESET_ALIASES.items():
            with self.subTest(alias=alias):
                self.assertEqual(_resolve_preset_name(alias), expected)
                self.assertIn(expected, PRESET_TEMPLATE_ROOTS)

    def test_canonical_presets_resolve_to_themselves(self) -> None:
        for preset in _list_presets():
            self.assertEqual(_resolve_preset_name(preset), preset)

    def test_choices_cover_presets_and_aliases(self) -> None:
        choices = _list_preset_choices()
        self.assertEqual(
            sorted(choices),
            sorted(set(_list_presets()) | set(PRESET_ALIASES)),
        )


if __name__ == "__main__":
    unittest.main()
