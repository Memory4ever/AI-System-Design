# Nov19九个最小准入门／只处理具体决定域

## 1. 范围与已发生层

本日补充窗口仅2025-11-18 BJT；九门来自本日五主题78唯一身份，非Nov18旧池。Ohm§9/11/12/13准入校准实际通过，九门仍需原决定事实，不因日期未定或Books已覆盖关闭；无新评分/确定当窗资格。当前SoCE已经窄锁实际写入、自读及范围QA，见SUP_SOCE_PRE§7，待非作者POST/root接纳；该写入不使本包准入自动通过。

## 2. 14101 APD／保留窄P，不把prompt当硬约束

实际读[精确v1 HTML](https://arxiv.org/html/2511.14101v1) §3.2–3.3（L115–148）、§4.1–4.3与§4.5（L154–185/216–239）、调度prompt L243–308。递归按层级JSON/criteria与templates细化，跨页样式是LLM总结规范的prompt消费，未披露硬约束求解或跨页一致性保证。但§4.5.1提供可改变评价解释的具体反侧：单次生成遗漏元素可使alignment/overlap指标看似更好，coarse-to-fine完整性改善却在这两指标退步；因此不能只凭几何指标判更好生成。保留**窄P：完整性与几何评价人口/分母的失配**，不按角色recipe关闭，也不采token-limit单因果、SOTA或所有成本更低。日期/当前已有说明另责；此处只是准入决定域，不授标准Source/Books。

## 3. 13152 GrammarPseudo／关闭提案

实际读[精确v1 HTML](https://arxiv.org/html/2511.13152v1) §3.2 Eq1–objective（L94–128）、§4.6–4.7（L213–244）及Limitation L306–308。实际规则是每epoch按伪标签MSE排序，下一epoch仅低loss的alpha比例获归一权重、其余为0，后续可再进入；不是抽象的新noise模块。已有small-loss/self-paced引用明确，所报alpha/生成LLM比较是两grammar数据集内效果，未揭示新的通用成立条件/失效反证或独立训练机制；故C提案，**不因教育领域/小模型/无日期关闭**。低loss不证明真标签clean，不采robust普效；无需为该非采用项补全所有实验/首公开日。

## 4. 13983 MoMoE／关闭提案

实际读[精确v1 HTML](https://arxiv.org/html/2511.13983v1) §3.1–3.3（L88–136）。neural侧为末FFN的token top-k与既有load-balance loss，其余权重冻结；agent侧没有新的资源路由，而是同prompt固定发三模型、拼接三输出后交GPT-4o分类。该两层组合未披露新的路由资格/训练信用/通用成立边界，不把synergy名称或金融准确率当系统贡献，C提案；不证明组合无学术价值，也不展开所有数据/方法对照。

## 5. 交独核与剩余普通

§2为新增明确评价反侧P，§3/4是具名最小门后C提案，请root转Ohm只核相应精确HTML决定域；不把本包当全九门或当窗日期完成。剩余00045指标/faithfulness、14043执行约束、13410异构层级memory、13293trigger/rolecredit、13103counterfactual advantage、21707RF codec/anchor仍普通，尚未因访问或准备状态隔离。原文片段结果存SUP_WEB_MINIMUM_FIRST_20261015.json；该存档是原件路由，不代语义核验。

## 6. 后六门实际决定域／版本角色分开

以下是后续实际读取，不将§5当时未读改成外部受阻；均未评分或认证当窗公开日，不把current内容回填v1。只如下必要域，不宣其余附件已读：

- **2512.00045 RTL-to-spec，窄P**：[v1 HTML](https://arxiv.org/html/2512.00045v1) §3.3.2–3.3.3 L125–140、§4.4.2/§5 L232–244。重建器只看生成spec，pass@1 RTL与golden共用testbench；reset同步/异步实例中高judge分仍可对应行为失败，故有具体评价盲点而非只hardware文档应用。重建器可能自己犯错，testbench通过也非完整形式等价，不采oracle可靠/普遍准确率；search元字段明确December公告另责，不由Submitted给Nov18。
- **2511.14043 AISAC，v1 C／晚v3具名不同方向保留**：实际读[v3 HTML](https://arxiv.org/html/2511.14043v3) §2–4 L60–143的driver无tool edges、depth与hard caps、memory/trace设计；当前AB“四保证”与正文“两hard、两objective”不等。为这个具体版本混淆，只读[v1 HTML](https://arxiv.org/html/2511.14043v1) L66–143及§4/5 L184–283：v1自限LangGraph/FAISS/SQLite、role prompts、tool-less planner、hash增量index与项目bootstrap的科学工作流集成，未披露能改变通用执行解释的新约束机制/成立反证，故原v1 C提案，不因Science标签直接关。官方[abs history](https://arxiv.org/abs/2511.14043)显示v2最早Submitted2026-02-06、v3为03-27，只作这些精确版本不能早于目标日的下界，不冒公开日；v3更强执行架构是未来归属线索，不能反填2025，未处理该未来日或全版本差异。
- **2511.13410 Mem-PAL，窄P**：实际读[current v2 HTML](https://arxiv.org/html/2511.13410v2) H2Memory L156–185/201–208及紧邻消融表。log关系→situation→background与dialogue topic→principle分层，有具体映射消费：检索近期situation再关联background，检索长历史topic再关联principle；不是只命名“heterogeneous”。保留表示组织/检索消费选择，派生Caused_by/requirements不是事实或真因果，未授quality/latency普效。该层是v2必要准入，未宣v1相同、v2重要修订落窗或已标准审阅。
- **2511.13293 GHAR，窄P**：实际读[v1 HTML](https://arxiv.org/html/2511.13293v1) III-B–F L169–245及Algorithm1 L248–292。Top决定LLM/RAG、meta-path及continue，Low总结被选subgraph；共享参数PPO有role rewards，另将正确rollout的相反检索决策记录为negative路径供对比，而非只医疗角色串联。保留这个训练/检索决策信用对象，不采医疗预测效果；token-overlap reward不授faithfulness，所印rank公式/负例不是因果反事实正确性证明。未扩临床实验或断言对照已可归因。
- **2511.13103 STACCA，窄P**：实际读[current v2 HTML](https://arxiv.org/html/2511.13103v2) IV-B–C L263–315及紧邻假设L259–262。固定他agent动作，对本agent候选动作分支环境，计算reward+gamma V(next)再减policy加权baseline、按同一步各agent归一后用于PPO；是学习模型信用对象的具体替代，不因非LLM/网络控制或小实验一概关。它依赖可构造分支next-state/reward的环境与离散枚举/采样，不是只拿V即可作反事实，也不能搬到无分支oracle的LLM rollout；不采局部O(1)/全体成本普适。v2最早2026提交，必要机制准入不冒v1或Nov18已公开。
- **2511.21707 WMLM，窄P**：实际读[v1 HTML](https://arxiv.org/html/2511.21707v1) III-A/IV–V L101–139。实际没有披露新RF codec；是按场景选择anchor、专属encoder contrastive对齐后接Transformer与task heads，beam/vision anchor和联合表示有明确比较，提供anchor选择/可用模态条件的窄表示问题。保留这项选择边界，不把新wireless领域或2.4B数目本身算贡献；不授任意跨场景泛化/无视觉通用能力或anchor单因果，未读所有通信应用。

九门作者提案至此为**6窄P、3C（含AISAC原v1）**；AISAC晚v3是家族内未来修订方向，不能与原v1 C互相覆盖或再加本日家族。与原38P合为44新潜力方向，正式当窗数仍未定；先前9minimum标签保作历史轨迹，不说已独核通过。请root转Ohm优先核这些决定域及APD新评价反侧/两C，不重前64AB或所有实验；必要current/日期/Source出口及完整six继续普通。

## 7. Ohm18实际读回／九门准入层闭合

作者已实际完整读回Ohm§18：后六必要决定域通过，九门最终6P/3C、AISAC仅原v1 C/晚v3角色分开。Ohm对Mem-PAL及STACCA额外实际核精确v1，作者此前只读current v2，故按真实非作者版本/命题层复用，不冒作者已读v1，也不重同命题方法。至此有效78＝66新AB（44P/22AB-C）＋10title-C＋2旧重合；九门不再普通队列。剩余current/必要安全/日期/来源尾部与six仍待实际独核，不以准入层完成授标准Evidence或确定当窗。
