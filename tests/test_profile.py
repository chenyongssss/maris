"""Local-only, consent-scoped staging/profile tests. No network access needed."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "maris" / "scripts" / "profile.py"
EXAMPLE = ROOT / "examples" / "sample-conversations.json"
CANDIDATE = ROOT / "examples" / "sample-profile-candidate.json"


class ProfileCLITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cwd = Path(self.tmp.name)

    def run_cli(self, *parts, expected=0):
        proc = subprocess.run([sys.executable, str(SCRIPT), *map(str, parts)], cwd=self.cwd, capture_output=True, text=True, timeout=15)
        self.assertEqual(proc.returncode, expected, f"stdout={proc.stdout}\nstderr={proc.stderr}")
        return proc

    def test_catalog_only_titles_not_message_body(self):
        output = self.run_cli("catalog", "--input", EXAMPLE).stdout
        self.assertIn("PDE solver discussion", output)
        self.assertNotIn("DO NOT STAGE", output)
        self.assertNotIn("I am comfortable", output)
        self.assertFalse((self.cwd / ".maris").exists())

    def test_stage_requires_consent_and_explicit_indices(self):
        self.run_cli("stage", "--input", EXAMPLE, "--indices", "1,2", expected=2)
        self.assertFalse((self.cwd / ".maris").exists())
        self.run_cli("stage", "--input", EXAMPLE, "--indices", "1,2", "--consent")
        staged = json.loads((self.cwd / ".maris/private/staged.json").read_text())
        self.assertEqual([c["catalog_index"] for c in staged["selection"]], [1,2])
        text = json.dumps(staged)
        self.assertNotIn("DO NOT STAGE", text)
        self.assertNotIn("Secret-demo-value", text)
        self.assertNotIn("I'll use concise technical language", text)
        self.assertIn("finite-volume discretizations", text)
        if os.name != "nt":
            self.assertEqual((self.cwd / ".maris/private/staged.json").stat().st_mode & 0o777, 0o600)

    def test_double_stage_needs_explicit_replace(self):
        args = ("stage", "--input", EXAMPLE, "--indices", "1", "--consent")
        self.run_cli(*args)
        self.run_cli(*args, expected=2)
        self.run_cli(*args, "--replace")

    def test_zip_read_no_extract(self):
        archive = self.cwd / "export.zip"
        with zipfile.ZipFile(archive, "w") as out:
            out.writestr("folder/conversations.json", EXAMPLE.read_text(encoding="utf8"))
            out.writestr("../evil.txt", "should not extract")
        self.run_cli("catalog", "--input", archive)
        self.run_cli("stage", "--input", archive, "--indices", "1", "--consent")
        self.assertFalse((self.cwd / "evil.txt").exists())

    def test_profile_approval_and_erase_gates(self):
        self.run_cli("template")
        target = self.cwd / ".maris/private/profile-candidate.json"
        target.write_text(CANDIDATE.read_text(encoding="utf8"), encoding="utf8")
        self.run_cli("approve", "--confirm", "wrong", expected=2)
        self.assertFalse((self.cwd / ".maris/private/profile.json").exists())
        self.run_cli("approve", "--confirm", "APPROVE-MARIS-PROFILE")
        profile = json.loads((self.cwd / ".maris/private/profile.json").read_text())
        self.assertTrue(profile["user_confirmed"])
        self.assertEqual(profile["purpose"], "personalized-ai-work-review")
        self.assertNotIn("raw_chat", profile)
        self.run_cli("show")
        self.run_cli("erase", "--confirm", "NOPE", expected=2)
        self.assertTrue((self.cwd / ".maris/private/profile.json").exists())
        self.run_cli("erase", "--confirm", "DELETE-MARIS-LOCAL-DATA")
        self.assertFalse((self.cwd / ".maris/private/profile.json").exists())
        self.assertFalse((self.cwd / ".maris/private/profile-candidate.json").exists())

    def test_reject_invalid_candidate_schema(self):
        self.run_cli("template")
        file = self.cwd / ".maris/private/profile-candidate.json"
        data = json.loads(file.read_text())
        data["knowledge_signals"] = [{"topic":"unknown", "signal":"psychometric score", "basis":"tentative", "evidence_ref":"x"}]
        file.write_text(json.dumps(data))
        self.run_cli("approve", "--confirm", "APPROVE-MARIS-PROFILE", expected=2)

    def test_markdown_single_conversation(self):
        path = self.cwd / "one.md"
        path.write_text("I want a mathematical derivation, not just a summary.", encoding="utf8")
        self.run_cli("catalog", "--input", path)
        self.run_cli("stage", "--input", path, "--indices", "1", "--consent")
        contents = (self.cwd / ".maris/private/staged.json").read_text(encoding="utf8")
        self.assertIn("mathematical derivation", contents)


if __name__ == "__main__":
    unittest.main()

class ChatGPTMappingCompatibilityTests(unittest.TestCase):
    def test_mapping_import_keeps_user_messages_only(self):
        with tempfile.TemporaryDirectory() as root:
            cwd = Path(root)
            example = [{
                "title": "ChatGPT export mapping fixture",
                "mapping": {
                    "a": {"message": {"author": {"role": "user"}, "content": {"parts": ["I prefer mathematical proofs."]}, "create_time": 1}},
                    "b": {"message": {"author": {"role": "assistant"}, "content": {"parts": ["Assistant message not part of profile stage"]}, "create_time": 2}},
                    "c": {"message": {"author": {"role": "user"}, "content": {"parts": ["I am learning backend security"]}, "create_time": 3}},
                },
            }]
            src = cwd / "conversations.json"
            src.write_text(json.dumps(example), encoding="utf8")
            out = subprocess.run([sys.executable, str(SCRIPT), "stage", "--input", str(src), "--indices", "1", "--consent"], cwd=cwd, capture_output=True, text=True)
            self.assertEqual(out.returncode, 0, out.stderr)
            staged = (cwd / ".maris/private/staged.json").read_text(encoding="utf8")
            self.assertIn("I prefer mathematical proofs", staged)
            self.assertIn("I am learning backend security", staged)
            self.assertNotIn("Assistant message not part", staged)
