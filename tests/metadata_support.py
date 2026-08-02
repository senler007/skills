import json
from pathlib import Path


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
