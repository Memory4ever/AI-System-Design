# 2026-05-06 非作者 Books 对账结论

本文件是 2026-05-06 冻结候选的命题级对读与最终写回结果。10 项新增已由 root 串行落地，并通过独立 post-write 审计。

## Gate 结论

- 冻结候选：137。
- 已完成独立 Books 对读：137/137。
- `Integrate — already present`：12；现存正文均找到具体机制命题，不以主题相似替代覆盖证明。
- `Integrate — applied and post-write audited`：10；由作者初判的 24 项收紧而来。
- `No Change — Existing Coverage`：115；其中 14 项为本轮从写回建议降级。
- `Rejected`：0；准入拒绝属于 356 个 pre-denominator closure，不混入候选 Books 账本。
- Withdrawal closure：`2605.03562`；不属于 137 个候选，Books 正向链复算通过。

## 已落实的 Root 串行写回

### 2605.02909 — `TRAIN-GRPO` / Ch33

- **现有命题：** “Verifier Error 可能在组内相关”已说明同一 prompt、答案格式与 parser path 会形成共同偏差，并要求切片估计相关性。
- **最小增量：** 在该段之后补足错误模式的动态后果：随机噪声主要延迟学习；系统性 false positive 会被 policy 主动发现并放大，随 trigger frequency 与 conditional advantage 进入 plateau 或 collapse。总体 error rate/FPR 不能替代错误模式与 policy visitation 的联合诊断。
- **证据边界：** exact-v1 §3、§4、§5；受控算术任务、人工注入错误模式，不证明开放式 verifier 的多重交互失效。
- **相邻衔接：** 上承“相关误差减少有效样本量”，下接“Verifier 也成为 Policy 时必须分离更新与权威”；新段只拥有训练动力学诊断，不把 verifier 提升为 correctness authority。

### 2605.03159 — `AGENT-WORKFLOW` / Ch81

- **现有命题：** 章节已把 workflow tests、structured obligation、runtime trace 与 outcome evidence 分开，并强调 trace 不是 workflow definition。
- **最小增量：** 增加一种由 3–5 条 passing traces 归纳 acceptance contract 的受限路径：PTA 保存观察到的序列，state merging 泛化等价状态，dominator/order constraint 表达必要状态与顺序；新执行只需满足必要状态的拓扑子序列，而非与一条 trace 完全相等。
- **证据边界：** exact-v1 §2.2、§3、§5；小型合成 VS Code extension 和极少 failure 样本，不证明开放 UI 的状态等价或 trace coverage 完备。
- **相邻衔接：** 放在 deterministic workflow tests 与 generated visible/hidden tests 之间；强调 observed trace、induced contract、authorized workflow 是三个身份。

### 2605.03188 — `PLATFORM-SECURITY` / Ch72

- **现有命题：** DP 章节已定义 privacy unit、adjacency、composition、accountant 与 post-processing，但尚未具体说明多轮 Agent 的同源值及其派生值如何避免重复消费/泄漏放大。
- **最小增量：** 增加 dependency-aware release graph：私有 root 只加噪一次，后续派生查询从同一 noised root 确定计算并复用；root identity、dependency DAG、budget allocation 与 release cache 必须共同版本化。独立重复加噪会让攻击者平均恢复 root，非线性派生还可能放大可区分性。
- **证据边界：** exact-v1 §3–§5；结构化数值、单用户、perfect-NER 假设。不得外推到自由文本、多用户组合或未识别的秘密根。
- **相邻衔接：** 放在 DP production contract 后、memorization/extraction 区分前；该机制落实 composition，不替代访问控制或内容识别。

### 2605.03252 — `TRAIN-LORA` / Ch30

- **现有命题：** 章节已说明 nominal rank 不等于 effective rank，A/B 几何与初始化会导致更新方向退化。
- **最小增量：** 增加 multi-expert LoRA 的 zero-init symmetry deadlock：所有 B 分支同时为零时，router 在相同输出/梯度下没有分化信号；将 expert update 限定到互不重叠的基座奇异子空间可在初始 forward 近似不变时打破对称。它是充分构造，不是最优分解。
- **证据边界：** exact-v1 §3–§5；DiT、受测 adapter/routing 配置，子空间受限可能损失最优更新方向。
- **相邻衔接：** 紧接 effective-rank 段，再进入 target-module/placement；把初始化、expert identity 与 optimizer state 纳入 adapter identity。

### 2605.03317 — `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24

- **现有命题：** 章节已把 diffusion 写成随 timestep 变化的生成过程，并区分 training objective 与 runtime sampler。
- **最小增量：** 补充 representation supervision 也应随 SNR/timestep 改变：高噪声阶段需要粗粒度全局结构，低噪声阶段需要细粒度局部细节；静态单层/单尺度 teacher alignment 会形成非平稳 mismatch，动态 router 只能选择指导尺度，不能拥有最终生成正确性。
- **证据边界：** exact-v1 §3–§5 与 Appendix J；依赖冻结 VAE 的层级特征，ImageNet/MS-COCO 与所测 SiT 规模，不证明所有 diffusion backbone 或 modality 通用。
- **相邻衔接：** 放在 diffusion training/inference mismatch 之后、few-step/correction 路线之前；它改变训练表征目标，不改变 sampler commit owner。

### 2605.03351 — `INFER-KV-CACHE` / Ch45

- **现有命题：** 章节已把 video ingestion state 与 decode KV 分为不同 cache object，也已说明 cache identity、reuse 与 invalidation。
- **最小增量：** 把视频 VLM 的两个复用阶段显式分开：同一视频 follow-up 可复用已经完成的 vision-tower/persistent KV，收益上界大；fresh-video first pass 只能在 vision tower 内做 frame pruning，整体收益受 stage share 限制。两类路径必须分别计时并校验 drift，不能混成一个 anti-recomputation headline。
- **证据边界：** exact-v1 §3–§6、§9；受测 Qwen/Gemma、VideoMME/MVBench/TOMATO、特定硬件与预处理。aggregate accuracy 不覆盖时序稀有事件。
- **相邻衔接：** 放在 video cache object 身份之后、block/page 管理之前；Ch45 拥有复用与失效，Ch23/24 继续拥有视觉表示/生成质量。

### 2605.03625 — `AGENT-PLANNING` / Ch79

- **现有命题：** “Search-based Planning 的边界”已比较单路径与运行时 tree search，并要求预算、heuristic、verifier 和外部 evidence。
- **最小增量：** 增加 training-time search teacher 与 runtime search 的分离：符号 graph search 可离线收集更优计划并迭代 fine-tune generative planner；部署时模型可直接生成计划，是否再启用 search 由 latency、optimality 与 verifier budget 决定。训练用 search 不意味着线上必须保留同等搜索。
- **证据边界：** exact-v1 §3–§7；PDDL/Blocksworld/Logistics/Labyrinth/Sokoban held-out problems，不证明开放世界、部分可观测或工具副作用下的 plan correctness。
- **相邻衔接：** 放在 Search-based Planning 基础段之后、dynamic branching 之前；它回答 search 在训练/运行两个阶段的 owner 分离。

### 2605.03724 — `TRAIN-LORA` / Ch30

- **现有命题：** 章节已说明 rank 是参数化上限而非任务本质维度，effective rank 还受初始化与 optimizer 影响。
- **最小增量：** 补充“rank threshold”不是跨 loss 的统一常数：MSE 下的充分阈值依赖显式随机特征/NTK与谱假设；cross-entropy 在一般情形没有同样的有限阈值，额外 PL 条件下才可恢复受限结论；经验最优 rank 仍受 bias–variance、样本量、层位置与类别数影响。
- **证据边界：** exact-v1 §4–§6；Gaussian-iid/NTK、binary/few-shot BERT/RoBERTa 条件，不能当作任意模型、任务和 loss 的 rank recipe。
- **相邻衔接：** 放在 nominal/effective-rank 判断之后；先限定可证明的充分条件，再回到 placement 与行为验证。

### 2605.03812 — `PLATFORM-SECURITY` / Ch72

- **现有命题：** 章节已要求 accelerator/driver 验证 buffer ownership、address range、DMA capability，并指出 IOMMU 不等于 device command 或内存完整性保证。
- **最小增量：** 增加 GPU page-table corruption 的跨层攻击链：DRAM Rowhammer 位翻转可篡改 GPU PTE，进而获得 GPU 任意读写、模型/代码篡改，并沿驱动路径升级到 CPU；因此 tenant isolation 还需 GPU page-table integrity、ECC/refresh/retirement、driver validation 与异常映射审计，单独 IOMMU 不能覆盖 device-local PTE 被破坏。
- **证据边界：** exact-v1 §IV–§VIII；实证限 NVIDIA RTX A6000/GDDR6 与其驱动/内存条件，不证明其他 GPU 可攻击或所列 mitigation 已生产有效。
- **相邻衔接：** 紧接 accelerator confused-deputy/DMA 边界；从合法命令越权推进到设备页表完整性，再回到 policy/attestation。

### 2605.03945 — `PLATFORM-SECURITY` / Ch72

- **现有命题：** DP 章节已强调隐私声明由 privacy unit、adjacency 与 accountant 限定，utility 不能反向证明同等级隐私。
- **最小增量：** 增加 CorrDP 作为较弱、显式条件化的 alternative branch：若把敏感/非敏感 feature correlation 写入 adjacency/distance，可降低噪声并提高 utility，但它提供的是 CorrDP guarantee，不是相同 epsilon 下的标准 record/user-level DP。相关性估计、公开辅助数据与高维误差都进入 privacy artifact。
- **证据边界：** exact-v1 §2–§6；理论假设和合成/Adult/Sepsis/Credit/Medical-Cost 实验，不证明真实相关结构稳定，也不能把 utility gain 外推为标准 DP 的免费改进。
- **相邻衔接：** 放在 DP production contract 后作为 Alternative Branch，并在进入 agent-derived-release 机制前先明确保证强度变化。

## 从写回建议降级为 Existing Coverage 的 14 项

| Source Family | Owner | 已有具体命题 | 降级理由 |
| --- | --- | --- | --- |
| `2605.03348` | `MULTIMODAL-REPRESENTATION` | modality-specific expert routing、融合位置、capacity sharing 已明确 | S3 的 specialize/select/sparsify 是受限方法实例，没有增加长期 owner 或新系统 contract |
| `2605.03356` | `PLATFORM-EVALUATION-SYSTEM` | correctness predicate、mutation kill、suite strength 与 evaluator ladder 已明确 | PostcondBench 只把既有评价合同应用到 formal postcondition |
| `2605.03363` | `MULTIMODAL-EMBODIED-VLA` | high-level task/trajectory proposal 与 low-level controller/safety commit 已明确 | 论文是该分层的直接案例，不新增机制边界 |
| `2605.03409` | `AGENT-WORKFLOW` | retry、idempotency、compensation/Saga 与 reconciliation 已明确 | RAC 是现有恢复分支的框架化实例 |
| `2605.03413` | `MULTIMODAL-WORLD-MODELS` | operator-structured dynamics、executable typed delta 与 Reason-then-Render 已明确 | 离散短 primitive proof-of-concept 没有新增长期命题 |
| `2605.03623` | `MULTIMODAL-GENERATIVE-PARADIGMS` | learned transport、few-step proposal、student-state验收与 multi-step fallback 已明确 | cumulative flow map 是局部算法分支，不能仅因新名称重复追加 |
| `2605.03669` | `MULTIMODAL-WORLD-MODELS` | persistent state、object address/mutable content、bounded active window 已明确 | dense voxel+sparse instance 是现有状态分层的实现案例 |
| `2605.03769` | `TRAIN-PRETRAINING` | matrix-aware update、scale/symmetry-aware geometry、gradient spectrum 已明确 | Nora 的 row-wise angular projection 未改变现有 optimizer contract |
| `2605.03821` | `MULTIMODAL-WORLD-MODELS` | visual quality 与 control-relevant transition/reward 分离、long-horizon state refresh 已明确 | judge 与 sliding-window 结果受具体 robot-video setup 限制 |
| `2605.03822` | `AGENT-WORKFLOW` | versioned code/proof artifact、cross-file dependency、toolchain identity 与 verifier authority 已明确 | KVerus 是特定 Rust/Verus pipeline 实例 |
| `2605.03941` | `MULTIMODAL-WORLD-MODELS` | video quality、action-conditioned transition、intervention fidelity 的 evaluation ladder 已明确 | iWorld-Bench 增加数据集规模，不改变评价分层 |
| `2605.03952` | `PLATFORM-SECURITY` | 局部合理动作可累积成有害轨迹、需 cumulative diff/effect gate 已明确 | MOSAIC-Bench 是强证据案例，但正文命题已由现有 owner 完整承载 |
| `2605.03953` | `MODEL-TRANSFORMER-LAYER` | depth-wise gated access、early representation selection 与 bounded slots 已明确 | SATFormer 是同一机制的架构实例 |
| `2605.04018` | `AGENT-RAG` | relevance 不等于 sufficiency、evidence portfolio 与 agentic acquisition 已明确 | Bright-Pro 没有改变 retrieval/evidence ownership |

## 12 项现存实体回读结果

以下均已在 canonical owner 中找到机制正文或受限证据锚点：`2605.02946`、`2605.02960`、`2605.03190`、`2605.03309`、`2605.03314`、`2605.03327`、`2605.03425`、`2605.03596`、`2605.03644`、`2605.03667`、`2605.03677`、`2605.03884`。它们不需要重复追加；root 只需在本轮共享写入后确认没有被并发覆盖。

## Withdrawal cleanup

`SF-2026-ARXIV-2605-03562` 已从 137 候选、评分与正向 Books 决定中排除。post-write 精确搜索未发现 Books 中存在 `2605.03562`、`HeadQ`、对应 source-family 或 HeadQ 特有的 score-space/query-basis side-code 结论，因此共享 Books 不需要删除正文。Ch45 的“Quantization Objective 应对齐 Attention Distortion”由其他仍有效来源支持，保留正确。
