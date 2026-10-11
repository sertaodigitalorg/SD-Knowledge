"""Testa cobertura integral do inventário SDKA a partir de fontes canônicas."""
import unittest
from sdka_product_inventory import inventory
from sdka_registry_gate import load_registry

class InventoryTests(unittest.TestCase):
    def test_every_registered_product_is_included(self):
        data=inventory()
        _,products,_=load_registry()
        self.assertEqual({p["product_id"] for p in data["products"]},set(products))

    def test_active_product_skills(self):
        rows={p["product_id"]:p for p in inventory()["products"]}
        self.assertEqual(rows["legislagd"]["skill"],"legislagd")
        self.assertEqual(rows["observatorio_mandacaru"]["skill"],"observatorio-mandacaru")

    def test_child_inherits_existing_parent_skill(self):
        rows={p["product_id"]:p for p in inventory()["products"]}
        for key in ("sapl_sd","portalmodelo_sd","ecidade_sd"):
            self.assertEqual(rows[key]["skill"],"legislagd")
            self.assertEqual(rows[key]["parent_product"],"legislagd")

    def test_missing_skill_is_not_activated(self):
        rows={p["product_id"]:p for p in inventory()["products"]}
        for key in ("sigi_sd","veredas"):
            self.assertIsNone(rows[key]["skill"])
            self.assertEqual(rows[key]["context_status"],"institutional_only")

    def test_pending_products_are_not_promoted(self):
        rows={p["product_id"]:p for p in inventory()["products"]}
        for key in ("plataforma360","noticia_sertaneja","roteiro_comercial"):
            self.assertEqual(rows[key]["context_status"],"pending_validation")
            self.assertFalse(rows[key]["implementation_verified"])

    def test_inventory_has_no_implementation_claims(self):
        self.assertTrue(all(not p["implementation_verified"] for p in inventory()["products"]))

if __name__=="__main__":
    unittest.main()
