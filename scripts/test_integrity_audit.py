"""Phase 12 integrity regression tests; never use network."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import yaml
from sdka_integrity_audit import audit, load_registry, ROOT

class IntegrityAuditTests(unittest.TestCase):
    def test_repository_catalog(self):
        result = audit()
        self.assertEqual(result["status"], "pass", result["issues"])
        self.assertFalse(result["external_sources_verified"])
        self.assertFalse(result["actions_authorized"])

    def test_missing_parent_fails(self):
        repos, products, skills = load_registry()
        products["sapl_sd"] = dict(products["sapl_sd"], parent_product="missing")
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("UNKNOWN_PARENT", {i["code"] for i in r["issues"]})

    def test_missing_active_dependency_fails(self):
        repos, products, skills = load_registry()
        skills = [dict(s, depends_on=["unknown-core"]) if s["name"] == "legislagd" else s for s in skills]
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("MISSING_ACTIVE_DEPENDENCY", {i["code"] for i in r["issues"]})

    def test_unregistered_repository_fails(self):
        repos, products, skills = load_registry()
        products["sigi_sd"] = dict(products["sigi_sd"], repository="https://github.com/sertaodigitalorg/NotCatalogued")
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("UNREGISTERED_REPOSITORY", {i["code"] for i in r["issues"]})

    def test_missing_skill_file_fails(self):
        repos, products, skills = load_registry()
        skills = [dict(s, location="skills/not-here/") if s["name"] == "legislagd" else s for s in skills]
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("MISSING_SKILL_FILE", {i["code"] for i in r["issues"]})

    def test_product_skill_without_core_fails(self):
        repos, products, skills = load_registry()
        skills = [dict(s, depends_on=[]) if s["name"] == "legislagd" else s for s in skills]
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("MISSING_INSTITUTIONAL_CORE", {i["code"] for i in r["issues"]})

    def test_duplicate_active_repository_fails(self):
        repos, products, skills = load_registry()
        repos = dict(repos)
        repos["duplicate_sigi"] = dict(repos["sigi_sd"])
        with patch("sdka_integrity_audit.load_registry", return_value=(repos, products, skills)):
            r = audit()
        self.assertIn("DUPLICATE_REPOSITORY", {i["code"] for i in r["issues"]})

if __name__ == "__main__":
    unittest.main()
