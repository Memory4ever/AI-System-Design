# AI Research Weekly — 2026-W06

> Coverage Window: 2026-02-02～2026-02-08
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Discovery Recall Re-audit: 2026-08-13 — 38/39 Full Source Reviews Complete / 1 Unverified Blocked / 0 Review Pending / Cross-index Recall Open
> Books Review: 2026-08-13 — 38 accessible families dispositioned / 1 blocked family skipped / Source-Family Books Gate Complete

## Executive Summary

原周报只保留 Sequential Attention 与 Protenix-v1 两项，不能代表 W06 的实际研究面。本轮按
Hugging Face discovery page 反查 arXiv identifier，再以 arXiv v1 / official publication date 重新归周，
已确认 39 个属于 2026-02-02～02-08 的候选入口，覆盖统一多模态模型、elastic training、width expansion、
长上下文 sparse attention / KV pruning、speculative decoding、serving、Agent orchestration、memory、
verifiable environment 与 executable evaluation。

这 39 项中已有 38 项完成 primary-source 全文审查：Batch A 覆盖 Kimi K2.5、ERNIE 5.0、SPARKLING、
FASA、Token Sparse Attention、POP 与 DFlash；Batch B 覆盖 SWE-Universe、FS-Researcher、Wiki Live
Challenge、FIRE-Bench、SafeGround 与 Spider-Sense；Batch C 覆盖 Fast Autoregressive Video Diffusion、
RE-TRAC、DAC-RL、MARS、WideSeek 与 WideSeek-R1；Batch D 覆盖 AOrchestra、FullStack-Agent、MemSkill、
D-CORE、Sage 与 Focus-dLLM；Batch E 覆盖 LycheeDecode、OmniSIFT、HySparse、Data2Behavior、
LUSPO、Infinite-World 与 DASH；Batch F 完成 Anthropic 0-day、OpenAI closed-loop laboratory、
TensorRT 10.15 与 vLLM NixlConnector roadmap 的联合来源审查；Batch G 由第二轮交叉检索恢复并
全文审查 Multi-Task GRPO 与 CauGym。Claude Opus 4.6 announcement
已核验，但 13 MB system card 在当前读取通道中无法完整取得，故保留为 `Unverified / Blocked`，
不能用发布页代替 system card。原有 2 项评分
只对旧候选成立。按照用户确认的 blocked-skip 规则，Claude Opus 4.6 独立保持 `Unverified / Blocked / No
Books Change`，不再锁住其余可访问 family。其余 38 项与两个低分/历史传播节点完成最终 disposition：
21 项 Integrate/Refine、15 项 No Change、4 项 Weekly Only、1 项 Unverified。W06 Source-Family Books Gate
已闭合；cross-index discovery 与 blocked source 仍使 Archive Gate 保持 Open。

## Coverage and Source Coverage

- 模型与研究机构：除 Google/Seed 旧条目外，恢复 Kimi K2.5、ERNIE 5.0、Claude Opus 4.6、Anthropic
  0-day 研究与 OpenAI closed-loop laboratory 研究；存在报告/system card 时必须联合阅读，不能只使用
  announcement 或 discovery 摘要。
- 论文与学术来源：完成 2026-02-03～02-06 Hugging Face discovery list 的首轮人工普查，并把 discovery
  date 还原为 arXiv v1 date；02-07/02-08 页面访问失败，后续还需用 arXiv category、OpenAlex、Google
  Scholar、DBLP 与官方 Research archive 交叉补漏。
- AI Infra：恢复 long-context inference、prefill pruning、speculative decoding、speech serving、optimizer
  implementation 等候选入口；尚未完成 code/artifact 与 hardware contract 核验。
- **Evidence boundary:** Hugging Face 只承担 discovery，不能证明机制、实验结论或事件日期；下表也不是
  评分表。只有 primary source 全文审查后，候选才可进入正式 Candidate Scoring。

## Discovery Recall Reconciliation

- **Original scored rows:** 2。
- **New date-verified W06 hits:** 39；均为 discovery candidate，不等于 retained candidate。
- **Full Source Review:** 旧有 2 项已审；新增 39 项中 38 项已审、1 项为 `Unverified / Blocked`。
- **Known cross-week exclusions:** VoxServe（arXiv v1 2026-01-30）、Representation-as-a-Judge
  （arXiv:2601.22588）、Gaming the Judge（arXiv:2601.14691）、PaperSearchQA（arXiv:2601.18207）只在
  本周 discovery page 出现，必须回归各自 first-public week，不计入 W06。
- **Open discovery gaps:** 02-07/02-08 HF 页面、arXiv category census、OpenAlex/Scholar/DBLP、官方 Research
  archive 与工程 Release/RFC 尚未完成交叉覆盖。
- **Gate status:** `39 metadata-verified / 38 Full Source Reviews complete / 1 blocked skipped / 41 scored rows
  dispositioned / Source-Family Books Gate Complete / Archive Gate Open`。

### Discovery Cross-Check Review — 2026-08-07

| Source Surface | Result | Evidence Boundary |
| --- | --- | --- |
| arXiv date/topic search + paper HTML | 恢复 Multi-Task GRPO 与 CauGym 两篇 W06 primary papers | 证明首轮 HF discovery census 有漏项；不是全分类 exhaustive export |
| Hugging Face 2026-02-07 / 02-08 date pages | web reader 被安全层拒绝，in-app browser 直连超时 | `Access Gap`；不得写成周末无新增 |
| Semantic Scholar related search | 可访问，但返回跨年份 related works，不能据此归周 | 只作 discovery；未形成新的 W06 date-verified candidate |
| Google Scholar | 定向查询未返回可审计结果 | `Access Gap`；不得作为负检索证明 |
| OpenAlex / DBLP | API URL 被当前安全层拒绝；搜索只返回零散 metadata pages | `Access Gap`；不能宣称完整 venue/identifier census |
| Official GitHub releases | TensorRT 10.15 与 vLLM RFC/PR 可核验；vLLM/SGLang/Transformers 历史 release pagination 不完整 | 可验证项逐项保留；不可见历史页不作“无发布”结论 |
| Model/research official sources | Anthropic/OpenAI 本周来源已审；Claude system card full read 仍失败 | announcement 不能替代 system card |

**Review verdict:** 第二轮成功发现并全文审查 2 篇漏项，说明修复方向有效；source-access gaps 尚未闭合，
所以 Archive Gate 维持 Open。Source-Family Books Gate 按已验证 family 独立执行；blocked family 不由摘要补写。

### Claude Opus 4.6 Access Recheck — 2026-08-09

- 官方 system-card 索引页和 14 MB PDF identity 已核验；搜索索引可恢复完整目录，并分别核对 model/release
  process、capability/decontamination、harmlessness、agentic safety、alignment audit、CBRN/autonomy/cyber
  evaluation 与 Appendix 的存在及局部文本。
- 普通 primary-source reader 仍因文档体积拒绝加载；直接浏览器读取又被用户侧网站访问权限拒绝。未尝试绕过
  权限，也未把 search snippets 或 announcement 拼接成“Full Source Review”。
- **Review verdict:** `Unverified / Blocked / No Books Change` 保持不变。现有证据足以确认 source family 和 evaluation
  taxonomy，不足以完成逐节 methodology、sample、baseline、failure slice、limitation 与 Appendix 核验；
  因此 Candidate Evidence Gate 仍是 `38/39`；该 family 的 Books Gate 关闭，但不阻塞其余 38 项。

### Recovered Candidate Ledger

| Candidate | Primary ID | First-public Date | Current Status |
| --- | --- | --- | --- |
| Kimi K2.5: Visual Agentic Intelligence | arXiv:2602.02276 | 2026-02-02 | 29/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| SWE-Universe | arXiv:2602.02361 | 2026-02-02 | 29/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| FS-Researcher | arXiv:2602.01566 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| SPARKLING | arXiv:2602.02472 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Wiki Live Challenge | arXiv:2602.01590 | 2026-02-02 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Fast Autoregressive Video Diffusion and World Models | arXiv:2602.01801 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| RE-TRAC | arXiv:2602.02486 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Divide-and-Conquer Reasoning / Test-Time Scalability | arXiv:2602.02477 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| AOrchestra | arXiv:2602.03786 | 2026-02-03 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| MARS | arXiv:2602.02660 | 2026-02-02 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| WideSeek | arXiv:2602.02636 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Token Sparse Attention | arXiv:2602.03216 | 2026-02-03 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| FullStack-Agent | arXiv:2602.03798 | 2026-02-03 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| LycheeDecode | arXiv:2602.04541 | 2026-02-04 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| FIRE-Bench | arXiv:2602.02905 | 2026-02-02 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| POP: Prefill-Only Pruning | arXiv:2602.03295 | 2026-02-03 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| SafeGround | arXiv:2602.02419 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| ERNIE 5.0 Technical Report | arXiv:2602.04705 | 2026-02-04 | 29/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| FASA | arXiv:2602.03152 | 2026-02-03 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| WideSeek-R1 | arXiv:2602.04634 | 2026-02-04 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| OmniSIFT | arXiv:2602.04804 | 2026-02-04 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| HySparse | arXiv:2602.03560 | 2026-02-03 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| From Data to Behavior | arXiv:2602.04735 | 2026-02-04 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| D-CORE | arXiv:2602.02160 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| DFlash | arXiv:2602.06036 | 2026-02-05 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Spider-Sense | arXiv:2602.05386 | 2026-02-05 | 26/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| MemSkill | arXiv:2602.02474 | 2026-02-02 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Length-Unbiased Sequence Policy Optimization | arXiv:2602.05261 | 2026-02-05 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Infinite-World | arXiv:2602.02393 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| DASH | arXiv:2602.02016 | 2026-02-02 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| SAGE | arXiv:2602.05975 | 2026-02-05 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Focus-dLLM | arXiv:2602.02159 | 2026-02-02 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Claude Opus 4.6 source family | Anthropic announcement + system card | 2026-02-05 | 23/30；announcement verified；system card full read blocked；Books blocked |
| LLM-discovered 0-days | Anthropic Research | 2026-02-05 | 27/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| GPT-5 lowers cell-free protein synthesis cost | OpenAI Research + paper | 2026-02-05 | 28/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| TensorRT 10.15 | GitHub release v10.15 | 2026-02-03 | 19/30；Full Source Review complete；Weekly Only |
| vLLM NixlConnector P/D Roadmap | GitHub issue #33702 + linked implementation PRs | 2026-02-03 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Multi-Task GRPO | arXiv:2602.05547 | 2026-02-05 | 29/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |
| Can Post-Training Transform LLMs into Causal Reasoners? / CauGym | arXiv:2602.06337 | 2026-02-06 | 25/30；Full Source Review complete；Final Books disposition recorded in Candidate Scoring ledger |

## Candidate Scoring — Final Source-Family Books Dispositions

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential Attention | 4 | 4 | 3 | 4 | 4 | 5 | 24/30 | Weekly Only — 2022 mechanism/publication state |
| Protenix-v1 | 3 | 3 | 3 | 4 | 2 | 4 | 19/30 | Weekly Only — low-score domain evidence |
| Kimi K2.5 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | No Change — Ch82 topology/capability boundary 已覆盖 |
| ERNIE 5.0 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — `MODEL-MOE` elastic execution profiles |
| SPARKLING | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Integrate — `TRAIN-PRETRAINING` state-aware expansion |
| FASA | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `INFER-KV-CACHE` selector/offload branch |
| Token Sparse Attention | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `INFER-PREFILL` reversible sparsity |
| POP | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Integrate — `INFER-PREFILL` phase-aware layer plan |
| DFlash | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — `INFER-SPECULATIVE-DECODING` diffusion drafter |
| SWE-Universe | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | No Change — Ch27/66 executable environment contract 已覆盖 |
| FS-Researcher | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | No Change — Ch75/81 artifact-backed workflow 已覆盖 |
| Wiki Live Challenge | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — Ch66 live/leakage-aware evaluation 已覆盖 |
| FIRE-Bench | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | No Change — Ch66 executable research tree 已覆盖 |
| SafeGround | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | No Change — Ch66/72 selective risk gate 已覆盖 |
| Spider-Sense | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | No Change — Ch72 sensor/authority split 已覆盖 |
| Fast Autoregressive Video Diffusion | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `MULTIMODAL-WORLD-MODELS` temporal/spatial split |
| RE-TRAC | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | No Change — Ch80 stateful search/monitoring 已覆盖 |
| Divide-and-Conquer Reasoning | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | No Change — Ch79 hierarchical planning 已覆盖 |
| MARS | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | No Change — Ch81 evaluator-driven repository search 已覆盖 |
| WideSeek | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine — `AGENT-MULTI-AGENT` dynamic fan-out |
| WideSeek-R1 | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `AGENT-MULTI-AGENT` count-normalized credit |
| AOrchestra | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `AGENT-MULTI-AGENT` runtime executor contract |
| FullStack-Agent | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — Ch66 cross-layer executable verification 已覆盖 |
| MemSkill | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine — `AGENT-MEMORY` operator-policy state |
| D-CORE | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `TRAIN-SFT` decomposition-aware tool trace |
| Sage | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Refine — `AGENT-RAG` query–retriever joint contract |
| Focus-dLLM | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` mutable-state refresh |
| LycheeDecode | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `MODEL-LONG-CONTEXT` selector ownership granularity |
| OmniSIFT | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | No Change — Ch23 modality-role-aware compression 已覆盖 |
| HySparse | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — `MODEL-LONG-CONTEXT` global/local state ownership |
| From Data to Behavior | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | No Change — Ch5/27 intervention evidence boundary 已覆盖 |
| Length-Unbiased Sequence Policy Optimization | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-GRPO` sequence-weighting contract |
| Infinite-World | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `MULTIMODAL-WORLD-MODELS` hierarchical lossy state |
| DASH | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | No Change — Ch28 optimizer/execution contract 已覆盖 |
| Claude Opus 4.6 source family | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Unverified / Blocked；system card inaccessible |
| LLM-discovered 0-days | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Refine — `PLATFORM-SECURITY` disclosure lifecycle |
| GPT-5 closed-loop CFPS optimization | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `AGENT-WORKFLOW` physical experiment authority |
| TensorRT 10.15 | 2 | 3 | 4 | 5 | 2 | 3 | 19/30 | Weekly Only — Version Fact |
| vLLM NixlConnector P/D Roadmap | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | No Change — Ch55 typed KV handoff 已覆盖 |
| Multi-Task GRPO | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — `TRAIN-GRPO` effective gradient mixture |
| CauGym / causal-reasoning post-training | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Weekly Only — bounded domain post-training case |

## Evidence Level

- `Primary / Full Source Review`：38 个可访问的新增 source families，以及两项 legacy/低分节点，均已检查
  method 或官方机制、implementation、evaluation contract、limitations 与相邻章节；作者实验仍只在各自
  model、hardware、precision、length、batch、concurrency、tool/harness 与 SLO 披露范围内成立。
- `Version/Product Fact`：TensorRT 10.15 与旧论文传播节点只证明版本、support matrix 或 publication state，
  不构成新的系统机制。
- `Unverified / Blocked`：Claude Opus 4.6 只能核验 announcement、system-card identity/目录与局部索引；
  未完成逐节全文审查，因此没有进入 Books。
- `Discovery Limitation`：02-07/02-08 及 Scholar/OpenAlex/DBLP 的可复算召回仍未闭合。它使 Archive Gate
  保持 Open，但不撤销已完成全文审计 family 的独立 Source-Family Books Gate。

## Cross-Week Deduplication

Sequential Attention 的 2022 feature-selection family 与 Transformer Attention 只存在命名重叠；
DFlash 的 W06 algorithm node 与 W26 runtime integration 属于同一 Source Family 的机制→工程演进；
Kimi K2.5、WideSeek/WideSeek-R1 与 AOrchestra 共同构成静态 topology→learned fan-out→runtime executor
contract 的相邻分支；FASA、Token Sparse、POP、HySparse 与 LycheeDecode 分别改变 KV tier、Prefill
execution、global/local ownership 与 head-level selector reuse，不能按“都叫 sparse”合并成同一方案。

## Knowledge Tree Position

本周长期 owner 分布于 `MODEL-MOE`、`MODEL-LONG-CONTEXT`、
`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-WORLD-MODELS`、`TRAIN-PRETRAINING`、
`TRAIN-SFT`、`TRAIN-GRPO`、`INFER-PREFILL`、`INFER-KV-CACHE`、
`INFER-SPECULATIVE-DECODING`、`PLATFORM-SECURITY`、`AGENT-RAG`、`AGENT-MEMORY`、
`AGENT-WORKFLOW` 与 `AGENT-MULTI-AGENT`。Sequential Attention 只保留 publication-state 记录，
不占用 Transformer Attention owner。

## Recommended Action

本轮不再等待 Claude system card：该 family 继续冻结，其余 40 个 scored rows 已完成最终 disposition。
后续只处理两类增量：恢复 Claude 可解析全文，或 cross-index discovery 找到新的 in-window family；任一情况
都会重新打开 W06 周级 Review。下一周可进入 W07，但不得把 W06 Source-Family Gate 误写为 Archive Complete。

## Event-Date Daily Decision

2026-02-04、02-06：Weekly only。

## Books Integration Decision

`Source-Family Books Gate Complete / Archive Gate Open`。41/41 scored rows 已有最终 disposition：
21 项 `Integrate / Refine`、15 项 `No Change`、4 项 `Weekly Only`、1 项 `Unverified / Blocked`。
21 项长期机制已进入 15 个 Stable Node owner；`No Change` 均由 Candidate Scoring 指向具体既有论点；
Claude 与未闭合 discovery surfaces 不进入 Books。周级反向检查确认没有把公告、作者 benchmark 或后续
revision 倒灌为通用结论。

## Ignored Noise

把理论 FLOPs 减少直接写成 latency、throughput 或 energy 的等比例收益。

## Full Source Review

### Sequential Attention for Feature Selection

- **Candidate / Week / Score:** Sequential Attention / 2026-W06 / 24/30；
  `Source Family ID: sequential-attention-feature-selection-omp`。
- **Source Type / Dates / Sources:** arXiv:2209.14881，v1 2022-09-29；2026 条目是 publication/
  institutional propagation state，不是 first-public mechanism。
- **Access and Full-read Coverage:** Verified；已检查 feature-selection problem、one-pass greedy
  algorithm、attention-weight proxy、linear-regression/OMP equivalence、experiments、baselines 和限制。
- **Problem / Previous Design / Changed Constraint:** 一次性 L1/attention selection 忽略“给定已选 features
  后”的 residual marginal value；exact forward selection 反复训练成本高。
- **Mechanism / State / Flow:** 当前 selected set 与 residual information 是 selector state；每轮训练/
  更新 attention scores，选择下一 feature，逐步逼近 greedy forward selection。在线性回归适配中与
  OMP 对应，不代表所有 neural settings 继承 OMP guarantee。
- **Implementation / Evaluation:** 作者在若干 tabular/image feature-selection tasks 比较 L1、attention
  和其他 baselines；hardware、serving concurrency、token/KV/SLO 不适用，不能写成 inference 优化。
- **Evidence Boundary / Trade-offs:** 支持 sequential marginal selection 在作者任务上的质量；不证明
  attention score 一般等于 causal feature importance。它增加多步 selection/training 成本并依赖 feature
  representation；一次性 filter 在成本敏感或 feature interactions 弱时仍合理。
- **Evolution / ROADMAP:** `Principle Reuse` with greedy/OMP feature selection；Ch23 主 owner。已读
  Ch22～24；不归 Ch14/21/45。
- **Integration Decision:** `Weekly Only — Publication-state correction`；不修改 Books。
- **Open Questions:** neural attention proxy 在 correlated features、distribution shift 和 downstream model
  change 下怎样校准？

### Protenix-v1 — Low-score verification

- **Candidate / Week / Score:** Protenix-v1 / 2026-W06 / 19/30；
  `Source Family ID: seed-protenix-v1`。
- **Source / Date / Verification:** ByteDance Seed 官方 research entry 与所链接 paper/code/model；
  2026-02-06。已核对其为 biomolecular structure prediction artifact，原评分不提高。
- **Boundary / Rejection:** 结构预测 benchmark 不证明通用 AI System runtime 机制；训练数据、domain
  evaluation 与 scientific validation 只在该领域成立。`Weekly Only — Low-score domain evidence`。
- **Open Questions:** scientific model registry 如何同时管理 sequence/structure data、license、confidence、
  wet-lab validation 和 model revision？

### Kimi K2.5: Visual Agentic Intelligence

- **Candidate / Week / Score:** Kimi K2.5 / 2026-W06 / 29/30；
  `Source Family ID: kimi-k2.5-visual-agentic-intelligence`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02276，v1 2026-02-02。已读 metadata、Introduction、
  multimodal pretraining、Zero-Vision SFT、visual RL、Agent Swarm / PARL、critical-step scheduling、模型架构、
  training stages、Decoupled Encoder Pipeline、evaluation 与相关 appendix。论文没有独立 Limitations 章节，
  因而未披露项不能由 benchmark 反推。
- **Problem / Previous Design / Changed Constraint:** 单体 Agent 避免协调开销，且在任务不可分解时更稳；但
  长时、可并行的视觉与工具任务会被串行 critical path 限制。约束从“单次回答质量”变成“多分支执行时间、
  子任务依赖与工具环境状态”。
- **Mechanism / State / Flow:** 以 Kimi K2 的 1.04T total / 32B active MoE 为基座，增加 15T vision-text
  tokens，并通过 Zero-Vision SFT 与 visual RL 对齐视觉与语言行为。Agent Swarm 由 orchestrator 拆分任务并
  调用 frozen subagents；子 Agent 输出作为 environment observations 返回。PARL 只更新 orchestrator，奖励
  联合 task outcome、实例化与完成率，辅助项逐步退火；critical steps 由最长依赖分支近似。
- **Implementation / Evaluation Contract:** vision encoder 通过 Decoupled Encoder Pipeline 从 Stage-0
  解耦，以降低可变长度 multimodal input 引发的流水线负载不均。训练上下文从 32K 扩到 262K；论文报告的
  Agent Swarm 收益绑定其公开与内部 benchmark、工具配置和 frozen-subagent 设置，不是通用多 Agent 加速率。
- **Evidence Boundary / Trade-offs:** 证据支持“可分解任务上，learned orchestration 能缩短关键路径并改善
  结果”的作者结论；不证明更多 Agent 必然更好，也不揭示闭源 serving/runtime 的所有实现。新增成本包括
  子任务分解错误、共享状态与工具冲突、结果合并、额外 token/调用成本及 error amplification。单 Agent 在
  任务耦合强、预算小或协调税高时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from single-agent tool use to learned parallel
  orchestration；Ch78 主 owner，Ch77/80 handoff。已读 Ch77～80；现有 Ch78 已覆盖 single-agent headroom、
  coordination tax、topology、critical path 与 shared state，是否仅 refine 须等全周 Gate 后比较。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** PARL 在 subagent policy 共同更新、异构模型、失败重试和共享外部状态下是否仍稳定？

### ERNIE 5.0 Technical Report

- **Candidate / Week / Score:** ERNIE 5.0 / 2026-W06 / 29/30；
  `Source Family ID: ernie-5-unified-multimodal-ultra-sparse-moe`。
- **Source / Date / Full-read Coverage:** arXiv:2602.04705，v1 2026-02-04。已读 architecture、unified
  multimodal pretraining、ultra-sparse MoE、elastic depth/width/sparsity、post-training、evaluation、controlled
  ablation 与 appendix。正文对 depth sampling 同时出现 75/25 与 controlled experiment 的 80/20 表述，
  本审计保留该不一致，不自行消解。
- **Problem / Previous Design / Changed Constraint:** 独立训练多种尺寸可得到清晰的 per-model optimum，但
  训练、存储与部署维护成本随型号数增长。部署约束转为同一权重族要适配不同 latency、memory 与算力预算。
- **Mechanism / State / Flow:** 一个 super-network 在同一反向传播中采样 full/submodel paths：depth 在完整层
  与较浅路径间切换，width 在全部与部分 experts 间切换，sparsity 在默认与更小 top-k 间切换。参数共享把
  多个 deployment points 变成一个训练状态，但也让梯度干扰、采样覆盖和校准成为系统问题。
- **Implementation / Evaluation Contract:** controlled ablation 使用 64 experts、3.2B total / 454M active、
  top-k 8、250B tokens 的小型 MoE；其 graceful degradation 结论绑定该训练方案与作者评测。模型整体能力
  结果不能证明任意 super-network 都能无损弹性切换。
- **Evidence Boundary / Trade-offs:** 证据支持在作者设置内共享训练可产生多个可用子网；未证明所有模态、
  hardware 或 SLO 下的 Pareto 最优，也未披露完整 production routing。收益是一次训练覆盖多种预算；代价是
  optimization interference、路径采样不均、子网校准和版本治理复杂度。固定模型在负载稳定、极致性能或
  验证边界严格时仍更容易优化。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from fixed-capacity MoE to elastic execution
  contracts；Ch21 主 owner，Ch24/37 handoff。已读 Ch21、Ch23、Ch24；Books 是否需要补入 deployment-aware
  super-network 机制，待全周 Gate 后决定。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何对不同 depth/width/top-k 子网分别建立 kernel、collective、capacity 与 quality SLO？

### SPARKLING

- **Candidate / Week / Score:** SPARKLING / 2026-W06 / 27/30；
  `Source Family ID: sparkling-width-expansion-pretraining`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02472，v1 2026-02-02。已读 activation-RMS 推导、
  fan-in/fan-out scaling、copy initialization、symmetry lock、optimizer-state reset、asymmetric LR rewarm、
  evaluation、ablation、cost 与 hardware appendix。
- **Problem / Previous Design / Changed Constraint:** 从头训练固定宽度模型最容易保持优化一致性；当训练中途
  扩宽以利用新增预算时，简单复制参数虽能近似保持 forward function，却会让重复单元获得相同梯度与相同
  optimizer state，形成 symmetry lock，新增容量无法分化学习。
- **Mechanism / State / Flow:** 扩宽时按 fan-in/fan-out 调整参数以保持 activation RMS；对新增参数重置或
  区分 optimizer state，并只对新增参数施加 asymmetric learning-rate rewarm，使复制单元脱离对称轨道。
  关键状态不只是 weight，而是 weight、momentum/variance 与 per-parameter schedule 的联合迁移。
- **Implementation / Evaluation Contract:** 主实验使用 64×A100 80GB、global batch 768、200B tokens；
  baseline MoE 约 2.56B total / 450M active。论文在作者 workload 中比较 from-scratch、naive expansion 与
  各组件 ablation；expanded run 仍有轻微 pretraining-loss gap。
- **Evidence Boundary / Trade-offs:** 证据说明 optimizer state 与 symmetry breaking 是中途扩容的一等问题；
  不证明任意架构、规模或数据阶段都能无损扩宽。收益是复用已有训练计算并延后容量决策；代价是状态迁移、
  schedule 设计、短期 loss shock 与 reproducibility 风险。从头训练在预算已知、稳定性优先时仍是基线。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from fixed-shape pretraining to state-aware
  capacity expansion；Ch24 主 owner，Ch21/32 handoff。已读 Ch21、Ch23、Ch24；现有 Ch24 已讨论 optimizer
  state 与 schedule，但缺少“结构变化时联合迁移”的具体机制。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** tensor/sequence/expert parallel layout 改变时，参数与 optimizer state 如何原子迁移并回滚？

### FASA

- **Candidate / Week / Score:** FASA / 2026-W06 / 28/30；
  `Source Family ID: fasa-frequency-aware-sparse-attention`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03152，v1 2026-02-03。已读 RoPE frequency-chunk
  observation、Token Importance Predictor、Focused Attention Computation、GPU-only 与 CPU-offload 实现、
  evaluation、baseline、ablation、calibration 和 appendix。
- **Problem / Previous Design / Changed Constraint:** 全量 attention/KV residency 在长上下文下开销随序列增长；
  固定 window 或全局压缩规则简单且 kernel-friendly，但无法针对 query 动态选择远程 token。约束转为在有限
  GPU memory 与 PCIe transfer budget 中保持 query-dependent retrieval。
- **Mechanism / State / Flow:** Token Importance Predictor 用少量 dominant RoPE frequency chunks 对 key
  打分，再由 Focused Attention 对选中 token 计算完整 attention。memory-oriented variant 将 dominant K
  常驻 GPU，把 non-dominant K 与 V 放在 CPU，按 query 即时传回选中片段。频率分块得分是 selector proxy，
  不是校准后的 attention probability。
- **Implementation / Evaluation Contract:** 论文使用单样本 offline calibration 选择配置，并报告 16 个
  dominant frequency chunks 的主要设置；模型、最大 context 与 selection budget 随实验表而定。文中约
  8× memory reduction 是给定 head dimension、selection ratio 与布局假设下的模型化结果，不是通用硬件事实。
- **Evidence Boundary / Trade-offs:** 证据支持作者模型/任务中的频率感知选择与 memory-quality 折中；不证明
  对 distribution shift、所有 RoPE scaling 或高并发 serving 均稳健。代价包括 selector error、CPU capacity、
  PCIe latency、page/pinning 管理与 prefetch miss。短上下文、带宽受限或高并发场景中 dense/window attention
  仍可能更优。
- **Evolution / ROADMAP / Chapter Read:** `Layering / Dependency` from KV residency to query-dependent
  sparse retrieval；Ch41 主 owner，Ch39/50/51 handoff。已读 Ch39～41、Ch50～51；是否整合须与 HySparse、
  Token Sparse Attention 等同周方案比较后决定。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** selector calibration、CPU transfer 与 batching/scheduler 应由同一控制器共同优化吗？

### Token Sparse Attention

- **Candidate / Week / Score:** Token Sparse Attention / 2026-W06 / 25/30；
  `Source Family ID: token-sparse-attention-prefill`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03216，v1 2026-02-03。已读 dynamic token coverage、
  reversible per-layer/per-head selection、FlashAttention integration、Triton scoring、evaluation、efficiency、
  sensitivity 与 appendix limitation。
- **Problem / Previous Design / Changed Constraint:** dense prefill 规则、实现成熟；但长 prompt 使每层都对全部
  history 重算 attention。固定稀疏模式减少工作量，却难以适配不同 head/layer/query 的相关 token。
- **Mechanism / State / Flow:** 每层每 head 计算轻量 token score，依据 threshold 动态保留覆盖集合；选择只在
  当前层生效，下一层可重新纳入 token，因此是 reversible sparsity。稀疏索引围绕 FlashAttention 组织，Triton
  kernel 负责评分和 compaction；不永久删除 KV state。
- **Implementation / Evaluation Contract:** Llama-3.1-8B 与 Mistral-Nemo-12B，RULER/InfiniteBench，单张
  A100 80GB；主要 threshold 为 0.005/0.008。结果聚焦 prefill，短上下文收益有限，不能外推到 decode 或
  distributed serving。
- **Evidence Boundary / Trade-offs:** 作者实验支持长 prompt 下的 latency/quality 折中；不证明 score 对所有
  domain 均保留关键 token。新增 scoring、index construction、irregular memory access 与误删风险；dense
  attention 在短上下文、规则 batch 或质量风险敏感时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from static sparse masks to reversible dynamic
  prefill sparsity；Ch39 主 owner，Ch14/41 handoff。已读 Ch39～41；等待与 FASA、POP、HySparse 比较 owner。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** dynamic token set 如何与 prefix cache identity、chunked prefill 与 deterministic replay 共存？

### POP: Prefill-Only Pruning

- **Candidate / Week / Score:** POP / 2026-W06 / 28/30；
  `Source Family ID: pop-prefill-only-layer-pruning`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03295，v1 2026-02-03。已读 virtual gates、prefill/decode
  asymmetry、independent KV projections、boundary-token handling、calibration、evaluation、ablation、prototype
  constraints 与 limitations。
- **Problem / Previous Design / Changed Constraint:** 全层执行保持 prefill/decode 一致且最易复用框架；统一
  layer pruning 会同时伤害 prompt encoding 与逐 token generation。论文利用两阶段 workload 不对称：
  prefill 是大矩阵批处理，decode 对每个新 token 的质量更敏感。
- **Mechanism / State / Flow:** 在 prefill 跳过约末三分之一 transformer layers，但保留完整 decode。被跳过层
  仍为 prompt 计算独立 KV projections，使后续 decode 的这些层拥有合法 KV state；最后一个 boundary token
  完整通过网络，以连接 prefill state 与 autoregressive transition。virtual gates 用于选层/校准，而非运行时
  任意动态跳层。
- **Implementation / Evaluation Contract:** calibration 使用 200 samples；速度实验在 A100 80GB、batch 8
  等论文配置中报告，最高约 1.37×。原型基于 monolithic Transformers execution，不包含生产级 distributed
  P/D runtime；方法不降低 peak VRAM，因为各层 KV 仍需存在。
- **Evidence Boundary / Trade-offs:** 证据支持“prefill compute 与 decode quality 可解耦优化”的机制；不证明
  任意模型、batch 或 SLO 均有相同收益。代价是额外 KV projection、校准依赖、边界语义与 framework surgery；
  full-layer prefill 在短 prompt、低风险部署或实现简单性优先时仍成立。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from phase-aware scheduling to phase-aware model
  execution；Ch39 主 owner，Ch40/41/51 handoff。已读 Ch39～41、Ch51；是否进入正文待同周方案比较。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** P/D disaggregation 下，跳层计划、KV materialization 与 model version 怎样成为可验证 contract？

### DFlash

- **Candidate / Week / Score:** DFlash / 2026-W06 / 28/30；
  `Source Family ID: dflash-diffusion-speculative-decoding`。
- **Source / Date / Full-read Coverage:** arXiv:2602.06036，v1 2026-02-05。已读 autoregressive/diffusion
  draft 背景、target-feature conditioning、training objective、block diffusion、exact verification、SGLang
  implementation、evaluation、ablation、sensitivity 和 appendix。
- **Problem / Previous Design / Changed Constraint:** autoregressive draft 与 target 易联合验证、语义清晰；但 draft
  自身仍串行。并行 diffusion draft 缩短 draft critical path，却可能因缺少 target context 造成接受率下降。
- **Mechanism / State / Flow:** target model 的 hidden features 经融合后注入 draft model 每层 KV，形成持续
  conditioning；draft 对 masked token block 并行去噪，再由 target 执行 exact verification，拒绝时回退到已验证
  prefix。正确性仍由 target verifier 保证，draft 只改变候选生成分布。
- **Implementation / Evaluation Contract:** 多数实验在 H200；SGLang 系统实验使用单张 B200、FlashAttention-4、
  concurrency 1～32，并包含 Spec-v2 overlap。与 EAGLE 的部分比较受 Spec-v1/tree-drafting 实现限制；论文报告的
  6× 以上结果只对相应模型、block size、hardware 与并发合同成立。
- **Evidence Boundary / Trade-offs:** 证据支持 target-conditioned diffusion draft 可提高作者设置下的并行度与
  acceptance；不证明普遍吞吐倍数。target hidden-feature storage 随长度线性增长，训练/推理 block-size mismatch
  会退化，并引入 feature versioning、draft/target compatibility 与 rollback 成本。短序列或强 AR draft 下，传统
  speculative decoding 仍可能更简单。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from autoregressive draft trees to target-conditioned
  parallel block drafting；Ch44 主 owner，Ch40/43 handoff。已读 Ch40、Ch43～44；Books 决策待全周 Gate。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** target feature cache 如何随 prefix reuse、model rollout 和 verifier rollback 保持一致？

### SWE-Universe

- **Candidate / Week / Score:** SWE-Universe / 2026-W06 / 29/30；
  `Source Family ID: swe-universe-verifiable-environment-factory`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02361，v1 2026-02-02。已读 PR curation、patch
  separation、building agent、iterative validation、in-loop hacking detection、builder-model training、distributed
  rollout、mid-training/RL、evaluation、quality analysis 与 related work。论文没有独立 Limitations 章节，
  但正文明确列出 task description、Docker environment 与 tests 仍可能错位。
- **Problem / Previous Design / Changed Constraint:** 人工构建少量 SWE environments 能保证质量与可复现性，
  但跨语言、跨 build system 扩展到训练规模时，yield、verifier strength 与单实例成本成为瓶颈。约束从
  “benchmark 可运行”变成“数十万 environment 可构建、可验证、可隔离且 reward 不易被 hack”。
- **Mechanism / State / Flow:** 从 issue-linked PR 分离 fix/test patch；agent 生成统一 `evaluation.sh`，并在
  buggy/resolved 两个 repository states 间原子切换。候选 verifier 必须满足 buggy fail、resolved pass，且
  通过 in-loop hacking detector，失败则带反馈迭代。成功 image 与 verifier 进入 registry，再由不同 agent
  scaffolds rollout，最终 artifact 作为 mid-training 或 RL reward source。
- **Implementation / Evaluation Contract:** 原始池约 33.3M PR，过滤后生产 807,693 instances / 52,960 repos；
  held-out builder benchmark 为 320 PR、8 个语言组。大规模任务在独立 ECS VM 中运行并推送容器 registry；
  作者报告 iterative validation 将 held-out yield 从 82.6% 提到 94%。这些数字绑定其 PR filters、builder model、
  cloud isolation 与 detector，不能当作任意 repository factory 的产率。
- **Evidence Boundary / Trade-offs:** 证据支持 dual-state execution 与 in-loop anti-hacking 比静态脚本检查更强，
  也支持作者数据对其模型训练的迁移收益；不证明 generated verifier 是 complete specification。quality judge
  人工 benchmark accuracy 为 78.72%，ambiguous issue、environment drift、false positive/negative 仍存在。
  人工 curation 在高风险任务仍合理；自动化获得规模，却增加 supply-chain、sandbox、image storage、license、
  flaky test、detector bias 与 reward-hacking failure modes。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from curated benchmarks to a versioned environment
  factory；Ch77 主 owner，Ch62/23 handoff。已读 Ch62、Ch68、Ch77；现有 Ch62 已覆盖 executable verifier 的
  不完备性，Ch77 可能缺少“environment construction 本身也是可重试 workflow”的机制。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** verifier、container、dependency mirror 与 source PR 的联合 identity 如何支持长期 replay？

### FS-Researcher

- **Candidate / Week / Score:** FS-Researcher / 2026-W06 / 27/30；
  `Source Family ID: fs-researcher-persistent-workspace`。
- **Source / Date / Full-read Coverage:** arXiv:2602.01566，v1 2026-02-02。已读 architecture、tools、Context
  Builder、Report Writer、workspace schema、checklists、test-time scaling、DeepResearch Bench/DeepConsult、
  module ablation、limitations、ethical considerations 与 benchmark appendix。
- **Problem / Previous Design / Changed Constraint:** 把全部 observation 留在模型 context 中，控制面简单；
  但长时 research 会挤占检索与写作 token，并在压缩中丢失 evidence。约束变为跨 session 持久化、按需回读、
  中间产物可审计，而不是仅扩大一次调用的 context window。
- **Mechanism / State / Flow:** Context Builder 将任务拆解、网页原文、带引用 notes 与 TODO 写入分层 workspace；
  Report Writer 以该 workspace 为唯一事实入口，按 section 回读并写作。`index.md` 同时承载 topic decomposition
  与知识树，raw sources、derived notes、control files 和 final deliverable 分离；两个 Agent 可跨 session 迭代。
- **Implementation / Evaluation Contract:** web tools 使用 Google SERP/Jina；DeepResearch Bench 用 RACE 与
  FACT，DeepConsult 做多次 judge comparison。GPT-5 ablation 中移除 persistent workspace、dual-agent、
  section-wise writing 都降低作者指标；增加 Context Builder rounds 与分数呈正相关，但不是因果/无限 scaling
  定律，且成本、网页变化和 judge noise 随轮数增加。
- **Evidence Boundary / Trade-offs:** 支持 externalized state 与 staged writing 在两套开放式 benchmark 上的
  framework-level 价值；不证明文件系统容量等于有效 memory，也不保证 source freshness/faithfulness。依赖强
  function-calling backbone；持久化网页会引入版权、敏感数据、prompt injection、stale source、conflict merge
  与 workspace corruption。短任务或事实少的查询仍适合单 Agent/单 context。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from context-only trajectories to artifact-backed
  durable workflow；Ch77 主 owner，Ch71/73 handoff。已读 Ch71、Ch73、Ch77；本书已有 context/memory/workflow
  边界，可能只需用该证据 refine workspace ownership，而非新增文件系统产品叙述。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** derived note 被 source revision 推翻时，怎样传播 invalidation 到 section 与 final claims？

### Wiki Live Challenge

- **Candidate / Week / Score:** Wiki Live Challenge / 2026-W06 / 25/30；
  `Source Family ID: wiki-live-deep-research-evaluation`。
- **Source / Date / Full-read Coverage:** arXiv:2602.01590，v1 2026-02-02。已读 dataset construction、Good
  Article criteria、Wiki Writing/Wiki Fact、judge/human agreement、DRA evaluation、leakage analysis、limitations
  与 appendix settings。
- **Problem / Previous Design / Changed Constraint:** 静态、模型生成 reference 易受过时、同源偏好与质量未知
  影响；使用新近、经人类编辑审查的文章提高 reference quality，却使 reference 本身在线可检索，污染从训练
  leakage 扩展为 test-time opportunity leakage。
- **Mechanism / State / Flow:** 从 2025-03-01～12-01 新建且达到 Wikipedia Good Article 的集合筛选 100 篇、
  15 domains；Wiki Writing 用 39 条 editorial criteria 做 pairwise judge，Wiki Fact 将 reference facts 与生成
  statements 检索匹配，再做 consistency 判断。目标页面引用被单独过滤并计算 statement-level leakage rate。
- **Implementation / Evaluation Contract:** writing judge 选 Gemini-2.5-Pro；用 10 对 article、390 条 criterion
  annotation 校准，human pairwise agreement 为 83.59%。因此结果仍是 model-judge proxy，不是专家逐篇终审；
  100-task scale、English Wikipedia editorial norms 与 agent web access 限制了外推。
- **Evidence Boundary / Trade-offs:** 证据支持将 style、neutrality、coverage、verifiability 与 leakage 分开测量；
  不证明 Wikipedia reference 完整或无偏，也不证明过滤 direct citations 可消除内容复制。live refresh 提高
  freshness，却降低 longitudinal comparability；frozen benchmark 仍适合回归，live benchmark 更适合测
  current research behavior。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from static answer scoring to live, leakage-aware
  report evaluation；Ch62 主 owner，Ch71/77 handoff。已读 Ch62、Ch71、Ch77；现有 evaluation object/dataset/
  judge governance 已覆盖大部分原则，可能 `No Change`，待 Gate 后逐段去重。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何在更新 live set 的同时保留 anchor tasks、judge drift 与跨版本可比性？

### FIRE-Bench

- **Candidate / Week / Score:** FIRE-Bench / 2026-W06 / 28/30；
  `Source Family ID: fire-bench-full-cycle-insight-rediscovery`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02905，v1 2026-02-02。已读 research-tree extraction、
  constrained rediscovery、task filters、claim matching、human validation、agent setup/cost、error taxonomy、
  contamination analysis、false-positive analysis、ethics 与 appendices relevant to evaluator reliability。
- **Problem / Previous Design / Changed Constraint:** 单独测 literature search、idea generation 或 coding，无法
  判断 Agent 能否把 planning、implementation、execution 与 conclusion 连成可信 research cycle。直接要求
  novelty 又缺乏当场可验证 ground truth，因此改为“重新发现已知但隐藏的 empirical finding”。
- **Mechanism / State / Flow:** 将论文抽成 research tree：root question、intermediate subproblems 与由 dataset/
  method/evaluation 定义的 experiment leaves；选择核心 parent node 作为开放 prompt，保留 leaf claims 作为隐藏
  verifier。Agent 得到公开输入并执行实验，最终 claims 与 ground-truth claims 做 entailment matching，trajectory
  failure 再映射到 Planning、Implementation、Execution、Conclusion 四阶段 taxonomy。
- **Implementation / Evaluation Contract:** 最终 30 papers，要求 inputs 公开、核心实验可在约 24 小时/80GB
  A100 级预算内完成、结论可由 figure/table 验证；OpenHands/Codex/Claude Code 同任务三次运行。claim judge
  使用 GPT-5.2，并在 33% subset 上获 human precision 0.95、recall 0.86、F1 0.89。Codex 成本还依赖 3:1
  input/output 假设，不能当作精确成本证据。
- **Evidence Boundary / Trade-offs:** 支持 full-cycle evaluation 揭示 planning 与 conclusion formation failure；
  不证明 benchmark failure 等于科学能力上限。rediscovery 会惩罚有效替代结论，论文日期只能粗略检查 contamination，
  小样本限制统计力度。它比 fragment benchmark 更接近研究流程，但昂贵、依赖 judge，且仍把现实科学压缩为
  已知结论；fragment tests 在诊断单项能力时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from isolated capability tests to executable,
  stage-attributed research evaluation；Ch62 主 owner，Ch77 handoff。已读 Ch62、Ch77；现有正文已有 artifact +
  environment + trace 与 claim provenance，但 FIRE-Bench 可补强“失败归因必须绑定 workflow stage”。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何让 benchmark 接受可复现的 alternative discovery，而不把开放评估变成不可判定？

### SafeGround

- **Candidate / Week / Score:** SafeGround / 2026-W06 / 27/30；
  `Source Family ID: safeground-selective-gui-grounding`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02419，v1 2026-02-02。已读 spatial uncertainty、三个
  dispersion measures、combined score、Learn-Then-Test/FDR calibration、cascade policy、models/dataset、
  baselines、ablation、split sensitivity、limitations 与 appendix robustness。
- **Problem / Previous Design / Changed Constraint:** 直接执行 top-1 GUI coordinate 延迟低；但错误点击可能产生
  不可逆副作用。logit confidence 对 black-box VLM 不可得，verbal confidence 又常失准，系统需要 output-only
  risk sensor 与明确 accept/defer contract。
- **Mechanism / State / Flow:** 对同一 screenshot/instruction 以 temperature 1.0 采样 10 次，从 spatial outputs
  构造 cluster/entropy/dispersion signals并固定加权；在 held-out calibration set 上用 binomial upper bound 选择
  threshold，使 accepted predictions 的 empirical FDR 以 `1-delta` confidence 不超过目标 alpha。超过 threshold
  的请求升级到 stronger model，而不是让 sensor 直接执行动作。
- **Implementation / Evaluation Contract:** 6 个 3B/7B GUI grounding models、ScreenSpot-Pro；100 次随机
  calibration/test split，delta=0.05，fixed weights 0.6/0.2/0.2。不同 model 的最有效 uncertainty component 不同，
  strict FDR 可能没有可行 threshold；作者 improvement 不能外推到分布漂移或真实 GUI action outcomes。
- **Evidence Boundary / Trade-offs:** 支持 calibration 把 uncertainty score 转成 deployment operating point；不证明
  score 是错误概率，也不覆盖 stale screenshot、permission 或 downstream tool side effect。收益是可控 abstention；
  成本是 10× sampling、coverage loss、strong-model cascade latency 与 calibration-set governance。低风险/高吞吐
  场景仍可直接执行，前提是业务接受相应错误率。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from confidence display to policy-bound selective
  execution；Ch62 主 owner，Ch68/74 handoff。已读 Ch62、Ch68；与 Security 中“sensor 不是 authority”一致。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** GUI distribution drift 时，risk bound 何时失效，谁触发 recalibration 或强制 abstain？

### Spider-Sense

- **Candidate / Week / Score:** Spider-Sense / 2026-W06 / 26/30；
  `Source Family ID: spider-sense-intrinsic-agent-risk-screening`。
- **Source / Date / Full-read Coverage:** arXiv:2602.05386，v1 2026-02-05。已读 threat model、Intrinsic Risk
  Sensing、Hierarchical Adaptive Screening、S2Bench construction、Mind2Web-SC/eICU-AC、baselines、metrics、
  ablations、case traces 与 appendix attack implementations。论文没有清晰独立 Limitations 章节，故生产边界
  只能按公开实验合同保守记录。
- **Problem / Previous Design / Changed Constraint:** 每步都调用重型 guardrail 容易增加 latency 与 false positives；
  只在输入/输出边界检查则漏掉 plan、action 与 poisoned observation。多步 Agent 的风险面随 trajectory 演进，
  需要 event-driven、stage-aware screening。
- **Mechanism / State / Flow:** 主 Agent 在 query、plan、action、observation 四阶段产生 risk indicator；触发后先
  将 artifact 规范化，再用 case retrieval/fast similarity 做 coarse screening，模糊项升级到 LLM reasoning。
  最终把 evidence 返回主 Agent，由其产生 Accept/Reject/Sanitize；这仍是 model-mediated decision，不等于独立
  authorization enforcement。
- **Implementation / Evaluation Contract:** Claude-3.5-Sonnet 与 Qwen-max base agents；Mind2Web-SC、eICU-AC
  及作者 S2Bench；对比 static guards 与 GuardAgent/AGrail，以 ASR、FPR、accuracy/F1、agreement 和 latency 衡量。
  8.3% overhead 与 near-optimal defense 是该模型、数据、攻击生成和 screening hierarchy 下的作者结果。
- **Evidence Boundary / Trade-offs:** 支持 stage-local sensing 可减少无差别重审并覆盖 indirect prompt/tool-result
  injection；不证明 Agent 能可靠自我授权，也未覆盖 adaptive attackers、case-store poisoning 或 model-family
  correlated failure。静态 deterministic policy 在权限/参数边界仍不可替代；hierarchical screening 新增 detector
  drift、retrieval poisoning、false negative 与 escalation tail latency。
- **Evolution / ROADMAP / Chapter Read:** `Layering / Dependency` from boundary guardrails to in-trajectory risk
  sensors；Ch68 主 owner，Ch77/74 handoff。已读 Ch68、Ch77；现有 tool boundary 已规定 deterministic executor，
  若吸收只能作为 sensor placement 演进，不能把 authority 下放给 Agent。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** risk sensor、policy engine 与 tool executor 的分歧应如何仲裁、记录和 replay？

### Fast Autoregressive Video Diffusion and World Models

- **Candidate / Week / Score:** Fast Autoregressive Video Diffusion / 2026-W06 / 27/30；
  `Source Family ID: temporal-cache-ann-video-diffusion`。
- **Source / Date / Full-read Coverage:** arXiv:2602.01801，v1 2026-02-02。已读 autoregressive video
  diffusion background、redundancy analysis、ANN formulation、TempCache、AnnCA/AnnSA、proof、Rolling-Forcing/
  LongVie2 experiments、baseline、length scaling、ablation 与 appendix。正文没有独立 Limitations 章节。
- **Problem / Previous Design / Changed Constraint:** dense attention 与完整 KV history 保持质量、实现规则；
  streaming video/world-model rollout 却让 per-step attention、累计计算和 cache memory 随时间增长。LLM 的
  token-level eviction 不能直接假定适用于时空 latent，因为跨帧 correspondence 与重复 denoising 改变了状态。
- **Mechanism / State / Flow:** TempCache 用 ANN 找跨帧对应 key，把近重复组压成最新 representative；相同 keys
  时以 log multiplicity 修正 logits、values 取组均值可保持 exact attention，实际相似 key 合并则是近似。
  AnnCA 按当前 frame query 选择 prompt tokens；AnnSA 复用 semantic buckets 做 block-sparse self-attention。
- **Implementation / Evaluation Contract:** Rolling-Forcing 与 LongVie2，dense FA3 baseline，PSNR/SSIM/LPIPS、
  video benchmark、attention recall/density 和 end-to-end speed；单 H100，最长约 3K-frame rollout。最高约
  5～10× 与 flat peak memory 绑定模型、threshold、LSH/quantization、sparse kernel 与长 rollout，不适用于一般 LLM。
- **Evidence Boundary / Trade-offs:** 支持 temporal correspondence 能把 cache growth 变为 bounded approximation；
  不证明 attention mass recall 等于长期语义一致性。代价包括 approximate-match drift、代表项合并误差、hash/
  quantization overhead、动态 sparse-kernel regularity 与 error accumulation。短 clip 或低重复场景中 dense FA3
  仍可能更快、更易验证。
- **Evolution / ROADMAP / Chapter Read:** `Principle Reuse` from LLM KV lifecycle to modality-specific temporal
  state compression；Ch41 主 owner，Ch39/50 handoff。已读 Ch39～41、Ch50；若 Books 吸收，应强调 state
  equivalence contract，而非复制视频 benchmark。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** approximate merged state 如何定义 error budget、rollback 与跨 diffusion-step invalidation？

### RE-TRAC

- **Candidate / Week / Score:** RE-TRAC / 2026-W06 / 27/30；
  `Source Family ID: re-trac-recursive-trajectory-compression`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02486，v1 2026-02-02。已读 incomplete-branch diagnosis、
  structured compression state、recursive execution、frontier-model prompting、small-model distillation、BrowseComp
  setup、TTS baselines、resource analysis、summarizer sensitivity、conclusion 与 prompts/appendix schema。
- **Problem / Previous Design / Changed Constraint:** 独立 Best-of-N 易并行且错误不共享，却反复访问相同来源；
  单条长 ReAct trajectory 则会遗忘早期计划分支。约束从“增加独立采样数”变为“跨 rollout 复用已验证 evidence，
  同时保留未完成 branches”。
- **Mechanism / State / Flow:** 每轮把 trajectory 与上一状态压成 `verified evidence + analysis/conclusions + source
  inventory/status + uncertainties/gaps`；下一轮把该 state 放在 system prompt 后重新执行 ReAct，默认最多 8 轮。
  这不是无限 context，而是有损 state transition；最后一轮输出作为结果。
- **Implementation / Evaluation Contract:** BrowseComp300，所有模型使用共同 self-hosted search/browse tools；比较
  Pass@1、RE-TRAC@8、majority/weighted voting 与 Best@8。作者观察跨轮 token/tool calls 下降并有 15～20%
  相对 ReAct 增益；4B 使用更强 GLM-4.7 summarizer 改善，30B 不明显，证明 compressor quality 是条件变量。
- **Evidence Boundary / Trade-offs:** 支持 structured cross-run state 减少重复探索；不证明压缩内容真实、完整，
  也不证明 round 增长单调改善。新增 confirmation bias、早期错误固化、source staleness、state injection 与顺序
  critical path；独立 rollouts 在错误相关性低、并行预算足或压缩难验证时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from isolated sampling to stateful recursive search；
  Ch73 主 owner，Ch71/75/77 handoff。已读 Ch71、Ch73、Ch75、Ch77；现有 derived-memory/provenance 论述可能
  已覆盖原则，待 Gate 后判断是否只补 `verified/pending branch` state schema。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 谁验证 compressor 的 evidence status，发现错误后怎样 supersede 跨轮派生结论？

### Training LLMs for Divide-and-Conquer Reasoning

- **Candidate / Week / Score:** DAC-RL / 2026-W06 / 27/30；
  `Source Family ID: dac-rl-test-time-scaling`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02477，v1 2026-02-02；HTML 不可用，已读 32 页 v1 PDF：
  introduction、CoT/DAC diagnosis、division/conquering objectives、algorithm、training curriculum、four benchmark
  evaluation、Pass@1/32、entropy/length analysis、reward alternatives、proof 与 appendix prompts。无独立 limitations。
- **Problem / Previous Design / Changed Constraint:** CoT 与通用 post-training 一致、调用简单；在能力边界处严格
  串行且单路径探索有限。仅在 inference 用 DAC prompt 又与既有 policy distribution 不对齐，常低于 CoT。
- **Mechanism / State / Flow:** policy 先生成多个 subproblem groups，再把原题和一组子题组成 conquering prompt，
  **顺序**求解子题后回答原题。division reward 组合 format、最小子题数与各组是否促成至少一个正确最终答案；
  conquer 只用原题 final-answer correctness。两类 trajectories 进入同一 policy update。
- **Implementation / Evaluation Contract:** Qwen2.5-7B-Instruct 与 Qwen3-4B-Instruct-2507；AIME24/25、Beyond-AIME、
  HMMT25；Pass@1 平均 32 次及 Pass@32，并与 CoT-RL/rollout budget 比较。8.6/6.3-point headline 只属于指定
  Qwen3 setup。最终答案是中间子题正确性的 surrogate，依赖论文 lemma 的 causal assumption，不能逐步验证。
- **Evidence Boundary / Trade-offs:** 支持 reasoning topology 必须进入 training distribution；不证明 DAC 普遍优于
  CoT，也不等同并行执行。新增 division rollouts、parser/format reward、错误子题传播与 sparse credit；CoT 在
  简单问题、低 latency 或缺乏可靠 decomposition reward 时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from inference-only decomposition to jointly trained
  reasoning policy；Ch29 主 owner，Ch75 handoff。已读 Ch29、Ch75；现有 GRPO 已讲 sequence reward 的粗粒度，
  DAC 提供 hierarchical credit assignment 的受限案例。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 若子问题本身有 verifier，process reward 会改善 credit 还是奖励局部正确、全局错误的分解？

### MARS

- **Candidate / Week / Score:** MARS / 2026-W06 / 28/30；
  `Source Family ID: mars-budget-aware-reflective-research-search`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02660，v1 2026-02-02；已读 66 页 PDF 的 problem setup、
  modular construction、comparative reflective memory、budget-aware MCTS、MLE-Bench experiment、ablations、
  lesson provenance、limitations、prompts 与 code examples。
- **Problem / Previous Design / Changed Constraint:** monolithic script generation 快且 context 简单；ML experiments
  却昂贵、失败归因不透明，blind search 会把预算耗在重复或过慢方案。约束变为 repository-level artifact、
  24-hour budget、可比较 experiment branches 与跨 branch credit assignment。
- **Mechanism / State / Flow:** Task Preparation 固化 instruction/environment/objective；MCTS node 是 repository
  solution，可 Draft、Debug 或 Improve。Design-Decompose-Implement 将变更组织为可测试模块和 atomic multi-file
  diffs。Comparative Reflective Memory 对当前方案与 best-known branch 做差异分析，生成带引用 lesson；MCTS reward
  将 validation metric 与 execution time penalty 联合，默认权重 -0.07。
- **Implementation / Evaluation Contract:** MLE-Bench 75 Kaggle tasks，每 task 24h，单 A100 40GB、12 vCPU、
  220GB RAM、1TB SSD。作者 ablation 支持 memory/comparison/search components；过强 penalty -0.15 偏向 trivial
  fast nodes，0 又忽略 cost。评估仅限 MLE-Bench，不覆盖 novel theory、literature synthesis 或 production deployment。
- **Evidence Boundary / Trade-offs:** 支持成本应进入 search objective，且 lesson 需由 branch comparison 产生；
  不证明差分解释具有因果性。MCTS/API/experiment 成本高，validation overfitting、shared-seed noise、lesson
  poisoning 与 stale best branch 均是新 failure modes。小 design space 或昂贵不可逆实验仍适合人工 shortlist。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from evaluator-driven candidate search to budget-aware,
  artifact-and-memory search；Ch77 主 owner，Ch73/75/66 handoff。已读 Ch73、Ch75、Ch77；现有 Evaluator-Driven
  Search 已覆盖 artifact population，MARS 可能补强 cost-aware node identity 与 comparative lesson boundary。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** noisy validation metric 如何进入 MCTS confidence、复测与 promotion gate，而非单值 reward？

### WideSeek

- **Candidate / Week / Score:** WideSeek / 2026-W06 / 27/30；
  `Source Family ID: wideseek-dynamic-wide-research`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02636，v1 2026-02-02。已读 WideSeekBench generation、logical
  composition、simulated corpus/search、main/subagent MDP、dynamic fan-out、trajectory linearization、GRPO、SFT/RL、
  scale/domain/constraint analyses、ablations、failure cases 与 appendices。
- **Problem / Previous Design / Changed Constraint:** fixed-role/fixed-count workers 易部署且预算可预测；broad retrieval
  的实体数量、约束结构与属性 schema 每题不同，固定 fan-out 可能欠分解或浪费。约束从单路径深度变为目标信息量、
  可并行粒度与合并完整性。
- **Mechanism / State / Flow:** main agent 动态调用 `create_sub_agent(k prompts)`；workers 在独立 local MDP 中用
  search/open_page，结果回传 main。所有同权 checkpoint 的 tree trajectories 被线性化为一个 joint sequence，
  用 final table outcome 做 GRPO；benchmark 由 knowledge graph constraints 组合并在 local corpus/search 验证。
- **Implementation / Evaluation Contract:** task 按 4～4096 atomic items、7 constraint types、18 domains 分层；
  Item/Row F1 与 Success Rate。作者结果显示低 volume 差异小，128～4096 显著退化，极端区间 SFT 模型反而减少
  tool calls，推断为 teacher refusal/early-stop inheritance。吞吐/工具倍数不等于 wall-clock parallel speedup。
- **Evidence Boundary / Trade-offs:** 支持 dynamic topology 与 task volume 共同决定效果；不证明任意数量 workers
  单调增益。linearized training 模糊真实 concurrency，final outcome 难分配责任；新增 duplicate search、merge
  conflict、shared-policy correlated errors 与 budget variance。fixed workflow 在规模已知、schema 稳定时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from static worker count to learned dynamic fan-out；
  Ch78 主 owner，Ch29/75/77 handoff。已读 Ch29、Ch75、Ch77、Ch78；现有 Ch78 已要求 decomposability、critical
  path 与 coordination tax，是否只添加 training-credit caveat 待 Gate。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** tree trajectory 线性化后，如何避免把并发顺序 artifact 学成虚假的 causal dependency？

### WideSeek-R1

- **Candidate / Week / Score:** WideSeek-R1 / 2026-W06 / 28/30；
  `Source Family ID: wideseek-r1-width-scaling-marl`。
- **Source / Date / Full-read Coverage:** arXiv:2602.04634，v1 2026-02-04。已读 lead/subagent architecture、20K
  dataset pipeline、MARL objective、agent/token reweighting、reward、width-scaling experiments、single/multi-agent
  baselines、role/data ablations、limitations discussion、credit assignment 与 appendices。
- **Problem / Previous Design / Changed Constraint:** single Agent 保持统一 context，但 broad table retrieval 产生
  context pollution 和串行 critical path。hand-crafted parallel workflows 能隔离 context，却不能按任务自适应组织。
- **Mechanism / State / Flow:** lead 只能调用 `call_subagent`，每轮生成一组 prompts 后 barrier-wait；workers 才能
  browse。shared model 的 lead/workers 端到端训练；rollout outcome 由 Item F1、format、tool-use 与 length 组成。
  agent-level averaging 防止 worker 多的 rollout 在 gradient 中天然占优，token-level reweighting平衡长短轨迹。
- **Implementation / Evaluation Contract:** 4B model、20K HybridQA-derived tasks、目标表 10～50 rows；与 single-agent、
  larger model 和 multi-agent baselines 比 Item/Row F1、success，Avg/Max/Pass@4。增加 agents 的 gain 绑定可并行
  broad search；lead barrier 与外部工具 latency 未形成通用 serving speedup 结论。
- **Evidence Boundary / Trade-offs:** 支持共同训练 orchestrator/worker 与 agent-count normalization；不证明结构性
  credit 已解决。所有 tokens 共享 final rollout advantage，作者也承认无法分辨 lead decomposition 与 worker execution
  failure。更多 workers 新增 barrier straggler、duplicate facts、merge error 与 cost；single Agent 对强耦合任务仍优。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from outcome-only multi-agent RL to count-normalized MARL，
  但 role-specific credit 仍开放；Ch29 主 owner，Ch78 handoff。已读 Ch29、Ch78。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** role-level counterfactual baseline 能否分配 responsibility，同时保持大规模 rollout 可训练性？

### AOrchestra

- **Candidate / Week / Score:** AOrchestra / 2026-W06 / 28/30；
  `Source Family ID: aorchestra-dynamic-agent-contract`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03786，v1 2026-02-03。已读 four-tuple abstraction、delegate/
  finish control flow、SFT/ICL orchestrator learning、GAIA/Terminal-Bench/SWE-Bench setup、context/model-routing
  ablation、plug-in workers、sandbox/tools、prompts 与 cost accounting。论文没有独立 Limitations 章节。
- **Problem / Previous Design / Changed Constraint:** 固定角色/固定工具 worker 易治理，却难覆盖开放任务；纯 context
  isolation 又不能按子任务配置 capability。约束变为每次 delegation 都要同时决定目标、可见状态、能力与成本。
- **Mechanism / State / Flow:** 任一 executor 被实例化为 `Phi=(Instruction, Context, Tools, Model)`；orchestrator
  只能 `Delegate(Phi)` 或 `Finish`，不直接执行 environment action。worker 只看到 curated context，持有指定工具，
  返回 summary、artifact、errors/logs。SFT 学 decomposition/tuple synthesis，iterative prompt optimization 用
  performance + monetary cost 学 model routing。
- **Implementation / Evaluation Contract:** GAIA、Terminal-Bench 2.0、SWE-Bench Verified，多种 backbone；context
  ablation 比较 none/full/curated。Gemini-3-Flash 的 headline improvement 绑定其 prompts、tool set 和 benchmark。
  GAIA 中 AOrchestra Gemini 成本 0.79 vs ReAct 0.07，ICL mixed routing 降至 0.57，说明 accuracy gain 非免费。
- **Evidence Boundary / Trade-offs:** 支持 delegation contract 必须同时绑定 working state 与 capabilities；不证明
  on-demand Agent 比静态角色普遍优，也未证明 tuple 中的 tool choice 等于 authorization。新增 context omission、
  model/tool compatibility、credential delegation、worker cold start、cost variance 与 orchestrator bottleneck。
  固定 worker 在任务稳定、合规边界严格时仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from static roles to runtime-instantiated execution
  contracts；Ch78 主 owner，Ch71/74/77 handoff。已读 Ch71、Ch77、Ch78；现有 identity/delegation 已覆盖权限原则，
  four-tuple 可作为 typed handoff 的机制候选。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** tuple version、credential scope、artifact owner 与 retry idempotency 如何绑定成一次 delegation identity？

### FullStack-Agent

- **Candidate / Week / Score:** FullStack-Agent / 2026-W06 / 25/30；
  `Source Family ID: fullstack-agent-development-verification-backtranslation`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03798，v1 2026-02-03。已读 FullStack-Dev agent roles/tools、
  development-oriented frontend/backend/database testing、error feedback、Repository Back-Translation/Augmentation、
  iterative SFT、FullStack-Bench、training/inference settings、ablations、test reliability、error analysis 与 prompts。
  无独立 Limitations 章节。
- **Problem / Previous Design / Changed Constraint:** screenshot/appearance evaluation 可快速判断前端，但会把没有真实
  backend/database semantics 的页面当作 full-stack success。约束从“生成看起来正确的页面”升级为跨 UI action、
  API response、database side effect 的一致性验证，同时需要真实 repository-derived training trajectories。
- **Mechanism / State / Flow:** coding agent 生成系统；GUI/API/database test agents 分别执行并把 error trace 回传。
  Back-Translation 先读取真实 repo 生成 instruction/plan，再在空 template 中重建；rule-based transform 删除原 repo
  痕迹并规范化成 development trajectory。初轮 SFT 改善模型后，再生成 augmented repos/trajectories并重新训练。
- **Implementation / Evaluation Contract:** FullStack-Bench 101 instructions、647 frontend、604 backend、389 database
  cases；back-translation temperature 0.5、context 131,072，主要 Qwen3-Coder 30B-A3B/480B-A35B variants。
  benchmark performance 绑定其 templates、test agents、appearance judge 与 generated task distribution。
- **Evidence Boundary / Trade-offs:** 支持 outcome verifier 应覆盖数据平面而不只 UI；不证明 agent-generated tests
  完整，也不证明 back-translated trace 等同真实 developer intent。新风险包括 license/provenance、repository secret、
  trace leakage、template bias、test gaming 与 self-training error amplification。人工 curated tasks 在安全关键领域仍必要。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from visual artifact scoring to cross-layer executable
  verification；Ch62 主 owner，Ch77/24 handoff。已读 Ch62、Ch77；现有 artifact/environment/verifier 边界较完整，
  该候选更可能作为受限案例而非新原则。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何证明 test agents 本身没有共享同一 model blind spot，并保存 side-effect rollback evidence？

### MemSkill

- **Candidate / Week / Score:** MemSkill / 2026-W06 / 28/30；
  `Source Family ID: memskill-evolving-memory-operations`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02474，v1 2026-02-02。已读 skill representation、controller/
  executor/designer、hard-case buffer、skill evolution、snapshot rollback/early stop、新 skill exploration、LoCoMo/
  LongMemEval/HotpotQA/ALFWorld evaluation、transfer、sensitivity、case studies 与 appendix algorithm。无独立 limitations。
- **Problem / Previous Design / Changed Constraint:** 固定 write/update rules 易预测，但在不同 interaction pattern 下会
  过存、漏存或错误覆盖。约束从“存哪些 facts”扩展为“memory operation policy 自身如何根据失败证据演进”。
- **Mechanism / State / Flow:** skill bank 中每项含 applicability description 与 extraction/revision instructions；controller
  为当前 span/已有 memory 选 Top-K skills，fixed executor 输出 structured updates。query task reward 训练 controller，
  failures 进入 sliding hard-case buffer；designer 周期性改写/新增 skills。cycle tail reward 不改善则回滚 best snapshot，
  patience 耗尽则 early stop；新 skills 通过短暂 logit bias 获得探索机会。
- **Implementation / Evaluation Contract:** LoCoMo、LongMemEval、HotpotQA distribution shift 与 ALFWorld；Top-K、
  controller steps/evolution cycle 等为论文配置。跨 HotpotQA 结果部分依赖 LLM judge；K=7 的最优点不应外推。
  task reward 改善只证明这些环境下的 downstream utility，不证明 memory truthfulness 或用户级安全。
- **Evidence Boundary / Trade-offs:** 支持 memory lifecycle 可分为“内容状态”和“操作策略状态”；不证明 designer
  生成的 skill 因果正确。新增 skill drift、controller/executor mismatch、hard-case selection bias、rollback lineage 与
  shared-bank poisoning。静态 rules 在合规、可解释或数据稀少场景仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from storing episodes to versioning the memory operator；
  Ch73 主 owner，Ch76 handoff。已读 Ch73、Ch76；现有 Ch73 已有 derived strategy/provenance/rollback，但可补强
  operator policy 与 content 的双状态边界。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** skill-bank rollback 后，由旧 skill 写出的 memory items 是否也应失效或重新验证？

### D-CORE

- **Candidate / Week / Score:** D-CORE / 2026-W06 / 27/30；
  `Source Family ID: d-core-decomposition-tool-use-rl`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02160，v1 2026-02-02。已读 lazy-reasoning diagnosis、tool-task
  categories、self-distillation/decomposition algorithms、sequential/parallel composition、DA-GRPO entropy advantage、
  theorem、reward、40K/5K data setup、BFCLv3/tau-bench、ablations、failure cases 与 prompts。
- **Problem / Previous Design / Changed Constraint:** 直接 multi-turn reasoning 在简单工具链上高效；复杂依赖会出现
  premature call、状态遗漏与 lazy reasoning。仅做 vanilla GRPO 时，group reward 相同会产生 zero-advantage tokens，
  训练可能停滞。
- **Mechanism / State / Flow:** 模型先按 system policy、tools、history 与 reference trajectory 自蒸馏 decomposition；
  顺序子任务将 `(tool call, observation)` 累积进下一状态，并行子任务从共同 context 出发后 compose。verified traces
  用于 SFT；DA-GRPO 在原 advantage 为零的位置加入 clipped、detached token entropy offset，以维持非零更新。
  reward 为 format/structure/key/value 组合。
- **Implementation / Evaluation Contract:** 40K self-distillation、5K RL，Qwen3-8B 等，在 BFCLv3 multi-turn 与
  tau-bench 测试。表中 vanilla GRPO 在 BFCL multi-turn 甚至下降，自蒸馏规模也非单调；最终增益依赖 reference
  trajectories、few-shot decomposition 与 exact tool schema。
- **Evidence Boundary / Trade-offs:** 支持 decomposition training 与 tool-state transition 必须联合；不证明 entropy
  bonus 生成的 token 更正确，也不证明所有 task 应拆分。新增 teacher/reference leakage、过度分解、parallel side
  effects、compose errors 与 reward gaming；简单/不可分任务仍应直接执行。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from prompt-only planning to decomposition-aware SFT +
  RL；Ch29 主 owner，Ch75/74 handoff。已读 Ch29、Ch75；其价值是把 zero-advantage 与 hierarchical tool trace 关联。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** entropy-derived update 如何与 verifier-derived step credit 分离，避免只增加多样性而不增正确性？

### Sage

- **Candidate / Week / Score:** Sage / 2026-W06 / 27/30；
  `Source Family ID: sage-agent-retriever-interface`。
- **Source / Date / Full-read Coverage:** arXiv:2602.05975，v1 2026-02-05。已读 benchmark curation、short/open
  questions、corpus/index construction、retrievers/agents、Exact Match/Weighted Recall、query analysis、corpus-level
  test-time scaling、agent-strength ablations、limitations 与 appendix query-locality findings。
- **Problem / Previous Design / Changed Constraint:** one-shot dense retrieval 假设自然语言 query 与 retriever training
  分布相似；deep-research Agent 会生成多轮、keyword-like subqueries，并把 retrieval 与 planning 耦合。更强 semantic
  encoder 因接口分布错位，不一定带来更好 end-to-end research。
- **Mechanism / State / Flow:** Sage 提供短问与 open-ended query、ground-truth papers 及受控 corpus。索引把 PDF
  转 Markdown，表格单独解析，每篇只嵌入前 32K tokens。corpus-level scaling 扩展候选/rerank budget；评价从
  short-form EM 扩展到带 seed/reference 权重的 recall，并同时记录 searches/references。
- **Implementation / Evaluation Contract:** 四 domain，各 150 short + 150 open questions；corpus 约 37K～50K PDFs。
  BM25@10 在作者 short-form 表格中优于所测 dense/reasoning retrievers；open-ended 只小幅改善，归因于 agent query
  diversity不足。early-answer locality、32K truncation 与未 fine-tune agent 都影响结果。
- **Evidence Boundary / Trade-offs:** 支持 retriever quality 是 `query generator × index × ranking × context use` 的
  joint contract；不证明 BM25 普遍优于 dense，也不证明 ground-truth citation set 完整。增加 test-time retrieval
  compute 会加重 latency、duplicate evidence 与 context packing；lexical retrieval 在 entity/keyword query 仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from standalone retriever benchmark to agent-conditioned
  retrieval evaluation；Ch72 主 owner，Ch62/71 handoff。已读 Ch62、Ch71、Ch72；现有 RAG 已区分 retrieval metrics，
  但可补 query-distribution compatibility。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** retriever-aware query policy 应由 Agent 学、gateway rewrite，还是由 hybrid retrieval 自适应吸收？

### Focus-dLLM

- **Candidate / Week / Score:** Focus-dLLM / 2026-W06 / 28/30；
  `Source Family ID: focus-dllm-confidence-guided-state-refresh`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02159，v1 2026-02-02。已读 dLLM inference/cache background、
  temporal confidence analysis、active-query prediction、sink-aware KV pruning、sparse attention、UltraLLaDA/Dream-7B
  experiments、baseline、LongBench/latency、ablation、sensitivity 与 limitations。
- **Problem / Previous Design / Changed Constraint:** autoregressive KV cache 假设过去 token state 不再改变；dLLM
  bidirectional denoising会持续更新 masked/unmasked states，只能近似复用。block-level refresh 简单但忽略下一步
  实际会变化的 token 与动态 attention sinks。
- **Mechanism / State / Flow:** 用上一步 confidence 对仍 masked positions 排序，选择预计下一步 unmask 的 focus
  set，并以 local window 扩成 active queries；只对这些 queries 计算 key relevance，同时保留动态 top-N attention
  sinks，再从 prompt/response state 中组装 sparse KV。未选 token 复用旧 KV，故 freshness 是 per-step近似状态。
- **Implementation / Evaluation Contract:** UltraLLaDA 与 Dream-7B-Instruct，对 Vanilla、Fast-dLLM、SparseD、
  Sparse-dLLM；LongBench 与 32K context efficiency。最高 19.95× 是特定 dLLM/context/hyperparameters 下相对
  baseline 的作者结果；论文承认 accuracy 略低于 SparseD、参数人工设置且未覆盖 multimodal。
- **Evidence Boundary / Trade-offs:** 支持“下一状态预测”可指导 selective refresh；不证明 confidence 是 cache-validity
  概率，也不适用于 AR decode。代价是 stale KV、sink misselection、manual thresholds、irregular gather 和 domain
  sensitivity；dense/native inference 在短 context 或 correctness-first 部署仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from block-wise approximate cache to predicted per-step
  refresh + sink preservation；Ch41 主 owner，Ch40/44 handoff。已读 Ch40、Ch41、Ch44；若吸收应作为 state
  freshness/invalidation 的 dLLM 分支，不覆盖 AR KV invariants。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** confidence drift、cache freshness 与 rollback 如何成为 scheduler 可观测的 typed metadata？

### LycheeDecode

- **Candidate / Week / Score:** LycheeDecode / 2026-W06 / 28/30；
  `Source Family ID: lycheedecode-hybrid-head-sparse-decode`。
- **Source / Date / Full-read Coverage:** arXiv:2602.04541，v1 2026-02-04。已读 Introduction、Related Work、
  HardKuma head specialization、constrained objective、algorithm、training/evaluation setup、LongBench/RULER/
  reasoning results、sparsity/head-identification ablations、TileLang kernel、implementation appendix 与 limitations。
- **Problem / Previous Design / Changed Constraint:** eviction 能缩小 KV capacity，但会永久丢失 token；selection-based
  sparsity 保留完整 KV，按 query 减少读取，却常让一层所有 heads 共享同一 token set。后者在相邻层 token overlap
  较高时合理，但忽略不同 head 的 retrieval function。约束从“跨层共享多少”变为“谁负责刷新 selector state”。
- **Mechanism / State / Flow:** 少数 retrieval heads 读取完整 KV、执行 dense attention 并将 top-k indices 传给下一层
  同 index head；多数 sparse heads 只读取继承 indices 指向的 KV，且不刷新集合。首层所有 heads 为 retrieval。
  HardKuma 为每个 head 学近二值 role，训练时混合 dense/sparse path，以 logit distillation 加带期望 `L0` budget 的
  Lagrangian；推理按 `E[z] > 0.5` 固化 role。Q/K/V output channels 预重排，kernel 按 head workload 分组执行。
- **Implementation / Evaluation Contract:** Llama3-8B、Qwen3-8B 与 R1 distilled 7B/8B；LongBench、RULER、AIME24、
  OlympiadBench。head identification 在单张 A100 80GB、batch 1 上训练 3,000 steps；passkey/BookSum prompt 1K～10K，
  HotpotQA 1K～20K，critical-token ratio 30%、retrieval-head budget 32。`2.7x @ 128K` 是 greedy decode、单 batch、
  固定 4,096 sparse budget、作者 TileLang kernel 相对 FlashAttention-2 的 TPOT 结果，不是 serving SLO。
- **Evidence Boundary / Trade-offs:** 论文证明该 head-role/selector-sharing 组合在作者模型与任务中可改善 quality/latency
  trade-off；不证明 sparse heads 的 inherited indices 始终正确，也不减少完整 KV 的存储量。固定 per-head budget、
  retrieval-head imbalance、跨层 stale selection、cache-correction 依赖与专用 kernel 是新增成本；短 context、容量优先
  或 framework 未集成时，dense attention、eviction 或 layer-level sharing 仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from layer-shared selector to head-scoped refresh/reuse；
  Ch22 主 owner，Ch14/15/40/41/45 handoff。已读 Ch14～15、Ch19、Ch22、Ch39～41、Ch45；现有 Ch22 已建立
  native sparse 的 training/kernel contract，但尚未展开 selector ownership granularity。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** selector indices 与 full KV 分别由谁 version、失效和迁移，batching 后 head imbalance 如何进入调度？

### OmniSIFT

- **Candidate / Week / Score:** OmniSIFT / 2026-W06 / 25/30；
  `Source Family ID: omnisift-modality-asymmetric-compression`。
- **Source / Date / Full-read Coverage:** arXiv:2602.04804，v1 2026-02-04。已读 modality compression taxonomy、
  STVP/VGAS formulas、training setup、五个 audio-video benchmarks、efficiency table、structural/paradigm/selector-depth
  ablations、case study 与 appendix。论文无独立 limitations section。
- **Problem / Previous Design / Changed Constraint:** independent audio/video pruning 实现简单但忽略 cross-modal dependency；
  symmetric compression 假设两个 modality 可互相对等提供 saliency，在 scoreboard 等视觉事实主要场景会误删关键 patch。
  新约束是 compression budget 应由 information role 而非 token source 均匀分配。
- **Mechanism / State / Flow:** 每个 multimodal chunk 先以 STVP 对第一帧相对全局均值的 cosine distance 提取 spatial
  anchors，并以相邻帧 patch difference 提取 temporal changes；再由单层、8-head、512-dim VGAS 用 visual anchors
  cross-attend audio tokens，按两个 retention ratios 选择最终 token sequence。视觉先筛、音频后受视觉条件筛选，
  因而是显式非对称 dataflow。
- **Implementation / Evaluation Contract:** Qwen2.5-Omni-7B/3B，AVoCaDO 107K pairs，仅微调 LLM decoder 与 VGAS，
  learning rate `1e-5`、global batch 128；VideoMME-audio、DailyOmni、WorldSense、OmniVideoBench 与 video-SALMONN-2，
  retained ratio 35%/25%，2 FPS、最多 256 frames。硬件、并发、precision 与 SLO 未披露；WorldSense latency/memory
  只是作者单次 workload contract，不能泛化为在线服务容量。
- **Evidence Boundary / Trade-offs:** ablation 支持 spatial/temporal cues 与 vision-guided audio selection 在所测数据有效；
  不证明 video 在所有 omni-modal task 中都拥有更高 truth authority，也不证明超过 full-token 的小幅分数是去噪因果。
  固定 ratio、chunk boundary、视觉缺失/遮挡、audio-primary events 与 learned selector drift 是 failure modes；对话、音乐、
  ASR 主导任务仍可能需要 audio-first、symmetric 或保留全 token。
- **Evolution / ROADMAP / Chapter Read:** `Principle Reuse` from uniform token pruning to modality-role-aware budget；
  Ch22 暂作 token-capacity owner，Ch17/38 handoff。已读 Ch17、Ch21～22、Ch38；现有 80 章没有独立 multimodal
  architecture owner，Books 阶段须先确认这是 Ch22 的受限案例还是结构缺口，不能硬塞进 Transformer Layer。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 当 audio 是因果主信号或两模态冲突时，谁动态切换 compression direction 并校准 abstention？

### HySparse

- **Candidate / Week / Score:** HySparse / 2026-W06 / 28/30；
  `Source Family ID: hysparse-oracle-selection-kv-sharing`。
- **Source / Date / Full-read Coverage:** arXiv:2602.03560，v1 2026-02-03。已读 sparse/hybrid background、modified
  FlashAttention score output、full/sparse block architecture、two-branch equations、1T/200B/500B-token training、7B/
  80B evaluation、RULER、SWA/KV-sharing ablations、discussion 与 offload outlook。
- **Problem / Previous Design / Changed Constraint:** pure full attention 保留全局寻址但成本高；interleaved full + SWA
  便宜且保留 locality，却在 full-to-local ratio 激进时丢失远程信息；独立 sparse selector 又会增加训练与 KV/index state。
  约束变为让少量 full layers 同时承担 global compute、oracle selection 与可复用 state owner。
- **Mechanism / State / Flow:** 每个 hybrid block 为一层 full attention 后接 N 层 sparse attention。full layer 的 modified
  FlashAttention 额外输出 block max scores，TopK blocks（默认 1,024 tokens、block 64）及该层 KV 被后续 global sparse
  branches 共用；GQA group 用 max 合并 indices。每个 sparse layer 另有自己 128-token SWA KV，经 sigmoid gate 融合。
  global 与 local state 故意分离：SA 可复用 full-layer KV，SWA 强制保留当前层局部 representation。
- **Implementation / Evaluation Contract:** 7B dense 36 layers、full:sparse 1:3，训练 1T×8,192 后 200B×32,768；
  80B-A3B MoE 49 layers、8/512 experts、ratio 1:11，训练 500B×32,768；BF16 仅对 7B 明示。general benchmarks 与
  RULER 16K/32K；硬件、kernel latency、batch/concurrency 与生产 SLO 未披露，因此“显著降低 compute/KV”不是
  已验证 serving speedup。
- **Evidence Boundary / Trade-offs:** 训练与 ablation 支持在作者模型中 global selected state 可跨层共享、local SWA state
  不应共享；不证明 full attention 可消失，也不证明 offload 设想已有实测。TopK/block/group-max 会牺牲 per-head
  granularity，full layers 仍是 quadratic refresh points，跨层 KV 还改变表示 ownership；纯 full 或 full+SWA 在较短窗口、
  实现简单性与低迁移风险场景仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from full+local hybrid to full-owned global sparse state +
  layer-local SWA state；Ch22 主 owner，Ch14/19/41/50 handoff。已读 Ch14、Ch19、Ch22、Ch40～41、Ch50；与
  LycheeDecode 一起说明 selector granularity 与 KV ownership 是两个独立设计轴。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** full-layer refresh interval、跨层 KV identity 与 speculative rollback 如何共同进入 runtime contract？

### From Data to Behavior

- **Candidate / Week / Score:** From Data to Behavior / 2026-W06 / 27/30；
  `Source Family ID: data2behavior-pretraining-risk-proxy`。
- **Source / Date / Full-read Coverage:** arXiv:2602.04735，v1 2026-02-04。已读 Data2Behavior task、MDF equations、
  bias/safety dataset construction、LoRA/full-FT baselines、keyword/semantic/random baselines、GPU-time comparison、
  scaling/layer/position analysis、mechanistic discussion、appendix evaluation 与 limitations。
- **Problem / Previous Design / Changed Constraint:** keyword、LLM semantic screening 与 human review 对显式风险有效，
  但“表面 benign、训练后迁移出 bias/unsafe behavior”的数据只能在 fine-tuning 后发现，成本高。新问题不是判断单个
  sample 是否恶意，而是用 base model 对 candidate dataset 的 aggregate representation 做训练前风险诊断。
- **Mechanism / State / Flow:** 用 vanilla model 对 dataset 每条样本 forward，取各层最后 token hidden state 并求均值，
  形成 layer-wise data feature signature；在 risk test inputs 推理时以系数 `alpha` 注入相应 activations，观察行为是否沿
  实际 fine-tuning 后方向变化。它是 activation intervention proxy，不更新参数，也不是 instance attribution。
- **Implementation / Evaluation Contract:** Qwen3-14B、Qwen2.5-32B-Instruct、Gemma-3-12B-it，A100；bias 数据 LoRA
  rank 64、alpha 128、3 epochs，safety 数据 full FT 3 epochs，均 `lr=1e-5`。作者单 A100 GPU-time table中 MDF 约为
  tuning 的 20%，但 batch、precision 与完整 workload 未统一披露。实验集中于作者构造 bias sets、Alpaca benign
  instruction 与 secure/insecure code transfer。
- **Evidence Boundary / Trade-offs:** 结果支持 aggregate hidden signature 可作为所测开放模型/数据上的预训练诊断；
  不证明它预测任意混合语料、闭源模型或具体 sample 的 causal contribution。大 `|alpha|` 会使 representation collapse，
  mean pooling 隐去 minority risk，layer/position/scaling 都需校准；真实 production mixture、distribution shift 与 false
  positive cost 未解决。传统 filtering 与 post-training evaluation 仍不可替代。
- **Evolution / ROADMAP / Chapter Read:** `Layering / Dependency` from content screening to model-conditioned behavioral
  risk proxy；Ch23 主 owner，Ch62/68 handoff。已读 Ch22～24、Ch62、Ch68；现有 Ch23 已把 data 定义为 behavior
  specification，但缺少“训练前 proxy 不是因果证明”的证据层级。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何在含少量 risky + 大量 normal data 的 mixture 中校准 operating point，并追踪 false negatives？

### Length-Unbiased Sequence Policy Optimization

- **Candidate / Week / Score:** Length-Unbiased Sequence Policy Optimization / 2026-W06 / 27/30；
  `Source Family ID: luspo-sequence-length-weighting`。
- **Source / Date / Full-read Coverage:** arXiv:2602.05261，v1 2026-02-05。已读 GRPO/GSPO derivation、length-bias
  analysis、LUSPO objective/gradient、dense/MoE/VL setup、training curves、benchmarks、cross-dataset ablation 与 conclusion。
  论文无独立 limitations section。
- **Problem / Previous Design / Changed Constraint:** token-average GRPO 让每个 sequence 总 gradient 近似随 `1/|y|`
  缩小；GSPO 虽改用 geometric-mean sequence likelihood，loss 仍按 sequence 聚合，并在 Clip-Higher 下使 negative samples
  更常被 clip，可能让正样本梯度主导并缩短 response。旧 weighting 对控制单条 trajectory 影响合理，但与长推理探索
  发生冲突。
- **Mechanism / State / Flow:** LUSPO 保留 GSPO group advantage、sequence likelihood ratio 与 clipping，仅将每个
  sequence clipped term 乘 `|y_i|`；在作者推导中它抵消 `log s_i` gradient 的 `1/|y_i|`，使 sequence 对 token-sum
  gradient 的权重不再随长度被平均掉。它改变的是 optimization measure，不是 reward/verifier 或 reasoning semantics。
- **Implementation / Evaluation Contract:** Qwen2.5-7B-Base、Qwen3-30B-A3B-Instruct、Qwen2.5-VL-7B-Instruct；
  8×H800（dense/VL）与 4×8 H800（MoE），verl，prompt batch 128、8 rollouts、mini-batch 16，text max 32,768、VL
  max 4,096，`lr=1e-6`。DAPO-MATH-17K、ViRL39K；AMC23/AIME24/25/MATH500 与 VL benchmarks。precision、
  policy lag、SLO 未披露。
- **Evidence Boundary / Trade-offs:** 作者实验支持该 weighting 在所测 recipe 下避免 GSPO length collapse并提高 scores；
  不证明 response 越长 capability 越强，也未隔离额外 generated tokens、reward opportunity 与 compute 的因果贡献。
  乘 length 会放大长错误 trajectory、straggler、memory 与 verifier cost，并可能鼓励 verbosity；短答案任务、严格 budget
  或没有 collapse 的分布仍可能保留 GSPO/GRPO weighting。
- **Evolution / ROADMAP / Chapter Read:** `Direct Evolution` from token-average GRPO to GSPO sequence clipping，再到
  length-rescaled sequence objective；Ch29 主 owner，Ch28/30 handoff。已读 Ch28～30；现有 Ch29 已警告 response/token
  normalization variants，却尚未给出 length measure 怎样改变 effective objective。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何在 unbiased credit、verbosity penalty、token budget 与 tail-latency 之间定义多目标 objective？

### Infinite-World

- **Candidate / Week / Score:** Infinite-World / 2026-W06 / 27/30；
  `Source Family ID: infinite-world-hierarchical-latent-memory`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02393，v1 2026-02-02。已读 world-model background、HPMC、
  uncertainty-aware action labels、revisit-dense strategy、1.3B/H800 setup、VBench/human evaluation、memory/UAL/RDD
  ablations、user-study appendix 与 future work。无独立 limitations section。
- **Problem / Previous Design / Changed Constraint:** direct history conditioning 保真且简单，但 memory 随 frames 线性增长；
  synthetic pose/action labels 精确，却不适用于 noisy real video；普通 internet trajectories 很少 loop closure。约束从短期
  visual continuation 转为在 bounded state 下保存 long-horizon revisit information，并从弱动作标签学习。
- **Mechanism / State / Flow:** HPMC 在短历史用 temporal encoder 4× direct compression；超出 budget 后把 latent history
  滑窗分块，先 local compression，再 concat 后用同一 encoder global compression到固定 `T_max`，并与 last-frame local
  latent、noisy target 一起输入 DiT。compressor 与 backbone 联训。pose estimator 的 translation/rotation 经两个阈值变成
  no-op/action/uncertain；30-minute revisit-dense data 再激活 loop-closure。
- **Implementation / Evaluation Contract:** Wanx-2.1-1.3B，16×H800；pretrain >30h real video，history 最多 4 chunks，
  finetune history 1～16 chunks，RDD 30 minutes；320 frames 递归压到 `T_max=20`。100 generated initial scenes、10 manually
  designed 16-chunk trajectories、VBench 加 30 volunteers/300 pairwise trials。memory curve在单张 80GB H800上显示 no
  compression >180 frames OOM、hierarchical约 45GB至1,300 frames；batch/precision/concurrency 未披露。
- **Evidence Boundary / Trade-offs:** 结果支持 bounded latent summary、revisit-dense examples 与 uncertainty labels 在作者
  world model 中互补；不证明 45GB plateau 等于 constant compute，也不证明视觉回访一致等于 causal/physical state
  correctness。递归压缩会丢 provenance/detail，训练 horizon 外曾发生 catastrophic collapse，pose thresholds、human
  preference、generated-scene distribution 与 cumulative drift 都限制外推；短轨迹或有可靠 geometry 时，direct history/
  explicit map 仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Principle Reuse` from full latent history to hierarchical lossy state；Ch10 主 owner，
  Ch22/73 handoff。已读 Ch9～10、Ch22、Ch72～74；它不是 Agent durable memory，Ch73 只能承接 provenance/forgetting
  类比，不能共享 truth authority。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何让 compressed latent 支持可定位纠错、reset 与 counterfactual action validation，而不只视觉偏好？

### DASH

- **Candidate / Week / Score:** DASH / 2026-W06 / 27/30；
  `Source Family ID: dash-batched-shampoo-preconditioning`。
- **Source / Date / Full-read Coverage:** arXiv:2602.02016，v1 2026-02-02。已读 Shampoo/Distributed Shampoo、EVD/CN/
  Newton-DB、scaling convergence、multi-Power-Iteration、3-D block layout、load balancing/state partition、Llama-953M
  evaluation、precision trade-offs、Chebyshev appendix、numerical precision 与 discussion/future work。
- **Problem / Previous Design / Changed Constraint:** Shampoo 的 matrix preconditioner 捕获 coordinate correlation，但 inverse
  roots昂贵；block Shampoo降低规模后，list-of-blocks、EVD 与低更新频率仍造成 fragmented GPU execution。旧的每 10～100
  steps 更新 preconditioner 用 stale curvature 换 runtime，约束变成能否把更多、更频繁的小矩阵工作变成 tensor-core
  friendly batch，同时维持数值收敛。
- **Mechanism / State / Flow:** 各层 gradient/preconditioner blocks 按 shape stack 成 3-D tensors，批量计算 Gram、inverse
  root 与 preconditioned updates，减少 list fragmentation；optimizer states按 greedy load balance 分配到 8 workers，更新后
  broadcast parameters。DASH 同时引入 Newton-Denman-Beavers 与 Chebyshev inverse-root paths，并用 batched half-precision
  multi-Power-Iteration估计每个 block spectral radius，使 Newton iterations满足 convergence region。
- **Implementation / Evaluation Contract:** 953M Llama、embedding 2,048、sequence 1,024、global batch 2M tokens、C4
  Chinchilla 20 tokens/parameter、9,089 steps、3 seeds；8 GPUs，block 1,024/2,048，EVD frequency 1/10、CN/NDB 1。
  具体 GPU 型号未披露。`up to ~5x` 只比较 optimizer step configuration；作者示例 full train由约10h53m降至10h21m，
  即约5%，不能写成端到端训练5倍。
- **Evidence Boundary / Trade-offs:** 证据支持“数学复杂度未变但 execution granularity/normalization 仍可主导 wall time”；
  不证明 Shampoo 普遍优于 AdamW，也未验证更大模型、tensor parallel 或所有 precision。FP16 CN 稳定且快，FP16 NDB
  会不稳定；更大 block 未带来明显 perplexity gain却更慢；Chebyshev 结果仍 preliminary。新增 block padding、condition
  estimation、solver selection、state redistribution 与 broadcast cost；对小模型/小 block 或低频 update，既有实现仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Layering / Dependency` from second-order optimizer math to batched numerical kernel
  and distributed state ownership；Ch24 主 owner，Ch31/32 handoff。已读 Ch23～25、Ch31～32；Ch24 已把 optimizer 纳入
  parameterization contract，但尚未区分 optimizer-step speedup 与 end-to-end training speedup。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 能否按 block condition number动态选 solver/precision，并把选择、state migration 与 recovery 写入 checkpoint？

### Claude Opus 4.6 source family

- **Candidate / Week / Score:** Claude Opus 4.6 source family / 2026-W06 / 23/30；
  `Source Family ID: anthropic-claude-opus-4.6`。
- **Source / Date / Access:** Anthropic announcement，2026-02-05；announcement、benchmark footnotes、
  product/API updates 与 system-card link 已核验。官方 system card 为约 13 MB 文档，当前 primary-source
  读取通道因内容长度拒绝抓取；没有用搜索摘要、发布页或第三方转述冒充 system-card 全文。
- **Verified Facts:** API 公布 adaptive thinking、四级 effort、context compaction beta、1M-token context
  beta 与 128K output；announcement 指向 agentic coding、computer use、search、cyber 等评测，并声明新增
  cyber probes。它们是版本/API/评测事实，不公开 model architecture、training recipe 或 compaction 内部算法。
- **Evaluation Boundary:** announcement 的 benchmark 数字受 sample count、effort、compaction、tool harness、
  token budget 与 vendor protocol 约束；customer quotations 不是独立实验。完整 capability/safety methodology、
  subgroup failure、ASL assessment 与 limitations 必须以 system card 为准。
- **Evolution / ROADMAP / Chapter Read:** `Version Fact / Mechanism Not Disclosed`；Ch22 可承接 long-context
  contract，Ch62 承接 evaluation identity，Ch77/78 承接 long-running workflow；已读 Ch22、Ch62、Ch77～78。
  这些 API 能力不能证明模型内部如何实现长期记忆或 planning。
- **Integration Decision:** `Unverified / Blocked`。system card 未全文取得前不修改 Books，也不把该候选
  计作完整 Source Review。
- **Open Questions:** 能否取得可解析的 system-card artifact，并核对长上下文、agentic/cyber eval 的完整
  harness、sample、budget、failure slices 与 safety limitations？

### LLM-discovered 0-days

- **Candidate / Week / Score:** LLM-discovered 0-days / 2026-W06 / 27/30；
  `Source Family ID: anthropic-opus-4.6-zero-day-workflow`。
- **Source / Date / Full-read Coverage:** Anthropic Research article，2026-02-05；已读 setup、discovery
  workflow、Ghostscript/OpenSC/CGIF examples、human validation/patching 与 safeguards。该来源是厂商官方
  research report，不是 peer-reviewed paper，也未提供完整 artifact、denominator 或可复现 benchmark。
- **Problem / Previous Design / Changed Constraint:** fuzzing 与定制 harness 对可执行输入空间覆盖有效，且
  结果易复现；但 patch-history gap、跨函数语义和特定 branch sequence 可能很难由随机输入触发。变化是
  code-reasoning model 可以把 repository history、source semantics 与现有分析工具组合成候选生成器。
- **Mechanism / State / Flow:** 模型进入含最新开源项目、coreutils、debugger 与 fuzzer 的 VM，阅读代码、
  提出 exploit hypothesis、运行工具并产生候选；模型还参与 critique、dedup 与 reprioritization。人类拥有
  vulnerability validation、severity、responsible disclosure、patch review 与 maintainer coordination。
- **Evaluation Contract:** 官方报告称已发现并人工验证 500+ high-severity vulnerabilities，并给出三个
  mechanism examples；未披露扫描项目总数、compute/tool-call budget、candidate denominator、false-positive
  rate、severity adjudication、time-to-fix 或未成功项目分布。因此不能把 500+ 外推为通用 autonomous
  exploit-development rate。
- **Evidence / Trade-offs / Failure Modes:** 证据支持“semantic proposal + executable reproduction + human
  disclosure”这一受限 workflow；不证明模型替代 fuzzers 或安全研究员。新成本包括大量候选验证、重复/
  已知漏洞归并、敏感 exploit 保管、maintainer burden 与 dual-use abuse；传统 fuzzing 在高吞吐、coverage
  feedback 与回归验证上仍成立。activation probes 是 policy-bound sensor，不是恶意意图真值。
- **Evolution / ROADMAP / Chapter Read:** `Layering / Dependency` from fuzzing/static analysis to model-assisted
  semantic search，再到 human-reviewed remediation；Ch68 主 owner，Ch62/74/77 handoff。已读 Ch62、Ch68、
  Ch74、Ch77；与现有“模型 proposal、runtime authority”一致，但增加 responsible-disclosure lifecycle 证据。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何发布匿名 denominator、false-positive、repair acceptance 与 time-to-fix 数据，同时
  不泄露尚未修复的 exploit details？

### GPT-5-driven closed-loop CFPS optimization

- **Candidate / Week / Score:** GPT-5 lowers cell-free protein synthesis cost / 2026-W06 / 28/30；
  `Source Family ID: openai-gpt5-cfps-closed-loop-lab`。
- **Source / Date / Full-read Coverage:** OpenAI Research article 与 25-page technical paper，2026-02-05。
  已读 problem、six-step loop、typed experiment schema、cloud-lab protocol、tool-access transition、dataset、
  cost/titer analysis、failure cases、discussion、methods 与 human contribution。没有独立代码/experiment
  artifact 可供本轮复跑。
- **Problem / Previous Design / Changed Constraint:** 人工 DOE 容易解释且适合小空间，但 CFPS 组合空间大、
  单次实验噪声高。变化不是“模型知道生物学真值”，而是自动化实验室提供大规模、低延迟的物理反馈，
  使 proposal→execution→measurement→next proposal 能迭代。
- **Mechanism / State / Flow:** GPT-5 每轮提出 384-well plate compositions；Pydantic schema 在执行前约束
  volume、concentration 与 logistics；人类编写 Catalyst protocols、准备/装卸试剂并改进 stock quality；
  cloud lab 执行，结果以 JSON 回流。第三步开始模型获得 computer、web、analysis packages、SOTA paper
  与更丰富 metadata。Workflow 而非模型拥有 experiment identity、physical validation 与执行权限。
- **Evaluation Contract:** 六个月内 >580 plates、>36,000 compositions、约 150k datapoints；只覆盖 sfGFP、
  一个 E. coli lysate CFPS system。作者报告相对既有 baseline $422/g vs $698/g（40% cost reduction）与
  27% titer increase；reagent-only 算法为 57%。反应 geometry、oxygenation、mixing 与成本口径影响结果；
  480 个设计 plate 中报告两次设计/执行错误。硬件 model-inference contract、token/tool budget 未披露。
- **Evidence / Trade-offs / Failure Modes:** 支持 typed contract + high-throughput physical feedback 能约束
  科研 Agent；不证明 GPT-5 单独造成改进，也未做 ablation 分离 model、tools、论文输入、人类 protocol/
  stock corrections 与 lab throughput。成本数字不是 commercial production price，且不能跨 protein、lysate、
  scale 外推。新增风险包括 unit conversion、schema blind spot、measurement drift、biosafety 与 optimizer
  对自动化平台局部条件过拟合；人工 DOE 在低吞吐或不可逆实验中仍合理。
- **Evolution / ROADMAP / Chapter Read:** `Direct Refinement` of proposal-only science Agent into typed,
  executable, human-governed closed loop；Ch77 主 owner，Ch62/74/80 handoff。已读 Ch62、Ch74、Ch77、Ch80；
  Ch77 已有物理实验边界，本来源更强地证明 schema validation 与 human protocol ownership。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** held-out lab、另一 protein/lysate、不同 geometry 下能否复现？如何把 unit、inventory、
  biosafety 与 experiment lineage 变成统一 release gate？

### TensorRT 10.15

- **Candidate / Week / Score:** TensorRT 10.15 / 2026-W06 / 19/30；
  `Source Family ID: nvidia-tensorrt-10.15-release`。
- **Source / Date / Full-read Coverage:** NVIDIA TensorRT GitHub v10.15 release，2026-02-03，commit
  `9973b2f`；已核对 release notes link、sample/plugin/parser/demo changes 与 deprecations。链接的独立
  10.15.1 docs URL 当前返回 404，故未把不可达页面内容纳入结论。
- **Mechanism / Facts:** release 新增 safety workflow samples、`IStreamWriter` streaming serialization、
  strongly typed AutoCast sample、cuDLA sample；parser 增加 RotaryEmbedding、RMSNormalization、
  TensorScatter 与更专门的 quantization ops，并新增 DLA node capability reporting / plugin override flags。
  同时弃用一个 BERT QKV plugin、移除旧 Stable Diffusion demo。这些是 support-matrix 与 migration facts，
  不是新的 GPU execution principle。
- **Evidence Boundary / Trade-offs:** release 没有给出 model/hardware/precision/length/batch/concurrency/SLO
  benchmark，不能从 parser/operator support 推导 latency、numerical equivalence 或 production readiness。
  Strong Typing、plugin override 与 safety samples提升显式 contract，但扩大 compatibility test、migration
  和 artifact-version matrix；旧 engine/plugin 若尚未迁移，稳定版本仍可能更合理。
- **Evolution / ROADMAP / Chapter Read:** `Version Fact` in build/runtime artifact evolution；Ch45 主 owner，
  Ch44/46 为相邻边界。已读 Ch44～46；Ch45 已覆盖 execution plan、precision 与 build/runtime separation，
  本 release 没有补出长期机制缺口。
- **Integration Decision:** `Weekly Only — Version/Product Fact / No Books Change`。
- **Open Questions:** 10.15.1 docs 是否迁址？具体 operator/plugin combination 的 numerical and compatibility
  tests 需绑定哪个 GPU/CUDA/driver matrix？

### vLLM NixlConnector P/D Roadmap

- **Candidate / Week / Score:** vLLM NixlConnector P/D Roadmap / 2026-W06 / 25/30；
  `Source Family ID: vllm-nixlconnector-pd-roadmap`。
- **Source / Date / Full-read Coverage:** GitHub issue #33702，opened 2026-02-03；已读 current roadmap、
  core NIXL PR #17751、async/preemption bug references、transport/TP/CPU/heterogeneous configuration、
  compatibility/failure/telemetry 与 work-in-progress sections。Issue body 在 2 月后持续编辑；当前清单不能
  倒灌成 opening-week implementation state。PR #17751 于 2025-05-12 合并，是基础实现，不是 W06 新代码。
- **Problem / Previous Design / Changed Constraint:** co-located P/D 没有跨实例 KV ownership transfer，简单且
  failure surface 小；分离池改善 resource specialization 后，KV bytes、request identity、compatibility、
  abort/preemption 与 remote failure 变成显式协议。
- **Mechanism / State / Flow:** 基础 connector 支持 runtime NIXL handshake、async send/recv、xPyD、homogeneous
  TP 与 P→D request flow；roadmap 将 transport backend、heterogeneous TP/block/layout、CPU staging、compatibility
  hash、transfer metrics 与 failure policy纳入同一 lifecycle。关键 state 不只是 bytes，而是 source lease、
  destination readiness、request/remote identity、block validity 与 ownership commit。
- **Implementation / Evidence Boundary:** #17751 的 merge summary证明基础 path 存在，也明确列出 D→P、heterogeneous
  TP、DP attention、failure robustness 等 follow-ups。当前 #33702 页面包含后来新增的 bidirectional transfer、
  hybrid-state、spec decode 等事项；未逐 PR 还原日期者只能作为后续 evolution，不可写成 2026-02-03 已支持。
  Roadmap 没有统一 hardware/model/precision/length/concurrency/SLO benchmark。
- **Trade-offs / Failure Modes:** async transfer隐藏 latency，却新增 abort/double-free、preempted-request resume、
  stale/expired blocks 与 remote disconnect；heterogeneous layout/TP 扩大 placement space，也扩大 compatibility
  hash、permutation、recompute 与 CI matrix。co-location 在小规模、链路受限或 failure isolation 更重要时仍成立。
- **Evolution / ROADMAP / Chapter Read:** `Direct Refinement` from KV byte transfer to typed, observable ownership
  protocol；Ch51 主 owner，Ch50/52 handoff，Ch46 implementation context。已读 Ch46、Ch50～52；现有 Ch51
  已有 handoff state machine，roadmap可用于验证 lease/compatibility/failure policy 的实现压力。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本批不修改 Books。
- **Open Questions:** 如何保存 issue/PR 的 event-time snapshot？在 destination commit、source failure、cancel 与
  retry 竞态下，block lease 和 recompute policy 的线性化点是什么？

### Multi-Task GRPO

- **Candidate / Week / Score:** Multi-Task GRPO / 2026-W06 / 29/30；
  `Source Family ID: mt-grpo-task-weight-gradient-realization`。
- **Source / Date / Full-read Coverage:** arXiv:2602.05547，v1 2026-02-05，2026-07/08 revision 后标注
  ICML 2026 accepted。已读 problem formulation、worst-task objective、improvement-aware update、
  Ratio-Preserving Sampler、3/9-task experiments、7B extension、ablation、sequential baseline、wall-clock
  overhead、limitations、proof 与 reproducibility appendix。后续 revision 用于核验机制，不改写 W06 event date。
- **Problem / Previous Design / Changed Constraint:** uniform multi-task averaging简单、吞吐稳定，且在 task
  difficulty/acceptance相近时合理；但平均分允许强任务掩盖弱任务。GRPO 又会过滤 group reward 全相同的
  zero-gradient prompts，不同 task 的过滤率不同，使声明的 task weight 与实际 gradient contribution 分离。
- **Mechanism / State / Flow:** policy parameters 与 task sampling distribution共同演化。Improvement-aware
  update 结合当前 task reward 与近期 improvement，避免只追最差 task 导致 weight collapse；RP sampler 先从
  target weights采样 post-filtered counts，再按估计的 zero-gradient rate 进行 acceptance-aware oversampling，
  直到各 task 的有效样本接近目标比例或耗尽 regeneration budget。控制对象是有效梯度 mixture，不是原始 prompt
  mixture。
- **Implementation / Evaluation Contract:** 主实验 Qwen2.5-3B、2×H200 141GB、verl、720 steps；3-task
  Countdown/Zebra/ARC 使用 72 rollouts、global batch 32，9-task 使用 8 rollouts、batch 256；prompt 1,024、
  response 4,096、temperature 1.0、verifiable rewards。另有 Qwen2.5-7B 与 OLMo-3 7B extension。作者报告
  Experiment 1 相对 DAPO 每 step 约 +10.2%（727s vs 659s），但在 80h budget 下更早达到 worst-task thresholds；
  这些数字不能跨模型、reward sparsity 或集群外推。
- **Evidence / Trade-offs / Failure Modes:** ablation支持 task reweighting 与 ratio preservation各自必要；
  sequential baseline显示 order-sensitive forgetting。证据只覆盖训练 mixture 内、可验证 reward task；不证明
  unseen-task robustness，也不适用于 subjective/non-verifiable reward。高过滤 task 会增加 rollout/resampling、
  straggler 与方差，worst-task权重也可能牺牲平均能力；若 task 同质或固定 mixture 已满足 product utility，uniform
  sampling仍更便宜。
- **Evolution / ROADMAP / Chapter Read:** `Direct Refinement` from uniform task sampling to adaptive weights，再到
  post-filtered gradient-mixture enforcement；Ch29 主 owner，Ch24/28/30 handoff。已读 Ch28～30，并复核 Ch24；
  它补出“dataset mixture 不等于 optimizer实际看见的 gradient mixture”的机制缺口。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本轮停在 Weekly Gate。
- **Open Questions:** 当 verifier false-negative/false-positive rate 各 task 不同时，是否会把 sampler 变成对
  verifier blind spot 的自适应放大器？

### CauGym — Can Post-Training Transform LLMs into Causal Reasoners?

- **Candidate / Week / Score:** CauGym / 2026-W06 / 25/30；
  `Source Family ID: caugym-causal-reasoning-post-training`。
- **Source / Date / Full-read Coverage:** arXiv:2602.06337，v1 2026-02-06，v2 2026-08-05。已读 synthetic
  SCM/DAG generation、seven tasks、SFT/DPO/KTO/PPO/GRPO adaptation、nine evaluations、base/scale ablation、
  generalization/internalization/robustness sets、failure taxonomy、ethical considerations、limitations 与 dataset
  appendix。当前 HTML 是 v2；revision 只用于复核，不把 8 月新增文字倒灌成 W06 新事件。
- **Problem / Previous Design / Changed Constraint:** causal library 能执行已正确指定的 estimand/assumption，
  但非专家仍需识别 task、backdoor set、公式与缺失条件。通用 LLM 的语言接口方便，却在精确 causal estimation
  上不可靠；问题是 narrow, formally checkable causal tasks能否通过 post-training internalize。
- **Mechanism / State / Flow:** 随机 10-node DAG 与 single-layer-perceptron SCM 生成概率，节点使用 real/random/fake
  semantics；DoWhy求 adjustment/mediator sets，模板生成 seven intervention/counterfactual tasks。SFT/离线偏好法
  使用 teacher-generated traces/pairs，PPO/GRPO只使用 question、final-answer 与 format rewards。五个测试变体分别
  改写措辞、隐藏 task cue、强制 deconfounding、加入冗余条件或移除必要条件。
- **Implementation / Evaluation Contract:** 主模型 DeepSeek-R1-Distill-Qwen-14B；各法约 3,500 questions/
  pairs，GRPO/PPO 三 epochs，exact-match，五次 runs；还测试 Mistral-7B、R1-Distill-Llama-8B 与 Qwen 7B/32B。
  作者报告主 synthetic/derived benchmark 上 GRPO 93.5%，但 GPU、precision、rollout count、wall-clock 与完整
  compute budget 未披露；与 o3/大模型的数字不能视为同 inference budget 的 capability ranking。
- **Evidence / Trade-offs / Failure Modes:** online RL 在作者生成分布、verifiable answers与多个 perturbation sets
  上明显优于 tested SFT/offline RL，且 failure analysis把错误分为 task/SCM/formula/application/numerical/unexpected。
  但 train/test 都源自相近 SCM/template family，teacher 参与正/负 trace，无法证明 real-world identification、
  hidden confounding、measurement error 或 policy decision reliability。专门化可能降低未知任务适用性；传统 causal
  analysis 在 assumptions必须由 domain expert审查时仍拥有 truth authority。论文本身明确否认 general-purpose claim。
- **Evolution / ROADMAP / Chapter Read:** `Principle Reuse` from verifiable math RL to domain-formal causal tasks；
  Ch29 主 owner，Ch62 主 evidence boundary handoff，Ch74 承接 library/tool authority。已读 Ch28～30、Ch62、Ch74；
  不能把 benchmark internalization写成 causal truth。
- **Integration Decision:** `Final Books disposition recorded in Candidate Scoring ledger`；本轮不修改 Books。
- **Open Questions:** 在 unseen graph size、continuous treatment、unknown confounding 与 real observational data 上，
  performance是否保持？怎样让模型显式拒绝不可识别 estimand，而非只输出公式？

## 2026-07-31 Full Re-Audit Addendum

- Sequential Attention 的机制论文 arXiv:2209.14881 首版为 2022 年，2026 条目属于正式发表/
  传播节点，不是新机制首次公开。它是 feature selection，不是 Transformer dynamic attention；
  旧 Addendum 中“现有 Attention 章节覆盖”的理由已纠正。
- Recommended Action 修正为 `Record publication state / no duplicate integration`。

## Repository Changes

- 2026-08-07：W06 从 2 项重新打开为 37 个新增 date-verified discovery candidates；记录 first-public
  日期、跨周排除项与 02-07/02-08/学术索引覆盖缺口。未修改 Books。
- 2026-08-07 Batch A：完成 7/37 项 primary-source 全文审查与重新评分；记录机制、实验合同、未证明边界、
  旧方案成立条件及候选章节 owner。其余 30 项仍 pending，未修改 Books。
- 2026-08-07 Batch B：完成 6 项 Agent/benchmark/safety primary-source 审查；累计 13/37，余 24 项 pending。
  未修改 Books。
- 2026-08-07 Batch C：完成 6 项 reasoning/search/world-model primary-source 审查；累计 19/37，余 18 项 pending。
  未修改 Books。
- 2026-08-07 Batch D：完成 6 项 orchestration/memory/retrieval/dLLM primary-source 审查；累计 25/37，
  余 12 项 pending。未修改 Books。
- 2026-08-07 Batch E：完成 7 篇论文的全文审查；累计 32/37，余 5 个官方 Research/Release/RFC source
  families pending。已逐项核验算法、状态/数据流、实验条件、limitations 与 owner chapter；未修改 Books。
- 2026-08-07 Batch F：完成 Anthropic 0-day、OpenAI CFPS closed-loop lab、TensorRT 10.15 与 vLLM
  NixlConnector roadmap 4 个 source families 的 primary-source review；累计 36/37。Claude Opus 4.6
  announcement 已核验，但 system card 因当前读取通道的文档长度限制保留为 `Unverified / Blocked`。
  对 mutable vLLM issue 明确冻结 event-time，未把后续编辑倒灌为 W06 已实现功能。未修改 Books。
- 2026-08-07 Batch G：第二轮交叉检索证明首轮召回不完整，恢复 Multi-Task GRPO 与 CauGym 两篇 W06
  primary papers，并完成 method、实验合同、ablation、limitations 与 revision-boundary 审查。候选 census
  增至 39，累计 38/39 complete；Claude system card 仍阻塞，其他索引覆盖仍未闭合。未修改 Books。
- 2026-08-07 Discovery Cross-Check Review：逐项记录 arXiv、HF、Semantic Scholar、Google Scholar、
  OpenAlex、DBLP、GitHub release 与官方 Research surfaces 的可访问结果和限制。W06 当时的 review checkpoint
  为 `Blocked, not complete`；2026-08-13 按 blocked-skip 规则完成其余 source-family Books Review，未改写
  Claude 的 Unverified 状态。
- 2026-08-13：完成 41/41 scored rows 的最终 disposition：21 Integrate/Refine、15 No Change、4 Weekly Only、
  1 Unverified/Blocked；对已验证 family 完成 owner/相邻章节反向检查，实际 refine 15 个 Stable Node owners：
  Ch21、Ch22、Ch24、Ch25、Ch28、Ch29、Ch33、Ch43、Ch45、Ch48、Ch72、Ch76、Ch77、Ch81、Ch82。
  同步纠正 Anthropic 0-day 与 OpenAI CFPS 两处 primary-source URL。Archive Gate 仍 Open。

## Open Questions

1. 动态 attention depth 如何与 batching、kernel regularity 和 KV lifecycle 协同？
2. Claude Opus 4.6 system card 能否通过另一可审计读取通道完整取得，而不是依赖 announcement 或搜索摘要？
3. 02-07/02-08 与 arXiv category / OpenAlex / Scholar / DBLP 交叉检索会否恢复更多漏项？
4. 对持续编辑的 GitHub roadmap，历史 Weekly 应如何保存 event-time snapshot 与 later-revision lineage？

## Sources

- Google Research February 2026 archive: https://research.google/blog/2026/02/
- ByteDance Seed Research, Protenix-v1 entry dated 2026-02-06:
  https://seed.bytedance.com/en/research
- Hugging Face Daily Papers discovery pages（仅用于发现；访问 2026-08-07）：
  https://huggingface.co/papers/date/2026-02-03
  https://huggingface.co/papers/date/2026-02-04
  https://huggingface.co/papers/date/2026-02-05
  https://huggingface.co/papers/date/2026-02-06
- Recovered primary-source entry pattern（每项以对应 arXiv ID 为准）：
  https://arxiv.org/abs/2602.02276
  https://arxiv.org/abs/2602.04705
  https://arxiv.org/abs/2602.02472
  https://arxiv.org/abs/2602.03152
  https://arxiv.org/abs/2602.03216
  https://arxiv.org/abs/2602.03295
  https://arxiv.org/abs/2602.06036
  https://arxiv.org/abs/2602.02361
  https://arxiv.org/abs/2602.01566
  https://arxiv.org/abs/2602.01590
  https://arxiv.org/abs/2602.02905
  https://arxiv.org/abs/2602.02419
  https://arxiv.org/abs/2602.05386
  https://arxiv.org/abs/2602.01801
  https://arxiv.org/abs/2602.02486
  https://arxiv.org/abs/2602.02477
  https://arxiv.org/abs/2602.02660
  https://arxiv.org/abs/2602.02636
  https://arxiv.org/abs/2602.04634
  https://arxiv.org/abs/2602.03786
  https://arxiv.org/abs/2602.03798
  https://arxiv.org/abs/2602.02474
  https://arxiv.org/abs/2602.02160
  https://arxiv.org/abs/2602.05975
  https://arxiv.org/abs/2602.02159
  https://arxiv.org/abs/2602.04541
  https://arxiv.org/abs/2602.04804
  https://arxiv.org/abs/2602.03560
  https://arxiv.org/abs/2602.04735
  https://arxiv.org/abs/2602.05261
  https://arxiv.org/abs/2602.02393
  https://arxiv.org/abs/2602.02016
  https://arxiv.org/abs/2602.05547
  https://arxiv.org/abs/2602.06337
- Anthropic, Claude Opus 4.6 announcement（2026-02-05；system card full read blocked）：
  https://www.anthropic.com/news/claude-opus-4-6
  https://www.anthropic.com/claude-opus-4-6-system-card
  https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf
- Anthropic Research, Evaluating and mitigating the growing risk of LLM-discovered 0-days
  （2026-02-05；2026-02-06 author-list edit）：
  https://www.anthropic.com/research/zero-days
- OpenAI Research, GPT-5 lowers the cost of cell-free protein synthesis（2026-02-05）：
  https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
  https://cdn.openai.com/pdf/5a12a3bc-96b7-4e07-9386-db6ee5bb2ed9/using-a-gpt-5-driven-autonomous-lab-to-optimize-the-cost-and-titer-of-cell-free-protein-synthesis.pdf
- NVIDIA TensorRT v10.15 release（2026-02-03）：
  https://github.com/NVIDIA/TensorRT/releases/tag/v10.15
- vLLM NixlConnector P/D Disaggregation Roadmap #33702（opened 2026-02-03）：
  https://github.com/vllm-project/vllm/issues/33702
  https://github.com/vllm-project/vllm/pull/17751

## 2026-08-13 Source-Family Books Integration

OmniSIFT 的原 structural owner gap 已由 ADR-008 关闭。Owner 为 `MULTIMODAL-REPRESENTATION`，Current chapter Ch23，Legacy N/A；最终 disposition 为 `Refine — modality-role-aware compression / Experimental`。书稿只吸收“compression direction 应由 information role 与 truth authority 决定”的长期机制，并保留 audio-first、symmetric 与 full-token 分支。作者 latency/memory 数字因 hardware、precision、concurrency 与 SLO 未披露，没有进入通用结论。修改文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`。Open question 仍是冲突模态下的动态方向选择和 abstention 校准；Archive Completion Gate 仍 Open。
