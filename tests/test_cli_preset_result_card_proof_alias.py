from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class PresetResultCardProofAliasTests(unittest.TestCase):
    def test_result_card_proof_alias_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("result-card-proof"), "web-app")


if __name__ == "__main__":
    unittest.main()
