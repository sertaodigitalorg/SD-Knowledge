#!/usr/bin/env python3
"""Cross-product impact planning based only on canonical SDKA registries.

Offline; advisory only; never opens issues or authorizes implementation.
"""
import argparse
import json
from sdka_registry_gate import ROOT, load_registry, repository_name

def plan(product_ids, root=ROOT):
    repos, products, skills = load_registry(root)
    requested = list(dict.fromkeys(product_ids))
    if not requested:
        raise ValueError("At least one product ID is required")
    unknown = [k for k in requested if k not in products]
    if unknown:
        raise ValueError("Unregistered product: " + ", ".join(unknown))
    active = {s["name"] for s in skills if s.get("status") == "active"}
    entries = []
    for key in requested:
        p = products[key]
        parent = p.get("parent_product", key)
        family = sorted(k for k, v in products.items()
                        if k == parent or v.get("parent_product") == parent)
        candidate_skill = parent.replace("_", "-")
        entries.append({
            "product_id": key,
            "parent_product": parent,
            "related_product_ids": family,
            "repository": repository_name(p.get("repository")),
            "active_product_skill": candidate_skill if candidate_skill in active else None,
            "catalog_status": p.get("status", "unknown"),
            "review_required": True,
            "impact_assessed_against_code": False
        })
    return {
        "status": "review_required",
        "authorization_granted": False,
        "cross_layer_impact_check_required": True,
        "sources": ["products.yaml", "knowledge.yaml", "repositories.yaml"],
        "affected_products": entries,
        "next_steps": [
            "Verify approved functional MASTER and technical source",
            "Identify owners and assess downstream interfaces",
            "Open issue/ADR/PR only after authorization",
            "Run Cross-Layer Impact Check before changes"
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="SDKA offline impact planning")
    parser.add_argument("product_ids", nargs="+")
    args = parser.parse_args()
    print(json.dumps(plan(args.product_ids), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
