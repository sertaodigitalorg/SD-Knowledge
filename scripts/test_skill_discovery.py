"""Offline tests for conservative SDKA product discovery."""
import unittest
from sdka_skill_discovery import discover

class DiscoveryTests(unittest.TestCase):
    def test_legislagd(self):
        result=discover("Sou junior e preciso corrigir um bug no LegislaGD")
        self.assertEqual(result["status"],"ready")
        self.assertIn("legislagd",result["skills"])
        self.assertFalse(result["authorization_granted"])

    def test_observatorio(self):
        result=discover("Preciso estudar o Observatório Mandacaru")
        self.assertIn("observatorio-mandacaru",result["skills"])

    def test_no_guess_on_generic_atendimento(self):
        result=discover("Quero integrar o atendimento ao cidadão")
        self.assertEqual(result["status"],"clarification_required")

    def test_mixed_with_inactive_product_skill(self):
        result=discover("Integração LegislaGD com SIGI-SD")
        self.assertEqual(result["status"],"review_required")
        self.assertIn("legislagd",result["skills"])
        self.assertTrue(result["unresolved"])

    def test_unknown(self):
        result=discover("Criar uma solução interplanetária")
        self.assertEqual(result["status"],"clarification_required")

    def test_empty(self):
        result=discover(" ")
        self.assertEqual(result["reason"],"empty_request")

    def test_word_boundaries(self):
        result=discover("Metalegislagdista desconhecido")
        self.assertEqual(result["status"],"clarification_required")

if __name__=="__main__":
    unittest.main()
