# 04/29 三项旧样本的有界反向准入（作者侧）

本批只处理旧 60 篇完整题摘中共用「局部产品比较或成熟组合」前闭理由的 `2604.24826`、`2604.25197`、`2604.25203`。读取官方 exact-v1 的身份/完整摘要及决定贡献的有限方法、对照、反证，并核当前 Ch27/63/66/72 的实际论点；没有把三篇一律转为全文队列。下面是贡献判断，不以 arXiv `submitted` 独证首次公开，也不代替非作者准入或日级 Gate。

## 2604.24826v1：维持具名前闭

[官方 v1](https://arxiv.org/html/2604.24826v1) §4–5、Appendix A 实际将八个公开安全集中的 1,018 项重标为 852 `BLOCKED` / 166 `ALLOWED`，用各产品 API 结果归一成二分类；DKnownAI 在此分母的召回 822/852、TNR 150/166。两类风险（Agent 威胁／有害内容）分账有用，但没有新防护机制或使现有安全授权决策改变的条件。更重要的是 Appendix A 对 Azure 任意 harmful severity `>0` 即阻断，对 Lakera 则只收 `l1_confident/l2_very_likely`，各产品阈值不是统一校准的 operating point；166 条允许样本又是从以有害输入为主的集合中重新标出，不代表生产良性基率。两项排名不能推出普遍最好或跨租户误报成本。实际 Ch66 的 `EvalSpec` 已拥有 eligible population、slice、threshold、scorer 与不确定性，Ch72 已将 detector 置于 policy 之前；论文未隔离这两者缺失的新合同。维持旧 60 的已计前闭，不再改工作数、不评分或写 Books。若有同 policy/阈值、同真实流量基率和执行 effect 的配对反证，再窄重开。

## 2604.25197v1：维持具名前闭

[官方 v1](https://arxiv.org/html/2604.25197v1) 摘要、§III–V、§VI-A/C 研究 split ResNet101 的 cut、子模型节点与 smashed-data route 联合 ILP，以及以 BCD 近似求解；这里确实同时考虑模型分割和多跳通信，不因「非 LLM」直接排除。可是架构本身沿用作者此前的 service-function-chain split 方案，新贡献是在该设定求一组 cut/placement/path，评价只用 ResNet101 的 37 个块、NSFNET 14 节点/42 定向链、1 Gbps 同质链路和按测量拟合的延迟模型；`K=2` 轻任务、`K=3` 重任务的最优点是该成本函数下的 compute/communication 平衡，不是新的跨工作负载模型状态、安全或 placement 失效条件。论文也明确 BCD 不保 ILP 全局最优，仿真/求解时间不等于真实端到端训练/推理服务延迟。Ch63 现有拓扑/可行性/调度权责已承载通信与 placement 共同决定可行路径的原则；若将来 LLM/VLA 的分割边界、activation privacy 或动态链路状态证明该原则遗漏特定长期约束，再重开。当前维持旧 60 已计前闭，不新增关闭数。

## 2604.25203v1 BARRED：从已计前闭恢复为潜在候选，待同行

[官方 v1](https://arxiv.org/html/2604.25203v1) §3 Algorithm 1 对自定义 policy 从无标签 seeds 提取维度与取值，按维度/标签采样边界例，再由 advocate 与两名 judge 争辩、未通过则修订或丢弃。维度覆盖、synthetic generation、debate 各自不是新原语；但这篇把**policy 边界样本的标签有效性**作为训练数据 Gate，并给与「不验证」和单人 self-refine 的直接消融：Table 4 人工标注测试的 accuracy 分别为 `0.85/0.58/0.53`，合成测试为 `0.99/0.65/0.65`。这构成不能仅以「成熟模块组合」前闭的有限反证：在缺标注的定制 policy 下，产生更多样本与核实边界标签是两个不同选择，且同一模型自我修订未替代对抗性核验。作者侧恢复为**潜在贡献**，拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 标准审阅、暂不写 Books；真实 owner 是 Ch27 的 synthetic-data quality/lineage 和 Ch72 的 policy-bound guardrail，Ch66 负责独立测试身份。是否真的超出三章已有主张，须非作者对具体句子判 `Only/Existing/最窄 gap`。

证据不可放大：四项评测为 repetition、privacy、一个 GAIA plan node 与 health advice；DynaGuard 原 278 rules 经至少 20 样本与非全合规筛到**两条**，GAIA 原 112 条非合规计划共有 missing `end_plan` 单一错误，作者先补该 tag 再人工构造 82+82 平衡测试。训练/辩论均使用 GPT-5-mini，两个 judge 不是独立真值；合成测试另起 seed/维度并人工核，但其生成流程与训练共享方法，最关键的人类测试规模是 158/112/164/200。§5.3 的 coverage 由 LLM relevance threshold `0.5` 判定，不能当真实政策空间覆盖；Table 4 未与等调用预算的强人工/异模型审核相比。不能由 `0.85` 推生产 guardrail effect、跨 policy 普遍优势或低总成本。首公开仍待本日联合批链和任何更早独立公开例外核验。旧 60 作者工作账由 `39 潜在/21 前闭` 改为 `40/20`；106 完整题摘工作集合由 `69/37` 改为 `70/36`，不是冻结候选分母。若非作者发现其消融只反映不同生成预算/训练样本量或 Ch27 已明确包含同一 policy-bound label-validity 命题，可复核后改回前闭或判仅报告。
