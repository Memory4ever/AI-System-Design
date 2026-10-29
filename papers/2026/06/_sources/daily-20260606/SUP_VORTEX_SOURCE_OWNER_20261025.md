# Vortex 2606.06453v1 必要缺层/actual Ch47/最小PRE

作者supp_20260606_author，2026-10-25。[精确v1](https://arxiv.org/html/2606.06453v1)，A6/R4题摘/身份/Jun05组合资格直接复用；旧Jun05评分 `3+3+2=8` 保持不重分，不由分数推贡献已证。

## 有效旧层与必要缺层

定点读旧Jun05 V2archive仅本ID Source/Books：vFlow→paged算子→kernel/runtime机制摘要及Qwen/GLM/MiniMax/H200/B200条件有效，复用。旧Books existing摘录是generic internal/external fragmentation与vLLM版本边界，并不承载page-centric tensor、auxiliarycache和跨operator layout传播；Ch47旧trace也是一句，不授真实新增/POST或已有覆盖。不改旧日报归属/评分，补本次实际缺层。

实际读exactv1 §3–5/6.3–6.4/Limitations/§8–9/11.2–11.3/13拟采用必要域，未无差别读20×3所有agent算法或附件/代码。§3 vFlow分query-independent forward_cache与per-query forward_indexer；named cache须声明，accumulatedstat可跨decode step，cache-side只block内而indexer可跨page。§4/8/9 vTensor为underlying tensor加batchsize/indptr/pageindices metadata，operator逐sequence应用后传播shape/layout；不允许变换batch维，非leadingdim须共同。KV与namedcache由serving页机制管理，temporary默认为ragged。compiler/userlayoutpolicy可新分配或复用页，不等得到全部prefix/auxstat语义正确性证明。

§5按已知batch/seqshape安排template/greedyfusion，仍有planner/indexer/cache与layoutfee；后端从sparseblocktable进入GQA/MLA已有kernel，geometry/blocksize/precision支持矩阵有条件，cuda_mla补不同形状不认证任意模型。§5.2与11.2–11.3明确approx radix topK早停随机补thresholdbin是有损，不是普通layout变换；选择recall>0.97门限的原文同时说低阈值竞争者会胜、极高阈值某些cell无法资格/需exactfallback。仅为有损vsexact分账，不采用headline核速或把route-recall当任务质量。无须为该限定复现实验。

§6.3原文“mask任一个几乎无损”与Fig13caption Quest任一个即崩矛盾，不采特定channel不变量；某Qwen channel与MLArope的局部观察不可外推所有family或部署mask。§6.4/11：SGLang0.5.9，Qwen0.6–8B单H200SXM141GB，block16/32–256，AMC23/AIME24输入至4K/输出至16K；大模型MiniMax229B/4B200 TP4、fp8、至32Kgen，与GLM单B200切片不拼同配置。合成latency16Kprompt/512output、1–8req/s、P1D1，只P95TPOT，不是完整request p95或TTFT/SLO。吞吐“sameaccuracy”宣传与正文允许5pp/1pp质量预算需分开，未披露全部precision/重复/CI不补，8trial条件不可从NVSHMEM移到此。图的精确点未看像素，不采具体倍率或无损结论。§Limitations明确decode-forward only，无sparsePrefill/backward/RNNMamba，也非完整自主研究系统。本文作者runtime结果不等本次代码/实验复现，prefixcache兼容只支持已声明布局，不验证任意mutableaux跨请求共享。

## actual owner差额

已实际读Ch47完整Kernel语义段、下正确性测试/普通attention关系及COW/mapping相关段；Ch46/48开篇交接沿本日有效读取复用。另定点比较Ch49执行计划joint逻辑稀疏/融合与retile段：该章拥有compiler/kernel优化，不在Ch47重推fusion、TopK优化或agentbenchmark。唯一 `INFER-PAGED-ATTENTION` Ch47小gap仅为paged tensor算子如何带sequence/pagemetadata跨operator传播，并把auxiliary统计与prefix共享身份分开。旧genericfragmentation/trace不能NC，Ch49一般mask/plan也不拥有该分页对象合同。

拟在Ch47“随后从对应physical block读取K/V。间接寻址…numerical contract。”完整段之后、紧接“正确性测试应在相同模型…”完整段之前插以下两段；无root新窄授尚不保存。

分页对象还可以进入多个可组合算子，而不只由一个attention kernel读取。一个[受限分页tensor分支](https://arxiv.org/html/2606.06453v1#S4)让每个对象携带sequence边界与page-index映射，逐请求应用算子后，再传播输出shape和新分配或复用的页；长短不同的中间结果可保持ragged布局，不必先拼成矩形再拆回。这个接口仍要求请求之间独立、非序列维相容，算子不能通过变换batch维偷偷跨请求混合；真实token位置与causal可见性也不能由逻辑连续view重写。

Query-independent的块摘要与query-dependent的累计统计又有不同身份：共用KV的allocator或page机制，不使统计自动取得跨prefix/分支共享资格。Namedcache的声明、更新/重置时点与请求映射须另验；layout传播合法也不证明稀疏选择等同full attention，随机早停的近似TopK还需独立质量预算和exact回退。Metadata、auxiliary驻留、选择与转换都计费；布局、统计身份、支持的backend或质量不合时，回到原已验paged kernel、重建请求局部统计或full attention，而不因算子可组合批准无损与服务SLO。<!-- source-family:SF-2026-ARXIV-2606-06453 -->

本人注拟：`SF-2026-ARXIV-2606-06453` — supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 §3–5/6.3–6.4/Limitations/8–9/11.2–11.3/13必要，保原3+3+2=8/唯一Ch47。只paged对象sequence/page metadata跨算子与auxstat身份，compiler优化归Ch49不重复。保batch/shape支持、approxTopK有损/阈值反侧、质量预算、channel表文矛盾与全fee，不授prefixstat自动共享/无损或SLO。旧有效摘要复用/错genericNC不沿，旧归属不搬。未核图像素/代码/复现；首次必要/PRE/root新窄授/实际SAVE/唯一POST按后到事实记，不预I/DAY。
