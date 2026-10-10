#!/usr/bin/env python3
"""SDKA institutional contract tests (offline; no network calls)."""
import copy
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from validate_engineering_contracts import check_assessment, check_connector
from sdka_registry_gate import check_registry_context

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assessment_schema = load("schemas/engineering-assessment.schema.json")
        cls.connector_schema = load("schemas/connector-operation.schema.json")
        Draft202012Validator.check_schema(cls.assessment_schema)
        Draft202012Validator.check_schema(cls.connector_schema)
        cls.assessment_validator = Draft202012Validator(cls.assessment_schema, format_checker=FormatChecker())
        cls.connector_validator = Draft202012Validator(cls.connector_schema, format_checker=FormatChecker())
        cls.assessment = load("examples/engineering-assessment.example.json")
        cls.connector = load("examples/connector-operation.example.json")

    def check_valid(self, validator, document):
        self.assertEqual(list(validator.iter_errors(document)), [])

    def check_invalid(self, validator, document):
        self.assertTrue(list(validator.iter_errors(document)))

    def test_assessment_fixture(self):
        self.check_valid(self.assessment_validator, self.assessment)
        check_assessment(self.assessment)
        check_registry_context(self.assessment)

    def test_connector_fixture(self):
        self.check_valid(self.connector_validator, self.connector)
        check_connector(self.connector)
        check_registry_context(self.connector)

    def test_non_institutional_assessment_rejected(self):
        modified = copy.deepcopy(self.assessment)
        modified["institution"] = "external"
        self.check_invalid(self.assessment_validator, modified)

    def test_non_institutional_connector_rejected(self):
        modified = copy.deepcopy(self.connector)
        modified["institution"] = "external"
        self.check_invalid(self.connector_validator, modified)

    def test_external_repository_rejected(self):
        for data, validator in ((self.assessment, self.assessment_validator), (self.connector, self.connector_validator)):
            modified = copy.deepcopy(data)
            modified["product_context"]["repository"] = "thirdparty/generic-platform"
            self.check_invalid(validator, modified)

    def test_missing_product_context_rejected(self):
        modified = copy.deepcopy(self.assessment)
        del modified["product_context"]
        self.check_invalid(self.assessment_validator, modified)

    def test_write_method_rejected(self):
        modified = copy.deepcopy(self.connector)
        modified["scope"]["methods"] = ["POST"]
        self.check_invalid(self.connector_validator, modified)

    def test_live_execution_rejected(self):
        modified = copy.deepcopy(self.connector)
        modified["execution"]["mode"] = "live"
        self.check_invalid(self.connector_validator, modified)

    def test_unredacted_evidence_rejected(self):
        modified = copy.deepcopy(self.connector)
        modified["evidence"]["redaction_required"] = False
        self.check_invalid(self.connector_validator, modified)

    def test_unverified_evidence_ref_rejected(self):
        modified = copy.deepcopy(self.assessment)
        modified["gaps"][0]["evidence_refs"] = ["UNKNOWN"]
        self.check_invalid_or_reference_error(modified)

    def check_invalid_or_reference_error(self, modified):
        self.check_valid(self.assessment_validator, modified)
        with self.assertRaises(AssertionError):
            check_assessment(modified)

    def test_duplicate_requirement_id_rejected(self):
        modified = copy.deepcopy(self.assessment)
        modified["requirements"].append(copy.deepcopy(modified["requirements"][0]))
        with self.assertRaises(AssertionError):
            check_assessment(modified)


    def test_unregistered_repository_with_valid_prefix_rejected(self):
        modified = copy.deepcopy(self.assessment)
        modified["product_context"]["repository"] = "sertaodigitalorg/InventedRepo"
        self.check_valid(self.assessment_validator, modified)
        with self.assertRaises(AssertionError):
            check_registry_context(modified)

    def test_known_repo_without_active_product_skill_rejected(self):
        modified = copy.deepcopy(self.assessment)
        modified["product_context"]["repository"] = "sertaodigitalorg/LegislaGD"
        modified["product_context"]["skill"] = "sertaodigital-core"
        with self.assertRaises(AssertionError):
            check_registry_context(modified)

    def test_canonical_product_skill_mapping_accepted(self):
        modified = copy.deepcopy(self.assessment)
        modified["product_context"]["repository"] = "sertaodigitalorg/LegislaGD"
        modified["product_context"]["skill"] = "legislagd"
        self.assertTrue(check_registry_context(modified))

    def test_pending_product_rejected_even_with_known_repo(self):
        modified = copy.deepcopy(self.assessment)
        modified["product_context"]["repository"] = "sertaodigitalorg/Plataforma360"
        modified["product_context"]["skill"] = "sertaodigital-core"
        with self.assertRaises(AssertionError):
            check_registry_context(modified)


if __name__ == "__main__":
    unittest.main()
