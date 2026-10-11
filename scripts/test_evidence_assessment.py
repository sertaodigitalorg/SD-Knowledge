"""Testes offline das lacunas por evidências declaradas."""
import copy
import json
import unittest
from pathlib import Path
from sdka_evidence_assessment import assess

ROOT=Path(__file__).resolve().parents[1]
FIXTURE=json.loads((ROOT/"examples/engineering-assessment.example.json").read_text(encoding="utf-8"))

class EvidenceAssessmentTests(unittest.TestCase):
    def test_institutional_fixture(self):
        result=assess(copy.deepcopy(FIXTURE))
        self.assertEqual(result["status"],"review_required")
        self.assertFalse(result["verified_against_source"])
        self.assertFalse(result["authorization_granted"])

    def test_legislagd_mapping(self):
        data=copy.deepcopy(FIXTURE)
        data["product_context"]={"repository":"sertaodigitalorg/LegislaGD","skill":"legislagd"}
        self.assertEqual(assess(data)["skill"],"legislagd")

    def test_mandacaru_mapping(self):
        data=copy.deepcopy(FIXTURE)
        data["product_context"]={"repository":"sertaodigitalorg/ObservatorioMandacaru","skill":"observatorio-mandacaru"}
        self.assertEqual(assess(data)["skill"],"observatorio-mandacaru")

    def test_reject_unknown_evidence(self):
        data=copy.deepcopy(FIXTURE)
        data["gaps"][0]["evidence_refs"]=["UNKNOWN"]
        with self.assertRaises(ValueError):
            assess(data)

    def test_reject_unconfirmed_met(self):
        data=copy.deepcopy(FIXTURE)
        data["evidence"][0]["confidence"]="inferred"
        with self.assertRaises(ValueError):
            assess(data)

    def test_reject_false_approval(self):
        data=copy.deepcopy(FIXTURE)
        data["decision"]="accepted"
        with self.assertRaises(ValueError):
            assess(data)

    def test_reject_unregistered_product(self):
        data=copy.deepcopy(FIXTURE)
        data["product_context"]["repository"]="sertaodigitalorg/Unknown"
        with self.assertRaises(AssertionError):
            assess(data)

if __name__=="__main__":
    unittest.main()
