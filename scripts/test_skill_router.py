"""Offline tests for canonical SDKA skill router."""
import unittest
from sdka_skill_router import route

class SkillRouterTests(unittest.TestCase):
    def test_legislagd_junior(self):
        x=route(["sertaodigitalorg/LegislaGD"])
        self.assertEqual(x["status"],"ready")
        self.assertEqual(x["skills"],["sertaodigital-core","legislagd"])
        self.assertTrue(x["guidance"])

    def test_observatorio(self):
        x=route(["sertaodigitalorg/ObservatorioMandacaru"])
        self.assertIn("observatorio-mandacaru",x["skills"])

    def test_cross_product(self):
        x=route(["sertaodigitalorg/LegislaGD","sertaodigitalorg/ObservatorioMandacaru"])
        self.assertEqual(x["skills"],["sertaodigital-core","legislagd","observatorio-mandacaru"])
        self.assertEqual(x["status"],"ready")

    def test_duplicate(self):
        x=route(["sertaodigitalorg/LegislaGD","sertaodigitalorg/LegislaGD"])
        self.assertEqual(x["skills"].count("legislagd"),1)

    def test_unknown_fails_closed(self):
        x=route(["sertaodigitalorg/InventedRepo"])
        self.assertEqual(x["status"],"review_required")
        self.assertEqual(x["skills"],["sertaodigital-core"])

    def test_registered_but_no_skill(self):
        x=route(["sertaodigitalorg/SIGI-SD"])
        self.assertEqual(x["status"],"review_required")
        self.assertNotIn("sigi-sd",x["skills"])

    def test_mixed_scope_requires_review(self):
        x=route(["sertaodigitalorg/LegislaGD","sertaodigitalorg/SIGI-SD"])
        self.assertEqual(x["status"],"review_required")
        self.assertIn("legislagd",x["skills"])
        self.assertEqual(len(x["unresolved"]),1)

    def test_institutional_only(self):
        x=route(["sertaodigitalorg/SD-Knowledge"])
        self.assertEqual(x["skills"],["sertaodigital-core"])
        self.assertEqual(x["status"],"ready")

if __name__=="__main__":
    unittest.main()
