#!/usr/bin/env python3
"""Local, guarded Rojo operations for the standalone Signal Lost Roblox place.

Requires Python 3.10+ and pinned Rojo 7.7.1.
This script NEVER publishes, uploads, or modifies Roblox account settings.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
PROJECT_FILE = ROOT / "default.project.json"
EXPECTED_ROJO_VERSION = "7.7.1"
REQUIRED_MAPPING = (
    ("ReplicatedStorage", "Shared", "src/shared"),
    ("ServerScriptService", "GameServer", "src/server"),
    ("StarterPlayer", "StarterPlayerScripts", "GameClient", "src/client"),
)


class SetupError(Exception):
    """Invalid project or unsafe local environment."""


def load_project(path: Path = PROJECT_FILE) -> dict:
    try:
        project = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SetupError(f"Cannot read Rojo project: {exc}") from exc
    if not isinstance(project, dict):
        raise SetupError("Rojo project must be a JSON object")
    return project


def allowed_place_ids(project: dict) -> list[int]:
    values = project.get("servePlaceIds")
    if not isinstance(values, list):
        raise SetupError(
            "servePlaceIds must be an explicit array: [] until a NEW dedicated place is verified"
        )
    if any(type(value) is not int or value <= 0 for value in values):
        raise SetupError("servePlaceIds must contain only positive numeric Roblox place IDs")
    if len(set(values)) != len(values):
        raise SetupError("servePlaceIds has duplicate place IDs")
    return values


def validate_project(project: dict) -> None:
    if project.get("name") != "SignalLost":
        raise SetupError("Unexpected project name; refusing to work on a different place")
    if project.get("tree", {}).get("$className") != "DataModel":
        raise SetupError("This must remain a DataModel place project")
    tree = project["tree"]
    for chain in REQUIRED_MAPPING:
        *parts, directory = chain
        node = tree
        for part in parts:
            if not isinstance(node, dict) or part not in node:
                raise SetupError(f"Missing expected Rojo mapping: {'/'.join(parts)}")
            node = node[part]
        if node.get("$path") != directory:
            raise SetupError(f"Unexpected path for {'/'.join(parts)}: {node.get('$path')!r}")
        if not (ROOT / directory).is_dir():
            raise SetupError(f"Missing mapped source folder: {directory}")
    allowed_place_ids(project)


def rojo_path() -> str:
    candidate = os.environ.get("ROJO_BIN") or shutil.which("rojo")
    if not candidate:
        raise SetupError(
            "Rojo not installed. Install Rokit, run 'rokit install', then reopen your terminal."
        )
    try:
        result = subprocess.run(
            [candidate, "--version"], capture_output=True, text=True,
            timeout=15, check=True,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise SetupError(f"Rojo unavailable: {exc}") from exc
    version_text = result.stdout + result.stderr
    if not re.search(r"(?<![0-9])7\.7\.1(?![0-9])", version_text):
        raise SetupError(
            f"Expected Rojo {EXPECTED_ROJO_VERSION}; received: {version_text.strip()}"
        )
    return candidate


def doctor() -> int:
    project = load_project()
    validate_project(project)
    print("[OK] Correct standalone project structure")
    ids = allowed_place_ids(project)
    if ids:
        print(f"[OK] Rojo live-sync place allowlist: {ids}")
    else:
        print("[LOCKED] Live sync disabled until dedicated place ID is approved")
    try:
        binary = rojo_path()
        print(f"[OK] Pinned Rojo {EXPECTED_ROJO_VERSION}: {binary}")
    except SetupError as exc:
        print(f"[MISSING TOOL] {exc}")
        return 1
    print("[NOTE] Roblox Studio GUI, plugin, real place and multiplayer tests are NOT verified by this command")
    return 0


def build() -> int:
    project = load_project()
    validate_project(project)
    binary = rojo_path()
    output = ROOT / "build" / "SignalLost.rbxlx"
    output.parent.mkdir(parents=True, exist_ok=True)
    print(f"Building source-only place snapshot: {output}")
    result = subprocess.run(
        [binary, "build", str(PROJECT_FILE), "-o", str(output)],
        cwd=ROOT, check=False,
    )
    if result.returncode != 0:
        return result.returncode
    if not output.is_file() or output.stat().st_size == 0:
        raise SetupError("Rojo completed without producing a nonempty build")
    print(f"[OK] Rojo generated {output.name}; this is not a Studio playtest or publish")
    return 0


def serve(place_id: int) -> int:
    project = load_project()
    validate_project(project)
    ids = allowed_place_ids(project)
    if len(ids) != 1:
        raise SetupError(
            "Live sync is LOCKED. Set servePlaceIds to exactly ONE NEW, independently "
            "verified Roblox place ID, then commit/review the change before serving."
        )
    if place_id != ids[0]:
        raise SetupError(
            f"Requested place ID {place_id} is not the reviewed allowlisted place ID {ids[0]}"
        )
    binary = rojo_path()
    print(f"[GUARD] Starting Rojo ONLY for approved place {place_id}.")
    print("[GUARD] Confirm the Roblox Studio title and make a place backup BEFORE Connect.")
    print("[GUARD] Never use another game's place, and never auto-publish.")
    try:
        return subprocess.call([binary, "serve", str(PROJECT_FILE)], cwd=ROOT)
    except OSError as exc:
        raise SetupError(f"Cannot start Rojo server: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe Signal Lost Rojo environment")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Validate mappings, tool version and sync lock")
    commands.add_parser("build", help="Make a local .rbxlx snapshot (not publish)")
    serve_parser = commands.add_parser("serve", help="Guarded live sync to ONE approved place")
    serve_parser.add_argument("--place-id", type=int, required=True)
    args = parser.parse_args()
    try:
        if args.command == "doctor":
            return doctor()
        if args.command == "build":
            return build()
        if args.command == "serve":
            return serve(args.place_id)
        return 2
    except SetupError as exc:
        print(f"[BLOCKED] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
