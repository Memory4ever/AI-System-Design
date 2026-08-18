# Daily Research — 2026-08-18

**Date:** 2026-08-18

**Timezone:** Asia/Shanghai

**Research Window:** 2026-08-16 00:00～2026-08-18 23:59

**Access Date:** 2026-08-18

**Status:** Daily Complete；3 Full Source Reviews Complete；Books Integration Complete；W33 Correction Queue Remains Open

## Executive Summary

今天确认三项能够补足长期 AI System 认知的机制。Rollplex 说明同步 RL post-training 不必以完整 phase 为最小
调度单元：只要 dependency、parameter snapshot 与 commit barrier 保持不变，response-independent prefix 可以
进入 rollout Decode 的空间空隙；真正新增的难题是跨 phase state lifetime、HBM residency 与不同 TP layout 的
共享。FreeBalance 把 MoE placement 的演进从历史静态表、事后迁移推进到“预测只拥有 placement 建议、正常
router 继续拥有语义”的预算内 pre-routing。AgentRewind 则把 Agent 恢复点定义为 Context 与 controlled
environment 的联合状态，明确了 Memory、Workflow authority 与外部副作用不能混为一谈。

三项均完成 primary-source 正文审计并分别进入 Ch36、Ch49、Ch81；正文只保留机制、适用条件、trade-off 与
failure boundary，没有把作者 speedup 写成通用事实。Dynamo v1.4.0 作为官方版本事实保留在 Daily：其跨数据中心
KV relay、reservation replay、多模态 disaggregation 与 simulation surface 值得跟踪，但 release bundle 不是单一
机制证据，本日不据此继续修改 Books。

8 月 17 日重开的 W33 correction queue 属于上周 recall 修复，今天没有把其中 32 项 pending identities 冒充为
8 月 18 日新事件，也没有关闭该 Gate。今天是 Tuesday，不生成 W34 provisional Weekly。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、Meta AI / FAIR、
Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、Qwen、DeepSeek、Kimi、
Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、
InclusionAI 与 Hugging Face Blog 的官方 Research、technical report、model/system card 与发布入口。

没有确认到本窗口内 first-public、同时公开足够长期机制的新模型或机构 Research 事件。产品页面、二次报道、
旧论文 revision 与没有 technical report 的能力声明不进入候选表。

### Candidate Scoring

本组没有 retained candidate。

## 2. arXiv / 学术来源

### Source Coverage

读取 arXiv `cs.AI → cs.CL → cs.LG → cs.DC` recent surface，并用 Google Scholar、OpenAlex、DBLP、
Semantic Scholar 与 Hugging Face 辅助发现和去重；Crossref 留给 Weekly metadata 交叉验证。今天公开可见的
Monday batch 包含 arXiv v1 timestamp 为 8 月 14 日的论文，故表中保留真实 first-public date，并明确记录本日
发现/访问时间，不把展示日改写成论文日期。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence / Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rollplex | 2026-08-14 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Integrate — New Mechanism，Ch36 |
| FreeBalance | 2026-08-14 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Integrate — New Mechanism，Ch49 |
| AgentRewind | 2026-08-14 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Integrate — New Mechanism，Ch81 |

## Deep Analysis 1 — Rollplex：同步语义不要求完整 Phase 串行

### Why → Principle

Text-only on-policy RL 常由 response Decode 主导，把 rollout、reference scoring、actor training 与 update 串行化，
可以用简单 barrier 保证同一 policy snapshot。VLM 的视频/长 Prompt 让 prefix encode/prefill 占比显著提高；
reference 与 training prefix 只依赖输入和 `theta_k`，继续等待 response 完成是调度粒度造成的空转，不是算法依赖。

稳定原则是：**从数据依赖推导重排范围，从 parameter version 与 commit frontier 保持同步语义。**更高 GPU
utilization 本身不是目标，可从关键路径隐藏的独立工作才是。

### Mechanism

Rollplex 把 reference/training invocation 在第一个 response token 边界拆成 prefix 与 suffix：

```text
theta_k read-only
→ rollout decode || reference prefix || training prefix
→ response and prefix boundaries ready
→ reference/training suffix + loss + backward
→ all theta_k readers quiesced
→ chunked optimizer update and theta_(k+1) publication
```

Phase-aware memory manager 按 producer、consumer 与 last-use 决定 HBM residency：保留 boundary KV，释放
phase-local rollout state，offload/recompute training state，并让 FP32 optimizer state 分块流经 HBM。CUDA VMM
保留虚拟地址，IPC 让不同进程映射兼容存储。Training TP=8、rollout TP=4 时，layout-compatible weights 使用
同一 physical backing；transpose-compatible layout 用 metadata view，只有不兼容 tensors 才重建。

### Evaluation Contract

- Model：Qwen2.5-VL-32B；GRPO，每 Prompt 8 个 responses。
- Hardware：32×H800，四节点；每节点 1.4 TB host memory、400 Gbps InfiniBand；部分策略实验使用 H20。
- Software：Megatron-Core 0.13.0、vLLM 0.17.0、ROLL、CUDA MPS/VMM/IPC。
- Workload：CLEVRER、PerceptionTest、LLaVA-Video-178K、STAR；rollout batch 32；最大 10K tokens，最多
  8K Prompt / 2K response。
- Precision：actor/reference weights BF16；optimizer state FP32；其他未披露 numeric details 为 `Not Disclosed`。
- Measurement：丢弃首个 warmup iteration，报告其余 step time 平均；concurrency 与 production SLO 未披露。

作者报告相对 serial colocation 为 `1.23×～1.30×`，相对同 32-GPU budget 的 disaggregation 为
`1.57×～2.24×`；这些数字只属于上述 contract。Memory ablation 中移除关键策略会 OOM，且 92.8% weights
可共享 physical storage；reward curve 相近只能支持训练行为没有明显系统性偏移，不是严格 trajectory equality。

### Trade-off / Connection / Evolution

重叠会增加 SM/HBM interference、state lifetime、host traffic、page mapping、IPC alias 与 failure recovery；Decode
被拖慢可能抵消 prefix overlap。Input 较短、独立 GPU pool 足够、offload 很慢或 layout 不兼容时，原 serial
colocation / disaggregation 仍合理。

演进关系为 `Direct Evolution`：phase-serial synchronous RL → dependency-split synchronous overlap；与
asynchronous rollout 是 `Alternative Branch`，后者会改变 freshness/selection contract。Owner 为
`TRAIN-DISTRIBUTED-TRAINING`（Ch36），Ch35/37 只提供 checkpoint 与 TP layout 前置知识。

## Deep Analysis 2 — FreeBalance：预测可以提前 Placement，不能提前模型语义

### Why → Principle

Offline expert placement 在 task mixture 稳定时成本最低，但面对逐 batch workload shift 会变 stale。Reactive
migration 等到 target router 得到准确 assignments 后才搬 weights，语义稳健，却把 migration 暴露在当前层关键
路径。真正缺少的是一个足够早、只拥有 execution hint 而不拥有模型决策的信号。

### Mechanism

FreeBalance 在目标层 Attention 前，用上一层 residual hidden state `h_(l-1)` 调用同一个 frozen target router，
汇总 predicted expert counts；正常 router 之后仍在 `H_l` 上运行，独占最终 token-to-expert assignment：

```text
h_(l-1)
→ early router invocation and predicted counts
→ deterministic heavy-to-light pair swaps
→ weight migration overlapped with target attention
→ normal router emits exact assignments
→ lossless dispatch / expert compute / combine
```

Planner 只交换 compact global counts，各 ranks 用确定性 order 重建相同 plan。每个 link/rank 的 swap 数量受
`attention window - safety margin` 约束；预测错了不会改变模型输出，但可能产生负收益或暴露 migration tail。

### Evaluation Contract

- Models：Qwen3-30B-A3B-Instruct-2507（128 experts、Top-8、9 MB/expert）与
  Moonlight-16B-A3B-Instruct（64 experts、Top-6、16.5 MB/expert）。
- Hardware：单节点 8×A800-SXM4 NVLink，EP=8。
- Workload：19 个 LongBench subsets 与 changing-subset mixed workload；默认 batch 16、input 8K，Prefill only。
- Baselines：fixed placement Vanilla、history-driven EPLB，分别与/不与 FreeBalance 组合；EPLB profile 为
  21 subsets × 20 samples。
- Measurement：一次 warmup、三次 measured runs 取平均；precision、concurrency、tail SLO、power 为
  `Not Disclosed`。

作者报告 max/mean rank-load ratio 最多下降 32.8%、end-to-end Prefill latency 平均下降 13.1%，以及平均可隐藏
5.1 个 experts/layer 的迁移；这些结论没有覆盖跨节点 fabric、Decode、continuous batching 或迁移失败。

### Trade-off / Connection / Evolution

新增成本包括第二次 router invocation、prediction error、planning、weight movement、placement version、partial
transfer、跨 batch thrashing 与 rollback。稳定任务仍优先 offline placement；短 Attention window、弱互联或
预测不稳时 reactive/no migration 更好。

演进关系为 `Direct Evolution`：offline placement → reactive post-route migration → budgeted predictive
pre-route migration。`MODEL-MOE` 继续拥有 router 语义，`INFER-TENSORRT-LLM`（Ch49）拥有 routing result 到
physical data movement / kernel plan 的映射。

## Deep Analysis 3 — AgentRewind：恢复点必须同时恢复“模型相信的世界”和真实受控状态

### Why → Principle

长程 Agent 在错误后只追加修复动作，可能无法消除早期错误的累积影响。Restart + summary 能清理污染，却会
重做可信前缀。只恢复 Context 或只恢复 workspace 都会产生 split-brain：模型与环境对已发生事实的理解不同。

### Mechanism

AgentRewind 在每个 LLM decision boundary 保存 `d_t=(c_t,s_t)` 与 segment metadata。Agent 可提出旧 checkpoint
并生成 failed-attempt memory；Runtime 同时恢复 Context 和 controlled workspace，把 retained prefix 从 event log
恢复而不是重新执行，然后注入累计 rewind memory，生成新 suffix。

实现以外部 bare Git repository 管理 workspace snapshots，避免改写 task repository 的 `.git`。恢复边界主要是
workspace files；network calls、外部 services、workspace 外 processes、empty directories 与部分 permission bits
并不由该 snapshot 完整撤销。

### Evaluation Contract

- Benchmark：MettleBench，82 个真实工程资源派生任务、640 个 ordered deterministic criteria；任务本身都有
  forward-only solution，不要求使用 rewind。
- Main setup：GPT-5.4、mini-SWE-agent；Continue、Restart with Experiences、Safety Review、AgentRewind；
  三次 runs。论文还覆盖其他 base models 与 harnesses。
- Recovery comparison：从同一 failed endpoint 开始的 50 paired trials。
- Limits：最多展示 80 个 checkpoint candidates，rewinds unlimited；无 step/wall-clock/shell timeout，model request
  timeout 600s；temperature 0.0。
- Hardware、token cost、storage overhead、并发、production SLO 为 `Not Disclosed`。

作者实验支持联合 rewind 在该受控 benchmark 提高 task success/checklist progress，并通过 context rollback、
environment rollback 与 rewind memory ablation 分离组件价值；它没有证明开放网络、并发协作者、不可逆 Tool 或
exactly-once external side effects 可被回滚。

### Trade-off / Connection / Evolution

Checkpoint 太密增加 storage/selection cost，太疏会重复工作；Agent 选择 checkpoint 与总结失败也可能出错。
外部副作用仍需 idempotency、compensation、reconciliation 和 pre-action approval。Forward repair 在局部、可补偿
错误中继续合理；Restart 在状态无法可信快照时仍是安全分支。

演进关系为 `Direct Evolution`：forward-only correction → restart with failure experience → aligned
context/environment rewind → future transactional/compensating recovery。Owner 为 `AGENT-WORKFLOW`（Ch81）；
`AGENT-MEMORY` 只拥有失败证据，不能拥有环境恢复 authority。

## 3. AI Infra 与工程项目

### Source Coverage

检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、
Transformers、Accelerate、DeepSpeed、Megatron-LM、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的官方
Release、RFC、PR、文档和代码入口。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence / Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| NVIDIA Dynamo v1.4.0 | 2026-08-15 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | E3；Weekly Only — Version Fact / bundled mechanisms |

### Dynamo v1.4.0 Source Review

官方 release 于 8 月 15 日 22:13 发布，包含 640 merged PRs。可验证的版本事实包括：experimental multi-DC
prefix routing、sequenced KV relay、reservation replay、endpoint-scoped event transport、cache-salt-aware tenant
isolation、跨 Router replicas 的 session affinity；vLLM-Omni 获得 NIXL RDMA multi-node disaggregation；Spica
simulation 进入仓库，并可把 production traces 转为 simulation artifacts。

这些内容分别关联 `INFER-DISTRIBUTED`、`INFER-DYNAMO`、`PLATFORM-EVALUATION-SYSTEM` 与多模态 Serving，
但 release note 把多个独立机制打成一个版本包。今天没有逐个 PR/代码路径完成与现有章节的 source-family 去重，
因此固定 disposition 为 `Weekly Only — Version Fact / Mechanism Review Deferred`。Release 中 throughput 数字没有
写入 Books；它的 model、hardware、trace、concurrency、precision 与 SLO contract 不完整，不能外推。

## Evidence Level and Claim Boundary

- **E2 / Primary paper:** 三篇论文均覆盖 metadata/revision、Introduction/Related Work、Method/公式、Implementation、
  Evaluation、baseline/ablation/sensitivity、limitations 与关键 Appendix；只有作者实验，尚无独立复现。
- **E3 / Official release:** Dynamo 内容只确认版本、公开功能和 PR links；没有从产品能力反推内部实现。
- **Discovery/index:** Scholar、OpenAlex、DBLP、Semantic Scholar、Hugging Face 与搜索排序只负责 discovery/identity，
  不承担机制结论。
- **Project inference:** Stable owner、演进关系与 Books disposition 来自 primary source 和目标/相邻章节联读，
  不是论文作者声明。
- 所有未披露的 model、hardware、precision、length、batch、concurrency、SLO、evaluator 和 fault contract 均写为
  `Not Disclosed`，不补猜。

## Knowledge Tree Position

| Candidate | Stable Owner | Current / Legacy | Adjacent Chapters Read | Decision |
| --- | --- | --- | --- | --- |
| Rollplex | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Ch35、Ch36、Ch37 | Integrate — New Mechanism |
| FreeBalance | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | Ch21、Ch49、Ch56 | Integrate — New Mechanism |
| AgentRewind | `AGENT-WORKFLOW` | Ch81 / Ch77 | Ch77、Ch81、Ch84 | Integrate — New Mechanism |
| Dynamo v1.4.0 | `INFER-DYNAMO` / `INFER-DISTRIBUTED` | Ch52 / Ch48 | Ch51、Ch52、Ch56 | Weekly Only — Version Fact |

## Recommended Action

- 已将 Rollplex 的 dependency-driven cross-phase schedule 写入 Ch36；保留 serial/disaggregated 与 asynchronous
  分支的成立条件。
- 已将 FreeBalance 写入 Ch49 的 MoE execution-plan 演进链；router 语义仍归 Ch21，placement 才归 Runtime。
- 已将 AgentRewind 写入 Ch81；Memory 只保存失败证据，Workflow Runtime 拥有联合恢复与 commit authority。
- Dynamo v1.4.0 等 Sunday Weekly 再逐 source family 去重；未完成 PR/代码审计前不继续写入 Books。
- W33 correction queue 继续保持 Open；今天的三篇新论文不用于掩盖或关闭旧 queue。

## Ignored Noise

- KV Cache Compression Through Transform Coding（arXiv:2608.14191）只完成 metadata/abstract identity；arXiv HTML
  本日返回内部错误，未以摘要代替全文，不计为 retained candidate。
- Monday recent-page 展示时间不取代 arXiv v1 date；cross-list/revision 不重复计分。
- 旧 release、营销 benchmark、社区转述、未披露 workload contract 的 headline 与框架功能清单。
- W33 的 32 项 Discovery Review Pending 属于另一个 correction ledger，不混入本日评分。

## Repository Changes

- 新增 `papers/2026/08/18/README.md`。
- Refine Ch36 `TRAIN-DISTRIBUTED-TRAINING`：加入 synchronous RL dependency-driven phase reordering、HBM state
  lifetime、snapshot/TP layout sharing 与 coexistence boundary。
- Refine Ch49 `INFER-TENSORRT-LLM`：加入 offline → reactive → predictive pre-routing expert placement 演进。
- Refine Ch81 `AGENT-WORKFLOW`：加入 aligned Context/environment checkpoint 与 external side-effect boundary。
- 更新 `docs/LEARNING_STATE.md` 的 Live Daily checkpoint；ROADMAP、DECISIONS 与 7 Part / 84 章结构不变。
- 未 stage、unstage、commit、push、reset、checkout 或 clean。

## Open Questions

1. Rollplex 的 barrier、VMM mapping 和 shared actor snapshot 在 rank/process failure 后怎样恢复且不暴露 torn version？
2. FreeBalance 在跨节点、continuous batching 与 Decode 中，prediction benefit 是否仍大于 weight migration 和
   placement churn？
3. AgentRewind 怎样把 network/service/process side effects 纳入 transaction、compensation 或 reconciliation，而不
   让 Agent 自己拥有恢复 authority？
4. Dynamo v1.4.0 的 multi-DC KV relay 怎样定义 event ordering、partition recovery、tenant salt 与 reservation expiry？
5. KV transform coding 在 HTML/PDF 可完整读取后，是否形成 Ch44/54 的新 compression–compute–error contract？

## Sources

- arXiv cs.AI recent（访问 2026-08-18）: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent（访问 2026-08-18）: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent（访问 2026-08-18）: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent（访问 2026-08-18）: https://arxiv.org/list/cs.DC/recent
- Rollplex, arXiv:2608.14498v1（first-public 2026-08-14；访问 2026-08-18）:
  https://arxiv.org/html/2608.14498v1
- FreeBalance, arXiv:2608.14205v1（first-public 2026-08-14；访问 2026-08-18）:
  https://arxiv.org/html/2608.14205v1
- AgentRewind, arXiv:2608.14380v1（first-public 2026-08-14；访问 2026-08-18）:
  https://arxiv.org/pdf/2608.14380v1
- NVIDIA Dynamo v1.4.0（released 2026-08-15 22:13；访问 2026-08-18）:
  https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.0
- KV Cache Compression Through Transform Coding, arXiv:2608.14191v1（identity only；访问 2026-08-18）:
  https://arxiv.org/abs/2608.14191
- OpenAI Research（访问 2026-08-18）: https://openai.com/research/
- Anthropic Research（访问 2026-08-18）: https://www.anthropic.com/research
- Google DeepMind publications（访问 2026-08-18）: https://deepmind.google/research/publications/
- Hugging Face Blog（访问 2026-08-18）: https://huggingface.co/blog
- vLLM releases（访问 2026-08-18）: https://github.com/vllm-project/vllm/releases
- SGLang releases（访问 2026-08-18）: https://github.com/sgl-project/sglang/releases
- KServe releases（访问 2026-08-18）: https://github.com/kserve/kserve/releases
