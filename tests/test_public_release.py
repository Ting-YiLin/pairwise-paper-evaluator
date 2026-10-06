import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "synthetic_example" / "results.json"
sys.path.insert(0, str(ROOT / "scripts"))
from validate_results import validate
from aggregate_results import summarize

class PublicReleaseTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_synthetic_file_validates(self):
        self.assertEqual(validate(self.data), [])

    def test_reversal_is_not_counted_as_an_extra_vote(self):
        result = summarize(self.data)
        self.assertEqual(result["original_edges"], 2)
        self.assertEqual(result["wins_for_left_target"], 1)
        self.assertEqual(result["ties"], 1)
        self.assertEqual(result["target_score"], 0.75)

    def test_changed_reversal_direction_is_rejected(self):
        reversed_edge = next(e for e in self.data["edges"] if e["position_variant"] == "reversed")
        reversed_edge["overall"] = "left"
        errors = validate(self.data)
        self.assertTrue(any("changed substantive direction" in e for e in errors))

    def test_cli_validation(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_results.py"), str(EXAMPLE)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("VALID edges=3", result.stdout)

if __name__ == "__main__":
    unittest.main()
