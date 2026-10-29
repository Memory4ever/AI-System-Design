# AsymCache 02964 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author；R45完整exact-v1题摘/准入/Jun03联合日证/notice复用，不第三。作者正式拟2+2+2=6：多段驻留、kernel与低维护费replacement跨执行/状态管理接口，改变只按hit或位置单启发式选块的机制；非按倍率/工作量加分。因actual长期gap深入受影响内容，仍待首次独核评分。

[exact-v1 HTML](https://arxiv.org/html/2606.02964v1) HTMLfirst；剥标保mathannotation TEXT93756字元（含末尾换行）已实际保存[原件](2606.02964v1.fulltext.txt)，fetch exit0，无工具truncation。必要实际读§2.2–6.5、Alg1/Eq2–9及A.1所列保序假设/证明；不核代码、kernel、图像像素或复现，不扩其它系统完整论文。支持与直接反侧足即停，下面哪些命题未采用明确隔离。

## 必要机制与关键反侧

§2.2 key不是单块文本，而是从开头到当前位置完整token序列；复用前后非连续resident块不授权将独立context的suffix当exact。模型/adapter/position/execution与shared授权身份按现有Ch45有效合同继续，不能由MSA减弱。§3的前/后端命中峰只是作者workload观察，异常模式可多峰，不采为普遍分布。

§4.1 MSA把每个request/segment的Attention分配CTA组、单GPUkernel调度，避免各段独立调用的launch/hostsync；MLP/LayerNorm逐token的hidden打包，Attention仍需split/dependency元数据。不能把非连续物理KV、recompute-query打包、logicalposition与可见性混为删历史或独立Prefill。印刷Eq2 O1=Attn(Q1,K1,V)的V切片/维度与mask/position不足以单独构成完整实现配方，不照式授可运行实现、数学逐bit等价或通用任意段无损。需实际验依赖/输出，作者称lossless只取物理驻留而非有损删context的设计意图。

§4.2 E(B,t)=fB(t)×ΔTB，选择较小free块；Alg1 Add仅在refcount0，hit/evict要Remove，不能回收仍被请求使用的块。f proportional future reuse是模型假设，不是概率校准/最优replacement证书。常数cost仅去掉cost项，是否LRU取决frequency定义，不采用“任意频率均退LRU”。后位block重算贵可与跨用户prefix高频竞争，不推出永远优先suffix。

§4.3 Eq4–7从two-segment prefill拟合，以近似替换querylength×context项，ΔTB只依不可变位置，便于固定key/O1提取。约1.1K profiling/R²>.999是fitting条件，不是跨GPU/shape/SLO的误差界、完整质量或在线必加速。原Eq5更依当前segment，近似用便宜key换模型精确性，不能混成exact recoverycost。

§4.4 Eq8只有在任意加权平移同序（含tie）、连续非负非恒定等条件下A.1推指数；A.1条目编号Lemma0/引用Lemma1不齐且正文“单调非负”省略假设，不将唯一性扩到任意策略。这里只需充分性：一个固定rate分支所有块随时间乘共同正因子，固定cost/同分支权重保序；分段min整体不保序，于是维护两棵树，evict比较两边root，选中块从两边移除。整段基于两树能得到min/min换序，不是单树永久不变。insert/delete/evict Ologn不是所有scheduler/lookup/metadata Ologn或零费用。新access需更新，life/profile参数改变不能假装旧key一直有效。

§5.1文字称全局λ×f会改turnpoint，但全局同乘不改argmin；Alg1实际比较root1与λ×root2，仅第二分支缩放才会改相对顺序。该不齐必须保留；另Alg1将w记在Add调用时，却未完整写出跨插入时刻的同一时间基准/两分支不同衰减率的root当前值校正。保序充分性不能单独认证伪码每步实现了同一t的Eq9。本文仅采用应维护的双树分责和条件代数，不采完整自适应λ公式/零开销/可运行recipe，必须验时间基准与动态更新。P99life/slope40是作者经验，不是未来reuse或参数鲁棒性证明。Adaptivechunk依#decoder门限减prefillchunk、有最小下界，费用/公平性和极端排队仍验；toolcall提高reuse分数不证明tool必返回。

§5.3作者vLLM扩展约6K Python+2K C++/CUDA，MSA基于CUDA/CUTLASS/Flash/Paged；evictC++，multi-segment lookup及metadata仍Python，没有核artifact或继承upstream生产能力。

§6.1 AMD EPYC9K84/96core，4×NVIDIAH20/96GB/NVLink，CUDA12.8；8B单GPU/487744tokenKV，70B四GPU TP/505152token。precision/quantization、blocksize、exactvLLMrevision、完整batch/concurrency/seed/CI/SLO Not Disclosed。LongBench/LooGLE各300request，平均input/output34.8K/2.6K、24.4K/.7K；预生成并逐step强制覆写outputtoken，固定length。Gamma到达CV.25、inter/intra比5:1或10:1是合成负载，不验证自然自由生成质量/相同token或真实userthinking。主要metric为meanTTFT/TPOT/requesthit/blockhit，不可当tailSLO。

所有baseline加PODattention后端；vLLM-LRU开prefix，Maxscore用同Eq9但O(n)，Pensieve未开源由作者reimplement并加MSA，不是原baseline独立复现。§6.2 headline只限这些条件。§6.3 T2的O(n)/logn对照hit略不同（例如low29.1/28.0，high12.50/12.32），不能纯粹把全部延迟差归复杂度。kernelmicrobench为8B、各128newtoken、suffix1K/10K形状；MSA改善短段launch开销，非全workload净收益证书。§6.4低reuseprob权重配置会伤高复用场景，小slope同样退，不能因“not sensitive”省去调参验证。

§6.5 BFCLv4WebSearch是GPT5.1预生成output在Llama8/70B回放；Asym单独对LRU平均job仅.4–4.2%，与Continuum叠加相对Continuum平均4.4–18.1%、P906.8–16.6是不同分母，不合并。近似相同hit仍有latency差支持cost-aware选择，但调度/复杂度/频率等混杂未全单独控制，不授功能quality/safety/普遍倍率。全部token、cachelookup/metadata、profile、两树/统计与动态chunk、kernel、请求等待、offload/restore和失败回退要同账；没有复现实机。

## actualowner与最小差额

唯一INFER-KV-CACHE Ch45。三Bookscontext/ROADMAP已重读；actual读本章开篇、136–175 prefix identity、294–332命中率口径、355–412 Eviction/Offload及453–498相关有损策略、相关family/title检索；Ch44/46开篇交接已读，owner不转移成batch调度或Ch49泛kernel收纳。现有hit不是加速、transfer/recompute比、hiddencheckpoint恢复、有损attention选择/semanticcache评分均有效但未承载**同一完整prefix身份下可保前后不连续exactKV、MSA降低分段launch、reuse×位置重算代价及可低维护费排序共同决定resident集合**。具体gap，不因主题近似NC，不复制已有identity或泛“测全费”当全部增量。

仅拟下列Eviction与Offload首两短段后/SparPR完整段前新增两段，加trueH2本人一注；本轮没有新授，未写Books/不预I。

完整上侧（含H3和两完整短段）：

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

拟增两段：

不把历史从模型语义中删除，也可以只让部分精确 KV 常驻：保留可跨请求复用的前部与重算较贵的后部，缺失位置到下次使用时再补算。缓存 key 仍绑定该位置之前的完整 token 历史、模型和位置身份，不能把另一上下文中独立算出的 suffix 当成合法命中。重算的多个 query 段若各自调用 Attention，会增加 launch 与同步；可在同一次 kernel 中按 request/segment 分配 CTA，沿各自原逻辑位置和 causal 可见范围读取兼容 KV，非 Attention 的逐 token 运算再按打包序列执行。这条[多段驻留分支](https://arxiv.org/html/2606.02964v1#S4)改变的是驻留与执行布局，不授权任意跳过依赖、压紧位置或逐 bit 等价。

淘汰目标也应从“少丢命中”变成“少增加未来重算时间”：只在引用计数已归零的块中，以衰减复用分数乘预计重算代价选较低者；位置较晚可能更贵，但历史热度与 profile 都只是预测。为了不每次扫描全池，可将位置相关代价近似为固定 key、把两段指数衰减分别维护在两棵平衡树中：固定代价与同一时间基准下，每一分支共同缩放而保序，比较时仍须将两个最小值校正到当前时间；新 access、分支切换或参数变化不能由一棵永久静态排序代替。这是维护合同，不是原伪码已经完整给出时间校正与自适应实现的认证，对数树操作也不等全部 lookup 免费。kernel、分段 metadata、代价 profile、树维护与 chunk 调度须同 TTFT/TPOT 结算，而不是只比 hit rate。作者在 H20、Llama 3.1 8B/70B、合成到达与固定输出 token 回放上的有限对照支持这条取舍，不验证自由生成质量或生产 SLO；实际依赖/mask、代价预测或完整费用不合格时，保留连续 prefix/LRU、完整重算与合适的 offload，不由同等命中率批准无损或净加速。<!-- source-family:SF-2026-ARXIV-2606-02964 -->

完整下侧：

比较成本时还要说明重建的起点。若另有对应层的 hidden-state checkpoint，可只做 K/V projection，按当前 query 的 block 摘要选择历史、合并相邻 span，再比较稀疏投影加碎片开销与整段搬回成本，昂贵时退回 full recovery；这不是从原 token 重跑完整 prefix。Hidden checkpoint、摘要和位置处理仍须存储与维护，恢复选中块的 K/V 也不等于保留完整 attention 的生成语义。[SparPR 的受限对照](https://arxiv.org/html/2610.18140v1#S3)在 OPT6.7B、单8GB消费GPU的静态offload路径中已有检索质量损失，checkpoint存放/更新与若干完整运行条件也未充分披露，不能从 projection 成本式推出总内存或端到端必然节省。短context、选择失准、无法核实hidden来源或质量/SLO不合适时，完整KV搬回、普通重算与更保守保留仍是必要分支。

本人trueH2注拟：

- `SF-2026-ARXIV-2606-02964`：Daily2026-06-04补Jun03；exact-v1 §2.2–6.5/Alg1/Eq2–9及A.1仅必要保序命题，2+2+2=6具体驻留/多段kernel/控制面代价差额深入。保完整prefix身份、causal/position、历史reuse和cost近似/双树时间基准分责、回放非自由生成质量与H20有限条件/全费；Eq2非完整实现配方、§5.1 lambda全局乘法措辞与Alg1分支缩放/时间校正未完整披露，不采完整调参recipe或指数唯一性作普遍定理，不授逐bit无损/生产SLO。未核代码/kernel/曲线像素或复现；待首次Source/正式评分/actualowner/PRE及新授，不预写/I/DAY。

