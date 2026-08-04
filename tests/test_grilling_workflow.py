from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"


def read_skill(name: str) -> str:
    return (SKILLS_ROOT / name / "SKILL.md").read_text(encoding="utf-8")


def read_metadata(name: str) -> str:
    return (SKILLS_ROOT / name / "agents" / "openai.yaml").read_text(
        encoding="utf-8"
    )


class GrillingWorkflowContractTests(unittest.TestCase):
    def test_both_grilling_skills_are_discoverable(self) -> None:
        for name in ("grilling", "grill-with-docs"):
            with self.subTest(skill=name):
                skill_root = SKILLS_ROOT / name
                self.assertTrue((skill_root / "SKILL.md").is_file())
                self.assertTrue((skill_root / "agents" / "openai.yaml").is_file())

    def test_invocation_policies_separate_discipline_from_workflow(self) -> None:
        self.assertIn("allow_implicit_invocation: true", read_metadata("grilling"))
        self.assertIn(
            "allow_implicit_invocation: false", read_metadata("grill-with-docs")
        )

    def test_documentation_aware_workflow_names_both_supporting_disciplines(self) -> None:
        workflow = read_skill("grill-with-docs")

        self.assertIn("$grilling", workflow)
        self.assertIn("$project-documentation", workflow)

    def test_documentation_aware_workflow_stops_before_specification(self) -> None:
        workflow = read_skill("grill-with-docs").lower()

        self.assertIn("shared understanding", workflow)
        self.assertIn("do not automatically invoke `$to-spec`", workflow)

    def test_documentation_aware_workflow_uses_module_guides(self) -> None:
        workflow = read_skill("grill-with-docs").lower()

        self.assertIn("module guide", workflow)
        self.assertIn("new module guide", workflow)


if __name__ == "__main__":
    unittest.main()
