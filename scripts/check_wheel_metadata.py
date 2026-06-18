#!/usr/bin/env python3
"""Builda o wheel e falha se algum import de terceiro não estiver em Requires-Dist."""
import ast
import re
import subprocess
import sys
import sysconfig
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STDLIB_NAMES = set(sysconfig.get_path_names()) | set(sys.stdlib_module_names)
NON_PACKAGE_DIRS = {"tests", "test", "build", "dist", "scripts"}

# Casos onde o nome do import difere do nome do pacote distribuído no PyPI.
IMPORT_TO_DIST = {
    "yaml": "pyyaml",
    "dateutil": "python-dateutil",
    "googleapiclient": "google-api-python-client",
    "google": "google-auth",
    "jwt": "pyjwt",
    "msoffcrypto": "msoffcrypto-tool",
    "bs4": "beautifulsoup4",
    "docx": "python-docx",
    "spellchecker": "pyspellchecker",
}


def top_level_imports(package_dir: Path) -> set[str]:
    names = set()
    for py_file in package_dir.rglob("*.py"):
        tree = ast.parse(py_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names.add(node.module.split(".")[0])
    return {n for n in names if n not in STDLIB_NAMES}


def requires_dist(wheel_path: Path) -> set[str]:
    with zipfile.ZipFile(wheel_path) as zf:
        metadata = next(n for n in zf.namelist() if n.endswith(".dist-info/METADATA"))
        text = zf.read(metadata).decode("utf-8")
    names = set()
    for line in text.splitlines():
        match = re.match(r"Requires-Dist:\s*([A-Za-z0-9_.\-]+)", line)
        if match:
            names.add(match.group(1).lower())
    return names


def main() -> int:
    subprocess.run([sys.executable, "-m", "build"], cwd=REPO_ROOT, check=True)
    wheel_path = next((REPO_ROOT / "dist").glob("*.whl"))

    package_dirs = [
        p for p in REPO_ROOT.iterdir()
        if p.is_dir()
        and p.name not in NON_PACKAGE_DIRS
        and not p.name.endswith(".egg-info")
        and (p / "__init__.py").exists()
    ]
    own_names = {p.name.lower() for p in package_dirs}
    imports = set()
    for package_dir in package_dirs:
        imports |= top_level_imports(package_dir)
    imports = {n for n in imports if n.lower() not in own_names}

    declared = requires_dist(wheel_path)

    def is_declared(name: str) -> bool:
        candidate = IMPORT_TO_DIST.get(name, name).lower()
        return candidate in declared or candidate.replace("_", "-") in declared

    missing = {name for name in imports if not is_declared(name)}

    if missing:
        print(f"Imports de terceiro sem Requires-Dist no wheel: {sorted(missing)}")
        return 1

    print(f"OK — Requires-Dist cobre todos os imports de terceiro: {sorted(declared)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
