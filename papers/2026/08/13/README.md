# AI Research Daily — 2026-08-13

- **Research date:** 2026-08-13（Asia/Shanghai）
- **Coverage window:** 2026-08-11 00:00 ～ 2026-08-13 09:08（Asia/Shanghai，约 48 小时）
- **Access date:** 2026-08-13
- **Status:** Daily primary-source review completed；5 个 `20+` 学术候选完成全文核验；3 个既有章节 refined

## Executive Summary

今天没有确认到窗口内足以改变知识树的模型机构公告或 AI Infra release；高价值证据集中在 8 月 11 日
首次公开的五篇 Agent/Memory/Workflow 论文。它们不是五条孤立“新方法”，而是三条相互衔接的演进：

```text
append-only instructions
→ rationale-aware maintenance
→ typed contract consolidation

semantic memory retrieval
→ provenance-aware authorization / action gating
→ dependency-guided state and execution repair

isolated search branches
→ evidence-backed shared environment constraints
→ stage-aware budget and uncertainty-guided exploration
```

五篇均为 arXiv v1；作者实验支持对应 mechanism 在其受控条件下成立，不构成 production-ready 或
跨 workload 的通用结论。本日因此 refine Ch70、Ch73、Ch77，保留旧方案成立条件，并明确新增的状态、
授权、污染传播和恢复成本；没有新增 Part、章节或 Roadmap 节点。

## 1. 模型与研究机构

### Source Coverage

按 Daily 固定顺序检查 OpenAI、Anthropic、Apple Machine Learning Research、Google DeepMind、Google
Research、Meta AI / FAIR、Microsoft Research、NVIDIA Research、Amazon Science，以及其余核心机构的
official Research / News / Publication surfaces。本次可访问索引中未确认到 first-public date 位于窗口内、
且达到本项目长期门槛的机构候选。

这是本次实际访问面的 `No Material Update`，不是对所有机构或所有页面的全局否定。旧 model release、
被搜索重新索引的论文和没有公开 mechanism 的产品内容未被移入今天。

### Candidate Scoring

本组没有新增评分候选。

## 2. 论文与学术来源

### Source Coverage

按 arXiv `cs.AI → cs.CL → cs.LG → cs.DC` 检查 recent list，并以 cs.SE / cs.MA / cs.CR 等主题交叉
发现 Coding Agent、Memory、Multi-Agent 和 Agent Security 候选；随后用 arXiv HTML 核验 v1 metadata、
Introduction、Related Work、Method、Implementation、Evaluation、Ablation、Appendix 与 limitation。
Hugging Face Daily Papers、Semantic Scholar、Google Scholar、OpenAlex 与 DBLP 只作为 discovery / metadata
入口，技术结论均回到 arXiv 正文；本轮没有用索引摘要提升 Evidence Level。

五个 retained candidates 同为 `arXiv v1, 2026-08-11`。cs.AI recent 页面在 8 月 12 日展示它们，不改变
first-public date。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Recovering Wasted Compute in Autoresearch Agents | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、代码链接与 10-seed protocol；单一 backbone、无独立复现 |
| Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding | 2026-08-11 | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | E2 — arXiv v1 全文、observational corpus + controlled worlds；单篇预印本 |
| Dependency-Guided Rollback Repair for Memory-Augmented Agents | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、controlled + adapted transfer；fault identifiers 已给定 |
| MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、ablation/backbone transfer；synthetic single-round benchmark |
| SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents | 2026-08-11 | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | E2 — arXiv v1 全文、contract audit 与 held-out tasks；保证仅覆盖 extracted contract |

### Deep Analysis 1 — Prompt / Skill：从追加记忆到可逆维护

#### Why

Agent instruction files 和 self-evolving skills 通常在失败后追加规则。追加一条约束的局部成本很低，
但 rationale 消失后，删除它必须重新判断与其他 rules 的干扰、触发条件和潜在 regression；于是“每次
修复都合理”可以累积成整体不可维护。

#### Principle

可删除性来自 write-time rationale 与 falsification evidence，而不是来自 age、frequency 或文本相似度。
压缩也不是删掉低频规则，而是在 hard coverage 下寻找最短的 faithful contract representation。

#### Mechanism

Catastrophic Remembering 先在 1,867 个 GitHub repositories、247,694 个 instruction lifetimes 中测量
instruction retention，再构造 184 个 inverse-IFEval worlds 比较 informative comments、noise comments 与
control；comment schema 保存 failure、outcome、recurrence/falsification lineage 等删除证据。

SkillZip 将 skill 抽成 interface、guards、workflow、tool requirements、constraints、outputs 和 exceptions，
把 source residuals 保留为 coverage boundary，再以 minimum-description-length 风格选择共享规则、scope
lifting、workflow reuse 与 guarded deltas。Zip-on-Write 把 patch 分成 absorb / refine / extend / refactor，
并在局部更新之外保留 periodic global repack。

#### Trade-offs and Evidence Boundary

- 真实 repository 结果是 observational，不能单独证明 rationale comment 导致增长；controlled worlds 才隔离机制。
- Catastrophic Remembering 的 pooled ratchet 主要由 two-constraint slice 支撑；部分 maintainer / judge 对照
  的区间不能排除零。
- SkillZip 的 hard coverage 保护的是 parser 抽出的 normative units；自然语言抽取错误或行为差异仍需 task evaluation。
- 更丰富的 rationale、sidecar contract、extractor version 和 repack policy 本身会增加 artifact、storage 与审计成本。

#### Connection and Evolution

主 owner 是 Ch70；Ch71 只接收 context-budget handoff，Ch80 继续拥有 Skill registry / rollout：

```text
short manually reviewed prompt
→ append-only failure rules
→ rationale ledger enables evidence-based deletion
→ typed local consolidation preserves rare guards
→ periodic global repack + behavioral regression
```

关系为 `Direct Evolution`。短 Prompt 与人工 review 没有失效；它们在规则少、owner 明确时成本更低。

#### Recommended Action

`Refine — Existing Argument`：Ch70 新增 Prompt maintenance / deletion contract 与 typed consolidation；不把
论文 compression rate 或 instruction-following headline写成通用收益。

### Deep Analysis 2 — Memory：从相关性检索到授权、污染传播与选择性恢复

#### Why

一条 Memory 即使语义相关，也可能来自 private、revoked、poisoned 或 wrong-user ancestor；删除源记录又
不会自动修复已派生的 summary、claim、plan、tool action 与 answer。Flat metadata 和“删除检索到的内容”
都无法表达完整影响域。

#### Principle

Memory control 要分离：hard authorization、graded path trust、action-risk evidence gate，以及 persistent
memory disposition 与 execution-trace disposition。Graph reachability 标记“可能受影响”，独立支持才判断
哪些节点仍可保留。

#### Mechanism

MAP-Graph 用 typed execution provenance graph 记录 owner、visibility、source/parent、trust 与 action，先做
permission filter，再以 semantic score × path trust 排序，最后按 action risk 选择 Allow / Block / Reverify /
Redact / AskUser。Revocation 会更新直接 affected records，并在后续 ancestry traversal 中传播。

Dependency-Guided Rollback 接受已诊断 faulty memories 与 failed trace，构造 memory-to-action dependency
graph，追踪 descendants，用 independent evidence 保留仍成立的节点；deterministic planner 将 memory 的
delete/quarantine/preserve 与 trace 的 invalidate/replay/preserve 分开，只重放 answer-relevant executable closure。

#### Trade-offs and Evidence Boundary

- MAP-Graph 的 2,700 tasks/method 是 synthetic、templated、四个 fixed-order roles 的单轮任务；不执行外部副作用。
- 其 trust 常数和 risk thresholds 是显式 policy，不是从开放世界事实中学到的“真值”。
- Rollback paper 的 controlled set 150 cases，transfer set 是 50 个经过 schema 筛选的 LongMemEval-V2 cases；
  单次 temperature-zero run 不能估计 inference nondeterminism。
- Repair 输入已包含 diagnosed fault identifiers，所以证据不覆盖在线 fault detection；replay 也不能撤销不可逆工具结果。

#### Connection and Evolution

主 owner 是 Ch73，Ch77 拥有 external compensation/reconciliation，Ch78 复用 shared-state authorization：

```text
semantic memory retrieval
→ permission-scoped records
→ ancestry-aware trust and revocation
→ action-time evidence gate
→ diagnosed fault + affected-subgraph tracing
→ selective state repair and replay
```

MAP-Graph 到 rollback repair 是 `Layering / Dependency`：前者降低错误读取与行动，后者处理错误已经传播后的恢复。

#### Recommended Action

`Refine — Existing Argument`：Ch73 将已有 provenance / selective repair 原则推进到可执行 read-action-repair
contract，并保留不可逆 side-effect 的 Workflow 边界。

### Deep Analysis 3 — Search Workflow：跨分支共享什么，预算在哪个阶段使用

#### Why

Tree-search Agent 为保持探索而隔离 branches，但这会让 library/API/runtime constraints 在每个 branch 中
重复发现；同时“找到第一个 valid solution”常导致预算提前停止，随机 sibling selection 又会把计算花在
长期 dead ends。

#### Principle

只共享可观察、可复现、绑定 environment identity 的 global constraints；hypothesis 和未经验证的 workaround
保持 branch-local。预算不是一个总数，而是随 search phase 在 exploration、validity 与 tuning 之间分配。

#### Mechanism

作者为 AIDE / ML-Master 增加 global debug consultant：从 error logs 抽取 banned patterns 与 verified fixes，
在 generation/debug 前注入相关 constraints，并把 timeout / empty log 视为 deterministic terminal dead end。
另以 prompt directive 或 control-loop reward 让 early stage 建 baseline、late stage 强化 tuning，并用 sibling-level
Beta posterior / Thompson Sampling 在 uncertainty 与 observed reward 之间选择下一节点。

#### Trade-offs and Evidence Boundary

- 实验覆盖九个 tabular competitions、GPT-5-mini、两种主要 Agent frameworks、每条件十个 seeds，固定
  `2 hours / 22 CPU cores`；不能外推到 scientific labs、software engineering 或长时外部工具任务。
- HPO quality 由 LLM rubric 评分，可能改变 selection objective；shared consultant 若错误会形成全树 poisoning。
- 论文只保持 model fixed，不意味着总系统成本或所有 runtime 条件相同；新的 registry、judge 与 control rule
  也消耗 token、CPU 和维护成本。

#### Connection and Evolution

主 owner 是 Ch77；Ch73 只拥有 constraint record 的 persistence，Ch78 只接收 shared-state handoff：

```text
independent tree branches
→ repeated environment discovery
→ provenance-bound shared constraint registry
→ stage-aware exploration / tuning budget
→ uncertainty-guided branch selection
```

这是 `Refine — Existing Argument`，不是“共享所有 Memory”或“Thompson Sampling 替代所有 search policy”。

## Full Source Review Addendum — Five `20+` Candidates

### Catastrophic Remembering — 28/30

- **Problem / Previous Design / Changed Constraint:** append-after-failure 简单、可局部验证；长期维护后，失去
  rationale 的删除需要重建被隐藏的 counterfactual constraints，规则 retention 出现 ratchet。
- **State / Flow / Implementation:** repository instruction lifetimes 用 line classification 与 deletion hazard 描述；
  controlled world 的 maintainer 在 observed failure 后维护 prompt，comment channel 保存 latent reasoning，executor
  独立测试 constraint satisfaction。正文和 Appendix 披露 judge checks、world draws 与 compute/artifact 边界。
- **Evidence / Not Proved:** corpus 支持“增长与 age-dependent retention”的关联，inverse-IFEval / WildIFEval 支持
  comment mechanism 在特定 worlds / models 中的因果效果；不证明所有仓库或 Prompt 都会无界增长，也不证明
  任意 comment schema 都有效。`Integrate — New Mechanism (Ch70)`。

### SkillZip — 28/30

- **Problem / Mechanism:** self-evolving skill 的冗余常是 scope overlap、复制 workflow 和 exception duplication；
  one structured extraction + deterministic min-cost cover 生成普通 SKILL.md，sidecar 保存 contract/provenance，
  structural audit 在缺项时恢复 source spans。continual mode 局部更新并在阈值触发 repack。
- **Evaluation Contract:** BFCL-V4、LiveMath、Spreadsheet，Qwen-3.7-Max / Qwen-3.6-Plus / Kimi-K2.6；与
  evolved skill、human skill、SkillReducer 比较，另测 held-out behavior、cross-model transfer、online rounds 与成本。
- **Evidence / Not Proved:** reported 31.2% average compression 与 fidelity 只绑定这些 generated/evolved skills、
  tokenizer、models 和 benchmarks；contract preservation 不等于 behavioral equivalence。`Refine — Existing
  Argument (Ch70; Ch80 handoff)`。

### MAP-Graph — 29/30

- **Problem / Mechanism:** relevant memory 可能不 admissible。typed graph 记录 User/Agent/Tool/Resource/Message/
  Memory/Claim/Action 及 derivation/access edges；permission 是 hard gate，path trust 是 graded factor，action risk
  再决定是否执行、重验证或脱敏。
- **Evaluation Contract:** 2,700 synthetic tasks/method，corporate/software/research 三领域、六实验组、四 roles；
  Qwen2.5-7B-Instruct 主实验及 GLM/Llama 20% subset transfer，temperature 0 single runs 与 cluster bootstrap。
- **Evidence / Not Proved:** ablation 支持 permission、trust propagation 与 action gate 分工；不证明 open-domain truth、
  多轮并发或真实 action safety。`Integrate — New Mechanism (Ch73; Ch78 handoff)`。

### Dependency-Guided Rollback Repair — 29/30

- **Problem / Mechanism:** delete-only 留下 downstream contamination，full reset/replay 破坏 benign state。typed graph
  将 user input、execution steps 和 memory records 相连；support check、deterministic plan 与 selective replay 分离
  state repair 和 computation repair。
- **Evaluation Contract:** 150 controlled cases、三 tool domains、四 fault types；50-case adapted LongMemEval-V2
  stress set；GPT-4o 主实验、Gemini/Qwen sensitivity，single temperature-zero run；报告 recovery、recurrence、
  faulty removal、benign preservation、invalidation F1、replay ratio 与 LLM calls。
- **Evidence / Not Proved:** 结果支持给定 fault IDs 后的 selective repair；不覆盖 fault detector、真实 side-effect
  undo、完整 LongMemEval-V2 分布或 production concurrency。`Integrate — New Mechanism (Ch73; Ch77 handoff)`。

### Recovering Wasted Compute in Autoresearch Agents — 29/30

- **Problem / Mechanism:** branch isolation 重复调试，premature stopping 留下预算，random search 困在低价值节点。
  consultant registry 共享可验证 runtime constraints，deterministic rules cut dead ends，stage-aware HPO reward 和
  Thompson Sampling 改变预算与 branch selection。
- **Evaluation Contract:** AIDE、ML-Master（及论文总研究中的第三 Agent 条件）、GPT-5-mini；九个 tabular tasks、
  每项十 seeds、2 小时和 22 CPU cores；official grading scripts，另含 adversarial EDA 与完整 code cases。
- **Evidence / Not Proved:** 支持该 contract 下 workflow design 改善 valid runs / task scores；不证明跨 domain、跨
  backbone、production SLO 或共享 registry 永远安全。`Integrate — New Mechanism (Ch77)`。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM → Ray →
KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed → Megatron-LM → Unsloth →
MLX → llama.cpp → ONNX Runtime → OpenXLA 检查 official release index / release notes 的窗口日期。

没有确认到 released-at 位于 2026-08-11～13、且改变本书稳定 runtime contract 的 Release、RFC 或重要 PR。
索引中较旧或无法对齐 tag date 的内容不回填今天。Evidence Level 为 `No Newly Verified Candidate`。

## Evidence Level and Fact Boundary

- **Official / metadata fact:** arXiv v1 日期、官方 research/release index 的可见日期与链接。
- **Primary paper evidence:** 五篇 `20+` candidates 已覆盖 metadata、background、method、state/control/data flow、
  implementation、evaluation、baselines/ablations、sensitivity/overhead、limitations 与关键 appendix。
- **Author experiment:** 所有性能和正确率只属于各自 model、task、seed、hardware/CPU budget、prompt/runtime 与
  evaluation contract；没有写成通用 production SLO。
- **Inference:** 三条演进路线是本项目基于多篇 primary evidence 与既有章节做的工程归纳，不是论文作者共同声明。
- **Community / discovery:** HF、Scholar、Semantic Scholar、OpenAlex、DBLP 的热度、摘要与 metadata 不承担技术结论。

## Knowledge Tree Position

| Source Family | Primary owner | Adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| Catastrophic Remembering + SkillZip | Ch70 Prompt | Ch71、Ch73、Ch80 | Integrate / Refine：rationale-aware deletion + typed consolidation |
| MAP-Graph + Rollback Repair | Ch73 Memory | Ch71、Ch76～78、Ch80 | Integrate：authorization/trust/action gate + selective repair |
| Recovering Wasted Compute | Ch77 Workflow | Ch73、Ch76、Ch78、Ch80 | Integrate：shared constraint registry + stage-aware budget |

## Recommended Action

- 已完成 `Refine — Existing Argument / Integrate — New Mechanism`：Ch70、Ch73、Ch77。
- 五篇论文均保持 `Status: Experimental`；不把作者 headline、单 benchmark 排名或特定 taxonomy 写成通用事实。
- Sunday W33 汇总时与 8 月 10～12 日 Daily 跨日去重，并判断上述三条路线是否需要形成更宽的 Source Family；
  Live Daily 不因 Weekly 生成而删除。
- 今日没有模型机构或 Infra 候选达到 Books 门槛。

## Ignored Noise

- arXiv recent 页面的 8 月 12 日分组时间没有被误写成论文 first-public date；五篇均按正文 metadata 记为 8 月 11 日。
- 搜索摘要、HF/Scholar 热度与旧机构文章只用于 discovery；没有因重新索引写入今天。
- Release 页面中缺少准确 tag date 或只有 feature list 的条目没有被当作窗口内正式进展。

## Repository Changes

- `papers/2026/08/13/README.md`
  - 新建当日 Daily，记录五个 Full Source Reviews、三条演进链及证据边界。
- `books/part-06-agent/70-prompt.md`
  - 增加 instruction rationale、删除 contract 与 typed skill consolidation；不改变 Prompt 仍是软接口的原结论。
- `books/part-06-agent/73-memory.md`
  - 将 provenance 从事后 metadata 推进到 authorization/trust/action gate，并补全 state/trace selective repair；
    增强已有 selective repair，不声称可撤销外部副作用。
- `books/part-06-agent/77-workflow.md`
  - 增加 search branches 的 shared constraint ownership、阶段预算与污染边界；不否定 branch isolation。
- `docs/LEARNING_STATE.md`
  - 同步本日稳定认知和未外推范围。

## Open Questions

1. Instruction rationale schema 在真实多人协作仓库中，能否降低长期维护成本而不显著增加 write friction？
2. Skill contract extractor 的 false omission 如何用独立 parser、behavioral tests 与 human review 联合估计？
3. Provenance graph 在 multi-tenant、多轮并发和大量 descendants 下，revocation latency 与 storage cost 如何控制？
4. 在线 fault detector 与 selective rollback 如何连接，且不把 detection false positive 扩大为大规模 replay？
5. Shared debug registry 如何定义 environment-equivalence key，并在 library/runtime 升级时撤销陈旧 constraints？
6. Search-phase budget policy 能否在 software engineering、scientific experiment 等非 tabular workload 跨模型复现？

## Sources

### 模型与研究机构（accessed 2026-08-13）

- OpenAI Research: https://openai.com/research/index/
- Anthropic News: https://www.anthropic.com/news
- Apple Machine Learning Research: https://machinelearning.apple.com/
- Google DeepMind: https://deepmind.google/discover/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research AI: https://www.microsoft.com/en-us/research/research-area/artificial-intelligence/
- NVIDIA Research: https://research.nvidia.com/
- Amazon Science Publications: https://www.amazon.science/publications/

### 论文 Primary Sources（published 2026-08-11；accessed 2026-08-13）

- Catastrophic Remembering: https://arxiv.org/abs/2608.11095
- Catastrophic Remembering HTML: https://arxiv.org/html/2608.11095
- SkillZip: https://arxiv.org/abs/2608.11079
- SkillZip HTML: https://arxiv.org/html/2608.11079
- MAP-Graph: https://arxiv.org/abs/2608.10509
- MAP-Graph HTML: https://arxiv.org/html/2608.10509
- Dependency-Guided Rollback Repair: https://arxiv.org/abs/2608.10502
- Dependency-Guided Rollback Repair HTML: https://arxiv.org/html/2608.10502
- Recovering Wasted Compute in Autoresearch Agents: https://arxiv.org/abs/2608.10424
- Recovering Wasted Compute HTML: https://arxiv.org/html/2608.10424
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent

### AI Infra 官方入口（accessed 2026-08-13）

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- KServe Releases: https://github.com/kserve/kserve/releases
