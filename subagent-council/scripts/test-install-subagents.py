#!/usr/bin/env python3
"""Regression tests for the subagent-council installer."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback.
    tomllib = None


SKILL_DIR = Path(__file__).resolve().parent.parent
INSTALLER = SKILL_DIR / "scripts" / "install-subagents.py"

GPT_5_6_PROFILE = {
    "repo-cartographer.toml": ("gpt-5.6-luna", "medium"),
    "product-architect.toml": ("gpt-5.6-sol", "xhigh"),
    "docs-oracle.toml": ("gpt-5.6-terra", "medium"),
    "implementation-surgeon.toml": ("gpt-5.6-terra", "medium"),
    "test-sentinel.toml": ("gpt-5.6-terra", "medium"),
    "api-contract-keeper.toml": ("gpt-5.6-sol", "high"),
    "security-privacy-guardian.toml": ("gpt-5.6-sol", "high"),
    "ux-accessibility-reviewer.toml": ("gpt-5.6-sol", "medium"),
    "performance-dx-reviewer.toml": ("gpt-5.6-sol", "medium"),
    "docs-writer.toml": ("gpt-5.6-terra", "medium"),
    "release-captain.toml": ("gpt-5.6-sol", "medium"),
    "final-reviewer.toml": ("gpt-5.6-sol", "medium"),
}


def run_installer(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), *args],
        check=check,
        capture_output=True,
        text=True,
    )


class InstallSubagentsTest(unittest.TestCase):
    def parse_toml(self, path: Path) -> dict[str, object]:
        if tomllib is None:
            self.skipTest("TOML parsing validation requires Python 3.11 or newer.")
        return tomllib.loads(path.read_text(encoding="utf-8"))

    def render_all(self, profile: str, target: Path, memory_dir: Path) -> None:
        run_installer(
            "--all",
            "--model-profile",
            profile,
            "--target",
            str(target),
            "--memory-dir",
            str(memory_dir),
            "--no-personalize",
        )

    def test_model_profiles_render_valid_toml(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            memory_dir = root / "memory"
            memory_dir.mkdir()

            for profile in ("gpt-5.6", "inherit"):
                target = root / profile
                self.render_all(profile, target, memory_dir)
                self.assertEqual({path.name for path in target.glob("*.toml")}, set(GPT_5_6_PROFILE))

                for filename, (model, effort) in GPT_5_6_PROFILE.items():
                    parsed = self.parse_toml(target / filename)
                    self.assertEqual(parsed["model_reasoning_effort"], effort)
                    if profile == "gpt-5.6":
                        self.assertEqual(parsed["model"], model)
                    else:
                        self.assertNotIn("model", parsed)

    def test_installed_refresh_preserves_unrelated_agents_and_backs_up(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "agents"
            target.mkdir()
            memory_dir = root / "memory"
            memory_dir.mkdir()
            selected = ["repo-cartographer.toml", "final-reviewer.toml"]
            for filename in selected:
                shutil.copy2(SKILL_DIR / "assets" / "agents" / filename, target / filename)

            unrelated = target / "unrelated-agent.toml"
            unrelated.write_text('name = "unrelated"\n', encoding="utf-8")

            preview = run_installer(
                "--installed",
                "--target",
                str(target),
                "--memory-dir",
                str(memory_dir),
                "--no-personalize",
                "--dry-run",
                "--explain",
            )
            self.assertIn("Model profile: gpt-5.6", preview.stdout)
            self.assertIn("repo_cartographer: model=gpt-5.6-luna, effort=medium", preview.stdout)
            self.assertIn("skip existing", preview.stdout)

            run_installer(
                "--installed",
                "--target",
                str(target),
                "--memory-dir",
                str(memory_dir),
                "--no-personalize",
                "--backup",
                "--force",
            )

            self.assertEqual(unrelated.read_text(encoding="utf-8"), 'name = "unrelated"\n')
            self.assertFalse((target / "product-architect.toml").exists())
            for filename in selected:
                self.assertTrue(list(target.glob(f"{filename}.bak.*")))
                parsed = self.parse_toml(target / filename)
                self.assertEqual(parsed["model"], GPT_5_6_PROFILE[filename][0])

    def test_installed_mode_is_a_safe_empty_no_op(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "agents"
            memory_dir = root / "memory"
            memory_dir.mkdir()

            result = run_installer(
                "--installed",
                "--target",
                str(target),
                "--memory-dir",
                str(memory_dir),
                "--no-personalize",
            )

            self.assertIn("no installed bundled agents", result.stdout)
            self.assertFalse(target.exists())

    def test_profile_listing_does_not_read_memory(self) -> None:
        result = run_installer(
            "--list-model-profiles",
            "--memory-archive",
            "/path/that/does/not/exist.zip",
        )

        self.assertIn("gpt-5.6", result.stdout)
        self.assertIn("inherit", result.stdout)
        self.assertIn("repo_cartographer", result.stdout)

    def test_installed_mode_is_exclusive(self) -> None:
        result = run_installer("--installed", "--all", check=False)

        self.assertEqual(result.returncode, 2)
        self.assertIn("Choose only one", result.stderr)


if __name__ == "__main__":
    unittest.main()
