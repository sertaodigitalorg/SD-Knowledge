import json
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / "config/drive-safety-policy.json").read_text(encoding="utf-8"))
SPEC = importlib.util.spec_from_file_location("drive_safety_gate", ROOT / "tools/drive_safety_gate.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class DriveSafetyGateTests(unittest.TestCase):
    def eval(self, **kwargs):
        request = {
            "operation": "read",
            "role": "READER",
            "actor_id": "human:test",
            "agent_id": "agent:test",
            "justification": "controlled test",
            "targets": [{"name": "test-document"}],
            "target_count": 1,
            "estimated_scope_percent": 0,
            "policy_engine_available": True,
        }
        request.update(kwargs)
        return MODULE.evaluate(request, POLICY)

    def test_read_allowed(self):
        self.assertEqual(self.eval()["decision"], "ALLOW")

    def test_writer_create_is_audited(self):
        self.assertEqual(self.eval(operation="create", role="WRITER")["decision"], "ALLOW_WITH_AUDIT")

    def test_agent_delete_denied(self):
        self.assertEqual(self.eval(operation="delete", role="WRITER")["decision"], "DENY")

    def test_agent_permission_change_denied(self):
        self.assertEqual(self.eval(operation="change_permission", role="WRITER")["decision"], "DENY")

    def test_bulk_mutation_requires_approval(self):
        result = self.eval(operation="update", role="WRITER", target_count=21)
        self.assertEqual(result["decision"], "REQUIRE_APPROVAL")

    def test_twenty_percent_scope_requires_approval(self):
        result = self.eval(operation="update", role="WRITER", estimated_scope_percent=20)
        self.assertEqual(result["decision"], "REQUIRE_APPROVAL")

    def test_critical_authority_target_requires_approval(self):
        result = self.eval(operation="update", role="WRITER", targets=[{"name": "SOURCE_OF_TRUTH POLICY"}])
        self.assertEqual(result["decision"], "REQUIRE_APPROVAL")

    def test_missing_justification_denied(self):
        self.assertEqual(self.eval(operation="update", role="WRITER", justification="")["decision"], "DENY")

    def test_policy_engine_failure_is_fail_closed(self):
        result = self.eval(operation="update", role="WRITER", policy_engine_available=False)
        self.assertEqual(result["decision"], "DENY")

    def test_quarantine_operator_can_quarantine(self):
        result = self.eval(operation="quarantine_move", role="QUARANTINE_OPERATOR")
        self.assertEqual(result["decision"], "ALLOW_WITH_AUDIT")

    def test_quarantine_operator_can_restore(self):
        result = self.eval(operation="restore", role="QUARANTINE_OPERATOR")
        self.assertEqual(result["decision"], "ALLOW_WITH_AUDIT")

    def test_human_purge_requires_dual_control(self):
        result = self.eval(operation="purge", role="ADMIN_HUMAN")
        self.assertEqual(result["decision"], "REQUIRE_DUAL_CONTROL")

    def test_unknown_role_fails_closed(self):
        self.assertEqual(self.eval(role="UNKNOWN")["decision"], "DENY")


if __name__ == "__main__":
    unittest.main()
