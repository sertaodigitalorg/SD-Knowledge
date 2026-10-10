"""Cross-reference SDKA engineering contracts against canonical manifests.

This is a fail-closed, offline validator. It does not access GitHub or Drive.
"""
from pathlib import Path
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPECIAL_REPOSITORY = "sertaodigitalorg/SD-Knowledge"

def load_registry(root=ROOT):
    with (root / "repositories.yaml").open(encoding="utf-8") as f:
        repositories = yaml.safe_load(f)["repositories"]
    with (root / "products.yaml").open(encoding="utf-8") as f:
        products = yaml.safe_load(f)["products"]
    with (root / "knowledge.yaml").open(encoding="utf-8") as f:
        skills = yaml.safe_load(f)["knowledge_architecture"]
    return repositories, products, skills

def repository_name(url):
    if not isinstance(url, str):
        return None
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        return None
    parts = parsed.path.strip("/").split("/")
    if len(parts) != 2:
        return None
    return "/".join(parts)

def check_registry_context(document, root=ROOT):
    assert document["institution"] == "sertaodigital", "institution outside SDKA"
    context = document["product_context"]
    selected_repo = context["repository"]
    selected_skill = context["skill"]
    repositories, products, skills = load_registry(root)

    registered = {
        repository_name(item.get("url")): (key, item)
        for key, item in repositories.items()
        if item.get("status") == "active" and repository_name(item.get("url"))
    }
    assert selected_repo in registered, "repository absent or inactive in repositories.yaml"
    skill_map = {item["name"]: item for item in skills if item.get("status") == "active"}
    assert selected_skill in skill_map, "skill absent or inactive in knowledge.yaml"

    if selected_repo == SPECIAL_REPOSITORY:
        assert selected_skill == "sertaodigital-core", "SDKA uses its own institutional skill"
        return True

    matched_products = {
        key: product for key, product in products.items()
        if repository_name(product.get("repository")) == selected_repo
        and product.get("status") == "active"
    }
    assert matched_products, "product absent or inactive in products.yaml"
    # Skills are product contexts, not just arbitrary organization skills.
    allowed_skill_by_product = {
        "legislagd": "legislagd",
        "observatorio_mandacaru": "observatorio-mandacaru",
    }
    for key, product in matched_products.items():
        domain = product.get("parent_product", key)
        skill = allowed_skill_by_product.get(domain)
        if skill and selected_skill == skill:
            return True
    raise AssertionError("No active product-specific skill mapping for repository")
