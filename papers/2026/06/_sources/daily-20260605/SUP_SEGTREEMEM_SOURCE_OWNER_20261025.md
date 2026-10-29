# 04555 SegTreeMem：必要Source / actual owner / 最小两段PRE

作者supp_20260605_author，2026-10-25，同一Daily2026-06-05补Jun04。复用R33–36准入/精确v1联合日证，不第三AB/date。采用[Temporal Order Matters for Agentic Memory: Segment Trees for Memory Construction and Retrieval, exact-v1](https://arxiv.org/html/2606.04555v1)，官方HTML实存`SUP_2606.04555v1_20261025.html`704158bytes。实际读§4–6/Eq1–4/T2–4、A两个算法/invariants、C.3两结构反侧/C.4 Q3和Q5、E受控baseline变更/F控制树更新规则/H限制及checklist统计口径；支持与关键反侧足够停止，不扩全prompt、可选匿名仓库、全部D网格或附件，未核代码/复现。

## 评分与必要域

首次2+2+2=6，针对新定位construction/retrieval结构与复杂度边界深入算法/关键反侧。具体增量：按topic合并会混开不同时间的episode→连续区间树只沿rightmost frontier更新，检索另传播到细/粗时间层→选择时间局部性还是远距同主题聚合及其维护/读取成本，不能用“hierarchy”通称替代。

- §4.1每叶是单utterance；内部节点覆盖连续时间区间，按时间顺序的孩子区间不重叠/相邻，annotation是派生summary。原始叶身份与summarized interval不是同一信息对象，连续不证明summary完整或事实真值。
- §4.2/A Alg1 frontier为right endpoint=t的一条叶→root路径，只从非叶frontier选compatible attachment；补单例chain保持层级，更新所选节点/祖先interval与annotation。NONE创建新root、旧树作左child及新右chain；不把未来同topic回插旧subtree。保叶顺序/连续区间，但并无强制平衡/重建。正文O(log|M|)明确只在balanced tree假设下，不能泛化实际逐条更新。
- C.3.1每次NONE时height O(T)、total nodes O(T²)，每个internal还需annotation，结构代价严格高于flat；作者称构造worst case、benchmark未观察，不把它说成通常部署已退化。C.3.2远距topic重现被分在不同subtree，有限H不能保证连接；增H会经过无关跨度，semantic cross-links是扩展建议而非当前已实现。重建/压缩/duplicate cleanup也属future。
- §4.3/A Alg2每个node先按query/annotation独立打local score，再以稀疏column-normalized结构matrix传播H轮，有限α幂混合后在eligible G取topK；H0恢复collapsed。TD向children细粒度，BU向parent宽跨度，只是倾向不保证每项最后选择；不等于跳过全节点初始scoring或ANN仅查frontier。主文把r∈R直接除总和称概率，未在必要域完整规定负cosine/零和与无出边列处理，因此不采用完整概率保证或自行补一个实现recipe；只采排序/传播分工。
- §5.2三数据：LoCoMo10groups/1986queries，LongMemEval-MAB5groups/300queries，RealMem10personas/1415queries；text-embedding-3-small，主gpt-5.4-mini construction/answer，另qwen3.5-flash结果，gpt-4o-mini judge。统一K10是节点数而非token/字节或全生命周期预算；internal与leaf长度可不同。LLM-judge accuracy和tokenF1不是真实用户效果/权限/安全验收。
- §5.4/T3把30%随机turn pairs交换后重建，batchLLM/no propagation同设置与受控非时间树比较，支持此结构依赖原顺序；扰乱也改变输入语境，不能推所有顺序都必须保留或排除全部结构/summary差异。T3 LoCoMo原0.639→0.538与表列Δ-0.111算术不一致（实差-0.101），不采用该精确drop或修造原件，保两字段差额；其他各项与保序设计主张不依赖这一数字。
- §5.4/E/F受控比较固定memory unit/summary prompt/embedding/retrieval与K，F非时间树改为对所有最低层cluster算cosine，阈值0.45后插入/新cluster并重算祖先；其update candidate/threshold也不同，不把总差额唯一归contiguity。外部baseline替换相同backbone/可见memory interface/answerprompt/judge等，不能照原baseline论文数当直接复现。
- T4代表setting batchLLM α0.1/H2，TD与BU各有好处，非单policy每题普胜；主文“nearly20%”绑定特定benchmark/比较，不作为普适总提升采用。checklist说明95%CI按evaluation examples计算，不是重复construction/API run变异；少量conversation/persona聚集不能当独立系统重复。运行seed/精确API设置/硬件/并发/尾SLO/总全链费用在必要域未充分披露，Not Disclosed，不补生产能力。
- Fig5仅online trace称cosine frontier matching约少10×token/5×construction latency；它仍需summary/embedding，不能说cosine版本无LLM/零construction成本，图示不等完整query+build生命周期净费。反侧§5.4/C.4 Q3：选中对的时间region仍因parent摘要漏literal date而失败；Q5 propagation加相关family distractor使答案错，较强/较远并非单调更好。保无传播/leaf独立匹配与raw utterance回读，不让结构分数认证证据。

只采用作者受限离线conversation QA和结构机制，未核匿名artifact或复现。未披露概率接口与表格算术只隔离相应完整保证/精确数，不降分/删准入或补造正确实现；现采最小命题不依赖它们。原episode、source身份、annotation/树revision和完整写读费用共同保存属本次工程推断。

## actual owner与最小差额

已读ROADMAP、三Books公共上下文、仅2026路由；actual Ch77 construction/retrieval failure组1038–1083、分层粒度517–540与graph组件1221–1245，邻76/78开头交接。唯一owner `AGENT-MEMORY` Ch77。现已覆盖construction与retrieval分责、raw/summary/profile粒度、graph不是默认优；没有按连续时间span维护的rightmost-frontier/新root分支及有限传播时间粒度/最坏退化。故不重复泛“raw保真/分层更好/先做消融”，只拟在Graph/summary/raw适用范围完整段后、BabyAI有界needle完整段前两段。

完整直接上锚：

Graph 适合 dependency 明确、multi-hop state 高频的轨迹；summary、raw history 和 embedding 在短历史、审计或
关系弱时仍更简单。AMA-Bench 的离线 QA 与 ablation 支持 construction-vs-retrieval 归因，却没有覆盖 cross-task、
lifelong update、并发写入或真实 side effect，因此不能证明 causal graph 是所有 Agent 的默认 memory。

原两段PRE：

当查询依赖连续经历而不只是同一topic时，可让叶保存有序utterance，每个内部summary只覆盖连续、不重叠孩子组成的时间区间；新utterance只在最右frontier的非叶节点中选接入点，更新接入节点及其祖先的区间和摘要，找不到兼容点则建新root与右侧chain。这样保留时间局部性，却不会把远处重现的同主题自动合并，也不自动平衡：O(logN)只在平衡假设下成立，持续不兼容的构造反例可长成线性高度与二次数量节点，还要逐层付summary费。短历史、频繁跨topic或需要精确字面回忆时，flat/raw索引仍是应保留的简单路径。

[SegTreeMem的受限文本QA](https://arxiv.org/html/2606.04555v1)把构造与读取再分开：先给各node独立算query相关性，再有限步向children或parent传播，分别偏向更细或更宽的时间证据，H0保collapsed读取。方向/强度/距离要按任务验，不由树连通或更高传播分授证据真值；同K节点不等同token预算，交换turn后重建也只支持所测顺序依赖。摘要可遗漏确切日期，传播还可能引入相似词汇的干扰证据；构造、重摘要、embedding、全节点打分/传播与生成评价都计费。跨度或质量失配时减小传播、保独立leaf匹配并回读原utterance，不让较高平均QA或一次局部省费批准无限记忆增长。<!-- source-family:SF-2026-ARXIV-2606-04555 -->

完整直接下锚：

两层损失还可用同一consumer的有界needle实验分账：先直接提供raw needle，再用该needle经过constructor后的memory替代，最后运行完整检索路径；前两者的差揭示构造期间的信息丢失，后两者的差暴露读取链的额外限制。[BabyAI的受限对照](https://arxiv.org/html/2602.22769v1)显示有的方法先在construction明显退步，另一些还在retrieval阶段损失，故仅增top-k不能修复已经删除的state。Oracle needle只给离线诊断，线上仍须真正定位；阶段accuracy差不是可相加的因果贡献，默认embedding/index不完全匹配、同源Qwen judge和reader误差也限制归因。“causality graph”只是抽出的关系候选，不签真实因果或无损保存。三条测量链、graph/索引与程序搜索都付费；分母、支持或构造保真不清时回读原trajectory、普通summary/raw与直接claim gate，不把一次诊断自动提交memory修复。<!-- source-family:SF-2026-ARXIV-2602-22769 -->

## 当前单篇准备态

6分必要Source/actualowner/两段PRE ready，待本篇首次独核，无Books新授/SAVE/POST/I。04923 R53–54已行政采用，累计新增I12＋旧Kimi合计13I。其余九04315/04980/04708/04463/04306/04104/04896/04364/04485必要层、有限官方标题stop与最终DAY仍ordinary；本准备阶段交root即结束释放槽，不因等核扩下一篇Methods。无State/index/他日/stage/commit/push。

## 当前R55–56实际采用；唯一修句后真实SAVE待POST

上节为R55前准备历史。本轮已实际完整读回R55–56并采用首次必要Source/6分/actual Ch77与限定PRE。首段仅把原“新utterance只在最右frontier选接入点，更新其祖先”精确修成“新utterance只在最右frontier的非叶节点中选接入点，更新接入节点及其祖先的区间和摘要”，其余两段逐字不变，旧简写不再代实际接入/更新界面。

按root本轮新窄授真实SAVE于Ch77 Graph/AMA完整段后→BabyAI完整段前，加本人true-H2 Review notes下注。完整新增两段、完整直接两侧及本人注已实际自读；两段逐字连续匹配/本family正文marker恰一处，BabyAI原marker与其他正文/他注保持。整Ch77移除本两段及本人注后，与写前快照`/tmp/jun05-segtree.9fUfAA/ch77.md`字节相同，sha256 `a47125e7d272ceb281c63bd11eb0f8461c7fe8abca61aaf521e36c2dc5952b2a`，其他并发修改原样保护。

新增由Graph/summary选型细化连续时间分支/无平衡反侧，再回到构造与检索损失诊断，接口自然；保最坏二次node/远topic不合并、有限TD/BU/全node打分、K非token/摘要漏日期/传播distractor、全费/flat/raw/leaf回退，未采概率保证或T3错误差列。当前只真实SAVE/selfread待唯一非writer actualPOST，累计既成仍新增I12＋旧Kimi13I，不预I/DAY。其余九及有限标题stop仍ordinary，先交本就绪写后层释放作者槽，不因等核扩下一篇Methods；无State/index/他日/stage/commit/push。

## 当前R57–58已真实采用

上节为R57前SAVE历史。现已实际读回R57–58唯一actualPOST通过，04555整合生效、Ch77窄位释放；累计新增I13＋旧Kimi合计14I。只行政同步README/本Source/本人true-H2注，不第三技术/Source/PRE/POST。其余九必要层及有限官方标题stop/最终DAY仍ordinary，未授DAY。
