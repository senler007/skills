from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"


def frontmatter_keys(skill_file: Path) -> set[str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return set()

    keys: set[str] = set()
    for line in lines[1:]:
        if line == "---":
            break
        if line and not line[0].isspace() and ":" in line:
            keys.add(line.split(":", 1)[0])
    return keys


class FoundationContractTests(unittest.TestCase):
    def test_repository_preserves_upstream_and_original_mit_attribution(self) -> None:
        license_text = (REPOSITORY_ROOT / "LICENSE").read_text(encoding="utf-8")

        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 Matt Pocock", license_text)
        self.assertIn("Copyright (c) 2026 senler007", license_text)

    def test_foundation_skills_use_the_standard_package_shape(self) -> None:
        for skill_name in ("setup-senler-skills", "project-documentation"):
            with self.subTest(skill=skill_name):
                skill_root = SKILLS_ROOT / skill_name
                skill_file = skill_root / "SKILL.md"
                self.assertTrue(skill_file.is_file())
                self.assertEqual({"name", "description"}, frontmatter_keys(skill_file))
                self.assertTrue((skill_root / "agents" / "openai.yaml").is_file())

    def test_invocation_policies_match_the_public_workflow(self) -> None:
        setup_metadata = (
            SKILLS_ROOT / "setup-senler-skills" / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")
        documentation_metadata = (
            SKILLS_ROOT / "project-documentation" / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")

        self.assertIn('allow_implicit_invocation: false', setup_metadata)
        self.assertIn('allow_implicit_invocation: true', documentation_metadata)
        self.assertIn('$setup-senler-skills', setup_metadata)
        self.assertIn('$project-documentation', documentation_metadata)

    def test_setup_bundles_every_supported_tracker_and_document_layout_contract(self) -> None:
        references = SKILLS_ROOT / "setup-senler-skills" / "references"

        for filename in (
            "issue-tracker-github.md",
            "issue-tracker-local.md",
            "issue-tracker-custom.md",
            "project-docs.md",
        ):
            with self.subTest(reference=filename):
                self.assertTrue((references / filename).is_file())

    def test_documentation_reference_defines_each_authoritative_role(self) -> None:
        roles = (
            SKILLS_ROOT
            / "project-documentation"
            / "references"
            / "document-roles.md"
        ).read_text(encoding="utf-8")

        for role in (
            "Project overview",
            "Glossary",
            "Design systems",
            "Architecture",
            "ADRs",
            "Tracker work",
            "Development record",
        ):
            with self.subTest(role=role):
                self.assertIn(role, roles)

    def test_architecture_reference_defines_the_code_atlas_contract(self) -> None:
        architecture = (
            SKILLS_ROOT
            / "project-documentation"
            / "references"
            / "architecture.md"
        ).read_text(encoding="utf-8")

        for required_section in (
            "一分钟模块地图",
            "关键数据流",
            "生产单元索引",
            "复杂模块深入说明",
            "状态所有权",
        ):
            with self.subTest(section=required_section):
                self.assertIn(required_section, architecture)

        self.assertIn("不要强制添加“文档边界”章节", architecture)
        self.assertIn("优先考虑拆分生产单元", architecture)

    def test_documentation_skill_requires_one_daily_record_for_modifying_tasks(self) -> None:
        instructions = (
            SKILLS_ROOT / "project-documentation" / "SKILL.md"
        ).read_text(encoding="utf-8")
        setup_template = (
            SKILLS_ROOT
            / "setup-senler-skills"
            / "references"
            / "project-docs.md"
        ).read_text(encoding="utf-8")

        self.assertIn("daily development record", instructions)
        self.assertIn("Never create or update it for a read-only task", instructions)
        self.assertIn("Development records:", setup_template)


if __name__ == "__main__":
    unittest.main()
