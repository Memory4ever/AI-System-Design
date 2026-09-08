"""The source list needs five readable columns, not duplicated contracts."""
import tempfile
import unittest
from pathlib import Path
from test_validate_research import load_validator, write_contract_root

SOURCE_LIST = '''# 研究来源

注册表版本：2026-09-06

<!-- validator:source-list -->
| ID | 来源 | 入口 | 频率 | 关注内容 |
| --- | --- | --- | --- | --- |
| SRC-A | 示例研究机构 | [研究](https://example.org/research) | 每日 | 模型训练机制 |
| SRC-B | 示例工程项目 | [发布](https://example.org/releases) | 每周 | 推理调度变化 |
| SRC-C | 辅助入口 | [检索](https://example.org/search) | 按需 | 恢复具体材料身份 |
'''

class SourceListTests(unittest.TestCase):
    def test_grouped_tables_preserve_all_sources_and_global_uniqueness(self):
        marker = '<!-- validator:source-list -->'
        header = '| ID | 来源 | 入口 | 频率 | 关注内容 |\n| --- | --- | --- | --- | --- |\n'
        grouped = SOURCE_LIST.replace('| SRC-B', '\n### 每周补齐\n\n' + marker + '\n' + header + '| SRC-B')
        grouped = grouped.replace('| SRC-C', '\n### 按需触发\n\n' + marker + '\n' + header + '| SRC-C')
        v = load_validator()
        expected, _ = v.validate_registry_text(SOURCE_LIST)
        rows, errors = v.validate_registry_text(grouped)
        self.assertEqual([], errors)
        self.assertEqual(expected, rows)
        for bad in (grouped.replace('SRC-C', 'SRC-A'),
                    grouped.replace('https://example.org/search', 'https://example.org/research'),
                    grouped.replace('| 按需 |', '| 随便 |')):
            with self.subTest(bad=bad):
                self.assertTrue(v.validate_registry_text(bad)[1])

    def test_simple_list_maps_only_the_fields_consumers_need(self):
        rows, errors = load_validator().validate_registry_text(SOURCE_LIST)
        self.assertEqual([], errors)
        self.assertEqual('Required Daily', rows['SRC-A']['Cadence'])
        self.assertEqual('Required Weekly', rows['SRC-B']['Cadence'])
        self.assertEqual('Event Trigger', rows['SRC-C']['Cadence'])
        self.assertNotIn('Fallback', rows['SRC-A'])

    def test_missing_entry_duplicate_or_invalid_frequency_is_rejected(self):
        for bad in (SOURCE_LIST.replace('SRC-B', 'SRC-A'), SOURCE_LIST.replace('每日', '随便'),
                    SOURCE_LIST.replace('[研究](https://example.org/research)', '—'),
                    SOURCE_LIST.replace('模型训练机制', '')):
            with self.subTest(bad=bad):
                self.assertTrue(load_validator().validate_registry_text(bad)[1])

    def test_one_prompt_is_sufficient_and_missing_prompt_fails(self):
        v = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            for p in root.glob('CODEX_*RESEARCH_PROMPT.md'):
                p.unlink()
            errors = v.validate_contract_bundle(root)
            self.assertTrue(any('CODEX_RESEARCH_PROMPT.md' in x for x in errors))
            (root / 'CODEX_RESEARCH_PROMPT.md').write_text('\n'.join(
                ['docs/RESEARCH_CONTRACT.md', 'docs/RESEARCH_SOURCES.md', 'docs/REPORT_CONTRACTS.md']))
            self.assertEqual([], v.validate_contract_bundle(root))

if __name__ == '__main__':
    unittest.main()
