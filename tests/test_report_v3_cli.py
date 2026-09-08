"""Current readable reports use the public validator without machine packets."""
import io
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

from test_check_report_v3 import report, SOURCE
from test_validate_research import load_validator, write_contract_root, VALID_REGISTRY
from test_validate_research import VALID_DAILY_V21
from test_source_list import SOURCE_LIST


class ReportV3CliTests(unittest.TestCase):
    def setup_root(self, directory):
        root = Path(directory)
        write_contract_root(root)
        (root / 'docs/REPORT_CONTRACTS.md').write_text(
            '# Report 合同\n\n版本：V3\n', encoding='utf-8')
        registry, errors = load_validator().validate_registry_text(VALID_REGISTRY)
        self.assertEqual([], errors)
        rows = '\n'.join(
            f'| {key} | https://example.org/sources 窗口内列表检查完 | 已检查 | 无 |'
            for key, entry in registry.items() if entry['Cadence'] == 'Required Daily')
        text = report().replace(SOURCE, rows)
        (root / 'daily.md').write_text(text, encoding='utf-8')
        return root, text, registry

    def test_current_docs_and_complete_report_need_no_old_markers(self):
        with tempfile.TemporaryDirectory() as directory:
            root, text, registry = self.setup_root(directory)
            validator = load_validator()
            self.assertEqual([], validator.validate_report_text(text, registry, strict=True))
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(0, validator.main(['--root', str(root), '--report', 'daily.md']), output.getvalue())
            self.assertIn('1 V3 report(s)', output.getvalue())
            self.assertEqual(text, (root / 'daily.md').read_text())

    def test_audit_does_not_silently_skip_current_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root, text, _ = self.setup_root(directory)
            (root / 'daily.md').write_text(text.replace('结论：通过', '结论：未通过'))
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(1, load_validator().main(['--root', str(root), '--audit', 'daily.md']))
            self.assertIn('复核', output.getvalue())

    def test_current_report_keeps_local_link_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root, text, _ = self.setup_root(directory)
            (root / 'daily.md').write_text(text.replace('本窗口没有', '[missing](missing.md) 本窗口没有'))
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(1, load_validator().main(['--root', str(root), '--report', 'daily.md']))
            self.assertIn('missing.md', output.getvalue())

    def test_legacy_report_with_current_source_list_fails_with_actionable_message(self):
        with tempfile.TemporaryDirectory() as directory:
            root, _, _ = self.setup_root(directory)
            (root / 'docs/RESEARCH_SOURCES.md').write_text(SOURCE_LIST)
            (root / 'daily.md').write_text(VALID_DAILY_V21)
            original = (root / 'daily.md').read_bytes()
            for option in ('--report', '--audit'):
                with self.subTest(option=option), redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(1, load_validator().main(['--root', str(root), option, 'daily.md']))
                self.assertIn('旧格式', output.getvalue())
                self.assertIn('--registry', output.getvalue())
                self.assertNotIn('Effective Date', output.getvalue())
                self.assertNotIn('validation passed', output.getvalue())
            (root / 'old-registry.md').write_text(VALID_REGISTRY)
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(0, load_validator().main(['--root', str(root), '--report', 'daily.md', '--registry', 'old-registry.md']), output.getvalue())
            self.assertIn('不是当前标准验收', output.getvalue())
            self.assertEqual(original, (root / 'daily.md').read_bytes())

    def test_current_report_cannot_use_legacy_snapshot_to_reduce_required_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root, _, _ = self.setup_root(directory)
            (root / 'old-registry.md').write_text(VALID_REGISTRY)
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(1, load_validator().main(['--root', str(root), '--report', 'daily.md', '--registry', 'old-registry.md']))
            self.assertIn('--registry 仅用于旧格式', output.getvalue())


if __name__ == '__main__':
    unittest.main()
