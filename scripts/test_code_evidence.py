"""Testes de validação de evidências estáticas da SDKA."""
import copy
import json
import unittest
from pathlib import Path
from sdka_code_evidence import validate

ROOT=Path(__file__).resolve().parents[1]
FIXTURES=json.loads((ROOT/"examples/phase11-2-code-evidence.json").read_text(encoding="utf-8"))

class CodeEvidenceTests(unittest.TestCase):
    def test_declared_evidence(self):
        self.assertTrue(validate(copy.deepcopy(FIXTURES)))

    def test_reject_duplicate(self):
        with self.assertRaises(ValueError):
            validate(FIXTURES+[copy.deepcopy(FIXTURES[0])])

    def test_reject_path_traversal(self):
        sample=copy.deepcopy(FIXTURES)
        sample[0]["path"]="../secret"
        with self.assertRaises(ValueError):
            validate(sample)

    def test_reject_invalid_commit(self):
        sample=copy.deepcopy(FIXTURES)
        sample[0]["commit"]="latest"
        with self.assertRaises(ValueError):
            validate(sample)

    def test_reject_invalid_level(self):
        sample=copy.deepcopy(FIXTURES)
        sample[0]["verification_level"]="production_verified"
        with self.assertRaises(ValueError):
            validate(sample)

    def test_reject_missing_limitation(self):
        sample=copy.deepcopy(FIXTURES)
        sample[0]["limitations"]=""
        with self.assertRaises(ValueError):
            validate(sample)

if __name__=="__main__":
    unittest.main()
