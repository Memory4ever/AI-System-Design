# AI Research Weekly — 2026-W10

> Coverage Window: 2026-03-02～2026-03-08
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: Source-Family Books Gate Complete — 36/36 final dispositions reviewed: 27 Refine, 4 No Change, 5 Weekly Only/Disputed; recorded-candidate Evidence Gate complete; broader historical discovery coverage keeps Archive Completion Gate Open

## Executive Summary

旧版只保留 GPT-5.4、Anthropic labor-market measurement 与 WAXAL 三项，无法代表本周研究面。
按 primary first-public date 重开后，目前恢复 23 项 in-window 候选，覆盖 rubric/judge、interactive
tool-use data synthesis、MoE routing、low-bit training、heterogeneous-agent RL、memory retrieval 与
indexed experience、multimodal safety、coding-agent evaluation、interactive benchmark、enterprise search
Agent、reasoning compression、CoT monitorability 与 long-context prefill。另有 Qwen3-Coder-Next 和
SkillNet 虽在 W10 的 discovery spillover 中出现，但 arXiv v1 分别为 2026-02-28 与 2026-02-26，已归回
W09 并重开其 Evidence Gate。

原 candidate set 的 23/23 候选已经完成 current-schema Full Source Review，旧版三份 Source Review 也已重新核对
完整官方材料、revision、artifact 和目标章节；新增 spillback 当前完成 11/11，故全周进度为 34/34。Evidence
Gate 已闭合。旧 candidate set 的结论只说明其 primary evidence 与逐项 disposition 已闭合，不表示所有 Books
候选都应写入正文。当前最重要的候选不是按 headline 排名，而是四条可能
形成长期演进链的机制：
`verifier/rubric as training state`、`memory index/read policy as learned state`、`interactive/executable
evaluation` 与 `prefill sparsity search overhead`。

2026-08-09 的 W11 推荐流复核又发现 11 个 v1 date 落在 3 月 2～8 日的候选。它们未包含在上述
23 项中，因此 W10 的当前候选账本为 34 项，原 Evidence Gate 只对原 candidate set 成立。Multi-Head
Low-Rank Attention、Believe Your Model、Progressive Residual Warmup、BandPO、Sparse-BitNet、ATLAS 与
Terminal Coding Agents 已完成 Full Source Review；AutoResearch-RL 也已完成全文与来源核验，但因 arXiv 管理员
撤稿而降级为 `Withdrawn / Disputed / Weekly Only`。最后三项 HCAPO、Scaling Data Difficulty 与
MicroCoder-GRPO 也已完成，当前没有 `Audit Pending`。既有 18 项 Books disposition 与正文不回滚；新增
11 项下一步仍须逐项完成 Books 去重，不能把 Evidence Gate 通过误写成 Books Integration 已完成。

2026-08-09 的 W12 curation-lag 复核又确认 `Recursive Language Models Meet Uncertainty` 的 v1 date
为 2026-03-07。它不属于 W12，而是新的 W10 spillback。故 `34/34 Passed` 只描述此前候选集，不再
代表 W10 周级 Discovery/Evidence Gate；该候选尚待评分与 Full Source Review。

2026-08-10 又纠正 Nemotron 3 Super 的 source-family 日期：Base checkpoint 在 03-04 已公开，post-trained
checkpoint 在 03-11 公开，04-14 arXiv v1 只是更晚的 formal report。该 family 因而从 W16 回拨 W10，
51 页报告、model cards 与公开 artifact 已完成 Full Source Review；当前账本为 35 个 scored/reviewed
candidates，另有 Recursive Language Models Meet Uncertainty 尚待评分与全文审计。

2026-08-12 已完成最后一项 spillback：Recursive Language Models Meet Uncertainty 的 31 页 sole-v1、
完整 Method、context-length/task-domain experiments、cost comparison、ablation、judge/confidence prompts、
dataset 与 detailed-results appendices，以及 Apple Research 后续 publication record 均已审计。它把 Long
Context 的瓶颈从“是否递归调用模型”推进为“如何在多条 context-interaction programs 中选择 trajectory”，
但 K=8 并行采样只匹配 wall-clock、并未匹配总 calls/tokens/FLOPs；self-consistency、self-reported
confidence 与 trace length 也都是同源 proxy，不是 calibrated ground truth。最终评分 25/30，暂定 Ch22
`Refine — Existing Argument (Experimental)`，Ch72/76/62 handoff。该句记录 2026-08-12 Books pass 前的状态；
2026-08-13 的最终结果见下方 Final Source-Family Books Integration。

## Coverage and Source Coverage

- 模型与研究机构：保留 OpenAI、Anthropic 与 Google Research 三项官方事件；模型内部机制未披露时
  固定为 `Version Fact / Mechanism Not Disclosed`。
- arXiv / 学术来源：按 v1 date 恢复 20 项 in-window 候选；metadata 只证明身份与首发日期，Method、
  Appendix、artifact 和 benchmark contract 仍须逐篇全文复核。
- AI Infra：旧报告的“未发现 stable release”尚未完成 GitHub Releases/RFC/PR 的同周补漏，不能当作
  已证明的空集合。
- Discovery limitations：本轮不能访问 Hugging Face 当日索引，未绕过权限；Google Scholar 与 OpenAlex
  的历史周窗口也未形成可审计结果。当前 23 项是 primary-source 恢复账本，不是数学完备的全集。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GPT-5.4 + system card | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | No Change — Version Fact / Mechanism Not Disclosed |
| Labor-market impact measurement | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | No Change — existing Evaluation evidence contract |
| WAXAL speech resource | 3 | 2 | 4 | 3 | 4 | 4 | 20/30 | Refine — `TRAIN-DATA` / Ch27 |
| RubricBench | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 / Experimental |
| CoVe constraint-guided verification | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-DATA` / Ch27 / Experimental |
| DynaMoE | 2 | 2 | 2 | 2 | 4 | 3 | 15/30 | Weekly Only — Disputed mechanism claim |
| SageBwd | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Refine — `TRAIN-PRETRAINING` / Ch28 / Experimental |
| Heterogeneous Agent Collaborative RL | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Refine — `TRAIN-GRPO` / Ch33 / Experimental |
| MemSifter | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-MEMORY` / Ch77 / Experimental |
| MUSE run-centric safety evaluation | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Refine — `PLATFORM-SECURITY` / Ch72 / Experimental |
| MOOSE-Star | 2 | 2 | 3 | 3 | 4 | 3 | 17/30 | Weekly Only — Disputed complexity/effect claim |
| Phi-4-reasoning-vision-15B report | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Refine — `TRAIN-DATA` / Ch27 / Experimental |
| Memex(RL) | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `AGENT-MEMORY` / Ch77 / Experimental |
| SWE-CI | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 / Experimental |
| Nemotron 3 Super | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Refine — `MODEL-MOE` / Ch21 / Experimental |
| V1 parallel generation/self-verification | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `MODEL-SAMPLING` / Ch20 / Experimental |
| T2S-Bench / Structure-of-Thought | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Weekly Only — No new mechanism |
| Interactive Benchmarks | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 / Experimental |
| KARL knowledge agents | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `AGENT-RAG` / Ch76 / Experimental |
| CRISP / On-Policy Self-Distillation for Reasoning Compression | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-SFT` / Ch29 / Experimental |
| MASQuant | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Refine — `INFER-TENSORRT-LLM` / Ch49 / Experimental |
| IF-RewardBench | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 / Experimental |
| Reasoning Models Struggle to Control their CoT | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `PLATFORM-SECURITY` / Ch72 / Experimental |
| FlashPrefill | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `INFER-PREFILL` / Ch43 / Experimental |
| Multi-Head Low-Rank Attention | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Refine — `MODEL-MULTI-HEAD-ATTENTION` / Ch15 / Experimental |
| Believe Your Model / DistriVoting | 4 | 3 | 4 | 4 | 5 | 4 | 24/30 | Refine — `MODEL-SAMPLING` / Ch20 / Experimental |
| Progressive Residual Warmup | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-PRETRAINING` / Ch28 / Experimental |
| BandPO | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | Refine — `TRAIN-GRPO` / Ch33 / Experimental |
| Sparse-BitNet | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Weekly Only — Disputed artifact order |
| ATLAS / Scaling Agentic Capabilities | 4 | 5 | 5 | 3 | 5 | 5 | 27/30 | Refine — `AGENT-WORKFLOW` / Ch81 / Experimental |
| Building AI Coding Agents for the Terminal / OpenDev | 3 | 4 | 5 | 3 | 5 | 5 | 25/30 | No Change — Ch78/81/84 already cover authority and recovery |
| AutoResearch-RL | 3 | 2 | 2 | 1 | 3 | 1 | 12/30 | Weekly Only — Withdrawn / Disputed |
| Hindsight Credit Assignment / HCAPO | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Refine — `TRAIN-GRPO` / Ch33 / Experimental |
| Scaling Data Difficulty / MicroCoder Dataset | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | No Change — Ch27 already owns policy-relative difficulty and lineage |
| MicroCoder-GRPO / Breaking Training Bottlenecks | 4 | 4 | 4 | 2 | 5 | 4 | 23/30 | Refine — `TRAIN-GRPO` / Ch33 / Experimental |
| Recursive Language Models Meet Uncertainty / SRLM | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `MODEL-LONG-CONTEXT` / Ch22 / Experimental |

评分是 discovery 优先级，不代表论文结论、作者 benchmark 或 Books disposition 已成立。所有 20+ 候选
在当前 Gate 下都必须阅读完整论文/报告；旧版三项也重新进入 revalidation。当前 36 个 scored candidates
均已完成相应 primary-source review 或可信拒绝核验；没有未评分 spillback pending。评分只表达
research priority，不替代后续 Books 去重。

## Recovered Candidate Census

| Event Date | Candidate | Primary Source | Initial Scope Decision | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-02 | RubricBench | arXiv:2603.01562 v1 + official dataset/evaluator | Ch62 owner; Ch27～29 handoff | Refine — Ch62 Integrated / Experimental |
| 2026-03-02 | CoVe | arXiv:2603.01940 v1 + project/model/dataset artifacts | Ch23 owner; Ch25/29/62/74/77 handoff | Refine — Ch23 Integrated / Experimental |
| 2026-03-02 | DynaMoE | arXiv:2603.01697 v1; no official code located | Ch21 claim check; Ch32/40/45 boundary | Full Review Complete — Disputed / Weekly Only |
| 2026-03-02 | SageBwd | arXiv:2603.02170 v1; related SageAttention code has no SageBwd path | Ch24 owner; Ch14/32/33/45 handoff | Refine — Ch24 Integrated / Experimental |
| 2026-03-03 | Heterogeneous Agent Collaborative RL | arXiv:2603.02604 v1/v2 + official code | Ch29 owner; Ch28/31/78 handoff | Refine — Ch29 Integrated / Experimental |
| 2026-03-03 | MemSifter | arXiv:2603.03379 v1 + official code/training/reward/toolkit | Ch73 owner; Ch72/29/75/77 handoff | Refine — Ch73 Integrated / Experimental |
| 2026-03-03 | MUSE | arXiv:2603.02482 v1 + official web app; public code not located | Ch68 owner; Ch62/69 handoff | Refine — Ch68 Integrated / Experimental |
| 2026-03-04 | MOOSE-Star | arXiv:2603.03756 v1/v4 + official code | Ch75 claim check; Ch72/62/77 boundary | Full Review Complete — Disputed / Weekly Only |
| 2026-03-04 | Phi-4-reasoning-vision-15B | arXiv:2603.03975 v1 + official model/repo artifacts | Ch23 owner; Ch17/20/25/62 handoff | Refine — Ch23 Integrated / Experimental |
| 2026-03-04 | Memex(RL) | arXiv:2603.04257 v1 + later official code artifact | Ch73 owner; Ch29/71/72/74/75 handoff | Refine — Ch73 Integrated / Experimental |
| 2026-03-04 | SWE-CI | arXiv:2603.03823 v1/v4 + official code/config | Ch62 owner; Ch23/63/77 handoff | Refine — Ch62 Integrated / Experimental |
| 2026-03-04 | Nemotron 3 Super | Base checkpoint/model card + 03-11 post-trained checkpoints + 04-14 arXiv formal report | `MODEL-MOE` / Ch21; Ch28/33/45/48/49 handoff | Refine — Experimental |
| 2026-03-04 | V1 parallel generation/self-verification | arXiv:2603.04304 v1; no official code located | Ch20 owner; Ch29/62/76 handoff | Refine — Ch20 Integrated / Experimental |
| 2026-03-04 | T2S-Bench / Structure-of-Thought | arXiv:2603.03790 v1 + official project/data/evaluator artifacts | Ch71 claim check; Ch70/62/72 boundary | Full Review Complete — Weekly Only / No Books Change |
| 2026-03-05 | GPT-5.4 + system card | OpenAI release + full Deployment Safety card | Ch74/68/62; Ch20 boundary | Full Review Complete — Weekly Only / No Change |
| 2026-03-05 | Labor-market impact measurement | Anthropic report + full appendix + correction | Ch62 owner; Ch63/64 handoff | Full Review Complete — No Change / Weekly Only |
| 2026-03-05 | Interactive Benchmarks | arXiv:2603.04737 v1/v4 + partial official code artifact | Ch62 owner; Ch74/75/76 handoff | Refine — Ch62 Integrated / Experimental |
| 2026-03-05 | KARL | arXiv:2603.05218 v1 + Databricks-hosted paper | Ch72 owner; Ch29/62/73/75/77 handoff | Refine — Ch72 Integrated / Experimental |
| 2026-03-05 | CRISP / On-Policy Self-Distillation for Reasoning Compression | arXiv:2603.05433 v1/v7 + official code/checkpoints | Ch25 owner; Ch20/29/31/62 handoff | Refine — Ch25 Integrated / Experimental |
| 2026-03-05 | MASQuant | arXiv:2603.04800 v1 + official code | Ch45 owner; Ch31/23 handoff | Refine — Ch45 Integrated / Experimental |
| 2026-03-05 | IF-RewardBench | arXiv:2603.04738 v1 + official data/inference/metrics code | Ch62 owner; Ch28/29 handoff | Refine — Ch62 Integrated / Experimental |
| 2026-03-05 | Reasoning Models Struggle to Control their CoT | arXiv:2603.05706 v1 + official code/research note | Ch68 owner; Ch5/62/69 handoff | Refine — Ch68 Integrated / Experimental |
| 2026-03-06 | WAXAL speech resource | Google Research + arXiv v1/v3 + dataset card v2.0.0 | Ch23 owner; Ch11/62 handoff | Refine — Ch23 Integrated |
| 2026-03-06 | FlashPrefill | arXiv:2603.06199 v1 + official code | Ch39 owner; Ch14/38/40/45/46 boundary | Refine — Ch39 Integrated / Experimental |

`Recovered Candidate Census` 只证明候选身份、primary URL、v1 date 与初始知识树位置已经核对；它不证明
摘要机制、性能数字或 Books 决策。Qwen3-Coder-Next（v1 2026-02-28）与 SkillNet（v1 2026-02-26）
归回 W09，不计入上述 23 项。

### W11 Spillback Intake Ledger

| Event Date | Candidate | Primary Source | Initial Scope Decision | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-02 | Multi-Head Low-Rank Attention | arXiv:2603.02188 v1 + official code | `MODEL-MULTI-HEAD-ATTENTION` / Ch15; Ch37/45 handoff | Refine — Experimental |
| 2026-03-04 | Believe Your Model / DistriVoting | arXiv:2603.03872 v1 + official code | `MODEL-SAMPLING` / Ch20; Ch66 handoff | Refine — Experimental |
| 2026-03-05 | Progressive Residual Warmup | arXiv:2603.05369 v1 | `TRAIN-PRETRAINING` / Ch28; Ch17/35 handoff | Refine — Experimental |
| 2026-03-05 | BandPO | arXiv:2603.04918 v1 + official code | `TRAIN-GRPO` / Ch33; Ch32/66 handoff | Refine — Experimental |
| 2026-03-05 | Sparse-BitNet | arXiv:2603.05168 v1 + official code | Ch28/49/54 boundary | Weekly Only — Disputed artifact order |
| 2026-03-05 | ATLAS / Scaling Agentic Capabilities | arXiv:2603.06713 v1 + Microsoft Research record | `AGENT-WORKFLOW` / Ch81; Ch33/66/75/78/84 handoff | Refine — Experimental |
| 2026-03-05 | Building AI Coding Agents for Terminal | arXiv:2603.05344 v1/v3 + official code | Ch78/81/84 existing coverage | No Change — Engineering report |
| 2026-03-07 | AutoResearch-RL | arXiv:2603.07300 v1; v2 admin-withdrawn | Ch77 claim check; Ch29/62/75 boundary | Full Review Complete — Withdrawn / Disputed / Weekly Only |
| 2026-03-07 | Hindsight Credit Assignment | arXiv:2603.08754 v1 | `TRAIN-GRPO` / Ch33; Ch66/77 handoff | Refine — Experimental |
| 2026-03-08 | Scaling Data Difficulty | arXiv:2603.07779 v1 | `TRAIN-DATA` / Ch27 existing coverage | No Change — Already Covered |
| 2026-03-08 | MicroCoder-GRPO / Breaking Training Bottlenecks | arXiv:2603.07777 v1 | `TRAIN-GRPO` / Ch33; Ch27/28/66 handoff | Refine — Experimental |

上述 11 项按 primary first-public date 归 W10，而不是按它们被 W11 推荐流发现的日期归周。十一项均已完成
阅读全文、实验合同、限制与目标章节核验；无公开 artifact 或 source 被撤回时，已明确降低 Source Reliability
并限制 disposition，而没有用 abstract、搜索片段或后续引用补足证据。

### W12 Spillback Intake Ledger

| Event Date | Candidate | Primary Source | Initial Scope Decision | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-07 | Recursive Language Models Meet Uncertainty / SRLM | arXiv:2603.15653 v1 + Apple Research later publication record | `MODEL-LONG-CONTEXT` / Ch22; Ch66/76/80 handoff | Refine — Experimental |

SRLM 在 W12 curation 中被发现，但唯一 arXiv v1 首发于 2026-03-07，故按 first-public date 回拨 W10。Apple
Research 的 2026-07 publication record 只用于作者与 publication-family 核验，不改写历史事件日期。

## Full Source Review

FlashPrefill、CoVe、Memex(RL)、SWE-CI、KARL、CoT-Control、SageBwd、MemSifter、V1、Interactive
Benchmarks、RubricBench、IF-RewardBench、DynaMoE、HACRL/HACPO、MUSE、MOOSE-Star、Phi-4-
reasoning-vision-15B、T2S-Bench、CRISP/OPSDC、MASQuant，以及旧报告保留的 GPT-5.4、labor-market
measurement 与 WAXAL，均已按当前 schema 完成 Full Source Review。新增 spillback 中的 MLRA、DistriVoting、
ProRes、BandPO、Sparse-BitNet、ATLAS、Terminal Coding Agents、AutoResearch-RL、HCAPO、Scaling Data
Difficulty 与 MicroCoder-GRPO 也已完成全文核验；Nemotron 3 Super 随后按 03-04 首发回拨并完成审计；
SRLM 最后按 03-07 首发回拨，完成 31 页全文、实验与章节邻接复核。当前为 36/36 scored reviews，0 pending。
这只关闭已记录候选的 Evidence queue；更广的 W10 Discovery Gate 与全历史 Books Gate 仍保持打开，不把
`Books Candidate` 自动等同于修改正文。

### FlashPrefill

- **Candidate / Week / Score:** FlashPrefill / 2026-W10 / 28/30；
  `Source Family ID: flashprefill-training-free-sparse-prefill`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-06）、完整 HTML、Appendix A/B、作者
  repository、Triton kernels 与 vLLM patch。当前只有 v1，无后续 arXiv revision。
- **Full-read Coverage:** Verified；已检查 Abstract、Introduction、Related Work、Method 3.1～3.5、公式
  1～4、Experiments、baselines、density/TTFT、ablation、Conclusion、两个 Appendix、官方 README、
  native/varlen operator 与 vLLM integration path。
- **Original Problem / Why Previous Design Was Reasonable:** dense FlashAttention 精确但 Prefill 的
  attention work 随 context 二次增长；MInference/FlexPrefill/XAttention 先估计 salient patterns 再执行
  sparse attention，是合理的 training-free 分支，但 coarse discovery、Top-k sorting 或 Top-p cumulative
  sum 可能在短中 context 抵消稀疏收益，固定预算还会保留 long-tail 低贡献 blocks。
- **Changed Constraint / Principle:** context 扩到 4K～256K 后，不仅 sparse kernel 的 retained density，
  发现 pattern 与构造 indices 的 control overhead 也进入 TTFT critical path。优化对象因此从“少算多少
  attention”扩展为“用多大代价决定哪些 attention 可以不算”。
- **Mechanism:** 先将每个 key block 平均为 proxy vector；每个 query tile 与 pooled keys 计算 block
  energy，以局部 max + online exponential reduction 得到稳定分数，再做跨 key blocks 的全局归一化。
  每行以 `alpha * row_max` 作为动态阈值，并与 causal mask、attention sinks、local window 合并；最后
  把 active block coordinates 压缩为 index list，由 index-driven Triton kernel 直接跳到物理 block，
  避免 masked-block loop 的逻辑 skip 开销。
- **State Ownership / Control and Data Flow:** attention layer 拥有当前 invocation 的 block score map、
  threshold factor、sink/window policy、active counts 与 compact indices；它们是从 Q/K 派生的 ephemeral
  execution state，不是跨请求持久 KV identity。数据流为 `Q/K -> pooled K + block energy -> normalized
  score -> threshold/masks -> compact indices -> sparse QK/softmax/V`。错误 index 会静默丢失 attention
  evidence，而不一定触发 runtime failure。
- **Implementation Details / Artifact Boundary:** 公开 README 固定 `torch 2.9.0`、`triton 3.3.0`、
  `transformers 4.56.1`、可选 `flash_attn 2.8.3` 与 vLLM 0.10/0.12；示例使用 BF16、TP=4、
  `max_model_len=32K`，并关闭 chunked prefill 与 prefix caching。效率说明明确为 native forward、
  `batch_size == 1`。kernel 注释限定 `key_len == query_len`，因此 prefix-hit、chunked/ragged `q_len < k_len`
  以及 production mixed batch 不能从现有结果直接外推。
- **Paper/Code Consistency Check:** 论文正确地消除了按 score 做 Top-k/Top-p global ranking/cumulative
  selection；但 Appendix Algorithm 2 和公开 `deal_output_score()` 仍对填充为 sentinel 的 block indices
  执行 stable/compact sort。故准确表述是“避免 attention-score ranking”，不是“端到端完全无 sort”。
- **Evaluation Contract:** Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct、Qwen3-30B-A3B-Instruct-2507；
  VLM 为 Qwen2.5-VL-7B 与 Qwen3-VL-30B-A3B；RULER、InfiniteBench、VideoMME；NVIDIA H20；
  Full Attention baseline 为 FlashAttention 2.8.3，另比 MInference、FlexPrefill、XAttention、FlashMoBA。
  block size 128，sink 256 tokens，local window 512 tokens；`alpha` 按模型在 4K 校准到约 70% density，
  并随长度自然降低 density。paper 未披露 serving arrival process、并发、P95/P99、功耗、完整 precision
  contract 或跨 GPU topology。
- **Evidence Proves:** 在上述作者 contract 下，block approximation 比两种 discovery baseline 提供更好的
  RULER/latency trade-off；max-threshold 在 32K～128K 比固定 Top-k/Top-p 获得长度相关 density；公开表中
  Qwen3 128K end-to-end TTFT 为 53,752ms -> 10,702ms（5.02x）。operator headline 的 27.78x 与
  end-to-end headline 的最大 7.22x 都只能绑定作者实现、模型、H20 与长度。
- **What It Does Not Prove / Limitations:** 不证明平均 pooled keys 在任意 domain/head 都保持 rank；不证明
  4K 校准的 `alpha` 能跨 model/revision/workload；不覆盖 concurrent serving、chunked prefill、prefix hit、
  PD 分离、tail SLO、fault recovery 或独立复现。论文没有独立 Limitations/Threats section，结果也未给
  seeds、confidence intervals 或 accuracy non-inferiority margin。
- **Trade-offs / New Failure Modes:** 更低 density 换来 approximation error、model-specific calibration、
  score/index workspace 与额外 control kernels；阈值过高会漏掉非局部重要 blocks，过低则退回 dense-like
  cost。sink/window 是 safety floor 也是固定开销。index compaction、kernel/version compatibility 与
  unsupported `q_len != k_len` 会形成新的 correctness/fallback surface。
- **Where Previous Designs Still Apply:** 短 context、严格 exactness、分布漂移大、模型 attention pattern
  不稳定或已有 chunked/prefix-cache 路径时，dense FlashAttention 仍可能更简单可靠；Top-k/Top-p 在需要
  固定 compute budget、跨请求可预测 resource envelope 时仍有优势；trained sparse architectures 则把
  sparsity 纳入模型 contract，代价是训练与可移植性。
- **Evolution Relationship:** `Direct Evolution`：exact dense attention -> training-free pattern discovery +
  fixed/top-p selection -> fused block approximation + row-relative threshold + physical index jump。它没有
  替代 chunked Prefill、prefix cache 或 PD disaggregation，而是与这些 scheduling/state mechanisms 正交，
  组合后必须重新验证 `q_len/k_len`、workspace、fairness 与 TTFT。
- **ROADMAP / Chapters Read:** 主 owner 从初筛 Ch41 修正为 Ch39 Prefill；已完整阅读 Ch38～40。
  Ch41 管理 persistent KV state，不应承载 Prefill attention sparsity；Ch45/46 只保留 kernel/runtime
  integration handoff。
- **Integration Decision:** `Refine — Existing Argument / Ch39 Integrated / Experimental`。Ch39 已补入
  discovery/selection/index-build cost、ephemeral index ownership、approximation failure、dense fallback 与
  `q_len/k_len` workload boundary。Ch38/40/45/46 不重复写入；正文未复制版本或峰值倍率。
- **Open Questions:** 如何支持 `q_len < k_len` 的 prefix-hit/chunked Prefill？active-index sort 是否会在
  大 batch/多 head 下成为新瓶颈？`alpha` 能否由 online error/SLO budget 控制而不是离线按 4K density
  校准？在生产 mixed traffic 中，approximation fallback 如何与 request identity、canary 和 rollback 对齐？

### CoVe：Constraint-Guided Verification

- **Candidate / Week / Score:** CoVe / 2026-W10 / 26/30；
  `Source Family ID: cove-constraint-derived-interactive-verification`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-02）、完整 HTML、官方 project page、
  CoVe-4B model card 与 CoVe-12k dataset card；当前 arXiv 只有 v1。论文声称开源代码，但 project page
  只给出 paper、model 与 dataset 链接，本轮未定位到可核验的官方 code repository，因此 implementation
  只按论文与公开 artifact 记录，不能标记为 code verified。
- **Full-read Coverage:** Verified for the paper；已检查 Abstract、Introduction、Related Work、POMDP
  formulation、Method 3.1～3.4、数据生成/SFT/RL 流程、Experiments、baselines、data scaling、user-
  simulator ablation、Limitations、Conclusion 与全部表格。arXiv HTML 在 Conclusion 后直接进入
  References，没有独立 Appendix。
- **Original Problem / Why Previous Design Was Reasonable:** tool-use Agent 必须把不完整、逐步揭示的
  用户意图映射为确定 API effects。人工任务和 verifier 质量高但昂贵；LLM-generated goals/judges 便宜，
  却可能生成 sandbox 中不可执行的任务，或以语言相似度替代最终环境状态。旧路线在开放语义任务中仍
  合理，因为很多 helpfulness、安全与权衡无法完全编译成结构化 predicates。
- **Changed Constraint / Principle:** 当环境本身已有数据库 schema、tool contract 与可观察状态时，
  可以先从 executable state 采样 ground-truth constraints，再把它们模糊化为自然语言，而不是先生成
  文本任务再猜测其可验证条件。长期原则是：`generate task and verifier from the same executable
  specification`，但可靠性上限仍由 specification coverage 决定。
- **Mechanism:** constraint sampler 从 synthetic sandbox database 采样可满足条件 `C`；fuzzification
  将显式标识转换为在该 sandbox 中保持唯一的自然描述 `F`；user simulator 依据隐藏 intent 逐轮揭示
  constraints；policy Agent 通过 tools 改变环境，产生 trajectory `tau`；rule-based verifier
  `V(tau,C)` 检查最终 outcome，并对 redundant actions 扣分。SFT 只保留 score=1 的 trajectories，
  RL 则把同一 verifier score 作为 GRPO reward。
- **State Ownership / Control and Data Flow:** sandbox environment 拥有数据库与可执行状态 `e`；task
  generator 拥有 sampled constraints `C` 与 fuzzified descriptions `F`；user simulator 拥有隐藏意图、
  disclosure 与 termination policy；Agent policy 拥有 tool decisions；trajectory log 保存 action/result；
  verifier 拥有 outcome checklist 与 redundancy rule。数据流为 `sandbox state -> constraints -> fuzzified
  request -> interactive disclosure -> tool trajectory -> final state + redundancy verification -> SFT filter /
  RL reward`。generator 与 verifier 共享 ontology，既带来一致性，也可能共享同一个遗漏。
- **Implementation / Artifact Boundary:** 论文基于 `Qwen3-4B-Instruct-2507`，使用 VeRL 与 SGLang；
  训练运行于两节点、每节点 8 张 80GB GPU，但 GPU 型号 Not Disclosed。SFT 使用 AdamW、learning rate
  `1e-6`、global batch 128；GRPO 使用 learning rate `1e-6`、batch 64、temperature 1.0、每 prompt
  16 rollouts，user/assistant 最大轮数分别 32/40。model card 标注 tensor type F32 与 Hermes tool-call
  format；dataset card 公开约 12K rows、`messages/data_source/tools` 等字段并标注 Apache-2.0。没有官方
  code path 可核验 sampler、fuzzifier、verifier 与 redundancy implementation。
- **Evaluation Contract:** 外部评估为 tau2-bench Airline/Retail，论文关闭 think tool，并报告 pass^1～
  pass^4。synthetic sandbox 内容与 tau2 分离但风格相似；SFT user simulators 包括 Qwen3-235B-A22B 与
  Gemini-3-Pro，teacher 为 Qwen3-235B；RL 因成本只用 Qwen3-235B simulator。公开结果未披露训练
  precision、token-length distribution、steps/epochs、wall-clock/cost、随机 seeds 或 confidence intervals。
- **What the Evidence Proves:** 在作者数据、simulator、tool schema 与 tau2 评估 contract 下，
  CoVe-4B SFT 的平均 pass^1 从 base 的 32.6 提升到 51.2（Airline 43.0，Retail 59.4）；相同 5K
  data budget 下报告 44.7，对比 APIGen 41.7、Simia 39.7。user-simulator ablation 中 Gemini-3-Pro 的
  generation yield 高于 Qwen3-235B，说明 termination/disclosure policy 是数据系统的一部分，而非可互换
  的文本生成器。
- **What It Does Not Prove:** 论文中的 `guaranteed quality`、`absolute correctness` 与
  `hallucination-free` 只能解释为“相对已编码 constraints 和 verifier rules 的确定性”。它不证明
  constraint ontology 完备，不验证所有对话 helpfulness、policy safety、privacy、不可逆副作用、真实
  ambiguity 或未编码的用户意图；也不证明 synthetic sandbox 中的唯一描述在真实生产数据中仍唯一。
  generator 与 verifier 若共享遗漏，可能产生内部自洽但外部错误的数据和 reward。
- **Ablation / Limitations:** SFT 为 51.2，纯 RL 为 40.7，SFT+RL 为 46.9；在当前 simulator 下，
  RL 没有超过 SFT，作者将瓶颈归因于 simulator 能力。论文只覆盖 Airline/Retail 两个 domain；没有
  independent verifier audit、human realism calibration、安全/隐私/irreversibility 分析，也没有公开
  code 供本轮检查同源规则是否存在 shortcut 或 leakage。
- **Trade-offs / New Failure Modes:** constraint-first generation 降低不可执行任务和 judge ambiguity，
  代价是 ontology/schema 建模、equivalence rules、simulator cost 与 domain portability。新 failure modes
  包括漏写 constraint、fuzzification 消歧失败、simulator 过早终止、允许路径集合不完整、冗余操作定义
  错误、shared-ontology blind spot，以及把 verifier gaming 当成用户任务成功。
- **Where Previous Designs Still Apply:** 人工 review 仍适合高风险、开放语义和规范不完备任务；LLM
  judge 仍可覆盖难以结构化的 style/helpfulness，但应与 executable checks 分层；真实 user traces 用于
  校准 ambiguity 与 workflow distribution。CoVe 不是这些路线的替代品，而是可执行子空间的强约束层。
- **Evolution Relationship:** `Layering / Dependency`：LLM-generated dialogue/judge -> blueprint or
  constraint generation -> executable constraint-derived task + outcome verifier -> same verifier reused for
  SFT filtering and RL reward。下一阶段压力从“能否自动生成数据”转为 verifier independence、spec
  completeness、真实用户校准与 reward-channel governance。
- **ROADMAP / Chapters Read:** 主 owner 确认为 Ch23 Data；已完整阅读 Ch22～24。Ch22 只提供模型
  effective utilization 与数据能力边界，Ch24 负责训练 objective；Ch25/29 承接 SFT/RL，Ch62 承接
  evaluation contract，Ch74/77 承接 tool workflow 与 executable artifact，不重复保存数据编译机制。
- **Integration Decision:** `Refine — Existing Argument / Ch23 Integrated / Experimental`。已在 Ch23 将
  synthetic data 从 `generate -> model judge` 扩展为 `executable state -> constraints -> fuzzification ->
  trajectory -> outcome verifier`，并保留 shared-ontology blind spot、independent audit 与 reward-channel
  governance。未复制 CoVe 名称、模型分数或作者的 absolute-correctness 表述；Ch25/29/62/74/77无需重复修改。
- **Open Questions:** 如何用独立 oracle 或 human audit 估计 verifier false-positive/false-negative？
  constraint schema 如何版本化、迁移并关联 dataset rows？同一个 verifier 同时用于筛选与 RL reward 时，
  怎样检测 policy exploitation？安全、隐私与不可逆 side effects 应由谁拥有、何时阻断 trajectory？

### Memex(RL)：Indexed Experience Memory

- **Candidate / Week / Score:** Memex(RL) / 2026-W10 / 26/30；
  `Source Family ID: memex-indexed-experience-memory-rl`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-04）、完整 HTML、Appendix A/B，以及当前
  可访问的 Accenture 官方 code repository。当前 arXiv 只有 v1；HTML title block 出现 2026-07-28，
  但 submission history 明确 v1 为 2026-03-04，归周使用 v1 date。官方 repository 是后续 artifact
  verification，不另算 W10 event；本轮未取得可审计的 repository first-commit date。
- **Full-read Coverage:** Verified；已检查 Abstract、Introduction、Related Work、Definitions 1～3、
  Algorithm 1、memory operations、GRPO reward、segmented trajectory processing、soft compression trigger、
  Propositions 1～2、Evaluation、Conclusion、Appendix A proofs 与 Appendix B conversion gap；并联读官方
  README、memory mixin/types、reward/project structure 与 training configuration。
- **Original Problem / Why Previous Design Was Reasonable:** long-horizon Agent 的 tool outputs 与中间
  evidence 会让 Context 持续增长。保留完整历史最忠实但 Prefill/token cost 与 context capacity 不可扩展；
  truncation/running summary 便宜但丢失细节；semantic retrieval 能找近似内容，却未规定 Agent 应怎样组织
  自己的 experience，也可能被 near-duplicate fragments 干扰。这三条旧路线在短任务、低风险摘要或开放
  query 场景仍合理。
- **Changed Constraint / Principle:** 当未来决策只需要少量历史证据，但无法预先知道是哪一条时，系统
  应分离 compact control state 与 full-fidelity evidence archive。摘要不再承担全部事实，而是保存进度、
  stable references 与 dereference cues；原始 artifacts 作为独立状态保留。真正的新约束是 index identity、
  write/read policy 与延迟 credit assignment，而不只是 storage capacity。
- **Mechanism:** working Context 保存 indexed summary `sigma=(s,I)`，外部 store `D[index]->content`
  保存 tool outputs、traces 与 code snippets。`CompressExperience` 归档 blocks 并把 dynamic Context 重写为
  system/task/indexed summary；`ReadExperience(index)` 精确解引用并把 artifact 重新注入 Context。
  block 可由模型直接 author，也可用 start/mid/end anchors 从当前 conversation 提取。ContextStatus 软提示
  token usage，Agent 自主选择 compression timing。
- **Learning Mechanism:** episode return 为 task reward 减去 context overflow、重复 tool call 与 malformed
  call penalties。每次 compression 改变后续 conditioning prefix，训练因而按 compression boundaries 切分
  trajectory；来自同一 episode 的 segments 共享 terminal reward，再通过 group-relative advantage 与
  PPO-style clipped objective 把延迟收益传回 write/read actions。训练先由 well-formed indexed summaries
  的 SFT demonstrations warm start，再做 RL。
- **State Ownership / Control and Data Flow:** runtime 拥有 system/task anchors、ContextStatus、store 与
  memory-tool execution；policy 拥有 summary、index naming、archive selection、compression timing 与
  dereference decisions；environment tools 拥有原始 observations；训练系统拥有 segment lineage、terminal
  reward 与 policy/reference revisions。数据流为 `trajectory -> summary + archive blocks -> stable indices ->
  Context rewrite -> explicit dereference -> evidence reinjection -> task action`。错误 index、覆盖或未解引用
  会表现为语义失忆，而非必然的 storage error。
- **Official Artifact Check:** 当前公开实现默认用 in-memory database 隔离 parallel Agents；index 只校验
  1～64 位字母/数字/下划线/连字符，同一次 compression 内拒绝重复，但明确允许覆盖已有 index。
  lossless store 记录 content、summary、original chars 与 message count；summary token limit 以 4 chars/token
  近似截断。公开 path 没有 production authorization、tenant scope、immutable version、content digest、
  supersession、delete propagation、durable transaction 或 crash recovery，因此“stable/full-fidelity”是实验
  interface 语义，不是已经验证的生产持久性保证。
- **Evaluation Contract:** backbone 为 Qwen3-30B-A3B-Thinking-2507；modified ALFWorld 隐藏 admissible
  commands 与初始 location IDs，`look` 每 episode 仅允许一次，并把 summary 截到 300 tokens，迫使 Agent
  通过 indexed blocks 保存/恢复 IDs。训练集 3,553 tasks；32K context、8K penalty threshold、batch 32、
  GRPO group 8；rollout 用 INT4，backward 用 QAT forward + BF16 gradients，Adam `5e-6`、weight decay
  0.1、KL 0.001、TIS clip 2.0。论文未披露 GPU 型号/数量、并发、训练时长、成本、seeds 或 confidence
  intervals；当前 README 给出 8 张 NVIDIA GPU、H100 recommended 的复现配置，不能反推论文原始硬件。
- **What the Evidence Proves:** 在上述单一模型和 modified ALFWorld contract 下，作者报告 RL 后 task
  success 24.22% -> 85.61%，peak working Context 16,934.46 -> 9,634.47 tokens；Compress calls 从约
  6.5 降到 3，Read calls 从约 1 升到 6～7。它支持“learned index/dereference policy 能在被迫依赖该
  interface 的环境中改善 success/context trade-off”，不是通用 Agent memory 的效果量。
- **Theory Boundary:** Proposition 1 假设 indexed summary 本身已经 `B`-bounded decision-sufficient，随后
  构造可复现 full-context optimal policy 的 Memex policy；Proposition 2 假设 summary length、dereference
  count 与 block length 均有上界，才推出 bounded working Context。两者说明接口在这些强条件下可能成立，
  不证明 MemexRL 会学到 decision-sufficient indices，也不证明 archive/storage cost 有界。论文 Introduction
  对这一点有明确限定。
- **What It Does Not Prove / Threats:** modified ALFWorld 的 one-look 与 300-token truncation 对 Memex
  interface 具有结构性偏好；论文没有独立 full-context、lossy-summary、semantic-RAG、oracle-index、随机
  index 或不同 Context budget 的完整 baseline/ablation matrix。没有多 domain、真实 tool failures、memory
  growth/index collision、concurrent writers、stale artifacts、authorization、privacy/deletion、crash recovery
  或长期 store latency 证据。Appendix B 的 prompt 内容未被 arXiv HTML 正确转换，只能由 source/PDF 或
  artifact 再核验。
- **Trade-offs / New Failure Modes:** exact dereference 降低 fuzzy retrieval ambiguity，却把正确性转移到
  index authoring、identity 与 availability；summary 变小会提高遗漏/错误引用风险，archive 变大则增加
  storage、GC 与 lookup cost。learned compression timing 更灵活，但 reward shaping 可能诱导过早归档、
  verifier gaming 或为避免重复 penalty 而读取不合适 artifact。覆盖 index、anchor false match、失效链接、
  retrieved-block Context 膨胀和 stale evidence 都是新增 failure modes。
- **Where Previous Designs Still Apply:** 短 trajectory 可保留 full Context；不可恢复细节不重要时 running
  summary 更简单；未知 query 和 corpus discovery 仍需要 semantic/hybrid retrieval；高风险原始证据应由
  immutable artifact store 与平台 policy 管理，而不是允许模型自由覆盖的 key-value map。更稳健的生产
  组合是 summary 负责 control、stable reference 指向 versioned evidence、retrieval 处理未知关联。
- **Evolution Relationship:** `Direct Evolution` within Agent Memory：full history -> lossy running summary ->
  external similarity retrieval -> compact indexed control state + exact archive -> learned write/read/timing policy。
  这条路线没有替代 RAG 或 Workflow state；它把“检索什么”前移到 experience write time，并新增 index
  lifecycle、provenance、supersession、authorization 与 recovery 压力。
- **ROADMAP / Chapters Read:** 主 owner 确认为 Ch73 Memory；已完整阅读 Ch72～74。Ch72 拥有针对未知
  query 的 corpus retrieval，Ch74 拥有 memory tool 的 typed execution contract，Ch71 仅短 handoff working
  Context，Ch29 负责 RL credit assignment，Ch75 负责 task planning。现有 Ch73 已覆盖 summary/source
  lineage 和 derived memory，但没有完整表达“compact control state + versioned exact evidence + explicit
  dereference”这一机制分层。
- **Integration Decision:** `Refine — Existing Argument / Ch73 Integrated / Experimental`。Ch73 已补入
  compact control state、versioned exact evidence archive、stable reference contract、read/write learning
  trade-off 与生产 durability gap；正文未复制 ALFWorld 数字或论文 API。
- **Open Questions:** index 是 immutable content address、mutable alias 还是 versioned pointer？如何对 write/
  read policy 分别评估 precision/recall？archive 的 ACL、retention、delete、supersession 和 crash recovery
  如何与 summary lineage 原子对齐？怎样设计不偏向特定 memory API 的 benchmark 与 oracle ablation？

### SWE-CI：从快照答题到演进轨迹评估

- **Candidate / Week / Score:** SWE-CI / 2026-W10 / 26/30；
  `Source Family ID: swe-ci-evolution-conditioned-software-evaluation`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-04）与 v4（2026-04-01）、两版完整 HTML、
  当前官方 repository、README、`config.toml` 与 `src/swe_ci` 代码树。归周依据 v1；v4 与当前 artifact
  只用于 revision correction 和机制核验，不另算 W10 event。Hugging Face dataset 本轮返回 401，未绕过
  权限，因此 dataset rows、license/card revision 与实际 image digests 标记 `Unverified`。
- **Revision History / Full-read Coverage:** v1 2026-03-04、v2 03-17、v3 03-18、v4 04-01。已检查两版
  Abstract、Introduction、Related Work、benchmark construction、Algorithm/metrics、data pipeline、agents、
  experiments、additional analyses、limitations、Conclusion、Appendix 与 artifact conversion gap；并联读当前
  README、运行配置和 source layout。v4 Appendix C 的 prompt 未被 arXiv HTML 正确转换，只能以官方
  artifact 为准，不能声称已从 HTML 验证 prompt 全文。
- **Original Problem / Why Previous Design Was Reasonable:** SWE-bench 式 snapshot benchmark 固定一个
  issue 和 repository state，能低成本、可重复地测量局部 patch 是否通过 tests；对 release regression 与
  isolated bug fix 仍然合理。但长期软件工程包含一连串相互依赖的修改，早期 architecture decision 会约束
  后续 change cost，最终 patch 的 pass/fail 会丢失中间回归、恢复速度和 accumulated technical debt。
- **Changed Constraint / Principle:** 评估对象从静态 artifact 变成 `state_0 -> action_1 -> state_1 -> ...`
  的演进轨迹。正确性不仅是最终测试数，还包括每轮相对目标的推进、回退与恢复；同时 evaluator 自己拥有的
  target、tests、iteration budget 和 temporal weighting 也成为 measurement state，必须版本化。
- **Mechanism / Control Flow:** 每个 task 保存 base commit `c0`、target commit `c*`、target tests 与固定
  environment。每轮先在当前 code 上运行 target tests，Architect 根据与 `c*` 的 test gap 生成至多五条
  requirements，Programmer 再修改 repository；最多 20 轮。归一化变化 `a(c)` 以 base/target passed-test
  差为尺度，EvoScore 用 `gamma` 对后续轮次加权。数据流为 `current repo + oracle target tests -> failing
  evidence -> Architect requirements -> Programmer patch -> pytest result -> trajectory score -> next state`。
- **State Ownership:** evaluator/harness 拥有 `c0/c*`、target tests、Docker image、dependency repair、retry、
  timeout、iteration limit 与 `gamma`；Architect 拥有 requirements synthesis；Programmer 拥有 code changes；
  pytest/report parser 只拥有可观测 test verdict。最终分数因此是 model、双 Agent 分工、test oracle、container、
  budget、provider API 与 harness revision 的联合结果，不是单一 base model 的固有能力。
- **Dataset / Implementation Contract:** 作者从 68 个 Python repositories 构造 100 tasks，平均跨约 233 天、
  71 commits、500+ source-line changes；pipeline 从 4,923 candidate pairs 经时间跨度、test gap、environment
  execution 与 top-100 selection 收缩。论文使用同一 base model 充当 Architect 和 Programmer、20 iterations、
  `pytest` JSON report 和每次 test 3,600 秒上限；总实验超过 100 亿 tokens。seeds、confidence intervals、
  GPU/CPU exact execution inventory 与 per-model concurrency 未披露。
- **Artifact Revision Boundary:** v4 论文使用 iFlow CLI，而当前 repository 已允许 iFlow/OpenCode，默认
  `agent_name="opencode"`；当前 README 把默认指标表述为 `ANC (gamma=1)`，论文则保留可变 `gamma` 的
  EvoScore；当前配置还暴露 16 workers、container memory/I/O limits、`max_epoch=20`、test timeout 与 retry。
  README 的 clone URL 仍指向旧 organization。由此可见 benchmark 名称不足以唯一标识评估，必须记录
  paper revision、code commit、agent adapter、container/data digest、metric parameter 与 retry policy。
- **What the Evidence Proves:** 在固定目标版本、oracle target tests、作者构造的 100 个 Python tasks 和
  20-round dual-agent harness 下，作者观察到模型在多轮演进中的累计推进与最终 snapshot ranking 不完全一致；
  solved cases 上，20 个模型的 Maintainability Index 均低于 human target，15/20 的 Pylint score 更高。
  这些结果支持“trajectory-aware evaluation 能暴露 final pass-rate 看不到的演进差异”，但只适用于该
  benchmark contract。
- **Revision Correction / What It Does Not Prove:** v1 把 MiniMax/DeepSeek/GPT 描述为偏长期，而把
  Kimi/GLM 描述为偏短期；v4 对这些家族的方向基本反转，并把 Qwen 纳入长期组。这说明排序对 revision、
  task/model set 与 `gamma` 很敏感，不能上升为 provider training strategy。测试来自已知 target commit，
  Architect 持续看到 oracle test gap，因此它测的是固定隐藏目标的迭代重建，不是未知用户需求、branch/
  merge、团队协作、线上反馈或自然 dependency drift。静态 Pylint/MI 也不能证明真实可维护性因果。
- **Limitations / Threats:** target tests 可能不完整或泄漏实现形状；模型可能对 tests 而非需求过拟合；
  Architect 是额外瓶颈且同模双角色造成 correlated error；自动修复 environment 与筛选 top tasks 带来
  survivorship/selection bias。任务仅覆盖热门、可执行、许可合适的 Python repositories，没有 security、
  performance、human review、concurrent editing、production SLO、rollback cost 或真实 issue ambiguity。
  单次昂贵运行和缺失不确定性使小排名差异不可解释为稳定能力差异。
- **Trade-offs / New Failure Modes:** 多轮 replay 更接近 stateful engineering，却显著提高 tokens、环境
  构建、flakiness、test leakage 和复现实验成本；temporal score 保存轨迹信息，却把“后期更重要”编码为
  `gamma` 的政策选择。固定 oracle 提供确定性，同时把真实 specification uncertainty 移出 benchmark。
  snapshot benchmark 仍适合局部 regression；evolution benchmark 适合测累积影响，但必须把两者分层，
  不能把前者宣布过时。
- **Evolution Relationship:** `Direct Evolution` within Evaluation：single-issue snapshot -> executable
  final-artifact verifier -> multi-step repository replay -> trajectory/temporal scoring -> future benchmark with
  requirement drift、human review、branching、production feedback and cost/risk gates。新阶段增加的是 state
  lineage 与 evaluator ownership，不是单纯延长 Context 或增加 Agent 次数。
- **ROADMAP / Chapters Read:** 主 owner 确认为 Ch62 Evaluation System；已完整阅读 Ch61～63。Ch62 已有
  model/harness/environment/budget identity、executable verifier 与 uncertainty 原则，但尚未系统表达“评估
  state sequence、早期决策累积与 metric temporal policy”。Ch63 只承接在线 telemetry，Ch23 承接 dataset/
  contamination，Ch77 承接实际 workflow state machine，避免重复保存 benchmark 细节。
- **Integration Decision:** `Refine — Existing Argument / Ch62 Integrated / Experimental`。Ch62 已补入
  snapshot、candidate coverage、feedback-conditioned trajectory 与 evolving state sequence 的分层，并记录
  evaluator-owned temporal policy、oracle-target 与 harness revision 边界。正文未写模型排名、厂商偏好、
  100-task 分数或未经验证的通用 maintainability 结论。
- **Open Questions:** 如何在没有 future target tests 泄漏的情况下生成可验证 requirement drift？怎样把
  human review、branch/merge、dependency/security/performance regression 与 rollback cost 纳入轨迹？
  `gamma` 应由业务风险/时间价值显式选择，还是报告完整 Pareto/frontier？如何估计 flaky tests、Architect
  errors、harness retries 与模型 variance 对 EvoScore 的贡献？

### KARL：检索、压缩与停止作为联合策略

- **Candidate / Week / Score:** KARL / 2026-W10 / 26/30；
  `Source Family ID: karl-grounded-retrieval-policy-and-offpolicy-rl`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-05）、77 页完整 HTML、Databricks 官方托管
  PDF。当前只有 v1。论文明确将 `aroll`、PMBench 与部分 production corpus 描述为内部资产；本轮没有
  定位到 KARL/OAPL/aroll 的公开 code、model weights、training config 或完整 dataset artifact，因此实现
  复现状态为 `Mechanism Described / Artifact Not Public`，不能拿无关同名 KARL repository 补证。
- **Full-read Coverage:** Verified；已检查 metadata、Introduction、Related Work、KARLBench 六类任务、
  corpus construction、nugget evaluation、Agent harness、agentic synthesis、OAPL 公式与 multi-step extension、
  multi-task RL、Parallel Thinking/VGS、Agent infrastructure、全部 training/evaluation/ablation/behavior sections、
  Conclusion，以及 cost/latency、dataset、prompts、data flow、failure cases、compression 与 evaluation UI
  Appendices。训练硬件、optimizer、learning rate、precision、global batch、总训练时长/成本均 `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable:** 一次 top-k retrieval + generation 在单跳 QA、
  低 token budget 和稳定 corpus 中便宜且可重复；单任务 SFT/RL 也能针对明确 search pattern 优化。但企业
  grounded reasoning 同时包含深搜、广搜、跨文档综合、表格计算和 exhaustive recall，长 trajectory 还会
  被重复 retrieval 与 Context accumulation 主导。旧方案不是错误，而是在任务多样性和 horizon 扩大后暴露
  policy、Context 与 evaluator 的耦合边界。
- **Changed Constraint / Principle:** Agentic Retrieval 的决策变量不再只有 query：`what to search`、
  `what evidence to retain/compress`、`whether to verify`、`when to stop/abstain` 共同决定 outcome 与成本。
  这些动作共享 terminal reward 时，应以同一 environment/harness identity 贯穿 synthesis、training、evaluation
  与 serving，否则观察到的 improvement 可能只是 tool、compression 或 budget distribution shift。
- **Harness / Retrieval Mechanism:** Agent 只使用 vector search；不同 corpus 按平均 chunk length 选择 `k`
  以近似固定 retrieved-token budget。历史超过阈值后，由同一 Agent 将 trajectory 压缩为 summary，再继续
  search。训练把 compression action 一并优化。内部 harness 让 Environment 拥有 interaction loop、tool
  execution、reward 与 lifecycle plugins；Agent 拥有逐步 generation；Strategy 拥有并发 rollout/aggregation。
  offline index 缓存在 shared storage，每个 worker 加载 in-process columnar vector DB，作者报告单 host 超过
  500 queries/s；这是其离线生成 contract，不是通用 vector-serving SLO。
- **Synthetic Data Flow:** Question-Answer Agent 先在 corpus 中探索并合成 grounded QA；dedup Agent 用
  embedding shortlist + LLM judge 去除 validation near-duplicates；多个 Solver rollouts 估计难度，all-correct/
  all-wrong 被过滤；Quality Filter 再检查歧义或错误 reference。下一 iteration 用更新后的 Agent 重新合成。
  BrowseComp-Plus 第一轮从 13,882 QA 收缩到 1,218 个八轨迹 prompts（8.8% yield），表明 verifier/filter
  本身是主要数据生产状态，而非无关清洗。
- **Training Mechanism / Mathematics:** OAPL 从 KL-regularized optimum
  `pi*(y|x) ∝ pi_ref(y|x) exp(r/beta)` 推出 log-ratio 对 optimal advantage 的 least-squares regression；
  rollouts 由 lagged reference/inference policy 批量产生，可复用于多个 update 与 hyperparameter runs。
  实现以 `beta1` 控制 log-sum-exp value estimate smoothness、`beta2` 控制 KL strength。长 rollout 在
  compression boundary 分段，tool tokens 被 mask；每个 segment 与 compression summary 都继承整个 episode
  reward，value estimate 仍取 initial prompt。这降低长序列训练显存，却保留粗粒度 delayed-credit bias。
- **Iterative / Multi-task / Test-time Evolution:** 更新 policy 后重新生成下一批数据，作者最多做三轮；两种
  training tasks 按 token roughly balance 后合并 losses。Serving 侧一条分支并行生成 `N` 个完整 rollouts，
  再由同模、可继续用 tool 的 aggregator 综合；另一条用 4B value model 对每个 assistant step 的两个候选
  排序，并行多棵 BFS 后 voting/Best-of-N。前者通用但增加 Context/compute，后者依赖 task-specific reward
  与 value calibration；它们都不是免费提升。
- **State Ownership / Control and Data Flow:** corpus owner 持有 source/chunk/ACL/index revision；retrieval
  environment 持有 embedding、`k`、tool outputs 与 step budget；compression plugin 持有 threshold/summary
  transition；policy 持有 query、evidence synthesis 与 stopping decision；training system 持有 rollout policy、
  reference、segment lineage、reward 与 iteration；evaluator 持有 nuggets/judges/subsets；serving Strategy 持有
  parallel budget 与 aggregation。完整流为 `corpus -> synthetic task/reference -> solver trajectories -> filter/
  reward -> lagged-policy update -> new policy -> retrieval/compress/stop trajectory -> nugget verdict`。
- **Evaluation Contract:** suite 包含 830/230-subset BrowseComp-Plus、65 TREC-Biogen、150 FinanceBench、
  1,000 QAMPARI、203 FreshStack 与 57-question proprietary PMBench；corpus chunking、embedding 与 `k` 各异，
  但 tool 限制为 vector search。BrowseComp-Plus 只索引文档前 512 tokens，覆盖作者所称 86.5% gold evidence，
  天然形成 retrieval ceiling；作者也观察到 gold document annotations 不完备。PMBench/corpus 不公开，外部
  无法审计 privacy、sampling、nuggets 或 judge errors。
- **Cost / Latency Boundary:** open models 的 latency run 使用 8×H200、vLLM、TP=8、同一 index、
  concurrency=1；每 benchmark 取少量 prompts、多 trajectories 和三 splits，并以 first actionable answer token
  为主指标。闭源模型运行在厂商 infrastructure；配置在 reasoning effort 与是否 compression 中选择最佳者，
  cost 又来自第三方 token prices。因此作者 Pareto frontier 是当时该 harness/config/pricing 下的产品比较，
  不能写成模型或架构的普遍成本/速度结论。
- **What the Evidence Proves:** 在 GLM-4.5-Air、作者生成数据、两个 training tasks、同一 vector-search harness
  与六-task suite 下，multi-task OAPL policy 相比 base/single-task variants 提高若干 held-out task 的作者
  metric；compression removal、search/compressor cross-swap、retriever swap、search horizon 与 retrieval-count
  ablations 支持“检索策略与压缩策略都参与结果”。作者还直接展示 shorter trajectories 既包含减少 answer 后
  冗余搜索，也包含 numerical reasoning 困难时 premature give-up，说明 efficiency 不能由 step count 单独定义。
- **What It Does Not Prove / Internal Inconsistency:** 所谓 OOD 仍共享 closed-corpus、vector-search tool、
  nugget evaluator 与相关任务族，不能外推任意 enterprise workflow。`max@k` 在有限 sample budget 上抬升支持
  sample support 变化，不足以哲学性证明“创造全新能力”。正文称 TREC-Biogen 使用 Quality Filter，Appendix
  D.3 却写 `No Quality Filter is applied for TREC-Biogen`；该 pipeline 状态存在未解释矛盾。没有 public code/
  weights、training hyperparameters、seeds/多次训练方差、独立 reproduction 或 PMBench audit。
- **Limitations / Threats:** synthesis、dedup、quality filter、nugget judge 与 training reward 由相近模型族和
  同一 ontology 构成，可能共享 blind spots；all-wrong filtering 丢弃 frontier/错误-reference 混合组，all-correct
  filtering 丢弃 retention evidence。segment 继承 terminal reward 会把成功错误归因到每次 compression；
  automatic summary 可能丢 provenance。single-tool design 隔离 retrieval，却未覆盖 structured query、code、
  ACL、freshness、live update、prompt injection 或 side effects。behavior taxonomy 只在 30 条人工样本校准，
  约 75% agreement，不能当稳定心理解释。
- **Trade-offs / New Failure Modes:** off-policy batch reuse 降低 online rollout coupling，却增加 policy lag、
  stale data 与 iteration boundary；同一 harness 降低 train/serve shift，却可能让 policy 过拟合 compression、
  tool schema 和 step budget。learned stopping 减少冗余验证，也会把“难以推理”误学成“应放弃”；parallel
  thinking 增加 coverage，也增加线性 rollout cost、aggregation Context 和 correlated error。static retrieval、
  external compressor、single-task expert 和 snapshot RAG 在短任务、严格证据要求或成本敏感场景仍合理。
- **Evolution Relationship:** `Direct Evolution` within Agentic Retrieval：single-shot top-k -> iterative query/
  evidence accumulation -> bounded Context compression -> outcome-trained query/compress/stop policy -> multi-task
  retrieval policy -> parallel/value-guided test-time search。另有 `Layering / Dependency`：Ch29 解释 lagged
  off-policy/credit mechanics，Ch62 约束 benchmark/judge identity，Ch77 拥有 harness/runtime state。
- **ROADMAP / Chapters Read:** 主 owner 确认为 Ch72 RAG；已完整阅读 Ch71～73，并联读 Ch74、Ch75、Ch77
  与 Ch28～30 的相关训练边界。Ch72 已有 iterative retrieval、sufficiency 与 evidence pipeline，但尚未完整
  表达 query/compression/stopping 的联合 policy 和“shorter is ambiguous”；Ch29 已覆盖 rollout version、policy
  lag 与 terminal reward，但不应把 OAPL 单篇公式改写成 GRPO 定义；Ch77 已有 deterministic spine，适合短
  handoff train/eval/serve harness identity。
- **Integration Decision:** `Refine — Existing Argument / Ch72 Integrated / Experimental`。Ch72 已补入
  query/compression/verify/stop joint policy、shorter-trajectory ambiguity、credit boundary 与 train/eval/serve
  harness identity。Ch29/62/77 不重复写入；正文未保留厂商排名、KARLBench 总分、QPS、价格或 OAPL
  优于 GRPO 的泛化结论。
- **Open Questions:** 如何为 search、compression 与 stop 分别做 counterfactual credit，而不把 terminal
  reward 复制到所有 segments？怎样测量“少搜”是去除冗余还是 premature failure？train/eval/serve harness
  必须共享哪些 identity，哪些差异可以显式建模？如何用独立 judge/source audit 估计合成 reference 与 nugget
  的共同盲区，并在 live ACL/freshness/structured tools 下验证迁移？

### CoT-Control：可控性代理不等于可监控性证明

- **Candidate / Week / Score:** Reasoning Models Struggle to Control their Chains of Thought / 2026-W10 /
  26/30；`Source Family ID: cot-control-monitorability-proxy`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-05，当前仅一个版本）、完整 HTML、官方
  CoTControl repository、QA/Agent harness 与 grader，以及 OpenAI 官方研究解读。官方 Blog 的“and that is
  good”属于作者机构的安全解释，不是论文之外的独立实验结果。
- **Full-read Coverage:** Verified；已检查 metadata、Introduction、Related Work、evaluation definition、
  三类九项 proxy、data generation、metrics/baselines、13 个模型结果、monitor-awareness、自动 prompt red-team、
  repeated attempts、difficulty/effort/length/domain/RL 分析、Discussion、Limitations、Appendix B～I、model/prompt
  details、regression diagnostics、reproducibility、failure examples，以及官方 QA/Agent 代码和 grader。
- **Original Problem / Why Previous Design Was Reasonable:** output-only safety monitor 看不到产生 action 的中间
  reasoning；显式 CoT 若较难被模型主动改写，可能为监督提供额外 signal。过去直接比较 output compliance 或
  inspection examples 成本低且容易复现，但它们不能区分“模型会不会按要求改变 reasoning channel”与“模型在
  真实 misaligned goal 下能否隐藏决定性推理”。
- **Changed Constraint / Principle:** 更强 Agent 产生更长 trajectory，并可多次尝试、读取反馈或感知自己被
  monitor。安全论证因此不能只问单次 CoT 是否可读，而要分离 `channel controllability`、`surface
  monitorability`、`faithfulness to latent computation` 与 `action/outcome verification`。低可控性至多削弱一条
  主动 obfuscation 路径，不自动证明 CoT faithful、complete 或足以阻止危险 action。
- **Mechanism / Proxy Construction:** 1,214 个 QA questions 与 350 个 Agent tasks 分别乘九种 constraints，
  形成 14,076 instances；proxy 覆盖 information suppression、information addition 与 stylistic transformation。
  keyword 来自 8 models × 3 baseline traces，再由 GPT-5 提候选并选择所有 traces 都出现的高频词；多数 grader
  用 exact programmatic rule，`ignore question` 由 GPT-5-mini 三次判定且仅三次都失败才记失败，人工核验只覆盖
  120 个随机样本。
- **State Ownership / Control and Data Flow:** dataset builder 持有 source questions、constraint generation、
  keyword/synonym 与 data weighting；model adapter 持有 provider-specific reasoning/output channel parsing、prompt
  template 与 token budget；grader 持有 exact rule、threshold、judge prompt 与 retry aggregation；analysis 持有
  macro weighting、regression specification 和 pass@k。完整流为 `task -> constraint -> provider-specific
  reasoning/output -> proxy grader -> per-instance binary verdict -> macro/regression/pass@k`。这些 identity 任一改变，
  “controllability”都可能改变。
- **Evaluation Contract:** 主评估横跨 GPQA、MMLU-Pro、HLE、BFCL 与 SWE-Bench Verified，默认比较九种
  constraints；论文对比例作等权 macro aggregation。大部分 run 使用 greedy decoding。RL section 改用 1,066
  QA subset、15K max generation、temperature 0.6、top-p 0.95 和更容易的 constraints；Mistral/Magistral 又只有
  500-token cap。Olmo base/RL-Zero 无独立 reasoning channel，作者把生成文本最后 10% 当答案并删除；不同
  family 的 CoT 因而不是同一个 measurement object。
- **Grader / Metric Boundary:** QA grader 默认要求 100% 字符大小写、句首/句尾或插词 compliance；一个违规
  字符即可失败，长度增长会机械提高至少一次违规的机会。word suppression 只统计显式 keyword/synonym，无法
  识别语义等价 concealment；句子、空格和标点依赖 heuristic parsing。grader dispatcher 会拒绝空 reasoning，
  但部分底层 rule 对“没有可检查字母/内容”的文本返回通过，说明 aggregation 必须保存 parser path，而不能只
  留最终 binary score。
- **What the Evidence Proves:** 在该 prompt-based suite、provider channel、constraint taxonomy 与 grader 下，
  多数被测模型改变 CoT 的成功率显著低于改变 output 的成功率；seen-type prompt search 对 held-out constraint
  transfer 弱，多次独立尝试与逐次 AI feedback 会提高至少一次通过的概率。结果支持“prompt-level CoT
  manipulation 并非随 output instruction following 自动获得，且机会预算是 threat model 的一部分”。
- **What It Does Not Prove:** 论文没有观测自发 misalignment、真实 monitor evasion 或 training-based attack；
  它不证明 raw CoT faithful、包含全部内部 computation、对 monitor 可解释，也不证明任何模型在生产中安全。
  human agreement 的 120 样本不足以验证全部九类、五套数据与 provider parsers。低 compliance 还混合任务难度、
  generation length、prompt following、formatting 与 channel extraction，不能归因单一内部机制。
- **RL / Correlation Boundary:** difficulty、length 与 domain 的 logistic regressions控制若干 observed covariates，
  仍是相关性而非因果识别。Olmo-Think 中 SFT 先显著降低可控性，DPO/RL 后部分恢复但未回到 base；论文也明确
  pre-RL stage 影响仍不确定。跨 family 的 pre/post 比较同时改变 checkpoint、prompt、channel、API 与 token
  cap，因此不能写成“reasoning RL 单调降低可控性”的普遍演进律。
- **Trade-offs / New Failure Modes:** 显式 CoT 增加可审计 surface，也会暴露敏感信息并形成新的 prompt/control
  interface；限制模型操纵该 surface 可能保留 monitor signal，却也可能降低合法格式控制、压缩或隐私处理能力。
  多次尝试、feedback 与更大 action volume 放大稀有成功路径；依赖单次平均值会低估 deployment risk。只优化
  CoT monitor 还可能诱导隐藏表示、不可读 shorthand 或对 monitor 的 reward hacking。
- **Evolution Relationship:** `Layering / Dependency`：output inspection -> explicit CoT inspection ->
  controllability stress test -> monitorability/faithfulness evaluation -> executable action/outcome verification。
  `Principle Reuse`：与 Ch62 的 evaluator identity、proxy boundary 和 repeated-run contract一致；与 Ch68 的
  defense-in-depth 连接，但不能替代 tool authorization、least privilege、sandbox、outcome verifier 与 incident
  response。旧 output-only control 在短、低权限、可执行验证任务中仍成立。
- **ROADMAP / Chapters Read:** 主 owner 确认为 Ch68 Security，负责“CoT monitor 是 policy-bound sensor，
  不是 authority”的安全边界；已完整阅读 Ch67～69，并联读 Ch62 与 Ch5。Ch62 已有 scorer/proxy/evaluator
  contract，可用短 handoff承接 measurement identity；Ch69 已有 progressive evidence/recovery，无须复制。
- **Integration Decision:** `Refine — Existing Argument / Ch68 Integrated / Experimental`。Ch68 已分开
  controllability、surface monitorability、faithfulness 与 outcome safety，并把 parser/grader、attempt/
  feedback budget 和 action verifier 组成 threat-model contract。Ch62 不重复写入；正文未保留模型排名、
  百分比或厂商 headline，也未把 proxy 结论提升为生产安全保证。
- **Open Questions:** 如何在不训练模型学会规避具体 monitor 的前提下评估 spontaneous obfuscation？怎样把
  channel parser、grader、attempt budget、feedback 和 action verifier 组成可版本化 threat-model contract？
  哪些信号可证明 reasoning surface 与真实 decision causally related，而非事后 rationalization？

### SageBwd：低比特训练的瓶颈从前向激活转向微小反向信号

- **Candidate / Week / Score:** SageBwd: A Trainable Low-bit Attention / 2026-W10 / 25/30；
  `Source Family ID: sagebwd-trainable-int8-attention`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-02，当前仅一个版本）、完整 HTML 与 Appendix
  A～C；联读作者团队官方 SageAttention repository 以核验技术演进与 artifact 状态。该 repository 当前公开
  SageAttention 1/2/2++/3 inference/training-exploration paths，但未出现 SageBwd 名称或独立实现；因此本项
  `Paper Verified / SageBwd Code Not Publicly Located`，不能把相关 SageAttention3 kernel 当作本文代码。
- **Full-read Coverage:** Verified；已检查 Introduction、Related Work、FlashAttention/quantization/smoothing
  preliminaries、forward/backward algorithm、QK-norm、`dS` sensitivity 与理论上界、tokens-per-step、activation
  scale、78B-token pretraining、intermediate error tracing、kernel benchmark、smoothing ablations、Limitations、
  Appendix pseudocode/proof/per-layer errors，以及相关官方 repository 的 feature/support matrix。
- **Original Problem / Why Previous Design Was Reasonable:** FlashAttention 通过 tiling/online softmax 避免
  显式物化 `T×T` score，保持 exact semantics；SageAttention 再用低比特 Tensor Core 路径压缩 Q/K/P/V
  multiplication。Inference 只需控制 forward output error，fine-tuning 的短程 experiment 也可能容忍近似；
  但 full pretraining 将每步数值误差跨数百亿 tokens 累积，必须同时维护 forward、backward 与 optimizer
  trajectory。完整 BF16/FP16 attention 因而仍是精度基线，而非落后方案。
- **Changed Constraint / Principle:** 训练低比特化不能按“所有矩阵乘统一降到 INT8”处理。softmax backward
  中 `dS = P ⊙ (dP - delta)` 的 RMS 随 sequence length 受到约 `1/sqrt(N)` 上界约束，实测还远小于 `dP`；
  量化 step 对该弱信号的相对误差随后经 Q/K norm 放大到 dQ/dK。precision policy 应由 sensitivity path 和
  training horizon 决定，不由算子名称或硬件支持表决定。
- **Mechanism / Precision Partition:** forward 对 Q/K/V 做 per-block INT8，P 采用 per-token INT8，并以
  online softmax 保留 O 与 log-sum-exp `L`。backward 重算 S/P；`P^T dO -> dV`、`dS K -> dQ`、
  `dS^T Q -> dK` 使用 INT8 multiplication，但最敏感的 `dP = dO V^T` 保留 FP16；随后才计算并量化 dS。
  这不是“全 INT8 backward”，而是精度按误差传播路径分区。
- **Smoothing / Algebraic Boundary:** QK-norm 控制 token-wise Q/K scale，降低 uniform INT8 step 并避免大
  logits。K-smoothing 在 quantization 前减去 K 的 token mean；由于每行 dS 求和为零，`dS K` 对该平移
  不变，不需额外 backward correction。Q-smoothing 为保持 dK 等价必须增加 bias-gradient branch，形成新的
  quantization-noise path；作者 ablation 中没有稳定收益。这解释了为什么 inference 中对称的 Q/K smoothing
  不能无条件搬到 training backward。
- **State Ownership / Control and Data Flow:** model architecture 持有 QK-norm 与 learned RMS scale；attention
  kernel 持有 block/token scales、quantized Q/K/V/P/dO/dS、O 与 L；autograd path 持有 dP 精度、dS 形成和
  dQ/dK/dV accumulation；training runtime 持有 global batch/TPS、sequence length、gradient accumulation、
  learning rate 与 checkpoint trajectory。数据流为 `Q/K/V -> low-bit tiled forward -> O/L -> dO -> FP16 dP
  + recomputed P -> tiny dS -> INT8 dQ/dK + INT8 dV -> optimizer step`。
- **Evaluation Contract:** 325M Llama、OpenWebText、78B training tokens、context 4096、hidden 3072、GPT-2
  tokenizer、learning rate `3e-5`、cosine schedule、BF16 mixed precision；paper 称 runs 位于 single B200 or
  RTX4090 GPU node，但未披露 node 内 GPU count/topology、完整 software versions、seed/replicates、power 或
  cost。TPS 通过固定 length、改变 global batch 从 64/260K 到 512/2.1M；两组分别训练 300K/37.5K steps，
  total tokens近似相同但 optimizer-step count 与 warmup count不同。
- **What the Evidence Proves:** 在上述 325M/4096/78B contract 下，260K TPS 的 SageBwd 与 FPA loss 落在
  作者所称 noise 范围，而 2.1M TPS 保留 gap；高 TPS 移除 QK-norm 会发散。pseudo-quantized layer-11 trace
  将最大 relative error 定位到 dS 及下游 dQ/dK，K-smoothing ablation支持其稳定性作用。RTX4090、head dim
  64/128 的 forward+backward kernel microbenchmark报告最高 1.67×，只证明该实现形状下的 kernel opportunity。
- **What It Does Not Prove:** 它不证明较小 batch 修复了量化误差；作者解释是更高 stochastic gradient noise
  可能掩盖误差，且 low-TPS no-QK-norm 的中间 tensor 仍更差。两种 TPS 同时改变 optimizer-step/warmup 数，
  不能把 loss差异单独归因 batch。single 325M model、单 dataset、固定 4096 context 不支持外推 billion-scale、
  long-context、MoE、multi-node 或不同 optimizer。intermediate trace 把 dO 当作无误差并只取一个 checkpoint/
  layer setup；没有独立 reproduction 或公开 SageBwd code。
- **Trade-offs / New Failure Modes:** INT8 matmul减少 bytes并利用低比特 throughput，却增加 scale calculation、
  quantize/dequantize、mixed-precision branches 和 kernel-specific validation。QK-norm/K-smoothing提高稳定性，
  也改变 architecture/artifact identity；用较小 TPS换容错会增加 optimizer steps、collective/launch frequency
  与 wall-clock exposure。learned QK scale随训练增长，早期稳定不能证明后期安全；silent gradient drift 可能
  先表现为稳定但更差的 loss，而不是立即 NaN。
- **Where Previous Designs Still Apply:** full-precision attention适合高 TPS、未知 architecture、长 context、
  strict convergence 或尚无低比特 kernel 的硬件；mixed precision仅低比特化较不敏感 GEMM/forward path，适合
  渐进部署；降低 batch/TPS 只有在 optimizer-step/cost预算允许并经端到端 convergence验证时才合理。Inference
  SageAttention 的 forward trade-off 与 SageBwd 的 training contract 可共享量化原则，但不是直接替代关系。
- **Evolution Relationship:** `Direct Evolution`：exact IO-aware attention -> low-bit forward attention ->
  quantized forward/backward with sensitive dP retained -> sensitivity-aware precision allocation for dS path。
  `Layering / Dependency`：QK-norm/smoothing约束数值范围，training runtime的 TPS/step contract决定噪声如何
  暴露；kernel speed只有在 convergence不变量成立后才是系统收益。
- **ROADMAP / Chapters Read:** 主 owner 从初筛 Ch32 修正为 Ch24 Pretraining；已完整阅读 Ch23～25，并联读
  Ch14、Ch32～33 与 Ch45 的相关边界。Ch24 已有 mixed precision 与 TPS，但缺少“precision × gradient
  sensitivity × batch noise × horizon”的机制链；Ch14 只保留 logical attention handoff，Ch32/33解释 global
  batch与 distributed execution，Ch45 的 inference quantization不能承载 training convergence。
- **Integration Decision:** `Refine — Existing Argument / Ch24 Integrated / Experimental`。Ch24 已将
  mixed precision 扩展为沿误差传播路径分区的 sensitivity-aware policy，并补入 weak-gradient、数学不变量、
  batch-noise 与 training-horizon 证据边界。Ch14/32/45 不重复写入；正文未保留 RTX4090 倍率或把
  260K TPS 写成推荐配方。
- **Open Questions:** 怎样对 dS 使用 finer-grained/dynamic fallback而不失去 kernel throughput？如何把 learned
  QK scale、per-layer gradient error 与 loss drift变成在线 precision escalation signal？固定 token budget时，
  怎样用 matched optimizer-step/schedule实验分离 batch noise 与 quantization bias？

### MemSifter

- **Candidate / Week / Score:** MemSifter / 2026-W10 / 25/30；
  `Source Family ID: memsifter-outcome-driven-memory-proxy`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-03，当前仅一个版本）、完整 HTML、Appendix A/B、
  作者 repository、训练入口、task reward、checkpoint merge 与 inference toolkit。arXiv metadata 是首发日期
  authority；HTML 中残留的 `5 June 2009`、ACM conference/DOI template 不是事件日期，也暴露了 artifact
  metadata 未清理的问题。
- **Access and Full-read Coverage:** Verified；已检查 Abstract、Introduction、Related Work、Method 2～3、公式
  1～5、Optimization、Experiments、八个 benchmark、baseline、ablation、training dynamics、latency、Conclusion、
  Appendix A/B，以及官方 pipeline、reward、merge 和 two-GPU toolkit。论文没有独立 Limitations / Threats to
  Validity 章节，限制由实验合同和实现反推并明确标为本报告推断。
- **Original Problem / Why Previous Designs Were Reasonable:** 原始长历史可以用 embedding top-k，成本低且易增量；
  graph/hierarchical memory在多跳关系和高复用 corpus 上用较高 ingestion/index cost换取 query-time结构；大模型
  直接读取完整 history 则避免 retriever information bottleneck。随着 episodic history 动态增长、相关性取决于
  下游任务而非语义相似、working LLM 的长上下文成本上升，三条旧路线分别暴露 semantic miss、write-time
  结构化开销/损失和 read-time计算问题，但都没有因此失效。
- **Changed Constraint / Principle:** Memory 不再只是“事实存在哪里”，还包含“当前 working model 应如何选择
  哪些历史”。MemSifter 把 raw sessions留在外部 token store，把 retrieval skill写入小型 proxy参数；这是
  fact state与 selection-policy state分离。稳定原则是：retrieval policy应按 downstream utility评估，但其
  model、reward、task scorer、candidate set和版本必须成为可审计 identity。
- **Mechanism / State Ownership:** external store拥有原始 session与 ID；BGE-M3在超过 proxy context时执行 coarse
  filter；Qwen3-4B-Thinking proxy对候选执行 Think-and-Rank并输出 session IDs；orchestrator dereference top-k
  raw sessions；working LLM生成答案；task scorer把多级 top-k 答案转成 RL reward。Proxy参数保存 policy，
  不保存事实；training pipeline与 checkpoint averaging拥有 policy evolution；working LLM既是消费者，又通过
  outcome score进入训练信号。生成 rationale只是 ranking intermediate，不是可信 provenance。
- **Control / Data Flow:** `raw history -> sessionization/ID -> optional embedding coarse filter -> proxy rationale +
  ranked IDs -> raw-session dereference -> working LLM -> task score -> proxy RL update`。当 history超过 128K，
  coarse filter先决定 proxy永远看不到什么，因此它是 hard recall ceiling，不是可忽略的加速器。官方 toolkit
  进一步固定为 `BGE-M3 on cuda:0 -> generative ranker on cuda:1 -> OpenAI-compatible working LLM API`，显示
  论文的“lightweight”仍包含 embedding、生成式 rerank和外部推理服务三段。
- **Reward / Credit Mechanism:** 无 Memory得分为 `s0`，按 Fibonacci top-k（1、2、3、5……）多次调用 working
  LLM得到 `s_k`，再用 DCG-like diminishing weights近似各批新 session的 marginal utility：
  `R_ans = -s0 + sum(w_k * s_k)`。它减少逐 rank调用，却只能观测一批新增 context后的 aggregate delta；
  session complementarity、prompt position和生成随机性仍会混入 credit。warm-up使用 annotated DCG reward，
  随后 anneal到 outcome reward；每轮按当前能力附近 `tau=0.2`选择样本，三轮训练之间对 validation top
  checkpoints做 FP32参数算术平均。
- **Paper / Code Boundary:** 论文称每样本 `n=6` 的 GRPO sampling，并说明 dynamic sampling受 DAPO启发；官方
  脚本实际配置 `reward_manager=dapo`、group filtering、rollout correction、async vLLM等控制，同时保留可配置
  advantage estimator。这说明公开实现是 DAPO-style training stack，不应把“GRPO”或“DAPO”任何一个名字
  写成完整算法 identity。reward代码在 working-agent输入不足或调用失败时有 parsing/error paths，并按 F1等
  task metric计算多级得分；checkpoint merge只是同名参数的 arithmetic mean，不是 ensemble、optimizer-state
  merge或已证明保持 specialist能力的 consolidation。
- **Training / Evaluation Contract:** proxy为 Qwen3-4B-Thinking；论文披露 128K input、16K formal output、
  4K buffer、batch 32、每样本6次 sampling、三轮、8×H200；working model为外部 Qwen3-30B-A3B-Instruct。
  官方脚本补充 actor LR `1e-6`、weight decay `0.1`、8 GPU/node、Ulysses/FSDP、async vLLM、chunked
  prefill、prefix caching disabled和单序列 rollout，但 public paper/repository仍不足以固定全部 dataset revision、
  seed、software image、API model revision与独立 reproduction。评估实际是五个 personal-memory和三个
  deep-research benchmark；正文 4.4 的“six datasets”与 Table 1/Section 4.1 的八项不一致，且 4.1 后续的
  sample描述还出现未在八项清单中的 PerLTQA，故 dataset/sample contract存在文本歧义。
- **What the Evidence Proves:** 在作者 benchmark、candidate construction、working LLM、scorer与 hardware
  下，outcome-trained proxy在表中多项 retrieval/end-task metric优于所列 embedding、memory framework、graph、
  generative-rerank和long-context baselines；ablation支持 marginal baseline、rank weights与dynamic curriculum
  对该实现有贡献。单 H20的 WebDancer 128K表显示 proxy路径位于 BGE和大模型 full-context之间；这只证明
  作者测得的局部 latency/cost frontier，不是通用 production TCO。
- **What It Does Not Prove / Threats:** `s_k-s0`是依赖 working model、sampling、prompt与 task scorer的
  counterfactual proxy，不是某条 memory的因果贡献；Fibonacci batch不能分离组内 session，分数还可能
  non-monotonic。结果没有证明 proxy跨 working-model/reward revision稳定，也没有证明 graph/index在高复用、
  ACL、freshness或multi-hop场景失去价值。`<1% recall drop`缺少足够独立 contract；latency表未完整披露
  concurrency、batch、runtime revision、precision与端到端 SLO。Deep-research数据包含从 MiroVerse构造的
  synthetic long history，不能直接代表 live enterprise memory。
- **Trade-offs / New Failure Modes:** 它把 graph-heavy write-time cost换成每次 query扫描/生成的 read-time cost；
  proxy降低 working-LLM token cost，却成为新的 omission、policy drift和availability control point。coarse
  filter误删无法由后续 reasoning恢复；working model、reward或task distribution变化会让 policy stale；raw
  history的 tenant/ACL、consent、retention与deletion没有因“无复杂 index”而消失；session IDs、store version、
  proxy checkpoint、working model和scorer若不共同入 trace，线上选择无法复现。checkpoint平均可能平滑波动，
  也可能模糊不同局部能力；parser/fallback路径可能把格式错误变成训练信号变化。
- **Where Previous Designs Still Apply:** embedding top-k适合高吞吐、短query、低复杂依赖；graph/hierarchical
  index适合高复用、显式关系和严格 query latency；full-context适合history仍可控且不能容忍retrieval miss；
  deterministic filters适合ACL、时间、版本和hard constraints。MemSifter更适合作为 authorized candidate set
  之后的 learned reranking/selection层，而不是代替 source-of-truth、policy filter或所有 index。
- **Evolution Relationship:** `Direct Evolution`：semantic top-k -> generative reranking -> downstream-utility-
  trained memory proxy。`Layering / Dependency`：raw/versioned store与authorized coarse retrieval -> learned
  ranking policy -> working LLM。下一阶段压力是把 proxy、working model、reward、corpus和policy组成可版本化
  retrieval contract，并支持 drift detection、fallback、rollback和selective deletion；不是继续无限增大 proxy。
- **ROADMAP / Chapters Read:** 主 owner确认为 Ch73 Memory；已完整阅读 Ch72～75，并联读 Ch29与 Ch77边界。
  Ch72已覆盖 relevance、sufficiency和Agentic Retrieval，Ch73已覆盖read policy、derived state、provenance、
  consolidation与deletion，但尚未明确区分“事实状态”和“以参数保存的retrieval-policy state”，也未说明
  retrieval policy必须绑定 working-model/reward identity。Ch29承接 outcome RL与credit assignment；Ch75/77
  分别承接 task plan与authoritative workflow，不能拥有 memory selection机制。
- **Integration Decision:** `Refine — Existing Argument / Ch73 Integrated / Experimental`。Ch73 已补入 fact
  state 与 parameterized selection-policy state 分离、policy identity/drift、coarse-filter recall ceiling 和
  read-time/write-time cost migration。Ch72/29/77 不重复写入；正文未保留作者排名、单卡 latency，也未把
  learned proxy 提升为默认 memory architecture。
- **Open Questions:** 如何用 paired/randomized working-model calls估计 retrieval的真实 causal utility，并控制
  generation variance？working model、scorer或ACL变化时，怎样检测并回滚 stale proxy？怎样在 coarse filter
  后仍为rare但critical memory提供可证明的 recall/fallback？删除原始 session后，如何验证训练参数中的
  retrieval skill没有保留可利用的敏感模式？

### V1: Parallel Generation and Pairwise Self-Verification

- **Candidate / Week / Score:** V1 / 2026-W10 / 25/30；
  `Source Family ID: v1-parallel-pairwise-self-verification`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-04，当前仅一个版本）与完整 HTML；未在论文、
  arXiv artifact links或作者检索中定位 official code/model artifact，因此算法只能按论文与 Appendix核验，
  public implementation/reproduction为 `Not Disclosed / Not Located`。
- **Full-read Coverage:** Verified；已检查 Abstract、Introduction、Related Work、当前 self-verification/
  aggregation限制、V1-Infer算法、公式与四个 helper procedures、全部 inference结果和ablation、V1-PairRL
  objective、reward-hacking defenses、training setup/results/ablation、Conclusion、Appendix A～H、prompt、
  hyperparameters与正反例。论文没有独立的自身 Limitations / Threats to Validity章节；Section 3讨论的是
  prior方法限制，不能代替作者方案限制。
- **Original Problem / Why Previous Designs Were Reasonable:** 单轨 greedy或低温采样成本低且语义清晰；
  majority vote在答案可规范化且错误近似独立时能利用多样性；pointwise judge只需每候选一次评分；recursive
  aggregation可融合互补思路而非只选一个。随着开放代码/推理任务没有 inference-time ground truth、绝对分数
  跨候选不校准、aggregation可能丢弃正确outlier，多轨迹的瓶颈从“能否采到正确答案”转成“能否以有限预算
  找到它”。旧方案仍分别适用于低预算、客观答案和可组合候选，不应被后发算法否定。
- **Changed Constraint / Principle:** Parallel test-time scaling至少包含两个独立概率：candidate set中存在
  可接受解的 coverage，以及selector把它排到首位的 discrimination。增加 `N`主要提高前者；verification
  policy决定后者。稳定原则是：generation policy、candidate identity、comparison graph、judge prompt、
  selection budget与final verifier必须共同进入一次可复现的 selection run。
- **V1-Infer Mechanism / State Ownership:** 同一模型先独立生成 `N`个solutions；pairwise judge对一对候选各给
  1～10分和winner；runtime维护每个candidate的estimated score `mu_i`、distinct comparison degree `d_i`
  与已比较边集合 `H`。Phase 1用minimum-degree coverage让所有节点至少进入比较图；Phase 2按当前排名在
  local window内选择未比较的near-ties，形成Swiss-style refinement；最后按weighted win rate排序。Candidate
  text属于request state，comparison graph与budget属于runtime control state，judge outputs只是观测，不是
  ground truth。
- **Uncertainty Boundary:** 论文用两候选的模型自报评分差 `|r_i-r_j|/9`作为confidence weight，并以
  `tau`设floor。这是heuristic confidence proxy，不是经过proper scoring rule、reliability diagram或外部
  correctness校准的uncertainty。相同模型的score saturation、order/position bias、shared misconception与
  verbosity/style bias可同时污染winner和weight；pairwise提供相对reference，不自动产生全局calibration。
- **Compute / Control Flow:** `sample N candidates -> coverage comparisons -> update sparse tournament graph ->
  near-tie comparisons -> rank -> select one`。给定 `B=O(N)` verification budget可避免全量 `O(N^2)` pairs，
  但 `O(N)` model calls不等于 `O(N)` tokens、FLOPs、latency或cost：pairwise prompt包含两个可能很长的
  solutions，generation/verification输出长度与batchability不同，RSA aggregation也有不同token contract。
  论文用call count和部分latency比较，未披露统一hardware、serving runtime、batch/concurrency与SLO。
- **V1-PairRL Mechanism:** 同一 Qwen3-4B-Instruct policy每题生成4个solver rollouts，并把online current-
  policy solutions组成4个judge rollouts；`J = J_Gen + lambda J_PairVerif`。solver由ground-truth tests给binary
  reward；verifier把两解各评分归一到 `[0,1]`，只有距离correctness label不超过0.2才获得稀疏reward。训练
  使用DAPO配置、Clip High、token-level loss与Dr.GRPO式取消std normalization；不训练separate verifier。
- **Reward-Hacking / Curriculum Boundary:** 稀疏threshold阻止全输出0.5的safe-bet collapse；只在pair中至少
  一解正确时训练verification，避免生成empty incorrect解却让judge轻易得分。这两个修补也改变训练分布：
  当前policy零正确解的最难问题不给verification学习信号；Correct-Correct pairs缺少错误contrast；只保留
  “至少一正”会让verifier curriculum依赖solver capability。它控制已观察到的collapse，不证明generator与
  self-verifier不再共享其他shortcut或collusion channel。
- **Training / Evaluation Contract:** DeepCoder 24K verified coding problems；Qwen3-4B-Instruct-2507；150
  steps；batch64；LR `1e-6`；4 solver + 4 judge rollouts，相对baseline 8 solver rollouts；max prompt 10,240、
  response 24,576，evaluation最高32K并对训练后模型使用2K continuation形成34K上限；temperature 0.6 code/
  1.0 math，top-p 0.95。base-model inference实验只跑一次；trained结果三seeds取mean；checkpoint按validation
  pass@1选择。hardware、wall-clock、energy、完整software image和public code均未披露。
- **Evaluation Scope:** inference覆盖GPT-OSS-20B/120B、Qwen3-4B Instruct/Thinking、Gemini-2.5-Flash，
  LiveCodeBench v5/v6、CodeContests、AIME/HMMT与SWE-bench Lite。SWE-bench selector只看到issue与patch diff，
  不读取repository、tests、execution feedback或trajectory；final resolve仍由benchmark harness判定。Appendix
  同时展示pairwise选对、pointwise选错，以及pairwise偏好复杂但回归patch的反例，因此证据支持平均趋势，
  不支持单次pairwise verdict是可靠oracle。
- **What the Evidence Proves:** 在作者固定models、sampling、prompts、benchmarks与call budgets下，pairwise
  selection多次优于同scale pointwise selection；random-pair ablation支持coverage+near-tie策略相对纯随机有
  增量；online co-evolving pairwise objective在作者三项code benchmark上优于其pointwise co-training和standard
  RL baselines。它也直接证明unified generator/verifier训练会出现safe-bet与empty-solution failure modes，
  selection/training topology是机制的一部分。
- **What It Does Not Prove / Threats:** 单一作者study且base inference一次运行，不能证明pairwise普遍优于
  deterministic verifier、independent judge、majority或aggregation。Pass@N upper bound不等于selector可达；
  call-matched不等于compute-matched；validation checkpoint selection与少量seeds限制统计解释。PairRL只在
  executable code reward下训练，不能外推开放问答或安全判断。同一模型judge不提供独立evidence，1～10差值
  也未证明是概率calibrated confidence。无official artifact阻止代码路径、parser、并行调度与reproduction核验。
- **Trade-offs / New Failure Modes:** 多候选扩大coverage，也线性增加Decode/KV/cost并产生straggler；pairwise
  降低绝对评分难度，却建立有路径依赖的comparison graph、可能重复暴露长solutions，并受到candidate order、
  correlated error和style preference影响。稀疏图提高budget efficiency，却可能让早期错误score影响后续near-
  tie pairing；同一模型减少separate verifier的内存/运维，又牺牲independence。co-training减少generator-
  verifier distribution shift，同时引入joint-objective interference、online data feedback与新reward-hacking面。
- **Where Previous Designs Still Apply:** greedy/单样本适合低风险或严格latency；majority适合可canonicalize答案；
  executable tests优先于self-judge；independent verifier适合高风险、不同failure mode或可承担额外model state；
  aggregation适合候选包含互补partial solutions；pointwise适合候选很多、每次pair prompt昂贵且已有校准judge。
  Pairwise应是selection option，不是final correctness proof。
- **Evolution Relationship:** `Direct Evolution`：single sample -> best-of-N/majority -> pointwise self-selection ->
  sparse pairwise tournament selection。`Layering / Dependency`：parallel sampling提供coverage，comparison graph
  提供selection，external verifier/production policy提供acceptance。训练侧是 `offline verifier data -> online
  co-evolving generator/verifier`，收益是distribution freshness，代价是joint failure与reward hacking。
- **ROADMAP / Chapters Read:** 初筛 Ch43 owner被纠正。主 owner确认为 Ch20 Sampling；已完整阅读 Ch19～21。
  Ch20已有sequential budget与“parallel sampling + verifier是另一种scaling”的handoff，但缺少coverage与
  selection分解、comparison graph state、compute identity和self-verifier相关误差。Ch29拥有grouped rollout/
  GRPO与verifier specification；Ch62拥有evaluation evidence；Ch76拥有inference-time feedback。Ch43只管理
  KV physical paging，不应承载reasoning policy。
- **Integration Decision:** `Refine — Existing Argument / Ch20 Integrated / Experimental`。Ch20 已补入
  coverage/selection 分层、comparison-graph state、self-verifier correlated error、abstention 与真实 compute
  contract。Ch29/62/76 不重复写入；正文未保留作者百分点、固定 N/B、产品模型排名，也未把
  self-verification 称作 ground truth 或把 call count 写成真实 compute。
- **Open Questions:** pairwise score difference怎样用held-out executable labels校准为uncertainty？如何随机交换
  candidate order并估计judge transitivity/cycle/correlated-error？怎样把token、prefill、decode、KV、latency与
  dollars统一成budget，而不是只数calls？当candidate set没有正确解时，selector应何时停止并abstain，而不是
  强制选出“最好”的错误解？

### DynaMoE：percentile routing 的 cardinality 与论文主张冲突

- **Candidate / Week / Re-scored:** DynaMoE / 2026-W10 / `15/30`（原20/30）；
  `Source Family ID: dynamoe-percentile-routing-disputed`。全文复核后将TN/SI/PV/SR/L分别下调，因为central
  variable-K mechanism、theorem与system claim存在内部冲突，实验也未覆盖Transformer/standard MoE baseline。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-02，当前只有一个version）、25页PDF/完整HTML、
  Appendix A～C与pseudocode。未从论文artifact links、作者检索或公开项目中定位official code/checkpoint；
  因此implementation只能按伪代码审计，不能执行复现。
- **Full-read Coverage:** Verified；已检查Introduction/Related Work、standard MoE、dynamic percentile routing、
  capacity/load discussion、六种layer schedule、architecture、两个theorems/proposition、datasets/model configs、
  training/evaluation、全部results/ablations、理论解释、Limitations、training curves/expert statistics、proof、
  pseudocode与hyperparameter sensitivity，并联读Ch21及Ch32/40/45边界。
- **Original Problem / Why Previous Design Was Reasonable:** fixed top-k让每token active compute可预测，并能与
  capacity factor、load-balancing loss、dropless dispatch与grouped GEMM共同设计；uniform expert count让layer
  layout、checkpoint和parallel plan一致。它们可能错配不同token/layer的capacity need，但稳定shape与负载控制
  是大规模MoE成立条件，不是无依据的“僵化假设”。
- **Claimed Mechanism:** 每层按预定义descending/ascending/pyramid/wave schedule设置expert数 `N_l`；router先
  softmax，再在训练时加Gaussian noise，对每个token自身的`N_l`个gate values取固定percentile `tau`，选择
  `g_i > percentile_tau(g)`的experts，并在选中集合再次softmax。论文称其令`K(x)`随input complexity变化，
  同时不使用expert token-capacity或auxiliary balancing loss。
- **Central Consistency Failure — Cardinality:** 对长度为`N`且无ties的连续score vector，固定percentile按rank
  切分；高于该quantile的元素个数由`N`、quantile interpolation和`>`规则决定，通常固定为约
  `(1-tau)N`，与score分布“复杂度”无关。Gaussian noise会改变哪些expert位于top fraction，但不会使选中数量
  自由落在`1..K_max`。因此该实现接近rank-based fixed-k routing，而不是论文声称的input-dependent variable-K。
  这是对公式/伪代码的数学推断，尚无official code可检验是否存在未写出的absolute threshold分支。
- **Theory Boundary:** Theorem 1把dynamic activation space写成`sum_{k=1}^{K_max} C(N,k)`，但当前percentile
  selector没有生成全部cardinalities的机制；可达模式主要是固定cardinality的top subset，故expressivity比较
  不由定义推出。gradient-variance theorem又把dynamic routing具有更高entropy作为assumption A2，论文自己
  承认percentile不保证A2、expert independence也可能失败，且没有数值验证bound；它只能描述条件性可能，
  不能证明该router降低variance。
- **Capacity / State Ownership Failure:** per-token minimum-activation fallback只保证token至少选一个expert，
  不限制一个expert接收多少tokens，因而不能“处理overflow”。没有capacity、dropping/reroute或balancing时，
  batch仍可能集中到同一expert，产生dynamic dispatch、OOM/straggler和gradient starvation。真正需要追踪的
  状态是per-layer expert set、per-token route、per-expert token count、overflow policy与physical placement；
  论文只定义了前两项。
- **Layer Schedule Mechanism / Boundary:** predefined schedule确实让总expert parameters按depth变化，是独立于
  variable-K claim的architecture hypothesis。但不同schedule拥有不同layer parameter distribution；论文同时
  承认parameter/FLOP未严格匹配。手工schedule没有根据在线diversity或curvature学习，所谓descending optimality
  proposition只在“early-layer Hessian curvature始终更大”的条件下成立，未在实验中测量该条件。
- **Evaluation Contract:** image experiments为MNIST/Fashion-MNIST/CIFAR-10上的小型MLP-style networks；LM
  只有1,000 Recycling-the-Web samples、GPT-2 tokenizer、length128、约85K～1.4M models，per-token accuracy约
  5%、PPL约1,000～2,500。optimizer AdamW、LR 1e-3、image batch256、LM batch32、temperature0.5、noise0.1；
  hardware、seeds/replicates、precision、software image与consistent active-FLOP/latency contract未披露。
  当前architecture没有self-attention，文中的attention entropy/distance/specialization probes均未执行。
- **Baseline / Attribution Boundary:** baseline只有dense MLP与无auxiliary balancing/capacity的uniform MoE；
  缺少Switch top-1、GShard top-2、expert-choice与标准balancing ablation。作者也明确承认无法判断收益来自schedule
  还是弱baseline/缺失regularization。LM的best schedule随Tiny/Small/Medium改变，且Tiny由MLP最佳、Small的
  最佳DynaMoE只比MLP约0.1%，不支持论文实践建议把ascending/pyramid推广到language/time-series。
- **What the Evidence Proves:** 在作者小型image MLP实验中，改变layer expert-count schedule会改变accuracy、
  parameter count与convergence curve，说明“capacity across depth值得作为实验变量”。它没有证明percentile
  实现了variable compute，也没有证明推荐schedule、threshold或temperature可迁移到Transformer LLM、MoE
  training或distributed serving。
- **Trade-offs / Where Previous Designs Still Apply:** 真正variable-K可用absolute cumulative-mass/entropy/
  margin threshold、learned halting或budget controller，但会引入ragged assignments、负载上界、latency jitter、
  calibration与fallback。fixed top-k适合可预测FLOPs、static dispatch与严格TPOT；expert-choice适合显式
  balance；uniform expert count适合同构parallel/checkpoint。depth-wise nonuniform capacity只有在matched
  parameter/active-FLOP实验与placement可执行时才值得采用。
- **Evolution Relationship:** `Disputed Claim`：fixed top-k -> paper-claimed percentile variable-K，但公式实际
  仍近似fixed-cardinality rank selection。`Principle Reuse`：layer-wise capacity不必uniform是可测试假设，
  不能由本实验提升为LLM设计结论。下一阶段需要先修正selector definition，再加入standard MoE baselines、
  per-expert capacity、matched compute和Transformer-scale artifact。
- **ROADMAP / Existing Coverage:** Ch21已明确top-k、load balancing、capacity、All-to-All、active FLOPs不等于
  latency，并已把routing objective连接到executable communication shape；Ch32/40/45分别承接parallel、decode
  small batches与kernel/collective mapping。该论文没有形成可靠的新机制，反而与既有“capacity属于正确性”
  原则冲突。无需让一个受争议案例占据正文。
- **Integration Decision:** `Full Review Complete — Disputed / Weekly Only / No Books Change`。保留在Weekly作为
  central-mechanism审计案例；不把降分后的论文作为Books证据，也不为此增加反例段落。若作者发布code或修订
  selector，使active cardinality真正由absolute confidence/complexity改变，再重开审计。
- **Open Questions:** 作者实际实现的quantile API与ties/interpolation是否产生未披露的variable cardinality？
  怎样用matched total parameters、active FLOPs与per-expert capacity比较depth schedule？若真正允许variable-K，
  怎样给每请求计算预算和per-expert load建立硬上界，而不是只依赖router distribution？

### HACRL / HACPO：跨策略 Rollout 复用不是推理时 Multi-Agent

- **Candidate / Week / Re-scored:** Heterogeneous Agent Collaborative Reinforcement Learning / 2026-W10 /
  `23/30`（原24/30）；`Source Family ID: hacrl-cross-policy-rollout-reuse`。Source Reliability 从4降为3，
  因为后续v2虽补充理论、seed/runtime/memory与official code，核心保证仍依赖oracle capability ratio、正分母、
  bounded reward与gradient-alignment assumptions，不能等同于实际clipped finite-batch objective无偏。
- **Source Type / Date / Revision History:** arXiv v1 于2026-03-03首次公开，是本周事件；v2于2026-05-21
  修订作者列表、ratio定义、有限样本分析与实验合同，只作为revision verification，不改写W10日期。已联合阅读
  v1/v2全文、Appendix、project page与后续official HACRL-code；代码基于verl，公开双WorkerGroup、双tokenizer
  data swap、MAPO advantage与`mapo_clip` loss path。
- **Full-read Coverage:** Verified；已检查metadata/revision、Introduction、taxonomy/problem formalization、四项
  mechanism、全部公式与pseudocode、theory及assumptions、training/evaluation setup、main results、ablations、
  seeds/runtime/memory appendix、official README、trainer data flow与core loss摘要，并联读Ch28～31和Ch78。
- **Original Problem / Why Previous Design Was Reasonable:** GRPO/GSPO让每个policy用自己生成的grouped rollouts
  更新，sampling policy、old logprobs、tokenizer与advantage statistics同源，importance ratio与checkpoint语义
  清楚；teacher→student distillation则明确知识流向与quality ceiling。若多个模型正在解决相同可验证任务，
  隔离训练会重复支付generation/verifier成本，但旧方案以样本效率换取了on-policy边界、可控方差和简单ownership。
- **Changed Constraint / Principle:** 当同一组织同时训练多个不同state、size或family的reasoning policies时，
  每个verified trajectory可能对其他policy也有价值。新问题不再只是扩大同policy的`G`，而是能否把另一个
  sampling distribution的experience带入当前policy，同时显式管理capability mismatch、support mismatch与
  tokenizer identity。长期原则是：**experience可以共享，但生成它的policy identity与概率坐标不能丢失。**
- **Mechanism:** 每个agent对同一prompt各采样`G`条response并共享verifier reward。目标agent的baseline用各
  agent rewards乘capability ratio后聚合；cross-agent advantage再以相对capability调制。目标policy对来源policy
  response计算length-normalized sequence probability ratio，对ratio低于1的cross-policy样本施加stop-gradient
  exponential attenuation，并用上界1、逐mini-batch收紧下界的asymmetric clipping，防止foreign samples在后续
  updates主导梯度。每个agent最终仍独立部署，collaboration只存在于training loop。
- **State Ownership / Control and Data Flow:** training controller拥有agent set、prompt batch、source
  `model_source`、各agent tokenizer/template、rollout-policy revision、source old logprob、target retokenized
  logprob、reward、capability statistics、clip step与optimizer step。官方实现为main/aux分别建立WorkerGroup，
  生成后合并batch，在更新每个模型前切换到其tokenizer视图并重算相应advantage/logprob。数据流是
  `shared prompt -> per-agent rollout/reward -> source-tagged joint batch -> target-specific retokenization/logprob
  -> capability-adjusted advantage -> clipped cross-policy update -> independent checkpoints`。
- **Tokenizer / Probability Boundary:** v1对不同tokenizer先detokenize再retokenize，却以单一response length
  表达ratio；v2改为target/source各自的`L_k/L_j`，并报告其MATH样本平均约700 tokens时Qwen/Llama token count
  相差4%。这只能说明该语料上的平均length接近，不能证明text normalization、chat template、token boundary、
  EOS或support mismatch可忽略。跨family ratio是两个不同tokenization coordinate下的geometric-mean sequence
  likelihood比较，不是严格token-wise importance correction。
- **Theory Boundary:** v1的unbiasedness假设capability ratio与当前batch reward realization独立，但algorithm
  的moving window包含当前batch；v2改为oracle ratio严格无偏，并给bounded `[0,1]` reward、independent prompt/
  response sampling与positive denominator下的finite-batch concentration。若某agent success rate接近0，ratio
  error会被分母放大。Gradient consistency还要求source是competent collaborator、权重与reward-related term正相关，
  并使用self ratio约1等近似；实际exponential weighting与clipping有意引入bias换variance/stability。故论文支持
  “有条件可用”，不支持任意异构policy互相学习都保持on-policy方向。
- **Evaluation Contract:** 训练使用MATH的7.5k questions，比较Qwen3不同state/scale与Qwen/Llama family，评估
  MATH-500、MATH、GSM8K、AIME2025、AMC23、Minerva与Olympiad。v1披露八张GPU但未给型号/precision；训练
  max response 4096，主实验评估最高8196；AIME2025报告best@30，其他为avg@1。v2新增五seed的MATH-500
  结果及wall-clock/memory表：HACPO在该1.7B+4B setting总时长5h31m、overall memory 86%，但仍缺GPU型号、
  power/communication、完整token throughput与production SLO，因此“half rollout cost”不能外推为half wall time
  或half infrastructure cost。
- **Baselines / Ablations / What Evidence Proves:** 作者比较GRPO、GSPO、增加updates/rollouts的GSPO×2与naive
  share，并分别消融advantage、capability coefficient、exponential weighting和stepwise clipping；v2 seed实验
  支持所选math contract内的重复性。结果证明在这些model pairs、shared exact-answer reward与training recipe下，
  structured cross-policy reuse可优于naive sharing和所列baselines。它没有证明开放式reward、不同task objectives、
  极端capability gap、many-agent拓扑或生产异步rollout仍稳定；也没有把cross-agent收益与更多target-side forward/
  update、retokenization、双模型驻留和coordination overhead完全分离。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply:** 收益是提高每条verified rollout的reuse并可能
  交换互补策略；新增capability-stat staleness、near-zero denominator、foreign-support clipping、tokenizer/template
  drift、shared-verifier correlated error、source-policy version mismatch、双模型memory/communication与互相污染。
  单policy GRPO/GSPO仍适合只有一个目标模型、严格on-policy、高异质性或SLO要求可预测的训练；one-way
  distillation适合教师明显更强且不希望被student反向影响；offline replay适合允许更强bias correction和审计的场景。
- **Evolution Relationship:** `Direct Evolution`：isolated grouped on-policy rollout → source-tagged cross-policy
  experience reuse；`Layering / Dependency`：verifier contract、policy/version lineage、tokenizer identity与checkpoint
  consistency必须先成立。它与Ch78是`Explanatory Boundary`，不是inference multi-agent或协同tool workflow。
- **ROADMAP / Chapters Read:** 主owner确认为Ch29 GRPO；已阅读Ch28 PPO、Ch29 GRPO、Ch30 DPO、Ch31
  checkpoint与Ch78 Multi-Agent。Ch29已有grouped rollout、ratio、verifier与policy lag，但缺少cross-policy sample
  reuse、source-policy ownership、capability ratio和tokenizer-coordinate boundary；Ch31已有rollout-policy revision
  一致性；Ch78明确多Agent是推理责任/状态/通信分解，不能承载仅训练时共享experience的算法。
- **Integration Decision:** `Refine — Existing Argument / Ch29 Integrated / Experimental`。Ch29 已补入
  source-tagged cross-policy experience、policy/tokenizer/version ownership、retokenization 与 probability-
  coordinate 边界、finite-batch bias 和退出共享条件。Ch31/78 不重复写入；正文未保留作者平均百分点、
  固定 clip 参数或“half cost”headline，也未把 conditional theorem 写成实际 objective 的普遍保证。
- **Open Questions:** capability denominator接近0时应做shrinkage、floor还是退出共享？怎样用effective sample size、
  ratio tails与source-conditioned reward监控negative transfer？跨tokenizer sequence ratio能否建立更严格的text-level
  density contract？shared verifier发生systematic false positive时，多个policies会不会同步放大同一reward exploit？

### MUSE：安全评估对象从单次 Prompt 演进为跨模态 Run

- **Candidate / Week / Re-scored:** MUSE / 2026-W10 / `23/30`（原24/30）；
  `Source Family ID: muse-run-centric-multimodal-red-team`。Source Reliability从4降为3：论文全文与live web app
  可访问，但论文虽称open-source，正文、arXiv artifact和公开检索均未定位official repository/commit；核心judge
  只做100条、单human annotator的final-turn复核，实验也没有seed/repeated-run uncertainty。
- **Source Type / Date / Direct Sources:** arXiv v1于2026-03-03首次公开且无后续revision；已阅读完整HTML/PDF
  结构、Appendix A、live official web app入口与作者研究页。web app是mutable service且需要登录，不能替代
  immutable code/config/data artifact；公开页面与论文中未发现可核验commit、release、container image或run export。
- **Full-read Coverage:** Verified；已检查Introduction/Related Work、client-server/run model、attack strategies、
  ITMS、modality conversion/cache、provider routing、five-level judge、dataset/model/strategy/metrics contract、single-turn
  baseline、main results、modality ablation、turn curves、human validation、UI/license与Conclusion，并联读Ch62及Ch67～69。
- **Original Problem / Why Previous Design Was Reasonable:** 单轮text safety benchmark便宜、可重复且容易控制prompt；
  单模态multimodal benchmark可以隔离image/audio attack；binary refusal/ASR便于release gate。它们在接口单一、风险
  可以由单次response判定时合理，但现代系统的policy state会跨turn累积，且TTS、OCR/vision encoder、video parsing、
  provider adapter和conversation history分别形成新的trust boundary。
- **Changed Constraint / Principle:** 当输入在同一conversation中跨text/image/audio/video变化时，评估对象不再是
  `(prompt, response)`，而是带完整状态的run：攻击目标、strategy revision、turn budget、modality sequence、media
  artifact、target model/API、attacker、judge、每轮label与stop reason共同决定结果。长期原则是：**安全不是某个
  modality的静态属性，而是policy在trajectory与representation transitions上的条件行为。**
- **Mechanism / Run State:** 每个run持久化target、strategy、goal、conversation turns、attacker prompt、target
  response、judge label、delivery modality和generated media；campaign按goal聚合runs并支持stop/resume。Crescendo
  与Violent Durian保留conversation/backtracking，PAIR每轮重写single-turn prompt。ITMS只扩展保留context的strategy，
  在user-selected与model-supported modalities交集中循环选择下一模态；text经TTS、canvas rendering与audio+image
  composition形成payload，并以`(project, prompt, modality)`缓存。
- **State Ownership / Control and Data Flow:** campaign controller拥有run/campaign identity、resume checkpoint与
  budget；attack engine拥有prompt evolution/backtrack；conversion service拥有media bytes、codec/TTS/render version
  与cache；provider adapter拥有API payload/retry/model capability；target conversation拥有history；judge拥有taxonomy、
  prompt/model与per-turn verdict。数据流为`goal -> attacker text -> modality transform/cache -> provider adapter -> target
  response -> judge label -> run append -> stop/backtrack/next modality`。只保存最终ASR会丢失导致failure的transition。
- **Metric Mechanism:** five-level taxonomy把Compliance、Partial Compliance、Indirect Refusal、Direct Refusal与
  Non-Responsive分开；hard ASR只计完整Compliance，soft ASR还计Partial Compliance，两者差值描述gray-zone width。
  这比binary label保留更多policy信息，但仍是ordinal taxonomy而非连续risk；partial capability的可行动性、伤害
  severity和用户context没有进入同一量纲，不能仅靠soft-hard差值决定release。
- **Evaluation Contract:** 50个由AdvBench抽样并改写的goals，均分weapons、controlled substances、malware、
  biological threats和fraud；六个provider models、五种strategies、最多10 turns、backtrack limit 3、attacker
  temperature 0.9、约3,700 runs。GPT-4o同时充当attacker与temperature-0 judge。single-turn为24个
  model-modality conditions共1,200 runs；main为5×6×50共1,500 runs；ITMS ablation对四个omni models、六种
  modality configs做1,000 runs并因synthesis latency排除video。API snapshot、日期、seed、重复次数、token/
  latency/cost、TTS/codec/render版本、retry policy、raw runs与hardware均未披露。
- **Judge Validation Boundary:** Appendix随机抽100个runs，由一个human annotator按同taxonomy重标final turn，
  与GPT-4o judge达到93% agreement，分歧集中在Compliance/Partial Compliance。没有第二annotator、IAA、blinding、
  category/modality/model slice、完整turn validation或false-positive/negative matrix；attacker与judge同源又可能产生
  shared style/preferences。因此93%只支持该小样本的一致性，不把judge升级为ground truth，也不足以证明hard ASR
  没有systematic bias。
- **Causal / Baseline Boundary:** single-turn baseline使用direct goal，而multi-turn使用attacker重写、history、
  sampling与backtracking，故高ASR说明完整attack workflow与single-turn direct prompt行为不同，不能单独归因于
  “multi-turn pressure”。ITMS使用按supported modalities固定循环的序列，没有随机化transition order、paired
  counterfactual或same-media controls；turn-2 refusal变化与modality switch相关，但也可能受prompt/history、
  transformation artifacts、provider preprocessing与judge noise影响。论文将其解释为transition destabilization是
  plausible inference，不是被隔离证明的内部机制。
- **What the Evidence Proves:** 在上述50-goal、API aliases、attack prompts与single judge contract内，contextual
  attack比direct single-turn baseline暴露更多compliance，且modality configuration的方向在Gemini与Qwen families
  间不同；ITMS在部分conditions减少successful runs的first-compliance turn。它不证明公开模型普遍有90～100%
  jailbreak rate、当前版本仍保持同样行为、modality switching总会降低安全，或观察差异来自model core而非外部
  filter/preprocessor/API policy。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply:** run-centric记录获得可重放trajectory、partial
  leakage与turn-level attribution，却增加有害media存储、secret/API access、judge injection、provider drift、
  cache poisoning、campaign resume correctness、成本与数据retention风险。Single-turn deterministic tests仍适合
  快速regression；isolated modality tests适合定位encoder/filter边界；human red team适合新型语义风险；automated
  multi-turn campaign适合扩大coverage，但不能独立承担release verdict。
- **Evolution Relationship:** `Direct Evolution`：single-turn text test → isolated multimodal test / multi-turn text
  attack → run-centric multimodal trajectory test。`Layering / Dependency`：Ch62的EvalSpec/run identity提供测量合同，
  Ch68拥有threat model与red-team boundary，Ch69将证据接入release/rollback。下一阶段压力是随机化/配对因果设计、
  immutable provider/media/judge identity、独立judges与secure harmful-artifact governance。
- **ROADMAP / Chapters Read:** 主owner确认为Ch68 Security；已完整阅读Ch62、Ch67～69。Ch62已经定义完整subject/
  environment/scorer identity与run evidence，足以承接schema；Ch68已有持续risk measurement但缺少“跨turn与跨模态
  transition也是attack surface”的演进；Ch69只消费安全证据形成gate，不复制attack mechanics。
- **Integration Decision:** `Refine — Existing Argument / Ch68 Integrated / Experimental`。Ch68 已补入
  run-level multimodal threat state、旧测试继续成立的条件、harmful-media lifecycle 与 judge boundary。
  Ch62 不重复写入；正文未写 provider 排名、ASR headline，也未声称 modality transition 必然破坏 alignment。
- **Open Questions:** 怎样把modality sequence随机化并构造same-content paired counterfactual？如何版本化TTS、font/
  rendering、codec、provider adapter和API alias，使run可重放？有害media/cache的access、retention与deletion怎样治理？
  attacker、judge与target同源时如何估计correlated error，并用独立human/executable evidence校准partial compliance？

### MOOSE-Star：有用的任务分解不等于普遍复杂度下界

- **Candidate / Week / Re-scored:** MOOSE-Star / 2026-W10 / `17/30`（原22/30）；
  `Source Family ID: moose-star-decomposed-scientific-hypothesis-search`。Technical Novelty从4降为2、System
  Impact从3降为2、Longevity从5降为3：分解与层次检索有工程价值，但核心`O(N^k)`与`O(log N)`叙述依赖
  论文自己选择的latent-inspiration模型和best-case routing，不能当作直接训练`P(h|b)`的一般复杂度定理。
- **Source Type / Date / Revision History:** arXiv v1于2026-03-04首次公开；v2/v3/v4分别在2026-04-06、
  05-05与05-11发布，v4标记ICML 2026。W10事件只按v1归档；v4、Appendix G与current repository仅用于核对
  revision、训练合同、额外实验和实现边界，不把后续模型或结果倒灌为3月事件。
- **Direct / Related Primary Sources and Access:** 已阅读v1完整HTML/PDF、v4完整HTML、全部Appendix、official
  repository、training/evaluation/inference说明、hierarchical tree/search path与IR probability extractor。论文与
  repository链接的dataset/model cards本轮受访问权限限制，未绕过；因此其内容只按论文和repo中可核对字段记录。
  repository当前无release/tag，公开main分支只有少量commits，不能提供与v1逐提交对应的immutable artifact。
- **Full-read Coverage:** Verified；覆盖Introduction/Related Work、decomposition assumptions、Dataset
  Construction、Method I～IV、公式与algorithm、train/eval setup、scaling、ablation、temporal reconstruction、
  test-time scaling、Limitations、theory appendices、case study及官方代码。已完整阅读Ch75，并联读Ch72、Ch62、
  Ch77以检查retrieval、planning、evaluation与workflow ownership。
- **Original Problem / Why Previous Design Was Reasonable:** 直接从研究背景生成假设把文献检索、证据选择、
  组合和表述隐含在一个生成目标内，难以定位失败、提供中间监督或控制search budget；brute-force sampling在
  verifier昂贵且正确组合稀疏时会快速浪费预算。但端到端autoregressive SFT本身只计算给定`(b,h)`的token loss，
  并不显式枚举`N^k`个inspiration tuples；旧设计在有高质量end-to-end demonstrations、latent path不唯一或无法可靠
  标注causal inspiration时仍然合理。
- **Changed Constraint / Useful Principle:** 当corpus、tool budget和可验证中间状态成为显式系统资源时，可以把
  开放生成改写为typed stages：`motivation -> inspiration retrieval -> bounded composition -> intermediate
  hypothesis`。这个分解获得局部训练/evaluation接口，却把原先隐含的不确定性转移为citation-derived labels、tree
  construction、routing probability、composition tolerance与stage handoff state。
- **Mechanism:** TOMATO-Star从论文抽取background、final hypothesis与cited inspirations，并强制每个citation
  对应一个motivation/mechanism/methodology delta。IR在15个候选中选择一个inspiration，HC把当前hypothesis与选中
  inspiration组合为下一状态；bounded composition用ground-truth inspiration的semantic neighborhood训练HC容忍
  retrieval noise；offline tree按SPECTER2语义聚类，online best-first search以沿路径概率的geometric mean维护frontier；
  motivation planning用对下一方向的描述引导路由。
- **State Ownership / Control and Data Flow:** dataset pipeline拥有paper split、background/hypothesis/citation labels与
  automated QA；tree builder拥有embedding、cluster hierarchy和node membership；IR model拥有candidate probability；
  search controller拥有frontier、path score、visited/proposed nodes与budget；HC model拥有intermediate hypothesis；
  evaluator拥有M3 rubric、judge identity和ground-truth target。数据流为`paper -> post-hoc decomposition -> IR/HC
  supervision -> offline tree -> motivation-conditioned best-first retrieval -> bounded HC -> target-recall judge`。
- **Theory Boundary:** `P(h|b)`可用latent inspirations分解是一个建模假设；Appendix还需要minimal path、Markov/
  conditional-independence以及固定或可重排inspiration sequence。由“有效hypothesis可以被某组inspirations解释”不能
  推出所有直接训练都必须显式搜索Cartesian product，也不能把model parameterization、optimization或sample
  complexity统一记为`O(N^k)`。因此论文证明的是该显式latent-search formulation可被顺序分解，不是通用下界。
- **Search-Complexity Boundary:** 作者明确把`O(log N)`限定为balanced hierarchy中IR作出ideal routing decision的
  best case；best-first frontier与backtracking没有worst-case sublinear保证。实际3,035项corpus实验平均需要67.78次
  IR calls，加入detailed motivation后仍为63.05次且ground-truth平均proposed rank为742.50；这支持相对tournament
  baseline更省calls，不支持将真实端到端复杂度等同于tree depth。
- **Dataset / Label Boundary:** 108,717篇NCBI open-access论文覆盖2020-01至2025-10，训练到9月、10月测试；
  DeepSeek-R1与R1-Distill-Qwen-32B从目标论文反向抽取background、hypothesis和citations，再做necessity、
  sufficiency、disjointness与non-redundancy自动检查。Citation是可审计proxy，却不是唯一causal inspiration；正确的
  uncited或alternative inspirations会在15-way IR中被当作negative，one-citation-one-delta也是强结构假设。
- **Training / Implementation Contract:** current v4 repo以R1-Distill-Qwen-7B学生和32B teacher rejection sampling
  构造SFT；full-parameter BF16、DeepSpeed ZeRO-3，HC effective batch 128/64 GPUs，IR batch 128/128 GPUs，IR
  sequence length 16,384、1 epoch；数据构造约38,400 A800 GPU hours。该资源合同说明分解并未消除系统成本，而是
  把成本转移到post-hoc decomposition、teacher sampling、双模型训练、offline clustering与多次online calls。
- **Artifact Consistency / Failure Mode:** `ir_probability_extractor.py`对API/format错误最多重试10次；最终仍找不到
  selection marker时给所有labels相同`-1.0` log-prob，再由`max(probabilities, key=...)`选择argmax。由于字典保持
  label插入顺序，这不是注释所称random selection，而会静默偏向首个candidate；缺失top-logprob的label另被设为
  `-100`。这使prompt format、truncation、candidate order和SGLang logprob contract成为retrieval correctness状态。
- **Evaluation Contract:** IR为15-way pool（一个citation-derived positive与14 negatives）；HC用GPT-4o执行0～12的
  M3 rubric，比对已知论文hypothesis的信息召回。层次检索只在1,658篇10月论文产生的3,035个inspirations上测试；
  temporal reconstruction按已知target/citations检查top-k retrieval与hypothesis recall。test-time scaling用IR+HC调用
  数计budget，而非matched tokens/FLOPs/wall time/cost；不同stage还有8K/20K级output budgets。
- **What the Evidence Proves / Does Not Prove:** 作者合同内，decomposed IR/HC可学习、hierarchical best-first比
  tournament减少IR calls，增加训练数据和搜索budget能改善部分target-reconstruction metrics。它不证明生成了此前
  未知且真实、有用、可实验验证的发现，不证明citation path是唯一ground truth，不证明direct`P(h|b)`训练有普遍
  exponential lower bound，也不证明`O(log N)`是average/worst-case或production latency。论文Limitations也明确未研究
  feedback-driven refinement与experiment-guided ranking。
- **Trade-offs / Previous Designs Still Apply:** 分解获得可观察state、局部监督、candidate pruning与bounded-noise
  training；代价是label/target leakage、stage error propagation、tree/index freshness、routing/parser bias、模型与
  judge相关误差、更多service calls和large offline cost。Direct generation适合latent path不唯一或low-latency场景；
  flat dense/vector retrieval适合中小corpus与高recall requirement；hierarchical search适合大corpus但必须有fallback、
  budget与recall audit；experiment-guided search在可执行反馈存在时仍是检验truth/utility的必要后层。
- **Evolution Relationship:** `Principle Reuse`：monolithic generation -> retrieval/composition decomposition ->
  hierarchical budgeted search -> motivation-guided search -> experiment/verifier-guided ranking。后一步不是覆盖前一步：
  proposal、retrieval与validation分别解决不同问题；没有外部evidence，层次搜索只提高已定义proxy下的candidate
  proposal效率。
- **ROADMAP / Existing Coverage:** Ch75已经明确decomposition的call/state-handoff代价、search branching与
  verifier boundary；Ch72已有coarse-to-fine retrieval prior、sufficiency与index identity；Ch62已有target、judge、
  dataset/environment版本及proxy边界；Ch77已有evaluator-driven search和lineage。MOOSE-Star没有提供足以改变这些
  设计结论的新可靠机制，其central complexity claim反而需要留在Weekly作为反例。
- **Integration Decision:** `Full Review Complete — Disputed / Weekly Only / No Books Change`。不把`O(N^k) ->
  O(log N)`写入Books，也不因论文headline新增章节。可取的typed decomposition与hierarchical prior已被Ch75/72覆盖；
  本轮以具体章节去重证据完成disposition。
- **Open Questions:** 能否用multiple valid inspirations、citation-removed blind annotation与prospective expert review
  重新定义label？best-first在recall target与adversarial routing下的average/worst-case calls是多少？如何用matched
  tokens/FLOPs/latency/cost比较direct sampling与IR+HC？parser fallback应怎样randomize、abstain或fail closed？

### Phi-4-reasoning-vision-15B：训练数据同时定义感知接口与推理预算

- **Candidate / Week / Score:** Phi-4-reasoning-vision-15B Technical Report / 2026-W10 / `22/30`；
  `Source Family ID: phi4-reasoning-vision-mixed-mode-multimodal-sft`。
- **Source Type / Date / Direct Sources:** arXiv v1于2026-03-04首次公开且当前无revision；已联合阅读完整
  technical report、Appendix A、Microsoft Research说明、official model card、official GitHub repository、
  Transformers/vLLM integration入口与Transparency Note。模型release date同为2026-03-04，MIT license。
- **Access / Artifact Verification:** paper、model card和repo可访问。official model card声明15B、16,384 context、
  text+image input/text output、240 B200训练4天，并列出软件与tested GPU；但Data Overview仍引用占位符
  `RRRR_nnnn_Data Card`，paper所称后续公开部分training data和evaluation logs在本轮没有形成可定位、immutable的
  artifact。GitHub当前无release/tag且只有少量commits，README citation还错误指向`arXiv:2511.19663`，故不能用
  repository headline替代paper identity和完整training provenance。
- **Full-read Coverage:** Verified；覆盖Introduction、early/mid-fusion rationale、vision encoder/resolution ablation、
  三阶段训练、数据过滤/纠错/合成、math/science与computer-use mixture、reasoning/non-reasoning路线、mode token、
  Applications、完整Evaluation/timing、Safety、Limitations、open release和公开数据Appendix；并阅读Ch23～25、
  Ch17、Ch20与Ch62相关边界。
- **Original Problem / Why Previous Designs Were Reasonable:** 纯text reasoning backbone看不到图像；early fusion让
  image patches与text从底层共同建模，expressivity高但需要更大data/compute；late/mid fusion复用成熟vision encoder
  与LLM，通过projector对齐，降低训练成本但可能压缩跨模态interaction。始终reason会增加输出tokens和latency；始终
  direct又可能损失math/science多步任务。独立thinking/non-thinking models边界清晰，却增加artifact、routing和capacity
  成本。它们分别在大规模联合预训练、可预测SLO或严格任务隔离时仍合理。
- **Changed Constraint / Principle:** 对compact multimodal model，能力瓶颈不只在LLM reasoning：若vision encoder
  没有保留细粒度UI/diagram evidence，后续reasoning无法恢复已丢失信息；而提高resolution会把更多visual tokens送入
  Transformer，增加attention/context成本。与此同时，训练集中`reasoning/direct`比例和mode marker会学习一个隐式
  compute policy。因此data pipeline同时定义**模型看见什么**以及**何时花更多sequential compute**。
- **Architecture / Mechanism:** SigLIP-2 NaFlex dynamic-resolution encoder把图像转换为最多3,600 visual soft tokens，
  MLP projector映射到Phi-4-Reasoning embedding space，再与text tokens交错进入mid-fusion LLM。Stage 1只训练随机初始化
  projector；Stage 2解冻projector、vision encoder和LLM，在single-image instruction mix上联合训练；Stage 3继续全量
  更新，加入long-context、multi-image和RAI data。Spatial coordinates统一归一化到`[0,1]`。
- **Mode Mechanism:** SFT reasoning samples包含`<think>...</think>`，direct samples以`<nothink>`开头；reasoning约占
  20%，主要覆盖math/science，direct覆盖captioning、grounding、OCR与simple VQA。模型从data/task correlation隐式学习
  mode boundary，用户也可显式token override。它是learned routing policy，不等同于独立验证“任务是否需要reasoning”，
  也不是runtime根据实时SLO、uncertainty或cost动态求解的controller。
- **State Ownership / Control and Data Flow:** data pipeline拥有source/provenance、image-text pair、quality label、
  synthetic correction lineage、task/domain与mode tag；image processor拥有resize/patch/token budget和coordinate
  normalization；vision encoder/projector拥有cross-modal representation；LLM拥有token generation；chat template/system
  prompt拥有default mode policy；runtime拥有max tokens、precision和serving implementation；evaluator拥有benchmark、
  prompt/mode、judge和hardware。流程为`image/source -> filter/correct/augment -> task+mode mixture -> staged SFT ->
  visual tokenization/projector -> learned mode selection -> direct or reasoning generation -> task/latency/safety eval`。
- **Data Quality Mechanism / Boundary:** 团队先人工抽查每个dataset约5～10分钟，分类正确性、可答性、image quality
  与format；对wrong answers/captions用GPT-4o和o4-mini再生成、验证或majority vote，失败较多的dataset删除；同一image
  还可生成detailed description、format instruction、scrambled/caption-matching multi-image与sequential screenshot
  “what changed” samples。该流程说明quality engineering比原始token count重要，但teacher/model-judge共享错误、source
  license/provenance、retention/slice变化及synthetic-lineage完整统计没有公开，不能把“data quality is primary lever”
  解释为独立因果定律。
- **Mixture Ablation Boundary:** math/science与computer-use比例实验只在5B variation、固定1M general pairs上进行；
  math使用150K records并可重复3次，CUA最多450K并可增加400K Phi-Ground。结果支持该受限设置下targeted GUI data
  能补ScreenSpot且两域未必互相伤害；不证明15B最终mixture最优、duplication普遍安全或single-model总优于specialized
  post-training。Resolution ablation也使用5B与10M image-text pairs；最多3,600 tokens提高部分high-resolution tasks，
  但不同方法的actual token usage和benchmark方向并不一致。
- **Training Contract:** 三阶段training samples为2.0M/62.8M/3.2M，tokens为1.4B/188.5B/12B，max sequence
  2,048/8,192/16,384，global batch 1,024/1,920/1,920；AdamW、BF16、DeepSpeed ZeRO-1、每阶段1 epoch。
  model card补充240 B200、4天，但没有stage级GPU utilization、wall time、energy、data-loader效率或failure/restart合同。
- **Evaluation Contract:** Accuracy使用Eureka ML Insights和VLMEvalKit，覆盖vision QA、OCR、math/science和
  ScreenSpot。Latency/accuracy frontier只从ChartQA、MathVista-mini、MMMU-val、ScreenSpot各随机100例测量；H100、
  single thread、no concurrency、batch 1。Phi用system prompt/chat template、temperature 0、greedy、max output 4,096；
  third-party models使用各自推荐设置，Qwen另做matched max-output variants。作者因vLLM提高interactive per-query latency
  而改用另一条timing path；因此这些结果描述单请求交互条件，不证明production throughput、tail SLO、memory或cost。
- **Safety Evidence Boundary:** report/model card只给Text-to-Text 1.4%与Image-to-Text 4.5% automated defect rate，
  没有公开denominator、dataset、policy taxonomy、judge/calibration、confidence interval、modality slices或attack budget。
  它只能作为版本化厂商结果，不能说明image input普遍比text“不安全”，也不能成为deployment release threshold。
- **What the Evidence Proves / Does Not Prove:** 在作者training/evaluation contract中，mid-fusion 15B model可由约202B
  multimodal SFT tokens形成多类能力；dynamic high-resolution与targeted data在5B ablation中改善部分细粒度任务；mixed
  mode在不同benchmarks上有时优于强制单一mode。它不证明mid fusion普遍优于early fusion，不证明20/80是最佳配比，
  不证明显式CoT忠实，也不证明作者benchmark、latency或safety结果可跨runtime/workload直接外推。
- **Trade-offs / New Failure Modes:** mid fusion换取component reuse与较低训练成本，但引入projector bottleneck、
  vision/text representation skew与component-version coupling；high resolution提高感知recall却增加context/attention/TTFT；
  mixed mode减少不必要reasoning，却会误路由、受task stereotype影响并暴露special-token/prompt injection surface；synthetic
  correction提高label质量也可能复制teacher blind spot。多阶段全量解冻还引入catastrophic forgetting与stage lineage。
- **Evolution Relationship:** `Layering / Dependency`：pretrained reasoning LLM + pretrained vision encoder -> frozen-
  component projector alignment -> joint multimodal instruction tuning -> long/multi-image/safety continuation；`Direct
  Evolution`：always direct / always reason / separate models -> one model with data-trained mode token -> future
  uncertainty/SLO-aware external routing。后一层未在本报告实现，不能把implicit mode choice写成已校准controller。
- **ROADMAP / Existing Coverage:** 初筛Ch27不正确：报告没有RLHF机制。主owner修正为Ch23 Data，负责multimodal
  source correction、task/mode mixture和synthetic lineage；Ch25拥有mode-tag SFT objective；Ch17只短接mid-fusion
  representation boundary；Ch20拥有generated-token budget；Ch62拥有mode/hardware/workload评估合同。当前Ch23已有一般
  data mixture/quality原则，但缺少“data tag同时学习compute policy”以及视觉token budget与data capability的连接。
- **Integration Decision:** `Refine — Existing Argument / Ch23 Integrated / Experimental`。已在 Ch23 补入
  data tag作为 learned mode/compute policy、visual-token transformation与serving/evaluation contract的连接，
  同时保留 separate model/external router/single mode 的成立条件。未复制模型名、benchmark表、20/80配方或
  240 B200数字；Ch17/20/25/62当前已有边界，无需重复修改。
- **Open Questions:** mode selection怎样用task uncertainty、visual evidence sufficiency和runtime SLO校准？visual token
  budget怎样在accuracy/TTFT/KV/cost间动态分配？synthetic correction怎样保留teacher/judge/source lineage并抽样审计？
  early/mid fusion如何在matched model/data/compute下比较？安全defect rate的完整measurement contract是什么？

### T2S-Bench：显式结构脚手架不等于已证明的通用内部表示

- **Candidate / Week / Score:** T2S-Bench / Structure-of-Thought / 2026-W10 / `18/30`（由
  `20/30` 调整；System Impact 与 Longevity 各下调 1）；`Source Family ID:
  t2s-structured-intermediate-evaluation`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-04 首次公开且当前只有一个版本；已阅读
  45 页完整 HTML/PDF、全部 Appendix、official project page、official repository、公开 evaluator 入口与
  dataset card 链接。repository 当前无 release/tag；公开 artifact 主要覆盖 evaluation，未定位到可复现
  dataset-construction 与 GRPO training 的完整 pipeline。
- **Full-read Coverage:** Verified；覆盖 Introduction/Related Work、结构定义、T2S-Train/MR/E2E 三部分
  构建流程、32 种 structure taxonomy、人工复核、E2E/MR metrics、18 个模型实验、SoT prompt、GRPO、
  LongBench/SCROLLS transfer、correlation analysis、Impact Statement、全部 construction/evaluation prompts、
  implementation details 与 examples；并联读 Ch70～72 和 Ch62。
- **Original Problem / Why Previous Designs Were Reasonable:** 自然语言 CoT 容易把实体、依赖、层级与因果
  混在序列中；对流程图、概念图和生物通路等任务，显式 graph-like state 能提供可检查的 node/link interface。
  但自由文本在结构不唯一、知识不完整、低延迟或任务只需最终答案时仍然合理；schema-first extraction 也早已是
  workflow/RAG 中把非结构 evidence 转成 typed state 的常见工程分支。
- **Changed Constraint / Principle:** 当任务要求跨段、多跳、层级或关系组合时，单一 token sequence 不再是最易
  审计的 working state。显式结构可以作为**外部脚手架与中间制品**，但 benchmark 中“输出一张图”与模型内部
  确实使用忠实、因果有效的结构表示是两个命题。必须分离 `representation format`、`extraction correctness`、
  `reasoning utility` 与 `faithfulness to latent computation`。
- **Dataset Construction / Provenance:** T2S-Train 为 1,200 条、MR test 为 500 条、E2E 为 87 条，覆盖六个
  scientific domains、17 个 subfields 与 32 种结构。作者使用 GPT-5.2 搜索论文、pdffigures2 crop、GPT-4o
  判 relevance、Gemini-2.5-Pro 判 JSON representability，再由 GPT-o3/Gemini 做 text alignment；首轮约
  1,521 pairs 后由 11 名 PhD experts 得到 672 vetted pairs。MR 从每个 reference graph 按四类、八模板生成
  questions，再经模型交叉检查与 15 名 PhD experts 复核；E2E 由 GPT-o3 转 JSON 并裁剪无关节点/边，再由
  GPT-5.2/Gemini 与五名 PhD students 检查。
- **Split / Ground-truth Boundary:** 论文只说明 MR 按 domain 做 7:3 stratified split，没有披露 split unit、
  source-document/diagram 去重或同一 graph 派生的多道问题是否跨 train/test；E2E 与 T2S-Train/MR 的 source
  overlap 也未披露。被同行评审论文中的 diagram 不是天然因果 ground truth；高引用、开放获取且有可解析图的
  选择还会系统性排除无图、低资源或不适合图表示的有效知识。
- **Evaluation Object / Oracle Boundary:** MR 输入只有 text、question 与 options，不给 reference graph，测的是
  multiple-choice answer；模型可能靠文本模式直接作答，并不证明先恢复结构。所谓 E2E 又被拆成两个条件任务：
  link evaluation 提供全部 gold nodes 后预测 links，node evaluation 提供已有 links/IDs 后预测 node labels。
  因而 node semantics 或 topology/cardinality 分别由 oracle 提供；这不是从原始文本自由发现完整 graph 的联合
  end-to-end extraction。
- **Metric Boundary:** node 指标是基于 sentence-embedding 的 semantic similarity，link 才使用 F1。headline 中
  的“node accuracy”不能按离散 entity correctness 解读；相似措辞可能高分但实体、方向或 provenance 错误。
  evaluator/model identity、threshold 与 schema parser 都是 measurement state，不能只保存一个总分。
- **SoT Prompt / Control Flow:** SoT 要求模型先列 nodes/links，再回答；作者在八项任务、三个模型上与 direct/
  CoT 比较。流程是 `text -> prompted graph-like serialization -> answer -> task metric`，并未验证 serialized state
  对答案有因果贡献。各 prompt 的输出 token、FLOPs、latency 与 cost 未做 matched-budget 控制，增益可能来自
  更强格式约束或更多 test-time compute，而非一种普遍优越的内部表示。
- **Training Contract / Internal Inconsistency:** 主文称 Qwen2.5-7B 与 Llama-3.1-8B 使用 GRPO 训练 `100
  epochs`，Appendix F 却写约 `200 steps`、batch 32、8×A100、单节点、veRL。reward definition、rollout group、
  learning rate、precision、sequence length、KL、random seeds 与完整 compute 未披露；公开 repo 也未定位到
  对应训练入口。这一冲突阻止把 downstream gain 解释成可复现的结构推理训练配方。
- **Evaluation Contract:** generation 使用 temperature 0 与 strict output schema；官方 evaluator 对 provider-
  specific reasoning/content field、retry/backoff 与 resume 有专门路径。LongBench/SCROLLS transfer table 未给
  seeds、置信区间或 significance，且 CoT 在若干任务下降。模型 scale/T2S/LongBench 的相关性没有控制 model
  family、training data、task difficulty 或 compute，不能推出“结构抽取是 long-context reasoning 的因果中介”。
- **What the Evidence Proves:** 在作者构建、模型辅助且经专家复核的 scientific-diagram corpus 上，多种模型可在
  oracle-conditioned node/link 子任务中恢复部分结构；显式 SoT prompt 和受限 GRPO runs 在若干 downstream
  metrics 上改善作者报告结果。这支持“typed intermediate artifact 值得作为可观察 workflow 分支进一步研究”。
- **What It Does Not Prove / Limitations:** 不证明模型内部形成忠实 graph，不证明 graph 是所有领域的 universal
  intermediate representation，不证明结构 extraction 导致 downstream gain，也不证明 E2E free-form discovery。
  论文没有独立 Limitations section；annotator allocation、blinding、IAA/disagreement、source-level leakage、
  evaluator calibration 与训练可复现合同均不完整。
- **Trade-offs / Previous Designs Still Apply:** 结构化 state 提高 inspectability、局部 validation、reuse 与 tool
  interoperability，但引入 schema loss、ontology drift、node/link identity、parser failure、graph versioning 与
  额外 token/latency。自由文本适合结构不唯一与探索性 reasoning；RAG evidence graph 适合有 provenance 的
  retrieval；executable state machine 适合需要强 action semantics 的 workflow。它们是并存分支，不是由 SoT
  单向替代。
- **Evolution Relationship:** `Principle Reuse`：free-form context -> externally serialized typed state -> local
  node/link validation -> downstream use -> causal/faithfulness audit。该研究位于“表示与评估”的接口，不构成模型
  架构的 `Direct Evolution`。
- **ROADMAP / Existing Coverage:** 主 claim owner 从初筛 Ch62 修正为 Ch71。Ch71 已明确 Context 是 working
  state、结构化压缩必须携带 loss/provenance、typed fields 需要 schema/version；Ch70 已区分 CoT 可读性与正确性；
  Ch62 已要求 dataset/metric/evaluator/run identity；Ch72 已覆盖 graph/evidence retrieval boundary。T2S 没有
  提供足以改变这些既有设计结论的新可靠机制。
- **Integration Decision:** `Full Review Complete — Weekly Only / No Books Change`。保留为“benchmark 如何把
  oracle-conditioned subtask 写成 E2E、prompt scaffold 如何被误读为 causal representation”的反例；不把论文名、
  相关性结论、100 epochs/200 steps 冲突配方或未对齐 budget 的 SoT gain 写入 Books。
- **Open Questions:** 如何按 source graph 做 leakage-safe split？怎样联合评估自由 graph discovery 而不注入 gold
  topology/cardinality？如何用 intervention/ablation 验证结构 artifact 对答案的 causal utility，并在 matched token/
  FLOPs/latency/cost 下比较 direct、CoT 与 SoT？schema 与 semantic matcher 怎样做版本化、calibration 和 abstention？

### CRISP：把 Prompt 中的行为蒸馏进权重，也把 Teacher Refresh 变成训练状态

- **Candidate / Week / Score:** CRISP（v1 名称为 On-Policy Self-Distillation for Reasoning Compression，
  OPSDC）/ 2026-W10 / `24/30`；`Source Family ID: crisp-on-policy-context-distillation`。
- **Source Type / Dates / Revision History:** arXiv v1 于 2026-03-05 首发，之后经历 v2～v7，当前 v7
  于 2026-07-03 发布并改名 CRISP。历史事件按 v1 归 W10；v7、current official repository 与 checkpoints
  只作为 revision/artifact 核验，不能倒写成 W10 当时已经公开的证据。
- **Direct / Related Primary Sources and Access:** 已阅读 v1 的 30 页 PDF/完整 HTML/Appendix A～H、当前 v7
  完整 HTML/Appendix A～J、revision history、official repository README、data builder、trainer、worker、
  reverse-KL implementation、launch config、dual-path scorer 与公开 checkpoint index。repository 当前 28 commits，
  未见 release/tag；代码是 current artifact，不是 immutable v1 snapshot。
- **Original Problem / Why Previous Designs Were Reasonable:** 长 reasoning trace 可能包含重复验证、回溯与格式
  重述，增加 Decode/KV/latency/cost；但长链也给困难任务保留 exploration 与 correction。最简单的 concise prompt
  无需训练且易回滚，却只在 prompt 存在时生效；筛选短且正确的 traces 做 SFT 容易部署，却引入 teacher/off-policy
  distribution shift；length-reward RL 能显式优化 correctness/length，却需要 verifier、multiple rollouts 与 reward
  shaping。三者在临时控制、有可靠 demonstrations 或有可靠 outcome verifier 时仍合理。
- **Changed Constraint / Principle:** 如果同一 checkpoint 已能在 privileged context `c` 下表现得更简洁，训练可以
  不依赖外部答案，而把“有 `c` 的条件分布”迁移到“无 `c` 的条件分布”。这是一类 **context distillation**：
  supervision 不是 sampled teacher text，而是同一 response prefix 上、不同 context 下的 full-vocabulary logits。
  它减少外部 label 依赖，却把 prompt wording、teacher snapshot、refresh cadence 与 student rollout distribution
  变成新的训练 specification。
- **Mechanism / Objective:** student 从原始 prompt 采样 `y ~ pi_theta(.|x)`；periodically frozen teacher 在同一
  student prefix `y_<t` 上读取带 conciseness instruction 的 prompt `(x,c)`，输出 `pi_bar(.|x,c,y_<t)`；训练最小化
  `KL(pi_theta(.|x,y_<t) || pi_bar(.|x,c,y_<t))`。因此 teacher 并没有先生成一条短 trace 供 student teacher-
  forcing；它对 student 实际访问的 prefixes 逐 token 重评分。所有 rollouts 无论答案正确与否都进入 loss，ground
  truth 只用于 validation metrics，不参与 update。
- **Periodic Teacher / Control Flow:** teacher 初始为 base snapshot，每 `M` steps 硬复制 student；每一步先由已同步
  rollout replica 生成，student/teacher 对同一 response 做双 forward 与 student backward，必要时 refresh teacher，
  再把新 student weights 同步给下一步 rollout engine。`M=∞` 稳定但只能蒸馏一次已有 prompt behavior；有限 `M`
  允许 iterative compression；过小 `M` 形成 co-adaptation feedback，作者实验中的 `M=1` 发生 accuracy/length
  collapse。refresh interval 不是普通超参数，而是 moving-target staleness 与 gain 的控制面。
- **State Ownership / Data Flow:** dataset 持有 question、ground truth（仅评估）、student/teacher prompt 与 split；
  rollout runtime 持有 sampling config、student policy revision 与 truncation；teacher state 持有 snapshot revision、
  instruction identity 和 refresh step；trainer 持有 response masks、reverse-KL reduction、optimizer/data cursor；
  evaluator 持有 benchmark、answer extractor、symbolic verifier、generation budget 与 checkpoint selection。流程为
  `prompt pair -> student rollout -> same-prefix student/teacher logits -> masked reverse KL -> student update -> optional
  teacher refresh -> rollout weight sync -> versioned evaluation`。
- **Implementation / Cost Contract:** v1/v7 使用约 13.6K DAPO-Math prompts、single rollout、temperature 1.0、
  max training response 8,192、batch 32、AdamW `1e-6`、BF16、8×H200；FSDP parameter/optimizer CPU offload、
  Ulysses SP=4、SGLang rollout TP=2。公开 worker 对 response positions 计算 full-vocab reverse KL，并按有效 tokens
  求 mean，chunked FP32 softmax/teacher freeing 控制显存。它不需要 Reward Model、critic 或 group rollouts，但仍需
  autoregressive generation、student forward/backward、额外 frozen-teacher forward、两份 mutable/frozen weight state、
  periodic copy 与 rollout sync；不能简称为普通廉价 SFT。
- **Revision / Scorer Boundary:** v1 用单一路径答案抽取时，Qwen3-14B MATH-500 base/OPSDC 被报告为
  `70.0/86.1`；v7 的 dual-path scorer 同时接受指定 `Answer:` 行或 literal `\\boxed{}`，同一模型族主要结果变为
  `93.0/95.2`（v2）或 `96.3`（v1 instruction）。v7 还显示 base correct outputs 分散在两种格式，而 CRISP 把
  输出集中到 `Answer:`。因此 v1 的大幅“accuracy gain”大量混合了 format compliance 与 reasoning correctness；
  可保留的结论是压缩/格式固化与受限 accuracy frontier，而不是 9～16 点的普遍能力提升。
- **Current Evaluation Contract:** v7 扩为 Qwen3-8B/14B 与 DeepSeek-R1-Distill-Llama-8B，MATH-500、AIME
  2024/2025、GPQA-D、MMLU；math generation 使用 temperature 0.6、top-p 0.95、top-k 20、mean@8、30K
  budget。不同 instruction 位于不同 compression/accuracy frontier，hard AIME 更易退化；继续训练超过 sweet spot
  也会以少量额外压缩换取明显 accuracy loss。没有 seeds/多次独立 training runs、confidence intervals、latency、
  throughput、KV、energy 或 production concurrency contract。
- **Agentic Appendix Boundary:** 后续 v7 在 DeepPlanning 上使用 Qwen3-14B、`M=40` 与 vLLM/function-calling
  harness，travel 取 100 samples、每 case 最多 400 LLM calls；base 只重复 10 次估 variance。shopping/travel
  metrics 在部分 checkpoints 附近保持，但没有 matched call/latency/cost、完整 slice uncertainty 或独立 reproduction，
  不能推出无 verifier 领域都能安全压缩。
- **Theory / Objective Boundary:** autoregressive KL chain rule适用于未归一化、完整 sequence distribution；论文
  algorithm 和公开代码实际按 response token mean 归一化，并允许 truncated partial rollouts，因而不等于文中直接
  使用的完整 sequence-level KL。accuracy bound又以“teacher 保持准确且 converged KL 足够小”为前提，periodic teacher
  则持续改变 reference；它是 conditional bound，不是方法自动保正确的证明。
- **Difficulty / Error Claims Boundary:** “difficulty adaptive”定理预设 harder task 的 essential-token fraction更高、
  且 compressible tokens 的 KL 更大；论文没有独立标注/干预这些 latent categories，以不同 benchmark 的平均长度/
  accuracy作支持，不能证明 instance-level difficulty calibration。`(1-p_err)^L`的 compounding-error模型又假设每个
  token独立、不可逆地产生错误且compression不改变per-token error rate；它只能是思想实验，不能解释实际因果收益。
- **Entropy Boundary:** current artifact记录on-policy response positions上的平均full-vocab per-token entropy在短训练
  窗口内未趋零。这排除一种局部next-token collapse，却不等于保留sequence-level mode diversity、calibration、
  rare skills或所有domain能力；output format和length distribution已经显著改变。
- **What the Evidence Proves:** 在作者math prompts、三种模型、公开full-vocab reverse-KL implementation与指定
  sampling/evaluator contract下，privileged conciseness context可通过student-prefix logit distillation迁移到无提示
  policy；periodic refresh、KL direction、instruction与training duration共同形成compression/stability frontier。公开
  code验证了所有rollouts参与loss、teacher hard refresh与rollout weight sync等核心control flow。
- **What It Does Not Prove:** 不证明短CoT更忠实或更安全，不证明teacher不看ground truth就不会蒸馏错误，不证明
  自动识别每个problem难度，不证明数学外任意领域或production Agent保持质量，也不证明v1 headline准确率提升。
  Current code注释仍混用JSD、frozen teacher和teacher solution等旧语义；最终run必须以actual config/checkpoint为准。
- **Trade-offs / New Failure Modes:** 获得persistent concision、无外部答案与dense token signal；付出双forward、
  rollout、teacher snapshot/refresh和更复杂lineage。instruction bias会固化为weight behavior；错误student prefixes同样
  被蒸馏；过快refresh引发feedback collapse，过慢refresh限制gain；过度training/过强prompt损伤hard-task exploration；
  answer format固化可提高某scorer却降低其他interface兼容性。prompt-only、verified short-trace SFT与outcome-RL分别在
  reversible control、可靠demonstrations和可验证任务中继续成立。
- **Evolution Relationship:** `Direct Evolution` within behavior compression：runtime concise prompt -> off-policy short-
  trace SFT -> student-rollout contextual logit distillation -> periodically refreshed self-policy distillation。另有
  `Layering / Dependency`：Ch20拥有runtime token/stopping budget；Ch31拥有teacher/student/rollout checkpoint lifecycle；
  Ch62约束format-aware scorer与compression/quality frontier。
- **ROADMAP / Existing Coverage:** 初筛Ch28/29不准确：本方法没有advantage、reward objective、policy ratio或group
  normalization，不能归为PPO/GRPO。主owner确认为Ch25 SFT/Distillation；已完整阅读Ch24～30相关边界，并联读Ch20、
  Ch31与Ch62。Ch25已有off-policy demonstration/cascade distillation与forgetting，但尚缺privileged-context logit
  distillation、student-prefix alignment和mutable teacher refresh；这是可进入Books的长期机制缺口。
- **Integration Decision:** `Refine — Existing Argument / Ch25 Integrated / Experimental`。Ch25 已补入
  same-prefix contextual-logit distillation、teacher snapshot/refresh ownership、stability frontier，以及
  correctness/format/length 的评估解耦。Ch20/31/62 不重复写入；正文未保留 v1 headline、具体 M/设备配方
  或单篇 benchmark 数字。
- **Open Questions:** 怎样用outcome verifier或counterfactual trace edit识别“短且正确”而非“短且自洽错误”？teacher
  refresh如何由KL/entropy/accuracy/length drift触发而不是固定step？如何定义length-normalized partial-prefix objective的
  正确理论边界？怎样同时审计sequence diversity、hard-tail accuracy、format portability与production cost？

### RubricBench：评估标准的形成与执行是两种不同状态

- **Candidate / Week / Score:** RubricBench / 2026-W10 / 23/30；
  `Source Family ID: rubricbench-specification-execution-gap`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-02，当前只有一个 arXiv version）、23 页
  PDF/完整 HTML、Appendix A～F、official dataset、sample outputs 与 evaluator code；后续 ACL 版本只用于
  publication identity，不改写 W10 event date。repository没有 release/tag，公开的是 dataset、四组 sample
  submissions 与 accuracy evaluator，不是完整 annotation、rubric generation和全部论文实验 pipeline。
- **Full-read Coverage:** Verified；已检查 Introduction/Related Work、三阶段 construction、domain/source
  composition、annotation/QC、controlled evaluation、models/checkpoints、preference与structural metrics、main
  results、test-time scaling、failure analysis、Limitations、annotator profiles、strict matching、human study、
  IAA、feature-analysis prompts、全部 judge prompts，以及 official evaluator 的 parse、missing/duplicate与
  grouped-accuracy semantics。
- **Original Problem / Why Previous Designs Were Reasonable:** scalar Reward Model 用单分数压缩 preference，
  便于训练与排序；generative judge增加 rationale，适合开放式响应；通用 preference benchmark则提供统一
  comparison。随着 instruction变得复合、implicit constraint与 safety boundary增多，三者容易把长度、格式、
  自信语气或完整叙述误当质量，但它们在低歧义、可校准或有 executable verifier 的任务上仍然合理。
- **Changed Constraint / Principle:** 复杂质量判断至少包含两个可独立失败的阶段：先形成“什么算正确”的
  evaluation specification，再执行这些 criteria 得出 verdict。更强 judge或更多 sampling只能扩大对当前
  specification的执行，不能保证补回被遗漏、倒置或虚构的标准。Rubric因此不是 prompt decoration，而是有
  owner、版本、优先级、适用域与审批边界的 measurement state。
- **Construction / Mechanism:** 作者从既有 preference datasets筛出 1,147 个困难 pair，覆盖 Chat、IF、STEM、
  Coding与Safety；过滤条件包括复合/隐含输入约束、rejected response的长度/格式/语气优势，以及由 judge CoT
  检出的多类process failure。九名专家分组三方参与：instruction-only双人独立标注，每题形成2～10个原子
  Yes/No checks，再由senior reviewer reconciliation、结构一致性/去重/指令对齐与spot stress test完成QC。
- **State Ownership / Control and Data Flow:** instruction与source label属于dataset state；human rubric及其
  reconciliation记录属于specification state；generated rubric属于judge-specific derived state；matcher
  model把generated item映射到gold item；verdict judge执行rubric；evaluator按公开label聚合accuracy。流程为
  `source pair -> hard-case filter -> instruction-only rubric -> QC/version -> rubric generation -> rubric matching
  and execution -> pairwise verdict -> slice aggregation`。specification owner与execution owner必须分开追踪。
- **Metrics / Matcher Boundary:** Preference Accuracy只比较A/B label。Rubric Recall统计gold items被至少一个
  generated item匹配的比例；Hallucination Rate统计generated items没有gold match的比例；Structural F1把
  `1-hallucination rate`当precision proxy。匹配本身由Qwen3-30B-A3B在temperature 0执行语义判定，而
  Claude-4.5-Haiku又用于necessity/rigidity feature分析；这些模型、prompt和parser都是metric identity，
  temperature 0不使语义判断变为deterministic ground truth。
- **Evaluation Contract:** 论文比较scalar/generative RM、vanilla LLM judge与多种rubric-aware pipeline，并在
  fixed backbone/prompt/decoding下切换Vanilla、Self-Generated和Human-Authored rubric。作者用100例、两位
  human evaluators检查rubric-source effect；用Qwen3-14B对全量matcher结果、human对200个stratified items
  检查matching agreement。论文列出主要 checkpoint/API ID，但未给出硬件、API snapshot、seed/replicates、
  sampling variance、完整software image或端到端成本/SLO。
- **What the Evidence Proves:** 在该作者筛选的公开困难集与指定judge pipeline下，human-authored rubric明显
  改善多类judge的pairwise accuracy，更多self-generated criteria或迭代refinement没有单调关闭差距；即便给
  定human rubric，judge仍有soft-constraint、implicit reweighting、abstention与execution failure。100例的人类
  子实验支持低质量generated rubric也会约束human evaluator，而不只是模型推理能力不足。
- **What It Does Not Prove / Threats:** `Human-Annotated Oracle`是controlled upper-bound命名，不证明human
  criteria完整、跨组织稳定或适合生产risk policy。hard-case filtering主动富集surface/process failure，使
  accuracy不能代表自然流量 prevalence；样本来自既有公开benchmarks，gold labels/rubrics也公开，存在
  contamination与benchmark-specific optimization风险。matcher 0.85 model-model、0.79 human-model agreement
  只是有限协议下的一致率，不证明每个match正确；论文将其称为稳定基础的表述强于证据。100例human study
  很小，且同一pair/rubric design与source labels并非完整factorial causal isolation。
- **Artifact / Reproduction Boundary:** official evaluator只读取公开 `case_id,label,domain`，把missing/invalid
  prediction计错、duplicate取最后一行，并报告总accuracy与五组domain accuracy；它不重放rubric generation、
  judge calls、matcher、annotation reconciliation或paper tables。current repo sample只含四组
  Gemini-3-Flash rubric systems，不能复现论文全模型矩阵。公开label使该artifact适合研究诊断与回归，不适合
  直接充当保密release gate或训练后无污染的最终测试。
- **Trade-offs / New Failure Modes:** atomic binary rubric提高可检查性、failure localization与治理能力，却会
  把连续质量、criteria dependency、must-have优先级和合法alternative压成平坦checklist。instruction-only防止
  response-aware leakage，也可能无法表达只有观察candidate/artifact后才显现的风险。human rubric提高质量但
  昂贵、更新慢且带组织价值判断；generated rubric便宜可扩展，却会漏掉implicit/safety constraint或制造无关
  条件。更多criteria还会增加judge token cost、conflict与soft-voting机会。
- **Where Previous Designs Still Apply:** exact/executable verifier优先用于可形式化correctness；scalar score适合
  大规模粗排且已校准的窄任务；generative judge适合开放式诊断；human review适合高风险、规范冲突与新域。
  Rubric应把这些证据组合成typed specification，而不是替代所有scorer。训练reward使用的rubric还必须防止
  policy直接优化公开表面形式，并与product evaluation保持独立holdout。
- **Evolution Relationship:** `Direct Evolution`：opaque scalar preference -> rationale-producing judge ->
  explicit rubric-guided judgment -> separately audited rubric formation and execution。`Layering / Dependency`：
  intended use/risk policy -> rubric specification -> criterion executor -> evidence aggregation -> release/reward
  decision。下一阶段压力是支持criteria priority/dependency、rubric drift、disagreement、holdout与可执行证据，
  不是把checklist数量继续放大。
- **ROADMAP / Chapters Read:** 主 owner确认为 Ch62 Evaluation System；已完整阅读 Ch61～63并联读
  Ch27～29。Ch62已有EvalSpec、scorer audit、judge identity与dataset governance，但尚未明确把rubric
  formation和rubric execution建模为两种可独立失败、独立版本化的状态。Ch27～29只承接reward specification
  进入训练后的优化风险，不复制evaluation机制。
- **Integration Decision:** `Refine — Existing Argument / Ch62 Integrated / Experimental`。Ch62 已补入
  rubric formation/criterion execution split、priority/dependency、generated-rubric holdout 与 human-rubric
  evidence boundary。Ch27～29 不重复写入；正文未写模型排名或通用比例，也未把 human rubric 称为绝对 oracle。
- **Open Questions:** rubric version改变时如何区分系统进步与measurement drift？如何表达must-have、soft
  preference、criteria dependency与合法替代路径，而不退化成flat vote？怎样用hidden holdout、executable
  verifier与human disagreement共同验证generated rubric，而不让policy学习公开gold checklist？

### IF-RewardBench：局部约束验证不自动形成一致的全局排序

- **Candidate / Week / Score:** IF-RewardBench / 2026-W10 / 24/30；
  `Source Family ID: if-rewardbench-verification-ranking-graph`。
- **Source Type / Date / Direct Sources:** arXiv v1（2026-03-05，当前只有一个 arXiv version）、27 页
  PDF/完整 HTML、Appendix A～G、official data、vLLM inference、position map与constraint/overall metrics
  code。后续 ACL publication只用于身份核验。repository当前只有6 commits且无release/tag、dependency lock
  或 license file，复现必须固定commit，不能只写 `main`。
- **Full-read Coverage:** Verified；已检查Introduction/Related Work、task definition、constraint taxonomy、
  instruction collection/synthesis/filter/decomposition、response generation、human annotation、Pareto preference
  graph、statistics、models/metrics、main results、complexity/hierarchy、inference scaling、downstream correlation、
  Limitations/Ethics、全部Appendix、prompts/hardware，以及official inference/metrics parser和Elo path。
- **Original Problem / Why Previous Designs Were Reasonable:** winner/loser pair准确率简单、便宜，并与pairwise
  preference data直接对应；Best-of-N只检查judge是否选到最优candidate，适合selection deployment。随着训练与
  inference需要在同一prompt下排序多个相近responses，孤立pair可能掩盖cycle、tie、global-order inconsistency，
  单轮/可执行格式约束也覆盖不了multi-turn carry-over和system/user priority。旧指标仍回答局部选择问题，但不
  足以代表完整ranking policy。
- **Changed Constraint / Principle:** Judge至少有两种可独立失败的能力：逐constraint判断是否满足
  (`verification`)，以及让多个responses的分数/比较与gold partial order一致 (`ranking`)。即使每条binary
  check大多正确，flat averaging、constraint priority、parser fallback或pairwise aggregation也可能产生错误
  global order；反之，偶然排对顺序不证明局部理由正确。
- **Construction / Mechanism:** 作者从真实应用与14个公开benchmarks收集、再按7类constraint与4种composition
  类型合成约24.6K instructions，经LLM评分、embedding+DBSCAN与人工过滤到3,978，再由LLM分解checklist并
  人工修订/平衡为2,459。16个response models各负责一部分instructions，每题生成8个responses。22位annotators
  做逐constraint双标、检查与cross-validation，之后只保留positive response在所有constraints上不差、至少一项
  更好的Pareto-dominance edge，并由两人一致确认；最终842个graphs、平均7.14 responses与10.86 edges。
- **State Ownership / Control and Data Flow:** instruction hierarchy与checklist属于evaluation specification；
  per-response constraint labels属于human evidence；preference graph只保存无歧义的partial-order edges；judge
  输出属于model/prompt/parser-specific derived state；Elo与Kendall aggregation属于metric state。数据流为
  `instruction/system/history -> checklist -> candidate responses -> per-constraint verdict vector -> Pareto edges ->
  judge pairwise/pointwise outputs -> parser -> score/Elo -> graph correlation`。
- **Metric Semantics:** constraint assessment对每题分别计算positive/negative F1，并用由flat mean constraint
  score产生的ranking与gold edges计算Kendall tau-b；overall assessment对所有response pairs调用judge，再用
  反复shuffle的Elo生成listwise scores。总体结果是三种instruction types的macro mean，而不是按sample数量
  micro average。Pareto graph避免显式trade-off label，却也删除了criteria互有胜负的真实难题，因此测的是
  “无歧义partial order恢复”，不是完整human preference utility。
- **Paper / Code Consistency Boundary:** official constraint parser要求特定中文marker；解析不到或返回项少于
  checklist时，`get_label`用positive (`1`) 补齐，格式失败不是invalid/abstain而是“默认满足”。这会抬高
  positive倾向、压低negative detection并改变derived ranking。overall path把含A且不含B解析为A、含B且不含A
  解析为B，其余跳过，再用固定seed的100轮Elo shuffle聚合。故prompt、language、marker、fallback、position
  map、Elo seed/K-factor/epochs都是benchmark identity，不能只引用model name与tau。
- **Evaluation Contract:** 21个judge models；non-thinking model用greedy，reasoning model用default decoding/
  thinking budget；open models在4×H100、vLLM上运行。pairwise candidate order随机化。作者另用300个经embedding
  去重的online-chat instructions、每题8 responses、15 judges做Best-of-8 correlation。API revision、具体
  reasoning budget、software versions、seed repeats、latency/token/cost与SLO未形成完整跨model contract。
- **What the Evidence Proves:** 在作者dataset、annotation、parser与aggregation下，constraint negative
  detection普遍弱于positive verification，multi-turn/system-prompt与更多constraints带来额外压力；明确提供
  checklist通常比让judge隐式恢复constraint更可靠。self-consistency在两个model上先改善后饱和，thinking-off
  ablation支持reasoning path对此任务有贡献。system/user冲突slice揭示judge可能奖励低优先级instruction。
  meta-eval与300题Best-of-8的正相关只支持该model set与selection protocol下的相对关联。
- **What It Does Not Prove / Threats:** 专用RM在本表落后不证明生产默认应换frontier API judge；两者成本、
  latency、privacy、版本稳定性与训练分布未匹配。constraint平均分把must-have与soft constraint等权，无法表达
  safety veto、依赖或合法替代。response每题来自单一generator减少style confound，也把graph difficulty与该
  generator的局部error modes绑定。仅71.2% candidate relations获一致保留会选择更易标注的edges；Kappa与长度
  均衡不消除selection、taxonomy和language bias。embedding dedup不证明无语义/训练污染，300题相关性也不是
  因果或跨域保证。
- **Trade-offs / New Failure Modes:** preference graph比isolated pairs更接近multi-candidate selection，代价是
  O(m²) judge calls、Elo path/ordering state与cycle/tie处理；constraint checklist提高诊断性，却增加分解、
  version与parser surface。Pareto-only提高label可信度，却回避真实trade-off；人工cross-validation提高质量但
  昂贵且更新慢。system hierarchy明确后更可验证，也可能把平台policy和task intent混入同一flat checklist。
- **Where Previous Designs Still Apply:** pairwise accuracy适合cheap regression与单次preference；BoN outcome
  适合实际selector；exact rules适合格式/数值；human review处理criteria conflict；listwise graph适合reward/
  selection模型的order consistency audit。生产需要同时保留local confusion matrix、graph violations、
  calibration、cost与high-risk veto，而不是以tau替代correctness。
- **Evolution Relationship:** `Direct Evolution`：isolated winner/loser -> best-of-N outcome -> multi-response
  preference graph -> verification/ranking joint audit。`Layering / Dependency`：instruction hierarchy -> typed
  constraints -> local verdicts -> partial order -> training/selection decision。它与RubricBench互补：后者审计
  criteria形成/执行，本项审计既定criteria的local-to-global consistency；不是两次重复的“judge不可靠”。
- **ROADMAP / Chapters Read:** 主owner确认为Ch62；已完整阅读Ch61～63并联读Ch28～29。Ch62已有scorer、
  disagreement与dataset governance，但缺少verification-to-ranking graph、criteria priority与parser fallback
  如何改变metric identity。Ch28/29只handoff到reward进入policy optimization后的放大风险。
- **Integration Decision:** `Refine — Existing Argument / Ch62 Integrated / Experimental`。已与 RubricBench
  合并沉淀 specification formation -> local execution -> global aggregation、partial-order graph、parser failure
  与 instruction hierarchy；未单独堆论文案例，也未写模型排名、tau 或硬件配置。
- **Open Questions:** 如何在不删除trade-off edge的前提下表达constraint priority、veto与partial order？parser
  failure应计错、abstain还是进入separate reliability metric？怎样用subquadratic comparison graph仍检测cycle、
  tie与global inconsistency？reward model的listwise error怎样映射到policy update，而不是只看meta-eval tau？

### Interactive Benchmarks：被评估对象从答案扩展为反馈约束下的策略

- **Candidate / Week / Score:** Interactive Benchmarks / 2026-W10 / 25/30；
  `Source Family ID: interactivebench-feedback-policy-evaluation`。
- **Source Type / Dates / Revision History:** 历史事件为 arXiv v1（2026-03-05）；完整阅读 v1 PDF，并以
  v4（2026-05-16；中间 v2/v3 为 05-11/05-12）核验后续限制与任务扩展。v1 只有 Situation Puzzle、
  Math、Texas Hold'em 与 Trust Game；UI2Html 是后续 revision 新增，不回写成 W10 新事件。联读作者
  repository、四个任务目录与运行说明；repository 当前未提供 release/tag，也没有与 v4 对齐的 UI2Html
  目录，因此状态为 `Paper Verified / Code Partially Aligned With Revision`。
- **Full-read Coverage:** Verified；已检查 metadata、v1/v4 Abstract、Introduction、Related Work、统一
  formalization、Interactive Proofs/Games、四个 v1 task、v4 UI2Html、实验设置、static/pass@k baselines、
  judge ablation、成本讨论、Limitations、Conclusion、Appendix prompts/results，并核对官方 repository 的
  math、situation-puzzle、poker 与 trust-game artifact。没有把后续 revision 的结果伪装成首发证据。
- **Original Problem / Why Previous Evaluation Was Reasonable:** static benchmark 把 prompt 固定后只观察
  final answer，容易复现、便于横向比较，也能隔离 one-shot prior capability；pass@k 在独立采样近似成立时
  估计 candidate coverage。它们适合无反馈任务，却无法测量 Agent 是否会主动提问、吸收反馈、分配预算、
  适时停止或在对手策略变化时调整。因此旧评测不是失效，而是只回答不同问题。
- **Changed Constraint / Principle:** 当系统允许与 judge、tool、environment 或其他 Agent 循环交互时，
  被评估对象不再是 `model(prompt) -> answer`，而是
  `policy × observation/action interface × judge/environment × budget × stopping/retry rule`。能力分数必须绑定
  反馈带宽与协议；否则“模型更会交互”可能只是更适配某个 judge 的语义习惯、错误模式或泄露通道。
- **Mechanism / Formalization:** 在 horizon `T` 内，history 为
  `h_t=(o_1,a_1,...,o_t)`，策略按 history 选择 action。Interactive Proofs 让隐藏 ground truth 的 judge
  回答受限问题，在总预算 `B` 内最大化 final correctness；Interactive Games 则与动态环境或其他 policy
  交互，最大化累计回报。Situation Puzzle/Math 使用最多 20 轮的
  `{YES, NO, BOTH, IRRELEVANT}` 反馈与 final verdict；Poker 与 Trust Game 分别引入 opponent pool、游戏规则、
  retry/auto-fold 或随机 horizon；v4 UI2Html 每轮提交完整 HTML，再由问题反馈与模型 judge 评分。
- **State Ownership / Control and Data Flow:** dataset 拥有 hidden solution/rules；judge 拥有 observation
  mapping、答案等价或视觉评分；harness 拥有 transcript、turn budget、retry、termination 与 opponent pool；
  player policy 拥有 question/action/stop decision；provider 拥有实际 model endpoint。数据流为
  `hidden task -> observation -> player action -> judge/environment transition -> transcript -> next action/final ->
  scorer`。任何一层 revision 都会改变 measurement identity，transcript 不是附属日志，而是核心证据。
- **Artifact / Reproducibility Boundary:** 官方 code 默认调用 OpenRouter-compatible API；math 输出文件编码
  dataset、provider、player 与 judge，支持 resume，并以 naive/intersection token estimate 推导 pass@k；
  situation puzzle 当前还硬编码 OpenRouter base URL。repository 声称结果会在“可能时”保存复现 metadata，
  但没有冻结 provider snapshot、commit/release、完整 dependency image 或 API model revision。v4 的 UI2Html
  没有出现在公开 src 目录，故论文与 code revision 不能视作一个完整、可执行 artifact。
- **Evaluation Contract:** v1 puzzle 为 46 个 curated items、math 为 52 个 expert-selected HLE hard items；
  Poker 将六个 LLM 固定成桌内 players，10 tables 共 5,000 hands，invalid output 只重试一次后 auto-fold；
  Trust Game 是带 continuation probability 的 repeated Prisoner's Dilemma round-robin。v4 UI2Html 采用
  50 个 screenshots 与模型 judge/summarizer。API 模型、judge、温度、协议、opponent composition、seat、
  random horizon 与 sampling seed共同构成实验合同；hardware、cache、端到端 latency、concurrency、energy
  与 production SLO 没有形成可迁移合同。
- **What the Evidence Proves:** 在作者指定的 task、player/judge组合和协议下，一些模型能利用多轮反馈提高
  final success，且 static ranking 与 interactive ranking 可能不同；v4 judge ablation 也直接支持 judge identity
  会显著改变 UI2Html score。论文因此证明“反馈利用与信息获取策略值得独立测量”，不是证明某个模型拥有
  跨环境稳定的单一 interactive-intelligence 标量。
- **What It Does Not Prove / Threats:** player-token matching 不等于 compute/cost matching，因为 judge tokens、
  accumulated context、额外 API calls、latency 与 environment work 被省略，v4 Limitations 也承认这一点。
  judge 知道 ground truth并输出结构化反馈，既是 evaluator也是 information channel；natural-language judge
  对复合问题、equivalence 或视觉质量的映射仍可能出错或被策略利用。只在 solved subset统计 turns 会产生
  survivor bias。Poker/Trust Game score受 opponent pool、seat、随机性和规则条件约束，不能当作绝对能力。
  temperature 0与可变 API endpoint也不保证跨 provider revision确定性；有限 curated set存在 contamination、
  domain-skill entanglement和模型漂移风险。
- **Trade-offs / New Failure Modes:** 交互评估观察到 question policy、feedback use 与 stopping，却增加
  judge dependence、调用成本、状态空间、路径依赖和复现难度；受限 feedback便于控制，也会压缩真实工具语义。
  更大 turn budget可能提高成功率，同时鼓励无效试探或 benchmark-specific exploitation。模型可能靠 domain
  prior直接解题，也可能很会提问但基础能力不足；只看最终 reward无法区分 prior capability、information
  acquisition、update quality、stop discipline 与 judge exploitation。
- **Where Previous Designs Still Apply:** static exact/executable evaluation仍适合确定性 correctness、低成本
  regression与 one-shot capability；pass@k仍适合衡量生成覆盖率；human review适合 judge语义不稳定或高风险
  task；interactive benchmark适合工具/反馈实际属于 deployment contract 的 Agent。生产 gate应同时保留
  outcome、trajectory、cost和policy-violation指标，而非用交互分数覆盖静态证据。
- **Evolution Relationship:** `Direct Evolution`：static answer -> repeated independent samples ->
  feedback-conditioned trajectory。`Layering / Dependency`：base/domain capability -> information acquisition ->
  feedback update -> stopping/action -> executable/environment outcome。下一阶段压力不是继续堆 turn数，而是
  分解 credit、冻结 environment identity、加入 cost/SLO与 adversarial judge，并提供可回放 transcript。
- **ROADMAP / Chapters Read:** 主 owner确认为 Ch62 Evaluation System；已完整阅读 Ch61～63，并联读
  Ch74～76。Ch62已经覆盖 evaluation subject、environment、trajectory、judge和成本，但还缺“信息获取策略”
  作为独立被评估状态，以及 static/pass@k/interactive 三者各自回答什么问题的演进边界。Ch74/75/76分别只
  handoff action interface、budgeted plan与feedback update，不重复承载 measurement contract。
- **Integration Decision:** `Refine — Existing Argument / Ch62 Integrated / Experimental`。Ch62 已补入 active
  information acquisition、feedback-channel identity、stopping 与 player+judge+environment cost contract；
  正文未写模型排行榜、通用百分比，也未把作者 judge 称为客观 oracle。
- **Open Questions:** 如何用 matched player+judge token/FLOPs/latency/cost预算公平比较 static、pass@k与
  interactive policy？如何拆分基础能力、提问质量、反馈吸收、停止策略和 judge exploitation 的 credit？
  opponent pool、API endpoint或 judge更新时，如何判断 score变化来自模型还是 environment drift？

### MASQuant：多模态量化把“一个 scale”演化为带条件状态的执行路径

- **Candidate / Week / Score:** MASQuant / 2026-W10 / 23/30；评分维度重新核为
  `TN 4 / SI 4 / PV 4 / SR 3 / PR 4 / L 4`，总分不变；
  `Source Family ID: masquant-modality-conditioned-ptq`。Source Reliability 从4降至3，是因为论文与代码虽公开，
  但 repository 没有 release/tag、论文没有完整复现合同，README 与 root license 及作者/citation metadata 也
  存在不一致；Longevity 从3升至4，因为“共享低精度基准路径 + 条件修正路径”的设计问题不依赖单一版本。
- **Source Type / Date / Revision History:** arXiv v1（2026-03-05，当前唯一版本；CVPR 2026）、完整 HTML/PDF、
  Alibaba `EfficientAI/masquant` 官方实现、README、calibration/inference entrypoint 与 low-rank decomposition/
  quantized-module code。历史事件冻结在 v1 日期；当前 `main` code 只用于验证 artifact 边界，不反写为新的
  W10 event。repository 当前无独立 MASQuant release 或 immutable artifact bundle。
- **Full-read Coverage:** Verified；已检查 metadata、Abstract、Introduction、Related Work、PTQ 与 whitening
  preliminaries、MAS/CMC 公式与两项 theorem/proof、双模态/三模态实验、全部 tables/figures/ablations、kernel
  性能、Conclusion 与 References；论文没有独立 Limitations/Threats section。代码侧核对 activation-scale
  generation、128-sample examples、两轮 scale optimization、`split_scales`、text/vision/audio scale state、
  whitening calibration type、rank、base-weight quantization、per-modality low-rank adapter build/load 与 model-
  specific replacement path。公开 repository 未定位到论文所称基于 Nunchaku 的完整 fused CUDA kernel artifact，
  因而 kernel 数字只能按论文作者实验处理。
- **Original Problem / Why Previous Design Was Reasonable:** text-only PTQ 的 channel-wise smoothing 用一个对角
  scale `S` 在 activation 与 weight 间搬移 outlier：`XW=(XS^-1)(SW)`。同一层共享同一权重、同一 tensor
  semantics，artifact 与 kernel 简单；只要 calibration distribution 近似单峰或各 token family 的 channel range
  相近，这个方案合理。多模态 decoder 继续共享 projection weights，但 vision、audio、text token 在同一 channel
  的 range 可相差一个或两个数量级；用混合样本的最大范围求统一 scale 时，dominant modality 会控制 scale，
  minority modality 的有效信号可能被过度平滑。旧方案没有错误，而是它隐含的“同一层只有一个稳定 activation
  distribution”约束被打破。
- **Changed Constraint / Principle:** 约束从“所有 token 共享权重”扩展为“共享权重但输入分布由 modality 条件化”。
  直接为每个 modality 保存 `Q(S_m W)` 可恢复各自量化质量，却复制大权重并破坏 quantization 的 memory 目标。
  因此系统需要分离两类状态：所有 token 共用的低精度 base representation，以及只在特定 token family 出现时
  执行的小型 correction。核心原则不是“多模态一定低秩”，而是先把共享部分与条件 residual 分离，再验证该
  residual 在指定 calibration metric 下是否可低秩近似。
- **Mechanism:** MAS 为每个 modality 学习 diagonal `S_m`，最小化加权的 modality-specific reconstruction MAE。
  CMC 选择 text 为 base，只保存 `Q(S_text W)`；对 vision/audio 计算
  `DeltaW_m = S_m W - Q(S_text W)`。它用 `X_m S_m^-1` 的 covariance 构造 whitening transform `T_m`，对
  `T_m DeltaW_m` 做 rank-`r` truncated SVD，再反变换得到 `L1_m L2_m`。text token 走低精度 base path；
  非 text token 走同一 base path并加上 `X_m S_m^-1 L1_m L2_m`。选择 text 不是普适语义优先级，而是把
  correction 从作者的 autoregressive text decode 移到 multimodal prefill。
- **Theory Boundary:** Theorem 2 证明的是：在给定 calibration activations、whitening 可用、两模态且仅
  weight-only quantization 的推导中，truncated SVD 对受限 rank-`r` reconstruction objective 最优；它没有证明
  任意 cross-modal difference 天生低秩。低 effective rank 是 Qwen2.5-VL/Omni-3B 上的经验观察，W4A8、三模态
  与其他模型的成立性来自实验而非该 theorem。Theorem 1 在 activation error 近似均匀、range ratio 很大且
  normalized channel activation近似一致时比较 SQNR upper bounds；HTML 公式还存在缺字符，不能把它写成对
  任意 token/distribution 的精确 degradation law。
- **State Ownership / Control and Data Flow:** source model revision 与 target modules 属于 model artifact；
  modality-labeled calibration set、sample count、sequence construction和split属于 data/evidence state；`S_m`、
  base modality、shared quantized weights、per-layer whitening matrices、rank与`L1/L2`属于 numerical/graph
  artifact；runtime/model wrapper拥有 token-modality mask与conditional branch；kernel/backend/hardware拥有实际
  execution capability。数据流为 `labeled calibration -> per-modality activation statistics -> learn S_m -> choose
  base -> whiten residual -> truncated SVD -> package base weight + corrections -> runtime token mask -> base GEMM
  + conditional correction -> modality-sliced evaluation`。少任何一层，只有“4-bit weights”不能重建已验证行为。
- **Implementation / Artifact Boundary:** README examples对 Qwen2.5-VL/Omni 使用128个 calibration samples、
  两个 scale-training epochs，并把 CMC 的 `rank`、`n_cali_samples` 与 `cali_data_type`作为单独参数；code保存
  text/vision/audio scales、whitening matrices和每模态 low-rank adapters，再交给 model-specific quantized
  replacement。`infer_mas.py` 默认 whitening sample数与README示例不同，且依赖 environment/config path；
  artifact lineage必须记录实际 run config，不能从默认值推断论文结果。README声称 MiniCPM-V支持与约2% FLOPs
  overhead，但论文主表只覆盖 Qwen2.5 family，后者没有形成完整 workload contract。
- **Evaluation Contract:** 论文量化 Qwen2.5-VL 3B/7B 与 Qwen2.5-Omni 3B/7B 的 language-model/Thinker
  component，比较 RTN、AWQ、SmoothQuant、MBQ，覆盖 W4A16、W8A8、W4A8、W4A6。audio 用 LibriSpeech
  `test-other`和 WenetSpeech `test-net` WER；vision用 OCRBench、TextVQA、VizWiz、ScienceQA、MMMU；
  tri-modal用 OmniBench。论文没有披露完整 calibration composition、seed/replicates、置信区间、software image、
  所有模型的运行硬件或服务 SLO。性能实验只报告 Qwen2.5-VL-7B、Desktop RTX 4090、sequence length 2048、
  W4A4、prefill、batch 1/8 与 rank ratio 0.01/0.02/0.05；未披露视觉/文本 token mix、输出长度、并发、TTFT/
  TPOT/tail、功耗或 fallback。
- **What the Evidence Proves:** 在作者四个 Qwen checkpoint、指定 benchmark 与 PTQ 配方下，统一 smoothing
  在激进 activation quantization 时可能严重伤害非 dominant modality；per-modality scales 与 whitened low-rank
  correction在这些设置中显著恢复质量。尤其 Qwen2.5-Omni-3B W4A8 的 SmoothQuant 在作者表中由 dense
  3.9/7.5 WER退化到77.4/94.2，而 MASQuant 为3.6/8.7；该数字只能作为 model/config-bound failure case。
  4090表还证明作者特定 fused path 在单一 prefill contract 下相对 FP16 有加速，并相对 MBQ付出约5～10%
  latency overhead；它没有证明 production serving 的通用收益。
- **What It Does Not Prove / Threats:** 主表的平均分会隐藏 task-level regression；MASQuant并非每一任务都最优，
  也没有与 rotation、mixed precision、QAT或更广 MLLM做 matched-budget comparison。论文称“decode latency
  identical”只适用于 text-base且输出 token 为 text 的路径；生成 audio/image、interleaved output或非 text base
  会重新引入 correction。离散 modality label假设 token family可可靠识别，不能自动覆盖融合 token、code-
  switching、continuous mixtures与 deployment drift。paper theorem没有覆盖三模态 activation quantization；
  official code、paper kernel与current repository也未形成一次可直接重放的 end-to-end release。
- **Trade-offs / New Failure Modes:** 获得 minority-modality signal preservation、单份低精度大权重与条件开销；
  付出 modality-aware calibration、更多 scales/whitening/correction state、rank选择、model-specific graph rewrite、
  mask routing与额外 prefill compute/memory。calibration偏置会把 minority modality修正到错误方向；covariance
  whitening可能数值不稳；rank太小产生 approximation error，太大吞掉量化收益；mask错误让 token走错 scale/
  branch；base modality选择会把成本转移到不同 phase；新增 modality或 distribution drift要求重建和重新验证
  artifact。统一 smoothing在单模态、分布相近、memory/implementation simplicity优先或 correction kernel不成熟时
  仍然成立；为每模态保存完整权重在模型很小、modality很少且隔离比内存更重要时也可能合理。
- **Evolution Relationship:** `Direct Evolution`：uniform channel smoothing -> modality-balanced loss但仍共享
  scale -> independent modality smoothing -> duplicated modality weights -> shared quantized base + conditional low-rank
  correction。`Layering / Dependency`：calibration/data contract -> numerical representation -> graph/mask semantics ->
  fused kernel -> modality-sliced quality与 serving SLO。下一阶段压力是自动 rank/base selection、连续或未知模态、
  drift detection、portable kernels和 artifact-level rollback，而不是把一个静态 4-bit 文件当成完整方案。
- **ROADMAP / Chapters Read / Existing Coverage:** 初筛 Ch17/27 不成立：Ch17拥有 Transformer block语义，Ch27
  属于 RLHF，均不应承载 deployment quantization。已完整阅读 Ch16～18、Ch23、Ch31、Ch44～46；主owner修正
  为 Ch45 的量化 execution plan，Ch31 handoff保存 numerical/graph/execution/evidence contract，Ch23 handoff
  calibration distribution与modality label provenance。Ch31/45已有 low-rank correction、fusion与artifact contract，
  但尚缺“一个 shared weight对应多个条件 activation distributions”、base/correction path选择和 modality-mask
  failure semantics；这是对现有论点的机制性 refine，不是新增论文笔记。
- **Integration Decision:** `Refine — Existing Argument / Ch45 Integrated / Experimental`。Ch45 已补入
  distribution-conditioned scales、shared base + conditional correction、mask routing、base-family cost
  placement 与 modality-sliced deployment contract。Ch31/23 不重复写入；正文未保留 benchmark、MiniCPM
  claim，也未把“天然低秩”或“decode 零开销”写成通用事实。
- **Open Questions:** production artifact怎样编码 token-family classifier/mask、base modality、per-modality scales、
  correction rank与fallback？未知/混合 modality如何避免 silent misrouting？calibration drift触发 scale refresh还是
  rollback，怎样做 per-modality canary？在 matched TTFT/TPOT/tail/quality/cost下，低秩 correction何时优于更高
  bit width、mixed precision或完整 modality-specific weights？

### GPT-5.4 + system card

- **Candidate / Week / Score:** GPT-5.4 + system card / 2026-W10 / 23/30；
  `Source Family ID: openai-gpt54-model-system-card`。
- **Source Type / Date / Revision History:** OpenAI official release、完整 Deployment Safety Hub system card 与
  PDF入口，首发均为2026-03-05。当前 card包含2026-03-17追加的mini appendix和2026-04-24更新的CoT
  monitorability section；它们用于辨认revision drift，不作为W10新事件，也不把mini结果合并进GPT-5.4 Thinking
  首发结论。release、ChatGPT/Codex surface、API model与system-card checkpoint名称并不完全相同，必须分别
  保存 identity。
- **Full-read Coverage:** Verified；已检查发布范围、professional/coding/vision/computer-use/tool-search/
  tool-calling/web-search与long-context评测、全部公开footnotes、availability/pricing；system card侧检查training
  disclosure、challenging/representative/dynamic safety eval、jailbreak、prompt injection、vision/health、destructive
  action、computer-use confirmation、bias、CoT monitorability/controllability、Bio/Chem/Cyber/AI self-improvement
  Preparedness assessments、external evaluations、cyber threat model、conversation monitor、actor enforcement、
  trusted access、security controls、internal deployment与revision appendix。weights、architecture、参数量、完整
  training recipe/data mix、训练硬件、serving topology、KV/runtime implementation均为`Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable:** 先前通用模型可把全部工具schema放入prompt，或由
  应用固定暴露少量tools；对小catalog这让模型一次看到完整接口，选择简单且易于cache/evaluate。随着connector/
  MCP catalog扩大，完整schema会消耗context、破坏prefix cache并扩大prompt-injection/selection surface；同时
  computer use把“输出文本”升级为跨应用的真实动作，使单一模型内confirmation policy难以适配不同platform/
  developer risk tolerance。旧方案在少量稳定工具、固定权限和低风险任务中仍合理。
- **Disclosed Mechanism / Mechanism Not Disclosed Boundary:** release披露了interface-level机制：tool search只先
  给轻量catalog，在需要时检索并把完整definition追加到conversation；computer use可通过screenshot坐标或代码
  驱动，并让system/developer message携带confirmation policy。system card披露deployment safety stack包含模型
  training、policy、两级conversation monitor、actor-level enforcement、trusted access与security controls。
  这些能证明tool discovery和policy placement，不证明模型内部存在何种planner、memory、router、视觉encoder、
  training curriculum或runtime scheduling。厂商把coding capability“incorporates”进mainline model也不能反推
  architecture merge方式。
- **State Ownership / Control and Data Flow:** provider拥有checkpoint/API revision、reasoning effort和hidden
  training；product/API surface拥有context limit、image detail、tool-search/computer interface与pricing；developer/
  platform拥有authorized tool catalog、confirmation policy、principal与executor；harness拥有environment、tool
  implementation、turn/yield budget、prompt/grader与network state；safety service拥有policy taxonomy、monitor/
  classifier revision、account/actor state与enforcement threshold。数据流应写为 `authorized lightweight catalog ->
  model search request -> schema retrieval -> model action proposal -> confirmation/authorization -> executor ->
  observation -> next turn -> model/harness/safety outcome`，而不是`GPT-5.4会使用工具`这一黑盒句子。
- **Evaluation Contract:** release默认多数eval为`xhigh` reasoning，个别使用none；GDPval、SWE-Bench Pro、
  OSWorld、Toolathlon、BrowseComp、MCP Atlas等分别采用不同artifact、tool/search environment与grader。MCP Atlas
  的47% token reduction只绑定250 tasks、36 MCP servers和“all schemas vs tool search”两种作者配置；BrowseComp
  明确承认新旧模型测试日期、search system、互联网状态和blocklist均变化，不能作纯model causal attribution。
  coding latency来自offline simulation，包含tool execution、sampled/input tokens且官方说明真实值可能显著不同。
  long-context表在256K～1M明显下降，故“支持1M”是interface capacity，不是整段可靠利用保证。
- **Safety Evaluation Boundary:** challenging benchmarks故意富集历史failure，error rate不代表production prevalence；
  representative-traffic estimate用GPT-5.2流量重采GPT-5.4 final turn，只测model-level output且受traffic/eval pipeline
  drift影响；dynamic safety eval按任一assistant turn是否违规统计，与static final-response metric不同。prompt-
  injection sets来自training splits，不测新攻击泛化。HealthBench有长度差异且部分指标回退；CoT monitorability的
  低TPR/TNR样本、monitor/grader mismatch与短trace confound被card明确承认。Preparedness eval被官方定义为
  capability lower bound，Bio/Chem和Cyber的`High`是holistic deployment classification，不是单一benchmark分数。
- **What the Evidence Proves:** 官方材料证明2026-03-05发布了特定产品/API model family、tool-search与computer-
  use接口，并公开了受限evaluation和defense-in-depth deployment posture；也证明安全证据本身是由checkpoint、
  elicitation、harness、policy、monitor、traffic slice与product controls共同构成。它为Ch74的“catalog retrieval再
  schema exposure”和Ch68的“model proposal不等于authority”提供版本案例，但没有提供新的长期第一性机制。
- **What It Does Not Prove / Threats:** vendor-reported leaderboard不能证明跨provider、硬件、价格、latency或
  production workload通用领先；partner quotes/internal eval不是独立复现。1M context、native computer use和更少
  tokens不能推出内部architecture或所有长任务更可靠。low CoT controllability是指定surface task与长度下的proxy，
  不是CoT faithful或monitoring永远有效。没有公开weights、training/system/runtime internals，不能将版本行为写成
  AI System design事实；card后续revision也说明“system card”本身是mutable evidence artifact。
- **Trade-offs / New Failure Modes:** deferred schema exposure降低context与cache成本，却新增catalog retrieval
  miss、tool-version drift、authorization filtering、schema injection和额外round trip；computer use扩大UI覆盖，
  同时引入视觉误定位、不可幂等副作用、confirmation fatigue与environment drift。可配置confirmation提高场景
  适配，但policy在system/developer message中传播会新增version、precedence、prompt integrity和fallback问题。
  defense-in-depth降低单点失效，却增加false positives、ZDR/non-ZDR差异、actor attribution、appeal与monitor drift。
  小模型/固定toolset/typed API在低延迟、确定性和高可审计场景仍成立，不能被frontier computer-use覆盖。
- **Evolution Relationship:** `Layering / Dependency`：larger model capability并不替代tool catalog、executor、
  authorization或monitor。工具侧是`Direct Evolution`：all schemas in context -> authorized catalog shortlist/search ->
  on-demand schema exposure -> typed proposal/execution。安全侧是model policy -> configurable confirmation policy ->
  model + conversation monitor + actor enforcement + trusted access。该演进增加了明确state owner，也增加了catalog、
  policy、monitor与account-level failure semantics。
- **ROADMAP / Chapters Read / Existing Coverage:** 已完整阅读Ch19～21、Ch61～63、Ch67～69与Ch73～75。
  Ch74已经明确写出`authorized tool catalog retrieval -> shortlist -> schema exposure -> model choice`，并把proposal、
  authorization、confirmation、idempotency和observation trust分离；Ch68已经把模型output定位为untrusted proposal，
  用least privilege、policy/executor、audit和defense-in-depth承载安全；Ch62已有subject/environment/scorer/decision
  contract。官方材料没有改变这些设计结论，也没有公开足够内部机制填补章节缺口。
- **Integration Decision:** `Full Review Complete — No Change / Weekly Only — Version/Product Fact / Mechanism
  Not Disclosed`。不修改Books；不是因为版本不重要，而是可沉淀机制已经逐项存在，新增内容只会复制产品名、
  benchmark和mutable deployment facts。后续若官方公开tool-search routing、computer-use training/runtime或monitor
  false-negative机制，作为同一source family重新判断。
- **Open Questions:** system card如何发布可机器比较的checkpoint、product surface、prompt/policy、harness、
  evaluator、monitor与revision manifest？catalog retrieval miss、schema poisoning、confirmation bypass和actor-
  enforcement false positive怎样进入统一release gate？后续card更新如何区分evidence correction与model change？

### Labor-market impact measurement

- **Candidate / Week / Score:** Labor-market impacts / 2026-W10 / 22/30；
  `Source Family ID: anthropic-observed-exposure-labor`。
- **Source Type / Date / Revision History:** Anthropic official research article、11页方法Appendix与PDF入口，
  2026-03-05；页面在2026-03-08明确记录Figure 7把top-quartile与zero-exposure inflow labels反转的correction。
  联读页面引用的O*NET task structure、前两期Economic Index usage window、Eloundou theoretical exposure、CPS/
  DOL UI data与occupation crosswalk说明。后续Economic Index只用于确认该metric继续演进，不回写为W10结果。
- **Full-read Coverage:** Verified；已检查counterfactual framing、三类输入源、task gate、work/API/automation
  weighting、time-fraction aggregation、shared/similar task allocation、occupation/worker mapping、BLS projection
  correlation、CPS unemployment与young-worker job-finding DID、detectable-effect discussion、cutoff sensitivity、
  22～25岁slice、DOL insured-unemployment robustness、task-granularity alternatives、measure-correlation matrix、
  数据imputation/threshold footnotes、Discussion、References与correction history。公开材料没有提供可独立执行的
  data/code release，private Claude traffic和部分classifier state不可复现。
- **Original Problem / Why Previous Design Was Reasonable:** theoretical exposure把O*NET task交给专家/模型判断
  “LLM或LLM+tools能否让任务至少快一倍”，适合描绘capability upper bound，且不依赖某一家产品当下adoption。
  但它会把技术上可行、真实被使用、在work context使用、augmentation、automation与最终labor outcome混成一层。
  当扩散受法律、软件集成、验证、组织流程和模型可靠性约束时，capability上界不等于deployment treatment。
  理论指标仍适合回答“可能覆盖哪里”，不能被observed measure否定。
- **Changed Constraint / Metric Mechanism:** observed exposure只把理论可行且在Claude样本中达到usage gate的task
  计入；Claude.ai只保留work-related usage，1P API全部作为更接近workflow integration的signal；automation share
  将task权重从纯augmentation的0.5推向automation的1。task value再按该task占occupation时间份额聚合。Appendix
  的hard gate是至少100次或约总样本0.0025%；低于阈值直接置0。高度相似/跨occupation共享task因缺少上下文，
  按employment share分配。该指标因此是“presence × deployment mode × task-time”的proxy，不是工作量百分比或
  causal displacement probability。
- **State Ownership / Control and Data Flow:** O*NET拥有occupation/task taxonomy；Eloundou study拥有early-2023
  capability labels；Anthropic sampler/classifiers拥有Claude.ai/API work-use、task match、automation/augmentation和
  privacy threshold；time-fraction estimate拥有task importance；crosswalk把O*NET-SOC映射到CPS occupation code；
  CPS/DOL/BLS分别拥有worker outcome、insured unemployment与forecast。数据流为 `theoretical task feasibility +
  sampled provider usage -> privacy/frequency gate -> work/API/automation weight -> time-weighted occupation exposure ->
  occupation crosswalk -> treatment/control slices -> unemployment/hiring outcome -> DID/robustness -> corrected report`。
  任一taxonomy、provider mix、classifier或crosswalk revision都会改变metric identity。
- **Sampling / Measurement Boundary:** exposure只使用2025年8月和11月的两期Economic Index样本；Appendix说明
  总体约含2M Claude.ai和2M first-party API observations。August缺use-case primitive，work share由September task
  embedding model impute。API traffic不区分personal/work；rare tasks会被privacy/frequency gate记为0；usage count
  不测同一task adoption的intensive margin。raw usage、success-gated、ridge-imputed、DWA/IWA aggregation与不同
  weighting的rank correlation较高，说明occupation排序对部分选择稳健，却不证明绝对exposure值或causal effect稳健。
- **Outcome / Counterfactual Contract:** 主分析把top quartile exposure workers与约30% zero-exposure workers比较，
  用ChatGPT release前后三类CPS outcome做DID。两组在人口、education、income和COVID sensitivity上显著不同；
  parallel-trend与“影响先在最高mean exposure出现”是设计假设。报告另改变treated percentile、检查22～25岁并用
  DOL insured-unemployment的coarse SOC/state-quarter数据复核。作者估计当前设计大致能识别约1 percentage-point
  differential unemployment increase；它看不见所有occupation同时变化、labor-force exit、job quality/wage、firm-
  level adoption、task complementarity或worker转岗全过程。
- **What the Evidence Proves:** 在该provider-specific usage、taxonomy、crosswalk和early labor window下，observed
  exposure远低于theoretical upper bound；它与BLS较低growth projection有弱相关。CPS/DOL分析未检测到high-
  exposure group相对control的系统性unemployment increase。22～25岁进入high-exposure occupations的job-finding
  rate在2024后相对下降，post-ChatGPT平均估计约14%，但只barely statistically significant，且可由继续原工作、
  转向其他occupation、返校或survey transition mismeasurement解释。这是early signal，不是displacement因果证明。
- **Correction / Claim Boundary:** 2026-03-08的Figure 7 label reversal没有被隐藏，反而说明report figure、underlying
  series、caption与narrative必须有独立revision lineage。当前结论不能写成“AI没有影响就业”，因为null estimate受
  power、treatment proxy、时间窗与shared shocks限制；也不能写成“AI已阻断年轻人就业”，因为单一marginal finding
  弱、alternative channels多且没有firm/worker adoption link。BLS projection相关也不是实际employment outcome或
  external validation的充分条件。
- **Trade-offs / New Failure Modes:** observed usage比capability score更接近deployment，却引入single-provider/
  product/customer selection、API work assumption、classifier/crosswalk error、privacy threshold censoring、taxonomy
  granularity与feedback loop：高adoption occupation更易被observed，低employment/rare tasks更易被记0。更细task
  保留语义但稀疏，更粗DWA/IWA提高coverage却合并不同工作；hard gate降噪也系统性低估long tail。time-fraction
  aggregation忽略task dependency：在O-ring workflow中，少数不可自动化task可阻止job-level displacement；相反，
  一个bottleneck task自动化也可能重构整份工作。theoretical、observed、firm adoption与outcome measure应并存。
- **Evolution Relationship:** `Direct Evolution` within measurement：benchmark/theoretical capability -> observed
  task usage -> work/automation-weighted occupational exposure -> longitudinal worker/firm outcomes。`Layering /
  Dependency`：capability frontier不是adoption，adoption不是automation，automation不是employment outcome，
  correlation不是counterfactual effect。下一阶段需要multi-provider/firm-linked panel、worker transitions、wage/job-
  quality、task complementarity与pre-registered correction/version protocol，而不是用一个exposure标量覆盖整条链。
- **ROADMAP / Chapters Read / Existing Coverage:** 已完整阅读Ch61～65。主owner为Ch62 Evaluation System，Ch63
  只承接provider telemetry sampling，Ch64/65承接correction/lineage和operation-level evidence。Ch62已明确任何分数
  都绑定subject/distribution/scorer、online feedback非随机、更多样本不能修复错误分布、slice/uncertainty、online
  observation不等于causal conclusion，并要求new version不覆盖旧evidence；Ch63也已把single-provider interaction
  metric限定为deployment-system observation。该研究是高质量案例，但没有补出AI System章节的新机制。
- **Integration Decision:** `Full Review Complete — No Change — Already Covered / Weekly Only`。不把宏观labor
  finding写入Books核心，因为本书owner是AI System evidence contract，不是劳动经济学；也不复制provider-specific
  exposure公式。Weekly保留完整measurement evolution、correction与因果边界，作为未来在线观测转业务结论的反例。
- **Open Questions:** multi-provider、on-prem和firm workflow telemetry怎样在隐私边界下组成representative adoption
  panel？如何把task dependency、remaining expertise、quality/wage与worker transition接入outcome graph？taxonomy/
  classifier/crosswalk/revision改变时，怎样用backfill和parallel version区分metric drift与真实经济变化？

### WAXAL speech resource

- **Candidate / Week / Score:** WAXAL / 2026-W10 / 20/30；轴向由旧版
  `3/2/4/4/3/4` 修正为 `3/2/4/3/4/4`；`Source Family ID: waxal-african-speech-resource`。Project
  Relevance 提升，因为采集协议、partition license 与 mutable dataset identity 是 Ch23 的直接问题；Source
  Reliability 下调，因为同一官方 source family 的规模与许可叙述互相冲突。
- **Source Type / Event Date / First-public / Revision:** W10 事件是 Google Research 2026-03-06 官方发布页与
  dataset expansion；论文 v1 首发于 2026-02-02，v2 为 2026-02-04，W10 内 v3 为 2026-03-02。论文家族
  first-public date 归属 W06，不把 v3/blog 当作一篇新论文；W10 只记录 official release 与 artifact state。
- **Direct / Related Primary Sources:** 已阅读全文 arXiv v1 与 v3，核对 abstract metadata/revision history、
  Google Research release、Hugging Face `google/WaxalNLP` dataset card v2.0.0、公开 configurations、row schema、
  split 与 provider-specific license。论文没有 Appendix、模型实现、baseline、ablation 或模型性能实验；Blog
  链接的衍生研究不替代本候选自身的 evidence。
- **Access and Verification / Full-read Coverage:** `Verified with conflicting official artifacts`。已覆盖
  Introduction、Related Work、collection methodology、ASR/TTS flow、statistics、limitations、ethical
  considerations 与当前 dataset artifact。未公开 QC threshold、annotator agreement、speaker sampling frame、
  split assignment algorithm、speaker-disjoint proof、consent form、deletion procedure 或 model evaluation。
- **Original Problem / Why Previous Design Was Reasonable:** 既有高资源、多语言或 scripted speech corpora
  适合复用统一 representation、标准化采集并降低单位数据成本；但对低资源非洲语言，它们可能缺少足够的
  speaker、dialect、code-switching、tonal variation 与真实 acoustic environment。这里的边界不是“数据量不够”
  一个标量，而是 collection protocol 没有产生目标 deployment distribution。
- **Changed Constraint / Principle:** ASR 与 TTS 需要不同的 source distribution。ASR 要覆盖多 speaker、自然
  环境和 spontaneous speech；TTS 要控制 script、speaker 与 acoustic fidelity。长期原则是：**collection
  protocol 先于 filtering 定义样本为何存在，因而也是训练分布 specification 的一部分。**同一语言标签下的
  elicitation task、speaker pool、recording environment 与 transcription policy 不同，会形成不同的 `q(x)`。
- **Mechanism / State Ownership / Control and Data Flow:** ASR 路径为 `50+ topic image prompt -> 至少 15 秒自然
  描述 -> 约 10% audio 由单个本地语言专家转写 -> clarity/language/relevance/content QC 与 PII removal ->
  labeled 80/10/10 + unlabeled partitions`；TTS 路径为 `phonetic script -> contracted community voice actor ->
  studio-like recording -> segmentation/text alignment/QC -> train/validation/test partitions`。African partner
  organizations拥有所采数据，Google 提供资助与技术指导；真正可执行的使用权限由 provider/language partition
  持有，不能只由顶层 dataset name 决定。
- **Implementation / Public Schema Boundary:** 论文称 ASR 有 age、gender、language 与 recording-environment
  attributes，当前公开 row schema只稳定暴露 `speaker_id/transcription/language/gender/audio`；TTS 暴露
  `speaker_id/text/locale/gender/audio`。未暴露字段不能从论文图表反推为每行可用 metadata。Dataset card给出
  80/10/10 labeled split，却没有证明 speaker-disjoint；若同一 speaker 跨 train/test，评估可能测到 speaker
  overlap，而不是对新 speaker 的泛化。
- **Artifact / License Lineage Conflict:** W10 v3 abstract为 24 languages、约 1,250h ASR、约 235h TTS，正文
  contribution 又写 TTS `over 180h`；2026-03-06 Blog称 27 languages、约 1,846h/565h；当前 v2.0.0 card称
  19 ASR languages、约 1,250h，以及17 TTS languages、`over 180h`。论文与 Blog 均概括为 CC-BY-4.0，
  当前 card却把 University of Ghana partitions列为 CC-BY-4.0，其余多家 partitions列为 CC-BY-SA-4.0，
  并明确要求按语言检查许可。以上数字只能绑定各自 artifact/version；不能合并成一个“当前规模”，也不能把
  顶层 permissive-license 宣称当作 partition-level authorization。
- **Evaluation Contract / What Evidence Proves:** 这组材料证明一种 community-partnered、task-specific speech
  acquisition pipeline 被公开，以及 dataset 的 declared composition、schema、split 与 limitations；它没有训练或
  比较任何 ASR/TTS model，没有 baseline、ablation、CER/WER/MOS、hardware、precision、batch、latency、SLO 或
  downstream adoption evidence。因此不能声称 image prompting 已在 WAXAL 内因果优于 scripted collection，不能
  由 corpus size推出模型 quality，也不能由 ASR+TTS 两类数据推出 full-duplex product readiness。
- **Limitations / Threats / New Failure Modes:** 只有约10% collected ASR audio被转写；单 annotator缺少公开
  agreement；语言内部 dialect/socio-linguistic coverage不完整；unscripted speech可能含不当内容；voice identity
  不能靠删除 transcript PII消除，accent/language仍可泄露敏感属性。扩大 coverage同时增加 consent scope、voice
  misuse、license inheritance、partner ownership、correction/deletion传播、schema drift与跨版本不可比问题。
- **Where Previous Design Still Applies / Trade-offs:** Scripted read speech仍适合 TTS、pronunciation coverage与
  controlled acoustic quality；自然环境 elicitation更适合 spontaneous ASR但更难转写、QC和复现；大型通用
  multilingual corpus仍可提供 shared representation，但不能替代按目标语言、dialect、speaker与环境做的 local
  validation。新方案不是替代旧方案，而是按 task contract 分叉 acquisition path。
- **Evolution Relationship:** `Direct Evolution`：read/scraped generic corpus -> active elicitation of natural speech
  -> task-specific ASR/TTS acquisition -> partner-owned partitions with per-partition policy。`Layering / Dependency`：
  collection protocol -> artifact/version/license manifest -> train/eval split -> model evaluation；后一层不能修复前一层
  未采集的人群或环境。下一阶段压力是 speaker-disjoint split、dialect/acoustic slices、consent withdrawal、voice-
  misuse controls 与 machine-readable partition lineage。
- **ROADMAP / Chapters Read / Existing Coverage:** 已完整阅读 Ch22～24，并检查 Ch11 tokenizer boundary 与 Ch62
  dataset-governance/evaluation contract。主 owner 为 Ch23。Ch23已有 source/license/provenance、immutable manifest、
  mixture与coverage原则，但主要从“已有 raw sources 如何过滤”开始，尚未明确 **active collection protocol 与
  partition-level license/consent 本身定义 dataset semantics**；Ch11不应承接采集治理，Ch62只承接 speaker/language/
  acoustic slice 与 split identity。
- **Integration Decision:** `Refine — Existing Argument / Ch23 Integrated`。已在 Ch23 将既有“data is
  specification”前移到 acquisition：补入 `acquisition objective -> collection protocol -> partition policy ->
  split/evaluation`、group-disjoint split 与 mutable-artifact conflict handling。正文不保留 WAXAL规模数字、
  版本列表或“更好”效果，Ch11/62无需重复修改。
- **Open Questions:** WAXAL的19/24/27 language与180/235/565h口径分别对应哪些 immutable manifests？公开 split
  是否 speaker-disjoint？consent是否覆盖商业 voice cloning、能否撤回、撤回后怎样传播到 derivatives/checkpoints？
  card、paper与Blog冲突由谁负责 correction/supersession，consumer怎样机器判定当前有效 contract？

### Multi-Head Low-Rank Attention：架构压缩必须同时满足并行可分片性

- **Candidate / Week / Score:** Multi-Head Low-Rank Attention（MLRA）/ 2026-W10 / 27/30；
  `Source Family ID: mlra-shardable-latent-kv`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-02 首次公开且当前仅一个版本；已阅读完整
  HTML、全部实验与 Appendix，并核对作者 repository、公开模型权重与训练数据说明。
- **Full-read Coverage:** `Verified`。覆盖 Abstract、Introduction、MLA/GQA background、Method、初始化/
  variance scaling、Training、Inference benchmark、PPL/zero-shot evaluation、ablation、Conclusion 与 Appendix。
- **Original Problem / Why Previous Design Was Reasonable:** MLA 把所有 KV heads 压入一个共享 latent state，
  在单卡或低并行度下能显著减少 KV Cache 与读带宽；但单一 latent head 不是天然可分片维度。Tensor
  Parallel 增大时，每个 rank 仍需读取完整 latent KV，故 per-device cache traffic 不随 TP degree 等比例下降。
  旧设计不是错误，而是优化目标主要是总 cache size；新约束把 shardability 与 per-rank bandwidth 放到同等位置。
- **Changed Constraint / Principle:** 当长上下文 Decode 的限制从“总 KV 容量”转为“每个 rank 在每步能读取多少
  KV state”时，压缩后的状态布局必须暴露可执行的 partition axis。长期原则是：**模型架构不仅定义参数量与
  表达能力，也定义 runtime 可以怎样切分和放置状态。**压缩成更小却不可分片的对象，可能在规模化执行时形成
  新的 bandwidth floor。
- **Mechanism / State Ownership / Control and Data Flow:** MLRA 将一份 latent KV 拆为四个 latent heads；每个
  latent head独立上投影出 NoPE Key/Value并计算attention，四路结果相加。模型checkpoint拥有latent-head
  projection与variance-scaling参数；TP runtime负责把latent heads映射到ranks、执行本地attention并在输出
  boundary恢复原operator语义。论文通过放大query、latent KV与output scale补偿多路求和的variance变化，说明
  “增加可分片维”并非只改layout，而会改变初始化与优化合同。
- **Implementation / Evaluation Contract:** 训练比较在参数匹配的2.9B模型上进行，使用FineWeb-Edu-100B，
  context 2,048、global batch 480 sequences（约一百万tokens/step）、100k steps、8×H100 80GB；MLRA-4平均
  perplexity 13.672、MLA 13.727，只能说明作者配置下质量近似而非普遍无损。Decode attention microbenchmark
  使用单张H100、batch 1、128K～2M context；8×H100 throughput比较则让MLA、GLA、MLRA、GQA采用不同TP/DP
  layouts，不能把1.05～1.26×相对GQA或约2.8×相对MLA外推为纯kernel加速或任意服务workload收益。
- **Baselines / Ablations / Sensitivity / Overhead:** 论文比较MHA/GQA/MLA/GLA与MLRA并检查latent-head数、
  scaling策略和多项语料PPL；但没有多seed/置信区间、超大规模模型训练、真实continuous batching、跨节点
  topology、TTFT/TPOT tail、failover或动态长度mix。作者代码与权重改善可审计性，不替代独立复现。
- **What the Evidence Proves / Does Not Prove:** 证据支持“单latent head会限制head-wise TP，而增加latent
  heads可在特定实现中降低per-device KV load并保持2.9B训练质量”；它不证明MLRA普遍优于GQA/MLA、四头是
  最优值、吞吐提升只来自cache sharding，或任意checkpoint都能无损转换。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 更多latent heads恢复并行自由度，也增加
  projection/aggregation、初始化耦合、checkpoint与kernel复杂性；当TP degree小、单卡cache仍可承受、通信比
  HBM读取更贵时，单latent MLA仍可能合理。GQA则在成熟kernel、简单head mapping与质量可预期性更重要时继续
  成立。新方案下一阶段压力是跨节点collective、continuous-batch length skew、kernel portability与大模型复现。
- **Evolution Relationship:** `Direct Evolution`：MHA -> GQA/MQA降低KV-head数量 -> MLA压缩为共享latent state
  -> MLRA为latent state恢复shardable head axis。`Layering / Dependency`：architecture state shape -> checkpoint
  layout -> TP placement -> per-rank KV traffic -> serving goodput；后层优化不能凭空创造前层未暴露的partition axis。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读Ch14～15、Ch19、Ch33、Ch41与Ch50相关段落。Ch15已说明
  head layout约束TP，Ch19/41已有`H_kv`容量公式，Ch33已有`H_kv < TP`导致replication；尚未明确“低秩latent
  state可能比GQA更小却更难分片”的架构—runtime反转。主owner将在Books Gate中于Ch15与Ch33之间裁决，
  Ch41只承接per-rank KV traffic handoff。
- **Integration Decision:** `Refine — MODEL-MULTI-HEAD-ATTENTION / Ch15 / Experimental`。已补入压缩状态的
  shardability、latent-head partition axis 与 TP/communication 共存边界，不保留作者吞吐 headline。
- **Open Questions:** 在真实多请求Decode中，latent-head sharding节省的HBM读取是否被output aggregation与
  collective抵消？不同TP/DP/topology下如何给出等资源goodput曲线？latent-head count能否与checkpoint转换、
  quantization和prefix-cache layout共同优化？

### Believe Your Model：从多数投票到分布建模，但自信仍不是外部正确性

- **Candidate / Week / Score:** Believe Your Model / Distribution-Guided Confidence Calibration（DistriVoting）/
  2026-W10 / 24/30；`Source Family ID: distrivoting-confidence-mixture-selection`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-04 首次公开且当前仅一个版本；已阅读完整
  HTML、公式、algorithm、全部实验与 Appendix，并核对官方 repository。
- **Full-read Coverage:** `Verified`。覆盖 related work、trajectory confidence、two-component GMM、negative-answer
  rejection、hierarchical voting、SelfStepConf、16-model evaluation、budget sensitivity、ablation、latency与prompt。
- **Original Problem / Why Previous Design Was Reasonable:** Test-time scaling通过采样多条轨迹增加正确答案被覆盖的
  概率；majority vote在答案可规范化、正确轨迹占最大簇且错误相对分散时便宜可靠。边界是高置信错误与低置信
  正确会重叠，增加样本只改善coverage，不保证selector辨别力随之增长。
- **Changed Constraint / Principle:** 当候选数上升到每题数十或上百条，系统不仅需要生成预算，还需要解释
  confidence分布、选择规则与abstention。原则是：**内部confidence可以作为selection evidence，但只有经过分布、
  task、model与sampling条件校准后才有含义；它不自动升级为acceptance proof。**
- **Mechanism / State Ownership / Control and Data Flow:** 系统从每条trajectory的answer-tail token logits构造
  confidence，在同一问题的候选集合上拟合two-component GMM，把两分量解释为较正/较负分布；随后用GMM
  filter、negative-answer reject与hierarchical voting聚合。SelfStepConf以EMA维护step-level confidence；置信下降时
  注入reflection token改变后续轨迹。Generator拥有logits与trajectory，selector拥有mixture parameters、filter与
  vote state；二者若同源，会共享校准偏差与语义盲点。
- **Implementation / Evaluation Contract:** 论文覆盖16个Qwen3与DeepSeek-R1-distill模型，评测HMMT2025、
  GPQA-D、AIME24/25、BRUMO2025；Qwen context为32K、DeepSeek为64K，默认每题128 trajectories并重复64次
  voting。硬件只披露NVIDIA H-Series，具体型号、并发与完整服务SLO未公开。SelfStepConf一个报告设置的每
  iteration时间由207.7ms增至212.5ms（约2.3%），不能外推为端到端cost。
- **Baselines / Ablations / Sensitivity / Overhead:** Ablation显示GMM filter贡献最大，reject filter依赖分布拆分，
  hierarchical voting在过滤后边际较小；trigger token差异不大。论文检查sample budget与多个confidence指标，但
  没有开放式任务、工具执行、独立verifier、真实成本/尾延迟、distribution shift或mixture collapse下的系统性
  failure study。
- **What the Evidence Proves / Does Not Prove:** 证据支持作者数学题配置中，候选confidence的经验分布结构可用于
  改善aggregation，并且step-level反思信号可低额外iteration开销嵌入生成；它不证明两个Gaussian等价于
  correct/incorrect ground truth、模型自信已校准、结果适用于开放式任务，或128-sample预算具有生产经济性。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** mixture fit增加selection compute与状态，且在
  单峰、分量交换、小样本或temperature/model变化时可能误标；SSC还会把早期confidence noise反馈进后续生成。
  Greedy/单样本在低预算场景仍合理；majority在可规范化答案与弱相关错误下仍强；pairwise/verifier适合需要局部
  比较或外部正确性时。新方案是增加一条分布证据，而不是淘汰旧selector。
- **Evolution Relationship:** `Direct Evolution`：single trajectory -> parallel sampling提高coverage -> majority/
  pointwise/pairwise selection -> query-level confidence distribution modeling -> generation-time confidence feedback。
  `Layering / Dependency`：coverage -> selection -> calibration -> acceptance；任何一层不能替代外部verifier。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读Ch20、Ch62与Ch66相关段落。Ch20已有coverage/selection
  分层、comparison graph与“judge分差不等于置信度”，Ch62已有scorer calibration与distribution contract；当前缺口
  不是再写一篇算法，而是是否应补出“query-local mixture state与component-identification failure”。主owner候选为
  Ch20，Ch62/66只承接校准与真实budget handoff。
- **Integration Decision:** `Refine — MODEL-SAMPLING / Ch20 / Experimental`。已补入 query-local distribution
  state、component failure 与 selection/acceptance 边界，不复制作者 benchmark。
- **Open Questions:** mixture component怎样在没有label时稳定识别、监测交换或退化？跨temperature/model/task的
  calibration怎样迁移？何时128条trajectory的边际正确率能覆盖Decode、KV与selector成本？

### Progressive Residual Warmup：从静态初始化到训练时间上的逐层状态激活

- **Candidate / Week / Score:** Progressive Residual Warmup（ProRes）/ 2026-W10 / 26/30；
  `Source Family ID: prores-depth-time-residual-activation`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-05 首次公开且当前仅一个版本；已阅读完整
  HTML、公式、全部主实验与 Appendix。论文未公开作者代码，故实现只能核验到论文算法与超参数。
- **Full-read Coverage:** `Verified`。覆盖Introduction、Pre/Post/Sandwich-LN与DeepNorm background、ProRes
  schedule、variance/gradient解释、130M～7B训练、depth scaling、spike metric、schedule/length/order ablation与结论。
- **Original Problem / Why Previous Design Was Reasonable:** Residual connection与Pre-Norm为深网络保留短梯度路径，
  static initialization与warmup在训练开始时控制更新尺度；这些设计让所有层从第一步共同学习，在宽度充分、深度
  适中和成熟recipe下仍然合理。边界是深层transform branches从随机初始化起就修改尚未稳定的表示，并把噪声
  梯度传回浅层；静态缩放只规定`t=0`，不能表达各深度何时应获得完整更新权。
- **Changed Constraint / Principle:** 当模型更深、更窄或采用Post-LN等敏感拓扑时，稳定性控制需要同时依赖layer
  depth与training time。长期原则是：**Residual topology定义可学习路径，schedule决定这些路径何时成为活跃状态；
  initialization、normalization和optimizer warmup不是彼此可替代的单旋钮。**
- **Mechanism / State Ownership / Control and Data Flow:** ProRes在每个residual branch上乘`alpha(l,t)`；训练开始
  所有branch为0，网络接近identity，随后按浅层到深层的顺序逐步增大到1。Checkpoint/runtime必须拥有global
  optimizer step、layer index与schedule配置；forward应用当前scale，backward沿同一路径传播。线性schedule在
  作者实验中最稳，equal/reverse order更敏感，说明顺序本身是训练语义而非纯工程启动参数。
- **Implementation / Evaluation Contract:** 主实验使用C4并辅以ClimbMix，模型130M、350M、1.3B，Appendix扩到
  7B；global batch 512、100k steps、AdamW `beta=(0.9,0.95)`、weight decay 0.1、gradient clip 1、WSD learning
  rate，单节点8×H800。另以71M模型从12层扩到120层，并用rolling 1,000-step窗口上超过7个标准差的loss定义
  spike。7B只提供training/eval loss差，不构成完整下游能力与系统效率证明。
- **Baselines / Ablations / Sensitivity / Overhead:** 论文比较Pre-LN、Post-LN、Sandwich-LN、DeepNorm、LayerNorm
  Scaling并检查warmup长度、shape、activation order与深度；短于1k或长于48k steps在作者配置中变差。缺少多seed/
  置信区间、跨optimizer/architecture、训练中断恢复、schedule-state错位与独立复现；作者对“浅层先稳定”的因果
  解释主要来自activation/cosine等相关观测，不是隔离所有替代机制的因果证明。
- **What the Evidence Proves / Does Not Prove:** 证据支持time-and-depth-dependent residual scaling在所测
  Transformer与训练recipe中减少loss spikes并改善PPL/部分benchmarks，Post-LN受益更明显；它不证明ProRes是
  通用最优、能替代learning-rate warmup或normalization，也不证明大于7B、超长训练和不同数据下收益持续。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 新方案增加schedule state、resume一致性、
  layer mapping与超参数敏感性；过短没有隔离效果，过长会延迟深层学习，错误恢复step会改变模型语义。Pre-Norm
  在成熟recipe、较宽模型与恢复简单性更重要时继续成立；受控Post-LN、DeepNorm与static residual scaling仍是不同
  设计分支。下一阶段压力是schedule自动化、checkpoint兼容与跨规模因果验证。
- **Evolution Relationship:** `Direct Evolution`：Post-Norm -> Pre-Norm改善identity gradient -> controlled
  Post-Norm/static residual parameterization -> ProRes把branch scale扩展为`layer × time`状态。`Layering /
  Dependency`：residual topology -> initialization -> residual schedule -> optimizer/LR schedule -> recovery state；
  后发schedule不能否定旧拓扑在其工作区间的合理性。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读Ch17与Ch24相关段落及相邻training-stability内容。Ch17已
  保留Pre/Post-Norm共存条件与controlled Post-LN，Ch24已有optimizer/LR warmup、precision与训练稳定性；尚未把
  residual branch activation作为独立的可恢复训练状态。主owner候选为Ch24，Ch17承接架构语义handoff。
- **Integration Decision:** `Refine — TRAIN-PRETRAINING / Ch28 / Experimental`。已补入 residual branch 的
  `layer × time` activation state、resume identity 与旧 normalization/warmup 分支的共存条件。
- **Open Questions:** resume时如何验证`alpha(l,t)`与optimizer/global-step一致？能否从gradient/activation telemetry
  自适应决定branch activation，而不是固定schedule？与sequence length warmup、curriculum和pipeline restart如何
  交互？

### BandPO：从固定 ratio clip 演进为概率感知的 trust-region 投影

- **Candidate / Week / Score:** BandPO / 2026-W10 / 28/30；
  `Source Family ID: bandpo-probability-aware-trust-region`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-05 首次公开；已阅读 23 页完整论文、公式、算法、
  全部主实验与 Appendix，并核对官方 repository、`band.py` 的 KL/TV/Pearson-chi-square solver 和训练入口。
- **Full-read Coverage:** `Verified`。覆盖 Background、f-divergence trust region、Band operator 推导、KL 数值求根、
  TV/chi-square 闭式解、GRPO 集成、五个模型规模实验、delta sensitivity、entropy/clip diagnostics 与 limitations。
- **Original Problem / Why Previous Design Was Reasonable:** PPO/GRPO 的固定 ratio clip 用低成本局部约束避免一次
  policy update 过大；它无需为整个 vocabulary 求解 constrained optimization，在 rollout policy 与 current policy
  接近、action probability 不极端时仍然是合理工程近似。边界在于 ratio 区间映射回 probability 后依赖旧概率：
  低概率且正 advantage 的 token 上升空间趋近于零，而高概率 token 的形式上界甚至可越过 simplex，统一
  `epsilon` 并不代表统一的 distributional distance。
- **Changed Constraint / Principle:** 当 reasoning RL 依赖长尾探索且 vocabulary probability 高度不均匀时，更新
  约束必须表达“整个 categorical distribution 能移动多远”，而不是只约束被采样 token 的统一 ratio。长期原则是：
  **clip 是 trust-region 的近似接口；其几何应由旧 policy state、divergence identity 与风险预算共同定义。**
- **Mechanism / State Ownership / Control and Data Flow:** BandPO 固定某个 sampled action 的候选概率，将其余
  action 按旧分布等比例重缩放，把高维 f-divergence 约束降为一维可行区间，再把区间映射为 token-specific ratio
  bounds。KL 版本通过并行 bisection 求根，TV 与 Pearson chi-square 有闭式边界；训练仍计算 GRPO advantage，
  但用 probability-aware lower/upper band 取代固定 clip。rollout policy `pi_old`、current policy、每 token 的
  `p_old`、divergence family、radius `delta` 与 reference-model KL 是不同状态，不能混成一个“KL 系数”。
- **Implementation / Evaluation Contract:** 作者在 verl 上训练 Qwen2.5-3B-Instruct 与 DeepSeek-R1-Distill-
  Qwen-1.5B/7B、Llama-8B，使用 DAPO 与 MATH 3～5 训练题，在 AMC2023、AIME2024、AIME2025 评估；硬件为
  8×H200。1.5B/3B 训练 800 steps，7B/8B 为 500；global batch 256、mini-batch 64、micro-batch 8、LR
  `1e-6`、temperature/top-p 均为 1，三次重复；报告 mean@32 与 pass@32。GRPO baseline 使用
  `epsilon_high=0.28`、`epsilon_low=0.2`，BandKL 默认 `delta=0.05`。论文未给生产并发、端到端 rollout
  latency、SLO 或 solver 占比。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 GRPO、Clip-Higher、Relaxed Band，并检查不同 delta、
  clip fraction、entropy 与 probability bucket。作者配置中 BandPO 的 mean@32 更高，低概率正 advantage token
  的 upper-tail clipping 接近消失；Qwen2.5-3B 的 entropy 约保持 0.2，而固定 clip 后期约 0.02。delta 对 3B
  比 7B 更敏感，过紧限制探索、过松削弱稳定性。KL 每 token 的数值求根增加 kernel 与近似误差；论文建议
  lookup table，但未给完整 memory/latency trade-off。
- **What the Evidence Proves / Does Not Prove:** 证据证明作者给出的 categorical projection 可产生满足所选
  f-divergence 半径的 action-specific bounds，并在所测数学 RLVR 合同中改善训练曲线与部分 pass/mean 指标。
  它不证明该 clip 是全局 policy optimum，也不证明对 code/tool/open-ended rewards、不同 advantage estimator、
  off-policy replay 或真实 serving cost 普遍有效。`mean@32` 与 `pass@32` 还绑定 32 次采样预算，不能外推成
  单次请求能力。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 新设计把 solver identity、delta、数值容差与
  `p_old` freshness 加入训练状态；global fixed delta 仍会把不同语义与不确定性的 token 同质化，旧 policy 或
  tokenizer 错位会直接改变 clip geometry。固定 PPO/GRPO clip 在计算预算紧、policy update 小、可复现简单性
  更重要时继续成立；adaptive-KL、KL penalty 与 early stopping 也是共存分支。下一阶段压力是 token/task-aware
  radius、solver telemetry 与 matched-compute 长程验证。
- **Evolution Relationship:** `Direct Evolution`：unconstrained policy update -> fixed-ratio clipping -> asymmetric/
  higher clipping -> divergence-derived token-specific band。`Layering / Dependency`：rollout identity -> advantage
  estimation -> trust-region geometry -> optimizer update -> evaluation budget；后发 band 只精炼更新边界，不替代
  reward correctness 与 credit assignment。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读 Ch28 与 Ch29 相邻内容，并复核 Ch62 的评估合同。
  Ch28 已解释 PPO ratio、clip 与 KL，但尚未把固定 ratio 的 probability geometry 展开；Ch29 负责 reasoning RL
  workflow，不应拥有通用 policy-update 机制。主 owner 为 Ch28，Ch29/62 只保留训练与评估 handoff。
- **Integration Decision:** `Refine — TRAIN-GRPO / Ch33 / Experimental`。已补入 probability-aware trust-region
  band 及 solver/calibration 成本，不把数学题实验外推为通用 RL recipe。
- **Open Questions:** 如何对 token/task 动态分配 divergence radius？solver approximation 与 policy lag 如何联合
  影响真实 trust region？在 matched rollout/FLOPs 与单样本成功率下，探索收益是否仍然成立？

### Sparse-BitNet：联合量化与结构稀疏，也暴露 artifact 顺序冲突

- **Candidate / Week / Score:** Sparse-BitNet / 2026-W10 / 24/30；
  `Source Family ID: sparse-bitnet-quantization-nm-mask`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-05 首次公开；已阅读全文 HTML、Method、训练与
  kernel 实验、全部 ablation/Appendix，并核对官方 repository、README 与 `llm/arch/model.py`。
- **Full-read Coverage:** `Verified with artifact conflict`。论文证据范围已读完，但 paper、README 与 executable
  code 对 mask/quantization 顺序并不一致，故不能把论文首选路径视为已由公开 artifact 复现。
- **Original Problem / Why Previous Design Was Reasonable:** 低比特量化减少权重带宽，N:M sparsity 利用硬件支持的
  规则零结构；分别优化二者可保持算法与 kernel 边界清晰。Full-precision 模型在严格 N:M 下容易质量下降，而
  BitNet 的 ternary weights 虽自然含约 42.3% 零值，却是非结构分布，不能直接获得规则 sparse-kernel 收益。
- **Changed Constraint / Principle:** 当部署目标同时受 bitwidth 与可执行稀疏结构约束时，训练必须共同维护“可学习
  连续参数”和“部署离散 artifact”。长期原则是：**离散压缩不是单一 checkpoint 变换；mask selection、scale
  estimation、quantization order 与 re-entry gradient 共同定义 artifact identity。**
- **Mechanism / State Ownership / Control and Data Flow:** 论文描述保留 BF16 master weights，按每个 N:M block
  的连续权重幅值选择 top-N mask，将权重 ternarize 至 `{-1,0,1}`，再在离散权重上施加 mask；activation 为
  8-bit。mask 每 step 重算，dual STE 让梯度穿过 quantizer 与 mask，使被屏蔽值仍可重新进入 top-N。训练状态
  因此包含 master weights、block partition、mask revision、quantization scale/order 与 optimizer state；部署只
  携带稀疏离散 artifact，二者不能互换。
- **Artifact Consistency Check:** 论文正文把 `quantize -> mask` 作为更优路径，并称 `mask -> quantize` 较差；
  官方 README 却写先 mask 再 quantize。公开 `WeightQuantMasked.forward` 先从 dense `x` 计算 scale，随后执行
  `x_masked = x * mask`，再量化 masked tensor，实际也是 mask-before-quantization。Appendix 渲染伪代码还在
  `w_masked` 定义前引用它。该冲突可能来自实现 revision 或术语差异，但在没有作者澄清与复现实验前，论文
  路径、代码路径及其 benchmark 不能静默视为同一机制。
- **Implementation / Evaluation Contract:** Qwen2.5-style 0.5B/1.5B/3B 从头训练，每个模型用 RefineWeb 50B
  tokens、sequence 2048；AdamW `beta=(0.9,0.95)`、`eps=1e-5`、LR `1e-5` cosine、warmup ratio 0.5、
  weight decay 0.1、micro-batch 16、gradient accumulation 4、BF16 master state。主要使用 6:8，也扫描 N:8
  与 2:4，并在五个 zero-shot benchmark 比较 dense/sparse BF16 与 dense/sparse BitNet。
- **Performance / Ablations / Sensitivity:** custom 6:8 kernel 在 Qwen2.5-3B 的 A100 prefill、sequence
  512～65536 报告 1.05～1.30×，在 B200 decode、batch 64～512 报告 1.09～1.18×；两阶段使用不同硬件，
  没有真实 server concurrency、KV/SLO 与端到端成本合同。mask-from-master、dense gradient 与论文所称
  quant-then-mask 在作者 ablation 中最好；从已量化权重选 mask 会产生 ties/flip noise，0.5B PPL 例为 32.23
  对 26.31。固定 50B budget 下 from-scratch 优于 dense-to-sparse，不构成跨预算普遍结论。
- **What the Evidence Proves / Does Not Prove:** 证据支持在作者训练合同中，BitNet 比同等 N:M 的 BF16 baseline
  相对更能承受结构稀疏，并展示 custom kernel 的局部 speedup；它不证明 sparse BitNet 的绝对质量超过 dense
  BF16，也不证明训练顺序已由公开代码复现、任意 GPU 都有加速，或 6:8 在生产 SLO 下优于更成熟 2:4/
  dense kernels。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 每 step 重选 mask 引入 topology churn、
  optimizer/mask 对齐、checkpoint replay 与 kernel portability；STE 允许 re-entry，但也令训练梯度与部署离散
  operator 不完全一致。dense low-bit 在硬件不支持 N:M、batch/shape 不适合 sparse kernel 或 artifact 简单性更
  重要时仍合理；post-training structured pruning 适合已有 dense checkpoint 的迁移路径。下一阶段压力是 artifact
  顺序澄清、matched-hardware end-to-end serving、mask stability 与 long-horizon scaling。
- **Evolution Relationship:** `Layering / Dependency`：dense BF16 -> weight/activation quantization -> unstructured
  ternary zeros -> hardware-aligned N:M mask -> joint trainable discrete artifact。它是压缩维度的组合，不意味着后者
  淘汰 dense、纯量化或 post-training sparsity。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读 Ch24、Ch45 与 Ch50 的相邻训练/量化/硬件协同内容。
  Ch45 已覆盖量化 calibration 与 kernel contract，Ch50 已覆盖 structured sparsity 的硬件依赖；缺口主要是训练时
  master/mask/discrete artifact 的状态分离，主 owner 为 Ch24，Ch45/50 使用短 handoff。
- **Integration Decision:** `Weekly Only — Disputed Artifact Order / No Books Change`。论文、README 与公开代码的
  mask/quantization 顺序仍冲突；不以未对齐 artifact 支撑长期训练机制。
- **Open Questions:** paper 与 code 的 operator order 哪一个对应已报告结果？mask revision 怎样进入 checkpoint
  manifest？在相同 GPU、模型、batch、length、quality 与 SLO 下，N:M kernel 的净收益何时覆盖训练复杂度？

### ATLAS：从加载所有工具描述到按需 schema 与持久执行状态

- **Candidate / Week / Score:** ATLAS / Scaling Agentic Capabilities, Not Context / 2026-W10 / 27/30；
  `Source Family ID: atlas-lazy-toolspace-persistent-execution-rft`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-05 首次公开；已阅读全文 HTML、系统架构、训练、
  评估与 Appendix，并核对 Microsoft Research 官方 publication record。未定位到作者官方代码，故 scaffold 与
  persistent interpreter 只能核验到论文描述。官方记录将其列为 2026 ICLR Agents in the Wild Spotlight。
- **Full-read Coverage:** `Verified with report inconsistency`。覆盖 MCP toolspace motivation、ISL/ITL/PTC、task
  generation/filter、rubric RFT、seen/unseen evaluation、ablation 与 judge analysis；论文没有独立 Limitations 节。
- **Original Problem / Why Previous Design Was Reasonable:** eager tool loading 把所有 schema 放进 prompt，接口少、
  上下文充足时可以让模型直接选择并生成 arguments，控制流透明且容易无状态重试。工具扩到多个 MCP server 后，
  schema 会占据上下文，长轨迹反复携带中间结果；小模型还要同时学习检索、参数构造、程序控制与结果整合，稀疏
  task reward 难以定位错误。
- **Changed Constraint / Principle:** toolspace 与 trajectory state 的增长速度开始超过模型有效 context 与 credit
  assignment 能力。长期原则是：**context 应携带当前决策所需证据，而工具目录、schema、intermediate state 与
  evaluator rubric 应由 runtime 分层拥有；扩大 agent capability 不等于无限扩大 prompt。**
- **Mechanism / State Ownership / Control and Data Flow:** ISL 迭代加载 server，ITL 只在需要时 materialize 具体
  tool schema；PTC 提供持久 Python interpreter，使 agent 用代码表达分支/循环并让中间值留在 execution state，
  而不是每轮重放到 context。scaffold 规范化 MCP schema、包装 server function、提取 output schema/example 并在
  error 后补提示。训练侧由 GPT-5 生成 task rubric，Qwen3-30B 对 trajectory 评分，再用 GRPO 更新 policy；tool
  output tokens 被 mask，不参与梯度。tool registry/schema revision、interpreter process、workspace/intermediate
  values、model context、rubric generator、judge 与 policy checkpoint 是不同 owner。
- **Implementation / Evaluation Contract:** 超过 1,000 个 o4-mini synthetic tasks 经规则过滤，再由 Kimi K2
  Thinking 以至少 4/10 solvability 筛到 304 个训练任务。评估包括 28 个 seen servers 上 104 个 held-out
  MCPBench tasks，以及 11 个 unseen、28 servers 的 100 个 ATLAS-Test tasks。训练 Qwen2.5-7B 与 Qwen3-4B，
  context 32K；Kimi K2 Thinking 1T/80K 作为 frontier baseline。verl、8×B200、batch 16、PPO mini-batch 4、
  max context 31,000、每题 4 rollouts、temperature 1、GRPO、LR `1e-6`、BF16、最多 20 次 tool call、response
  4,000 tokens、KL 0.001。外部 o4-mini judge 评 task fulfillment、tool appropriateness、grounding 与 parameter
  accuracy；未报告生产 latency、permission boundary、side effects 或 SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** ITL 显著减少 schema tokens，但单独使用时 task fulfillment
  可能下降；PTC 在部分 seen tasks 改善，未配 RL 时在 ATLAS-Test 的 task fulfillment 从 2.96 降到 2.76。
  主要收益往往来自 rubric RFT，说明 execution scaffold 是 substrate，不是独立能力来源。task solvability 由
  Kimi 过滤、rubric 由 GPT-5 生成、结果由 o4-mini judge，形成 selection/judge dependence；没有 deterministic
  outcome verifier。正文称尚未对 PTC 使用 rubric reward，但表格包含 `PTC + RL w/ Qwen3-30B J. (Rubrics)`，
  报告内部不一致，不能自行推定哪一版训练合同正确。
- **What the Evidence Proves / Does Not Prove:** 证据支持 lazy schema exposure 与 persistent program state 可以
  降低 prompt/token 搬运，并在所测 MCP harness 与 rubric-RFT 组合下提高部分 agent 指标；它不证明小模型在真实
  开放工具空间中达到 frontier 能力，也不证明 PTC 单独带来提升、LLM rubric 等于可执行正确性，或 interpreter 在
  多租户生产环境安全可靠。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** PTC 把上下文成本迁移为 runtime state、进程
  lifecycle、依赖/资源治理与恢复问题，并扩大 code execution、secret/permission、side-effect 与 cross-task leakage
  风险；lazy schema 还会因搜索漏召回、版本漂移或错误提示造成不可见工具。eager schema 在工具少、权限敏感、
  deterministic replay 与 stateless retry 更重要时仍成立；structured function calling、retrieval-only schema 与
  external workflow engine 是共存方案。下一阶段压力是 capability/authority separation、sandbox、state provenance、
  deterministic verifier 与 failure recovery。
- **Evolution Relationship:** `Direct Evolution`：eager all-schema prompt -> iterative server loading -> on-demand tool
  schema -> persistent program state -> rubric-guided policy adaptation。`Layering / Dependency`：registry discovery ->
  schema retrieval -> plan/code generation -> authorized execution -> state persistence -> outcome verification；后发 runtime
  不替代 tool permission 与 correctness gate。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读 Ch77 与 Ch71/74/80 相邻 workflow、tool、runtime 内容，
  并复核 Ch29/62 的 RL/evaluation boundary。Ch77 已有 workflow state 与 side-effect control，但尚可进一步区分
  prompt context、tool registry、interpreter state 与 rubric training state；主 owner 为 Ch77，其余章节短 handoff。
- **Integration Decision:** `Refine — AGENT-WORKFLOW / Ch81 / Experimental`。已补入 lazy schema exposure、
  persistent interpreter 与 durable workflow state 的 owner/failure 分层。
- **Open Questions:** 如何把 schema/tool/server revision 与 trajectory 一起回放？persistent interpreter 怎样隔离
  tenant、credential、filesystem 与 network authority？若 rubric/judge/provider 改版，policy improvement 如何重验？

### Building AI Coding Agents for the Terminal：设计经验不是效果证明

- **Candidate / Week / Score:** Building Effective AI Coding Agents for the Terminal / OpenDev / 2026-W10 /
  25/30；`Source Family ID: opendev-terminal-agent-engineering-report`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-05 首次公开，v2/v3 分别于 3 月 9/13 日修订；
  已阅读 v1 全文、全部架构与实现 Appendix，并以 v3 核对 revision，联读官方 repository、README 与 build/
  provider 配置。论文自称 work in progress；当前 repository 已演进为 Rust workspace，因此历史论文描述与当前
  code 必须按 revision 分离。
- **Full-read Coverage:** `Verified as engineering report`。覆盖 session/agent/workflow/model 四级结构、factory、
  Extended ReAct、五类模型路由、context compaction、memory、tool registry、shell safety、approval、persistence、
  undo、全部 constants/catalog 与 conclusion。论文没有自身 benchmark、对照实验、ablation 或生产 SLO 数据。
- **Original Problem / Why Previous Design Was Reasonable:** IDE copilot 或单一 ReAct loop 在短任务中结构简单，
  人类持续监督时可以把 context、tool selection、failure recovery 与安全边界留在交互层。终端 Agent 直接接触
  repository、build、shell、background process 与 credentials，任务又跨长轨迹后，纯 prompt 约束会遭遇 context
  膨胀、instruction fade、重复调用、隐式 completion 和副作用放大。
- **Changed Constraint / Principle:** 当 Agent 从“生成建议”进入“持续改变 workspace”时，model output 不再是
  唯一状态。长期原则是：**能力、上下文与 authority 必须分别分层；可靠性主要来自 runtime 对状态、工具暴露、
  停止与恢复的约束，而不是让同一个模型同时记住所有规则。**
- **Mechanism / State Ownership / Control and Data Flow:** OpenDev 把 session 分成 main/planner/subagents，再把
  normal、thinking、critique、vision、compact 绑定到可独立选择的 provider/model。Planner 的 schema 不含 write
  tools，以 capability absence 而非运行时拒绝形成 read-only 边界；tool registry 延迟发现 MCP schemas。Extended
  ReAct 在每轮先按 context pressure 分级 compact，再 thinking/action；相同 `(tool,args)` fingerprint 在最近 20
  次调用中达到 3 次先 warning，再升级为真实 execution pause。tool output 可按类型摘要，超过阈值 offload 到文件；
  episodic/working memory、Reflector/Curator playbook、session store、operation log 与 shadow-git snapshot 分别持有
  经验、当前上下文、恢复与 undo 状态。
- **Implementation Contract:** v1 论文给出 compaction 的 70/80/90/99% pressure thresholds、tool-output offload
  8,000 chars、最近 6/3 observations 保真、subagent 15 iterations、三次 error nudge 等实现常量；shell path 还包括
  permission config、allowed-command match、dangerous-pattern deny、PTY/background、timeout 与 cancellation。当前
  repository README 证明多 provider、五个 workflow slots、MCP 与跨平台 release/build 入口，但这些是版本化功能
  事实，不证明 paper 中每条路径仍按 v1 常量运行。
- **Evaluation / Evidence Boundary:** 论文大量引用外部 benchmark 与相关研究，却没有对 OpenDev 自身报告 task
  success、human intervention、duplicate side effects、context-loss rate、token/cost、latency、security bypass 或
  recovery success，也没有与单模型/无 compaction/无 memory baseline 对照。因此 evidence 只证明一个公开系统的
  architecture 与作者设计经验，不证明“dual agent”“五模型路由”或某组 threshold 提升了真实软件工程效果，更
  不能把 `production-ready` 当作独立验证。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** specialization 可降低单步 prompt 噪声，却
  增加 provider/model fallback、跨上下文 handoff、成本与 attribution；compaction 节省 token，也可能丢失精确约束；
  playbook memory 会积累错误经验；fingerprint 只能发现完全相同调用，无法识别参数微变的 semantic loop；shadow
  undo 不等于外部副作用 rollback。单 Agent、eager tools 与人工 review 在短任务、工具少、成本或可解释性优先时
  仍合理。下一阶段压力是 revision-pinned replay、component ablation、权限/副作用测试与 task-level evidence。
- **Evolution Relationship:** `Layering / Dependency`：inline completion -> IDE copilot -> terminal ReAct loop ->
  schema-restricted planner/executor -> specialized workflows -> persistent context/memory/recovery control plane。
  `Principle Reuse`：capability-based security、event log 与 content-addressed snapshot 来自系统工程，而非模型能力替代。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读全文 Ch74、Ch77 与 Ch80，并检查 Ch71/73 的 context/
  memory boundary。Ch74 已拥有 proposal/executor、lazy discovery 与 loop limits；Ch77 已拥有 deterministic spine、
  durable state、approval/replay；Ch80 已拥有 AgentRun 与平台控制面。新增价值主要是把 context-pressure policy、
  capability-absent planner schema、semantic loop detection 和 version-pinned harness 连成案例，主 owner 为 Ch77。
- **Integration Decision:** `No Change — Already Covered / Engineering Report`。Ch78/81/84 已覆盖 capability
  separation、compaction、loop limits、event log、snapshot/recovery 与 platform authority；无 task-level evidence
  支持再增加机制正文。
- **Open Questions:** current Rust implementation 与 v1/v3 论文哪些路径一一对应？怎样评估 compaction 丢失关键
  invariant、memory poisoning 与 parameter-varying doom loop？undo 如何覆盖 shell、network 与 deployment side effects？

### AutoResearch-RL：撤稿状态使机制主张不能进入 Books

- **Candidate / Week / Score:** AutoResearch-RL / 2026-W10 / 12/30；
  `Source Family ID: autoresearch-rl-withdrawn-claim-family`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-07 首次公开；v2 于 2026-03-19 被 arXiv 管理员
  撤回，页面明确说明违反 acceptable-submission policy，当前无 PDF。已阅读全文残留的 v1 HTML、公式、算法、
  实验表与 limitations，并核对 withdrawal metadata。未定位到作者官方代码、training logs、checkpoint 或 artifact。
- **Access and Verification Status / Full-read Coverage:** `Withdrawn / Disputed`。v1 文本可用于记录它提出了什么，
  但撤稿、无 artifact 与内部可执行性矛盾使实验和训练主张不能作为可靠 evidence。该项的“完成”是完成拒绝核验，
  不是验证论文结论。
- **Original Problem / Proposed Mechanism:** 文本把自动 ML 研究表述为 MDP：state 包含 current `train.py`、最近
  32 次实验、top-5/best summary 与 GPU/time diagnostics；action 是 atomic unified diff；固定 300 秒训练后以
  validation bits-per-byte 改善和 efficiency bonus 作为 reward，失败编译给予 penalty，再用 PPO 更新提出代码的
  policy。self-evaluator 每 30 秒拟合 power-law loss curve，通过 threshold/SPRT 决定 early abort；best-so-far
  artifact 单调保留，失败配置回退。
- **Why the Previous Design Was Reasonable / Changed Constraint:** greedy LLM 或人工 hyperparameter search 不需要
  在线更新 proposer，易于审查且避免 meta-training state；固定 environment、单 mutable file 和可执行 metric 则
  试图让长周期实验可比较。可迁移原则本应是：冻结 evaluator、限制 mutable scope、保留 lineage，并把 early-stop
  当成有 false-negative 风险的资源调度决策，而不是“Agent 自我改进”的证明。
- **Claimed Evaluation Contract:** v1 声称 FineWeb 10B-token subset、5M-token held-out、BPE vocabulary 4,096、
  sequence 512、单 H100 80GB SXM、每实验 300 秒；比较 human GPT-2-small baseline、random search、GPT-4o
  greedy Agent 与完整系统，约 8 GPU-hours/88～101 experiments，并给出最长一周 2,147 experiments 的 val-bpb。
  文本还声称 policy 从 `claude-sonnet-4-20250514` 初始化并对 attention projections 做 LoRA/PPO fine-tuning，
  但没有说明如何取得可训练权重，也没有 checkpoint、代码、rollout 或 optimizer artifact 支撑该关键实现。
- **What the Text Claims / Why It Is Not Evidence:** v1 报告 early abort 54.3%、每 GPU-hour 1.35× experiments、
  sample efficiency 2.4×，并声称发现 QK norm、optimizer 与 clipping/depth 修改。这些数字缺少公开 raw runs、
  seed/variance、matched proposal budget 与 executable artifact；withdrawal 后不应作为论文实验结论引用。所谓
  convergence theorem 还假设每次实验独立且始终有正概率改进，而真实 policy、history 与 code state 明显相关；
  best-so-far 不变只说明记录策略单调，不能证明系统安全、不会浪费资源或最终达到真实最优。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 即便按概念讨论，固定 wall-clock 会混合 compile、
  kernel warmup、hardware noise 与算法质量；early stopping 会系统性淘汰慢热配置；单 validation metric 容易
  overfit；diff-reward 对多步研究 credit 不充分；perpetual loop 会增加 benchmark leakage、资源与治理风险。人工
  研究、greedy/evolutionary search、Bayesian optimization 与 frozen proposer 在证据不足或实验昂贵时继续成立。
- **Evolution Relationship:** `Explanatory Analogy`：manual tuning -> LLM proposal loop -> evaluator-driven search ->
  claimed policy-learning research loop。由于 source 已撤回，不能把最后一步记录为已验证的 `Direct Evolution`；
  AlphaEvolve 等已核验系统仍是 Ch77 中 evaluator-driven search 的可靠 owner 案例。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读 Ch77 evaluator-driven search，并复核 Ch29、Ch62、Ch75。
  Ch77 已明确 frozen evaluator、artifact lineage、held-out verification 与 deployment authority；Ch29 覆盖 PPO/GRPO
  训练边界，Ch62 覆盖 metric/evaluator identity。现有 Books 已包含该文本中唯一可取的长期原则，无需用撤稿来源
  增补或佐证。
- **Integration Decision:** `Full Review Complete — Withdrawn / Disputed / Weekly Only`。不进入 Books，不保留作者
  benchmark，不把 withdrawn v1 当作 primary evidence。若未来出现可核验的独立论文或 artifact，应作为新的
  source family 重新审查，而不是恢复本候选结论。
- **Open Questions:** arXiv 管理员未公开更具体的违规类型；因此这里只记录正式 withdrawal，不推断动机。未来若
  相似系统发布，必须核验 proposer 权重可训练性、raw experiment lineage、early-stop false-abort 与 held-out metric。

### Hindsight Credit Assignment：后见相关性不是未经条件验证的因果 credit

- **Candidate / Week / Score:** Hindsight Credit Assignment Policy Optimization（HCAPO）/ 2026-W10 /
  24/30；`Source Family ID: hcapo-long-horizon-agent-credit`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-07 首次公开且当前仅一个版本；已阅读完整 HTML、
  HCA derivation、Generative Verification、multi-scale objective、三个任务族实验、temporal smoothing、完整
  Appendix/hyperparameters 与 limitations。未定位到作者官方 code、checkpoint 或 rollout artifact。
- **Full-read Coverage:** `Verified`。覆盖 classical HCA/GRPO background、公式 4～12、algorithm、ALFWorld、
  WebShop、search-augmented QA、三 seed smoothing、latency breakdown、prompt/history 与 4×/8×H20 训练合同。
- **Original Problem / Why Previous Design Was Reasonable:** terminal reward 直接广播到整条 trajectory，GRPO 的
  group-relative signal 能稳定比较同 prompt 的成败，也避免 critic 状态；当轨迹短、每步贡献接近或 process
  supervision 昂贵时，这种 coarse credit 仍然合理。长 horizon 中，成功路径包含关键 action 与无关 action，初始
  state 的 global baseline 也未表达中途 state value，uniform credit 会放大偶然共现步骤。
- **Changed Constraint / Principle:** 当 Agent trajectory 变长且 reward 稀疏，训练需要同时保留 outcome-level
  direction 与 step-local discrimination。长期原则是：**细粒度 credit 由 outcome、state/action identity、critic/
  posterior estimator 与 normalization 共同定义；未来结果可提供诊断信息，但不能自动把相关性升级为因果贡献。**
- **Mechanism / State Ownership / Control and Data Flow:** 对每条成功 trajectory，HCAPO 把 final state 注入同一
  LLM，让模型重新计算 observed action token 的 length-normalized hindsight log-probability；再用一条轨迹内所有
  steps 的均值近似 prior，将 ratio clip 到 `[0.8,1.2]`。hindsight Q 为 ratio、discounted terminal reward 的乘积，
  cross-state/group normalization 形成 micro advantage，再以 `omega=1` 与 macro GRPO advantage 相加；可选
  temporal smoothing `alpha=0.5` 向相邻步骤传播。rollout policy、reference policy、final-state representation、
  hindsight prompt/model、trajectory step boundary、normalization population 与 environment revision 都是训练状态。
- **Approximation Boundary:** classical HCA 的 `h(a|s,outcome)/pi(a|s)` 被实现为“conditioned action score / 同一
  trajectory 的 conditioned-score 均值”，不是对 behavior-policy probability 的直接估计；不同 steps 的 action
  length、state 与 semantics 也不同。论文把它称为 self-normalized importance ratio 和 causal filter，但公开证据
  只支持 learned hindsight relevance score。`do-no-harm` mask 还会在成功 trajectory 上删除负 micro signal，主动
  引入 bias；theory 的 bottleneck-state 分解不能证明 LLM posterior calibration 或真实 action causality。
- **Implementation / Evaluation Contract:** Qwen2.5-Instruct 1.5B/3B/7B；ALFWorld max prompt/response
  2048/512、50 steps，WebShop 4096/512、15 steps，group size 8、每 rollout 16 groups/128 envs，rollout/
  validation temperature 1.0/0.4；search QA max 4 turns、group 5、train size 256。actor LR `1e-6`，KL 为
  0.01 或 0.001；ALFWorld/WebShop 的 1.5B 用 4×H20、7B 用 8×H20、150 iterations；search QA 用
  8×H20、200 iterations。baseline 数字直接取自 GiGPO/EMPG 论文，没有在本文统一重跑。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 PPO/RLOO/GRPO/EMPG/GiGPO 与 search RL 方法；论文
  报告 ALFWorld temporal smoothing 三 seeds，并称 hindsight audit 约占 training time 8.3%，但没有披露各阶段
  absolute time、sequence/token volume、并发或 SLO。部分 tasks/模型上 HCAPO 不超过 GiGPO，且 QA gains 很小；
  baseline 跨论文复用削弱 matched-code/hardware 声明。缺 ratio calibration、posterior model ablation、counterfactual
  action intervention、omega/clip/temperature sensitivity 与独立复现。
- **What the Evidence Proves / Does Not Prove:** 证据支持这套 self-hindsight score 与 macro GRPO 组合在作者
  ALFWorld/WebShop/QA 合同中改善若干 success/score，并显示 non-generative audit 可并行；它不证明 estimator
  unbiased、识别真实 causal action、适用于失败 trajectory/开放工具、或优于 learned critic/process verifier 的
  matched-compute 方案。作者自己承认小模型 reasoning 限制 precision，hindsight context 形成 OOD input。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 同模型自评减少外部 critic，却共享 policy 的
  blind spot，并引入 future-information leakage、prompt/replay 膨胀、posterior drift 与 normalization 跨 state
  不可比；temporal smoothing 稳定训练，也可能把 credit 扩散到无关邻步。terminal GRPO 在短轨迹与廉价 verifier
  下继续成立；learned value、PRM、state-anchor 与 counterfactual environment replay 是共存分支。
- **Evolution Relationship:** `Direct Evolution`：terminal trajectory credit -> process/value estimates -> state-anchor
  group credit -> outcome-conditioned hindsight score + macro/micro advantage。后发方法精炼 credit interface，不否定
  coarse signal 在证据不足时更稳健。`Layering / Dependency`：environment outcome -> trajectory identity -> hindsight
  scoring -> normalization/masking -> clipped update。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读全文 Ch28、Ch29，并复核 Ch62/73。Ch29 已指出 terminal
  reward 的 token/step credit 缺口与 process reward trade-off，但尚未系统说明 outcome-conditioned self-critic 的
  estimator/bias/future-leakage 边界。主 owner 为 Ch29；Ch62 只承接 evaluator evidence，Ch73 不拥有训练 credit。
- **Integration Decision:** `Refine — TRAIN-GRPO / Ch33 / Experimental`。已把它限定为 hindsight relevance proxy，
  补入 future leakage、normalization 与同源 critic bias，不复制“causal filter”或 benchmark headline。
- **Open Questions:** 怎样用 action intervention 或 learned behavior denominator 校准 hindsight ratio？失败轨迹如何
  分配局部负 credit？posterior model 与 policy 同源时，何时会把自洽错误稳定地放大？

### Scaling Data Difficulty：难度是 model-relative curriculum state，不是样本固有标签

- **Candidate / Week / Score:** Scaling Data Difficulty / MicroCoder Dataset / 2026-W10 / 23/30；
  `Source Family ID: microcoder-model-relative-difficulty-curation`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-08 首次公开且当前仅一个版本；已阅读全文、四阶段
  data pipeline、predict-calibrate-select、全部 dataset statistics、training/filtering ablation 与 conclusion。论文称
  产生 13,300 个题目，但未定位到作者官方 dataset card、immutable manifest、license/provenance 清单或 pipeline code。
- **Full-read Coverage:** `Verified with artifact gap`。论文没有独立 Limitations 节，也未披露训练硬件、manual
  review protocol/IAA、private collection 的授权边界或可复现 dataset artifact。
- **Original Problem / Why Previous Design Was Reasonable:** 大规模公开 coding data 以覆盖和数量为先，platform
  difficulty label、格式与 tests 可直接复用；对能力较弱或 broad pretraining，这能提供足够基础分布。随着模型更强，
  easy/all-pass groups 对 RL 几乎无 gradient，旧题还可能已被 pretraining 见过；混合 function-completion 与 stdin/
  stdout 格式、缺失 tests 和噪声又会把 execution failure 当成 reasoning failure。
- **Changed Constraint / Principle:** 有效训练分布取决于 current model 的 success frontier，而不是题目名称上的固定
  easy/hard。长期原则是：**difficulty 是 `task × model/checkpoint × sampling budget × verifier` 的关系状态；数据
  curriculum 必须版本化该测量合同，并保留 coverage/diversity，而不是永久删除“简单题”。**
- **Mechanism / State Ownership / Control and Data Flow:** pipeline 依次 collect public/web/private problems、翻译与
  normalize、按文本/相关性/overlap/difficulty filter、再人工 verify readability/completeness/tests。先以 GPT-4o
  按五维 rubric 对每题评分三次；再让 Qwen3-4B-Thinking 每题尝试四次，以 empirical success rate 校准 2.5/2.75
  边界；最后删除低于目标难度的题。16-gram similarity 阈值 0.22 用于 train-test screening，tests 最多保留 15 个
  longest cases。dataset row 应拥有 source/license、normalizer、tests/verifier、predictor/rubric、calibration model/
  checkpoint/sampling 与 selection revision。
- **Implementation / Evaluation Contract:** 用 Qwen3-4B-Instruct-2507，GRPO/DAPO，max response 8K、temperature
  1.2、batch 64、LR `1e-6`、每 prompt 8 samples、binary execution reward；在 AtCoder、LeetCode 与
  LiveCodeBench v6 用四次 inference 的平均 accuracy，主要比较 MicroCoder 与 DeepCoder，也给 1.7B/4B/8B/14B
  与 filtering subsets。论文没有 GPU、precision、optimizer、总 tokens/steps 的完整统一合同，性能数字不能跨设置
  外推。
- **Contamination / Evaluation Boundary:** 论文报告 16-gram 筛查中约 3% 超阈值但“无完全相同”，以及 embedding
  cosine 0.04～0.14，进而宣称 zero overlap；这些检测只能证明在给定 detector/threshold 下未发现特定匹配，不能
  排除翻译、语义变体、solution/test leakage。用目标 benchmark 直接筛训练数据还会让 selection policy 适配其
  domain；“fresh”与 private source、platform、test quality、difficulty 同时变化，论文没有 factorized causal ablation。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持经该联合 pipeline 选择的数据在所测 code-RL recipe
  上比若干 dataset baseline 更改善 medium/hard slices，也说明 stronger model 需要重新定位 difficulty frontier。
  它不证明 recency 或 rubric difficulty 单独导致提升、不证明 13,300 rows 的授权/可复现性、不证明 GPT-4o rubric
  是 ground truth，也不证明四次 sampling 足以稳定标定 per-item difficulty。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 难度过滤提高 mixed-outcome 密度，却可能丢失
  基础技能、过采样长答案、放大某些 platform/style，并随着 checkpoint 提升迅速 stale；manual verification 与
  private data 增加 lineage/删除/许可成本。固定 broad mixture 在基础训练、回归保持与未知 deployment 分布中仍
  合理；online curriculum、loss-based sampling 与 source-balanced mixture 是共存分支。
- **Evolution Relationship:** `Direct Evolution`：source/platform labels -> heuristic quality filters -> model pass-rate
  difficulty -> calibrated model-predicted difficulty -> checkpoint-aware dynamic curriculum。新阶段把 difficulty 变成
  mutable control state，不淘汰简单样本，而改变其采样权重与用途。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读全文 Ch23，并复核 Ch29 与 Ch62。Ch23 已覆盖 data
  distribution、quality、dedup、contamination 与 lineage，但尚未明确 difficulty 必须绑定 checkpoint/sampling/verifier
  并随能力重新校准。主 owner 为 Ch23；Ch29 只接收 curriculum 对 mixed-reward groups 的影响。
- **Integration Decision:** `No Change — Already Covered / TRAIN-DATA Ch27`。Ch27 已明确 difficulty 是
  `task × checkpoint × sampling × verifier` 的 policy-relative state，并覆盖 lineage、retire/revise 与
  contamination；本候选没有新增可验证机制。
- **Open Questions:** private rows 的 source/license/withdrawal 如何治理？difficulty boundary 怎样随 checkpoint
  更新而不造成 catastrophic forgetting？怎样用 source/time/platform-matched ablation 分离 recency 与 difficulty？

### MicroCoder-GRPO：保护长输出潜力，也可能把长度代理误当成能力

- **Candidate / Week / Score:** Breaking Training Bottlenecks / MicroCoder-GRPO / 2026-W10 / 23/30；
  `Source Family ID: microcoder-grpo-length-diversity-evaluator`。
- **Source Type / Date / Direct Sources:** arXiv v1 于 2026-03-08 首次公开且当前仅一个版本；已阅读全文、公式、
  conditional truncation mask、temperature/KL/clip 分析、dataset/evaluator、三十余实验与 conclusion。未定位到
  作者官方 training code、MicroCoder-Evaluator、dataset artifact、checkpoint 或 raw curves。
- **Full-read Coverage:** `Verified with artifact and workload gaps`。论文没有独立 Limitations 节，未披露 GPU、
  precision、optimizer、并发、absolute wall time 或 evaluator human-gold audit；因此 headline cost/accuracy 不能复核。
- **Original Problem / Why Previous Design Was Reasonable:** 标准 GRPO 的 fixed max length、temperature、KL 与
  clip 在短数学答案或成熟 policy 上提供稳定受限更新；完全 mask 所有 truncation 也避免把不完整回答当成负样本。
  code reasoning 的输出更长、binary tests 更稀疏时，严格 length cap 会让潜在正确但未完成的 trajectory 全部失去
  learning signal，而过强 reference constraint 与 diversity collapse 又可能过早锁死探索。
- **Changed Constraint / Principle:** 训练 budget 不只是容纳最终答案，也塑造 policy 能探索哪些 trajectory。
  长期原则是：**truncation、sampling temperature、diversity metric、verifier 与 trust-region policy 共同构成
  curriculum；它们必须按 outcome/length slices 联合观测，不能把更长输出或更高 entropy 直接等同于能力。**
- **Mechanism / State Ownership / Control and Data Flow:** conditional mask 只对同时达到 `L_max`、被判定为
  non-incorrect、末尾 128 tokens 未重复且命中概率 `rho` 的 responses 将 advantage 置零；temperature 依据初始及
  后续 output-diversity trend 分阶段选择；同时沿用 DAPO 风格移除 KL、扩大 positive clip。MicroCoder-Evaluator
  通过 6～7 种 comparison fallback、type conversion、`np.allclose`、whitespace/multiline normalization 与并行执行
  产生 binary reward。policy/rollout temperature、max length、mask RNG/rule、diversity statistic、reference/KL/
  clip、evaluator fallback order/tolerance 与 tests 都是训练 identity。
- **Implementation / Evaluation Contract:** Qwen3-1.7B-Instruct 与 Qwen3-4B-Instruct-2507，主要是 MicroCoder/
  DeepCoder、LiveCodeBench v6 的 AtCoder/LeetCode；默认 max response 8K、temperature 1.2、batch 64、LR
  `1e-6`、DAPO、每题 8 samples、0/1 reward、四次 inference average。temperature 分析使用 OlympicCoder 与
  200 个随机 test problems、4K；另比较 4K train 到 8K eval、1.7B/4B 和表中的更大模型。论文用 theoretical
  `O(n^2)` 推出 4K 相对 6K 节省约 40～50%，但未给实际 token distribution、hardware 或 measured training cost。
- **Baselines / Ablations / Sensitivity:** 比较 GRPO、DAPO、no/full/conditional truncation mask、多 masking rate、
  temperature transitions、KL/high clip、batch/on-vs-off-policy 与 context extension。作者曲线显示完全 mask 可更快
  到 peak 后下降，30% conditional mask 在所测设置平衡增长与稳定；早期短 context 后续延长不能完全恢复。但许多
  axes 同时变化，缺 multi-seed uncertainty、matched token/FLOPs、mask classifier error 与 independent reproduction。
- **Evaluator Boundary:** 多 fallback/type coercion 可能减少合法输出的 false negative，也可能把不等价输出宽松地
  判对；`np.allclose` tolerance、set/list conversion 与 comparison order 是 reward policy。论文以更高 critic reward
  和后续 training curve 支持“约 25% evaluator accuracy improvement”，却没有公开 human-gold confusion matrix；
  更快执行也缺 hardware/concurrency contract，不能视为 verifier 更正确或通用更快。
- **What the Evidence Proves / Does Not Prove:** 证据支持 length/truncation/diversity controls 会改变所测 code-RL
  learning path，conditional masking recipe 在作者数据/模型上优于报告 baselines；不证明长答案本身更有 reasoning、
  去 KL/high clip 对所有任务安全、早期 length 限制普遍不可逆，或 4K cap 产生已测量的 40～50% 端到端节省。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** mask 保留探索，但会忽略真正错误的 truncated
  samples；高 temperature/clip 与无 KL 增加 drift、format failure 和 reward hacking；diversity proxy 可被无意义变化
  提高；宽松 evaluator 可放大 false positive。fixed temperature/KL、complete truncation mask 与 shorter outputs 在
  verifier 可靠、答案短、成本/SLO 严格时继续成立。下一阶段压力是 adaptive budget、verifier calibration 与
  outcome-conditioned—not length-only—credit。
- **Evolution Relationship:** `Direct Evolution`：fixed cap + terminal reward -> mask all truncations -> conditional
  truncation mask -> diversity-aware sampling/trust-region policy -> adaptive outcome/compute curriculum。`Layering /
  Dependency`：data difficulty -> rollout budget -> evaluator verdict -> group advantage -> clip/KL update；后发 recipe
  不能替代 reward correctness。
- **ROADMAP / Chapters Read / Existing Coverage:** 已阅读全文 Ch28/29，并复核 Ch23/62。Ch29 已覆盖 all-equal
  groups、length/reward correlation、KL/clip variants 与 verifier state；仍可补“length cap 形成 path-dependent
  curriculum”及 conditional masking 的 bias。主 owner 为 Ch29；Ch23/62 分别拥有 data/evaluator contract。
- **Integration Decision:** `Refine — TRAIN-GRPO / Ch33 / Experimental`。已补入 length/truncation/temperature/
  verifier 的 path-dependent curriculum 与 masking bias，不复制 recipe、benchmark 或未绑定硬件的效率数字。
- **Open Questions:** non-incorrect truncation 怎样用独立 verifier 校准？mask probability 与 max length 能否由
  expected value per token 自适应控制？去 KL/high clip 下怎样检测 semantic drift 与 reward hacking？

### Nemotron 3 Super — 28/30

- **Candidate / Week / Source Family**：`NEMOTRON3-SUPER-HYBRID-SPARSE-STATE-MODEL`；W10。Base BF16
  model card 明确 NGC/Hugging Face release 为 2026-03-04，post-trained FP8 card 为 03-11；51 页
  technical report 封面为 04-03，arXiv 2604.12374 v1 为 04-14。主事件按第一个可用 checkpoint 归 W10，
  后两次只作为同一 source family 的 checkpoint/formal-evidence 演进，不在 W11/W16 重复计分。
- **Direct / Related Primary Sources and Full-read Coverage**：已阅读 technical report 的 Pretraining、
  architecture/LatentMoE/MTP/hybrid anchors、NVFP4 stability、25T data/hyperparameters、1M extension、SFT、
  multi-environment RLVR/SWE-RL/RLHF、async infrastructure/resiliency、evaluation、FP8/NVFP4 PTQ、SSM-
  cache quantization、Appendix A/B；联合核验 base/post-trained BF16/FP8/NVFP4 model cards、公开 data/
  checkpoint/recipe 入口与 serving instructions。报告没有独立 Limitations/Threats、完整 hardware count/
  energy、per-stage causal ablation、seed/CI、training failure statistics 或跨 runtime production SLO。
- **Original Problem / Why Previous Designs Were Reasonable**：Dense Transformer 将每 token compute、总参数
  和 KV state 一起放大，质量可预测但 memory/communication 昂贵；标准 MoE 用少数 experts 解耦 total/
  active parameters，但低-latency 时仍读大 expert matrices，throughput 时又被 hidden-width×top-k 的 all-to-
  all payload 限制；纯 Mamba 用固定 recurrent state 降低长程 KV 成本，却弱化任意 token-to-token 的显式
  global interaction。旧方案在规模较小、互联充足或精确 attention 更重要时仍合理。
- **Changed Constraint / Mechanism**：88-layer stack 以 Mamba-2 + LatentMoE 为主并周期插入 attention
  anchors。LatentMoE 先以 learnable `W_down` 将 hidden width `d=4096` 投到 `l=1024`，在 latent space
  routing/expert compute，再以 `W_up` 回到 full width；理论上 routed weight load 与 all-to-all bytes 按
  `d/l` 缩小，节省预算用于扩大到 512 experts、top-22。routing gate、shared expert 与非-expert layers
  仍留在 full dimension，避免把所有表示都压过潜在 task-rank floor。两层 weight-shared MTP heads 同时
  提供 future-token auxiliary objective 与内生 draft，target model 一次验证多个 candidate tokens；少量
  attention anchors 恢复 global interaction，其余 recurrent layers 控制 decode state bytes。
- **State Ownership / Control and Data Flow**：router 拥有 token→expert assignment 与 load-balance state，
  latent projections 定义 dispatch payload coordinate；Mamba layer 拥有 recurrent SSM cache，attention layer
  拥有 KV cache，两类 state 不能被 runtime 当作同质 block。MTP heads 只拥有 draft logits，accept/reject
  与 rollback 仍由 target sampling/runtime 负责。训练侧 model server 保留 token/logprob/policy metadata，
  agent server 运行 rollout kernel，resource server 计算 verifier reward，NeMo RL controller/Megatron 更新
  policy；Ray/SLURM 只负责编排，不能成为 reward 或 environment truth owner。
- **Training / Implementation Contract**：120.6B total、12.7B active（不含 embedding 为 12.1B），25T
  tokens、sequence 8192、global batch 3072（约 25.17M tokens/batch），WSD schedule 在 200B tokens warmup
  到 4.5e-4，末 5T minus-sqrt decay 到 4.5e-6；AdamW `beta=(0.9,0.95)`、weight decay 0.1。NVFP4
  覆盖 weight/activation/gradient tensor path；Nano-scale instrumentation 发现小梯度 underflow，而 Super
  在 19T 切 MXFP8 到 20.6T 虽改善 loss、未带来持续 downstream gain，故最终沿 NVFP4 完成。post-
  training 为 7M SFT samples/80B tokens、multi-stage RLVR、SWE-RL 20B、RLHF、MTP healing 18B；RL
  使用 NeMo Gym/RL、Megatron、vLLM、Ray/SLURM，报告称扩到 1k GPUs。
- **Async / Failure Contract**：generation 与 training 解耦并固定 one-step off-policy earmarking；in-flight
  weight update 允许单 trajectory 混合不同 policy age 的 tokens/logprobs，且作者明确未重算已生成 KV
  cache。这提高利用率，却把 per-token policy version、cache-generation identity、importance correction、
  loss mask 与 recovery 变成训练状态。1k-GPU 规模暴露 port-binding race、shared-kernel Apptainer 中的
  runaway process/OOM 和 `killall/pkill` blast radius；memory watchdog 与 command blocklist 是工程缓解，
  不是强隔离或安全证明。
- **Quantization / Serving Contract**：FP8 checkpoint 使用 W8A8 expert/Mamba GEMMs、FP8 KV cache、FP16
  Mamba cache；NVFP4 checkpoint 通过 sensitivity+deployment-budget search 在 NVFP4/FP8/BF16 之间做 per-
  operator assignment，router 保持 FP32，QKV/attention/Mamba projections 中部分保高精度。PTQ 用单 B200
  节点 8 GPUs、512 samples×4096，约两小时；`99.8% median relative accuracy` 是作者 benchmark aggregation，
  不是逐任务等价。Mamba recurrent cache 的 rounding error 会随状态递推累积；FP16 stochastic rounding
  以无偏噪声替代 coherent drift，是该架构特有的 state-precision 约束，而非所有 cache 的通用配方。
- **Evaluation Contract / Performance Boundary**：headline `2.2×/7.5×` 绑定 8K input、64K output、B200、
  GPT-OSS MXFP4/MXFP8+FP8-KV、Qwen BF16，并为每个模型取 vLLM/TRT-LLM 中较优结果；没有统一 runtime、
  concurrency、TTFT/TPOT percentile 或质量完全匹配。MTP 图仅为 B300、TRT-LLM、TP=1、SPEED-Bench
  Throughput-1k、1K output，比较 draft depth 0/1/3；不能推出任意 batch/length 的加速。能力表混用官方、
  aggregator 与自测数字，且 Agent 分数依赖 OpenHands/OpenCode/Codex harness，不能归因于架构单项。
- **What the Evidence Proves / Does Not Prove**：公开结构、权重和训练/量化细节证明 hybrid state、latent
  dispatch、native draft 与 per-operator precision 必须共同进入 model/runtime contract；作者 ablations 支持
  latent projection 和 MTP 在所测设置下移动 accuracy/cost frontier。它不证明 LatentMoE 独立导致最终
  Agent benchmark、1M advertised length 等于所有 long-range task 有效、NVFP4 普遍优于 BF16、异步 mixed-
  age trajectories 无 bias，或 2.2×/7.5× 可迁移到其他 GPU/runtime/SLO。
- **Trade-offs / New Failure Modes / Previous Designs**：更窄 latent dispatch 降 bytes，却增加 down/up
  projections、组合 routing、top-22 load balance 与 expert-placement complexity；Mamba 减 KV bytes，却引入
  recurrent cache precision/error accumulation 和不可随机回看的 state semantics；attention anchors 恢复
  global mixing，也重新引入长度相关 KV。MTP 省 target passes 的条件是 acceptance 足够高，并新增 draft
  state/rollback；mixed precision 降 bandwidth，却需 sensitivity search、calibration、kernel/fusion support 与
  stochastic state update。Dense、standard MoE、pure attention、BF16 和 synchronous RL 仍分别适用于较小
  模型、简单 portability、精确 context interaction、数值审计和严格 on-policy 需求。
- **Evolution Relationship**：`Direct Evolution`：dense full-width MLP → standard sparse MoE → latent-
  coordinate routing/expert compute；pure attention → recurrent-heavy hybrid + sparse global anchors；external
  draft → model-native MTP draft；uniform dtype → operator/state-aware mixed precision；synchronous rollout/
  update → one-step stale async → in-flight mixed-policy trajectory。各路线是 layerable design branches，
  不是“新模型整体替代旧模型”。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch20～22、Ch24、Ch29、Ch41、Ch45。Ch21
  已覆盖 router/top-k/active-vs-total/All-to-All 和 DynaMoE 反例，但缺少“先改变 communication coordinate
  再增加 experts/top-k”的 LatentMoE 分支，主 owner 暂定 Ch21。Ch24 承接 low-precision gradient error-
  path，Ch29 承接 mixed-policy-age trajectory，Ch41/44 承接 heterogeneous cache/MTP verification，Ch45
  承接 deployment-restriction-aware per-operator precision；均只做短 handoff，避免复制整份模型报告。
- **Integration Decision / Open Questions**：`Refine — MODEL-MOE / Ch21 / Experimental`；已补入 latent-coordinate
  expert dispatch、projection cost 与 full-width MoE 共存条件。待核验 matched-parameter/FLOP/byte LatentMoE ablation、projection/
  top-k/anchor 独立贡献、training hardware/energy、MTP acceptance 对 batch/SLO 的 sensitivity、mixed-age
  trajectory correction、SSM-cache stochastic rounding 的跨任务/长度 variance，以及同 runtime/precision/
  quality/SLO 下的独立 serving reproduction。

### Recursive Language Models Meet Uncertainty：长上下文程序搜索的瓶颈从生成转向选择 — 25/30

- **Candidate / Week / Source Family:** Recursive Language Models Meet Uncertainty / SRLM / 2026-W10 / 25/30；
  `Source Family ID: srlm-uncertainty-guided-program-search`。
- **Source Type / Event Date / Revision History:** primary event 是 arXiv:2603.15653 的 sole v1，首发于
  2026-03-07；31 页 PDF 已完整读取。Apple Machine Learning Research 的 publication record 发布于
  2026-07，只作为作者与 publication-family 的后续官方核验，不把事件迁移到 7 月。未定位到作者公开代码、
  environment image 或可执行 artifact。
- **Full-read Coverage:** 已覆盖 metadata、Abstract、Introduction、RLM background、SRLM Method、选择公式、
  全部三组主实验、扩展 context-length/domain experiments、wall-clock comparison、selection-signal ablation、
  Related Work、Conclusion、Appendix A～C、dataset details、prompt、judge、confidence extraction 与 detailed
  results。论文没有独立 Limitations / Threats to Validity 小节，以下边界来自已披露方法与实验合同。
- **Original Problem / Why Previous Design Was Reasonable:** 大 context window 解决“输入能否被装入”的容量问题，
  RLM 再把 context 外置为 REPL variable，让模型用代码搜索、切片、聚合并可递归调用子模型。这在结构化搜索、
  精确字符串定位或需要分块处理时合理；但一条交互程序可能因为错误 search term、过早停止或中间状态污染而失败，
  单纯增加 context 或允许 recursion 不会自动选出正确 trajectory。
- **Changed Constraint / Principle:** 当 context 已可外置、系统又能生成多条 candidate programs 时，新的约束不再
  只是“模型能否访问信息”，而是“在没有外部 verifier 时，怎样选择更可能正确的程序轨迹”。长期原则是：
  **capacity、interaction policy、candidate coverage、trajectory selection 与 final acceptance 是五个不同层级；
  同源 uncertainty proxy 只能改善 selection，不能升级为 correctness proof。**
- **Mechanism:** SRLM 不要求 recursive self-query，而是独立采样 `K=8` 条 REPL programs。系统先取最终答案的
  plurality 形成 self-consistency 集合，只保留与 plurality answer 一致的轨迹；再对每一步模型 verbalized
  confidence 的 log value 求和，并以完整 trace token length 作为 behavioral proxy，在一致集合中用
  `VC(p) * Len(p)` 排序。两项值均不大于零，选择乘积最大、即最接近零的 trajectory。它没有引入独立 reward、
  gold label 或可执行 verifier，而是把“答案簇 + 自报置信度 + 行为长度”组合成无监督 selector。
- **State Ownership / Control Flow / Data Flow:** sandbox/REPL 拥有外置 context、代码执行结果与 mutable execution
  state；generator 拥有 program steps、终止答案与 token-level输出；selector 拥有 candidate set、normalized
  answer identity、plurality group、per-step confidence log 与 trace length；GPT-5-mini judge 只拥有离线评测 verdict。
  数据流为 `context C -> K program trajectories -> execution states/answers -> plurality filter -> confidence/length
  ranking -> selected answer -> external benchmark judge`。若 plurality group 共同错误，后两项 proxy 无法恢复被
  过滤掉的少数正确答案。
- **Implementation Details:** 两个主 backbone 为 Qwen3-Coder-480B-A35B 与 GPT-5 medium reasoning；GPT-5-mini
  同时用于 RLM recursive subcall 与最终 semantic-equivalence judge。所有方法共享 RLM REPL；每条 trajectory
  最多 30 个 interaction steps、每步 600 秒，Qwen 路径最多生成 260K tokens，GPT API 使用默认限制。缺失
  confidence 时，以同一 trajectory 其他 step 的平均 confidence 填补。这个 imputation、answer normalization、
  judge prompt 与停止规则都是 selector/evaluation identity，而不是无关实现细节。
- **Evaluation Contract:** 主实验使用 BrowseComp+ 的 150 个样本、约 5.4M～11.1M context；OOLONG
  `trec_coarse` 的 50 个 131K 样本；LongBench-v2 CodeQA 的 50 个样本。扩展实验覆盖 OOLONG 约 650 个
  1K～4M 样本和 LongBench-v2 全 503 个、六个 domain、8K～4M context。baseline 包括 base LLM、
  CodeAct+BM25、CodeAct+subcalls、summary agent、depth-1 RLM 与 no-subcall RLM。论文没有披露执行硬件、
  API revision、总 calls/tokens/FLOPs、价格、并发资源 envelope、seed/CI 或 production SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** 作者按 backbone、task、context length 比较 recursion 与
  self-reflective selection，并分别消融 self-consistency、verbalized confidence 与 trace length；完整组合在作者
  聚合实验中最好，但 confidence 或 length 单独都不与正确性严格单调。`K=8` trajectories 并行执行使报告的
  wall-clock 没有等比例增加，却不代表 compute、token、call、GPU 或 API cost matched；因此不能把较低延迟
  直接解释为更高资源效率。
- **What the Evidence Proves:** 在作者模型、任务、REPL、judge 与采样合同下，多轨迹生成之后使用组合 proxy
  选择，优于其所比较的单轨迹 RLM，且 recursion 的收益依 backbone/task/context 而变化。结构化、搜索导向的
  code/data tasks 更可能受益于 recursive traversal；语义文档/对话类任务在作者实验中更常受益于 self-reflective
  selection。这支持“long-context policy 必须包含 trajectory-selection state”，而不是一个固定 recursion 开关。
- **What It Does Not Prove:** 作者报告的最高相对改进不能外推到其他模型、工具、context distribution 或等成本
  服务；它不证明 recursion 已过时、self-report 是 calibrated uncertainty、trace 越短越正确，或 self-consistency
  等于外部事实。GPT-5-mini 同时进入 recursive path 与 judge，增加相关误差；没有代码、独立 reproduction、
  human-gold confusion matrix 或 resource-matched baseline。
- **Trade-offs / New Failure Modes:** 多轨迹提高 coverage，却线性增加潜在 calls、tokens 与 sandbox state；
  plurality 对 correlated wrong answers 敏感；verbalized confidence 可 miscalibrated 或被策略性迎合；length proxy
  会惩罚真正困难但正确的长轨迹；confidence imputation 可能掩盖关键 step 的缺失；外置执行状态还引入 sandbox
  isolation、timeout、nondeterminism 与 replay identity。selector 越复杂，越需要记录 candidate set 与决策轨迹，
  否则无法复现为何某个答案胜出。
- **Where Previous Designs Still Apply:** 当答案可一次生成、context 较短或成本/SLO 严格时，direct prompting
  仍合理；BM25/typed retrieval 在索引稳定、查询明确时更便宜可审计；summary 适合容忍有损压缩的语义任务；
  recursion 在可分解、结构化 search/computation 上继续成立；独立 executable verifier 在存在确定规则时仍比
  同源 proxy 更强。SRLM 是 selector 分支，不是对这些路径的覆盖或否定。
- **Evolution Relationship:** `Direct Evolution`：扩大 raw context window -> 外置 context + programmatic RLM
  traversal -> 多条 context-interaction programs -> uncertainty-proxy trajectory selection -> 独立 verifier/
  abstention 与 resource-aware controller。`Layering / Dependency`：context capacity -> access/traversal policy ->
  candidate coverage -> selection -> acceptance；后层不能修复前层遗漏，也不能把同源信号变成 ground truth。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage:** 主 owner 为 Ch22 Long Context；已阅读
  Ch22 及 Ch72 RAG、Ch76 Reflection、Ch62 Evaluation。Ch22 已区分容量、有效利用、RAG/summary/memory，
  但尚未明确“context-interaction program 的候选集合与 selection state”；Ch76 已覆盖 same-model self-critique
  的 correlated-error boundary，Ch62 已覆盖 scorer identity、uncertainty 与完整成本合同，二者只作 handoff；
  Ch72 承接 retrieval/context access policy，不复制 selector 机制。
- **Integration Decision:** `Refine — MODEL-LONG-CONTEXT / Ch22 / Experimental`。已把 long context 从容量/检索
  推进到 programmatic interaction、candidate-program state 与 trajectory selection，同时保留 direct、retrieval、
  summary 与 recursive traversal 的成立条件，不写作者模型排名或 22% headline。
- **Open Questions:** 怎样在 matched calls/tokens/FLOPs/latency/cost 下比较单轨迹 recursion 与 K-way selection？
  answer clusters 共同错误时，何种独立 verifier 或 abstention 可越过 plurality failure？confidence/length proxy
  如何跨 model、task 与 context length 校准？program、sandbox snapshot、tool revision 与 selector decision trace
  如何组成可回放 artifact？

## Evidence Level

- **Source/date screened (36/36 scored):** 原 34 项、Nemotron 3 Super 与 SRLM 均已核对 primary metadata、
  v1 date、source-family 与归周；这不替代正文、实验与 artifact 阅读。
- **Current-gate Full Source Review complete (36/36 scored; 0 pending):** 原 34 项均已完成；Nemotron 3 Super 的
  51 页报告、model cards、checkpoints/data/recipe 与章节邻接，以及 SRLM 的 31 页全文、Appendix、实验合同、
  proxy-selection 边界和 Ch22/72/76/62 邻接均已完成。原 23 项均已完成；新增 MLRA、DistriVoting、ProRes、
  BandPO、Sparse-BitNet、ATLAS、Terminal Coding Agents 与 AutoResearch-RL 已完成全文、实验合同、限制、
  目标章节与 artifact（存在时）复核；AutoResearch-RL 因管理员撤稿降级为 `Withdrawn / Disputed`；
  Hindsight Credit Assignment、Scaling Data Difficulty 与 MicroCoder-GRPO 也完成了 Method、实验、Appendix、
  限制、artifact gap 与目标章节核验。原 candidate set 中，FlashPrefill 已完成论文、Appendix、官方代码、
  runtime patch 与 Ch38～40 联读；CoVe 已完成论文、project/model/dataset artifacts 与 Ch22～24 联读；
  Memex(RL) 已完成论文、Appendix、后续官方代码 artifact 与 Ch72～74 联读；SWE-CI 已完成 v1/v4、
  官方 code/config 与 Ch61～63 联读，并纠正跨 revision 反转的
  provider-strategy 归因；KARL 已完成 77 页论文、全部 Appendix、Databricks 官方 PDF 与 Ch71～73 owner
  去重，并将公开 artifact 缺失和 data-pipeline 内部矛盾保留在证据边界；CoT-Control 已完成论文、Appendix、
  官方 harness/grader 与 Ch62/68 安全边界联读，并把 proxy controllability 与 monitorability/faithfulness 分离；
  SageBwd 已完成论文、全部 Appendix、相关官方 repository 与 Ch23～25 owner 联读，并把 dS sensitivity、
  TPS/noise、QK-norm 与 smoothing 机制分离；MemSifter 已完成论文、Appendix、官方 training/reward/
  merge/toolkit 与 Ch72～75 联读，并把 raw fact state、learned retrieval-policy state、working-model/scorer
  identity 与 coarse-filter recall ceiling 分离；V1 已完成论文、全部 Appendix、algorithm/prompt/
  hyperparameters 与 Ch19～21 联读，并把 parallel coverage、pairwise selection、self-verifier correlation、
  call-count budget 与 executable acceptance 分离；Interactive Benchmarks 已完成 v1/v4 全文、Appendix、
  partial official code 与 Ch61～63 联读，并把 static answer、candidate coverage、feedback-conditioned policy、
  judge/environment identity 与真实 compute/cost 分离；RubricBench 已完成论文、Appendix、official
  dataset/evaluator 与 Ch61～63 联读，并把rubric formation、rubric execution、semantic matcher与公开
  benchmark contamination分离；IF-RewardBench 已完成论文、Appendix、official data/inference/metrics code
  与Ch61～63联读，并把local verification、global ranking、Pareto graph、parser fallback与instruction hierarchy
  分离；DynaMoE已完成论文、Appendix、pseudocode与Ch21/32/40/45联读，并识别percentile selector实际
  cardinality、activation-space theorem、overflow claim与standard-baseline缺失的central conflict，状态为
  `Disputed / Weekly Only`；HACRL/HACPO已完成v1/v2、全部Appendix、official code与Ch28～31/78联读，
  将cross-policy rollout reuse与inference multi-agent分离，并把oracle unbiasedness、finite-batch ratio、
  tokenizer coordinate、clipping bias、双模型runtime cost与shared-verifier failure纳入边界。其余十三项Books
  候选结论保持`Experimental`；MUSE已完成全文、Appendix、official web app与Ch62/67～69联读，把安全评估
  对象从单次prompt扩展为带turn/modality/media/provider/judge/stop state的run，并将single-turn与multi-turn、
  modality transition因果、同源attacker/judge与public code缺失保留为证据边界；MOOSE-Star已完成v1/v4全文、
  theory/evaluation appendices、official code与Ch75/72/62/77联读，将特定latent-search formulation与通用训练复杂度
  分离，并识别best-case`O(log N)`、citation-derived ground truth、temporal reconstruction与parser fallback的边界，
  状态为`Disputed / Weekly Only`；Phi-4-reasoning-vision-15B已完成technical report、Appendix、model card、
  official repo与Ch23～25/17/20/62联读，把mid-fusion、visual-token budget、multimodal data correction与mixed
  reasoning-mode SFT连成同一能力/计算合同，并保留5B ablation、single-request H100 timing、safety rate与artifact
  provenance边界；T2S-Bench已完成45页全文、Appendix、official project/data/evaluator artifacts与Ch70～72/62
  联读，纠正oracle-conditioned node/link subtasks不等于自由端到端graph extraction、semantic similarity不等于
  entity accuracy、SoT prompt未做matched-compute causal test以及`100 epochs`/`200 steps`训练合同冲突，状态为
  `Weekly Only / No Books Change`；CRISP/OPSDC已完成v1/v7全文、全部Appendix、official trainer/worker/
  reverse-KL/scorer/checkpoint artifacts与Ch24～31/20/62联读，识别student-prefix contextual-logit distillation、
  periodic teacher state与refresh collapse，并用v7 dual-path scorer纠正v1大幅accuracy gain中的format confound，
  状态为`Books Candidate / Refine Ch25 / Experimental`；MASQuant已完成全文、公式/proof、全部消融、
  official calibration/inference/low-rank artifact与Ch16～18/23/31/44～46联读，将统一scale、per-modality
  scale、duplicated weights与shared base + conditional correction重建为完整演进，并把theorem、mask、base
  modality、kernel与服务性能边界分离，状态为`Books Candidate / Refine Ch45 / Experimental`；GPT-5.4已完成
  official release与完整Deployment Safety card复核，并将model/product、tool-search catalog、computer-use
  confirmation、harness、monitor与actor enforcement分层；Ch74/68/62已有相同长期机制，状态为
  `Weekly Only / No Change / Version Fact`；Anthropic labor-market report已完成正文、11页Appendix、usage gate/
  weighting、occupation/CPS crosswalk、DID、cutoff/UI robustness与Figure 7 correction复核，把theoretical capability、
  provider-specific observed exposure、adoption、automation和employment outcome分成五层；Ch62/63已有相同长期
  evidence contract，状态为`Weekly Only / No Change`；WAXAL已完成 arXiv v1/v3、Google official release、
  dataset card v2.0.0、schema/split/provider-license 与 Ch22～24/11/62 联读，识别 collection protocol、
  partition-level ownership/policy、speaker-disjoint split缺失，以及 19/24/27 languages、180/235/565h 与
  CC-BY/CC-BY-SA 的 official-artifact冲突，状态为`Books Candidate / Refine Ch23`。
- **Recorded Candidate Evidence Complete / Archive Gate Open:** 36 个 scored candidates 均有 current-schema
  Full Source Review 或可信拒绝核验，当前没有 `Audit Pending`。这关闭的是已记录候选 queue，不证明
  Google Scholar、OpenAlex、Hugging Face 与同周工程 release 的历史召回数学完备；故 broader W10 Discovery
  discovery recall 仍未独立闭合；这只保持 Archive Completion Gate Open，不撤销已完成的 Source-Family Books Gate。
- GPT-5.4 页面与 system card 只能证明发布范围和安全评估边界；benchmark 属厂商结果。劳动市场
  与 WAXAL 结论分别受样本、taxonomy、artifact revision、语言覆盖和任务设置限制。
- 论文或官方材料缺少 evaluation/artifact 时已明确记录 `Not Disclosed`；任何作者倍率、厂商 benchmark、
  dataset headline 或跨版本数字都没有被外推为通用结论。

## Cross-Week Deduplication

后续 GPT-5.4 mini/nano 归为同一 model-family 的 cost/latency branch，不重复宣称新架构。
Qwen3-Coder-Next 与 SkillNet 按 first-public date 归回 W09；discovery 页面日期不参与归周。

## Knowledge Tree Position

本周候选横跨 Ch14～15/17/20～24/27～29/32～33、Ch41/43/45～46、Ch50、Ch62/66/68～69、
Ch72～75/77～78。
初始 owner 只是待验证假设；一个候选最终只保留一个主 owner，其余章节使用短 handoff。

## Recommended Action

1. 36 个候选已完成 owner/adjacent-chapter 去重和最终 disposition；只把 27 项的长期机制融入 15 个 Stable Node owners。
2. Sparse-BitNet 因 paper/code 的 operator-order 冲突保持 `Weekly Only / Disputed`；AutoResearch-RL 因正式撤稿保持
   `Weekly Only / Withdrawn`。二者不得成为 Books 机制证据。
3. OpenDev 与 Scaling Data Difficulty 分别由 Ch78/81/84 的 authority/recovery 合同、Ch27 的 policy-relative
   difficulty/lineage 合同完整覆盖，故为 `No Change`，不为增加 diff 重复写入。
4. Archive Completion Gate 保持 Open，继续记录 Scholar/OpenAlex/Hugging Face 与同周工程 release 的历史发现限制；
   该限制不撤销已完成 Source Review 的 36 个 Source Families，也不被误写成绝对 recall 完备。

## Event-Date Daily Decision

Historical Backfill 只维护完整 ISO Weekly，不补造 2026-03-02～03-08 Daily。事件日期、revision、
source-family 与最终 disposition 直接记录在本周档案。

## Final Source-Family Books Integration

`Source-Family Books Gate Complete — 36/36 final dispositions: 27 Refine, 4 No Change, 5 Weekly Only/Disputed`。
Archive Completion Gate 仍为 Open：历史 discovery coverage 尚未独立闭合，但 36 个已记录 Source Families 的
primary-source、owner、相邻章节和最终 disposition 已逐项复核。

| Stable owner / Current chapter | Integrated source families | Result |
| --- | --- | --- |
| `MODEL-MULTI-HEAD-ATTENTION` / Ch15 | MLRA | compressed-state shardability and partition axis |
| `MODEL-SAMPLING` / Ch20 | V1, DistriVoting | coverage/selection graph and query-local distribution state |
| `MODEL-MOE` / Ch21 | Nemotron 3 Super | latent-coordinate expert dispatch |
| `MODEL-LONG-CONTEXT` / Ch22 | SRLM | context-interaction program and trajectory selection |
| `TRAIN-DATA` / Ch27 | WAXAL, CoVe, Phi-4-reasoning-vision | collection/artifact contract, executable specification and data-tagged compute policy |
| `TRAIN-PRETRAINING` / Ch28 | SageBwd, Progressive Residual Warmup | precision-sensitive backward path and depth-time branch activation |
| `TRAIN-SFT` / Ch29 | CRISP | same-prefix context distillation and teacher lifecycle |
| `TRAIN-GRPO` / Ch33 | HACRL, BandPO, HCAPO, MicroCoder-GRPO | cross-policy provenance, trust region, hindsight relevance and truncation curriculum |
| `INFER-PREFILL` / Ch43 | FlashPrefill | sparse discovery/index-build cost and fallback |
| `INFER-TENSORRT-LLM` / Ch49 | MASQuant | distribution-conditioned precision and execution contract |
| `PLATFORM-EVALUATION-SYSTEM` / Ch66 | RubricBench, SWE-CI, Interactive Benchmarks, IF-RewardBench | specification, interaction and aggregation identity |
| `PLATFORM-SECURITY` / Ch72 | MUSE, CoT-Control | run-level multimodal threat state and monitorability boundary |
| `AGENT-RAG` / Ch76 | KARL | joint query/compression/verify/stop policy |
| `AGENT-MEMORY` / Ch77 | MemSifter, Memex(RL) | fact/policy state and compact-control/exact-archive split |
| `AGENT-WORKFLOW` / Ch81 | ATLAS | lazy schema exposure and persistent interpreter boundary |

四项 `No Change` 均有章节级依据：GPT-5.4 只有 Version Fact 且内部机制未公开；labor-market report 没有改变
Ch66 的 evidence contract；OpenDev 的 capability separation、compaction、loop/recovery 已由 Ch78/81/84 覆盖；
Scaling Data Difficulty 的 model-relative difficulty、verifier/checkpoint identity 与 lineage 已由 Ch27 覆盖。

五项 `Weekly Only/Disputed` 为 DynaMoE、MOOSE-Star、T2S-Bench、Sparse-BitNet 与 AutoResearch-RL：分别因
机制推导争议、复杂度/效果主张争议、没有新增长期机制、artifact 顺序冲突和正式撤稿而不进入 Books。

## Pre-Integration Decision Snapshot（Superseded）

`Recorded Candidate Evidence Complete — 36/36 scored candidates reviewed; 0 pending; broader Discovery
Gate Open; Historical Books Integration Blocked`。

原 23 项候选均已有最终 disposition；新增 11 项已全部完成 Source Review 或可信拒绝核验。AutoResearch-RL
因管理员撤稿不会进入 Books，其余 10 项仍需逐项章节去重，当前不得标记 Books Integration complete。
原 `Books Integration Complete` 仅对旧 candidate set 成立，不再描述当前完整 W10。SRLM 已完成 Source
Review，并在该历史检查点暂定 Ch22 refinement。该段只保留最终 Books pass 之前的审计状态；当前状态以上方
Final Source-Family Books Integration 和 Candidate Scoring 最终列为准。

- WAXAL：`Refine — Ch23 Integrated`；补入 collection protocol、partition-level policy、group-disjoint split 与
  artifact supersession，未复制数据规模和发布摘要。
- CoVe：`Refine — Ch23 Integrated / Experimental`；补入 executable-specification compilation、verifier lineage
  与 shared-blind-spot boundary。
- Phi-4-reasoning-vision-15B：`Refine — Ch23 Integrated / Experimental`；补入 data-tagged compute policy、
  visual-token evidence budget 与外部 routing 共存边界。
- V1：`Refine — Ch20 Integrated / Experimental`；补入 coverage/selection 分层、comparison-graph state、
  self-verifier 相关错误、abstention 与真实 compute contract。
- SageBwd：`Refine — Ch24 Integrated / Experimental`；补入 backward sensitivity、precision boundary、
  batch-noise 与 long-horizon convergence contract。
- CRISP/OPSDC：`Refine — Ch25 Integrated / Experimental`；补入 same-prefix context distillation、teacher
  snapshot/refresh state 与 correctness/format/length 解耦。
- HACRL/HACPO：`Refine — Ch29 Integrated / Experimental`；补入 source-tagged cross-policy experience、
  tokenizer/probability-coordinate ownership、finite-batch bias 与退出共享条件。
- FlashPrefill：`Refine — Ch39 Integrated / Experimental`；补入 sparse discovery/selection/index-build cost、
  ephemeral index state、dense fallback 与 `q_len/k_len` 组合边界。
- MASQuant：`Refine — Ch45 Integrated / Experimental`；补入 distribution-conditioned scales、shared base +
  conditional correction、mask routing 与 modality-sliced deployment contract。
- SWE-CI 与 Interactive Benchmarks：`Refine — Ch62 Integrated / Experimental`；补入 static、candidate
  coverage、feedback-conditioned trajectory、state evolution、temporal policy 与完整 interaction-cost contract。
- RubricBench 与 IF-RewardBench：`Refine — Ch62 Integrated / Experimental`；补入 rubric formation、criterion
  execution、local verification、partial-order/global ranking、parser 与 aggregation policy 分层。
- MUSE：`Refine — Ch68 Integrated / Experimental`；补入 run-level multimodal threat state、harmful-media
  lifecycle、旧测试共存条件和 judge/causal boundary。
- CoT-Control：`Refine — Ch68 Integrated / Experimental`；补入 controllability、monitorability、faithfulness、
  outcome safety 分层，以及 attempt/feedback/action-verifier threat contract。
- KARL：`Refine — Ch72 Integrated / Experimental`；补入 query/compression/verify/stop joint policy、
  shorter-trajectory ambiguity、credit boundary 与 train/eval/serve harness identity。
- Memex(RL)：`Refine — Ch73 Integrated / Experimental`；补入 compact control state、versioned exact evidence
  archive、stable reference contract 与 read/write learning/durability 边界。
- MemSifter：`Refine — Ch73 Integrated / Experimental`；补入 fact state 与 parameterized selection-policy state
  分离、working-model/reward identity、coarse-recall ceiling 与 read/write cost migration。
- SRLM：当时为 `Refine candidate — Ch22 / Experimental / Provisional`；其后已在
  `MODEL-LONG-CONTEXT` / Ch22 完成 context-interaction program、candidate coverage、trajectory selection
  与 acceptance 分层。

## Ignored Noise

- 缺少 tool budget、software image、input length 与 sampling policy 的横向模型排名。
- 只看 abstract 或项目 headline 就把 memory、Agent RL、judge 或 sparse prefill 写成默认架构。
- 把作者峰值倍率脱离 model、hardware、precision、length、batch、concurrency、baseline 与 SLO 外推。

## Repository Changes

- 重开并扩充本文件：候选先由 3 项恢复为 23 项，后由 W11/W12 discovery 补回 W10 spillback，当前为
  36 个 scored candidates、0 pending；新增 spillback intake ledger，并完成 MLRA、DistriVoting、ProRes、BandPO、Sparse-BitNet、ATLAS、
  Terminal Coding Agents、AutoResearch-RL、HCAPO、Scaling Data Difficulty 与 MicroCoder-GRPO 十一份
  非模板化 Full Source Review；AutoResearch-RL 按正式 withdrawal 降级。Nemotron 3 Super 从 W16 回拨并
  完成第 35 份 review；SRLM 完成第 36 份 review，已记录候选 queue 闭合，但 broader Discovery Gate 仍 open。
  Qwen3-Coder-Next、SkillNet 按 first-public date 归回 W09。
- 将 SWE-CI、Interactive Benchmarks、RubricBench 与 IF-RewardBench 的四份 Source Review 合并回 Ch62
  的两个长期机制：stateful evaluation object 与 specification/execution/aggregation split；保留 snapshot、
  exact verifier、human review 和 partial order 等旧分支，未复制模型排名或 benchmark 数字。
- 将 MUSE 与 CoT-Control 合并回 Ch68 的 run-centric safety 与 sensor/authority 分层；保留 single-turn、
  isolated-modality、human red team、output inspection 和 deterministic authorization 分支，未外推 ASR 或
  controllability proxy 为生产安全保证。
- 将 KARL 的 joint retrieval/compression/stopping policy 整合到 Ch72；将 Memex(RL) 的 compact-control/
  exact-archive 分层与 MemSifter 的 fact/policy-state 分层整合到 Ch73。未复制作者模型排名、任务分数、
  QPS、单卡 latency 或固定 RL 配方。
- 完成 FlashPrefill 的论文、Appendix、官方代码与 Ch38～40 联读；owner 从初筛 Ch41 修正为 Ch39，
  并记录 score-ranking 与 index-compaction sort、`q_len == k_len`、batch=1、chunked/prefix-cache disabled
  等证据边界；随后在 Ch39 完成 sparse-Prefill selection-cost 与 fallback 机制整合。
- 完成 CoVe 的论文、project/model/dataset artifacts 与 Ch22～24 联读；owner 确认为 Ch23，并记录
  constraint/verifier 同源盲区、RL 未超过 SFT、simulator bottleneck 以及官方 code 未定位的边界。
- 完成 Memex(RL) 的论文、Appendix、后续官方 code artifact 与 Ch72～74 联读；owner 确认为 Ch73，
  并记录 conditional theorem、benchmark interface bias、index overwrite 以及生产 durability/governance gap。
- 完成 SWE-CI 的 v1/v4、官方 repository/config 与 Ch61～63 联读；owner 确认为 Ch62，并记录 oracle-target
  boundary、trajectory metric policy、harness revision identity，以及 v1/v4 provider-strategy 归因反转。
- 完成 KARL 的 77 页论文、全部 Appendix、Databricks 官方 PDF 与 Ch71～73 去重；owner 确认为 Ch72，
  并记录 query/compression/stopping 联合 policy、OAPL 粗粒度 credit、train/eval/serve harness identity、
  public artifact 缺失与 Quality Filter 叙述矛盾。
- 完成 CoT-Control 的论文、Appendix、官方 QA/Agent harness 与 grader，并联读 Ch5、Ch62、Ch67～69；
  owner 确认为 Ch68，记录 proxy controllability 不等于 monitorability/faithfulness、grader 的长度与 parsing
  coupling、跨 provider channel 不同构，以及 repeated-attempt threat model。
- 完成 SageBwd 的论文、Appendix A～C、相关 SageAttention 官方 repository 与 Ch23～25 联读；owner 从
  Ch32 修正为 Ch24，记录 dS 弱信号的量化放大、dP 精度保留、QK-norm/K-smoothing 的非对称作用、TPS 与
  gradient-noise 混杂，以及 SageBwd code 未公开定位的 artifact 边界；随后在 Ch24 完成 sensitivity-aware
  precision policy 整合，未复制作者硬件吞吐或固定低比特配方。
- 完成 MemSifter 的论文、Appendix A/B、官方 training/reward/merge/toolkit 与 Ch72～75 联读；owner 确认
  为 Ch73，记录 raw fact state 与 learned retrieval-policy state分离、working-model/scorer identity、
  coarse-filter recall ceiling、read-time/write-time cost迁移、paper/code 的 GRPO/DAPO边界，以及 dataset
  count/sample contract不一致。
- 完成 V1 的论文、Appendix A～H、algorithm/prompt/hyperparameters 与 Ch19～21 联读；owner 从 Ch43
  纠正为 Ch20，记录 candidate coverage 与 selection分离、comparison-graph state、self-verifier correlated
  error、model-score差不等于calibrated uncertainty、call count不等于compute，以及official code未定位；
  随后在 Ch20 完成机制整合，未复制作者 benchmark 或固定预算配方。
- 完成 Interactive Benchmarks 的 v1/v4、Appendix、部分官方 code artifact 与 Ch61～63 联读；owner
  确认为 Ch62，记录历史 v1 与后续 UI2Html revision 的事件边界、static/pass@k/interactive 的不同评估对象、
  feedback/judge/environment ownership、player-token 不等于系统 compute/cost，以及 paper/code revision
  未完全对齐。
- 完成 RubricBench 的论文、Appendix A～F、official dataset/evaluator 与 Ch61～63 联读；owner确认为
  Ch62，记录rubric formation与execution的双重failure、semantic matcher也是metric state、human rubric只是
  controlled upper bound、hard-case selection与公开gold的污染边界，以及repo只能复现accuracy aggregation而
  不能复现完整paper pipeline。
- 完成 IF-RewardBench 的论文、Appendix A～G、official data/inference/metrics code 与Ch61～63联读；
  owner确认为Ch62，记录local verification与global ranking分离、Pareto-only graph的选择边界、system/user
  hierarchy、pairwise-to-Elo aggregation，以及constraint parser缺项默认positive对metric identity的影响。
- 完成DynaMoE论文、Appendix、pseudocode与Ch21/32/40/45联读；将评分从20/30纠正为15/30并标记
  `Disputed / Weekly Only`：固定per-token percentile对连续scores近似产生固定cardinality，不能支持variable-K
  与activation-space theorem；minimum-activation也不处理per-expert overflow，且缺standard MoE baseline、
  matched compute、Transformer实验与official code。未修改Books。
- 完成HACRL/HACPO的v1/v2、Appendix、project page、official HACRL-code与Ch28～31/78联读；评分从24/30
  调整为23/30，owner确认为Ch29。记录cross-policy rollout reuse的source-policy/tokenizer/version state，
  区分oracle无偏与finite-batch/clipped objective，补充near-zero capability denominator、shared-verifier error、
  retokenization与双模型runtime成本，并确认它不是推理时Multi-Agent；随后在 Ch29 完成 cross-policy
  experience reuse 的机制整合。
- 完成MUSE全文、Appendix、official web app与Ch62/67～69联读；评分从24/30调整为23/30，owner确认为
  Ch68。记录run-level multimodal threat state、partial-compliance taxonomy、media/provider/judge identity，
  并指出single-turn/direct-goal与multi-turn/rewritten workflow不可直接作单变量归因，fixed modality rotation
  不能证明transition causality，同源GPT-4o attacker/judge及100条单annotator复核不足以形成ground truth；
  论文所称public source code未定位。本检查点未修改Books。
- 完成MOOSE-Star的v1/v4全文、全部Appendix、official repository、hierarchical search与IR probability
  extractor，并联读Ch75、Ch72、Ch62与Ch77；评分从22/30调整为17/30并标记`Disputed / Weekly Only`。
  核心纠正是：`O(N^k)`只来自论文选定的显式latent-inspiration search formulation，不是所有直接`P(h|b)`
  训练的下界；`O(log N)`只是ideal routing的best case。另记录citation-derived label、target-reconstruction judge、
  unmatched call-count budget，以及format重试耗尽后uniform probabilities被deterministic argmax变成首位置偏置。
  Ch75/72/62/77已覆盖可取机制，本检查点未修改Books。
- 完成Phi-4-reasoning-vision-15B technical report、Appendix A、Microsoft Research说明、official model card、
  GitHub与runtime入口，并联读Ch23～25、Ch17、Ch20与Ch62；owner从错误的Ch27修正为Ch23。保留mid-fusion
  复用、visual-token感知/成本边界、三阶段SFT、synthetic correction与mixed mode机制，同时限定5B ablation、
  H100 batch-1/no-concurrency timing、自报safety defect rate和不完整data/log provenance。本检查点未修改Books。
- 完成T2S-Bench 45页全文、全部Appendix、official project/repository、公开evaluator与Ch70～72/62联读；
  评分从20/30调整为18/30，owner从Ch62修正为Ch71，状态为`Weekly Only / No Books Change`。记录MR无需
  输出graph、E2E node/link任务分别注入oracle links/nodes、node semantic similarity并非离散accuracy、SoT
  prompt未对齐token/FLOPs/latency/cost、source-level split与IAA未披露，以及主文`100 epochs`和Appendix
  `约200 steps`的训练合同冲突。现有Ch71/70/62/72已覆盖可取的typed-state与评估边界，本检查点未修改Books。
- 完成CRISP/OPSDC v1与当前v7全文、全部Appendix、official repository、data builder、trainer/worker、
  reverse-KL实现、launch config、dual-path scorer和checkpoint index，并联读Ch24～30、Ch20、Ch31与Ch62；
  owner从错误的Ch28/29修正为Ch25。确认核心机制是同一student prefix上有/无conciseness context的full-vocab
  logit distillation，periodic teacher refresh把snapshot/cadence/sync变成训练状态；同时纠正v1 Qwen3大幅accuracy
  gain主要混合单路径answer-format scorer，v7 dual-path scorer下结论收缩为压缩且大体保持准确率；随后在
  Ch25 完成 context-distillation 机制整合。记录token-mean/
  partial-rollout objective不等于完整sequence KL、difficulty/error理论的强假设、dual-forward/rollout成本与current
  code旧注释语义。本检查点未修改Books。
- 完成MASQuant v1全文、全部公式/proof、实验/消融、official README、calibration/inference与low-rank
  implementation，并联读Ch16～18、Ch23、Ch31、Ch44～46；评分维度从`SR4/L3`修正为`SR3/L4`而总分
  保持23，owner从错误的Ch17/27修正为Ch45。重建uniform smoothing -> modality-specific scales -> duplicated
  weights -> shared base + conditional low-rank correction演进；同时限定SQNR theorem的分布假设、low-rank theorem
  的两模态/weight-only objective、text-base decode边界，以及只覆盖RTX 4090/Qwen2.5-VL-7B/W4A4/seq2048/
  prefill/BS1或8的性能合同；随后在 Ch45 完成 distribution-conditioned quantization 机制整合。
- 完成GPT-5.4 official release与完整Deployment Safety card复核，区分首发GPT-5.4 Thinking、ChatGPT/Codex/
  API surface、后续mini appendix及4月CoT section update；记录tool-search为deferred schema exposure、computer-use
  confirmation policy与model proposal/platform authority分离，并把vendor benchmark、mutable search environment、
  capability lower bound和model/monitor/actor-level safety stack限制在各自证据合同。Ch19～21、61～63、67～69、
  73～75已覆盖长期机制，最终状态为`Weekly Only / No Change / Version Fact`，未修改Books。
- 完成Anthropic labor-market impact report正文、11页Appendix与2026-03-08 Figure 7 correction复核；核对
  theoretical exposure、Claude usage/frequency gate、work/API/automation weighting、task-time aggregation、O*NET-
  CPS crosswalk、DID、treated-cutoff与insured-unemployment robustness。将capability、provider observation、adoption、
  automation与labor outcome分层，并保留single-provider selection、rare-task censoring、task dependency、parallel-
  trend/power与young-worker hiring弱证据边界。Ch61～65已覆盖可取evidence contract，最终状态为`Weekly Only /
  No Change`，未修改Books。
- 完成WAXAL arXiv v1/v3、Google Research release、dataset card v2.0.0、schema/split/provider license与
  Ch22～24/11/62联读；将评分轴从`SR4/PR3`修正为`SR3/PR4`而总分保持20。确认active collection protocol
  是training-distribution specification的一部分，并记录paper/blog/card在19/24/27 languages、180/235/565h、
  CC-BY/CC-BY-SA上的冲突、公开schema与paper metadata差异及speaker-disjoint split未证明。状态为
  `Refine — Ch23 Integrated`。已更新 `books/part-03-training-system/23-data.md`，沉淀 acquisition protocol、
  partition-level authorization、group-disjoint split 与 immutable artifact contract；未修改 Ch11/62。
- 将 CoVe 与 Phi-4-reasoning-vision-15B 的长期机制合并 refine Ch23：前者补 constraint-derived synthetic
  data/verifier lineage，后者补 data-tagged compute policy 与 visual-token evidence budget；未修改 handoff章节。
- 该旧 checkpoint 当时只覆盖 23 项并记录 Books Integration `3/18`；后续虽已完成原 18/18 dispositions，
  后续 spillback 曾使全周 Gate 重新打开；当前 36/36 scored Source Reviews 已完成、0 pending，已记录候选
  Evidence queue 闭合，但 broader Discovery 当时仍打开，新增候选 Books Integration 尚待后续 Source-Family
  Books pass。本段保留历史过程；当前 36/36 最终状态以上方 Final Source-Family Books Integration 为准。
  本检查点未修改 ROADMAP、DECISIONS 或历史 Daily。

## Open Questions

1. professional-work evaluation 怎样版本化 toolchain、workspace 与 external state？
2. CoVe 的 deterministic constraint verifier 能覆盖哪些 semantic correctness，哪些错误会被数据生成器与
   verifier 共同漏掉？
3. MemSifter 与 Memex(RL) 分别学习 retrieval ranking 和 index/dereference policy；两者的 cost、staleness、
   provenance 与 failure-recovery 边界怎样对齐？
4. FlashPrefill 的 sparse-pattern search、thresholding 与 kernel speedup 在不同 context、head pattern、
   GPU、accuracy tolerance 和 SLO 下何时胜过 dense attention？
5. 如何在没有 future target tests 泄漏的情况下，把 SWE-CI 的 trajectory scoring 与 Interactive
   Benchmarks 的 budgeted interaction 扩展为需求漂移、human review 和 production feedback 评估？
6. KARL 的 search、compression 与 stopping policy 如何获得可分离的 counterfactual credit，并在 live
   ACL、freshness、structured tools 与独立 judge 下验证，而不是只优化同一 closed-corpus harness？
7. CoT monitorability 的 evaluation 怎样把 channel parser、surface grader、attempt/feedback budget 与
   executable action verifier 组合起来，并验证被观察 reasoning 对真实 decision 有因果贡献？
8. 训练低比特 attention 如何在不减小 TPS 的情况下保护 dS 路径，并用 matched-step/matched-schedule
   实验区分 quantization bias、gradient noise 与 learned QK scale drift？
9. outcome-trained memory proxy 如何把 working model、task scorer、corpus/ACL、coarse filter 与 proxy
   checkpoint绑定为可回放的 policy identity，并在任一组件变化时检测 drift、fallback与rollback？
10. parallel reasoning怎样用统一的token/FLOPs/KV/latency/cost contract分配generation与verification预算，
    并在candidate set没有正确解、pairwise graph出现cycle或self-judge相关错误时选择abstain/escalate？
11. interactive evaluation怎样分离基础能力、主动信息获取、反馈吸收、停止纪律和judge exploitation，并在
    player+judge+environment的完整成本合同下与static/pass@k公平比较？
12. rubric system怎样对criteria priority/dependency、合法alternative与版本漂移建模，并用hidden holdout、
    executable evidence和human disagreement分别审计specification formation与execution？
13. instruction-following judge怎样把local constraint verdict转换成带priority/veto的global order，并把parser
    failure、cycle、tie与abstention纳入可审计metric，而不是让fallback或Elo静默决定training signal？
14. DynaMoE作者是否会发布可验证code或修订percentile selector；若真正实现variable-K，怎样同时约束token
    compute、per-expert capacity、dispatch shape与tail latency？
15. HACPO如何在capability denominator接近0、tokenizer/template不同、source-policy过旧或shared verifier被
    exploit时检测negative transfer并退出共享？跨policy reuse的effective sample size与真实system cost怎样定义？
16. multimodal red-team run怎样对modality order、media conversion、provider API与judge做immutable versioning、
    paired counterfactual和安全retention，并避免attacker/judge同源误差被ASR聚合掩盖？
17. scientific-hypothesis proposal怎样区分citation-derived reconstruction与prospective discovery，并用multiple-valid-
    inspiration labels、matched compute、independent expert review与experiment-guided ranking校准retrieval/composition？
18. multimodal model怎样把visual-token budget、evidence sufficiency、reasoning-mode selection与runtime SLO组成可校准
    controller，而不是把训练集中的task/mode correlation固化为不可观察的implicit policy？
19. 结构推理benchmark怎样在不注入gold topology/cardinality的条件下联合评估graph discovery，并用source-level
    split、matched compute与causal intervention区分结构脚手架、额外推理预算和真实representation utility？
20. contextual self-distillation怎样用可验证outcome、hard-tail slice与sequence-level diversity约束teacher refresh，
    并把prompt、teacher/student/rollout/scorer revision组成可回放训练合同，避免压缩format shortcut或自洽错误？
21. 多模态量化artifact怎样编码base modality、token-family mask、per-modality scale、whitening/correction rank与
    fallback，并在未知/混合模态或distribution drift下避免silent misrouting、支持canary与rollback？
22. speech dataset怎样把elicitation protocol、speaker identity、environment、consent scope、provider license、
    split policy与supersession组成partition-level immutable manifest，并在paper/blog/card冲突时判定有效contract？
23. LatentMoE 的 projection/top-k/anchor contribution 能否在 matched parameter/FLOP/byte 下分离；mixed-policy-
    age trajectory、Mamba recurrent-cache rounding 与 MTP acceptance 又如何进入统一可恢复训练/服务 contract？
24. SRLM 的 K-way trajectory selection 怎样在 matched calls/tokens/FLOPs/latency/cost 下与 recursion 比较；
    plurality 共同错误时，怎样用独立 verifier、abstention 与可回放 sandbox/selector state 建立 acceptance boundary？

## Sources

- RubricBench metadata: https://arxiv.org/abs/2603.01562
- RubricBench full HTML v1: https://arxiv.org/html/2603.01562v1
- RubricBench PDF v1: https://arxiv.org/pdf/2603.01562v1
- RubricBench official dataset/evaluator repository: https://github.com/planepig/rubricbench
- RubricBench official evaluator:
  https://github.com/planepig/rubricbench/blob/main/eval_submission.py
- CoVe metadata: https://arxiv.org/abs/2603.01940
- CoVe full HTML v1: https://arxiv.org/html/2603.01940v1
- CoVe official project page: https://cove-agent.github.io/
- CoVe-4B official model card: https://huggingface.co/Zichen1024/CoVe-4B
- CoVe-12k official dataset card: https://huggingface.co/datasets/Zichen1024/CoVe-12k
- DynaMoE metadata: https://arxiv.org/abs/2603.01697
- DynaMoE full HTML v1: https://arxiv.org/html/2603.01697v1
- DynaMoE PDF v1: https://arxiv.org/pdf/2603.01697v1
- SageBwd metadata: https://arxiv.org/abs/2603.02170
- SageBwd full HTML v1: https://arxiv.org/html/2603.02170v1
- Related official SageAttention repository（SageBwd implementation not located）:
  https://github.com/thu-ml/SageAttention
- Heterogeneous Agent Collaborative RL metadata: https://arxiv.org/abs/2603.02604
- HACRL/HACPO full HTML v1: https://arxiv.org/html/2603.02604v1
- HACRL/HACPO full HTML v2: https://arxiv.org/html/2603.02604v2
- HACRL/HACPO PDF v1: https://arxiv.org/pdf/2603.02604v1
- HACRL/HACPO official project page: https://zzx-peter.github.io/hacrl/
- HACRL/HACPO official code: https://github.com/zzx-peter/HACRL-code
- MemSifter metadata: https://arxiv.org/abs/2603.03379
- MemSifter full HTML v1: https://arxiv.org/html/2603.03379v1
- MemSifter official code: https://github.com/plageon/MemSifter
- MemSifter official training entry:
  https://github.com/plageon/MemSifter/blob/main/scripts/train/qwen3_4b_task_reward.sh
- MemSifter task-outcome reward implementation:
  https://github.com/plageon/MemSifter/blob/main/genrank_verl/task_reward_score.py
- MemSifter checkpoint averaging implementation:
  https://github.com/plageon/MemSifter/blob/main/genrank_verl/merge_ckpts.py
- MemSifter inference toolkit:
  https://github.com/plageon/MemSifter/blob/main/memsifter/toolkit.py
- MUSE metadata: https://arxiv.org/abs/2603.02482
- MUSE full HTML v1: https://arxiv.org/html/2603.02482v1
- MUSE PDF v1: https://arxiv.org/pdf/2603.02482v1
- MUSE official web app: https://muse-duke.com/
- MOOSE-Star metadata: https://arxiv.org/abs/2603.03756
- MOOSE-Star full HTML v1: https://arxiv.org/html/2603.03756v1
- MOOSE-Star current HTML v4: https://arxiv.org/html/2603.03756v4
- MOOSE-Star PDF v1: https://arxiv.org/pdf/2603.03756v1
- MOOSE-Star official repository: https://github.com/ZonglinY/MOOSE-Star
- MOOSE-Star hierarchical-search entry:
  https://github.com/ZonglinY/MOOSE-Star/blob/main/Inference/hierarchical_search_eval.py
- MOOSE-Star tree construction/search implementation:
  https://github.com/ZonglinY/MOOSE-Star/blob/main/Preprocessing/hierarchical_search/tree_search.py
- MOOSE-Star IR probability extractor:
  https://github.com/ZonglinY/MOOSE-Star/blob/main/Inference/ir_probability_extractor.py
- Phi-4-reasoning-vision-15B metadata: https://arxiv.org/abs/2603.03975
- Phi-4-reasoning-vision-15B full HTML v1: https://arxiv.org/html/2603.03975v1
- Phi-4-reasoning-vision-15B PDF v1: https://arxiv.org/pdf/2603.03975v1
- Microsoft Research technical note:
  https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/
- Phi-4-reasoning-vision-15B official model card:
  https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B
- Phi-4-reasoning-vision-15B official repository:
  https://github.com/microsoft/Phi-4-reasoning-vision-15B
- Phi-4-reasoning-vision-15B transparency note:
  https://github.com/microsoft/Phi-4-reasoning-vision-15B/blob/main/TRANSPARENCY_NOTE.md
- Microsoft Eureka ML Insights: https://github.com/microsoft/eureka-ml-insights
- OpenCompass VLMEvalKit: https://github.com/open-compass/VLMEvalKit
- Memex(RL) metadata: https://arxiv.org/abs/2603.04257
- Memex(RL) full HTML v1: https://arxiv.org/html/2603.04257v1
- Memex(RL) official code: https://github.com/Accenture/MemexRL
- Memex(RL) memory implementation:
  https://github.com/Accenture/MemexRL/blob/main/src/agents/memory/mixin.py
- Memex(RL) reward/training implementation:
  https://github.com/Accenture/MemexRL/tree/main/src/rewards
- SWE-CI metadata: https://arxiv.org/abs/2603.03823
- SWE-CI full HTML v1: https://arxiv.org/html/2603.03823v1
- SWE-CI full HTML v4: https://arxiv.org/html/2603.03823v4
- SWE-CI official code: https://github.com/SKYLENAGE-AI/SWE-CI
- SWE-CI current config: https://github.com/SKYLENAGE-AI/SWE-CI/blob/main/config.toml
- SWE-CI current source tree: https://github.com/SKYLENAGE-AI/SWE-CI/tree/main/src/swe_ci
- V1 metadata: https://arxiv.org/abs/2603.04304
- V1 full HTML v1: https://arxiv.org/html/2603.04304v1
- T2S-Bench metadata: https://arxiv.org/abs/2603.03790
- T2S-Bench full HTML v1: https://arxiv.org/html/2603.03790v1
- T2S-Bench PDF v1: https://arxiv.org/pdf/2603.03790v1
- T2S-Bench official project page: https://t2s-bench.github.io/T2S-Bench-Page/
- T2S-Bench official repository: https://github.com/T2S-Bench/T2S-Bench
- T2S-Bench official model-evaluation entry:
  https://github.com/T2S-Bench/T2S-Bench/blob/main/scripts/evaluate_model.py
- T2S-Bench official structure-evaluation entry:
  https://github.com/T2S-Bench/T2S-Bench/blob/main/scripts/evaluate_structure.py
- Interactive Benchmarks metadata and revision history: https://arxiv.org/abs/2603.04737
- Interactive Benchmarks v1 PDF: https://arxiv.org/pdf/2603.04737v1
- Interactive Benchmarks current v4 HTML: https://arxiv.org/html/2603.04737
- InteractiveBench official code: https://github.com/interactivebench/InteractiveBench
- InteractiveBench math artifact:
  https://github.com/interactivebench/InteractiveBench/tree/main/src/math
- InteractiveBench situation-puzzle artifact:
  https://github.com/interactivebench/InteractiveBench/tree/main/src/situation_puzzle
- InteractiveBench poker artifact:
  https://github.com/interactivebench/InteractiveBench/tree/main/src/poker
- InteractiveBench trust-game artifact:
  https://github.com/interactivebench/InteractiveBench/tree/main/src/trust_game
- KARL metadata: https://arxiv.org/abs/2603.05218
- KARL full HTML v1: https://arxiv.org/html/2603.05218v1
- KARL Databricks-hosted PDF: https://www.databricks.com/sites/default/files/2026-03/karl.pdf
- On-Policy Self-Distillation for Reasoning Compression metadata:
  https://arxiv.org/abs/2603.05433
- OPSDC full HTML v1: https://arxiv.org/html/2603.05433v1
- OPSDC PDF v1: https://arxiv.org/pdf/2603.05433v1
- CRISP current full HTML v7: https://arxiv.org/html/2603.05433v7
- CRISP official repository: https://github.com/HJSang/CRISP_Reasoning_Compression
- CRISP official trainer:
  https://github.com/HJSang/CRISP_Reasoning_Compression/blob/main/workspace/src/self_distill_hybrid/opsd_trainer.py
- CRISP official worker and reverse-KL implementation:
  https://github.com/HJSang/CRISP_Reasoning_Compression/blob/main/workspace/src/self_distill_hybrid/opsd_worker.py
- CRISP official data builder:
  https://github.com/HJSang/CRISP_Reasoning_Compression/blob/main/workspace/src/data/prepare_length_prune_data.py
- CRISP official training launch configuration:
  https://github.com/HJSang/CRISP_Reasoning_Compression/blob/main/workspace/scripts/sft/train_opsd.sh
- CRISP dual-path math scorer:
  https://github.com/HJSang/CRISP_Reasoning_Compression/blob/main/workspace/src/rewards/dual_path_math_verify.py
- MASQuant metadata: https://arxiv.org/abs/2603.04800
- MASQuant full HTML v1: https://arxiv.org/html/2603.04800v1
- MASQuant PDF v1: https://arxiv.org/pdf/2603.04800v1
- MASQuant official code: https://github.com/alibaba/EfficientAI/tree/main/masquant
- MASQuant official calibration/inference entrypoint:
  https://github.com/alibaba/EfficientAI/blob/main/masquant/infer_mas.py
- MASQuant official README and reproduction commands:
  https://github.com/alibaba/EfficientAI/blob/main/masquant/README.md
- IF-RewardBench metadata: https://arxiv.org/abs/2603.04738
- IF-RewardBench full HTML v1: https://arxiv.org/html/2603.04738v1
- IF-RewardBench PDF v1: https://arxiv.org/pdf/2603.04738v1
- IF-RewardBench official repository: https://github.com/thu-coai/IF-RewardBench
- IF-RewardBench constraint metric implementation:
  https://github.com/thu-coai/IF-RewardBench/blob/main/metrics/analysis_constraint_assessment.py
- IF-RewardBench overall/listwise metric implementation:
  https://github.com/thu-coai/IF-RewardBench/blob/main/metrics/analysis_overall_assessment.py
- Reasoning Models Struggle to Control their Chains of Thought metadata:
  https://arxiv.org/abs/2603.05706
- Reasoning Models Struggle to Control their Chains of Thought full HTML v1:
  https://arxiv.org/html/2603.05706v1
- CoT-Control official code: https://github.com/YuehHanChen/CoTControl
- CoT-Control QA grader:
  https://github.com/YuehHanChen/CoTControl/blob/master/CoT-Control-QA/grading.py
- CoT-Control QA evaluation harness:
  https://github.com/YuehHanChen/CoTControl/blob/master/CoT-Control-QA/run_cceval.py
- OpenAI official CoT controllability research note:
  https://openai.com/index/reasoning-models-chain-of-thought-controllability/
- FlashPrefill metadata: https://arxiv.org/abs/2603.06199
- FlashPrefill full HTML v1: https://arxiv.org/html/2603.06199v1
- FlashPrefill official code: https://github.com/qhfan/FlashPrefill
- FlashPrefill native Triton forward path:
  https://github.com/qhfan/FlashPrefill/blob/main/ops/flashprefill_native_forward.py
- FlashPrefill variable-length path:
  https://github.com/qhfan/FlashPrefill/blob/main/ops/flashprefill_varlen_func.py
- FlashPrefill vLLM 0.10 patch:
  https://github.com/qhfan/FlashPrefill/blob/main/patches/patch_loader_vllm_0_10_0.py
- OpenAI, “Introducing GPT-5.4,” published 2026-03-05:
  https://openai.com/index/introducing-gpt-5-4/
- OpenAI, “GPT-5.4 Thinking System Card,” published 2026-03-05:
  https://openai.com/index/gpt-5-4-thinking-system-card/
- OpenAI Deployment Safety Hub, full “GPT-5.4 Thinking System Card”:
  https://deploymentsafety.openai.com/gpt-5-4-thinking
- Anthropic Research index, labor-market entry dated 2026-03-05:
  https://www.anthropic.com/research
- Anthropic, “Labor market impacts of AI: A new measure and early evidence”:
  https://www.anthropic.com/research/labor-market-impacts
- Anthropic, full methodological appendix:
  https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf
- WAXAL metadata and revision history: https://arxiv.org/abs/2602.02734
- WAXAL full HTML v1: https://arxiv.org/html/2602.02734v1
- WAXAL full HTML v3: https://arxiv.org/html/2602.02734v3
- Google Research, “WAXAL: A large-scale open resource for African language speech technology,”
  published 2026-03-06:
  https://research.google/blog/waxal-a-large-scale-open-resource-for-african-language-speech-technology/
- WAXAL official dataset card v2.0.0: https://huggingface.co/datasets/google/WaxalNLP
- WAXAL dataset card source/schema/splits/licenses:
  https://huggingface.co/datasets/google/WaxalNLP/blob/main/README.md?code=true
- Google Research March 2026 archive: https://research.google/blog/2026/03/
- Multi-Head Low-Rank Attention metadata: https://arxiv.org/abs/2603.02188
- Multi-Head Low-Rank Attention full HTML v1: https://arxiv.org/html/2603.02188v1
- Multi-Head Low-Rank Attention official code: https://github.com/SongtaoLiu0823/MLRA
- Believe Your Model / DistriVoting metadata: https://arxiv.org/abs/2603.03872
- Believe Your Model / DistriVoting full HTML v1: https://arxiv.org/html/2603.03872v1
- DistriVoting official code: https://github.com/yxizhong/DistriVoting
- Progressive Residual Warmup metadata: https://arxiv.org/abs/2603.05369
- Progressive Residual Warmup full HTML v1: https://arxiv.org/html/2603.05369v1
- BandPO metadata: https://arxiv.org/abs/2603.04918
- BandPO full paper: https://arxiv.org/pdf/2603.04918
- BandPO official repository: https://github.com/OpenMOSS/BandPO
- BandPO trust-region solver implementation:
  https://github.com/OpenMOSS/BandPO/blob/main/RLtraining/verl/verl/bandpo/band/band.py
- Sparse-BitNet metadata: https://arxiv.org/abs/2603.05168
- Sparse-BitNet full HTML v1: https://arxiv.org/html/2603.05168v1
- Sparse-BitNet official repository: https://github.com/AAzdi/Sparse-BitNet
- Sparse-BitNet public model implementation:
  https://github.com/AAzdi/Sparse-BitNet/blob/main/llm/arch/model.py
- ATLAS metadata: https://arxiv.org/abs/2603.06713
- ATLAS full HTML v1: https://arxiv.org/html/2603.06713v1
- Microsoft Research ATLAS publication record:
  https://www.microsoft.com/en-us/research/publication/scaling-agentic-capabilities-not-context-efficient-reinforcement-finetuning-for-large-toolspaces/
- Building AI Coding Agents for the Terminal metadata and revision history:
  https://arxiv.org/abs/2603.05344
- Building AI Coding Agents for the Terminal full HTML v1:
  https://arxiv.org/html/2603.05344v1
- Building Effective AI Coding Agents for the Terminal current HTML v3:
  https://arxiv.org/html/2603.05344v3
- OpenDev official repository: https://github.com/opendev-to/opendev
- AutoResearch-RL metadata and administrator withdrawal record:
  https://arxiv.org/abs/2603.07300
- AutoResearch-RL withdrawn v1 HTML retained by arXiv:
  https://arxiv.org/html/2603.07300v1
- Hindsight Credit Assignment metadata: https://arxiv.org/abs/2603.08754
- Hindsight Credit Assignment full HTML v1: https://arxiv.org/html/2603.08754v1
- Scaling Data Difficulty metadata: https://arxiv.org/abs/2603.07779
- Scaling Data Difficulty full HTML v1: https://arxiv.org/html/2603.07779v1
- Breaking Training Bottlenecks / MicroCoder-GRPO metadata:
  https://arxiv.org/abs/2603.07777
- Breaking Training Bottlenecks / MicroCoder-GRPO full HTML v1:
  https://arxiv.org/html/2603.07777v1
- Nemotron 3 Super base BF16 model card（03-04 release）:
  https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-Base-BF16
- Nemotron 3 Super FP8 model card（03-11 release）:
  https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8
- Nemotron 3 Super technical report PDF:
  https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf
- Nemotron 3 Super arXiv metadata（04-14 formal report）: https://arxiv.org/abs/2604.12374
- NVIDIA Nemotron 3 Super official project page: https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/
- NVIDIA Nemotron developer repository: https://github.com/NVIDIA-NeMo/Nemotron
- Recursive Language Models Meet Uncertainty metadata and revision history:
  https://arxiv.org/abs/2603.15653
- Recursive Language Models Meet Uncertainty full PDF v1:
  https://arxiv.org/pdf/2603.15653
- Apple Machine Learning Research publication record:
  https://machinelearning.apple.com/research/self-reflective-program-search
