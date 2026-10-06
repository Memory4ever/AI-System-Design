# Daily Research — 2026-05-07

**规范：** V3
**窗口：** 2026-05-06T09:00:00+08:00 ～ 2026-05-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-15T12:35:00+08:00

## 1. 结论

第二次终审的 6 个明确 false negative 已全部恢复并完成 exact-v1 审阅；围绕同一错误关闭理由又定点复核 11 项，额外恢复 2605.04470、2605.05118 与 2605.05172，另外 8 项保留具体关闭理由。当前 active 账面为 **548 = 160 候选 + 387 关闭 + 1 撤回排除**；候选 Evidence 为 **156 完成、4 争议、0 待审**，Books 处置为 **63 整合、76 已有覆盖、17 仅报告、4 争议**。

`2605.04450` 已以 Ch54 现存旧标题 marker `SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING-` 作为 canonical family，并在 active ledger/packet 明确登记 `SF-2026-ARXIV-2605-04450` 与 `arxiv:2605.04450v1` alias；没有重复正文。本轮新增 7 项 Books 语义增量已由 root 写入正文。第三次非作者 fresh-context 终审确认这些正文的语义与边界成立；其指出的 7 项 exact-v1 locator、23 项旧 marker alias 与 29/29 Books comparison 漂移已完成限定返修，并由新的非作者终审逐项验证通过。日报已闭合。

arXiv ID/version、DataCite initial-created 与官方 Wednesday 20:00 EDT 共同支持 public-batch-derived **05-07 08:00**；这是批次推导，不是单篇页面直接披露。548 项 route 中 400 为 direct OAI corroboration、148 为 revision reconciliation，后者只有 72 项保存了 later OAI 日期，不能虚构其余均被 revision 覆盖。日期方法见[共享依据](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)。撤回 2605.04356 在 active ledger 只留最小排除。

## 2. 来源覆盖

已逐个重新访问每日机构入口，详细 endpoint、实际邻接日期、Seed 分页停止点与隔离 family 见[机构窗口复查](../_sources/daily-20260507/INSTITUTION_WINDOW_RECHECK.md)。DeepSeek、ERNIE、MiniMax 的当前可见历史目录已跨越窗口；Seed 读取 242 项目录的前两页至04-08，发现旧关闭依据漏项。NLA 与 Cola DLM 各保持单一跨截点隔离 identity，未计入当日分母；只有命中各自明确重开条件时才重新归属。访问失败与历史覆盖不足是明确 limitation，不写成“0候选且全站关闭”。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research；May6两条官方正文 | 已检查 | privacy guide/B2B Signals不准入；历史分页未穷尽 |
| SRC-ANTHROPIC | Research/NLA博客及primary paper | 已检查 | May7日级时间不足以归属 09:00 截点；family 已隔离并有明确重开条件 |
| SRC-GOOGLE-AI | Research/DeepMind官方目录与窗口查询 | 已检查 | 未重建完整日级历史；AI for Science暂停 |
| SRC-META-AI | Research两次读取 | 已检查 | 正文为空，无可用浏览器 |
| SRC-QWEN | 官方博客跳转qwen.ai | 已检查 | 旧目录停留2025，新入口无研究正文 |
| SRC-DEEPSEEK | 官方News/Research | 已检查 | 实际Feb25/Jun24与Apr24/Sep10跨窗，不泛化全站 |
| SRC-MOONSHOT | Kimi Platform Blog | 已检查 | 26可见项最新2025-11-07，不能覆盖2026 |
| SRC-TENCENT-HUNYUAN | Research/官方日期查询/浏览器尝试 | 已检查 | 空正文；No browser available |
| SRC-ZAI | Research两次timeout/官方日期查询 | 已检查 | 历史列表不可读，不沿用旧邻接声明 |
| SRC-BYTEDANCE-SEED | Publications API第1/2页至04-08 | 已检查 | 05-06 TDDFT暂停；Cola DLM目录回填日期不等于首次公开 |
| SRC-BAIDU-ERNIE | 官方博客实际May9/Apr30 | 已检查 | 仅可见官方博客范围 |
| SRC-XIAOMI-MIMO | 8 Papers/12 Blog cards | 已检查 | Paper Jun29/Mar13跨窗；Blog无日期 |
| SRC-MINIMAX | Blog实际May26/Mar18 | 已检查 | 仅可见官方博客范围 |
| SRC-ARXIV | 548身份；官方batch+DataCite初始+ID/version交叉 | 已检查 | 160候选；387 项有具体或分层关闭记录；current OAI revision不等于owner gap |

## 3. 候选与判断

公开时间为 public-batch-derived。分数针对本次拟采用的窄命题，不因已有 Books 或全文工作量反推。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [LCM: Lossless Context Management](https://arxiv.org/html/2605.04050v1) | 2026-05-07T08:00:00+08:00 | 把不可变原文、摘要 DAG 与检索/压缩策略拆成不同状态所有权，避免把有损摘要误当成事实记忆；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`AGENT-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-04050` 已承载“把不可变原文、摘要 DAG 与检索/压缩策略拆成不同状态所有权，避免把有损摘要误当成事实记忆”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [A Self-Attentive Meta-Optimizer with Group-Adaptive Learning Rates and Weight Decay](https://arxiv.org/html/2605.04055v1) | 2026-05-07T08:00:00+08:00 | 各参数组的梯度、动量与相关性统计可以驱动 group-wise learning-rate / weight-decay 调节，但元优化器自身增加训练状态、目标耦合与额外计算；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“各参数组的梯度、动量与相关性统计可以驱动 group-wise learning-rate / weight-decay 调节，但元优化器自身增加训练状态、目标耦合与额外计算”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [MP-ISMoE: Mixed-Precision Interactive Side Mixture-of-Experts for Efficient Transfer Learning](https://arxiv.org/html/2605.04058v1) | 2026-05-07T08:00:00+08:00 | 混合精度冻结主干释放出的显存可以转投 side-MoE 容量，但收益依赖量化误差、路由交互与任务分布；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch30 已把 frozen base、adapter capacity/precision、routing/composition 与 artifact identity 分开；本材料的窄命题“混合精度冻结主干释放出的显存可以转投 side-MoE 容量，但收益依赖量化误差、路由交互与任务分布”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-LORA`，[章节](../../../../books/part-04-training-system/30-lora.md)） |
| [Continual Distillation of Teachers from Different Domains](https://arxiv.org/html/2605.04059v1) | 2026-05-07T08:00:00+08:00 | 连续蒸馏时旧 teacher 不再可访问；外部无标签数据保留其 logits，分离新知识迁移与旧知识遗忘，因此需要比较仅当前 teacher 蒸馏和保留旧响应的取舍。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“连续蒸馏时旧 teacher 不再可访问；外部无标签数据保留其 logits，分离新知识迁移与旧知识遗忘，因此需要比较仅当前 teacher 蒸馏和保留旧响应的取舍。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [Single-Position Intervention Fails: Distributed Output Templates Drive In-Context Learning](https://arxiv.org/html/2605.04061v1) | 2026-05-07T08:00:00+08:00 | 单位置 probe 可读不等于单位置具有因果控制力；ICL task template 由跨位置、跨层的分布式状态共同承载；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；Ch14 已写入单位置可解码不等于因果控制，以及跨位置/跨层分布式 task template 的受限边界。（`MODEL-SELF-ATTENTION`，[章节](../../../../books/part-02-model/14-self-attention.md)） |
| [EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation](https://arxiv.org/html/2605.04062v1) | 2026-05-07T08:00:00+08:00 | 低于 4-bit 压缩受质量/重训代价约束；混合精度结构量化、层自适应特征蒸馏和熵调 KL 联合提供新的低比特执行分支，需对齐硬件与训练预算。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“低于 4-bit 压缩受质量/重训代价约束；混合精度结构量化、层自适应特征蒸馏和熵调 KL 联合提供新的低比特执行分支，需对齐硬件与训练预算。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [Free Energy-Driven Reinforcement Learning with Adaptive Advantage Shaping for Unsupervised Reasoning in LLMs](https://arxiv.org/html/2605.04065v1) | 2026-05-07T08:00:00+08:00 | 无监督推理不能固定奖励/探索分配；FER 的自由能信号与 AAS 的 advantage 统计调整提供新的训练信号控制分支，须核查是否超出已有熵奖励。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch33 已把 group sampling、advantage aggregation、reward/verifier、exploration 与 bounded optimizer update 分开；本材料的窄命题“无监督推理不能固定奖励/探索分配；FER 的自由能信号与 AAS 的 advantage 统计调整提供新的训练信号控制分支，须核查是否超出已有熵奖励。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning](https://arxiv.org/html/2605.04066v1) | 2026-05-07T08:00:00+08:00 | 固定 policy 聚合/clip 不随训练能力变化；power-mean 目标在算术/几何均值间切换并反馈调 clip，改变 RLVR 更新控制。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch33 已把 group sampling、advantage aggregation、reward/verifier、exploration 与 bounded optimizer update 分开；本材料的窄命题“固定 policy 聚合/clip 不随训练能力变化；power-mean 目标在算术/几何均值间切换并反馈调 clip，改变 RLVR 更新控制。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [LAWS: Learning from Actual Workloads Symbolically -- A Self-Certifying Parametrized Cache Architecture for Neural Inference, Robotics, and Edge Deployment](https://arxiv.org/html/2605.04069v1) | 2026-05-07T08:00:00+08:00 | 参数化expert cache需要可核验validity domain；本文的自认证证明存在未控制后缀与归一化界疑问，不能采用其部署正确性保证。；**2 + 1 + 1 = 4** | 争议 | 暂缓：Disputed；LAWS 的 self-certification 尚未控制后缀与 LayerNorm validity boundary；只有作者给出可核验的修订证明或等价勘误后才重开，当前不得支持 Books。 |
| [Toward Human-AI Complementarity Across Diverse Tasks](https://arxiv.org/html/2605.04070v1) | 2026-05-07T08:00:00+08:00 | 高风险 human-oversight routing 不能把模型 confidence 当作错误可识别性；应先测 AI 与人的错误重叠、互补区域和人类纠错能力，再决定 route 或 assistance。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：Ch66 已明确自报/内部 confidence 只是需按 deployment slice 校准的 sensor，高风险 route/defer 还需外部证据、human adjudication 与 risk-coverage；本结果为该命题提供受限反证，但不改变 owner 或 fallback。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction](https://arxiv.org/html/2605.04075v1) | 2026-05-07T08:00:00+08:00 | 多模态 KV eviction 可从离散删除转为 uncertainty-aware 的连续 state-space memory evolution，但要承担状态近似与恢复误差；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch45 已把 KV identity、保留/压缩/驱逐、恢复误差与 correctness fallback 绑定；本材料的窄命题“多模态 KV eviction 可从离散删除转为 uncertainty-aware 的连续 state-space memory evolution，但要承担状态近似与恢复误差”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-KV-CACHE`，[章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)） |
| [Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO](https://arxiv.org/html/2605.04077v1) | 2026-05-07T08:00:00+08:00 | 指出 loss reduction 本身会重写 credit 权重：token aggregation 偏向长序列，sequence aggregation 又压低长响应；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-GRPO` 正文中的 `SF-2026-ARXIV-2605-04077` 已承载“指出 loss reduction 本身会重写 credit 权重：token aggregation 偏向长序列，sequence aggregation 又压低长响应”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [Validity-Calibrated Reasoning Distillation](https://arxiv.org/html/2605.04078v1) | 2026-05-07T08:00:00+08:00 | 固定模仿 teacher 路径会忽略 student 当前状态；同一 prefix 下比较两者下一步 validity 再分配蒸馏强度，改变逐步监督的选择。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“固定模仿 teacher 路径会忽略 student 当前状态；同一 prefix 下比较两者下一步 validity 再分配蒸馏强度，改变逐步监督的选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [AsymmetryZero: A Framework for Operationalizing Human Expert Preferences as Semantic Evals](https://arxiv.org/html/2605.04083v1) | 2026-05-07T08:00:00+08:00 | Evaluation 必须冻结 criterion、judge procedure 与 aggregation；聚合后 task score 稳定可能掩盖 criterion-level jury dissent，低成本 jury 不能未经 human anchor 就取得同等判定权。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：Ch66 已把 per-criterion outcomes、judge/rater identity、aggregation function、disagreement 和 release authority 分权保存；该 source family 强化了 aggregation masking 边界，但未改变现有 contract。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression](https://arxiv.org/html/2605.04084v1) | 2026-05-07T08:00:00+08:00 | calibration-free product quantization 把 weight compression 变成子空间 codebook 与目标 kernel 的联合选择，但不能省略模型质量和执行格式验收；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“calibration-free product quantization 把 weight compression 变成子空间 codebook 与目标 kernel 的联合选择，但不能省略模型质量和执行格式验收”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [OpenCLAW-Nexus: A Self-Reinforcing Trust Framework for Byzantine-Resilient Decentralized Federated Learning](https://arxiv.org/html/2605.04091v1) | 2026-05-07T08:00:00+08:00 | 无可信根的异构联邦学习不能依赖固定可信聚合者；折扣 Beta reputation 联合客户端选择、RepFedAvg 与 BFT，需核查 Byzantine/Sybil 假设下的训练信任边界。；**2 + 2 + 2 = 6** | 标准完成 | 仅报告：证据属于去中心化联邦学习的 reputation/BFT 协议，依赖其 Byzantine/Sybil 与 honest-majority 假设；未改变本书 LLM distributed-training 的 collective、parallel state 或 checkpoint contract。 |
| [Regularized Centered Emphatic Temporal Difference Learning](https://arxiv.org/html/2605.04100v1) | 2026-05-07T08:00:00+08:00 | 直接中心化 emphatic TD 可能破坏关键矩阵正定性；仅正则辅助变量的修复改变稳定算法构造，结论限该线性 TD 设定而非所有 RL。；**3 + 1 + 2 = 6** | 标准完成 | 仅报告：结论是有限线性 off-policy TD 的正定性修复，不是 RLHF/RLVR 的生成 policy、reward 或 rollout 机制，不能据类比改写 TRAIN-RLHF。 |
| [TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments](https://arxiv.org/html/2605.04107v1) | 2026-05-07T08:00:00+08:00 | TSCG 将 JSON tool schema 确定性编译为 token-efficient structured text，直接改变 schema 表征、压缩和 tool-selection 输入；它不提供 validator、adapter 或 effect-side correctness。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch78 已把 schema/argument proposal、deterministic validation、authorization 与 effect receipt 分层；本材料的窄命题“TSCG 将 JSON tool schema 确定性编译为 token-efficient structured text，直接改变 schema 表征、压缩和 tool-selection 输入；它不提供 validator、adapter 或 effect-side correctness。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-TOOL-CALLING`，[章节](../../../../books/part-07-agent/78-tool-calling.md)） |
| [Learning reveals invisible structure in low-rank RNNs](https://arxiv.org/html/2605.04115v1) | 2026-05-07T08:00:00+08:00 | 相同已实现函数不意味着相同后续学习动力学；低秩 RNN 中 loss-invisible 状态承载训练历史，改变仅由当前 loss/输出判断可塑性的解释。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：低秩 RNN 中 loss-invisible state 的理论结果不证明 Transformer residual stream 或 LLM 训练动力学存在同一机制。 |
| [Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering](https://arxiv.org/html/2605.04116v1) | 2026-05-07T08:00:00+08:00 | retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04116` 已承载“retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [Frontier Lag: A Bibliometric Audit of Capability Misrepresentation in Academic AI Evaluation](https://arxiv.org/html/2605.04135v1) | 2026-05-07T08:00:00+08:00 | capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-2026-ARXIV-2605-04135` 已承载“capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [FlowEval: Reference-based Evaluation of Generated User Interfaces](https://arxiv.org/html/2605.04165v1) | 2026-05-07T08:00:00+08:00 | 生成式 UI 评价应把静态外观与可执行 interaction flow 分开；reference trace 是可诊断 evidence，但 metric、CUA 与 reference coverage 都必须属于 evaluation identity。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已要求以可执行 environment transition、artifact 与 human anchor 评价 agent，不让 judge 取代 outcome；FlowEval 是 UI trace 的受限实例，未改变现有 evaluation owner。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures](https://arxiv.org/html/2605.04178v1) | 2026-05-07T08:00:00+08:00 | GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [MedFabric and EtHER: A Data-Centric Framework for Word-Level Fabrication Generation and Detection in Medical LLMs](https://arxiv.org/html/2605.04180v1) | 2026-05-07T08:00:00+08:00 | 真假文本来自不同作者会把风格线索混入 factuality 评价；v1 将真答案同样改写为 LLM 风格并约束伪造局部改词，观察 detector 随风格/结构对齐退化，要求用配对风格控制检验事实检测能力。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“真假文本来自不同作者会把风格线索混入 factuality 评价；v1 将真答案同样改写为 LLM 风格并约束伪造局部改词，观察 detector 随风格/结构对齐退化，要求用配对风格控制检验事实检测能力。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions](https://arxiv.org/html/2605.04209v1) | 2026-05-07T08:00:00+08:00 | 在 Sparse-PCA 硬度与 margin/dither 假设下，FC 预测头的后门参数与 Gaussian-dithered clean 参考计算不可区分；不是相对原模型的统计不可区分，也未建立语言触发器可行性。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04209` 已承载“在 Sparse-PCA 硬度与 margin/dither 假设下，FC 预测头的后门参数与 Gaussian-dithered clean 参考计算不可区分；不是相对原模型的统计不可区分，也未建立语言触发器可行性。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [The Anatomy of Silent Data Corruption: GPU Error Pattern Study and Modeling Guidance](https://arxiv.org/html/2605.04213v1) | 2026-05-07T08:00:00+08:00 | silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-MONITORING` 正文中的 `SF-2026-ARXIV-2605-04213` 已承载“silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-MONITORING`，[章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)） |
| [Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs](https://arxiv.org/html/2605.04215v1) | 2026-05-07T08:00:00+08:00 | fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`MULTIMODAL-GENERATIVE-PARADIGMS` 正文中的 `SF-2026-ARXIV-2605-04215` 已承载“fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MULTIMODAL-GENERATIVE-PARADIGMS`，[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)） |
| [Jordan-RoPE: Non-Semisimple Relative Positional Encoding via Complex Jordan Blocks](https://arxiv.org/html/2605.04217v1) | 2026-05-07T08:00:00+08:00 | RoPE phase 与 ALiBi 距离通道不能表示所有耦合；Jordan block 生成距离调制 phase，且稳定 shear 破坏群律，改变位置基函数与数值稳定的取舍。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch13 已把位置基函数、相对距离、外推与数值稳定性写成替代分支；本材料的窄命题“RoPE phase 与 ALiBi 距离通道不能表示所有耦合；Jordan block 生成距离调制 phase，且稳定 shear 破坏群律，改变位置基函数与数值稳定的取舍。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-POSITION-ENCODING`，[章节](../../../../books/part-02-model/13-position-encoding.md)） |
| [Layerwise LQR for Geometry-Aware Optimization of Deep Networks](https://arxiv.org/html/2605.04230v1) | 2026-05-07T08:00:00+08:00 | 结构化 preconditioner 提早丢弃跨层几何；dense quadratic step 的 layerwise LQR 等价式给出参考，再学习可复用的近似逆，改变二阶优化近似评价。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“结构化 preconditioner 提早丢弃跨层几何；dense quadratic step 的 layerwise LQR 等价式给出参考，再学习可复用的近似逆，改变二阶优化近似评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [Adaptive Consensus in LLM Ensembles via Sequential Evidence Accumulation: Automatic Budget Identification and Calibrated Commit Signals](https://arxiv.org/html/2605.04236v1) | 2026-05-07T08:00:00+08:00 | ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Temporal Reasoning Is Not the Bottleneck: A Probabilistic Inconsistency Framework for Neuro-Symbolic QA](https://arxiv.org/html/2605.04243v1) | 2026-05-07T08:00:00+08:00 | 事件结构抽取缺失可能使一致性检测沉默；PIS区间公式与‘表示而非推理是唯一瓶颈’尚无足够解释，仅保留诊断问题，不采用通用结论。；**2 + 1 + 1 = 4** | 争议 | 暂缓：Disputed；credal interval 的 coverage 前提与论文对 temporal inconsistency 的解释尚未对齐；需修订正文明确 posterior/coverage 条件并复算结论后才重开。 |
| [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/html/2605.04251v1) | 2026-05-07T08:00:00+08:00 | 漏洞补丁通过 oracle 不等于修复根因；动态定位多样化、加权证据排名与 root-cause 评价改变 repair 验收目标。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“漏洞补丁通过 oracle 不等于修复根因；动态定位多样化、加权证据排名与 root-cause 评价改变 repair 验收目标。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks](https://arxiv.org/html/2605.04256v1) | 2026-05-07T08:00:00+08:00 | 异构物理神经基底不能被压平成无状态 tool；control plane 必须暴露 capability、时钟、生命周期、遥测、校准与安全状态，并把 twin state 与真实 substrate execution 分权管理。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch83 已有唯一正文明确物理 capability 不能被普通 MCP tool schema 压平，并保留 calibration、safety、人工审批与 substrate adapter 边界；本轮恢复账本绑定，没有重复正文。（`AGENT-MCP`，[章节](../../../../books/part-07-agent/83-mcp.md)） |
| [Laundering AI Authority with Adversarial Examples](https://arxiv.org/html/2605.04261v1) | 2026-05-07T08:00:00+08:00 | VLM 的感知差异可被攻击者用来借模型权威背书外部观察者看到的另一内容，使视觉输入成为 effect-side trust boundary；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：Ch72 已明确多模态输入的 provenance/语义通道必须由独立 policy adjudicate，模型输出只是 proposal 而非 authority；视觉感知错配是该 trust-boundary 的受限攻击实例。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [Parallel Prefix Verification for Speculative Generation](https://arxiv.org/html/2605.04263v1) | 2026-05-07T08:00:00+08:00 | semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`INFER-SPECULATIVE-DECODING` 正文中的 `SF-2026-ARXIV-2605-04263` 已承载“semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`INFER-SPECULATIVE-DECODING`，[章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)） |
| [Explaining and Preventing Alignment Collapse in Iterative RLHF](https://arxiv.org/html/2605.04266v1) | 2026-05-07T08:00:00+08:00 | iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-2026-ARXIV-2605-04266` 已承载“iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [Adapt or Forget: Provable Tradeoffs Between Adam and SGD in Nonstationary Optimization](https://arxiv.org/html/2605.04269v1) | 2026-05-07T08:00:00+08:00 | 非平稳目标下 Adam 的历史矩估计会变成 stale state；优化器选择取决于 gradient noise 与 objective drift 的相对主导；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-PRETRAINING` 正文中的 `SF-2026-ARXIV-2605-04269` 已承载“非平稳目标下 Adam 的历史矩估计会变成 stale state；优化器选择取决于 gradient noise 与 objective drift 的相对主导”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [Gradient Flow Structure and Quantitative Dynamics of Multi-Head Self-Attention](https://arxiv.org/html/2605.04279v1) | 2026-05-07T08:00:00+08:00 | 多头 Attention 的总能量可具有梯度流结构，但单头演化仍经共享 token state 和球面投影发生 radial-shadow 耦合；head 正交不等于优化动力学独立。；**3 + 1 + 3 = 7** | 深入完成 | 整合：已落实；Ch15 已写入共享 token trajectory 与 radial-shadow coupling，使 head 正交不再被误解为逐 head 动力学独立；Radial Dominance 仅保留为受限充分条件。（`MODEL-MULTI-HEAD-ATTENTION`，[章节](../../../../books/part-02-model/15-multi-head-attention.md)） |
| [Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion](https://arxiv.org/html/2605.04291v1) | 2026-05-07T08:00:00+08:00 | 离散 text diffusion 可把预训练 causal/masked LM 作为能量/条件分布来定义 Glauber transition，并以迭代局部重写换取全局修正；这与均匀 corruption 的从零训练是不同分支。；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；Ch24 已写入复用预训练 causal/masked LM 条件分布定义 Glauber-style 局部 transition 的分支，并保留有限步非稳态、NFE、streaming 与 AR fallback。（`MULTIMODAL-GENERATIVE-PARADIGMS`，[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)） |
| [LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy](https://arxiv.org/html/2605.04295v1) | 2026-05-07T08:00:00+08:00 | 选择性拒答需要区分P(accept\|correct)与P(correct\|accept)；本文把两者混用，不能采用其风险保证。；**2 + 1 + 1 = 4** | 争议 | 暂缓：Disputed；ACSE 对两个条件概率的叙述存在混淆；需 exact-v1 勘误并在同一 calibration split 上复算 coverage/risk 后才重开。 |
| [SWAN: Semantic Watermarking with Abstract Meaning Representation](https://arxiv.org/html/2605.04305v1) | 2026-05-07T08:00:00+08:00 | token-level watermark 在改写下易失效；AMR 语义结构嵌入及 parser 检测提供不同 provenance 机制，需核查语义保持与解析误差。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch72 已把 threat model、untrusted input/artifact、model sensor、authorization、effect 与 rollback 分层；本材料的窄命题“token-level watermark 在改写下易失效；AMR 语义结构嵌入及 parser 检测提供不同 provenance 机制，需核查语义保持与解析误差。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping](https://arxiv.org/html/2605.04308v1) | 2026-05-07T08:00:00+08:00 | 新知识通常靠权重更新并承担遗忘；Markov token 状态扩展与 token-to-dictionary embedding tuning 给出保留旧转移的条件，需限定模型化假设而非承诺真实 LLM 零遗忘。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：一阶 Markov token-to-dictionary 构造只覆盖其样本效率理论，未建立现代 LLM embedding、参数知识或外部 memory 的更新机制。 |
| [Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games](https://arxiv.org/html/2605.04312v1) | 2026-05-07T08:00:00+08:00 | 多智能体对局生成的新鲜任务可以同时缓解 benchmark 饱和与训练污染，但测到的是特定 game policy 下的相对能力；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“多智能体对局生成的新鲜任务可以同时缓解 benchmark 饱和与训练污染，但测到的是特定 game policy 下的相对能力”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [The Scaling Properties of Implicit Deductive Reasoning in Transformers](https://arxiv.org/html/2605.04330v1) | 2026-05-07T08:00:00+08:00 | 隐式推理的规模泛化不等于深度泛化；Horn-clause 受控任务分离图宽度/拓扑与深度外推，改变何时需要显式 CoT 的判断。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch14 已把 Q/K/V 内容路由、跨位置聚合、causal mask 与后续组合层职责分开；本材料的窄命题“隐式推理的规模泛化不等于深度泛化；Horn-clause 受控任务分离图宽度/拓扑与深度外推，改变何时需要显式 CoT 的判断。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-SELF-ATTENTION`，[章节](../../../../books/part-02-model/14-self-attention.md)） |
| [Resilient AI Supercomputer Networking using MRC and SRv6](https://arxiv.org/html/2605.04333v1) | 2026-05-07T08:00:00+08:00 | large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale；**2 + 3 + 2 = 7** | 深入完成 | 整合：已落实；`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-2026-ARXIV-2605-04333` 已承载“large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-DISTRIBUTED-TRAINING`，[章节](../../../../books/part-04-training-system/36-distributed-training.md)） |
| [Budgeted LoRA: Distillation as Structured Compute Allocation for Efficient Inference](https://arxiv.org/html/2605.04341v1) | 2026-05-07T08:00:00+08:00 | parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-LORA` 正文中的 `SF-2026-ARXIV-2605-04341` 已承载“parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-LORA`，[章节](../../../../books/part-04-training-system/30-lora.md)） |
| [Perturbation is All You Need for Extrapolating Language Models](https://arxiv.org/html/2605.04344v1) | 2026-05-07T08:00:00+08:00 | 精确前缀条件预测受经验支持域限制；先扰动到语义邻居的 pre/post additive-noise 模型给出外推条件，改变采样/输入扰动的适用解释。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：perturbation extrapolation 依赖强 support-bridging 假设，未给出可迁移到开放语言分布的 sampling/runtime contract。 |
| [Covariance-Aware Goodness for Scalable Forward-Forward Learning](https://arxiv.org/html/2605.04346v1) | 2026-05-07T08:00:00+08:00 | 全局反向传播和保存全网 activation 不是唯一训练契约；block-local goodness 可通过协方差统计、边界对齐和可配置梯度 horizon，在内存、跨层协同与准确率之间形成连续取舍。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch28 已解释 BP activation memory 与 checkpoint/recompute，但缺少改变梯度 ownership 的 block-local 训练分支；应补入从全局 BP 到可配置 gradient horizon 的演进，并保留端到端 BP fallback。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [Coral: Cost-Efficient Multi-LLM Serving over Heterogeneous Cloud GPUs](https://arxiv.org/html/2605.04357v1) | 2026-05-07T08:00:00+08:00 | heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`INFER-SCHEDULING` 正文中的 `SF-2026-ARXIV-2605-04357` 已承载“heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`INFER-SCHEDULING`，[章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)） |
| [When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration](https://arxiv.org/html/2605.04361v1) | 2026-05-07T08:00:00+08:00 | context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；`AGENT-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-04361` 已承载“context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [Mitigating Label Shift in Tabular In-Context Learning via Test-Time Posterior Adjustment](https://arxiv.org/html/2605.04363v1) | 2026-05-07T08:00:00+08:00 | tabular ICL 受 context 类别先验偏移影响；test-time posterior/prior rescaling 无需重训，改变 label-shift 校准选择。；**3 + 1 + 2 = 6** | 标准完成 | 仅报告：tabular ICL 的 label-shift posterior adjustment 只在所测表格分类设定成立，未改变 LLM evaluation 或 in-context state owner。 |
| [Worst-Case Discovery and Runtime Protection for RL-Based Network Controllers](https://arxiv.org/html/2605.04373v1) | 2026-05-07T08:00:00+08:00 | 平均任务奖励不保证最坏情形 runtime 安全；bilevel regret 搜索反例再编译 counterfactual 干预规则，改变保护层如何从失败样本构造。；**2 + 2 + 2 = 6** | 标准完成 | 仅报告：这是 RL 网络控制器的 worst-case discovery/protection 机制，不是 VLA/Embodied 的 perception-action schema、物理 transition 或 safety envelope 证据。 |
| [Critical Windows of Complexity Control: When Transformers Decide to Reason or Memorize](https://arxiv.org/html/2605.04396v1) | 2026-05-07T08:00:00+08:00 | regularization timing creates a critical training window that changes the reasoning-versus-memorization basin；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“regularization timing creates a critical training window that changes the reasoning-versus-memorization basin”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [Counterfactual identifiability beyond global monotonicity: non-monotone triangular structural causal models](https://arxiv.org/html/2605.04413v1) | 2026-05-07T08:00:00+08:00 | 非单调具身动力学的 counterfactual identifiability 不要求全局 monotonicity；triangular recursion 下还需 mechanism-wise invertibility 与 context-independent inverse transport，局部可逆本身不足。；**3 + 2 + 3 = 8** | 深入完成 | 整合：已落实；Ch25 已区分 predictive continuation 与 unrestricted counterfactual contract，也提醒 structured factorization 不等于 causal identification；尚缺非单调 triangular 机制下的充分条件与“局部可逆仍不足”反例。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [Demystifying Manifold Constraints in LLM Pre-training](https://arxiv.org/html/2605.04418v1) | 2026-05-07T08:00:00+08:00 | explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-PRETRAINING` 正文中的 `SF-DEMYSTIFYING-MANIFOLD-CONSTRAINTS-IN-LLM-PRE-TRAINING` 已承载“explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning](https://arxiv.org/html/2605.04421v1) | 2026-05-07T08:00:00+08:00 | 离散 attention 与连续 RNN 的组合缺少统一状态解释；attention-logit ODE 及门控极限连接 SDPA/CT-RNN，提供可核验的 sink 控制设计分支。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch14 已把 Q/K/V 内容路由、跨位置聚合、causal mask 与后续组合层职责分开；本材料的窄命题“离散 attention 与连续 RNN 的组合缺少统一状态解释；attention-logit ODE 及门控极限连接 SDPA/CT-RNN，提供可核验的 sink 控制设计分支。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-SELF-ATTENTION`，[章节](../../../../books/part-02-model/14-self-attention.md)） |
| [Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting](https://arxiv.org/html/2605.04426v1) | 2026-05-07T08:00:00+08:00 | 固定比率 token 删除会丢关系；原子事实行与符号语义重写同时形成压缩和寻址索引，改变压缩单位而非仅换摘要 prompt。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch75 已把不可变 source、active context、derived summary、回读与丢失 fallback 分权；本材料的窄命题“固定比率 token 删除会丢关系；原子事实行与符号语义重写同时形成压缩和寻址索引，改变压缩单位而非仅换摘要 prompt。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning](https://arxiv.org/html/2605.04431v1) | 2026-05-07T08:00:00+08:00 | RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO` 已承载“RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [Misrouter: Exploiting Routing Mechanisms for Input-Only Attacks on Mixture-of-Experts LLMs](https://arxiv.org/html/2605.04446v1) | 2026-05-07T08:00:00+08:00 | MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-MISROUTER-EXPLOITING-ROUTING-MECHANISMS-FOR-INPUT-ONLY-ATTACKS-ON-MIXTUR` 已承载“MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving](https://arxiv.org/html/2605.04450v1) | 2026-05-07T08:00:00+08:00 | 当 embedding hot cache 与 KV cache 竞争同一 HBM 时，静态分池会随 workload regime 变化而失效；memory allocator 与 request router 必须共享同一容量、迁移与 tail-SLO contract。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch54 已写入 EMB/KV 双 cache 共享 HBM 时 allocator 与 router 的联合控制，并保留迁移提交、P99、burst failure 与静态分区回退边界。（`INFER-GPU-MEMORY`，[章节](../../../../books/part-05-inference-system/54-gpu-memory.md)） |
| [Deployment-Relevant Alignment Cannot Be Inferred from Model-Level Evaluation Alone](https://arxiv.org/html/2605.04454v1) | 2026-05-07T08:00:00+08:00 | deployment claims require interaction and scaffold evidence rather than model-only scores；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“deployment claims require interaction and scaffold evidence rather than model-only scores”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Stream-T1: Test-Time Scaling for Streaming Video Generation](https://arxiv.org/html/2605.04461v1) | 2026-05-07T08:00:00+08:00 | 整段视频 TTS 候选探索昂贵且缺 temporal guidance；chunk noise 继承、跨窗 reward pruning 与奖励驱动被逐出 KV 的更新路径，提供 streaming 特有的质量/状态成本选择。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch24 已把 AR/diffusion 的 factorization、iterative state、correction、commit 与 runtime handoff 分开；本材料的窄命题“整段视频 TTS 候选探索昂贵且缺 temporal guidance；chunk noise 继承、跨窗 reward pruning 与奖励驱动被逐出 KV 的更新路径，提供 streaming 特有的质量/状态成本选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MULTIMODAL-GENERATIVE-PARADIGMS`，[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)） |
| [KEET: Explaining Performance of GPU Kernels Using LLM Agents](https://arxiv.org/html/2605.04467v1) | 2026-05-07T08:00:00+08:00 | Nsight 指标多不等于可操作瓶颈解释；由 profile 数据约束 agent 解释并测下游优化效果，需核其新增证据反馈能否改变 kernel 优化循环。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“Nsight 指标多不等于可操作瓶颈解释；由 profile 数据约束 agent 解释并测下游优化效果，需核其新增证据反馈能否改变 kernel 优化循环。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [Stabilizing LLM Supervised Fine-Tuning via Explicit Distributional Control](https://arxiv.org/html/2605.04468v1) | 2026-05-07T08:00:00+08:00 | current model 与冻结 SFT reference 插值得到 dynamic anchor，内层离线蒸馏近似拟合；改变 SFT 目标轨迹的控制，代价为额外 forward/memory，不是全局 retention 保证。；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-SFT` 正文中的 `SF-STABILIZING-LLM-SUPERVISED-FINE-TUNING-VIA-EXPLICIT-DISTRIBUTIONAL-CONTR` 已承载“current model 与冻结 SFT reference 插值得到 dynamic anchor，内层离线蒸馏近似拟合；改变 SFT 目标轨迹的控制，代价为额外 forward/memory，不是全局 retention 保证。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies](https://arxiv.org/html/2605.04470v1) | 2026-05-07T08:00:00+08:00 | 具身策略 post-training 可把 dense 但有偏的 counterfactual supervision 当 proxy，再用稀疏但 grounded 的真实 closed-loop event 学 residual correction；两者必须在同一 on-policy visited-state distribution 下对齐。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch26 已区分 learned proposal、closed-loop observation 与 safety commit，但缺少 dense biased proxy 与 sparse grounded residual 的同分布组合，以及保留 pretrained behavior 的 teacher boundary。（`MULTIMODAL-EMBODIED-VLA`，[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)） |
| [Data-dependent Exploration for Online Reinforcement Learning from Human Feedback](https://arxiv.org/html/2605.04477v1) | 2026-05-07T08:00:00+08:00 | online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN-` 已承载“online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](https://arxiv.org/html/2605.04478v1) | 2026-05-07T08:00:00+08:00 | 跨 host/kernel 的 rank probes 与 collective trace 支撑慢/挂根因定位；诊断证据不等于自动 remediation 的正确性或权限。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-CCL-D-A-HIGH-PRECISION-DIAGNOSTIC-SYSTEM-FOR-SLOW-AND-HANG-ANOMALIES-IN-` 已承载“跨 host/kernel 的 rank probes 与 collective trace 支撑慢/挂根因定位；诊断证据不等于自动 remediation 的正确性或权限。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-DISTRIBUTED-TRAINING`，[章节](../../../../books/part-04-training-system/36-distributed-training.md)） |
| [Towards General Preference Alignment: Diffusion Models at Nash Equilibrium](https://arxiv.org/html/2605.04494v1) | 2026-05-07T08:00:00+08:00 | BT 标量偏好不能表达一般扩散偏好；self-play Nash 目标替代 reward-induced preference，改变 diffusion alignment 的目标建模。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch34 已把 preference pair、reference identity、relative margin、update sensor 与独立行为评估分权；本材料的窄命题“BT 标量偏好不能表达一般扩散偏好；self-play Nash 目标替代 reward-induced preference，改变 diffusion alignment 的目标建模。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-DPO`，[章节](../../../../books/part-04-training-system/34-dpo.md)） |
| [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](https://arxiv.org/html/2605.04495v1) | 2026-05-07T08:00:00+08:00 | 文档相关性不等于生成器有用性；query-only 稳定性为 control 估计 passage 边际影响，再最小 Kendall 修正排名，改变检索/生成衔接且不把稳定性当正确率。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch76 已把 query、chunk、retrieval candidate、sufficient evidence 与 evaluator 分开；本材料的窄命题“文档相关性不等于生成器有用性；query-only 稳定性为 control 估计 passage 边际影响，再最小 Kendall 修正排名，改变检索/生成衔接且不把稳定性当正确率。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-RAG`，[章节](../../../../books/part-07-agent/76-rag.md)） |
| [SCOUT: Active Information Foraging for Long-Text Understanding with Decoupled Epistemic States](https://arxiv.org/html/2605.04496v1) | 2026-05-07T08:00:00+08:00 | long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`AGENT-CONTEXT` 正文中的 `SF-SCOUT-ACTIVE-INFORMATION-FORAGING-FOR-LONG-TEXT-UNDERSTANDING-WITH-DECOU` 已承载“long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [Distilling Bayesian Belief States into Language Models for Auditable Negotiation](https://arxiv.org/html/2605.04507v1) | 2026-05-07T08:00:00+08:00 | 可校准 belief 文本不等于因果 belief-conditioned action；Bayesian teacher 蒸馏与 posterior-prefix 干预分离报告和控制，改变 agent 可解释性验收。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“可校准 belief 文本不等于因果 belief-conditioned action；Bayesian teacher 蒸馏与 posterior-prefix 干预分离报告和控制，改变 agent 可解释性验收。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [From Priors to Perception: Grounding Video-LLMs in Physical Reality](https://arxiv.org/html/2605.04515v1) | 2026-05-07T08:00:00+08:00 | 视频物理错误可能混入生成 artifacts 或常识先验；物理程序生成对抗课程分离视觉事实与叙事先验，改变物理 reasoning 评价和监督。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch25 已区分生成 observation、action-conditioned dynamics、imagined rollout、真实 transition 与 planning authority；本材料的窄命题“视频物理错误可能混入生成 artifacts 或常识先验；物理程序生成对抗课程分离视觉事实与叙事先验，改变物理 reasoning 评价和监督。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks](https://arxiv.org/html/2605.04525v1) | 2026-05-07T08:00:00+08:00 | 长时域具身规划可把探索性强但迭代慢的 diffusion 放在高层 sparse subgoal，把快速 rectified flow 放在低层 dense trajectory，并由在线 MPC 持续重规划。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch26 已有多时间尺度 controller 与 diffusion/flow action head，但尚未把两种生成范式按高层探索/低层实时性分权，也未写清 manifold projection、MPC replan 与 inverse-dynamics handoff。（`MULTIMODAL-EMBODIED-VLA`，[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)） |
| [SADE: Symptom-Aware Diagnostic Escalation for LLM-Based Network Troubleshooting](https://arxiv.org/html/2605.04530v1) | 2026-05-07T08:00:00+08:00 | 自由 ReAct 混合收集证据与承诺根因；phase-gated escalation 在同 backend 对照下提高诊断，改变工具诊断 workflow 的可行性判断。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch81 已把 phase state、retry/rollback、escalation 与 commit authority 组织为 durable workflow；本材料的窄命题“自由 ReAct 混合收集证据与承诺根因；phase-gated escalation 在同 backend 对照下提高诊断，改变工具诊断 workflow 的可行性判断。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-WORKFLOW`，[章节](../../../../books/part-07-agent/81-workflow.md)） |
| [RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization](https://arxiv.org/html/2605.04539v1) | 2026-05-07T08:00:00+08:00 | 偏好胜率会奖励冗长而不保证 entailment；NLI/verifier 混合信号及相反 judge 排序改变知识生成的偏好目标和评价。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch34 已把 preference pair、reference identity、relative margin、update sensor 与独立行为评估分权；本材料的窄命题“偏好胜率会奖励冗长而不保证 entailment；NLI/verifier 混合信号及相反 judge 排序改变知识生成的偏好目标和评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-DPO`，[章节](../../../../books/part-04-training-system/34-dpo.md)） |
| [Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation](https://arxiv.org/html/2605.04542v1) | 2026-05-07T08:00:00+08:00 | 逐 token power sampling 不等于序列分布幂变换；后缀信息与 true-reward/self-reward 协方差决定收益，改变温度自奖励的理论解释。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch20 已把 token distribution、sampling policy、calibration 与 sequence-level evaluation 分开；本材料的窄命题“逐 token power sampling 不等于序列分布幂变换；后缀信息与 true-reward/self-reward 协方差决定收益，改变温度自奖励的理论解释。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-SAMPLING`，[章节](../../../../books/part-02-model/20-sampling.md)） |
| [UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding](https://arxiv.org/html/2605.04543v1) | 2026-05-07T08:00:00+08:00 | 将多步、多 draft 的接受问题写为 conditional optimal transport，在给定 prefix 下构造接受方案；不是只重述 proposal-verification-commit 状态机。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch48 已把 proposal、exact verification、accepted prefix 与 rollback/commit 分权；本材料的窄命题“将多步、多 draft 的接受问题写为 conditional optimal transport，在给定 prefix 下构造接受方案；不是只重述 proposal-verification-commit 状态机。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-SPECULATIVE-DECODING`，[章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)） |
| [RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs](https://arxiv.org/html/2605.04563v1) | 2026-05-07T08:00:00+08:00 | Range Identifier 把显存错误保护从逐 bit 正确性改为数值范围内的有界近似恢复，新增了可声明的误差 contract；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`INFER-TENSORRT-LLM` 正文中的 `SF-RANGEGUARD-EFFICIENT-BOUNDED-APPROXIMATE-ERROR-CORRECTION-FOR-RELIABLE-D` 已承载“Range Identifier 把显存错误保护从逐 bit 正确性改为数值范围内的有界近似恢复，新增了可声明的误差 contract”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination](https://arxiv.org/html/2605.04568v1) | 2026-05-07T08:00:00+08:00 | 在可微 latent world model 上通过梯度 MPC 优化动作，并与 gradient-free 计划比较；不能由该结果推导 uncertainty 为所有 latent planning 的必要条件。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch25 已区分生成 observation、action-conditioned dynamics、imagined rollout、真实 transition 与 planning authority；本材料的窄命题“在可微 latent world model 上通过梯度 MPC 优化动作，并与 gradient-free 计划比较；不能由该结果推导 uncertainty 为所有 latent planning 的必要条件。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/html/2605.04569v1) | 2026-05-07T08:00:00+08:00 | 动态稀疏 Attention 不应只按 token saliency 剪枝；execution plan 可依据 query-specific approximation-risk proxy，在 full attention 与低阶近似路径之间逐块路由并保留 exact fallback。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch49 已写入 query-specific approximation-risk 驱动 full/Taylor sparse attention 的条件执行分支；proxy 只提出路径，runtime 与 full attention fallback 保留提交权。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [From Parameter Dynamics to Risk Scoring : Quantifying Sample-Level Safety Degradation in LLM Fine-tuning](https://arxiv.org/html/2605.04572v1) | 2026-05-07T08:00:00+08:00 | fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-FROM-PARAMETER-DYNAMICS-TO-RISK-SCORING-QUANTIFYING-SAMPLE-LEVEL-SAFETY-` 已承载“fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://arxiv.org/html/2605.04595v1) | 2026-05-07T08:00:00+08:00 | KV capacity and queue stability must be analyzed together under arrival and service contracts；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch45 已把 KV identity、保留/压缩/驱逐、恢复误差与 correctness fallback 绑定；本材料的窄命题“KV capacity and queue stability must be analyzed together under arrival and service contracts”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-KV-CACHE`，[章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)） |
| [Temporal Structure Matters for Efficient Test-Time Adaptation in Wearable Human Activity Recognition](https://arxiv.org/html/2605.04617v1) | 2026-05-07T08:00:00+08:00 | 把 vision TTA 平滑直接套流式传感会错过状态转换；feature surprise 按 prototype 几何决定惯性保持/释放，提供无反传在线适配机制，适用范围限 WHAR。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：wearable activity recognition 的 temporal test-time adaptation 属于领域模型方法，未改变 LLM SFT 数据、objective 或 artifact lifecycle。 |
| [AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair](https://arxiv.org/html/2605.04624v1) | 2026-05-07T08:00:00+08:00 | repair selector 使用 evaluator signal 形成测量 coupling；channel-blocking 配对对照可改变方法排名，要求分离用于选择与用于独立验收的信号。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-AUDITREPAIRBENCH-A-PAIRED-EXECUTION-TRACE-CORPUS-FOR-EVALUATOR-CHANNEL-R` 已承载“repair selector 使用 evaluator signal 形成测量 coupling；channel-blocking 配对对照可改变方法排名，要求分离用于选择与用于独立验收的信号。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies](https://arxiv.org/html/2605.04637v1) | 2026-05-07T08:00:00+08:00 | Coding-agent 平台评价必须区分从零创建与修改既有系统，并沿 requirements、artifact、runtime、operations 与 security 保存分阶段 evidence，避免漂亮 UI 掩盖后端和生产失败。；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：Ch66 已区分 static issue、从零 repository、需求访问、完整 artifact、测试、部署/安全与 environment identity，并要求分阶段 evidence；该 68-metric benchmark 提供实例，但未改变现有主线。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Gradients with Respect to Semantics Preserving Embeddings Tell the Uncertainty of Large Language Models](https://arxiv.org/html/2605.04638v1) | 2026-05-07T08:00:00+08:00 | 把白盒 gradient signal 作为 hallucination sensor，而不是把生成概率直接当作事实置信度；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“把白盒 gradient signal 作为 hallucination sensor，而不是把生成概率直接当作事实置信度”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving](https://arxiv.org/html/2605.04647v1) | 2026-05-07T08:00:00+08:00 | 具身 action token 可以先并行 draft、再原位 edit，但 revision 必须和 full-rollout RL credit、mutable action cache invalidation 及最终 controller commit 同时设计。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch26 已讨论 action chunk、fast/slow controller 与 warm-start/refinement，但缺少同一离散 action space 的 draft/edit authority、full-rollout credit 以及编辑后 cache rewind/recompute 的一致性边界。（`MULTIMODAL-EMBODIED-VLA`，[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)） |
| [FAAST: Forward-Only Associative Learning via Closed-Form Fast Weights for Test-Time Supervised Adaptation](https://arxiv.org/html/2605.04651v1) | 2026-05-07T08:00:00+08:00 | 新例子适配通常支付反传或长 context 成本；单遍把带标签例子编译进 fast weights，提供冻结表征下不同训练/推理成本分配。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“新例子适配通常支付反传或长 context 成本；单遍把带标签例子编译进 fast weights，提供冻结表征下不同训练/推理成本分配。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs](https://arxiv.org/html/2605.04665v1) | 2026-05-07T08:00:00+08:00 | semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation；**3 + 1 + 2 = 6** | 深入完成 | 整合：已落实；`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-PARAPHRASE-INDUCED-OUTPUT-MODE-COLLAPSE-WHEN-LLMS-BREAK-CHARACTER-UNDER-` 已承载“semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement](https://arxiv.org/html/2605.04677v1) | 2026-05-07T08:00:00+08:00 | LLM 代码优化应把 runtime profile 当作 target-selection evidence，把候选 edit 当作 proposal；只有通过 build、tests、performance 与静态检查的 artifact 才能进入搜索 population。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch81 已把 proposal、typed artifact、deterministic checks、retry/rollback 与 commit authority 分离；Ch49 已要求 profile→plan→correctness fallback。CodeEvolve 是受限组合实例，无需复制框架正文。（`AGENT-WORKFLOW`，[章节](../../../../books/part-07-agent/81-workflow.md)） |
| [From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models](https://arxiv.org/html/2605.04678v1) | 2026-05-07T08:00:00+08:00 | latent action supervision changes the representation bridge between pixels, language and controllable action；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`MULTIMODAL-EMBODIED-VLA` 正文中的 `SF-FROM-PIXELS-TO-TOKENS-A-SYSTEMATIC-STUDY-OF-LATENT-ACTION-SUPERVISION-FO` 已承载“latent action supervision changes the representation bridge between pixels, language and controllable action”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MULTIMODAL-EMBODIED-VLA`，[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)） |
| [Average Attention Transformers and Arithmetic Circuits](https://arxiv.org/html/2605.04683v1) | 2026-05-07T08:00:00+08:00 | attention 计算能力不能只用通用逼近描述；average hard attention 与特定 arithmetic-circuit 家族的双向模拟界定其表示能力，须保留替代 FFN 等假设。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：average-attention arithmetic circuits 是受限函数类/构造性理论，不证明标准 Transformer 的实际 attention state 或训练机制。 |
| [Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization](https://arxiv.org/html/2605.04700v1) | 2026-05-07T08:00:00+08:00 | 音频 token 对齐梯度高度非均匀，使少数 waveform 区域足以承载 jailbreak 优化，也暴露多模态安全评测的稀疏攻击面；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch72 已把 image/audio encoder、跨模态 adversarial robustness 与最终 effect authorization 分开；白盒稀疏 waveform 优化补充攻击样式，但不改变安全 owner 或 fallback。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC](https://arxiv.org/html/2605.04709v1) | 2026-05-07T08:00:00+08:00 | visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`MULTIMODAL-WORLD-MODELS` 正文中的 `SF-ELVIS-ENSEMBLE-CALIBRATED-LATENT-IMAGINATION-FOR-LONG-HORIZON-VISUAL-MPC` 已承载“visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [Budget-aware Auto Optimizer Configurator](https://arxiv.org/html/2605.04711v1) | 2026-05-07T08:00:00+08:00 | optimizer state 可依据各 block 的 gradient stream 风险，在统一 memory/time budget 下做配置分配，而不是全模型固定 recipe；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-PRETRAINING` 正文中的 `SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR` 已承载“optimizer state 可依据各 block 的 gradient stream 风险，在统一 memory/time budget 下做配置分配，而不是全模型固定 recipe”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-PRETRAINING`，[章节](../../../../books/part-04-training-system/28-pretraining.md)） |
| [SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning](https://arxiv.org/html/2605.04712v1) | 2026-05-07T08:00:00+08:00 | 增加专家不保证持续 RL 可塑性；expert feature 的谱 proxy 与 Parseval penalty 针对 spectral plasticity loss，改变 MoE 正则选择。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch21 已把 router、expert capacity、placement、communication 与 overflow fallback 联合建模；本材料的窄命题“增加专家不保证持续 RL 可塑性；expert feature 的谱 proxy 与 Parseval penalty 针对 spectral plasticity loss，改变 MoE 正则选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-MOE`，[章节](../../../../books/part-02-model/21-moe.md)） |
| [Every Step Counts: Step-Level Credit Assignment for Tool-Integrated Text-to-SQL](https://arxiv.org/html/2605.04719v1) | 2026-05-07T08:00:00+08:00 | tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT-` 已承载“tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols](https://arxiv.org/html/2605.04727v1) | 2026-05-07T08:00:00+08:00 | attention-enhanced 模型优势可能来自序列时间泄漏和设置差异；时间排序/固定跨折超参后差距缩小，改变 sequential learner 比较的有效性条件。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“attention-enhanced 模型优势可能来自序列时间泄漏和设置差异；时间排序/固定跨折超参后差距缩小，改变 sequential learner 比较的有效性条件。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization](https://arxiv.org/html/2605.04738v1) | 2026-05-07T08:00:00+08:00 | 激活/权重 outlier 不必总靠在线 rotation/scaling；Hessian 稳定零空间的 additive suppression 可离线吸收，改变低比特量化的执行负担。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“激活/权重 outlier 不必总靠在线 rotation/scaling；Hessian 稳定零空间的 additive suppression 可离线吸收，改变低比特量化的执行负担。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [Knowledge-Free Correlated Agreement for Incentivizing Federated Learning](https://arxiv.org/html/2605.04747v1) | 2026-05-07T08:00:00+08:00 | FL 客户贡献奖励通常依赖公开 test/标签；categorical reports 与 honest majority 下的 KFCA 修复 label-flipping 激励，提供不同信任假设。；**2 + 2 + 2 = 6** | 标准完成 | 仅报告：federated-learning incentive 的 correlated-agreement 结论依赖其参与者与信号假设，未改变 LLM distributed runtime 的更新语义。 |
| [AxMoE: Characterizing the Impact of Approximate Multipliers on Mixture-of-Experts DNN Architectures](https://arxiv.org/html/2605.04754v1) | 2026-05-07T08:00:00+08:00 | 近似乘法器稳健性不能从 CNN 推到 ViT 或 dense 推到 MoE；架构与重训条件下的排序反转改变硬件近似的质量验收。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“近似乘法器稳健性不能从 CNN 推到 ViT 或 dense 推到 MoE；架构与重训条件下的排序反转改变硬件近似的质量验收。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study](https://arxiv.org/html/2605.04763v1) | 2026-05-07T08:00:00+08:00 | 语法函数边界并非默认最佳 code chunk；864 受控设置中 function chunking 不占 Pareto 前沿，改变 chunking 与 context budget 的联合选择。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch76 已把 query、chunk、retrieval candidate、sufficient evidence 与 evaluator 分开；本材料的窄命题“语法函数边界并非默认最佳 code chunk；864 受控设置中 function chunking 不占 Pareto 前沿，改变 chunking 与 context budget 的联合选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-RAG`，[章节](../../../../books/part-07-agent/76-rag.md)） |
| [Elicitation Matters: How Prompts and Query Protocols Shape LLM Surrogates under Sparse Observations](https://arxiv.org/html/2605.04764v1) | 2026-05-07T08:00:00+08:00 | LLM surrogate 的 prompt/逐点或联合查询不是格式细节；不确定性对齐与 downstream regret 受协议改变，要求把 elicitation 计入 surrogate 定义。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“LLM surrogate 的 prompt/逐点或联合查询不是格式细节；不确定性对齐与 downstream regret 受协议改变，要求把 elicitation 计入 surrogate 定义。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use](https://arxiv.org/html/2605.04785v1) | 2026-05-07T08:00:00+08:00 | tool calls require runtime interception and effect-side safety checks；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch78 已把 schema/argument proposal、deterministic validation、authorization 与 effect receipt 分层；本材料的窄命题“tool calls require runtime interception and effect-side safety checks”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-TOOL-CALLING`，[章节](../../../../books/part-07-agent/78-tool-calling.md)） |
| [DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/html/2605.04808v1) | 2026-05-07T08:00:00+08:00 | Agent red-team 必须绑定可重放的环境状态转换、注入/威胁身份与 effect-side judge，不能把静态 prompt 成功率外推到真实 workflow；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已要求冻结环境 revision、真实 transition/effect receipt，并把模拟器与 judge 限定为测量工具；本材料补充实例但不改变该命题。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/html/2605.04811v1) | 2026-05-07T08:00:00+08:00 | multi-agent memory requires tree-structured credit assignment over shared and delegated state changes；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`AGENT-MEMORY` 正文中的 `SF-TREE-BASED-CREDIT-ASSIGNMENT-FOR-MULTI-AGENT-MEMORY-SYSTEM` 已承载“multi-agent memory requires tree-structured credit assignment over shared and delegated state changes”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-MEMORY`，[章节](../../../../books/part-07-agent/77-memory.md)） |
| [Concurrence of Symmetry Breaking and Nonlocality Phase Transitions in Diffusion Models](https://arxiv.org/html/2605.04830v1) | 2026-05-07T08:00:00+08:00 | 局部 denoising 可用性与语义分岔常被分开分析；DiT 中两个 critical time 接近提供何时需要 conditioning/global compute 的诊断。；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`MULTIMODAL-GENERATIVE-PARADIGMS` 正文中的 `SF-2026-ARXIV-2605-04830` 已承载“局部 denoising 可用性与语义分岔常被分开分析；DiT 中两个 critical time 接近提供何时需要 conditioning/global compute 的诊断。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MULTIMODAL-GENERATIVE-PARADIGMS`，[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)） |
| [Agentic Repository Mining: A Multi-Task Evaluation](https://arxiv.org/html/2605.04845v1) | 2026-05-07T08:00:00+08:00 | Repository context 的选择是条件分支：预工程 context 在规模可控时更快；自主探索在 artifact 超窗或 taxonomy 不完整时更稳健，但增加工具步骤、错误和时延。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch75 已明确小仓库/完整工作集可直接拼接，大仓库应按 task 与 repository revision 定点检索，并把 retrieval confidence 与事实充分性分开；本结果没有改变该条件分支。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [Uncertainty-Aware Exploratory Direct Preference Optimization for Multimodal Large Language Models](https://arxiv.org/html/2605.04874v1) | 2026-05-07T08:00:00+08:00 | 多模态 DPO 可用 token-level epistemic uncertainty 重分配偏好学习压力，但该信号仍由训练中模型自估并可能失准；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch34 已把 token/pair geometry 视为 update sensor，并要求 preference truth、chosen likelihood、KL 与 optimizer commit 分权；模型自估视觉 uncertainty 未经独立校准，不足以形成新的 DPO 长期机制。（`TRAIN-DPO`，[章节](../../../../books/part-04-training-system/34-dpo.md)） |
| [Self-Attention as Transport: Limits of Symmetric Spectral Diagnostics](https://arxiv.org/html/2605.04893v1) | 2026-05-07T08:00:00+08:00 | attention 谱诊断存在 orientation-blind 的可证明不可辨识边界，因此 hallucination sensor 必须区分 transport capacity 与 flow orientation；**3 + 1 + 3 = 7** | 深入完成 | 已有覆盖：Ch66 已规定 attention/probe 等内部量只能作为需校准的 sensor，不能取得 truth authority；orientation-blind 的谱不可辨识定理强化这一边界，但不改变 evaluation contract。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [SynConfRoute: Syntax-Aware Routing for Efficient Code Completion with Small CodeLLMs](https://arxiv.org/html/2605.04894v1) | 2026-05-07T08:00:00+08:00 | 逐请求 model routing 不能只读生成置信度；应把模型 sensor 与可验证的 domain signal 组合，再在 local accept、large-model escalation 与 privacy/cost 之间决策。；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：Ch56 已规定 confidence 只是 proposal，router 应从可验证局部 observation 更新 belief，并由 SLO/风险 controller 决定 accept/escalate；syntax validity 是该原则的代码域实例，不新增 owner。（`INFER-SCHEDULING`，[章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)） |
| [Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall](https://arxiv.org/html/2605.04897v1) | 2026-05-07T08:00:00+08:00 | durable storage is not usable memory without retrieval, admission and update ownership；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch77 已把 immutable episode、derived view、retriever 与 truth authority 分离，并明确保存不等于可召回；本架构是受限实现案例。（`AGENT-MEMORY`，[章节](../../../../books/part-07-agent/77-memory.md)） |
| [On the (In-)Security of the Shuffling Defense in the Transformer Secure Inference](https://arxiv.org/html/2605.04901v1) | 2026-05-07T08:00:00+08:00 | 反证 activation shuffling 足以保护模型机密性：恶意客户端可利用暴露的中间表示恢复服务器权重；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04901` 已承载“反证 activation shuffling 足以保护模型机密性：恶意客户端可利用暴露的中间表示恢复服务器权重”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](https://arxiv.org/html/2605.04913v1) | 2026-05-07T08:00:00+08:00 | local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN` 已承载“local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [Reinforcement Learning for Compositional Generalization with Outcome-Level Optimization](https://arxiv.org/html/2605.04920v1) | 2026-05-07T08:00:00+08:00 | token-level 模仿可能偏重训练组合；outcome RL 与 binary/composite reward 对照检验组合泛化，改变 SFT/RL 的目标选择边界。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch33 已按 outcome 可验证性、credit horizon 与 execution replay 讨论何时选择 terminal/group reward；该结果未改变现有条件分支。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation](https://arxiv.org/html/2605.04922v1) | 2026-05-07T08:00:00+08:00 | 多 Agent 并行修订不能让 role-local 文本直接覆盖共享真值；各角色应在同一 frozen snapshot 上形成 typed patch，固定顺序 materialize 后再由 graph-global commit 判断是否进入最终 artifact。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch81 已写入同轮角色基于 frozen graph snapshot 提案、typed patch 验证、确定性 materialization 与 graph-global commit 的状态链，并保留顺序 barrier 回退。（`AGENT-WORKFLOW`，[章节](../../../../books/part-07-agent/81-workflow.md)） |
| [Adaptive Inverted-Index Routing for Granular Mixtures-of-Experts](https://arxiv.org/html/2605.04952v1) | 2026-05-07T08:00:00+08:00 | 细粒度 MoE 的全专家打分会抵消稀疏计算收益；VQ shortlist 后做受限精确 router，改变路由精度与执行成本边界。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch21 已把 router、expert capacity、placement、communication 与 overflow fallback 联合建模；本材料的窄命题“细粒度 MoE 的全专家打分会抵消稀疏计算收益；VQ shortlist 后做受限精确 router，改变路由精度与执行成本边界。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-MOE`，[章节](../../../../books/part-02-model/21-moe.md)） |
| [KernelBenchX: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels](https://arxiv.org/html/2605.04956v1) | 2026-05-07T08:00:00+08:00 | generated GPU kernels need fixed-contract correctness and performance evaluation across architectures；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-2026-ARXIV-2605-04956` 已承载“generated GPU kernels need fixed-contract correctness and performance evaluation across architectures”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](https://arxiv.org/html/2605.04957v1) | 2026-05-07T08:00:00+08:00 | 图耦合会破坏普通 conformal 的 exchangeability；条件高频谱分解提供不同校准机制，需把交通图结果限定为图预测而非通用 LLM coverage。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：graph time-series conformal prediction 只重申 non-exchangeability 条件，不提供 LLM evaluation 的新 estimator、release gate 或 truth authority。 |
| [EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance](https://arxiv.org/html/2605.04960v1) | 2026-05-07T08:00:00+08:00 | GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-GRPO` 正文中的 `SF-EP-GRPO-ENTROPY-PROGRESS-ALIGNED-GROUP-RELATIVE-POLICY-OPTIMIZATION-WITH` 已承载“GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [Skill Neologisms: Towards Skill-based Continual Learning](https://arxiv.org/html/2605.04970v1) | 2026-05-07T08:00:00+08:00 | 独立技能适配常需改权重或堆 context；冻结模型的 soft-vocabulary skill tokens 可单独训练再组合，改变技能更新与组合的参数界面。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“独立技能适配常需改权重或堆 context；冻结模型的 soft-vocabulary skill tokens 可单独训练再组合，改变技能更新与组合的参数界面。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [Why Geometric Continuity Emerges in Deep Neural Networks: Residual Connections and Rotational Symmetry Breaking](https://arxiv.org/html/2605.04971v1) | 2026-05-07T08:00:00+08:00 | 跨层几何连续性不能仅归于非线性；保旋转非线性反例分离 residual 梯度相干与对称破缺，改变 activation/norm 角色解释。；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`MODEL-TRANSFORMER-LAYER` 正文中的 `SF-2026-ARXIV-2605-04971` 已承载“跨层几何连续性不能仅归于非线性；保旋转非线性反例分离 residual 梯度相干与对称破缺，改变 activation/norm 角色解释。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MODEL-TRANSFORMER-LAYER`，[章节](../../../../books/part-02-model/17-transformer-layer.md)） |
| [Why Expert Alignment Is Hard: Evidence from Subjective Evaluation](https://arxiv.org/html/2605.04972v1) | 2026-05-07T08:00:00+08:00 | 显式专家 criteria 未必能稳定提升对齐；专家/样本身份/评价维度的受限证据挑战只增加 rubric 的策略，需区分主观异质性与模型错误。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66/Ch31 已把 rubric、rater identity、disagreement 与 release authority 分离；该小样本结果只提供受限反例。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Conceptors for Semantic Steering](https://arxiv.org/html/2605.04980v1) | 2026-05-07T08:00:00+08:00 | inference-time semantic steering 不必把概念压成单一方向；由 bipolar activations 估计的 soft projection subspace 可保留多维结构，并通过 Boolean composition 形成更丰富但仍需校准的控制 artifact。；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；Ch20 已把 hidden-state control vector 绑定 checkpoint、layer、window 与阈值，但默认仍是单方向 artifact；缺少多维 soft-projection、layer quota sensor 和组合操作的替代分支。（`MODEL-SAMPLING`，[章节](../../../../books/part-02-model/20-sampling.md)） |
| [Self-Induced Outcome Potential: Turn-Level Credit Assignment for Agents without Verifiers](https://arxiv.org/html/2605.04984v1) | 2026-05-07T08:00:00+08:00 | turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`TRAIN-RLHF` 正文中的 `SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W` 已承载“turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-RLHF`，[章节](../../../../books/part-04-training-system/31-rlhf.md)） |
| [You Snooze, You Lose: Automatic Safety Alignment Restoration through Neural Weight Translation](https://arxiv.org/html/2605.04992v1) | 2026-05-07T08:00:00+08:00 | safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-SECURITY` 正文中的 `SF-YOU-SNOOZE-YOU-LOSE-AUTOMATIC-SAFETY-ALIGNMENT-RESTORATION-THROUGH-NEURA` 已承载“safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [Adaptivity Under Realizability Constraints: Comparing In-Context and Agentic Learning](https://arxiv.org/html/2605.04995v1) | 2026-05-07T08:00:00+08:00 | 自适应查询优势不必在实现约束后保留；ReLU realizability 下四类构造分离 adaptive querying 与表示能力，改变 agent 学习理论解释。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch79 已把 adaptive search 设为有观测价值、预算与 verifier 条件的分支，并保留 static plan；理论构造强化边界但不改变 owner 结论。（`AGENT-PLANNING`，[章节](../../../../books/part-07-agent/79-planning.md)） |
| [Misaligned by Reward: Socially Undesirable Preferences in LLMs](https://arxiv.org/html/2605.05003v1) | 2026-05-07T08:00:00+08:00 | reward model 的通用指令偏好分数不能代替社会域 preference audit；bias avoidance 与 context faithfulness 还可能相互冲突；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66/Ch31 已要求 rubric/rater/domain 版本化并禁止 scalar reward 取得 truth authority；无新增长期机制。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/html/2605.05007v1) | 2026-05-07T08:00:00+08:00 | multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`AGENT-MULTI-AGENT` 正文中的 `SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION` 已承载“multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-MULTI-AGENT`，[章节](../../../../books/part-07-agent/82-multi-agent.md)） |
| [Learned Neighbor Trust for Collaborative Deployment in Model-Agnostic Decentralized Learning](https://arxiv.org/html/2605.05009v1) | 2026-05-07T08:00:00+08:00 | 异构分散模型不能默认互相可信；同一验证 trust gate 同时控制辅助蒸馏与部署 ensemble，改变训练和推理共享信任信号的设计。；**2 + 2 + 2 = 6** | 标准完成 | 仅报告：decentralized model collaboration 的 neighbor-trust 证据限其网络/reputation 设定，未改变集中式或并行 LLM training 的状态所有权。 |
| [Position: Embodied AI Requires a Privacy-Utility Trade-off](https://arxiv.org/html/2605.05017v1) | 2026-05-07T08:00:00+08:00 | Embodied privacy 不是 perception 阶段的单点遮蔽，而是从 instruction、sensing、planning 到 interaction 的 lifecycle control signal；privacy level 改变会沿闭环传播为 utility 与可达 action 的变化。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch72 已把 privacy 从静态存储扩展到端到端 observable data flow，并按 embodied supply/perception/world-state/planning/action 等 trust boundary 分责；SPINE 提供生命周期实例，但不改变现有 owner、threat-model 或 fail-closed contract。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels](https://arxiv.org/html/2605.05023v1) | 2026-05-07T08:00:00+08:00 | 把已有专家 kernel 提升为 executable IR，再由模型提出结构变化并经 lowering/verifier 落回可运行实现；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`INFER-TENSORRT-LLM` 正文中的 `SF-2026-ARXIV-2605-05023` 已承载“把已有专家 kernel 提升为 executable IR，再由模型提出结构变化并经 lowering/verifier 落回可运行实现”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`INFER-TENSORRT-LLM`，[章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)） |
| [Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals](https://arxiv.org/html/2605.05025v1) | 2026-05-07T08:00:00+08:00 | 采样一致性 UQ 有多次 decode 成本；attention 对均匀分布的 KL probe 提供单 pass 替代，需与低成本首 token/语义梯度 sensor 同协议比较。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“采样一致性 UQ 有多次 decode 成本；attention 对均匀分布的 KL probe 提供单 pass 替代，需与低成本首 token/语义梯度 sensor 同协议比较。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models](https://arxiv.org/html/2605.05026v1) | 2026-05-07T08:00:00+08:00 | 扩散结构幻觉不仅可用 mode interpolation 解释；局部内在维数与 IQ 抑制提供另一诊断/纠正分支，需区分机制证据和下游医学类比。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：受限 detector/correction 案例未改变 Ch24 的 factorization、state 与 commit 主线；保留日报证据，不新增正文。 |
| [The Predictive-Causal Gap: An Impossibility Theorem and Large-Scale Neural Evidence](https://arxiv.org/html/2605.05029v1) | 2026-05-07T08:00:00+08:00 | 最小预测误差可以系统性偏好环境慢变量而不是目标系统的因果状态，world-model objective 必须显式声明 system/environment boundary；**3 + 1 + 2 = 6** | 争议 | 暂缓：Disputed；定理从特定预测模型外推到因果类、角度叙述与实验 grid 计数彼此不一致；需作者勘误或可复算证明/实验包后才重开。 |
| [Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization](https://arxiv.org/html/2605.05040v1) | 2026-05-07T08:00:00+08:00 | self-distillation 不必只匹配自身原分布；reward 重加权 teacher 给出目标与最优性条件，改变何时应选择外部 teacher 或 self-teacher。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“self-distillation 不必只匹配自身原分布；reward 重加权 teacher 给出目标与最优性条件，改变何时应选择外部 teacher 或 self-teacher。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise](https://arxiv.org/html/2605.05045v1) | 2026-05-07T08:00:00+08:00 | 视觉识别对旋转/噪声稳健不代表关系判断稳健；关系幻觉的分离对照及部分有效预处理改变 VLM robustness 评价。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch23 已把 modality encoder、shared representation、relation binding、provenance 与 evaluation slice 分开；本材料的窄命题“视觉识别对旋转/噪声稳健不代表关系判断稳健；关系幻觉的分离对照及部分有效预处理改变 VLM robustness 评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MULTIMODAL-REPRESENTATION`，[章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)） |
| [Piper: Efficient Large-Scale MoE Training via Resource Modeling and Pipelined Hybrid Parallelism](https://arxiv.org/html/2605.05049v1) | 2026-05-07T08:00:00+08:00 | large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication；**2 + 3 + 2 = 7** | 深入完成 | 整合：已落实；`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-PIPER-EFFICIENT-LARGE-SCALE-MOE-TRAINING-VIA-RESOURCE-MODELING-AND-PIPEL` 已承载“large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-DISTRIBUTED-TRAINING`，[章节](../../../../books/part-04-training-system/36-distributed-training.md)） |
| [SoK: Robustness in Large Language Models against Jailbreak Attacks](https://arxiv.org/html/2605.05058v1) | 2026-05-07T08:00:00+08:00 | 把 jailbreak evaluation 从单一 ASR 展开为 attack、defense、judge 与模型配置的多维合同；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch66/Ch72 已要求 threat model、attack、defense、judge、model 和 effect receipt 分权记录；taxonomy 不构成额外机制 owner。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [The Impossibility Triangle of Long-Context Modeling](https://arxiv.org/html/2605.05066v1) | 2026-05-07T08:00:00+08:00 | 长序列机制不能同时获得与长度无关的单步计算、与长度无关的固定状态，以及随历史事实数增长的精确召回容量；必须选择 workload-conditioned trade-off；**3 + 2 + 3 = 8** | 深入完成 | 整合：已落实；`MODEL-LONG-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-05066` 已承载“长序列机制不能同时获得与长度无关的单步计算、与长度无关的固定状态，以及随历史事实数增长的精确召回容量；必须选择 workload-conditioned trade-off”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MODEL-LONG-CONTEXT`，[章节](../../../../books/part-02-model/22-long-context.md)） |
| [Automatically Finding and Validating Unexpected Side-Effects of Interventions on Language Models](https://arxiv.org/html/2605.05090v1) | 2026-05-07T08:00:00+08:00 | model interventions need systematic validation of unexpected side-effects before release；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-AUTOMATICALLY-FINDING-AND-VALIDATING-UNEXPECTED-SIDE-EFFECTS-OF-INTERVEN` 已承载“model interventions need systematic validation of unexpected side-effects before release”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics](https://arxiv.org/html/2605.05097v1) | 2026-05-07T08:00:00+08:00 | 每条关联 edge 的 fast/slow 双变量耦合使重复事件巩固、缺少强化时衰减，检索只读 fast 状态；13 文档实验只检验动力学，不证明 retrieval 质量或系统优势。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch77 已把 immutable episode、derived memory、retriever 与 truth authority 分离；本材料的窄命题“每条关联 edge 的 fast/slow 双变量耦合使重复事件巩固、缺少强化时衰减，检索只读 fast 状态；13 文档实验只检验动力学，不证明 retrieval 质量或系统优势。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`AGENT-MEMORY`，[章节](../../../../books/part-07-agent/77-memory.md)） |
| [Text Corpora as Concept Fields: Black-Box Hallucination and Novelty Measurement](https://arxiv.org/html/2605.05103v1) | 2026-05-07T08:00:00+08:00 | groundedness sensor 不必二次生成或读内部状态；语料句间 embedding delta 的局部 Gaussian field 给出可追溯偏离信号，不把语料偏离等同事实错误。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：这是特定表示空间的 detector，不改变 Ch66 已有 grounding/evidence authority；不把语料距离升级为真值判断。 |
| [Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime](https://arxiv.org/html/2605.05112v1) | 2026-05-07T08:00:00+08:00 | binary-reward RL should control rollout pass rate to keep sampling in an informative regime；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-GRPO` 正文中的 `SF-ROLLOUT-PASS-RATE-CONTROL-STEERING-BINARY-REWARD-RL-TOWARD-ITS-MOST-INFO` 已承载“binary-reward RL should control rollout pass rate to keep sampling in an informative regime”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-GRPO`，[章节](../../../../books/part-04-training-system/33-grpo.md)） |
| [How Long Does Infinite Width Last? Signal Propagation in Long-Range Linear Recurrences](https://arxiv.org/html/2605.05113v1) | 2026-05-07T08:00:00+08:00 | 长递推不能无条件套无限宽初始化；线性复高斯状态在 t≈sqrt(n) 出现有限宽边界，改变长程稳定性解释。；**3 + 1 + 3 = 7** | 深入完成 | 已有覆盖：Ch22 已把有限 state、compute、精确召回、压缩/检索与长程稳定性写成条件分支；本材料的窄命题“长递推不能无条件套无限宽初始化；线性复高斯状态在 t≈sqrt(n) 出现有限宽边界，改变长程稳定性解释。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MODEL-LONG-CONTEXT`，[章节](../../../../books/part-02-model/22-long-context.md)） |
| [Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior](https://arxiv.org/html/2605.05115v1) | 2026-05-07T08:00:00+08:00 | 线性 activation steering 可能离开自然行为流形；双向几何干预比较显示路径形状重要，改变内部控制从方向到几何轨迹的选择。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：受限 representation-control 案例，没有足够证据改写 Ch17 的层级机制；原 owner 从 Self-Attention 收窄为 Transformer Layer，但不写 Books。 |
| [On the Hardness of Junking LLMs](https://arxiv.org/html/2605.05116v1) | 2026-05-07T08:00:00+08:00 | 无语义 junk token 也能触发目标有害前缀，说明对齐安全边界不能只覆盖人类可解释的 jailbreak prompt；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch72 已把 untrusted content、对抗生成、检测可见性与最终 policy/effect gate 分层；非语义 junk-token 白盒搜索是受限 proof-of-concept，不改变该防御主线。（`PLATFORM-SECURITY`，[章节](../../../../books/part-06-ai-infrastructure/72-security.md)） |
| [On the Wasserstein Gradient Flow Interpretation of Drifting Models](https://arxiv.org/html/2605.05118v1) | 2026-05-07T08:00:00+08:00 | 生成式 drifting 的理论标签必须区分 proposed KL/Wasserstein fixed-point construction 与实际实现的 Sinkhorn-like proxy；后者一般不是任何 distributional loss 的 Wasserstein gradient，也不继承相同收敛性质。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：Ch24 未采用 GMD/Drifting 作为正文机制；该 note 纠正 emerging family 的理论解释，但在原 family 形成可复用系统路线前，不为一篇 correction 新建孤立正文。 |
| [Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical System Prediction](https://arxiv.org/html/2605.05134v1) | 2026-05-07T08:00:00+08:00 | 黑盒幻觉检测通常需要多采样或外部 grounding；两种 regime 的 Koopman transition residual 加阈值校准提供单样本替代，必须检查训练标签和域迁移。；**2 + 1 + 2 = 5** | 标准完成 | 仅报告：特定 hallucination sensor 未改变 Ch66 对外部 evidence、校准与 abstention 的长期结论；不进入正文。 |
| [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/html/2605.05138v1) | 2026-05-07T08:00:00+08:00 | 纯文本计划不易反证 world model；可执行 Python model 由历史观测 verifier 约束再规划，同时关闭 harness 泄漏渠道，改变模型校验与动作执行关系。；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`MULTIMODAL-WORLD-MODELS` 正文中的 `SF-2026-ARXIV-2605-05138` 已承载“纯文本计划不易反证 world model；可执行 Python model 由历史观测 verifier 约束再规划，同时关闭 harness 泄漏渠道，改变模型校验与动作执行关系。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [The First Token Knows: Single-Decode Confidence for Hallucination Detection](https://arxiv.org/html/2605.05166v1) | 2026-05-07T08:00:00+08:00 | 多次生成语义一致性未必比单 decode 更有价值；首个内容 token 的 top-k entropy 在受控 QA 达到相当检测，改变 UQ 成本基线。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“多次生成语义一致性未必比单 decode 更有价值；首个内容 token 的 top-k entropy 在受控 QA 达到相当检测，改变 UQ 成本基线。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`PLATFORM-EVALUATION-SYSTEM`，[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)） |
| [Design Conductor 2.0: An agent builds a TurboQuant inference accelerator in 80 hours](https://arxiv.org/html/2605.05170v1) | 2026-05-07T08:00:00+08:00 | 把长任务拆成 proposal/implementation、constraint pack/milestone evidence 与 human/release commit authority 三层；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`AGENT-PLATFORM` 正文中的 `SF-2026-ARXIV-2605-05170` 已承载“把长任务拆成 proposal/implementation、constraint pack/milestone evidence 与 human/release commit authority 三层”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`AGENT-PLATFORM`，[章节](../../../../books/part-07-agent/84-agent-platform.md)） |
| [When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning](https://arxiv.org/html/2605.05172v1) | 2026-05-07T08:00:00+08:00 | BC→online RL 不应让新 critic 立即覆盖已有可靠动作；可先从 BC action likelihood/entropy 与少量 rollout 估计冻结价值基线，再由双 Q gate 在 BC 保留与 RL 探索之间逐状态选择。；**3 + 2 + 2 = 7** | 深入完成 | 整合：已落实；Ch26 已有 compact RL head 与 human/safety handoff，但缺少 offline BC 可靠动作的独立价值 owner，以及在在线分布偏移下让 BC 与 RL proposal 竞争而非直接覆盖的分支。（`MULTIMODAL-EMBODIED-VLA`，[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)） |
| [Understanding In-Context Learning for Nonlinear Regression with Transformers: Attention as Featurizer](https://arxiv.org/html/2605.05176v1) | 2026-05-07T08:00:00+08:00 | 线性 ICL 理论不足解释 nonlinear regression；attention 构造多项式/spline 特征并给 context/training size 误差界，补充 attention 作为 featurizer 的机制解释。；**2 + 1 + 2 = 5** | 深入完成 | 整合：已落实；`MODEL-SELF-ATTENTION` 正文中的 `SF-2026-ARXIV-2605-05176` 已承载“线性 ICL 理论不足解释 nonlinear regression；attention 构造多项式/spline 特征并给 context/training size 误差界，补充 attention 作为 featurizer 的机制解释。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MODEL-SELF-ATTENTION`，[章节](../../../../books/part-02-model/14-self-attention.md)） |
| [OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents](https://arxiv.org/html/2605.05185v1) | 2026-05-07T08:00:00+08:00 | 把搜索失败拆成可恢复步骤错误与 fatal transition，并在 rollout/update 中区别处理；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：Ch81 已按 recoverable/fatal transition、environment authority、retry/rollback 与 evidence receipt 组织 workflow；训练时 clamping 是受限实现，不改变 workflow owner。（`AGENT-WORKFLOW`，[章节](../../../../books/part-07-agent/81-workflow.md)） |
| [LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/html/2605.05187v1) | 2026-05-07T08:00:00+08:00 | World-model video evaluation 应把 perceptual quality、physical realism、condition alignment、temporal consistency 与 anomaly localization 分开，避免平均视觉分数掩盖局部物理失败。；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch25 已区分 perceptual、temporal、geometry/physics、action-conditioned transition 与真实 outcome，并要求局部 predicate/failure localization；PhyScore 没有补上 causal/controllable world-model contract。（`MULTIMODAL-WORLD-MODELS`，[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)） |
| [Sharp Capacity Thresholds in Linear Associative Memory: From Top-1 Retrieval to Tail-Average Learning](https://arxiv.org/html/2605.05189v1) | 2026-05-07T08:00:00+08:00 | 线性记忆容量不能只数 d² 参数；top-1 retrieval 有 log n 极值代价，而 top-k/TAM 改变阈值，明确容量必须绑定读取判据。；**3 + 1 + 3 = 7** | 深入完成 | 整合：已落实；`MODEL-LONG-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-05189` 已承载“线性记忆容量不能只数 d² 参数；top-1 retrieval 有 log n 极值代价，而 top-k/TAM 改变阈值，明确容量必须绑定读取判据。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`MODEL-LONG-CONTEXT`，[章节](../../../../books/part-02-model/22-long-context.md)） |
| [LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents](https://arxiv.org/html/2605.05191v1) | 2026-05-07T08:00:00+08:00 | long-horizon search needs elastic context orchestration across active, compressed and recoverable state；**2 + 1 + 2 = 5** | 标准完成 | 已有覆盖：Ch75 已分 active、compressed、recoverable state，保留 summary lineage、回读和不可把可恢复等同找对证据；五操作是实现词汇。（`AGENT-CONTEXT`，[章节](../../../../books/part-07-agent/75-context.md)） |
| [D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://arxiv.org/html/2605.05204v1) | 2026-05-07T08:00:00+08:00 | 普通 SFT 会损伤少步扩散能力；同模型 teacher 额外读目标图像、student 在自身 rollout 上蒸馏，改变保留 few-step 能力的连续适配路径。；**2 + 2 + 2 = 6** | 深入完成 | 整合：已落实；`TRAIN-SFT` 正文中的 `SF-2026-ARXIV-2605-05204` 已承载“普通 SFT 会损伤少步扩散能力；同模型 teacher 额外读目标图像、student 在自身 rollout 上蒸馏，改变保留 few-step 能力的连续适配路径。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。（`TRAIN-SFT`，[章节](../../../../books/part-04-training-system/29-sft.md)） |
| [Taming Outlier Tokens in Diffusion Transformers](https://arxiv.org/html/2605.05206v1) | 2026-05-07T08:00:00+08:00 | 简单屏蔽 DiT 高 norm token 并不能修复语义损伤；encoder 与 denoiser 双 register 分治提供不同 outlier 处理机制。；**3 + 1 + 2 = 6** | 标准完成 | 已有覆盖：Ch24 已把 AR/diffusion 的 factorization、iterative state、correction、commit 与 runtime handoff 分开；本材料的窄命题“简单屏蔽 DiT 高 norm token 并不能修复语义损伤；encoder 与 denoiser 双 register 分治提供不同 outlier 处理机制。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。（`MULTIMODAL-GENERATIVE-PARADIGMS`，[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)） |

## 4. 证据与知识整合


### [LCM: Lossless Context Management](https://arxiv.org/html/2605.04050v1)

- **Method**（§2–2.3; §3.2）：消息原文不可变存储，摘要 DAG 为派生缓存，软硬阈值触发三级压缩 fallback；lcm_expand 仅子任务可用。大型文件仅保存路径引用而非不可变内容快照。
- **Key evaluation**（§4.1–4.3）：OOLONG trec_coarse 8K–1M，Volt/ClaudeCode v2.1.4共享Opus4.6和Haiku4.5；报告平均74.8/70.3，优势同时涉及LLM-Map外部聚合，未独立隔离摘要DAG贡献。
- **Direct limitation**（§2 opening; §2.2; §5）：lossless只指消息原文保留且可达，不能保证agent真的检索；大型外部文件路径不保证历史字节不变。OOLONG污染依靠reasoning trace排除，raw baseline无相同trace；声明scope-reduction不足以形式化保证文本委派严格下降。
- **采用边界**：把不可变原文、摘要 DAG 与检索/压缩策略拆成不同状态所有权，避免把有损摘要误当成事实记忆
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-04050` 已承载“把不可变原文、摘要 DAG 与检索/压缩策略拆成不同状态所有权，避免把有损摘要误当成事实记忆”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [A Self-Attentive Meta-Optimizer with Group-Adaptive Learning Rates and Weight Decay](https://arxiv.org/html/2605.04055v1)

- **Method**（§2.2–2.6; Appendix A）：层类型/深度/bias分组统计送入attention调节group LR/WD；周期元更新复制参数、两个训练batch与validation batch构造梯度对齐/损失下降/generalization-gap，用含用户priority的HUW组合，再恢复原参数。
- **Key evaluation**（§3.1–3.4; Table 2）：五个轻量任务与AdamW同base超参，比较best validation/early-stopping总时间；各任务另调meta频率/特征/attention。多任务收益伴随不同训练长度，不能把早停总时间当每step加速。
- **Direct limitation**（§3.4–3.6）：任务特定超参显著不同；meta peak可达约1.5–2倍AdamW，普通步特征也有成本；十亿级Transformer未验证，公平性仍取决于是否同等调优baseline与验证集使用预算。
- **采用边界**：各参数组的梯度、动量与相关性统计可以驱动 group-wise learning-rate / weight-decay 调节，但元优化器自身增加训练状态、目标耦合与额外计算
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“各参数组的梯度、动量与相关性统计可以驱动 group-wise learning-rate / weight-decay 调节，但元优化器自身增加训练状态、目标耦合与额外计算”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [MP-ISMoE: Mixed-Precision Interactive Side Mixture-of-Experts for Efficient Transfer Learning](https://arxiv.org/html/2605.04058v1)

- **Method**（Methodology: GNP-IQ / ISMoE）：将大部分 backbone 以8bit存储、LayerNorm全精度可训练，side-MoE16bit；周期抽样重量重新量化并学习Gaussian扰动，backbone代表token与expert代表token相似度修正路由。
- **Key evaluation**（Experimental Settings; Main Results; Tables 1–4）：五类VL任务及T5-base/large GLUE；UniPT/SHERL配方比较训练显存、任务指标、GNP-IQ/ISMoE消融。量化释放显存再扩大side容量是直接资源取舍。
- **Direct limitation**（Iterative Quantization Strategy; Implementation Details; On Effect of ISMoE）：正文对多数backbone冻结与部分量化权重更新的路径说明不足，多项细节转Extended Version；稀疏固定k不自动证明端到端零推理成本，不能用分类/检索提升证明通用知识无遗忘。
- **采用边界**：混合精度冻结主干释放出的显存可以转投 side-MoE 容量，但收益依赖量化误差、路由交互与任务分布
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch30 已把 frozen base、adapter capacity/precision、routing/composition 与 artifact identity 分开；本材料的窄命题“混合精度冻结主干释放出的显存可以转投 side-MoE 容量，但收益依赖量化误差、路由交互与任务分布”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Continual Distillation of Teachers from Different Domains](https://arxiv.org/html/2605.04059v1)

- **Method**（§3.1–3.4）：顺序不可回访 teacher、固定无标注蒸馏集下，SE2D 同时蒸馏当前 teacher 与上一 student checkpoint，但后一项仅施于所有 teacher 未见 external data，保护未在学生数据出现的旧域知识。
- **Key evaluation**（§4 / §5.1–5.3 Tables 1–4）：CIFAR20、Digits、DomainNet 多域对比有/无 external data 与多种蒸馏基线。相关外部域促进迁移，但也会强化遗忘；DomainNet 上 SE2D 可落后普通 self-distillation。
- **Direct limitation**（§5.3 Limitations of SE2D）：依赖 external/teacher 域距离、teacher 在未见域的质量，并要求知道数据域来源；任意 FM 黑盒训练数据未知时难确认 external 身份。
- **采用边界**：连续蒸馏时旧 teacher 不再可访问；外部无标签数据保留其 logits，分离新知识迁移与旧知识遗忘，因此需要比较仅当前 teacher 蒸馏和保留旧响应的取舍。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“连续蒸馏时旧 teacher 不再可访问；外部无标签数据保留其 logits，分离新知识迁移与旧知识遗忘，因此需要比较仅当前 teacher 蒸馏和保留旧响应的取舍。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Single-Position Intervention Fails: Distributed Output Templates Drive In-Context Learning](https://arxiv.org/html/2605.04061v1)

- **Method**（§3.3–3.6）：比较 centroid probe、单位置 activation transplant、多位置 demo-output transplant 与噪声因果追踪，区分可解码、必要与充分。
- **Key evaluation**（§4.1–4.6）：5-shot、greedy；主 Llama3.2-3B，复核另三 1–3B 模型。主 N=50，单位置0转移不阻止多位置转移；支持分析不少仅N=10。
- **Direct limitation**（Appendix D.1–D.5）：只测确定分类/简单转换，未证明大模型、开放生成或复杂CoT；全向量移植未定位最小子空间。30%层深不是普适规则。
- **采用边界**：单位置 probe 可读不等于单位置具有因果控制力；ICL task template 由跨位置、跨层的分布式状态共同承载
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch14 已写入单位置可解码不等于因果控制，以及跨位置/跨层分布式 task template 的受限边界。

### [EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation](https://arxiv.org/html/2605.04062v1)

- **Method**（§3.1–3.3; EAKLD equation）：周期supergroup混合4bit/ternary，teacher相邻层低cosine选feature蒸馏；batch平均min(entropy,log k)/log k在forward/reverse KL间混合，显式clip保证系数在[0,1]。
- **Key evaluation**（§4.1–4.6）：350M/0.6B/1.7B text及7B Omni，14指标和两视频任务；Qwen0.6B在M4Pro/llama.cpp实测storage/memory/512prefill+512decode。
- **Direct limitation**（§4.1/4.6）：训练含所列commonsense任务train split，泛化需与测试隔离理解；接近全参数量化和baseline仅decoder覆盖不同，压缩率不能都归精度策略。具体实测TQ格式并非所有fractional mixed-bit layout，ternary prefill可慢于Q2_K，不能只报decode收益。
- **采用边界**：低于 4-bit 压缩受质量/重训代价约束；混合精度结构量化、层自适应特征蒸馏和熵调 KL 联合提供新的低比特执行分支，需对齐硬件与训练预算。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“低于 4-bit 压缩受质量/重训代价约束；混合精度结构量化、层自适应特征蒸馏和熵调 KL 联合提供新的低比特执行分支，需对齐硬件与训练预算。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Free Energy-Driven Reinforcement Learning with Adaptive Advantage Shaping for Unsupervised Reasoning in LLMs](https://arxiv.org/html/2605.04065v1)

- **Method**（§3.1–3.2）：用最终答案频率的非线性 sharpen 分布及熵导出 group confidence：高置信偏 consensus、低置信偏探索；reward skewness 再压低正偏分布中的稀少高奖励正优势、负偏分布中的稀少低奖励负优势，接 GRPO。
- **Key evaluation**（§4.1–4.2 / Figures 5,8）：最大3B模型，数学、SQL、Geometry3K；400 steps、每题8 rollouts，匹配超参数比较GRPO/TTRL/Entropy/Intuitor及组件消融。结论是这些设置中的自奖励改进，非共识等于真值。
- **Direct limitation**（Limitations / Appendix C.1 Assumption 1）：仅≤3B；最终答案分布忽略中间路径，batch skewness掩盖组内差异。理论依赖consensus-truth proxy，不能提供无真值条件下的正确性担保。
- **采用边界**：无监督推理不能固定奖励/探索分配；FER 的自由能信号与 AAS 的 advantage 统计调整提供新的训练信号控制分支，须核查是否超出已有熵奖励。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch33 已把 group sampling、advantage aggregation、reward/verifier、exploration 与 bounded optimizer update 分开；本材料的窄命题“无监督推理不能固定奖励/探索分配；FER 的自由能信号与 AAS 的 advantage 统计调整提供新的训练信号控制分支，须核查是否超出已有熵奖励。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning](https://arxiv.org/html/2605.04066v1)

- **Method**（§4.2–4.4）：batch reward均值驱动power-mean指数从偏算术向几何式变化；FSS均值/标准差映射upper clipping，lower固定；非负幅值与advantage sign分离，不能对有负数的PPO loss直接套power mean。
- **Key evaluation**（§5.1–5.2.3）：1.5B/3B，数学、BIRD/Spider SQL、Geometry3K；binary verifier、400step/8rollout，与PMPO/FAC及FSS分量消融，pass@1/16按bench区分。
- **Direct limitation**（Limitations; Appendix F assumption）：准确可验证outcome是前提；FSS为质量proxy假设，reward一致不意味着语义正确，大模型/无法verifier场景未验证，不把adaptive clip当单调提升保证。
- **采用边界**：固定 policy 聚合/clip 不随训练能力变化；power-mean 目标在算术/几何均值间切换并反馈调 clip，改变 RLVR 更新控制。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch33 已把 group sampling、advantage aggregation、reward/verifier、exploration 与 bounded optimizer update 分开；本材料的窄命题“固定 policy 聚合/clip 不随训练能力变化；power-mean 目标在算术/几何均值间切换并反馈调 clip，改变 RLVR 更新控制。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [LAWS: Learning from Actual Workloads Symbolically -- A Self-Certifying Parametrized Cache Architecture for Neural Inference, Robotics, and Edge Deployment](https://arxiv.org/html/2605.04069v1)

- **Method**（§3–5; Theorem 3/4）：LAWS以trie-prefix signpost和参数化cheap expert作cache，提出Lipschitz自证及首分歧embedding Jacobian correction；Theorem4仅针对首分歧变量写Taylor误差，未约束后续任意suffix变化。
- **Key evaluation**（Theorem 3/4; Remark 1/2; §11.4）：主要证据为条件上界与架构推导，未提供训练LLM真实workload的效用/能耗评价；self-certification要求delta大于可能指数放大的epsilon_fit+2Lambda*C_E，实用非空保证未建立。
- **Direct limitation**（Remark 1; Theorem 4; §11.4）：首分歧embedding的O(r²)不能直接覆盖其他suffix同时变化；LayerNorm stabilizer不证明输入原始variance下界，local empirical Lipschitz不能替代全域证书。stationarity/energy推论与实际cache命中分开，当前核心证书有争议。
- **采用边界**：参数化expert cache需要可核验validity domain；本文的自认证证明存在未控制后缀与归一化界疑问，不能采用其部署正确性保证。
- **审阅/Books**：exact-v1 Source Review 完成；争议：LAWS 的 self-certification 尚未控制后缀与 LayerNorm validity boundary；只有作者给出可核验的修订证明或等价勘误后才重开，当前不得支持 Books。

### [Toward Human-AI Complementarity Across Diverse Tasks](https://arxiv.org/html/2605.04070v1)

- **Method**（§3.1–§3.4）：在 1,886 个跨知识、事实性、长上下文与欺骗检测样本上比较 confidence hybridization、top-2 assistance 与 subtask delegation；模型 confidence 先经 isotonic calibration，再按固定 calibration/test split 形成路由。
- **Key evaluation**（§4.1–§4.4；§5）：每项收集 20 个 GPT-5-mini 响应和 3–5 个人类判断；AI 错且人对的互补区域仅 8.9%，confidence routing 相比 AI-only 只增加 0.4pp。top-2 的收益主要来自人采纳正确 AI 候选，而不是识别并推翻 AI 错误。
- **Direct limitation**（§6；Appendix）：任务、模型和 assistance protocol 有限；14 个 tie-breaking 不一致被披露。结果反证所测条件下的 confidence routing，不证明所有模型、人群或领域都缺乏互补性，也不提供生产安全率。
- **采用边界**：高风险 human-oversight routing 不能把模型 confidence 当作错误可识别性；应先测 AI 与人的错误重叠、互补区域和人类纠错能力，再决定 route 或 assistance。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已明确自报/内部 confidence 只是需按 deployment slice 校准的 sensor，高风险 route/defer 还需外部证据、human adjudication 与 risk-coverage；本结果为该命题提供受限反证，但不改变 owner 或 fallback。

### [RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction](https://arxiv.org/html/2605.04075v1)

- **Method**（§3.1–3.7）：将选定evicted KV外积吸入固定矩阵state，以attention/entropy调吸收和衰减，按image空间双方向与text recall分离；query取state特征并gate回现有attention，非原softmax等价压缩。
- **Key evaluation**（§4.1–4.5）：LLaVA7B/Qwen3VL4B/8B八视觉语言bench，单A100 5–60%cache budget，task scores/latency/memory与state/entropy/分模态消融。
- **Direct limitation**（§6; §3.1/3.7）：最大8B，audio/video仅未来方向；移除softmax后的state是近似，并非可恢复原KV；learnable retrieval gate训练/开销边界不能默认为免训，固定每图state不等于无论图数恒定总内存。
- **采用边界**：多模态 KV eviction 可从离散删除转为 uncertainty-aware 的连续 state-space memory evolution，但要承担状态近似与恢复误差
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch45 已把 KV identity、保留/压缩/驱逐、恢复误差与 correctness fallback 绑定；本材料的窄命题“多模态 KV eviction 可从离散删除转为 uncertainty-aware 的连续 state-space memory evolution，但要承担状态近似与恢复误差”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO](https://arxiv.org/html/2605.04077v1)

- **Method**（§3.3–3.6; Appendix A/B）：按advantage正负分组分别做token平均，再以组内序列数/G混合，在binary GRPO消除跨sign的长度权重耦合，同时不强制每条序列等权。非二值扩展须用advantage mass而非只数序列。
- **Key evaluation**（§4.1–4.3）：Qwen2.5-Math7B/Qwen3-1.7B，DAPO17k/Polaris，500steps、G16、2K/8K最大回复，数学/code六基准；记录peak/best@8/last-step，token与sequence优劣随模型翻转。
- **Direct limitation**（§4.3.3; Appendix B）：长度统计与性能翻转是所测训练的解释，不是任意奖励/模型普遍最优证明；原公式依赖binary reward，非二值需重新分配权重，peak与末步不能混报。
- **采用边界**：指出 loss reduction 本身会重写 credit 权重：token aggregation 偏向长序列，sequence aggregation 又压低长响应
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-GRPO` 正文中的 `SF-2026-ARXIV-2605-04077` 已承载“指出 loss reduction 本身会重写 credit 权重：token aggregation 偏向长序列，sequence aggregation 又压低长响应”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Validity-Calibrated Reasoning Distillation](https://arxiv.org/html/2605.04078v1)

- **Method**（§2.1–2.3）：在teacher/student各自prefix下比较双方所提token的局部validity，以student/teacher比率加权teacher-prefix SKL与student-prefix SRKL；学生提议更优时放大，不把全局teacher优越性当每步优越性。
- **Key evaluation**（§4.1–4.6）：Qwen数学7B→1.5B、代码7B→1.5B/14B→7B与instruction-following；比较蒸馏基线及禁放大消融。另DeepSeek-Coder6.9B→1.3B用teacher likelihood代理，非外部真值。
- **Direct limitation**（§2.2 与 Appendix D.4（直接方法边界））：局部judge不评价全局解正确性；PRM-free用top128 teacher概率collision baseline、log smoothing并将权重clip到[0.5,2]，仍是teacher支持集内的信号分配。主文无独立limitations段，不能把Conclusion充当限制。
- **采用边界**：固定模仿 teacher 路径会忽略 student 当前状态；同一 prefix 下比较两者下一步 validity 再分配蒸馏强度，改变逐步监督的选择。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“固定模仿 teacher 路径会忽略 student 当前状态；同一 prefix 下比较两者下一步 validity 再分配蒸馏强度，改变逐步监督的选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [AsymmetryZero: A Framework for Operationalizing Human Expert Preferences as Semantic Evals](https://arxiv.org/html/2605.04083v1)

- **Method**（§3–§4）：把专家要求编码为逐 criterion 的稳定 evaluation contract，并在 model-only Inspect 与 agentic Harbor 中复用；固定 task/reference/criteria/aggregation，只替换五模型 frontier 或 compact jury。
- **Key evaluation**（§5）：四个 frontier-class solver 上 criterion agreement 为 75.9%–89.6%，compact jury 的 3–2 dissent 明显更高；成本/延迟下降很多，但聚合 task outcome 往往把差异冲淡。
- **Direct limitation**（§6）：agreement 是相对 frontier jury，不是绝对正确率；分歧项没有 human/gold adjudication，只测单一 agent/harness 与有限任务。不能把成本下降外推成 judge 等价。
- **采用边界**：Evaluation 必须冻结 criterion、judge procedure 与 aggregation；聚合后 task score 稳定可能掩盖 criterion-level jury dissent，低成本 jury 不能未经 human anchor 就取得同等判定权。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 per-criterion outcomes、judge/rater identity、aggregation function、disagreement 和 release authority 分权保存；该 source family 强化了 aggregation masking 边界，但未改变现有 contract。

### [FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression](https://arxiv.org/html/2605.04084v1)

- **Method**（§3.1–4.2）：weight-only subspace kmeans码本/索引免校准；decode每output直接fetch必要centroid，prefill每sequence position建LUT供output features复用，不先物化全FP16权重。
- **Key evaluation**（§5.1/5.4）：Llama3/Qwen8–9B及Llama2 7/13B，WT2/五常识任务；端到端Llama3-8B128prompt/128generate，CUDA warmup计时，storage不含KV/activation。
- **Direct limitation**（§5.4.3; Limitations）：prefill LUT不能用tensor core，935ms对FP16 41ms；hybrid FP16 prefill需要临时全weight物化而违背该阶段compressed-only内存。TTFT/并发/长prompt不能从decode速度推出普遍收益。
- **采用边界**：calibration-free product quantization 把 weight compression 变成子空间 codebook 与目标 kernel 的联合选择，但不能省略模型质量和执行格式验收
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“calibration-free product quantization 把 weight compression 变成子空间 codebook 与目标 kernel 的联合选择，但不能省略模型质量和执行格式验收”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [OpenCLAW-Nexus: A Self-Reinforcing Trust Framework for Byzantine-Resilient Decentralized Federated Learning](https://arxiv.org/html/2605.04091v1)

- **Method**（§IV-A–D / Propositions 1–2）：公共验证集分片多数表决产生binary质量信号，折扣Beta信誉同时控制参与选择、data×reputation聚合与加权共识；共识权重仅在固定epoch内冻结，DP按每记录最坏参与次数核算。
- **Key evaluation**（§V-A–F）：声明1000跨云节点其中200 GPU可训练、每轮100、CIFAR10/ResNet18；20%gradient-flip时72.6%对BALANCE71.4%是单次点估计。另测Sybil、DP与选择策略，不称统计显著。
- **Direct limitation**（§VI-A）：公共基准完整性/代表性仍是信任根，存在刷分；仅静态攻击/固定权重epoch安全，不证明动态成员liveness。DP不保护参与身份/信誉，生成任务无对应判分分离证明，多数结果无重复seed区间。
- **采用边界**：无可信根的异构联邦学习不能依赖固定可信聚合者；折扣 Beta reputation 联合客户端选择、RepFedAvg 与 BFT，需核查 Byzantine/Sybil 假设下的训练信任边界。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：证据属于去中心化联邦学习的 reputation/BFT 协议，依赖其 Byzantine/Sybil 与 honest-majority 假设；未改变本书 LLM distributed-training 的 collective、parallel state 或 checkpoint contract。

### [Regularized Centered Emphatic Temporal Difference Learning](https://arxiv.org/html/2605.04100v1)

- **Method**（§3.2–§5 / Theorem 1）：两状态反例说明直接中心化 emphatic TD 的耦合矩阵可失正定；RETD保留follow-on trace，仅对辅助均值递推加阻尼c，不是value/Bellman-error正则项。
- **Key evaluation**（§6.1–6.3 / Tables 1–2）：七个线性off-policy prediction任务，比较TD/GTD2/TDC/TDRC/ETD/TETD/CETD；统一主步长0.01，报告末10%RMSE、跨run标准差并显式列发散。新两状态中CETD/RETD都bounded，差异为固定点几何。
- **Direct limitation**（§5 Assumptions 1–3 / §6.4）：有限状态动作、几何遍历、递减步长与c充分界支持定理；固定步长经验未验证该定理。未扩展nonlinear近似、eligibility traces或大型control。
- **采用边界**：直接中心化 emphatic TD 可能破坏关键矩阵正定性；仅正则辅助变量的修复改变稳定算法构造，结论限该线性 TD 设定而非所有 RL。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：结论是有限线性 off-policy TD 的正定性修复，不是 RLHF/RLVR 的生成 policy、reward 或 rollout 机制，不能据类比改写 TRAIN-RLHF。

### [TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments](https://arxiv.org/html/2605.04107v1)

- **Method**（§3.1–3.5）：固定10 transforms/8 operators把schema编译成token-efficient text，并重新布局constraints、delimiters和anchors；确定性、无model调用，非工具执行validator或adapter。
- **Key evaluation**（§5.1–6.6）：TAB工具选择/参数F1，多模型19K+ API调用，并区分native FC→json-text格式效应与json-text→TSCG压缩效应；BFCL60调用和单MCP spot-check仅有限外部验证。
- **Direct limitation**（§8）：自建benchmark、只测selection/parameter而非多轮任务完成；小模型少工具时压缩可降7–23pp，English-only，API版本冻于March–April，未与schema replacement完整head-to-head。
- **采用边界**：TSCG 将 JSON tool schema 确定性编译为 token-efficient structured text，直接改变 schema 表征、压缩和 tool-selection 输入；它不提供 validator、adapter 或 effect-side correctness。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch78 已把 schema/argument proposal、deterministic validation、authorization 与 effect receipt 分层；本材料的窄命题“TSCG 将 JSON tool schema 确定性编译为 token-efficient structured text，直接改变 schema 表征、压缩和 tool-selection 输入；它不提供 validator、adapter 或 effect-side correctness。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Learning reveals invisible structure in low-rank RNNs](https://arxiv.org/html/2605.04115v1)

- **Method**（§3–§5）：rank-1 RNN以4个loss-visible及6个invisible overlap闭合学习动力学，Gram metric把参数空间梯度映射到overlap；相同输入输出可因invisible状态而有不同后续学习。线性gradient-flow不变量限制记忆，非线性可破坏。
- **Key evaluation**（§3–§5.2 / Figures 1–4）：线性filter对照全参数训练与10D ODE；非线性flip-flop在Gaussian小步长下匹配。历史解码用20个网络的ODE、50随机split；非大模型实测。
- **Direct limitation**（Limitations / §5.1）：主分析rank-1，无full-rank随机bulk；非线性需要参数近Gaussian但训练不保证，较大步长/Adam偏离。不能由此证明Transformer相同机制或可靠历史提取。
- **采用边界**：相同已实现函数不意味着相同后续学习动力学；低秩 RNN 中 loss-invisible 状态承载训练历史，改变仅由当前 loss/输出判断可塑性的解释。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：低秩 RNN 中 loss-invisible state 的理论结果不证明 Transformer residual stream 或 LLM 训练动力学存在同一机制。

### [Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering](https://arxiv.org/html/2605.04116v1)

- **Method**（§II-B/C; §III-A/B）：API-only retrieval-ICL成员推断，用多个query前缀的回答相似度及位置衰减，或reference模型从语义相似度拟合缺失的目标log-prob；攻击对象是检索示例身份，不是模型训练集身份。
- **Key evaluation**（§IV-A; §V-A/C）：Gemma2B/Pythia1.4B及7B扩展，SQuAD/SQuADShifts/NewsQA，1-shot greedy；完整/改写前缀、AUROC/TPR@lowFPR，重复查询与低比例前缀成本对比。
- **Direct limitation**（§VII-B; §VI-B/C）：调用数量仍随query长度增长，sampling/k-shot未充分测；ensemble防御是经验抑制而非DP保证，确定性kNN不享受Poisson采样隐私放大。
- **采用边界**：retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04116` 已承载“retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Frontier Lag: A Bibliometric Audit of Capability Misrepresentation in Academic AI Evaluation](https://arxiv.org/html/2605.04135v1)

- **Method**（§3.1–3.5）：OpenAlex 112303-pool用固定LLM extraction/inclusion管线得到18574项应用评价；区分model snapshot、tier、elicitation disclosure与泛化claim，按冻结frontier index定义gap而非直接测latent能力。
- **Key evaluation**（§4.1; §3.4; §6.1–6.3）：报告corpus分母/各outcome子集、300 predicted-include gold和150 cross-family复核；4766可取PDF约25.7%，主要题摘要分辨率，不能把一套分母用于所有指标。
- **Direct limitation**（§6.1–6.12）：OpenAlex非census、gold是precision-only、全文子集非随机，extractor同族共错与纠正迁移性未消除；单标量frontier/二元claim severity及原协议改动均有限制，不指控个体作者、不能证明换frontier后具体结果必反转。
- **采用边界**：capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-2026-ARXIV-2605-04135` 已承载“capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [FlowEval: Reference-based Evaluation of Generated User Interfaces](https://arxiv.org/html/2605.04165v1)

- **Method**（§3.1–§3.3）：从高质量 reference UI 与生成 UI 运行同一验证任务，由 CUA 产生截图轨迹，再以 DTW、eBLEU 与 WMD 比较交互序列；不是只让 MLLM 看最终截图。
- **Key evaluation**（§4–§4.1）：27 个 reference sites、7 个 generator、每条件 5 次，共 945 个 UI；两位 HCI 专家提供 429 个盲比较。WMD 对人类 Elo 的 Spearman 相关为 0.96，但逐对 agreement 只有 73.0%。
- **Direct limitation**（Limitations: Scope / Implementation / Evaluation）：只覆盖 common one-shot web flows；两个 annotator、一个 CUA，best-of-nine aggregation 依赖 agent 能力。缺少认证/支付等受限流程、迭代式开发、可访问性、安全与完整生产评价。
- **采用边界**：生成式 UI 评价应把静态外观与可执行 interaction flow 分开；reference trace 是可诊断 evidence，但 metric、CUA 与 reference coverage 都必须属于 evaluation identity。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已要求以可执行 environment transition、artifact 与 human anchor 评价 agent，不让 judge 取代 outcome；FlowEval 是 UI trace 的受限实例，未改变现有 evaluation owner。

### [Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures](https://arxiv.org/html/2605.04178v1)

- **Method**（§IV-A–G）：用TMEM/TMA/同步关键路径、cache hit/occupancy以及实测launch/interference参数分段预测GPU kernel time；复用原语模型但每平台workload FLOPs/bytes和kernel形态要重新刻画。
- **Key evaluation**（§V-A–E）：B200/MI300A校准微基准与Rodinia/SPEChpc Tiny kernel-sum；H200/MI250X仅改平台参数的迁移应用误差高达43.6–555%，不能只报本机0.09/1.3%误差。
- **Direct limitation**（§IV-D/G; §V-E）：regular access/steady clocks/known cache hit；CTA排队与multi-node未建模，host-copy overlap未建模。profiler-derived/per-case calibration不等于独立预测，跨平台characterization必须验证。
- **采用边界**：GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [MedFabric and EtHER: A Data-Centric Framework for Word-Level Fabrication Generation and Detection in Medical LLMs](https://arxiv.org/html/2605.04180v1)

- **Method**（§3.1–3.2 / Algorithm 1）：先将真答案重写成 LLM 风格，按证据局部伪造并用 ROUGE-L≥0.7 与误判筛选；EtHER 将文本拆表、互补 mask 后依证据重建，再结合 embedding 与 LLM 判断。
- **Key evaluation**（§4.1–4.3 / Figure 4）：原数据→风格重写→高结构相似伪造的 fine-tuned detector 平均 F1 为69.54→59.84→42.10；EtHER在这些设置为60.60–70.10。支持控制生成风格混淆，而非 v2 的错误证据消融。
- **Direct limitation**（§3.1 Algorithm 1 与 §4 实验范围（直接实验边界））：只覆盖医学词级伪造，保留能诱发筛选器误判的样本；不是随机真实部署分布，不能据此推出一般检索可靠性或临床效果。v1 未提供 gold/wrong/no evidence 对照。
- **采用边界**：真假文本来自不同作者会把风格线索混入 factuality 评价；v1 将真答案同样改写为 LLM 风格并约束伪造局部改词，观察 detector 随风格/结构对齐退化，要求用配对风格控制检验事实检测能力。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“真假文本来自不同作者会把风格线索混入 factuality 评价；v1 将真答案同样改写为 LLM 风格并约束伪造局部改词，观察 detector 随风格/结构对齐退化，要求用配对风格控制检验事实检测能力。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions](https://arxiv.org/html/2605.04209v1)

- **Method**（§5.1–5.2; §6.2 Theorem 6.5）：在 FC 预测头注入稀疏方向并加入 Gaussian dither；不可区分对象是仅加 dither 的 clean reference 与带结构信号的权重，结论依赖 Sparse-PCA hardness。
- **Key evaluation**（§7.1–7.4; Appendices E–F）：三种图像分类数据×ConvNet/ResNet-18/ViT-Small，10 seeds；对比原模型、加 dither 参考、后门模型及三检测器，另测微调后的 ASR。微调恢复干净准确率不等于清除触发行为。
- **Direct limitation**（§8 Discussion and Limitations; §6.2 assumptions）：只改 FC head；语言/语音触发器仍开放。Margin regularity、calibrated dither 与信号传播假设的检验是架构特定经验支持，不是相对原始模型的统计不可区分。
- **采用边界**：在 Sparse-PCA 硬度与 margin/dither 假设下，FC 预测头的后门参数与 Gaussian-dithered clean 参考计算不可区分；不是相对原模型的统计不可区分，也未建立语言触发器可行性。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04209` 已承载“在 Sparse-PCA 硬度与 margin/dither 假设下，FC 预测头的后门参数与 Gaussian-dithered clean 参考计算不可区分；不是相对原模型的统计不可区分，也未建立语言触发器可行性。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [The Anatomy of Silent Data Corruption: GPU Error Pattern Study and Modeling Guidance](https://arxiv.org/html/2605.04213v1)

- **Method**（§II–IV; §VI-B）：在缩减2-SM production-class GPU gate-level netlist注入single stuck-at permanent faults，以golden memory XOR记录unit/type条件下nullification、多bit和warp对齐空间模式，转成分布感知软件注入模板。
- **Key evaluation**（§IV–V）：63 CUDA microbench、超过3M simulator hours和600M observed corruptions；特殊值合计1.01%、nullification50.68%，单bit不足non-special的40%；都是此注入/筛选条件统计。
- **Direct limitation**（§II-A; §IV; §V-B）：产品未披露、2-SM缩减、testability预筛、永久SAF非瞬态/所有物理故障；FP8样本有限。不能把比例当生产fleet故障率，software template尚不是现场保护有效性证据。
- **采用边界**：silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-MONITORING` 正文中的 `SF-2026-ARXIV-2605-04213` 已承载“silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs](https://arxiv.org/html/2605.04215v1)

- **Method**（§III-B/C）：CatBoost从prompt预测D-LLM canvas长度，以正向预测残差分位数加safety margin，并在截断时fallback重跑；解析FLOPs区分短序列线性与长序列attention二次项。
- **Key evaluation**（§IV-A–F）：LLaDA8B/H100测64–30K canvas FLOPs/显存；39994 SFT对按GPT2 tokenizer长度80/20分割，比较4096固定、200翻倍、mean翻倍和oracle；主要total TFLOPs含重试。
- **Direct limitation**（§IV-D/F; §V）：mean翻倍在该短回答分布已接近预测法，19%优势含模拟双峰分布；质量主要引用LLaDA既有结果非完整联合验收，变长batch调度未解决，不把经验0.1%重试当SLA保证。
- **采用边界**：fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MULTIMODAL-GENERATIVE-PARADIGMS` 正文中的 `SF-2026-ARXIV-2605-04215` 已承载“fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Jordan-RoPE: Non-Semisimple Relative Positional Encoding via Complex Jordan Blocks](https://arxiv.org/html/2605.04217v1)

- **Method**（§3–4; Proposition 1）：非正交Jordan动作必须query用contragredient、key用对应动作以得相对lag；nilpotent增加distance×phase基。bounded shear稳定长距却破坏exact group law/纯lag位置因子。
- **Key evaluation**（§5.1–5.4）：固定basis probes、Jordan-friendly synthetic LM、6layer384dim WikiText byte LM，1K训练到8K测试；RoPE+ALiBi仍最佳，强shear损害自然语言，三seed微小差异非显著分离。
- **Direct limitation**（§6; Appendix C）：证明的是exact表示/basis及特定目标利用，不是通用RoPE替代；stabilized版非exact relative representation，自然语言收益主要可能来自damping而非强shear。
- **采用边界**：RoPE phase 与 ALiBi 距离通道不能表示所有耦合；Jordan block 生成距离调制 phase，且稳定 shear 破坏群律，改变位置基函数与数值稳定的取舍。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch13 已把位置基函数、相对距离、外推与数值稳定性写成替代分支；本材料的窄命题“RoPE phase 与 ALiBi 距离通道不能表示所有耦合；Jordan block 生成距离调制 phase，且稳定 shear 破坏群律，改变位置基函数与数值稳定的取舍。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Layerwise LQR for Geometry-Aware Optimization of Deep Networks](https://arxiv.org/html/2605.04230v1)

- **Method**（§4–5; Appendix E.2）：把divergence局部二次模型写成layerwise LQR/KKT-Riccati，exact仅作参照；实用法周期学习结构化inverse preconditioner，以JVP/VJP/HVP隐式作用，非实际每step全Riccati。
- **Key evaluation**（§6.1–6.6）：Rosenbrock exact equivalence，CIFAR/ResNet/ImageNet、IWSLT与grokking；ImageNet约1.03倍时间，IWSLT BLEU小幅提升伴1.16倍时间，分开epoch与wallclock。
- **Direct limitation**（§4.3; Appendix E.3/E.5）：exact递推不适用于现代大网络实做；结构、inner steps/频率/LR耦合，warm-start U反而不稳，当前默认每次identity重启并EMA；未证明大LLM或任意curvature普遍更优。
- **采用边界**：结构化 preconditioner 提早丢弃跨层几何；dense quadratic step 的 layerwise LQR 等价式给出参考，再学习可复用的近似逆，改变二阶优化近似评价。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“结构化 preconditioner 提早丢弃跨层几何；dense quadratic step 的 layerwise LQR 等价式给出参考，再学习可复用的近似逆，改变二阶优化近似评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Adaptive Consensus in LLM Ensembles via Sequential Evidence Accumulation: Automatic Budget Identification and Calibrated Commit Signals](https://arxiv.org/html/2605.04236v1)

- **Method**（§3; Appendix I）：持久plurality阈值或一维arena sequential heuristic控制何时commit/何时fallback；round2注入共识使workers相关，不继承neuroscience DP最优性。
- **Key evaluation**（§5–7）：GPQA546的70%与最优budget Debate统计打平，AIME300随W变化；120B commit partition和latency，routing比较仅AIME2010–23，120B约6倍单模型墙钟。
- **Direct limitation**（§10; §7.2 scope）：W按benchmark偏好为posthoc，worker非独立，置信partition不是conditional risk证书；同准确率不等效成本，27%routing disagreement不可外推GPQA/领域。
- **采用边界**：ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Temporal Reasoning Is Not the Bottleneck: A Probabilistic Inconsistency Framework for Neuro-Symbolic QA](https://arxiv.org/html/2605.04243v1)

- **Method**（§3.1–3.3）：提取event graph后融合Dirichlet不确定性与credal interval，MCTS按信号选择补检索或结构修复。具体公式把窄区间宽度惩罚作矛盾，尚未说明为何区间收窄等价不可满足。
- **Key evaluation**（§4.1–4.3）：Llama3-70B，structured/Synthetic-200与TempReason、TimeX-NLI、TRACIE；报告1.0/75.1%/~50%和组件消融，但跨数据集下降未隔离表示与推理的因果归属。
- **Direct limitation**（§5 / §3.3–4.1（直接限制及审阅争议））：主文承认隐式事件抽取失败且PIS可能低；代码/log仅承诺发表后释放。需澄清credal定义、MCTS与single-pass协议及因果诊断，不能采用‘推理不构成瓶颈’普遍结论。
- **采用边界**：事件结构抽取缺失可能使一致性检测沉默；PIS区间公式与‘表示而非推理是唯一瓶颈’尚无足够解释，仅保留诊断问题，不采用通用结论。
- **审阅/Books**：exact-v1 Source Review 完成；争议：credal interval 的 coverage 前提与论文对 temporal inconsistency 的解释尚未对齐；需修订正文明确 posterior/coverage 条件并复算结论后才重开。

### [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/html/2605.04251v1)

- **Method**（§3.1–3.3）：PoC的12h AFL++ crash变体追踪与ASan锚定CodeQL候选合并，按bug类将同源证据折扣/封顶、跨family noisy-OR排序，top20函数交修复agent；编译/原PoC/testsuite循环不等于根因修复。
- **Key evaluation**（§4.1–4.4）：178 C/C++漏洞30项目，同GPT5.2后端；动态oracle后305 plausible patches由匿名专家评根因/症状及无关修改。Kumushi/Codex oracle通过近似，根因修复129/119；聚合差距未达p<.05，不混用配对偏好显著性。
- **Direct limitation**（§6 Limitations of Crash-Anchored Localization）：不透明bytecode/IPC边界可能使根因不可由crash证据到达；依赖fuzz预算、sanitizer与基础设施；专家判断不规模化，不提供所有路径无漏洞证明。
- **采用边界**：漏洞补丁通过 oracle 不等于修复根因；动态定位多样化、加权证据排名与 root-cause 评价改变 repair 验收目标。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“漏洞补丁通过 oracle 不等于修复根因；动态定位多样化、加权证据排名与 root-cause 评价改变 repair 验收目标。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks](https://arxiv.org/html/2605.04256v1)

- **Method**（§III–§V）：定义 capability descriptor、timing/lifecycle/telemetry contract，并把 control plane、twin plane 与 substrate-specific data plane 分离；task matcher 只能在当前 readiness、policy 与 twin validity 下提出 backend。
- **Key evaluation**（§VII–§VIII）：reference prototype 覆盖三类代表性 backend、HTTP externalized path 与 Cortical Labs wetware-facing API；验证 descriptor portability、runtime-aware matching、代表性故障下的 telemetry recovery 与局部 control-path overhead。
- **Direct limitation**（§VIII-D）：证据是 reference architecture 与 prototype-level validation，不是成熟 substrate、跨地域分布式部署或生产安全证明；twin fidelity、物理漂移和 substrate-specific policy 仍需独立验收。
- **采用边界**：异构物理神经基底不能被压平成无状态 tool；control plane 必须暴露 capability、时钟、生命周期、遥测、校准与安全状态，并把 twin state 与真实 substrate execution 分权管理。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch83 已有唯一正文明确物理 capability 不能被普通 MCP tool schema 压平，并保留 calibration、safety、人工审批与 substrate adapter 边界；本轮恢复账本绑定，没有重复正文。

### [Laundering AI Authority with Adversarial Examples](https://arxiv.org/html/2605.04261v1)

- **Method**（§3.2–3.5；§4.1–4.2）：三方 observer/model/adversary 定义同时要求行为达标与观察者约束；借公开视觉encoder代理使模型感知与观察者感知错配。
- **Key evaluation**（§5 setup 与四类案例/量化对照）：六个production VLM及图像服务，手选source/target并给多对量化结果；证明该错配可被利用，不估计自然流量攻击率。
- **Direct limitation**（§6.1）：依source/target/prompt选择；输出详细信息可能暴露错配，文字/OCR通道可使攻击失败，扰动并非完全不可见。
- **采用边界**：VLM 的感知差异可被攻击者用来借模型权威背书外部观察者看到的另一内容，使视觉输入成为 effect-side trust boundary
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch72 已明确多模态输入的 provenance/语义通道必须由独立 policy adjudicate，模型输出只是 proposal 而非 authority；视觉感知错配是该 trust-boundary 的受限攻击实例。

### [Parallel Prefix Verification for Speculative Generation](https://arxiv.org/html/2605.04263v1)

- **Method**（§3.1–3.2; Appendix A）：小模型完整draft先做full judge，失败后把多个chat suffix挂到共享causal draft上，用隔离attention mask并行判断各prefix；接受full、续写最长通过prefix或无边界restart。
- **Key evaluation**（§4.1–4.6）：Qwen235B/8B及GLM4.7/Qwen3.5跨族，4H200、greedy、instruct非CoT，知识/数学/code/chat；和适配SpecReason比较，EAGLE3可组合，partial verification消融区分吞吐贡献。
- **Direct limitation**（§4.4; Appendix C scope）：跨族GPQA可能因验证开销变慢；judgment阈值/提示是经验校准，准确率接近但非目标分布精确保持，不能当lossless speculative decoding。prefix通过也不构成逐步真值证明。
- **采用边界**：semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`INFER-SPECULATIVE-DECODING` 正文中的 `SF-2026-ARXIV-2605-04263` 已承载“semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Explaining and Preventing Alignment Collapse in Iterative RLHF](https://arxiv.org/html/2605.04266v1)

- **Method**（§3–5; Appendix C.3.1）：将当前policy输出改变未来RM最优响应的steering梯度写入bilevel目标；exact Hessian影响近似为梯度内积。实用oracle-free proxy丢失过置信方向，不能等同exact自校正。
- **Key evaluation**（§6 Table 2; Appendix C.3）：10维MLP模拟及Llama1B LoRA、冻结DeBERTa主干/可训练RM head、500轮BoN8；817 TruthfulQA由70B judge评。relaxed借oracle方向优于baseline p=.014，oracle-free差异p=.41不显著。
- **Direct limitation**（§7; Appendix C.3.1）：强凸RM best-response不适用于一般神经RM；LLM proof-of-concept小尺度且oracle为冻结LM CE代理而非人类真偏好。不得采用不可避免collapse/实用惩罚普遍防collapse断言。
- **采用边界**：iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-2026-ARXIV-2605-04266` 已承载“iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Adapt or Forget: Provable Tradeoffs Between Adam and SGD in Nonstationary Optimization](https://arxiv.org/html/2605.04269v1)

- **Method**（§2–4; Theorem 3.1）：在可预测漂移分布、bounded gradient/subGaussian noise及adaptive strong monotonicity下分解Adam tracking误差为初始化、目标漂移、动量记忆、preconditioner扰动；与SGD的噪声平滑/适应速度交换。
- **Key evaluation**（§5; Appendix F.1–F.2）：四个在线合成问题，normalized random-walk target、高漂移低噪/低漂移高噪；双方同LR grid、三seed，gradient clip10/box投影匹配假设。
- **Direct limitation**（§6; Assumptions 2.1–3.1）：有界梯度对pathwise控制关键；tracking条件不是任意非凸训练成立，minimax最优性未证明。只能用来解释state陈旧的受限机制，不能规定所有非平稳任务必选SGD。
- **采用边界**：非平稳目标下 Adam 的历史矩估计会变成 stale state；优化器选择取决于 gradient noise 与 objective drift 的相对主导
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-PRETRAINING` 正文中的 `SF-2026-ARXIV-2605-04269` 已承载“非平稳目标下 Adam 的历史矩估计会变成 stale state；优化器选择取决于 gradient noise 与 objective drift 的相对主导”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Gradient Flow Structure and Quantitative Dynamics of Multi-Head Self-Attention](https://arxiv.org/html/2605.04279v1)

- **Method**（§2–§4）：在单位球面 token dynamics 上定义多头 interaction field 与总能量，分解每头输出的切向分量和 radial shadow，并给出 per-head 单调性的充分 Radial Dominance 条件及近似正交鲁棒性。
- **Key evaluation**（§5–§7）：主要证据是定理：标量/equiangular regime 给出 critical inverse temperature、异质头的 super-additive early clustering rate、ReLU/softmax 线性化时间分离与 entropy production identity；不是生产模型 benchmark。
- **Direct limitation**（§8；assumptions in §3–§7）：许多结论依赖 score symmetry、sphere-normalized dynamics 或 scalar/equiangular regime；未证明训练后真实 Transformer 的所有 heads 满足充分条件，也未给出通用因果功能分工。
- **采用边界**：多头 Attention 的总能量可具有梯度流结构，但单头演化仍经共享 token state 和球面投影发生 radial-shadow 耦合；head 正交不等于优化动力学独立。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch15 已写入共享 token trajectory 与 radial-shadow coupling，使 head 正交不再被误解为逐 head 动力学独立；Radial Dominance 仅保留为受限充分条件。

### [Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion](https://arxiv.org/html/2605.04291v1)

- **Method**（§3–§3.1；Appendix A/D）：把单位置条件重采样解释为 mask-infilling，使用共享 causal/masked 权重的 UL2 构造能量与 stationary-distribution proxy，再增加 timestep embedding 并以 score-entropy objective 训练反向 Glauber dynamics。
- **Key evaluation**（§4.1–§4.4）：在 UL2/T5-Gemma 规模与语言建模、commonsense、Sudoku/Zebra 上比较 diffusion 与 AR；iso-compute 比较把一次 AR pass 加一次 full edit 与两个 AR candidates 对齐。结果依赖作者 evaluator 和有限模型。
- **Direct limitation**（§7）：比既有 discrete diffusion 与 AR 需要更多 model invocations；大模型训练披露为 32×H100 近 6 天。stationary/energy 解释不等于有限步采样已经收敛，也不证明生产 latency 或 streaming 优势。
- **采用边界**：离散 text diffusion 可把预训练 causal/masked LM 作为能量/条件分布来定义 Glauber transition，并以迭代局部重写换取全局修正；这与均匀 corruption 的从零训练是不同分支。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch24 已写入复用预训练 causal/masked LM 条件分布定义 Glauber-style 局部 transition 的分支，并保留有限步非稳态、NFE、streaming 与 AR fallback。

### [LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy](https://arxiv.org/html/2605.04295v1)

- **Method**（§3.1–3.2; Theorem 1/2）：semantic cluster uncertainty按brittleness特征放大，正确response子集quantile决定acceptance/response set；这是正确样本被保留的coverage，不是accepted response正确率下界。
- **Key evaluation**（§4.1; Appendix B）：五QA/math数据、四7B、每题10sample、60/40cal-test；经验AUROC/acceptance/risk，但AppendixB条件为correct，§4.1 P-Cov及selective-risk文字反向解释。
- **Direct limitation**（Theorem 1/2 proofs vs §4.1）：P(accept|correct)不推出P(correct|accept)≥1−α；多response同prompt依赖及score使用calibration统计还需交换性细化。当前不采用‘strict selective risk≤α’保证，保留受限UQ信号问题。
- **采用边界**：选择性拒答需要区分P(accept|correct)与P(correct|accept)；本文把两者混用，不能采用其风险保证。
- **审阅/Books**：exact-v1 Source Review 完成；争议：ACSE 对两个条件概率的叙述存在混淆；需 exact-v1 勘误并在同一 calibration split 上复算 coverage/risk 后才重开。

### [SWAN: Semantic Watermarking with Abstract Meaning Representation](https://arxiv.org/html/2605.04305v1)

- **Method**（§3.1–3.3）：私有AMR模板bank引导逐句生成，parse-back的S2match不达阈值则rejection、预算内换模板；检测以句子最匹配bank模板及段落hit-rate z-test判水印。
- **Key evaluation**（§4.1–4.6）：RealNews前250种子、14B生成、50模板bank及≤800消融、三paraphraser；1250句平均17.7次尝试对SemStamp13.8，体现鲁棒性与额外生成成本交换。
- **Direct limitation**（Limitations）：AMR误解析会降recall或抬false positive；仅英语新闻，专业/低资源语种未验证；bank保密是安全条件，不能宣称密码学不可伪造或所有语义改写稳健。
- **采用边界**：token-level watermark 在改写下易失效；AMR 语义结构嵌入及 parser 检测提供不同 provenance 机制，需核查语义保持与解析误差。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch72 已把 threat model、untrusted input/artifact、model sensor、authorization、effect 与 rollback 分层；本材料的窄命题“token-level watermark 在改写下易失效；AMR 语义结构嵌入及 parser 检测提供不同 provenance 机制，需核查语义保持与解析误差。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping](https://arxiv.org/html/2605.04308v1)

- **Method**（§2–§3; first-order Markov and special-token formulation）：把新词学习分成固定旧词转移字典与新词→旧词稀疏混合，仅训练新增 embedding；无遗忘定理把旧→新及新→新转移置零，并要求均匀新词出现、混合可辨识与 Lipschitz 有界参数。
- **Key evaluation**（§4; arithmetic / synthetic words / multilingual experiments）：Llama3.2-3B 只训练3072个特殊token参数，100–8000训练例/1000留出算术；另测Llama1B合成词与Qwen3B西/德/阿语迁移及英语保持。与全量微调的遗忘对比提供受限机制证据。
- **Direct limitation**（§3 assumptions; Discussion）：一阶转移与均匀频率、分离常数和表达能力是假设；真实语言实验放松了理论禁止转移，不能继承零遗忘保证；高阶上下文扩展有词汇状态爆炸，样本界的常数仍可随词汇变坏。
- **采用边界**：新知识通常靠权重更新并承担遗忘；Markov token 状态扩展与 token-to-dictionary embedding tuning 给出保留旧转移的条件，需限定模型化假设而非承诺真实 LLM 零遗忘。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：一阶 Markov token-to-dictionary 构造只覆盖其样本效率理论，未建立现代 LLM embedding、参数知识或外部 memory 的更新机制。

### [Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games](https://arxiv.org/html/2605.04312v1)

- **Method**（§2 game protocol; Bayesian ranking）：7名匿名参与者经5轮淘汰与终局投票，胜者数据进入Bayesian Plackett–Luce排名；是互动竞争偏好而非单题正确率。
- **Key evaluation**（§3 experimental setup / ranking; 999 completed games）：49模型、999完整日志，后验2000采样/500burn-in；匿名化与同供应商偏好分析测试社交推理，但排名条件化于实际对手池。
- **Direct limitation**（Limitations）：低表现、供应商与成本影响参赛池随时间变化；模型未显式建模pairwise matchup，低风险游戏不能证明真实高风险社交能力，也不保证永不饱和或污染免疫。
- **采用边界**：多智能体对局生成的新鲜任务可以同时缓解 benchmark 饱和与训练污染，但测到的是特定 game policy 下的相对能力
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“多智能体对局生成的新鲜任务可以同时缓解 benchmark 饱和与训练污染，但测到的是特定 game policy 下的相对能力”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [The Scaling Properties of Implicit Deductive Reasoning in Transformers](https://arxiv.org/html/2605.04330v1)

- **Method**（§3.1–3.5 / §5.2–5.4）：合成Horn clauses按逻辑深度平衡，r2构造相反label近表面特征配对，双向problem prefix与彼此隔离的direct/CoT分支联合目标减弱shortcut；不能泛化为所有Transformer宽深度定律。
- **Key evaluation**（§6.1–6.3 / Figures 5–6）：Llama式小toy模型，训练≤30 predicates/深度6，测试≤60/深度12；8→128层在训练horizon闭合implicit/explicit差距，CoT仍更善深度外推。
- **Direct limitation**（§7.1 / §4.1–4.3）：短上下文合成任务，r2仍有高阶shortcut且难构造，双向mask难迁移多轮；复杂度界依赖算法/每层顺序检索及标准复杂度假设，非一般自然语言LLM下界。
- **采用边界**：隐式推理的规模泛化不等于深度泛化；Horn-clause 受控任务分离图宽度/拓扑与深度外推，改变何时需要显式 CoT 的判断。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch14 已把 Q/K/V 内容路由、跨位置聚合、causal mask 与后续组合层职责分开；本材料的窄命题“隐式推理的规模泛化不等于深度泛化；Horn-clause 受控任务分离图宽度/拓扑与深度外推，改变何时需要显式 CoT 的判断。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Resilient AI Supercomputer Networking using MRC and SRv6](https://arxiv.org/html/2605.04333v1)

- **Method**（§2.1–2.4; §3）：MRC每packet携地址/key实现乱序写，EV跨plane/path喷洒；SACK/trim-NACK快速重传、故障EV退出与probe复活；EV映射静态SRv6路径，让端点承担path health，非动态BGP收敛替代名称。
- **Key evaluation**（§5.1; §5.2.2/6/7/8）：50K/75K生产training故障事件、42K NCCL sendrecv及小型Pollara/Thor RoCE对照；区分NIC–T0失带宽、T0–T1多路径掩蔽、all-plane损失测试。
- **Direct limitation**（§5.1; §5.2.7）：完整NIC光模块故障仍使QP失败；MRC只支持write/write-immediate，RoCE对照仅小规模且网络plane/PFC策略各用合适配置，不是同拓扑纯协议消融。1%全plane损失也仅约三分之一吞吐，不足持续训练。
- **采用边界**：large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-2026-ARXIV-2605-04333` 已承载“large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Budgeted LoRA: Distillation as Structured Compute Allocation for Efficient Inference](https://arxiv.org/html/2605.04341v1)

- **Method**（§3.1–3.3）：冻结dense W配可学习LoRA rank gates；按MAC cost顺序降低dense retention至cosine budget，EMA平滑。训练后显式按threshold删dense/SVD残余/保dense合并，raw系数变小本身不会省matmul。
- **Key evaluation**（§4–5; Appendix F）：固定6layer学生来自0.13B，teacher0.13/0.5/1B，2.55B Pile tokens、2A100；PPL与19个10shot function probes（三示例seed），ICL是低绝对能力下相对retention。
- **Direct limitation**（Appendix A; §5.1）：训练成本为adapted-module proxy而非硬件FLOPs/墙钟；速度只测替换压缩module不是全生成。阈值/预算/teacher温度迁移律、大模型和其他架构未验证。
- **采用边界**：parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-LORA` 正文中的 `SF-2026-ARXIV-2605-04341` 已承载“parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Perturbation is All You Need for Extrapolating Language Models](https://arxiv.org/html/2605.04344v1)

- **Method**（§2.1–§2.2; Assumptions1–2 / Theorems1–3）：在训练和推理均随机扰动前缀，以Jensen下界训练混合预测；实现主要为抽取前缀词、生成同义词后随机插入。外推定理依赖扰动可辨识及域外前缀与某训练前缀具有相同扰动分布。
- **Key evaluation**（§4; §4.3 ablation）：OPT125M/GPT2/GPTNeo1.3B在WikiText2训练、WikiText103/WebText/WritingPrompts域外测试，以Mauve/ROUGE1等衡量；仅训练或仅测试扰动不复现双阶段收益。
- **Direct limitation**（Assumptions1–2; §3 Remark1; discussion）：零外推不确定性是扰动桥接训练支持的强条件结论，不等于任意域外前缀语义正确；随机同义词操作不自动满足该假设，实验仅支持所测小模型和文本分布，学习扰动器/多模态仍属未来工作。
- **采用边界**：精确前缀条件预测受经验支持域限制；先扰动到语义邻居的 pre/post additive-noise 模型给出外推条件，改变采样/输入扰动的适用解释。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：perturbation extrapolation 依赖强 support-bridging 假设，未给出可迁移到开放语言分布的 sampling/runtime contract。

### [Covariance-Aware Goodness for Scalable Forward-Forward Learning](https://arxiv.org/html/2605.04346v1)

- **Method**（§3.1–§3.6）：每个 block 用局部交叉熵且在边界 detach；BiCovG 以跨通道投影和多尺度聚合保留二阶信息，FAL 在隔离块边界做零初始化校正，HGB 用 block size m 控制梯度传播 horizon。
- **Key evaluation**（§4.1–§4.3；Appendix A）：CIFAR-100、Tiny-ImageNet、ImageNet-100 上以 VGG-16 比较严格 layer-local、不同 HGB block size 与 BP；m=4 在作者设置中把峰值显存降低约一半，同时保留更接近 BP 的准确率，并分别消融 covariance、FAL 与 fusion。
- **Direct limitation**（§4.3；§5；Appendix A.1–A.4）：证据限 CNN/VGG、监督分类与作者硬件；局部目标依赖标签、readout 和特征统计，未证明可扩展到 Transformer/LLM 预训练、跨设备通信或与 BP 等价。
- **采用边界**：全局反向传播和保存全网 activation 不是唯一训练契约；block-local goodness 可通过协方差统计、边界对齐和可配置梯度 horizon，在内存、跨层协同与准确率之间形成连续取舍。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch28 已解释 BP activation memory 与 checkpoint/recompute，但缺少改变梯度 ownership 的 block-local 训练分支；应补入从全局 BP 到可配置 gradient horizon 的演进，并保留端到端 BP fallback。

### [Coral: Cost-Efficient Multi-LLM Serving over Heterogeneous Cloud GPUs](https://arxiv.org/html/2605.04357v1)

- **Method**（§4.1–4.3; §5.1）：离线枚举有限节点组合并ILP求SLO下placement为Serving Template；在线跨model/region选实例以满足需求和资源约束，计新增实例初始化成本，缩容drain不迁移decode。
- **Key evaluation**（§6.1–6.7）：core20–40GPU部分真实硬件，extended100–300GPU全部模拟，Azure/BurstGPT与缩放Alibaba资源trace；30min实验每6min重配，成本按60min摊销；sim prefill/decode平均偏差5.6/7.2%。
- **Direct limitation**（§4.1–4.2; §6.1/6.6/6.7）：全部组合才有lossless分解，实用node/memory pruning仅有限敏感性支持；大规模/Helix对照模拟且跨论文数字，region内template，price/trace/初始化摊销条件影响cost，不能普遍最优或现场SLA保证。
- **采用边界**：heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`INFER-SCHEDULING` 正文中的 `SF-2026-ARXIV-2605-04357` 已承载“heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration](https://arxiv.org/html/2605.04361v1)

- **Method**（§3.1–3.6）：10设计任务比较7种前团队artifact与无context，再在两任务操纵prompt收敛压力；五persona独立工作后综合，以预定义tradeoff被讨论比例量exploration。
- **Key evaluation**（§4.8–4.9; §5）：Sonnet4、temperature.5、20trial/cell、2700+ runs；artifact方向随baseline探索变化，60对条件检验；irrelevant context也可能提高，不能把收益直接归属知识正确迁移。
- **Direct limitation**（§6.4）：单模型/同模型judge、作者tradeoff列表、固定5agent与设计任务；coverage不是架构质量/代码正确性，既有实现材料效应不能外推debugging或所有RAG。
- **采用边界**：context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-04361` 已承载“context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Mitigating Label Shift in Tabular In-Context Learning via Test-Time Posterior Adjustment](https://arxiv.org/html/2605.04363v1)

- **Method**（§4.1–§4.4; label-prior correction）：用模型预测类别边际/训练类先验比率校正后验，并以预测边际相对训练先验的交叉熵温度平滑；默认批量预测边际，也比较单样本方案。Bayes校正要求类条件分布固定，预测边际只是测试先验的插件估计。
- **Key evaluation**（§5.1–§5.2; accuracy/rank/ECE and shift tables）：253个OpenML数据集、50/50固定拆分、5种子及三种tabular foundation models；六档合成shift并比较EME/BBE。TabPFNv2平均shift准确率.775→.789/.792，no-shift均.818。
- **Direct limitation**（§4.4 vs §5.1 setup; label-shift assumption and oracle comparison）：正文§4.4的train oversampling叙述与§5.1改test固定train叙述不一致，合成shift实现需代码复核；预测边际误差和conditional shift不被Bayes公式消除，温度交叉熵不是纯分布距离，不能声称真实测试先验已识别或任意shift保证。
- **采用边界**：tabular ICL 受 context 类别先验偏移影响；test-time posterior/prior rescaling 无需重训，改变 label-shift 校准选择。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：tabular ICL 的 label-shift posterior adjustment 只在所测表格分类设定成立，未改变 LLM evaluation 或 in-context state owner。

### [Worst-Case Discovery and Runtime Protection for RL-Based Network Controllers](https://arxiv.org/html/2605.04373v1)

- **Method**（§4.1–4.3 / §5.1–5.4）：外层搜索时变场景最大化相对同场景最佳参考策略的regret；隔离各控制器闭环状态并验证外部条件同时生效。离线反事实标注→阈值规则→累计反例重新学整套规则，线上仅bounded action correction/abstain。
- **Key evaluation**（§6.1–6.2 / Figures 4–8）：Sage拥塞、Pensieve码率、Park负载均衡，原trace train/test拆分；搜索及保护对比fine-tuning/curriculum等。在线不跑参考策略，测controller+规则是否满足各自决策预算。
- **Direct limitation**（Appendix A.9 / §4.3）：近最坏regret证书依赖外层ε-optimal与参考误差δ，论文未证明任意RL solver满足；Sage/Park为启发式portfolio。保护限已观察state与搜索场景，不等价所有环境安全保证。
- **采用边界**：平均任务奖励不保证最坏情形 runtime 安全；bilevel regret 搜索反例再编译 counterfactual 干预规则，改变保护层如何从失败样本构造。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：这是 RL 网络控制器的 worst-case discovery/protection 机制，不是 VLA/Embodied 的 perception-action schema、物理 transition 或 safety envelope 证据。

### [Critical Windows of Complexity Control: When Transformers Decide to Reason or Memorize](https://arxiv.org/html/2605.04396v1)

- **Method**（§3–§4; §5.2–§5.3; AppendixA）：在固定累计weight-decay预算下改变施加窗口，以初始化尺度控制记忆/推理竞争；两时间尺度线性化解释中间窗口可能影响解选择。
- **Key evaluation**（§5.2–§5.3; modular addition / SCAN extensions）：720条anchor组合任务：同预算早窗OOD约.15、中窗.93、全程.91；但modular addition窗口grokking较全程约延迟5倍，SCAN jump全部窗口仍零序列准确率。负例界定窗口策略非通用改进。
- **Direct limitation**（AppendixA.6; cross-task extensions）：理论仅初始化附近线性化，忽略softmax/MLP及高阶项；经验依赖任务中两类解都可达，不能从小型组合任务推广为大模型通用weight-decay日程。
- **采用边界**：regularization timing creates a critical training window that changes the reasoning-versus-memorization basin
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开；本材料的窄命题“regularization timing creates a critical training window that changes the reasoning-versus-memorization basin”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Counterfactual identifiability beyond global monotonicity: non-monotone triangular structural causal models](https://arxiv.org/html/2605.04413v1)

- **Method**（§3；Theorems 1–3；§4）：证明 context-independent inverse transport 等价于 exogenous isomorphism 并导出完整反事实可识别性，同时给出 context-dependent transport 的反例；CausalInverter 用三角可逆层、orientation gate 与 transport-stability regularization 实例化。
- **Key evaluation**（§5.1–§5.2；Appendix C–E）：108 个合成配置、160 个 bridge runs，以及 MuJoCo Door/Push 的 state-based counterfactual 评价；Door 的强非单调区间支持结构偏置，Push 则显示在非单调性较弱时灵活 baseline 仍可更合适。
- **Direct limitation**（Appendix A.4–A.6；Appendix F）：只覆盖共享顺序 triangular SCM、mechanism-wise invertibility、低轨迹 state-based 环境；不处理 cyclic SCM、图像 world model、深 latent causal discovery，也不证明真实机器人因果变量完备。
- **采用边界**：非单调具身动力学的 counterfactual identifiability 不要求全局 monotonicity；triangular recursion 下还需 mechanism-wise invertibility 与 context-independent inverse transport，局部可逆本身不足。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch25 已区分 predictive continuation 与 unrestricted counterfactual contract，也提醒 structured factorization 不等于 causal identification；尚缺非单调 triangular 机制下的充分条件与“局部可逆仍不足”反例。

### [Demystifying Manifold Constraints in LLM Pre-training](https://arxiv.org/html/2605.04418v1)

- **Method**（§3 Algorithm1）：梯度/动量先投影切空间，再谱steepest direction、更新/权重比对齐和每步retraction；不是简单给Muon套weight decay。
- **Key evaluation**（§5; AppendixD.3）：120M/330M/1B Qwen3-like在OpenWebText训练，1D和embedding仍AdamW；MACRO与MuonH接近，RMSNorm存在时谱/Frobenius差异较小。
- **Direct limitation**（§3 Assumptions1–2; §5）：光滑紧流形、有界方差与Lipschitz假设；整个spectral sphere非流形，需谱间隙受限集合。1B省略双循环SSO/FSO，固定种子不能给跨seed稳定性；不证明任意规模都可去Norm。
- **采用边界**：explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-PRETRAINING` 正文中的 `SF-DEMYSTIFYING-MANIFOLD-CONSTRAINTS-IN-LLM-PRE-TRAINING` 已承载“explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning](https://arxiv.org/html/2605.04421v1)

- **Method**（§3.1.2–3.3）：先计算dense QK得top-k，再对选中pair作门控ODE logits/Euler精炼并clamp步长；输出后query-sigmoid gate与hyper-connections。稀疏的是后续pair处理，未消除dense选择成本。
- **Key evaluation**（§4.1–4.6）：不规则spiral/eventMNIST、ETTm1/Jena、控制模拟；top-k等消融5初始化。效率仅T4、d64、batch1、seq1024、10 forward均值，不是LLM serving benchmark。
- **Direct limitation**（§4.5 / §5 Discussion）：Top-k可能丢上下文；unconstrained hyperconnections可破坏identity传播，大规模训练未验证。所测sink注意力0.255→0.249仅缓解，不支持通用sink-free或LLM替换。
- **采用边界**：离散 attention 与连续 RNN 的组合缺少统一状态解释；attention-logit ODE 及门控极限连接 SDPA/CT-RNN，提供可核验的 sink 控制设计分支。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch14 已把 Q/K/V 内容路由、跨位置聚合、causal mask 与后续组合层职责分开；本材料的窄命题“离散 attention 与连续 RNN 的组合缺少统一状态解释；attention-logit ODE 及门控极限连接 SDPA/CT-RNN，提供可核验的 sink 控制设计分支。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting](https://arxiv.org/html/2605.04426v1)

- **Method**（§3.1–§3.4）：以430行语法提示进行原子命题/符号压缩，单次LLM调用内六遍整理和12点自检；自检不是独立语义验证器。
- **Key evaluation**（§4.3; §5.1/5.4）：原文/压缩文MCQ对照、LLMLingua2基线；4081 key facts中nano有187项原对压错，日期/单位/条件词为实际失真。
- **Direct limitation**（§8）：英文+OpenAI生成和评价QA、每chunk额外调用；多轮动态context架构只论证格式可行，未做长会话实验，不能采用无损或持续状态正确性保证。
- **采用边界**：固定比率 token 删除会丢关系；原子事实行与符号语义重写同时形成压缩和寻址索引，改变压缩单位而非仅换摘要 prompt。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch75 已把不可变 source、active context、derived summary、回读与丢失 fallback 分权；本材料的窄命题“固定比率 token 删除会丢关系；原子事实行与符号语义重写同时形成压缩和寻址索引，改变压缩单位而非仅换摘要 prompt。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning](https://arxiv.org/html/2605.04431v1)

- **Method**（§III; §V）：16故障/5族注入并筛保已呈现预期签名的run；正常profile校准IVS、时序指纹分类，再由agent诊断→配置干预→重验。
- **Key evaluation**（§VI-A/D/E/F）：RFT-FaultBench、20step窗口、5fold、Qwen-plus干预；hard detection F1 70.75%，diagnosis50.16%；mitigation46.25%而severity中位变化−5.84%。
- **Direct limitation**（§III-A/B; §VI-F）：注入且事后筛选的可辨识故障不覆盖真实纠缠故障；自动干预中位反而恶化，不能由检测准确率推出自治修复安全，仍需回退和重新评价。
- **采用边界**：RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO` 已承载“RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Misrouter: Exploiting Routing Mechanisms for Input-Only Attacks on Mixture-of-Experts LLMs](https://arxiv.org/html/2605.04446v1)

- **Method**（§2.3; §4.1–§4.3）：输入只读攻击先在可见MoE surrogate统计路由关联，再优化routing目标和输出目标；目标API只有query access，不直接改路由。
- **Key evaluation**（§5.1–§5.3）：白盒同模型与API迁移分开评测AdvBench/StrongREJECT；API一些pair有增益、GPT4o-mini/StrongREJECT较Jailbroken更差，ASR是guard分类结果。
- **Direct limitation**（§2.3; §5.1/5.3; §6）：surrogate routing loss不证明目标服务路由机制；本文把架构未由此确认的GPT4o-mini/Phi4等直接列MoE，不能继承该身份断言。单surrogate与不自然token优化限制迁移，局部防御有utility/cost代价。
- **采用边界**：MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-MISROUTER-EXPLOITING-ROUTING-MECHANISMS-FOR-INPUT-ONLY-ATTACKS-ON-MIXTUR` 已承载“MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving](https://arxiv.org/html/2605.04450v1)

- **Method**（§3–§4）：以 online residual policy 调整 EMB/KV 分区，以 burst-aware recovery 限制突发期动作，并让 router 同时考虑 KV residency、embedding locality 与 node load；allocation proposal 不等于迁移已经完成。
- **Key evaluation**（§5–§6）：三类 production-scale dataset、32-node A100、8K–15K sequences、Steady/Trend/Burst 三类 workload regime 与五次重复运行；P99 与 SLO 数字只属于所披露模型、硬件、分区和路由实现。
- **Direct limitation**（§7）：证据来自生成式推荐的 EMB/KV 双缓存，不证明普通 LLM serving 也存在相同比例或收益；online controller 还引入 H2D refill、policy drift、跨节点路由与 burst recovery failure。
- **采用边界**：当 embedding hot cache 与 KV cache 竞争同一 HBM 时，静态分池会随 workload regime 变化而失效；memory allocator 与 request router 必须共享同一容量、迁移与 tail-SLO contract。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch54 已写入 EMB/KV 双 cache 共享 HBM 时 allocator 与 router 的联合控制，并保留迁移提交、P99、burst failure 与静态分区回退边界。

### [Deployment-Relevant Alignment Cannot Be Inferred from Model-Level Evaluation Alone](https://arxiv.org/html/2605.04454v1)

- **Method**（§1.3; §3）：把部署行为写成模型、scaffold、上下文共同函数，锁定8维rubric编码benchmark实际计分属性，而非把judge基础设施当用户可验证性。
- **Key evaluation**（§3.3; §5.3; AppendixG）：11+5 benchmark双人编码；180 transcripts/3模型/4scaffold的盲评，D1–D3对scaffold响应依模型异质，不能仅模型分数识别部署行为。
- **Direct limitation**（§5.4; AppendixG What this shows and does not show）：rubric非中立穷尽，16目录非全生态；180为小型stress test，不是参与者成功/repair burden的全因子实验，D4–D8未在stress test计分。
- **采用边界**：deployment claims require interaction and scaffold evidence rather than model-only scores
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“deployment claims require interaction and scaffold evidence rather than model-only scores”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Stream-T1: Test-Time Scaling for Streaming Video Generation](https://arxiv.org/html/2605.04461v1)

- **Method**（§3.2–§3.4）：前chunk优选噪声关联初始化、图像/视频reward beam pruning；移出KV低质丢弃，高质连续EMA，高质transition另建sink。
- **Key evaluation**（§4.1–§4.4）：LongLive/Wan1.3B、seed42、946 VBench5秒/128 MovieGen30秒；去memory改善imaging却损一致性，显示质量目标冲突。
- **Direct limitation**（§3.2–§3.4; §4.1）：reward降幅只是语义边界proxy，reward quality不构成KV语义正确保证；优选后的噪声非独立高斯，不能无条件继承文中边际严格不变说法；30秒单backbone不是无限流/有界总sink证明。
- **采用边界**：整段视频 TTS 候选探索昂贵且缺 temporal guidance；chunk noise 继承、跨窗 reward pruning 与奖励驱动被逐出 KV 的更新路径，提供 streaming 特有的质量/状态成本选择。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch24 已把 AR/diffusion 的 factorization、iterative state、correction、commit 与 runtime handoff 分开；本材料的窄命题“整段视频 TTS 候选探索昂贵且缺 temporal guidance；chunk noise 继承、跨窗 reward pruning 与奖励驱动被逐出 KV 的更新路径，提供 streaming 特有的质量/状态成本选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [KEET: Explaining Performance of GPU Kernels Using LLM Agents](https://arxiv.org/html/2605.04467v1)

- **Method**（§III）：代码先产performance hypotheses，再选择Nsight profiles/metrics检验，聚合附引用，reviewer按证据确认/反驳/未定；解释与优化执行分离。
- **Key evaluation**（§IV–§VI）：Rodinia9kernels+LULESH/XSBench，主要H100；3份报告、20下游尝试，可重试3次，以NSYS三次测时并单列pass@1。
- **Direct limitation**（§V-C; §VI-H/I）：speedup@1排除最终无效代码，不能当无条件部署收益；一些优势来自baseline退化，单profile难调launch，测试通过也非所有输入正确性证明。
- **采用边界**：Nsight 指标多不等于可操作瓶颈解释；由 profile 数据约束 agent 解释并测下游优化效果，需核其新增证据反馈能否改变 kernel 优化循环。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“Nsight 指标多不等于可操作瓶颈解释；由 profile 数据约束 agent 解释并测下游优化效果，需核其新增证据反馈能否改变 kernel 优化循环。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Stabilizing LLM Supervised Fine-Tuning via Explicit Distributional Control](https://arxiv.org/html/2605.04468v1)

- **Method**（§4.1–4.3）：current model 与冻结 SFT reference 插值得 dynamic anchor，内层在固定数据上离线蒸馏近似投影；区别于固定 teacher 或持续替换 reference。
- **Key evaluation**（§6.1–6.4）：iGSM/MedCalc/IFEval 目标训练，另用 MMLU-Pro/数学/代码评价遗忘；Qwen2.5 1.5–14B 与 Llama3.2-3B，作者按同目标数据/优化预算比较，并消融插值系数和更新计划。
- **Direct limitation**（独立 Limitation 段；§4.2；§5/Appendix A）：作者披露额外 forward 导致约 1.5–2 倍训练时延/内存开销；目前离线固定数据蒸馏。局部 KL/投影理论有支持与近似条件，不保证任意任务全局 retention。
- **采用边界**：current model 与冻结 SFT reference 插值得到 dynamic anchor，内层离线蒸馏近似拟合；改变 SFT 目标轨迹的控制，代价为额外 forward/memory，不是全局 retention 保证。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-SFT` 正文中的 `SF-STABILIZING-LLM-SUPERVISED-FINE-TUNING-VIA-EXPLICIT-DISTRIBUTIONAL-CONTR` 已承载“current model 与冻结 SFT reference 插值得到 dynamic anchor，内层离线蒸馏近似拟合；改变 SFT 目标轨迹的控制，代价为额外 forward/memory，不是全局 retention 保证。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies](https://arxiv.org/html/2605.04470v1)

- **Method**（§3.1–§3.4）：CRAFT 将真实 closed-loop policy gradient 分解为 proxy 与 residual：group-normalized counterfactual advantages 提供密集信号，interaction-critical rollouts 校正 proxy bias，EMA teacher 的 asymmetric KL 和 dual clipping 约束更新。
- **Key evaluation**（§4.1–§4.5；Appendix B–D）：Bench2Drive 的 hierarchical planning、VLA 与 vocabulary-scoring policies 上比较 closed-loop RL、counterfactual tuning 与组合；component ablation、scaling/stability 和 transfer 支持所测 simulator。作者修改了若干 protocol 细节，主结果不是未经变化的官方 harness。
- **Direct limitation**（§5；Appendix A.5、B、D）：counterfactual proxy 仍依赖 future evaluator，grounded residual 受稀有事件和 simulator realism 限制；EMA 自蒸馏可能保留错误，单一 driving suite 不证明真实道路安全或通用 VLA post-training。
- **采用边界**：具身策略 post-training 可把 dense 但有偏的 counterfactual supervision 当 proxy，再用稀疏但 grounded 的真实 closed-loop event 学 residual correction；两者必须在同一 on-policy visited-state distribution 下对齐。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch26 已区分 learned proposal、closed-loop observation 与 safety commit，但缺少 dense biased proxy 与 sparse grounded residual 的同分布组合，以及保留 pretrained behavior 的 teacher boundary。

### [Data-dependent Exploration for Online Reinforcement Learning from Human Feedback](https://arxiv.org/html/2605.04477v1)

- **Method**（§4.1–§4.4）：历史比较的表示协方差椭圆UCB给低覆盖方向exploration bonus；实践用median稳标、512维投影与分块刷新sampler，非照搬理论置信宽。
- **Key evaluation**（§5.1–§5.3）：Llama3-8B、同oracle/sampler/迭代预算，3轮onlineRLHF测六benchmark与同RM的IID/Alpaca；GPQA中间轮退化后恢复。
- **Direct limitation**（Assumptions1–3; §4.3; §5.1）：BT/线性reward/有限类与diversity是理论条件，经验bonus近似不自动保regret界；固定训练RM高分不同于人类偏好泛化。
- **采用边界**：online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN-` 已承载“online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](https://arxiv.org/html/2605.04478v1)

- **Method**（§3–5；§4.2.2）：各 rank 采集 host/kernel 指标和 collective trace，带外 analyzer 区分未进入、不一致、硬件挂起与计算/通信慢，定位根因 rank；不是自动恢复协议。
- **Key evaluation**（§6.1–6.3）：16 H20 功能故障注入、两个月最多 4000 GPU 日志；NCCL/RCCL 对照五种诊断基线。检测窗口 5 分钟/1 分钟与定位时延分开；人工基线时延含作者设定。
- **Direct limitation**（§4.2.2 与 §6.1–6.2 的直接配置/范围）：阈值依赖 baseline 和集群统计；所测故障与可观测 rank 指标界定覆盖，不证明所有故障或恢复动作。论文未单列自身 limitation；这里是直接设置限定及作者整改的外推边界，不引用 prior-work limitations 充数。
- **采用边界**：跨 host/kernel 的 rank probes 与 collective trace 支撑慢/挂根因定位；诊断证据不等于自动 remediation 的正确性或权限。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-CCL-D-A-HIGH-PRECISION-DIAGNOSTIC-SYSTEM-FOR-SLOW-AND-HANG-ANOMALIES-IN-` 已承载“跨 host/kernel 的 rank probes 与 collective trace 支撑慢/挂根因定位；诊断证据不等于自动 remediation 的正确性或权限。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Towards General Preference Alignment: Diffusion Models at Nash Equilibrium](https://arxiv.org/html/2605.04494v1)

- **Method**（§3.2–§3.3）：在online selfplay用current/previous policy与frozen reference双KL约束；理想OMD期望优势转为可算pairwise logistic surrogate和单扩散步损失。
- **Key evaluation**（§4.1–§4.2）：SD1.5/SDXL、PickaPic训练，三提示集评价；每prompt8图、五自动scorer平均rank选正负，评价也用这些scorer。
- **Direct limitation**（§3.3; §5）：方向监督不等于理想优势数值匹配；同五scorer生成与评价偏好有闭环偏差，没有真实非传递偏好或Nash duality gap收敛实测，不能把winrate提升说成已达Nash。
- **采用边界**：BT 标量偏好不能表达一般扩散偏好；self-play Nash 目标替代 reward-induced preference，改变 diffusion alignment 的目标建模。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch34 已把 preference pair、reference identity、relative margin、update sensor 与独立行为评估分权；本材料的窄命题“BT 标量偏好不能表达一般扩散偏好；self-play Nash 目标替代 reward-induced preference，改变 diffusion alignment 的目标建模。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](https://arxiv.org/html/2605.04495v1)

- **Method**（§3.2–§3.4）：query-only与query-document各多采样，双向entailment聚类最大簇比作confidence；低queryconfidence才按margin三档稳定重排，档内保原排序。
- **Key evaluation**（§4.1–§4.4）：BEIR四集/Qwen7B每输入10采样/top10，七reranker；强监督排序收益约.1–.2%，NQ端到端F1对照。
- **Direct limitation**（§3.4; §5.3）：明确Bayesian-style非校准posterior，稳定错答也可高confidence；额外采样/entailment费用、阈值验证与域外聚类错误均限制低延迟和可信度主张。
- **采用边界**：文档相关性不等于生成器有用性；query-only 稳定性为 control 估计 passage 边际影响，再最小 Kendall 修正排名，改变检索/生成衔接且不把稳定性当正确率。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch76 已把 query、chunk、retrieval candidate、sufficient evidence 与 evaluator 分开；本材料的窄命题“文档相关性不等于生成器有用性；query-only 稳定性为 control 估计 passage 边际影响，再最小 Kendall 修正排名，改变检索/生成衔接且不把稳定性当正确率。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [SCOUT: Active Information Foraging for Long-Text Understanding with Decoupled Epistemic States](https://arxiv.org/html/2605.04496v1)

- **Method**（§2.3）：探索轨迹H与带source span的知识E分离，最终答案只能看E；forage/read与update/evaluate拆动作，同backbone自判gap。
- **Key evaluation**（§3.1–§3.4）：LooGLEv2/InfinityBench、agent基线统一Sonnet4.5；去epistemic/grounding等消融，需注意去foraging等于不能访问文档的强消融。
- **Direct limitation**（Limitations; AppendixE.4）：多轮绝对延迟更高、每query重搜无法摊销；仅稀疏文本，source pointer/同模型gap判断不证明claim正确或证据充分，非通用有损摘要零失真。
- **采用边界**：long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-CONTEXT` 正文中的 `SF-SCOUT-ACTIVE-INFORMATION-FORAGING-FOR-LONG-TEXT-UNDERSTANDING-WITH-DECOU` 已承载“long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Distilling Bayesian Belief States into Language Models for Auditable Negotiation](https://arxiv.org/html/2605.04507v1)

- **Method**（§3.1–§3.4）：CaSiNo六种对手priority假设；全对话LM compatibility产生可审计posterior，teacher用posterior菜单评分，8BLoRA学生蒸馏posterior/intent/action标签。
- **Key evaluation**（§4.1/4.3; AppendixA）：150对话1054turn，Brier teacher.085/student.114/均匀.139；删除posterior标签学生决策更好，反转posterior仅1.8%动作变化。
- **Direct limitation**（§4.3; AppendixA）：逐utterance Bayes更新反而差于均匀；学生belief/action并行而非因果耦合，1054仅14原生结构bid，不把可解析belief称执行依据或真实人类心理。
- **采用边界**：可校准 belief 文本不等于因果 belief-conditioned action；Bayesian teacher 蒸馏与 posterior-prefix 干预分离报告和控制，改变 agent 可解释性验收。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“可校准 belief 文本不等于因果 belief-conditioned action；Bayesian teacher 蒸馏与 posterior-prefix 干预分离报告和控制，改变 agent 可解释性验收。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [From Priors to Perception: Grounding Video-LLMs in Physical Reality](https://arxiv.org/html/2605.04515v1)

- **Method**（§3.3–§3.5）：758正负视频对，经观察锚定/人工修改或合成/双人复核；VARC要求observation→attribution→verdict，LoRA绑定成对样本。
- **Key evaluation**（§4.1–§4.2）：604对训练/154对测试、统一16frames，VideoLLaMA3-7B平均paired accuracy41.56%，与零样本baseline比较。
- **Direct limitation**（§3.4–§3.5; Conclusion and Limitations）：明确观察链是模型输出约束而非因果充分证明，成对SFT梯度不必数学抵消共享特征；少量人工短视频，未证明开放真实物理域或工具安全。
- **采用边界**：视频物理错误可能混入生成 artifacts 或常识先验；物理程序生成对抗课程分离视觉事实与叙事先验，改变物理 reasoning 评价和监督。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch25 已区分生成 observation、action-conditioned dynamics、imagined rollout、真实 transition 与 planning authority；本材料的窄命题“视频物理错误可能混入生成 artifacts 或常识先验；物理程序生成对抗课程分离视觉事实与叙事先验，改变物理 reasoning 评价和监督。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks](https://arxiv.org/html/2605.04525v1)

- **Method**（§4.1–§4.2.3）：先训练 RSSM latent world model，并用 progress contrastive 与 inverse dynamics 形成任务状态；高层 diffusion 生成稀疏 subgoal，经 EBM guidance 与 local manifold projection 修正，低层 rectified flow 生成短轨迹，MPC 重规划后由 inverse dynamics 输出控制。
- **Key evaluation**（§5.1–§5.3；Appendix B–C）：FurnitureBench 仿真与四个真实装配任务、RLBench 18 tasks、OGBench 比较 diffusion/flow 的高低层组合；消融 world model、EBM guidance、projection 和两层生成器，真实任务每项 10 次评价且训练示范有限。
- **Direct limitation**（§6；§5.1.3；Appendix B–C）：依赖带成功/失败标记的 demonstration、RSSM 表示与 inverse dynamics；真实样本和 trial 数有限，未证明开放世界安全、任意 embodiment 迁移或 end-to-end latency SLO。
- **采用边界**：长时域具身规划可把探索性强但迭代慢的 diffusion 放在高层 sparse subgoal，把快速 rectified flow 放在低层 dense trajectory，并由在线 MPC 持续重规划。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch26 已有多时间尺度 controller 与 diffusion/flow action head，但尚未把两种生成范式按高层探索/低层实时性分权，也未写清 manifold projection、MPC replan 与 inverse-dynamics handoff。

### [SADE: Symptom-Aware Diagnostic Escalation for LLM-Based Network Troubleshooting](https://arxiv.org/html/2605.04530v1)

- **Method**（exact-v1 PDF §III pp3–4）：先reachability；无直接症状逐层探测，再按证据路由15故障skills，区分收集信息与提交根因。
- **Key evaluation**（PDF §IV–V pp4–7）：NIKA留出523incident/11scenario；同Sonnet基线F1约.55→.77，跨backend .40不当纯policy效果。
- **Direct limitation**（PDF §VI pp8–9）：stock injector并非每项故障真实生效；39训练例验证不能证明523测试标签，修正不保证只增分。median输入344k vs189k，少探测不等于便宜；模拟缺硬件/延迟/监控故障。
- **采用边界**：自由 ReAct 混合收集证据与承诺根因；phase-gated escalation 在同 backend 对照下提高诊断，改变工具诊断 workflow 的可行性判断。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch81 已把 phase state、retry/rollback、escalation 与 commit authority 组织为 durable workflow；本材料的窄命题“自由 ReAct 混合收集证据与承诺根因；phase-gated escalation 在同 backend 对照下提高诊断，改变工具诊断 workflow 的可行性判断。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization](https://arxiv.org/html/2605.04539v1)

- **Method**（§3.1–§3.3）：NLI与fluency dual signal构造DPO pair，乘性版本另ACR gate/length penalty，加性版本不含这些门；selector是事后经验。
- **Key evaluation**（§4–§5）：5学科各100test、13k学生SFT，500prompt多候选；同一NLI训练/评价，长度与judge偏差对照。
- **Direct limitation**（§3.3; §6.3）：复合分数更高不保证两个分量都更高，本文该句及梯度单调说法不成立；NLI循环评价、未盲held-out大型NLI、student参考质量限制。仅保多信号/评价反证，不采用无逻辑税保证。
- **采用边界**：偏好胜率会奖励冗长而不保证 entailment；NLI/verifier 混合信号及相反 judge 排序改变知识生成的偏好目标和评价。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch34 已把 preference pair、reference identity、relative margin、update sensor 与独立行为评估分权；本材料的窄命题“偏好胜率会奖励冗长而不保证 entailment；NLI/verifier 混合信号及相反 judge 排序改变知识生成的偏好目标和评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation](https://arxiv.org/html/2605.04542v1)

- **Method**（§4.1–4.2 / §5.1–5.3）：序列power distribution不同于逐token temperature，差异依赖suffix Rényi entropy；sequence logprob self-reward的KL-RL population最优给power target，换成forward-KL离线蒸馏共享目标而非同一受限优化过程。
- **Key evaluation**（§6.1–6.2 / Appendix B）：Qwen7B/Phi3.5数学代码GPQA，主500 MATH样本LoRA；MH power α4、温度0.25及随机权重负控。真实reward变化与self-reward协方差相连，弱基座/负相关不保证改进。
- **Direct limitation**（§7 Limitations / Proposition 3 / §6.1）：有限horizon；sharpness定理假设有限可实现策略类、IID准确target样本。实验self-reward用completion平均logprob，不与变长序列未归一logprob定理直接等同；离线采样成本未消失。
- **采用边界**：逐 token power sampling 不等于序列分布幂变换；后缀信息与 true-reward/self-reward 协方差决定收益，改变温度自奖励的理论解释。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch20 已把 token distribution、sampling policy、calibration 与 sequence-level evaluation 分开；本材料的窄命题“逐 token power sampling 不等于序列分布幂变换；后缀信息与 true-reward/self-reward 协方差决定收益，改变温度自奖励的理论解释。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding](https://arxiv.org/html/2605.04543v1)

- **Method**（§3; Theorems3–6）：top-down传播prefix acceptance mass和scaled OT，postorder以预计算接受/残差分布选择；局部losslessness连接全树分布保真。
- **Key evaluation**（§5.1–§5.2）：SpecBench6域、Vicuna/EAGLE及Llama3.1、A6000三seed；acceptance length+7.5%对应约7%TPS，不只报接受率。
- **Direct limitation**（Theorem6; Limitations and Future Work）：conditional optimality是固定局部/混合采样约束，不是全树全局最优；温度0/近0无额外收益，树拓扑和采样策略耦合。
- **采用边界**：将多步、多 draft 的接受问题写为 conditional optimal transport，在给定 prefix 下构造接受方案；不是只重述 proposal-verification-commit 状态机。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch48 已把 proposal、exact verification、accepted prefix 与 rollback/commit 分权；本材料的窄命题“将多步、多 draft 的接受问题写为 conditional optimal transport，在给定 prefix 下构造接受方案；不是只重述 proposal-verification-commit 状态机。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs](https://arxiv.org/html/2605.04563v1)

- **Method**（§V-A–V-C）：数据生成 RID，存 ECC parity 后丢弃显式 RID；读时由数据重建 RID 并解码，受影响数值换范围代表值。错误-free 数据仍保留原精度。
- **Key evaluation**（§VI-A–VI-E）：SE/DAE/16E/32E/FC 注入比较 ECC/Weight Nulling/VAPI；PyTorch ResNet/Llama 权重和激活故障评价，每 BER 100 次。RTL 28nm 综合与 V100 模拟的硬件成本不等同生产 GPU 部署。
- **Direct limitation**（§V-A.3；§VI-A/VI-E）：超过 RID 纠错数仍 DUE 或罕见 SDC，整芯片故障未保证恢复；σ/映射粒度影响质量与面积，保护目标为 bounded approximate 而非 bit-exact。
- **采用边界**：Range Identifier 把显存错误保护从逐 bit 正确性改为数值范围内的有界近似恢复，新增了可声明的误差 contract
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`INFER-TENSORRT-LLM` 正文中的 `SF-RANGEGUARD-EFFICIENT-BOUNDED-APPROXIMATE-ERROR-CORRECTION-FOR-RELIABLE-D` 已承载“Range Identifier 把显存错误保护从逐 bit 正确性改为数值范围内的有界近似恢复，新增了可声明的误差 contract”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination](https://arxiv.org/html/2605.04568v1)

- **Method**（§4）：policy warm-start少量action trajectories，world-model梯度优化、receding-horizon复用、Qensemble分歧惩罚，替换MPPI而非单纯latent imagination。
- **Key evaluation**（§5.1–§5.6）：24controltasks，BMPC底座有收益，TD-MPC2底座不能稳定胜MPPI；4090实测低维约同MPPI延迟，调用数下降非同比wallclock加速。
- **Direct limitation**（AppendixA; AppendixE.3）：依赖强policy prior/模型梯度质量，少候选可能早收敛，高维较慢；单任务/短horizon，Acrobot模型误差小不证明通用防model exploitation。
- **采用边界**：在可微 latent world model 上通过梯度 MPC 优化动作，并与 gradient-free 计划比较；不能由该结果推导 uncertainty 为所有 latent planning 的必要条件。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch25 已区分生成 observation、action-conditioned dynamics、imagined rollout、真实 transition 与 planning authority；本材料的窄命题“在可微 latent world model 上通过梯度 MPC 优化动作，并与 gradient-free 计划比较；不能由该结果推导 uncertainty 为所有 latent planning 的必要条件。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/html/2605.04569v1)

- **Method**（§3.2–§3.5）：ISA 先按 saliency 预选 context K/V，再用 query sharpness 作为 approximation error proxy：高风险 query 走 full attention，低风险 query 走 blockwise zeroth-order Taylor sparse attention。
- **Key evaluation**（§4.1–§4.5；ablation）：LIVEditor-14B 与三类视频编辑 benchmark 上报告 attention-module latency 约降 60%；公开 sensitivity 显示提高 full-path sparsity 会降低质量，作者配置的端到端加速约 1.47×。数字只属于所披露模型/硬件与阈值。
- **Direct limitation**（§4.4–§5）：“near-lossless”是作者 benchmark 结论；query sharpness 不是通用误差证书，阈值、block shape、预选成本与视觉指标均 workload-dependent。unsupported shape 或 proxy 漂移时必须回退 full attention。
- **采用边界**：动态稀疏 Attention 不应只按 token saliency 剪枝；execution plan 可依据 query-specific approximation-risk proxy，在 full attention 与低阶近似路径之间逐块路由并保留 exact fallback。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch49 已写入 query-specific approximation-risk 驱动 full/Taylor sparse attention 的条件执行分支；proxy 只提出路径，runtime 与 full attention fallback 保留提交权。

### [From Parameter Dynamics to Risk Scoring : Quantifying Sample-Level Safety Degradation in LLM Fine-tuning](https://arxiv.org/html/2605.04572v1)

- **Method**（§3.2–§4.3）：用已训练危险/安全方向跟踪drift；样本单步LoRA权重更新按module归一化，危险减安全投影作SQSD，选择高敏感初始化checkpoint。
- **Key evaluation**（§5.1–§5.3）：3模型、Dolly/Alpaca、三安全benchmark，风险分5子集再分别训练；10/12配置ASR排序单调，并测8B→14/32B和LoRA→FFT。
- **Direct limitation**（§4.2–§4.3; §6 Outlook）：一阶Taylor和module normalization不等于精确累计损害；依赖方向/初始化敏感性、特定ASR judge，不是数据无害通用证书；与安全微调联合尚未来工作。
- **采用边界**：fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-FROM-PARAMETER-DYNAMICS-TO-RISK-SCORING-QUANTIFYING-SAMPLE-LEVEL-SAFETY-` 已承载“fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://arxiv.org/html/2605.04595v1)

- **Method**（§3–§4）：以增长KV驻留的memory-time需求建连续batch队列，joint input/output分布决定容量；λ>μ不稳定，λ<μ(1−δ)是所建策略充分条件，中间留界。
- **Key evaluation**（§5.1–§5.3）：Llama3-8B/vLLMv1/A100，单卡与8独立replica，合成PD与LongBench2校准batchtime后实测误差约10%以内。
- **Direct limitation**（§3; §6 Scope）：固定近饱和batchtime、单请求远小于M、独立到达、免费swap是假设；容量用数据估计，不给P99/SLO保证；8卡为DP非TP，PP/PD分离改变队列拓扑未证明。
- **采用边界**：KV capacity and queue stability must be analyzed together under arrival and service contracts
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch45 已把 KV identity、保留/压缩/驱逐、恢复误差与 correctness fallback 绑定；本材料的窄命题“KV capacity and queue stability must be analyzed together under arrival and service contracts”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Temporal Structure Matters for Efficient Test-Time Adaptation in Wearable Human Activity Recognition](https://arxiv.org/html/2605.04617v1)

- **Method**（§4.1–§4.3）：前belief经prototype预测feature，surprise释放惯性；几何位移+flattened habit决定转移方向，soft prototype更新并锚回source初始化，无backprop。
- **Key evaluation**（§5.1–§5.3）：HARTH/CAPTURE24按时间顺序跨subject、各6对/3seed同源模型，以macroF1及efficiency比较；不是打乱流协议。
- **Direct limitation**（AppendixA3 Limitations）：source校准影响早期，shuffle/稀疏/突变削弱时间信号；仅accelerometer跨subject，长期/跨设备/多模态尚未证实，soft update也非漂移免疫。
- **采用边界**：把 vision TTA 平滑直接套流式传感会错过状态转换；feature surprise 按 prototype 几何决定惯性保持/释放，提供无反传在线适配机制，适用范围限 WHAR。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：wearable activity recognition 的 temporal test-time adaptation 属于领域模型方法，未改变 LLM SFT 数据、objective 或 artifact lifecycle。

### [AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair](https://arxiv.org/html/2605.04624v1)

- **Method**（§3–6；Appendices B/P）：测 repair selector 对 evaluator channel 的依赖，以配对 channel surgery 和 sham/off-target 对照分离阻断路径与一般 winner change。
- **Key evaluation**（§4；§6）：576000 是注册 cell，只有 96000 executed paired traces；80 source-level surgery cases 覆盖三开源 agent，比较 path-block AUROC、排名与负控制。
- **Direct limitation**（§13 Limitations, governance, and conclusion）：作者明确不恢复潜在因果构念、不认证机制、不声称强 prospective validity；依赖内部 observability，closed API/GUI-heavy 不属 primary scope，独立组仍由维护者选择。
- **采用边界**：repair selector 使用 evaluator signal 形成测量 coupling；channel-blocking 配对对照可改变方法排名，要求分离用于选择与用于独立验收的信号。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-AUDITREPAIRBENCH-A-PAIRED-EXECUTION-TRACE-CORPUS-FOR-EVALUATOR-CHANNEL-R` 已承载“repair selector 使用 evaluator signal 形成测量 coupling；channel-blocking 配对对照可改变方法排名，要求分离用于选择与用于独立验收的信号。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies](https://arxiv.org/html/2605.04637v1)

- **Method**（§3–§5）：以 ACR/AMR × PM/Engineering/Ops × T4/T5 组织 68 个指标，并按 deterministic、LLM、human、expert judge tiers 组合需求、代码、运行、运维和安全证据。
- **Key evaluation**（§6–§7）：六个平台、三个领域、18 个 evaluation cells；报告 specification bottleneck、frontend/backend decoupling、production-readiness cliff 与安全/并发失败。AMR 只在 QwikBuild 上执行，结论是描述性样本。
- **Direct limitation**（§8）：作者中两人与 QwikBuild 有关联；平台、prompt、版本、部署环境和 judge 有限，AMR 横向不可比。不能从分数推断所有 vibe-coding 平台或真实长期维护能力。
- **采用边界**：Coding-agent 平台评价必须区分从零创建与修改既有系统，并沿 requirements、artifact、runtime、operations 与 security 保存分阶段 evidence，避免漂亮 UI 掩盖后端和生产失败。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已区分 static issue、从零 repository、需求访问、完整 artifact、测试、部署/安全与 environment identity，并要求分阶段 evidence；该 68-metric benchmark 提供实例，但未改变现有主线。

### [Gradients with Respect to Semantics Preserving Embeddings Tell the Uncertainty of Large Language Models](https://arxiv.org/html/2605.04638v1)

- **Method**（§3.2–§3.3）：paraphrase within/between差选semantic-preserving token，top-half hidden梯度按detached tokenentropy加权；HybridGrad依熵混合LM-head梯度。
- **Key evaluation**（§4.1–§4.2）：3开放模型/3QA集，用BEM正确性与AUROC；SemGrad在多答案TruthfulQA更好，单答案有时不及parameter gradient。
- **Direct limitation**（§3.3; AppendixA）：semantic proxy非完美语义隔离，白盒需梯度/权重，短claim实验不能保证长输出；AUROC区分力不是校准概率或epistemic/aleatoric精确分解。
- **采用边界**：把白盒 gradient signal 作为 hallucination sensor，而不是把生成概率直接当作事实置信度
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“把白盒 gradient signal 作为 hallucination sensor，而不是把生成概率直接当作事实置信度”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving](https://arxiv.org/html/2605.04647v1)

- **Method**（§4.1–§4.5；§5）：goal-point posterior 提供行为级候选，masked discrete diffusion 起草 trajectory token，AutoEdit 在同一 token space 直接替换选中位置；完整 draft-and-edit rollout 接收终局 RL reward，并复用 shared-prefix KV、回卷 action cache 后重算 mutable block。
- **Key evaluation**（§6.1–§6.5）：NAVSIM 上用 0.7B backbone、0.1B ViT、4 秒/2Hz trajectory 和 SFT→RFT；标准 PDMS、AutoEdit/RL 消融及 NVIDIA Thor 路径支持所披露 operating point。best-of-6 的 94.8 是 oracle，不属于标准在线结果。
- **Direct limitation**（§7）：固定分辨率 BEV token 限制精度，RL reward 是 proxy，未在更高保真 simulator 验证；编辑扰动集中纵向/横向误差，31.8ms 平均延迟不证明尾延迟或安全闭环。
- **采用边界**：具身 action token 可以先并行 draft、再原位 edit，但 revision 必须和 full-rollout RL credit、mutable action cache invalidation 及最终 controller commit 同时设计。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch26 已讨论 action chunk、fast/slow controller 与 warm-start/refinement，但缺少同一离散 action space 的 draft/edit authority、full-rollout credit 以及编辑后 cache rewind/recompute 的一致性边界。

### [FAAST: Forward-Only Associative Learning via Closed-Form Fast Weights for Test-Time Supervised Adaptation](https://arxiv.org/html/2605.04651v1)

- **Method**（§4.1–4.2 / Appendix B.3）：固定representation以截断SVD伪逆求fast linear weights，预训练readout与importance scorer后冻结；测试适配免反传。累计KᵀK/KᵀV可精确更新，但简单batch权重插值仅近似、不能称一般全历史精确最优。
- **Key evaluation**（§5–§6）：CLIP分类、GPT2情感/WikiText、Qwen3B/7B翻译；分清固定特征projection成本与完整模型、in-domain readout的upper bound，不把所有结果叫一次forward从零训练。
- **Direct limitation**（§7 Discussion and Limitations / Appendix B.3）：依赖冻结encoder表征，组合推理/规划弱；readout先训练。batch插值不一般等价合并least-squares，伪逆optimal只对固定特征线性目标，不保证无灾难遗忘。
- **采用边界**：新例子适配通常支付反传或长 context 成本；单遍把带标签例子编译进 fast weights，提供冻结表征下不同训练/推理成本分配。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“新例子适配通常支付反传或长 context 成本；单遍把带标签例子编译进 fast weights，提供冻结表征下不同训练/推理成本分配。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs](https://arxiv.org/html/2605.04665v1)

- **Method**（§III-A–D）：150base各原文+5变体，保payload但可改变task scaffold；分answer agreement、embedding similarity、length stability，固定组合权重。
- **Key evaluation**（§IV-B/E）：5API模型温度0共4500calls；mode collapse大量变体不再输出label，另部分label在长回答中，可区分接口失守和知识错答。
- **Direct limitation**（§III-A; §IV-F）：明确不是完整prompt严格语义等价；任务不均衡、单generator、wholeword会过计偶然标签，不能把SCS直接当模型语义推理能力或正确率。
- **采用边界**：semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-PARAPHRASE-INDUCED-OUTPUT-MODE-COLLAPSE-WHEN-LLMS-BREAK-CHARACTER-UNDER-` 已承载“semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement](https://arxiv.org/html/2605.04677v1)

- **Method**（§3.1–§3.5）：用 JFR 构造带 cumulative time/call count 的 component graph，选择热点并冻结邻接 read-only context；MCTS/evolution 生成局部 edits，级联 evaluator 决定 retention。
- **Key evaluation**（§4–§5）：Apex 20-iteration ablation 中 valid filter、context/sampling 与 MCTS 逐步加入；Java 只覆盖七个 hotspot functions，作者报告平均 15.22×，不等于 repository 或生产端到端加速。
- **Direct limitation**（§6.2）：依赖 profile 代表性、tests/KPI 完整性、语言 evaluator 和局部 writable-region 假设；combined score 聚合可能掩盖 component trade-off，性能测试噪声会污染 search。
- **采用边界**：LLM 代码优化应把 runtime profile 当作 target-selection evidence，把候选 edit 当作 proposal；只有通过 build、tests、performance 与静态检查的 artifact 才能进入搜索 population。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch81 已把 proposal、typed artifact、deterministic checks、retry/rollback 与 commit authority 分离；Ch49 已要求 profile→plan→correctness fallback。CodeEvolve 是受限组合实例，无需复制框架正文。

### [From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models](https://arxiv.org/html/2605.04678v1)

- **Method**（§4.1–§4.3）：统一VLA比较图像latent作轨迹中间监督的三接口与action token目标统一；四种均单次前向，不增加单独推理阶段。
- **Key evaluation**（§5.1–§5.4）：LIBERO-Long图像latent更强，RoboTwin四task action token更强；JAKA单臂10rollout、离散较连续平均+2–3pp。
- **Direct limitation**（§6）：比较supervision接口非latent模型本身优劣；单real embodiment，任务差异是经验而非对所有长程/灵巧任务普遍规律，强latent模型可改变排序。
- **采用边界**：latent action supervision changes the representation bridge between pixels, language and controllable action
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MULTIMODAL-EMBODIED-VLA` 正文中的 `SF-FROM-PIXELS-TO-TOKENS-A-SYSTEMATIC-STUDY-OF-LATENT-ACTION-SUPERVISION-FO` 已承载“latent action supervision changes the representation bridge between pixels, language and controllable action”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Average Attention Transformers and Arithmetic Circuits](https://arxiv.org/html/2605.04683v1)

- **Method**（Definitions2.13–2.15; Theorems3.1/4.7/4.9）：将受限hard-average attention与算术电路双向simulation，input携带电路编码，activation允许有限算术circuit。
- **Key evaluation**（§3–§4 constructive theorems）：固定深度K的semi-unbounded circuit可用维8、2K层averageattention模拟；唯一hardattention对应更受限fan-in；这是构造证明而非训练benchmark。
- **Direct limitation**（§5 Conclusion）：需有序含有理数ring及特定算术activation，普通FFN不自动做乘法；非uniform circuit family不能推出每一函数由一个普通softmax训练Transformer计算，未给可学习性/有限精度性能。
- **采用边界**：attention 计算能力不能只用通用逼近描述；average hard attention 与特定 arithmetic-circuit 家族的双向模拟界定其表示能力，须保留替代 FFN 等假设。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：average-attention arithmetic circuits 是受限函数类/构造性理论，不证明标准 Transformer 的实际 attention state 或训练机制。

### [Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization](https://arxiv.org/html/2605.04700v1)

- **Method**（§3.3；§4–5）：white-box audio梯度按token receptive field聚合并在优化过程中稀疏选择；模型兼容prefix与EOS项分别控制开始和继续，非dense结束后简单剪枝。
- **Key evaluation**（§6.1–6.4）：三ALM；AdvBench-50两voice共100音频及补充集，对照dense/Post-hoc prune并扫稀疏度和停机阈值；prefix拒绝字指标与LLM有害判定不同。
- **Direct limitation**（§3.3；§6.3；Appendices D/E）：需要参数/音频梯度，稀疏可增加迭代，极稀疏样本可能hit预算；条件下降/前缀概率不证明必然有害完成或黑盒transfer。
- **采用边界**：音频 token 对齐梯度高度非均匀，使少数 waveform 区域足以承载 jailbreak 优化，也暴露多模态安全评测的稀疏攻击面
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch72 已把 image/audio encoder、跨模态 adversarial robustness 与最终 effect authorization 分开；白盒稀疏 waveform 优化补充攻击样式，但不改变安全 owner 或 fallback。

### [ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC](https://arxiv.org/html/2605.04709v1)

- **Method**（§IV-A/B）：RSSM belief上并行GMM-MPPI保多峰；critic ensemble均值+分歧的UCB归一化调λ，高UCB缩短return传播，训练与planner共享该return。
- **Key evaluation**（§V-A/B）：14DMC视觉任务消融GMM/horizon/λ；喷砂零样本sim2real每法5次，实际排序由模拟TD-MPC2优势反转。
- **Direct limitation**（§IV-B; §VI）：UCB含价值不等纯误差置信界，缩horizon是启发式；稠密reward/连续控制、额外规划算力和小hardware样本，不保证任意遮挡部署安全。
- **采用边界**：visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MULTIMODAL-WORLD-MODELS` 正文中的 `SF-ELVIS-ENSEMBLE-CALIBRATED-LATENT-IMAGINATION-FOR-LONG-HORIZON-VISUAL-MPC` 已承载“visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Budget-aware Auto Optimizer Configurator](https://arxiv.org/html/2605.04711v1)

- **Method**（§3.1–§3.3）：warmup稀疏block梯度风险proxy，MILP在外给optimizer-state memory与update-time预算下选机制/精度；不是自动找全局最佳预算。
- **Key evaluation**（§4.1–§4.4）：ViT/GPT2/T5/UNet/Llama1B/3B，固定预算和sweep，StateMem/PeakMem/wallclock分列，部分三seed、longrun单结果。
- **Direct limitation**（§3.1/3.3; §5）：StateMem不含weights/mastercopies/activation，时间为平均update ratio proxy；线性风险忽略block耦合，online迁移与ZeRO/FSDP仍需验证。
- **采用边界**：optimizer state 可依据各 block 的 gradient stream 风险，在统一 memory/time budget 下做配置分配，而不是全模型固定 recipe
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-PRETRAINING` 正文中的 `SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR` 已承载“optimizer state 可依据各 block 的 gradient stream 风险，在统一 memory/time budget 下做配置分配，而不是全模型固定 recipe”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning](https://arxiv.org/html/2605.04712v1)

- **Method**（§4.1–§4.4）：用eNTK有效秩诊断plasticity；block-diagonal GN/Kronecker proxy下，对actor最后expert加weighted feature Gram各向异性惩罚。
- **Key evaluation**（§5.1–§5.2; AppendixJ.13）：Humanoid5task/MetaWorldCW10、独立RL/连续CRL五seed，相同PPO；固定新任务state batch测eNTK，成功率与effective rank均有对照。
- **Direct limitation**（Theorem4.7 proof AppendixF.7; AppendixJ.13）：正文Thm4.7写实际rank增，但证明只推出proxy lower bound增，不能从下界提高推出真实量单调；单checkpoint相关性不证明所有训练满足近似。只采用经验保plasticity与受限surrogate，不采用无条件定理。
- **采用边界**：增加专家不保证持续 RL 可塑性；expert feature 的谱 proxy 与 Parseval penalty 针对 spectral plasticity loss，改变 MoE 正则选择。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch21 已把 router、expert capacity、placement、communication 与 overflow fallback 联合建模；本材料的窄命题“增加专家不保证持续 RL 可塑性；expert feature 的谱 proxy 与 Parseval penalty 针对 spectral plasticity loss，改变 MoE 正则选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Every Step Counts: Step-Level Credit Assignment for Tool-Integrated Text-to-SQL](https://arxiv.org/html/2605.04719v1)

- **Method**（§3.2–§3.4）：syntax/duplicate hard gate×SQL结果cell-recall soft signal；outcome反向折扣、process逆向平滑，group所有validsteps归一化，反馈tokens不反传。
- **Key evaluation**（§4; AppendixA.7）：BIRD/Spider及三变体、Qwen4B/8B/30B-A3B/Verl group8，多数GRPO/DAPO等对照获益；AIME移除SQLsoft/smoothing仅弱约束+重outcome。
- **Direct limitation**（Limitation; AppendixA.7）：cell recall依赖中间结果超集启发式，不等因果信息增益或逐步真值；非SQL迁移改了奖励，不能说同一过程验证器通用有效。
- **采用边界**：tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT-` 已承载“tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols](https://arxiv.org/html/2605.04727v1)

- **Method**（§3–§4）：纠正Code-DKT softmax沿time归一化看未来→沿ASTpath；按ServerTimestamp恢复序列，assignment validationfold调参后冻结。
- **Key evaluation**（§5–§6）：CodeWorkout69627交互/413学生/5作业，复现旧优势后纠正部分AUC下降，baseline公平调参改变架构排序。
- **Direct limitation**（§7）：单dataset/有限模型；复核显示评价泄漏和调参敏感，不推出code representation普遍无益，也不自动证明所有PKT比较失效。
- **采用边界**：attention-enhanced 模型优势可能来自序列时间泄漏和设置差异；时间排序/固定跨折超参后差距缩小，改变 sequential learner 比较的有效性条件。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“attention-enhanced 模型优势可能来自序列时间泄漏和设置差异；时间排序/固定跨折超参后差距缩小，改变 sequential learner 比较的有效性条件。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization](https://arxiv.org/html/2605.04738v1)

- **Method**（§4–§5）：用校准Hessian低特征值tail-energy子空间构造加性weight修正，固定softmax权重的regularized least-squares压制outlier，再接GPTQ等；近零曲率不是严格全局loss-invariance。
- **Key evaluation**（§6.1–6.3 / Appendices D–F）：Llama7B–70B及123B/405B instruction模型，PPL/QA/MMLU；GPTQ128×2048校准，2bit†另加coordinate descent。A100量化24对22分钟；解码速度来自低bitkernel，不是修正单独加速。
- **Direct limitation**（§4 Taylor 展开、§5 tail-energy 与 §6.3 / Appendix D（直接边界））：Hessian仅局部近似且所取eigenvalues非零；FP16 PPL也5.47→5.52，不能写严格保性能。null空间稳定性只在已测校准分布/大小成立，未证明任意shift。
- **采用边界**：激活/权重 outlier 不必总靠在线 rotation/scaling；Hessian 稳定零空间的 additive suppression 可离线吸收，改变低比特量化的执行负担。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“激活/权重 outlier 不必总靠在线 rotation/scaling；Hessian 稳定零空间的 additive suppression 可离线吸收，改变低比特量化的执行负担。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Knowledge-Free Correlated Agreement for Incentivizing Federated Learning](https://arxiv.org/html/2605.04747v1)

- **Method**（§2 assumptions; §3 Definitions/Propositions）：同任务相关agreement减跨任务基线的peer reward，categorical-world Δ对角正/非对角负免估计符号；同label permutation仍等价。
- **Key evaluation**（§4.2/4.4; AppendixA.12）：MNIST10clients与四域federated adapter10round、1bit update检查符号结构/攻击reward；是激励排序而非下游效用Shapley等价。
- **Direct limitation**（§3.2; AppendixA.7/A.9）：riskneutral/独立同先验任务/条件符号是前提，少于50%恶意只限binary uniform symmetric噪声；任意nonIID/共享置换或信号变换不自动满足，blockchain仅草案。
- **采用边界**：FL 客户贡献奖励通常依赖公开 test/标签；categorical reports 与 honest majority 下的 KFCA 修复 label-flipping 激励，提供不同信任假设。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：federated-learning incentive 的 correlated-agreement 结论依赖其参与者与信号假设，未改变 LLM distributed runtime 的更新语义。

### [AxMoE: Characterizing the Impact of Approximate Multipliers on Mixture-of-Experts DNN Architectures](https://arxiv.org/html/2605.04754v1)

- **Method**（§III-A–D）：CNN/ViT的dense/hard/soft/cluster拓扑与8bit近似乘法LUT仿真交叉，router保持exact且retrain冻结；按effective MAC和库中乘法器功耗归一核算，不能把每op节省等同整个MoE省电。
- **Key evaluation**（§IV-A / §V-B–D）：CIFAR100/ResNet,VGG及TinyImageNet/ViT-Small，5epoch approximate-aware retraining。CNN与ViT拓扑抗误差顺序不同；soft/cluster额外MAC可吞掉算术节省。
- **Direct limitation**（§III-C / §IV-A / §V（直接范围））：是GPU上的LUT误差仿真与MAC功耗模型，不是测得GPU/部署能耗；未测LLM或expert通信。§V-C/V-D对ViT normalized power有不一致值，不引用其精确Pareto/省电百分比。
- **采用边界**：近似乘法器稳健性不能从 CNN 推到 ViT 或 dense 推到 MoE；架构与重训条件下的排序反转改变硬件近似的质量验收。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback；本材料的窄命题“近似乘法器稳健性不能从 CNN 推到 ViT 或 dense 推到 MoE；架构与重训条件下的排序反转改变硬件近似的质量验收。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study](https://arxiv.org/html/2605.04763v1)

- **Method**（§4.1–4.5）：把function/declaration/sliding-window/cAST与retriever、generator、chunk size、context预算交叉控制；从repo重新分块检索而非复用gold片段，评价end-to-end补全EM和token成本。
- **Key evaluation**（§5.1–5.4 / §6.1）：主RepoEval3200与Python CrossCodeEval1937、另Java复核；6–9B，top10 greedy。Function在所测配置落后且会遗漏module内容，Java最优次序变化。
- **Direct limitation**（§7 External/Internal/Construct validity）：top-k固定10使function部分预算未用尽，未验证更大k/模型；单run、潜在训练污染，EM不是功能正确性；未直接测retrieval precision。不能概括所有代码RAG都应弃function chunk。
- **采用边界**：语法函数边界并非默认最佳 code chunk；864 受控设置中 function chunking 不占 Pareto 前沿，改变 chunking 与 context budget 的联合选择。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch76 已把 query、chunk、retrieval candidate、sufficient evidence 与 evaluator 分开；本材料的窄命题“语法函数边界并非默认最佳 code chunk；864 受控设置中 function chunking 不占 Pareto 前沿，改变 chunking 与 context budget 的联合选择。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Elicitation Matters: How Prompts and Query Protocols Shape LLM Surrogates under Sparse Observations](https://arxiv.org/html/2605.04764v1)

- **Method**（§2.2–§2.3）：固定稀疏观测改prompt、pointwise独立或joint自回归查询，定义protocol-conditioned predictive law，effective prior仅行为解释。
- **Key evaluation**（§3–§6）：受控函数50温度1样本、顺序/冲突观测，3个BO后果实验各10seed；modifiedBranin逆转prior收益，HPO最终SMAC3更好。
- **Direct limitation**（§6; §8）：token uncertainty作acquisition启发式非目标空间校准std；无CoT多为noise-free，电池例LLM获得额外领域信息，不是跨模型或普适优化器胜出。
- **采用边界**：LLM surrogate 的 prompt/逐点或联合查询不是格式细节；不确定性对齐与 downstream regret 受协议改变，要求把 elicitation 计入 surrogate 定义。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“LLM surrogate 的 prompt/逐点或联合查询不是格式细节；不确定性对齐与 downstream regret 受协议改变，要求把 elicitation 计入 surrogate 定义。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use](https://arxiv.org/html/2605.04785v1)

- **Method**（§3–§4）：trusted in-process pretool拦截：文本去混淆→规则最大风险→可选judge/chain，内部异常review；无rule命中默认可allow，cache仅在相同/append条件复用。
- **Key evaluation**（§5–§6）：内部300/另630场景，630包含按miss补规则后的96.7%，不属zeroshot；stateless套件SessionTracker零贡献，hybrid不严格优于rules。
- **Direct limitation**（§5.2; §6.7; §7.1）：单作者标签与postpatch评测不等独立盲验；regex不能追runtime数据流/完整shell语义，runtime可绕过inprocess拦截；未证明chain安全或缓存摘要完整保风险上下文。
- **采用边界**：tool calls require runtime interception and effect-side safety checks
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch78 已把 schema/argument proposal、deterministic validation、authorization 与 effect receipt 分层；本材料的窄命题“tool calls require runtime interception and effect-side safety checks”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/html/2605.04808v1)

- **Method**（§3.1–3.2；§4.2）：DTap 将风险 policy、模拟工具环境、victim agent 与可验证 effect judge 分开；DTap-Red 从 policy 推导恶意目标并组合 prompt/tool/skill/environment 注入。
- **Key evaluation**（§6.1–6.3；Appendix A–P）：14 个领域、50 余模拟环境，2,503 个 direct/indirect tasks，覆盖四类 agent framework 与披露 backbone；matched attack generator 的高 ASR 是受控上界。
- **Direct limitation**（§3.1；§6.1；§7）：环境与 judge 均为作者模拟/实现；100% ASR 来自 GPT-5.1+OpenAI Agents SDK 的匹配生成设置，不是生产攻击率，也不证明所有真实工具副作用被复现。
- **采用边界**：Agent red-team 必须绑定可重放的环境状态转换、注入/威胁身份与 effect-side judge，不能把静态 prompt 成功率外推到真实 workflow
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已要求冻结环境 revision、真实 transition/effect receipt，并把模拟器与 judge 限定为测量工具；本材料补充实例但不改变该命题。

### [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/html/2605.04811v1)

- **Method**（§3.2–3.3）：builder→summarizer→responder 展开 G×J×K rollout，按子树末端奖励 Monte Carlo 平均分配各 agent credit，builder 加长度惩罚；抽路径作 policy 更新，部署不展开树。
- **Key evaluation**（§4.1–4.6）：PersonaMem 三历史长度与 Qwen/Llama 两系，再测 LongMemEval/LOCOMO；至少三次种子运行，奖励/branch 消融区分 tree credit 与终端统一奖励。
- **Direct limitation**（Appendix D；§4.5–4.6）：分支数提高 credit 精度也提高 rollout/训练/GPU 成本；小分支噪声大、大分支收益饱和。系统成本结论限相同 agent 架构比较，不提供 memory 写权限或 lineage。
- **采用边界**：multi-agent memory requires tree-structured credit assignment over shared and delegated state changes
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-MEMORY` 正文中的 `SF-TREE-BASED-CREDIT-ASSIGNMENT-FOR-MULTI-AGENT-MEMORY-SYSTEM` 已承载“multi-agent memory requires tree-structured credit assignment over shared and delegated state changes”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Concurrence of Symmetry Breaking and Nonlocality Phase Transitions in Diffusion Models](https://arxiv.org/html/2605.04830v1)

- **Method**（§1.1；§3.1–3.5）：用 conditional/unconditional score gap 诊断 symmetry breaking，用 global/截断局部 score gap 诊断 nonlocality，再以 forward-backward 与时间窗切换检验最终样本影响。
- **Key evaluation**（§3；Appendix C）：ImageNet DiT-XL 与 SD3-medium，在披露 sampler/noise levels 下比较 instantaneous 与 integrated probes；SD3 window 实验因成本仅 62 个样本。
- **Direct limitation**（Appendix D）：只覆盖两个 DiT 系统；截断 attention 只是近似 local denoiser；并发 critical windows 是经验观察，不是普适定理。
- **采用边界**：局部 denoising 可用性与语义分岔常被分开分析；DiT 中两个 critical time 接近提供何时需要 conditioning/global compute 的诊断。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MULTIMODAL-GENERATIVE-PARADIGMS` 正文中的 `SF-2026-ARXIV-2605-04830` 已承载“局部 denoising 可用性与语义分岔常被分开分析；DiT 中两个 critical time 接近提供何时需要 conditioning/global compute 的诊断。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Agentic Repository Mining: A Multi-Task Evaluation](https://arxiv.org/html/2605.04845v1)

- **Method**（§3–§4）：比较能用 bash 动态探索 repository 的 agent 与一次性接收预工程 context 的简单 LLM，覆盖 commit/review/line/repository 四类 classification 与八种配置。
- **Key evaluation**（§5）：4,943 个 classifications；agent 平均约 5.7–10.5 steps、6.1–14.1 commands、21–29s，simple 路径约 1.5–6s。优势按任务变化，主要体现在避免 context overflow，并非全面准确率领先。
- **Direct limitation**（§6 Threats to Validity）：标签质量和 setup 可能偏向某一路径；public/smaller repository filter、有限 features/baselines、模型训练污染与 ground-truth ambiguity 未完全排除。
- **采用边界**：Repository context 的选择是条件分支：预工程 context 在规模可控时更快；自主探索在 artifact 超窗或 taxonomy 不完整时更稳健，但增加工具步骤、错误和时延。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch75 已明确小仓库/完整工作集可直接拼接，大仓库应按 task 与 repository revision 定点检索，并把 retrieval confidence 与事实充分性分开；本结果没有改变该条件分支。

### [Uncertainty-Aware Exploratory Direct Preference Optimization for Multimodal Large Language Models](https://arxiv.org/html/2605.04874v1)

- **Method**（§4.1–4.3）：清晰/加噪图像的token logit对比构成视觉敏感性/uncertainty proxy；preferred弱视觉高uncertainty增探索，dispreferred视觉敏感减罚，token权重停止梯度。
- **Key evaluation**（§6.1–6.3）：LLaVA7/13B与Qwen2.5-VL3B，RLHF-V/RLAIF-V，LoRA两epochs、至多4A100；preferred/dispreferred与强度阈值消融。
- **Direct limitation**（§6.2–6.3 的直接反证）：AMBER-d F1改善但Acc可下降，数据覆盖改变trade-off；跨方法数据量不同，不能把总表全当同预算机制证明。proxy不是独立校准正确率。
- **采用边界**：多模态 DPO 可用 token-level epistemic uncertainty 重分配偏好学习压力，但该信号仍由训练中模型自估并可能失准
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch34 已把 token/pair geometry 视为 update sensor，并要求 preference truth、chosen likelihood、KL 与 optimizer commit 分权；模型自估视觉 uncertainty 未经独立校准，不足以形成新的 DPO 长期机制。

### [Self-Attention as Transport: Limits of Symmetric Spectral Diagnostics](https://arxiv.org/html/2605.04893v1)

- **Method**（§4 Theorem4/Proposition6）：singular-value或对称部分谱统计对M与M转置不变，因此不能辨方向；Frobenius反对称残差控制Lipschitz统计的最大转置差。
- **Key evaluation**（§6–7）：长度分层LC-AUROC、三数据集/15模型组合与Pythia尺度组，bootstrap；所加G在大多数配置接近chance，统计关联与结构定理分开。
- **Direct limitation**（§8.2；对§4公式的作者整改核算）：需要attention tensors；不测value geometry，zero-shot只指特征计算，决策仍需50–100标注校准。G范数本身转置不变，不能由加G宣称恢复实际流向；仅保留严格谱不可辨识结论。
- **采用边界**：attention 谱诊断存在 orientation-blind 的可证明不可辨识边界，因此 hallucination sensor 必须区分 transport capacity 与 flow orientation
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已规定 attention/probe 等内部量只能作为需校准的 sensor，不能取得 truth authority；orientation-blind 的谱不可辨识定理强化这一边界，但不改变 evaluation contract。

### [SynConfRoute: Syntax-Aware Routing for Efficient Code Completion with Small CodeLLMs](https://arxiv.org/html/2605.04894v1)

- **Method**（§3–§4）：SynConfRoute 以首三个 token 的平均 log-probability组合 syntax validation，决定保留本地 3B completion 或升级至更大 self-hosted model；syntax 只证结构有效，不证语义正确。
- **Key evaluation**（§5–§6）：29 个 0.5B–480B code models、HumanEval-Infilling 与 SAFIM 的 Python/Java/C++；小模型使用单 80GB accelerator 上 Q4_K_M/Ollama，大模型使用 8×80GB/vLLM，greedy、50-token。作者报告相对 confidence-only 的受限提升。
- **Direct limitation**（§7）：短 FIM benchmark 不是真实 IDE；以 Qwen routing 为主，跨文件 context、用户采纳与 production concurrency/SLO 未测。46% confident-wrong 是 syntax-broken，剩余语义错误形成 detector ceiling。
- **采用边界**：逐请求 model routing 不能只读生成置信度；应把模型 sensor 与可验证的 domain signal 组合，再在 local accept、large-model escalation 与 privacy/cost 之间决策。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch56 已规定 confidence 只是 proposal，router 应从可验证局部 observation 更新 belief，并由 SLO/风险 controller 决定 accept/escalate；syntax validity 是该原则的代码域实例，不新增 owner。

### [Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall](https://arxiv.org/html/2605.04897v1)

- **Method**（§2–3）：六层 retrieval-centered pipeline 保留 verbatim events，再在 ingestion、post-ingestion 与 query-time 分阶段检索；SQLite/CPU 是实现选择而非 memory 定义。
- **Key evaluation**（§4；Tables 1–3）：LoCoMo、LongMemEval、BEAM-1M 使用统一 harness、top-k window 与 gpt-4o-mini 三次多数 judge；LoCoMo 另做 56 配置检索消融。
- **Direct limitation**（Limitations）：所有 benchmark 都关闭 encoding gate；未验证数周/月真实历史；semantic-match judge 比 strict match 宽松，绝对分数不可直接跨论文比较。
- **采用边界**：durable storage is not usable memory without retrieval, admission and update ownership
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch77 已把 immutable episode、derived view、retriever 与 truth authority 分离，并明确保存不等于可召回；本架构是受限实现案例。

### [On the (In-)Security of the Shuffling Defense in the Transformer Secure Inference](https://arxiv.org/html/2605.04901v1)

- **Method**（§4）：攻击者跨查询对齐 shuffled intermediate activations，消去 permutation ambiguity 后逐层恢复暴露路径上的权重。
- **Key evaluation**（§5.1–5.3）：在 Pythia-70M/GPT-2 及论文两种暴露设置上报告表示对齐与权重恢复误差；private-matmul 变体的 Wqk 恢复仍未解决。
- **Direct limitation**（Limitations）：只在小模型验证，规模增大时恢复精度下降；不覆盖所有 secure-inference 协议、side channel 或生产攻击预算。
- **采用边界**：反证 activation shuffling 足以保护模型机密性：恶意客户端可利用暴露的中间表示恢复服务器权重
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-2026-ARXIV-2605-04901` 已承载“反证 activation shuffling 足以保护模型机密性：恶意客户端可利用暴露的中间表示恢复服务器权重”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](https://arxiv.org/html/2605.04913v1)

- **Method**（§3–4）：在 midpoint 截断 task gradient：后半段学习任务，前半段以 bottleneck 重建 stop-gradient 输入 embedding；先更新前部再重算并 detach boundary activation。
- **Key evaluation**（§5–6）：在披露的 4B–8B SFT/GRPO 设置中比较质量、显存和 policy-update 时间，并以 32B 做可扩展性检查；k=2/k=4 是有限切分消融。
- **Direct limitation**（§6；Appendix）：feature reconstruction 只约束接口兼容，不保证保留全部下游信息；额外 forward、midpoint 选择与跨层协同可能抵消收益。
- **采用边界**：local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN` 已承载“local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Reinforcement Learning for Compositional Generalization with Outcome-Level Optimization](https://arxiv.org/html/2605.04920v1)

- **Method**（§3）：将组合任务的监督从 token imitation 改为 outcome-level GRPO，并比较 binary 与 composite reward，直接检验训练组合到未见组合的迁移。
- **Key evaluation**（§4–5）：四个 compositional benchmark、两个模型，SFT/GRPO 与 reward 变体对照；总体 binary reward 接近 composite，而困难 split 上存在互补差异。
- **Direct limitation**（§6）：证据限四个构造任务和简单 reward family；RL 计算更高，结果不证明 outcome reward 普遍优于过程监督。
- **采用边界**：token-level 模仿可能偏重训练组合；outcome RL 与 binary/composite reward 对照检验组合泛化，改变 SFT/RL 的目标选择边界。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch33 已按 outcome 可验证性、credit horizon 与 execution replay 讨论何时选择 terminal/group reward；该结果未改变现有条件分支。

### [Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation](https://arxiv.org/html/2605.04922v1)

- **Method**（§3.2–§3.4；Appendix C–D）：typed idea graph 保存 claim、assumption、risk、evidence need 与它们的关系；role-local action selection、patch materialization、deterministic merge、realized transition 与 graph-global commit 被拆成不同 runtime object。
- **Key evaluation**（§4；Appendix H）：AI Idea Bench 2025 与 LiveIdeaBench 的 512-group held-out packet、三 seeds 和 controller/frozen-snapshot ablation 支持所测 ideation runtime；顺序更新对照还混有 drop-in controller mismatch。
- **Direct limitation**（§5；Appendix H–I）：结果只评价 proposal quality，不验证科学结论或真实实验；critic 来自 heuristic weak labels，graph schema 固定，benchmark evaluator 和 Qwen3-8B backbone 限制外推。
- **采用边界**：多 Agent 并行修订不能让 role-local 文本直接覆盖共享真值；各角色应在同一 frozen snapshot 上形成 typed patch，固定顺序 materialize 后再由 graph-global commit 判断是否进入最终 artifact。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch81 已写入同轮角色基于 frozen graph snapshot 提案、typed patch 验证、确定性 materialization 与 graph-global commit 的状态链，并保留顺序 barrier 回退。

### [Adaptive Inverted-Index Routing for Granular Mixtures-of-Experts](https://arxiv.org/html/2605.04952v1)

- **Method**（§3.1–3.3; Proposition 1）：AIRMoE 用球面码字余弦量化把 token 路由到倒排 shortlist，再只在 shortlist 内算精确专家分数；每个 optimizer step 刷新全部 shortlist，码字用 EMA/球面聚类而非 STE。保留路由质量依赖量化误差和 shortlist 概率质量条件。
- **Key evaluation**（§5–5.3）：WikiText103、C5、OpenWebText2 上 61M/270M/450M 模型，以单个中间 FFN 的细粒度专家替换比较 PPL/训练 FLOPs；expert-choice 高 overlap 仍出现 78.6% dead experts，不能将 overlap 单独视为路由质量。
- **Direct limitation**（§6; Proposition 1）：主要效率证据为 FLOPs，不是实测端到端时延；索引更新、非规则内存访问和 batch 大小决定实际收益。shortlist 不保证无条件 exact top-k。
- **采用边界**：细粒度 MoE 的全专家打分会抵消稀疏计算收益；VQ shortlist 后做受限精确 router，改变路由精度与执行成本边界。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch21 已把 router、expert capacity、placement、communication 与 overflow fallback 联合建模；本材料的窄命题“细粒度 MoE 的全专家打分会抵消稀疏计算收益；VQ shortlist 后做受限精确 router，改变路由精度与执行成本边界。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [KernelBenchX: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels](https://arxiv.org/html/2605.04956v1)

- **Method**（§3–4）：KernelBenchX 将 kernel 任务按 15 类组织，用两阶段 correctness filter 排除随机碰巧通过，再在相同语义门后测硬件效率与 portability。
- **Key evaluation**（§5–6）：176 个任务、六类 GPU、五种生成/修复方法；区分 compile、correctness、speedup 与跨架构表现，并观察迭代修复提高正确率却可能降低性能。
- **Direct limitation**（§6–7）：这是作者 benchmark 与给定 toolchains/models 的结果；不能把 microbenchmark speedup 外推端到端模型，也不证明测试覆盖等于形式正确。
- **采用边界**：generated GPU kernels need fixed-contract correctness and performance evaluation across architectures
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-2026-ARXIV-2605-04956` 已承载“generated GPU kernels need fixed-contract correctness and performance evaluation across architectures”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](https://arxiv.org/html/2605.04957v1)

- **Method**（§4–5; Theorem 5.1; Appendix B）：SCALE 将预测残差分解为低频条件与高频分量，以高频统计及低频条件产生 gated quantile predictor；覆盖率结论依赖 SGCE 条件交换性，并非弱相关即可推出交换性。
- **Key evaluation**（§6）：METR-LA、PEMS04/07/08，共享预测 backbone，残差按时间 40/40/20 分割，trainable 方法五个种子；比较 coverage、interval width、Winkler，窗口 12、预测 horizon 1 或 96。
- **Direct limitation**（Appendix C; §5 assumptions）：稳健界依赖 score/CDF Lipschitz、低频估计误差以及相对交换性的 TV 偏离，不是任意分布漂移下的无条件有限样本保证。
- **采用边界**：图耦合会破坏普通 conformal 的 exchangeability；条件高频谱分解提供不同校准机制，需把交通图结果限定为图预测而非通用 LLM coverage。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：graph time-series conformal prediction 只重申 non-exchangeability 条件，不提供 LLM evaluation 的新 estimator、release gate 或 truth authority。

### [EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance](https://arxiv.org/html/2605.04960v1)

- **Method**（§V-A–V-C；§VI）：outcome advantage 符号不变而幅度受 entropy gate 调节；frozen-reference log-ratio 经 outcome 符号定向，零方差改 reward threshold；累计 entropy 的相对 progress 桶内归一化再合并。
- **Key evaluation**（§VII-A–G）：Qwen2.5 3B/7B LoRA，8000 数学训练题、五数学测试、1000 steps，固定 seed 42、2048 token 上限；entropy/progress/零方差消融及 wall-clock 对照。
- **Direct limitation**（§VI 定理前提；§VII-A/C）：单训练 seed 与数学/短生成预算限制统计及任务外推；商业模型在同 2048 上限被截断，不把该排名当通用能力优势。progress 是自监督 proxy，并非逐步 truth/verifier。
- **采用边界**：GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-GRPO` 正文中的 `SF-EP-GRPO-ENTROPY-PROGRESS-ALIGNED-GROUP-RELATIVE-POLICY-OPTIMIZATION-WITH` 已承载“GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Skill Neologisms: Towards Skill-based Continual Learning](https://arxiv.org/html/2605.04970v1)

- **Method**（§3–4）：Skill Neologisms 为新技能增加可学习 soft tokens，在冻结既有模型权重时训练新增 token，并用围绕技能的组合数据学习可复用指令；冻结 backbone 不等于所有参数不更新。
- **Key evaluation**（§5）：Qwen 0.5B 的合成数字操作，在已有 LoRA 学习后的模型加入 SHIFT/INV-POL，比较 LoRA/prefix tuning 和独立新 token 的零样本组合；REV 因 OOD 为 0% 被排除，不能把所选技能结果解释为普遍组合能力。
- **Direct limitation**（§6; Appendix C）：合成任务概念验证，依赖技能中心的数据变化，对初始化和 token 长度敏感；训练仍需经全模型反传，成本可能接近微调，不支持一般真实技能的无遗忘结论。
- **采用边界**：独立技能适配常需改权重或堆 context；冻结模型的 soft-vocabulary skill tokens 可单独训练再组合，改变技能更新与组合的参数界面。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“独立技能适配常需改权重或堆 context；冻结模型的 soft-vocabulary skill tokens 可单独训练再组合，改变技能更新与组合的参数界面。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Why Geometric Continuity Emerges in Deep Neural Networks: Residual Connections and Rotational Symmetry Breaking](https://arxiv.org/html/2605.04971v1)

- **Method**（§3–5）：把跨层 representation geometry 分解为 residual 引起的 gradient coherence 与非线性引起的 rotational symmetry breaking；用 rotation-equivariant 非线性构造反例。
- **Key evaluation**（§6；Appendix）：toy MLP 多 seed、小型 34M Transformer 单 seed与若干预训练模型表征统计；前者检验机制，后者只观察几何模式。
- **Direct limitation**（§6–7）：小模型和受控任务不能证明大模型训练的因果动力学；预训练快照上的相关几何不等于训练期机制。
- **采用边界**：跨层几何连续性不能仅归于非线性；保旋转非线性反例分离 residual 梯度相干与对称破缺，改变 activation/norm 角色解释。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MODEL-TRANSFORMER-LAYER` 正文中的 `SF-2026-ARXIV-2605-04971` 已承载“跨层几何连续性不能仅归于非线性；保旋转非线性反例分离 residual 梯度相干与对称破缺，改变 activation/norm 角色解释。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Why Expert Alignment Is Hard: Evidence from Subjective Evaluation](https://arxiv.org/html/2605.04972v1)

- **Method**（§3）：在同一主观任务中分别改变 expert identity、样本、时间与评价维度，并比较 prompting、fine-tuning 与 weight edit 是否吸收专家判断。
- **Key evaluation**（§4–5）：九名专家、一个任务、一个 base model 和披露对齐方法；criteria/rationale 的加入并未稳定改善所有维度。
- **Direct limitation**（§6）：单任务、九专家、单模型/编辑方法；disagreement 可能来自真实价值差异，不能把少数意见当模型错误或通用 alignment failure。
- **采用边界**：显式专家 criteria 未必能稳定提升对齐；专家/样本身份/评价维度的受限证据挑战只增加 rubric 的策略，需区分主观异质性与模型错误。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66/Ch31 已把 rubric、rater identity、disagreement 与 release authority 分离；该小样本结果只提供受限反例。

### [Conceptors for Semantic Steering](https://arxiv.org/html/2605.04980v1)

- **Method**（§4；§5）：从正/负概念对的 pooled hidden activations 构造 conceptor soft projection matrix；quota 用作无参数 layer-selection sensor，replacement/interpolation 改写 hidden state，AND/OR/NOT 在子空间几何上组合。
- **Key evaluation**（§5.1–§5.4；Appendix A.2–A.4；Appendix B）：Gemma-2-2B/9B、Qwen2.5-3B，三个英文语义维度、五轴设计空间、500 prompts 与两组 Boolean 任务；quota 与 probe separability 在多数设置相关，interpolation 的退化输出少于更激进 replacement/additive 路径。
- **Direct limitation**（§7）：只测三种较小 instruction model、三个英文概念、单层 intervention、有限 contrastive pairs 与自动 classifier；Boolean composition 依赖子空间 overlap，不证明行为正确或生产安全。
- **采用边界**：inference-time semantic steering 不必把概念压成单一方向；由 bipolar activations 估计的 soft projection subspace 可保留多维结构，并通过 Boolean composition 形成更丰富但仍需校准的控制 artifact。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch20 已把 hidden-state control vector 绑定 checkpoint、layer、window 与阈值，但默认仍是单方向 artifact；缺少多维 soft-projection、layer quota sensor 和组合操作的替代分支。

### [Self-Induced Outcome Potential: Turn-Level Credit Assignment for Agents without Verifiers](https://arxiv.org/html/2605.04984v1)

- **Method**（§3）：从每个 turn state 采样 future answers，按语义聚类形成 outcome-potential distribution，以 reliability-weighted cluster mass 的相邻差分生成 turn reward。
- **Key evaluation**（§4）：Qwen3-4B/8B 在七个 search-QA benchmark 上比较 outcome、turn credit 与组件消融；训练不使用 gold verifier，但可靠性/聚类器仍是代理。
- **Direct limitation**（§5–6）：只覆盖有可聚类短答案的 search QA；开放代码/长 artifact 没有稳定 outcome identity，self-induced reliability 可能共享模型偏差。
- **采用边界**：turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-RLHF` 正文中的 `SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W` 已承载“turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [You Snooze, You Lose: Automatic Safety Alignment Restoration through Neural Weight Translation](https://arxiv.org/html/2605.04992v1)

- **Method**（§3）：NeWTral 在 paired unsafe/safe adapters 上训练 layer-wise/MoE weight translator，将新 unsafe adapter 映射到较安全的 aligned adapter。
- **Key evaluation**（§4–5）：八个技术域、最高 72B 模型，联合比较 safety 与 utility；zero-shot 指新 adapter 的部署映射，不代表 translator 从未使用安全数据。
- **Direct limitation**（§6）：不能消除全部 unsafe output；结构新颖域的泛化未证，训练依赖 paired adapters 与 safety data，repair 还可能损伤能力。
- **采用边界**：safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-SECURITY` 正文中的 `SF-YOU-SNOOZE-YOU-LOSE-AUTOMATIC-SAFETY-ALIGNMENT-RESTORATION-THROUGH-NEURA` 已承载“safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Adaptivity Under Realizability Constraints: Comparing In-Context and Agentic Learning](https://arxiv.org/html/2605.04995v1)

- **Method**（§2–5）：在 ReLU realizability 约束下构造四类任务，分别展示 adaptivity 优势保持、消失、出现或反转，分离查询策略与表示可实现性。
- **Key evaluation**（理论构造与证明）：结论来自四个显式函数族/查询模型的近似界，不是 agent benchmark 或生产 tool-use 实验。
- **Direct limitation**（§6）：构造只说明 adaptivity 与 realizability 没有单调关系；不提供开放环境中的成本、噪声、工具副作用或模型选择结论。
- **采用边界**：自适应查询优势不必在实现约束后保留；ReLU realizability 下四类构造分离 adaptive querying 与表示能力，改变 agent 学习理论解释。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch79 已把 adaptive search 设为有观测价值、预算与 verifier 条件的分支，并保留 static plan；理论构造强化边界但不改变 owner 结论。

### [Misaligned by Reward: Socially Undesirable Preferences in LLMs](https://arxiv.org/html/2605.05003v1)

- **Method**（§3）：把 reward model 在 bias、safety、morality 与 ethical reasoning 上的 pairwise preference 分开测，比较 criteria 与 context faithfulness 的冲突。
- **Key evaluation**（§4–5）：五个公开 reward models 与两个 instruct proxies；部分数据是定向构造诊断，不是客观 correctness gold，也不测下游 policy。
- **Direct limitation**（Limitations）：英语与来源规范有限，社会价值标签依赖语境/人群；reward preference 不能直接推出部署行为或内部机制。
- **采用边界**：reward model 的通用指令偏好分数不能代替社会域 preference audit；bias avoidance 与 context faithfulness 还可能相互冲突
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66/Ch31 已要求 rubric/rater/domain 版本化并禁止 scalar reward 取得 truth authority；无新增长期机制。

### [Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/html/2605.05007v1)

- **Method**（§3–4）：单一 causal orchestrator 联合决定是否分解、分解深度及 worker/model+primitive 路由；SFT 后用 verifier-gated Agentic-GRPO 学习选择性委派。
- **Key evaluation**（§5）：22 个 baseline、13 个 benchmark，联合报告准确率与成本；worker catalog、API 能力与价格是实验快照。
- **Direct limitation**（§6）：单 orchestrator 与固定 worker 集不证明任意多 Agent 拓扑收益；API 漂移、共享工具状态、权限和副作用未由 benchmark 解决。
- **采用边界**：multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-MULTI-AGENT` 正文中的 `SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION` 已承载“multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Learned Neighbor Trust for Collaborative Deployment in Model-Agnostic Decentralized Learning](https://arxiv.org/html/2605.05009v1)

- **Method**（§4）：LNTrust 先本地预训练，再以有标签验证集探测邻居的逐类能力，用六类关系特征产生信任权重；验证集 ensemble 优于自身及置信阈值共同 gate 邻居 logit 蒸馏，部署时仍查询含自身的邻居 ensemble。
- **Key evaluation**（§6; Appendix G）：CIFAR10/100、EuroSAT，50 节点、三种子和异构架构，固定类别 logit 空间与缓存 backbone；需区分蒸馏后 Self 和依赖邻居推理的 Test 指标。
- **Direct limitation**（Appendix G; theoretical assumptions）：静态无向同步图、诚实邻居、有标签验证数据；部署额外邻居查询带来延迟，未建立 Byzantine/隐私保证。理论是固定预测器局部估计与漂移分析，不是端到端自身模型必然提升。
- **采用边界**：异构分散模型不能默认互相可信；同一验证 trust gate 同时控制辅助蒸馏与部署 ensemble，改变训练和推理共享信任信号的设计。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：decentralized model collaboration 的 neighbor-trust 证据限其网络/reputation 设定，未改变集中式或并行 LLM training 的状态所有权。

### [Position: Embodied AI Requires a Privacy-Utility Trade-off](https://arxiv.org/html/2605.05017v1)

- **Method**（§3；§4.1）：SPINE 以 stage/function/control/budget 的 tuple 表达隐私标签，在 instruction→perception→planning→interaction 之间传播 policy；导航案例用区域敏感度触发 pixelation、camera depression、edge/cloud placement 或禁止进入。
- **Key evaluation**（§4.2–§4.3）：Habitat/R2R-CE 的 pixelation sensitivity 与小型 AGV 路径演示只作为受控 probe：SR/SPL 和路线会随遮蔽/区域 policy 改变；作者明确 pixelation K 不是实际 privacy measure。
- **Direct limitation**（§5；§7–§8）：position paper 与概念性案例不提供统一 threat model、形式保证或生产评测；state-based/视觉导航不能覆盖 latent、gradient、memory、旁观者与多机器人泄漏，很多机制仍是 future work。
- **采用边界**：Embodied privacy 不是 perception 阶段的单点遮蔽，而是从 instruction、sensing、planning 到 interaction 的 lifecycle control signal；privacy level 改变会沿闭环传播为 utility 与可达 action 的变化。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch72 已把 privacy 从静态存储扩展到端到端 observable data flow，并按 embodied supply/perception/world-state/planning/action 等 trust boundary 分责；SPINE 提供生命周期实例，但不改变现有 owner、threat-model 或 fail-closed contract。

### [CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels](https://arxiv.org/html/2605.05023v1)

- **Method**（§3.1–3.5）：CUDA lift 到可执行 CuIR，依据目标 PyTorch reference 变换 IR，再按 IR 差异局部 patch 回 source CUDA；IR 保留 tile、依赖和同步，并执行检查。
- **Key evaluation**（§4.1–4.4）：A100/H100，FlashAttention v2.8.0 源，八类 attention/组合；1–8k 序列且 batch 总 16k tokens，LLM 方法 best-of-10；96-case 消融对比直接改写/ReAct/CuIR。
- **Direct limitation**（Limitations；§4.1）：依赖高质量 expert source kernels，非主流硬件可缺源；主要验证 attention，不证明全 kernel 适用。100% 正确限所测 best-of-k 与数值容差，非任意输入的形式证明。
- **采用边界**：把已有专家 kernel 提升为 executable IR，再由模型提出结构变化并经 lowering/verifier 落回可运行实现
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`INFER-TENSORRT-LLM` 正文中的 `SF-2026-ARXIV-2605-05023` 已承载“把已有专家 kernel 提升为 executable IR，再由模型提出结构变化并经 lowering/verifier 落回可运行实现”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals](https://arxiv.org/html/2605.05025v1)

- **Method**（§4）：用生成答案 token 的各头 attention 相对均匀分布的平均 KL 特征，训练 L1 logistic probe 预测答案正确性；属于需内部 attention 的有监督检测器。
- **Key evaluation**（§5–7）：Llama 3B、Qwen 4B、Mistral 7B，四个 QA/math 数据集，三次数据划分/CV，AUROC；包含 shuffle、长度、head ablation 和 prompt/answer/full sequence 比较，基线只在匹配子集可比。
- **Direct limitation**（§8）：注意力偏离与正确性是相关而非因果真值规则，冗余相关头消融不直接定位因果功能；需要内部访问及分布相关 probe，不支持黑盒或跨模型无校准保证。
- **采用边界**：采样一致性 UQ 有多次 decode 成本；attention 对均匀分布的 KL probe 提供单 pass 替代，需与低成本首 token/语义梯度 sensor 同协议比较。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“采样一致性 UQ 有多次 decode 成本；attention 对均匀分布的 KL probe 提供单 pass 替代，需与低成本首 token/语义梯度 sensor 同协议比较。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models](https://arxiv.org/html/2605.05026v1)

- **Method**（§3–4）：以生成轨迹的 local intrinsic dimension 作为结构不稳定 proxy，并用 intrinsic-quality correction 抑制 LID 虚高。
- **Key evaluation**（§5）：toy/image datasets、作者 diffusion models 与人评比较 structural hallucination；结果绑定所选 estimator、采样与视觉标签。
- **Direct limitation**（§6）：结构幻觉定义与人评主观，LID 是相关诊断而非因果或事实 verifier；质量、diversity 与 correction 的权衡尚未闭合。
- **采用边界**：扩散结构幻觉不仅可用 mode interpolation 解释；局部内在维数与 IQ 抑制提供另一诊断/纠正分支，需区分机制证据和下游医学类比。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：受限 detector/correction 案例未改变 Ch24 的 factorization、state 与 commit 主线；保留日报证据，不新增正文。

### [The Predictive-Causal Gap: An Impossibility Theorem and Large-Scale Neural Evidence](https://arxiv.org/html/2605.05029v1)

- **Method**（Theorem1/Corollary2；S1/S7）：线性高斯单位范数encoder的latent self-prediction MSE可偏离指定system轴；扩大模型类只能推出其最小risk不高于特定NZ风险，不能据此排除所有非线性因果表示。
- **Key evaluation**（正文 Linear sweep/Neural network evidence；S8–S9）：报告线性grid、MLP和高维扩展及Duffing-GRU，但列出的7×7×10×5网格与539 configurations缺解释；理论例子的43.7°与环境分量占优表述冲突。
- **Direct limitation**（Theorem1及其紧邻构造；S8.1）：争议未解决：需解释encoder尺度/约束、从排除特定NZ到排除整个因果类的推论、角度与grid计数。当前不据此建立普适scaling/自监督不可能命题，保持争议状态而非虚构直接 limitation 章节。
- **采用边界**：最小预测误差可以系统性偏好环境慢变量而不是目标系统的因果状态，world-model objective 必须显式声明 system/environment boundary
- **审阅/Books**：exact-v1 Source Review 完成；争议：定理从特定预测模型外推到因果类、角度叙述与实验 grid 计数彼此不一致；需作者勘误或可复算证明/实验包后才重开。

### [Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization](https://arxiv.org/html/2605.05040v1)

- **Method**（§2.1–2.2; Algorithm 1）：PBSD 把 teacher-referenced KL 与 latent reward 相加，以 privileged-context teacher 采样作为偏好正例、当前学生采样作为负例，用 teacher log-ratio 的 DPO logistic margin 优化；teacher 固定于初始 checkpoint，不是更大外部 oracle。
- **Key evaluation**（§4.1–4.3; Tables 2/5）：Qwen3 1.7B/4B/8B，数学 Avg@12 和工具 top-1；LoRA、8 H100、500 steps 内选择 peak checkpoint，对比 SFT/GRPO/DAPO/OPSD/SDFT/SRPO，并比较每 5 step 更新或固定 teacher。
- **Direct limitation**（Appendix A; §2.2 assumption）：正负偏好依赖额外上下文确实让 teacher 更好；弱 privileged context 会减小收益，teacher 生成并非经真值逐项验证。peak checkpoint/fixed task budget 不是部署鲁棒性或无条件超越 teacher 的证明。
- **采用边界**：self-distillation 不必只匹配自身原分布；reward 重加权 teacher 给出目标与最优性条件，改变何时应选择外部 teacher 或 self-teacher。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开；本材料的窄命题“self-distillation 不必只匹配自身原分布；reward 重加权 teacher 给出目标与最优性条件，改变何时应选择外部 teacher 或 self-teacher。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise](https://arxiv.org/html/2605.05045v1)

- **Method**（§3.1–3.2; §4.1–4.2）：对图像施加 90/270 度旋转或四类质量扰动，比较附加提示、方向校正和图像去噪对 VLM relation accuracy 的影响；不用感知恢复指标代替关系正确性。
- **Key evaluation**（§3 Tables 1/2; §4 Tables 3/4）：五个开源与三个闭源 VLM，R-Bench/Reefknot/MMRel；详细提示/去噪机制主要用 GPT-5.1，方向检测器在随机 90/270 旋转下测试；高 LPIPS/PSNR/SSIM 质量不稳定映射推理提升。
- **Direct limitation**（§4.2; §5 Conclusion）：去噪收益依赖数据集和损坏，MMRel 恢复后仍降 9–12 pp；只覆盖离散旋转与选定噪声/模型，不证明一般几何鲁棒性。感知关系题沿用原答案必须区分旋转后语义标签是否保持。
- **采用边界**：视觉识别对旋转/噪声稳健不代表关系判断稳健；关系幻觉的分离对照及部分有效预处理改变 VLM robustness 评价。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch23 已把 modality encoder、shared representation、relation binding、provenance 与 evaluation slice 分开；本材料的窄命题“视觉识别对旋转/噪声稳健不代表关系判断稳健；关系幻觉的分离对照及部分有效预处理改变 VLM robustness 评价。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Piper: Efficient Large-Scale MoE Training via Resource Modeling and Pipelined Hybrid Parallelism](https://arxiv.org/html/2605.05049v1)

- **Method**（§III–VI；§VI-A）：把 memory/compute/communication 模型与微基准结合选择 pipeline+expert-data 并行；token imbalance 触发 EP 组内最小交换专家迁移，显式算参数/optimizer/gradient 搬运成本。
- **Key evaluation**（§VII-A–D）：单层/整模型/细粒度 MoE framework 对照；64→1024 GPU 的弱扩展同时增加专家数。所报 2–3.6× throughput 绑定平台与细粒度模型，不是所有并行配方。
- **Direct limitation**（§IV、§VI-A 与 §VII-D 的直接范围）：成本模型需目标机器校准；migration 限 EP 组内并阈值触发，增专家弱扩展不是固定模型强扩展。论文未单列自身 limitation，不以结论首句替代，亦不声称按链路任意在线改 pipeline。
- **采用边界**：large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-DISTRIBUTED-TRAINING` 正文中的 `SF-PIPER-EFFICIENT-LARGE-SCALE-MOE-TRAINING-VIA-RESOURCE-MODELING-AND-PIPEL` 已承载“large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [SoK: Robustness in Large Language Models against Jailbreak Attacks](https://arxiv.org/html/2605.05058v1)

- **Method**（§III）：Security Cube 将 jailbreak robustness 拆成 attacker、defender、judge 三轴，并为 attack/defense/judge family 建立组合评价。
- **Key evaluation**（§IV）：13 attacks、5 defenses、4 judges 及披露模型配置；排名与 ASR 只对相应组合有效。
- **Direct limitation**（§V）：SoK/作者实验是 2023–2025 方法快照；选择的攻击、防御与 judge 不能穷尽开放威胁，也不能证明单一配置生产安全。
- **采用边界**：把 jailbreak evaluation 从单一 ASR 展开为 attack、defense、judge 与模型配置的多维合同
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66/Ch72 已要求 threat model、attack、defense、judge、model 和 effect receipt 分权记录；taxonomy 不构成额外机制 owner。

### [The Impossibility Triangle of Long-Context Modeling](https://arxiv.org/html/2605.05066v1)

- **Method**（§2–6；Theorems）：在 OSP 抽象下证明长序列系统不能同时保持长度无关的单步计算、固定有限状态与随历史增长的精确随机关联召回；容量通过有限精度信息量进入下界。
- **Key evaluation**（§7）：d=64、2-layer 的 synthetic associative recall 五组实验用于检验边界趋势；52 架构分类只是渐近性质映射，不是统一 benchmark。
- **Direct limitation**（§8.4）：经验规模很小且任务为 worst-case random KV；常数、近似召回、分布结构和更强压缩可能改变实际 operating point，不否定 workload-specific architecture。
- **采用边界**：长序列机制不能同时获得与长度无关的单步计算、与长度无关的固定状态，以及随历史事实数增长的精确召回容量；必须选择 workload-conditioned trade-off
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MODEL-LONG-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-05066` 已承载“长序列机制不能同时获得与长度无关的单步计算、与长度无关的固定状态，以及随历史事实数增长的精确召回容量；必须选择 workload-conditioned trade-off”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Automatically Finding and Validating Unexpected Side-Effects of Interventions on Language Models](https://arxiv.org/html/2605.05090v1)

- **Method**（§3）：对 base/intervention model 生成配对响应，先提出自然语言 side-effect 假设，再用独立 discriminative validation、对照与 FDR 筛选。
- **Key evaluation**（§4–5）：先在已知合成行为验证召回，再覆盖 reasoning distillation、ROME editing 与 unlearning interventions；测的是发现/验证协议而非实时监控。
- **Direct limitation**（Limitations）：发现依赖 prompt bank，稀有/对抗性行为会漏检；discriminator/model shared bias 与计算成本限制开放分布结论。
- **采用边界**：model interventions need systematic validation of unexpected side-effects before release
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`PLATFORM-EVALUATION-SYSTEM` 正文中的 `SF-AUTOMATICALLY-FINDING-AND-VALIDATING-UNEXPECTED-SIDE-EFFECTS-OF-INTERVEN` 已承载“model interventions need systematic validation of unexpected side-effects before release”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics](https://arxiv.org/html/2605.05097v1)

- **Method**（§3.1–3.4，Eq.1–3）：每条有向 edge 有 fast/slow 双变量；外部共现只直接驱动 fast，slow 通过双向耦合巩固，retrieval 只读 fast 且不更新记忆。
- **Key evaluation**（Appendix A.1–A.4）：13 篇 Wikipedia 文档、51 对关系，四种重复/近期状态组比较耦合、去 slow 的匹配消融与无衰减累加；测 edge dynamics 而非 retrieval。
- **Direct limitation**（Appendix A.5 Scope；§4 Discussion）：作者明确无 retrieval 指标、无已发表系统比较，较大/变化文档流验证待做。当前 official abs/v1 HTML 相互一致；raw 旧摘要的 no empirical wording 只作历史元数据，不能压过 exact-v1 实际 Appendix。
- **采用边界**：每条关联 edge 的 fast/slow 双变量耦合使重复事件巩固、缺少强化时衰减，检索只读 fast 状态；13 文档实验只检验动力学，不证明 retrieval 质量或系统优势。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch77 已把 immutable episode、derived memory、retriever 与 truth authority 分离；本材料的窄命题“每条关联 edge 的 fast/slow 双变量耦合使重复事件巩固、缺少强化时衰减，检索只读 fast 状态；13 文档实验只检验动力学，不证明 retrieval 质量或系统优势。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Text Corpora as Concept Fields: Black-Box Hallucination and Novelty Measurement](https://arxiv.org/html/2605.05103v1)

- **Method**（§2）：将语料句向量 delta 拟合为局部 Gaussian concept field，用相对场的 z-distance 量生成文本对语料概念轨迹的偏离。
- **Key evaluation**（§3–4）：在 CFR groundedness、Gutenberg novelty 与受控 LLM rewrites 上比较分离能力；该量依赖 embedding、corpus 和局部校准。
- **Direct limitation**（§5）：corpus-attributable drift 不等于事实错误；黑盒可追溯性不消除 domain/embedding bias，也未给跨语料稳定阈值。
- **采用边界**：groundedness sensor 不必二次生成或读内部状态；语料句间 embedding delta 的局部 Gaussian field 给出可追溯偏离信号，不把语料偏离等同事实错误。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：这是特定表示空间的 detector，不改变 Ch66 已有 grounding/evidence authority；不把语料距离升级为真值判断。

### [Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime](https://arxiv.org/html/2605.05112v1)

- **Method**（§2.1–2.3）：N=8：0/8、8/8过滤；3–5普通训练；1–2成功 prefix、6–7失败 prefix。逐桶 EMA 调 replay ratio，经原 parser/executor 重建状态后 current-policy continuation，旧 assistant prefix mask=0。
- **Key evaluation**（§3–4；Appendix D）：Qwen3 14/32B SWE-bench 与4/8B数学，共用同数据/rollout-budget GRPO++；峰值同step和达到baseline分数所需step分开，avg8不是独立训练seed；agent端到端时间包含重放执行。
- **Direct limitation**（Appendix A.1–A.2）：只验证 binary reward/N=8 与筛过的数学集；需能保存/replay prefix，非确定工具行为依框架；50%是此奖励信号目标，不是所有 curriculum/controller 最优。
- **采用边界**：binary-reward RL should control rollout pass rate to keep sampling in an informative regime
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-GRPO` 正文中的 `SF-ROLLOUT-PASS-RATE-CONTROL-STEERING-BINARY-REWARD-RL-TOWARD-ITS-MOST-INFO` 已承载“binary-reward RL should control rollout pass rate to keep sampling in an informative regime”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [How Long Does Infinite Width Last? Signal Propagation in Long-Range Linear Recurrences](https://arxiv.org/html/2605.05113v1)

- **Method**（§1.1; Theorem 2.1; §3.1–3.3）：对独立 proper complex Gaussian recurrent matrix、与矩阵独立且逐时二阶矩单位的输入，推导有限宽线性 RNN/LRU 期望信号能量；深度约 sqrt(width) 时出现非消失修正，超临界亚线性深度放大。
- **Key evaluation**（§4 Figures 2/3）：Monte Carlo 信号能量与闭式/渐近轮廓对比，验证复 Gaussian 临界规律并展示实 Gaussian 对照；这是初始化动力学数值检验，不是训练任务基准。
- **Direct limitation**（§5.1）：实 Gaussian 只有偏离条件而非全套精确结果；非 Gaussian 实用初始化、非线性、训练稳定性和 feature learning 均未解决，不能当作所有 SSM/LRU 的部署长度界。
- **采用边界**：长递推不能无条件套无限宽初始化；线性复高斯状态在 t≈sqrt(n) 出现有限宽边界，改变长程稳定性解释。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch22 已把有限 state、compute、精确召回、压缩/检索与长程稳定性写成条件分支；本材料的窄命题“长递推不能无条件套无限宽初始化；线性复高斯状态在 t≈sqrt(n) 出现有限宽边界，改变长程稳定性解释。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior](https://arxiv.org/html/2605.05115v1)

- **Method**（§3–4）：分别拟合 activation 与 behavior manifold，用 pullback metric 求 geodesic intervention，并与线性 activation steering 比较路径偏离。
- **Key evaluation**（§5）：简单语言属性任务与一个 Mountain Car recurrent world-model 案例；只验证受控概念/小模型上的路径差异。
- **Direct limitation**（§6）：依赖可拟合低维 manifold 与 chosen behavior metric；简单任务不证明大模型复杂能力的通用安全 steering。
- **采用边界**：线性 activation steering 可能离开自然行为流形；双向几何干预比较显示路径形状重要，改变内部控制从方向到几何轨迹的选择。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：受限 representation-control 案例，没有足够证据改写 Ch17 的层级机制；原 owner 从 Self-Attention 收窄为 Transformer Layer，但不写 Books。

### [On the Hardness of Junking LLMs](https://arxiv.org/html/2605.05116v1)

- **Method**（§2；§4）：直接在非语义token输入上提高目标prefix概率，以最小随机坐标搜索作诊断基线；prefix成功与后续真正有害完成分别测。
- **Key evaluation**（§4–5）：四个7B开源对齐模型、50 AdvBench目标；访问概率/token-ID，greedy生成，报告整条search trajectory最佳judge输出而非单次末端无挑选结果。
- **Direct limitation**（Appendix A）：仅proof-of-concept、7B/open模型，受限API未证实；高perplexity可检测，作者明确不是现实威胁模型。发现序列不识别其训练成因。
- **采用边界**：无语义 junk token 也能触发目标有害前缀，说明对齐安全边界不能只覆盖人类可解释的 jailbreak prompt
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch72 已把 untrusted content、对抗生成、检测可见性与最终 policy/effect gate 分层；非语义 junk-token 白盒搜索是受限 proof-of-concept，不改变该防御主线。

### [On the Wasserstein Gradient Flow Interpretation of Drifting Models](https://arxiv.org/html/2605.05118v1)

- **Method**（§2.3；§3；Appendix B–D）：把简化 GMD 写成 Parzen-smoothed KL 的 WGF fixed point，再分析实际 cross-weighted implementation：它的零速度条件可识别 p=q，但一般不存在对应的 WGF functional，并给出 distant non-overlapping modes 的 failure construction。
- **Key evaluation**（§3.3；§4.3；Appendix D/F）：二维 toy distributions 比较 Sinkhorn proxy、KL/W2 flow，并展示 non-overlapping support 下的 failure；主要证据是命题与反例，不是图像/文本质量、吞吐或生产 benchmark。
- **Direct limitation**（§3.2–§4；Appendix assumptions）：分析依赖 kernel/Parzen 和连续分布假设，未证明 finite neural parameterization、训练稳定性或部署收益；它修正机制解释，不单独建立 GMD 为长期默认生成范式。
- **采用边界**：生成式 drifting 的理论标签必须区分 proposed KL/Wasserstein fixed-point construction 与实际实现的 Sinkhorn-like proxy；后者一般不是任何 distributional loss 的 Wasserstein gradient，也不继承相同收敛性质。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：Ch24 未采用 GMD/Drifting 作为正文机制；该 note 纠正 emerging family 的理论解释，但在原 family 形成可复用系统路线前，不为一篇 correction 新建孤立正文。

### [Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical System Prediction](https://arxiv.org/html/2605.05134v1)

- **Method**（§3）：分别拟合 correct/hallucinated token-embedding dynamics 的 Koopman transition，以 differential residual 和小量标注校准单次输出阈值。
- **Key evaluation**（§4）：在 HaluEval 等披露数据/模型上比较检测 AUROC/成本；需要训练期 regime labels 与可得 embedding。
- **Direct limitation**（§5）：只能检测不能纠正；阈值、embedding 与域迁移决定 false positives，单次低 residual 不构成 factuality guarantee。
- **采用边界**：黑盒幻觉检测通常需要多采样或外部 grounding；两种 regime 的 Koopman transition residual 加阈值校准提供单样本替代，必须检查训练标签和域迁移。
- **审阅/Books**：exact-v1 Source Review 完成；仅报告：特定 hallucination sensor 未改变 Ch66 对外部 evidence、校准与 abstention 的长期结论；不进入正文。

### [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/html/2605.05138v1)

- **Method**（§3）：Agent 从 action/observation history 编写可执行 Python world model，用已见 transition 回放验证并修订，再在模型上 rollout 计划。
- **Key evaluation**（§4）：ARC-AGI-3 的 25 个公开游戏，主要每局一次 fresh run，解出 7 个且 RHAE 分布不均；私有游戏和跨环境泛化未测。
- **Direct limitation**（§5）：scripted controller/fixed API 与公开环境可能形成 harness-specific prior；通过历史 transition 不证明未来模型正确，代码执行还新增 sandbox 风险。
- **采用边界**：纯文本计划不易反证 world model；可执行 Python model 由历史观测 verifier 约束再规划，同时关闭 harness 泄漏渠道，改变模型校验与动作执行关系。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MULTIMODAL-WORLD-MODELS` 正文中的 `SF-2026-ARXIV-2605-05138` 已承载“纯文本计划不易反证 world model；可执行 Python model 由历史观测 verifier 约束再规划，同时关闭 harness 泄漏渠道，改变模型校验与动作执行关系。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [The First Token Knows: Single-Decode Confidence for Hallucination Detection](https://arxiv.org/html/2605.05166v1)

- **Method**（§2.1–2.3）：单次 greedy 的首个内容 answer token，跳过模板/标点后将 top100 概率重归一化，以归一化熵构造 confidence；比较10次采样与双向 NLI semantic agreement 的额外成本。
- **Key evaluation**（§3.1–3.5 Tables 1–4）：PopQA/TriviaQA 各1000题，三种7–8B instruct模型，自动 judge，AUROC与paired bootstrap；semantic-AU差异只在6格中的3格显著，ensemble仍有平均0.021补充，不能说完全取代多样本信号。
- **Direct limitation**（Limitations）：仅英文 closed-book 短事实 QA；需 logits 和正确首token定位，不能外推长回答/RAG/黑盒。TriviaQA 控制正确性后仍有长度相关，自动 judge 噪声及未调优基线限制比较。
- **采用边界**：多次生成语义一致性未必比单 decode 更有价值；首个内容 token 的 top-k entropy 在受控 QA 达到相当检测，改变 UQ 成本基线。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化；本材料的窄命题“多次生成语义一致性未必比单 decode 更有价值；首个内容 token 的 top-k entropy 在受控 QA 达到相当检测，改变 UQ 成本基线。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

### [Design Conductor 2.0: An agent builds a TurboQuant inference accelerator in 80 hours](https://arxiv.org/html/2605.05170v1)

- **Method**（§2）：Agent 在固定 harness 中构建 RTL/accelerator，并用 Python reference、testbench、cycle trace 与 timing feedback 迭代实现。
- **Key evaluation**（§2.1–3）：四个设计案例含 TurboQuant accelerator；一个 80 小时长任务观察 human-review bottleneck、过度复杂修复与激进 goal setting。
- **Direct limitation**（§4.2）：案例不实现通用 constraint-revision、milestone commit 或 release authority 协议，也不证明自治硬件设计跨任务可靠。
- **采用边界**：把长任务拆成 proposal/implementation、constraint pack/milestone evidence 与 human/release commit authority 三层
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`AGENT-PLATFORM` 正文中的 `SF-2026-ARXIV-2605-05170` 已承载“把长任务拆成 proposal/implementation、constraint pack/milestone evidence 与 human/release commit authority 三层”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning](https://arxiv.org/html/2605.05172v1)

- **Method**（§III-A–III-C；Appendix A）：Q-Estimation 从 BC policy 的 action likelihood、entropy 与少量交互拟合 Q_BC；在线阶段保留冻结 Q_BC，并训练 Q_RL，gate 比较两者对 BC/RL action proposal 的值来收集数据和更新策略。
- **Key evaluation**（§IV；Appendix B–D）：D4RL/robomimic 用 20 rollouts、5 seeds，另有 Franka Panda 真实 pipe assembly、peg insertion 与 kitting；Q-initialization/Q-gating、replay seeding、BC auxiliary loss 和 rollout 数量均做消融。真实结论限 1–2.5h、单 A6000 与所测机器人。
- **Direct limitation**（§V；Appendix C）：需要 BC policy 暴露 action likelihood 与 entropy；soft-optimality、Q estimation 和 critic calibration 可能失准，尚不支持 diffusion/flow policy，Q gate 也不替代 physical safety envelope。
- **采用边界**：BC→online RL 不应让新 critic 立即覆盖已有可靠动作；可先从 BC action likelihood/entropy 与少量 rollout 估计冻结价值基线，再由双 Q gate 在 BC 保留与 RL 探索之间逐状态选择。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：Ch26 已有 compact RL head 与 human/safety handoff，但缺少 offline BC 可靠动作的独立价值 owner，以及在在线分布偏移下让 BC 与 RL proposal 竞争而非直接覆盖的分支。

### [Understanding In-Context Learning for Nonlinear Regression with Transformers: Attention as Featurizer](https://arxiv.org/html/2605.05176v1)

- **Method**（§3–5）：证明 attention 可构造多项式/spline features，再由后续层执行 least-squares，从而把 nonlinear ICL 分成特征生成与在线求解。
- **Key evaluation**（§6）：合成 nonlinear regression、多种 context/training sizes 与三 seed 数值实验检验误差趋势。
- **Direct limitation**（§7；Appendix）：结论依赖 polynomial/spline approximability 与特定 sum-based attention construction；不证明预训练 LLM 普遍按该算法执行 ICL。
- **采用边界**：线性 ICL 理论不足解释 nonlinear regression；attention 构造多项式/spline 特征并给 context/training size 误差界，补充 attention 作为 featurizer 的机制解释。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MODEL-SELF-ATTENTION` 正文中的 `SF-2026-ARXIV-2605-05176` 已承载“线性 ICL 理论不足解释 nonlinear regression；attention 构造多项式/spline 特征并给 context/training size 误差界，补充 attention 作为 featurizer 的机制解释。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents](https://arxiv.org/html/2605.05185v1)

- **Method**（§4.2；Appendix B）：Fatal-aware GRPO 将不可恢复 tool transition 识别为 fatal step，以 one-sided advantage clamping 避免失败 token 梯度支配，同时保留可恢复步骤学习。
- **Key evaluation**（§5）：Qwen3-VL 8B/30B-A3B/32B 在七个搜索 benchmark 上比较 SFT/RL 与 fatal-aware 组件消融。
- **Direct limitation**（Limitations）：search ranking/fetch/summarization 漂移增加 reward variance；专有 judge、外部 API 与单一训练 recipe 限制归因，视觉中间操作未单独评分。
- **采用边界**：把搜索失败拆成可恢复步骤错误与 fatal transition，并在 rollout/update 中区别处理
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch81 已按 recoverable/fatal transition、environment authority、retry/rollback 与 evidence receipt 组织 workflow；训练时 clamping 是受限实现，不改变 workflow owner。

### [LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/html/2605.05187v1)

- **Method**（§2–§3）：PhyScore 将 1,554 个、七类 generator 产生的视频分成 text-to-2D、image-to-4D、video-to-4D 三轨与 26 类，并由四名 trained annotators 给出四维分数及物理异常时间段。
- **Key evaluation**（§4）：最终 composite 为 0.2×timestamp IoU + 0.4×SRCC + 0.4×PLCC；自动 QC 只检查标注一致性。challenge 排名比较提交方法，不证明 composite 等于物理真值。
- **Direct limitation**（§5；challenge protocol）：维度权重与标签是 challenge 设计，learned metric 仍可能拟合 annotator/model family；没有 action-conditioned counterfactual、真实环境 rollout 或 causal intervention。
- **采用边界**：World-model video evaluation 应把 perceptual quality、physical realism、condition alignment、temporal consistency 与 anomaly localization 分开，避免平均视觉分数掩盖局部物理失败。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch25 已区分 perceptual、temporal、geometry/physics、action-conditioned transition 与真实 outcome，并要求局部 predicate/failure localization；PhyScore 没有补上 causal/controllable world-model contract。

### [Sharp Capacity Thresholds in Linear Associative Memory: From Top-1 Retrieval to Tail-Average Learning](https://arxiv.org/html/2605.05189v1)

- **Method**（§2–5）：对 isotropic Gaussian key-value 证明 top-1 读取需要 d²≈n log n，并提出 Tail-Average Margin 将目标改为受控候选列表；TAM 的完整渐近依赖 leave-one-out/postulates。
- **Key evaluation**（§5.3）：数值实验检验 top-1 与 TAM 的相变/score profile；小-tail 外推到 top-1 明确仍是 conjecture。
- **Direct limitation**（§4.2–5.4）：结论限线性记忆、Gaussian associations 与论文读取准则；listwise 降门槛是改变 correctness contract，不是免费增加精确容量。
- **采用边界**：线性记忆容量不能只数 d² 参数；top-1 retrieval 有 log n 极值代价，而 top-k/TAM 改变阈值，明确容量必须绑定读取判据。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`MODEL-LONG-CONTEXT` 正文中的 `SF-2026-ARXIV-2605-05189` 已承载“线性记忆容量不能只数 d² 参数；top-1 retrieval 有 log n 极值代价，而 top-k/TAM 改变阈值，明确容量必须绑定读取判据。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents](https://arxiv.org/html/2605.05191v1)

- **Method**（§3.1–3.4）：Context-ReAct 在 reasoning/tool loop 中加入 Skip、Compress、Rollback、Snippet、Delete 五种 meta-operation；Compress 的表达完备性与专门操作的效率分开论证。
- **Key evaluation**（§4）：BrowseComp/中文子集等四个 benchmark、LongSeeker-30B，部分集合各采样 200 问；比较 append-only/coarse curation 与原子操作。
- **Direct limitation**（§5）：仅 SFT synthetic trajectories，无 rejection/RL；表达完备不证明事实保真、检索正确或开放 workflow 的 rollback 语义。
- **采用边界**：long-horizon search needs elastic context orchestration across active, compressed and recoverable state
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch75 已分 active、compressed、recoverable state，保留 summary lineage、回读和不可把可恢复等同找对证据；五操作是实现词汇。

### [D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://arxiv.org/html/2605.05204v1)

- **Method**（§2.2）：同一 step-distilled diffusion model 在 student 自身 few-step rollout 上训练：student 只见文本，teacher 同时见目标图像与 prompt 的 multimodal feature。
- **Key evaluation**（§3）：LoRA 与 full fine-tuning 覆盖新 concept/style/domain preference，并比较 vanilla SFT 与组件消融；质量结论绑定作者模型、数据与评价。
- **Direct limitation**（§4）：约 4× FLOPs、2× iteration time；依赖 encoder/base model 的 in-context teacher 能力，teacher 在 multimodal condition 下失败时训练也失败。
- **采用边界**：普通 SFT 会损伤少步扩散能力；同模型 teacher 额外读目标图像、student 在自身 rollout 上蒸馏，改变保留 few-step 能力的连续适配路径。
- **审阅/Books**：exact-v1 Source Review 完成；整合（已落实）：`TRAIN-SFT` 正文中的 `SF-2026-ARXIV-2605-05204` 已承载“普通 SFT 会损伤少步扩散能力；同模型 teacher 额外读目标图像、student 在自身 rollout 上蒸馏，改变保留 few-step 能力的连续适配路径。”，并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。

### [Taming Outlier Tokens in Diffusion Transformers](https://arxiv.org/html/2605.05206v1)

- **Method**（§3.1–4.2）：编码器 high-norm outlier 在 RAE-DiT 内进一步放大；mask outlier loss 不改善生成，因而检验编码器 registers/TTR 与 generator diffusion registers，而非把范数截断视为语义恢复。
- **Key evaluation**（§5.1–5.2; Tables 7–9; Appendix D）：ImageNet256 DiT-B/L/XL，pixel/VAE/多编码器输入及24.7M synthetic Scale-RAE T2I；gFID/GenEval/DPG，register 深度/数量有非单调最优，100 registers 可恶化。
- **Direct limitation**（§5.2; Appendix C/D）：TTR 改变编码器分布，现有decoder无需重训仅为所测设置；T2I只用原Scale-RAE四分之一数据、一个epoch。patch语义损坏为机制假说，不能由loss-mask负结果单独证明；register处理需保留encoder/generator两类区别。
- **采用边界**：简单屏蔽 DiT 高 norm token 并不能修复语义损伤；encoder 与 denoiser 双 register 分治提供不同 outlier 处理机制。
- **审阅/Books**：exact-v1 Source Review 完成；已有覆盖：Ch24 已把 AR/diffusion 的 factorization、iterative state、correction、commit 与 runtime handoff 分开；本材料的窄命题“简单屏蔽 DiT 高 norm token 并不能修复语义损伤；encoder 与 denoiser 双 register 分治提供不同 outlier 处理机制。”是受限机制/反例，没有改变现有 state/data/control owner、适用条件或失败回退。

## 5. 缺口与下一步

作者侧 Evidence 计数为 **156 完成、4 争议、0 待审、0 retained-candidate access blocker**。Books disposition 为 **63 整合、76 已有覆盖、17 仅报告、4 争议**。7 项 locator 已按 exact-v1 真实目录重定位；23 项 canonical family 已登记旧 Books marker 与 `arxiv:*v1` alias；Books comparison 已从 active 160-item packet 重建为 63 项整合，旧快照双方各 29 项漂移已消除，跨日 `2605.08215`、`2605.08234` 已排除。

当前没有需要用户补充的 primary material。NLA、2605.06548 与四项争议均为本窗终态保留项，只保留身份、限制和定点重开条件；它们不用于正面证据，不支持 Books 或无遗漏断言。root 写回、第三次限定返修与新的非作者终审均已完成；Coverage、Evidence 与 Books 已处理到安全终态，当前没有未处理的可执行工作。

## 6. 复核

复核者：`fresh-context:may07_fourth_final_reviewer:2026-09-15`

结论：通过

### 第四次 Fresh-context 非作者终审（2026-09-15）

复核者：`fresh-context:may07_fourth_final_reviewer:2026-09-15`；结论：**通过**。本复核者未参与第三次作者返修或 root Books 写回，且未修改 Books。复核确认 `548 = 160 + 387 + 1`、`156 complete + 4 disputed`、`63 Integrate + 76 No Change + 17 Daily Only + 4 Disputed`；逐篇在线核对 7 个 exact-v1 locator，验证 23 组 canonical/旧 marker alias、active comparison 63/63、29/29 漂移修复、两个跨日 family 排除、withdrawn 隔离及 63 个 Books marker 的 owner/唯一性/正文位置。另对前轮以外的 18 个高风险 closure 做分层假阴性挑战，未发现新漏项。完整记录见[第四次非作者终审](../_sources/daily-20260507/V3_FOURTH_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md)。日报状态改为完成。

### 第三次作者限定返修交接（2026-09-15）

已按第三次终审的最小范围完成返修：7 项 exact-v1 locator 均以官方 HTML 实际目录重定位；23 项 active canonical Source Family 与旧 Books marker 已在 active ledger、packet 和 comparison 建立显式 alias；`books-current-content-comparison.json` 已按 active 160-item packet 重建为 63 项整合，并排除跨日 `2605.08215`、`2605.08234`；active evidence manifest 同步重建为 160 项。精确账目与校验见[第三次作者返修 checkpoint](../_sources/daily-20260507/V3_THIRD_AUTHOR_REPAIR_20260915.md)。未修改 Books 正文；作者不能验收自己，状态保持进行中，等待新的非作者限定复核。

复核者：`fresh-context:may07_final_independent:2026-09-15`；结论：**未通过**。分母、withdrawn、评分加总、Stable Node、63 项 Books marker 与新增 7 项正文语义均通过；但 exact-v1 在线对读发现新增 7 项 locator 均需校正，另有 23 项 canonical/旧 marker alias 未登记，`books-current-content-comparison.json` 与 active 63 项整合集合存在 29/29 漂移。完整证据与最小返修范围见[第三次终审清单](../_sources/daily-20260507/V3_THIRD_FRESH_CONTEXT_FINAL_REVIEW_20260915.md)。日报保持进行中。

复核者：`fresh-context:may07_second_final_reviewer:2026-09-15`；结论：**未通过**。本轮确认当前 151 项计数、三项新增正文和四项 disputed 状态一致，但在 35 项关闭样本中发现 6 个高置信度 false negative，并发现 `2605.04450` 的 canonical Source Family 与 Ch54 marker 不一致。完整范围、反查边界与最小修复见[第二次终审清单](../_sources/daily-20260507/V3_SECOND_FRESH_CONTEXT_FINAL_REVIEW_20260915.md)。日报保持进行中。

复核者：`fresh-context:may07_final_reviewer:2026-09-14`；原终审结论：**未通过，已进入作者修复**。本轮作者已处理该清单，root Books 写回也已落实，但作者不能复核自己；日报继续保持“进行中”，等待新的独立 reviewer。

复核者：原独立 reviewer `/root/may06_independent_review`；结论：未通过。其审计已封存为[问题清单](../_sources/daily-20260507/INDEPENDENT_REVIEW_20260914.md)：全 78 题摘/评分/证据字段，469 关闭标题与36完整摘要分层抽查，11项在线 exact-v1、44项 Books 正文。该身份现已转为作者，不能验收自己修后的稿。

原独立审计的 137 项，以及后续 148、151 项，均为已经被本轮修复取代的历史 checkpoint，不再作为当前计数。root 此前写回的 56 项保持不变；本轮新增 7 项已按 owner 合并写入 Books，并以唯一正文 marker 记录；该 checkpoint 当时尚未完成独立语义终审，现已由上述第四次复核闭合。

本轮重新检查格式、JSON 唯一性、评分、alias、链接与范围内 diff；通过只证明可判定一致性。第二次独立语义复核发现的漏项与 Source Family trace 问题已由作者修复，新增 7 项 Books 写回也已完成；该 checkpoint 当时仍等待新的非作者验收，现已由上述第四次复核闭合。未 stage、commit、push。

### 第二次作者修复交接（2026-09-15）

分母守恒：**548 = 160 retained + 387 pre-denominator closure + 1 withdrawn**。Evidence：**156 complete + 4 disputed + 0 pending**。Books：**63 Integrate + 76 No Change + 17 Daily Only + 4 Disputed**。

指定 6 项与同簇新增 3 项均已完成 exact-v1 Method/Evaluation/limitations、V3 score、唯一 owner 和 Books disposition。Ch54 alias 已贯通，不重复正文。新增 7 项 Integrate 已由 root 写入 Books，见 root 写回记录；该 checkpoint 当时保持进行中，现已由上述第四次非作者终审验收通过；未 stage、commit、push。
