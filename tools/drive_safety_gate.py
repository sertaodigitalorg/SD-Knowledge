#!/usr/bin/env python3
"""Reference policy engine for SDKA Google Drive safety.

Stdlib-only and intentionally independent from any LLM. It evaluates a proposed
Drive operation and returns a deterministic decision. It does not call Google
Drive itself; adapters must call this gate before mutating the functional MASTER.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

MUTATING = {
    "create", "update", "move", "quarantine_move", "restore", "delete",
    "purge", "change_permission", "backup_create", "backup_delete", "disable_gate",
}

DECISION_RANK = {
    "ALLOW": 0,
    "ALLOW_WITH_AUDIT": 1,
    "REQUIRE_APPROVAL": 2,
    "REQUIRE_DUAL_CONTROL": 3,
    "DENY": 4,
}


def max_decision(*values: str) -> str:
    return max(values, key=lambda value: DECISION_RANK[value])


def is_critical_target(targets: list[dict[str, Any]], markers: list[str]) -> bool:
    upper_markers = [m.upper() for m in markers]
    for target in targets:
        text = " ".join(str(target.get(k, "")) for k in ("name", "path", "document_type")).upper()
        if any(marker in text for marker in upper_markers):
            return True
    return False


def evaluate(request: Dict[str, Any], policy: Dict[str, Any]) -> Dict[str, Any]:
    operation = str(request.get("operation") or "").strip()
    role = str(request.get("role") or "").strip()
    actor_id = request.get("actor_id")
    agent_id = request.get("agent_id")
    justification = str(request.get("justification") or "").strip()
    targets = request.get("targets") or []
    target_count = int(request.get("target_count") or len(targets))
    scope_percent = float(request.get("estimated_scope_percent") or 0)
    policy_available = bool(request.get("policy_engine_available", True))

    reasons: list[str] = []
    risk = "LOW"
    decision = "ALLOW"

    if not policy_available:
        return {"decision": "DENY", "risk_level": "CRITICAL", "reasons": ["policy_engine_unavailable_fail_closed"]}

    if not operation or role not in policy.get("roles", {}):
        return {"decision": "DENY", "risk_level": "CRITICAL", "reasons": ["unknown_operation_or_role"]}

    allowed_operations = set(policy["roles"].get(role, []))
    if operation not in allowed_operations:
        return {"decision": "DENY", "risk_level": "HIGH", "reasons": ["operation_not_allowed_for_role"]}

    if operation in MUTATING and (not actor_id or not justification):
        return {"decision": "DENY", "risk_level": "HIGH", "reasons": ["missing_identity_or_justification"]}

    if role not in {"ADMIN_HUMAN", "BACKUP"} and operation in set(policy.get("forbidden_for_agents", [])):
        return {"decision": "DENY", "risk_level": "CRITICAL", "reasons": ["operation_forbidden_for_agents"]}

    if operation in {"search", "read"}:
        decision = "ALLOW"
    elif operation in {"create", "update", "quarantine_move", "restore", "backup_create"}:
        decision = "ALLOW_WITH_AUDIT"
        risk = "MEDIUM"
    elif operation == "move":
        decision = "REQUIRE_APPROVAL"
        risk = "HIGH"
    elif operation in {"purge", "change_permission"} and role == "ADMIN_HUMAN":
        decision = "REQUIRE_DUAL_CONTROL"
        risk = "CRITICAL"
    else:
        decision = "DENY"
        risk = "CRITICAL"

    if target_count > int(policy.get("bulk_change_threshold", 20)):
        reasons.append("bulk_change_threshold_exceeded")
        decision = max_decision(decision, "REQUIRE_APPROVAL")
        risk = "CRITICAL"

    if scope_percent >= float(policy.get("critical_scope_percent", 20)):
        reasons.append("critical_scope_percent_reached")
        decision = max_decision(decision, "REQUIRE_APPROVAL")
        risk = "CRITICAL"

    if operation in MUTATING and is_critical_target(targets, policy.get("critical_name_markers", [])):
        reasons.append("critical_authority_target")
        decision = max_decision(decision, "REQUIRE_APPROVAL")
        risk = "CRITICAL"

    if operation in {"purge", "change_permission"}:
        decision = max_decision(decision, "REQUIRE_DUAL_CONTROL")
        risk = "CRITICAL"

    if not reasons:
        reasons.append("policy_evaluated")

    return {
        "decision": decision,
        "risk_level": risk,
        "operation": operation,
        "role": role,
        "target_count": target_count,
        "agent_id": agent_id,
        "reasons": reasons,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", help="Path to JSON request")
    parser.add_argument("--policy", default="config/drive-safety-policy.json")
    args = parser.parse_args()

    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    request = json.loads(Path(args.request).read_text(encoding="utf-8"))
    result = evaluate(request, policy)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["decision"] in {"ALLOW", "ALLOW_WITH_AUDIT"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
