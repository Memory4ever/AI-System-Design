# 04/28 arXiv 贡献准入：首个有限校准批

窗口仍为北京时间 `[04/27 09:00, 04/28 09:00)`。本批只处理旧 945 身份库存中原标 `retained` 的前 30 个身份（`2604.22778`～`2604.23139`），不沿用旧标签。逐项读了已保存 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 的完整标题与摘要；其中 `.22782v1`、`.22783v1`、`.22879v1`、`.23046v1` 又与官方版本页对读。**本批不是最终候选分母**：旧摘要可能被后发版本污染，以下“继续”只说明题摘提出值得核的具体增量，进入正式日报前需 exact-v1、日期例外、现有 Books 命题和证据核验；“关闭”是可独立复核的前分母理由。批次日期采用[相邻批次有界推断](./V3_REVIEW_CHECKPOINT.md#相邻批次的有限归属推断不是-doi-日期等同公告)，不把 submitted/DOI/OAI 单字段当首次公开。

| ID | 题摘判断 | 具体理由或下一核验点 |
| --- | --- | --- |
| 2604.22778 | 继续 | 小中模型训练中 Q/K 与 V/O 的深度谱演化不同，若消融确能区分瞬时 rank 与稳定谱形对剪枝的作用，会改动按层重要性代理；先核训练轨迹/跨模型和剪枝归因，不采摘要“因果”措辞。 |
| 2604.22782 | 继续 | 不沿时间维逐 token 删 KV，而在训练时随机把层注意力指向前层状态，使部署时按深度共享 cache；需核“无信息损失”、TTFT/throughput 与训练成本的限定。 |
| 2604.22783 | 继续 | LoRA 可训练参数少仍保留随长度增长的激活，论文改约束激活子空间；若实测隔离 batch/长度/模型，改变端侧 PEFT 的 memory owner，而非仅同量纲速度竞赛。 |
| 2604.22871 | 继续 | 安全测试从固定 prompt 模板转成受固定 harness 反馈驱动的可执行攻击程序搜索；核 program-search 与目标集隔离、攻击预算，不能直接把 jailbreak 数字外推生产风险。 |
| 2604.22879 | 继续 | 局部动作安全而跨组织私有上下文合成违规的失效模型，提出 sidecar 传播受限语义状态；核跨域状态是否真的可验证、泄漏/延迟成本和可执行权限边界。 |
| 2604.22881 | 前分母关闭 | v1 §4 的 GPU page / CPU chunk、pinned DMA、双缓冲与局部性替换确是真实的 HSTU 推荐状态机制；但 Ch45 已有可恢复状态的 tier、页/批量传输和有效性/成本分账，论文未证明新的 LLM/Agent 状态身份或改变既有 tier 选择。3.1×/98.5% 只属该推荐负载，不外推 LLM Serving。 |
| 2604.22888 | 继续 | 有效 Skill 内夹带恶意内容，文本筛查可能失灵；用 response-conditioned attention/隐藏态对齐作为执行前检测信号，需核检测是否依赖已生成响应、真实 effect 前是否来得及阻断及成本。 |
| 2604.22891 | 继续 | Judge 自偏好的“等质”响应配对可能分离质量辨别与偏向；核等质构造独立性及人工真值缺失是否令 31.5% 缓解结果仅是代理指标，不把自评当客观真值。 |
| 2604.22893 | 前分母关闭 | v1 §3/§5.6 确测 proxy leave-one-source-out gain 排序，但只有每域 12 训练/6 验证样本和 4 source shards 的 smoke run，ensemble 还远弱于 proxy；Ch27 已要求固定 checkpoint/compute 后的 held-out/full-training 验收。该受限数据定价组合尚未改变此选择，Merkle 账本也不建立新训练目标或因果贡献保证。 |
| 2604.22901 | 前分母关闭（定点重开后） | 官方 v1 §3.3/Alg.1 确有 half-spectrum token、累计残差 KV、event-intensity 选择刷新及周期 probe/error-feedback，不能再按“仅固定缓存”排除；但 Ch24 当前已具体承载 trajectory-conditioned token refresh、probe/误差预算、周期校准与 full-recompute fallback。half-spectrum 和低频常刷新是该 3.2M 参数 Fourier 时间序列 score model 的受限状态划分，未改变本项目现有多模态生成 cache-validity/refresh 选择。§4.3 ECG 消融的 full cache SW 0.015 vs no-cache 0.014，非无损；五组时间序列、N=134–365，未与跨模型/模态同预算策略比较。保留领域方法学价值，不把 2.2× 写成大模型服务结论。 |
| 2604.22906 | 前分母关闭 | 端侧 LLM 架构、模型压缩与资源管理的综述，只归纳已有挑战及方向；题摘无新的可归责机制、反证或足以解决现有知识分歧的综合证据。 |
| 2604.22935 | 前分母关闭 | ASIC+eFPGA监测、旁路缓解、补丁是安全架构设想，题摘无已实现对照/威胁覆盖或可执行新边界；不能把可重配置本身计作已验证的长期机制。 |
| 2604.22981 | 继续 | 让终局 reward model 的每个前缀输出成为条件终局期望，连接 MC/TD 目标与 PPO 内存；需核两正则的条件与“零架构/数据变化”边界，不能把 token PRM 分数外推为正确过程监督。 |
| 2604.22985 | 继续 | Function Calling 的 AST 等价类和语义 token 选择使不确定性测量与自然语言回答不同；可改变外部 effect 前的置信门槛，但要核真实 effect/错误代价与校准定义。 |
| 2604.23001 | 前分母关闭 | VLA 数据集/benchmark/data engine 综述提出 fidelity-cost、grounding 议程；没有新增可验证的机制或解决当前章节具体冲突的证据，不能因列出主线问题就保留。 |
| 2604.23002 | 前分母关闭 | 主要在物理题的自动形式化/Lean 数据集与 agent pipeline；AI for Science 当前暂缓，语义漂移观察仍属该领域任务，未单独验证通用 Agent/形式化接口的新边界。 |
| 2604.23036 | 继续 | MoE SFT 低频专家仍含有用信息，拟 always-active condenser 与稀疏路由并存；需核是否在相同计算/参数预算下分离 tail preservation 与梯度饥饿，非只看 QA 增益。 |
| 2604.23046 | 继续 | 删除后性能/一阶梯度回归可能掩盖二阶 optimizer state 残留；需核实测删除定义、状态扰动与隐私/信息残留的证明界，可能修改 unlearning 的验收对象。 |
| 2604.23049 | 前分母关闭 | 将 HITL 由应用逻辑搬到协议/环境层的四维框架，题摘仍是成熟审批/角色/通道分权的抽象，不给新的控制一致性失效或执行对照；不因多代理标题自动准入。 |
| 2604.23051 | 继续 | 多轮问答中时间范围隐式继承/切换，oracle context 下仍漂移，可能揭示单轮准确率无法代表状态转移正确性；核合成 Wikidata 链的真值与模型记忆/上下文错误如何分账。 |
| 2604.23056 | 前分母关闭 | 1D Kalman reward 平滑只在 CartPole/LunarLander 验证，未连接大模型后训练的组内奖励、变长轨迹或非平稳策略分布；不能因 RL 术语归入 LLM post-training。 |
| 2604.23058 | 前分母关闭 | 企业 AI 能力、授权暴露、网络风险的经济模型说明治理会影响部署；属于行业/经济条件分析，未给当前 Agent 权限系统的新执行机制或可用安全合同。 |
| 2604.23069 | 前分母关闭（反向抽检完成） | v1 §3 用 LLM 估父边、BFS 保全祖先，并将执行反馈标为 passed/failed/unknown/superseded，禁止失败或被替代节点继续作 parent；Ch77 已分 construction/retrieval、superseded/history 与 dependency-closure 失效。文中未独立证明父边的真实因果性或新增可验证一致性不变量，滑窗对照亦未隔离图结构和反馈标签的作用。 |
| 2604.23073 | 继续 | VLA 预训练表示导出 RL token、轻量 actor-critic 在真实机器人在线练习并约束原 policy；需核读出与已有 action adapter/critic 的差异和真实物理反馈预算。 |
| 2604.23080 | 继续（实际正文已承载，待日期/非作者终核） | [官方 exact-v1](https://arxiv.org/html/2604.23080v1) §3–5 把 node churn 与 agent warm/cold 分开，发现 Kademlia 的 discovery success 与 gossip 的 maintenance/部分 latency 优势并非同一指标；全证据为 SimPy 合成运行。实际 Ch84「Agent Discovery 是可修复的路由状态」已有该 family 的 semantic-body-binding 与 Review note，明确 node membership/readiness、identity 与权限、两类 overlay 成本和受限证据。此文的贡献不能仅因已经写入 Books 而前关闭；若本日公告归属成立且非作者核正文，可判候选的 Existing Coverage，**不是**新 Books 写入。 |
| 2604.23099 | 继续（exact-v1 定点核后） | [官方 v1 §2.2–2.4、§3、Appendix B](https://arxiv.org/html/2604.23099v1) 在同题多历史模型成绩矩阵构造 GP prior，用后验积分方差选题估总体分、用超水平集与主题采样找失败；Ch66 现有 adaptive evaluation/WILD 选题与 surrogate 回退原则，但未把**估总体表现与主动寻找失败**两种 estimand/样本预算明确共享一个 prior。真实增量值得继续核，而非纯“GP 新名”。关键限制：Theorem 3 的均值等式是对后验条件期望，偏差界比较估得与理想 GP posterior mean（`S_t`），不能直接称对实际有限题库平均分 `S*` 无偏/有界；§3 的 MAE 才按 `S*` 实测。跨新 benchmark 的 prompt-feature 迁移无该 score-feature 定理，Table 1 新 benchmark 部分任务输随机；生成失败依赖 generator reference（80 题人工抽核仍有 8 个生成器错答），不能把“发现失败率”当独立真值。后续须核日期、非作者准入和成本/Books，不预评分或写入。 |
| 2604.23102 | 前分母关闭 | 六类 Bayesian 学习法在五个回归数据集的小样本 ranking 波动；对当前大模型评价只可类比一般置信区间原则，题摘没有新增 foundation-model 评价合同或关键既有结论反证。 |
| 2604.23108 | 继续 | 异构 expert 组的 token 复杂度路由与 GPU 按组分配耦合，可能改变“专家尺寸统一”与设备负载的取舍；需核 group auxiliary loss 是否确实隔离 routing 和 placement 收益、硬件/预算可比性。 |
| 2604.23121 | 继续 | 低数据 VLA SFT 后概念/空间 steerability 锁定，训练期 visual grounding 与测试期对比引导分担保留与恢复；核测试期调用预算、无额外数据断言与真实任务反证。 |
| 2604.23139 | 前分母关闭 | 具体贡献是分布式 GNN 的远程特征缓存随网络拥塞动态调整；当前主线聚焦大模型训练/推理，题摘未建立它对 LLM 通信/参数或 KV 状态的直接机制转移。 |

阶段数量：30 个旧保留线索中，16 个“继续”、1 个“继续核贡献”、13 个具体前分母关闭；**不是**本日报 17 个候选。`22901` 曾由[非作者有限校准](./V3_APR01_ADMISSION_BATCH1_INDEPENDENT.md)定点重开；作者随后对官方 [v1 §3.3、§4](https://arxiv.org/html/2604.22901v1) 与 Ch24 现有具体正文对读，因未形成当前 AI System 长期设计增量而重新关闭；非作者已定点复核该修订理由通过，见[第二批独立审计](./V3_APR01_ADMISSION_BATCH2_INDEPENDENT.md)。正式准入前仍须读 pinned-v1 及对应实际 Books 命题。下一小批以相同门槛检查后续旧保留项和代表性旧关闭项，不能以此批比例推算全日。
