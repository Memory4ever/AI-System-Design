# 2026-05-10 V3 Independent Final Audit

## 独立性与范围

- Reviewer：`fresh-context:may10-independent-gate-20260914`。
- Independence：未参与本日 V3 作者重建，也未参与旧 436/57/29 cohort 的生成或 Books 写回。
- Window：`[2026-05-09T09:00:00+08:00, 2026-05-10T09:00:00+08:00)`。
- Scope：Daily 的 13 个机构来源、arXiv 公开节奏、ERNIE 5.1、Seed / arXiv `2605.09233`、旧 cohort
  身份守恒与 supersede 边界；本终审不修改 Books。

## 1. 时间与 arXiv owner

窗口换算为 UTC `2026-05-09T01:00:00Z ～ 2026-05-10T01:00:00Z`。arXiv 的
[官方公开规则](https://info.arxiv.org/help/availability.html)说明稿件通常在 Sunday～Thursday 通过 scheduled
announcement 公开，Friday 和 Saturday 没有公告；Thursday 14:00～Friday 14:00 ET 的队列到 Sunday
20:00 ET 才公告。2026 年 5 月为 EDT，Sunday 20:00 ET 等于北京时间 2026-05-11 08:00，晚于本窗右边界。
因此本窗 arXiv public event 确为 0。

[`2605.09233`](https://arxiv.org/abs/2605.09233) 的 v1 submission history 为
`Sun, 10 May 2026 00:23:05 UTC`，即北京时间 08:23，虽然投稿落窗，但当时尚未进入 scheduled announcement。
submission event 不能替代 public event；将它排除于 05-10 denominator 正确。后续 Seed 目录展示时间只用于
family 身份恢复，不能重写 arXiv 首次公开日。

## 2. 机构来源与两个边界事件

[ERNIE 5.1 官方正文](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)的 JSON-LD
`datePublished` 为 `2026-05-09T00:00:00Z`，即北京时间 08:00，早于窗口左边界一小时；归属 05-09 正确。

对 13 个 Daily 机构入口重新核对后，DeepSeek、Hunyuan、ZAI、Seed、ERNIE、MiniMax 以及 Anthropic 当前
可见/嵌入式历史记录中未发现落窗且通过贡献 Gate 的事件。Anthropic 的相邻公开时间为
`2026-05-08T12:18:00Z` 与 `2026-05-14T17:06:12.172Z`。OpenAI、Google AI、Meta、Qwen、Moonshot 与
MiMo Blog 没有可复算的官方日级历史分页；它们按终态 Coverage limitation 隔离，不用于正向证据、Books 或
“全站绝无遗漏”断言。故可以确认的是“已核实公开事件中的候选为 0”，不能写成“13 个机构全站绝对零事件”。

## 3. 旧 cohort 隔离与身份守恒

独立复算结果：

| 历史层 | 数量 | 守恒与用途 |
| --- | ---: | --- |
| `screening-ledger-final.json` identities | 436 | 436 个唯一 identity 均仍在文件中；仅作迁移身份与旧方法取证 |
| `exact-v1-review-packet.json` items | 57 | 57 个唯一 arXiv ID 均保留；不得继承为 05-10 Evidence |
| `BOOKS_WRITEBACK_QUEUE.md` headings | 29 | 29 个 Source Family 均保留；不得继承为 05-10 Books queue |

旧 cohort 的首条 identity 已显示 `submitted_v1_utc=2026-05-09T01:05:34Z`，review packet 还包含
`2605.109xx`、`2605.163xx` 与 `2605.23951` 等显然不可能由 05-10 本窗公开事件拥有的 family，进一步证实
旧口径混入投稿时间、later-indexed identity 或回填。三个旧 Markdown 结果均有 V3 warning，同目录 JSON、TSV、
脚本和附件由 `V3_OWNER_RECONCILIATION.md` 统一声明为历史取证材料；没有删除 identity，后续可按每个 family
真实 scheduled announcement 或其他官方首次公开日迁移。

## 4. 修正与 Gate 结论

终审发现一处过强表述：作者稿把“已核实公开事件中的候选为 0”写成“全来源候选 denominator 为 0”。已在
Daily 与 owner reconciliation 中收紧，避免把六个终态受限入口（包括 MiMo Blog）的历史分页缺口算成零命中证明。
该修正不改变 arXiv、ERNIE、Seed 或旧 cohort 的归属结论。

- Coverage：已处理到安全终态；六个受限入口（包括 MiMo Blog）保留精确限制与定点重开条件。
- Evidence：通过；本日没有正向候选，因此没有未完成的 Source Review。
- Books：通过；本日决定为 `No Change`，没有写回；旧 29 项不属于本日 queue。
- Independent Review：通过。
- Final Status：完成。

机器校验结果由本轮命令重新生成，仅作为格式和引用证据，不替代上述语义终审。
