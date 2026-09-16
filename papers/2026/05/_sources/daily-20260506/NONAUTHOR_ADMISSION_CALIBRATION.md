# 2026-05-06 非作者候选准入校准

**角色：** fresh-context 非作者复核  
**检查时间：** 2026-09-14T18:06:52+08:00  
**结论：** 未通过；当前 `118 retained / 375 closure` 不能直接冻结，也不能据此启动 118 项全文审阅。

## 实际检查范围

- 完整读取当前研究合同、报告合同、05-06 日报、唯一 active 筛选账本和 493 项 raw identity receipt。
- 逐条读取并独立判断全部 118 个 `retained` 的标题与完整存档摘要。
- 扫描全部 375 个 `closure` 的标题及 family-specific 关闭理由。
- 对 89 个关闭项回读完整存档摘要：覆盖安全/隐私/纠错信号、LLM/Agent/Transformer/RAG/生成/多模态/训练/推理/基础设施主题，以及按账本顺序等距取得的低风险对照样本。该抽样不是 375 项全文审阅。
- 未把 title+abstract 校准冒充 exact-v1 Method、evaluation 或 Books 审阅；本轮未直接修改 Books。

## 高置信误收：应降回 pre-denominator closure

| Source family | 当前问题 | 可执行改判 |
| --- | --- | --- |
| `2605.03069` | 连续数据的 federated privacy encoder 只在 MNIST/CelebA/HAPT 验证；没有 LLM、基础模型或其基础设施的直接机制和适用边界。 | `Rejected — out of current LLM / LLM-infrastructure scope` |
| `2605.03723` | 人类/LLM 共创文本分段是内容来源检测应用；change-point 方法没有改变模型、训练、推理、平台或 Agent 的长期设计判断。 | `Rejected — application-specific provenance detection` |
| `2605.03870` | Flower 在高时延/丢包下的 TCP 生命周期是边缘 federated-learning operating point；摘要没有连接当前 LLM 训练通信或基础设施选择。 | `Rejected — federated edge transport outside current mainline` |
| `2605.03983` | MPI Sessions 的一般实现重构与初始化扩展性没有 AI workload 或 LLM distributed-runtime 证据；不能仅凭 HPC 可类比性进入候选。 | `Rejected — general HPC mechanism without AI-system evidence` |

以上四项共享的错误是“泛 ML/HPC/AI 名称可映射到章节”被当成直接贡献。应只扩查同一错误理由的 retained 项，不回滚与之无关的候选。

## 高置信漏收：应恢复为候选，再按分数做 exact-v1 定点审阅

| Source family | 摘要已给出的具体增量 | 拟核验选择 |
| --- | --- | --- |
| `2605.02910` | creative tool use benchmark 把 object、part、affordance、physical mechanism 分离，并观察 scaling 与 CoT 很快饱和。 | Agent 工具/规划评价是否必须验证物理 mechanism 而非只验证可用 object。 |
| `2605.03129` | 把 indirect prompt injection 反向用作网页所有者的 PII 防护，并暴露浏览接口和 sanitizer 改写会改变有效性。 | Web-grounded Agent 的 trust boundary 是否必须包含内容提供者侧防护及 sanitizer threat model。 |
| `2605.03140` | 在结构化 VirusTotal evidence 已充分时，RAG 可因弱相关上下文降低 malware explanation 质量。 | 检索是否应以 evidence insufficiency 触发，而非默认添加更多 context。 |
| `2605.03153` | 用 correction-count 曲线联立新类恢复与旧分布保持，并观察 ANN recall 大幅下降时分类仍稳定。 | 在线纠错的评价合同是否应从 top-k recall 转向任务 margin、恢复速度和 retention。 |
| `2605.03159` | 从 2–10 条 passing trace 学习 essential states，以 PTA 合并和 topological-subsequence 验证非确定执行。 | Agent workflow 的成功验收能否由可解释的必要状态与顺序约束拥有，而非 exact trace matching。 |
| `2605.03179` | 证明现有恶意代码 refusal benchmark 混合了 executable weapon 与 harmful knowledge，并给出跨厂商一致性标注轴。 | 代码安全评价是否必须先分离请求能力类型再解释 refusal rate。 |
| `2605.03196` | pre-generation geometry 在 math answerability 上有效、fact 上无可靠信号，并定位到早层后逐渐衰减。 | “模型知道自己不知道”能否使用表示 sensor，以及该 sensor 的 form-conditional 边界。 |
| `2605.03229` | sparse memory rows 以较小适配收益换取显著较少 forgetting，并与 LoRA/full tuning 明确形成 branch。 | 参数外 memory adaptation 的收益是否由容量、row selection 与遗忘预算共同决定。 |
| `2605.03310` | 固定模型/工具/提示后只改变 coordination configuration，并把 calibration 与 discrimination 分开；同时报告多重检验未显著的限制。 | Multi-Agent coordination 是否可成为独立可测的 architecture variable，而非隐藏在 agent prompt 中。 |
| `2605.03317` | diffusion 训练中有用的 representation granularity 随 SNR/timestep 改变，静态 alignment target 形成 mismatch。 | 生成模型 alignment 是否需要由 denoising state 路由 coarse-to-fine prior。 |
| `2605.03363` | 高层 task-space RL 与低层 joint-space QP 分权，使安全约束和动态 margin 无需重训 policy。 | Embodied policy 的语义 intent 与 physical commit 是否必须由不同 controller owner 承担。 |
| `2605.03413` | world model 不只预测 observation，而把解释表示为可执行、可组合 latent program，并由共享 transition 执行。 | World state 的 owner 是否应包含显式理论/程序，而不只 latent next-state prediction。 |
| `2605.03426` | 在异构 VLM client 间以 routed reward/preference 协作替代参数聚合。 | 架构异构使 parameter federation 失效时，supervision interface 能否成为跨客户端共享状态。 |
| `2605.03475` | 具体指出二元 VQA 的 yes-bias、低分辨率 auditor 和单维 prompt 混杂，并以 native-resolution Likert 与人类分层对照。 | 视频生成评价是否必须绑定 auditor resolution、question form 和多维共同失效。 |
| `2605.03505` | 同一 RCA agent 在开放 benchmark 为 91.3%，真实 incident 仅 65.1%，差距指向多因根因、大规模依赖与缺失观测。 | Agent evaluation 是否必须把 observability completeness 和真实 incident topology 纳入 contract。 |
| `2605.03547` | multimodal unlearning 评价同时约束跨变化的忘却泛化与原能力保留，而不是只测单一 concept removal。 | “已遗忘”是否必须在 modality、composition 和 utility preservation 上共同验收。 |
| `2605.03609` | 在 transformer branch point 做局部 residual steering，并用最小范数二维更新校准目标偏好。 | activation steering 是否能从全局 direction 改成 layer-local、branch-conditional control。 |
| `2605.03623` | cumulative flow map 把局部 drift 与 finite-time transport 统一，支持 few/one-step generation 而不增加容量。 | few-step 生成应比较全程 state transition parameterization，而非只比较 sampler 步数。 |
| `2605.03625` | 多次模型调用与 graph search 生成更优 plan，再反哺训练；同时保留 inference-time search 分支。 | planner self-improvement 中 search teacher、model weights 与 runtime search 的责任边界。 |
| `2605.03637` | 用互信息约束分离 task 与 embodiment latent，从单个人类视频生成机器人执行视频；没有下游 policy 收益是必须保留的 non-proof。 | 跨 embodiment 数据转换能否成为 VLA data interface，而不是把形态差异留给单一 policy 吸收。 |
| `2605.03669` | 同一 voxel world state 联合 dense 与 instance semantic layer，并用 sliding window 限定昂贵 fusion。 | 持久语义地图是否需要同时拥有局部稠密状态、对象身份与有界活动窗口。 |
| `2605.03782` | 用语言预测与后续视觉 reality 的差异作为 intrinsic curiosity，主动寻找会修正内部 world model 的观测。 | 部分可观测 Agent 的 exploration 是否应由可证伪 prediction error 驱动。 |
| `2605.03903` | 对文档采集条件做十因素归因，显示总体准确率相近的 LMM 有不同真实采集失败图谱。 | 多模态部署评价是否必须从 aggregate score 下钻到 acquisition condition。 |
| `2605.03937` | 公开小型 omni 模型把 middle-layer semantic bridge、八 codebook audio buffer 和 multimodal sequence format 作为可检查接口。 | Thinker/Talker 与 codec state 的边界是否可在小模型中形成可复现实例；性能不可外推到 frontier omni model。 |

这 24 项的共同错误是：材料已经给出具体机制、评价混杂或设计反例，却因“领域窄、没有新 owner、只是局部方法/benchmark”被提前关闭。恢复只表示进入证据审阅，不表示结论或 Books 已成立。

## 保持关闭但需要保留的边界样本

- `2605.02913` 的 GFCR 综述提供有用分类，但摘要没有新的 primary mechanism 或解决具体知识分歧的综合证据。
- `2605.03042` 的 research harness 列出 claim ledger 与 adversarial reviewer，但没有对 assurance 机制的受控有效性证据。
- `2605.03213` 的 confidential-agent survey 指出 multi-hop attestation 缺口，但没有可检查的新协议或 production guarantee。
- `2605.03227` 再次证明 deterministic computation 应委托 interpreter；这是成熟原则的受控复现，没有新增适用边界。
- `2605.03788` 的 swarm 案例再次证明 grounding/guardrail 有益，但没有分离新的通用闭环机制。
- `2605.03916` 只证明 atomic fact-checking 增加 clinician trust，未测事实正确性或 over-trust，不能把 trust 当安全收益。
- `2605.03956` 的 PoV agent 是 call path、context、execution feedback 的安全应用组合；摘要没有新的 reachability 或 oracle 保证。

这些样本用于约束恢复尺度：不能因“安全、Agent、benchmark、framework”字样反向把所有相关条目恢复。

## 校准后的可执行状态

- 当前账本仍是作者侧 `118 retained / 375 closure`，尚未接受为冻结分母。
- 先执行 4 项降级与 24 项恢复后，工作分母为 `138 retained / 355 closure`；这只是下一位作者需要落实并再校准的题摘结果，不是数量目标，也不是证据完成数。
- 对上述 4 项误收扩查共享“泛 ML/HPC 可映射即保留”的 retained 理由；对 24 项漏收扩查共享“局部/领域/无新 owner 即关闭”的 closure 理由。只重开受影响族，不推倒 493 项身份恢复。
- 完成改判后，再按三维分数只对冻结候选定点读取 exact-v1 的 Method、关键 evaluation 与直接 limitation。不得先把 118 或 138 项全部全文化。

## 日期与 withdrawn 边界

- raw receipt 有 493 个唯一身份；493 个 initial DataCite registration 均为 2026-05-06，346 个当前 OAI datestamp 仍为 05-06，147 个已被后续 revision metadata 覆盖。
- 结合 `2605` family ID、receipt 保存的 v1 identity/history 与[官方 announcement 规则](../ARXIV_ANNOUNCEMENT_PROVENANCE.md)，批次层面支持把 Tuesday 20:00 EDT 推导为本窗 2026-05-06 08:00（Asia/Shanghai）。这是 `public-batch-derived`，不是单篇页面披露的秒级时间；`datacite_initial_created_owner_proxy` 也不能称为“官方 arXiv batch”。
- 本次准入复核没有逐页重新打开 493 个 exact version history；因此逐 family withdrawal 与版本状态仍属于候选 exact-v1 审阅的一部分，不能由 raw receipt 的空字段替代。
- 已知 `2605.04356v1` 不在本日 493 raw pool，且 v1 withdrawn、v2 是另一个有效版本事件。本日只保留跨窗最小纠错，不把它计入 raw、candidate、score 或 Books，也不把 v1 状态扩张到整个 family。

## Books 与完成条件

- 本轮未写共享 Books，也没有复用旧 14 个 Integrate 或 43 个 No Change 作为通过证明。
- 下一步先落实题摘分母校准；之后才按冻结候选评分和 exact-v1 审阅，并逐项核对旧 Books 判断。
- 日报继续保持 `In Progress`。只有机构源覆盖、冻结候选证据、Books 决定/必要实体改动及另一轮独立语义复核全部通过，才可 Complete。
