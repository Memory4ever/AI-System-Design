# 2604.24929v1：翻译 Agent benchmark 的功能有效性

本日作者有界必要证据审阅；未作非作者单篇、日期例外或日级 Gate。身份：[official exact-v1](https://arxiv.org/html/2604.24929v1) *GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation*。本日 arXiv 公告窄批次链暂支持北京时间 04/29 08:00 的 v1 归属，不以页眉 04/27 投稿日期独证首次公开；若同家族已有更早正式正文须定点重开。

## 原文必要机制与结果

§3–5 的 GAIA 派生任务不是只把 query 译顺：输出格式、query–answer key 身份、地区事实与可解路径要同时保持。§4.2 的两端反例明确：本地棋步有效答案会因沿用英文 `Rd5` 被错判，而 IOC `CUB` 这样的固定代码若被译为普通词则破坏三字符输出合同。§4.3–4.4 另指出 locale 变化和目标语言网页可得性会改变任务本身难度。作者用确定性语言/泄漏/固定项检查、单轴 LLM judges 和双人层级人工审阅修订原机器翻译 GAIA；每种目标语言都是同一 165 条 validation QA，五语言是 Arabic/German/Hindi/Korean/Brazilian Portuguese。Table 1 task-level edit rate 84.8–100%，并非所有文字 84.8–100% 重写。

§6 Table 2 用 GPT-5.4、Gemini 3.1 Pro、Claude Opus 4.6 的同一 Open Deep Research harness，对每语言原 MT 与修订版比较。各格为 165 题的 pass@1 accuracy，manager 最多 12 步、search subagent 最多 20 步；修订后增幅约 `10.9–32.7` 个**百分点**，并不证明所有非英语 gap 都由翻译造成。最低修订后与 English 差距 3.1pp 是特定 model/language 格；Arabic 仍有大 gap。§6 Fig 7 的 67.9% functional-alignment flip 是**被标注该问题且有共同存在问题**的切片，原文明确因 issue 共现只能作相关而非单因素因果；不能从该图宣称 functional audit 独自产生 67.9% 总收益，也不能把文化改写后的 GAIA 当跨语言完全等价。

## 实际 owner 与处置

唯一 owner `EVAL-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 现文“跨语言派生 benchmark 视为 semantics-preserving compilation”已具体要求保留 task invariant、label/choice identity、format/parser contract、language-specific invalid cases、item transformation lineage，逐项 validation 与 native review，并明说翻译会改变难度/知识前提、派生版不能与英文分数直接互换。其后 locale 段也将显式地方知识与未指定地区的默认选择分账。本篇受控 MT→审校对比可作这些合同的独立受限例证，但目前没有超出现有 owner 的新责任或验收条件。作者侧拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard，`No Change — Existing Coverage`，不是整本“所有多语评测”已有覆盖。若非作者复核发现其 stepwise query-answer/external tool 可达性构成现文未承载的具体缺口，再仅重开 Ch66 对应一段；暂不申请共享锁。

本项原在 106 篇完整题摘的潜在线索中，必要审阅不增减 `64 潜在＋41 贡献前闭＋1 早公开隔离` 的工作账；正式候选冻结、source/日期与独立证据 Gate 未过。
