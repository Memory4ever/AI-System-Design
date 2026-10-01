# 2026-09-15 Screening Record

## 窗口与公告归属

- Daily 窗口：`[2026-09-14T09:00:00+08:00, 2026-09-15T09:00:00+08:00)`。
- arXiv 事件：官方 past-week 页的 `Tue, 15 Sep 2026` 公告块，按北京时间约 `2026-09-15T08:00:00+08:00` 归属本窗。
- 检查分类：`cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA`。
- 12 个分类原始条目跨分类去重后为 1,064 个身份。

## 日期与重复归并

以下 12 个旧 ID 是本日 cross-list/replacement 事件，不是本日首次公开正文，不进入本日候选分母：

- `2411.04319`
- `2504.01157`
- `2504.19962`
- `2511.09665`
- `2607.12399`
- `2607.14162`
- `2607.21411`
- `2608.14714`
- `2609.03301`
- `2609.10714`
- `2609.11365`
- `2609.11999`

其余 1,052 个本窗身份按完整题名进行范围/贡献判断。737 个题名含义已经足以明确关闭；315 个含义不明确或可能影响 AI-System-Design 的条目进入完整题名与摘要语义筛选，身份见 [`title-screen-review.txt`](./title-screen-review.txt)，完整题摘见 [`title-abstract-review.json`](./title-abstract-review.json)。逐身份的日期/深度/处置与具体关闭理由见 [`denominator-closure.tsv`](./denominator-closure.tsv)，它同时证明 12 个旧事件、737 个题名关闭、270 个题摘关闭与 45 个候选可以相加回原始 1,064 个身份。

## 冻结候选分母

315 个完整题摘审阅后，270 个因以下具体边界关闭：仅把既有模型用于垂直领域；只提供单任务/单 benchmark 局部增益且没有新的机制或评价合同；属于普通 CV、robotics、RL、数据库、HPC 或算法研究而未直接改变大模型及其基础设施；是 survey/position paper；或其增量不足以改变当前设计判断。

首次筛选保留 14 个 arXiv 材料家族；fresh-context false-negative audit 依据来源/主题/关闭理由分层检查全部 14 个拟入选项、所有安全/纠错信号项，并对题摘关闭项做受影响扩查。它发现同一系统性错误：原筛选把“已有章节存在相近原则”误当成“没有新增机制/证据”，因而漏掉 24 项。这 24 项全部重新读取完整题摘与 exact-v1 的相关 Method、Evaluation、Limitations；受该错误影响的 315 项题摘层已重新裁决，题名即可明确关闭的 737 项不受影响。

随后对 13 个摘要首句解析错误做定点返修：7 项恢复为候选，6 项按完整摘要的具体贡献边界关闭。因此本窗最终保留 45 个 arXiv 材料家族：

- `2609.13161` — PDD
- `2609.13205` — Self-Indexing Attention
- `2609.13285` — Grouped Value Attention
- `2609.13537` — VAMP
- `2609.13585` — mKernel
- `2609.13672` — Recoverability as a System Primitive
- `2609.13692` — Prefix Sharing Is a Sorting Problem
- `2609.13714` — Certifying Model Upgrades
- `2609.13866` — The Filter Metric is Safety-Critical
- `2609.14744` — AcquireBound
- `2609.14758` — Fabrication After Tool Failure
- `2609.14780` — The Stochastic Deputy
- `2609.15021` — Shared KV Caching for Replicated 27B Inference
- `2609.15504` — How Lossless Is Lossless Speculative Decoding?
- `2609.13149` — BudgetBench
- `2609.13544` — PEAT
- `2609.13592` — BOOST
- `2609.13612` — AttnFuse
- `2609.13637` — Identity Is More Than Recall
- `2609.13642` — When Compliance Data Masquerades as Evaluation
- `2609.13800` — Do Not Restart
- `2609.13889` — Persistent Memory Poisoning
- `2609.14003` — FlowSeal
- `2609.14157` — When Tools Get in the Way
- `2609.14237` — OpWeave
- `2609.14306` — Flattening Every Memory Peak
- `2609.14507` — InplaceKVCache
- `2609.14717` — Carryover Drafting
- `2609.14773` — Pull
- `2609.14872` — AgentKV
- `2609.14987` — ActGuard
- `2609.15013` — Overflip
- `2609.15030` — Hybrid-state Cache Recovery
- `2609.15230` — ETCInfer
- `2609.15359` — MAPS
- `2609.15397` — Agent-tool Effect Histories
- `2609.15561` — Factuality Judge Perturbation
- `2609.15636` — Trillion-Parameter MoE in a Box
- `2609.13489` — QCAR
- `2609.13645` — ForgeTrain
- `2609.14579` — Synthetic–Authentic RAG Evaluation
- `2609.14631` — IntentCap
- `2609.14643` — BigMoMo
- `2609.14767` — Loop-Back Authority
- `2609.15627` — DeepSeek-V4-Flash on AMD gfx90a

45 项 exact-v1 HTML 保存在 [`html/`](./html/)；恢复项的证据位置与边界见 [`evidence-review.md`](./evidence-review.md)，Books writer 的精确输入见 [`books-queue.md`](./books-queue.md)。正文判断、评分与最终状态仍以 [`../README.md`](../README.md) 为准。这里的 315 不是候选数，1,064 更不是“对项目有贡献的论文数”。

`arXiv:2609.13285` 的官方 version history 显示 v1 首次公开属于本窗；v2 提交于 `2026-09-15T23:00:18+08:00`，在本窗终点之后。因此本日报审阅并评分 exact-v1，不能把 v2 倒灌为本窗 revision。
