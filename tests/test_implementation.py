from pathlib import Path
import unittest

try:
    from tests.metadata_support import parse_simple_metadata
except ModuleNotFoundError:
    from metadata_support import parse_simple_metadata


SKILLS = Path(__file__).resolve().parents[1] / "skills"


class ImplementationPackageContractTests(unittest.TestCase):
    def test_tdd_metadata_contract(self) -> None:
        metadata = parse_simple_metadata(SKILLS / "tdd" / "agents" / "openai.yaml")
        self.assertEqual("TDD", metadata["interface"]["display_name"])
        self.assertIn("$tdd", metadata["interface"]["default_prompt"])
        self.assertIs(True, metadata["policy"]["allow_implicit_invocation"])

    def test_implement_metadata_contract(self) -> None:
        metadata = parse_simple_metadata(
            SKILLS / "implement" / "agents" / "openai.yaml"
        )
        self.assertEqual("Implement", metadata["interface"]["display_name"])
        self.assertIn("$implement", metadata["interface"]["default_prompt"])
        self.assertIs(False, metadata["policy"]["allow_implicit_invocation"])

    def test_tdd_bundles_required_references(self) -> None:
        root = SKILLS / "tdd"
        self.assertTrue((root / "SKILL.md").is_file())
        self.assertTrue((root / "references" / "mocking.md").is_file())
        self.assertTrue((root / "references" / "tests.md").is_file())

    def test_implement_has_required_package_files(self) -> None:
        root = SKILLS / "implement"
        self.assertTrue((root / "SKILL.md").is_file())
        self.assertTrue((root / "agents" / "openai.yaml").is_file())

    def test_implement_updates_the_daily_development_record(self) -> None:
        instructions = (SKILLS / "implement" / "SKILL.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("daily development record", instructions)


if __name__ == "__main__":
    unittest.main()
