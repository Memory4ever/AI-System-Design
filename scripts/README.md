# 项目工具

当前报告执行入口由根目录研究 Prompt 定义；脚本不能代替贡献判断、证据阅读或 Books 语义复核。

| 工具 | 用途 |
| --- | --- |
| [validate_research.py](validate_research.py) | 报告、来源表和 Markdown 的结构校验入口 |
| [check_report_v3.py](check_report_v3.py) | 当前简版报告的校验实现，由入口调用 |
| [research_records.py](research_records.py) | 已有报告格式的兼容依赖；新报告不需要额外 JSON 投影 |
| [extract_arxiv_evidence_inventory.py](extract_arxiv_evidence_inventory.py) | 为已有 v1 HTML/文本建立章节目录，不代替审阅 |
| [fetch_arxiv_datacite_created_month.py](fetch_arxiv_datacite_created_month.py) | 按需恢复月级身份元数据，不是日常必跑步骤或公开日期证明 |
| [refresh_research_manifests.py](refresh_research_manifests.py) | 检查已有材料校验清单；不要求新报告创建清单 |

## 检查已有旧格式

当前报告使用 `python3 scripts/validate_research.py --report <报告路径>`，读取当前来源清单。
日期窗口回归测试：`python3 -m unittest scripts.test_report_windows`（包含日窗、七日周窗、跨年和闰日边界）。
对已获用户授权保留旧候选日期的增量补查，可用 `**冻结候选日期：** [原报告](同日补查前档案路径)` 显式引用本日 `_sources/daily-YYYYMMDD/baseline-before-supplement-YYYYMMDD.md`。兼容读取旧 Candidate Ledger 的精确版本 arXiv 身份及公开日，或原 V3 候选表的完整材料链接（标题与 URL）及原日期；均核对原标题/窗口。仅这些原日期不重新归属，其他字段仍正常校验。新增材料仅按补充自然日检查，缺档案、改原日期、替换材料链接或原表结构不合法均报错。此字段不是用户授权或语义验收的替代品。
仅核对旧报告原有结构时，可显式运行 `python3 scripts/validate_research.py --report <旧报告路径> --registry <对应旧来源快照>`。
工具要求实际快照与报告声明匹配；没有快照就不能核验旧结构，不回填虚构字段或修改报告版本来凑通过。
旧结构通过不是当前标准验收，也不代表 Evidence、Books 或独立语义复核完成。
