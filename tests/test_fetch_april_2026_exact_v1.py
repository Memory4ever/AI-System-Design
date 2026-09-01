import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "fetch_april_2026_exact_v1.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_april_2026_exact_v1", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FetchAprilExactV1LedgerTest(unittest.TestCase):
    def test_reads_retained_ids_from_legacy_rows_schema(self):
        module = load_module()
        ledger = {
            "rows": [
                {"arxiv_id": "2604.00001", "screening_decision": "retained"},
                {"arxiv_id": "2604.00002", "screening_decision": "pre_denominator_closure"},
            ]
        }

        self.assertEqual(module.retained_arxiv_ids(ledger), ["2604.00001"])

    def test_reads_retained_ids_from_independent_final_schema(self):
        module = load_module()
        ledger = {
            "identities": [
                {"arxiv_id": "2604.00003", "screening_decision": "retained"},
                {"arxiv_id": "2604.00004", "candidate_state": "retained"},
                {"arxiv_id": "2604.00005", "screening_decision": "pre_denominator_closure"},
            ]
        }

        self.assertEqual(
            module.retained_arxiv_ids(ledger),
            ["2604.00003", "2604.00004"],
        )

    def test_prefers_independent_final_ledger_when_present(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            packet = Path(tmp)
            (packet / "screening-ledger.json").write_text(
                '{"rows":[{"arxiv_id":"2604.00001","screening_decision":"retained"}]}'
            )
            (packet / "screening-ledger-final.json").write_text(
                '{"identities":[{"arxiv_id":"2604.00002","screening_decision":"retained"}]}'
            )

            ledger, path = module.load_screening_ledger(packet)

        self.assertEqual(path.name, "screening-ledger-final.json")
        self.assertEqual(module.retained_arxiv_ids(ledger), ["2604.00002"])

    def test_reads_reopened_false_negatives_from_independent_adjudication(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            packet = Path(tmp)
            (packet / "independent-denominator-adjudication.json").write_text(
                '{"items":['
                '{"arxiv_id":"2604.00006","status":"false_negative_retained_pending_exact_v1"},'
                '{"arxiv_id":"2604.00007","status":"fresh_context_closure_confirmed"}'
                ']}'
            )

            ids = module.challenged_arxiv_ids(packet)

        self.assertEqual(ids, ["2604.00006"])


if __name__ == "__main__":
    unittest.main()
