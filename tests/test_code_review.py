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

    def test_review_axes_are_independent_and_read_only(self) -> None:
        skill = (SKILLS / "code-review" / "SKILL.md").read_text(encoding="utf-8")
        for axis in ("Standards", "Spec", "Documentation"):
            self.assertIn(axis, skill)
        self.assertIn("read-only", skill.lower())
        self.assertIn("fixed point", skill.lower())
        self.assertNotIn("launch three fresh review contexts", skill.lower())
        self.assertIn("current context", skill.lower())

    def test_review_reference_covers_documentation_integrity(self) -> None:
        axes = (
            SKILLS / "code-review" / "references" / "review-axes.md"
        ).read_text(encoding="utf-8")
        for concern in (
            "one authoritative owner",
            "accidental duplication",
            "unapproved or unnecessary new module guides",
            "explained code/design gaps",
        ):
            self.assertIn(concern, axes)


if __name__ == "__main__":
    unittest.main()
