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


    def test_phase9_observatorio_junior(self):
        x = guide("Sou novo e preciso corrigir um erro no Observatório Mandacaru")
        self.assertEqual(x["status"], "ready")
        self.assertEqual(x["intent"], "bugfix")
        self.assertIn("observatorio-mandacaru", x["skills"])
        self.assertFalse(x["task_execution_authorized"])

    def test_phase9_observatorio_indicators(self):
        x = guide("Implementar uma nova funcionalidade de indicadores no Observatório Mandacaru")
        self.assertEqual(x["status"], "ready")
        self.assertEqual(x["intent"], "feature")
        self.assertIn("observatorio-mandacaru", x["skills"])

    def test_phase9_observatorio_legislagd(self):
        x = guide("Implementar uma nova funcionalidade de integração entre Observatório Mandacaru e LegislaGD")
        self.assertEqual(x["status"], "ready")
        self.assertEqual(x["intent"], "feature")
        self.assertEqual(set(x["skills"]), {"sertaodigital-core", "observatorio-mandacaru", "legislagd"})
        self.assertFalse(x["task_execution_authorized"])

    def test_phase9_citizen_service_unknown(self):
        x = guide("Preciso corrigir atendimento ao cidadão")
        self.assertEqual(x["status"], "clarification_required")

    def test_phase9_ambiguous_intents(self):
        x = guide("Preciso corrigir e documentar o LegislaGD")
        self.assertEqual(x["status"], "clarification_required")
        self.assertEqual(x["intent"], "ambiguous")

    def test_phase9_legislagd_sigi(self):
        x = guide("Corrigir integração LegislaGD com SIGI-SD")
        self.assertEqual(x["status"], "review_required")
        self.assertIn("legislagd", x["skills"])
        self.assertTrue(x["unresolved"])

if __name__=="__main__":
    unittest.main()
