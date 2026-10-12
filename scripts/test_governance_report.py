"""Testes offline do relatório de governança institucional SDKA."""
import unittest
from sdka_governance_report import report
from sdka_registry_gate import load_registry

class GovernanceReportTests(unittest.TestCase):
    def test_covers_canonical_catalog(self):
        result = report()
        _, products, _ = load_registry()
        self.assertEqual(set(products), {item["product_id"] for item in result["products"]})
        self.assertEqual(result["counts"]["products"], len(products))
    def test_does_not_claim_external_validation(self):
        result = report()
        self.assertFalse(result["external_evidence_verified"])
        self.assertFalse(result["automated_approval"])
        self.assertTrue(all(not item["implementation_verified"] for item in result["products"]))
    def test_missing_product_skill_requires_review(self):
        items = {r["product_id"]: r for r in report()["products"]}
        self.assertTrue(items["sigi_sd"]["review_required"])
        self.assertTrue(items["veredas"]["review_required"])
        self.assertIsNone(items["sigi_sd"]["context_skill"])
    def test_active_product_scopes(self):
        items = {r["product_id"]: r for r in report()["products"]}
        self.assertEqual(items["legislagd"]["context_skill"], "legislagd")
        self.assertEqual(items["observatorio_mandacaru"]["context_skill"], "observatorio-mandacaru")
    def test_sorted_deterministic(self):
        keys = [p["product_id"] for p in report()["products"]]
        self.assertEqual(keys, sorted(keys))
if __name__ == "__main__":
    unittest.main()
