# 02-17 增量准入首包与有限恢复

本轮授权：只补遗漏；补充窗为2026-02-16北京自然日。原77候选/日期/评分/有效Source与Books、09:00窗口和原§4连续正文全部冻结。本文不以Submitted、Atom published、DataCite Created/Registered/Updated或邻ID决定首公开。

## 有限入口与停止

每日14源有限日期/主题搜索，另四主题精确日期搜索未返回arXiv结果，均不授零命中；原输出见supplement-search0～3及supplement-arxiv-topics。四Atom主题的发现范围先为Submitted 02/12～16，首50出现被02/16提交占满的截断；只对受影响主题缩窄到Submitted 02/13日，max100/start0，实际72+2+47+29=150出现，均到totalResults，停止，不继续整类/全年/catchup。Submitted只是发现过滤，不是public。全部精确URL、时间、身份和current版本题摘见supplement-arxiv-native-20261008.json及supplement-arxiv-narrow-20261008.zlibbase64.txt（base64→zlib→UTF8 JSON）。后一批非旧139题摘78唯一身份，已读完整摘要；易读原件见supplement-new-abstracts0～3-20261008.json。分层范围/贡献关闭不为日期再扩恢复。

官方日路径的Web恢复失败；旧YYMM月路径原生404，修正为YYYY-MM后恢复月级目录，但没有16 Feb日级批次标记，不能决定首公开。只定点检索78命中身份与相关标题，不把1935/18085等月库存变成逐项关闭队列。首公开日仍需同身份官方announcement/当期dated作者正文；月份与Submitted均不抬日期。

## 首批14条与复用

- CacheMind2602.12422：CPU cache replacement分析问答/trace检索的领域工具；结果是领域检索与缓存策略改进，摘要未新增服务LLM计算的runtime/缓存机制。拟贡献前关闭，公开日期未核；不因cache+RAG能映射章节而入池。
- MING2602.11966：四层以内CNN的MLIR/FPGA streaming HLS，未给LLM/基础模型计算的约束变化；拟范围关闭，日期未核。
- LoRA malware2602.11655：设备侧既有LoRA适应+协调器聚合在IoT攻击识别中的收益，未给新聚合机制、可比隐私约束或传递条件；拟贡献前关闭，日期未核。
- OServe2602.12151、AuroraRL2602.11456、PASCAL2602.11530、GORGO2602.11688、PrefillShare2602.12029：定点身份去重，已有02-14有效原记录；不继承题摘current数字、不重审或改其原日期。
- PAM2602.11521：02-14已有具名prior-public/原式保留，复用终态隔离，不签新的Feb16贡献。
- Roofline2602.11506：02-14已有具体贡献前关闭（未归一化混合Φ不足建立新可比机制），不重开全文。
- RynnBrain2602.14979：官方repo News标2026.02.17发布Technical Report、2026.02.09代码/weights；两个不同事件均不属于02/16。只作真实归属恢复线索，不用第三方Feb10替原正文日期，未审后续1.1。
- SpargeAttention2 2602.13515、AsyncVLA2602.13476、FlowHOI2602.13444：完整题摘潜在增量分别是hybrid masking/蒸馏稀疏目标、异步高低频控制与轨迹加权、HOI pose/contact消费表征；具名官方repo/精确abs恢复未给可用Feb16首公开字段。暂为日期保留，不评分、不列确认候选、不进入Books。

上述正文/日期原源恢复见supplement-specific-originals-20261008.txt；RynnBrain技术报告/代码事件分开。没有新增已确认候选。

## 后续78条完整题摘校准清单

题摘是发现/贡献依据，不是exact-v1必要证据审阅。current v2/v3只用来定位身份与潜在增量，不把当前数字带回v1。以下潜在贡献已由root逐项完整AB独立校准，不因日期受阻改成贡献EX；校准不授必要公开日、性能或Books，具体限制见supplement-independent-20261008.md：

| ID | 原约束 → 潜在实际增量 → 若成立将改变的选择 |
| --- | --- |
| 2602.13529 | 联邦LLM隐私/效用冲突 → sanitized/revealing双LoRA的token gate → 需区分路径授权与攻击泄漏，100% routing不等安全保证 |
| 2602.13524 | attention奇异向量feature解释缺依据 → 充分条件与sparse decomposition可检验预测 → 收窄何时能以SVD识别feature |
| 2602.13517 | 长度不可靠地代理reasoning compute → 深层prediction修正的deep-thinking ratio/前缀拒绝 → 重考虑sample选择与成本归因 |
| 2602.13498 | orthogonalization抹掉幅度且能量burst → RMS+相对能量trust region → 重新比较几何更新/步长稳定边界 |
| 2602.13483 | circuit只解释head名称 → 单forward的attention-causal子空间信号与prompt cluster → 不把跨prompt/语言组件复用当相同信号 |
| 2602.13466 | NTP hidden memory重构信息不足 → regeneration+causal双目标、冻结encoder curriculum → 比较计算压缩与信息恢复的成立条件 |
| 2602.13452 | 翻译质量与危机urgency被混同 → 同情景跨语言urgency漂移、人类判断稳定反侧 → 重新考虑测量identity/构念，非仅新语料 |
| 2602.13379 | 单轮安全测试遗漏工具多轮 → taxonomy+新tool自探索test/effect经验 → 定位真实执行风险与防御边界 |
| 2603.05520 | 单agent局部隐私不授串联隐私 → mutual-information composition界/flow regularization → 重考跨agent中间表示泄漏 |
| 2603.02238 | Transformer有限长度成功不授全长度 → C-RASP不可计算界/positive fixedprecision可计算且指数界 → 收窄length extrapolation保证 |
| 2602.13370 | free-text agent communication语义漂移 → shared-graph typed ops/explicit traversal → 检验可验证trace与“消除hallucination”是否混同 |
| 2602.13367 | 3B多能力互相挤占 → point/pair reward、complexity reward与turn supervision组合的具体长期交互条件 → 需正文限定非只ranking |
| 2603.02237 | global steering假定concept均质 → mixture-cluster OT/input-dependent barycentric shifts → 重新考虑局部vs全局方向 |
| 2603.09989 | hallucination自动分数不等用户经验 → SHS人类构念与response维度 → 不把感知量表当detector/benchmark真值 |
| 2603.02236 | CUDA编译通过不授功能或资源有效 → text-to-CUDA执行验证+roofline metric → 重新比较评测分母与硬件边界 |
| 2604.06185 | 人工complex tool tasks遗漏真实用户行为 → compositional/implicit intent/transition协议与57模型低准确反侧 → 重考tooluse benchmark代表性 |
| 2602.15902 | 每prompt context distillation更新太贵 → single-forward hypernetwork生成LoRA → 比较无原上下文QA与容量/更新成本边界 |
| 2603.02232 | binary preference heuristic margin没ordinal生成模型 → learned thresholds的NLL/all-threshold → 重新考虑等级反馈reward目标 |
| 2602.12546 | ASR语音/文本外部encoder适配 → disjoint MoE+hybrid causality+CTC/text CE单stack → 对比表示/生成路由语义 |
| 2602.12533 | 固定modality steering强度伤敏感样本 → functional contribution诊断+instance-aware scaling → 重考modality证据消费的局部调节 |
| 2602.12506 | VLM RL只看accuracy → grounding/CoT faithfulness与鲁棒性的反向收益、augmentation shortcut → 修正优化与测量归因 |
| 2602.13530 | semantic memory retrieval不处理episodic推理 → time-aware gist/fact hybrid graph+iterative tools → 重新比较history事实与derived memory |
| 2602.13521 | NL2SQL restate schema不修正misconception → mistake-derived knowledge+applicability-conditioned index → 具体反馈何时可复用 |
| 2602.13516 | 隐私只看typed文本输出 → click/scroll/navigation的行为oversharing、prompt mitigation反侧 → 重新界定外传trace与最小上下文 |
| 2602.13477 | orchestrator有access control不等组合安全 → indirect injection多agent泄漏 → 明确授权控制与信息流/任务分解的边界 |
| 2602.18493 | querytime RAG不维护演化state → once-built CRUD memory、QA-branch reward分组Task-Stratified GRPO → 重考query-independent维护监督 |
| 2602.13363 | 编码agent一般能力不授滥用能力 → 40agent真实website/codebase测量关联 → 需限定可执行危害评测与抽象ranking |
| 2603.00077 | rubric structure不消除judge偏差 → criterion-specific校准/拒判/ensemble实验无universal mitigation → 重考统一评价堆栈的适用边界 |
| 2602.12510 | multi-vector索引/search成本随patch数膨胀 → model-aware pooling+coarse stage再exactMaxSim → 比较不重训的质量/存储/检索取舍 |
| 2602.13515 | topk/topp在高稀疏失效 → hybrid masking+distillation目标 → 比较稀疏注意力损失与生成目标差额 |
| 2602.13476 | slow semantic VLA阻断control loop → remote guidance+fast edge adapter、动态轨迹加权 → 比较延迟下reactivity/semantic控制 |
| 2602.13444 | endeffector轨迹不表示接触结构 → hand/object/contact HOI消费接口 → 比较retargeting与physics执行条件 |
| 2602.12686 | 图像sign语义不等3D行动 → sign-centric spatial-semantic表示 → 重考VLM场景编码与导航消费接口 |
| 2602.12679 | 双向I2V路径各随条件motion prior发生分叉 → forward residual向reverse路径distillation → 重考inbetweening路径耦合 |
| 2602.12616 | 单环境CP不授shift安全 → nuisance-conditioned生成数据+robustCP discrepancy → 检验模型误差与控制证书边界 |
| 2602.12498 | negation机制诊断与uniform微调脱节 → CTE调制逐层gradient → 需判断是否有一般模型适应增量，而非自动按医学域排除 |
| 2602.12639 | semantic accuracy与legal style被混同 → authentic/restored对比对学习feature coefficients及judge经验 → 需区分评价构念、局部校准与一般有效性 |

以上37潜在贡献均未获得必要首公开日；没有以Submitted或月列表进入确定候选。必要日期恢复只围绕这些身份及已有官方批次失败进行，后续若可取当期announcement或dated作者正文，仅重开对应家族，当前不支持任何正面Evidence/Books/无遗漏。CLASE12639经root完整AB独校撤销法律域一刀切EX，准入限定为评价构念/对比校准接口；一次官方abs只给Submitted，作者repo当前LREC2026 May citation不授首次公开日（supplement-clase-date/project-date-20261008原件），不拉全文绕过日期门。

撤回关闭：[2602.13376](https://arxiv.org/abs/2602.13376) An Online Reference-Free Evaluation Framework for Flowchart Image-to-Code Generation。2026-10-08必要官方事件页检查发现current v2（Submitted 2026-07-09）明确withdrawn，history中v1也标withdrawn；Comments解释内部审阅未完成即公开并由作者撤回。完整题摘仅作原始记录，退出潜在准入链，不评分、不进入Books；不为其补无关首公开日期。当前官方说明及history落盘于supplement-date-fields-20261008.json，撤回影响仅限本次新线索，不修改旧77。

## 明确关闭项（日期未核）

| ID | 具体范围/贡献理由 |
| --- | --- |
| 2602.13504 | Turkish新闻AI检测BERT域训练，新增语料/发生率估计，不改变模型/系统机制 |
| 2603.04418 | 图时空预测的JFT/FreST loss，摘要无foundation/model系统的具体新增边界 |
| 2602.13419 | 化学retrosynthesis的保护基规则/状态，AI for Science暂缓 |
| 2602.13087 | time-series classification的VQ压缩XAI/SSA，没有本项目foundation机制差额 |
| 2602.13084 | HR competency workflow与库embedding匹配，领域评分有效不授新Agent执行机制 |
| 2603.09990 | NDA分段LLM+LegalRoBERTa组合，仅合同域结果，无新生成/执行条件 |
| 2602.13003 | 目标检测与trajectory forecasting object融合，非基础WorldModel/VLA机制；主收益为nuScenes域预测 |
| 2602.12921 | Bengali idiom corpus/benchmark增加低资源条目，题摘未发现新的评价盲区或模型机制 |
| 2602.12889 | fortune-telling symbolic chart题集与固定reasoning order，未给新可验证机制/可迁移评价边界 |
| 2602.12871 | DSM临床diagnosis/病例知识图谱，领域医学研究暂缓；不借Evaluation重新入池 |
| 2602.12798 | 一般network telemetry MPN greedy routing，不服务foundation compute/state通信 |
| 2602.12708 | 一般vertical federated sample alignment，预设experts服务CIFAR/tabular缺失，未给本项目foundation训练边界 |
| 2602.12681 | 二进制code similarity模型的变换鲁棒性，非LLM/code-agent系统增量 |
| 2603.02231 | 波场PE-PINN物理嵌入，AI for Science暂缓 |
| 2603.09987 | LLM tabular feature-transform经验库/selection组合，领域性能结果未给新记忆成立条件 |
| 2602.13473 | EEG pipeline演化/生理先验，AI for Science暂缓 |
| 2602.13458 | Moltbook人口social portrait，未新增执行/委派机制或可靠性设计边界 |
| 2602.15066 | LLM depositors银行run社会仿真，领域经济结论非模型机制 |
| 2602.13405 | 通用probabilistic multiagent temporal logic验证，未给foundation驱动执行的直接机制关联 |
| 2602.15064 | Moltbook社会网络形状对比，非Agent执行机制；统计population特征不足新的设计选择 |
| 2602.13088 | cyborg propaganda政策/治理概念分析，不是模型/平台机制研究 |
| 2602.13047 | 临床cognitive screening族群差异，领域医学研究暂缓 |
| 2602.13372 | trolley ethical Gym/SafeRL，未见LLM/foundation模型具体测量协议差额 |
| 2602.15062 | UN financing合作博弈，非模型/系统研究 |
| 2602.12875 | 普通microservice/media streaming的SLO控制平台，不是LLM资源/证据平面机制 |
| 2602.12873 | tutoring社会机器人访谈知识需求，非可验证VLA执行/模型机制 |
| 2602.12833 | ICU协议state与四agent预测组合，医学应用研究暂缓 |
| 2602.12830 | 一般stochastic game singlebit equilibrium，不是LLM agent通信边界 |
| 2602.12763 | comedy machine identity的人类偏好实验，领域使用收益非prompt机制成立条件 |
| 2603.02233 | 通用PFL kernel-mean finite-risk/RFF理论，当前题摘没有foundation训练/平台切片直接差额 |
| 2602.13353 | 通用meanfield riskaverse equilibrium理论，无model-driven agent执行的直接设计关联 |
| 2602.12517 | stationary meanfield game benchmark taxonomy，无基础模型训练/Agent协议实证 |
| 2602.12502 | 传统drone small-team策略DP扩队，不是foundation/VLA/LLM多agent机制 |
| 2602.13041 | dietary portion几何重构benchmark，AI for Science领域应用暂缓 |
| 2602.12877 | Indian-road QA新增dataset/baseline，未新增基础多模态机制或具体评价盲区 |
| 2602.13361 | image separation双diffusion+wavelet去雨雪，领域恢复网络非生成基础模型采样机制 |
| 2602.12659 | 区域face人口dataset+既有INLP，扩条目与局部公平性结果无新的评价/模型差额 |
| 2602.12597 | 智能cane的已有perception/planning/LLM组合，无新增控制接口/状态机制 |
| 2602.12540 | JEPA应用LiDAR OCF与proof-of-concept收益，未给相对既有JEPA新机制/成立边界 |

37潜在贡献+39明确关闭+1官方撤回关闭+RynnBrain1窗外=78。首批14另外含10不在78内的旧日/领域身份；不把不同入口重复计候选。No Change仅指本轮Books无新写，旧52整合与4已有覆盖均原样保留。

本轮root增量DAY已实际通过：全部37潜在AB、官方撤回及最终普通EX8/39分层样本独校，其余31普通EX不声称逐项独核；CLASE初筛纠正及一次必要日期尝试已落实。确认新增0、新Books写入0，37日期身份与来源缺段安全隔离，不授Coverage/Evidence或无遗漏。本日报六部分与最终机器结果为完成入口；原77/原窗口/连续§4及有效Source/Books冻结，未改共享文件、stage/commit/push或开始其他日。
