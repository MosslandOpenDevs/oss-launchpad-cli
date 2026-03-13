from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetFirstProofValidateStatusBridgeTests(unittest.TestCase):
    def test_readme_mentions_preset_first_proof_validate_status_bridge(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_FIRST_PROOF_VALIDATE_STATUS_BRIDGE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_FIRST_PROOF_VALIDATE_STATUS_BRIDGE.md").exists())


if __name__ == "__main__":
    unittest.main()
