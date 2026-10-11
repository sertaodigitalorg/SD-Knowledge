#!/usr/bin/env python3
"""SDKA Phase 12: offline integrity checks of canonical institutional manifests.

Never fetches URLs, makes changes or activates product skills.
"""
import argparse
import json
from pathlib import Path
from sdka_registry_gate import ROOT, load_registry, repository_name


def audit(root=ROOT):
    repos, products, skills = load_registry(root)
    issues = []
    def issue(code, location, message):
        issues.append({"code": code, "location": location, "message": message})

    active_skills = {s["name"]: s for s in skills if s.get("status") == "active"}
    all_skills = {s["name"]: s for s in skills}

    for name, s in all_skills.items():
        location = s.get("location")
        if not location or not (root / location / "SKILL.md").is_file():
            issue("MISSING_SKILL_FILE", name, "Skill catalogada sem SKILL.md")
        for parent in s.get("depends_on", []):
            if parent not in active_skills:
                issue("MISSING_ACTIVE_DEPENDENCY", name, "Dependência não ativa: " + parent)

    known_repos = {repository_name(x.get("url")) for x in repos.values()
                   if repository_name(x.get("url"))}
    for key, p in products.items():
        parent = p.get("parent_product")
        if parent and parent not in products:
            issue("UNKNOWN_PARENT", key, "parent_product não cadastrado: " + parent)
        url = p.get("repository")
        slug = repository_name(url) if url else None
        if url and slug is None:
            issue("INVALID_REPOSITORY_URL", key, "URL de repositório inválida")
        elif slug and slug not in known_repos:
            issue("UNREGISTERED_REPOSITORY", key, "Repositório fora de repositories.yaml")
        if p.get("status") == "active" and not slug:
            issue("ACTIVE_PRODUCT_WITHOUT_REPOSITORY", key, "Produto ativo sem repositório")
    return {"status": "pass" if not issues else "review_required",
            "checked": {"products": len(products), "repositories": len(repos), "skills": len(skills)},
            "issues": issues, "external_sources_verified": False,
            "actions_authorized": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, help="Gravar JSON local do resultado")
    a = parser.parse_args()
    result = audit()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if a.report:
        a.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    if result["status"] != "pass":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
