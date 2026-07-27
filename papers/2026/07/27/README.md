# AI Research Daily — 2026-07-27

> Research window: 2026-07-24 至 2026-07-27
>
> Accessed: 2026-07-27（Asia/Shanghai）
>
> Scope: 官方研究页面、论文原文、官方 GitHub Release 与官方工程文档
>
> Organization: 模型与研究机构 → arXiv 论文 → AI Infra 与工程项目

## Executive Summary

过去 72 小时没有发现需要立即改写项目核心认知的模型实验室官方研究发布。OpenAI、Anthropic、Google DeepMind、Meta AI 等已扫描页面没有出现达到本项目收录门槛的新研究，因此不使用更早的产品新闻填充日报。

论文侧有两项值得深入保留的工作。HiKV 从算法与硬件协同角度压缩 Decode 阶段的 KV 访问，展示了 importance-aware retention 和 element-level selection 的潜力，但结论仍受专用硬件与实验条件约束。Ground Truth First 则把事实有效期、来源和写入质量纳入长期 Agent Memory 评测；其方法论与 Part VI 第 73 章直接相关，但单篇 synthetic benchmark 尚不足以成为核心章节结论。

AI Infra 与工程项目侧的主要信号来自 vLLM v0.26.0 与 SGLang v0.5.16：两者都在处理 hybrid model、分层存储和多种 cache/state layout。这表明 Serving runtime 的抽象正在从“管理统一的 KV Cache”扩展为“管理异构、分层且具有 ownership 的模型状态”。

Hugging Face 的 Nunchaku Lite 与 AMD MI455X 文章位于 72 小时时间边界。前者揭示通用量化接口与模型专用 kernel fusion 的取舍，后者提供 HBM 容量如何转化为 KV concurrency 的初步案例；两者均不足以单独触发新的核心结论。

## 1. 模型与研究机构

### Source Coverage

以下结果严格按照本轮实际留有访问证据的机构顺序列出。这里的“无重要更新”表示在本次公开页面扫描与检索条件下，没有识别到时间窗内达到收录门槛的条目，并不等于对机构所有渠道的完备性证明。

| Order | Institution | Source reviewed | Decision |
| ---: | --- | --- | --- |
| 1 | OpenAI | OpenAI Research | 无重要更新 |
| 2 | Anthropic | Anthropic News | 无重要更新 |
| 3 | Google DeepMind | Google DeepMind Blog | 无重要更新 |
| 4 | Meta AI | Meta AI Blog | 无重要更新 |
| 5 | Hugging Face | Hugging Face Blog | 发现工程类边界条目，归入第 3 节 |
| 6 | DeepSeek | DeepSeek API Updates | 无达到研究门槛的更新 |
| 7 | ByteDance Seed | Seed Blog、Seed Research | 最新项目早于时间窗，不回填 |

### No Material Update

本组没有 Must Read 或 Worth Watching 级别的模型实验室研究发布。Seed Blog 最新可见条目为 2026-04-09 的 Seeduplex，Seed Research 的 Seed3D 2.0 Blog/Publication 位于 2026-04-22～23，均早于本次 72 小时窗口。Hugging Face Blog 中与 Nunchaku Lite、AMD MI455X 相关的内容属于 inference runtime、quantization 与硬件工程观察，因此放在第 3 节，不与模型机构研究混排。

## 2. arXiv 论文

### Candidate Triage

评分维度依次为 Technical Novelty、System Impact、Practical Value、Source Reliability、Project Relevance、Longevity，每项 0～5 分。

| Candidate | Published | Score | Decision |
| --- | --- | ---: | --- |
| HiKV | 2026-07-24 | 24/30 | Must Read |
| Ground Truth First | 2026-07-24 | 22/30 | Must Read |
| Scaling Native Multimodal Pre-Training From Scratch | 2026-07-24 | 22/30 | Worth Watching |

### Must Read

#### 1. HiKV：以分层重要性选择降低 Decode 的 KV 访问

- Source: arXiv paper
- Authors: Chao Fang, Jun Yin, Man Shi, Marian Verhelst
- Published: 2026-07-24
- URL: [arXiv abstract](https://arxiv.org/abs/2607.22389), [HTML paper](https://arxiv.org/html/2607.22389v1)
- Score: 24/30 = 5 + 4 + 2 + 4 + 5 + 4
- Category: KV Cache / Hardware-Software Co-design

##### What

HiKV 提出两阶段 KV 选择机制，并为两种选择路径设计可重构的 importance sorter。论文报告在其评测条件下，Attention 最多获得 `7.95×` speedup、约 `90%` energy reduction、低于 `1%` accuracy loss，并付出约 `8%` area overhead。

这些数字是作者报告的专用设计结果，不代表通用 GPU Serving 的可实现收益。

##### Why

Decode 每一步只产生少量 query，却需要访问不断增长的历史 K/V。随着 context length 和 concurrency 增长，瓶颈容易从计算转为 off-chip memory traffic。仅按 token 粗粒度保留或淘汰 KV，可能丢失 K 与 V 在元素层面的不同重要结构。

##### Principle

如果某些历史 token 或 feature dimension 对当前及未来 query 的贡献长期较小，可以用受控的信息损失换取较少的数据搬运：

```text
更少的 retained KV elements
→ 更少的 off-chip traffic
→ 更低的 Decode latency / energy
```

真正困难的部分不是“删除 KV”，而是用低于节省收益的成本估计重要性，并维护稳定、可实现的选择结构。

##### Mechanism

Stage I 将固定预算拆为 recent bank 与 important bank：

- recent bank 保留局部最近上下文；
- important bank 累积历史重要性；
- frozen important bank 使用 min-heap 维护候选；
- eviction 的维护复杂度为 `O(log B)`，其中 `B` 是 bank capacity。

Stage II 进一步在元素级选择：

- 对 K，根据 query magnitude 选择 feature dimensions；
- 对 V，按 token row 进行 chunked sorting；
- 将全局排序近似化为局部结构，论文给出的复杂度从 `O(N log N)` 降为 `O(N log d_h)` 的量级表达。

##### Trade-offs

- Importance estimation 本身占用计算、存储和控制逻辑。
- 冻结或近似重要性可能无法及时响应 topic shift。
- Accuracy loss 与 token budget、任务分布、head/layer sensitivity 相关。
- 专用 sorter 的收益依赖硬件数据流；迁移到 GPU 时可能受 kernel launch、irregular access 和 synchronization 限制。
- 论文的 iso-accuracy 结果仍需更多模型、任务和独立复现验证。

##### Connection

HiKV 位于现有知识树的联合边界：

```text
第 41 章：KV runtime lifecycle
→ 第 50 章：GPU memory budget
→ Part V：hardware-aware scheduling / capacity governance
```

它优化的是 KV 保留与访问机制，不改变 Self Attention 的数学语义，也不能与 PagedAttention 的逻辑到物理映射混为一谈。

##### Evolution

未来值得观察两条路线：

1. importance-aware compression 是否能在 commodity GPU 上形成可重复的端到端收益；
2. scheduler 是否能感知每个请求的精度预算，并把 cache compression 纳入 SLO 和 quality trade-off。

##### Evidence Level

已公开论文，作者标注将发表于 TCAS-I。结果尚未独立复现，且实验平台与通用 GPU runtime 存在距离。

##### Relevance to AI-System-Design

高。它展示了 memory hierarchy、algorithm 和 accelerator dataflow 必须联合分析，不能只用容量公式解释 KV Cache 的系统成本。

##### Recommended Action

保留为第 41、50 章的候选研究材料，不立即更新正文。需要等待公开实现、GPU baseline 或独立实验。

#### 2. Ground Truth First：长期 Agent Memory 评测应先定义事实生命周期

- Source: arXiv paper
- Author: Quentin Spencer
- Published: 2026-07-24
- URL: [arXiv abstract](https://arxiv.org/abs/2607.21962), [HTML paper](https://arxiv.org/html/2607.21962v1)
- Score: 22/30 = 4 + 4 + 3 + 3 + 4 + 4
- Category: Agent / Memory / Evaluation

##### What

论文提出 truth-first longitudinal evaluation：先构造包含事实、有效期、变化事件和来源 channel 的 life script，再由 LLM 渲染成 conversation、email 等自然历史，最后从脚本机械生成问题并执行 answerability audit。

实验覆盖短期与最长九周的 synthetic histories。作者报告 curated map 随时间增长明显退化，而 provenance graph 保持较高表现；但样本规模、judge、answerer 和 benchmark construction 都限制了结论外推。

##### Why

如果先生成长对话再人工编题，评测者很难判断：

- 某事实在提问时是否仍然有效；
- 多个来源冲突时哪个具有更高 provenance；
- 系统答错是检索失败、写入失败，还是题目本身不可回答；
- 一个短期有效的 memory design 是否能跨更长 horizon 保持行为。

因此，长期记忆的 ground truth 需要时间语义和来源语义，不能只是一组无时间戳的 key-value facts。

##### Principle

Agent memory 的评测对象不是静态 retrieval accuracy，而是一个随时间演化的状态系统：

```text
fact
+ valid interval
+ provenance
+ supersession relation
+ write result
→ answerable state at query time
```

只有先定义这一层，read、write、update 和 conflict resolution 才能被分开诊断。

##### Mechanism

该评测流程包含：

1. 预先生成结构化 life script；
2. 将脚本渲染为多 channel interaction；
3. 校验渲染内容与脚本的 fidelity；
4. 从脚本生成带类型的问题；
5. 独立执行 answerability audit；
6. 比较 raw history、curated map、provenance graph 等 memory design。

论文还把 write-path weakness 与 downstream misses 关联起来，但作者明确将其表述为 association，而非因果证明。

##### Trade-offs

- Synthetic history 提高可控性，却可能缺少真实用户行为的噪声和隐含语境。
- Truth-first script 便于审计，但也可能偏向擅长结构化 provenance 的架构。
- LLM judge 和单一 answerer 会引入 evaluator bias。
- 九周 horizon 比常见短 benchmark 更长，但仍不足以代表多年个人记忆。
- 缺少更强 raw-chunk RAG、competitive reranker 和 oracle baseline。

##### Connection

该工作属于 Part VI 第 73 章“Memory”的直接研究入口，并与全局知识树中的 Evaluation System 相连。它也复用了 Part IV 的系统思想：memory 不只是内容集合，而是具有 identity、lifecycle、ownership 和 consistency 的状态。

##### Evolution

如果后续 benchmark 能扩展到真实用户、多个 answerer、可竞争的 RAG baseline 和更长 horizon，Agent memory 的架构比较可能从“短期问答准确率”转向：

```text
write quality
+ temporal validity
+ provenance correctness
+ read cost
+ behavioral safety
```

##### Evidence Level

单篇 preprint、single-author、synthetic benchmark。方法论值得保留，架构排名不应视为稳定结论。

##### Relevance to AI-System-Design

中高。它为 Agent 系统中的 Memory 节点提供了比“向量数据库 + RAG”更完整的状态模型。

##### Recommended Action

保存为第 73 章及 Evaluation System 的候选来源。等 Part V 完成并进入 Part VI 撰写时重新检索该方向，不因单篇论文提前填充核心章节。

### Worth Watching

#### Scaling Native Multimodal Pre-Training From Scratch

- Source: [arXiv:2607.22043](https://arxiv.org/abs/2607.22043)
- Published: 2026-07-24
- Score: 22/30
- Category: Multimodal / Scaling Law / Pretraining

论文使用 71M～3B 的六个模型规模、约 250B text tokens 与 75B multimodal tokens，研究 native multimodal pretraining 的 compute-optimal allocation。其重要信号是：语言侧 allocation 可能对 mixture ratio 相对稳定，而 multimodal allocation 对数据比例更敏感，因此联合训练需要 Pareto frontier，不能直接套用 text-only scaling law。

该结论仍受 3B 规模上限、特定 MoE 架构、数据组成和 training-loss proxy 限制。它与第 7、23、24 章相关，但目前只作为候选证据，不修改 Scaling Law 或 Pretraining 的稳定结论。

## 3. AI Infra 与工程项目

### Source Coverage

| Project or source | Latest item retained | Window decision |
| --- | --- | --- |
| vLLM | v0.26.0 | 时间窗内，Must Read |
| SGLang | v0.5.16 | 时间窗内，Must Read |
| Kubeflow Trainer | v2.3.0-rc.3 | 时间窗内，但证据不足，仅记录 |
| Hugging Face Diffusers / Nunchaku | Nunchaku Lite | 72 小时边界，Worth Watching |
| Hugging Face Transformers / AMD | MI455X first results | 72 小时边界，简要观察 |

### Candidate Triage

| Candidate | Type | Published | Score | Decision |
| --- | --- | --- | ---: | --- |
| vLLM v0.26.0 + SGLang v0.5.16 | Official engineering releases | 2026-07-25～27 | 25/30 | Must Read |
| Kubeflow Trainer v2.3.0-rc.3 | Official pre-release | 2026-07-24 | 13/30 | Record Only |
| Nunchaku Lite in Diffusers | Official engineering blog and PR | 2026-07-23 | 23/30 | Worth Watching |
| Transformers on AMD MI455X | Community article + official specification | 2026-07-23 | 18/30 | Worth Watching, brief |

### vLLM 与 SGLang

#### Must Read：Serving Runtime 正在从统一 KV Cache 走向异构状态管理

- Source: vLLM 与 SGLang 官方 GitHub Release
- Published: vLLM 页面显示 2026-07-25，GitHub API 的 `published_at` 为 2026-07-27；SGLang 为 2026-07-25
- URL: [vLLM v0.26.0](https://github.com/vllm-project/vllm/releases/tag/v0.26.0), [vLLM release API](https://api.github.com/repos/vllm-project/vllm/releases/tags/v0.26.0), [SGLang v0.5.16](https://github.com/sgl-project/sglang/releases/tag/v0.5.16)
- Score: 25/30 = 4 + 5 + 4 + 5 + 4 + 3
- Category: AI Infra / Inference Runtime / Official Release

##### What

vLLM v0.26.0 增加了 heterogeneous model family、按 KV-cache group 选择 Attention backend、hybrid model 的 partial prefix cache，以及面向 secondary storage 和 object store 的 tiered KV 能力。

SGLang v0.5.16 同时引入 UnifiedRadixTree、针对 SWA、Mamba 和 DSA 的 state/cache 管理调整，并处理 speculative verification 中 SSM state snapshot 的成本。两个项目的具体实现不同，但都在突破“每层具有相同 Attention 与 KV layout”的默认假设。

##### Why

传统 LLM Serving runtime 经常隐含如下同构前提：

```text
每一层
→ 相同 Attention 语义
→ 相同 KV shape
→ 相同 cache allocation policy
→ 相同 eviction / transfer path
```

Hybrid model 将 full attention、sliding-window attention、linear attention 或 state-space layer 放在同一模型内。此时 runtime 不再只是为 token 分配一组统一 KV blocks，而要识别每层产生什么状态、状态如何增长、能否复用、由谁持有，以及能否迁移到其他存储层。

##### Principle

Serving state 的正确抽象不应绑定某一种 Attention 实现，而应表达：

```text
State identity
+ layer or state-family layout
+ lifecycle
+ ownership
+ placement tier
+ consistency rule
```

KV Cache 只是其中最重要的一种 state family。随着模型结构异构化，runtime correctness 越来越依赖 state contract，而不仅是 kernel dispatch。

##### Mechanism

从两个 Release 可以抽象出三层变化：

1. **Execution capability**：不同 layer group 可以选择不同 backend 或 kernel path。
2. **State capability**：不同 cache/state group 具有不同 shape、增长方式和复用边界。
3. **Placement capability**：状态可位于 GPU HBM、host memory、local storage 或 object store，并受身份、拓扑和一致性约束。

这是跨 Release 的归纳，不是任一项目官方宣称的统一架构。

##### Trade-offs

- 通用 state abstraction 提高模型覆盖范围，但会增加 scheduler、block manager 和 correctness testing 的复杂度。
- Tiered storage 扩大逻辑容量，但引入传输延迟、带宽竞争、失效处理和身份认证问题。
- Prefix reuse 对共享前缀有效，但 hybrid layout 会使可复用边界与收益估计更复杂。
- Release 中的吞吐数字绑定具体模型、GPU、batch、量化与输入输出长度，不能外推为框架的普遍加速比。
- 快速扩张的 capability matrix 会增加版本兼容和回归验证成本。

##### Connection

该变化连接现有知识链：

```text
第 19 章：模型级 K/V shape
→ 第 41 章：runtime state lifecycle
→ 第 43 章：逻辑到物理 block 映射
→ 第 46～47 章：Serving runtime
→ 第 50～52 章：容量、placement 与调度
```

现有章节已经把 KV ownership、offload、scheduler 和 framework version boundary 分开，因此今天的 Release 是对既有框架的增强证据，不构成核心观点反转。

##### Evolution

短期内可以预期 runtime 的核心接口继续从 model-specific branches 演化为显式的 cache/state group contract。更长期的分界点是：scheduler 能否使用统一的 cost model 同时决策 KV、SSM state、encoder cache 与 remote prefix state，而不是为每种模型手写独立策略。

##### Evidence Level

- Release 功能：官方实现事实。
- 性能数字：官方、workload-bound、尚未在本文独立复现。
- “异构状态管理成为 runtime 主抽象”：基于两个独立项目同向变化的工程推断。

##### Relevance to AI-System-Design

高。它直接验证 Part IV 将 inference 定义为“状态持续演化的 token-generation process”是比“模型执行一次 forward”更稳定的系统视角。

##### Recommended Action

保留在 Daily。等相关 state/cache API 在后续版本稳定，并出现跨模型、跨 workload 的系统性设计文档后，再评估是否补充第 41、46、47 或 52 章。

### Kubeflow

#### Record Only：Kubeflow Trainer v2.3.0-rc.3

- Source: [official release](https://github.com/kubeflow/trainer/releases/tag/v2.3.0-rc.3)
- Published: 2026-07-24
- Score: 13/30
- Category: Training Platform / Pre-release

Release 页面仅提供候选版本标识和极少的实质性设计说明。它与 AI Platform 章节相关，但当前证据不足以形成 mechanism 或 trade-off 分析。等待正式版本、迁移说明或架构文档。

### Hugging Face Diffusers / Nunchaku

#### Worth Watching：Nunchaku Lite 的通用量化接口与模型专用 Fusion 边界

- Source: Hugging Face Blog、Diffusers integration 与 SVDQuant/Nunchaku work
- Published: 2026-07-23
- URL: [Hugging Face Blog](https://huggingface.co/blog/nunchaku-diffusers), [Diffusers integration PR](https://github.com/huggingface/diffusers/pull/14100), [SVDQuant paper](https://arxiv.org/abs/2411.05007)
- Score: 23/30 = 3 + 4 + 5 + 4 + 4 + 3
- Category: Diffusion Inference / Quantization / Runtime Integration
- Window note: 页面只提供日期而无精确时间；Hugging Face 索引在访问时显示“3 days ago”，因此作为 72 小时边界条目处理。

##### What

Nunchaku Lite 将 SVDQuant 的 4-bit diffusion Transformer 执行路径集成到 Diffusers。量化 checkpoint 可以通过常规 `from_pretrained()` 加载；runtime 在权重加载前把 stock Diffusers model 中目标 `nn.Linear` 替换为 SVDQ W4A4 或 AWQ W4A16 layer，CUDA kernels 则通过 Hugging Face `kernels` package 获取。

它不是新的量化理论，而是把已有量化机制从独立、模型专用的 inference engine 转换为可被通用 framework 加载、组合和发布的 artifact/runtime contract。

##### Why

常见 weight-only quantization 主要减少权重存储，在计算前仍需反量化到高精度，因此不一定降低 latency。SVDQuant 同时量化 weights 与 activations，可以减少内存流量并使用低精度计算，但原始 Nunchaku 的高性能依赖 QKV、GELU/MLP 等 architecture-specific fused paths。

系统矛盾是：

```text
通用 framework integration
→ 更低的模型接入成本与更强的组合能力

模型专用 graph rewrite + fusion
→ 更高性能，但每个架构都需要额外适配
```

##### Principle

量化能否转化为端到端加速，不只取决于每个参数占多少 bit，还取决于：

```text
effective latency
= low-precision compute
+ quantize / dequantize cost
+ kernel launch overhead
+ unfused memory traffic
+ non-quantized pipeline components
```

因此，“checkpoint 更小”和“请求更快”是两个不同结论。通用 module replacement 保留 framework composability，模型专用 structural rewrite 则进一步压缩 launch 与 memory-access overhead。

##### Mechanism

SVDQuant 面对 diffusion Transformer activation outliers 时：

1. 将 activation outlier 的困难部分迁移到 weights；
2. 用一个小型 16-bit low-rank branch 表示难量化部分；
3. 将剩余 residual 量化到 4 bit；
4. 在 kernel 中融合 low-rank projection、input quantization 与 4-bit matrix multiplication，避免修正分支抵消量化收益。

Nunchaku Lite 在 framework 层把这些执行要求编码进 `quantization_config`：

- 哪些 modules 使用 `svdq_w4a4`；
- 哪些 precision-sensitive modules 使用 `awq_w4a16`；
- precision、group size 和 low-rank rank；
- runtime 应实例化哪种 quantized linear。

普通模型可以只做 module replacement；需要 fused QKV 等 graph rewrite 的模型仍要通过 target config 和 runtime adapter 明确参数拼接、拆分与执行语义。

##### Trade-offs

- 通用 Lite path 减少模型接入成本，但无法自动推断所有 structural rewrites，性能低于原始模型专用 Nunchaku engine。
- NVFP4 kernel 仅支持 Blackwell；较早 GPU 需要 INT4 variants，Volta 与 Hopper 在该版本中不受这些 4-bit kernels 支持。
- 作者 benchmark 绑定 RTX PRO 6000、ERNIE-Image-Turbo、`1024×1024` 和特定 pipeline。其 `1.35×`～`1.8×` speedup 与 `31.1 GB → 16.0/20.6 GB` peak VRAM 不能外推到其他模型和硬件。
- `torch.compile` 能减少额外 kernel launches，但会引入 compilation latency、graph capture 边界和版本兼容成本。
- 视觉样例不能替代大规模 image quality、prompt distribution 与 regression evaluation。

##### Connection

该工作将项目中的几个稳定概念连接起来：

```text
第 31 章：Checkpoint 不只是权重文件
→ 第 45 章：engine build / kernel fusion / quantization
→ 第 50 章：weights + workspace 的显存预算
→ Part V：artifact governance 与 hardware capability matching
```

它也提醒本项目：Part IV 的 execution plan 思想不仅适用于 autoregressive LLM，diffusion runtime 同样需要让 artifact metadata、module graph、kernel capability 与硬件代际对齐。

##### Evolution

值得持续观察的不是某个 Diffusers API，而是 quantized artifact 是否逐渐形成稳定的跨 runtime contract：

```text
quantization semantics
+ module mapping
+ structural rewrite
+ kernel capability
+ hardware constraint
+ quality regression metadata
```

如果这层契约成熟，量化模型可以在保留 framework composability 的同时，逐步选择更激进的 architecture-specific fusion；否则每一种低精度格式仍会绑定独立 engine 和转换链。

##### Evidence Level

- Integration 与 hardware support：官方 Blog、开源 PR 和文档描述的实现事实。
- Benchmark：作者在单一硬件与 workload 上的报告，未在本项目独立复现。
- “量化 artifact contract”：基于实现结构提炼的工程推断。

##### Relevance to AI-System-Design

中高。它为 Checkpoint → conversion → runtime load → kernel dispatch 链提供了 diffusion 场景的具体证据，但本项目当前没有独立的 diffusion inference 章节。

##### Recommended Action

保留在 Daily。暂不扩展 ROADMAP；等待更多模型、硬件和 runtime 使用相似 artifact contract 后，再考虑将其抽象为核心内容。

### Hugging Face Transformers / AMD

#### Worth Watching：MI455X 的 HBM 容量不等于吞吐，但会改变 KV 并发上限

- Source: [Hugging Face Community Article](https://huggingface.co/blog/badaoui/transformers-on-amd-mi455), [AMD official specification](https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html)
- Published: 2026-07-23
- Score: 18/30 = 1 + 4 + 3 + 3 + 4 + 3
- Category: GPU / Transformers Compatibility / Preliminary Capacity Study
- Window note: 与 Nunchaku Lite 相同，作为发布日期缺少精确时间的边界候选。

文章报告 MI455X 具有 `432 GB HBM4` 和 `23.3 TB/s` peak memory bandwidth；这两项规格可由 AMD 官方页面交叉核验。Hugging Face 使用约 `64 GB` 的 Qwen3-32B BF16 model 做单卡 capacity study，报告 MI455X 在 OOM 前支持的并发请求超过 `192 GB` MI300 的三倍。

这一结果可以用第 50 章的 memory budget 做近似解释：

```text
M_KV_available
= M_HBM - M_weights - M_workspace - M_reserve

C_requests
≈ floor(M_KV_available / M_KV_per_request)
```

如果暂时忽略 workspace 与 reserve，仅扣除 `64 GB` weights：

```text
(432 - 64) / (192 - 64)
= 368 / 128
= 2.875
```

这说明更大 HBM 对并发容量的收益不是简单采用 `432 / 192`，而应先扣除固定权重和 runtime 开销。实际“超过三倍”的结果还依赖请求长度、KV dtype、allocator、reserve 和 OOM 判定，文章没有给出足够信息用于独立复算。

作者还报告 24 个 curated model architectures 的测试通过率约为 `99.5%`，并明确存在少量 flaky tests。该指标只能说明初步 Transformers compatibility，不能证明模型数值完全等价、kernel 已优化或 Serving throughput 已达到生产水平；文章也明确把 speed comparison 留给后续工作。

**Recommended Action**：保留为第 50 章容量公式的观察案例，不将该硬件特定结果写成普遍结论。等待公开 benchmark methodology、端到端 throughput/latency、功耗和多卡通信结果。

## Ignored Noise

- 未把 Release 中脱离模型、GPU、batch、输入输出长度和 SLO 的单点加速数字写成通用结论。
- 未把 Hugging Face Community Articles 等同于 Hugging Face 官方研究结论；MI455X 条目因测试配置具体且硬件规格可由 AMD 交叉核验，仅作为低等级候选。
- Seed 官方 Blog 与 Research 页面没有窗口内更新，因此未回填 4 月的 Seeduplex、Seed3D 2.0 等旧内容。
- OpenAI、Anthropic、Google DeepMind、Meta AI 等官方页面在本次时间窗内未发现符合门槛的新研究；没有为了填满 Daily 而回填更早的产品新闻。
- 未把旧论文在社交媒体上的再次传播计为新进展。

## Repository Changes

- 将日报统一迁移到 `papers/2026/07/27/README.md`，并移除旧的单数目录。
- 更新 `CODEX_DAILY_RESEARCH_PROMPT.md`：以后统一写入 `papers/`，并强制使用“模型与研究机构 → arXiv 论文 → AI Infra 与工程项目”的输出顺序。
- 更新 `docs/LEARNING_STATE.md` 中的日报来源路径。
- 清理今天日报中意外插入的整篇重复内容，并按新的固定来源顺序重组。
- 本次目录与结构调整没有修改 `books/` 核心章节，也没有改变日报中的技术结论。
- 未执行 commit 或 push。

## Open Questions

1. Hybrid model 的统一 state contract 最少需要哪些字段，才能同时覆盖 KV、SSM state、encoder cache 和 remote prefix？
2. Tiered KV 的 cost model 应如何联合表达 transfer latency、cache hit probability、SLO 与 failure recovery？
3. HiKV 的 irregular selection 能否在 commodity GPU 上获得端到端收益，而不是只减少理论 traffic？
4. Agent memory benchmark 在真实用户、强 RAG baseline 和多 evaluator 条件下，是否仍保持相同架构排序？
5. Native multimodal scaling 在更大规模、不同数据质量和 dense architecture 下是否仍呈现相同 allocation law？
6. Quantized artifact contract 能否统一表示 module replacement、structural rewrite 与硬件 kernel capability？
7. MI455X 的额外 HBM 在真实 Serving workload 中会优先转化为更高 concurrency、更长 context，还是更大的 batch？

## Sources

### 1. Official Research Pages Scanned

- [OpenAI Research](https://openai.com/research/index/), accessed 2026-07-27.
- [Anthropic News](https://www.anthropic.com/news), accessed 2026-07-27.
- [Google DeepMind Blog](https://deepmind.google/blog/), accessed 2026-07-27.
- [Meta AI Blog](https://ai.meta.com/blog/), accessed 2026-07-27.
- [Hugging Face Blog](https://huggingface.co/blog), accessed 2026-07-27.
- [DeepSeek API Updates](https://api-docs.deepseek.com/updates/), accessed 2026-07-27.
- [ByteDance Seed Blog](https://seed.bytedance.com/en/blog), accessed 2026-07-27.
- [ByteDance Seed Research](https://seed.bytedance.com/en/research), accessed 2026-07-27.

### 2. Papers

- Fang et al., [HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding](https://arxiv.org/abs/2607.22389), submitted 2026-07-24; accessed 2026-07-27.
- Spencer, [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962), submitted 2026-07-24; accessed 2026-07-27.
- [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043), submitted 2026-07-24; accessed 2026-07-27.

### 3. Official Engineering Releases and Documents

- [vLLM v0.26.0](https://github.com/vllm-project/vllm/releases/tag/v0.26.0), published 2026-07-25 on rendered page; GitHub API reported 2026-07-27; accessed 2026-07-27.
- [SGLang v0.5.16](https://github.com/sgl-project/sglang/releases/tag/v0.5.16), published 2026-07-25; accessed 2026-07-27.
- [Kubeflow Trainer v2.3.0-rc.3](https://github.com/kubeflow/trainer/releases/tag/v2.3.0-rc.3), published 2026-07-24; accessed 2026-07-27.
- [Bringing Nunchaku 4-bit Diffusion Inference to Diffusers](https://huggingface.co/blog/nunchaku-diffusers), published 2026-07-23; accessed 2026-07-27.
- [Diffusers Nunchaku integration PR](https://github.com/huggingface/diffusers/pull/14100), accessed 2026-07-27.
- [Hugging Face on AMD Instinct MI455X: First Transformers Results](https://huggingface.co/blog/badaoui/transformers-on-amd-mi455), published 2026-07-23; accessed 2026-07-27.
- [AMD Instinct MI455X official specification](https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html), launch date 2026-07-23; accessed 2026-07-27.

> “未发现”只表示本次按公开页面和检索条件没有识别到达到门槛的条目，不等于对所有官方渠道的完备性证明。
