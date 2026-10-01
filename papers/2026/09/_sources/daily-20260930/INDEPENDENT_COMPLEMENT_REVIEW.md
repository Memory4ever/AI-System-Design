# 2026-09-30 Daily：独立主题补检与 exact-v1 证据复核

## 范围、身份与状态

- Reviewer：`sep30_complement_review`，非 Daily 作者；初始独立补检只写本文件。之后父任务明确授权 Ch25/26/28/72 的最小 Books 整合；Report 与共享索引仍不写，所写 Books 由父任务作非作者写后核。
- 本窗：`[2026-09-29T09:00:00+08:00, 2026-09-30T09:00:00+08:00)`。
- 已完整重读当日适用 AGENTS、Research/Report 合同、Research Sources 使用说明/每日与主题路由、Research Prompt、ROADMAP；学习 checkpoint 仅作当天路由。
- 输入是作者从本期官方 arXiv API 主题补检取得的九条线索，不是事先冻结的候选或强制保留名单。本复核逐项读完整标题/摘要，再按实际贡献准入和评分，不因模型小、局部实验或篇数排除。
- 九项都有具体机制增量，建议进入候选。6 分项完成标准审阅；因发现具体 Books 缺口，又定点补读相关方法/限制。7–8 分项完成深审所需的方法、关键对照与非支持边界；均未复现作者代码或实验。
- 本文件不证明整个 Daily 的来源覆盖、全体候选分母或最终完成门已通过；冻结、家族合并、跨来源首公开核去重由作者汇总。本轮无访问隔离项，无以普通未完成项冒充 blocked。

## 日期证据：公告而非提交

独立查看官方新列表，页头均为 `Showing new listings for Wednesday, 30 September 2026`：

| 官方入口 | 本轮定位项 |
| --- | --- |
| [cs.RO/new](https://arxiv.org/list/cs.RO/new) | Rho，new 项 112 |
| [cs.CV/new](https://arxiv.org/list/cs.CV/new) | Honeycomb，new 项 180；HelixWorld，new 项 220 |
| [cs.LG/new](https://arxiv.org/list/cs.LG/new) | Delta-Matching，new 项 258；SOMA，new 项 264；WUSH-KV，new 项 292 |
| [cs.AI/new](https://arxiv.org/list/cs.AI/new) | AdviSD，new 项 205；ToolFence，cs.CR cross-list 项 409 |
| [cs.CL/new](https://arxiv.org/list/cs.CL/new) | Mnemon，new 项 31 |

按[官方 Availability 日程](https://info.arxiv.org/help/availability.html)的周一 14:00 至周二 14:00（Eastern）截止区间→周二 20:00 公告，本期公告为 `2026-09-29 20:00 EDT = 2026-09-30 08:00 +08:00`，在本窗内。列表身份加官方日程支持的是这次公开公告归属，不用 abs 的 Submitted 字段代替公开日期。九项当前原文/身份页未显示撤稿、更正或足以改写归属的更早正文发布声明；这不是穷尽全网早期发布证明。若作者机构/项目来源查到明确早期正文，须以更早事件校正。

特别注意 Mnemon 的提交为 `2026-09-28 18:17:13 UTC`：提交晚于当日 14:00 EDT 截止，不能按 submitted 把它挪到 09-29 Daily。

## 准入与分数校准

评分顺序为 Design Delta / System Reach / Durability，各 0–3。以下是 reviewer 建议，不是已冻结最终评分；证据强弱不计入 System Reach。

| exact-v1 | 完整标题 | 分数 | 实际增量与 owner |
| --- | --- | --- | --- |
| 2609.38164v1 | Rho: A Foundation for Efficiently Adaptable VLA Models | 2/2/2 = 6 | embodiment midtraining 与冻结 action generator 的 latent-policy 适配面分离；`MULTIMODAL-EMBODIED-VLA` |
| 2609.38123v1 | HelixWorld: A Real-time Interactive Audio-Visual World Model | 2/2/2 = 6 | camera-conditioned 视听联合状态与在 student 轨迹上纠偏的 streaming distillation；`MULTIMODAL-WORLD-MODELS` |
| 2609.37690v1 | Honeycomb: Constant-Size Scene Memory Representation for Video World Models | 2/2/3 = 7 | 固定六平面 memory 的 bounds 扩张/warp/增量写入及分辨率代价；`MULTIMODAL-WORLD-MODELS` |
| 2609.37852v1 | Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs | 3/2/3 = 8 | forward/backward 不一致的 stale delta 破坏 softmax 梯度不变量；`TRAIN-PRETRAINING` |
| 2609.37899v1 | Scaling Zero-Order Pretraining through Model Sharding | 2/2/3 = 7 | 固定可分目标上移除跨 expert SPSA 扰动噪声，而非通用通信分片；`TRAIN-PRETRAINING` |
| 2609.37196v1 | ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents | 3/2/2 = 7 | capability-shape grant 与当前参数 provenance 的分离，缓解 within-tool attack；`PLATFORM-SECURITY` |
| 2609.38121v1 | WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms | 2/2/2 = 6 | K/V 分别按 consumer sensitivity 变换，post-RoPE K 代价不能折叠；`INFER-KV-CACHE` |
| 2609.38142v1 | AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation | 2/2/3 = 7 | advice-sensitive 决策的预测性门控与共享参数蒸馏干扰；`TRAIN-GRPO` |
| 2609.36059v1 | Mnemon: Raw Records, Fast Judgments, Slow Thoughts | 2/2/3 = 7 | raw evidence 权威、可重建索引与 bounded judgment-wave 读路径分离；`AGENT-MEMORY` |

重新校准第二维后，各项 System Reach=2 的依据分别是：Rho 跨 embodiment 数据/任务更新/冻结执行器的适配接口；Helix 跨离线 teacher 与在线视听 stream；Honeycomb 跨 memory writer/store 与生成 readout；Delta-Matching 跨低精度 attention-core kernel 与训练图梯度 contraction；SOMA 跨目标/表示分解与并行专家更新边界；ToolFence 跨 blueprint/judge 与实际 tool executor；WUSH 跨离线 calibration 与在线 post-RoPE cache consumer；AdviSD 跨可训练 advisor 与冻结外部 executor；Mnemon 跨 raw store/后台派生索引与在线 View/answer。它们没有因“可以关联多个章节”而加分，也不声称原文验证了完整生产生命周期，故第二维不取 3。

本轮是 primary-source 审閱，不是独立 rerun。SOMA 的小 LSTM 证据不等于贡献不成立；也不能把它外推成大型 Transformer 的已验证方案。Rho/Helix/WUSH 的 6 分不升格成“突破”，Books 只补下文列出的具体边界。

## 逐项证据与 Books 最小缺口

### 1. Rho — 2609.38164v1

身份：[abs/v1](https://arxiv.org/abs/2609.38164v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.38164v1)。

- 方法位置：§6.1–6.2；§7.3 控制 midtraining 初始化；§7.6 corrective adaptation；Limitations。支持的链是先用 embodiment 数据学习该硬件的共性，再做 task adaptation；在线 corrective variant 冻结 backbone/action generator，仅学 observation-conditioned latent initialization。反演修正 action 得到 latent target 的 FlowDAgger 是复用机制，不应写成 Rho 首创。
- 评价身份：MetaWorld 六任务，每任务 50 个 scripted correction episodes 后 100 rollouts；实机 FR3 Duo 两任务先有 150 offline demonstrations，再以 15 次人工纠正适配十个已知难配置，每任务 30 trials。作者 test-tube/plug 成功次数为 9→21、20→28（分母均 30）。这些结果支持已知失败区域的低数据适配，不证明未见配置或任意机器人 OOD；语言 steerability 未系统评测，冻结 generator 仍限制可达行为。
- Books 检查：[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已有持续反馈、latent control 与 VLA 训练/适配背景（正文约 L465 附近）；现有正文未找到这条“hardware 共性 midtraining→任务微调→冻结 generator latent repair”的接口链。建议仅补三层数据/更新 owner 与冻结支持域边界，不复制模型排行。主 owner 保持 Ch26，无结构候选。

### 2. HelixWorld — 2609.38123v1

身份：[abs/v1](https://arxiv.org/abs/2609.38123v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.38123v1)。

- 方法位置：§2，§3.1–3.2。metric camera 经 PRoPE 约束视觉，cross-modal 路径把控制传播到 stereo audio；streaming student 在自身中间状态查询 frozen teacher PF-ODE endpoint，以 trajectory loss 纠正 rollout drift，与 DMD 随机择一而非无条件相加。
- 评价位置：§4 HelixBench 的 1,015 筛选 clips、§5.1/Table 4 的 matched-video redub 对照、§5.2 与 Appendix D.7 的速度口径。24 FPS/单 H800、768×512 的稳态 RTF 0.77 包含 decode，但计时两次 warmup 后取两次 run 中位数，排除加载/准备/MP4 编码；不是 first-response latency 或并发 SLO。空间 stereo cue 指标不是完整声学物理；同步指标也非全项优于 teacher，不应复述“普遍 drift-free”。
- Books 检查：[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) L910–916 附近已覆盖 silent camera world model 的状态/实时蒸馏。最小缺口是“同一 camera/world state 的视觉与空间音频联合条件，以及 student-state 纠偏的 streaming 质量/时延口径”，不是再开视听世界模型章；representation 可消费 Ch23，机制归 Ch25。

### 3. Honeycomb — 2609.37690v1

身份：[abs/v1](https://arxiv.org/abs/2609.37690v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.37690v1)。

- 方法位置：§3.2–3.5。六 spatial/spatiotemporal planes 固定张量形状；范围扩张时把旧 feature/confidence warp 到新 bounds，confidence-weighted pooling 加 residual 写入，仅处理最新 chunk。范围扩大而格点不增会降低空间/时间分辨率；“constant size”只指 feature storage，不应扩大为整个生成器、几何辅助状态或系统总内存恒定。
- 评价身份：§4/Table 2–4，Wan2.2 5B、RealEstate10K+ViPE/DA3、H200、33 帧 704×1280 chunks、40 UniPC steps；100 条 RE10K 与 100 个 loop scenes 等作者测试。复访 PSNR 与 memory/update 对照支持固定 feature-plane 的质量/写入成本取舍；基线使用各自默认设置，未匹配全部训练 recipe，也不证明物理状态保持。memory resolution 降低虽省空间，仍须单独验收分辨率损失。
- Books 检查：[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) persistent-state 部分（L313 附近）已有历史压缩、稀疏 memory 和 revisit 约束；缺固定 tensor 在 expanding bounds 下 coarsen 的机制/代价。建议补“表示容量恒定≠信息精度恒定；writer 只更新新 chunk”的最小链及定位/深度错误 fallback。

### 4. Delta-Matching — 2609.37852v1

身份：[abs/v1](https://arxiv.org/abs/2609.37852v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.37852v1)。

- 方法位置：§3.1–3.4/Eq.2、Eq.4。forward 保存的 output-derived delta 与 backward 量化 dP 不一致，产生 stale delta；用当前 `sum(P*dP_hat)` 重算匹配 delta，恢复 softmax 梯度 zero-row-sum。证明要求归一化 P、前后相同 V 与 stated rounding 假设；恢复的是 dS 再量化前的 FP32 不变量，不消灭其后 FP8 rounding、全部梯度误差或保证任意 optimizer 收敛。
- 评价身份：§4，主实验 1.67B GDN/GQA、30B Nemotron-CC tokens、8K context、两初始化种子，并测 569M/5.29B 和指定架构/64K extension；小模型短训练可掩盖 stale-delta degradation。Appendix A.4 的速度只计 attention kernel，排除输入 quantization/autograd wrapper，不能当端到端训练或分布式吞吐；“native FP8”指 attention-core GEMM operands，不是所有算子/状态均 8-bit。
- Books 检查：[Ch28](../../../../../books/part-04-training-system/28-pretraining.md) L900–935 已有 FP4 scale/view identity、rounding 与无偏 estimator 不等于有限 horizon 稳定。缺口是跨 forward/backward 的 contraction identity 与零行和检查。建议补这一可计算 invariant、为何旧 saved-delta 在 BF16 合理而量化后失配、重算代价与 BF16 fallback；不以 kernel 数字证明免费训练。

### 5. SOMA — 2609.37899v1

身份：[abs/v1](https://arxiv.org/abs/2609.37899v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.37899v1)。web 页面读取多入口报 Internal Error 后，仅用同一官方 exact-v1 HTML 的直接 HTTP 入口取得 200 正文，并读 §3–9；已恢复，不标访问隔离，也不改用未知镜像。

- 方法位置：§3–5/Eq.3–4。byte-LSTM experts 按 TF-IDF/SVD 数据簇独立 SPSA；冻结 shared embedding/decoder 与 router，top-k 合并；seed decoder 有 exact delta-rule，不能称全模型纯 ZO。固定 C3 可分 loss、等大 blocks、非零 gradient、小扰动与 dense Rademacher 下，独立 loss 约 1/N relative variance；实际 sparse probes 的收益靠实验，非任意耦合 Transformer 保证。
- 评价身份：§6–9，8.44M/约 150 aggregate GPU-hours 的 byte-LSTM controls；固定初始权重/data/probes/compute、N=4 独立 vs summed loss，三 seeds 的 1,000 updates 对照隔离 cross-expert noise。大 N 的 top-4 推理收益以更大 aggregate training compute 为代价；多数 scale runs 单 seed，范围小且未验证 Transformer。独立专家放弃跨域 jointly learned representation，这不是 ZeRO optimizer-state partition。
- Books 检查：[Ch28](../../../../../books/part-04-training-system/28-pretraining.md) L297 附近已有 zero-order fine-tuning 的 paired forward 估计，未覆盖 objective separability→扰动维度/噪声→表征耦合损失。主 owner 为 Ch28；Ch36 只交叉引用“无 exchange 以独立目标为条件”，不得另写通用通信优化链。

### 6. ToolFence — 2609.37196v1

身份：[abs/v1](https://arxiv.org/abs/2609.37196v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.37196v1)。

- 方法位置：§3.1–3.5。在 untrusted observations 前编译 typed blueprint；deterministic monitor 验 tool/effect/binding/provenance，遗漏时 judge 批准 capability shape，当前参数再核。跨 session 只 cache shape，不 cache 参数值/证据；occurrence-based provenance tracing 是启发式，不是语义意图证明。
- 评价身份：§4 AgentDojo 的 629 task-attack pairs（524 cross-tool、85 within-tool、20 ambiguous）、六攻击方法与三指定 backbone；Qwen3-max ASR 约 0.20%，clean utility 损失 3.80pp。速度来自 50 clean tasks+200 attacked pairs，不是 production SLO。§4.4 保留失败：攻击者在相同 allowed shape 的合法候选列表中诱导选择，授权仍可能通过；模糊 URL/data-flow 会误拒，judge 也非形式安全 oracle。
- Books 检查：[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) L1424 附近 Permission Graph/deterministic Authorizer 与 L525/L708 source authority/reference monitor 已有骨架。最小缺口为“shape grant 与 concrete-value provenance 分离；cache 权限不等于 cache 证据；合法候选内恶意选择不由授权解决”。安全 verdict 归 Ch72，Ch78 tool protocol 只引用，不复制 owner。

### 7. WUSH-KV — 2609.38121v1

身份：[abs/v1](https://arxiv.org/abs/2609.38121v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.38121v1)。

- 方法位置：§4.2–4.4/Eq.4–5：K 用 post-RoPE cache Gram 与 query consumer Hessian，V 用 output-projection Hessian；general invertible K/Q paired transform 保持 dot product，V 可折入权重而 K 需在线 dense transform。near-optimal 证明仅对 QuEST/stated noise/clipping 条件，不覆盖实际 OSCAR-style affine quantizer。
- 评价身份：§5.2 Qwen3-8B、128×32,768 FineWeb-Edu 校准、YaRN×4、WikiText-2 2,048 chunks、sink/keep/flush=16/128/16；§5.3 的 SGLang 两位 cache 指定 Qwen 模型、三 seeds，窗口改为 64/256/8。Appendix D.2：matched-size OSCAR recalibration 控制并未改善基线，但主要下游对照仍用不同 calibration data；局部 L2 误差也未预测 autoregressive 质量。32B 非全任务获胜，MRCR 明显低于 BF16；无 throughput/SLO 证据，Hadamard 对照不等于完整 TurboQuant codec。
- Books 检查：[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) L1021 已有 transform/bit-allocation artifact，L1058 已有循环量化、Hadamard/scale 与 precision fallback。未解释 K/query 与 V/output 的不同 consumer metric、post-RoPE 折叠边界，以及 reconstruction vs decode-quality 的反例。建议只补这三点，不写“2-bit 无损且加速”。

### 8. AdviSD — 2609.38142v1

身份：[abs/v1](https://arxiv.org/abs/2609.38142v1)；正文：[exact-v1 HTML](https://arxiv.org/html/2609.38142v1)。

- 方法位置：§4–5。shared-parameter theorem 在 fixed teachers/stationary retention 条件下解释无效 correction 干扰；predictive contrast 比较 advisor 对同一 recorded executor response 的 with/without advice likelihood，不做 executor counterfactual rollout，也不是 advice 的因果贡献。reflection gate 后用 donor-advice 校准选择，保留 abstention；GRPO 原 outcome advantages 不变，选中决策加 self-distillation。
- 评价身份：§7/Appendix E，Qwen3-8B advisor+冻结 Gemini 3.7 Flash/Claude Sonnet 4.6，BFCL-v3/EnvScaler，三 training seeds、validation-selected checkpoint 各四 test evaluations；matched-count random control 说明选择内容不只减少次数。跨 executor transfer 仍弱于专门训练的配置；Claude ACEBench multi-step 可弱于纯 GRPO。理论不证明 changing-teacher GRPO–AdamW 收敛，API 模型更新限制复现。
- Books 检查：[Ch33](../../../../../books/part-04-training-system/33-grpo.md) L932/L985 已有 token selection、teacher/base divergence 的 distillation gate；缺外部冻结 executor 对 advisor correction 的敏感性与 predictive-not-causal 边界。建议接到 joint outcome/self-distillation 的选择门，不新建训练算法排行；Ch29 拥有通用 distillation objective，Ch80 只消费 reflection 信号。

### 9. Mnemon — 2609.36059v1

身份：[abs/v1](https://arxiv.org/abs/2609.36059v1)；[exact-v1 HTML](https://arxiv.org/html/2609.36059v1) 入口不稳定，实际读取[官方 HTML](https://arxiv.org/html/2609.36059)，页头明确 `arXiv:2609.36059v1`，不是混入后续版本。

- 方法位置：§3/Eq.1–3、§4、§5。raw records 是证据，background index 只指回原记录；planner 负责开放搜索/needs，Jev 批量判 typed propositions，rules 固定 pool/round/View。规则只读 ordering 与 1/2 threshold，校准不变性需 strictly increasing map 且固定 1/2，不能推广到不同 ranking/decision。预算界定 token/model critical work，不使 search 随历史不增长。
- 评价身份：§6.1–6.7，gpt-4.1-mini 2025-04-14/temperature 0、Jev 1.13、LoCoMo 1,540 原标签非 adversarial questions、LongMemEval-S 500；与 OmniMemEval 有 grader 差异，不把 published-claim Table3 排成统一系统胜负。ECI 只含错误修复假设+answer context，排除 read/write；小 answer context 也由 Jev 更广扫描换来。HaluMem/BEAM 并不领先，当前搜索对全部 records 评分，长史搜索延迟增长。
- Books 检查：[Ch77](../../../../../books/part-07-agent/77-memory.md) 已有“从 Write-time Summary 转向 Query-conditioned Late Construction”、raw authority/consolidation 的 L1490–1550，以及 learned selector 与预算 trade-off。不能把“raw history+late construction”本身算未覆盖。仅补可替换判定器的 decision/rank contract、sequential waves vs total judgments、ECI vs lifecycle cost 三点；若作者已有等价细节则 `No Change`，而不是追加 Mnemon 简介。

## 作者接入时的门与范围

1. 九项可准入，不等于九项必须全部写 Books。上述均为对当前相关正文的具体覆盖/缺口建议；作者开始 Books 写回仍须按 AGENTS 重新载入完整 Books 上下文、协调共享 owner。
2. 优先保持最小稳定链：Delta-Matching 的 numerical invariant；Honeycomb 的 constant-storage/coarsening；SOMA 的 separability boundary；ToolFence 的 authority-shape/current-evidence boundary。其余也不能以优先级为由跳过证据或关闭贡献。
3. 任何报告数字必须保留本文列出的 exact-v1、模型/任务、主要条件与评价对象。缺少真实 hardware/concurrency/SLO 时明确 `Not Disclosed`，不补造生产吞吐。
4. 当前独立复核结论：九线索的标题/摘要贡献校准、版本与本期公告核对、相应深度证据位置及最小 Books owner 路由已完成；整个报告最终独立验收尚未执行。

## 后续明确授权的实际 Books 整合

父任务纠正标题预判后的路径，以 ROADMAP 为准，授予本 reviewer 下列文件 ownership。没有改 owner、扩结构、学习状态或研究完成数。

| 家族 | 实际写入位置（source-family 标记） | 本轮状态 |
| --- | --- | --- |
| Honeycomb | Ch25 persistent world state 的固定 planes / expanding bounds / coarsening | 已最小写入；父任务非作者写后待验 |
| HelixWorld | Ch25 可控视频 world model 边界之后的联合 camera/stereo 与 student-state correction | 已最小写入；父任务非作者写后待验 |
| Rho | Ch26 多源数据对齐之后、语义与动作保持之前的 midtraining/latent repair | 已最小写入；父任务非作者写后待验 |
| Delta-Matching | Ch28 attention backward 的 zero-row-sum 不变量之后 | 已最小写入；父任务非作者写后待验 |
| SOMA | Ch28 不保留反向图的零阶更新之后 | 已最小写入；父任务非作者写后待验 |
| ToolFence | Ch72 Permission Graph/deterministic authorizer 之后 | 已最小写入；父任务非作者写后待验 |

WUSH Ch45 交独立 infra reviewer；AdviSD Ch33、Mnemon Ch77 交另一 evidence reviewer处理。本 reviewer未写这些共享文件。Mnemon 的 generic raw/late-construction 已有覆盖结论不变。每处正文保持旧方案成立条件、机制 owner、代价/failure/fallback 和精确来源，未直接照录作者排行榜或加速宣传；Review notes 标明未复现/待写后核。

## 后续限定委派：其余九项及 ER-JEPA 的最终处置

本节复核者仍为 `sep30_complement_review`，不是 Daily 作者，且未写以下 Books 段落。仅复用同窗已读题摘与精确 v1 必要正文，不扩大来源/附件审阅，不改 Books。原 NoPE、STEPQuant、evalstats 三项由另一非作者核，不重复认证。九项的源证据与作者记录见 [ROOT_EVIDENCE_NOTES](./ROOT_EVIDENCE_NOTES.md)，本节补充实际采用和写后结果；作者记录不代替本次已执行的阅读。

| 家族（精确 v1） | Design Delta / System Reach / Durability | 必要证据与实际采用边界 | 最终 Books 处置 / 写后结果 |
| --- | --- | --- | --- |
| [OLIVE 2609.36246v1](https://arxiv.org/html/2609.36246v1) | 2/2/2 = 6 | §2–3、§4.1–4.3、§5：student 新前缀后，teacher 沿自己的后续选择生成有界 suffix；CE 只监督 teacher tokens。主配方的 partial/unfiltered continuation 与 §5.1 full/verified 实验不能互换；不可恢复前缀、depth=3 update lag、top-16 近似 OPD 及独立 API 配置保留。 | 整合 `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)“Teacher Text Continuation 可以免去 Logit 接口，但不能免去状态与成本”。实际两段把 occupancy 与监督边界分开，保留调用成本和旧路径；本 reviewer 已读实际段落及邻接，通过。该段作者为 sep30_evidence_check，不是本 reviewer。 |
| [Intrinsic self-correction 2609.35832v1](https://arxiv.org/pdf/2609.35832v1) | 2/1/2 = 5 | §2–4：KEEP/CHANGE 应用后的最终答案、invalid denominator、条件 recovery/harm 与两种 unconditional baselines；pre-revision gate 不等 post-generation acceptance。82-setting/gate summaries 缺 frozen configs 或 matched IDs，不能作为独立无偏收益。 | 已有覆盖 `AGENT-REFLECTION` / [Ch80](../../../../../books/part-07-agent/80-reflection.md)“Stopping Policy”：约 L195–209 的 `(1-A)ECR-A EIR`、verify-first/预算，以及后续 cheap sensor→selective critic 已实际承载论点；No Change 通过。 |
| [ATTUNER 2609.36722v1](https://arxiv.org/html/2609.36722v1) | 2/2/2 = 6 | §3.1–4、§5.1–5.3：relevant-only multi-artifact 仍有损失，不能只归因选择；oracle 用 full attention rows 和 hybrid online values，是恢复路径而非 values 普遍无损证明。query LoRA 保留 artifact KV，但在线 hidden/new KV 演进；warm-cache TTFT 不含离线构造。 | 整合 `INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“固定缓存 Producer，适配读取它的 Consumer”。原插入误落 Eviction 标题下已移成独立小节；实际边界、代价/完整 Prefill 回退与邻接复读通过。 |
| [Hidden dates 2609.36931v1](https://arxiv.org/html/2609.36931v1) | 2/1/2 = 5 | controlled 2024-date sweep 改变确定性输入，不是相同 prompt 的随机噪声；§5.2 proprietary week trace 是观察性证据，不能独立证明服务端注入日期的因果效应；§5.5 不支持日期总比其他变量强。 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“数值可复算不等于复现了同一个实验”约 L255 的 prompt/render hash→resolved model/call receipt，及 Response Rate 段的 access path/system prompt identity；No Change 通过。 |
| [Correct, Don't Delete 2609.37624v1](https://arxiv.org/html/2609.37624v1) | 2/1/2 = 5 | §3.2–3.4、§4–5、Appendix C/D：固定 nested rows、seed-paired contrasts、conditional coherent-output EM；unresolved 不等无效。post-poison assistant-loss tokens 近似匹配，不等 total-token/wall-clock 匹配；三 judge 与不完全修复不能支持普遍安全。 | 整合 `TRAIN-DATA` / [Ch27](../../../../../books/part-04-training-system/27-data.md)“从删除坏监督到尝试纠正监督”。原“删除正面示范”错误已改为移除该输入监督机会、纠正提供正面目标；本次实际复读修复句、两段及前后代码质量/synthetic data 交接，通过。 |
| [Attention retrieval capacity 2609.37879v1](https://arxiv.org/html/2609.37879v1) | 2/1/3 = 6 | §2、§3.1–3.4、§4：原权重删除与 renorm 分别产生 `(1-m)mu_T` 与 `(1-m)(mu_T-mu_S)`；NLL tolerance 测干预下保行为支持，不测存储事实数。useful set 未直接观测，geometry 不是一般 loss predictor；dense-before-selection 不证明加速。 | 整合 `MODEL-SELF-ATTENTION` / [Ch14](../../../../../books/part-02-model/14-self-attention.md)“路由权重不等于独立的知识贡献”。误置在三 token 例子内已改独立小节；实际公式、Value 尺度/方向与非加速边界及邻接复读通过。 |
| [SchurReplay 2609.36654v1](https://arxiv.org/html/2609.36654v1) | 2/2/2 = 6 | §4.1–4.2、§5.1–5.3：continuous-future Schur surrogate 与 recurrence-exact E2M1 replay 分开；各候选私有同入口状态、winner-only commit，不交换依赖列。old scale 仅保证局部 surrogate 不增，不保证任务单调；七任务是 15,461 questions，不是 154,617。 | 整合 `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“未来补偿能力决定当前舍入的代价”。原误置 bit-budget 标题下已修；实际连续子问题假设、私有轨迹/提交与预算/质量回退复读通过。正文未采用速度数字。 |
| [AnswerPool 2609.37494v1](https://arxiv.org/html/2609.37494v1) | 2/1/2 = 5 | §3.1–3.2/3.4、§4.3/4.6、§5：一对一 assignment 使题目耦合，random joint chance 不等原独立 MCQ；unique valid 和非共享 correct option 是前提，LLM ambiguity screen 不是 oracle。equal-size unrelated control 不证明任意长池无混杂；不采用缺答案变体。 | 整合 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)多选 evaluator 后的 coupled-pool 两段。实际“各题唯一有效且不同题不共用正确 option”修复已读，任务改变/原 MCQ 保留与邻接通过；最终此句亦由 sep30_evidence_check 独立写后确认。 |
| [ParaAnya 2609.36522v1](https://arxiv.org/html/2609.36522v1) | 2/2/2 = 6 | §2–4：同 timestep 跨 PinT 迭代缓存输入/输出 pair，仅 miss 更新；τcache 不等 solver τ，保更新公式不等 exact trajectory。SD1.5/COCO 的同资源缓存控制与 8-GPU 对 1-GPU 不能混合；低阈值省 NFE 仍较慢的 sweep 属 H100，主对照属 V100。 | 整合 `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“同一 Timestep 的跨迭代缓存是一条近似执行分支”。误置 Microscaling 标题下已修；实际近似/identity、hit/通信成本及质量/未缓存回退复读通过。 |

6 分整合项，以及 5 分而发现明确 Books 差异的 Correct/AnswerPool，只对拟采用的机制/控制/限制加深阅读，未为产生 diff 升分。最终采用没有把作者 benchmark 转成生产、全模型最优、安全或端到端 SLO 保证。

### ER-JEPA：代表性排除纠错后保留为标准候选

[ER-JEPA 2609.36952v1](https://arxiv.org/html/2609.36952v1)，Design Delta / System Reach / Durability 为 **2/1/2 = 5，标准完成**。作者将其加入第 42 家族；本 reviewer 未独立统计其他 41 家族，不用这个序号证明整日冻结分母。

原“成熟 replay 组合/小模型”关闭理由不能保留：§2.2/Eq5–6 用当前模型重算所存 raw source/target token pairs，加入 target CE 与 cosine JEPA；§3.2–3.3 的 SYNTH/Llama-3.2-1B、六个 40.05–240.31 PFLOPs 预算及五 seeds，加 token-matched 和同 replay loss 的 current-batch 控制，支持历史样本内容的局部独立作用。§3.3 在相同 2,000 测试样本上分 correction 与 retention；§5 保留 paired-view、β grid-search 的训练成本，推理移除 episodic path 不等于训练免费。Reach=1 针对同一训练图中历史/当前目标的局部改变，不借用 Agent memory 或 World Model 名称抬分。

最终 **已有覆盖 / Books No Change：`TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)**。实际对读约 L226–228 的 latent alignment/CKA/cosine≠held-out 行为；“Catastrophic forgetting 与能力回退”和“早期回退还要区分暂态欠优化与持续遗忘”中的 acquisition/retention/连续 checkpoints；“Replay Ratio 从固定超参数演进为可迁移 Controller”中的历史 replay/配方身份、搜索成本与双域 holdout。这些正文实际承载拟保留的稳定机制和验证边界。论文提供受限 JEPA 新验证/识别控制，值得作为候选保留，但不产生新的长期职责或机制缺口；不为它追加 JEPA 名称综述，不路由到 Ch25。

### 日期和身份修复范围

本 reviewer 已在无 query 的 [官方 cs.CL/new](https://arxiv.org/list/cs.CL/new) 上确认 `Wednesday, 30 September 2026`、New submissions 145：self-correction 为第22项、AnswerPool 第103项、ER-JEPA 第80项。带 query 的缓存别名曾返回 Sep28 列表，不用它认定窗外；替代官方入口恢复后关闭该访问问题，不保留伪受阻。沿用上文官方公告日程推定，不用 submitted 代替公开，不声称全网最早时刻已穷尽证明。

### 写后复核权限与本阶段结论

本批九项最终处置为七项实际整合、两项已有覆盖；ER-JEPA 另为准入后已有覆盖。上述由本 reviewer 实际只读核验或记录明确的另一非作者修复核，未自验本 reviewer 早前写入的 Honeycomb/Helix/Rho/Delta-Matching/SOMA/ToolFence 六项。这六项由 root 非作者验收，结果归 [ROOT_EVIDENCE_NOTES](./ROOT_EVIDENCE_NOTES.md) 的实际写后记录；原“待验”表是当时阶段快照，不是当前终态。

当前没有本批尚可执行的源证据/Books 写后待办；最终 Daily 尚待作者提供正式 Report，本文件此刻不签整日 Coverage/Evidence/Books Gate，不替代完整报告独立验收。未复现实验、未修改 Books/索引、未 stage/commit/push。

## 正式 Report 最终限定复核

复核者：`sep30_complement_review`，不是 [正式 Daily](../../30/README.md) 作者 root。结论：**本次委派范围通过**。本节覆盖上文其余九项及 ER-JEPA 的最终候选行、证据摘要、评分、具体 Books 处置与已执行写后结果；不重新抓源或扩大附件阅读，不自验本 reviewer 写入的六项 Books。六项的非作者验收仍由 root 负责。

- 九项仍为七项整合、两项已有覆盖，ER-JEPA 另为 5 分标准完成、Ch29 已有覆盖。七项实际正文及邻接已经非作者读后确认；Ch27 本次再次实际只读确认“删除移除该输入监督机会，纠正提供正面目标”，没有把删除说成移除已有正面示范。OLIVE 的 Books 写入者是 `sep30_evidence_check`，本 reviewer 是非作者写后复核者。
- 两处 Report 修复已实际复读确认：self-correction 的两组可恢复材料明确为 GSM8K 初答/修订文件，gate 汇总仍缺对应 paired records、冻结配置和不相交 IDs；hidden-date 九模型六数据集的主控制定位为 §3–4，§5.5 仅受限 precision/batch 对照。二者没有据此扩大因果或无偏收益断言。
- 候选表逐行计数为 42 家族、37 深入完成、5 标准完成；Books 标签为 37 整合、3 已有覆盖、2 仅报告，与结论统计一致。这是表内一致性复核，不是用数字替代其他 32 家族的源证据验证。5 项标准对应 self-correction、hidden-date、ER-JEPA、MultiTalk、SYNTH；本批低分整合项 Correct/AnswerPool 保持 5 分，因已确认的具体知识缺口而深入，不为产出 diff 升分。
- 本批证据与处置无尚可执行修复点。整个 Daily 的来源覆盖、其他候选审阅、机械校验和最终完成状态由各非作者结果汇总验收；本限定结论不单独签整日 Coverage/Evidence/Books Gate，不把终态外部保留项当作覆盖通过或全网无遗漏。

本轮仅追加本文件。未修改 Books、Report 或索引，未复现实验，未 stage、commit 或 push。
