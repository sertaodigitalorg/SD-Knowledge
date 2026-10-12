#!/usr/bin/env python3
"""Relatório offline de governança SDKA baseado somente nos manifestos canônicos."""
import argparse
import json
from pathlib import Path
from sdka_registry_gate import ROOT, load_registry, repository_name

def report(root=ROOT):
    repositories, products, skills = load_registry(root)
    active = {s["name"] for s in skills if s.get("status") == "active"}
    rows = []
    for key, item in products.items():
        parent = item.get("parent_product", key)
        expected_skill = parent.replace("_", "-")
        skill = expected_skill if expected_skill in active else None
        rows.append({
            "product_id": key,
            "name": item["name"],
            "catalog_status": item.get("status", "unknown"),
            "repository": repository_name(item.get("repository")),
            "context_skill": skill,
            "skill_activation_claim": bool(skill and item.get("status") == "active"),
            "implementation_verified": False,
            "review_required": not bool(skill and item.get("status") == "active"),
        })
    rows.sort(key=lambda p: p["product_id"])
    return {
        "scope": "canonical_catalog_only",
        "sources": ["products.yaml", "repositories.yaml", "knowledge.yaml"],
        "external_evidence_verified": False,
        "automated_approval": False,
        "counts": {
            "products": len(rows),
            "active_catalog_products": sum(x["catalog_status"] == "active" for x in rows),
            "awaiting_validation": sum(x["catalog_status"] != "active" for x in rows),
            "with_active_context": sum(bool(x["context_skill"]) and x["catalog_status"] == "active" for x in rows),
        },
        "products": rows
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(data, encoding="utf-8")
    print(data, end="")

if __name__ == "__main__":
    main()
