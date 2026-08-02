import json
from pathlib import Path
import unittest


SKILLS = Path(__file__).resolve().parents[1] / "skills"


def parse_simple_metadata(path: Path) -> dict[str, dict[str, object]]:
    parsed: dict[str, dict[str, object]] = {}
    section: dict[str, object] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line or raw_line.lstrip().startswith("#"):
            continue
        if not raw_line.startswith(" ") and raw_line.endswith(":"):
            name = raw_line[:-1]
            if name in parsed:
                raise ValueError(f"duplicate metadata section: {name}")
            section = parsed[name] = {}
            continue
        if section is None or not raw_line.startswith("  ") or ":" not in raw_line:
            raise ValueError(f"unsupported metadata line: {raw_line}")
        key, raw_value = raw_line.strip().split(":", 1)
        if key in section:
            raise ValueError(f"duplicate metadata field: {key}")
        value = raw_value.strip()
        if value in {"true", "false"}:
            section[key] = value == "true"
        else:
            section[key] = json.loads(value)
    return parsed


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


if __name__ == "__main__":
    unittest.main()
