# Daily Research — 2026-08-06

**Coverage Window:** 2026-08-04 09:02 ～ 2026-08-06 09:02（Asia/Shanghai）
**Access Date:** 2026-08-06
**Archive Clock:** Thursday；仅生成 Daily，不生成 provisional `2026-W32`
**Status:** Primary-source review complete；3 项形成长期机制增量并已 refine 现有章节

## Executive Summary

过去 48 小时没有发现模型公司官方 Research 或核心 AI Infra 项目的窗口内重要发布。主要增量
来自 2026-08-04 首次公开、在 2026-08-05 recent 批次出现的三篇 arXiv v1：

1. **HeteroPanacea** 把 P/D disaggregation 继续展开为 Attention/FFN 与四池
   `P/D/A/F`，但更重要的长期结论不是“四池更好”，而是 disaggregation 是条件化的
   execution-graph factorization：specialization gain 必须覆盖新增 state/activation movement、
   queueing、control 与 recovery cost。
2. **TARL** 形式化了 binary `Write/Hold` 的信息损失：相同 label 可能对应 append、revise、
   reject、defer 或 noop，无法唯一确定下一版 memory。长期可吸收的是 typed memory transition，
   不是论文给出的五类 taxonomy 本身。
3. **When Attention Goes Blind** 指出 ALiBi 的线性 bias 会在有限精度 softmax 中下溢，形成
   未声明的隐式有效窗口。它修正了“数学上可定义更远位置即可执行”的直觉，同时保留默认
   ALiBi 在论文部分实验中仍是强 baseline 的事实边界。

三项均为单篇 v1 preprint，Evidence Level 均为 `Experimental`。正文只吸收机制、验证 contract
与旧方案继续成立的条件，不吸收作者峰值 benchmark，也没有新增 Part、章节或 ROADMAP 节点。

## 1. 模型与研究机构

### Source Coverage

按 `CODEX_DAILY_RESEARCH_PROMPT.md` 的每日核心来源顺序记录扫描结果：

- **OpenAI — No Material Update**
- **Anthropic — No Material Update**
- **Apple Machine Learning Research — No Material Update**
- **Google DeepMind — No Material Update**
- **Google Research — No Material Update**
- **Meta AI / FAIR — No Material Update**
- **Microsoft Research — No Material Update**
- **NVIDIA Research — No Material Update**
- **xAI News / Model Cards — No Material Update**
- **Amazon Science / AGI — No Material Update**
- **Cohere Labs — No Material Update**
- **Ai2 — No Material Update**
- **Mistral AI — No Material Update**
- **Alibaba Qwen — No Material Update**
- **DeepSeek — No Material Update**
- **Moonshot AI / Kimi — No Material Update**
- **Zhipu AI — No Material Update**
- **MiniMax — No Material Update**
- **ByteDance Seed / Research — No Material Update**
- **Baidu ERNIE — No Material Update**
- **Tencent Hunyuan — No Material Update**
- **Huawei Noah's Ark Lab / Pangu — No Material Update**
- **Shanghai AI Laboratory / InternLM — No Material Update**
- **StepFun — No Material Update**
- **Xiaomi MiMo — No Material Update**
- **InclusionAI / Ant Group — No Material Update**
- **Hugging Face Blog — No Material Update**

- 窗口内未发现同时具备 event date、primary technical evidence 与 AI System Design 长期增量的
  新发布。
- Hugging Face Blog 的社区文章、vendor post、challenge 与模型 headline 不替代 technical report、
  model card、system card 或论文，因此未作为候选。
- 搜索结果中的旧内容重收录、产品营销与缺少机制披露的 benchmark 宣传已去重。

### Candidate Scoring

本组无达到候选门槛的窗口内新事件。

## 2. arXiv / 学术来源

### Source Coverage

按 primary-source 顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML`
recent，并按关键词触发 `cs.CR`、`cs.PF`、`cs.MA` 等相关 cross-list；随后检查 OpenReview 与
TMLR 入口。TMLR submissions 页面本次返回错误，因此记录为 coverage limitation，没有据此断言
“无更新”。

Discovery / metadata 层检查 Hugging Face Daily Papers、Semantic Scholar、Google Scholar、
OpenAlex 与 DBLP。Google Scholar、OpenAlex 与 DBLP 用于标题、作者、identifier 与 first-public
date 交叉检查；Semantic Scholar 与 Hugging Face 只用于发现和 related-work，不作为结论或
first-public authority。全文优先读取 arXiv HTML，并核对 metadata、v1 时间、method、
implementation、evaluation、ablation、limitations 与影响结论的 appendix。

### Candidate Scoring

评分维度依次为 Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、Source
Reliability（SR）、Project Relevance（PR）、Longevity（L），每项 0～5。

| Candidate | TN | SI | PV | SR | PR | L | Total | Evidence / Action |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TARL: executable memory transactions | 5 | 5 | 5 | 4 | 5 | 4 | 28 | Experimental；Refine Ch73 |
| ALiBi numerical underflow | 5 | 5 | 4 | 4 | 5 | 5 | 28 | Experimental；Refine Ch13 |
| HeteroPanacea: P/D/A/F simulation | 5 | 5 | 4 | 4 | 5 | 4 | 27 | Experimental；Refine Ch51 |
| TAOT: topology-aware expert replicas | 4 | 5 | 4 | 4 | 4 | 3 | 24 | Must Read；Weekly source-family 联读 |
| Oilbird: verifier-key speculative decoding | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Watch；未完成全文 Source Packet |
| Formal verification over operational Agent data | 4 | 4 | 3 | 4 | 4 | 3 | 22 | Watch；未完成全文 Source Packet |

`SR=4` 表示可直接访问作者论文与 metadata，但尚未 peer review；它不是对结论真实性的满分背书。

### Deep Analysis 1 — HeteroPanacea

**Primary source:** arXiv:2608.03741v1，first public 2026-08-04 14:35:25 UTC。
**Evidence Level:** Experimental / single preprint / component-level simulator。
**Knowledge Tree:** Ch51 PD 分离（owner）→ Ch52 推理调度（handoff）→ Ch59 集群 placement。

#### Why

P/D 分离假设 Prefill 与 Decode 的资源画像差异足够大，值得用 KV handoff 和双队列换取独立
capacity planning。但每个 phase 内的 Attention 与 FFN 也可能因为序列长度、KV width、MoE
sparsity、precision 和 hardware 而呈现不同 compute、bandwidth 与 capacity pressure。问题因此
从“是否拆 P/D”变成“execution graph 应该在哪里切开”。

#### Principle

Disaggregation 的第一性原理不是增加 pool 数，而是让每个 pool 的 resource signature 更同质，
并且让 specialization gain 超过新切边的全部成本：

```text
specialization + reduced interference + independent control
>
state/activation transfer + queue/sync + control/recovery
```

#### Mechanism

作者构造 event-driven simulator，对 co-located、P/D、A/F 与四池 PDAF 拓扑建模；每个 stage 可
配置 NPU peak throughput、memory/bandwidth、precision、TP/PP/EP/DP 与 allocation。模型使用
component-level roofline，并分别表示 device-to-device collective 与 node-to-node KV/activation
transfer。搜索空间同时包含 quantization、parallelism 与异构 hardware allocation。

验证只覆盖 component kernels：单服务器、8×NVIDIA B200、Intel Xeon 6960P、CUDA 12.8、
PyTorch 2.10.0+cu128、NCCL 2.27.5、Python 3.12.13，使用 BF16 与 FP8 E4M3 的
cuBLAS/cuBLASLt timing。系统模拟覆盖八个 dense/MoE models，固定 output 1000 tokens、500
requests/config、125 requests/s，并扫描 input/output ratio 与模型属性。作者的吞吐结果只对这些
模拟、定价、硬件和输入假设成立，不能作为实际 serving guarantee。

#### Trade-off

- Attention/FFN 分池可能匹配不同 NPU 或 power domain，也新增 activation transfer 与同步边界。
- Decode Attention 的 KV bandwidth/capacity 与 Decode FFN 的 weight streaming 不同；MoE 又让
  expert utilization 对 batch 和 routing distribution 敏感。
- Simulator 不是 cycle-accurate；component validation 没有验证 end-to-end batching、scheduler、
  tail SLO、failure recovery 与 multi-tenant fairness。
- 论文声称代码在 acceptance 后公开，访问日尚不能检查 artifact。

#### Connection / Evolution

与 2026-08-05 的 AFlex 属于 `Principle Reuse`：AFlex 在披露的 A800 环境实现 A/F pools 和
独立 DVFS，HeteroPanacea 用模拟探索更大的 architecture/resource space。它们不是直接 lineage，
也不能互相补齐未披露条件。演进应保留为：

```text
co-location
→ P/D phase separation
→ conditional A/F or P/D/A/F factorization
→ more ownership, transfer and recovery boundaries
```

旧分支在规模较小、resource signature 接近或 interconnect 受限时仍成立。

### Deep Analysis 2 — TARL

**Primary source:** arXiv:2608.03699v1，first public 2026-08-04 14:02:55 UTC。
**Evidence Level:** Experimental / single preprint / constructed benchmark。
**Knowledge Tree:** Ch73 Memory（owner）→ Ch77 Workflow authoritative execution（boundary）。

#### Why

长期 Memory 的风险不只在“该不该写”，还在“应怎样改变旧状态”。Binary `Write/Hold` 会把
append 与 revise 合并为 Write，把 noop、reject 和 defer 合并为 Hold；同一个 label 因而不能
唯一恢复下一版 state，错误更新又会被后续 retrieval 反复放大。

#### Principle

Memory write 应是带 target、evidence 与 precondition 的 typed state transition。Accepted、
pending 与 history/inactive state 必须分离，derived view 不能抹去冲突、supersession 与等待验证
的 provenance。

#### Mechanism

TARL 用 `M_t=(A_t,P_t,H_t)` 表示 Accepted、Pending、History ledgers，把一次更新表示为包含
action、target slot 与 reliability margin 的 transaction。Pipeline 先 grounding affected slot，再
解析 temporal scope 与 source reliability，最后在 append、noop、revise、reject_conflict、
defer_verify 中选一项，由 deterministic executor 生成 next state。

训练阶段会执行 alternative actions，与 gold next state 比较 ledger-weighted quality；推理阶段只
评分一次并执行选中操作。TARL-Mem 含 5,422 个由 HaluMem-hard、LoCoMo、LongMemEval 转换并
标注的 examples；作者使用 frozen Llama-3.1-8B-Instruct、默认最多 16 visible slots，并报告
entity/topic-disjoint split、duplicate/source-majority/pattern leakage audit、cross-source holdout、
ablation 与 sequential rollout。论文正文未披露可复用的 hardware/latency/cost contract。

#### Trade-off

- Typed actions 增加 next-state 可解释性，也增加 target grounding、conflict resolution 与 policy
  versioning 的错误面。
- Source reliability metadata 本身可能错误或被攻击，不能把 model estimate 当 authority。
- 论文中的 transaction 是语义 transition，不自动提供 ACID、concurrent isolation、durability、
  crash recovery、multi-user authorization、privacy delete 或 rollback。
- 数据集来自既有 benchmarks 与作者 taxonomy；尽管有 leakage audit，仍可能对 ledger schema
  过拟合，不能证明五类 action 完备。

#### Connection / Evolution

这是对 Ch73 既有 `candidate → validate → persist with provenance` 的 `Refine — Existing
Argument`：从单向 pipeline 提升为显式 state machine，不替代 authoritative transactional system。
与 MemSecBench、ReasoningBank 和 derived-memory 路线形成：

```text
append history
→ governed candidate write
→ typed next-state transition
→ consolidation with provenance
→ review / delete / rollback across derived views
```

### Deep Analysis 3 — ALiBi numerical underflow

**Primary source:** arXiv:2608.03994v1，first public 2026-08-04 17:54:01 UTC。
**Evidence Level:** Experimental / analytic result + limited pretrained probes + 148M training study。
**Knowledge Tree:** Ch13 Position Encoding（owner）→ Ch22 Long Context effective utilization（handoff）。

#### Why

ALiBi 为距离增加线性负 bias。数学上任意距离的 bias 都有定义，但 softmax 在有限精度中执行；
当 shifted logit 的指数下溢为零，某些 heads 对远端 token 的 attention weight 会精确归零。模型
因此可能接受更长 position，却无法在特定 head/dtype/distance 组合上利用它。

#### Principle

Position mechanism 需要同时定义数学语义与 numerical execution contract：

```text
defined position
≠ representable attention score
≠ non-zero softmax weight
≠ effective retrieval
```

#### Mechanism

对 slope `m_h`，线性 bias 随距离增长；超过由 dtype、content logits、slope 与 kernel 决定的阈值
后，softmax numerator 下溢。结果既包括 positional blindness，也包括 denominator 中远端项消失后
的 weight redistribution。若局部窗口是设计目标，依赖 underflow 会先计算 score 再静默归零，
不如显式 sparse/window semantics 可测。

作者在 BLOOM 560M、Falcon-RW 7B、MPT 7B 做 pretrained probes，并训练固定架构、固定语料的
148M decoder，对 clamp、window-targeted slopes、log-scaled distance 与 soft-capped logits 做
比较。Default ALiBi 在其部分 retrieval tests 中仍然很强，log-distance 的改进也没有与所有
mitigation 稳定叠加。

#### Trade-off

- Clamp 或改变 slope 会扩大数值可见范围，也改变局部性归纳偏置。
- Log-distance 与 soft-cap 可以缓解极端 score，却可能改变训练动态和 head specialization。
- 平均 perplexity 对 sparse retrieval failure 不敏感，需要按 head、distance、dtype 与 retrieval
  slice 观察。
- 实验只有 148M training runs、固定 architecture/corpus，作者明确没有证明可推广到更大模型。

#### Connection / Evolution

它修正的是 Ch13 的实现契约，不覆盖 ALiBi：默认方案在训练窗口和经验证 dtype 内仍可成立；
只有当 context、slope 或 precision 变化使 numerical boundary 越过工作区间时，才需要 mitigation
或显式窗口。Ch22 继续拥有“可接受长度、可寻址长度与有效利用长度”的全系统边界。

## Evidence Level

| Evidence | Level | Boundary |
| --- | --- | --- |
| 三篇论文 metadata、v1 history 与完整 HTML | Primary / Experimental | 作者材料，可核验但未 peer review |
| HeteroPanacea component timing + simulator | Experimental System Evidence | 非 cycle-accurate、非端到端 production serving |
| TARL benchmark、ablation、rollout | Experimental Agent Evidence | 构造 ledger/dataset；无 production transaction contract |
| ALiBi analytic underflow + limited probes/training | Experimental Mechanism Evidence | 大模型、更多 dtype/kernel 的外推未验证 |
| 本日报的跨论文演进关系 | Inference | 已与官方事实和作者实验分开表述 |

## 3. AI Infra 与工程项目

### Source Coverage

按固定项目顺序检查官方 Release、Blog、RFC、重要 PR 与 documentation：

- **PyTorch — No Material Update**
- **JAX — No Material Update**
- **CUDA — No Material Update**
- **Triton — No Material Update**
- **vLLM — No Material Update**
- **SGLang — No Material Update**
- **NVIDIA Dynamo — No Material Update**
- **TensorRT-LLM — No Material Update**
- **Ray — No Material Update**
- **KServe — No Material Update**
- **Kubeflow — No Material Update**
- **Kubernetes — No Material Update**
- **Hugging Face Transformers — No Material Update**
- **Hugging Face Accelerate — No Material Update**
- **DeepSpeed — No Material Update**
- **Megatron-LM — No Material Update**
- **Unsloth — No Material Update**
- **MLX — No Material Update**
- **llama.cpp — Record Only**：8 月 5 日 rolling builds 包含测试恢复、OCR batching、MTP
  allocation fix 与 speculative-decoding metrics 等小改动；逐项属于 bugfix/observability，未形成
  新的长期机制或 Books 结论。
- **ONNX Runtime — No Material Update**
- **OpenXLA — No Material Update**

- 除上述 llama.cpp rolling builds 外，未发现窗口内值得单独建立 Books mechanism 的 stable
  release、merged RFC 或兼容性变化。
- Nightly、dependency bump、未合并 PR 与未来 roadmap 日期不作为 release event。
- 版本页面仅用于确认“无 material update”；未把搜索摘要或 planned date 写成当前事实。

### Candidate Scoring

本组无达到候选门槛的窗口内新事件。

## Knowledge Tree Position

| Candidate | Primary Owner | Adjacent Chapters | Relationship |
| --- | --- | --- | --- |
| ALiBi underflow | Ch13 Position Encoding | Ch14 Self Attention、Ch22 Long Context | Refine / numerical contract |
| HeteroPanacea | Ch51 PD 分离 | Ch50 GPU Memory、Ch52 推理调度 | Layering / conditional factorization |
| TARL | Ch73 Memory | Ch72 RAG、Ch74 Tool Calling、Ch77 Workflow | Direct refinement / typed transition |
| TAOT | Ch21 MoE | Ch32 Communication、Ch35～37 | Full review complete 2026-08-13；Refine candidate / Experimental |
| Oilbird | Ch44 Speculative Decoding | Ch41 KV Cache、Ch52 Scheduling | Full review complete 2026-08-13；Refine candidate / Experimental |
| Agentic formal verification | Ch68 Safety | Ch62 Evaluation、Ch77 Workflow | Full review complete 2026-08-13；Refine candidate / Experimental |

## Recommended Action

- 已 refine Ch13：加入 ALiBi 的 formal-definition / finite-precision gap、隐式有效窗口与验证方法。
- 已 refine Ch51：把 P/D→A/F/PDAF 写成条件化 graph factorization，保留 co-location、P/D 与更细
  拆分的共存边界。
- 已 refine Ch73：把 Memory write 从 boolean decision 提升为 typed transition，并明确论文
  transaction 不等于数据库 ACID。
- 2026-W32 结束时，将 HeteroPanacea 与 AFlex 联读，将 TARL 与 MemSecBench/derived-memory
  联读；若没有独立证据，不继续复制 taxonomy 或 benchmark。
- TAOT、Oilbird 与 Agent formal verification 已在 2026-08-13 完成完整 Source Packet 和章节级去重；
  分别为 Ch21、Ch44、Ch68 的 Experimental refine candidates，Books Gate 关闭。

## Books Integration

### Absorbed

- `books/part-02-model/13-position-encoding.md`：补充 ALiBi 有限精度 underflow 与数值验证 contract。
- `books/part-04-inference-system/51-pd-disaggregation.md`：补充 P/D/A/F conditional factorization、
  break-even 与旧拓扑共存条件。
- `books/part-06-agent/73-memory.md`：补充 typed memory actions、ledger state 与 authoritative
  transaction 边界。
- `docs/LEARNING_STATE.md`：同步三项稳定认知与 Experimental evidence boundary。

### Not Absorbed

- **TAOT / Oilbird / Formal Verification**：2026-08-13 已分别核验 topology-aware replica placement、
  verifier-key retrieval drafting 与 bounded/equivariant operational-state verification。作者实验/证明的
  topology、batch、store、formal assumptions 仍受限，故均标记 Experimental，未写 Books。

## Ignored Noise

- 模型榜单、community challenge、partner marketing 与缺少 technical report 的功能 headline。
- arXiv recent 中只增加 benchmark、缺少机制或与 AI System Design 关联弱的条目。
- 缺少 model、hardware、precision、input/output、batch、concurrency 与 SLO contract 的性能宣传。
- GitHub nightly、dependency bump、未合并 PR、未来 roadmap 与搜索引擎重收录。

## Repository Changes

- 新增 `papers/2026/08/06/README.md`。
- Refine Ch13、Ch51、Ch73，并同步 `docs/LEARNING_STATE.md`。
- 未修改 ROADMAP 或 `docs/DECISIONS.md`；未生成 provisional `2026-W32`。
- 运行前已有 Ch11、Ch16、Ch21、Ch22、Ch45、Ch77、Learning State、ADR、interview、8 月 4 日
  与 8 月 5 日 Daily 修改均保留；未执行 stage、unstage、commit、push、reset、checkout 或 clean。

## Recovery Addendum — 2026-08-13

- TAOT：已读 method、OT objective、topology repair、4×8 A800 / Qwen3-30B-A3B experiments、ablation
  与 planner overhead；主 owner Ch21。
- Oilbird：已读 store/retrieve/merge/verify、batch sensitivity、memory/retrieval overhead、privacy 与
  task-dependence；主 owner Ch44。
- Formal Verification：已读 state-transition formalization、FO-CTL、boundedness/equivariance、complexity、
  case study 与适用限制；主 owner Ch68。
- 三项都只更新 Daily/Weekly evidence，不修改 Books。

## Open Questions

1. HeteroPanacea 在公开代码后，component-level model 对 end-to-end batching、queue interference、
   KV/activation overlap 与 tail SLO 的误差是多少？
2. A/F 或 PDAF 新切边的 ownership、cancellation、retry 与 partial-transfer recovery 怎样定义？
3. TARL 的五类 action 在真实 multi-user concurrent store 中是否完备，source reliability 又由谁授权？
4. Typed memory transition 怎样与 CAS/version、delete propagation、derived views 和 crash recovery
   组成真正可重放的 state machine？
5. ALiBi underflow threshold 在 FP32、BF16、FP16、FP8、不同 fused attention kernels 与更大模型
   上如何校准？
6. 显式 window 与数值 mitigation 如何同时比较 retrieval quality、compute saved 与训练稳定性？

## Sources

访问日期均为 2026-08-06；论文日期为 arXiv first-public date。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Google DeepMind: https://deepmind.google/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/
- Apple Machine Learning Research: https://machinelearning.apple.com/
- NVIDIA Research: https://research.nvidia.com/
- Amazon Science: https://www.amazon.science/
- xAI News: https://x.ai/news
- Cohere Labs: https://cohere.com/research
- Ai2 Papers: https://allenai.org/papers
- Mistral AI Research: https://mistral.ai/research
- Alibaba Qwen: https://qwenlm.github.io/
- DeepSeek: https://api-docs.deepseek.com/news/
- Moonshot AI / Kimi: https://www.kimi.com/
- Zhipu AI: https://www.zhipuai.cn/
- MiniMax: https://www.minimaxi.com/news
- ByteDance Seed: https://seed.bytedance.com/
- Baidu ERNIE: https://ernie.baidu.com/blog/zh/publication/
- Tencent Hunyuan: https://github.com/Tencent-Hunyuan
- Huawei Noah's Ark Lab: https://noahlab.com.hk/
- Shanghai AI Laboratory: https://www.shlab.org.cn/
- StepFun Research: https://www.stepfun.com/research
- Xiaomi MiMo: https://mimo.xiaomi.com/
- InclusionAI: https://www.inclusion-ai.org/publication/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Sources

- HeteroPanacea metadata（2026-08-04）: https://arxiv.org/abs/2608.03741
- HeteroPanacea full HTML: https://arxiv.org/html/2608.03741
- TARL metadata（2026-08-04）: https://arxiv.org/abs/2608.03699
- TARL full HTML: https://arxiv.org/html/2608.03699
- ALiBi numerical failure metadata（2026-08-04）: https://arxiv.org/abs/2608.03994
- ALiBi numerical failure full HTML: https://arxiv.org/html/2608.03994
- TAOT metadata（2026-08-04）: https://arxiv.org/abs/2608.03676
- Oilbird metadata（2026-08-04）: https://arxiv.org/abs/2608.03839
- Formal Verification of Agentic Systems metadata（2026-08-04）: https://arxiv.org/abs/2608.03609
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- arXiv cs.IR recent: https://arxiv.org/list/cs.IR/recent
- arXiv stat.ML recent: https://arxiv.org/list/stat.ML/recent
- OpenReview: https://openreview.net/
- TMLR submissions（本次访问失败）: https://openreview.net/submissions?venue=TMLR
- Hugging Face Daily Papers: https://huggingface.co/papers
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- JAX Releases: https://github.com/jax-ml/jax/releases
- CUDA Toolkit Release Notes: https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
- Triton Releases: https://github.com/triton-lang/triton/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
- TensorRT-LLM Releases: https://github.com/NVIDIA/TensorRT-LLM/releases
- Ray Releases: https://github.com/ray-project/ray/releases
- KServe Releases: https://github.com/kserve/kserve/releases
- Kubeflow Releases: https://github.com/kubeflow/community-distribution/releases
- Kubernetes Releases: https://github.com/kubernetes/kubernetes/releases
- Hugging Face Transformers Releases: https://github.com/huggingface/transformers/releases
- Hugging Face Accelerate Releases: https://github.com/huggingface/accelerate/releases
- DeepSpeed Releases: https://github.com/deepspeedai/DeepSpeed/releases
- Megatron-LM Releases: https://github.com/NVIDIA/Megatron-LM/releases
- Unsloth Releases: https://github.com/unslothai/unsloth/releases
- MLX Releases: https://github.com/ml-explore/mlx/releases
- llama.cpp Releases: https://github.com/ggml-org/llama.cpp/releases
- ONNX Runtime Releases: https://github.com/microsoft/onnxruntime/releases
- OpenXLA Releases: https://github.com/openxla/xla/releases
