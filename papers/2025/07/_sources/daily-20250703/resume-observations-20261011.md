# 2025-07-03 补查续跑：新增题摘与网页观察

作者：root / Codex。2026-10-11 10:04 BJT 前后实际读取下列官方精确 v1 的完整题名、摘要、comments/history；入口为每行链接。网页工具返回可读正文，不声称已下载为本地 raw 或独立复现实验。此前 38 份本地 v1 中的首 14 复用 Bernoulli 校准，额外 23 正独立校准，00460 撤回另列。本文的 22 份与这 38 份不重复；13 项来自此前已浏览的 cs.CL 月表前 25 标题，6 项来自六主题结果，另 2 项因标题含糊补摘要，SAFER 单列版本。没有把月表 1672 或查询库存 90 转成逐项全文队列。

P 仅指贡献潜力，C 是具体贡献关闭，V 是必要版本隔离；均非已确认 July02 候选。不评分，不授正面 Evidence/Books。公开日没有由 submitted 或 ID 算出；先前旧候选/有效证据保持。下列作者初判等待非作者校准，不能当最终验收。

| 精确身份与入口 | 作者初判；约束 → 增量 → 待核选择及限制 |
| --- | --- |
| [MoNE 2507.00390v1](https://arxiv.org/abs/2507.00390v1) | P。所有专家常驻容量高 → 访问频次与输出方差联合挑冗余专家、轻量 novice 估计输出 → 压缩不能只看路由冷热；三类校准条件稳定性待核，不采用摘要准确率。 |
| [VQ-VLA 2507.01016v1](https://arxiv.org/abs/2507.01016v1) | P。动作 tokenizer 的数据规模与迁移受限 → 合成轨迹扩大 VQ 动作表示训练 → 重估动作编码/真实域差距；零样本及长任务结论须按实际机器人/任务核，不将两真实任务外推。 |
| [WebArXiv 2507.00938v1](https://arxiv.org/abs/2507.00938v1) | P。动态网页评价不可复核、历史反思固定 → snapshot/确定答案与按决策选择历史 → 评价稳定性和记忆选择的联合条件。**v1 是 275 tasks，不是查询当前摘要的 510**；不得混用 v2。 |
| [MIV-head 2507.00401v1](https://arxiv.org/abs/2507.00401v1) | P。冻结/黑盒骨干不可微调 → 多实例验证 head 跨域少样本适配 → 表示适配成本与骨干访问权限的边界；已披露 CNN/ViT ImageNet 条件，不推所有闭源 LLM。 |
| [Driving Video 2507.01264v1](https://arxiv.org/abs/2507.01264v1) | P，受限设计/反证线索。脚本控制和画面真实感不同 → Scenic/CARLA 给结构，再用 Cosmos-Transfer1 条件化画面 → 重新检查“真实画面=保留物理事件”的判断；实际必要读段见下文，不授安全证明。 |
| [Robotic BDD 2507.05125v1](https://arxiv.org/abs/2507.05125v1) | C。DSL/知识图谱/BDD/Isaac Sim 对现成 pick-place 程序生成验收测试；正文摘要未建立 foundation/VLA/world-model 机制或其特有可靠性增量。不是因为机器人学、日期或无 owner 排除。 |
| [TableEval 2507.00152v1](https://arxiv.org/abs/2507.00152v1) | P。平均多模态分数掩盖领域/格式困难 → 五格式、科学/非科学表格跨域对照和 context 相关性 → 重估表示与评价切片；研究对象是模型表格能力，不因含科学表格而误作 AI for Science。 |
| [LineRetriever 2507.00210v1](https://arxiv.org/abs/2507.00210v1) | P。语义检索/底部截断损失动作相关观察 → LLM 按 planning horizon 选观察行 → 语义相关不等下一行动所需上下文；selector 额外成本与执行成功边界待核。 |
| [Reasoning-Infused 2507.00214v1](https://arxiv.org/abs/2507.00214v1) | P，窄监督对照线索。标签训练与 rationale 训练混写 → 答案条件生成 rationale、下游 Q→RA 与 Q→A 对照 → 验证监督形式作用与答案合理化；只给单 emotion 数据集，不采用普遍泛化口号。 |
| [RASTA 2507.00216v1](https://arxiv.org/abs/2507.00216v1) | P。语义翻译不保证听者理解风格 → 学得风格概念的检索式对齐与文化/语言失效反侧 → style transfer 的评价对象需另定；不等通用文化理解保证。 |
| [Refused Knowledge 2507.00239v1](https://arxiv.org/abs/2507.00239v1) | P/安全反侧。直接拒答不等知识消除 → hidden-state 线性 probe/base→aligned 迁移及间接比较相关 → 对齐抑制与表征遗忘应区分；相关不证因果、预测到偏见值不证明现实事实。 |
| [EfficientXLang 2507.00246v1](https://arxiv.org/abs/2507.00246v1) | P。英文默认推理预算 → 七语言/三模型对照，翻回英文后仍有 trace 差额 → token 预算同时受语言/多语言基础影响；不以 token 减少替代 latency/cost 实测。 |
| [Finetuning Memorization 2507.00258v1](https://arxiv.org/abs/2507.00258v1) | P/隐私反侧。微调效用不等隐私风险 → prompt/parameter 方法 membership inference 对照 → 参数更新方式与记忆风险须联合评价；低 MIA 风险不等 DP 保证或所有泄漏不可发生。 |
| [Failure by Interference 2507.00322v1](https://arxiv.org/abs/2507.00322v1) | P/设计反侧。错误不必等于无正确部件 → heads/FF 的可靠与错误贡献竞争、RASteer 干预 → 机制存在与最终输出可靠性不同；仅 124M～7B/括号及局部算术，不授任意推理可修复。 |
| [Question Decomposition 2507.00355v1](https://arxiv.org/abs/2507.00355v1) | P，局部成立条件。多跳证据分散 → 子问题检索联合 cross-encoder 去噪 → 成熟模块组合若改变覆盖/噪声取舍仍可核；预算、公平 baseline 与额外 LLM 调用待证。 |
| [CAPITAL 2507.00389v1](https://arxiv.org/abs/2507.00389v1) | P。CoT 多数投票可能有虚假相关 → front-door 分解、聚类/NWGM/对比学习近似 → 因果识别假设与 prompt 选择应分开；不能用因果命名授真实世界因果保证。 |
| [Ad Co-Evolution 2507.00509v1](https://arxiv.org/abs/2507.00509v1) | P/安全反侧。检测分数与内容可信混同 → 合成检测器反过来指导 SFT/BoN 的隐蔽广告 → 评价器被优化后的对抗适应边界；不传播欺骗操作或声称通用攻击成功率。 |
| [Low-Resource Transfer 2507.00601v1](https://arxiv.org/abs/2507.00601v1) | P 拟，准入事实待校准。少标注跨语言适配 → knowledge alignment loss/soft prompt/冻结联合 → 是否有超出成熟组件的新成立条件；摘要只述对照/稳定性，不授具体公式或不遗忘保证。 |
| [Mixture of Reasonings 2507.00606v1](https://arxiv.org/abs/2507.00606v1) | C 拟。生成 CoT/ToT 模板再做 SFT，摘要未提供新的自适应 selector、预算公平性或模板成立条件；微小指标不是排除理由，“不需要外部 task prompt”不证明内部自主策略选择。 |
| [African Languages 2507.00297v1](https://arxiv.org/abs/2507.00297v1) | P。web 噪声/未见低资源语言 → 数据质量与表示有效性、少单语数据迁移对照 → 重估“大语料足够”的条件；博士论文可能包含更早公开家族，首次公开身份需核，不因体裁或语言关闭。 |
| [Capsule Intent 2507.00540v1](https://arxiv.org/abs/2507.00540v1) | C。成熟 CNN/capsule 动态 routing/margin loss 用于 intent 分类，摘要没有新通用表示机制或改变 foundation-model 设计的可比有效性证据；不是把所有小模型理论排除。 |
| [SAFER 2507.00665v1](https://arxiv.org/abs/2507.00665v1) / [当前版本](https://arxiv.org/abs/2507.00665) | V。v1 有 SAE 特征→偏好数据改动的安全潜力；v2 2025-10-14 withdrawn，当前 v3 2026-01-30重新有正文。旧版本门未解除，不把 v2 撤回泛化成全部版本均撤回，也不以 v3 恢复反填 v1。等待影响早期结果的作者澄清，现不评分/采用/Books。 |

仅标题可明确范围外的月表条目：00244 morphosyntax 的语言结构代数、00380 chant 的 Bayesian 分段、00547 topic-modelling 方法论，均没有本次基础模型具体线索，不送全文队列；不声称其没有学术贡献。

## 必要核心：Driving Video 的实际采用边界

实际读 [2507.01264v1 HTML](https://arxiv.org/html/2507.01264v1) §III-A、III-B、IV-A/B。Scenic/CARLA 负责可执行场景；segmentation/depth 的叙述与实验 edge/depth 不完全一致。Cosmos-Transfer1-7B、H100、50去噪步、control .8 是作者本例配置。三类碰撞示例和定性视频展示不足以证明所有物理事件保真、AV 闭环安全或 sim-to-real 泛化；从脚本到生成画面还需独立检验。只保留此设计/评价问题，不采营销式可靠性，非完整候选 Evidence。独立复核可以只核这些必要段。

## 本次额外来源恢复

- [Meta Blog?page=6](https://ai.meta.com/blog/?page=6)：网页工具现成功取卡，但主体是 2025-02、2024、2023 混排，顶栏是 2026；不能把相邻数字分页当 July02 的完整历史。Research 先前 SSL/reset 原件仍独立受限。没有查询 catchup、也没有从该页无 July 卡得出零研究。
- 官方 [cs.CL July 2025 前25](https://arxiv.org/list/cs.CL/2025-07?skip=0&show=25) 与本地原件相符；这是月表标题查漏，不是日级公告。Advanced 原件明确公告日期仅年/月精度，不能由其排序推出 July02；恢复只需要可核的日级公开日期/范围，不索要秒级时间。

本次网页读取没有更改已有日期或确认新当窗事件。日期/版本到达只重开对应身份；首批14 R1/R2/PB-LLMs/安全反侧与 RAG-R1 v1已有11.1%等校正直接复用有效独核，不重复读9core。新的22项尚待独立校准，不能据此写普通待办0或DAY通过。

## 两个准入疑点的必要正文恢复

以下为root实际读取，不代替独立裁决；只解决准入问题，不计标准/深入候选Evidence。两份exact-v1 HTML均404，改用PDF。

- [2507.01067v1 PDF](https://arxiv.org/pdf/2507.01067v1)：网页首次cache miss，随后HTTP下载成功；本地PDF文本实际读§III、V、VI（物理页3～11），未验像素或复现。七年84个月的总体数据，根因标注仅覆盖部分；TableIV/V中六年总体与最近两年的优胜模型翻转，TablesVI/VII又随根因及MAE/RMSE变化。TableVIII及正文的小规模单根因fine-tuning无收益，原有训练/验证与数据归一化细节仍限制推断。潜在增量在基础预测模型的条件性反例，不在ML服务应用名或年末误差数字；不能推广为所有基础模型/微调的结论。
- [2507.02975v1 PDF](https://arxiv.org/pdf/2507.02975v1)：网页工具实际读Methods、来源对照及Limitations（物理页2～6）。三项Boolean分别判断直接回答、主题相关、答案grounding，由单LLM judge评价；两套同PubMed系统的支持率不同，但retrieval/prompt/style未控制，医疗观察数据也不是独立真值。目标问题数与表内总数不一致。只能考虑证据相关与直接支持分离的评价线索，不采用医疗有效性、通用正确率或系统因果优势。其具体增量是否超出成熟rubric，交第二批复核者定点裁决。

## 新22项独立裁决的差额

[独立准入复核§7～10](source-review-supplement-20261011.md)实际读取22份完整v1题摘及决定性局部正文，最终仍为18P/3C/1V，但00601改C、00606改窄P：前者只有成熟适配组件及未归因汇总对照；后者正文确有教师按题选择模板，不能沿用“没有selector”的宽关闭。00297中至少两条贡献已经有2020/2022更早家族，不计2025新贡献。SAFER v2撤回原因是发表审批，非已公布实验错误；v3恢复不追认v1采用。原表保留初判过程，后续以独立裁决为准，不构造第二份活跃清单。

**后续生效裁决：** [版本窄核§11](source-review-supplement-20261011.md)实际比较官方恢复状态及v1/v3必要方法，解除SAFER旧审批V门，改窄P；不把v3消融反填v1，不授实验真实性，但没有具名必要版本冲突需继续机械索要作者澄清。网页22当前为19P/3C/0V。第二批[§5](second-calibration-supplement-20261011.md)已实际独读/关键表目视，两U转窄P，23当前为19P/4C/0U；02975 limitations实际PDF p7、同1739子集对照为44.5%/21.3%，不能与总体44.6%混用。前文root页码粗定位以该独核精确位置为准。当前全部采用限制已写回日报，新增51P/8C/1撤回，不是候选/Evidence；日级普通剩余仅最终非作者DAY，不从分层结果直接继承通过。

最终恢复停点：[Ptolemy非作者DAY§6](second-calibration-supplement-20261011.md#6-july03-当前六部分最终非作者-day2026-10-11)已通过六部分安全终态，root已同步完成态和State当前13/132。完成态初检要求§5明确写“外部终态保留项”，root已将原来的“可以终态隔离”收敛为实际已隔离状态，具体请求/限制未变；随后重跑完成态V3，不沿用进行中通过。原窗口/连续§4及0正式候选保持，Books本轮新写0；本日普通待办0，不授缺口正面覆盖/Evidence或无遗漏，不stage/commit/push。
