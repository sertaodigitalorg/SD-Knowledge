#!/usr/bin/env python3
"""Validate SDKA's canonical skill bootstrap and active skill paths offline."""
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check_bootstrap(root=ROOT):
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    index = yaml.safe_load((root / "knowledge.yaml").read_text(encoding="utf-8"))
    workflow = "skills/sertaodigital-core/workflows/skill-routing-and-onboarding.md"
    assert workflow in agents, "AGENTS.md does not route through the core onboarding workflow"
    assert (root / workflow).is_file(), "core onboarding workflow is missing"
    skills = index["knowledge_architecture"]
    active = [s for s in skills if s.get("status") == "active"]
    assert any(s["name"] == "sertaodigital-core" for s in active), "missing active core skill"
    for entry in active:
        skill_file = root / entry["location"] / "SKILL.md"
        assert skill_file.is_file(), "missing active skill file: " + entry["name"]
        if entry["name"] != "sertaodigital-core":
            assert "sertaodigital-core" in entry.get("depends_on", []), "core dependency missing"
    assert not any(s["name"] == "sdka-engineering-intelligence" and s.get("status") == "active" for s in skills), "experimental skill activated prematurely"


class BootstrapTests(unittest.TestCase):
    def test_bootstrap(self):
        check_bootstrap()


if __name__ == "__main__":
    unittest.main()
