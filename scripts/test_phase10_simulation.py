#!/usr/bin/env python3
"""Offline phase 10 simulation; no live products, network, or authorization."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from sdka_task_guidance import guide

CASES = [
 ("A", "Sou novo no Sertão Digital e preciso corrigir um erro no LegislaGD", "ready", "bugfix", {"sertaodigital-core","legislagd"}),
 ("B", "Sou novo no Sertão Digital e preciso implementar uma funcionalidade de indicadores no Observatório Mandacaru", "ready", "feature", {"sertaodigital-core","observatorio-mandacaru"}),
 ("C", "Preciso desenvolver uma integração entre LegislaGD e Observatório Mandacaru", "clarification_required", "unspecified", {"sertaodigital-core","legislagd","observatorio-mandacaru"}),
 ("D", "Preciso corrigir um erro no SIGI-SD", "review_required", "bugfix", {"sertaodigital-core"}),
]

def simulate():
    report=[]
    for code,prompt,expected_status,expected_intent,expected_skills in CASES:
        result=guide(prompt, "junior")
        passed=(result["status"]==expected_status and result["intent"]==expected_intent
                and set(result["skills"])==expected_skills
                and result.get("task_execution_authorized") is False)
        report.append({"case":code,"passed":passed,"expected_status":expected_status,
                       "actual_status":result["status"],"intent":result["intent"],
                       "skills":result["skills"]})
    return report

class Phase10SimulationTests(unittest.TestCase):
    def test_scenarios(self):
        for case in simulate():
            with self.subTest(case=case["case"]):
                self.assertTrue(case["passed"],case)

if __name__=="__main__":
    print(json.dumps(simulate(),ensure_ascii=False,indent=2))
    unittest.main(argv=[sys.argv[0]])
