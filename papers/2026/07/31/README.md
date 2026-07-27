# AI Research Daily — 2026-07-31

> Research window: 2026-07-29 至 2026-07-31（重点核验过去 24～48小时）
>
> Accessed: 2026-07-31（Asia/Shanghai）
>
> Scope: 官方 Research / Blog / model card、primary research papers、官方工程文档、
> RFC、重要 PR 与 GitHub Releases。
>
> Organization: 模型与研究机构 → arXiv 论文 → AI Infra 与工程项目

## Executive Summary

本轮没有发现过去 24～48小时内、足以改变本书模型或 AI Infra 设计结论的一线机构正式
研究发布。长期信号集中在 7 月 29 日提交的三篇系统相关预印本：

1. **InferScale** 把持久用户 memory 从“每次重新拼进 prompt”改写为“检索后注入可复用
   KV state”。它揭示了一个长期设计空间：外部知识不一定只通过 token layer 进入模型，
   也可能通过 attention state layer 进入；但 position、encoding context、cache
   compatibility 与离线构建成本会成为新的正确性边界。该论文使用 vLLM `v0.19.1`
   和单卡实验，尚无独立复现，因此只保留在 Daily。
2. **MemSecBench** 将 Agent memory poisoning 拆成
   persistence → recall → adoption → external consequence → selective repair。稳定价值是：
   memory security 不能只测“恶意内容是否写入”，修复也不能只测“是否删除恶意内容”，
   还要验证 benign state 是否被保留。该生命周期与 selective-repair 原则已吸收到
   第 73 章；不复制单篇 benchmark 数字或 backend 排名。
3. **Revisiting Lossy Verification in Speculative Decoding** 明确了 runtime optimization
   的语义边界：经典 acceptance 与 residual sampling 保持 target distribution；
   放宽 verification 则是在改变 sampling contract，不能仍以“纯加速”描述。对于
   truncation-based verification，比较基线必须是相同 truncation policy 下的 target
   sampling。该长期原则已局部吸收到第 44 章。

另保留 **Filesystem-Based Memory for LLM Agents** 作为 Worth Watching：文件组织在大规模
材料上主要降低 search cost，却未自动改善 answer quality，并会随增长退化。这一结果与
本项目的文件化知识库实践相关，但仍是单篇研究，尚不足以改写第 73 章。

本次没有推翻已有结论，只把一个边界变得更精确：**lossless speculative decoding 是
保持输出分布的 execution optimization；lossy verification 是显式的 decoding-policy
变化，必须同时承担质量、校准和 matched-baseline 证据责任。**

## Candidate Scoring

评分维度均为 `0～5`：Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、
Source Reliability（SR）、Project Relevance（PR）、Longevity（L）。

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| InferScale：GPU-native KV injection | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Must Read；Daily only |
| MemSecBench：memory poisoning lifecycle | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Must Read；吸收进第 73 章 |
| Lossy verification：sampling contract 边界 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；吸收进第 44 章 |
| Filesystem-Based Memory for LLM Agents | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Worth Watching；Daily only |

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查官方 Research/Publications、技术 Blog、model/system card、官方
GitHub/Hugging Face organization 与 technical report，并与最近 7 天日报去重。

| Institution | Window result | Decision |
| --- | --- | --- |
| OpenAI | 官方 Research 无窗口内新条目；7 月 27 日内容已在旧日报处理 | Deduplicated |
| Anthropic | 官方 Research 最新条目超出窗口 | No Material Update |
| Apple Machine Learning Research | 官方 Research / Highlights 无窗口内新条目 | No Material Update |
| Google DeepMind | Publications 无窗口内新条目 | No Material Update |
| Google Research | Research Blog 无窗口内新条目 | No Material Update |
| Meta AI / FAIR | 无达到门槛的一手研究更新 | No Material Update |
| Microsoft Research | 无达到门槛的一手研究更新 | No Material Update |
| NVIDIA Research | 无窗口内正式研究发布 | No Material Update |
| xAI | 官方 News / model entry 无窗口内研究更新 | No Material Update |
| Amazon Science / AGI | 无达到门槛的一手研究更新 | No Material Update |
| Cohere Labs | 无窗口内正式研究更新 | No Material Update |
| Ai2 | 无窗口内正式研究更新 | No Material Update |
| Mistral AI | 无窗口内正式研究更新 | No Material Update |
| Alibaba Qwen | 最新可发现正式条目超出窗口 | No Material Update |
| DeepSeek | 官方入口无窗口内正式研究更新 | No Material Update |
| Moonshot AI / Kimi | Kimi K3 已在 7 月 29 日日报处理 | Deduplicated |
| Zhipu AI | 无达到门槛的一手研究更新 | No Material Update |
| MiniMax | 官方 News 无窗口内技术研究更新 | No Material Update |
| ByteDance Seed / Research | 无达到门槛的一手研究更新 | No Material Update |
| Baidu ERNIE | 无窗口内正式研究更新；lossy verification 论文在 arXiv 组处理 | No Material Update |
| Tencent Hunyuan | 无窗口内正式模型/系统研究更新 | No Material Update |
| Huawei Noah's Ark Lab / Pangu | 无达到门槛的一手研究更新 | No Material Update |
| Shanghai AI Laboratory / InternLM | 无达到门槛的一手研究更新 | No Material Update |
| StepFun | 无窗口内正式研究更新 | No Material Update |
| Xiaomi MiMo | 无达到门槛的一手研究更新 | No Material Update |
| InclusionAI / Ant Group | 发现近期 Hub activity，但缺少可核验的正式发布说明 | 尚未验证 |
| Hugging Face Blog | 窗口内可发现内容以社区/应用文章为主，无新的高信号一手机制 | No Material Update |

### Evidence Level

- **官方事实**：日期和页面状态来自各机构官方入口。
- **尚未验证**：部分机构缺少稳定的按日期索引；“No Material Update”只表示本轮在公开
  官方入口中未识别到达到门槛的内容，不证明机构不存在未索引发布。
- **Recommended Action**：不修改模型章节，不以 Hub activity 替代 model card、
  technical report 或正式 release。

## 2. arXiv 论文

### Source Coverage

按顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML` recent，
并按系统主题补充 `cs.CR`、`cs.SE`、`cs.AR`。OpenReview / TMLR 未发现窗口内、状态明确
且比下列论文更相关的 Accepted 项。

Hugging Face Daily Papers 用于 discovery；Semantic Scholar、Google Scholar、OpenAlex
与 DBLP 用于 metadata、related-work 与去重检查。下列新预印本尚未在所有索引中形成稳定
的独立 metadata match，最终标题、作者、日期与版本均回到 arXiv 原文核验。Crossref
仅用于 Weekly 或 metadata 冲突；本轮没有 DOI、venue 或 version 冲突，不触发。

### InferScale — Must Read：Memory 从 Token Injection 走向 Attention-State Injection

- Source: primary research paper / arXiv
- Submitted: 2026-07-29 16:18:22 UTC
- Accessed: 2026-07-31
- URL: https://arxiv.org/abs/2607.27090
- Score: 27/30
- Status: Experimental
- Category: Personalized Serving / KV Cache / Agent Memory

#### Why

传统 memory system 先检索历史 facts，再把文本重新放进 prompt。即使同一用户的 facts
跨请求复用，模型仍要重复 Prefill；retrieval budget 越大，TTFT 越容易随注入 token
增长。问题的本质不是“能否检索”，而是“已经计算过且仍然兼容的模型状态能否复用”。

#### Principle

外部知识可以在不同 representation boundary 注入：

```text
text / token injection
→ model recomputes K/V

attention-state injection
→ system reuses compatible K/V
```

后者把计算复用前移，但复用成立必须证明 model revision、layer layout、dtype、position
semantics 与 encoding context 兼容。KV bytes 相同不代表语义可组合。

#### Mechanism

InferScale 离线为每个 memory fact 计算 pre-RoPE KV，并与 semantic embedding 一起保存
在 GPU。请求到来后先检索 facts，再通过 Chunked RoPE 按 serving-time position 旋转 key，
由 vLLM KV connector 把 K/V scatter 到 paged slots；scheduler 为这些 externally
available tokens 分配 blocks，却只让 model Prefill query tokens。

固定组合上下文下的 KV 注入可保持对应 forward state；但把 facts 独立编码会丢失
cross-fact context。论文用 Context-Window Encoding 在离线阶段带入少量前序 context，
只缓存目标 fact 的 KV。这个 accuracy/space/preprocessing knob 是近似，不应描述为普遍
等价于 joint Prefill。

#### Trade-off

- 避免重复 Prefill，但把容量压力移到持久 KV store；论文报告单 conversation 可能需要
  `1.8～4.8 GB`，不能忽略 admission、eviction 与 multi-tenant isolation。
- GPU-resident retrieval 和 KV injection 降低数据移动，却占用原本用于 weights、active
  KV 和 workspace 的 HBM。
- Independent encoding 可组合、易缓存，却牺牲跨 fact interaction；扩大 context window
  提高质量，也增加离线编码时间和存储。
- Position remapping 解决 RoPE placement，不自动解决 model revision、adapter、
  quantization、tokenizer 或 cache-layout compatibility。

#### Connection

```text
第 39、41、43 章 Prefill / KV / PagedAttention
→ 第 46 章 external KV connector and cache identity
→ 第 50、51 章 HBM budget / state transfer
→ 第 73 章 Agent Memory read policy
```

#### Evolution

prompt text injection
→ prefix caching
→ externally loaded KV
→ semantic retrieval + dynamically composed KV
→ future identity-aware, tiered and revocable attention-state service

#### Evidence Level

**论文实验结论**：作者在单张 NVIDIA RTX PRO 6000 Blackwell Server Edition
（96 GB GDDR7、1597 GB/s peak bandwidth、PCIe 5.0 x16 64 GB/s peak read）上，
使用 vLLM `v0.19.1`、BF16 KV、16-token page、prefix caching，以及
Llama-3.1-8B-Instruct、Mistral-7B-Instruct-v0.3、Qwen2.5-7B-Instruct 和 LoCoMo。
在 `k=50` 时，作者报告 TTFT 降低 `72%～79%`（`3.6～4.8×`）、accuracy
`60.3%` 对 Mem0 `63.3%`、并发负载 throughput `3.7～4.5×`。这些数字还排除了
fact extraction、embedding、KV encoding、index build 与 engine startup 等离线成本，
且摘要未形成完整生产 SLO，不能外推为通用收益。

**尚未验证**：独立复现、当前 vLLM 版本兼容、adapter/quantization 组合、模型升级后的
invalidation、跨租户隔离、动态写入与删除、长时间运行下的 HBM pressure。

#### Knowledge Tree Position

主位置为 Part IV 第 41、43、46、50 章；语义 read/write policy 仍属于 Part VI 第 73 章。

#### Recommended Action

Daily only。它提供了重要演化方向，但当前证据来自单篇预印本和旧于仓库当前观察版本的
vLLM 实现；等待独立复现、cache-identity 说明或主流 runtime 稳定支持后再判断书稿。

### MemSecBench — Must Read：Memory Security 是完整生命周期

- Source: primary research paper / arXiv
- Submitted: 2026-07-29 16:06:54 UTC
- Accessed: 2026-07-31
- URL: https://arxiv.org/abs/2607.27080
- Score: 26/30
- Status: Experimental
- Category: Agent Memory / Security Evaluation / Recovery

#### Why

只检查恶意文本是否被 memory store 接受，会把 persistence 当成 harm。真正风险需要它在
未来任务中被 recall、被 Agent adoption，并形成外部后果；恢复同样不能只删除恶意
semantics，还要避免把 benign memory 一并破坏。

#### Principle

Memory security 应沿同一攻击语义追踪：

```text
write
→ persistence
→ recall
→ adoption
→ external consequence
→ selective repair
```

每个阶段有不同 denominator 与控制点。Write 成功不是 authorization bypass 的充分证据，
而 repair target removal 也不是安全恢复的充分证据。

#### Mechanism

MemSecBench 使用 Write–Execute–Forget protocol，在隔离 runtime 中设置 deterministic
write checks、checkpoint-specific judge evaluation 与 programmatic gates。实验把
agent harness、memory backend 和 LLM backend 组成精确 configuration identity，并分别
报告 MPSR、条件化的 MESR、全链路 E2E-ASR 与同时保留 benign state 的 SRSR。

#### Trade-off

- 生命周期 checkpoint 增强可诊断性，但测试成本高于单次 retrieval/attack success。
- Judge model 可覆盖语义变化，却引入 evaluator dependency；programmatic gate 更稳定，
  但只能覆盖可形式化后果。
- Selective repair 比整体清空更符合生产恢复，却需要 provenance、dependency 和
  supersession 信息。
- 条件指标能定位阶段，跨配置比较时也更容易因 denominator 不同而误读。

#### Connection

```text
第 68 章 platform security and evidence
→ 第 73 章 Memory write/read/forgetting
→ 第 74、77 章 action and workflow consequence
→ 第 62、80 章 lifecycle evaluation
```

#### Evolution

retrieval accuracy
→ poisoning persistence
→ downstream exploitation
→ external consequence
→ selective, evidence-preserving repair

#### Evidence Level

**论文实验结论**：作者使用 310 cases、48 contexts、24 configurations
（2 harnesses × 4 memory backends × 3 LLM backends），报告 configuration macro
average：persistence `84.2%`、recall `76.1%`、adoption `53.7%`、E2E `50.3%`；
在成功 poisoning 的条件下 SRSR 为 `56.1%`。每个 configuration–case pair 只运行一次，
结果是 descriptive，不支持因果归因；MESR/SRSR 的 denominator 还随成功 write 数变化。

**尚未验证**：独立复现、judge sensitivity、真实权限系统、访问获取、不同 tool
side effect、长期多轮自然 memory growth，以及修复对 derived summaries / indexes /
backups 的传播。

#### Knowledge Tree Position

主位置为 Part VI 第 73 章 Memory；安全控制连接 Part V 第 68 章和 Part VI 第 77、80 章。

#### Recommended Action

已 refine 第 73 章，补全 persistence → recall → adoption → external consequence →
selective repair 的评估链，并明确 successful repair 必须同时移除恶意语义与保留必要
benign state。只沉淀生命周期和恢复原则；论文的 configuration-level rates、backend
差异与 judge 结论仍留在 Daily。

### Revisiting Lossy Verification — Must Read：Verification 是 Sampling Contract

- Source: primary research paper / arXiv
- Submitted: 2026-07-29 08:54:27 UTC
- Accessed: 2026-07-31
- URL: https://arxiv.org/abs/2607.26627
- Score: 25/30
- Status: Experimental
- Category: Speculative Decoding / Sampling / Evaluation

#### Why

经典 speculative decoding 的价值不只是多接受 tokens，而是在减少 target serial steps
时保持 target distribution。若为了 acceptance 或 block efficiency 放宽 verification，
输出分布会改变。此时系统优化已经跨过 semantics boundary，不能继续只报告 speedup。

#### Principle

```text
lossless verification:
execution changes, target distribution unchanged

lossy verification:
sampling policy changes, quality contract must be redefined
```

因此评估必须比较相同 decoding policy。若方法内含 min-p 或 eta truncation，正确基线是
target model 在相同 truncation policy 下的 sampling，而不是未截断 target；否则会把
truncation 自身效果误归因于 verification。

#### Mechanism

经典算法对 draft token `x` 使用：

```text
h(x) = min(1, p(x) / q(x))
```

拒绝后从 `normalize((p - min(p,q))_+)` 采样，从而恢复 target distribution `p`。
论文把 lossy 方法归纳为两类：truncation-based verification 接受 allowed set 内的
draft tokens，实际更接近被截断的 draft distribution；collaborative verification 则
混合或重塑 `p` 与 `q`。论文实验进一步指出，draft probability 相对 target 的
overshoot 是 collaborative path 的关键风险变量；该经验结论仍需跨模型验证。

#### Trade-off

- Lossless path 保留分布契约，但 acceptance 上界可能限制进一步加速。
- Lossy path 可能提高 accepted progress，却引入 task-dependent quality loss 和新的
  calibration lifecycle。
- Block efficiency 是机制指标，不是质量或端到端 goodput；必须与 task quality、TPOT、
  draft/verification cost 和 SLO 一起报告。
- Matched baseline 提高因果解释力，但需要完整记录 temperature、top-p/min-p/eta、
  tokenizer、model pair 与 verification implementation。

#### Connection

```text
第 18 章 sampling distribution
→ 第 40 章 Decode semantics
→ 第 44 章 Speculative Decoding
→ 第 52、62 章 scheduling goodput / Evaluation
```

#### Evolution

exact speculative sampling
→ multi-candidate / tree drafting
→ relaxed verification for more accepted progress
→ explicit speed–quality contract and matched-policy evaluation

#### Evidence Level

**论文实验结论**：标准 SD 使用
Qwen2.5-72B-Instruct-GPTQ-Int8 target 与
Qwen2.5-0.5B-Instruct-GPTQ-Int8 draft；EAGLE-3 使用
Llama-3.1-8B-Instruct 和官方 drafter。Figure 1 使用单张 H200 140 GB，EAGLE-3
实验使用单张 A6000 48 GB，其余实验使用 2×A100 80 GB。作者报告从 GSM8K 到 AIME，
matched-baseline accuracy gap 从 `0.38` percentage points 扩大到 `6.67`；在其四任务
汇总中，EAGLE-3 将 SpecCascade 与 typical acceptance 的平均 deficit 分别放大约
`4×` 与 `20×`。这些是固定 model pair、quantization、task 和 hyperparameter sweep
下的作者结果；没有输入/输出长度、并发与 serving SLO，不能外推为生产性能结论。

**跨来源工程推断**：无论具体 taxonomy 是否被后续研究保留，“放宽 exact acceptance
即改变 sampling semantics，必须使用 matched-policy baseline”来自定义本身，是比单篇
benchmark 更稳定的系统边界。

**尚未验证**：overshoot 结论对其他模型家族、draft-target ratio、sampling regime、
reasoning workload 和生产 batch 的泛化。

#### Knowledge Tree Position

主位置为 Part IV 第 44 章；采样语义回连第 18 章，服务评估连接第 52、62 章。

#### Recommended Action

已 refine 第 44 章，增加 lossless / lossy verification 的 distribution contract 与
matched-policy baseline。书稿不复制作者 taxonomy 的全部方法清单，也不写入 benchmark
headline；taxonomy 与 overshoot 结论保留 `Status: Experimental`。

### Filesystem-Based Memory for LLM Agents — Worth Watching

- Source: primary research paper / arXiv
- Submitted: 2026-07-29 08:59:43 UTC
- Accessed: 2026-07-31
- URL: https://arxiv.org/abs/2607.26637
- Score: 23/30
- Status: Experimental

论文把单一 memory filesystem 分成 management、search、execution 三个角色，并比较
agent-organized hierarchy、verbatim dump、chunk retrieval、tool harness 与不同模型。
作者报告大规模 material 下，组织化 store 大致把 retrieval cost 减半；但未观察到
organization 本身改善 answer quality，且除最强 manager 外，目录组织会随增长退化；
tool set 对 store shape 的影响可与更换模型同量级。

这提示文件不是中性存储介质：tool affordance、maintenance budget、source citation、
conflict/expiry policy 共同决定 memory quality。现有第 73 章已经覆盖 consolidation、
forgetting、provenance 与 derived summary；当前先保留 Daily，等待独立复现或真实长期
repository/agent workload 证据。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查官方 Releases、Release Notes、文档、RFC 与重要 PR，并与 7 月 27～30 日
日报去重。

| Project | Window result | Decision |
| --- | --- | --- |
| PyTorch | latest stable `v2.13.0` 发布于 7 月 8 日 | Outside Window |
| JAX | 无窗口内高信号正式 release | No Material Update |
| CUDA | 无窗口内高信号正式 release | No Material Update |
| Triton | latest stable release 超出窗口 | No Material Update |
| vLLM | `v0.26.0` 发布于 7 月 27 日，已在 7 月 29 日日报与第 46 章处理 | Deduplicated |
| SGLang | 无需覆盖最近日报的新稳定机制 | No Material Update |
| NVIDIA Dynamo | 7 月 27 日 Kimi K3 experimental build 已在 7 月 29 日记录 | Deduplicated |
| TensorRT-LLM | 无窗口内高信号正式 release | No Material Update |
| Ray | 无窗口内高信号正式 release | No Material Update |
| KServe | 无窗口内高信号正式 release | No Material Update |
| Kubeflow | 无窗口内高信号正式 release | No Material Update |
| Kubernetes | 无窗口内与 AI System 直接相关的高信号 release/RFC | No Material Update |
| Hugging Face Transformers | 无窗口内高信号正式 release | No Material Update |
| Hugging Face Accelerate | 无窗口内高信号正式 release | No Material Update |
| DeepSpeed | 无窗口内高信号正式 release | No Material Update |
| Megatron-LM | 无窗口内高信号正式 release | No Material Update |
| Unsloth | 无窗口内高信号正式 release | No Material Update |
| MLX | 无窗口内高信号正式 release | No Material Update |
| llama.cpp | continuous build / 局部 commits 缺少稳定机制边界 | Ignored Noise |
| ONNX Runtime | 无窗口内高信号正式 release | No Material Update |
| OpenXLA | 无窗口内高信号正式 release | No Material Update |

### Evidence Level

- **官方事实**：release status 与发布日期来自项目官方 GitHub Releases / 文档。
- **社区观点**：本轮未使用 issue 评论、社交媒体或转载作为结论证据。
- **自己的推断**：连续构建和零散 PR 若没有明确 compatibility、correctness 或长期机制
  变化，不聚合成“趋势”。
- **Recommended Action**：不重复吸收 vLLM `v0.26.0`；不为制造 diff 更新 Infra 章节。

## Ignored Noise

- 模型发布转载、聚合站排名与没有 model/system card 的 benchmark headline。
- 把旧论文重新包装为“今日更新”的内容。
- 缺少模型 revision、硬件、输入/输出长度、并发、precision/quantization 与 SLO 的
  performance claim。
- GitHub continuous build、局部 bugfix 和未合并 PR；除非它修正 correctness/security
  结论或形成清晰机制演化链。
- InclusionAI Hub activity：尚未找到可稳定引用的正式发布说明或完整 model card。
- 新预印本的索引缺失：Google Scholar、Semantic Scholar、OpenAlex 或 DBLP 暂无稳定
  metadata 不等于论文无效，也不能充当独立复现。

## Repository Changes

- 新增 `papers/2026/07/31/README.md`，完成当日研究、证据分级和 Books Integration 记录。
- Refine `books/part-04-inference-system/44-speculative-decoding.md`：
  增加 lossless / lossy verification 的 sampling contract、matched-policy baseline 与
  证据边界。
- Refine `books/part-06-agent/73-memory.md`：增加 poisoning lifecycle 与 selective
  repair 的 benign-state preservation 边界。
- Refine `docs/LEARNING_STATE.md`：同步第 44、73 章新增的稳定边界；不更新
  `docs/DECISIONS.md`，因为没有改变知识树结构。
- 保留运行前已有的 nano-vLLM、Daily prompt 与其他章节未提交修改，不覆盖、不清理。

## Open Questions

1. InferScale 的 KV identity 如何覆盖 model revision、LoRA、quantization、tokenizer、
   RoPE configuration 与不同 cache layout？当前 vLLM 版本能否保持 connector semantics？
2. 动态 memory 写入、用户删除和 model upgrade 如何传播到 GPU / CPU / object-store KV
   replicas，并提供可审计 completion evidence？
3. MemSecBench 的 lifecycle metrics 在多次重复、不同 judges、真实 authorization 和
   tool side effects 下是否稳定？Selective repair 如何覆盖 summaries、indexes 与 backups？
4. Lossy verification 的 overshoot 经验结论能否跨模型家族和 sampling regime 复现？
   生产系统应怎样把 distribution distance、task quality 与 latency/goodput 放入同一 SLO？
5. Filesystem memory 的 organization decay 能否通过 deterministic maintenance、
   schema validation 和 source-backed compaction 缓解，而不让维护成本超过 retrieval 收益？

## Sources

Primary sources，均于 2026-07-31 访问：

- InferScale: https://arxiv.org/abs/2607.27090
- InferScale full text: https://arxiv.org/html/2607.27090v1
- MemSecBench: https://arxiv.org/abs/2607.27080
- MemSecBench full text: https://arxiv.org/html/2607.27080v1
- Revisiting Lossy Verification in Speculative Decoding:
  https://arxiv.org/abs/2607.26627
- Lossy Verification full text: https://arxiv.org/html/2607.26627v1
- Filesystem-Based Memory for LLM Agents: https://arxiv.org/abs/2607.26637
- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- Triton Releases: https://github.com/triton-lang/triton/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases

Discovery / metadata cross-check：

- arXiv recent: https://arxiv.org/list/cs/recent
- Hugging Face Papers: https://huggingface.co/papers
- Semantic Scholar: https://www.semanticscholar.org/
- Google Scholar: https://scholar.google.com/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/
- OpenReview / TMLR: https://openreview.net/group?id=TMLR
