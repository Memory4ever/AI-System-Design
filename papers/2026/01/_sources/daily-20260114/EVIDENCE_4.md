# Jan14 已准入余四项必要证据（待非作者裁决）

不新增发现。四项精确v1完整题摘已root准入校准，原6/6/6/7不随工作量或Books处置改变；必要原返回CORE_16_INDEX、CORE_17～24已保存，下面仅使用实际必要内容，未运行实现或复现。日期原字段仍DATE_FIELDS_1，公开区间需最后整体核，不把Submitted等于public。

## [Non-decoupling exact-v1](https://arxiv.org/html/2601.07389v1)

原2+2+2=6。actual§2～5：CORE_19 L157～189中Theorem3.1严格要求pSFT=data，C1≥0是Jensen/KL恒等式；不能从任意未最优checkpoint推出所有RL必损SFT。CORE_20 L213～243 Assumption3只给0<a≤E KL≤A，proof232～237却推出unregularized reward J有严格KL-growth λ>0，缺严格曲率与目标同一性。直接有限反例：单prompt/二答案，bounded reward r≡0，reference及regularized-RL最优pRL=(.5,.5)，pSFT=(.75,.25)，KL=.75log1.5+.25log.5≈.130812满足a=.1/A=.2，J恒0，不存在严格C2>0。即使r非constant且某action有tie，在tie内KL改变也不保证reward严格下降；不把reference-KL最优当纯reward严格最优。

§5 L245～258有限Qwen3-.6B/CoLA/2epoch/GRPO。RL严格format训练、robust最后label出现的评价另口径；loss与reward两目标可退是局部观察，不授通用训练互损/唯一因果。Hardware/seed与全部优化token/compute未披露，不照抄性能。拟原6中心暂缓，只隔离Theorem4.1/必然strict reward drop及依赖结论；保Theorem3.1条件恒等式和经验事实，不否所有实验。重开只需明确严格curvature/目标/支持假设或勘误，并绑定实现与相应配置；不进入Books，不做全数学附件审计。

## [MoE-DisCo exact-v1](https://arxiv.org/html/2601.06857v1)

原2+2+2=6。actual§3.1～3.2/Alg1 CORE_18/19 L94～138：每层只保单expert、移除gate，每个子模型完整shared backbone独立更新；mean embedding Kmeans数据分配，专家直接拼接、shared parameters均值（正文不均衡时weighted，而Alg1均匀），再完整MoE/globalFT。这不是保持同一参数点梯度语义的EP/普通DP，不能凭BCD/SimulParallel引用授nonconvex globalopt或unbiased gradient。

actual§4/AppendixC/D/E CORE_20/21：4×4090分支、1×A10080GB重接；BF16/batch16/seq1024，两阶段LR不同。Table1是fine-tune阶段steps对full训练，不是全预算equal；Table3租价乘device-hours，S-time取最长branch，原文“4×最长duration”与表中walltime展示不等，不采nearconstant expert cost或普遍倍率。各expert sharedbackbone驻留、聚类/合并/最后jointFT均付成本。Kmeans→random有限ablation说明data partition影响局部结果，不证明语义簇maxdistributiondivergence；LlamaWiki PPL163.27>160.91有反側。未验证10B+，未跑代码。

actualowner Ch36:51～86已有common-replica localSGD/parameter averaging及freshness，未承载expert-index×cluster阶段去gate/独立shared-backbone→重接的更新身份。拟该localSGD分支后≤1段：不同training-function须完整记录expert/data/shared版本，重接后jointFT权力与额外预算，不授训练轨迹等价或平均globalopt；fullEP/原同步路径回退。仅该长期分责gap深入受影响内容，原6不变，待非作者source→owner/锁。

## [Mosaic exact-v1](https://arxiv.org/html/2601.06562v1)

原2+2+3=7。actual§3～5 CORE_18～21：mask-only gatherGEMM减少未被sampler消费logits；explicit symbolic graph/addalias/addbarrier把chunk输入lifetime延至全loop，不以局部graphbreakallocator推全图reuse。按currentmaskratio变化只chunk logit/FFN当前峰，until可容纳或nonchunkable peak；这是heuristic可行search，不授全局optimal。全tensoroffset/firstfit+virtualreserve/physicalpagebinding与inplace consumer共合同，不把virtualaddress=physicalresident。多alias/lifetime若未准确建模不可授安全reuse，需保原allocator/dense路径。

§5.1 RTX3090-24GB/A10040GB、LLaDA8B/Dream7B/LLaDA-MoE。最大context明确dummy input超过model训练长度，因此是资源可容纳不是semantic有效长context；主要per-step latency/OOM指标不是全request/concurrency SLO。累计ablation添加globalmanager也同时替换inplaceoperator，非全factorial单因果；firstfit/ILP同Lmax有限比较不证明所有shape最优。precision/实际并发/完整output质量population未充分披露，不采headline无损/生产速度。

actualCh54:73～131已有resident/step-peak预算，却未承载maskratio下logits/FFN峰切换及registered-loop lifetime→lazychunk→physicalmapping的具体资格。拟Step-peak表及“只测idle”说明之后≤2段：参数化完整graph与barrier资格、当前active logits峰/FFN不同chunk、非chunkable stop、VMM逻辑/物理分账；计划与kernel/alias验证cost及dense/allocator回退。待非作者必要source→owner/锁。

## [Doob's matching exact-v1](https://arxiv.org/html/2601.06514v1)

原2+2+2=6。actual§3.1～3.4 CORE_22 Eq3.10/3.16～3.24：从base样本的noised endpoint和terminal weight做regression，guidance为gradlog h，不需w的gradient，但估计器训练及每step读gradient不免费，也非完全training-free。weight/objective已给定，reward质量不由h真值代替。htransform本身是既有，不给它新颖性分；增量是同时function/gradient拟合的带正则接口及边界。

actual§4.1～4.4 CORE_23/24：boundedcompact support、positive bounded weight；convex model class、h global lower/upper与derivative bound（4.3）是loggradient分母稳定的额外条件。lambda→0可提高value拟合但gradient界含1/lambda；derivative-class复杂度/regularizationbias与sigma^-8低噪声敏感性分账，n阶数有维数成本。早停/截断/scaling和base/guide/init/discretization误差均独立，不授默认NN或任意reward/sampler无损。本文无必要实测评价，不要求硬件benchmark，但不声称已部署/已验证训练优化。

exactHTML headerJan10/bodyAugust24构建日期字段不同保留，尚不把body日期等同真实正文改版，必要identity结论需独立核。拟Ch24现函数/导数/solver门槛段后1窄段：h-value/regressiongradient/logguidance三者区别，positive denominator与受约束class、gradientpenalty拟合成本/低噪声/早停条件，不能仅L2拟合授guidance；原base/conservativeguidance回退。旧Jacobian段有function/derivative一般分责，但无terminalweight/noisedregression和h>0分母对象，待非作者确认具体gap。只采用该接口，不采用完整W2定理/全附件证明；原6不变。
