# Daily Research — 2026-08-10

**规范：** V3
**窗口：** 2026-08-09T09:00:00+08:00 ～ 2026-08-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:03:21+08:00

## 1. 结论

本窗 14 个每日来源均已检查。arXiv 官方公告批次跨相关分类去重后有 484 个身份；先按标题排除明确的领域应用与传统 ML，再对可能改变大模型模型、训练、推理或 Agent 系统设计的条目读完整摘要。独立复核发现原作者漏掉九个具有具体机制增量的家族，纠正后冻结 24 个候选。没有使用旧 Daily 的候选、评分或 Books 处置，也没有引用 Weekly。

最重要的共同变化是把“模型算法”重新放回运行时 contract：长任务压缩要验证执行连续性，SLO 调度要联合队列与 KV tier，量化要检查具体 decision margin 而非只看 aggregate score；新增证据又把 persistent world state、稀疏 attention 的 head identity、完整 hybrid retrieval 与细粒度 KV reuse 纳入同一条状态责任链。21 项完成深入审阅，3 项完成标准审阅；6 项由 Books 现有正文承载，17 项长期增量已写入对应 canonical owner，1 项仅保留日报。独立写后审计确认 marker 唯一、语义绑定正确且正文均位于 Review notes 之前。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期检查，8 月 1 日后下一项为 8 月 18 日 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查；8 月 10 日数学能力材料属于 AI for Science，准入前排除 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 发布目录按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期检查 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog 与公开仓库发布页按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录按日期检查 | 已检查 | 无 |
| SRC-ZAI | Research 日期目录按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research / Blog 按日期检查 | 已检查 | 无 |
| SRC-ARXIV | 相关分类官方新公告跨分类去重 484 项；逐项题摘筛选并经独立漏项复查，保留 24 项；候选 v1 HTML 均可访问且未显示 withdrawn | 已检查 | 无 |

候选的实现或 benchmark artifact 仅在论文正文触发时定点核对，没有扩扫每周来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Reliable Context Compression](https://arxiv.org/html/2608.06503v1) | 2026-08-10T08:00:00+08:00 | 将压缩质量从文本相似度改为相同环境状态下的执行回归；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Adaptive VLA Inference](https://arxiv.org/html/2608.06434v1) | 2026-08-10T08:00:00+08:00 | 将快慢 VLA 从内部耦合改为环境反馈驱动的独立模型切换；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Cascade](https://arxiv.org/html/2608.06557v1) | 2026-08-10T08:00:00+08:00 | 用剩余 SLO budget 联合调度请求与 KV tier；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Quantization Damage Is Multiplicative](https://arxiv.org/html/2608.06564v1) | 2026-08-10T08:00:00+08:00 | 揭示低比特量化按比例收缩 decision margin，aggregate benchmark 可掩盖工具调用与拒答翻转；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Policy-Masked Private Experts](https://arxiv.org/html/2608.06690v1) | 2026-08-10T08:00:00+08:00 | 让授权决定私有 expert 参数路径是否可达；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AgentChaos](https://arxiv.org/html/2608.06790v1) | 2026-08-10T08:00:00+08:00 | 在共享 LLM API 边界做可验证的 runtime fault injection；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [StateFlow](https://arxiv.org/html/2608.06838v1) | 2026-08-10T08:00:00+08:00 | 为线性递归/混合模型传播 chunk boundary state 与 gradient；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-PIPELINE-PARALLEL`，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [PFM Dual-View Memory](https://arxiv.org/html/2608.06989v1) | 2026-08-10T08:00:00+08:00 | 将物理布局与 NPU/PIM accessor view 解耦以适配动态执行；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Explicit Epistemic Stance in Compressed Memory](https://arxiv.org/html/2608.06953v1) | 2026-08-10T08:00:00+08:00 | 受控证明“显式标记立场”比增加字数更能让压缩记忆保留不确定性；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [HiSparse](https://arxiv.org/html/2608.07009v1) | 2026-08-10T08:00:00+08:00 | 将 sparse-attention 的完整可寻址 KV 历史与有限 HBM residency 分离；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [GraceKV](https://arxiv.org/html/2608.07001v1) | 2026-08-10T08:00:00+08:00 | 将 token eviction 与 merge 统一成 coverage/resolution 的全局预算分配；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [MemOPD](https://arxiv.org/html/2608.07068v1) | 2026-08-10T08:00:00+08:00 | 区分 student action provenance 与 teacher scoring state 的真正一致性；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [FACTOR](https://arxiv.org/html/2608.07118v1) | 2026-08-10T08:00:00+08:00 | 分离 action credit 与 token allocation，并保持 credit conservation；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Two-Hop Generalization](https://arxiv.org/html/2608.07261v1) | 2026-08-10T08:00:00+08:00 | 把组合泛化失败定位为跨层 intermediate representation 与 reasoning circuit 不匹配；3 + 1 + 3 = 7 | 深入完成 | 整合：`WORLDVIEW-LLM-INTELLIGENCE`，[Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [Diffusion LLM Mechanistic Safety Exploits](https://arxiv.org/html/2608.07430v1) | 2026-08-10T08:00:00+08:00 | 揭示 diffusion LM 的安全表征可稀疏继承并跨架构迁移攻击；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AtlasVLA](https://arxiv.org/html/2608.06729v1) | 2026-08-10T08:00:00+08:00 | 用 persistent world/ego state 让单腕部相机策略在遮挡与长任务中保留空间和进度状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [CubicQuant](https://arxiv.org/html/2608.06763v1) | 2026-08-10T08:00:00+08:00 | 在规则整数码流中用组级单调三次曲线表达非均匀重建，并直接进入 packed GPU execution；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Autonomy-of-Heads](https://arxiv.org/html/2608.06849v1) | 2026-08-10T08:00:00+08:00 | 从冻结 Q/K 权重几何推断 retrieval/streaming head，在无校准数据时生成 sparse-attention plan；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [LLMRouter](https://arxiv.org/html/2608.06867v1) | 2026-08-10T08:00:00+08:00 | 将模型路由拆成 encoder、scoring、decision 与 learning signal 的统一实验接口；2 + 2 + 2 = 6 | 标准完成 | 仅报告：主要增量是统一框架与 benchmark，未建立超出现有路由 contract 的新稳定机制 |
| [HarnessSafe](https://arxiv.org/html/2608.06984v1) | 2026-08-10T08:00:00+08:00 | 把跨任务攻击拆成 carrier entry、persistence、benign trigger 与真实 violation 的生命周期；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Exact Adaptive Hybrid Retrieval](https://arxiv.org/html/2608.07152v1) | 2026-08-10T08:00:00+08:00 | 将完整列表融合定义为正确性目标，并用未读贡献上界决定每请求检索深度；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Agent Memory Distillation](https://arxiv.org/html/2608.07169v1) | 2026-08-10T08:00:00+08:00 | 把 teacher trajectory 分解为主动 workflow/subtask memory 与错误触发的 function memory；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [TEMPO](https://arxiv.org/html/2608.07314v1) | 2026-08-10T08:00:00+08:00 | 将 VLA 语义投影与低层 action expert 置于不同 RL 更新频率，避免快速控制更新扰动语义状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [CoinRAG](https://arxiv.org/html/2608.07458v1) | 2026-08-10T08:00:00+08:00 | 将离线 chunk KV 细化为可组合 semantic nugget cache，并显式支付 position/context alignment；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；handoff：Ch76 |

## 4. 证据与知识整合

### [Reliable Context Compression](https://arxiv.org/html/2608.06503v1)

v1 §3 在相同 AppWorld 状态比较压缩前后 continuations，§4 用 blocked/repeated actions 构造 boundary-local verifier；证据支持“摘要保留事实仍可能丢失执行位置”，但只是初步单环境研究。拟在 Ch75 的 context compaction 路线中，接在“信息保留不等于控制状态连续”之后补入 paired-state regression gate，而不是加入 TRACE 产品介绍。

### [Adaptive VLA Inference](https://arxiv.org/html/2608.06434v1)

v1 将 slow deliberative planner 与 fast reactive policy 解耦，由强化学习 switching policy 消费实时环境反馈选择模型；仿真与双臂实机实验只证明作者 workload 的可行 operating point，不能把 93.4 Hz 外推到其他 embodiment。Ch26 已明确 high-level reasoning、low-level controller、control frequency 与环境反馈的分层及共存条件，故不重复写入。

### [Cascade](https://arxiv.org/html/2608.06557v1)

v1 §III～V 将 latency budget 定义为 SLO 减去预测剩余服务时间，并让同一预算同时控制排队优先级、KV restore/prefetch/retain/recompute；§VI 的生产 traces 只支持作者模型与负载。Ch56 已经把 SLO slack、KV 容量与剩余工作纳入同一调度状态，因此判定已有覆盖，不重复写入。

### [Quantization Damage Is Multiplicative](https://arxiv.org/html/2608.06564v1)

v1 §2～5 对 16 个模型、三类量化方法和 8～2 bit 做 paired per-decision margin 测量；受损 tool-call 与 safety family 更符合 margin shrinkage 加 family-specific push，而不是固定尺度噪声。该关系能在同一 model/bit-width 内预测 flip，却不能跨模型借用常数，2 bit 时 instrument 也会失效。拟在 Ch49 的逐例一致性验收之后补入“margin 不是 certificate、经本模型本位宽校准后才是 risk predictor”，并要求工具调用、拒答等 decision slice 单独验收。

### [Policy-Masked Private Experts](https://arxiv.org/html/2608.06690v1)

v1 §2 明确 threat model 与“不等价的三个主张”，§3 在 top-k 之前选择 public/private expert pool，并用 hook 审计实际 routed rows；它证明的是给定 TCB 下私有参数不可达，不证明 public model 不具备同等语义能力。拟在 Ch72 的“policy 不能只约束输出”之后补充 parameter-path authorization，保留 TCB、fallback 与语义能力边界。

### [AgentChaos](https://arxiv.org/html/2608.06790v1)

v1 §3 定义 crash/omission/value fault，§4 在 HTTP response 字段做非侵入注入并确认 fault 真正触发，实验表明正常 benchmark 排名不能替代故障韧性。拟在 Ch66 的 evaluation contract 中补入“注入成功收据 + downstream effect + diagnosis”三段式 chaos test；不外推论文的跨系统排名。

### [StateFlow](https://arxiv.org/html/2608.06838v1)

v1 §3～4 把长序列切为 chunks，显式传播 recurrence boundary state/gradient，并用非均匀 chunk 平衡混合 attention 与 recurrence；收益绑定 32B、256K 及作者并行配置。拟在 Ch38 传统 stage pipeline 之后增加 sequence-pipeline 分支，突出新的 dependency edge、activation lifetime 与负载不均衡代价。

### [PFM Dual-View Memory](https://arxiv.org/html/2608.06989v1)

v1 的核心不是“统一内存更快”，而是同一 tensor 在 prefill/decode 或 MoE routing 下可能更换最佳执行设备；物理布局保持单份，address translation 向不同 accessor 提供逻辑 view。拟在 Ch54 的 placement/residency 之后补充 logical view 与 physical layout 的分离，同时限定于 NPU-PIM 原型和受测模型。

### [Explicit Epistemic Stance in Compressed Memory](https://arxiv.org/html/2608.06953v1)

v1 的 matched-note 实验固定 claim、stance、budget 与 filler，只改变 stance 的表示位置；两模型与预注册复现支持“显式表达”这一交集结论，但 full sentence 的收益不跨模型，且样本仅 60 条英文 claim、紧预算和 model-judge readout。拟在 Ch77 的压缩 schema 中把 epistemic status 做成可校验字段，并明确 provenance 原文仍是 authority，字段缺失时不得把摘要语气当成已验证事实。

### [HiSparse](https://arxiv.org/html/2608.07009v1)

v1 §2～4 保留 host 侧完整 KV history，在 GPU 只维护固定大小 working set，并把 hit/LRU/fetch 放入 decode graph；输出 exactness 来自只改 placement、不改 selected KV。拟在 Ch45 的 tiered KV 路线中补入 addressability≠residency、IO 是剩余价格，以及 shared-selection layer prefetch 的成立条件。

### [GraceKV](https://arxiv.org/html/2608.07001v1)

v1 把 layer-head-slot 表示成 prototype tree：增加 root 扩大 coverage，拆分 node 提高 local resolution，所有动作竞争同一 cache budget。其作者 benchmark 支持该无训练方法在受测任务与压缩率下的排序，不证明 tree proxy 在任意 query 分布都保持语义。Ch45 已把 cache budget、coverage、resolution 与 fallback 作为联合选择，并保留 FullKV/固定策略边界，判定已有覆盖。

### [MemOPD](https://arxiv.org/html/2608.07068v1)

v1 §3.3 证明 compact-memory rollout 在持久历史中重编码后，action 虽由 student 采样，却可能被 teacher 在从未访问的 position/visibility state 上评分；方法记录每次 invocation 的 token IDs、positions 与 causal mask 后再 packed reconstruction。§4.4 的 matched control 支持 state alignment 的增量，但任务只覆盖长程 retrieval agent。拟在 Ch33 的 student-owned on-policy state 后加入 conditioning-state equality 与 replay-compute-equivalence gate，防止“来源 on-policy”掩盖 state off-policy。

### [FACTOR](https://arxiv.org/html/2608.07118v1)

v1 §3 先用 TD residual 分配 action credit，再用 teacher-student likelihood gap 分给 action tokens，并用 normalization 防止符号翻转和长度隐式加权；实验只覆盖三个 agent 环境。拟在 Ch33 的 multi-turn credit assignment 中补入“先多少、再给哪里”的守恒分解及 estimator bias/teacher cost。

### [Two-Hop Generalization](https://arxiv.org/html/2608.07261v1)

v1 在受控 symbolic setting 中分离“两个 atomic fact 都记住”与“能组合推理”：成功来自 bridge entity 在不同 context 的一致表示，失败来自 lower layer 已构造中间状态、upper layer 却只学会 output mapping。单 loop 的 recurrent-style 训练改善 symbolic 与 natural-language OOD，但不能证明真实大模型的全部 multi-hop failure 都由同一电路造成。拟在 Ch8 的组合泛化路线补入“存储事实不等于复用推理电路”，并 handoff Ch17 解释跨层 representation contract。

### [Diffusion LLM Mechanistic Safety Exploits](https://arxiv.org/html/2608.07430v1)

v1 §4～6 从 safety neurons 的映射/剪枝到离线 diffusion steering 建立攻击链；作者结果说明 AR 初始化可能把稀疏安全 footprint 一同迁移给 diffusion model，但不证明所有闭源模型具有同一因果机制。拟在 Ch72 的 model artifact threat model 中增加 architecture conversion 后的 inherited safety state 与跨架构 red-team gate。

### [AtlasVLA](https://arxiv.org/html/2608.06729v1)

v1 §3 将腕部相机的瞬时观测提升为持续更新的 4D voxel-hashed world state，并以独立 ego-working memory 保存动作历史和任务进度；消融支持两种 memory 在 LIBERO、RLBench 与有限实机长程任务中的互补作用。证据不证明单目重建在开放场景中始终正确，也不赋予记忆绕过低层 controller 的权限。Ch25 已完整承载 persistent world state、不可见实体与 observation correction 的责任边界，故判定已有覆盖。

### [CubicQuant](https://arxiv.org/html/2608.06763v1)

v1 §2～5 用两个 shape 参数和一个 scale 将规则 magnitude codes 映射到单调非均匀 level，并给出直接 packed-weight kernel；§6 的 H200 结果只证明特定 GEMV/GEMM shape 下 model-dtype 与 Dynamic-A8 的 crossover。论文明确未测 downstream model quality 与跨设备端到端性能。拟在 Ch49 的量化路线加入“规则码流与自适应重建不必二选一”，同时要求 format metadata、group size、activation path、shape 与质量回归共同版本化。

### [Autonomy-of-Heads](https://arxiv.org/html/2608.06849v1)

v1 由 `W_K^T W_Q` 的有效秩刻画 head 的 dominant matching geometry，并在 `d_head` 空间计算，从而在无运行时 attention score 或校准 prompt 时提出 retrieval/streaming head 划分。受测 decoder-only 模型在固定稀疏率下的延迟与质量支持这一 data-free proposal，但 head role 并非输入无关真值，论文也未覆盖 multimodal、cross-attention 与 workload drift。拟在 Ch22 将 frozen-weight geometry 写成 sparse-attention admission 的候选信号，最终 selection 仍需长上下文任务回归与 dense fallback。

### [LLMRouter](https://arxiv.org/html/2608.06867v1)

v1 的主要贡献是把 router 实现整理为 context/model encoder、scoring、decision rule 与 learning signal，并提供监督构造和多任务 benchmark。它有助于公平比较成本—质量路线，但作者实验没有建立一种超出现有 gateway/scheduler 路由主线的新机制或普遍最优策略；不同 workload、用户状态与候选模型 revision 仍需单独校准。因此作为有用的实验基础设施仅保留日报，不用框架目录制造 Books 新正文。

### [HarnessSafe](https://arxiv.org/html/2608.06984v1)

v1 将 328 个 executable cases 按 memory、skill、tool、artifact 等七类 persistent carrier 建模，并用 trace 判断攻击停在 entry、persistence、trigger 还是 observable effect。结果只支持所测 harness/model 组合，不能由平均 attack success 推导任意 carrier 的安全性。拟在 Ch72 把 harness 安全从 prompt-local detection 扩成 persistent-risk lifecycle，并要求 carrier identity、跨会话 lineage、benign-trigger canary 与 effect receipt 共同组成 containment evidence。

### [Exact Adaptive Hybrid Retrieval](https://arxiv.org/html/2608.07152v1)

v1 先冻结 complete-list weighted RRF 的 ordered Top-K 作为 correctness contract，再让 dense/sparse iterator 用未读贡献上界按请求扩展深度；只有界证明剩余条目不能改变 Top-K 才停止，否则安全耗尽列表。150 个 query-snapshot 组合支持 exactness 与常见场景加速，也明确反相关 rankings 可能耗尽两表并更慢。拟在 Ch76 补入 fixed Top-L → adaptive exact fusion 的演进：节省来自可证停止，不来自把未读项默认为零。

### [Agent Memory Distillation](https://arxiv.org/html/2608.07169v1)

v1 从成功 teacher trajectories 生成 workflow、subtask 与 function 三层 memory，前两层在任务开始主动注入，后一层仅在 tool error 时检索；消融显示 subtask memory 在作者四个 4B～8B student 与三组工具 benchmark 中贡献最大。teacher quality、student compatibility、静态离线 memory 与文本工具任务限制其外推。Ch77 已将 hierarchical memory、proactive/reactive read、teacher provenance 与 student-state compatibility 串成同一机制，判定已有覆盖。

### [TEMPO](https://arxiv.org/html/2608.07314v1)

v1 冻结 vision-language backbone，仅让 semantic projection 低频更新、action expert 高频吸收在线控制反馈；不同频率消融支持作者 CALVIN 与两项实机任务中的稳定性，而不是证明固定 `5:1` 或 `10:1` 比例可跨 embodiment 复用。Ch26 已明确慢语义状态、快 action module、训练 staleness envelope 与安全 controller 的分责，现有正文已覆盖该长期机制。

### [CoinRAG](https://arxiv.org/html/2608.07458v1)

v1 将离线 chunk 编码切为可组合的 information-nugget KV，并用两阶段检索选择较小 semantic working set；消融显示 position alignment 在紧 prefill budget 下是关键组成。结果只覆盖 LongBench 多跳 QA、静态 corpus 与作者 cache construction，未披露生产并发、更新和多租户条件。拟由 Ch45 承载 cache identity、position/context alignment、offline build cost 与 full-chunk fallback；Ch76 只 handoff semantic nugget selection，避免让 RAG 章节拥有物理 KV 真值。

## 5. 缺口与下一步

无

17 个 Books 增量已写入并通过独立写后审计。

## 6. 复核

复核者：独立 fresh-context reviewer（2026-09-08）

结论：通过

独立复核重放 484 个官方公告身份的高信号题摘范围，确认原稿存在九个 false negative，并将分母由 15 修正为 24；同时抽查原 15 项未发现需要移出分母的 false positive。24 个候选均核对 exact-v1 HTML 与 withdrawn 页面状态，评分只描述采用命题，不把作者 benchmark 外推为生产保证。6 项“已有覆盖”均能在相应正文找到具体机制，1 项框架型材料降为“仅报告”；17 项 Books 增量逐项完成 marker、canonical owner、相邻衔接、证据边界和 Review notes 位置检查。Coverage、Candidate、Evidence、Books 与独立复核 Gate 均已闭合。Cross-model skipped: 本轮为父任务分派的非交互独立复核。
