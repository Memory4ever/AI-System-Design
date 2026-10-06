# 有限筛选 — 2025-10-06

作者Huygens。BJT窗口 `[2025-10-05T09:00:00+08:00,2025-10-06T09:00:00+08:00)`。原请求实际UTC2026-10-04 23:32～23:38；必要core23:45～23:52。请求时刻不是历史公开时刻；raw仅为原件，不为已读证明。

## 查询与停止

arXiv统一 `submittedDate:[202510050000 TO 202510052359]`（UTC提交日期仅恢复线索），`start=0,max_results=40,sortBy=submittedDate,sortOrder=ascending`。四条实际query主题部分如下；完整编码URL及执行时间分别在 `arxiv-{model,systems,agent,multimodal}.receipt.json`。

1. `(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:LLM OR ti:transformer OR ti:"mixture of experts") AND (ti:architecture OR ti:training OR ti:optimization OR ti:reasoning OR ti:attention OR ti:compression OR ti:sparsity)`：7命中。
2. `(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (all:"language model" OR all:LLM OR all:transformer) AND (ti:GPU OR ti:kernel OR ti:parallel OR ti:serving OR ti:inference OR ti:quantization OR ti:cache OR ti:communication)`：1命中。
3. `(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:"language model" OR all:LLM) AND (ti:agent OR ti:RAG OR ti:retrieval OR ti:memory OR ti:tool OR ti:planning)`：22命中。
4. `(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:"vision language" OR ti:"vision-language" OR ti:VLA OR ti:"world model" OR ti:"multimodal language" OR ti:"diffusion model")`：8命中。

38命中跨分类去重37。每条首批返回数均小于40，止于首批；不能将Atom published当first-public。提交切片不能覆盖未在此提交的本窗修订或未显示历史公告，保留该限制。

有界标题补检同一提交日期，分类CL/CV/DC/PL/IR，`start=0,max_results=25,ascending`：实际25/59、25/45、3/3、2/2、10/10，共65条标题已浏览；CL/CV止于首25，不抓其余total形成队列。只恢复29个相关标题，连同四主题共66份exact-v1题摘。标题补检选择见restore.py显式ID，非关键词自动准入。所有66完整题摘和页上版本史实际读完；当前页未显示撤回标记，不据此证明全版本无勘误。

辅助官方域搜索实际两条输入及完整响应保存在 [SEARCH_RAW](./SEARCH_RAW.json)：`"October 5, 2025" "research" "model"` 限openai.com/ai.meta.com/qwen.ai/minimax.io；`"Oct 5, 2025" "language model" agent research` 限openai.com/ai.meta.com/agent.minimax.io。response_length=short，合并首批5结果后停止，主要为社区/论坛线索，无可采用官方研究事件；不证明对应机构无事件。

本次窄同步不认领SEARCH_RAW所指搜索的执行时刻，也不以其他原件请求23:32～23:38Z替代。保留原查询/响应，不改原响应或补造时间字段；README已撤销该时间虚指。

## 明确关闭与旧事件

| exact-v1 | 处置依据 |
| --- | --- |
| [04002](https://arxiv.org/abs/2510.04002v1) AgriGPT-VL | 农业多模态数据与既有多阶段/GRPO训练用于领域指标，题摘没有另一个可识别的通用机制或失效证据；AI for Science暂缓，不以“有训练”绕回owner |
| [04017](https://arxiv.org/abs/2510.04017v1) Zephyrus | 气象科学数据、工具与Agent benchmark；没有改变当前模型/执行机制的具体增量，按暂缓范围关闭 |
| [04020](https://arxiv.org/abs/2510.04020v1) SFP | 标题World Model含糊，已补§5：SEVIR/海洋热浪/PDE/CFD、CSI/TKE等科学预测目标，无action-conditioned控制；本次科学应用路线暂缓 |
| [04127](https://arxiv.org/abs/2510.04127v1) ANN hashing综述 | 摘要明确早期投影/量化历史入门，未指出新增机制、评价混杂或改变当前检索选择的反证；不是因“综述”统一排除 |
| [04139](https://arxiv.org/abs/2510.04139v1) 低资源微调指南 | 数据整理/文化适配/Gemma2微调复制流程，题摘未识别新的目标、机制或可比有效性条件；非因小模型或低资源语言关闭 |
| [04145](https://arxiv.org/abs/2510.04145v1) SiteShield | 既有LVLM+RAG加入现场音频的建筑报告应用；没有新增通用检索/融合机制。因安全主张实际读v1 PDF pp15–16、24–25及结果示例：两位有建筑经验研究者评25报告，有真实有限验证，但不能推为自动现场安全/法规保证 |
| [04239](https://arxiv.org/abs/2510.04239v1) IADSR | LLM只提供item语义embedding，改进传统序列推荐的冷item去噪；未改变foundation model或LLM检索/Agent机制；不因有IR分类纳入 |
| [05179](https://arxiv.org/abs/2510.05179v1) Agentic Misalignment | 本日own Anthropic Research Flight `publishedOn=2025-06-20T22:30:00.000Z`，与官方[六月原文](https://www.anthropic.com/research/agentic-misalignment)同标题、16模型、虚构企业二元困境和相同中心安全主张。v1 §3/6与官方Methods/限制定点比较，未发现所核命题的本窗重要新增事件。仅该命题的first-public归六月，不称全文逐字相同或六月已经独立审毕；保留安全反侧与归属恢复线索 |

关闭贡献者不继续请求不影响处置的first-public日期；05179是已有明确窗外发布依据，不混同后来arXiv收录。

## 58项日期隔离潜力

下表每项均读完整题摘后指出实际增量。它们尚无完全落窗官方first-public时刻/bounds，故不评分、不进入正式候选、不授正面Evidence/Books。仅允许恢复该ID的官方历史公告/原发布事件，不能将58项变成全文附件队列。必要安全、反侧及含糊scope定点core见 [CORE_BOUNDARIES](./CORE_BOUNDARIES.md)。

| ID（均2510.*v1） | 原约束 → 实际增量 → 需重新考虑的选择 |
| --- | --- |
| 03984 | 静态persona评测漏偏好变化 → 两会话reference interview/偏好carryover测试 → 长期个性化评价粒度；仍为有限case |
| 03992 | clean工具选择掩盖metadata攻击 → 自适应工具注入和分布置信下界 → 工具检索/选择可靠性评价 |
| 03993 | 未标注分布未知时伪标签失衡 → 可控标签混合、logit调整、筛选反馈 → 自训练分布假设 |
| 03999 | 单轮审计漏长期欺骗 → performer/supervisor状态与整轨迹auditor → 审计粒度和judge边界 |
| 04009 | 创造力单分指标混合维度 → convergent/divergent并列U/O/S协议 → 评价选择与能力取舍 |
| 04013 | 自报置信过度自信 → 首输出token隐状态正确性分类 → 早期审计，不能当正确性证明 |
| 04016 | 语音Agent句尾等音频才判 → 泰语粒子文本EOT比较轻量Transformer/LLM → 特定语言端点延迟/质量边界 |
| 04019 | diffusion token概率昂贵 → 对真实unmask轨迹均匀MC估GRPO目标 → 训练预算/方差选择 |
| 04022 | 固定视频token预算浪费非目标帧 → 低fps定位后重分配span并联合IoU/答案reward → 输入与训练预算 |
| 04023 | DS Agent评价重功能少治理 → 45系统生命周期与缺少显式机制的统计 → workflow评价盲区，不推不安全率 |
| 04024 | 视频/叙事组合漏fabrication → 四类多对多构造和不确定性主动增广 → 数据覆盖而非只换fake-news应用 |
| 04031 | 自报词重要性未改变决策 → counterfactual生成并检查/精炼 → 黑盒解释评价，非因果faithfulness证明 |
| 04032 | 医疗专训默认优于通用 → 17小模型QA/摘要对照出现反例 → 域SFT选择；不推临床部署 |
| 04034 | 文本编辑回环不一致 → cycle-consistent attention reweight → 生成编辑的一致性机制 |
| 04039 | 大量GUI训练仍漏局部目标 → iterative spotlight和工具聚焦 → grounding数据/视觉预算替代 |
| 04041 | VLA imitation无法搜索后果 → world/simulator rollout奖励选动作 → 控制计算与oracle边界 |
| 04044 | 层内权重范围使低比特失真 → 变换权重的层局部min-convex搜索 → CNN量化设计，不外推LLM |
| 04045 | 价值立场与CoT训练混合 → 人工/合成/GRPO与faithfulness/offensiveness对照 → pluralistic对齐协议 |
| 04058 | 无retain数据难unlearn → variational塑性项与参数稳定项 → diffusion遗忘的假设和残留边界 |
| 04066 | 低比特去摩尔纹banding → 极值保FP16和频率校准 → 局部生成质量/量化约束，非只PSNR数字 |
| 04067 | CE总量默认同一power law → 分解error-entropy/self-alignment/confidence → scaling指标解释 |
| 04071 | DLM数据效率被归因目标 → 同架构mask/MLP dropout/decay对照 → 多epoch正则化替代解释 |
| 04072 | on-policy rollout慢且off-policy漂移 → 同batch短快轨迹与慢校正 → RL稳定性/采样计算选择 |
| 04080 | listwise reward信用分配失败 → point-to-hybrid curriculum和index-slice归因 → 排序RL目标 |
| 04081 | NL合成链难验证 → executable CodeCoT后反向指令/过滤 → 数据生成，执行不证明语义真 |
| 04090 | 分类输出维度随类别数增长 → 固定latent目标向量和最近邻 → 大类别表征/持续学习替代 |
| 04096 | 静态偏好评价漏对手适应 → ranker竞争反馈与OOD对手 → 非静态奖励训练 |
| 04120 | 隐喻分数混合上下文/语法线索 → contextualized/decontextualized和shuffle反例 → 能力归因条件 |
| 04128 | reasoning token差异只观察 → crosscoder特征干预 → backtracking与feature的局部因果测试 |
| 04135 | 只调prompt忽视agent配置成本 → 多目标Pareto配置/生成代码协同 → 质量/运行预算设计 |
| 04136 | AVSR输入压缩破坏跨尺度 → shared router/expert和Matryoshka token压缩 → 多模态表示预算 |
| 04142 | 多教师推理分歧传递偏差 → learn/compare/critique APO概念对齐 → 蒸馏一致性；局部CXR非临床验证 |
| 04173 | 框架绑定Agent描述 → declarative Agent Spec interchange → portability契约；不以宣传benefits为保证 |
| 04174 | debias须知bias/反例 → bias-domain生成配对、自适应修正和对齐 → 标签/生成数据假设 |
| 04195 | 增量空间图累积矛盾 → 来源关联version control和edge-impact最小修复 → memory更新粒度 |
| 04206 | 多任务多轮RL执行异构 → async生成训练/function-call容器接口、cross-policy采样和task优势归一 → 生命周期/优化边界 |
| 04212 | BF16 Flash Attention固定失稳 → 相同batch复现、低秩舍入链、定点softmax修改 → 精度稳定性归因 |
| 04214 | 单reward平均掩盖业务约束 → RM/RJ/programmatic增强组合 → 异质奖励选择；谈判局部人评 |
| 04226 | 文本多样性不等claims多样 → claim decomposition跨27模型/12国/RAG对照 → 知识多样性评价及judge噪声 |
| 04234 | 固定控制policy不能改目标 → diffusion-MPC reward/projection及交互更新 → action/state规划；投影非全闭环安全 |
| 04246 | 多帧VLA训练推理开销 → 过去帧amortized单context token → 部分可观测动作表示预算 |
| 04257 | 文本注入评测漏图中文字 → black-box字体优化/策略检索 → 多模态攻击面与可见性取舍 |
| 04284 | outcome reward掩盖问诊过程 → 分层veto+过程/结果reward与经验回收 → 长轨迹训练反馈，不授临床安全 |
| 04293 | 独立RAG chunk丢文档结构 → 可训练树路由/自动action curation → evidence装配机制 |
| 04303 | 单heuristic漏多Agent隐蔽协作 → channel干预、MI/fairness等联合检测 → 审计覆盖；理论估计假设仍争议 |
| 04311 | MAS/SAS比较忽视复杂度 → depth/width形式化与受控任务 → multiagent收益条件而非普遍优胜 |
| 04317 | fairness工具人工配置难控阈值 → Agent迭代指标/mitigation调节，对两数据集目标阈值误差 → 局部控制边界 |
| 04340 | SFT混合trait一起泛化 → 训练时诱发trait提示、测试撤去 → 选择学习，不等遗忘/永久防后门 |
| 04347 | encoder后门罕见trigger控制分类 → attention/gradient异常与净化 → 防御依赖clean校准/攻击类别 |
| 04365 | 单瞬时观测需补历史却引噪声 → backward/forward diffusion与dual-head aleatoric传递 → 生成不确定性传播，非交通安全 |
| 04371 | Agent串行慢调用 → 猜测动作并发预执行/逐步匹配 → 延迟/成本选择及不可逆effect边界 |
| 04373 | 离线失败trace难复用 → zooming蒸馏为状态相关hint并检索 → memory证据粒度与适应预算 |
| 04392 | paraphrase一致性混检索/生成 → 分层固定检索评估和PS-GRPO相似reward → 一致性与事实真分开 |
| 05168 | QIF表达力但训练不稳 → 离散化与参数导出的surrogate窗口 → SNN组件学习稳定性，不因非Transformer关闭 |
| 05173 | T2I安全拒绝损效用 → EOS embedding recognizer+SAFE搜索 → 检测/修正路径及adaptive边界 |
| 05174 | synergy与时间耦合混同 → TDMI/PID三随机干预及无协作baseline → MAS协作评价而非拟人化 |
| 05176 | KV离群值隔离仍不flat → 在线pattern对齐后量化残差 → 状态量化与额外模式维护 |
| 08595 | 总数学准确率遮蔽失败类型 → sentence clustering诊断 → 评价粒度；trace标签不能证明句级skill因果 |

正式候选0；58日期保留、7贡献关闭、1既有窗外主张。Curie FIRST实际通过，DAY已核36必要信号、14来源与16个完整AB样本；未把日期潜力升级为Evidence。唯一剩余是本次搜索时间虚指撤销与旧FIRST路由句更新的Curie窄POST，不重读有效核心。下载全集不要求逐篇全文；本日36有限core停止于对应命题，未读其余30全文或全附件。
