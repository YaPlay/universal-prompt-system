#!/usr/bin/env python3
"""Repository QA for the Universal Prompt System v1.0 release contract.

The checks are intentionally standard-library-only.  The release-specific
expectations live in RELEASE_CONTRACT so the checking architecture can be
reused for a future release by changing the contract, not the checks.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import os
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

MODE_DIRS = {
    "Standard": "standard",
    "RPG": "rpg",
    "Sakura": "sakura",
    "Cyber": "cyber",
    "Anime Magic": "anime-magic",
    "Executive": "executive",
    "Study": "study",
}
LANGUAGES = ("RU", "EN", "FR", "ES", "UA")
CORE_SYSTEM_FILES = (
    "CHANGELOG.md",
    "CORE-SYSTEM-HARDENING-v1.0.md",
    "MAIN-ROUTER-v1.0.md",
    "MODES.md",
    "STARTUP-FLOW-v1.0.md",
    "QA-CHECKLIST.md",
    "START-HERE.md",
    "VERSION-MAP.md",
)
ALLOWED_AUXILIARY_SYSTEM_FILES = {"MAINTENANCE.md", "RELEASE-WORKFLOW.md"}

# Current main is a strict v1.0 release contract.  QA_EXPECTED_VERSION gives
# future releases an explicit override without changing the reusable checks.
RELEASE_CONTRACT = {
    "version": os.environ.get("QA_EXPECTED_VERSION", "v1.0"),
    "mode_file_count": 35,
    "system_file_count": 8,
    "registry_tuple_count": 35,
    "section_counts": {
        "Standard": 87,
        "RPG": 99,
        "Sakura": 98,
        "Cyber": 107,
        "Anime Magic": 108,
        "Executive": 107,
        "Study": 100,
    },
}

EXPECTED_TUPLES = set(product(MODE_DIRS, LANGUAGES))
METADATA_RE = {
    key: re.compile(rf"^{re.escape(key)}:\s*(.*?)\s*$", re.MULTILINE)
    for key in ("Mode", "Language", "Prompt Version", "Status")
}
REGISTRY_ROW_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*$"
)
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(\d+)\.")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

issues = defaultdict(list)


def fail(category: str, message: str) -> None:
    issues[category].append(message)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        fail("File readability", f"{path.relative_to(ROOT)}: {exc}")
        return None


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def tracked_paths() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail("Forbidden repository leakage", f"cannot inspect tracked files: {exc}")
        return []
    names = [name for name in result.stdout.decode("utf-8").split("\0") if name]
    return [ROOT / name for name in names]


def metadata(text: str) -> dict[str, str]:
    values = {}
    for key, pattern in METADATA_RE.items():
        match = pattern.search(text)
        if match:
            values[key] = match.group(1).strip()
    return values


def sections_and_fences(text: str) -> tuple[list[tuple[int, int]], bool]:
    sections: list[tuple[int, int]] = []
    fence: tuple[str, int] | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is None:
            heading = HEADING_RE.match(line)
            if heading:
                sections.append((int(heading.group(1)), line_number))
    return sections, fence is not None


def parse_registry(text: str) -> list[tuple[str, str, str, str]]:
    rows = []
    for line in text.splitlines():
        match = REGISTRY_ROW_RE.match(line)
        if match:
            rows.append(tuple(part.strip() for part in match.groups()))
    return rows


def check_mode_files() -> tuple[list[Path], dict[Path, dict[str, str]]]:
    paths = sorted((ROOT / "prompts").glob("*/*.md"))
    if len(paths) != RELEASE_CONTRACT["mode_file_count"]:
        fail(
            "Canonical file count",
            f"Mode files: expected {RELEASE_CONTRACT['mode_file_count']}, found {len(paths)}",
        )

    system_paths = sorted((ROOT / "system").glob("*.md"))
    core_system_paths = [ROOT / "system" / name for name in CORE_SYSTEM_FILES if (ROOT / "system" / name).is_file()]
    if len(core_system_paths) != RELEASE_CONTRACT["system_file_count"]:
        fail(
            "Canonical file count",
            f"canonical system files: expected {RELEASE_CONTRACT['system_file_count']}, found {len(core_system_paths)}",
        )
    unexpected_system = sorted(
        path.name
        for path in system_paths
        if path.name not in CORE_SYSTEM_FILES and path.name not in ALLOWED_AUXILIARY_SYSTEM_FILES
    )
    if unexpected_system:
        fail("Canonical file count", f"unexpected system files: {unexpected_system}")

    values_by_path: dict[Path, dict[str, str]] = {}
    tuple_to_paths: defaultdict[tuple[str, str], list[Path]] = defaultdict(list)
    for path in paths:
        text = read_text(path)
        if text is None:
            continue
        values = metadata(text)
        values_by_path[path] = values
        mode = values.get("Mode")
        language = values.get("Language")
        if mode not in MODE_DIRS:
            fail("Mode matrix", f"{relative(path)}: unknown Mode {mode!r}")
        if language not in LANGUAGES:
            fail("Mode matrix", f"{relative(path)}: unknown Language {language!r}")
        if mode in MODE_DIRS and language in LANGUAGES:
            tuple_to_paths[(mode, language)].append(path)

    for item in sorted(EXPECTED_TUPLES):
        matches = tuple_to_paths.get(item, [])
        if not matches:
            fail("Mode matrix", f"missing tuple: {item[0]} × {item[1]}")
        elif len(matches) != 1:
            fail(
                "Mode matrix",
                f"duplicate tuple {item[0]} × {item[1]}: {', '.join(relative(p) for p in matches)}",
            )
    return paths, values_by_path


def check_registry(mode_paths: list[Path]) -> dict[str, tuple[str, str, str]]:
    registry_path = ROOT / "system" / "MODES.md"
    text = read_text(registry_path)
    if text is None:
        fail("Canonical registry", "system/MODES.md is unreadable")
        return {}

    rows = parse_registry(text)
    expected_count = RELEASE_CONTRACT["registry_tuple_count"]
    if len(rows) != expected_count:
        fail("Canonical registry", f"canonical rows: expected {expected_count}, found {len(rows)}")

    path_counts = Counter(row[3] for row in rows)
    for path, count in sorted(path_counts.items()):
        if count > 1:
            fail("Canonical registry", f"duplicate canonical path ({count}): {path}")

    tuple_counts = Counter((row[0], row[1], row[2]) for row in rows)
    for item, count in sorted(tuple_counts.items()):
        if count > 1:
            fail("Canonical registry", f"duplicate canonical tuple ({count}): {item}")

    registry_map: dict[str, tuple[str, str, str]] = {}
    for mode, language, version, path_text in rows:
        key = path_text
        registry_map[key] = (mode, language, version)
        if mode not in MODE_DIRS or language not in LANGUAGES:
            fail("Canonical registry", f"unknown tuple: {mode} × {language} × {version}")
        if version != RELEASE_CONTRACT["version"]:
            fail("Canonical registry", f"unexpected version for {path_text}: {version}")
        target = ROOT / path_text
        if not target.is_file():
            fail("Canonical registry", f"missing path: {path_text}")

    registry_tuples = {(row[0], row[1]) for row in rows}
    if registry_tuples != EXPECTED_TUPLES:
        missing = sorted(EXPECTED_TUPLES - registry_tuples)
        extra = sorted(registry_tuples - EXPECTED_TUPLES)
        if missing:
            fail("Canonical registry", f"missing tuples: {missing}")
        if extra:
            fail("Canonical registry", f"unexpected tuples: {extra}")

    filesystem_paths = {relative(path) for path in mode_paths}
    registry_paths = set(registry_map)
    if filesystem_paths != registry_paths:
        missing = sorted(filesystem_paths - registry_paths)
        extra = sorted(registry_paths - filesystem_paths)
        if missing:
            fail("Canonical registry", f"unregistered files: {missing}")
        if extra:
            fail("Canonical registry", f"registry paths without files: {extra}")
    return registry_map


def check_metadata_and_sections(
    mode_paths: list[Path],
    values_by_path: dict[Path, dict[str, str]],
    registry_map: dict[str, tuple[str, str, str]],
) -> None:
    section_counts = RELEASE_CONTRACT["section_counts"]
    for path in mode_paths:
        values = values_by_path.get(path, {})
        mode = values.get("Mode")
        language = values.get("Language")
        if values.get("Prompt Version") != RELEASE_CONTRACT["version"]:
            fail("Metadata", f"{relative(path)}: Prompt Version must be {RELEASE_CONTRACT['version']}")
        if values.get("Status") != "Final":
            fail("Metadata", f"{relative(path)}: Status must be Final")
        registry_tuple = registry_map.get(relative(path))
        if registry_tuple and (mode, language, values.get("Prompt Version")) != registry_tuple:
            fail("Metadata", f"{relative(path)}: metadata disagrees with registry {registry_tuple}")

        text = read_text(path)
        if text is None:
            continue
        sections, unclosed_fence = sections_and_fences(text)
        if unclosed_fence:
            fail("Markdown code fences", f"{relative(path)}: unclosed fenced code block")

        expected = section_counts.get(mode)
        if expected is None:
            continue
        numbers = [number for number, _ in sections]
        if len(numbers) != expected:
            fail("Expected section counts", f"{relative(path)}: expected {expected}, found {len(numbers)}")

        duplicates = sorted(number for number, count in Counter(numbers).items() if count > 1)
        missing = sorted(set(range(1, expected + 1)) - set(numbers))
        if duplicates:
            fail("Section numbering", f"{relative(path)}: duplicate numbers {duplicates}")
        if missing:
            fail("Section numbering", f"{relative(path)}: missing numbers {missing}")
        if not numbers or numbers[0] != 1:
            fail("Section numbering", f"{relative(path)}: first section is not 1")
        if not numbers or numbers[-1] != expected:
            fail("Section numbering", f"{relative(path)}: last section is not {expected}")


def check_internal_links() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        if text is None:
            continue
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split(None, 1)[0].strip("<>")
            if target.startswith(("http://", "https://", "//", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail("Internal Markdown links", f"{relative(path)}: link escapes repository: {raw_target}")
                continue
            if not candidate.exists():
                fail("Internal Markdown links", f"{relative(path)}: missing target {raw_target}")


def check_forbidden_leakage() -> None:
    paths = tracked_paths()
    tracked_names = {path.relative_to(ROOT).as_posix() for path in paths}
    ds_store = sorted(name for name in tracked_names if Path(name).name == ".DS_Store")
    if ds_store:
        fail("Forbidden repository leakage", f"tracked .DS_Store: {ds_store}")

    env_files = sorted(
        name
        for name in tracked_names
        if Path(name).name == ".env"
        or (Path(name).name.startswith(".env.") and Path(name).name != ".env.example")
    )
    if env_files:
        fail("Forbidden repository leakage", f"tracked environment files: {env_files}")

    patterns = {
        "Unix personal path": re.compile(r"/Users/"),
        "Windows personal path": re.compile(r"(?i)\b[A-Z]:\\Users\\"),
        "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "GitHub token": re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}\b"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    }
    qa_script = Path(__file__).resolve()
    for path in paths:
        # The scanner's own regex literals intentionally contain the patterns
        # it is designed to detect; do not report those literals as leakage.
        if path.resolve() == qa_script:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            fail("Forbidden repository leakage", f"{relative(path)}: {exc}")
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                fail("Forbidden repository leakage", f"{relative(path)}: possible {label}")


def check_release_hygiene() -> None:
    required = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        "system/MAINTENANCE.md",
        "system/RELEASE-WORKFLOW.md",
        "docs/README-RU.md",
        "docs/README-EN.md",
        "docs/README-FR.md",
        "docs/README-ES.md",
        "docs/README-UA.md",
    ]
    for item in required:
        path = ROOT / item
        if not path.is_file() or path.stat().st_size == 0:
            fail("Public release hygiene", f"missing or empty: {item}")


def print_results() -> int:
    categories = [
        "Canonical file count",
        "Mode matrix",
        "Canonical registry",
        "Metadata",
        "Expected section counts",
        "Section numbering",
        "Markdown code fences",
        "Internal Markdown links",
        "Forbidden repository leakage",
        "Public release hygiene",
        "Startup Flow contract",
        "File readability",
    ]
    for category in categories:
        messages = issues.get(category, [])
        if messages:
            print(f"[FAIL] {category}")
            for message in messages:
                print(f"       - {message}")
        else:
            print(f"[PASS] {category}")

    failure_count = sum(len(messages) for messages in issues.values())
    print("\nQA SUMMARY")
    if failure_count:
        print(f"FAIL: {failure_count} blocking issue(s)")
        return 1
    print("PASS: all repository QA checks passed")
    return 0


def main() -> int:
    mode_paths, values_by_path = check_mode_files()
    registry_map = check_registry(mode_paths)
    check_metadata_and_sections(mode_paths, values_by_path, registry_map)
    startup_path = ROOT / "system" / "STARTUP-FLOW-v1.0.md"
    startup_text = read_text(startup_path) or ""
    required_startup_terms = (
        "Repository Entry",
        "Language Selection",
        "Mode Selection",
        "Mode Confirmation",
        "Startup Lock",
        "Start Trigger Aliases",
        "Resume Behavior",
        "Error / Recovery Behavior",
        "Language → Mode → Confirmation → Router → Mode Start",
        "Mandatory Language → Mode Transition",
        "acknowledgement-only response",
        "Mode choices shown immediately",
        "Mobile-first Mode Selection",
        "Standard** — structured project management",
        "Study** — learning mode",
        "Auto** — analyzes the stated goal",
        "Beautiful Startup Screen",
        "Step 1 of 3 — Language",
        "Step 2 of 3 — Mode",
        "Step 3 of 3 — Confirmation",
        "Language selected → immediately render Style Selection → wait for style choice",
        "Переключаюсь на русский.",
        "form of address",
    )
    for term in required_startup_terms:
        if term not in startup_text:
            fail("Startup Flow contract", f"system/STARTUP-FLOW-v1.0.md: missing {term!r}")
    if "Auto" not in startup_text or "never silently activate" not in startup_text:
        fail("Startup Flow contract", "Auto must be proposal-only and require explicit confirmation")
    if "35 canonical Mode × Language × Version tuples" not in startup_text:
        fail("Startup Flow contract", "Startup Flow must preserve the 35 canonical tuple registry")

    modes_text = read_text(ROOT / "system" / "MODES.md") or ""
    if "Startup label" not in modes_text or "Short description" not in modes_text:
        fail("Startup Flow contract", "MODES.md must expose Startup label and Short description")
    if "Startup-only selector: Auto" not in modes_text:
        fail("Startup Flow contract", "MODES.md must define Auto as startup-only")

    router_text = read_text(ROOT / "system" / "MAIN-ROUTER-v1.0.md") or ""
    if "## Startup Routing" not in router_text:
        fail("Startup Flow contract", "MAIN-ROUTER-v1.0.md must include Startup Routing")

    check_internal_links()
    check_forbidden_leakage()
    check_release_hygiene()
    return print_results()


if __name__ == "__main__":
    raise SystemExit(main())
