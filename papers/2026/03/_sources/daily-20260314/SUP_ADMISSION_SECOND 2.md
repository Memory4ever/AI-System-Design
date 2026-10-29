# 第二包有限题摘：保留初读与当前校准

作者mar14_supplement；只从既有四主题有限发现中选择相关/含糊标题，未另扩类别/机构历史池。实际完整读25精确v1题摘、Comments/Subjects/history，原件`SUP_ABS_<ID>.raw/.txt`，请求/停止见`SUP_ABS_SECOND_MANIFEST.json/RESULT.json`。以下为作者贡献筛选，不是日期已核候选/评分或Evidence；首包九潜力及两EX有效复用。准备好单篇不等整包，但尚未取得的日期/必要证据不虚构。

## 明确潜力17项：仍需日期与必要证据

| 精确v1 | 原约束/判断→原文增量→可能改变的选择 |
| --- | --- |
| [11214 Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios](https://arxiv.org/abs/2603.11214v1) | 单步成功不能代表长horizon能力/版本进步→32步企业/7步ICS协议控制模型与token预算，增加推理预算可强烈改变成功率→评价应分离能力进步与测试计算；仅核受控能力测量，不采用攻击操作指引 |
| [11219 Senna-2](https://arxiv.org/abs/2603.11219v1) | 高层VLM决策和低层轨迹可不一致→implicit-embedding adapter与三阶段训练/3DGS闭环RL连高低策略→重新考虑语言监督与动作闭环的对齐接口，不以驾驶分数替代机制 |
| [11220 Frequency-Modulated Visual Restoration for Matryoshka Large Multimodal Models](https://arxiv.org/abs/2603.11220v1) | token压缩可能偏向salient而损低/高频细节→频率恢复/轻量salience与nested token sets→多预算视觉表示应兼顾非salient结构，而非只录FLOP |
| [11245 Mind the Sim2Real Gap in User Simulation for Agentic Tasks](https://arxiv.org/abs/2603.11245v1) | simulator排行榜常被视为真实交互能力→451人/165任务/31simulators对读发现过度合作、容易化和反馈偏差→sim fidelity与agent成功率须分开验收 |
| [11279 AI Psychometrics](https://arxiv.org/abs/2603.11279v1) | 单项ToM分数不等构念有效性→用psychometric validity框架检验四LLMs心理推理测量→可能改变模型能力评测的validity条件；Comments已accepted HICSS2025，先核早公开家族，不能因arXiv新ID重复处理 |
| [11320 UniCompress](https://arxiv.org/abs/2603.11320v1) | Unified理解/生成的discrete image token存算共同昂贵→learnable meta-token同时压缩/解压两任务接口→压缩应保持生成和理解共同表示合同 |
| [11327 Meta-Reinforcement Learning with Self-Reflection for Agentic Search](https://arxiv.org/abs/2603.11327v1) | 跨episode反思缺credit assignment→context反思metaRL加turn-level relative advantage→区分经验记忆与训练信号，不只搜索benchmark提升 |
| [11331 Jailbreak Scaling Laws](https://arxiv.org/abs/2603.11331v1) | 安全能力固定预算测量可能不稳→长度/计算扩张下经验polynomial–exponential crossover和受限理论→重新界定防护与测试资源条件；当前v4轻量核纠错信号，不自动逐版diff |
| [11337 RewardHackingAgents](https://arxiv.org/abs/2603.11337v1) | agent训练成绩默认评测器可信→evaluator编辑与train-test leakage两向量、fresh-workspace/可信标签与runtime access防护→评价完整性须限制两种写读权限，不把仅锁文件当充分 |
| [11351 Novelty Adaptation](https://arxiv.org/abs/2603.11351v1) | symbolic planner无缺失operator就不能适应新情况→LLM发现operator并给RL reward/policy学习→明确新operator怎样进入反馈验证，非仅模块编排 |
| [11356 iSWE Java Agent](https://arxiv.org/abs/2603.11356v1) | 代码agent自由编辑易误改→问题定位/编辑分工与rule-based静态分析/变换工具→可能通过typed操作收窄修改空间；需核工具具体机制，不借Java场景入选 |
| [11395 ARROW](https://arxiv.org/abs/2603.11395v1) | 固定replay不能同时适应新task/保留旧world dynamics→短长双buffer以distribution matching/diversity增强DreamerV3 replay→world-model continual memory应比较同容量和旧task retention |
| [11397 Edge-Cloud Speech Emotion Captioning](https://arxiv.org/abs/2603.11397v1) | edge受限又不宜整句上云→uncertainty-guided token/block选择性cloud escalation→有损音频draft路径的成本/隐私发送边界；不能自动宣称exact sampling或隐私证明 |
| [11415 BLooP](https://arxiv.org/abs/2603.11415v1) | 流畅摘要可偏离source→来源bigram lookup对生成token概率boost→改变source fidelity vs采样policy，非事实性保证 |
| [11447 Group Competitive Learning](https://arxiv.org/abs/2603.11447v1) | 小VLM SFT难兼顾navigation偏好→guide/learner不对称group competitive objective→训练目标与语义分布正则的取舍，不凭社会导航应用重收 |
| [11513 Retrieval Utilization Across Model Scale](https://arxiv.org/abs/2603.11513v1) | RAG失败常归检索质量→oracle/no-retrieval与parametric knowledge split分离utilization/distraction→小模型context利用可能比retrieval提升更关键；Comments明确Zenodo早稿/此次updated draft，先核本次新增而非newID |
| [11535 Expert Threshold Routing](https://arxiv.org/abs/2603.11535v1) | 固定topK或batch expert-choice约束自回归算量/因果性→全局token分布EMA的per-expert阈值，逐token独立训练/推理routing→可考虑动态算量但须核无专家命中/平衡/threshold drift |

## 三项只需决定准入的核心，不自动全文

- [11228 Markovian Generation Chains](https://arxiv.org/abs/2603.11228v1)：迭代改写/翻译的Markov chain、temperature改变recurrent class可能揭示生成多样性退化，但有限状态收敛本身是已有结论；需只读新机制/实证干预是否改变长链模型设计，不能因统计物理/Markov词入选或因有限模型排除。
- [11382 Unified Continuation-Interest Protocol](https://arxiv.org/abs/2603.11382v1)：QBM latent measurements识别内在/工具性continuation，gridworld已知label/插值测试可能只是新classifier且未对LLM成立；只需核控制条件/observability是否新增可复用agent评价边界。不因小模型自动排除，不用quantum类比代替证据。
- [11495 Tool-DC](https://arxiv.org/abs/2603.11495v1)：divide-and-conquer/try-check-retry可能引入长工具集的分治重试接口，也可能只是现成步骤组合；只读partition/check/retry与训练标签具体新增，给出是否改变工具选择/错误恢复的决定理由即停。

## 五项具体贡献前关闭：待分层独核，不追日期

- [11322 Embeddings to Dyson Series](https://arxiv.org/abs/2603.11322v1)：完整题摘是把Transformer表成非Hermitian operators/Dyson解释框架，未给实际新增算法、适用界/反证或可改变设计的验证；概念重表述与可映射attention本身不足。不否认理论价值；当前v2只轻量事件信号，不因版本号展开。
- [11399 Entropy Guided Diversification/Preference Elicitation](https://arxiv.org/abs/2603.11399v1)：具体增量是产品属性偏好提问/entropy去重的推荐应用，未识别模型训练、检索表示或agent执行的新可靠性合同，agentic名称/用户指标不足。
- [11445 Verified Multi-Agent Orchestration](https://arxiv.org/abs/2603.11445v1)：完整题摘为plan DAG/专职agent/LLM verify/replan stop的编排组合及25market任务收益；没有新执行原语、失败边界或独立有效性证据，控制术语不能代替增量。
- [11461 CoViLLM](https://arxiv.org/abs/2603.11461v1)：制造装配中的深度相机定位human/component分类+LLM自然语言规划，题摘未新增模型或机器人执行/反馈的机制、适用界或反证；不因组件齐全/速度提升映射VLA。
- [11528 Highly Autonomous Cyber-Capable Agents](https://arxiv.org/abs/2603.11528v1)：159页的能力预测、战术分类、战略风险和政策建议；完整题摘未给当窗实证事故/实际防护接口变更或模型系统机制证据。安全主题不等真实新安全约束事件；明确安全信号须独核，不采纳攻击战术细节，也不把长度作为排除理由。

以上保留作者首读判断，不能当当前最终层级。root实际25AB校准为15P/5决定core/5EX；五core后实际原证校准四P/11382具体EX。11279官方HICSS2025-01-07重呈现关闭、11513ZenodoMarch5同稿而当前未识别重要增量重呈现关闭，署名差异/updated原说明与必要已读反侧保留。故目前第二包17项窄P普通必要待办、六具体EX和两事件关闭；日期夹证见SUP_DATE_SECOND.md，身份/Source各按单项推进，不授所有P Evidence。11228已准备必要Source/PRE并窄写待POST；不因已有Books覆盖或深审成本关闭家族。
