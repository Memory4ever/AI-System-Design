# Daily 2026-08-26 Source Snapshot

- Window: `2026-08-25T09:00:00+08:00` ～ `2026-08-26T09:00:00+08:00`
- Query: arXiv Atom API `submittedDate:[202608250100 TO 202608260100]`, ascending, `start=0`, `max_results=2000`
- API total: 930；returned entries: 930；pagination closed in one page
- First result: `2026-08-25T01:01:48Z`
- Last result: `2026-08-25T17:59:49Z`
- Raw XML SHA-256: `9b506122aec302a1ab1a4d525d795a2ca4cc01773df779701038bfb2636045d0`
- Archived gzip SHA-256: `ca0c46825a796c0b1af19e581136ac1f52b69f40fc3488470a573d12d50362e2`

该快照只证明 arXiv 查询结果与候选分母的输入，不代替逐篇 Source Review。

## Additional Required Daily Receipts

- `hf-papers-20260825.md`：冻结 HF 8 月 25 日 discovery 页面的 35 条完整 identity。HF 只提供发现线索；其中更早公开的 arXiv family 进入独立 delayed-discovery recovery ledger，不进入 8 月 26 日候选分母，也不在本轮重开历史 Daily。
- `huawei-noah-news-20260826.md`：冻结 Huawei Noah 官方 dated news archive 的 no-hit 水位。
- `required-daily-organizations-20260826.md`：冻结 19 个 Required Daily 机构来源的规范化 listing 水位、响应摘要、边界判断与 fallback reconciliation。
- `organization-snapshots/`：冻结 18 份 ordinary-client response bytes 及 raw/gzip digest；OpenAI
  response 是 Cloudflare challenge，只作 access receipt；`rendered-listing-extracts-20260826.md`
  冻结五个动态页面的规范化 listing 证据。

## Artifact Recovery Receipts

- `SF-2026-OPDVR`：按报告截止时刻查询 GitHub Commits API：
  `repos/LeapLabTHU/OPDVR/commits?until=2026-08-26T01:00:00Z&per_page=100`。返回唯一 commit
  `2e14685ea4cbf051073aa0a26bc0e9c75f17878d`，committer time
  `2026-08-25T14:32:43Z`；JSON 3,657 bytes，SHA-256
  `de88de9ea27d64b65b934c8fd62b35b3b901ad7b57eb8b9125ec2d89fed93193`。
- `SF-2026-RESISPEC`：v1 声明的 `https://github.com/Czzzk/Resispec` 在本轮访问时返回 404；
  因此 mechanism claim 只使用 versioned arXiv v1，不形成代码实现主张。
- `SF-2026-JUDGE-DELTA-VALIDITY`：论文报告公开 TriDeHall-ECP dataset；本轮长期机制判断只使用
  versioned arXiv v1 的 intervention design、实验与限制，不使用无法固定 event-time revision 的 dataset 内容。
