# arXiv V2.1 Replay Snapshot Manifest — 2026-08-01～2026-08-24

本目录保存 2026-08-01～2026-08-24 Daily V2.1 Full Replay 使用的原始 arXiv Atom 响应。文件只做 gzip 压缩；下表的 Raw SHA-256 对解压后的 XML 计算，因此不依赖压缩时间或 gzip 实现。

**Retrieved At:** 2026-08-25（Asia/Shanghai）

**Canonical Manifest Algorithm:** 按原始 basename 排序，每行编码为 `basename<TAB>raw-sha256<LF>`，再对完整 UTF-8 manifest 计算 SHA-256。

**Canonical Manifest SHA-256:** `4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7`

## Snapshot Files

| Raw basename | Query window (UTC) | Start | Max results | Raw SHA-256 | Gzip SHA-256 |
| --- | --- | ---: | ---: | --- | --- |
| `arxiv-20260801-24-g01.xml` | `202607310100 TO 202608040100` | 0 | 2000 | `7e688effccb55c5b491868e0fe1cf986bb8f2c51856d028f75c52c3b0ac1e723` | `37e49af29a90a4c22f1071ceb0db02ec0cd88f9e4fe23b3cb7fd2ab49226a30e` |
| `arxiv-20260801-24-g02-page2.xml` | `202608040100 TO 202608080100` | 2000 | 2000 | `4b6de8539528d517c31307666c0b400e9927a40ddb907f7ed70107a937f996c3` | `fbe7c7fbed594c9aa6cccc0c8f899fc57a70f3376ddd501167220b71911d51c2` |
| `arxiv-20260801-24-g02.xml` | `202608040100 TO 202608080100` | 0 | 2000 | `f20e84ae2a50ff3dbe9e0b281427ed9a3a309985e44f8ba78aee9749a87e9940` | `08e671ddbb7e262de75cef262936e84c073b2d91c6b383a1171a3687472091dc` |
| `arxiv-20260801-24-g03.xml` | `202608080100 TO 202608120100` | 0 | 2000 | `0d8f7b3ee6421ac12323ba4d7ce3d5d520b6b4964b69c162c759db54f8e14529` | `2a53c24b5f7bb443b9c8e7e4cd7be225685aece698e6dde974c2143d27e5f3f6` |
| `arxiv-20260801-24-g04.xml` | `202608120100 TO 202608160100` | 0 | 2000 | `254289cbc96c6fac55bcbee2f016af52facd9336452e0fae37e04ad91c6a8899` | `86864108a6b9defead2130acf55a346ca8b3a5bd1185ba32694e79cd8389765c` |
| `arxiv-20260801-24-g05.xml` | `202608160100 TO 202608200100` | 0 | 2000 | `c6e1556be44f658612d3c885852f6ebac051fa5c9c8d53c2f4700ca78eb4ff51` | `fef57262bf348424e92aa0b4562622d5f370e077fad05891c32bebbe99555e5c` |
| `arxiv-20260801-24-g06.xml` | `202608200100 TO 202608240100` | 0 | 2000 | `0f3583dd6e0cb67191bebcf49b351944faa47bcf9e549c54fd101a625b0b1fb6` | `9c118df9b1525eb71c15cffc287f90a841012d03e232377d128305a438ce0183` |

## Query Contract

所有请求使用同一分类过滤器：

```text
(cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.IR OR
 cat:stat.ML OR cat:cs.CV OR cat:cs.RO OR cat:cs.SE OR cat:cs.CR OR
 cat:cs.AR OR cat:cs.PF OR cat:cs.OS OR cat:cs.PL OR cat:cs.MA OR
 cat:cs.DB OR cat:cs.NI OR cat:eess.AS OR cat:cs.SD)
AND submittedDate:"<UTC window>"
```

API endpoint 为 `https://export.arxiv.org/api/query`；排序和分页信息保留在每个 Atom feed 的 `<title>` 与 `<link>` 中。Daily 再以 entry 的 `published` timestamp 转为 Asia/Shanghai，并按 `[前一日 09:00，当日 09:00)` 半开窗口分桶。Cross-listing 以 arXiv ID 去重，revision 不作为新 Source Family。

该快照只闭合 arXiv 路由，不能替代模型机构、GitHub release 或 Hugging Face 历史页面的独立 Coverage Receipt。
