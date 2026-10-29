# Tangram 2606.06302v1 必要缺层与actual owner

作者supp_20260606_author，2026-10-25。[精确v1 HTML](https://arxiv.org/html/2606.06302v1)、[官方DOI原字段](SUP_SYSTEMS_FIRST_20261025.md)。A6/R4有效题摘与联合Jun05日证直接复用，非current v2（v1题名不含Compression）。旧Jun05既有分 `2+2+2=6` 保持，不重分/不改旧归属；这里补必要和实际Books缺层，不拿旧完成/trace代研究。

## 旧有效层与失效层

具名读取旧Jun05 `V3_RECOVERY_BLOCKERS.md`仅本ID§4及`V2_1_EVIDENCE_ARCHIVE.md`本IDSource/Books单篇：静态预算/分页/AOT的机制摘要仍有效，复用。其model/hardware NotDisclosed与v1 §5.1明确披露不符，质量/费用必要层不足；旧Existing片段写idleHBM/NVLink借用hotprefix，不是本篇headgroup物理回收，故NC层不沿用，不重做日期或搬候选。原反侧保留，新补下述直接缺层。

## 精确v1必要（首次待独核）

实际读§2.2/3–5/7、算法1/核心公式及直接反侧。原统一head页对nonuniform保留按最长head分配，逻辑淘汰不兑现物理回收；动态压缩后回收散页又增加host工作，异构层/头还破坏单kernel-plan跨层复用。§3的50样本/三个model族两domain只支持所测相对排名/variance稳定，不证明input-independent自然定律或所有domain无漂移。

§4.1以query-agnostic FastKVzip分数作offline预算，均值+margin并截inputlen，然后online按固定各head预算选token；固定shape不等固定token，原页预算不是decoder语义不变证明。§4.2按预算排序head、同规模分组、每组独立页表，物理组容量取maxhead，G小减fragment但表数/hostfee增；OpenMP/SIMD仅减少部分控制成本，不是zero开销。§4.3 offline预算推每层group splitmap，运行读表配置kernel；算法1未保证sum splits恰等CTA总量，代码group索引与排序置换映射未充分闭，不照录可执行recipe/完美balance或绝对无尾延迟。

关键容量反侧：§4.1.1式(1)仅sum headbudget×D×dtype，按其K与V各tensor定义未显式2份，又未计groupmax/pagerounding/metadata、full Prefill transient/workspace、后续decode增长与reserve。不能采“guaranteed maximum prefill+compression footprint、batch至true physical limit”承诺。固定离线retention profile只是postcompression目标，必须另验证峰值、质量和越界fallback。

§5.1三model Qwen3-4B/Qwen2.5-7B-Instruct-1M/Qwen2.5-32B；SCBench/LoCoMo/RealTalk/LongMemEval，Short<20K/Mid20–100K/Long>100K，50pilot/alpha2。单server XeonGold6326(16physicalcore)与4A10080GB；vLLM+基于FlashAttention自定义kernel，baseline FlashAttention2/FlashInfer及vLLM，具体runtime版本、precision、每modelGPU/TP placement、完整到达/输出分布、独立重复/CI与acceptance SLO未充分披露，不补。§5.2/5.3为作者受限真实runtime结果而非本次复现；不把图caption/定性parity变逐任务无退步。G=4–8最佳只限本试验。75%compression图14/平均30K请求下TTFT不授全混合请求tail SLO；吞吐分解递增组件有助归因但不是证明任何组合普遍最优。没有读图像素、核实现或运行实验，不引用精确曲线数值。

必要支持的是headgroup页粒度与静态shape规划如何交换fragment/hostfee；不采全部倍率、精确峰值公式、permodel绝对质量或无runtimeoverhead。旧6分相合：D2真实物理回收替代，Reach2跨selector/页/hostkernel接口，Durability2为稳定布局预算边界；不是借旧标签推准入。为实际Bookdelta已深入受影响域。

## actual owner比较与逐字PRE（首次待独核）

已读当前Ch45旧Tangram NC提及的idleHBM侧及KVidentity，不能承载本篇物理页delta；当前Ch47开篇、逻辑物理映射、Block数量内部fragment完整段/共享slab段、token-liveness relocation完整节/COW与kernel接线，Ch46/48开篇承接有效。唯一owner `INFER-PAGED-ATTENTION` Ch47；这不改旧日报字段或搬旧归属。现Ch47 blockwaste解释token尾fragment、token virtualization解释跨blockholes需搬运，却未承载不同head保留长度让同页最长head锁住容量、staticheadgroup预算并不等峰值上界。拟在blocksize权衡完整段（末“Block size 因此是 metadata/kernel efficiency 与内部碎片之间的权衡。”）之后、模型共置sharedslab完整段之前，仅以下两段/独立marker与本人注，尚未请求root窄授或保存。

一个token位置在不同head中不再保留同样长度时，页的内部碎片还会沿head维度返回：只要所有head共用同一长度的分配，短head删掉KV也可能仍被最长head锁住物理容量。一条[受限非均匀缓存分支](https://arxiv.org/html/2606.06302v1#S4)先从离线profile固定每层各head的保留预算，再按相近预算分组，为每组维护独立页表，并复用按该shape准备的kernel分割计划。这里固定的是容量形状，不是每次选中的token；减小group能少留空洞，却增加页表、host维护和kernel接线费用，仍需保持原head身份与位置映射。

静态预算也不能直接当作请求峰值显存证书：KV双份、组内最大值、页对齐和metadata之外，还须另计压缩前的Prefill瞬时空间、后续增长与reserve。少量pilot上的预算稳定不保证新domain同样成立，固定split也不批准完美balance、零在线成本或质量无损；本地vLLM/A100对照不替完整服务SLO。Profile、token选择、页表/分割产物和实际kernel应绑定同一模型/布局版本并计全部费用；预算、质量或真实峰值失配时，回退较保守保留、普通统一页与动态规划，而不由逻辑压缩率放行更多请求。<!-- source-family:SF-2026-ARXIV-2606-06302 -->

本人注拟：`SF-2026-ARXIV-2606-06302` — supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 §2.2/3–5/7与Alg1必要，保原2+2+2=6/唯一实际Ch47。仅headgroup物理回收/shape与peak分责，保profile漂移、组表fee、原容量式/CTA分配不闭和受限runtime；不采zerooverhead、精确recipe/峰值/质量或SLO保证。旧Jun05日期/候选不搬，旧机制摘要复用而错NC不沿；未看图像素/代码/实验复现，首次必要/PRE/root新窄授/真SAVE/唯一POST按后到事实记，不预I/DAY。
