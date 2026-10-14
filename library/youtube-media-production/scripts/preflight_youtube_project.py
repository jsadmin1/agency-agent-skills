#!/usr/bin/env python3
"""Read-only preflight for a local YouTube production project and episode."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys


REQUIRED_EPISODE_INPUTS = (
    "script.locked.md",
    "script_segments.json",
    "rights.json",
)
DEFAULT_TOOLS = ("ffmpeg", "ffprobe")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--episode-root", type=Path, required=True)
    parser.add_argument("--require-doc", action="append", default=[], metavar="RELATIVE_PATH",
                        help="project document the studio treats as mandatory (repeatable)")
    parser.add_argument("--require-tool", action="append", default=[], metavar="NAME",
                        help="additional executable required on PATH (repeatable)")
    parser.add_argument("--project-python", default=None, metavar="RELATIVE_PATH",
                        help="optional project interpreter to check, e.g. .venv/bin/python")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def check_path(root: Path, relative: str, required: bool = True) -> dict[str, object]:
    path = root / relative
    exists = path.is_file()
    return {
        "name": relative,
        "path": str(path),
        "status": "PASS" if exists else ("STOP" if required else "WARN"),
    }


def main() -> int:
    args = parse_args()
    project = args.project_root.expanduser().resolve()
    episode = args.episode_root.expanduser().resolve()
    results: list[dict[str, object]] = []

    results.append({
        "name": "project_root",
        "path": str(project),
        "status": "PASS" if project.is_dir() else "STOP",
    })
    results.append({
        "name": "episode_root",
        "path": str(episode),
        "status": "PASS" if episode.is_dir() else "STOP",
    })

    if project.is_dir():
        results.extend(check_path(project, item) for item in args.require_doc)
        if args.project_python:
            results.append(check_path(project, args.project_python, required=False))

    if episode.is_dir():
        try:
            episode.relative_to(project)
            inside_project = True
        except ValueError:
            inside_project = False
        results.append({
            "name": "episode_inside_project",
            "path": str(episode),
            "status": "PASS" if inside_project else "STOP",
        })
        results.extend(check_path(episode, item) for item in REQUIRED_EPISODE_INPUTS)
        results.append(check_path(episode, "production_manifest.json", required=False))

    for tool in (*DEFAULT_TOOLS, *args.require_tool):
        resolved = shutil.which(tool)
        results.append({
            "name": f"tool:{tool}",
            "path": resolved,
            "status": "PASS" if resolved else "STOP",
        })

    stop_count = sum(item["status"] == "STOP" for item in results)
    warn_count = sum(item["status"] == "WARN" for item in results)
    report = {
        "valid": stop_count == 0,
        "stop_count": stop_count,
        "warn_count": warn_count,
        "checks": results,
    }

    if args.as_json:
        print(json.dumps(report, indent=2))
    else:
        for item in results:
            print(f"{item['status']:4} {item['name']}: {item['path']}")
        print(f"SUMMARY stop={stop_count} warn={warn_count}")
    return 0 if stop_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
