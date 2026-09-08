"""Historical report validation must not rewrite its registry identity."""
import io
import hashlib
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from test_validate_research import VALID_DAILY_V21, VALID_REGISTRY, load_validator, write_contract_root


class RegistrySnapshotTests(unittest.TestCase):
    def test_current_contract_does_not_require_retired_editorial_schema(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            report_contract = root / "docs/REPORT_CONTRACTS.md"
            report_contract.write_text(report_contract.read_text().replace(
                "<!-- validator:deep-analysis-selection-v1 -->\n", ""), encoding="utf-8")
            self.assertEqual([], validator.validate_contract_bundle(root))

    def test_explicit_snapshot_preserves_legacy_report_and_default_mismatch(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            (root / "docs/RESEARCH_SOURCES.md").write_text(
                VALID_REGISTRY.replace("注册表版本：2026-08-25", "注册表版本：2026-09-04"),
                encoding="utf-8",
            )
            snapshot = root / "old-registry.md"
            snapshot.write_text(VALID_REGISTRY, encoding="utf-8")
            report = root / "daily.md"
            report.write_text(VALID_DAILY_V21, encoding="utf-8")
            original = report.read_bytes()
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(1, validator.main(["--root", str(root), "--report", "daily.md"]))
            self.assertIn("does not match loaded registry", output.getvalue())
            for snapshot_arg in ("old-registry.md", str(snapshot)):
                with self.subTest(snapshot=snapshot_arg), redirect_stdout(io.StringIO()) as output:
                    status = validator.main([
                        "--root", str(root), "--registry", snapshot_arg, "--report", "daily.md",
                    ])
                    self.assertEqual(0, status, output.getvalue())
                    self.assertIn(str(snapshot.resolve()), output.getvalue())
                    self.assertIn(hashlib.sha256(snapshot.read_bytes()).hexdigest(), output.getvalue())
                    self.assertIn("provenance not authenticated", output.getvalue())
            self.assertEqual(original, report.read_bytes())

    def test_snapshot_errors_do_not_fall_back_to_current_registry(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            (root / "daily.md").write_text(VALID_DAILY_V21, encoding="utf-8")
            cases = {
                "missing.md": None,
                "invalid.md": VALID_REGISTRY.replace("Creator Primary", "Invented Authority", 1),
                "wrong-version.md": VALID_REGISTRY.replace("注册表版本：2026-08-25", "注册表版本：2026-08-26"),
            }
            for name, content in cases.items():
                if content is not None:
                    (root / name).write_text(content, encoding="utf-8")
                with self.subTest(snapshot=name), redirect_stdout(io.StringIO()) as output:
                    status = validator.main([
                        "--root", str(root), "--registry", name, "--report", "daily.md",
                    ])
                    self.assertEqual(1, status, output.getvalue())
                    self.assertIn("ERROR:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
