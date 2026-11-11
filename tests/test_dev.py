"""Run with: python -m unittest discover -s tests -v

These are configuration and safety unit tests, not Roblox Studio gameplay tests.
"""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import dev  # noqa: E402


class ProjectSafetyTests(unittest.TestCase):
    def test_project_structure_and_guard(self):
        project = dev.load_project()
        dev.validate_project(project)
        self.assertIsInstance(project["servePlaceIds"], list)

    def test_empty_allowlist_is_valid_and_locked(self):
        self.assertEqual(dev.allowed_place_ids({"servePlaceIds": []}), [])

    def test_missing_allowlist_is_rejected(self):
        with self.assertRaises(dev.SetupError):
            dev.allowed_place_ids({})

    def test_invalid_ids_are_rejected(self):
        for value in [-1, 0, "123", True, None, 1.5]:
            with self.subTest(value=value):
                with self.assertRaises(dev.SetupError):
                    dev.allowed_place_ids({"servePlaceIds": [value]})

    def test_duplicate_ids_are_rejected(self):
        with self.assertRaises(dev.SetupError):
            dev.allowed_place_ids({"servePlaceIds": [123, 123]})

    def test_explicit_place_id_accepted(self):
        self.assertEqual(dev.allowed_place_ids({"servePlaceIds": [123]}), [123])

    def test_wrong_mapping_is_rejected(self):
        project = json.loads((ROOT / "default.project.json").read_text())
        project["tree"]["ServerScriptService"]["GameServer"]["$path"] = "src/other"
        with self.assertRaises(dev.SetupError):
            dev.validate_project(project)


if __name__ == "__main__":
    unittest.main()
