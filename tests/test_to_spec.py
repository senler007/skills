from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "to-spec"


class ToSpecContractTests(unittest.TestCase):
    def test_skill_is_discoverable_and_explicit_only(self) -> None:
        self.assertTrue((SKILL_ROOT / "SKILL.md").is_file())
        metadata = (SKILL_ROOT / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("$to-spec", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)
        self.assertIn("lightweight change spec", metadata)

    def test_change_spec_template_contains_required_sections(self) -> None:
        template = (SKILL_ROOT / "references" / "spec-template.md").read_text(
            encoding="utf-8"
        )
        headings = [
            line.removeprefix("## ")
            for line in template.splitlines()
            if line.startswith("## ")
        ]

        self.assertEqual(
            ["Goal", "Change", "Scope", "Acceptance & Testing"], headings
        )
        self.assertIn("Optional", template)

    def test_workflow_links_configuration_and_testing_confirmation(self) -> None:
        instructions = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("issue-tracker.md", instructions)
        self.assertIn("project-docs.md", instructions)
        self.assertIn("confirm", instructions.lower())
        self.assertIn("testing seam", instructions.lower())


if __name__ == "__main__":
    unittest.main()
