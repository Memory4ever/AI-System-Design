# 02/20 第十有限必要包：16473 / 16490 / 16498 / 16500

作者实际读必要精确v1的方法、关键评价与反侧，root必要原源/actual owner PRE及16490/16498实际正文/完整邻接/自身末注POST通过；16473仅报告、16500中心争议隔离限定通过，无Books写锁。位置由 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`（16500为CORE文件）取得。current官方事件页完整题摘/Comments/history已读；16473当前v2摘要的optimization措辞与v1的minimization不同，未见纠错说明，未比较全文历史；其余v1。16500 Comments只是TKDE投稿，不授发表/同行验收。

| ID | v1 Submitted UTC | Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16473 | 2026-02-18T14:04:02Z | 2026-02-19T02:47:02Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:47:03+08:00 |
| 16490 | 2026-02-18T14:25:16Z | 2026-02-19T02:47:26Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:47:27+08:00 |
| 16498 | 2026-02-18T14:41:09Z | 2026-02-19T02:47:37Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:47:38+08:00 |
| 16500 | 2026-02-18T14:43:20Z | 2026-02-19T02:47:40Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:47:41+08:00 |

## [Synthesis and Verification of Transformer Programs](https://arxiv.org/html/2602.16473v1)

2+1+2=5，必要理论深入。§0.3（453–575）C-RASP规则译为Lustre变量/累积counter，finite word添加结束符及eternity符号进入infinite stream，input-validity gate保护接受语义；Kind2检验语言包含/等价，失败trace去marker后成为counterexample。Proposition0.3.2证明是**这两个C-RASP程序**的包含；bounded-range计数若binary编码会指数膨胀，unary条件下才多项式。§0.4/0.5（576–620、662–695、742–765）固定Boolean/count规则数与常数界的有限shape中annealing搜索，样本错误+AST大小目标；minimization交替全语言等价核与反例添加，constraint learning只检包含。1000 balanced strings/length≤100、100000迭代、300s timeout，表1的样本100%不等语言等价或全搜索最小。§0.6（995–1007）C-RASP与length-generalizable Transformer关系仍conjecture、未从任意训练网络提取；1025–1033实际robustness定义仍future。timeout本身不能证明目标不可表达，只能复用所引用独立理论的对应结果。hardware/precision/随机重复在采用位置Not Disclosed，不采用普遍速度或保证。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:4051–4055已经承载形式化spec→checker反例修订→最终checker，specification validity与proof result分账、开放语义回退测试。这里的具体Lustre编码是受限symbolic representation的实现与局部应用，不是已经建立任意trained Transformer的语义提取或生产验证接口。拟**仅报告**受限程序工具；不因缺C-RASP名字强写书，亦不把现有通用spec链说成覆盖所有具体编码。

## [From Growing to Looping: A Unified View of Iterative Computation in LLMs](https://arxiv.org/html/2602.16490v1)

2+1+2=5，设计/直接反侧深入。§3.1/3.2（288–331）固定width/heads/tokenizer、深度成长只训练时复制中层，最终各层untied；loop则weight tied、unique parameter与effective depth分账。SmolLM360M/1.7B约200B/400B tokens、iso-param和iso-inference对照并非同时等所有费用；baseline超参未单独调为loop/grown。§4.1（338–355）depth score/Tuned Lens与local effect共同显示late/block-periodic signatures；local干预逐一改future-layer输入但不传播，不证明唯一内部算法。全loop换序更脆弱、保留独立encoder/decoder中层loop较稳。§4.2（357–360）grown未训loop仍可复用四层middle block，单/双额外重复有收益，更多常退化；不是looping更多普遍更好。§5.2/5.3（374、490–496）最后15%训练math20%/source选择+一次loop适配改变收益，选block位置/数据预算须一起保留。§5.1（368–371）三seed只SFT数据变动，不外推全部预训重复。采用位置硬件/精度未绑定完整性能配置，不用2x泛化。

actual `MODEL-TRANSFORMER-LAYER` Ch17:511–531已shared recurrence及费用/非单调、570–584已有局部middle层段的boundary-memory与budget，`TRAIN-PRETRAINING` Ch28:171–180已有固定深度→learned exit分支。真实差额是**训练成长的参数初始化/轨迹与部署显式共享是不同维度，保持untied最终模型也可能获得可复用middle computation；不可只把两者当互斥architecture**，而非重复局部循环原则。拟Ch28 Adaptive Depth的一段训练轨迹→有限部署重用交接，保非因果signature、数据/选择/串行费用与原固定架构；是否需要正文由root核现有更具体覆盖决定。

## [Fast and Scalable Analytical Diffusion](https://arxiv.org/html/2602.16498v1)

2+1+2=5，必要理论/反侧深入。§3.1–3.4（133–213）经验prior的posterior weighted mean需要逐步读取训练样本；early高噪声需要广aggregation但容许粗筛，late需要较精确neighbor recall但较小aggregation。downsample1/4 proxy**仍扫描全部N**，candidate m随噪声下降增、final k减、候选内精确距离；Eq2的posterior query缩放与Eq5文字查询未完整统一，不授算法exactness。§3.5/Theorem1（239–256）及必要A1（891–948）在**真实logit top-k**与有限radius R下，误差≤2R×discarded mass≤2R(N−k)exp(−gap)。该界不证明proxy recall、局部PCA任意算子或低噪声沿整个轨迹保持正gap；高噪声上界宽也不能由上界反推dense必要的下界。复杂度仍O(Nd+m p D)，m/k按N比例设置（394–395），不能照录与N解耦。

关键评价§4.1（371–397）MNIST/自然图/64²ImageNet，默认10 DDIM；U-Net/EDM只是作者的比较oracle、MSE/r²测相对该网络，不是未知真实score；128 samples平均不足复现实验不确定性。§4.3（605–643）同GoldDiff上WSS/SS只控归一化、coarse或final pool过小会退步；637/641写4/N和20/N与395的N/4、N/20相反，不采用这些冲突配方。hardware/precision/batch与整个生成walltime在必要位置Not Disclosed，71x逐step未授端到端或生产。§3.1（154）经验exact低噪声仍可memorize，training-free不授泛化。

actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:147–149已有posterior mean/score接口与有限posterior成本，243–250已有低噪声模态边界/局部误差放大，尚未承载**经验prior的support选择把coarse recall和aggregation count拆成反向噪声预算、真实top-k误差界并不担保proxy召回**。拟仅一段接posterior接口，保全数据低维scan、样本隐私/驻留/近似误差与原神经score；不采中心decoupling/exact-convergence普遍结论。

## [Optimizing Soft Prompt Tuning via Structural Evolution](https://arxiv.org/html/2602.16500v1)

2+1+2=5，具体正则准入，不授topology或语义保证。§III/IV（109–110、134–198）prompt向量作point cloud，记录persistent homology；训练实际用soft-min distance variance与距离区间attract/repel，threshold为距离的正负softmax加权期望、辅助CE。作者自推边界：Eq1写j含i且Dii=0，未披露自距离mask；softmax加权α→∞趋min/max，不一般quantile。必要AppB（905–908）把点最近邻死亡尺度等同H0 lifetimes，但多点H0 merge由连通分量/bridge决定，不能据nearest-neighbor方差认证整体persistent diagram。pair-distance hinge也无H1拓扑保持证明，§VI（602）semantic effects明确future；好看PCA/tSNE图不授解释/faithfulness。

关键control §V-B/C（344–350）同初始化/AdamW5e-5/b8/300epochs、10train/100test multi-sample，8×3090，precision/independent seed uncertainty未披露；比较L2和pairdistance不能单独支持topology语义。§V-D（514）“convergence”是实例100%任务accuracy所需iterations，非loss全局收敛/泛化walltime。T6（550–581）CE/H0/H1/full局部component对照只支持有限regularizer经验，TDA每20epochs与pairwise costs都不能忽略。作者自身比training accuracy和test能力的边界须分清。

actual `TRAIN-LORA` Ch30:191–201已optimizer geometry与任务quality分账、Frobenius decorrelation proxy≠实际输入正交、正则费用；422–436区分prompt输入与weight/state适配。该source具体auxiliary distance recipe有局部收益潜力，但中心“拓扑解释/保持”桥接尚不成立，不能将其改名为拓扑真保证并写Books。拟**暂缓中心结构/语义解释，有限正则方法/作者局部结果仅报告**；恢复点是自距离实现与真正拓扑functional/等价或独立受控证据，而非要求全部代码可选访问。无Books写入。
