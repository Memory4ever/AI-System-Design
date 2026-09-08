# Daily Research — 2026-08-07

**规范：** V3
**窗口：** 2026-08-06T09:00:00+08:00 ～ 2026-08-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:30:00+08:00

## 1. 结论

本窗从 arXiv Friday 公告的 539 个宽身份中，经逐项题摘语义筛选和独立漏项复核保留 16 个 Source Family。它们不是“一天有 539 篇影响项目”的结论：大量领域应用、局部 benchmark 或已有方法组合已在题摘阶段关闭；新增项集中在 judge information flow、skill supply chain、procedural compression、world-model 物理证据与 harness optimization evaluation。

16 项均取得 v1 原文且未见 withdrawal。PLoRA 与 anytime-valid stopping 已有 Books 覆盖；Activity Frames 因单用户证据只保留报告；TensorCast 仍为结构候选；其余 12 项完成正文整合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 按本窗及相邻日期检查，无符合范围的新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 相邻研究日期为 Jul28 与 Aug10 | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) Aug05 条目已在真实归属日关闭，本窗无新增 | 已检查 | 无 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) Aug05 Muse 已在真实归属日处理，本窗无新增 | 已检查 | 无 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 按日期检查，本窗无相关正文 | 已检查 | 无 |
| SRC-DEEPSEEK | [Research](https://www.deepseek.com/) 与公开更新按日期检查，本窗无新机制正文 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [GitHub](https://github.com/MoonshotAI) 按发布时间检查，本窗无相关研究事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research) 中 Jul21 后下一条为 Aug11 | 已检查 | 无 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 中 Jun16 后下一条为 Aug14 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) 最近相关条目为 Aug05，早于本窗 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 按日期检查，最近记录早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) 论文与博客按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 相邻研究记录不落窗 | 已检查 | 无 |
| SRC-ARXIV | Friday 08:00 北京时间公告；539 个宽身份作发现索引，逐项题摘语义筛选和独立漏项复核后保留 16 项并重开 v1 原文 | 已检查 | 无 |

本窗未触发额外按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Scaffold-Mediated Post-Training](https://arxiv.org/html/2608.05156v1) | 2026-08-07T08:00:00+08:00 | 让 procedural scaffold graph 与参数通过 discovery、distillation、recompilation 共同演进，改变 post-training artifact identity；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [QEvict](https://arxiv.org/html/2608.05326v1) | 2026-08-07T08:00:00+08:00 | 将 KV eviction 从不可逆删除改为 full/quantized/deleted 三层状态，并允许随 query drift 恢复；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Evidence Lock Before Commitment](https://arxiv.org/html/2608.05353v1) | 2026-08-07T08:00:00+08:00 | 受控证明把持久 evidence record 变成 judge 唯一输入会丢失 source information，审计接口不能替代原始答案；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DBLast](https://arxiv.org/html/2608.05448v1) | 2026-08-07T08:00:00+08:00 | 修正 block drafter 在 stochastic decoding 下错误的跨位置条件独立假设，并以 acceptance-oriented objective 训练；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [PLoRA](https://arxiv.org/html/2608.05483v1) | 2026-08-07T08:00:00+08:00 | 用 CXL/NVLink pooled memory 与 near-data reduction 改写千 adapter serving 的容量/链路边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Trajectory Poisoning in Self-Evolving Skills](https://arxiv.org/html/2608.05563v1) | 2026-08-07T08:00:00+08:00 | 揭示不可信 trajectory 经 attribution/promotion 变成持久 instruction 的 supply-chain 边界；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillZip](https://arxiv.org/pdf/2608.05604v1) | 2026-08-07T08:00:00+08:00 | 将 skill 文本压缩改为保留接口、依赖闭包、verifier 可达性和可展开 source 的 procedural graph compression；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [DreamGuard](https://arxiv.org/html/2608.05695v1) | 2026-08-07T08:00:00+08:00 | 从逐 action 反应式 guard 演进为预测 trajectory prefix risk 的 recurrent world-state guardrail；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [In-Context VLA](https://arxiv.org/html/2608.05738v1) | 2026-08-07T08:00:00+08:00 | 以分析与实验显示生成式 CoT 会破坏低层控制，提出“消费 grounded language、只监督 action”的替代分支；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Activity Frames](https://arxiv.org/html/2608.05784v1) | 2026-08-07T08:00:00+08:00 | 将屏幕活动确定性编译为带 evidence pointer 的 typed episodes，提供可审计 Agent memory/replay 分支；2 + 2 + 2 = 6 | 标准完成 | 仅报告：核心效果来自单用户语料，尚不足以改变通用 memory 设计结论 |
| [Runtime Observability for Heterogeneous Attention Memory](https://arxiv.org/html/2608.05863v1) | 2026-08-07T08:00:00+08:00 | 用 typed error metric 与 weakest-tier composition 统一 KV、latent、sparse selector、recurrent state 的运行时风险账本；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MONITORING [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [AppDeltaWorld](https://arxiv.org/html/2608.05891v1) | 2026-08-07T08:00:00+08:00 | 将 GUI world prediction 从自由图像生成改成 action-transition 约束的 executable delta code，并用于闭环训练；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [GAUGE](https://arxiv.org/html/2608.05948v1) | 2026-08-07T08:00:00+08:00 | 用现实轨迹、物理参数和不确定度将 world-model 评测从观感推进到定律与参数误差；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TensorCast](https://arxiv.org/html/2608.06007v1) | 2026-08-07T08:00:00+08:00 | 把 weight、KV、checkpoint 与路由共享状态抽象为统一 tensor lifecycle/control layer，挑战按单引擎内嵌管理的结构；3 + 3 + 3 = 9 | 深入完成 | 结构候选：现有节点分别拥有各类状态，没有跨生命周期 tensor-management owner |
| [HarnessOpt-Bench](https://arxiv.org/html/2608.06301v1) | 2026-08-07T08:00:00+08:00 | 将 harness optimization 固定为 seed、预算、不可见 test partition、候选版本与受信执行环境的能力评测；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AV-AIVAT](https://arxiv.org/html/2608.06362v1) | 2026-08-07T08:00:00+08:00 | 以 anytime-valid confidence sequence 和 predictable correction 在未知样本量下安全停止交互评测；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Evidence Lock Before Commitment](https://arxiv.org/html/2608.05353v1)

论文比较 standard pairwise、单次 structured judging、两次 evidence lock 与三次 pointwise lock；24,000 次判断中，后两者降低人类偏好一致性并增加顺序敏感。该结果不证明显式 evidence 无用，而是证明自然语言摘要不能成为 final judge 的唯一信息源。Ch66 应保留 source answers 与 evidence record 的双通道：record 负责审计，最终决定仍可读取原始材料。

### [Scaffold-Mediated Post-Training](https://arxiv.org/html/2608.05156v1)

§3 将 scaffold graph 置于 discovery、augmented data generation、progressive distillation 与 dynamic recompilation 循环；FeatureBench 结果只支持作者 task/scaffold 体系。拟在 Ch29 SFT 的 demonstration provenance 后加入：外部 scaffold 既是 rollout policy 也是训练数据生成器，必须与 base model、tool contract 和 compiler revision 共同版本化；distillation 后无 scaffold 的能力不证明策略已完整内化。

### [QEvict](https://arxiv.org/html/2608.05326v1)

§3 用 Future Missed Mass 与 Global LIR 显示被逐出的 window 会因 query 演进重新重要；§4 的三层 cache 允许 quantized window 晋升回 full precision，只对最低置信区间永久删除。实验不证明 attention score 等于语义重要性。拟在 Ch45 eviction 演进中加入 recoverable state：低把握时先降精度而非删除，promotion 需计入 dequantization latency 与 bandwidth，预算紧或 risk 超界时回退 FullKV/更保守 eviction。

### [DBLast](https://arxiv.org/html/2608.05448v1)

§3 以 low-rank latent mixture 建模 block positions 依赖，并用 expected verified length 导向训练；§4 显示 target sampling entropy 上升时独立 block draft 接受长度下降。该结果限 Qwen3-4B/8B 与披露任务，不证明非贪心总更快。拟在 Ch48 block drafting 段加入：exact verifier 保留分布提交权，但 drafter 的 factorization 必须匹配 stochastic target 的多模态 continuation；吞吐收益仍需包含 draft cost、batch 与 entropy。

### [PLoRA](https://arxiv.org/html/2608.05483v1)

§III 解释 PCIe+CPU staging 的容量与 kernel-stop 压力，后续设计把 adapter/KV 放入 pooled memory 并近数据归约；H100 与硬件校准 simulation 的 6.6× 不等于现成 CXL 生产测量。Ch54 已承载 pooled state、NDP、cache policy 与链路饱和边界。

### [Trajectory Poisoning in Self-Evolving Skills](https://arxiv.org/html/2608.05563v1)

攻击者不能直接改 skill bank，只通过少量看似有用、重复且能被归因的 trajectory，使 evolver 将行为晋升为持久 instruction；真实 provenance 因此不等于可信 provenance。实验用 inert canary 证明 artifact poisoning，不证明真实破坏执行。Ch72 应把 experience-to-skill promotion 视为供应链发布：需要独立 evidence、跨 trajectory 反事实和 quarantine，不能由同一 evolver 自证。

### [SkillZip](https://arxiv.org/pdf/2608.05604v1)

论文把 whole-skill package 改成带 intent、precondition、operation、verifier、output 与 source pointer 的 section-level graph，只有 boundary signature、dependency closure 与 verifier reachability 保留时才折叠为可逆 macro；ReZip 再按执行证据修订。作者指标不证明压缩后语义绝对等价。Ch77 应把 procedural memory 的压缩单位从文本改成 contract-bearing subgraph，无法证明闭包时回退展开原始 skill。

### [DreamGuard](https://arxiv.org/html/2608.05695v1)

§3 的 recurrent latent state 同时给 immediate hazard 与 prefix risk，融合后在 action 执行前干预；25ms 是作者评测平均值，world model 可能误判或漏掉 OOD 风险。拟在 Ch72 runtime guardrail 段加入：预测状态只提供 risk evidence，不拥有 effect commit；不可逆工具仍由 policy/authorization veto，低置信时 fail closed 或请求人工。

### [In-Context VLA](https://arxiv.org/html/2608.05738v1)

Method 对比生成 free-form CoT 与 grounded evidence consumption：文本 reasoning 会引入 latency、ungrounded narration 和 action/reasoning objective 冲突；替代方案通过 detector/depth/VLM 工具取得结构化证据，只对 action token 监督。拟在 Ch26 high/low controller handoff 中加入：语言是 observation/context，不是必须生成的中间 action；control deadline 紧时生成 CoT 不应进入关键路径。

### [Activity Frames](https://arxiv.org/html/2608.05784v1)

§3 将 capture rows 确定性分段成 typed frame/episode 并保留 raw evidence pointer；结果来自一名专业用户 51 天语料，accuracy 还依赖独立 oracle。它提供可审计编译分支但外部效度不足，暂留日报；后续跨用户/应用复现或与 Ch77 现有 provenance 结论冲突时再重开。

### [Runtime Observability for Heterogeneous Attention Memory](https://arxiv.org/html/2608.05863v1)

§2 定义三种 operator、local contract 与 metric-typed composition；不能转换 metric 时组合无定义，能桥接时整体 tier 继承最弱证据。§3 与请求级 ledger/并发回放支持实现可行，但不证明 risk bound 对最终语义 tight。拟在 Ch67 evidence telemetry 后加入：metric identity 是 type，certified/partial/empirical 不得混加；state identity 和 slot reuse 失败必须 fail closed，而不是用平均误差掩盖。

### [AppDeltaWorld](https://arxiv.org/html/2608.05891v1)

Method 在 action-transition 约束下检索 Level-1 HTML，生成可执行 Level-2 delta code 并浏览器渲染；world-model-in-loop SFT 与 test-time RL 只在移动 GUI benchmark 上验证。拟在 Ch25 controllable world model 段加入：对离散界面，预测 reachable state transition 可比自由像素 rollout 更易验证；真实 app state 仍是 authority，模拟 delta 只能产生 provisional training branch。

### [GAUGE](https://arxiv.org/html/2608.05948v1)

benchmark 用现实轨迹、校准物理 metadata、不确定度和 task-specific observable，分别测碰撞、摩擦、动量、振荡与变形，而不是只看 perceptual similarity。22 个 task family 不能覆盖开放世界物理。Ch66 应让 world-model physical fidelity 同时报告定律形式、参数误差与测量不确定度；视觉一致只能作 surface evidence。

### [TensorCast](https://arxiv.org/html/2608.06007v1)

§2 从 weight loading、KV management、checkpoint synchronization 抽取共同 lifecycle primitives，§3 将 policy 与 data movement/execution 分离，并接入 vLLM/SGLang。作者结果支持抽象可行，不证明通用层总优于专用 fast path。它跨越 TRAIN-CHECKPOINT、INFER-KV-CACHE、INFER-GPU-MEMORY 与 PLATFORM-MODEL-REGISTRY，任何单章都会丢失统一 ownership；建议 root 在全书结构复核中评估“Tensor State Lifecycle”稳定节点，而不是先塞入 Ch49 或 Ch57 杂物段。

### [HarnessOpt-Bench](https://arxiv.org/html/2608.06301v1)

评测把 seed harness、优化预算、可见反馈、候选版本与不可见 test partition 固定在 trusted execution environment 中，避免 optimizer 对 validation 过拟合或越权读 test。111 次运行不证明模型排序普遍成立。Ch66 应把自动优化对象定义为完整 harness artifact，并将搜索期证据与最终 held-out 证据隔离。

### [AV-AIVAT](https://arxiv.org/html/2608.06362v1)

方法用 predictable online value correction 降方差，并以 anytime-valid confidence sequence 保证连续监控下的停止有效；普通置信区间配 optional stopping 不成立。74× 只属于所测不完美信息游戏。Ch66 已包含 sequential evaluation、anytime-valid stopping、stopping metadata 与完整回退，保持已有覆盖。

## 5. 缺口与下一步

无

本窗没有可执行未决或外部材料请求。TensorCast 保持结构候选，待季度结构审计，不阻塞本日报。

## 6. 复核

复核者：独立复核智能体（2026-09-07）
结论：通过

复核纠正 6 项 false negative。以 539 个 official-announcement identity 为分母逐题摘重筛；16 项均复核 exact-v1、withdrawal、评分、证据边界与 owner。2 项已有覆盖真实，1 项仅报告、1 项结构候选均合理，12 项长期机制均位于 canonical owner 的正文区。
