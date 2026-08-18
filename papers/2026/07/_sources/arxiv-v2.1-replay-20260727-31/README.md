# arXiv V2.1 Replay Snapshot — 2026-07-27～2026-07-31

该目录冻结 2026-07-27～2026-07-31 Daily V2.1 回放使用的官方 arXiv Atom 响应。所有 Daily 窗口均按 Asia/Shanghai 的 `[前一日 09:00, 当日 09:00)` 归属；查询使用等价 UTC 边界，v1 以 Atom `published` timestamp 为准。

## Query Coverage

| File | UTC query | Start | Entries | Total Results | SHA-256 |
| --- | --- | ---: | ---: | ---: | --- |
| `arxiv-20260727-29-start0000.xml.gz` | `submittedDate:[202607260100 TO 202607290100]` | 0 | 2000 | 2924 | `5a5666244bd213f327db44542c5d4ac951e7ab79926d49fca3bc3b52f0a0c345` |
| `arxiv-20260727-29-start2000.xml.gz` | `submittedDate:[202607260100 TO 202607290100]` | 2000 | 924 | 2924 | `aa91527bdfdbcbdf7fad1b64f292ced980e129d1aa6a3beab349b93cfa94ef42` |
| `arxiv-20260729-31-start0000.xml.gz` | `submittedDate:[202607290100 TO 202607310100]` | 0 | 2000 | 2539 | `183bfd6dad34883fb0ed2321e3b3bca7f6f9ef7fe9d00c0140c89dc928117999` |
| `arxiv-20260729-31-start2000.xml.gz` | `submittedDate:[202607290100 TO 202607310100]` | 2000 | 539 | 2539 | `8bf79cb9d6d1d8fdb44fa5378713d3ad794993661faffca56f8bb16b55090f7f` |

四个响应共有 5,463 个唯一 arXiv ID。按严格 Daily 窗口路由后的 raw counts 为：2026-07-27 `549`、07-28 `1174`、07-29 `1201`、07-30 `1186`、07-31 `1353`。

## Important Revision Packet

SafeFlow `arXiv:2607.25255v2` 的 `updated=2026-07-29T23:58:46Z`（北京时间 2026-07-30 07:58:46）落入 7 月 30 日 Daily 窗口。为了不用当前 arXiv 页面覆盖历史 revision 证据，本目录同时冻结了审阅时使用的 exact v1/v2 HTML：

| File | Evidence Version | Retrieved At | Uncompressed SHA-256 | Archived SHA-256 |
| --- | --- | --- | --- | --- |
| `arxiv-2607.25255v1.html.gz` | `arXiv:2607.25255v1` | 2026-08-26 | `832e7e0acb7e3ef2e73c5e58cd02ee0b7ff9cef9004e8eaf27490cc5c7e212d6` | `7729795db4a52a8ce52d8eb21a58ce41bb029031afbe08982db0d59a1377a53e` |
| `arxiv-2607.25255v2.html.gz` | `arXiv:2607.25255v2` | 2026-08-26 | `f1cd189b066a9fe6f022de5556b9f9649d8e745048f84352736dda23430df553` | `ed0384e8a266a607f26d64c54140a5e0c72ad28704c5d67b36d986762acd7e42` |

逐节比较支持的有界结论是：v2 在 abstract 新增公开仓库 `https://github.com/Haowen-academic/SafeFlow`，并修订作者/机构元数据；Method、Architecture 与 Experiments 的主体没有形成新机制或新 Source Family。这一结论只支持 `important_revision` reconciliation，不把代码可用性误写为新的性能或安全证明。

## Canonical Manifest

Manifest 行按 basename 排序，格式为 `basename<TAB>sha256(file)<LF>`。canonical manifest SHA-256：

```text
ec82a1f28ee96359d86fd58b84301083004450e32e146a7c5bfa25fec413c6b6
```

这些快照只证明 arXiv API 的候选分母。机构历史页面与 Hugging Face Daily Papers 缺少可冻结的严格 09:00 intraday cursor，因此其 Coverage 限制保留在各 Daily 的 Source Coverage Receipt 中。
