#!/usr/bin/env python3
"""Fase 11: relatório offline de lacunas a partir de evidências declaradas.

Não coleta dados, não verifica links nem aprova implementação.
"""
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from sdka_registry_gate import ROOT, check_registry_context

SCHEMA = ROOT / "schemas" / "engineering-assessment.schema.json"

def assess(data, root=ROOT):
    schema = json.loads((root / "schemas/engineering-assessment.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda e: str(e.path))
    if errors:
        raise ValueError("schema validation failed: " + "; ".join(e.message for e in errors))
    check_registry_context(data, root)
    if data["decision"] != "review_required":
        raise ValueError("automatic assessment cannot approve or reject decisions")
    evidence_ids = [e["id"] for e in data["evidence"]]
    requirement_ids = [r["id"] for r in data["requirements"]]
    gap_ids = [g["id"] for g in data["gaps"]]
    for title, ids in [("evidence",evidence_ids),("requirements",requirement_ids),("gaps",gap_ids)]:
        if len(set(ids)) != len(ids):
            raise ValueError("duplicate " + title + " ID")
    declared_evidence = {e["id"]:e for e in data["evidence"]}
    requirements = set(requirement_ids)
    results = []
    for gap in data["gaps"]:
        if gap["requirement_id"] not in requirements:
            raise ValueError("unknown requirement: " + gap["requirement_id"])
        if not set(gap["evidence_refs"]).issubset(declared_evidence):
            raise ValueError("unknown evidence reference: " + gap["id"])
        if gap["current_state"] == "met" and not gap["evidence_refs"]:
            raise ValueError("met without evidence: " + gap["id"])
        if gap["current_state"] == "met" and any(
            declared_evidence[e]["confidence"] != "observed" for e in gap["evidence_refs"]
        ):
            raise ValueError("met relies on unverified or inferred evidence: " + gap["id"])
        results.append({"gap_id":gap["id"],"requirement_id":gap["requirement_id"],
                        "declared_state":gap["current_state"],"evidence_refs":gap["evidence_refs"],
                        "recommendation":gap["recommendation"]})
    return {"institution":"sertaodigital","repository":data["product_context"]["repository"],
            "skill":data["product_context"]["skill"],"status":"review_required",
            "verified_against_source":False,"authorization_granted":False,
            "warning":"Evidências declaradas no arquivo; referências externas e implementação não foram verificadas.",
            "gaps":results}

def main():
    parser=argparse.ArgumentParser(description="Relatório offline de evidências SDKA")
    parser.add_argument("assessment_file", type=Path)
    args=parser.parse_args()
    document=json.loads(args.assessment_file.read_text(encoding="utf-8"))
    print(json.dumps(assess(document),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
