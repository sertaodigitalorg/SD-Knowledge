"""Ensure preliminary product skills are present but cannot be routed as active."""
import unittest
from pathlib import Path
from sdka_registry_gate import ROOT, load_registry
from sdka_skill_router import route

class ScaffoldTests(unittest.TestCase):
    def test_initial_skills_not_activated(self):
        _, products, skills = load_registry()
        registered = {s["name"] for s in skills if s.get("status") == "active"}
        for key, name, repo in [
            ("sigi_sd", "sigi-sd", "sertaodigitalorg/SIGI-SD"),
            ("veredas", "veredas", "sertaodigitalorg/VEREDAS"),
        ]:
            self.assertIn(key, products)
            self.assertNotIn(name, registered)
            skill_file = ROOT / "skills" / name / "SKILL.md"
            self.assertTrue(skill_file.is_file())
            self.assertIn("**Status:** inactive", skill_file.read_text(encoding="utf-8"))
            result = route([repo])
            self.assertEqual(result["status"], "review_required")
            self.assertEqual(result["skills"], ["sertaodigital-core"])

if __name__ == "__main__":
    unittest.main()
