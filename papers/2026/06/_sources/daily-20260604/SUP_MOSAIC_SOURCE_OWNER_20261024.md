# MOSAIC 03014 — necessary Source / actual owner / PRE

作者 supp_20260604_author；R2准入/Jun03日期有效复用。正式2+2+2=6，finite offline model-call调度/实际qualitycost边界gap深入。作者必要读exact-v1完整TEXT §2–5/7、A2/A4/A5/A6；支持与关键反侧足够停止。未核代码、figure像素或复现，不采用医学/科学应用能力。

## 必要 Source

已知fixedpromptset/upstreamskillrecruit之后才调度，6独立model experts>4workers，每model与完整32K KV可装单A10080，TP1 experts，同worker顺序vLLM0.7.1sessions。offline traincalibration mean/maxoutlen、多N sweep回归，tau=T(N)/N solve-time常数；ILP binaryplacementY/integerpromptcountsX、守恒、X<=NY、replicacap与每worker不同model数cap K，minmax(load+tau*count)。只对线性proxy最优，不是真实batching全局最优，分片后tau随N非线性/长尾profile漂移不能自动消除。引用provablyoptimal milliseconds仅M≤6,N4，不推大集群求解。

AppA6/RRvsDP显示DP可降idle却增加多次load/小shard吞吐退，allnonR反慢631→892s；每worker一个驻留模型，不是同时共驻K个。K2是约束模型种类，不是软显存预算。§5.3称K3会overreplicate却又称Rcap禁止轻model复制，其解释不足以证明K2普遍最优；Eq8 rho .2–.95也不自动全得floor(T/load)=1，不采用“所有轻模型依公式必pin1”或K2理论最优。校准、load38–47s、求解/重排/重载/所有expert生成费均保。

§4.2/A5将normalize/extractexpertanswers后的plurality作为C，k3的tau1只3:0、tau2/3再含2:1，其他走aggregator；agreement是经验proxy非校准置信度或独立errors定理，全部experts已运行不省前段。T1实际保守MMLU +.24pp、Med -.04、GPQA +1，激进MMLU -.62/Med+.32/GPQA+.49；正文“±.1”不全齐，不能采用headline无损/严格等精度总speedup。extract/normalization细节未验，不补执行recipe。

4×A10080GB/单host/vLLM.7.1，expertTP1/32K KV、aggregator示例TP4；fullprecision/各run完整batchconcurrency矩阵未披露。RR按queryfirstseensolverorder一次load、不profiling，不是最佳online或MuxServe强基线。traincalib350MMLU/504Med，fixedtestbatch；5.3专家三seed，AppA4仅MOSAICwall±6%不是质量CI。1.69/1.53/2.54 expertstage、1.71/2.04/2.34 summedexpert+aggwall是作者该offlinepipeline，不含upstreamrecruit/离线profile/端到端在线到达。Aggskip84.62%仅1.74x因1:1:1残留更长（2696vs1064tok），不能按skip率算wall。Limiter预先固定阈值不在线学、一般Agent非LLMbottleneck未验证。

## actual owner / PRE

三Bookscontext/ROADMAP已读；actual Ch56开头、553–613 placement/confidence邻接、1537–1563 Agentserving/Scepsy/Ready完整相关论证、Ch55开头和Ch82 equalbudget/聚合分责已读。唯一INFER-SCHEDULING Ch56：新增有限已路由callbatch的整数分片/复制经济与residualaggregation尾成本，而非重写Ch82真值聚合、参数MoE内expert或Ch55KV分离。当前Scepsy用dynamic统计pipeline/TPfraction，不承载fixedallcalls + sequentialmodelloads分支。仅在Scepsy 15186完整第二段inline后/Ready真H3前两段+本人trueH2注，不加新章节。

完整上锚：

这种压缩换来更小的配置搜索，却丢失跨不同模型的并行 critical path；同一模型的双峰调用人口和不可忽略的 tool time 也会使代理失准，分位延迟直接相加更不是整体 tail 保证。[Scepsy v1](https://arxiv.org/html/2604.15186v1)的16张RTX A6000、100Gb InfiniBand及两类工作流只支持受测范围，baseline的prefix cache/engine版本差异、低负载Ayo略优与128GPU搜索约70秒均限制 headline 的解释。Tracing、逐TP profiling、搜索、放置与MPS共驻干扰需要另计，实际completion/queue/KV仍由runtime拥有；统计失配时保留逐阶段trace、显式tool预算和已测保守allocation，而不向任意Agent程序承诺吞吐或SLO。<!-- source-family:SF-2026-ARXIV-2604-15186 -->

拟增两段：

如果整批问题及其候选模型调用已经确定，控制面还能使用更窄的离线分支：把每种模型的载入成本、生成成本估计、worker 放置与整数 prompt 分片共同优化，只有预计生成工作足以摊销额外载入时才增加副本。一项[受限多模型批处理](https://arxiv.org/html/2606.03014v1)让每张 GPU 一次驻留一个模型、顺序执行多个 session；它不是模型内部 MoE 的 expert routing，也不改变上游选择哪些模型。全部复制虽然减少 straggler idle，却可能使短输出模型承受重复载入与过小 batch 的吞吐损失，因此 prompt 数均衡或把所有模型平均分四份都不是充分条件。<!-- source-family:SF-2026-ARXIV-2606-03014 -->

前段排程与后段减少聚合调用还须分别结账：一致答案可以作为经验旁路信号，但不是已校准正确率；保留的争议样本通常更长，跳过大部分调用也不同比例缩短聚合墙钟。该离线四卡对照的激进旁路在部分题集损失准确率，不能用近似相同平均分签发无损服务，更不能把线性成本代理的最优排程当真实 batching 或在线 tail 的最优。上游选择、校准 profiling、求解、重载、全部专家生成、答案提取/聚合和回归均计费；路由人口、长度、硬件或质量条件漂移时，重测 profile/阈值，保留完整聚合与简单已验 placement，不让共识或较低 makespan 取得答案真值和 SLO 权威。<!-- source-family:SF-2026-ARXIV-2606-03014 -->

完整下锚：

### Ready 只表示可释放，不能自动把工作提交给 Engine

前文的 control-plane capacity 先回答“能否可靠发现并送达这么多执行单元”；进入 Agent DAG 后，下一问才是“哪些已就绪工作
现在应该送达”。把两者混在一个扩容数字里，会让 healthy data plane 掩盖 release queue 已经失控。

本人trueH2Review note拟：`SF-2026-ARXIV-2606-03014`：2+2+2=6；exact-v1 §2–5/7/A2/A4/A5/A6，finite offline modelcall placement/count/replica与residualaggregation分账；保分片非线性、4A100/vLLM.7.1/单驻留与RR条件、MMLU激进-.62pp/表文±.1不齐、K2解释不授最优和全部profiling/load/recruit费用。未核figure像素/实现或复现。待实际写后复核。
