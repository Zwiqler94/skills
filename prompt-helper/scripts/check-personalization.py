#!/usr/bin/env python3
"""Check local prompt-helper personalization for advisory sufficiency."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Local Surfaces",
    "Memory Policy",
    "Companion Skills",
    "Preferred Receipts",
    "Local Constraints",
]

PLACEHOLDER_LABELS = {
    "CLI",
    "IDE extension",
    "Codex app",
    "Use memory for",
    "Do not use memory for",
    "Verification rule",
    "`subagent-council`",
    "`subagent-council` custom agents",
    "Documentation skills",
    "Repo-specific skills",
    "Default receipt shape",
    "Extra validation notes",
    "Manual validation preferences",
    "Never assume",
    "Ask before",
    "Safe defaults",
}

SECRET_ASSIGNMENT = re.compile(
    r"(?i)\b(api[_-]?key|token|password|secret|private[_-]?key)\b\s*[:=]\s*\S+"
)


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")


def section_exists(text: str, section: str) -> bool:
    return re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE) is not None


def placeholder_lines(text: str) -> list[str]:
    placeholders: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^- \[[ xX]\]\s+", stripped):
            placeholders.append(stripped)
            continue
        match = re.match(r"^- (?P<label>[^:]+):\s*$", stripped)
        if match and match.group("label") in PLACEHOLDER_LABELS:
            placeholders.append(stripped)
    return placeholders


def memory_policy_ok(text: str) -> bool:
    lowered = text.lower()
    has_memory = "memory" in lowered
    optional = "optional" in lowered or "stable preferences" in lowered
    not_policy = "not policy" in lowered or "as policy" in lowered
    not_current = "current truth" in lowered or "current facts" in lowered
    return has_memory and optional and not_policy and not_current


def council_status() -> tuple[list[str], list[str]]:
    notes: list[str] = []
    gaps: list[str] = []
    home = codex_home()
    council_skill = home / "skills" / "subagent-council"
    agents_dir = home / "agents"

    if council_skill.is_dir():
        notes.append(f"subagent-council skill installed: {council_skill}")
        tomls = sorted(agents_dir.glob("*.toml")) if agents_dir.is_dir() else []
        if tomls:
            notes.append(f"custom agent TOMLs installed: {len(tomls)} in {agents_dir}")
        else:
            gaps.append(f"custom agent TOMLs missing under {agents_dir}")
            notes.append(
                "dry run: bash "
                f"{council_skill}/scripts/install-subagents.sh "
                "--recommended --dry-run --explain"
            )
    else:
        notes.append(f"subagent-council skill missing: {council_skill}")
    return notes, gaps


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check prompt-helper local personalization sufficiency."
    )
    parser.add_argument(
        "--skill-dir",
        default=".",
        help="Path to the prompt-helper skill directory.",
    )
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).expanduser().resolve()
    personalization = skill_dir / "references" / "personalization.local.md"

    if not personalization.is_file():
        print(f"MISSING personalization: {personalization}")
        return 2

    try:
        text = personalization.read_text(encoding="utf-8")
    except OSError as error:
        print(f"UNREADABLE personalization: {personalization}: {error}")
        return 2

    gaps: list[str] = []
    notes: list[str] = []

    for section in REQUIRED_SECTIONS:
        if not section_exists(text, section):
            gaps.append(f"missing section: {section}")

    placeholders = placeholder_lines(text)
    if placeholders:
        gaps.append("blank template placeholders remain:")
        gaps.extend(f"  {line}" for line in placeholders)

    if SECRET_ASSIGNMENT.search(text):
        gaps.append("possible secret assignment found")

    if not memory_policy_ok(text):
        gaps.append("memory policy must treat memory as optional context, not policy/current truth")

    council_notes, council_gaps = council_status()
    notes.extend(council_notes)
    gaps.extend(council_gaps)

    if gaps:
        print(f"INCOMPLETE personalization: {personalization}")
        for gap in gaps:
            print(f"- {gap}")
        for note in notes:
            print(f"NOTE: {note}")
        return 1

    print(f"SUFFICIENT personalization: {personalization}")
    for note in notes:
        print(f"NOTE: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
