#!/usr/bin/env python3
"""Validação offline de registros de evidência estática da Fase 11.2."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_LEVELS = {"tree_observed", "content_reviewed", "test_executed"}
REPOSITORY_PATTERN = re.compile(r"^sertaodigitalorg/[A-Za-z0-9_.-]+$")
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")

def validate(records):
    if not isinstance(records, list) or not records:
        raise ValueError("nonempty list required")
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("record must be object")
        if set(record) != {"repository", "commit", "path", "claim", "verification_level", "limitations"}:
            raise ValueError("invalid record fields")
        if not REPOSITORY_PATTERN.fullmatch(record["repository"]):
            raise ValueError("invalid repository")
        if not SHA_PATTERN.fullmatch(record["commit"]):
            raise ValueError("invalid commit")
        p = record["path"]
        if not isinstance(p, str) or not p or p.startswith("/") or "\\" in p or ".." in p.split("/"):
            raise ValueError("unsafe path")
        if record["verification_level"] not in ALLOWED_LEVELS:
            raise ValueError("invalid verification level")
        if not isinstance(record["claim"], str) or not record["claim"].strip():
            raise ValueError("claim required")
        if not isinstance(record["limitations"], str) or not record["limitations"].strip():
            raise ValueError("limitations required")
        key = (record["repository"], record["commit"], p)
        if key in seen:
            raise ValueError("duplicate evidence")
        seen.add(key)
    return True

if __name__ == "__main__":
    records=json.loads((ROOT/"examples/phase11-2-code-evidence.json").read_text(encoding="utf-8"))
    validate(records)
    print(f"Validated {len(records)} declared offline records; implementation not verified")
