# 第二十二包：AB12 三项必要证据及一次 v1 准入纠偏（待非作者复核）

以下不增加 35safe；没有 PRE/Books lease，不写 Books。精确 v1 方法、对应对照及直接反侧已读，不遍历全部附录。23280与发现稿不一致，只重开同 ID 准入，不能由发现摘要授权采用新版机制。

## 23271 Evaluating Stochasticity in Deep Research Agents：拟 2+1+3=6，Ch66 一段

[v1](https://arxiv.org/html/2602.23271v1) blocks36–115已实际读。相同问题反复运行，分别对 answer、canonical findings、URL集合计算归一化 pairwise方差，另留输出数方差；它量测的是所抽取对象的变化，不是事实正确性。空向量规则、LLM finding聚类与URL normalization都会改变测量；同URL可以含不同内容，greedy evaluator不能取消 judge偏置或全部API非确定性。

query/compression/update 在早/中/晚指定step单独提高temperature，其他模块greedy，提供局部控制，而不是无干预地从trace认定随机性因果。total-variance law只是形式分解，作者77承认 exact intrinsic/propagated terms不可计算；干预改变后续trajectory，不能把模块平均差当精确方差占比。20 WebWalkerQA题、10runs、Qwen3-30B-A3B-Instruct-2507、lambda .5/1；You.com相同query结果一致及50小时短窗口不能证明外部环境完全固定，未缓存网页/索引版本，不采用“eliminating environmental stochasticity”。

直接反侧：更大TV不单调更高accuracy；Table4 structured-sum的citation TV .64高于baseline .62，不能宣称每一指标总下降。换Qwen3-235B-A22B Together API/DeepSearchQA20题、10runs、temperature1后，schema约束与query交集组合作局部mitigation；交集为空取first proposal，额外采样与search budget不是免费。质量.24→.36只是这20题平均，不授总体显著性或所有研究任务无损；硬件/precision/并发/wall完整费用 ND。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66 387–411完整重复预算邻接实际读，拥有 fixed environment identity、多次trajectory、assertions/selection与不确定性，不拥有 **findings/citations/answers三个对象的方差分计，以及早step×模块temperature干预不等exact分解**。拟一窄段，保数量/语义匹配、环境冻结限制、accuracy独立测量及真实versioned replay/随机审计回退；若现有重复分责充分可具体Existing。

日期原值：Submitted2026-02-26T17:46:42Z，same-ID registered2026-02-27T03:06:46Z；结合已核官方公告下界，arXiv事件区间02/27 09:00～11:06:47+08。当前页面无相关withdrawal/correction，不做默认revision差分。

## 23320 ParamMem：拟 2+2+2=6，Ch80 反思候选来源一段

[v1](https://arxiv.org/html/2602.23320v1) blocks15–49/50–67/76/89–104/110–112实际读。不同于从bank直接retrieve或当前失败作self-reflection，另训练LoRA反思generator，从问题x产生可能错误/子任务；运行时与episodic反馈拼接，plus再检索成功trace。参数学习形成另一种 **diagnostic proposal来源**，不直接访问当前环境，也不把生成多样性当已验证的真实失败原因。假设空间增大可能找到正确cue，也可能反复强化错误建议。

5iterations、首轮T.2后续1，Llama3.1-8B LoRAr128/alpha32/lr2e-5/3epochs；APPS4000+synthetic4200、MATH各subject800、两个QA训练集各10000由GPT4o-mini生成supervision。自生成版不使用更强teacher，但仍有现有数据、原模型与visible/synthetic tests/任务评价权限；不说整个流程无监督/无reward。500样本先从大池Kmeans选择，不是全部准备费用只有500。

现有base、Reflexion、DoT、DoT-bank与Retroformer提供局部对照，但温度/训练/额外token不匹配，diversity Pearson .76与embedding cluster不唯一识别收益因果。逐项直接慢侧：weak-to-strong Table3 ParamAgent LiveCode61.33低于DoTbank62，Hotpot79.67低于83.33，不采用正文“全部超过baseline”。Table8 Hotpot prompt3.65M/总费.67997高于DoTbank2.18M/.42740，prices只是作者以2025-08-20单价估算，非当前计费事实或训练总费；硬件/precision/墙钟 ND。最终hidden tests与过程中visible tests分开，最后成功也未认证开放需求全正确。

actual `AGENT-REFLECTION` Ch80 270–338完整相关邻接已读，拥有belief采样、retry/review归因、反馈writegate与typed停止；未显式拆 **持久权重中的跨样本反思generator，与可追溯episodic feedback/外部bank三种候选来源**。拟反思来源/Memory交接一段，保trained proposal身份、current feedback独立验证、token/训练费用与错误模式固化回退；不另造Memory事实权或promotion协议。

日期：Submitted2026-02-26T18:28:04Z，registered2026-02-27T03:07:58Z，arXiv事件区间02/27 09:00～11:07:59+08。v2 Submitted02/27 08:21:31Z在窗内，current Comments没有具体重要改动说明，版本号本身不触发全文diff；本包采用exact-v1，不由v2编号造重要修订或替代证据。

## 23280 Physics Informed Viscous Value Representations：实际 v1 一次局部准入，拟 2+1+2=5

2026-10-06 后续必要原证/actual owner终态：fresh非原packet作者实际必要blocks35–50/100–108，原v1题名纠正已复用，Eq7 one-sided/target MC与representation/hierarchy反侧；Gaussian非有界/全PDE最优不采用，15/50episode冲突、4seed费用。采用2+1+2=5，具体差额深入后窄融AGENT-PLANNING/Ch79正文278/280，完整270–286，末注566；final_audit必要原源/actual owner非写入者独核通过，root实际正文/完整邻接/自身末注POST通过，已同步并释放窄锁。精确v1身份/家族日期沿用本日原字段和政策下界、同ID注册秒上界，只支持09:00～11:07:01+08半开范围，不授注册首公开；未核实现/复现或全证明，非日级。

[原v1](https://arxiv.org/html/2602.23280v1) full title/abstract、blocks17–20/26–58/100–108实际读。发现题名是Mollified Value Learning，发现主张pointwisePDE→localmeasure；原稿不是该表述，不能沿用准入理由。实际增量：对offline goal-conditioned value，引入粘性HJB的Cole–Hopf表示，再以随机邻域的target-network value和one-sided penalty替代显式高阶梯度求值；**表示几何/regularizer与hierarchy有具体交互和负结果**，需要重新考虑在哪个表示空间、是否仍须hierarchical policy使用几何prior，而非只是机器人专域指标提升。

原问题假定连续state/quadratic control cost、isotropic dynamics，unknown dynamics并不推出真实isotropy。Cole–Hopf和Feynman–Kac是成熟数学，贡献采纳只限该value-learning接口和实验条件，不授它们本身新颖、真实动力学已识别或通用PDE最优性。finite-horizon到stationary equation、采样/实际边界条件尚未整体证明，本次不采用形式最优性链。39“永不生成kinematically invalid”子命题直接隔离：所写 s'=s+min(nu,d_boundary)*epsilon，epsilon非单位Gaussian，1D距边界1、nu=1、epsilon=2会越界；未核实现实际是否另做normalize/clip，不授实现有bug，更不因此抹去独立实验贡献。

Table1 Orig平均34→30，而VIB35→45、Dual41→48，说明不“representation-agnostic universal改善”；Table2 point-stitch-large Dual+EIK55 vsDualFK30，humanoid-giant HIQL-FK4 vsEikHIQL68，保hierarchy/geometry各自边界。noise-task控制与K1/5/10/20、nu1e-4～1e-1支持局部稳定条件，不证所有sample budget鲁棒。Powderworld latent10 vs7仅表面收益，非Euclidean latent不能继承物理prior。

4seeds、13state任务/32variants；gradient1M state/.5M pixel、Adam3e-4、batch1024/256、MLP512³、target.005、gamma.99/.995、K10/nu.01。102说15episodes而106说50episodes/五goals/最后三epochs，人口口径冲突不合并CI或计算总体效应；硬件/precision/wall ND。训练regularizer与MC、BFS64anchors/representation有额外费用。

actual `AGENT-PLANNING` Ch79 261–276完整value/geometry邻接已读，拥有success-leaf几何代理与value分责，没有 **value-learning的粘性随机邻域one-sided regularizer、表示空间失配与hierarchy慢侧**。拟value/search替代接口附近一段或具体Existing，等待root先校准改变后的exact-v1增量，再核必要owner；不直接发写锁请求，也不把发现稿贡献与原稿混合。

Submitted2026-02-26T17:53:46Z、registered2026-02-27T03:07:00Z，same-ID原登记题名是后来稿，但ID及时间界复用并以原abs确认v1。arXiv事件09:00～11:07:01+08；后续v2在May窗外，没有具体安全说明，不自动版本比较。

## 23242 / 23306 精确停点

23242 [AIQI v1](https://arxiv.org/html/2602.23242v1) 已读phase-separated Monte-Carlo return predictor、Alg1、grain-of-truth、Th4.6及off-policy非self-optimizing定理所写条件。有限A/O/R、bounded reward、discount、tau/M/N/H与reflective-oracle class不能略；理论正面证明中的部分aligned数学未被当前HTML转换保留，不把可见theorem声明算所有证明已核，也不称不可计算是无长期价值。下一只核所采用方法/理想理论边界的actual owner与必要缺段，不遍历全proof；普通未完成，不增加safe。

23306 ThinkOmni 同题OpenReview forum pMpCOjzwI1、ICLR2026PDF身份信号已实际核；api2必要notes403，2026-10-06打开官方forum也只返回browser-verification challenge。缺首次公开pdate/可支持本窗新事件的官方说明；arXiv Submitted18:10:41Z、registered03:07:37Z不替代家族public，未授当窗候选/Books，精确恢复该forum公开记录即可重开，不无限追查全部稿件。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：23271：原必要blocks45–60/74–80/94–102及采用相关prepared控制/反侧与actual owner独核；Ch66正文431/完整414–442/own5683 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
