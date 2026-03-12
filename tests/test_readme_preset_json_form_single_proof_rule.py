from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonFormSingleProofRuleTests(unittest.TestCase):
    def test_readme_mentions_single_proof_rule(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_FORM_SINGLE_PROOF_RULE.md', readme)

    def test_doc_mentions_result_card_and_validation_command(self) -> None:
        doc = (ROOT / 'docs' / 'PRESET_JSON_FORM_SINGLE_PROOF_RULE.md').read_text(encoding='utf-8')
        self.assertIn('one generated result card', doc)
        self.assertIn('visible validation command', doc)


if __name__ == '__main__':
    unittest.main()
