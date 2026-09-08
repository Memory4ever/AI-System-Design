# Daily Research — 2026-08-06

**规范：** V3
**窗口：** 2026-08-05T09:00:00+08:00 ～ 2026-08-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:30:00+08:00

## 1. 结论

本窗 arXiv Thursday 公告的宽身份数为 503；经逐项题摘语义筛选和独立漏项复核保留 16 个 Source Family。它们围绕 KV 量化、MoE optimizer state、VLA 闭环、评测、Agent skill、云边 speculation、split inference 与 world-model 训练等真实系统边界聚合。没有把通用视觉、机器人控制应用或单任务指标提升纳入候选。

16 项 v1 HTML 均重新打开并检查撤回状态。NOVA-KV、层级 VLA memory、成本感知评测预算与 MemoryCPT 的长期机制已有 Books 覆盖，Deltoris 只保留报告，其余 11 项完成正文整合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 按本窗及相邻日期检查，无符合范围的新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 相邻研究日期为 Jul28 与 Aug10 | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) Aug05 条目已在前一日报告判断，本窗无新增 | 已检查 | 无 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) Aug05 Muse 已在真实归属日处理，本窗无新增 | 已检查 | 无 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 按日期检查，本窗无相关正文 | 已检查 | 无 |
| SRC-DEEPSEEK | [Research](https://www.deepseek.com/) 与公开更新按日期检查，本窗无新机制正文 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [GitHub](https://github.com/MoonshotAI) 按发布时间检查，本窗无相关研究事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research) 中 Jul21 后下一条为 Aug11 | 已检查 | 无 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 中 Jun16 后下一条为 Aug14 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) 的 SeedRealtime 已归属 Aug05，本窗无新条目 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 按日期检查，最近记录早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) 论文与博客按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 相邻研究记录不落窗 | 已检查 | 无 |
| SRC-ARXIV | Thursday 08:00 北京时间公告；503 个宽身份作发现索引，逐项题摘语义筛选和独立漏项复核后保留 16 项并重开 v1 HTML | 已检查 | 无 |

本窗没有额外按需来源触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [NOVA-KV](https://arxiv.org/html/2608.04074v1) | 2026-08-06T08:00:00+08:00 | 从 attention-product distortion 推导 key/value transform，改变 2-bit KV 的误差目标而非只均衡元素方差；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Cost-Aware Multi-Objective Bandits](https://arxiv.org/html/2608.04333v1) | 2026-08-06T08:00:00+08:00 | 将配置评测建模为带异质成本、噪声与 Pareto 目标的预算分配；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MESH](https://arxiv.org/html/2608.04407v1) | 2026-08-06T08:00:00+08:00 | 以受控诊断证明 routed expert 的条件性梯度需要 temporal smoothing，不能直接套 dense stateless Sinkhorn；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Deltoris](https://arxiv.org/html/2608.04428v1) | 2026-08-06T08:00:00+08:00 | 将 VLA 连续输入相似性、bit sparsity、speculation 与专用 accelerator 联合设计；2 + 2 + 2 = 6 | 标准完成 | 仅报告：硬件模拟与特定 diffusion VLA 结果不足以改变通用章节结论 |
| [Inference Backend Side-effect](https://arxiv.org/html/2608.04714v1) | 2026-08-06T08:00:00+08:00 | 全交叉实验显示同一模型的 benchmark 结果受 backend、版本和 generation config 影响，纠正“分数只属于权重”的假设；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LoginTrap](https://arxiv.org/html/2608.04741v1) | 2026-08-06T08:00:00+08:00 | 把 web agent 的 login 从普通页面动作识别为独立认证边界，展示任务无关间接注入可诱导凭据泄露；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Explicit Language Memory for VLA](https://arxiv.org/html/2608.04765v1) | 2026-08-06T08:00:00+08:00 | 用 high-level language memory 与 low-level controller 分层解决 long-horizon 非 Markov 状态和纠错；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Closed-Loop Task-Vector Negation Audit](https://arxiv.org/html/2608.04692v1) | 2026-08-06T08:00:00+08:00 | 证明 VLA skill suppression 与未目标控制能力的 collateral damage 必须在闭环矩阵中共同评估；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Canary Tools](https://arxiv.org/html/2608.04719v1) | 2026-08-06T08:00:00+08:00 | 以六类可控诱饵把“选错工具”拆为可诊断的 reasoning failure；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Skill-Use](https://arxiv.org/html/2608.04828v1) | 2026-08-06T08:00:00+08:00 | 将 skill 能力拆成 Trigger、Compliance 与 Boundary，并以真实文件/沙箱 trajectory 评分；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MemoryCPT](https://arxiv.org/html/2608.04843v1) | 2026-08-06T08:00:00+08:00 | 联合离线构建、在线 retrieval/summarization 与 token 成本优化 Agent memory；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Causal Audit of Relayed KV](https://arxiv.org/html/2608.04893v1) | 2026-08-06T08:00:00+08:00 | 用 mismatched、zero 与 random cache 干预区分“有 cache 效果”和“传递了当前样例私有信息”；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [WorldCycle](https://arxiv.org/html/2608.04964v1) | 2026-08-06T08:00:00+08:00 | 以可逆 action cycle 产生无需未来真值的自验证长期一致性信号，改变 world model RL 的 verifier 设计；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [AsymSpec](https://arxiv.org/html/2608.04974v1) | 2026-08-06T08:00:00+08:00 | 在非对称云边网络中分离 acceptance-sufficient uplink、progressive correction 与 confirmed-prefix scheduling；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [RAC](https://arxiv.org/html/2608.04991v1) | 2026-08-06T08:00:00+08:00 | 以历史/同轮/预测 reference 加 residual quantization 压缩 split-inference 边界 activation；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Physics of Multimodal Pretraining](https://arxiv.org/html/2608.05000v1) | 2026-08-06T08:00:00+08:00 | 以合成控制和大规模训练拆分 modality knowledge flow、synergy/competition 与 early/late unification；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |

## 4. 证据与知识整合

### [Cost-Aware Multi-Objective Bandits](https://arxiv.org/html/2608.04333v1)

论文把每个 LLM configuration 视为成本不同、返回 noisy vector outcome 的 arm，分别求在线 hypervolume-per-cost 与预算内 Pareto set identification。理论和实验不证明给定业务目标可压成唯一 hypervolume。Ch66 已要求质量、成本、延迟在 hard constraints 内作 Pareto comparison，并把 adaptive evaluation 视为实验过程，保持已有覆盖。

### [NOVA-KV](https://arxiv.org/html/2608.04074v1)

§3 从 query statistics 下的 attention-product error 推导非正交 key transform 与 value transform，§4 再落到 fixed-width vector quantization；高分辨率近似和 calibration distribution 是前提。它不证明 2-bit 对任意模型/查询安全。Ch45 已将它作为“按 query-sensitive distortion 分配 bit”的实验分支，保留 full-KV fallback。

### [MESH](https://arxiv.org/html/2608.04407v1)

§3 在 110M MoE 上先复现 memory-efficient Sinkhorn 的质量退化，再把 routed expert matrix 定位为主要失败点；§4～§5 的 ablation 显示 matrix normalization 前的 temporal smoothing 是核心，full coordinate-wise AdamW state 并非唯一方法。规模很小，不能宣称替代 AdamW。拟在 Ch28 optimizer-state 段加入：conditional expert gradient 的生命周期不同于 dense matrix；减状态时至少保留跨 step 的一阶时间信号，并以 dense/AdamW 作为稳定 fallback。

### [Deltoris](https://arxiv.org/html/2608.04428v1)

§4～§6 将 temporal-aware bit sparsity、跨控制步 speculative loading 与 bit-serial PE 协同；报告的 34.2×/6.1× 依赖作者 accelerator model、VLA、精度和控制频率。它证明一个共同设计点，而非通用 runtime 规则；现有 Ch26/Ch49 已覆盖 freshness、speculation 与硬件耦合，保留日报即可。

### [Inference Backend Side-effect](https://arxiv.org/html/2608.04714v1)

§3 采用 3 模型 × 5 backend × 6 benchmark × 4 generation mode 全交叉，分开 backend、defaults 与 sampling noise；即使 greedy 也出现结构性差异。该结果只属于披露版本，不能说明任一 backend 更正确。拟在 Ch66 run identity 中将 backend name/version、tokenizer、generation defaults 与 deterministic kernel 一并冻结；“同权重”不再足以比较分数。

### [LoginTrap](https://arxiv.org/html/2608.04741v1)

§2.4 威胁模型允许攻击者控制页面上下文和诱导的登录流但不知道任务/agent internals，§3 fuzzing 生成 page-specific injection；实验的 86% 仅限所测 agent/defense。拟在 Ch72 web-agent trust boundary 中加入：authentication 是 effect-capability escalation，网页文本不能自行声明 login prerequisite；凭据填充需由可信 UI/identity broker 和用户授权，而非模型依据页面内容提交。

### [Explicit Language Memory for VLA](https://arxiv.org/html/2608.04765v1)

§3 用 high-level VLM 递归更新 temporal language memory/subtask，low-level VLA 只执行连续控制；simulation 与 sim-to-real 支持分层可行，不证明文本 memory 为环境真值。Ch26 已有相同 owner 分工、fresh observation 与 controller correction，新增论文名不会增加机制。

### [Closed-Loop Task-Vector Negation Audit](https://arxiv.org/html/2608.04692v1)

正文对目标 skill suppression、其余 skill survival 与多 skill composition 做完整闭环矩阵，并展示平均 cosine 或单层定位不能预测 collateral damage。结果随 suite、架构与系数变化，不能证明 weight subtraction 等于删除知识。Ch66 应要求模型编辑同时报告 target effect、control survival、跨架构外推与 relearning；只测目标下降不足以授权发布。

### [Canary Tools](https://arxiv.org/html/2608.04719v1)

方法在真实 tool set 中植入 semantic decoy、parameter trap、capability mirage、prerequisite blindness、temporal decoy 与 granularity trap，并用独立 judge/第二 judge 验证 outcome。8 个模型上的结果不构成通用安全等级。Ch66 应把 tool-selection failure 从单一 success rate 拆成可控 probe profile；canary 只能诊断 reasoning weakness，不能进入 production tool authority。

### [Skill-Use](https://arxiv.org/html/2608.04828v1)

benchmark 在 progressive disclosure 下分别测 agent 是否主动触发 skill、是否遵守 procedure、是否避免越界，并用真实文件、隔离沙箱与 trajectory rubric 验证。79 个 skills/177 个任务不覆盖所有生态。Ch66 应明确“skill 存在”不等于“被正确使用”：Trigger、Compliance、Boundary 要独立报告，outcome success 不能掩盖违规路径。

### [MemoryCPT](https://arxiv.org/html/2608.04843v1)

系统联合 query-agnostic memory construction、query-aware retrieval/summarization 与 cost-aware reward，说明 memory quality 与上下文成本应共同评测。其结果依赖教师、价格与数据。Ch77 已把 construction、retrieval、compression、token budget 与 evidence preservation 分开，保持已有覆盖。

### [Causal Audit of Relayed KV](https://arxiv.org/html/2608.04893v1)

§3 将 cache 替换为 deranged、zero、moment-matched random，并区分 receiver 是否需要 sender 私有信息；§4～§5 显示大 cache effect 有时几乎没有 pairing effect。拟在 Ch82 communication evidence 后加入：latent communication 的因果验收必须用 mismatched-example intervention，单纯 zero ablation 只证明 receiver 使用了某种 cache，不证明传递了正确 teammate state。

### [WorldCycle](https://arxiv.org/html/2608.04964v1)

Method 将 action sequence 与 inverse 组成 closed cycle，以 spatial closure 和 repeated-cycle temporal consistency 奖励训练；CycleBench 与实验只支持可逆、可表达的动作结构，不能把像素回归等同物理正确。拟在 Ch25 world-model verification 段加入：无未来真值时可从 known invariants 构造 self-verifiable loop，但不可逆动作、非对称动力学和隐藏状态必须退出该 reward contract。

### [AsymSpec](https://arxiv.org/html/2608.04974v1)

协议在常见接受路径只上传足够的候选信息，拒绝时由 downlink 渐进补充 residual distribution，并以 total-variation certificate 决定 top-k 是否足够；confirmed-prefix frontier 只调度独立有效请求。28.03× 属于作者网络与 pair。Ch48 应将网络消息也纳入 exact verification：证书失败必须逐级升级直至完整分布，不能 optimistic same-request runahead。

### [RAC](https://arxiv.org/html/2608.04991v1)

split inference 在本地—云—本地边界反复传 activation；RAC 以 exact-token 历史 span、同轮已重建状态和 causal predictor 建 reference，再编码对齐 residual，并由 sender 以 wire format 重建以保持下一轮同步。作者结果限 3 模型与 9 个链路 pair。Ch55 应把 boundary activation identity、reference revision、校准与 quality gate 纳入传输合同；reference miss 回退原始 activation。

### [Physics of Multimodal Pretraining](https://arxiv.org/html/2608.05000v1)

§3 的合成控制拆分跨模态 transfer，§4 比较 synergy/competition，后续 early-unification 与 13.5B MoE/2T token 验证提供规模证据。作者“5% compute”配方依赖其数据、tokenizer 与目标，不能外推。拟在 Ch23 shared space 段加入：shared attention/normalization 与 modality-specific FFN 是 capacity-sharing 分支；晚融合会产生 vision laziness，但早融合也带来目标竞争，选择取决于数据复杂度和模态预算。

## 5. 缺口与下一步

无

本窗没有可执行未决或外部材料请求。16 项候选均完成证据判断与 Books 决定。

## 6. 复核

复核者：独立复核智能体（2026-09-07）
结论：通过

复核纠正 7 项 false negative。以 503 个 official-announcement identity 为分母逐题摘重筛；16 项均复核 exact-v1、withdrawal、评分、证据边界与 owner。4 项已有覆盖真实，1 项仅报告边界合理，11 项长期机制均位于 canonical owner 的正文区。
