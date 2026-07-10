#!/usr/bin/env python3
"""Install bundled Codex custom agents for the subagent-council skill."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback.
    tomllib = None


SCAN_EXTENSIONS = {
    ".json",
    ".md",
    ".markdown",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
SCAN_CHAR_LIMIT = 2_000_000


@dataclass(frozen=True)
class Agent:
    name: str
    filename: str


@dataclass(frozen=True)
class ModelConfiguration:
    model: str | None
    reasoning_effort: str


AGENTS = [
    Agent("repo_cartographer", "repo-cartographer.toml"),
    Agent("product_architect", "product-architect.toml"),
    Agent("docs_oracle", "docs-oracle.toml"),
    Agent("implementation_surgeon", "implementation-surgeon.toml"),
    Agent("test_sentinel", "test-sentinel.toml"),
    Agent("api_contract_keeper", "api-contract-keeper.toml"),
    Agent("security_privacy_guardian", "security-privacy-guardian.toml"),
    Agent("ux_accessibility_reviewer", "ux-accessibility-reviewer.toml"),
    Agent("performance_dx_reviewer", "performance-dx-reviewer.toml"),
    Agent("docs_writer", "docs-writer.toml"),
    Agent("release_captain", "release-captain.toml"),
    Agent("final_reviewer", "final-reviewer.toml"),
]

AGENT_BY_NAME = {agent.name: agent for agent in AGENTS}
AGENT_BY_FILE_STEM = {agent.filename.removesuffix(".toml").replace("-", "_"): agent for agent in AGENTS}
CORE_AGENT_NAMES = {
    "repo_cartographer",
    "implementation_surgeon",
    "test_sentinel",
    "final_reviewer",
}

ROLE_REASONING_EFFORTS = {
    "repo_cartographer": "medium",
    "product_architect": "xhigh",
    "docs_oracle": "medium",
    "implementation_surgeon": "medium",
    "test_sentinel": "medium",
    "api_contract_keeper": "high",
    "security_privacy_guardian": "high",
    "ux_accessibility_reviewer": "medium",
    "performance_dx_reviewer": "medium",
    "docs_writer": "medium",
    "release_captain": "medium",
    "final_reviewer": "medium",
}

MODEL_PROFILES = {
    "gpt-5.6": {
        "repo_cartographer": ModelConfiguration("gpt-5.6-luna", "medium"),
        "product_architect": ModelConfiguration("gpt-5.6-sol", "xhigh"),
        "docs_oracle": ModelConfiguration("gpt-5.6-terra", "medium"),
        "implementation_surgeon": ModelConfiguration("gpt-5.6-terra", "medium"),
        "test_sentinel": ModelConfiguration("gpt-5.6-terra", "medium"),
        "api_contract_keeper": ModelConfiguration("gpt-5.6-sol", "high"),
        "security_privacy_guardian": ModelConfiguration("gpt-5.6-sol", "high"),
        "ux_accessibility_reviewer": ModelConfiguration("gpt-5.6-sol", "medium"),
        "performance_dx_reviewer": ModelConfiguration("gpt-5.6-sol", "medium"),
        "docs_writer": ModelConfiguration("gpt-5.6-terra", "medium"),
        "release_captain": ModelConfiguration("gpt-5.6-sol", "medium"),
        "final_reviewer": ModelConfiguration("gpt-5.6-sol", "medium"),
    },
    "inherit": {
        agent.name: ModelConfiguration(None, ROLE_REASONING_EFFORTS[agent.name])
        for agent in AGENTS
    },
}


def validate_model_profiles() -> None:
    expected_names = {agent.name for agent in AGENTS}
    for profile_name, configurations in MODEL_PROFILES.items():
        actual_names = set(configurations)
        if actual_names != expected_names:
            missing = ", ".join(sorted(expected_names - actual_names)) or "none"
            extra = ", ".join(sorted(actual_names - expected_names)) or "none"
            raise RuntimeError(
                f"Model profile '{profile_name}' is incomplete: missing {missing}; extra {extra}."
            )


validate_model_profiles()

SIGNAL_RULES = [
    (
        "Angular/Node/docs",
        "docs_oracle",
        [
            "angular",
            "typescript",
            "node",
            "npm",
            "firebase",
            "openai",
            "codex",
            "api",
            "sdk",
            "cli",
            "official docs",
        ],
    ),
    (
        "Architecture/scope",
        "product_architect",
        [
            "architecture",
            "design",
            "mvp",
            "scope",
            "refactor",
            "migration",
            "tradeoff",
        ],
    ),
    (
        "API/data contracts",
        "api_contract_keeper",
        [
            "express",
            "route",
            "endpoint",
            "schema",
            "database",
            "postgres",
            "sqlite",
            "firebase function",
            "env var",
            "config",
            "persistence",
        ],
    ),
    (
        "Security/privacy",
        "security_privacy_guardian",
        [
            "secret",
            "password",
            "token",
            "auth",
            "oauth",
            "api key",
            "credential",
            "privacy",
            "pii",
            "log",
            "storage",
            "upload",
        ],
    ),
    (
        "UI/a11y",
        "ux_accessibility_reviewer",
        [
            "ui",
            "ux",
            "component",
            "form",
            "modal",
            "dialog",
            "keyboard",
            "focus",
            "accessibility",
            "a11y",
            "screen reader",
        ],
    ),
    (
        "Performance/DX",
        "performance_dx_reviewer",
        [
            "performance",
            "perf",
            "slow",
            "latency",
            "bundle",
            "build",
            "dx",
            "developer experience",
            "script",
            "dev server",
            "test speed",
        ],
    ),
    (
        "Docs",
        "docs_writer",
        [
            "readme",
            "documentation",
            "docs",
            "adr",
            "changelog",
            "migration note",
            "release note",
            "markdownlint",
        ],
    ),
    (
        "Release/PR",
        "release_captain",
        [
            "release",
            "version",
            "semver",
            "rc",
            "pr",
            "pull request",
            "npm publish",
            "tag",
            "changelog",
        ],
    ),
]

FOCUS_NOTES = {
    "Angular/Node/docs": "Verify version-sensitive APIs against official docs before coding.",
    "Architecture/scope": "Separate v1 scope from migration or refactor follow-ups.",
    "API/data contracts": "Name request, response, schema, env, and persistence impacts explicitly.",
    "Security/privacy": "Treat logs, fixtures, examples, screenshots, and docs as leak surfaces.",
    "UI/a11y": "Check keyboard flow, focus, labels, semantics, copy, and error states.",
    "Performance/DX": "Measure slow paths before optimizing and keep tooling lightweight.",
    "Docs": "Keep docs compact, command-tested, and free of private context.",
    "Release/PR": "Name validation, versioning, rollback, and release-readiness gaps.",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recommended", action="store_true", help="Install core agents plus memory-selected specialists.")
    parser.add_argument("--all", action="store_true", help="Install all bundled agents.")
    parser.add_argument("--installed", action="store_true", help="Refresh bundled agents already present in the target directory.")
    parser.add_argument("--agent", action="append", default=[], help="Install only the named agent. May be repeated.")
    parser.add_argument(
        "--model-profile",
        choices=MODEL_PROFILES,
        default="gpt-5.6",
        help="Role-optimized model profile to render (default: gpt-5.6).",
    )
    parser.add_argument("--list-model-profiles", action="store_true", help="List model profiles and exit.")
    parser.add_argument("--target", default=str(Path.home() / ".codex" / "agents"), help="Target directory for custom agent TOML files.")
    parser.add_argument("--memory-dir", default=str(Path.home() / ".codex" / "memories"), help="Memory directory to scan read-only.")
    parser.add_argument("--memory-archive", help="Optional memories.zip archive to scan read-only.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing agent files.")
    parser.add_argument("--backup", action="store_true", help="Back up existing files before overwriting.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files.")
    parser.add_argument("--explain", action="store_true", help="Print selection inputs and detected categories.")
    parser.add_argument("--list", action="store_true", help="List bundled agents and exit.")
    parser.add_argument("--no-personalize", action="store_true", help="Do not append memory-derived category focus notes.")
    args = parser.parse_args()

    selected_modes = sum([args.recommended, args.all, args.installed, bool(args.agent)])
    if selected_modes > 1:
        parser.error("Choose only one of --recommended, --all, --installed, or --agent.")
    return args


def skill_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def templates_dir() -> Path:
    return skill_dir() / "assets" / "agents"


def normalized_agent_name(raw_name: str) -> str:
    return raw_name.strip().replace("-", "_")


def resolve_agent(raw_name: str) -> Agent:
    name = normalized_agent_name(raw_name)
    agent = AGENT_BY_NAME.get(name) or AGENT_BY_FILE_STEM.get(name)
    if agent is None:
        valid = ", ".join(agent.name for agent in AGENTS)
        raise SystemExit(f"Unknown agent '{raw_name}'. Valid agents: {valid}")
    return agent


def read_text_file(path: Path, limit: int) -> str:
    if limit <= 0:
        return ""
    try:
        data = path.read_bytes()[:limit]
    except OSError:
        return ""
    return data.decode("utf-8", errors="ignore")


def collect_memory_from_dir(memory_dir: Path) -> str:
    if not memory_dir.is_dir():
        return ""

    chunks: list[str] = []
    remaining = SCAN_CHAR_LIMIT
    for path in sorted(memory_dir.rglob("*")):
        if remaining <= 0:
            break
        if not path.is_file() or path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        text = read_text_file(path, remaining)
        if not text:
            continue
        chunks.append(text)
        remaining -= len(text)
    return "\n".join(chunks)[:SCAN_CHAR_LIMIT]


def collect_memory_from_zip(archive_path: Path) -> str:
    if not archive_path.is_file():
        raise SystemExit(f"Memory archive not found: {archive_path}")

    chunks: list[str] = []
    remaining = SCAN_CHAR_LIMIT
    with zipfile.ZipFile(archive_path) as archive:
        for member in sorted(archive.infolist(), key=lambda item: item.filename):
            if remaining <= 0:
                break
            suffix = Path(member.filename).suffix.lower()
            if member.is_dir() or suffix not in SCAN_EXTENSIONS:
                continue
            with archive.open(member) as stream:
                data = stream.read(remaining)
            text = data.decode("utf-8", errors="ignore")
            if not text:
                continue
            chunks.append(text)
            remaining -= len(text)
    return "\n".join(chunks)[:SCAN_CHAR_LIMIT]


def collect_memory_text(args: argparse.Namespace) -> tuple[str, str]:
    if args.memory_archive:
        archive = Path(args.memory_archive).expanduser()
        return collect_memory_from_zip(archive), str(archive)

    memory_dir = Path(args.memory_dir).expanduser()
    return collect_memory_from_dir(memory_dir), str(memory_dir)


def term_matches(text: str, term: str) -> bool:
    escaped = re.escape(term.casefold())
    if " " in term:
        pattern = escaped
    else:
        pattern = rf"\b{escaped}\b"
    return re.search(pattern, text) is not None


def detect_signals(memory_text: str) -> list[str]:
    haystack = memory_text.casefold()
    detected: list[str] = []
    for category, _agent_name, terms in SIGNAL_RULES:
        if any(term_matches(haystack, term) for term in terms):
            detected.append(category)
    return detected


def selected_agents(args: argparse.Namespace, signals: list[str], target_dir: Path) -> list[Agent]:
    if args.list or args.list_model_profiles:
        return []

    if args.all:
        selected_names = {agent.name for agent in AGENTS}
    elif args.installed:
        selected_names = {
            agent.name
            for agent in AGENTS
            if (target_dir / agent.filename).is_file()
        }
    elif args.agent:
        selected_names = {resolve_agent(name).name for name in args.agent}
    else:
        selected_names = set(CORE_AGENT_NAMES)
        signal_agents = {
            agent_name
            for category, agent_name, _terms in SIGNAL_RULES
            if category in signals
        }
        selected_names.update(signal_agents)

    return [agent for agent in AGENTS if agent.name in selected_names]


def memory_appendix(signals: list[str], personalize: bool) -> str:
    if not personalize or not signals:
        return ""

    notes = [FOCUS_NOTES[signal] for signal in signals if signal in FOCUS_NOTES]
    if not notes:
        return ""

    lines = [
        "",
        "Memory-derived focus:",
        *[f"- {note}" for note in notes],
        "",
        "Do not quote or expose raw memory contents. Treat memory as recall, not policy.",
    ]
    return "\n".join(lines)


def model_configuration(agent: Agent, profile_name: str) -> ModelConfiguration:
    return MODEL_PROFILES[profile_name][agent.name]


def render_model_configuration(configuration: ModelConfiguration) -> str:
    lines = []
    if configuration.model is not None:
        lines.append(f'model = "{configuration.model}"')
    lines.append(f'model_reasoning_effort = "{configuration.reasoning_effort}"')
    return "\n".join(lines)


def render_template(agent: Agent, appendix: str, profile_name: str) -> str:
    path = templates_dir() / agent.filename
    if not path.is_file():
        raise SystemExit(f"Missing template for {agent.name}: {path}")
    content = path.read_text(encoding="utf-8")
    if content.count("{{MODEL_CONFIGURATION}}") != 1:
        raise SystemExit(f"Expected one model configuration marker in {agent.filename}")
    rendered = content.replace("{{MEMORY_PROFILE_APPENDIX}}", appendix).replace(
        "{{MODEL_CONFIGURATION}}",
        render_model_configuration(model_configuration(agent, profile_name)),
    )
    if "{{" in rendered or "}}" in rendered:
        raise SystemExit(f"Unresolved template placeholder in {agent.filename}")
    validate_toml(rendered, agent.filename)
    return rendered


def validate_toml(content: str, filename: str) -> None:
    if tomllib is None:
        return
    try:
        tomllib.loads(content)
    except Exception as exc:
        raise SystemExit(f"Invalid TOML in {filename}: {exc}") from exc


def backup_path(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = path.with_name(f"{path.name}.bak.{timestamp}")
    counter = 1
    while candidate.exists():
        counter += 1
        candidate = path.with_name(f"{path.name}.bak.{timestamp}.{counter}")
    return candidate


def install_agent(agent: Agent, content: str, target_dir: Path, args: argparse.Namespace) -> str:
    target = target_dir / agent.filename
    if target.exists() and not args.force:
        return f"skip existing {target}"

    if args.dry_run:
        if target.exists() and args.force and args.backup:
            return f"would back up and write {target}"
        if target.exists() and args.force:
            return f"would overwrite {target}"
        return f"would write {target}"

    target_dir.mkdir(parents=True, exist_ok=True)
    if target.exists() and args.force and args.backup:
        shutil.copy2(target, backup_path(target))
    target.write_text(content, encoding="utf-8")
    return f"wrote {target}"


def print_list() -> None:
    for agent in AGENTS:
        print(f"{agent.name:<28} {agent.filename}")


def model_label(configuration: ModelConfiguration) -> str:
    return configuration.model or "inherit (parent session)"


def print_model_profiles() -> None:
    for profile_name, configurations in MODEL_PROFILES.items():
        print(profile_name)
        for agent in AGENTS:
            configuration = configurations[agent.name]
            print(
                f"  {agent.name:<28} "
                f"model={model_label(configuration)}, "
                f"effort={configuration.reasoning_effort}"
            )


def print_explain(args: argparse.Namespace, memory_source: str, signals: list[str], agents: list[Agent]) -> None:
    print(f"Skill directory: {skill_dir()}")
    print(f"Template directory: {templates_dir()}")
    print(f"Target directory: {Path(args.target).expanduser()}")
    print(f"Model profile: {args.model_profile}")
    print(f"Memory source: {memory_source}")
    print("Detected categories:")
    if signals:
        for signal in signals:
            print(f"- {signal}")
    else:
        print("- none")
    print("Selected agents:")
    if agents:
        for agent in agents:
            configuration = model_configuration(agent, args.model_profile)
            print(
                f"- {agent.name}: model={model_label(configuration)}, "
                f"effort={configuration.reasoning_effort}"
            )
    else:
        print("- none")


def main() -> int:
    args = parse_args()
    if args.list:
        print_list()
        return 0
    if args.list_model_profiles:
        print_model_profiles()
        return 0

    memory_text, memory_source = collect_memory_text(args)
    signals = detect_signals(memory_text)
    target_dir = Path(args.target).expanduser()
    agents = selected_agents(args, signals, target_dir)
    appendix = memory_appendix(signals, personalize=not args.no_personalize)

    if args.explain:
        print_explain(args, memory_source, signals, agents)

    if args.installed and not agents:
        print(f"no installed bundled agents in {target_dir}")
        return 0

    for agent in agents:
        content = render_template(agent, appendix, args.model_profile)
        print(install_agent(agent, content, target_dir, args))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
