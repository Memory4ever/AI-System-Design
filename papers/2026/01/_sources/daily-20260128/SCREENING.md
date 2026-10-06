# 2026-01-28 独立发现与题摘筛选

作者：jan28_v3。检查窗口：2026-01-27T09:00:00+08:00 ～ 2026-01-28T09:00:00+08:00。

2026-10-04 独立纠错：Submitted≠公开，但官方Friday14ET～Monday14ET→Monday20ET给最早公告下界。Jan23T19Z～Jan26T19Z提交项结合created可访问上界，93个arXiv事件完整包络落窗，逐项原值与包络见DATE_BOUNDS.json；它们不是93候选。表内旧“日期隔离”标记仅对16986～17087中10项仍有效，其他项按REVIEWS的实际贡献/证据停点继续；不因日期恢复称已审全文。原增量共同误收理由只在具名受影响项重新校准，不扩池。

本记录不把 registration、Submitted 或 Updated 当 first public。以下仅是完整原题摘后的潜在贡献判断；日期仍缺必要证据者不是确定当窗候选，不评分，不引用其性能/安全主张，不进入 Books。原文题摘和精确 v1 链接在对应 `abs-NNNNN.json`，不用此表代替原文。

## 有界发现

四个 arXiv API 主题查询全部 HTTP 429，原请求见 `theme-{model,multi,agent,system}.json`，不是零命中。以 DataCite registration 窗口 2026-01-27T01:00Z ～ 01-28T02:59:59Z（覆盖截点两侧，仅为发现）做 model/multi/agent/system 标题同义主题恢复：165/76/152/49 条，model/agent 各 2 页，其余各 1 页，实际页 URL 和全部响应在 `scope.json`。跨组去重 377 条，不是当日新论文数，也不是逐项摘要或全文队列。

monthly 分类标题只作相关线索补检和定点日期恢复：CL skip700/show500 与 skip1200/show500、LG skip1500/show1000 与 skip1000/show500、CV skip1000/show1000、DC skip0/show2000、AI skip1000/show1000。主题为基础语言/多模态模型、Attention/MoE/学习/后训练、推理/KV/量化/调度、Agent/RAG/记忆/评价与模型安全；无关领域标题未送入题摘队列。实际页见 `category-*.json`。这不是所有分类/全月召回；日期列表失效后不继续扩全月。

从主题查询与相关标题线索定点选取首批 4、第二批 50、第三批 50，共 104 个唯一 v1 题摘，均已完整实际阅读。随后 native 首查目录发现 Keel 和 DeepSeek-OCR2，各另读一个 v1 题摘；总计 106 个，不把 native 同家族重复算一篇。宽列表剩余标题不是普通待办。

## 日期必要终态：arXiv

官方 monthly 原始页没有逐日公告 day heading，只有月份和 Authors and titles heading。`official-daylist.json` 的 YYYY-MM-DD 列表 HTTP400，`official-yymmdd.json` 的 YYMMDD HTTP404，`official-advanced.json` 明示 announcement 过滤只到 YEAR+MONTH，替代 API 仍429。`availability.json` 仅支持一般公告节奏/审核延迟，不能确定材料身份属于某批公告。

`arxiv-meta-date.json`、`oai17063.json`、`oai17087.json` 的 OAI header datestamp 是 metadata modification；不可把它当首次公开。DataCite created/registered给首次可访问上界，Updated不用于公开时间；仅老Submitted的10项最早下界不完全落窗。示例：16986 Submitted=2026-01-05T07:42:58Z，Updated(v1)=01-27T01:00:08Z，created/registered=01-27T03:39:25Z；17063 Submitted=01-22T17:07:33Z，Updated=01-27T01:01:54Z，created/registered=03:41:11Z；17087 Submitted(v1)=01-23T08:46:50Z，Updated(v1)=01-27T01:02:25Z，created=03:41:43Z，registered=03:41:44Z。三者不能排除更早公开或确定落窗。17087的v2 Submitted=01-28T00:01:18Z亦不证明公开/重要修订落窗。对其余Jan23T19Z之后提交项，官方公告schedule与created共同建立Jan27T01Z到对应created(+1秒保守exclusive end)包络，已逐项复算，不再请求不可得day heading。

10个老Submitted必要保留项共享一个请求：恢复其ID与明确公告日的官方公告/list映射，或作者首次公开正文/不可回溯发布日志支持完整落窗区间。只在该ID重开；不从metadata modification造公开，不重扫全月。已清楚排除贡献项停止日期恢复。93日期可支持项的普通贡献/证据待办不记受阻。

## 104 个完整题摘的实际判断

表中通过准入只表示具体原增量值得核验，不是“已读全文”或实验已证。106个完整arXiv题摘（此表104+native2）中，当前候选冻结64家族、关闭30、必要日期保留12，无贡献判断普通待办；另两个非arXiv native日期保留不并入106。64家族必要证据/Books处置已root逐项独立通过，本报告六部分最终日级验收亦已root通过，直接复用REVIEWS不反复校准。关闭侧9代表样本完整原AB实际独立通过，18386安全信号另实际core通过；分层复核不是全30量验。首批16986/17063/17087贡献准入与17067关闭已由root实际读原完整AB校准。

| ID | 原文新增命题及被影响的选择 | 本次处置 |
| --- | --- | --- |
| 2601.16986 | reasoning KV 重要性由答案偏好反馈、LRFU 淘汰与 head 预算结合；改变只按历史 attention 淘汰的选择 | 保留，日期隔离 |
| 2601.16987 | 利用 reward model 最大分歧选择偏好比较，oracle 排名可能被 RM 同质评价扭曲 | 保留，日期隔离 |
| 2601.17006 | 可调难度的数学题合成与 curriculum 联动；是否超出既有合成 recipe 尚需方法辨别 | 未定，日期隔离 |
| 2601.17037 | 同一语义的图像理解与生成逆向任务不对称，不能把一个方向能力代理另一方向 | 保留，日期隔离 |
| 2601.17042 | MCR2 将 membership/subspace 解耦导出 sparse linear attention，改变二次 attention 实现路径 | 保留，日期隔离 |
| 2601.17050 | 单像素空间采样下身份可恢复阈值与行为任务质量不同，改变隐私/表示采样折中 | 保留，日期隔离 |
| 2601.17063 | SSD expert offload 下 recency/frequency 自适应缓存，RAM-only cache 策略不直接成立 | 保留，日期隔离 |
| 2601.17067 | 状态/context/latent dynamics 分类与功能评价倡议，未给原实验或新增具体失效条件；主题/术语归纳不足 | 贡献/范围关闭：无原实验/新条件的分类倡议 |
| 2601.17082 | 多模态道德判断随扰动/迎合/指令发生不同变化，单一文本评价不能代理鲁棒性 | 保留，日期隔离 |
| 2601.17086 | 编辑更新投影至 acoustic 保留语料 nullspace，限定一阶不变而非任意行为不变 | 保留，日期隔离 |
| 2601.17087 | 真实跨地域用户 vs LLM 用户代理的难度/语言差异，代理成功率不能直接校准真人 | 保留，日期隔离 |
| 2601.17123 | video beamforming 形成空间声场表示，支持通用 VLM 感知声源而不只摘要转写 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17133 | 异构 peer pairing 用无中心模型 profiling 与 LinUCB 调节 distillation | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17152 | role suitability 的 meta-debate+peer scoring；组合是否新增选择机制需有限方法辨别 | 贡献/范围关闭：多proposal/peer互评/均值分配无新成立条件 |
| 2601.17197 | 多模态比喻 reasoning traces 在讽刺/幽默等风格间迁移，限定跨风格训练选择 | 贡献/范围关闭：traceSFT/相关style迁移配方无新训练条件 |
| 2601.17212 | 查询特定 MMR 多样性动态融合，不训练即可改变 RAG redundancy/coverage 取舍 | 贡献/范围关闭：MMR/query动态diversity成熟检索recipe |
| 2601.17223 | 医学 risk-of-bias/evidence synthesis 的中间规则奖励；本次 AI for Science 应用路线暂缓，不从通用 verifier owner 绕回 | 贡献/范围关闭：暂缓AI for Science领域应用 |
| 2601.17261 | activation-gradient 子空间内 low-rank ZO perturbation，改变随机全空间查询效率 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17275 | frozen decoder 用 assistant latent K 与双奖励 latent 搜索替代显式长 trace | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17277 | 人工 code-switch 数据与机器合成在自然结构/模型表现上的差异 | 贡献/范围关闭：human codeswitch结构/人口差异未给新控制证据 |
| 2601.17311 | 有相关错误与有损通信的多数树协作，仅特定组织/计算指数条件出现收益 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17329 | answer-specific conformal reliability 加权偏好更新，改变统一偏好权重 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17334 | PPA 用 O(L^(1+p)) 介于 window/full 的注意范围，经验拐点而非一律线性替代 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17343 | 编辑 specificity 指标与真实 preserve 行为相关性弱，连续严格度控制 fluency 混杂 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17344 | benign autonomy 的不安全价值选择随 framing 改变，guardrail 并非稳定代理 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17348 | disability 场景下 speculative hallucination 超出视觉身份识别，需 lived-experience 判断 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17360 | RobustPrivacy 的 input radius/certification 与推荐质量关系；与通用模型隐私主线的直接论点尚需辨别 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17367 | pretrained adapter router 按 head 动态在 sparse/full attention 间切换 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17383 | 现实环境、query-agnostic 的视觉 prompt injection，扩大工具输入信任边界 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17399 | symbolic grounding score+Neyman 方差调度，聚合权重会改变模型排名 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17418 | app transition 图和不确定性 HTML 校验下的 query 节约规划 | 贡献/范围关闭：离线appgraph/不确定HTML/验证重试成熟组合 |
| 2601.17421 | token-level reasoning 信号随 scale 稳定但 training 影响利用程度 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17426 | syllogism 的 existential-import 假设影响模型判断，thinking/scale 并非同向 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17443 | personal memory 聚类避免冲突；平均化偏好会损坏固定预算个性化质量 | 贡献/范围关闭：memory相似聚类/merge成熟冲突压缩 |
| 2601.17450 | AI compiler 多阶段测试报告整合已有 OPERA/OATest/HARMONY；新 stage 边界与既有实验需辨别 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17467 | trace boundary 的 latent perturbation/answer agreement 自生成 reasoning detector 监督 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17500 | 配对 cased/uncased 检索中 lowercase 消除 gap，token vocabulary 是混杂项 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17507 | semantic VLM 与 latent dynamics 多策略融合/选择 motion prior | 贡献/范围关闭：softmax expertselection/linear prior融合为成熟分层 |
| 2601.17532 | passage NDCG 对 QA 不可靠，generator-aligned pruning 改变检索优化目标 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17549 | MCP 架构攻击放大与 MCPSec；具体安全保证未审不得采用 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17551 | contextual MAB 在部分反馈/无 calibration 下在线 energy-quality routing | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17564 | functional/stateless Jax ARC 环境批量执行，改变 RL reasoning environment backend | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17566 | query-only tool attack 保留任务结果同时放大服务费用 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17569 | 服务端 draft+端侧私人 profile 编辑迭代，个性化隐私并非只由数据驻留决定 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17593 | hidden state 对 DAG depth/distance 的几何编码，控制表面文本后 probing | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17602 | Bernoulli dropout/BEC 稀疏表示恢复的理论假设与 top1 保持 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17644 | multimodal RAG asset membership 与 caption leakage 的 inference 接口 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17645 | 无文本声音 meme 的文化含义与真人差异，通用声学 QA 不代理文化理解 | 贡献/范围关闭：新文化meme域失败与排名无新系统条件 |
| 2601.17654 | 频率/kernel 联合的 static/dynamic 能耗调度 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17668 | frozen weights 的轻量 sink gates forward-only 重建 KV 压缩 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17671 | pivot language 翻译与 self-teacher target reasoning 无标签迁移；是否成熟组合需方法辨别 | 贡献/范围关闭：pivot翻译/同policy一致reward无新正确性条件 |
| 2601.17680 | 连续采样 FFN 参数子集而非离散 expert pool，改变 capacity/compute 接口 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17699 | SQL execution 下 adaptive turn budget+composite reward，影响多轮 RL 数据效率 | 贡献/范围关闭：execution feedback/turn budget/reward成熟组合 |
| 2601.17702 | SAE K/Q 索引减内存但 CPU 搜索 wall-clock 可更慢，压缩不等于端到端加速 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17716 | 部分可观察情境中的提问信息增益与 thinking 差异，评价只答题会漏主动信息获取 | 贡献/范围关闭：IG问答game与CoT排名无新策略条件/预算控制 |
| 2601.17722 | database schema/SQL 状态转移提供可执行 agent 评价而非视觉 judge | 贡献/范围关闭：schema合成/SQL验收组合未揭示新盲区 |
| 2601.17737 | executable script+scene continuity 的视觉生成/脚本评价张力 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17744 | canonical intent、executor 授权校验与 append-only replay 重述既有 reference monitor 原则，AB 无新失效条件/可比证据；安全命名不是增量 | 贡献/范围关闭：reference-monitor成熟组合无新边界，安全独立已核 |
| 2601.17755 | degree比率结构检索与outcome-prob diff/entityoverlap reward为成熟shaping组合，无新credit条件 | 贡献关闭；必要§3.2～3.3已读 |
| 2601.17756 | temporal-shift RoPE 区分 subject 与 view reference identity | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17768 | fixed-shape schedule+verification/rollback 控制 batch-dependent nondeterminism | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17814 | 多模态 routing 同预算候选成本比较，输入信号与新域能力受控 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17818 | visual/text step co-pruning 基于 K L2，无显式 attention matrix，兼容 Flash path | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17824 | scoped crawling、语义变化再索引与 freshness/relevance 组合，未新增选择条件/机制对照；已有搜索 recipe | 贡献/范围关闭：既有freshness/relevance搜索配方 |
| 2601.17830 | diffusion representation 与既有 VAE encoder 对齐，避免额外昂贵 external teacher | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17855 | stateful drift 不能迁移时 universal load balancing 的有限 batch/integer 边界 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17868 | bidirectional dLLM video 的 visual cache async refresh+chunk anchors | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17879 | agent ThreadControlBlocks 的隔离异步 context 与重路由执行 | 贡献/范围关闭：async TCB线程管理无新执行或受控干扰条件 |
| 2601.17885 | per-token depth 3D lift/neighbor，text-aware readout+depth teacher | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17902 | dLLM ASR prior initialization、length anchor、confidence stop/prune | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17917 | streaming dLLM suffix masked token prune 与动态 confidence early exit | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17927 | 模型编辑 learned Riemannian geodesic、task pruning 的新更新路径 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17958 | input-dependent operator 表达 attention/norm/FFN/residual，不能误作固定全局线性模型 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.17982 | frozen embedding semantic diversity reward 与多目标 zscore RL | 贡献/范围关闭：embedding diversity与zscore多reward组合无新选择条件 |
| 2601.18053 | 无关概念控制可改变输出多样性，不简单等价温度；局部证据不外推 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18065 | 配对同 text backbone 的 vision pretraining/text-only 输入隔离 concreteness 效应 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18077 | 外部engine deductions与agent滚动deduction/perspective条件的差额，使scaffolded成绩不认证内生state tracking；不采用RL memory-transfer因果 | 准入5；标准OnlyReport，root必要命题校准通过 |
| 2601.18091 | reasoning/instruct 配对训练分布下 depth/width/dynamic pruning 差异 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18100 | depth+RGB 长 egovideo navigation，specialized/general 能力取舍 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18110 | attention heads+perturbation divergence 的会员推断与 extraction 接口 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18113 | disguised malicious URL 被 agent 接受，URLGuard 的安全处理边界 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18116 | forest hierarchical traversal+structure propagation 双路径、显式预算控制 | 贡献/范围关闭：hierarchy/双路structure检索/预算成熟组合 |
| 2601.18130 | embeddingrouter+posterior self/crossjudge平均为成熟MoA路由配方，无新有效条件 | 贡献关闭；必要§3.2～3.4已读 |
| 2601.18146 | pre-generation model-aware difficulty route Think/Non-Think，验证 Pareto 控制 | 贡献/范围关闭：ranking pregen Think gate/Pareto已知配方无新成立条件 |
| 2601.18150 | RL 每步 QKV scale 重标定+FP8 rollout 的 TIS/MIS 校正，训练/推理精度失配不能忽略 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18188 | chunk inverse dynamics supervision+entropy 执行 horizon，视觉变化绑定动作 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18203 | hierarchical/relational document map+reflective sufficiency retrieval，是否超出成熟结构 RAG 需辨别 | 贡献/范围关闭：层次multimodalRAG/reflection及预期模态消融无新边界 |
| 2601.18204 | temporal graph/experience/original passage memory 双通道证据检索 | 贡献/范围关闭：graph/experience/passage双通道成熟memory组合 |
| 2601.18217 | state richness 与 planning complexity 比域 realism 更相关，goal-irrelevant randomization 与 SFT generalization tax | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18220 | slot-filling timestamp 的 non-shift causal loss、non-AR inference，避免 NTP 累计漂移 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18225 | 增加 shopping simulator、描述 deep search/product-selection 失败及 SFT+RL gain，未建立新增机制/评价盲区/成熟选择失效条件 | 贡献/范围关闭：shopping新bench/训练提分无新条件 |
| 2601.18226 | binary tool feedback 的 in-situ synthesis/reuse 与 parallel batch evolution | 贡献/范围关闭：synth/reuse/batchmerge与newtool-use比例无新条件 |
| 2601.18253 | PI极端case生成rubric及median-density resampling条件，改变冷启动评价sensor训练选择 | 准入5；标准OnlyReport，独立通过 |
| 2601.18267 | section evidence admissibility/coverage reflection/packing只声明hard约束，无新runtime enforcement或semantic保证 | 贡献关闭；必要§2.4已读 |
| 2601.18281 | responseaudio+transcript/unspokenreflection交替，前置CoT/禁reflection及过密chunk反退，改变spoken反馈接口选择 | 准入5；标准OnlyReport，独立通过 |
| 2601.18282 | function/parameter 粒度 think augmentation 与 complexity-trigger reasoning；原创收益边界需辨别 | 贡献/范围关闭：thinkfield/complexitygate/prompt优化无新失效条件 |
| 2601.18292 | attacker/defender/evaluator 三方 RL 互相更新，区别固定第三方 evaluator | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18296 | hard-first reverse curriculum 避免 easy-question shortcut、内部 action 扩展 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18306 | GPTQ/AWQ 多语 calibration 与 activation range failure，English-only 非中性基准 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18323 | video 中 tool pointcloud trajectory → decoupled 6DoF/action heads 的 plan/action bridge | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18350 | medical LoRA PT/SFT 的线性 weighted adapter 合并，给单 merged model 指标/decoding 曲线，无原新增干扰条件证据；案例应用不足 | 贡献/范围关闭：领域adapter合并提分无新干扰条件 |
| 2601.18352 | 动态规则与预训练语义冲突时 inverse scaling，executable code 与反事实训练改变 prior inhibition | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18383 | reasoning trace decision-critical token 的 KV 保留，不等价任意 token 丢弃 | 日期支持；通过具体增量准入，必要证据/处置已root独立通过，见REVIEWS |
| 2601.18386 | LLM 编排既有视觉 adversarial primitives 与调参/混合；是否新增主线执行/安全论点需辨别 | 贡献/范围关闭：既有binary imageclassifier攻击调参，无新LLM系统论点，安全排除已root实际core独立通过 |

## Native 增量与其他处置

- Keel 2601.19895v1：Seed Publication 原日期 2026-01-27（日精度、时区未披露），arXiv Submitted=2026-01-27T18:58:46Z。Highway-style residual 支持重新考虑 Post-LN 极深网络梯度；日期无法核落窗，保留，不评分，不采用“1000层”宣传为事实。Seed 页仅精选 10 篇、论文目录仅近期18条，不证明历史完整。
- DeepSeek-OCR2 2601.20552v1：native Research Index 日期2026-01-28，arXiv Submitted=01-28T12:46:07Z（晚于截止），但 native first public 时刻未披露，不能据提交断言整个家族窗外。semantic visual-token reordering 的具体增量保留日期未知；不进入 Books。direct news 429，web primary index/read 可恢复身份；仅有当前精选10篇非历史全覆盖。
- MiniMax-M2-her：`native-m2her.json` 可读核心原文。situated reenactment 的 multi-turn self-play 错误检测、online preference filtering/causal denoising、diversity early stop 有潜在增量；日精度2026-01-27，JSON-LD midnight 看似合成日期，不能造实际公开时刻。日期终态保留，不采用作者排名/因果结论。
- Kimi K2.5：原 tech blog 经 web primary 可读，direct旧URL308/新URL403，当前 official model/help 页仅说 Jan27 release。PARL trainable orchestrator+frozen subagents、auxiliary reward annealing 和 CriticalSteps 对 serial collapse/spurious parallelism 有具体增量，但 native date 未建立完整落窗范围；日期终态保留。不得调用 2月技术报告证明1月当时已公开机制，不引用当前K2.6/K3文档的300-agent数。
- OpenAI Prism：原介绍可 web 读，scientific-writing workspace 是现成能力集成/产品发布，未披露新增模型或系统机制；贡献关闭，日期未核实后停止。
- Google ATLAS Jan27 blog：核心说明链接2510.22037，复述旧论文 scaling/语言配比结果，未新增实验/修订/机制；贡献关闭，不冒充“已处理重复项”。root 已校准。
- Google agent-scaling Jan28 blog：链接2512.08296。实际读 `abs-google-agent-v2.json`（Dec17v2 原完整 AB）定点核增量，180配置/架构-任务匹配/87%/错误放大已在旧版；blog没有新方法或新实验披露，R²数值略异未形成新增设计结论，不采用其性能/安全宣传。关闭本次事件增量，不称该家族已被他日报处理。

## 尚可执行

日期恢复按上述有限停点结束，106 个 arXiv 题摘均实际读完，不能伪写 evidence review 完成。剩余本日报告/独立审阅见 `STOP.md`；无 Books 改动。
