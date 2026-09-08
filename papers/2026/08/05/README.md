# Daily Research — 2026-08-05

**规范：** V3
**窗口：** 2026-08-04T09:00:00+08:00 ～ 2026-08-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:30:00+08:00

## 1. 结论

本窗从 arXiv Wednesday 公告的 656 个宽身份中，经逐项题摘语义筛选和独立漏项复核保留 15 项，并从每日机构源保留 SeedRealtime 与 Muse 两项，共 17 个唯一 Source Family。Google Aug05 的 moral Turing test 研究人对模型判断的感知，不改变模型或基础设施机制，已在题摘阶段关闭；框架采用率综述等“相关但没有设计增量”的论文也未进入候选。

17 项原始正文均可访问，未见 withdrawal。Verified Tool Calls、HeteroPanacea、Oilbird 与 JudgeArena 的长期命题已有覆盖；其余 13 项形成正文整合。厂商 benchmark 均限定为其公开配置，不作为通用能力证明。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 按本窗与相邻日期检查，无符合范围的新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 相邻研究日期为 Jul28 与 Aug10 | 已检查 | 无 |
| SRC-GOOGLE-AI | [A moral Turing test](https://deepmind.google/research/publications/118955/) 日期为 Aug05；完整题摘显示其研究人类来源判断与偏差，不提供模型/系统机制增量，初筛关闭 | 已检查 | 无 |
| SRC-META-AI | [Muse Code / Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) 页面 `datePublished=2026-08-05T00:00:00Z`，北京时间 08:00，落窗并入选 | 已检查 | 无 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 按日期检查，本窗无相关正文 | 已检查 | 无 |
| SRC-DEEPSEEK | [Research](https://www.deepseek.com/) 与公开更新按日期检查，本窗无新机制正文 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [GitHub](https://github.com/MoonshotAI) 按发布时间检查，本窗无相关研究事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research) 中 Jul21 后下一条为 Aug11 | 已检查 | 无 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 中 Jun16 后下一条为 Aug14 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [SeedRealtime](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction) 的官方 `PublishDate=1785859200000`，即 Aug05 00:00 北京时间，落窗并入选 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 按日期检查，最近记录早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) 论文与博客按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 相邻研究记录不落窗 | 已检查 | 无 |
| SRC-ARXIV | Wednesday 08:00 北京时间公告；656 个宽身份作发现索引，逐项题摘语义筛选和独立漏项复核后保留 15 项并重开当前 v1 HTML | 已检查 | 无 |

本窗未发生需另行加载的按需来源触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SeedRealtime](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction) | 2026-08-05T00:00:00+08:00 | 将音视频、文本与 duplex turn-taking 放入一个实时交互状态机，改变多模态流的时间与打断契约；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) | 2026-08-05T08:00:00+08:00 | 把长程 coding agent 的持久执行、append-only event log 与 model-harness co-training 结合，改变 AgentRun 恢复边界；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Verified Tool Calls](https://arxiv.org/html/2608.02645v1) | 2026-08-05T08:00:00+08:00 | 用 postcondition、verify-before-retry 与 idempotency key 修正 Agent 把 timeout 当原子失败的错误假设；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [JudgeArena](https://arxiv.org/html/2608.02620v1) | 2026-08-05T08:00:00+08:00 | 把 benchmark、judge、prompt、backend 与运行 metadata 绑定为可复算评测身份；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TraceCompiler](https://arxiv.org/html/2608.02680v1) | 2026-08-05T08:00:00+08:00 | 从 noisy Agent trace 中只把带参数来源证据的依赖固化为 deterministic workflow edge；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [MutMem](https://arxiv.org/html/2608.02843v1) | 2026-08-05T08:00:00+08:00 | 将 memory 权重变更建模为带 signer epoch、predecessor 与承诺的授权状态转换，区分完整性与内容真值；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [AnchorKV](https://arxiv.org/html/2608.02901v1) | 2026-08-05T08:00:00+08:00 | 用 exact anchor、量化 residual 与输出敏感预算统一“全保留”和“选择性高精度”；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [OPTD](https://arxiv.org/html/2608.02942v1) | 2026-08-05T08:00:00+08:00 | 用 student 自己访问的状态和一致性验证决定 Diffusion transition 可跨越多少 teacher step；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [AcceptMoE](https://arxiv.org/html/2608.02989v1) | 2026-08-05T08:00:00+08:00 | 按 draft position 的实际提交概率与 expert residency 自适应 verifier expert set；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [SparSEEty](https://arxiv.org/html/2608.02995v1) | 2026-08-05T08:00:00+08:00 | 证明稀疏 serving 的 input-dependent weight access 会把 token 泄露进 confidential VM 的确定性侧信道；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Frequency- and Length-Aware Deduplication](https://arxiv.org/html/2608.03089v1) | 2026-08-05T08:00:00+08:00 | 将跨 shard duplicate detection 与 copy-retention policy 分离，纠正“精确去重等于统一只留一份”的数据判断；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [LLaDA MoE v2](https://arxiv.org/html/2608.03457v1) | 2026-08-05T08:00:00+08:00 | 给出 diffusion MoE 与 AR 不同的 learning-rate、batch、model-data 和 expert-pool scaling 边界；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [SkillSentry](https://arxiv.org/html/2608.03485v1) | 2026-08-05T08:00:00+08:00 | 以 adaptive honey world、matched no-skill 对照和真实 effect trace 验证 Agent skill 的隐藏越权行为；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Does Disaggregation Pay?](https://arxiv.org/html/2608.03741v1) | 2026-08-05T08:00:00+08:00 | 联合量化、设备内外并行与 PDAF 硬件异构，明确 disaggregation 收益依赖模型、互连和自定义 NPU；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Oilbird](https://arxiv.org/html/2608.03839v1) | 2026-08-05T08:00:00+08:00 | 用 verifier 已计算 hidden state 为历史 continuation 建语义地址，补足 exact suffix drafter 的 addressing gap；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Cross-Model KV Cache Transfer](https://arxiv.org/html/2608.03893v1) | 2026-08-05T08:00:00+08:00 | 将同模型家族切换的重复 prefill 改写为带配对约束、RoPE factoring 与 calibration 的 KV 映射问题；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Resume Means Resume](https://arxiv.org/html/2608.03836v1) | 2026-08-05T08:00:00+08:00 | 将 interrupt/resume 的 prefix continuation、exactly-once、fork、checkpoint validity 与 recovery 写成机器可检验合同；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |

## 4. 证据与知识整合

### [JudgeArena](https://arxiv.org/html/2608.02620v1)

正文把 instruction set、candidate、judge、prompt hash、backend、依赖和生成配置保存为一个自描述 run artifact，并以 human preference 做 meta-evaluation。它不能消除 judge bias，也不保证跨版本排名可比。Ch66 已有 `model × dataset × harness × environment × scorer` 的同一身份合同，保持已有覆盖。

### [TraceCompiler](https://arxiv.org/html/2608.02680v1)

系统从多条 noisy trace 中抽取 producer—consumer 数据依赖；只有 consumer 参数能唯一归因到 producer output 时才生成 hard edge，含糊关系保持 suspected，残余决策继续交给 LLM。证据只覆盖作者语料，且正文主动披露一组不可复现结果。Ch81 应把“轨迹编译”为带证据的降随机化过程：复用 workflow 不能把时间相邻冒充因果依赖，无法证明的边保留动态执行。

### [SeedRealtime](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction)

官方正文描述统一 audio-video-text architecture、原生 full-duplex、joint perception、主动交互与 tool call；展示与作者评测只证明其公开系统在披露场景中的表现，未披露项不能补造成通用 interrupt/safety guarantee。拟在 Ch23 时间与 modality identity 后加入：streaming representation 除 token 还必须绑定 timestamp、speaker/turn、interrupt frontier 与 observation freshness；生成器只能提议响应，duplex runtime 决定何时打断、丢弃或提交。

### [Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)

官方正文说明异步 background agent、append-only local event log 的 replay/restart，以及以 rejection-sampled harness trajectory 联合训练 model 与 coding harness。公开 benchmark 是厂商证据，不证明长期任务 exactly-once、权限延续或跨仓库普适。拟在 Ch84 AgentRun 生命周期之后加入：event log 保存可重放事实，model context 是派生视图；恢复必须重新核验 workspace revision、side effect 与 authorization，模型/脚手架 co-training 也要求 version-paired artifact。

### [Verified Tool Calls](https://arxiv.org/html/2608.02645v1)

§2 将 timeout-after-dispatch、delayed visibility 与 partial update 与二元成功/失败模型对照，§4～§5 在注入故障的模拟环境评估 wrapper。结果支持 verify-before-retry 与 idempotency，不证明真实工具都能提供可靠 postcondition。Ch78 已把 proposal、effect identity、commit、verification 与 retry 分开，正文无需重复。

### [MutMem](https://arxiv.org/html/2608.02843v1)

§2～§6 把每次非平凡 memory weight mutation 绑定 terminal provenance node、signer epoch、old/new quantized weight、no-fork predecessor 与签名；双端验证证明授权链完整，不证明存储内容为真。拟在 Ch77 derived-state 版本链加入 authorized mutation record 与 supersession；content truth 仍由 evidence/verifier 拥有，签名不能升级 epistemic authority。

### [AnchorKV](https://arxiv.org/html/2608.02901v1)

方法保留少量 exact anchor，将其他 token 表示为 anchor 加量化 residual，再按 attention-output 敏感度在字节预算内保留高价值 residual。20× 和 99% 只属于披露模型、数据与实现。Ch45 应把 anchor/residual 写成“全 token 可寻址、精度分层”的替代分支；anchor 选择或分布漂移失败时回退更高精度 residual 或 FullKV。

### [OPTD](https://arxiv.org/html/2608.02942v1)

few-step student 从自己生成的 partial state 出发，由冻结 teacher 找到 outcome-aligned future candidates，只提交保持 teacher rollout outcome 的最长前缀，并对其他位置施加 KL anchor。作者数学与代码 benchmark 不证明开放域稳定。Ch24 应说明 transition distillation 不能只在 teacher trajectory 上训练；压缩跨度是经一致性验证的 commit decision，验证失败回退更短 transition。

### [AcceptMoE](https://arxiv.org/html/2608.02989v1)

方法以每个 draft position 的离线提交概率加权 target-router demand，用有效秩自适应决定 verifier expert set，并结合 residency 做受预算裁剪。证据限 12 个 model-task pair。Ch48 应把 verifier 计算成本绑定实际可提交 token，而不是固定 block budget；裁剪不能移除 root token 的自然 top-k，风险超界回退完整 expert routing。

### [SparSEEty](https://arxiv.org/html/2608.02995v1)

§III～§V 说明攻击者从稀疏 neuron weight access 构造 activation oracle，再反演 token；TDX 实验只支持披露平台、模型与侧信道。拟在 Ch72 confidential serving 段补入：enclave 保护 memory contents 不等于隐藏 access pattern；动态稀疏收益必须与 constant-pattern/padding、隔离与性能代价共同评估。

### [Frequency- and Length-Aware Deduplication](https://arxiv.org/html/2608.03089v1)

§3 揭示 shard-local suffix array 会漏跨 shard 重复且 retention 受分片改变；§4 用自然边界、全局 exact hash aggregation 与显式 frequency/length budget 分离 detection 和 policy。模型结果只属于披露语料与训练规模。拟在 Ch27 数据去重段加入两阶段 owner：检测层产生 duplicate group identity，policy 层决定保留几份；数据 shard 变化不得静默改变 retention semantics。

### [LLaDA MoE v2](https://arxiv.org/html/2608.03457v1)

§3 的 IsoFLOP 与超参实验显示 diffusion MoE 的最佳 nominal batch 增长更快、learning rate 衰减更快，并在固定 activated capacity 下偏好更大 expert pool；§4 的 30B-A3B 训练是单一设计点。拟在 Ch28 scaling 段增加 Alternative Branch：AR 的最优 compute allocation 不能直接搬给 diffusion MoE，需按 objective/factorization 重新 sweep optimizer、data 与 routed capacity；不写成 diffusion 优于 AR。

### [SkillSentry](https://arxiv.org/html/2608.03485v1)

系统先推断 skill 声明的能力边界，在受控 honey world 中布置诱饵资源并自适应生成任务，再用 matched no-skill execution 和 source/trace 证明 effect 由 skill 导致。benchmark 指标不证明所有环境模拟真实。Ch72 应要求 skill 安全 verdict 同时具备声明边界、激活条件、真实 effect 与反事实对照；静态扫描仍是低成本前置层，动态执行失败时不能宣称安全。

### [When Does Disaggregation Pay?](https://arxiv.org/html/2608.03741v1)

§IV 的 simulator 联合 compute、interconnect、quantization 与 parallelization，结果中四路 PDAF 的优势依赖假设中的 custom NPU。Ch55 已明确 PD/PDAF 必须绑定模型结构、硬件比例、网络与 SLO，不采用未落地硬件的 headline speedup。

### [Oilbird](https://arxiv.org/html/2608.03839v1)

§3 将失败定位为历史池中有正确 continuation 但 exact suffix 无法寻址，§4 用 verifier hidden state 增加语义 draft source，§6 在三个 drafter 上验证。Ch48 已把它写为受验证器状态约束的替代 source，并保留 batch/pool/greedy 边界。

### [Cross-Model KV Cache Transfer](https://arxiv.org/html/2608.03893v1)

§2.3 先测 matched KV head/dimension 的跨模型线性结构，§3 对 key 去 RoPE、按 head 做 ridge mapping，并用 500 条 calibration sequence；六个 pair 中两个明显失败，恰好说明模型家族标签不够。拟在 Ch45 cache identity 后加入：跨模型 reuse 必须绑定 source/target layer map、KV shape、RoPE convention、calibration revision 与 acceptance test；失败 pair 回退 receiver re-prefill，不能把近似 KV 当 exact cache。

### [Resume Means Resume](https://arxiv.org/html/2608.03836v1)

论文把 prefix continuation、effect exactly-once、fork determinism、checkpoint validity、consume-once 与 recovery determinism写成机器检查合同，并对固定版本的五个 workflow framework 做 fault matrix。模型检查只在声明界限内成立。Ch81 应让 resume API 明确 effect ledger、fork intent 与并发消费语义；无法满足 exactly-once 时必须暴露 at-least-once，而不是用“持久化”掩盖差异。

## 5. 缺口与下一步

无

本窗没有可执行未决或外部材料请求。17 项候选均完成证据判断与 Books 决定。

## 6. 复核

复核者：独立复核智能体（2026-09-07）
结论：通过

复核纠正 7 项 false negative。以 656 个 official-announcement identity 为分母逐题摘重筛；17 项均复核原始正文、withdrawal、评分、证据边界与 owner。4 项已有覆盖真实，13 项长期机制均位于 canonical owner 的正文区。
