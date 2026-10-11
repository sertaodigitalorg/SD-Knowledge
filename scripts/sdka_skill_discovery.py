#!/usr/bin/env python3
"""Offline conservative natural-language discovery over SDKA canonical manifests.

Discovery is a candidate suggestion, never access authorization.
No network, model call, execution, fuzzy similarity or external catalog.
"""
import argparse
import json
import re
import unicodedata
from sdka_registry_gate import ROOT, load_registry, repository_name
from sdka_skill_router import route

def normalize(value):
    value = unicodedata.normalize("NFKD", str(value).casefold())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def discover(request, experience="junior", root=ROOT):
    if not request or not request.strip():
        return {"institution":"sertaodigital","status":"clarification_required",
                "reason":"empty_request","candidates":[],"skills":["sertaodigital-core"]}
    repos, products, _ = load_registry(root)
    active_repo_urls = {repository_name(x.get("url")) for x in repos.values()
                        if x.get("status") == "active"}
    prompt = " " + normalize(request) + " "
    candidates = []
    for key, product in products.items():
        if product.get("status") != "active":
            continue
        repo = repository_name(product.get("repository"))
        if repo not in active_repo_urls:
            continue
        # Names come from the canonical product record; keys are canonical IDs.
        terms = {normalize(product.get("name", "")), normalize(key),
                 normalize(repo.split("/")[-1])}
        terms = {term for term in terms if len(term) >= 4}
        matches = [term for term in sorted(terms, key=len, reverse=True)
                   if (" " + term + " ") in prompt]
        if matches:
            candidates.append({"product":key,"repository":repo,
                               "matched_term":matches[0],"basis":"canonical-product-name"})
    if not candidates:
        return {"institution":"sertaodigital","status":"clarification_required",
                "reason":"no_canonical_product_identified","candidates":[],
                "skills":["sertaodigital-core"]}
    # Parent and component mentions are separate candidates, as cross-component
    # work may require several codebases. Require review if any lacks active skill.
    result = route([c["repository"] for c in candidates], experience, root)
    result["candidates"] = candidates
    result["discovery_method"] = "exact_normalized_canonical_name"
    result["authorization_granted"] = False
    return result

def main():
    parser = argparse.ArgumentParser(description="SDKA offline guided skill discovery")
    parser.add_argument("request")
    parser.add_argument("--experience",choices=["junior","intermediate","senior"],default="junior")
    args = parser.parse_args()
    print(json.dumps(discover(args.request,args.experience),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
