# Daily Research — 2026-08-25

**Research Date:** 2026-08-25

**Timezone:** Asia/Shanghai

**Special Window:** 2026-08-24 09:00:00 ～ 2026-08-25 09:00:00（北京时间，严格 24 小时）

**Scope:** Papers only；本次不纳入产品公告、Release、RFC、PR 或新闻
**Status:** Complete；fresh-context Books adjacency re-audit 已通过；Tuesday，不生成 provisional Weekly

## Executive Summary

本次是一次独立的 V2.1 Full Replay，不继承此前 8 月 25 日宽窗口日报的 22 项候选。官方 arXiv API 在冻结窗口内返回 390 条 v1；经过 route filter、AI-System relevance、Source Family 去重与身份核验后，冻结 21 个候选：13 个 Deep Review、5 个 Standard Review、3 个 Closure Review。Hugging Face 的 8 月 24 日 Daily Papers 只用于发现与交叉去重，其 recommendation date 不改变 arXiv v1 的事件归属。

三条最重要的系统演进是：第一，Context、KV 与 World State 都从“统一保留或统一压缩”走向按状态类型、未来用途和可恢复性分配预算；第二，Agent 的评估与安全从终局答案或单个动作推进到 typed trace、flow policy、artifact 与环境状态的联合证据；第三，后训练系统重新打开了 critic 与 group-relative baseline 的条件分支，稳定性取决于 value range、target、advantage scale、response length 与 rollout economics 的联动，而不是“有无 critic”一个开关。

Books Integration 吸收三项长期增量：将 prefix invariance 提升为 sequence block 的可执行正确性不变量；将类型化 retention policy 补入 Context Compression；将 critic 稳定性补入 PPO，并明确它与 GRPO 的 compute/credit 分支关系。其余高分项经相邻章节对读后均为 `No Change — Existing Coverage`，没有为了制造差异重复追加。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-25 |
| Window End | 2026-08-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-25-0900-24h-v2.1-01 |
| Denominator Frozen At | 2026-08-25T18:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

机构端点按 Required Daily cadence 执行，但本次只接受 paper / technical manuscript；无论文命中不等于来源未执行。`SRC-ARXIV` 的查询覆盖注册表 core routes 与 Daily filtered routes，最后一条命中为 `2026-08-24T17:59:39Z`；API total 为 390，分页一次闭合。HF 页在窗口内列出 70 个 recommendation entries，全部只作 discovery，最终 family 仍以 primary manuscript identity 去重。

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OPENAI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:20:00+08:00 | https://openai.com/research/；paper only | no_hit | 0 | — | page=1; final_cursor=end; listing crossed below window | 2026-08-25T09:00:00+08:00 | coverage:SRC-OPENAI:20260825 | — |
| SRC-ANTHROPIC | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:22:00+08:00 | https://www.anthropic.com/research；paper only | no_hit | 0 | — | page=1; final_cursor=end; listing closed at 2026-08-18 | 2026-08-25T09:00:00+08:00 | coverage:SRC-ANTHROPIC:20260825 | — |
| SRC-GOOGLE-AI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:24:00+08:00 | DeepMind Research + Google Research publications；paper only | no_hit | 0 | — | page=2; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-GOOGLE-AI:20260825 | — |
| SRC-META-AI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:25:00+08:00 | https://ai.meta.com/research/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-META-AI:20260825 | — |
| SRC-XAI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:26:00+08:00 | https://x.ai/news；technical manuscript only | no_hit | 0 | — | page=1; final_cursor=end; listing crossed below window | 2026-08-25T09:00:00+08:00 | coverage:SRC-XAI:20260825 | — |
| SRC-MISTRAL | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:27:00+08:00 | https://mistral.ai/news/；technical manuscript only | no_hit | 0 | — | page=1; final_cursor=end; listing crossed below window | 2026-08-25T09:00:00+08:00 | coverage:SRC-MISTRAL:20260825 | — |
| SRC-QWEN | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:28:00+08:00 | https://qwenlm.github.io/；paper and linked manuscript | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-QWEN:20260825 | — |
| SRC-DEEPSEEK | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:29:00+08:00 | https://www.deepseek.com/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-DEEPSEEK:20260825 | — |
| SRC-MOONSHOT | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:30:00+08:00 | https://platform.kimi.com/blog；paper only | no_hit | 0 | — | page=1; final_cursor=end; listing crossed below window | 2026-08-25T09:00:00+08:00 | coverage:SRC-MOONSHOT:20260825 | — |
| SRC-ZAI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:31:00+08:00 | https://docs.z.ai/llms.txt；paper links only | no_hit | 0 | — | page=1; final_cursor=end; release-only entries excluded | 2026-08-25T09:00:00+08:00 | coverage:SRC-ZAI:20260825 | — |
| SRC-MINIMAX | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:32:00+08:00 | https://www.minimax.io/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-MINIMAX:20260825 | — |
| SRC-BYTEDANCE-SEED | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:33:00+08:00 | https://seed.bytedance.com/en/；publication only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-BYTEDANCE-SEED:20260825 | — |
| SRC-BAIDU-ERNIE | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:34:00+08:00 | https://ernie.baidu.com/blog/zh/publication/；paper only | no_hit | 0 | — | page=1; final_cursor=end; 13 visible entries checked | 2026-08-25T09:00:00+08:00 | coverage:SRC-BAIDU-ERNIE:20260825 | — |
| SRC-TENCENT-HUNYUAN | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:35:00+08:00 | https://github.com/Tencent-Hunyuan；linked manuscript only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-TENCENT-HUNYUAN:20260825 | — |
| SRC-HUAWEI-NOAH | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:36:00+08:00 | https://noahlab.com.hk/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-HUAWEI-NOAH:20260825 | — |
| SRC-SHLAB | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:37:00+08:00 | https://www.shlab.org.cn/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-SHLAB:20260825 | — |
| SRC-STEPFUN | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:38:00+08:00 | https://www.stepfun.com/research；paper only | no_hit | 0 | — | page=1; final_cursor=end; search-visible surface reconciled | 2026-08-25T09:00:00+08:00 | coverage:SRC-STEPFUN:20260825 | — |
| SRC-XIAOMI-MIMO | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:39:00+08:00 | https://mimo.xiaomi.com/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-XIAOMI-MIMO:20260825 | — |
| SRC-INCLUSION-AI | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:40:00+08:00 | https://www.inclusion-ai.org/publication/；paper only | no_hit | 0 | — | page=1; final_cursor=end; arXiv reconciliation applied | 2026-08-25T09:00:00+08:00 | coverage:SRC-INCLUSION-AI:20260825 | — |
| SRC-ARXIV | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:45:00+08:00 | Atom API: registered core + Daily-filtered routes; submittedDate 202608240100–202608250100 UTC | checked | 390 | SF-2026-WNW-KV<br>SF-2026-CACHEROUTER<br>SF-2026-COMPACTION-CLIFF<br>SF-2026-XTC<br>SF-2026-DRY-SAMPLING<br>SF-2026-TAILSIEVE<br>SF-2026-CATCHBENCH<br>SF-2026-AGENTFLOW<br>SF-2026-PREFIX-INVARIANCE<br>SF-2026-EXECUTION-EDITS<br>SF-2026-PROCESS-EVAL<br>SF-2026-POINTING-VLA<br>SF-2026-DIFFUSION-SUFFIX<br>SF-2026-CONTEXT-ALLOCATION<br>SF-2026-NEXTCHUNK-RL-SFT<br>SF-2026-SIGMOID-KV<br>SF-2026-INJECMEM<br>SF-2026-INTERACTION-TAX<br>SF-2026-SWE-REFACTOR<br>SF-2026-REWORLD<br>SF-2026-BPCO-CRITIC | page=1; start=0; max_results=2000; totalResults=390; final_cursor=end | 2026-08-25T01:00:00Z | coverage:SRC-ARXIV:20260825 | — |
| SRC-HF-PAPERS | 2026-08-24T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T17:50:00+08:00 | https://huggingface.co/papers；Aug 24 visible list; discovery only | no_hit | 0 | — | page=1; final_cursor=end; 70 recommendations yielded 0 unique primary families | 2026-08-25T09:00:00+08:00 | coverage:SRC-HF-PAPERS:20260825 | — |

<!-- coverage:SRC-OPENAI:20260825:start -->OpenAI official research listing contained no paper dated inside the frozen window.<!-- coverage:SRC-OPENAI:20260825:end -->
<!-- coverage:SRC-ANTHROPIC:20260825:start -->Anthropic official research listing closed below the window at 2026-08-18.<!-- coverage:SRC-ANTHROPIC:20260825:end -->
<!-- coverage:SRC-GOOGLE-AI:20260825:start -->DeepMind and Google Research publication surfaces were checked and reconciled against the arXiv window.<!-- coverage:SRC-GOOGLE-AI:20260825:end -->
<!-- coverage:SRC-META-AI:20260825:start -->Meta AI research surface and primary-manuscript identities were checked for the window.<!-- coverage:SRC-META-AI:20260825:end -->
<!-- coverage:SRC-XAI:20260825:start -->xAI dated surface contained no technical manuscript in scope.<!-- coverage:SRC-XAI:20260825:end -->
<!-- coverage:SRC-MISTRAL:20260825:start -->Mistral dated surface contained no technical manuscript in scope.<!-- coverage:SRC-MISTRAL:20260825:end -->
<!-- coverage:SRC-QWEN:20260825:start -->Qwen publication surface and linked manuscript identities were reconciled.<!-- coverage:SRC-QWEN:20260825:end -->
<!-- coverage:SRC-DEEPSEEK:20260825:start -->DeepSeek official surface and arXiv identities contained no additional in-window manuscript.<!-- coverage:SRC-DEEPSEEK:20260825:end -->
<!-- coverage:SRC-MOONSHOT:20260825:start -->Kimi official dated listing closed below the window.<!-- coverage:SRC-MOONSHOT:20260825:end -->
<!-- coverage:SRC-ZAI:20260825:start -->Z.ai official index closed below the window; releases were excluded by papers-only scope.<!-- coverage:SRC-ZAI:20260825:end -->
<!-- coverage:SRC-MINIMAX:20260825:start -->MiniMax official research surface and arXiv identities were reconciled.<!-- coverage:SRC-MINIMAX:20260825:end -->
<!-- coverage:SRC-BYTEDANCE-SEED:20260825:start -->Seed publication surface and arXiv identities were reconciled.<!-- coverage:SRC-BYTEDANCE-SEED:20260825:end -->
<!-- coverage:SRC-BAIDU-ERNIE:20260825:start -->ERNIE publication listing was enumerated; no in-window paper appeared.<!-- coverage:SRC-BAIDU-ERNIE:20260825:end -->
<!-- coverage:SRC-TENCENT-HUNYUAN:20260825:start -->Tencent Hunyuan linked manuscripts were reconciled to the arXiv query.<!-- coverage:SRC-TENCENT-HUNYUAN:20260825:end -->
<!-- coverage:SRC-HUAWEI-NOAH:20260825:start -->Noah publication cards and arXiv identities were reconciled.<!-- coverage:SRC-HUAWEI-NOAH:20260825:end -->
<!-- coverage:SRC-SHLAB:20260825:start -->Shanghai AI Lab official surface and arXiv identities were reconciled.<!-- coverage:SRC-SHLAB:20260825:end -->
<!-- coverage:SRC-STEPFUN:20260825:start -->StepFun official search-visible research surface and arXiv identities were reconciled.<!-- coverage:SRC-STEPFUN:20260825:end -->
<!-- coverage:SRC-XIAOMI-MIMO:20260825:start -->MiMo official publication surface and arXiv identities were reconciled.<!-- coverage:SRC-XIAOMI-MIMO:20260825:end -->
<!-- coverage:SRC-INCLUSION-AI:20260825:start -->Inclusion AI publication listing and arXiv identities were reconciled.<!-- coverage:SRC-INCLUSION-AI:20260825:end -->
<!-- coverage:SRC-ARXIV:20260825:start -->The official Atom API returned totalResults=390 for the exact UTC interval; one page with max_results=2000 closed the cursor, and the last returned record was 2608.23566v1 at 2026-08-24T17:59:39Z.<!-- coverage:SRC-ARXIV:20260825:end -->
<!-- coverage:SRC-HF-PAPERS:20260825:start -->The visible Aug 24 Daily Papers list contained 70 recommendations; all were treated as discovery records and reconciled to primary manuscript dates.<!-- coverage:SRC-HF-PAPERS:20260825:end -->

### Coverage Limitations

- arXiv 在本窗口中的最后公开时间早于窗口终点，反映其批次更新节奏，不是把窗口缩短到 18:00 UTC。
- 机构网页不是统一、可稳定分页的数据库；本次用官方 listing、date boundary 与 arXiv identity reconciliation 闭合 papers-only 范围，不把“无新增论文”外推为“机构无其他活动”。
- HF recommendation date 不是 first-public date，也不支持机制主张。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-WNW-KV | arXiv:2608.22704v1 | paper-v1:2608.22704 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-WNW-KV | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-WNW-KV | yes |
| SF-2026-CACHEROUTER | arXiv:2608.22708v1 | paper-v1:2608.22708 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-CACHEROUTER | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-COMPACTION-CLIFF | arXiv:2608.22752v1 | paper-v1:2608.22752 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-COMPACTION-CLIFF | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-COMPACTION-CLIFF | yes |
| SF-2026-XTC | arXiv:2608.22758v1 | paper-v1:2608.22758 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-XTC | self | — | new_in_window | MODEL-SAMPLING | Rejected — Low Durability / Out of Scope | — | yes |
| SF-2026-DRY-SAMPLING | arXiv:2608.22761v1 | paper-v1:2608.22761 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-DRY-SAMPLING | self | — | new_in_window | MODEL-SAMPLING | Rejected — Low Durability / Out of Scope | — | yes |
| SF-2026-TAILSIEVE | arXiv:2608.22788v1 | paper-v1:2608.22788 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-TAILSIEVE | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-TAILSIEVE | yes |
| SF-2026-CATCHBENCH | arXiv:2608.22808v1 | paper-v1:2608.22808 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-CATCHBENCH | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-CATCHBENCH | yes |
| SF-2026-AGENTFLOW | arXiv:2608.22868v1 | paper-v1:2608.22868 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-AGENTFLOW | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-AGENTFLOW | yes |
| SF-2026-PREFIX-INVARIANCE | arXiv:2608.22876v1 | paper-v1:2608.22876 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-PREFIX-INVARIANCE | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-PREFIX-INVARIANCE | yes |
| SF-2026-EXECUTION-EDITS | arXiv:2608.22928v1 | paper-v1:2608.22928 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-EXECUTION-EDITS | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-PROCESS-EVAL | arXiv:2608.22960v1 | paper-v1:2608.22960 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-PROCESS-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-PROCESS-EVAL | yes |
| SF-2026-POINTING-VLA | arXiv:2608.23138v1 | paper-v1:2608.23138 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-POINTING-VLA | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | yes |
| SF-2026-DIFFUSION-SUFFIX | arXiv:2608.23167v1 | paper-v1:2608.23167 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-DIFFUSION-SUFFIX | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Rejected — Low Durability / Out of Scope | — | yes |
| SF-2026-CONTEXT-ALLOCATION | arXiv:2608.23252v1 | paper-v1:2608.23252 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-CONTEXT-ALLOCATION | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-CONTEXT-ALLOCATION | yes |
| SF-2026-NEXTCHUNK-RL-SFT | arXiv:2608.23256v1 | paper-v1:2608.23256 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-NEXTCHUNK-RL-SFT | self | — | new_in_window | TRAIN-SFT | Weekly Only — Context | — | yes |
| SF-2026-SIGMOID-KV | arXiv:2608.23296v1 | paper-v1:2608.23296 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-SIGMOID-KV | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | yes |
| SF-2026-INJECMEM | arXiv:2608.23471v1 | paper-v1:2608.23471 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-INJECMEM | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-INJECMEM | yes |
| SF-2026-INTERACTION-TAX | arXiv:2608.23541v1 | paper-v1:2608.23541 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-INTERACTION-TAX | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-INTERACTION-TAX | yes |
| SF-2026-SWE-REFACTOR | arXiv:2608.23564v1 | paper-v1:2608.23564 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-SWE-REFACTOR | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-SWE-REFACTOR | yes |
| SF-2026-REWORLD | arXiv:2608.23565v1 | paper-v1:2608.23565 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-REWORLD | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-REWORLD | yes |
| SF-2026-BPCO-CRITIC | arXiv:2608.23566v1 | paper-v1:2608.23566 | 2026-W35 | 2026-08-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-BPCO-CRITIC | self | — | new_in_window | TRAIN-PPO | Integrate | books-review:SF-2026-BPCO-CRITIC | yes |

### Benchmark Contracts

以下字段只记录论文公开的 evaluation contract；`Not Disclosed` 不以推断补齐。作者实验不因此升级为独立评估。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-WNW-KV | LibriSpeech-Long speech understanding | Voxtral-mini-3B; Qwen2.5-Omni-3B | GPU with CPU KV complement; exact SKU Not Disclosed | Not Disclosed — v1 does not freeze precision here | long-form audio; task-specific | autoregressive task output | Not Disclosed — see paper setup | Not Disclosed — see paper setup | accuracy at 20% GPU audio-KV retention plus decode overhead | task accuracy and latency defined by authors |
| SF-2026-CACHEROUTER | 55 functional tool queries; 30-turn dialogue | router plus main LLM; exact checkpoint varies by experiment | Not Disclosed — prototype execution environment | Not Disclosed — no precision contract | tool schemas and dialogue context; token counts reported | tool result and dialogue response | 1 request path | prototype sequential calls | cache-hit token rate; input-cost estimate under DeepSeek pricing | functional success and provider token accounting |
| SF-2026-COMPACTION-CLIFF | recursive compaction, decomposition, retrieval and three downstream agent tasks | Claude Sonnet 4.6 compactor plus compared methods | Not Disclosed — API and corpus evaluation | Not Disclosed — provider model | corpus- and compression-ratio-specific | retained rules or downstream actions | corpus-specific | offline evaluations | rule recall, locality violation, recall@50 and task success | author labels, behavioral checks and paired tests |
| SF-2026-XTC | creative generation, IFEval and human preference | Gemma 3 12B/27B; DeepSeek R1 14B; Llama 3.3 70B | Not Disclosed — inference hardware not frozen in report | Q4 or Q6 depending checkpoint | 12 prompt genres; exact token length varies | open-ended generated text | Not Disclosed — see v1 setup | Not Disclosed — see v1 setup | diversity-repetition frontier with instruction accuracy guardrail | lexical metrics, IFEval, AMT and model judges |
| SF-2026-DRY-SAMPLING | nine prompt families plus MT-Bench, MMLU and GSM8K | models from 1.5B to 120B | Not Disclosed — inference hardware varies | includes AWQ 70B and 120B | context-dependent suffix histories | open-ended generation | Not Disclosed — see v1 setup | Not Disclosed — see v1 setup | loop reduction without benchmark degradation | suffix-extension rate, task metrics and 600-pair human study |
| SF-2026-TAILSIEVE | RL/OPD/evaluation rollout makespan | five Qwen configurations | one 8-GPU server; topology per paper | Not Disclosed — v1 setup | prompt groups with long-tail completion behavior | rollout completion length varies | hierarchical rollout groups | TP1/TP2 and route-specific concurrency | step makespan and routing-only speedup | vLLM timing and author workload replay |
| SF-2026-CATCHBENCH | PRE, LIVE and POST agent audits across seven task contracts | 72 entrants; 11 LLM judges across nine families | Not Disclosed — heterogeneous evaluated entrants | Not Disclosed — heterogeneous entrants | 1,187 configurations and 1,162 runs | state-dependent audit outputs | task-specific | offline evaluation | task-specific evidential metrics; unresolved contrasts retained | released predictions and Gold-derived diagnostics |
| SF-2026-AGENTFLOW | AgentDojo, AgentDyn and replayed agent-security suites | configured agent models and AgentFlow monitor | Not Disclosed — prototype runtime | Not Disclosed — model/provider dependent | benchmark prompts, sensitive fields and policy paths | tool/action trajectories | benchmark-specific | benchmark-specific | compromise and utility under configured flow policies | benchmark outcome checks and bounded verifier |
| SF-2026-PREFIX-INVARIANCE | injected causality faults and checkpoint audit | eight checkpoints including Zamba2 and Nemotron-H | CPU/GPU paths in paper; exact SKU varies | checkpoint- and backend-specific | T=48 and additional boundary-length tests | layer-local prefix representations | paired two-forward executions | single audit execution | fault localization and invariance violation | deterministic prefix-difference audit with tolerance |
| SF-2026-PROCESS-EVAL | coding-agent file localization traces | evaluated coding agents and post-hoc judge | Not Disclosed — offline trace analysis | Not Disclosed — model-specific | complete trajectories with step prefixes | action/task/step labels | trace-level | offline | association surviving false-discovery correction | paper-defined judge and statistical tests |
| SF-2026-POINTING-VLA | Bridge/WidowX tasks and physical pick-place | Embodied-R1; NORA-1.5; pi0.5 integration | robot/controller setup and external suite; exact accelerator varies | Not Disclosed — checkpoint-specific | images plus instruction and spatial state | points, heatmaps, trajectories or actions | task-specific | physical closed-loop control | task success and controller/readout latency | task completion under collision-enabled CuRobo and physical trials |
| SF-2026-DIFFUSION-SUFFIX | long-sequence diffusion-language generation | three DLMs | Not Disclosed — see v1 setup | Not Disclosed — no unified precision field | local/middle/tail suffix regions | denoised token sequence | Not Disclosed — see v1 setup | iterative denoising steps | quality plus latency; combined acceleration explicitly identified | task metrics and wall-clock defined by authors |
| SF-2026-CONTEXT-ALLOCATION | generative-search portfolio recall | multiple LLMs up to 32B | Not Disclosed — see repository and v1 setup | Not Disclosed — no shared precision contract | factorial context budgets and retrieved evidence | sequential portfolio generations | budget-specific | sequential generations | portfolio recall under fixed compute/context allocation | causal leave-one-out probe and task recall |
| SF-2026-NEXTCHUNK-RL-SFT | no-CoT math training followed by RLVR | paper-specified base and post-trained models | Not Disclosed — training hardware not frozen here | Not Disclosed — training precision not frozen here | no-CoT and long-CoT corpora | reasoning responses | recipe-specific | training pipeline | post-RLVR ceiling and training compute | in-domain and out-of-domain reasoning benchmarks |
| SF-2026-SIGMOID-KV | learned hard KV eviction on OpenWebText | GPT-2-scale Transformers | Not Disclosed — controlled training setup | Not Disclosed — controlled setup | matched live-cache protocol | language-model continuation | controlled factorial cells | offline | perplexity under matched cache budget | PPL against dense references, H2O and KeyDiff implementations |
| SF-2026-INJECMEM | one-interaction memory injection across 19 synthetic domains | Qwen, Llama and Mistral backbones with MemoryOS/MemGPT | Not Disclosed — offline memory-system evaluation | Not Disclosed — multiple backbones | variable fused contexts and placements | targeted later responses | system/domain-specific | repeated related queries | targeted retrieval/generation with non-target utility boundary | author attack success and topic-conditioned behavior |
| SF-2026-INTERACTION-TAX | 11 verifier-scored optimization tasks | multiple LLM families under matched budgets | Not Disclosed — provider/model execution | Not Disclosed — heterogeneous models | task prompts and exchanged solutions/critiques | candidate solutions | matched total budget | independent or interacting agents | verifier score per equal budget and diversity change | deterministic task verifiers |
| SF-2026-SWE-REFACTOR | 20 whole-repository stack migrations | eight frontier models; 26 effort configurations | Not Disclosed — heterogeneous agent providers | Not Disclosed — provider models | whole repositories | migrated repositories and tests | 520 runs | agent-run-specific | migration completeness plus behavioral correctness | migration audit, fixed tests and six-agent targeted verification |
| SF-2026-REWORLD | interactive video world rollouts and out-and-back revisit | Wan2.2-based 5B world model | Not Disclosed — real-time serving hardware in v1 setup | Not Disclosed — no single precision contract | 64-second / 384-latent long rollout among other tests | 704x1280 streamed video | 1 interactive trajectory | streaming generation | action following, long-horizon recall, video quality and real-time mode | three-axis author protocol against six systems |
| SF-2026-BPCO-CRITIC | mathematical reasoning RL and rubric rewards | 1.5B model; two Qwen3 30B-A3B MoE variants | Not Disclosed — training hardware not frozen in claim | Not Disclosed — verl recipe details are source of truth | up to 24k response length in larger-data study | one rollout per prompt for critic branch | 1,024 trajectories per iteration in sanity test; other setups vary | training iteration | held-out AIME accuracy, training reward and explained variance | author-controlled ablations and group-based baseline |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-WNW-KV | RP-de4c0b56ff720dce | deep | arXiv:2608.22704v1 | SRC-ARXIV@arXiv:2608.22704v1 | https://arxiv.org/html/2608.22704#S3 | https://arxiv.org/html/2608.22704#S4 | https://arxiv.org/html/2608.22704#S5 | Not Disclosed — v1 does not link a frozen implementation commit | claim:SF-2026-WNW-KV | complete |
| SF-2026-CACHEROUTER | RP-b480fc3e8a0e10c2 | standard | arXiv:2608.22708v1 | SRC-ARXIV@arXiv:2608.22708v1 | https://arxiv.org/html/2608.22708#S3 | https://arxiv.org/html/2608.22708#S4 | https://arxiv.org/html/2608.22708#S5 | Not Required — standard route does not require an artifact | claim:SF-2026-CACHEROUTER | complete |
| SF-2026-COMPACTION-CLIFF | RP-951e6e77187459e1 | deep | arXiv:2608.22752v1 | SRC-ARXIV@arXiv:2608.22752v1 | https://arxiv.org/html/2608.22752#S3 | https://arxiv.org/html/2608.22752#S4 | https://arxiv.org/html/2608.22752#S5 | https://arxiv.org/html/2608.22752#S4.SS1 | claim:SF-2026-COMPACTION-CLIFF | complete |
| SF-2026-XTC | RP-b4b52cf6f0795a81 | closure | arXiv:2608.22758v1 | SRC-ARXIV@arXiv:2608.22758v1 | https://arxiv.org/abs/2608.22758v1 | Not Required — closure route does not assess performance | Not Required — rejection is based on durability and owner coverage | Not Required — closure route does not require an artifact | claim:SF-2026-XTC | complete |
| SF-2026-DRY-SAMPLING | RP-ee4a135fed0f61bf | closure | arXiv:2608.22761v1 | SRC-ARXIV@arXiv:2608.22761v1 | https://arxiv.org/abs/2608.22761v1 | Not Required — closure route does not assess performance | Not Required — rejection is based on durability and owner coverage | Not Required — closure route does not require an artifact | claim:SF-2026-DRY-SAMPLING | complete |
| SF-2026-TAILSIEVE | RP-07d0212f2c1c4534 | deep | arXiv:2608.22788v1 | SRC-ARXIV@arXiv:2608.22788v1 | https://arxiv.org/html/2608.22788#S3 | https://arxiv.org/html/2608.22788#S4 | https://arxiv.org/html/2608.22788#S5 | Not Disclosed — v1 does not link a frozen implementation commit | claim:SF-2026-TAILSIEVE | complete |
| SF-2026-CATCHBENCH | RP-1524b2130e44159d | deep | arXiv:2608.22808v1 | SRC-ARXIV@arXiv:2608.22808v1 | https://arxiv.org/html/2608.22808#S3 | https://arxiv.org/html/2608.22808#S5 | https://arxiv.org/html/2608.22808#S7 | https://arxiv.org/html/2608.22808#S6 | claim:SF-2026-CATCHBENCH | complete |
| SF-2026-AGENTFLOW | RP-e32d4356dcb7c016 | deep | arXiv:2608.22868v1 | SRC-ARXIV@arXiv:2608.22868v1 | https://arxiv.org/html/2608.22868#S3 | https://arxiv.org/html/2608.22868#S8 | https://arxiv.org/html/2608.22868#S9 | Not Disclosed — v1 describes a prototype without a frozen public commit | claim:SF-2026-AGENTFLOW | complete |
| SF-2026-PREFIX-INVARIANCE | RP-f90e73f20012556a | deep | arXiv:2608.22876v1 | SRC-ARXIV@arXiv:2608.22876v1 | https://arxiv.org/html/2608.22876#S2 | https://arxiv.org/html/2608.22876#S3 | https://arxiv.org/html/2608.22876#S5 | Not Disclosed — v1 does not link a frozen audit implementation | claim:SF-2026-PREFIX-INVARIANCE | complete |
| SF-2026-EXECUTION-EDITS | RP-27b8a7453730e221 | standard | arXiv:2608.22928v1 | SRC-ARXIV@arXiv:2608.22928v1 | https://arxiv.org/abs/2608.22928v1 | https://github.com/eunomia-bpf/agent-check-restore-safety | https://arxiv.org/abs/2608.22928v1 | Not Required — standard route does not require artifact review beyond identity | claim:SF-2026-EXECUTION-EDITS | complete |
| SF-2026-PROCESS-EVAL | RP-7700af5220c649f0 | deep | arXiv:2608.22960v1 | SRC-ARXIV@arXiv:2608.22960v1 | https://arxiv.org/html/2608.22960#S3 | https://arxiv.org/html/2608.22960#S4 | https://arxiv.org/html/2608.22960#S6 | Not Disclosed — v1 does not link a frozen evaluation artifact | claim:SF-2026-PROCESS-EVAL | complete |
| SF-2026-POINTING-VLA | RP-9d1ab2bfe9fa6dcd | standard | arXiv:2608.23138v1 | SRC-ARXIV@arXiv:2608.23138v1 | https://arxiv.org/abs/2608.23138v1 | https://arxiv.org/abs/2608.23138v1 | https://arxiv.org/abs/2608.23138v1 | Not Required — standard route does not require an artifact | claim:SF-2026-POINTING-VLA | complete |
| SF-2026-DIFFUSION-SUFFIX | RP-bd45d74039bfb42d | closure | arXiv:2608.23167v1 | SRC-ARXIV@arXiv:2608.23167v1 | https://arxiv.org/abs/2608.23167v1 | Not Required — closure route does not assess performance | Not Required — rejection is based on durability and owner coverage | Not Required — closure route does not require an artifact | claim:SF-2026-DIFFUSION-SUFFIX | complete |
| SF-2026-CONTEXT-ALLOCATION | RP-fe3cd1b30d3b2fcf | deep | arXiv:2608.23252v1 | SRC-ARXIV@arXiv:2608.23252v1 | https://arxiv.org/html/2608.23252#S2 | https://arxiv.org/html/2608.23252#S5 | https://arxiv.org/html/2608.23252#S7 | https://github.com/PeiYangLiu/ascp | claim:SF-2026-CONTEXT-ALLOCATION | complete |
| SF-2026-NEXTCHUNK-RL-SFT | RP-d433dd4edb30edb1 | standard | arXiv:2608.23256v1 | SRC-ARXIV@arXiv:2608.23256v1 | https://arxiv.org/abs/2608.23256v1 | https://arxiv.org/abs/2608.23256v1 | https://arxiv.org/abs/2608.23256v1 | Not Required — standard route does not require an artifact | claim:SF-2026-NEXTCHUNK-RL-SFT | complete |
| SF-2026-SIGMOID-KV | RP-c381305673095026 | standard | arXiv:2608.23296v1 | SRC-ARXIV@arXiv:2608.23296v1 | https://arxiv.org/abs/2608.23296v1 | https://arxiv.org/abs/2608.23296v1 | https://arxiv.org/abs/2608.23296v1 | Not Required — standard route does not require an artifact | claim:SF-2026-SIGMOID-KV | complete |
| SF-2026-INJECMEM | RP-3189cec823ea2bcc | deep | arXiv:2608.23471v1 | SRC-ARXIV@arXiv:2608.23471v1 | https://arxiv.org/html/2608.23471#S3 | https://arxiv.org/html/2608.23471#S4 | https://arxiv.org/html/2608.23471#S6 | Not Disclosed — v1 does not identify a frozen public implementation commit | claim:SF-2026-INJECMEM | complete |
| SF-2026-INTERACTION-TAX | RP-9b5640aeaeeedbce | deep | arXiv:2608.23541v1 | SRC-ARXIV@arXiv:2608.23541v1 | https://arxiv.org/html/2608.23541#S3 | https://arxiv.org/html/2608.23541#S4 | https://arxiv.org/html/2608.23541#S6 | Not Disclosed — v1 does not link a frozen implementation commit | claim:SF-2026-INTERACTION-TAX | complete |
| SF-2026-SWE-REFACTOR | RP-eca7db715c83701f | deep | arXiv:2608.23564v1 | SRC-ARXIV@arXiv:2608.23564v1 | https://arxiv.org/html/2608.23564#S3 | https://arxiv.org/html/2608.23564#S5 | https://arxiv.org/html/2608.23564#S6 | https://arxiv.org/html/2608.23564#S4 | claim:SF-2026-SWE-REFACTOR | complete |
| SF-2026-REWORLD | RP-b0316d92ad440129 | deep | arXiv:2608.23565v1 | SRC-ARXIV@arXiv:2608.23565v1 | https://arxiv.org/html/2608.23565#S3 | https://arxiv.org/html/2608.23565#S4 | Not Disclosed — v1 has no explicit limitations section; physical-action correctness is unevaluated | Not Disclosed — v1 does not link a frozen training repository | claim:SF-2026-REWORLD | complete |
| SF-2026-BPCO-CRITIC | RP-d0d8cc3e8d74edea | deep | arXiv:2608.23566v1 | SRC-ARXIV@arXiv:2608.23566v1 | https://arxiv.org/html/2608.23566#S3 | https://arxiv.org/html/2608.23566#S4 | https://arxiv.org/html/2608.23566#S5 | https://github.com/QPHutu/golden_critic | claim:SF-2026-BPCO-CRITIC | complete |

### Source Reviews

<!-- review:SF-2026-WNW-KV:start -->
<!-- claim:SF-2026-WNW-KV:start -->作者实验说明 long-form speech 的 prefill attention 排名不能可靠代表 decode-time usefulness；anchor heads 充当在线 observer，CPU complement 使被驱逐状态可按 chunk 召回。证据限于两个 3B speech backbones、LibriSpeech-Long 及论文给定的 CPU–GPU 路径，不能外推为所有模型的 20% GPU retention 都近似无损。<!-- claim:SF-2026-WNW-KV:end -->
其长期价值是把 eviction 从不可逆删除推进为分层、可恢复状态；代价是 calibration、host capacity、transfer scheduling 与 observer error。Books 第45章已经明确拥有这条演进。
<!-- review:SF-2026-WNW-KV:end -->

<!-- review:SF-2026-CACHEROUTER:start -->
<!-- claim:SF-2026-CACHEROUTER:start -->论文把 tool discovery 与 main-model prefix 分成两条路径，以固定 core schema 保住 prompt cache，再由 router 执行长尾工具。55 个功能查询和 30-turn dialogue 只证明原型及特定 DeepSeek 价格合同下的可行性；绝对成功率、跨模型安全性和生产尾延迟未建立。<!-- claim:SF-2026-CACHEROUTER:end -->
它是 Tool Calling 的受限架构案例，不足以改变当前 canonical owner。
<!-- review:SF-2026-CACHEROUTER:end -->

<!-- review:SF-2026-COMPACTION-CLIFF:start -->
<!-- claim:SF-2026-COMPACTION-CLIFF:start -->统一摘要对 episodic log 与 safety rule 使用同一损失函数，会在递归 compaction 中系统性损害 exact-rule retention。论文用 TypeCompact、TypeDecompose、TypeRetrieve 分别处理类型保真、分区复制与带 rule pinning 的外部检索；作者在 20 个 production configurations 与五个 public corpora 上报告受限增益。该证据不证明这些百分比跨模型、语言或私有策略成立。<!-- claim:SF-2026-COMPACTION-CLIFF:end -->
长期机制是 retention policy 必须由 knowledge type 与 future correctness contract 决定，并保留 raw-evidence fallback；这补全了 Context Compression 的 owner，而不是新增一个 memory framework 清单。
<!-- review:SF-2026-COMPACTION-CLIFF:end -->

<!-- review:SF-2026-XTC:start -->
<!-- claim:SF-2026-XTC:start -->XTC 是 next-token sampling 的 head exclusion 变体；v1 日期、身份和 MODEL-SAMPLING owner 已核验。其 human preference 与 diversity 数字受模型、量化、prompt genre 和 judge 合同约束，尚不足以改变本书的 sampling 主线。<!-- claim:SF-2026-XTC:end -->
最终处置为低耐久受限案例，不进入 Books。
<!-- review:SF-2026-XTC:end -->

<!-- review:SF-2026-DRY-SAMPLING:start -->
<!-- claim:SF-2026-DRY-SAMPLING:start -->DRY 按 suffix continuation 而非 token recurrence 惩罚 exact loop；身份、日期与 sampling owner 已闭合。它解决特定 open-ended degeneration，但不改变采样分布、终止与任务正确性的通用合同。<!-- claim:SF-2026-DRY-SAMPLING:end -->
实现采用情况与作者实验不构成跨 workload 的长期设计结论。
<!-- review:SF-2026-DRY-SAMPLING:end -->

<!-- review:SF-2026-TAILSIEVE:start -->
<!-- claim:SF-2026-TAILSIEVE:start -->Rollout step 的目标是 group makespan，而非在线 serving 的单请求 latency；TailSieve 用 partial rollout history 识别稳定长尾组，并联合控制隔离组数与 replica split。作者在五个 Qwen configurations、同一 8-GPU server 与 vLLM 设置中报告 routing-only 1.02×–1.67×，再与特定 speculative methods 组合；ragged verification 与 CUDA graph overhead 构成明确边界。<!-- claim:SF-2026-TAILSIEVE:end -->
TRAIN-GRPO 已将 partial rollout、straggler、trajectory state 与 phase-aware orchestration 写成主线，因此无需重复追加。
<!-- review:SF-2026-TAILSIEVE:end -->

<!-- review:SF-2026-CATCHBENCH:start -->
<!-- claim:SF-2026-CATCHBENCH:start -->CatchBench 把可审计性分成 PRE configuration、LIVE prefix、POST trace 三种 information state，并让七个 task contract 保留各自 label/metric。72 个 entrants 与 1,162 runs 揭示不少排序不成立，且一个简单规则可利用单一 corpus construction shortcut；证据支持“先审 label process，再读 leaderboard”，不支持某个统一 auditor 胜出。<!-- claim:SF-2026-CATCHBENCH:end -->
Evaluation chapter 已有 run identity、trajectory evidence 与 benchmark-reference audit，故为既有覆盖。
<!-- review:SF-2026-CATCHBENCH:end -->

<!-- review:SF-2026-AGENTFLOW:start -->
<!-- claim:SF-2026-AGENTFLOW:start -->AgentFlow 将敏感数据的合法流向表示为 labeled edges、path rules、task-scoped capability 与 stateful taint，由 reference monitor 执行、SMT verifier 检查受限结构。AgentDojo 等作者实验只覆盖 policy-visible flows 与配置过的 policy；overtaint、未建模 side effect 和 policy completeness 仍未解决。<!-- claim:SF-2026-AGENTFLOW:end -->
Security chapter 已从单动作授权推进到 cumulative effect 与 trajectory-level harm，并明确 model/judge 不是 authority；该论文强化但不改变现有结论。
<!-- review:SF-2026-AGENTFLOW:end -->

<!-- review:SF-2026-PREFIX-INVARIANCE:start -->
<!-- claim:SF-2026-PREFIX-INVARIANCE:start -->Causal mask 只是声明，prefix invariance 才是 observable property：固定前缀的 representation 不应因未来 suffix 改变。两次 forward-pass audit 在 192 个 injected-fault trials 中定位全部注入缺陷，并发现两个共享 lineage 的模型缺陷；它证明 audit 的存在性与局部有效性，不证明同类缺陷在所有 sequence implementations 中普遍存在。<!-- claim:SF-2026-PREFIX-INVARIANCE:end -->
该性质跨 attention、scan、normalization 与 hybrid block，补全 Transformer Layer 的 correctness invariant；因此进入 Books，但不外推具体 prevalence。
<!-- review:SF-2026-PREFIX-INVARIANCE:end -->

<!-- review:SF-2026-EXECUTION-EDITS:start -->
<!-- claim:SF-2026-EXECUTION-EDITS:start -->论文把 checkpoint、fork、restore、merge 视为不能撤销既有 authorization/tool request 的 execution edits，并给出有限模型上的 exact checker、Lean proof 与测试。它提供强形式化线索，但当前 Source Review 未把所有假设映射到现实异步工具、外部副作用与分布式 workflow。<!-- claim:SF-2026-EXECUTION-EDITS:end -->
因此保留在 Weekly，等待更完整 artifact/runtime 对读后再决定是否进入 AGENT-WORKFLOW。
<!-- review:SF-2026-EXECUTION-EDITS:end -->

<!-- review:SF-2026-PROCESS-EVAL:start -->
<!-- claim:SF-2026-PROCESS-EVAL:start -->Coding-agent process evaluation 的 action、task 与 step 是不同随机变量；论文在完整 trace 后回判单步，FDR correction 后没有单步效应存活，且范围限于 file-localization。它反驳“单步看起来正确即可解释终局成功”，但不能外推为所有 process reward 无效。<!-- claim:SF-2026-PROCESS-EVAL:end -->
Evaluation chapter 已明确区分 narrative、typed action、environment transition 与 completion evidence，故无需重复。
<!-- review:SF-2026-PROCESS-EVAL:end -->

<!-- review:SF-2026-POINTING-VLA:start -->
<!-- claim:SF-2026-POINTING-VLA:start -->Pointing-VLA 用 typed hidden-state readout 承载 point、heatmap 与 trajectory，避免把 geometry 串行化为文本；作者在 Bridge/WidowX 与有限实机 pick-place 中报告受限增益。模型、controller、collision setting 与视觉环境绑定，不能推出 typed head 在所有 embodiment 上优于 action token。<!-- claim:SF-2026-POINTING-VLA:end -->
它是 MULTIMODAL-EMBODIED-VLA 的案例，暂留 Weekly。
<!-- review:SF-2026-POINTING-VLA:end -->

<!-- review:SF-2026-DIFFUSION-SUFFIX:start -->
<!-- claim:SF-2026-DIFFUSION-SUFFIX:start -->该工作把 diffusion language model suffix 分为 local/middle/tail 并复用前一步结果；身份与日期已闭合。最高 speedup 来自与其他 acceleration 组合的 long-sequence contract，不能作为单机制收益或跨 DLM 的通用结论。<!-- claim:SF-2026-DIFFUSION-SUFFIX:end -->
现有生成范式章节已拥有 iterative refinement 与 cache/parallelism trade-off，本轮不吸收。
<!-- review:SF-2026-DIFFUSION-SUFFIX:end -->

<!-- review:SF-2026-CONTEXT-ALLOCATION:start -->
<!-- claim:SF-2026-CONTEXT-ALLOCATION:start -->论文用 causal leave-one-out probe 区分 evidence availability 与实际 utilization，再以 sequential generation、submodular scheduling 和 attribution-steered decoding分配 context budget。作者在指定 generative-search tasks、最高 32B models 中报告 portfolio recall 增益；斜率和绝对幅度依赖任务、retrieval density、decoder 与预算。<!-- claim:SF-2026-CONTEXT-ALLOCATION:end -->
RAG chapter 已把 query、compression、stopping 写成 joint policy，并区分 relevance 与 sufficient context，故是原则强化而非新结论。
<!-- review:SF-2026-CONTEXT-ALLOCATION:end -->

<!-- review:SF-2026-NEXTCHUNK-RL-SFT:start -->
<!-- claim:SF-2026-NEXTCHUNK-RL-SFT:start -->受控比较显示 Mixed SFT 在论文的 no-CoT math pipeline 中比 next-chunk reasoning RL 得到更高 post-RLVR ceiling 且训练 compute 更低；它证明 baseline 选择会改变“RL 增量”的解释，不证明 SFT 普遍优于 next-chunk RL。<!-- claim:SF-2026-NEXTCHUNK-RL-SFT:end -->
当前证据作为 TRAIN-SFT / post-training pipeline 的 Weekly context 保留。
<!-- review:SF-2026-NEXTCHUNK-RL-SFT:end -->

<!-- review:SF-2026-SIGMOID-KV:start -->
<!-- claim:SF-2026-SIGMOID-KV:start -->在 GPT-2-scale、OpenWebText 与 2×2×2 controlled study 中，sigmoid attention 虽作为 dense LM 更差，却使 learned soft gate 更容易迁移到 hard KV deletion。证据说明 attention substrate 会影响 eviction transfer，不证明大型现代 decoder 应改用 sigmoid attention。<!-- claim:SF-2026-SIGMOID-KV:end -->
其 scale 与 workload 尚不足以改变 INFER-KV-CACHE 主线，保留 Weekly。
<!-- review:SF-2026-SIGMOID-KV:end -->

<!-- review:SF-2026-INJECMEM:start -->
<!-- claim:SF-2026-INJECMEM:start -->InjecMEM 通过 retriever-agnostic topical anchor 与在不确定 fused context 下优化的 adversarial command，使一次交互形成以后可被相关 query 召回的定向 memory。实验覆盖 MemoryOS、MemGPT、多个 backbone 与 19 个 synthetic domains；rewrite-heavy memory、真实长期用户流和独立防御评估仍未建立。<!-- claim:SF-2026-INJECMEM:end -->
Memory chapter 已把 write、retrieval、provenance、ACL、derived state 与 repair 分开，并把 memory 当受保护资产；该工作提供 threat instance，但不改变 owner 结论。
<!-- review:SF-2026-INJECMEM:end -->

<!-- review:SF-2026-INTERACTION-TAX:start -->
<!-- claim:SF-2026-INTERACTION-TAX:start -->在 11 个 verifier-scored optimization tasks 与 matched budgets 中，full-solution sharing 会让不同模型方案在一轮内趋同，独立 proposal 保留 diversity；critique 仅在 violated rule 易识别和修复时有用。它支持“通信内容与时机比 Agent 数量更重要”，但不证明所有 multi-agent interaction 都有负收益。<!-- claim:SF-2026-INTERACTION-TAX:end -->
Multi-Agent chapter 已以 independence、communication tax、verification 与 budget allocation 为主线，因此无需修改。
<!-- review:SF-2026-INTERACTION-TAX:end -->

<!-- review:SF-2026-SWE-REFACTOR:start -->
<!-- claim:SF-2026-SWE-REFACTOR:start -->SWE Refactor Bench 将 migration completeness、fixed behavioral tests 与 independent agent-generated tests 分三道 Gate，避免“复制旧实现使测试通过”的 blindness。20 个 whole-repository migrations、520 runs 只证明该 benchmark contract 下 capability 与 failure slices；不能把 5.4% 或最佳分数外推到任意仓库。<!-- claim:SF-2026-SWE-REFACTOR:end -->
Evaluation chapter 已明确 artifact、process、environment 与 verifier-first contract，故为 Existing Coverage。
<!-- review:SF-2026-SWE-REFACTOR:end -->

<!-- review:SF-2026-REWORLD:start -->
<!-- claim:SF-2026-REWORLD:start -->ReWorld 用少量 global heads、recent local windows、chunk-drop、固定 KV budget 与 pose-indexed landmark bank协调短期控制和长期 revisit；四步 LoRA distillation 服务实时生成。作者 evaluation 覆盖 action following、long-horizon recall 与画面质量，但没有证明真实物理 action、causal environment correctness 或开放世界 safety。<!-- claim:SF-2026-REWORLD:end -->
World Models chapter已区分 video generation、action-conditioned transition 与 persistent state，并保留 view-indexed memory、fixed budget 与 observation reconciliation，故无需重复。
<!-- review:SF-2026-REWORLD:end -->

<!-- review:SF-2026-BPCO-CRITIC:start -->
<!-- claim:SF-2026-BPCO-CRITIC:start -->BPCO 把 critic instability 分解为 token-probability clipping、value range、bootstrapped target、advantage normalization、response-length weighting与 critic input 六个控制面；作者以 1.5B sanity test、40.3K math dataset 和两个 30B-A3B MoE 做逐项 ablation，并与 group-based baseline 比较。它证明一个受控 math-RL recipe 可使 single-rollout critic 成为 GRPO 分支的替代，不证明其跨 reward、environment 与模型规模普遍稳定。<!-- claim:SF-2026-BPCO-CRITIC:end -->
这补全 PPO 章节对 critic failure 的机制解释，并把 PPO / GRPO 的选择从“状态还是采样”推进为 credit fidelity、variance、rollout compute 与 overfitting 的联合权衡。
<!-- review:SF-2026-BPCO-CRITIC:end -->

## 4. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-COMPACTION-CLIFF | score_7_9<br>potential_books_delta | selected | DA-BOUNDED-STATE | — | 直接揭示 uniform compression 在 heterogeneous correctness contract 下失效，并连接 Context、KV 与 World State | analysis:DA-BOUNDED-STATE |
| SF-2026-WNW-KV | score_7_9 | subsumed | — | DA-BOUNDED-STATE | 可恢复 KV recall 是同一 bounded-state 演进的 runtime 分支 | analysis:DA-BOUNDED-STATE |
| SF-2026-CONTEXT-ALLOCATION | score_7_9 | subsumed | — | DA-BOUNDED-STATE | closed-loop evidence allocation 改变同一 budget 的使用策略 | analysis:DA-BOUNDED-STATE |
| SF-2026-REWORLD | score_7_9 | subsumed | — | DA-BOUNDED-STATE | fixed KV 与 landmark bank 把问题扩展到 persistent world state | analysis:DA-BOUNDED-STATE |
| SF-2026-AGENTFLOW | score_7_9<br>forced_review | selected | DA-ENFORCEABLE-EVIDENCE | — | flow policy 把自然语言风险提升为 runtime 可执行的 state/edge contract | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-CATCHBENCH | score_7_9 | subsumed | — | DA-ENFORCEABLE-EVIDENCE | PRE/LIVE/POST information states约束可审计性 | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-PREFIX-INVARIANCE | score_7_9<br>potential_books_delta | subsumed | — | DA-ENFORCEABLE-EVIDENCE | observable invariant 说明配置声明不能替代行为审计 | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-PROCESS-EVAL | score_7_9 | subsumed | — | DA-ENFORCEABLE-EVIDENCE | action/task/step 分层约束 evaluator claim | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-INJECMEM | score_7_9<br>forced_review | subsumed | — | DA-ENFORCEABLE-EVIDENCE | persistent memory 扩大了 untrusted-flow 与 repair 边界 | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-SWE-REFACTOR | score_7_9 | subsumed | — | DA-ENFORCEABLE-EVIDENCE | migration audit 与 behavioral evidence 分离终局叙述和真实 artifact | analysis:DA-ENFORCEABLE-EVIDENCE |
| SF-2026-BPCO-CRITIC | score_7_9<br>potential_books_delta | selected | DA-CREDIT-ECONOMICS | — | critic stability 与 rollout cost 同时改变 post-training 分支选择 | analysis:DA-CREDIT-ECONOMICS |
| SF-2026-TAILSIEVE | score_7_9 | subsumed | — | DA-CREDIT-ECONOMICS | long-tail rollout makespan 是 group-based branch 的系统成本 | analysis:DA-CREDIT-ECONOMICS |
| SF-2026-INTERACTION-TAX | score_7_9 | subsumed | — | DA-CREDIT-ECONOMICS | matched-budget interaction 说明更多协作并不自动产生更多有效探索 | analysis:DA-CREDIT-ECONOMICS |

<!-- analysis:DA-BOUNDED-STATE:start -->
### 从统一压缩到类型化、可恢复的状态预算

最初的短 Context、短音频与短视频可以把历史视为同质序列：超出预算后统一截断或摘要，简单且容易复算。约束改变后，不同状态承担的 correctness role 不同：safety rule 需要 exact retention，episodic log 可有损压缩；speech KV 的 prefill ranking 不代表 decode-time usefulness；世界状态既要短期控制，又要长程 revisit；RAG evidence 是否被模型真正使用也不能从 relevance proxy 推断。

新机制共同改变的是状态 owner 与恢复路径：类型化 policy 决定 compact/decompose/retrieve，anchor heads 观察后召回 host complement，causal probe 反馈调度 context，landmark bank 保存可按 pose 取回的历史。收益是同一预算服务更多未来决策，代价是分类错误、stale index、transfer latency、额外 control state 与 recovery verification。统一 sliding window 在短 horizon、状态同质、回读昂贵度高于重算时仍合理；新路线没有让压缩免费，只把不可见丢失变成可观测、可恢复的策略选择。
<!-- analysis:DA-BOUNDED-STATE:end -->

<!-- analysis:DA-ENFORCEABLE-EVIDENCE:start -->
### 从声明与终局答案到可执行证据合同

旧系统常用 causal mask、tool ACL、final success 或完整自然语言 trace 表示正确性。这些做法在 block 简单、动作无副作用、任务短且 evaluator 稳定时合理；一旦 scan/normalization、跨工具数据流、memory retrieval 与长程 migration 加入，配置声明和最终叙述都可能与真实执行分离。

本轮证据把问题拆为多层：prefix invariance 用行为测试审计序列因果；AgentFlow 对 labeled edges/path 施加 runtime policy；CatchBench区分 PRE/LIVE/POST 可见信息；process evaluation 分开 action/task/step；SWE Refactor 先验证 migration artifact 再跑行为测试；InjecMEM 说明一次 untrusted write 可在未来 retrieval 中重新激活。收益是错误可定位、release claim 可复算，代价是 policy completeness、overtaint、false reject、trace retention、隐私与 verifier maintenance。模型 judge 仍是 sensor，不拥有 authorization 或 truth。
<!-- analysis:DA-ENFORCEABLE-EVIDENCE:end -->

<!-- analysis:DA-CREDIT-ECONOMICS:start -->
### Critic 与 group baseline 是条件分支，不是代际替代

PPO 的 token-prefix critic 提供细粒度 credit，却引入 value state、bootstrapping error 与训练不稳定；GRPO 移除 critic，用同 prompt 多 rollout 的组内基线换更简单的状态，但 generation、reward evaluation 与 long-tail makespan 随 group 扩大。BPCO 说明 critic failure 不是一个超参数问题：value range、target、advantage normalization、length-adaptive GAE 与 privileged training-only input 共同决定稳定性；TailSieve则展示 group rollout 的尾部请求会决定整个 step 的 critical path。

因此选择应绑定 reward structure、credit granularity、group mixed-outcome probability、rollout price、straggler distribution 与 critic calibration，而不是默认“GRPO 更新、PPO 过时”。单 rollout critic 在受控 math reward 下可能降低采样成本，却增加 value overfit 与 recipe complexity；group-relative baseline 在 parallel rollout 便宜且比较信号可靠时仍更直接。Interaction Tax 的 matched-budget evidence 提醒我们，同理也不能把更多 Agent communication 当作免费的探索增量。
<!-- analysis:DA-CREDIT-ECONOMICS:end -->

## 5. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-WNW-KV | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L260 | books/part-02-model/19-kv-cache.md#L14; books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-WNW-KV | delta:SF-2026-WNW-KV | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-WNW-KV |
| SF-2026-COMPACTION-CLIFF | AGENT-CONTEXT | books/part-07-agent/75-context.md#L184 | books/part-07-agent/74-prompt.md#L14; books/part-07-agent/76-rag.md#L14; books/part-07-agent/77-memory.md#L14 | existing:SF-2026-COMPACTION-CLIFF | delta:SF-2026-COMPACTION-CLIFF | Direct Evolution | Integrate | books-review:SF-2026-COMPACTION-CLIFF |
| SF-2026-TAILSIEVE | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L943 | books/part-04-training-system/32-ppo.md#L14; books/part-05-inference-system/56-inference-scheduling.md#L14 | existing:SF-2026-TAILSIEVE | delta:SF-2026-TAILSIEVE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-TAILSIEVE |
| SF-2026-CATCHBENCH | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1145 | books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-07-agent/84-agent-platform.md#L14 | existing:SF-2026-CATCHBENCH | delta:SF-2026-CATCHBENCH | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-CATCHBENCH |
| SF-2026-AGENTFLOW | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L483 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14 | existing:SF-2026-AGENTFLOW | delta:SF-2026-AGENTFLOW | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-AGENTFLOW |
| SF-2026-PREFIX-INVARIANCE | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#L309 | books/part-02-model/16-feed-forward-mlp.md#L14; books/part-02-model/18-decoder-only.md#L14 | existing:SF-2026-PREFIX-INVARIANCE | delta:SF-2026-PREFIX-INVARIANCE | Direct Evolution | Integrate | books-review:SF-2026-PREFIX-INVARIANCE |
| SF-2026-PROCESS-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1145 | books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-07-agent/84-agent-platform.md#L14 | existing:SF-2026-PROCESS-EVAL | delta:SF-2026-PROCESS-EVAL | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-PROCESS-EVAL |
| SF-2026-CONTEXT-ALLOCATION | AGENT-RAG | books/part-07-agent/76-rag.md#L260 | books/part-07-agent/75-context.md#L14; books/part-07-agent/77-memory.md#L14 | existing:SF-2026-CONTEXT-ALLOCATION | delta:SF-2026-CONTEXT-ALLOCATION | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-CONTEXT-ALLOCATION |
| SF-2026-INJECMEM | AGENT-MEMORY | books/part-07-agent/77-memory.md#L797 | books/part-07-agent/76-rag.md#L14; books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-INJECMEM | delta:SF-2026-INJECMEM | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-INJECMEM |
| SF-2026-INTERACTION-TAX | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L34 | books/part-07-agent/81-workflow.md#L14; books/part-07-agent/83-mcp.md#L14 | existing:SF-2026-INTERACTION-TAX | delta:SF-2026-INTERACTION-TAX | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-INTERACTION-TAX |
| SF-2026-SWE-REFACTOR | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1231 | books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-07-agent/84-agent-platform.md#L14 | existing:SF-2026-SWE-REFACTOR | delta:SF-2026-SWE-REFACTOR | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-SWE-REFACTOR |
| SF-2026-REWORLD | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L191 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14 | existing:SF-2026-REWORLD | delta:SF-2026-REWORLD | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-REWORLD |
| SF-2026-BPCO-CRITIC | TRAIN-PPO | books/part-04-training-system/32-ppo.md#L109 | books/part-04-training-system/31-rlhf.md#L14; books/part-04-training-system/33-grpo.md#L14 | existing:SF-2026-BPCO-CRITIC | delta:SF-2026-BPCO-CRITIC | Alternative Branch | Integrate | books-review:SF-2026-BPCO-CRITIC |

<!-- books-review:SF-2026-WNW-KV:start --><!-- existing:SF-2026-WNW-KV:start -->第45章已从 workload-aware eviction 推进到 exact main、approximate residual 与可恢复分层 recall。<!-- existing:SF-2026-WNW-KV:end --><!-- delta:SF-2026-WNW-KV:start -->WnW 增加 speech decode-time observer 的受限实例，不改变通用 state ownership。<!-- delta:SF-2026-WNW-KV:end -->相邻边界复核：第19章只拥有 KV 的模型语义，第54章拥有 HBM budget；分层 recall 的生命周期仍由第45章负责。<!-- books-review:SF-2026-WNW-KV:end -->
<!-- books-review:SF-2026-COMPACTION-CLIFF:start --><!-- existing:SF-2026-COMPACTION-CLIFF:start -->第75章已说明 generic summary 会丢 exception、数字与 provenance，但未把不同 knowledge types 的 retention operator 连成显式 contract。<!-- existing:SF-2026-COMPACTION-CLIFF:end --><!-- delta:SF-2026-COMPACTION-CLIFF:start -->新增 typed compact/decompose/retrieve 演进及其 raw-source、rule pinning 与 failure boundary。<!-- delta:SF-2026-COMPACTION-CLIFF:end -->相邻边界复核：Prompt 只定义输入，RAG 提供 evidence，Memory 保存跨调用状态；本次调用的选择与压缩仍由 Context owner 承担。<!-- books-review:SF-2026-COMPACTION-CLIFF:end -->
<!-- books-review:SF-2026-TAILSIEVE:start --><!-- existing:SF-2026-TAILSIEVE:start -->第33章已拥有 partial rollout、straggler、trajectory persistence、policy freshness 与 phase-aware orchestration。<!-- existing:SF-2026-TAILSIEVE:end --><!-- delta:SF-2026-TAILSIEVE:start -->TailSieve 提供 tail isolation + replica split 的作者实验，不改变既有原则。<!-- delta:SF-2026-TAILSIEVE:end -->相邻边界复核：PPO 章节拥有 critic 分支，推理调度只提供可复用的 tail-control 原理；group rollout 的持久状态和同步边界仍归 GRPO。<!-- books-review:SF-2026-TAILSIEVE:end -->
<!-- books-review:SF-2026-CATCHBENCH:start --><!-- existing:SF-2026-CATCHBENCH:start -->第66章已分离 agent narrative、typed actions、environment transition 与 completion checks，并要求审计 benchmark reference。<!-- existing:SF-2026-CATCHBENCH:end --><!-- delta:SF-2026-CATCHBENCH:start -->PRE/LIVE/POST 三态细化 auditor information contract，但不改变 owner 结论。<!-- delta:SF-2026-CATCHBENCH:end -->相邻边界复核：Monitoring 只提供 observed signals，Agent Platform 提供 runtime identity；信息可见性与 verdict contract 仍归 Evaluation。<!-- books-review:SF-2026-CATCHBENCH:end -->
<!-- books-review:SF-2026-AGENTFLOW:start --><!-- existing:SF-2026-AGENTFLOW:start -->第72章已将 authorization、cumulative effect、trajectory harm 与 independent enforcement 分层。<!-- existing:SF-2026-AGENTFLOW:end --><!-- delta:SF-2026-AGENTFLOW:start -->flow/path policy 和 bounded verifier 是具体实现分支，policy completeness 仍是开放问题。<!-- delta:SF-2026-AGENTFLOW:end -->相邻边界复核：Multi-tenancy 提供 principal identity，Production 负责 recovery；跨动作授权与 trajectory harm 的 canonical owner 仍是 Security。<!-- books-review:SF-2026-AGENTFLOW:end -->
<!-- books-review:SF-2026-PREFIX-INVARIANCE:start --><!-- existing:SF-2026-PREFIX-INVARIANCE:start -->第17章解释 causal sequence block 的组成，却主要把 causality 当 attention-mask 构造。<!-- existing:SF-2026-PREFIX-INVARIANCE:end --><!-- delta:SF-2026-PREFIX-INVARIANCE:start -->新增 prefix invariance 作为跨 attention/scan/norm 的 observable invariant 与两次-forward审计。<!-- delta:SF-2026-PREFIX-INVARIANCE:end -->相邻边界复核：MLP 只拥有逐位置非线性，Decoder-only 拥有 causal 接口；跨子层的 prefix invariant 必须由 Transformer Layer 负责。<!-- books-review:SF-2026-PREFIX-INVARIANCE:end -->
<!-- books-review:SF-2026-PROCESS-EVAL:start --><!-- existing:SF-2026-PROCESS-EVAL:start -->第66章已明确过程叙述、动作证据与终局状态不能互换。<!-- existing:SF-2026-PROCESS-EVAL:end --><!-- delta:SF-2026-PROCESS-EVAL:start -->file-localization 的 action/task/step evidence进一步限制 process-score 外推，但无需新增正文。<!-- delta:SF-2026-PROCESS-EVAL:end -->相邻边界复核：Monitoring 不定义质量真值，Agent Platform 不拥有 scorer；process/outcome evidence 的版本合同仍归 Evaluation。<!-- books-review:SF-2026-PROCESS-EVAL:end -->
<!-- books-review:SF-2026-CONTEXT-ALLOCATION:start --><!-- existing:SF-2026-CONTEXT-ALLOCATION:start -->第76章已区分 relevance 与 sufficient context，并把 query、compression、stopping 定义为 joint policy。<!-- existing:SF-2026-CONTEXT-ALLOCATION:end --><!-- delta:SF-2026-CONTEXT-ALLOCATION:start -->causal utilization probe 与 sequential portfolio allocation 为受限实现证据，不改变原则。<!-- delta:SF-2026-CONTEXT-ALLOCATION:end -->相邻边界复核：Context 约束单次可见输入，Memory 约束跨调用持久状态；检索预算与 stopping policy 仍归 RAG。<!-- books-review:SF-2026-CONTEXT-ALLOCATION:end -->
<!-- books-review:SF-2026-INJECMEM:start --><!-- existing:SF-2026-INJECMEM:start -->第77章已经把 write admission、retrieval、provenance、ACL、derived state 与 repair 分开，并包含 memory security。<!-- existing:SF-2026-INJECMEM:end --><!-- delta:SF-2026-INJECMEM:start -->单次交互的 retriever-anchored injection 是威胁实例，没有改变 canonical defense contract。<!-- delta:SF-2026-INJECMEM:end -->相邻边界复核：RAG 负责 retrieval，Tool Calling 负责 effect-time execution；持久污染、派生状态与 repair 仍由 Memory owner 管理。<!-- books-review:SF-2026-INJECMEM:end -->
<!-- books-review:SF-2026-INTERACTION-TAX:start --><!-- existing:SF-2026-INTERACTION-TAX:start -->第82章已把 independent exploration、communication tax、diversity、verification 与 matched budget 连成主线。<!-- existing:SF-2026-INTERACTION-TAX:end --><!-- delta:SF-2026-INTERACTION-TAX:start -->full-solution sharing 的趋同实验强化已有 boundary，不增加新 owner。<!-- delta:SF-2026-INTERACTION-TAX:end -->相邻边界复核：Workflow 拥有 durable control，MCP 只标准化协议；协调拓扑与 communication tax 仍归 Multi-Agent。<!-- books-review:SF-2026-INTERACTION-TAX:end -->
<!-- books-review:SF-2026-SWE-REFACTOR:start --><!-- existing:SF-2026-SWE-REFACTOR:start -->第66章已从 final answer 推进到 executable artifact、process、environment 与 verifier-first synthesis。<!-- existing:SF-2026-SWE-REFACTOR:end --><!-- delta:SF-2026-SWE-REFACTOR:start -->migration audit 防止行为测试被旧实现绕过，是既有 contract 的强实例。<!-- delta:SF-2026-SWE-REFACTOR:end -->相邻边界复核：Monitoring 只观察运行，Agent Platform 只交付执行面；artifact/process/environment 的证据次序仍归 Evaluation。<!-- books-review:SF-2026-SWE-REFACTOR:end -->
<!-- books-review:SF-2026-REWORLD:start --><!-- existing:SF-2026-REWORLD:start -->第25章已拥有 view-indexed memory、recent/local 与 global state、fixed budget、revisit 和 observation reconciliation。<!-- existing:SF-2026-REWORLD:end --><!-- delta:SF-2026-REWORLD:start -->ReWorld 把这些机制组合进实时视频生成，但未提升到物理 causal correctness。<!-- delta:SF-2026-REWORLD:end -->相邻边界复核：第24章拥有生成 factorization，第26章拥有 physical action；latent transition 与 revisable world state 仍归 World Models。<!-- books-review:SF-2026-REWORLD:end -->
<!-- books-review:SF-2026-BPCO-CRITIC:start --><!-- existing:SF-2026-BPCO-CRITIC:start -->第32章已有 value/GAE、critic cost 与 GRPO 分支，但缺少 critic instability 的联合 failure contract。<!-- existing:SF-2026-BPCO-CRITIC:end --><!-- delta:SF-2026-BPCO-CRITIC:start -->新增 value range、unbiased target、raw advantage、length-adaptive GAE 与 privileged critic input 的条件链，并保留实验边界。<!-- delta:SF-2026-BPCO-CRITIC:end -->相邻边界复核：RLHF 只拥有 reward/alignment 目标，GRPO 拥有 group-relative branch；critic 的联合稳定性合同仍归 PPO。<!-- books-review:SF-2026-BPCO-CRITIC:end -->

## 6. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260825-COVERAGE | fresh-context:window-replay-audit | coverage | coverage:SRC-ARXIV:20260825; coverage:SRC-HF-PAPERS:20260825; coverage:SRC-OPENAI:20260825 | none | Not Required — exact 24-hour window, API total, cursor, watermark and paper-only exclusions are explicit | passed |
| SA-20260825-EVIDENCE | fresh-context:claim-boundary-audit | evidence | validator:review-completion-v1; review:SF-2026-COMPACTION-CLIFF; review:SF-2026-BPCO-CRITIC | none | Not Required — every family has route-matched locators, bounded claims and non-generalization limits | passed |
| SA-20260825-SELECTION | fresh-context:selection-adversary | deep_analysis_selection | analysis:DA-BOUNDED-STATE; analysis:DA-ENFORCEABLE-EVIDENCE; analysis:DA-CREDIT-ECONOMICS | none | Not Required — all 13 eligible families are selected or explicitly subsumed by three non-duplicative narratives | passed |
| SA-20260825-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-WNW-KV; books-review:SF-2026-COMPACTION-CLIFF; books-review:SF-2026-TAILSIEVE; books-review:SF-2026-CATCHBENCH; books-review:SF-2026-AGENTFLOW; books-review:SF-2026-PREFIX-INVARIANCE; books-review:SF-2026-PROCESS-EVAL; books-review:SF-2026-CONTEXT-ALLOCATION; books-review:SF-2026-INJECMEM; books-review:SF-2026-INTERACTION-TAX; books-review:SF-2026-SWE-REFACTOR; books-review:SF-2026-REWORLD; books-review:SF-2026-BPCO-CRITIC; review:SF-2026-CACHEROUTER; review:SF-2026-EXECUTION-EDITS; review:SF-2026-POINTING-VLA; review:SF-2026-NEXTCHUNK-RL-SFT; review:SF-2026-SIGMOID-KV; semantic-review:SA-20260825-BOOKS | none | Verified — all 13 target propositions, semantic adjacent-owner boundaries, bounded Books receipts and five Weekly Only dispositions | passed |

<!-- semantic-review:SA-20260825-BOOKS:start -->Fresh-context reviewer verified all 13 Books receipts after target and semantic-adjacency corrections; no unresolved finding remains.<!-- semantic-review:SA-20260825-BOOKS:end -->

## 7. Ignored Noise

390 条 arXiv 命中中，369 条未进入最终 denominator，按以下可复算理由闭合：

- 领域应用但不改变 AI-System contract：医学、金融、天文、材料、遥感、推荐与单一垂直任务论文。
- 纯 benchmark / dataset 增量，未改变 measurement、evidence 或 release contract。
- 单模型、单数据集上的 quality gain，没有机制、状态所有权或系统 trade-off 增量。
- 与 21 个 family 重复的 cross-listing、同一 v1 多分类命中。
- 只在标题或摘要中提到 LLM / Agent，但系统贡献属于应用层，不进入 Books 知识树。

代表性拒绝包括 domain-specific KG-RAG、医疗 dialogue、单项 image/video generation 与常规 federated optimization；它们没有被当作“低分候选”稀释账本，而是完成 identity/topic closure 后计入 rejection denominator。

## 8. Recommended Action

1. 2026-W35 Sunday Weekly 聚合时复用本日报的 Review Provenance，并检查 8 月 25～30 日是否出现 revision、artifact 或反证。
2. 对本次三个 Books Integration 章节做人工顺读，重点检查是否与相邻段落重复，而不是只确认 Git Diff。
3. BPCO 的 privileged critic input 只作为 training-time branch；没有独立 reward correctness 和 overfit evidence 时，不提升为默认 recipe。
4. ReWorld、Pointing-VLA 与 AgentFlow 的作者 benchmark 保持 Experimental / scoped，不把画面质量、局部实机成功率或 benchmark ASR 外推到生产。

## 9. Repository Changes

- 重建 `papers/2026/08/25/README.md`，替换旧宽窗口 V2.1 migration report。
- 更新 `books/part-02-model/17-transformer-layer.md`：prefix invariance 与行为审计。
- 更新 `books/part-04-training-system/32-ppo.md`：critic 稳定性的联合合同及与 GRPO 的分支边界。
- 更新 `books/part-07-agent/75-context.md`：按 knowledge type 的 compact / decompose / retrieve retention policy。
- 不更新 `docs/LEARNING_STATE.md`；本次没有推进学习进度或改变全书结构。
- 不生成 provisional Weekly，不 stage、commit 或 push。

## 10. Open Questions

- Critic recipe 从 math outcome reward 迁移到 long-horizon tool environment 后，value range、target 与 privileged information 如何重新定义？
- 类型化 compaction 的 classifier 错误如何进入 safety SLO，哪些规则必须由 deterministic registry 而非 LLM classification 拥有？
- Prefix invariance audit 如何扩展到 fused kernels、distributed sequence parallel 与缓存复用，而不把数值噪声误判为 causality leak？
- World-model landmark memory 能否在 object mutation、contradictory observation 与 multi-agent interaction 下保持 identity 和 supersession？

## 11. Sources

访问日期均为 2026-08-25；论文日期均以 arXiv v1 为准。

- WnW: https://arxiv.org/abs/2608.22704v1
- CacheRouter: https://arxiv.org/abs/2608.22708v1
- The Compaction Cliff: https://arxiv.org/abs/2608.22752v1
- XTC: https://arxiv.org/abs/2608.22758v1
- DRY: https://arxiv.org/abs/2608.22761v1
- TailSieve: https://arxiv.org/abs/2608.22788v1
- CatchBench: https://arxiv.org/abs/2608.22808v1
- AgentFlow: https://arxiv.org/abs/2608.22868v1
- The Mask Is Not the Model: https://arxiv.org/abs/2608.22876v1
- Safe Execution Edits: https://arxiv.org/abs/2608.22928v1
- Process Evaluation of Coding Agents: https://arxiv.org/abs/2608.22960v1
- Pointing-VLA: https://arxiv.org/abs/2608.23138v1
- Structured Suffix Modeling: https://arxiv.org/abs/2608.23167v1
- Laws of Context Allocation: https://arxiv.org/abs/2608.23252v1
- Next-Chunk RL vs SFT: https://arxiv.org/abs/2608.23256v1
- Sigmoid Attention for KV Eviction: https://arxiv.org/abs/2608.23296v1
- InjecMEM: https://arxiv.org/abs/2608.23471v1
- The Interaction Tax: https://arxiv.org/abs/2608.23541v1
- SWE Refactor Bench: https://arxiv.org/abs/2608.23564v1
- ReWorld: https://arxiv.org/abs/2608.23565v1
- How to Train a Critic Stably and Efficiently: https://arxiv.org/abs/2608.23566v1
