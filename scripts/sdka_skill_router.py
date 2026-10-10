#!/usr/bin/env python3
"""Deterministic SDKA skill routing from existing canonical manifests.

No LLM or network use. Unknown/ambiguous/inactive contexts fail closed.
"""
import argparse
import json
from pathlib import Path
from sdka_registry_gate import ROOT, load_registry, repository_name

def route(repositories_requested, experience="junior", root=ROOT):
    repos, products, skills = load_registry(root)
    active_skills = {x["name"]: x for x in skills if x.get("status") == "active"}
    active_repos = {repository_name(x.get("url")): x for x in repos.values()
                    if x.get("status") == "active" and repository_name(x.get("url"))}
    active_products = {k: p for k, p in products.items() if p.get("status") == "active"}
    out = {"institution": "sertaodigital", "status": "ready",
           "skills": ["sertaodigital-core"], "products": [],
           "unresolved": [], "guidance": []}
    if experience not in ("junior", "intermediate", "senior"):
        raise ValueError("invalid experience level")
    for repository in dict.fromkeys(repositories_requested):
        if repository == "sertaodigitalorg/SD-Knowledge":
            continue
        if repository not in active_repos:
            out["unresolved"].append({"repository": repository, "reason": "repository_not_active"})
            continue
        matches = [(k,p) for k,p in active_products.items()
                   if repository_name(p.get("repository")) == repository]
        if len(matches) != 1:
            out["unresolved"].append({"repository": repository, "reason": "product_not_unique_or_active"})
            continue
        product_id, product = matches[0]
        domain = product.get("parent_product", product_id)
        matching = [s for s in active_skills.values()
                    if s["name"].replace("-", "_") == domain
                    and s.get("type") == "product-context"]
        if len(matching) != 1:
            out["unresolved"].append({"repository": repository, "reason": "product_skill_not_active"})
            continue
        skill = matching[0]["name"]
        if "sertaodigital-core" not in matching[0].get("depends_on", []):
            out["unresolved"].append({"repository": repository, "reason": "core_dependency_missing"})
            continue
        out["products"].append(product_id)
        if skill not in out["skills"]:
            out["skills"].append(skill)
    if out["unresolved"]:
        out["status"] = "review_required"
    if experience == "junior":
        out["guidance"] = [
            "Ler AGENTS.md, SOURCE_OF_TRUTH.md e as Skills selecionadas",
            "Confirmar escopo, permissoes e documentos MASTER antes de alterar arquivos",
            "Trabalhar em branch permitida; executar testes; abrir issue/PR para revisao",
        ]
    else:
        out["guidance"] = ["Revisar fontes MASTER e governanca antes de executar",
                           "Confirmar testes, impactos entre camadas e PR"]
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repositories", nargs="+")
    parser.add_argument("--experience", choices=["junior", "intermediate", "senior"], default="junior")
    args = parser.parse_args()
    print(json.dumps(route(args.repositories, args.experience), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
