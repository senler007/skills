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
        self.assertIn("Spec or Ticket scope", metadata["interface"]["default_prompt"])
        self.assertIs(False, metadata["policy"]["allow_implicit_invocation"])

    def test_tdd_preserves_matt_package_shape(self) -> None:
        root = SKILLS / "tdd"
        self.assertTrue((root / "SKILL.md").is_file())
        self.assertTrue((root / "mocking.md").is_file())
        self.assertTrue((root / "tests.md").is_file())
        self.assertFalse((root / "references" / "mocking.md").exists())

    def test_implement_preserves_the_direct_matt_flow(self) -> None:
        instructions = " ".join(
            (SKILLS / "implement" / "SKILL.md")
            .read_text(encoding="utf-8")
            .lower()
            .split()
        )

        for requirement in (
            "implement the work described by the user in the spec or tickets",
            "a spec is sufficient input",
            "use `$tdd` where possible, at pre-agreed seams",
            "run typechecking regularly",
            "full test suite once at the end",
            "use `$code-review` to review the work",
            "commit the work to the current branch",
        ):
            self.assertIn(requirement, instructions)

        for forbidden_gate in (
            "small cohesive spec",
            "stop and recommend `$to-tickets`",
            "if absent, propose",
            "wait for confirmation",
        ):
            self.assertNotIn(forbidden_gate, instructions)

    def test_implement_keeps_only_the_approved_documentation_extension(self) -> None:
        instructions = (SKILLS / "implement" / "SKILL.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("$project-documentation", instructions)
        self.assertIn("daily development record", instructions)
        self.assertIn("Ask before", instructions)
        self.assertIn("new module guide", instructions)


if __name__ == "__main__":
    unittest.main()
