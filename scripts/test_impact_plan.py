"""Regression tests for read-only SDKA impact planning."""
import unittest
from sdka_impact_plan import plan

class ImpactPlanTests(unittest.TestCase):
    def test_legislative_component_family(self):
        result=plan(["sapl_sd"])
        affected=result["affected_products"][0]
        self.assertEqual(affected["parent_product"],"legislagd")
        self.assertIn("portalmodelo_sd",affected["related_product_ids"])
        self.assertEqual(affected["active_product_skill"],"legislagd")
        self.assertTrue(result["cross_layer_impact_check_required"])

    def test_missing_product_skill(self):
        result=plan(["sigi_sd", "veredas"])
        self.assertEqual(len(result["affected_products"]),2)
        self.assertTrue(all(x["active_product_skill"] is None for x in result["affected_products"]))
        self.assertFalse(result["authorization_granted"])

    def test_reject_unknown_product(self):
        with self.assertRaises(ValueError):
            plan(["unknown_product"])

    def test_reject_empty_input(self):
        with self.assertRaises(ValueError):
            plan([])

    def test_deduplication_and_no_autoapproval(self):
        result=plan(["legislagd","legislagd"])
        self.assertEqual(len(result["affected_products"]),1)
        self.assertEqual(result["status"],"review_required")
        self.assertTrue(result["affected_products"][0]["review_required"])
        self.assertFalse(result["affected_products"][0]["impact_assessed_against_code"])

if __name__=="__main__":
    unittest.main()
