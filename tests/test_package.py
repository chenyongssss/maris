"""Package checks: no claim about model behavior or host compatibility."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "maris" / "SKILL.md"


class PackageTests(unittest.TestCase):
    def test_skill_and_documentation_present(self):
        for path in [
            SKILL, ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "LICENSE",
            ROOT / "SECURITY.md", ROOT / "docs" / "USAGE.md", ROOT / "docs" / "PRIVACY.md",
            ROOT / "skills" / "maris" / "scripts" / "profile.py",
            ROOT / "skills" / "maris" / "references" / "profile-protocol.md",
        ]:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_skill_frontmatter(self):
        text = SKILL.read_text(encoding="utf8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s+maris\s*$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*>-")
        self.assertLessEqual(len(SKILL.read_text().splitlines()), 500)
        self.assertEqual(SKILL.parent.name, "maris")

    def test_core_contract_and_privacy(self):
        content = SKILL.read_text(encoding="utf8")
        for token in ("OBSERVED", "REPORTED", "INFERRED", "UNKNOWN", "No hidden history access", "Profile: on", "human", "references/profile-protocol.md"):
            with self.subTest(token=token):
                self.assertIn(token, content)

    def test_no_version_in_hero(self):
        hero = ROOT.joinpath("README.md").read_text(encoding="utf8").split("## 20-second demo")[0]
        self.assertNotRegex(hero, r"\bv0\.1\b")
        self.assertNotIn("alpha", hero.lower())


if __name__ == "__main__":
    unittest.main()
