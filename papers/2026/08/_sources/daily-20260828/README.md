# Daily 2026-08-28 Source Snapshot

- Window: `2026-08-27T09:00:00+08:00` ～ `2026-08-28T09:00:00+08:00`
- arXiv primary closure: OAI-PMH `ListRecords`, day partitions `2026-08-27` and `2026-08-28`
- Enumerated sets: complete `cs` set plus `stat:ML` and `eess:AS` overlap partitions
- Raw records across six snapshots: 2,234；strict-window unique v1 records: 434
- Strict-window first v1: `2026-08-27T01:03:35Z`
- Strict-window last v1: `2026-08-27T16:48:39Z`

The Atom API returned HTTP 429 during this run. The OAI-PMH snapshots are the registered official fallback and were filtered by each record's first `<version>` timestamp, not by OAI datestamp alone. The two complete `cs` day partitions cover every registered core and keyword-filtered computer-science category; `stat.ML` and `eess.AS` were separately enumerated because they can contain records without a `cs.*` cross-list.

| Snapshot | Raw SHA-256 | Gzip SHA-256 |
| --- | --- | --- |
| `arxiv-oai-cs-20260827.xml.gz` | `70c4461f4ae92ca639524dd9c4755da6a6c37f4f74f1f23e1f7c118957ca2180` | `439d7d123fe7e7a1594ca872fedc126a7d33a35938d3eafd5a90e46fbdbb7368` |
| `arxiv-oai-cs-20260828.xml.gz` | `66384647c99cb2c6dd11a6fc92f67ad648f76a10994c8023fc61a55052e6593f` | `dc3b9b112b002634d0346abb4445c23ef2c0a1841104843dbf026f0583eb18e5` |
| `arxiv-oai-stat-ML-20260827.xml.gz` | `6524aecd547f4b70db9426158d7e1e7e025b2f03108f9201708342e3888a876e` | `1251bf152e579f277d4335c0d38be5049d84da84e030806f9b27aff258e85be4` |
| `arxiv-oai-stat-ML-20260828.xml.gz` | `943acd15a31dff8f610d2c51e5665f5a707bbbac197c50799ae6bbf4ff168586` | `bc28b9f73dcad25d009a675de40143cce10ad52c0b6813c4245eedb20a860665` |
| `arxiv-oai-eess-AS-20260827.xml.gz` | `59ecd53f9746b926e41af30850cb36fa6758d9fe83bb0860596853d0b66008b5` | `dd31ae09b951b2540b17a15a15a04ccd72643f0215301d95bfa747adae082b06` |
| `arxiv-oai-eess-AS-20260828.xml.gz` | `d4acb9212e6f6102fbcd7032852f672c373ef295c13bb548bb9a3906d479268e` | `509c1bb2614b6e322b66899dd2083374eab6ccc78dd0417497a0475e6e47fdc6` |

Exact-version manuscript review used `arxiv.org/pdf/<id>v1` or `export.arxiv.org/pdf/<id>v1`. When a just-announced PDF returned 404 or arrived truncated, `ar5iv.labs.arxiv.org/html/<id>` supplied a readable rendering of the same v1 identity; this fallback is recorded per candidate and is not treated as a separate Source Family.

`required-daily-organizations-20260828.md` freezes the organization-source listing decisions and the bounded Hugging Face discovery limitation. These snapshots establish discovery and event identity only; they do not replace the per-family Source Review in the Daily report.
