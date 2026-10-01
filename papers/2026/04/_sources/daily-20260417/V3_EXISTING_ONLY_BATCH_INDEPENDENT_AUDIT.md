# 2026-04-17 V3：十项 Existing / Only 有限独立复核

## 范围与结论

本轮是非作者的 source→owner 复核，只处理 14228、14362、14414、14572、14612、14683、14419、14434、14717、14732。复用已经实际阅读的当前 AGENTS、研究合同、报告合同与统一 Prompt；重新打开这十项官方 exact-v1 HTML 的必要方法、结果和关键反证，并直接核对 ROADMAP 对应的实际 Books 命题。本文件不修改作者 README、Books 或全局 checkpoint，不重开此前七项复核，不扩展 raw/candidate 分母。

结果：六项可使用 `No Change — Existing Coverage`，四项可使用 `Weekly Only — Context`（本日仅报告）。14228 的 Existing 必须收窄采用范围；14732 需要避免合并两处不同消融的 K 表述。下述 PASS 只指具体证据与处置，不证明整日日期、覆盖、候选分母或整日 Gate 已通过；未复现实验。

| Family 后缀 | 结果 | 最终处置 | 实际 owner |
| --- | --- | --- | --- |
| 14228 | 收窄后 PASS | No Change — Existing Coverage | PLATFORM-SECURITY / AGENT-MCP |
| 14362 | PASS | No Change — Existing Coverage | AGENT-MEMORY |
| 14414 | PASS | No Change — Existing Coverage | PLATFORM-EVALUATION-SYSTEM |
| 14572 | PASS | No Change — Existing Coverage | AGENT-RAG |
| 14612 | PASS | Weekly Only — Context | INFER-SPECULATIVE-DECODING |
| 14683 | PASS | No Change — Existing Coverage | PLATFORM-EVALUATION-SYSTEM |
| 14419 | PASS | Weekly Only — Context | MODEL-MOE |
| 14434 | PASS | No Change — Existing Coverage | MODEL-MOE |
| 14717 | PASS | Weekly Only — Context | AGENT-MEMORY |
| 14732 | 边界澄清后 PASS | Weekly Only — Context | MULTIMODAL-EMBODIED-VLA |

所有项暂定 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 与本批受限结论相容；14228 仍由安全触发必要深入，不因只有 5 分降为摘要审阅。这里不是重新计算整日候选评分账目。

## 逐项证据与实际 Books 比较

### 14228 — Dive into Claude Code

[exact-v1](https://arxiv.org/html/2604.14228v1) §11.3、§16：分析的是 npm 提取的 v2.1.88 静态材料；feature gate、部署启用状态和当前 runtime prevalence 不能由此推出。§11.3 的 pre-trust 初始化漏洞与复杂命令解析 fallback 引用第三方安全报告，而非作者对当前版本的独立运行实验。

采用范围限定为“授权边界须覆盖初始化副作用，不能只有后续调用 gate”。[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)“从文件哈希到可执行来源链”实际要求 deserialize/initialize/operator invocation 分阶段隔离，由独立安全 owner 持有放行；[Ch83](../../../../../books/part-07-agent/83-mcp.md)“Authorization 之前还需要可验证的 Server Admission”实际区分 admission 与 effect-time authorization，并保留 sandbox/只读/拒绝分支。此范围 Existing PASS，交接是可执行 artifact 安全→Host 注册→每次 effect 授权，不是按章节名称判覆盖。

修正：作者 README 的“共享性能预算可能让多层防御共同降级”可作为论文分析线索，但本轮没有找到两章对这一精确命题的独立承载，也没有核验其二手具体案例。不得将它一并写成“本批采用且已有覆盖”，更不得断言当前 Claude 仍有同一 bypass。无需为这一二手线索扩展当前任务或重新公告旧 CVE。

### 14362 — APEX-MEM

[exact-v1](https://arxiv.org/html/2604.14362v1) §3–4、§6 Tables 2–3：typed fact、有效时间、event anchor 与 evidence span 保留会话来源；entity resolution 是候选检索后的模型判断，confidence 不是事实真值。GraphSQL 只执行受限只读查询，Search 提供宽召回，Agent 再组合时间/关系计算；Table 3 的总体提升并非所有任务单调改善，增加 Search 后 temporal 子项有退步。

[Ch77](../../../../../books/part-07-agent/77-memory.md) typed state transition（accepted/pending/history）、“anchor→bounded expansion→evidence packing”及 source validtime/supersession 正文承载要采用的时间、证据与冲突责任。Existing PASS；不是声称现章逐条实现该 SQLite schema 或所有 append-only 策略。跨系统 backbone、检索设置和工具预算不同，不能把作者总体分数归因于 append-only，也不推出 LLM conflict resolution 的正确性保证。交接仍由 Memory 写入/读取状态进入 Context，不让 derived graph 取得事实 authority。

### 14414 — Conversation Autocorrelation

[exact-v1](https://arxiv.org/html/2604.14414v1) §4.1–4.2、§5/限制：stationary AR(1) 提供有效样本量筛查；conversation bootstrap 按整段会话重采样，而非独立 turn。它仍依赖会话之间可作独立抽样单元，不能把“无参数分布假设”解释成“无独立性假设”。五名德国用户、202 会话的结果不是所有 LLM 评估失效比例。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 标准误差后实际指出同 prompt 重采样、同源数据、用户聚类和时间相关性，要求匹配采样结构的 bootstrap/clustered analysis。Existing PASS，采用的是统计单元与抽样合同，不是照搬该 42% 或无条件 AR(1) 公式。新增复杂估计有样本与模型假设成本；近似独立任务仍可用简单统计，不能靠更多 turn 伪造更多独立证据。

### 14572 — Don't Retrieve, Navigate

[exact-v1](https://arxiv.org/html/2604.14572v1) §3.2–3.3、§4、§5：offline K-means 硬分支和逐级摘要构成 skill forest，在线 navigation 负责选择入口，get_document 再返回原文。200 WixQA 问题、6,221 文档的比较包含不同 online round/input 预算，不能将质量变化当严格等预算优势。硬单路径会漏分支，论文未实现持续增量维护。

[Ch76](../../../../../books/part-07-agent/76-rag.md) corpus compiler→navigable skill/topic graph→budget traversal→source dereference 正文精确承载该分支，且已有 compiler hallucination、更新/ACL/delete propagation、graph drift 和成本边界。Existing PASS；采用的是 navigation index 不拥有事实权威，非全部具体分簇参数。小 corpus、频繁更新或复杂权限仍可用 top-k + deterministic filter。章节交接是 RAG 构建索引→Agent 选择读取路径→原文支撑 claim，不将 skill summary 当原始证据。

### 14612 — ConfLayers

[exact-v1](https://arxiv.org/html/2604.14612v1) §3.1–3.3、§4.1–4.3：attention/FFN hidden state 经共享 LM head 得层熵，标准化后按邻域梯度选择 skip set；搜索达到阈值或轮数上限后，将最佳集合用于剩余 prompts。不能仅据“dynamic”标题写成持续逐请求自适应控制。中间预测熵不是最终 token 正确率或概率等价证明。

100 样本、最多 512 输出 tokens、AMD MI300X/ROCm 6.4.1 的作者测量支持受限层选择方案；固定窗口也可变慢。只把新层熵启发式和 search/freeze 操作点保留在报告，Only PASS，不能虚写“没有机制增量”。[Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md) 已有 proposal subpath、provisional state、target verify/commit/rollback 和调度开销边界；本证据未迫使改写该 correctness owner。短输出、低 acceptance 或搜索成本高时直接解码/固定 drafter 仍可能更合适；production batch、concurrency、tail SLO 未由该结果证明。

### 14683 — DR3-Eval

[exact-v1](https://arxiv.org/html/2604.14683v1) §2.3、§3.2、§4.1–4.3：reverse construction 冻结任务事实/必要文档，IR-UF、IR-SC、citation coverage 与 claim-source entailment 分账。Live web 对照中部分模型的 insight 增多，UF/coverage 仍退，不能用单个平均分代替证据回收。文本/多模态模型 judge、有限专家校准不提供事实 oracle 或完整开放世界 ground truth。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 除 EvalIdentity 的 harness/environment/scorer 身份，实际还有 Deep Research 多 evidence planes，以及先构建 expected-fact inventory、再判 present/contradicted/omitted/not-applicable 的正文。Existing PASS，不是只因已有“评估”主题。采用范围是 evidence 质量和 omission denominator 的独立责任；具体 100 任务、噪声预算与该 rubric 只留报告，不能保证所有正确替代研究路径都被 reverse construction 枚举。

### 14419 — Equifinality

[exact-v1](https://arxiv.org/html/2604.14419v1) §3.3–3.7、§4.3–4.4、§5：五种 cosine topology、各三 seeds 的收敛 PPL 在预设 1-PPL TOST 范围近似等价；router 容量与收敛阶段必须与 topology 分开。冻结 hop routing 在收敛点仍使 34.62→37.26，下游九组检验仅一组通过等价，不能推出“路由不影响质量”或“所有 topology 都可换”。

Only PASS：保存 topology/capacity/convergence 三因素比较及冻结干预反证，绝非仅模型名字或主题匹配。[Ch21](../../../../../books/part-02-model/21-moe.md) 的 causal expert-function audit 并未精确承载这一比较，但作者有限小模型、语料和训练配置尚不足以改写一般 MoE 设计判断；不采用“expert pool 决定一切上限”。iso-active dense 的极窄 FFN 也不能当一般部署基线。若以后采用跨拓扑设计结论，应另有足够对照，而非本轮假造 Existing 或因参数小自动否定所有贡献。

### 14434 — Geometric Expert Control

[exact-v1](https://arxiv.org/html/2604.14434v1) §3、§7–8：underfit 模型的 logit projection 与 converged 模型的 knockout/steering/suppression 是不同证据。44 prompts 上定向干预与随机同数量 suppress 对照提供局部因果证据；cardinal/discourse 路径近零及扩大邻居无额外收益限制其解释。不能把投影出的词类命名提升为 expert 拥有完整领域知识或可靠生产编辑。

[Ch21](../../../../../books/part-02-model/21-moe.md) 实际区分 route frequency、写入幅度、自然语言标签与因果必要性，并要求删除/替换后的独立行为验收；specialization 不是预划知识部门。Existing PASS。采用的是功能诊断→干预→行为验证链，不是声称本章已覆盖几何 router 的全部局部控制方法。精确方向、activation 支持集与任务外副作用未闭合时应保留普通 routing/held-out evaluation，而非按解释标签裁剪模型。

### 14717 — Layered Mutability

[exact-v1](https://arxiv.org/html/2604.14717v1) §6.1–6.4、§9.2：四个 prompt/memory 条件、gpt-4.1-mini 生成与 gpt-4.1 judge，在五个手工任务上观察到 visible self-description 回滚而 persistent memory 保留时行为未回 baseline。不是纯 taxonomy，也不证明 weights 被修改。缺少无编辑但同 memory 的完整因果析分及广泛重复方差，不能把初步残余差异升级为所有 Agent 的连续性定律。

Only PASS，保留 prompt-only rollback 不等于全状态回滚的受限案例。[Ch77](../../../../../books/part-07-agent/77-memory.md) 已有 derived memory 的 source/version/supersession、撤销重建、external/weights 回滚差异和 memory operator held-out 验收，但未精确写此四条件反例；不标成虚假 Existing。论文没有提供能替代上述 provenance/rollback 的生产机制，暂不扩写身份治理 taxonomy。实际 effect 与 workflow 授权仍是外部 owner，不因 self-description 恢复就自动晋级。

### 14732 — WAV

[exact-v1](https://arxiv.org/html/2604.14732v1) §4.2–4.3、§5.2–5.3：video/value 两套 Gaussian noise 经采样、max-n value-SNR 排序、elite mean/std 更新与平滑迭代，action decoder 消费两者。是显式 latent 优化，不是取消搜索；value SNR 是选择 proxy，不是物理可信度。三阶段 flow 训练及有限 Piper 每任务 15 trials 支持该局部分支，不独立证明生成先验保证可行。

Only PASS：保留双 noise 搜索/价值工作点。[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的 latent goal/target forward model、critical-phase dream 排序与 controller commit，以及 action proposal/value/controller 分权，承载既有责任；尚不必新增具体采样配方。修正表述：§5.3 首段说 K 从 1→5 改善、10 边际；performance-efficiency 段说 0→3 改善、之后成本继续涨而收益饱和。应分别保留，不能压成所有成功率一律 K>3 无收益。理论可行性依赖所设 latent 先验/动作界，不能外推任意规划器或真实闭环安全。

## 验收边界

本批十项实际 evidence 与处置可关闭，无新增 Books gap 被本批证据确认；14228 的采用范围与14732 的消融措辞应由作者同步到报告。日期归属仍由整日官方槽/first-public reconciliation 负责，本审阅不替代该 Gate。访问了必要 exact-v1 正文，但没有扫描全部附件、版本差异或其他候选，亦未宣称零遗漏。已有七项独立审阅保持有效，不重复工作。
