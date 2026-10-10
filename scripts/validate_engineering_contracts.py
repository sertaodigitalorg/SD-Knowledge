#!/usr/bin/env python3
"""Offline safety and referential checks for SDKA engineering fixtures.

Requires Python 3.9+. No network or third-party dependencies.
Schema validation is separate: use jsonschema Draft202012Validator in CI when available.
"""
import json
from pathlib import Path
from sdka_registry_gate import check_registry_context

ROOT = Path(__file__).resolve().parents[1]

def check_assessment(data):
    assert data["schema_version"] == "0.1.0"
    assert data["institution"] == "sertaodigital"
    assert data["product_context"]["repository"].startswith("sertaodigitalorg/")
    assert data["product_context"]["skill"] == "sertaodigital-core"
    evidence = {e["id"] for e in data["evidence"]}
    requirements = {r["id"] for r in data["requirements"]}
    assert len(evidence) == len(data["evidence"]), "duplicate evidence IDs"
    assert len(requirements) == len(data["requirements"]), "duplicate requirement IDs"
    for gap in data["gaps"]:
        assert gap["requirement_id"] in requirements, "unknown requirement"
        assert set(gap["evidence_refs"]) <= evidence, "unknown evidence"
        if gap["current_state"] == "met":
            assert gap["evidence_refs"], "met state requires evidence"
    assert data["decision"] == "review_required", "fixture must not preapprove"

def check_connector(data):
    assert data["schema_version"] == "0.1.0"
    assert data["institution"] == "sertaodigital"
    assert data["product_context"]["repository"].startswith("sertaodigitalorg/")
    assert data["product_context"]["skill"] == "sertaodigital-core"
    assert data["scope"]["methods"] == ["GET"]
    assert data["execution"]["mode"] == "dry_run"
    assert data["execution"]["read_only"] is True
    assert data["authorization"]["approved_by"] is None
    assert data["evidence"]["redaction_required"] is True
    assert all("://" not in h and "/" not in h for h in data["scope"]["allowed_hosts"])

def main():
    assessment = json.loads((ROOT / "examples/engineering-assessment.example.json").read_text())
    connector = json.loads((ROOT / "examples/connector-operation.example.json").read_text())
    check_assessment(assessment)
    check_registry_context(assessment)
    check_connector(connector)
    check_registry_context(connector)
    print("SDKA contract fixtures: OK (offline, no external calls)")

if __name__ == "__main__":
    main()
