"""Testes offline de orientacao de tarefas SDKA."""
import unittest
from sdka_task_guidance import classify, guide

class TaskGuidanceTests(unittest.TestCase):
    def test_bugfix(self):
        x=guide("Sou novo e preciso corrigir um erro no LegislaGD")
        self.assertEqual(x["intent"],"bugfix")
        self.assertEqual(x["status"],"ready")
        self.assertIn("legislagd",x["skills"])
        self.assertFalse(x["task_execution_authorized"])

    def test_feature(self):
        x=guide("Implementar uma nova funcionalidade no LegislaGD")
        self.assertEqual(x["intent"],"feature")
        self.assertTrue(x["task_steps"])

    def test_documentation(self):
        self.assertEqual(classify("Documentar o Observatório Mandacaru"),"documentation")

    def test_architecture(self):
        self.assertEqual(classify("Revisar arquitetura do LegislaGD"),"architecture")

    def test_study(self):
        self.assertEqual(classify("Quero estudar o LegislaGD"),"learning")

    def test_no_product(self):
        x=guide("Preciso corrigir um bug")
        self.assertEqual(x["status"],"clarification_required")

    def test_unregistered_product(self):
        x=guide("Corrigir erro no SIGI-SD")
        self.assertEqual(x["status"],"review_required")

    def test_ambiguous(self):
        x=guide("Preciso corrigir e documentar o LegislaGD")
        self.assertEqual(x["intent"],"ambiguous")
        self.assertEqual(x["status"],"clarification_required")

if __name__=="__main__":
    unittest.main()
