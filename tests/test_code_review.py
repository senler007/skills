from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


class ReviewContractTests(unittest.TestCase):
    def test_code_review_is_discoverable_and_implicit(self) -> None:
        skill_root = SKILLS / "code-review"
        self.assertTrue((skill_root / "SKILL.md").is_file())
        metadata = (skill_root / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("$code-review", metadata)
        self.assertIn("allow_implicit_invocation: true", metadata)

    def test_review_preserves_matt_fixed_point_and_smell_baseline(self) -> None:
        skill = (SKILLS / "code-review" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("git diff <fixed-point>...HEAD", skill)
        self.assertIn("git log <fixed-point>..HEAD --oneline", skill)
        for smell in ("Mysterious Name", "Feature Envy", "Shotgun Surgery", "Middle Man"):
            self.assertIn(smell, skill)

    def test_review_keeps_the_approved_senler_differences(self) -> None:
        skill = (SKILLS / "code-review" / "SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(skill.split())

        for axis in ("Standards", "Spec", "Documentation"):
            self.assertIn(axis, skill)
        self.assertIn("current conversation", skill)
        self.assertIn("Do not create sub-agents", normalized)
        self.assertIn("project-docs.md", skill)
        self.assertIn("module guides", skill)


if __name__ == "__main__":
    unittest.main()
