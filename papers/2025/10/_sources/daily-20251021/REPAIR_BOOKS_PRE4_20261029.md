# B15–19 完整 PRE 提案

只申请下面五处精确自然段、独立marker和本人完整末注，不申请整章锁。必要层R6/8/10/11/15/16与writer W11/12 key已成；实际owner/完整直接邻接已读，Books三上下文、ROADMAP与Ch24/27/75/77交接均已重载。未写Books，不预签POST。

## B15 15047 / MULTIMODAL-WORLD-MODELS Ch25

文件：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`，原训练期未来辅助分支`<!-- source-family:SF-2025-ARXIV-2510-12796 -->`后、`## 在谈 State 之前，先声明预测 Channel`前。原段只分辅助未来预测与部署生成；新增具体差额是自交互trajectory的thought状态用环境真值校正后产生SFT标签，而非自产状态自证。

完整新增正文：

预测状态也可以先成为可校正的训练标签，而不是部署时另跑一个外部模拟器：让agent自交互收集带当前/下一状态描述的trajectory，再用环境ground-truth替换这些描述中的状态，先监督适配内部表示，随后才用环境回报更新policy。[SPA首版的受限分支](https://arxiv.org/html/2510.15047v1#S3)改变的是监督来源与训练次序，不是让同模型的belief证明环境真实；部署没有独立world-model模块，也不等于内部状态已具可校准的反事实动力学。格式相同而坐标随机的对照会退化，更多SFT epoch亦是额外预算，不能用相同RL步数批准同总费用。环境状态权限、描述schema、筛选人口、SFT checkpoint与RL版本须共同保存，全部交互、状态校正、训练和独立闭环回归都计费；状态标签、随机性或格式支持失配时，保真实观测、短horizon反馈与原policy，不由更高游戏成功率签发真实物理状态或控制安全。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15047 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15047` — Daily2025-10-21补Oct20；writer首次exact-v1§2/3/4.1–4.4/7，Lorentz R15 key，2+1+2=5，环境真值→thought状态监督接口深入。限Qwen/Llama与三text games，保random-coordinate collapse、初始policy/format筛选、更多SFT费用和stochastic限制；不采用内部belief即真实world model或物理安全，未核实现/复现。

## B16 15189 / MULTIMODAL-EMBODIED-VLA Ch26

文件：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，原双actor传递段`<!-- source-family:SF-2025-ARXIV-2510-12560 -->`后、以“当更新目标确实需要 action likelihood 时”开头的原段前。原论证是actor参数交接；新增是相似初始scene内实测最好reward动作生成离散监督标签，再周期重放与PG并行。

完整新增正文：

模仿标签还可由在线实际试过的动作产生，而不由另一份actor参数直接传递：在相似初始scene内保留实测reward最高的动作，把它的离散位置/朝向标签用于该组状态，周期性以交叉熵重放，同时继续policy-gradient探索。[RM-RL的受限分支](https://arxiv.org/html/2510.15189v1)将环境测量、标签生成和两种更新分开；较高reward不是专家真值，初态相似也不证明动作可跨状态无损转移。固定目标pose、预规划放置轨迹与历史预训数据仍是额外权限，不能称无需参考或从零自学；标签覆盖陈旧时还可能固化过去赢家。Scene相似规则、reward/动作量化、采集时间和replay版本须共同保存，全部预训、试验重置、环境采集与训练均计费；支持、估值或控制质量失配时，保可信示教、原policy和独立controller，不由有限机器人任务的成功率批准任意操作或物理安全。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15189 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15189` — Daily2025-10-21补Oct20；Lorentz首次exact-v1 III-B/C、IV-A/B/C，writer核III-C1/2，2+1+2=5，同scene实测reward动作→重放标签差额深入。限XARM6/D435/RTX4060与cell-plate任务，200历史样本、每轮采集2–3分钟/约7h训练均收费；不采未核53%宣传、任意6DoF迁移或安全保证，未核实现/复现。

## B17 15191 / AGENT-RAG Ch76

文件：`books/part-07-agent/76-rag.md`，本日已POST的AutoGraph-R1 `<!-- source-family:SF-2025-ARXIV-2510-15339 -->`后、`### Checker Reward 不能同时充当训练信号和独立证据`前。前段训练constructor的图目标分流；新增为结构块单独作为二次consumer输入的充分性reward，不重复carrier/index目标。

完整新增正文：

训练结构化产物还可以直接检验“删掉原context后，这份结构是否足以支持当前问题”：先生成思考、结构与答案，再仅把结构块交给第二次回答，用答案匹配信号训练第一次结构生成。[Structure-R1的受限分支](https://arxiv.org/html/2510.15191v1#S3)把结构的消费资格变成反馈，而不只奖励可解析格式；但同模型的二次回答不是独立事实来源，当前问答可恢复也不证明结构忠实保留原文或支持所有未来查询。更高结构reward权重会使部分任务退步，额外reinference、gold QA与训练均须付费。原context/结构schema、两个consumer条件、reward与checkpoint应共同保存；充分性、事实支持或净预算失配时，保原文回读、普通检索与独立checker，不让自我答对替代来源证据或把派生结构升格为事实。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15191 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15191` — Daily2025-10-21补Oct20；Lorentz首次exact-v1§3.1.2–3.2.4/4.1.1/4.2/4.3，writer核§3.2.3/4.3，2+1+2=5，仅结构再消费的训练接口深入。保同模型EM非独立事实、7K+7K与局部1000采样、lambda .3反退和reinference全费；不采用§3.3因果理论或通用充分性，未核实现/复现。

## B18 15683 / AGENT-RAG Ch76

文件同B17，在原EBCAR完整段和`<!-- source-family:SF-2025-ARXIV-2510-13329 -->`后、`## Offline Ingestion 不是预处理细节`前。现有段说明离线embedding与在线候选交互；新增是post-transformer表示expert的训练路由与推理聚合模式分别定义编码/索引资产。

完整新增正文：

检索encoder增加expert容量时，还须分开训练时的路由与建库、查询时实际运行的模式。先由共同Transformer产生表示，训练时以带噪top-1选择post-transformer expert，推理却可以继续TOP1或运行ALL再聚合；[SB-MoE的受限分支](https://arxiv.org/html/2510.15683v1)中，这两种variant不是同一份质量/费用合同。稀疏训练不证明ALL推理少算，ALL的收益也不能回签TOP1；改变expert/聚合模式后，document向量、query编码和索引须共同重建或重验，不能只换查询端。更多expert与更大base仍可反退，单seed及不同训练日程不授容量普效。全部训练、文档重编码/刷新、expert驻留与在线检索回归均付费；表示、模式一致性或净预算不合时，保原dense encoder、匹配索引与原文核验，不由稀疏标签或局部排名签发全链加速和事实支持。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15683 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15683` — Daily2025-10-21补Oct20；writer首次exact-v1 III/IV setup/T1/V–VII，Lorentz R16 key，2+1+2=5，retrieval expert训练/推理模式与索引资格差额深入。明确TOP1/ALL两variant、ALL收益与费用不回签TOP1；保大Contriever反退、单seed42与不同epoch预算、100k docs非per-query计算。未核实现/复现，不授同预算普胜或生产SLO。

## B19 15720 / MULTIMODAL-EMBODIED-VLA Ch26

文件同B16，在坐标归一化节中以“这增加 pose 同步、坐标变换与漂移检测成本”开头的完整段后、以“相机、深度图、机器人基座与末端执行器各自拥有坐标系”开头的原段前。原段分CMDP软代价与独立controller；新增为风险budget状态/critic误差消费条件，而非已实现确定hard-veto。

完整新增正文：

若约束对象是期望折扣cost，还可把剩余风险预算加入state，再由shield在原policy与最小cost-critic动作间混合。[ProSh的受限分支](https://arxiv.org/html/2510.15720v1#S3)把策略收益与预算消费分开，但其保证依赖初始预算条件、有效slack及全state-action域的critic最大误差界；训练MSE小不能替代这个界，单条trajectory或某次动作仍可能越限。最优性又有deterministic CMDP与误差趋零等额外前提，不从一般TD3训练自动获得；SafetyGym的局部均值改善还保留环境反退与波动越线。Budget更新、cost定义、critic版本/误差假设和实际控制时钟须共同验收，全部critic训练、shield计算、rollout与真实安全回归均计费；没有可用误差界或部署支持失配时，保守动作集、原policy与独立物理controller仍必要，不由期望约束批准每次执行安全或实机部署。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15720 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15720` — Daily2025-10-21补Oct20；Lorentz首次exact-v1§3.2 Theorem5/8、§4 Theorem1/Remark1与§5.1/5.2，writer核Theorem5，2+1+2=5，期望风险预算/critic sup误差接口深入。保初始budget、2Delta/(1-gamma)条件与正文slack口径差异，不抄完整recipe；三seed/SafetyGym有reward反退与cost波动越线，非每轨迹硬安全。未核实现/复现，shield端到端硬件成本Not Disclosed。
