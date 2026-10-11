#!/usr/bin/env python3
"""Inventário inicial, offline, de todos os produtos do catálogo SDKA.

Não cria Skills, não confirma funcionalidades nem consulta endpoints.
"""
import argparse
import json
from sdka_registry_gate import load_registry, repository_name, ROOT

def inventory(root=ROOT):
    repositories, products, skills = load_registry(root)
    active_skills = {s["name"] for s in skills if s.get("status") == "active"
                     and s.get("type") == "product-context"}
    registered_repos = {repository_name(r.get("url")) for r in repositories.values()
                        if r.get("status") == "active" and repository_name(r.get("url"))}
    items=[]
    for key, p in products.items():
        parent=p.get("parent_product",key)
        proposed_skill=parent.replace("_","-")
        selected_skill=proposed_skill if proposed_skill in active_skills else None
        repo=repository_name(p.get("repository"))
        items.append({
            "product_id":key,
            "name":p["name"],
            "type":p.get("type"),
            "catalog_status":p.get("status"),
            "parent_product":p.get("parent_product"),
            "repository":repo,
            "repository_validated":repo in registered_repos if repo else False,
            "skill":selected_skill,
            "context_status":"active_skill" if selected_skill and p.get("status")=="active"
                else "pending_validation" if p.get("status")!="active"
                else "institutional_only",
            "description_from_catalog":p.get("description",""),
            "implementation_verified":False,
            "recommended_next_action":"verify_product_status_and_sources" if p.get("status")!="active"
                else "verify_existing_product_skill" if selected_skill
                else "prepare_product_skill_proposal",
        })
    return {"institution":"sertaodigital","source":"products.yaml + repositories.yaml + knowledge.yaml",
            "mode":"offline_catalog_only","products":items,
            "counts":{"total":len(items),"active_skill":sum(x["context_status"]=="active_skill" for x in items),
                      "institutional_only":sum(x["context_status"]=="institutional_only" for x in items),
                      "pending_validation":sum(x["context_status"]=="pending_validation" for x in items)}}

def main():
    argparse.ArgumentParser(description="Inventário offline de produtos SDKA").parse_args()
    print(json.dumps(inventory(),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
