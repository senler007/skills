from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "skills" / "to-tickets"


class ToTicketsContractTests(unittest.TestCase):
    def test_package_and_explicit_policy(self) -> None:
        self.assertTrue((ROOT / "SKILL.md").is_file())
        metadata = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$to-tickets", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_ticket_template_has_delivery_contract(self) -> None:
        template = (ROOT / "references" / "ticket-template.md").read_text(
            encoding="utf-8"
        )
        for heading in ("Parent", "What to build", "Acceptance criteria", "Blocked by"):
            self.assertIn(f"## {heading}", template)

    def test_workflow_requires_approval_and_preserves_parent(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("approval", skill)
        self.assertIn("do not close, rewrite, or republish the parent spec", skill)


if __name__ == "__main__":
    unittest.main()
