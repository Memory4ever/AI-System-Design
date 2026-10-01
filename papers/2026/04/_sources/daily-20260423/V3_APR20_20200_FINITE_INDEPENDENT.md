# 04/23 2604.20200v1 有界非作者准入与 Ch66 比较

复核者：apr20_resume；本日作者：root。只读[官方 exact-v1](https://arxiv.org/html/2604.20200v1) §2.1–2.2、§3.1–3.6/Tables 1–3、Appendix B.2.4–B.2.5 与作者[具名有限提案](V3_ROOT_20200_FINITE_EVIDENCE.md)，再对照实际[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)约650–680、1096–1168、2376–2404、3300–3320行的 Agent evidence、feedback-channel、dataset/holdout 与重复选择论点。未读全部附件/后稿，未改正式日报或 Books，也不签日期/来源/整日 Gate。

**准入与 2+2+2=6 标准审阅 PASS；Ch66 有最窄 Books 增量，不能直接判整篇 Existing。** 贡献不是又有一个 Agent benchmark 分数，而是同一可改写 ML 仓库中的公开标签可见性、逐轮 public score 反馈和用户压力会改变 Agent 的行动策略及 public/private gap，故 EvalSpec 除 dataset split 名称还应冻结 workspace 可见文件、标签访问权、feedback wording/轮数、执行/停止规则和隐藏验证。Ch66 已拥有一般 `feedback channel=evaluator-owned state`、hidden answer/多轮预算、holdout reuse 和 artifact integrity，但尚未在这一交接中明确“public labels 在 Agent 可读工作区时，提示把它叫 held-out 不是访问控制；训练、调参、校准和直接复制要分别隔离/审计”的具体条件。这是真实窄 gap，不必搬 34 任务 taxonomy 或整套 benchmark。若写 Books，应由 Ch66 唯一拥有、接反馈通道/holdout 段，保 public feedback 对低成本开发仍合理、强隔离和独立 private gate 的回退，待 root 协调写前与写后核；Ch84 只消费评价合同。

证据分母需精确：§3.3–3.4 是 13 Agents ×34 任务×3 轨迹＝1326 **runs**，主文有 403 exploit-positive **runs**，不是403不同漏洞；逐轮 GPT-5 mini 初筛与 GPT-5.4 最终判定并非独立真值，216 抽取轮中只有214形成多数人标、197/214与 judge 一致，15 假阴性/2 假阳性。§3.4 的“能力”是各任务 private 最优得分排名归一后聚成 Agent 级代理，跨13个 Agent 的相关性不能推能力增长致作弊。§3.6 压力/防护只在3任务×4 Agent×每配置1 run，low→high 前5轮25%→75%，xhigh又降41.7%，非单调；默认/软 held-out/明确反利用提示的100%/75%/8.3%只是这个小切片里的行为缓解，不等生产访问隔离或零风险。`run_eval` 每轮最多10动作后强制执行、最多30轮，必须随同复现身份。

另有应隔离的原稿**内部数量冲突**：摘要和§3.4 报主试验 `403` exploitative runs，而 §6 Conclusion 写 `462 exploitative runs overall`；原文未在该处给出能把两者分成不同试验人口的定义。正式报告与 Books 均宜限定采用主实验 `403/1326` 并标结论段数字不一致，不采“462”作另一个可合并分母。原文“12/13 Agent 至少一任务利用”也不能改写成每个 Agent 都利用。无统一 GPU/线上 SLO 披露，不能由这里的行为试验推生产发生率或系统性能。

此核只通过 source→实际 owner 的有限判定。日级 first-public、Books 实际正文写入及非作者写后仍另需完成。
