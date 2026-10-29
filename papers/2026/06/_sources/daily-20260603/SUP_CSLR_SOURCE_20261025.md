# 00426 CSLR：必要证据 / 六分 / Ch36 两段最小提案

只补Jun03报告的Jun02 BJT。当前合同、本日适用来源/统一入口、ROADMAP/Books公共上下文及停点已重读；R26/28完整题摘、准入与联合日证有效复用，不第三验证。精确v1提交May29 23:22:23Z，精确DOI `10.48550/arxiv.2606.00426` arxiv.content/findable/registered Jun02 03:51:15Z，按适用公告规则的最早界至登记上界全在Jun02 BJT；不把单字段当实际公开时刻。[当前官方abs](https://arxiv.org/abs/2606.00426)唯一v1，所见无撤回/勘误提示，无全版本史或假想发布渠道排查。

## 实读与必要边界

[exact-v1 HTML](https://arxiv.org/html/2606.00426v1)实际读§3–7/Alg1/T1–3、理论命题与条件、E/T4–5、F/G必要设置；未核全部证明/Additional表、图像素、匿名artifact或代码复现。首次输出被截断的§4.3–4.5已定点完整补读，未把未见部分当已审。支持本次身份对齐和隐私scope边界已足，停止。

冻结公开encoder，client产生DP候选回放分布的无序list，而非上传原文本或共同有序梯度。公开anchor句子经相同encoder后，对每候选求log-density签名，server按签名clustering/assignment赋canonical ID，再按mode聚合clipped means/second moments/weights/targets、secure aggregation与Gaussian noise，做PSD/simplex投影产生embedding replay。公共anchor用于识别可比较对象，不是补充private replay样本；表示或anchor改变会改变匹配身份。

Theorem2依任意需区分的pair有(p,gamma)anchor可见性，有限union bound只保证noiseless signature有某coordinate margin；并非任意分布/噪声下clustering语义正确。对本来应同一mode的不同client估计也不能仅凭pair separation自动归组。Prop3只针对无共享参数/公参评估/seed的unordered-label oracle；真实共享坐标下nearest-mean/Hungarian/OT合法，不能写“没有anchor就不可能聚合”。Theorem5还假设bounded loss、replay TV接近理想分布、风险-回放损失桥及优化条件，是条件稳定界，不是任意FCL收敛证明。

签名只读已DP释放的候选时才是post-processing；若从非私有统计直接计算须另计费。Theorem4的条件RDP组合及表中epsilon只覆盖list/replay统计释放，不覆盖传出的task-head更新；End-to-end还需匹配私有optimizer及预算组合。算法公开描述/投影合法不认证实现conformance、secureagg信任和client全生命周期敏感度。本次不签完整端到端DP或所有clipping/accountant实现正确性。

评价是frozen MiniLM384维+两层head（NER用frozen BERT token表征）、四分类/NER/intent任务、20/50/30/40client、task-incremental已知task身份，不是full LLM参数微调/生成式能力或真实网络。五seed共享partition/anchors/sampling，30%参与、50轮/task、500replay/轮、L4/K任务数/anchor100、Adam3e-4；各数据异构和F1/accuracy不能混单指标。epsilon4/delta1e-5下T2相对最强non-CSLR DP基线+3.9–5.6是replay-release预算域；DP-SGD只私有optimizer与之不等预算，FedTA非私有reference。共享坐标OT与Hungarian实测仍可行，anchor也只有受测相同摘要空间的局部优势。G采用summary-level区间而非paired原始run分析，不能自己补统计显著/普遍支配。

F实际重复clipped EM/noisy summary、低weight保留不变list size、固定公开dictionary；原表未完整给每项噪声分配/总sigma到每轮完整accountant配置，未核artifact或重算真实DP，硬件/precision、完整端到端时间、bytes及在线长度/concurrency/SLO未披露/本实验不适用，不能拿utility授加速/全隐私。候选拟合、anchor log-density/匹配、全部统计交换与会计、replay/head训练都付费；冻结表示/Gaussian族局限、encoder漂移需要reanchor，表示信息不足不能靠排列对齐恢复。

## 评分、actual owner 和 PRE

正式Design Delta2 + System Reach2 + Durability2 = 6：改变无序局部候选能直接按位置聚合的选择，将身份可识别性放到merge之前，跨客户端表示/聚合接口与回放生产；不是privacy/一般联邦主题或成熟匹配名字加分。只采用条件身份接口，不采更广不可能性/端到端隐私保证。已有具体小gap，深入受影响命题，不全附件。

唯一 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)。实际读“Federated Tensor Type”完整encode→merge→decode两段与marker、之后GradsSharding完整工作集/成本两段、再后实际update权重/参与身份组；另读跨family public-prompt behavior consensus完整组。现文定义通信可表达性、共同坐标、成员及weight语义，但没解释无序density replay对象需怎样建立可聚合mode身份，不能主题NC，也不以无marker硬I。Ch35/37开篇交接已读；Ch72 privacy conformance与accountant完整组已读，只引用其责任，不新增第二DP owner。

拟在 `<!-- source-family:SF-2026-ARXIV-2605-21103 -->` 后、GradsSharding“聚合工作集超过单个function内存时”完整段前，原两段如下；从类型能表达什么→对象如何识别→同一聚合如何分块，保旧内容。未授写/SAVE/POST/I/DAY，待首次非writer核。

### 原两段 PRE

协议能编码一类对象，还不等于各client给出的第一个对象属于同一全局成分。冻结共同encoder后，客户端可能只释放一小组无序的回放分布；直接按list位置平均，会把不同语义模式混合。一个[受限canonicalization分支](https://arxiv.org/html/2606.00426v1)用同一组公开anchor在每个已释放分布上求log-density签名，先匹配并赋共同mode身份，再按mode聚合有界统计和回放目标。Anchor在这里提供可识别性，不是额外私有训练数据；encoder、anchor、匹配规则、mode与round必须绑定，不能让局部编号自行取得全局merge含义。

这种可识别性有条件：公开anchor须能区分需要分开的候选，估计与噪声也会使匹配错误；没有anchor的不可识别结果只覆盖缺少共享参数/参考的抽象oracle，不排除共同坐标下的Hungarian或OT。现有实验只适配冻结表示上的小型任务head，更新encoder后需重新对齐，不能外推full LLM持续训练。签名仅由已私有释放的对象计算时才属于post-processing，回放释放的隐私预算也不覆盖另行上传的head更新，完整会计仍由[Ch72](../part-06-ai-infrastructure/72-security.md)负责。拟合、anchor评估/匹配、全部统计交换和回放训练均付费；身份不可辨、表示漂移或质量不合时，保留声明清楚的共同模式/可比较参数匹配与已验回放基线，不把局部utility提高签成端到端隐私或收敛保证。<!-- source-family:SF-2026-ARXIV-2606-00426 -->

## 后续已成事实

R155首次必要/正式6/actual Ch36原两段PRE通过后，root按指定完整双锚真实保存原两段及章末单注；R156唯一实际写后复核通过，整合生效。前文提案时态仅准备历史，无POST待办，不预DAY。
