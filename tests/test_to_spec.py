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

    def test_spec_is_synthesis_not_another_interview(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Do NOT interview the user", skill)
        self.assertIn("Check with the user that these seams match", skill)
        self.assertNotIn("consequential product decision is unresolved", skill)

    def test_inline_template_has_only_the_four_approved_sections(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        template = skill.split("<spec-template>", 1)[1].split("</spec-template>", 1)[0]
        headings = [
            line.removeprefix("## ")
            for line in template.splitlines()
            if line.startswith("## ")
        ]

        self.assertEqual(
            ["Goal", "Change", "Scope", "Acceptance & Testing"], headings
        )

    def test_explicit_invocation_publishes_without_duplicate_permission(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").lower()

        self.assertIn("authorizes this one spec publication", skill)
        self.assertIn("do not ask for a second confirmation", skill)
        self.assertIn("do not write a temporary spec file", skill)


if __name__ == "__main__":
    unittest.main()
