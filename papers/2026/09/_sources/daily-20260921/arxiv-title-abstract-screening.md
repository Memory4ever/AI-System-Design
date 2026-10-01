# 09/21 补漏完整题摘裁决（作者工作记录）

**当前终态见正式Daily142与唯一evidence末最终冻结节；下方未审/待采用数字是初筛过程快照，不是普通未完队列。** 末六negative抽样纠正21953/21629/21749/21259四误关，均已获得必要审阅与具体Books处置；未变明确关闭保理由，未扩大475宽库存。21468/20873关闭独立通过。

访问日期：2026-09-27。以下 **53 个身份**均实际完整读取官方 `https://arxiv.org/abs/<id>v1` 题名、摘要及页面可见 Comments；完整题名对应 [官方标题底稿](./arxiv-mon21-titles.md)。逐ID与旧67迁移表交集核得 **21299/21465两条旧未决重开 + 51条额外身份**，合并完整题摘层为118个身份，不是120或最终贡献候选。额外51暂为9个具体贡献前关闭、1个更早公开家族关闭、41个仍需必要证据/实际处置的工作信号；本表还包括两条旧未决，共43工作行。评分在准入确定后填写，未评分不是零分。

本窗按官方 Mon21 公告批次定位，见 [恢复记录](./arxiv-recovery-20260927.md)。更早渠道/版本例外单独处理，不以 submitted 字段替代公告。题摘中的机制是待核主张，不冒充事实证明；没有逐篇检索完整发表史，也没有将475个宽列表身份逐篇全文阅读。

## 实际题摘与最小必要消歧

| 精确 v1 身份 | 具体准入问题或关闭理由 | 已投入 / 当前状态 |
| --- | --- | --- |
| [20981 CaLR](https://arxiv.org/abs/2609.20981v1) | 潜在因果拓扑与隐式微分如何限制 latent revision，而不是仅增加并行思考长度；须核 teacher/oracle 与因果措辞。 | 完整题摘；必要方法待审。 |
| [21001 MCR2 limits](https://arxiv.org/abs/2609.21001v1) | 相同 coding-rate 最优目标仍可保留环境相关特征并在反转相关性时失效，是 objective→OOD 设计反证而非新增榜单。 | 完整题摘；必要定理/反例待审。 |
| [21113 representation/importance](https://arxiv.org/abs/2609.21113v1) | 表示 drift 与 EAP causal importance 不等价、跨任务定位重叠不保证 transfer，改变诊断代理的解释边界。 | 实际读精确HTML §3–5；实际 Books 命题对照待做。 |
| [21126 layerwise sparsification](https://arxiv.org/abs/2609.21126v1) | 层内归一与外层组惩罚的分离可能避免 joint pruning 失稳；须确认是新适用条件还是局部实现 operating point。 | 完整题摘；不因 OPT1.3B 自动拒绝，也不先标长期知识缺口。 |
| [21139 TinyCeNN](https://arxiv.org/abs/2609.21139v1) | 逐层冻结前次已接受替换、当前学生校准、四门一致才提交；NLL 通过而 representation 失败是实际反例。 | 实际读HTML IV–VII；研究 wrapper `use_cache=False` 且 baseline 更快，不能从分析 state 推部署收益。拟标准/仅报告，待处置。 |
| [21183 proactive AudioLLM](https://arxiv.org/abs/2609.21183v1) | 将 interrupt/silent 作为受监督事件，联合 onset、维持与重复抑制，而非只缩短音频延迟。 | 完整题摘；须核事件粒度及与已有 duplex 表示/控制分工差异。 |
| [21190 SWE-Proof](https://arxiv.org/abs/2609.21190v1) | 机器证明与 known-patch 引导的自建 specification/axiom 分开，检查机械正确但任务不忠实的主要失效。 | 完整题摘；证明/规格接口必要证据待审，不称机械证明等同用户 intent。 |
| [21216 Coda](https://arxiv.org/abs/2609.21216v1) | 冻结 flow policy 的少步输出经 endpoint corrector 修复，须区别 source-noise conditioning、更多 solver steps 与缓存收益。 | 完整题摘；必要 Method/eval 待审。 |
| [21220 INSPO](https://arxiv.org/abs/2609.21220v1) | 在生成 policy 的输入 noise 空间搜索约束动作，改变直接 action projection 的支持范围；不是物理安全证明。 | 完整题摘；约束及成本必要审阅待做。 |
| [21228 FOCAL-VLA](https://arxiv.org/abs/2609.21228v1) | 几何/未来状态 teacher 仅训练期供潜表示，需核 privileged supervision 与部署观测的责任交接。 | 完整题摘；局部方案 operating point 不能自动称知识缺口。 |
| [21247 MT reasoning traces](https://arxiv.org/abs/2609.21247v1) | 描述翻译任务 reasoning taxonomy 与分布，没有受控的新机制/设计反证；单任务分析不能凭可映射 Evaluation 保留。 | **贡献前关闭**；不否定翻译研究价值。 |
| [21251 CAT](https://arxiv.org/abs/2609.21251v1) | 切向/法向曲率预算与 Armijo/dual step 分工可能改变 guidance 稳定条件；须核局部理论假设。 | 完整题摘；必要公式/限制待审。 |
| [21259 CogGym](https://arxiv.org/abs/2609.21259v1) | sampling重复调用与verbalized人群分布是不同estimand，Gemini配对与重复数对照修正以mean拟合认知分布的评价盲区；原不含internalmechanism不足为关闭理由。 | **误判修正→标准5/窄E**；peer必要source→actual Ch66“能描述分布”通过，不称整CogGym配方覆盖。 |
| [21268 Edit-VAR](https://arxiv.org/abs/2609.21268v1) | 源条件概率替换、stage/token 调制与残差剪枝，须核 source preservation 与生成控制的独立条件，不只看编辑指标。 | 完整题摘；必要机制待审。 |
| [21281 personalized retrieval](https://arxiv.org/abs/2609.21281v1) | GPU/CPU personalized search 的广深组合服务应用，摘要未给改变当前大模型/RAG 主线的新机制或反证。 | **贡献前关闭**；不因 GPU 字样直接选入。 |
| [21299 BrainAPI](https://arxiv.org/abs/2609.21299v1) | OPA/Cedar 到声明式 decision artifact 的规则覆盖、作用域与 default 极性，是治理 DSL 迁移的具体语义反证。 | 实际读HTML §3–4/11.1–11.6；audit记录不等正确性，ranking/context未完整实现，待实际owner对照。 |
| [21325 LEGIT](https://arxiv.org/abs/2609.21325v1) | signed配置/task/budget与cost记录是既有身份原则；Sybil deposit/fee 属市场机制，题摘未新增可执行 acceptance/失效合同。 | **贡献前关闭**；root独立完整题摘校准。不是说 signed credential 无价值。 |
| [21362 factorized syllables](https://arxiv.org/abs/2609.21362v1) | onset/rime/tone 同位置三头预测改变 atomic-token接口与长度/词表取舍，而非只换汉语 tokenizer 名称。 | 完整题摘；必须核 fallback、语言及 prediction-head 成本。 |
| [21383 depth dynamics](https://arxiv.org/abs/2609.21383v1) | 共同平移/方向及 pair-gap 随深度变化，需核回顾轨迹的 qualifying depth 是否能支持在线停止；不能倒推可部署 oracle。 | 完整题摘；必要评价待审。 |
| [21407 QuAKE](https://arxiv.org/abs/2609.21407v1) | 历史 denoiser 窗口的 Gaussian state-space posterior 会同时修正历史状态，再交给原 solver，不是简单 refresh。 | 实际读HTML §2–3/4.1、Table1/Fig4；剩校准/消融必要成本待核，见证据记录。 |
| [21422 Brownian heads](https://arxiv.org/abs/2609.21422v1) | same-sample 特征选择与固定 head 的复杂度成本不同，是受条件理论边界而非现代 LM 泛化保证。 | 完整题摘；标准理论审阅待做。 |
| [21423 DENSE](https://arxiv.org/abs/2609.21423v1) | shortcut tree 保留证据与 unresolved obligations，outcome-blind/reset recipient 对照可检查压缩反馈是否仍有效。 | 完整题摘；必要构造与反证待审。 |
| [21465 OmniVChat](https://arxiv.org/abs/2609.21465v1) | 参考回复依据 accepted rendered media 而非原脚本；tier gate、固定参考历史和最终轮评分需区分真正交互。 | 官方PDF实际恢复p1–7/§2–4.1；非 live interruption，后续reward/评价页普通恢复待办，不称整家族不可取。 |
| [21474 MT-WAM](https://arxiv.org/abs/2609.21474v1) | future visual teacher 与 action-conditioned future motion 两路用途不同，运行时一次预测不能冒称已掌握物理 dynamics。 | 完整题摘；必要表示/训练交接待核。 |
| [21482 epistemic truncation](https://arxiv.org/abs/2609.21482v1) | ensemble/dropout epistemic signal 在 warm-up 后控制离线 imagined rollout 长度，须核过早停止/模型偏差与误差阈值。 | 完整题摘；step saving 不等真实GPU成本，标准审阅待做。 |
| [21484 HE-Guardrail](https://arxiv.org/abs/2609.21484v1) | 密文输入让 server 不可明文 guard；密文 response-return gate 与近似门 residual 产生新保护边界。 | 2+2+2=6保护深入例外；必要III/IV已读，Ch72真实gap提案待非作者采用核。 |
| [21509 communication bottleneck](https://arxiv.org/abs/2609.21509v1) | exact symbolic round-trip 分开生成器/提取器错误并对称测试编码通道，改变以最终答案掩盖信息丢失的测量。 | 完整题摘；必要协议/成本待核。 |
| [21515 ServeGuard](https://arxiv.org/abs/2609.21515v1) | monitor盲子空间→受限LoRA read factor→承诺/证明→实际adapter bytes admission，保护范围与来源身份不等同。 | 2+2+2=6保护深入例外；必要§3/5/6/7/9已读，Ch72真实gap提案待非作者采用核。 |
| [21523 task/state frontier](https://arxiv.org/abs/2609.21523v1) | finite linear-task advice partition 的 exact rank/state frontier 可给压缩何须保留任务信息的条件分支。 | 完整题摘；不扩成任意LLM容量定理，标准理论审阅待做。 |
| [21525 IncentRL](https://arxiv.org/abs/2609.21525v1) | 本次重开并读§1–4.1，作者明言standard bounded-reward perturbation；有限discounted MDP/full-support q的value bound与strict-action-gap条件是成熟理论应用，distance proxy未校准、Beta外循环fit非Bayesian、未建立KL-specific或信息匹配的新选择机制。 | **贡献前关闭（2026-09-30重新校准）**；root独立定点核§1/方法通过。保留ties/support-mismatch反例，不按无LLM/小模型或审阅费时拒绝。 |
| [21527 OpenMAS-GCom](https://arxiv.org/abs/2609.21527v1) | matched budget 下拓扑、角色、消息腐化与worker失效分开干预，可以改变以总成功率选择multi-agent图的测量。 | 完整题摘；干预是否真正触发及归因须必要审阅。 |
| [21533 MACE](https://arxiv.org/abs/2609.21533v1) | functional memory unit 与presentation format共同按outcome更新，不能把单位价值与格式价值独立相加。 | 完整题摘；必要控制/反馈环待核。 |
| [21629 multichannel images](https://arxiv.org/abs/2609.21629v1) | independent masks改变compactindex与真实grid位置对应；equal-k assignment与star多通道配对修复structured attention接口，不能因显微/遥感实验领域拒收泛机制。 | **原关闭误判已纠正**；必要§3–5/actualCh23/literal root PRE与实际两段/邻接POST均通过，整合完成。共同patch必自配断言反例隔离，不全recipe保证。 |
| [21656 JEPA geometry](https://arxiv.org/abs/2609.21656v1) | Gaussian uniqueness依赖Euclidean latent几何，spherical目标有另一恢复条件；挑战“分布结论不依赖表示几何”。 | 完整题摘；具体条件/反例必要审阅待做。 |
| [21672 L0-MoE](https://arxiv.org/abs/2609.21672v1) | dense专家独立domain训练、冻结non-MLP的L0结构构造后拼装，改变专家形成而非只宣传推理速度。 | 实际读HTML §2–3/4及限制；sequence-domain/token-router偏差和总参数成本保留，真实Ch21对照待做。 |
| [21677 GUARD](https://arxiv.org/abs/2609.21677v1) | unlearning安全CoT轨迹与稳定答案guidance再distill，检查仅止泄漏却破坏正常回答的失效。 | 完整题摘；保护深入例外，必要威胁/效用审阅待做。 |
| [21704 SpecQuant](https://arxiv.org/abs/2609.21704v1) | official Crossref同题DOI published-print=2026-03，ICPC2T活动03/11–13；September arXiv不是新家族首发。 | **更早家族关闭，不评分/不入当窗候选**；精确March日不假造，created Aug19不是公开时间。 |
| [21740 Sandwich-Residuals](https://arxiv.org/abs/2609.21740v1) | frozen world backbone 外围 prediction-error residual 是 test-time 更新职责分支；须区分观测误差适配与真实动力学。 | 完整题摘；标准必要证据待做，不仅按少参数保留。 |
| [21749 GraphSkillEvo](https://arxiv.org/abs/2609.21749v1) | globalguidance/node/path的优化scope与消费graph组织分别受控；graph-stripping保guidance与nodes、mutation/crossover预算匹配给局部结构/搜索证据，非仅DAG+GA成熟组合。 | **原关闭误判修正→深入5/窄I**；peer必要source→freshCh81及两段POST通过。schema不授权effect，LiveMath/各任务cost反侧保留。 |
| [21787 compact/moving geometry](https://arxiv.org/abs/2609.21787v1) | 可干预低维结构随recurrent Jacobian传递而移动，不等于固定/dynamically closed状态空间。 | 完整题摘；受控GRU/LSTM机制边界必要审阅待做。 |
| [21849 Weight Is Over](https://arxiv.org/abs/2609.21849v1) | posthoc文本encoder替换需对齐共享tokenizer与translator；feature cosine不可当最终图像质量。 | 实际读HTML §3/必要§4–5：GPU encoder原不在critical path时主要省memory；质量反例/187M translator成本保留，标准待处置。 |
| [21888 ETD](https://arxiv.org/abs/2609.21888v1) | loss与entropy调整的membership sensor需对照均值/方差与真实成员标签，不能把likelihood等同训练暴露。 | 完整题摘；具体估计器标准必要证据待做。 |
| [21899 ExpBoN](https://arxiv.org/abs/2609.21899v1) | finite-n exponential-noise选择与生成器采样的分解，需核选择偏差和预算估算而非直接宣称同计算优于BoN。 | 完整题摘；必要公式/预算待核。 |
| [21924 active re-ID questions](https://arxiv.org/abs/2609.21924v1) | 人物检索问题策略应用成熟闭环VOI，题摘没有独立新的foundation训练机制或受控反证。 | **贡献前关闭**；不因Agent措辞自动保留。 |
| [21941 hard-label extraction](https://arxiv.org/abs/2609.21941v1) | hard label下sign recovery的query职责与end-to-end恢复不同，须限定浅/窄ReLU模型及查询假设。 | 完整题摘；保护深入例外，不宣称可抽任意LLM。 |
| [21948 GALA](https://arxiv.org/abs/2609.21948v1) | 3D end-effector codec与视觉latent共同承担cross-embodiment预训，action-free数据与真机执行分开。 | 完整题摘；必要codec/数据责任待核。 |
| [21953 RACER](https://arxiv.org/abs/2609.21953v1) | query-conditioned、class-role正确率与coherentrelabelinvariant接口改变专家能力估计；routing score不等概率，不能按医疗应用/无serving关闭。 | **原关闭误判已纠正**；必要§2–4/关键proof及freshCh66/literal root PRE与实际两段/邻接POST均通过，整合完成；稀疏context/summary充分性/OOD人口反侧保留。 |
| [21960 tau-leaping schedule](https://arxiv.org/abs/2609.21960v1) | 因子化误差与schedule-dependent profile的常数/阶数分离，可能改变只按名义步数选采样器的判断。 | 完整题摘；理论正则条件/评价必要核查待做。 |
| [21996 lie detector](https://arxiv.org/abs/2609.21996v1) | 内部可读识别与concealment/unlearning分开测，probe成绩不直接等同内部知识真值。 | 完整题摘；可用答案/标签、干预及部署可得性必要审阅待做。 |
| [22008 DiaVLo](https://arxiv.org/abs/2609.22008v1) | SHOULD-KNOW scene reference与self-rationale triplets分离；counterfactual遮蔽/DML不能自动授予self-rationale真实内部身份。 | 实际读HTML §4.1–4.3；RK fidelity作者列future work，配对阈值换encoder；拟标准/仅报告，待最终处置。 |
| [22043 MDL](https://arxiv.org/abs/2609.22043v1) | 正交signal编码的几何稳定不等语义reliability；四action门使用heldout结果校准，拒答收益要与覆盖分开。 | 实际读HTML §3/5必要表：MDL overall hallucination高于RAG，几何不推truth；拟标准/仅报告，待处置。 |
| [22083 MintAct](https://arxiv.org/abs/2609.22083v1) | 有效域贡献由生成速度×mixed-group率决定；消费配额与quota-normalized producer背压分权，fallback改变混合保证。 | 必要HTML §3.4.1–3.4.3/4.3已读；6分真实gap深入例外，Ch33精确提案待非作者源/owner核。 |
| [22086 Designer-RSI](https://arxiv.org/abs/2609.22086v1) | frozen Agent的procedural skill扩宽/加深与用户traffic gate耦合，须核heldout/独立结果而非只在LLM judge回路自证。 | 完整题摘；必要控制/反馈范围待做。 |

## 已经定点收紧的反例

- L0-MoE 不能沿“只有速度数字”的初读关闭；实际构造是domain训练与结构约束分工。但这也不使其自动成为Books增量。
- BrainAPI不能只因现有治理主题就关闭，规则编译default极性/量词语义是原文实际反证；audit存在不等于选择正确。
- TinyCeNN/WeightIsOver/MDL没有从模型大小、标题热词或新框架名称准入；已经读到counterexample与执行路径后，先保留受限报告问题，不编造部署收益。
- SpecQuant按正式同族证据去重，不把Crossref created或September ID当首发日。

## 仍待执行的最小范围

本表43行工作信号并非43个最终候选。继续按实际增量与评分关闭局部无长期改变项；只有最低投入和Books判断落实后才移入最终Report。优先保护合同、设计反证和已明确真实gap，普通证据待办不得改名外部阻断。当前独立校准仅root明确读过21113/21325/21484/21515完整题摘，不能写所有53已非作者审阅。

## 2026-09-30有界题名查漏：45条完整题摘

只从本日475题名中补取明确大模型/多模态/训练/Agent主线及含糊新命名线索，未对所有学科条目逐项题摘或全文；此前118不能反推来源闭合。下列45个精确`2609.<id>v1`官方abs摘要均本次实际完整读取，均在Mon21题名底稿内；未把题名或关键词当准入证明。32条有具体机制/边界/反证信号需评分后的必要审阅，13条按具体增量关闭。21514/21983相似名称需要家族消歧，故这里不冻结新增家族数。停止继续扩宽，优先闭合已经有具体贡献依据的有限队列；普通正文待读保持待办。

| 精确v1 ID（官方abs） | 原有判断→实际题摘增量→需考虑的选择 / 关闭理由 | 作者初分流 |
| --- | --- | --- |
| [20842](https://arxiv.org/abs/2609.20842v1) | SQL augmentation只扩数据→结构coverage greedy补缺与step/epoch双层verified-failure监督→训练反馈应区分覆盖缺口与当前未解样本。 | `2+1+2=5`标准待审 |
| [20849](https://arxiv.org/abs/2609.20849v1) | audio CoT偏离音频→最终语义register训练对齐→audio-grounding与latent目标监督需分清。 | `2+1+2=5`标准待审 |
| [20850](https://arxiv.org/abs/2609.20850v1) | 单模态/单风险metric→跨模态stealth/risk exposure/defense integrity分层→防御评价不能只计拒答。 | `2+2+2=6`保护深入待审 |
| [20873](https://arxiv.org/abs/2609.20873v1) | GF(2)最小XOR电路的DRAT UNSAT证明应用成熟certifying discipline；不是服务大模型的compiler/kernel机制，也未新增模型能力形成条件。 | 贡献前关闭（非泛系统类比） |
| [20886](https://arxiv.org/abs/2609.20886v1) | BI领域数据+search/join/transform编排+SFT/RL，题摘未给超出成熟工具分解的新control/失效协议。 | 贡献前关闭（领域组合） |
| [20892](https://arxiv.org/abs/2609.20892v1) | plausible预测不等控制进展→signed servo coordinate监督latent consequence、冻结model再训练policy→world-model objective必须绑定task-error contraction。 | `2+1+2=5`标准待审 |
| [20912](https://arxiv.org/abs/2609.20912v1) | Rydberg物理数据scaling与语言统计类比，未建立主线模型-data条件的新机制；AI for Science暂缓。 | 范围/贡献前关闭 |
| [20945](https://arxiv.org/abs/2609.20945v1) | 单语言unlearning测试→训练/holdout语言及跨语言分散知识→删除验收不能只在原语言。 | `2+2+2=6`保护深入待审 |
| [20973](https://arxiv.org/abs/2609.20973v1) | 既有推理方法的state/controller统计解释与diagnostic hypothesis，无新验证机制或受控反证。 | 贡献前关闭（综述归纳） |
| [20980](https://arxiv.org/abs/2609.20980v1) | tactile仅当前反馈→未来tactile预测与groundtruth-to-prediction课程→action conditioning需核预测误差与部署交接。 | `2+1+2=5`标准待审 |
| [21018](https://arxiv.org/abs/2609.21018v1) | uniform reconstruction压缩多向量→MaxSim demand source marginal与balanced target OT→按检索实际需求和facet usage共同压缩。 | `2+1+2=5`标准待审 |
| [21054](https://arxiv.org/abs/2609.21054v1) | diffusion难物理控制→在VAE latent feature space修改rendering equation、单图拟合scene参数→物理控制与latent refinement分权。 | `2+1+2=5`标准待审 |
| [21094](https://arxiv.org/abs/2609.21094v1) | 道德二选偏好/option bias与task-vector正交化示例，未建立成熟task arithmetic之外的新机制/有效性条件。 | 贡献前关闭（偏好应用） |
| [21117](https://arxiv.org/abs/2609.21117v1) | 只看产出quality→相同quality有70倍interaction cost且task关系不同→productivity应分别测quality/repair cost，不以主观评分代替。 | `2+2+2=6`标准待审 |
| [21133](https://arxiv.org/abs/2609.21133v1) | SQL deterministic Execution Accuracy→AI operator的stochastic语义使正确query被拒→关系逻辑与AI语义需分层评价。 | `3+2+2=7`纠错深入待审 |
| [21157](https://arxiv.org/abs/2609.21157v1) | chip任务HLS/RTL成熟分层流程+Agent组合的性能比较，未改变服务大模型的compiler/kernel或Agent execution机制。 | 贡献前关闭（领域workflow比较） |
| [21181](https://arxiv.org/abs/2609.21181v1) | backbone/task embedding联合TTT→先只学embedding再冻结学backbone，known-rule测试显示interpolation非extrapolation→rule induction与execution分开诊断。 | `2+1+2=5`标准待审 |
| [21227](https://arxiv.org/abs/2609.21227v1) | near-copy或semantic-drift paraphrase监督不足→先meaning稳定再奖励QA一致性下降→robustness pressure与meaning-preservation必须共同验收。 | `2+1+2=5`标准待审 |
| [21242](https://arxiv.org/abs/2609.21242v1) | style/content硬分离→保留有信息overlap、可变空间粒度与norm budget→content suppression与style fidelity有显式代价。 | `2+1+2=5`标准待审 |
| [21293](https://arxiv.org/abs/2609.21293v1) | 平均check-pass掩盖task失败→predeclared interface、verified reference、L1/L2 prerequisite及strict task success→执行验收区分局部check与整体合同。 | `2+1+2=5`标准待审 |
| [21296](https://arxiv.org/abs/2609.21296v1) | 多fairness工具通过capability/input声明组合并携带config，题摘未给成熟typed admission之外的新失效/选择条件。 | 贡献前关闭（工具整合） |
| [21319](https://arxiv.org/abs/2609.21319v1) | LLM迭代edit robot mode/resource/transition程序与RL评估，属成熟evolution/controller组合应用，未新增foundation/VLA学习或执行机制。 | 贡献前关闭（控制应用） |
| [21323](https://arxiv.org/abs/2609.21323v1) | vehicle/roadside detection的SELECT/REFINE/REJECT+deterministic geometry，题摘未给成熟bounded arbitration之外的新主线机制。 | 贡献前关闭（cooperative-perception应用） |
| [21344](https://arxiv.org/abs/2609.21344v1) | verdict正确与justification正确不等→专家多任务代码/诊断评分暴露证据缺口→安全评价应区分结论与理由支持。 | `2+1+2=5`标准待审 |
| [21358](https://arxiv.org/abs/2609.21358v1) | continual VLA action normalization看似预处理→五策略四stream揭露coordinate drift/coverage/train-test mismatch，task-independent calibration后冻结→representation identity进入持续学习。 | `3+2+2=7`设计反证深入待审 |
| [21363](https://arxiv.org/abs/2609.21363v1) | refusal/pixel防地理泄漏不足→GeoCLIP-guided latent diffusion perturbation→威胁/transfer/utility需一起核。 | `2+2+2=6`保护深入待审 |
| [21369](https://arxiv.org/abs/2609.21369v1) | 仅最终failure分类→proprioceptive action boundary与earliest-onset localization→诊断timing不等失败后解释。 | `2+1+2=5`标准待审 |
| [21371](https://arxiv.org/abs/2609.21371v1) | social-proactivity从image拓到video+taxonomy/labels，题摘没有受控新失效条件或执行机制，综合ranking不能单独准入。 | 贡献前关闭（benchmark扩面） |
| [21386](https://arxiv.org/abs/2609.21386v1) | video答案分数→solution trace测是否真的获取支持证据→video agent评价增加evidence-acquisition盲区。 | `2+1+2=5`标准待审 |
| [21392](https://arxiv.org/abs/2609.21392v1) | response quality不测是否应回应→multimodal demand与non-demand false triggers→intent admission先于generation评价。 | `2+2+2=6`标准待审 |
| [21400](https://arxiv.org/abs/2609.21400v1) | 3D persistent feature memory→text-only object state增删改→world state codec与维护正确性是新的取舍分支。 | `2+1+2=5`标准待审 |
| [21449](https://arxiv.org/abs/2609.21449v1) | tactile作为condition→video/tactile/action joint flow experts与统一hand/tactile codec→预测观测与action supervision分权。 | `2+2+2=6`标准待审 |
| [21455](https://arxiv.org/abs/2609.21455v1) | 单一手工physics motion→structured semantics、composite dynamics与one-shot prior matching→物理约束和image-quality生成分权。 | `2+1+2=5`标准待审 |
| [21468](https://arxiv.org/abs/2609.21468v1) | restoration skills按condition/effect/failure记忆、candidate verify后commit，题摘仅把成熟verified residual-state loop应用于图像tools，没有新verification criterion/独立条件。 | 贡献前关闭（不是按可映射Agent准入） |
| [21492](https://arxiv.org/abs/2609.21492v1) | outcome reward漏逻辑错误→autoformalization/ATP与backtracking reward→mechanical validity与自然语言忠实性须分开。 | `2+1+2=5`标准待审 |
| [21502](https://arxiv.org/abs/2609.21502v1) | 3D foundation有限memory→learned gate+temporal/spatial regulator、local submaps/global refinement→persistent learned state与geometric consistency分权。 | `2+1+2=5`标准待审 |
| [21514](https://arxiv.org/abs/2609.21514v1) | human无robot action标签→skeleton overlay+2.5D共同topology、video/keypoint dynamics与robot Action Expert分离→跨embodiment监督接口。 | `2+2+2=6`标准待审；10/01 exact-v1核与21983是不同题名/作者/机制，见末尾消歧。 |
| [21521](https://arxiv.org/abs/2609.21521v1) | caption matching允许shortcut→逐事件human-verified support/hard negatives→生成能力不能替代verifier可靠性。 | `2+1+2=5`标准待审 |
| [21543](https://arxiv.org/abs/2609.21543v1) | specialized OCR可能新head→heldout干预与matched base-specialized保持head identity、强度变化→表征drift不等新机制形成。 | `2+2+2=6`标准待审 |
| [21554](https://arxiv.org/abs/2609.21554v1) | Selector/Reasoner多perspective直到confident再aggregate，题摘未建立成熟ensemble/control之外的新机制、budget-matched边界或反证。 | 贡献前关闭（模块组合） |
| [21576](https://arxiv.org/abs/2609.21576v1) | discrete streaming gesture codec限制expressiveness→causal continuous latent+per-token flow，再head-only distill→causal backbone与sampling cost分离。 | `2+1+2=5`标准待审 |
| [21650](https://arxiv.org/abs/2609.21650v1) | sparse-reward PPO没有success→privileged teacher demos/SFT再PPO，fixed RL compute测reward coverage→总teacher预算和探索覆盖须分开。 | `2+1+2=5`标准待审 |
| [21659](https://arxiv.org/abs/2609.21659v1) | 同success以为可互换→dependent matched policy pairs的DTW方向稳定、比例随表示变→task outcome与execution geometry分开。 | `2+1+2=5`标准待审 |
| [21666](https://arxiv.org/abs/2609.21666v1) | SALM family/公开训练/mobile artifact及size-class榜单，题摘未披露新架构/可比资源边界机制；不从privacy/edge标签推保护贡献。 | 贡献前关闭（不是按小模型拒绝） |
| [21675](https://arxiv.org/abs/2609.21675v1) | verbose multimodal CoT稀释visual evidence→observation/deduction structured trace+三视角reference rewards→trace compactness与忠实性共同验收。 | `2+1+2=5`标准待审 |

## 2026-09-30 恢复后的有限准入再校准：十二个较弱信号

停止新入口；从已有139个暂工作信号中选十二条机制组合、领域证据或 operating point 较弱项，重新实际完整读精确v1官方题摘与可见 Comments。不把这十二条或139条自动变成必要正文队列，不为小池而关闭真实局部机制。此前题摘层身份/数量不变，最终候选尚未冻结；以下五个拟关闭判断已交 root 独立校准，尚不声称全部通过。

| exact-v1 | 本次实际新增信息与作者判断 | 当前下一步 |
| --- | --- | --- |
| [20844](https://arxiv.org/abs/2609.20844v1) | DR rollout把snippet换原URL全文→LongQA→再DR训练；题摘只给61.6%长上下文错误归因和7.3/13.5结果，保留原evidence关系是一项构造声明，没有新关系保持条件/失效反证。不能因为训练stage/handoff可映射Ch22而准入。 | **拟贡献前关闭，待独立校准**；如果 necessary minimal 方法显示独立新保持机制再重开，不因总预算未披露关闭。 |
| [20849](https://arxiv.org/abs/2609.20849v1) | conclusion-aligned register/SBERT cosine监督使SALMONN audio CoT向目标语义收敛，是具体表示机制，不能按组合直接关闭。Comments Accepted at Interspeech2026 只提供更早正式家族线索，不证明具体公开时刻。 | 定点确认官方同题正式稿/会议公开身份；日期未定不按Submitted/accepted字段回填。 |
| [20889](https://arxiv.org/abs/2609.20889v1) | 四种语义routing signal构造round-adaptive decentralized稀疏图，规模与永久failure对照是实际新选择条件，不只是通信命名。 | 保留准入必要协议/代价与fault对照；不因35B/397B scale差就拒绝。 |
| [21117](https://arxiv.org/abs/2609.21117v1) | 两dataset四task描述quality相同cost至70倍、任务关系异质、主观评分非成本和earlyprobe关联；量化既有quality/interaction-cost双分母，但题摘未新增measurement成立条件、干预机制或改变既有分账的证据。 | **拟贡献前关闭，待独立校准**；局部研究有资格准入，此判断仅限题摘实际增量。 |
| [21228](https://arxiv.org/abs/2609.21228v1) | subtask-relevant图像区域承接VGGT geometry，Track4World当前/未来监督，部署不跑teacher；不是只扩大数据或robot指标。 | 保留必要distillation区域与future teacher交接/消融审阅。 |
| [21344](https://arxiv.org/abs/2609.21344v1) | CESBench IoT密码工程380题，88.5%正确verdict与53.4%理由分描述领域难度；题摘未改变一般verdict≠证据支持的评价命题，也未识别新的模型/系统故障机制。 | **拟贡献前关闭，待独立校准**；不是所有安全benchmark一律排除。 |
| [21461](https://arxiv.org/abs/2609.21461v1) | 三种ego/robot共同训练/迁移/video-action范式与2659h数据，题摘只给data scale×alignment quality归纳，没有改变范式选择的具体条件或反转；范式名称和规模不足。 | **拟贡献前关闭，待独立校准**；若原文有明确选择反证再定点重开。 |
| [21474](https://arxiv.org/abs/2609.21474v1) | 两stream结构mask分离；motion tokens进入action conditioning，visual-feature stream只训练backbone却不进入action condition，部署cache一次/replan。 | 保留必要机制与matched Fast-WAM增量控制，不称所有预测表示已有真实dynamics。 |
| [21712](https://arxiv.org/abs/2609.21712v1) | mixed fisheye/pinhole projection-adapter、每latent causal蒸馏、多view共同critic及cross-trajectory place-memory构造都是具体机制，不能按107.7x generator-only数字关闭。 | 保留实际geometry/causality/memory必要范围；end-to-end/SLO未证。 |
| [21967](https://arxiv.org/abs/2609.21967v1) | streaming encoder/decoder +parallel text/function calls+RNN-T/TTS及FDB分数证明组合artifact；题摘未增加speech/tool admission、播放取消或effect合同的长期机制/成立条件。 | **拟贡献前关闭，待独立校准**；不是native/small model不可准入。 |
| [22055](https://arxiv.org/abs/2609.22055v1) | curriculum复合action/perception轴区分新任务学习与已有机制reuse，modular vs canonical continual-learning对照可能修正适应分数解释。 | 保留必要构造与两轴反证；不按benchmark类别关闭。 |
| [22086](https://arxiv.org/abs/2609.22086v1) | noisy反馈下widen/deepen skill由matched replay gate接纳repair且不退步已观察success；heldout组合vs单机制对照，不只是成功率提高。 | 保留必要judge/traffic依赖、matched gate与消融反证；不把无oracle变成已认证feedback。 |

本轮完整题摘再读不是上述七条必要正文已完成，也不是五条独立关闭已通过。20874必要证据→Ch56 actual gap两段提案已持久于 [Books恢复队列](books-queue-restoration.md#2026-09-30-20874已备必要证据真实-owner-提案)，仍待root非作者源核/窄锁/实际写后。

### 2026-10-01 同名信号消歧

### 2026-10-01 第二组贡献分流（局部，而非余信号全文分母）

有限重新完整读取21533/21527/21383/21096/21267/21793/22068/21482/21888/21650/21386/21521，以及20850/21293/21455/21054/21242/21543/20945/21363 exact-v1题摘与可见Comments；没有新发现查询。明确准入：21533 content固定时format改变单位组合偏好、配对feedback胜分开评分；21527固定task/model/prompt/budget的单组件干预揭示相同原分不同message/failure退化；21383 sharp margin拆translation/direction/competitor-gap是有限理论条件，retrospective不当在线oracle；21096 attention图semi-local/global topology单pass sensor；21267 chronological calibration/heldout、subset fidelity与部署复杂度/五family稳定；21482 calibrated epistemic truncation改变训练rollout人口，step-saving≠GPU-saving；21888 entropy correction的mean/variance条件改变membership signal的可分性；21650 fixed PPOrecipe/compute下zero-success救10/27与privileged demos后27/27分开，teacher成本另外计；21521 plausible event-negative暴露generation与verification角色差异；21293 mean checks高而strict task/交集低、effort非单调是具体可靠性反证；21455 composite dynamics+structured prompt+prior matching；21054改rendering equation到VAE feature-space、single-image校准使geometry/light/view变化可控；21242保style/content有信息交集与norm budget，不是硬投影；21543 matched base→specialized causal head identity稳定但strength变；21363 pixel-space defense transfer局限与GeoCLIP-guided latent干预分开。21793最小组合表已有同一两defense次序不同导致ASR方向差，保留composition非交换的受限机制，不以泛fair评测标语准入，也不把全配置表当已审。

贡献前关闭：root独立exact-v1完整题摘及21386必要§3.4/Table1校准通过21386、20945。21386 tool-agnostic evidence milestones与LLM五维rating套既有过程评估，workflow两分提高/少量方向差未形成新的grounding验收对象或成立条件；20945只有train/heldout/dispersed多语切片与泛称需multilingual策略，未给具体哪个删除方法失效/新验收边界。两项不进入候选、不按领域/小模型或Books主题已覆盖关；关闭不否定跨语未学/视频证据研究的主题价值。

上述两项的决定准入事实已有限补读并获root独立校准：20850在§3/4.3/Fig4只增加stealth×severity分层和复合分账profile；前代SIUO已给multimodal-benign/harmful，不控制固定实例只改变stealth、未干预识别filter机制，modality usage是自评，CoT/size混版本。故按具体增量前关闭，不以benchmark名称拒绝。22068在§3.1–3.4从source-only公共可观察行为构造任务、原程序作独立reference oracle、隐藏verifier只grading可见、未规定细节不能转成私有断言，具有任务来源与oracle权限的新取舍；窄准入`2+1+2=5`，评价和actual owner仍普通必要待办，不自动deep。

目前已逐项按具体机制/反证确认35个arXiv准入：20830/21058/21079/21484/21515/22083/20874/20845/20888/21407/20849/20844/20889/21228/21474/21712/22055/22086/21533/21527/21383/21096/21267/21793/21482/21888/21650/21521/21293/21455/21054/21242/21543/21363/22068。加有效机构6家族为41个目前真实正向家族，不是最终冻结候选；17家族Evidence/Books已完成，其他按贡献评分后必要投入。原139工作信号内7前关闭、0决定准入含糊，另97尚未完成本轮逐项贡献收敛（不是97已准入/待全文）；139之外原已明确贡献/首发关闭维持精确理由，末Gate另按分层核。四已备标准单篇待root有限peer，不能漏记为关闭或未发现。没有把64旧正文计划继承为候选。

2026-10-01 root 已实际完整读 exact-v1 题摘，独立校准21117/21344/21461/21967贡献前关闭通过。关闭理由分别为现有质量/交互成本双分母的量化、领域verdict/justification分数、仅scale×alignment的ego/robot范式归纳、多流RNN-T工具speech成熟组合而无新的commit/取消/执行条件；不是按领域、小模型、映射章节或审阅成本拒绝。上述四条不再属于待审working signals，也不进入候选分母；旧139是本轮收敛前停点。20844最小方法补读发现新构造与对照，撤销其拟关闭，见本日 evidence；SPARE20849必要源/actual PEARL分工独立核通过，以训练-only answer目标/撤aux不证明真实执行这一采用命题 E，而非宣称全recipe已覆盖。

重新直接取得两份官方 exact-v1 完整题名、作者、摘要，确认不是同一 Source Family：21514 **Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer**，Zetao Cai等11作者，以hand overlay+2.5D共同拓扑，Video/Keypoint Experts由human/robot共同监督、另robot Action Expert；21983 **SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation**，Pengjun Niu等5作者，以arm centerline/TCP/parallel-jaw共同25D state、source-only训练与embodiment-specific constrained decoder，无target-task演示/update。两者是近似名称而非重复身份，不能合并“skeleton world action”题名家族。本次只解决已具名重复关系，不新增发现数、不宣称两篇必要方法完成；公开归属仍沿官方Mon21，不拿Submitted回填。

20849当前官方ISCA同题作者页未给首次上线时间，conference会期Sep27–Oct1；Accepted不证明更早公开，未据此排除Mon21。必要方法/结果与actual Ch23训练期辅助目标比较已实际完成作者标准范围，倾向E/recipe仅报告待root有限校准，见 [必要证据末节](arxiv-evidence-restoration.md#2026-10-01-有限接续20849-spare)。其余五拟关闭仍等独立校准，六局部新机制仍普通必要工作，不因等待共享写锁扩大正文队列。

### 2026-10-01 第三组：明确机制与准入事实含糊分开

复用先前有效的完整题摘、再直接实际完整读取以下十四个精确v1摘要；没有扩大发现入口，也不继承旧owner映射或64全文计划。下表十二项明确有新机制或具体局部反证，先准入后按新增命题评分；表中“标准待审”不等于已读必要实验。另21223/21675只补决定准入的小段，不自动进入候选。

| exact-v1 | 原约束 → 实际题摘增量 → 需重新考虑的选择 | 分流 |
| --- | --- | --- |
| [20824](https://arxiv.org/abs/2609.20824v1) | token entropy能识别回答不确定性 → 7 pairs/5 tasks中91%组合近零、不辨对错，semantic重采样恢复信号且cross-family与same-family收益不同 → 不以token entropy作通用SLM路由，代价应按增算而非省算解释。 | `2+1+2=5`标准待审 |
| [20831](https://arxiv.org/abs/2609.20831v1) | 覆盖正确规则足以泛化 → 全trace simplicity bias选择OOD shortcut，子任务context隔离排除此失效而IID仅常数差 → context visibility是泛化约束，不是递归名字本身。 | `2+1+2=5`标准理论待审 |
| [20846](https://arxiv.org/abs/2609.20846v1) | 加长推理改善欠定题 → underspecified题更长CoT却不拒答，效率reward联合完整信息判断、保持答题能力 → length reward须以abstention与answerability共同验收。 | `2+1+2=5`标准待审 |
| [20942](https://arxiv.org/abs/2609.20942v1) | synthetic reviewer监督可直接补真实监督 → 同初始Llama3.1-8B、四successors系统改变ICLR synthetic/official比例使rating与语义diversity收缩 → recursive feedback须检测评价分布塌缩；不是AI for Science任务恢复。 | `2+1+2=5`标准待审 |
| [21187](https://arxiv.org/abs/2609.21187v1) | gold-history下一轮提升可预测workflow能力 → 四model pre/SFT同对象对照下一轮皆升、strict workflow至多10.4% → next-turn收益不能代替自主执行收益，核暴露人口差异。 | `2+1+2=5`标准待审 |
| [20842](https://arxiv.org/abs/2609.20842v1) | 扩数据/SFT或RL单环处理所有错误 → greedy结构缺口补样本、step verified失败trace监督和epoch结构邻域练习分层 → 覆盖缺口与当前失败反馈的训练职责分开。 | `2+1+2=5`标准待审 |
| [21126](https://arxiv.org/abs/2609.21126v1) | joint结构惩罚与decoupled目标不易比较 → positively homogeneous条件下归一inner/惩罚outer与特定joint目标最优等价，数值usable强度/灾难over-pruning不同 → 等价目标不等于优化稳定性相同。 | `2+1+2=5`标准理论待审 |
| [21369](https://arxiv.org/abs/2609.21369v1) | 最终failure解释给出失效位置 → proprioceptive动态选时间边界、状态转语言与视觉joint诊断最早failure onset → timing测量与失败后分类是不同验收对象。 | `2+1+2=5`标准待审 |
| [21392](https://arxiv.org/abs/2609.21392v1) | response quality评价可代表交互正确 → media-grounded/human-verified demand与non-demand，14模型11个false trigger>50% → 是否应该回应必须与回应质量单独验收，局部反证不作全流SLO。 | `2+1+2=5`标准待审 |
| [21400](https://arxiv.org/abs/2609.21400v1) | persistent 3D状态须feature-rich专用mapping → structured text是唯一跨帧memory，由VLM按image增删改，训练任务直接监督maintenance → text-only状态codec替代几何feature有新的信息/容量取舍。 | `2+1+2=5`标准待审 |
| [21502](https://arxiv.org/abs/2609.21502v1) | foundation reconstruction缺persistent state → learned recurrence gates、test-time temporal/spatial一致性调节forgetting和local/global submap refinement → 学习state传播与几何一致性责任分开。 | `2+1+2=5`标准待审 |
| [21659](https://arxiv.org/abs/2609.21659v1) | 同task success即execution可互换 → 3600匹配且dependent policy pairs、9表征方向稳定但比例多倍变化，matched baseline仍异质 → 成功、行为geometry和interchangeability不能互授。 | `2+1+2=5`标准待审 |

21139/21849/22008/22043的准入命题与作者标准必要证据也已明确，不因拟Only/E从候选删去；四项各`2+1+2=5`，root必要源→actual owner有限peer尚待。这与下列含糊准入不是同一状态。

本轮到此为51个明确arXiv准入加6机构=57个已明确家族（不等于最终池或必要审阅完成）；原139内7贡献前关闭、2决定准入含糊（21223/21675）、79尚未本轮逐项贡献分流。原17家族完成仍有效，未扩大源；79不是候选或全文任务数。

### 2026-10-01 第四组：复用有效题摘的三十六个具体增量

下列仅复用本作者已完整读取、身份/精确v1/当前公告归属未变的题摘。原旧67迁移表§3.1只作具体问题路由，本次实际逐条判断机制或反证，不以建议owner、旧阅读标记或64队列推准入；更不是打开三十六篇正文。公开日期统一沿本日Mon21的08:00 BJT，版本Comments已经轻量核过。评价可信度尚待核不等决定准入含糊。来源入口没有新增。

| exact-v1 | 原约束 → 原文实际增量 → 重新考虑的选择 | 新增命题评分 / 最低投入 |
| --- | --- | --- | --- |
| [20957](https://arxiv.org/abs/2609.20957v1) | 固定每request服务时间不足描述continuous batch → 三参数iteration成本与state-dependent queue联合估TTFT/ITL → 在Markovian/light-moderate限制下分开容量模型与SLO控制。 | `2+1+2=5`标准 |
| [20971](https://arxiv.org/abs/2609.20971v1) | block centroid mean dilution漏相关token → radius bound rescue补block选择 → matched-density下核miss与IO，不以均值概括block内容。 | `2+1+2=5`标准 |
| [20974](https://arxiv.org/abs/2609.20974v1) | router只局部token scoring → attention-window routing、冻结base下depth与sink/检索冲突 → attention状态和expert选择耦合需分位置验收。 | `2+1+2=5`标准 |
| [20995](https://arxiv.org/abs/2609.20995v1) | model生成即durable voice history → 私有speculation、可取消播放与browser rendered-ACK才提交history → speech内容预测与消费commit不同owner。 | `2+2+2=6`标准 |
| [21022](https://arxiv.org/abs/2609.21022v1) | 高频观测须全VLA重跑 → 最后denoising step留高频反馈接口 → chunk规划与末步纠正分别计成本/能力边界。 | `2+1+2=5`标准 |
| [21032](https://arxiv.org/abs/2609.21032v1) | 多Agent通信必胜独立best-k → progress feedback与充足compute的条件性排序、条件不足反转 → 通信比较须固定总预算与可观察progress。 | `2+1+2=5`标准 |
| [21039](https://arxiv.org/abs/2609.21039v1) | factor自由gauge让factor blow-up → 一factor Stiefel约束配坐标AdamW → gauge固定和预条件分工，不作一般optimizer最优。 | `2+1+2=5`标准理论 |
| [21081](https://arxiv.org/abs/2609.21081v1) | 已展示审批A等于执行授权 → 审批后替换B的阳/阴性对照、canonical rendering/use-time绑定 → 审批内容和sink执行身份必须同时验收。 | `2+2+2=6`保护深入 |
| [21137](https://arxiv.org/abs/2609.21137v1) | 每expert独立全权重搬运 → expert-private量化/shared低秩分解与scratchpad多engine DMA overlap → 表示分解和执行供给共同设计。 | `2+2+2=6`标准 |
| [21155](https://arxiv.org/abs/2609.21155v1) | isolated fault审计选repair即可 → shared-information fault中repair排序反转、固定权重干预 → fault隔离协议是repair成立条件。 | `3+1+2=6`设计反证深入 |
| [21172](https://arxiv.org/abs/2609.21172v1) | decode reactive eviction循环 → prefill hidden需求预测、decode前exact/low-rank/flash联合分配 → demand proposal与恢复执行需独立核成本。 | `2+2+2=6`标准 |
| [21208](https://arxiv.org/abs/2609.21208v1) | co-trained tests宽松奖励塌缩 → GT correctness锚定IG、diversity-pruned tests → verifier与coder共同训练仍要独立correctness锚。 | `2+2+2=6`标准 |
| [21246](https://arxiv.org/abs/2609.21246v1) | OOD类别标签足以判断执行失败 → action-prefix/progress加入failure预测 → shift detection与rollout failure detection分别验收。 | `2+1+2=5`标准 |
| [21257](https://arxiv.org/abs/2609.21257v1) | 实验完成等于可归因结果 → evaluator深度不一致使head归因反转、mutation拒无效比较 → model开发必须锁评估身份而非只记run成功。 | `3+2+2=7`深入纠错 |
| [21264](https://arxiv.org/abs/2609.21264v1) | memory分级改善继续靠fusion → XDNA1 streaming已compute-bound、XDNA2需fusion的roofline分歧 → fusion何时停止由每层瓶颈而非框架名决定。 | `2+1+2=5`标准 |
| [21277](https://arxiv.org/abs/2609.21277v1) | judge panel等效人数是单一值 → spectral diversity与distribution recovery给不同人数 → judge diversity和分布恢复目标不能互换。 | `2+1+2=5`标准理论 |
| [21284](https://arxiv.org/abs/2609.21284v1) | root撤权cut即全任务已停止 → sink fence/provider证书cutset、alternative支持/重绑定 → delegation与异步执行的quiescence必须由证据确认、缺证indeterminate。 | `3+3+2=8`保护深入 |
| [21299](https://arxiv.org/abs/2609.21299v1) | 政策DSL移植保持授权语义 → scalar/quantifier覆盖缺口与Cedar default极性具体反例 → policy迁移应核decision等价，不由audit/prototype外推。 | `3+2+2=7`语义纠错深入；已有必要§3–4/11部分有效 |
| [21340](https://arxiv.org/abs/2609.21340v1) | re-ID top1给固定privacy risk → candidate ambiguity set在exchangeability下校准coverage → attack recoverability与set coverage分开，不作普遍隐私保证。 | `2+2+2=6`保护深入 |
| [21346](https://arxiv.org/abs/2609.21346v1) | full-expert参与必须全materialization → finite codebook block与全expert composition共存 → participation/execution/materialization是不同预算。 | `2+1+2=5`标准 |
| [21378](https://arxiv.org/abs/2609.21378v1) | trajectory ranking只能整条分配credit → tournament相对reward传pivotal steps和utility skill → step credit与memory更新共享证据但不互当truth。 | `2+2+2=6`标准 |
| [21432](https://arxiv.org/abs/2609.21432v1) | 旧GVPO只处理post-training → extended版将KL-optimum weighting扩到OPD、无需IS的条件 → 只核新增OPD命题，不重算旧核心首次创新。 | `2+1+2=5`标准理论；版本扩展本身不推重要 |
| [21450](https://arxiv.org/abs/2609.21450v1) | quant误差单一norm → compensation与orthogonal residual精确拆分 → sign/rotation/scaling作用区不同，改选工具而非看总误差。 | `2+1+2=5`标准理论 |
| [21465](https://arxiv.org/abs/2609.21465v1) | script/reference等于交互事实 → accepted rendered media重建reply reference、tier gate/fixed-history终轮人口 → 合成reference与live AV能力必须分开。 | `2+1+2=5`标准；方法p1–7有效，reward/eval普通未完 |
| [21483](https://arxiv.org/abs/2609.21483v1) | fixed SM split重叠compute/comm → 路由后每layer/GPU通信量已知、persistent megakernel动态时空SM分配 → 执行调度利用实际工作而非静态比例。 | `2+2+2=6`标准 |
| [21561](https://arxiv.org/abs/2609.21561v1) | privileged teacher提升都当正确性 → attractive/repulsive共享偏移抵消的distill干预 → teacher行为偏移与能力差距要分辨。 | `2+1+2=5`标准 |
| [21562](https://arxiv.org/abs/2609.21562v1) | runnable/最终状态通过即game逻辑正确 → tick-level状态assertions和mutant校准发现途中违规 → final-artifact与途中execution分开验收。 | `2+1+2=5`标准 |
| [21573](https://arxiv.org/abs/2609.21573v1) | 逐passage审毒足够 → 多局部合理弱信号累积、top-k/database diversity改共同出现概率 → retrieval组合人口进入attack威胁模型。 | `2+2+2=6`保护深入 |
| [21594](https://arxiv.org/abs/2609.21594v1) | shard隐在runtime通信 → autograd边界的layout语义、validation/production两mode与layout-driven Muon → collective拓扑和optimizer对象归属分别验证。 | `2+2+2=6`标准 |
| [21605](https://arxiv.org/abs/2609.21605v1) | physical depth与每词计算混为规模 → 同block compute预算用thought-token recurrence换层深/参数 → 参数节省不等推理无代价，按匹配口径比较。 | `2+1+2=5`标准 |
| [21619](https://arxiv.org/abs/2609.21619v1) | teacher/student差全是student错误 → 正负privileged干预校准teacher偏移区间、只学超区间差额 → capability discrepancy与teacher prompt drift分开。 | `2+1+2=5`标准 |
| [21662](https://arxiv.org/abs/2609.21662v1) | 相当latent displacement可控制language → latent-to-language输出转译gap → steering验收需核readout接口而非只测hidden变化。 | `2+1+2=5`标准 |
| [21686](https://arxiv.org/abs/2609.21686v1) | internal敏感依赖等于外部泄漏 → channel观察面/检索深度改变recoverability、semantic audit补exactmatch漏项 → dependency与可恢复泄漏分别给证据。 | `2+2+2=6`保护深入 |
| [21748](https://arxiv.org/abs/2609.21748v1) | localization失败即没world model → causal intervention可见地图但superposition阻断读出 → 表示存在与可访问能力分开判断。 | `2+1+2=5`标准 |
| [21827](https://arxiv.org/abs/2609.21827v1) | dynamic-tree proxy概率可直接验证采样 → proxy构树/真实sampling分开，避免one-hot top-k损随机acceptance → lossless权必须由真实概率/校正掌握。 | `2+2+2=6`标准理论 |
| [21858](https://arxiv.org/abs/2609.21858v1) | multi-draft依drafter coupling且水印减acceptance → Poisson list采样与watermark联合条件 → unbiasedness/水印效力不能仅由相同decode接口推出。 | `2+2+2=6`保护深入理论 |

至此87个arXiv明确准入加6机构=93个部分家族；139内7前关闭、2决定准入含糊、43本轮未分流。该数量来自上述具体命题，不来自旧计划或需要凑的比例，未最终冻结。必要审阅按每个新增命题的最低范围推进，不能把“标准”变成全部附录全文，也不能因Only/E取消已经准入的局部有效证据。

### 2026-10-01 第五组：余下具体题摘收敛与两项最小补读

本组不扩源，按之前有效的完整exact-v1题摘、逐条明确贡献而非只凭owner。本轮另实际完整再读22048/21509/21908/21940/21996/21740/21948/21492，纠正其中“只是成熟combo”的潜在误关：22048提出固定order的partition DP、分planning/selection splits处理finite-data损失，不仅复述binomial；21509十六model所有pair交换generator/extractor方向改变60.4pp、domain-disjoint训练也改善，不仅角色命名；21908 monitor阻依赖/当前state+base-action correction/minimal gain选择；21940 data-driven complementary views前移写入而非静态schema；PIR借人类CIT但实测concealment与unlearning各自作用，不能按借原理关闭。这些潜在贡献清楚、可信度尚待核，进入相应必要范围而非默认读完整附件。

| exact-v1 | 原约束 → 实际增量 → 需考虑的选择 | 评分 / 最低投入 |
| --- | --- | --- | --- |
| [21908](https://arxiv.org/abs/2609.21908v1) | stage command发出即可续步 → current evidence monitor阻dependent动作、frozen base action条件下局部correction与最小gain → 执行stage确认和纠正幅度分别验证。 | `2+1+2=5`标准 |
| [21940](https://arxiv.org/abs/2609.21940v1) | 固定memory schema留检索时去干扰 → 从interaction发现compact互补views、write-time provenance extraction → semantic disentangle前移写入，consolidation收益另核。 | `2+1+2=5`标准 |
| [21942](https://arxiv.org/abs/2609.21942v1) | confidence能代表问人价值 → 已知注入failure/multisensor审计中选择不随可靠性/cost → dialogue启动必须核measured accuracy而非自述confidence。 | `2+1+2=5`标准 |
| [21983](https://arxiv.org/abs/2609.21983v1) | action spaces异构须target示范 → source-only25D共同skeleton/TCP/jaw与embodiment decoder → shared状态监督和device constraints分权。 | `2+2+2=6`标准；与21514非同族 |
| [22005](https://arxiv.org/abs/2609.22005v1) | attention gate仅一个降噪作用 → matched scale/controlled value干扰使abstention与noise filtering收益反向 → 两种门的语义不能互换。 | `2+1+2=5`标准 |
| [22041](https://arxiv.org/abs/2609.22041v1) | nominal ratio clipping可保flow RL → Gaussian transition的per-step path variance解释negative梯度/ratio失效，预算gradient effort → kernel概率与budget必须一起核。 | `2+2+2=6`标准理论 |
| [22048](https://arxiv.org/abs/2609.22048v1) | valid certificate即可用 → finite evidence使细分人口不可certify、partition DP与双split planner回收coverage → certification validity与availability分开优化。 | `2+1+2=5`标准理论 |
| [22056](https://arxiv.org/abs/2609.22056v1) | 单confidence proxy通用降低confident failure → ANN特征与success互信息决定可降性、regime互补 → gate信号必须按retrieval regime验收。 | `2+1+2=5`标准 |
| [20981](https://arxiv.org/abs/2609.20981v1) | latent revision只是多思考长度 → causal topology与implicit differentiation约束latent更新 → structural依赖与teacher/oracle角色要核。 | `2+1+2=5`标准理论 |
| [21001](https://arxiv.org/abs/2609.21001v1) | coding-rate最优消除环境相关特征 → 同最优目标仍保environment feature、相关性反转失效 → objective最优与OOD不互推。 | `3+1+2=6`设计反证深入 |
| [21113](https://arxiv.org/abs/2609.21113v1) | representation drift揭示重要组件 → EAP/patching定位与drift不等、跨task重叠不保证transfer → diagnostic proxy需分别干预验收。 | `3+1+2=6`设计反证深入；必要§3–5有效 |
| [21183](https://arxiv.org/abs/2609.21183v1) | proactive只是低音频延迟 → interrupt/silent事件监督、onset/maintain/repetition联合 → event预测与播放控制不能互代。 | `2+1+2=5`标准 |
| [21190](https://arxiv.org/abs/2609.21190v1) | solver proof等于issue intent → known-patch引导spec/axiom和机械证明分开 → 规格faithfulness与formal validity各自验收。 | `2+1+2=5`标准 |
| [21216](https://arxiv.org/abs/2609.21216v1) | flow policy更准只能增solver步 → frozen少步endpoint corrector → source-noise/额外步数/caching与局部修正分开成本。 | `2+1+2=5`标准 |
| [21220](https://arxiv.org/abs/2609.21220v1) | 约束action直接projection → 生成policy输入noise搜索保其action支持 → latent/noise约束和真实物理安全分别核。 | `2+1+2=5`标准 |
| [21251](https://arxiv.org/abs/2609.21251v1) | guidance单step size处理曲率 → tangent/normal预算、Armijo/dual步分工 → 受限曲率条件下选择不同修正。 | `2+1+2=5`标准理论 |
| [21268](https://arxiv.org/abs/2609.21268v1) | editing只改prompt权重 → source条件概率替换、stage/token调制与残差prune → source preservation与生成控制不同条件。 | `2+1+2=5`标准 |
| [21362](https://arxiv.org/abs/2609.21362v1) | 声音单位须单atomic token → 同position onset/rime/tone三head → output接口在序列长/词表/联合一致性间新取舍。 | `2+1+2=5`标准 |
| [21422](https://arxiv.org/abs/2609.21422v1) | learned feature当固定head复杂度 → same-sample feature selection另付complexity → 条件理论不能外推任意LM泛化。 | `2+1+2=5`标准理论 |
| [21423](https://arxiv.org/abs/2609.21423v1) | trajectory shortcut只压短token → 证据/未决obligation tree与outcome-blind/reset recipient对照 → feedback压缩有效性不能从最终成功倒推。 | `2+1+2=5`标准 |
| [21509](https://arxiv.org/abs/2609.21509v1) | 最终答案评价通信单向能力 → exact symbolic roundtrip交换16×16 generator/extractor、方向最多60.4pp，disjoint-domain训练控制 → 两端的信息损失与训练transfer分别测。 | `2+1+2=5`标准 |
| [21523](https://arxiv.org/abs/2609.21523v1) | finite压缩state容量按参数数猜 → linear-task advice partition的exact rank/state frontier → task信息保留须绑定明确函数族/任务人口。 | `2+1+2=5`标准理论 |
| [21656](https://arxiv.org/abs/2609.21656v1) | JEPA分布唯一性不依latent geometry → Euclidean Gaussian唯一性与spherical另一恢复条件 → 表示几何进入目标可识别条件。 | `2+1+2=5`标准理论 |
| [21672](https://arxiv.org/abs/2609.21672v1) | sparse MoE只router选择既有expert → 独立domain curriculum、freeze non-MLP/L0结构构造后拼装 → expert形成和token-router exposure分开。 | `2+1+2=5`标准；必要§2–4部分有效 |
| [21677](https://arxiv.org/abs/2609.21677v1) | 只止危险CoT泄漏即可 → unlearn安全轨迹/稳定answer guidance再distill → leakage下降与正常utility保持必须同时核。 | `2+2+2=6`保护深入 |
| [21740](https://arxiv.org/abs/2609.21740v1) | TTA须改内部多百万参数 → 冻结world-model主干、预测器前后残差由self-supervised error在线更新 → label-free correction不等已修真实dynamics，compound shift/matched内部适配比较。 | `2+1+2=5`标准 |
| [21787](https://arxiv.org/abs/2609.21787v1) | compact空间即固定closed state → 可干预低维结构随recurrent Jacobian移动 → readout结构与动态闭合需分开核。 | `2+1+2=5`标准理论 |
| [21899](https://arxiv.org/abs/2609.21899v1) | finite-n BoN选择等于原generator → exponential-noise/GSI分解与finite预算 → sampling law和budget估计不能互作wall-clock证明。 | `2+1+2=5`标准理论 |
| [21941](https://arxiv.org/abs/2609.21941v1) | hard-label end-to-end抽取一概困难 → sign recovery的query职责与完整重建分开 → 限shallow/narrow ReLU与查询假设，不作任意LLM抽取。 | `2+2+2=6`保护深入理论 |
| [21948](https://arxiv.org/abs/2609.21948v1) | image LAM丢finger geometry、naive pointcloud缺共享语义 → UEMR共同motion配visual/geometric latent → 细动作保真与跨embodiment语义共同验收。 | `2+2+2=6`标准 |
| [21960](https://arxiv.org/abs/2609.21960v1) | nominal sampler阶数即可选步数 → factorization error/profile调度常数与阶数分开 → schedule选择依regularity而非名称。 | `2+1+2=5`标准理论 |
| [21996](https://arxiv.org/abs/2609.21996v1) | 不回答即没有知识 → candidate-decoy internal recognition在concealment保持、unlearning下降 → 认出/报告/未学分别测，probe因果与部署可得性尚待必要核。 | `2+2+2=6`保护深入 |
| [20892](https://arxiv.org/abs/2609.20892v1) | plausible world预测等于控制价值 → signed servo coordinate监督latent consequence、freeze后训练policy → objective绑定task-error contraction。 | `2+1+2=5`标准 |
| [20980](https://arxiv.org/abs/2609.20980v1) | 当前tactile作condition足够 → 未来tactile预测与GT→prediction课程 → 部署接收预测误差与privileged训练观测分开。 | `2+1+2=5`标准 |
| [21018](https://arxiv.org/abs/2609.21018v1) | uniform reconstruction压多vector → MaxSim需求marginal与balanced OT target → query需求和facet use共同决定压缩。 | `2+1+2=5`标准 |
| [21133](https://arxiv.org/abs/2609.21133v1) | deterministic execution accuracy可判AI-SQL → stochastic AI operator使正确query被拒 → 关系逻辑与AI语义不同评价。 | `3+2+2=7`纠错深入 |
| [21181](https://arxiv.org/abs/2609.21181v1) | joint TTT代表rule induction → 先embedding后freeze学backbone、known-rule测试interp非extrap → induction与execution单独诊断。 | `2+1+2=5`标准 |
| [21227](https://arxiv.org/abs/2609.21227v1) | paraphrase强干扰就能练robustness → meaning稳定后奖励QA下降 → meaning preservation与adversarial pressure联合验收。 | `2+1+2=5`标准 |
| [21358](https://arxiv.org/abs/2609.21358v1) | action normalization仅无害预处理 → 五策略四stream坐标drift/coverage/train-test mismatch、task-independent freeze → 持续训练representation身份必须稳定。 | `3+2+2=7`设计反证深入 |
| [21449](https://arxiv.org/abs/2609.21449v1) | tactile只是外加条件 → video/tactile/action joint-flow experts与hand/tactile codec → 观测预测和action supervision分别核。 | `2+2+2=6`标准 |
| [21492](https://arxiv.org/abs/2609.21492v1) | 正确答案reward掩盖逻辑错 → autoformalization/ATP验证每step、Solver-Based Backtracking Reward作搜索/SFT → 机械validity与自然语言忠实性分开。 | `2+1+2=5`标准 |
| [21514](https://arxiv.org/abs/2609.21514v1) | human视频无robot action标签 → hand-overlay/共同2.5D topology、human-robot共享Video/Keypoint experts与独立robot Action Expert → shared表示监督与动作监督接口分开。 | `2+2+2=6`标准 |
| [21576](https://arxiv.org/abs/2609.21576v1) | discrete streaming gesture限制expression → causal continuous latent/per-token flow、head-only distill → causal backbone与sampler算力分别控制。 | `2+1+2=5`标准 |

另21223与21675决定准入小段已root有限校准为5分标准候选，未称普通Review已完成。21223 §core/Results/Table5–6固定task objective三prompt：specific虽降低final-state hazard却增加execution hazard、SR/SSR降低，unsafe-success下降主要因为更少成功，不是安全提高。21675 §3.3.1–.2 tri-perspective reference与Nmatch/hall correction（答案正确亦受罚）、Neff允许不同分解/Ndeep capped bonus防compact SFT低variance早停；LLM judge及reference不是机械真值。二者有明确局部选择/反证，不是从分类或格式名准入，标准评价/实际owner仍普通待办。

**当前有界范围的作者侧贡献分流：132个arXiv provisional准入家族+6机构=138部分工作候选，139旧working中7个具体前关闭、准入事实含糊0、尚未作者分流0；不是最终冻结分母。** root仍在对新增36及受影响成熟组合/局部数字理由作有限独立校准，具体误判仅重开相关项。这个较高作者保留数来自先前已经定点取题摘的主线机制人口，并非475宽库存的固定比例；不按结果配额强关局部机制。旧139本身不再当候选分母，138不是138论文已经证实、独立准入通过或需无差别全文/Books更新。139之外另有24个明确scope/贡献、早首发及同族去重关闭，保留原身份与理由；另1个12748日期保留项不是贡献关闭。Replacement历史清单/12748仍终态隔离，不计当窗候选或无遗漏。筛选/日期源范围须最后独立Gate复核，普通证据和Books继续。

### 2026-10-01 第五组有限独立准入校准（sep22_resume_v3）

root委派的本组43行中，21908/21940已有root完整题摘准入PASS，本轮不重复；21208/21378属于其他组，不扩入本表。03:24 BJT实际取得并读完余41项官方 `https://arxiv.org/abs/2609.<ID>v1` 的完整题名、摘要及可见Comments，逐项对照上述原约束→增量→选择与当前研究合同§3，不读全文/附录，不新增发现入口。本表仅校准准入：不核日期落窗、中心定理成立、实验归因、实际owner覆盖或Books采用，也不替代最后日Gate。第五组43为有界校准集合，不是数量配额。

41项均有摘要可指认的具体机制、条件或反证，未发现仅主题/泛化成熟原则的误收；没有因小模型、局部负结果、借用成熟数学而关闭真实增量。此组全部为拟准入项，未审139之外的排除集合，不能称无漏收或全日分层negative通过。逐项依据与需要保留的最小边界如下，PASS均仅指准入。

| exact-v1（官方题摘） | 独立准入判断与支持范围 |
| --- | --- |
| [21942](https://arxiv.org/abs/2609.21942v1) | PASS：注入已知故障+传感器可诊断性审计，选项次序与问人费用反事实、force文本恢复诊断，是问人策略失效的具体证据；不是换机器人场景后总分。准确率/费用政策与模型confidence不可等同，有限模拟故障不外推所有交互。 |
| [21983](https://arxiv.org/abs/2609.21983v1) | PASS：同一25D skeleton/TCP/jaw接口供视觉与whole-body未来监督，再经具身特定受约束decoder，确有action空间桥接设计；source-only/无target-task更新只是拟核条件，43.3%不作普遍zero-shot承诺，与21514身份不同。 |
| [22005](https://arxiv.org/abs/2609.22005v1) | PASS：sink abstention与per-value filtering分开，matched 10M–350M尺度收益趋势相反且控制value干扰，纠正‘一种gate一种作用’；规模人口有限，两种gate盲区与联合机制待必要证据，不以缓存兼容表述替代实现核。 |
| [22041](https://arxiv.org/abs/2609.22041v1) | PASS：Gaussian transition导出per-step path variance并据此分配gradient effort，区别经验ratio stabilizer，改变flow RL更新预算；精确law、负侧和晚步预算只在相应kernel/策略条件下核，两个reward设置非通用提升。 |
| [22048](https://arxiv.org/abs/2609.22048v1) | PASS：exact binomial是借用，但固定order partition DP、finite-data可认证不足与planning/selection双split回收coverage是真增量；truth-informed .157不可当可部署，.060及59/60需绑定实验。validity与availability分别核。 |
| [22056](https://arxiv.org/abs/2609.22056v1) | PASS：feature–success信息条件、regime互补的witness及无额外LLM调用ANN信号组合改变abstention选型；iff定理/AUC与50%coverage的CWAR降幅均待必要证据，不能从一项transfer推出domain-agnostic普律。 |
| [20981](https://arxiv.org/abs/2609.20981v1) | PASS：expert CTM+implicit differentiation将DLM中间latent修改约束为因果拓扑下优化，非只是多推理token；expert来源、拓扑依赖与是否真保逻辑一致需核，摘要SOTA不证明所有步骤正确。 |
| [21001](https://arxiv.org/abs/2609.21001v1) | PASS：global MCR² optimum仍可完全依赖不稳定环境特征，以及support一致时near-optimal却近全错，直接反证‘coding最优⇒OOD稳定’，shared optimal operator也不足。深入核反例/假设，不要求LM规模替代理论。 |
| [21113](https://arxiv.org/abs/2609.21113v1) | PASS：fine-tuning drift大与EAP重要组件不同，高组件重叠亦可跨task退化，是诊断proxy失效而非仅新增probe榜；EAP及跨task人口局限必须保留，不能读成所有drift无用。既有必要源不重审。 |
| [21183](https://arxiv.org/abs/2609.21183v1) | PASS：interrupt/silent decoding直接表示onset、维持、抑制与去重四事件，不只是音频任务/低延迟数字；决策输出不自动等播放/真实用户效用，ESC与noisy厨房覆盖、3.5s协议待核。 |
| [21190](https://arxiv.org/abs/2609.21190v1) | PASS：known-correct patch建spec+callee axioms并经mechanical/adversarial admission，观察test-pass仍反例与自写spec faithfulness失败，是真评价盲区；correct formal spec的95%依赖特权条件，不当自动从issue生成忠实spec。 |
| [21216](https://arxiv.org/abs/2609.21216v1) | PASS：frozen少步flow endpoint后加demo-supervised residual，复用source noise/prefix cache；matched同五步与nearly equal latency控制使budget改配值得核，不把相对十步30.2%只归corrector或所有VLA。 |
| [21220](https://arxiv.org/abs/2609.21220v1) | PASS：在one-step policy输入noise空间做trajectory constraint搜索+prior regularization，不直接project输出action，确有支持空间取舍；粒子搜索/预测轨迹成本及真实约束满足分别核，不授‘安全实时’普遍保证。 |
| [21251](https://arxiv.org/abs/2609.21251v1) | PASS：共享noise-dependent曲率预算为normal一阶/tangent二阶分账、dual求幅度再Armijo校有限步，区别只切掉normal；局部几何/score支持与计算代价待核。只采用生成guidance主线，不引入黑洞科学应用。 |
| [21268](https://arxiv.org/abs/2609.21268v1) | PASS：VAR源token条件替换、按位置/scale放松限制及late-scale release联合控制source保留/编辑，final高分辨率residual剪枝另计；不是仅‘免训练’，源保真/时序/速度归因与不同inversion条件需核。 |
| [21362](https://arxiv.org/abs/2609.21362v1) | PASS：onset/rime/tone共享一个context position与三预测head、unsupported character fallback，改变vocabulary/sequence/联合还原接口；语言特定IPA与中文controlled pretraining/越南pretrained对照分开，不声称任意LLM更优。 |
| [21422](https://arxiv.org/abs/2609.21422v1) | PASS：fixed-representation activation mass与same-sample selection的quadratic process分开，固定mass实验展示selection gap，具体挑战fixed-feature分析漏成本；只在Brownian RKHS、ReLU/norm/trace人口核，不移植成任意Transformer界。 |
| [21423](https://arxiv.org/abs/2609.21423v1) | PASS：nested progress/recovery/unfinished obligations反馈压缩，REFIT shared-source/outcome-blind/reset recipients使复用效果可区分，非泛总结；同task fresh retry收益不是新task泛化，observed token下降≠含建树成本端到端节省。 |
| [21509](https://arxiv.org/abs/2609.21509v1) | PASS：16×16 generator/extractor全pair符号roundtrip分账，交换方向60.4pp以及disjoint-domain训练改善，发现通信方向/内容损失盲区；symbolic equivalence是该表达族oracle，73.6%归因下界及训练transfer条件待核。 |
| [21523](https://arxiv.org/abs/2609.21523v1) | PASS：task消息先于state形成、具体task后知时的partition joint-rank精确frontier及近似/难度条件，直接指导task-dependent状态保留；softmax九bit例不是通用cache压缩保证，finite linear-task信息假设不可省。 |
| [21656](https://arxiv.org/abs/2609.21656v1) | PASS：JEPA Gaussian唯一性依赖Euclidean latent/positive-pair dynamics，sphere匹配可orthogonal recovery及更紧近似界，确为目标可识别条件修正；exact distribution matching/优化成功不等实训所有JEPA保证。 |
| [21672](https://arxiv.org/abs/2609.21672v1) | PASS：摘要明确L0专家形成、domain-aware cluster confusion matrix及dynamic batching，非仅2.5×数字，可按具体结构/数据机制进入必要核；freeze non-MLP与独立curriculum等原Method笔记未在本轮摘要独立重新核过，不能给本次全文PASS。 |
| [21677](https://arxiv.org/abs/2609.21677v1) | PASS：不是单压泄漏，而把unsafe disclosures换成coherent non-disclosing CoT+稳定safe-exit answer，再frozen guidance/distillation；建议原行‘unlearn安全轨迹’精确为‘将不安全披露改为safe-exit轨迹并蒸馏’。replacement质量与normal utility需保护深入，不以低泄漏代表真知识删除。 |
| [21740](https://arxiv.org/abs/2609.21740v1) | PASS：frozen world-model predictor前后小residual在线以self-supervised prediction error适配，区别内部多百万参数TTA，21条件/compound对照有局部选择；无reward/label不等纠正真实dynamics，source/noise与计算预算待核。 |
| [21787](https://arxiv.org/abs/2609.21787v1) | PASS：rank4 entry干预离开固定子空间，但Jacobians transport后的moving低秩结构保未来功能，直接纠正compact⇒closed state；checkpoint/有限horizon及LSTM privileged初始化/full-amplitude反侧不能省。 |
| [21899](https://arxiv.org/abs/2609.21899v1) | PASS：exponential report-noisy-max的finite-n精确decomposition、TV/reward/双向KL收敛并接GSI，是真sampling-law替代而非改名称；estimated computation14–39%/45%非wall-clock，条件/候选与reward调用成本待核。 |
| [21941](https://arxiv.org/abs/2609.21941v1) | PASS：hard-label sign recovery无需其专用query使trained ReLU完整black-box extraction可行，是模型资产威胁机制变化；MNIST/Fashion宽16、4/6层及98% label agreement不等任意LLM或完整参数精确恢复。 |
| [21948](https://arxiv.org/abs/2609.21948v1) | PASS：image LAM缺fine end-effector articulation而naive pointcloud缺shared semantics，以UEMR配visual/geometric latent监督VLA，确有双约束表示设计；real/sim success分开、动作自由human视频不当已知robot action标签。 |
| [21960](https://arxiv.org/abs/2609.21960v1) | PASS：即便perfect predictor，parallel revealed block product近似仍有factorization error，rho profile/finite-K优化与随机block额外成本是真采样设计增量；strict-positive uniform profile仅改leading constant，degenerate profile才可能改阶，非提高名义solver阶数。 |
| [21996](https://arxiv.org/abs/2609.21996v1) | PASS：CIT是成熟借用，但candidate/decoy internal recognition在concealment保留、unlearning下降及unknown baseline，具体区分不愿报告/不知道；reference-free≠没有候选、truth或assay条件，因果与free-form推广待必要源，不授部署可读保证。 |
| [20892](https://arxiv.org/abs/2609.20892v1) | PASS：signed四维servo coordinate对齐action consequences，冻结model再用imitation+consequence+short rollout训练policy，明确改变plausibility与control价值目标；30/30曾达阈值≠25/30保持到最后，外部AprilTag仅有限验证。 |
| [20980](https://arxiv.org/abs/2609.20980v1) | PASS：future tactile forecast进入VLA动作condition，GT→prediction课程显式处理部署接预测误差，非仅添加触觉；四task95%及low-light结果须核observed/privileged传感信息、forecast代价/闭环控制，不推出普适contact robustness。 |
| [21018](https://arxiv.org/abs/2609.21018v1) | PASS：MaxSim-induced surrogate+retrieval-demand source marginal和balanced target marginal的双约束OT，改变统一reconstruction压缩盲区；frozen post-hoc可复用设计与ViDoRe人口/需要何种query统计、压缩计算分别核。 |
| [21133](https://arxiv.org/abs/2609.21133v1) | PASS：stochastic AI operator使确定execution accuracy错拒正确SQL，按关系逻辑/AI语义分层验证并跨两个backend测误判，是具体评价盲区；valid query真值/AI predicate标准及97.2%范围待纠错深入，不借agent verifier成熟原则打分。 |
| [21181](https://arxiv.org/abs/2609.21181v1) | PASS：先embedding TTT后freeze再backbone，known-rule数据可独立观察rule induction与execution，interpolation非extrapolation是真边界；不是ARC换榜，rule可probe不等普遍已学symbolic规则。 |
| [21227](https://arxiv.org/abs/2609.21227v1) | PASS：先稳meaning/diversity后奖励QA错误的adversarial paraphrase双阶段，明确区分攻击压力与语义漂移；局部artifact/drift控制与lightweight robust fine-tuning分别核，不以被攻击后错推底层事实全遗忘。 |
| [21358](https://arxiv.org/abs/2609.21358v1) | PASS：五normalization×四continual task streams发现坐标drift/coverage/train-test mismatch，预先task-independent calibrate并冻结的3C/FAN是设计修正；calibration如何无future泄漏与经验最优范围需深入。 |
| [21449](https://arxiv.org/abs/2609.21449v1) | PASS：video/tactile/action三expert joint-flow未来建模，不只是触觉condition；canonical hand+unified tactile codec处理异构布局，trace-replay tactile数据生产有独立接口；sensor真实/模拟、预测和动作因果收益及生成数据成本待核。 |
| [21492](https://arxiv.org/abs/2609.21492v1) | PASS：逐step autoformalization+ATP产生backtracking reward并将轨迹用于SFT，针对correct final/invalid intermediate盲区有具体机制；所形式化spec的机械validity不等自然语言忠实/所有high-stakes可靠性，solver与建数据成本另核。 |
| [21514](https://arxiv.org/abs/2609.21514v1) | PASS：2.5D hand topology/overlay供human–robot shared Video/Keypoint dynamics，独立robot Action Expert使无robot action标签human视频可训练，接口分工真实；与21983 source-only25D不是同族，不用cotraining倍增推任意具身零样本。 |
| [21576](https://arxiv.org/abs/2609.21576v1) | PASS：causal continuous motion latent配per-token flow，frozen causal backbone只distill flow head为one evaluation，明确改变表达/latency预算；仅BEAT2 streaming可比质量与实时协议需核，token-causal不等音频未来无泄漏已证明。 |

本次结果：41/41准入校准PASS，加root原21908/21940两项涵盖第五组43行的准入层；不是43 Evidence/Books PASS。原评分是拟证命题的最低投入，本轮不按保留数调分；21677措辞校正、21672前轮Method复用权限及各行条件在必要审阅中继续落实。未新增Source Family、改Books或冻结全日分母。
