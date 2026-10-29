# Daily Research — 2026-06-01

**规范：** V3
**窗口：** 2026-05-31T09:00:00+08:00 ～ 2026-06-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗复用并核实 canonical owner 恢复结果：注册 arXiv 分类在官方可用性日历、DataCite DOI identity/created 与 first-public owner 对账后，本日 arXiv owner bucket 为 0。旧 submission-date 报告中的条目已经迁往各自真实公开日，不能在本日重复计入候选；本轮厂商源再认证恢复 MiniMax M3，并已完成证据审阅与 Books 判断。

本次没有继承旧 `Complete` 标签，而是重新检查 arXiv 空分母的来源依据、厂商页面、迁出路径、撤回清理与 Books 影响。撤回家族 `arXiv:2606.24369v1` 不在本日 owner bucket，也没有保留任何候选、采用或 Books 链路；MiniMax M3 的长期机制已由后续 exact-v1 在 `MODEL-LONG-CONTEXT` 承载，Books 维持不变。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：本窗无保留事件 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；MiniMax M3 的 JSON-LD 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-ARXIV | [官方可用性日历](https://info.arxiv.org/help/availability.html)、DataCite DOI identity/created 与 [`official-arxiv-first-public-owner-receipt-v1.json`](../_sources/daily-20260601/official-arxiv-first-public-owner-receipt-v1.json) 复核；[`canonical-raw-identity-inventory-v2.1.json.gz`](../_sources/daily-20260601/canonical-raw-identity-inventory-v2.1.json.gz) 的本日 owner identity 为 0 | 已检查 | 无 |

DataCite 只承担 DOI identity 与 immutable `created` 的交叉核验，不承担论文机制证据。空 bucket 是本日没有 owner identity 的结论，不宣称互联网在该时段绝无其他材料。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MiniMax M3](https://www.minimax.io/blog/minimax-m3) | 2026-06-01T01:31:18+08:00 | MSA 把长上下文稀疏选择与 KV-outer block execution 联合设计，并披露原生多模态训练与 Agent workload；3+3+2=8 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT` — [章节](../../../../books/part-02-model/22-long-context.md)；正文锚点「稀疏选择器本身还需要明确 gradient ownership」 |

本窗 arXiv owner identity 为 0；厂商源再认证恢复 1 个候选家族。迁往其他公开日的旧 arXiv 条目不在本日报告重复评分。

## 4. 证据与知识整合

### [MiniMax M3](https://www.minimax.io/blog/minimax-m3)

官方 Blog 的 JSON-LD 把发布时间固定为 `2026-05-31T17:31:18Z`。正文披露 MSA 以 blockwise selector 缩减 full attention，并把执行组织为 KV-outer gather-Q，使命中同一 KV block 的 query 共享连续读取；同时说明 native multimodal 从训练起点混合 modality。它证明的是厂商公开架构和作者实验，不证明 1M Context、4×/9×/15× 或能力分数可跨模型、硬件、精度、batch、并发和 SLO 外推；Blog 当时也说明完整 technical report 与权重将在以后发布。

`MODEL-LONG-CONTEXT` 后续已用 `arXiv:2606.13392v1` 把 selector gradient ownership、GQA-group/block selection、KV-outer reuse、hot-block load balance 与 dense fallback 写入正文。因此本事件是同一机制家族的首次官方公开，本次不重复写 Books；模型与多模态产品声明不替代其后 exact-v1 的证据边界。

撤回家族 `arXiv:2606.24369v1` 已从 selected、candidate 与 Books queue 清除。本次再次确认本日报告及对应 owner queue 中没有该家族的正向采用链；其他有效材料的证据不受该撤回清理影响。

## 5. 缺口与下一步

无

本窗没有外部材料请求或可执行待办。跨日对账只用于确认 arXiv bucket 为空；MiniMax M3 已作为独立厂商候选完成证据与 Books 比较。

## 6. 复核

复核者：`fresh-context:canonical-owner-empty-denominator`（复用未变化的非作者独立复核）

结论：通过

复核重新检查了本日 arXiv owner receipt、0 条 arXiv raw identity、厂商候选、跨日迁出关系、撤回家族清理与 Books 比较；没有沿用旧完成标签。V3 结构校验与限定 diff 检查在本轮完成后统一记录。
