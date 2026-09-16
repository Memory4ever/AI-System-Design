# 2026-05-01 V3 分母重新认证

## 目的与口径

本文件只保存过程证据，不是第二份日报。重新认证严格使用窗口 `2026-04-30 09:00～2026-05-01 09:00 Asia/Shanghai`，并以当前 `RESEARCH_CONTRACT` 的长期贡献准入替代旧 V2.1 分母。`ROADMAP` 只用于解释贡献与定位 owner；能够映射到章节、属于 AI 研究或在作者任务上提高指标，都不自动成为候选。

## 结果

- 窗口身份：556；去重后仍为 556。
- 题目与摘要语义筛选：556/556。
- 旧分母：63；新分母：47。
- 旧候选保留：37；旧候选降级：26；旧关闭项恢复：10。
- 新候选前关闭：509。
- 候选正文访问：47/47；未发现 withdrawn。

509 项关闭按主要理由归并为：局部任务或垂直领域结果 221；受限模型、表示、多模态或 world-model 变体 96；未改变责任边界的 Agent / Security / Workflow 实例 65；未改变训练、推理或执行计划的局部优化 61；单一 benchmark、数据集或评测实现 43；secondary synthesis、AI for Science 暂缓或项目外材料 15；重复、revision 或身份关闭 8。总数只用于审计分母，逐项身份、题目、摘要与旧 family-specific 理由仍保存在 `arxiv-owner-receipt.json` 和 `screening-ledger.json`。

## 从旧候选降级的 26 项

| arXiv ID | 分母前关闭理由 |
| --- | --- |
| 2604.26997 | 将 DID、VC、OPA 与 Kubernetes CRD 组合成 50-agent PoC；未形成新的可迁移 identity、authority 或 production evidence contract。 |
| 2604.27032 | LLM 辅助搜索运行参数的局部启发式；未改变配置搜索、校准或 SLO 的长期控制权。 |
| 2604.27039 | token-level 剩余长度 value 是受限预测头；未改变 serving admission、scheduler authority 或通用 value-training contract。 |
| 2604.27045 | 医疗双流 memory 是垂直领域 reconciliation；FHIR 约束与 26-patient 数据不能外推通用 Agent Memory owner。 |
| 2604.27221 | Web2BigTable 是搜索与表格抽取系统实例；未改变 RAG evidence identity 或 retrieval authority。 |
| 2604.27233 | inference-time feedback 改进 tool-calling 的局部策略；未形成可迁移 effect commit、rollback 或 workflow-state contract。 |
| 2604.27238 | RTL 数据投毒与防御绑定单一生成任务；没有改写通用训练供应链或 artifact admission。 |
| 2604.27249 | adversarial multiple-choice 中的 positional shortcut 是窄评测现象；未形成跨任务 release/evaluation contract。 |
| 2604.27251 | reasoning controllability 的行为观察没有改变 Transformer layer 的结构、状态或执行机制。 |
| 2604.27267 | 机器人威胁建模是 secondary synthesis；没有新的 primary enforcement mechanism。 |
| 2604.27283 | 编码 Agent memory 的 contextual-bandit controller 只在 smoke/proxy 数据上验证；未改变通用 Memory admission 结论。 |
| 2604.27289 | 形式化治理主张依赖论文自定义抽象与运行时；Coq 证明不自动建立真实 AI effect boundary。 |
| 2604.27292 | 结构治理立场与 Rice 定理类比没有给出新的可部署 authority 或 evaluation evidence。 |
| 2604.27309 | EHR Agent evaluation 是医疗领域部署案例；未改变跨领域 evaluation identity。 |
| 2604.27351 | 科学 foundation model 协作属于当前明确暂缓的 AI for Science 范围。 |
| 2604.27419 | 网站生成 benchmark 绑定单一交互任务；没有改变通用 workflow/action verification contract。 |
| 2604.27488 | Skills-Coach 是 training-free skill 优化实例；作者 task/judge 不能建立通用 skill release gate。 |
| 2604.27660 | context-to-skill 提取是局部模型方法；未建立 durable skill identity、validity 或 safe reuse contract。 |
| 2604.27695 | evidence-gap iterative retrieval 是 memory/RAG 的局部实现；未补全现有 construction/retrieval failure 边界。 |
| 2604.27711 | ExoActor 的视频生成到 humanoid control 绑定特定模拟与物理任务；未改变通用 action authority。 |
| 2604.27776 | WindowsWorld 增加一个 process-centric benchmark；未形成新的跨环境 evaluation authority。 |
| 2604.27781 | AI supply-chain survey 是 secondary synthesis，不作为新机制的 primary evidence。 |
| 2604.27792 | Motubrain 是机器人 world-action model 实例；未改变 persistent state、controller authority 或 sim-to-real contract。 |
| 2604.27906 | schema-aware memory extraction 是受限实现；现有 Memory 章节已覆盖 construction、validation 与 retry 的一般边界。 |
| 2604.28157 | FlashRT 主要优化既有 red-team 攻击的算力与显存；没有改变威胁模型、security authority 或 release gate。 |
| 2604.28158 | 自动科学发现知识图谱属于当前暂缓的 AI for Science 范围，且主要证据为自动抽取图谱本身。 |

## 从旧关闭项恢复的 10 项

| arXiv ID | 恢复理由 |
| --- | --- |
| 2604.26985 | masked diffusion 通过跨 denoising step 的 clean-state self-conditioning 改变可变生成状态。 |
| 2604.27019 | adversarial fine-tuning 会重组 refusal geometry，改变安全表示与 utility 耦合的判断。 |
| 2604.27077 | normalized parameterization 的学习率跨 width/depth/token-horizon transfer 改变 pretraining scaling contract。 |
| 2604.27201 | control token 选择 mode-pure expert path，把 reasoning mode 变成显式 routing state。 |
| 2604.27263 | byte-level controlled simulation 分离 subword 的吞吐收益与 boundary prior。 |
| 2604.28082 | emergent-misalignment persona 的自我报告并不稳定，改变自评证据可用性。 |
| 2604.28118 | transformer component measurement 与 fault-propagation graph 建立诊断证据链。 |
| 2604.28119 | SAE feature 可能以 global/local atom group 表示 concept manifold，限制单方向解释。 |
| 2604.28122 | topology-aligned latent 对视觉几何压缩的可用性提出新的表示约束。 |
| 2604.28192 | VLA RL 把 physical latent reasoning 作为决策变量并与 action reward 联合优化。 |

## 当前 Gate

作者重新认证和正文对读已完成。非作者 fresh-context 复核随后检查 10 个恢复项、26 个降级项、其余关闭项的风险分层样本，以及 21 个 `Integrate` 的真实正文锚点；修复 ZipCCL 来源标记与对应正文错位后，Coverage、Evidence、Books 与独立复核均闭环，日报状态为“完成”。
