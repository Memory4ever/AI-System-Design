# CALVO 21257v1：必要Source与Books差额提案

状态：作者准备，未独立PRE，未写Books。只属03-25补03-24。题摘/Submitted/registered原值见 SUP_FIRST_ABSTRACT_DATE_20261012.json；exact-v1 [HTML](https://arxiv.org/html/2603.21257v1)实际读§2～5，关键位置§3.1～3.2、§4.1 footnote3、§4.2～4.3、§5。

## 必要证据与采用边界

旧compute-centric集中执行在无远程cache的负载里合理。本文针对高prefix reuse的network-intensive prefill，把L3→L2、L2→L1分别交给dispatcher/executor；source block ready且destination allocated才可搬，lower stage预留上层空间并发进展，HBM不足退reactive。priority profile分别估Tload(context)与Tcomp(query)，服务成本用于SJF或deadline slack，而非只按prefill token排队。

原评价vLLM0.9.1/LMCache0.3.1/Mooncake，80GB GPU+128GB DRAM、远端512GB、400Gbps RDMA；Llama3.1-8B/Qwen2.5-14B-1M、LooGLE/ICL/Code长context、Poisson arrival，TTFT-only。对照也修batch_get_into、多CUDAstream，并限一request prefill。SLO为无干扰TTFT×随机2/4/8；FIFO变体与不同hit ratio支撑load-cost及stage组合的局部作用。不采用最大宣传增益，不把SJF/LSTF引用当多资源online普遍最优；precision、GPU具体型号与重复运行不披露。Decode TPOT、agent workflow关联KV调度及生产route为未证明/未来工作，未核实现或复现。

## 具体owner与拟差额

已读当前AGENTS、ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE及最新相关LS；Ch56开篇～SLO admission、第380～440行token scheduling局部，Ch55开篇/收尾、Ch57开篇交接。

INFER-SCHEDULING 当前Ch56第80～82行stage-aware fabric已解释消费层/剩余bytes/permit，token scheduling解释swap搬运预算；它们未承载remote prefix load独立两stage、提前destination reservation及load+compute二元服务成本接口。本拟差额不是重复“network计费”，而是在ready/allocated分别成立后自治跨级loading、用两种token数量分别估服务成本，并说明额外HBM/排队/预测失配及反侧。Ch55仍拥有KV有效性/handoff commit，不能借调度优先级批准KV内容。

拟在Ch56 SLO-aware Admission中现有fabric段前添加两段：先从cache命中节省compute但新增load约束推到跨级ready/space allocation接口，再说明profile成本校准、单prefill局部证据/额外memory与反例，不写普遍最优/全agent吞吐。实际插入位置与措辞待root Source/差额PRE和窄family锁；作者不会自行写入。

## 普通下一步

root非准备者核必要源及实际owner差额；通过后申请SF-2026-ARXIV-2603-21257 / INFER-SCHEDULING / Ch56两段与自身末注窄锁。未授Evidence Gate、PRE、POST或DAY。

## 拟两段正文与本人静态注（供具体PRE，不是实际Books写入）

插入Ch56 SLO-aware Admission中conservative margin段之后、已有fabric小标题之前；不改已有fabric/MFS段及其它family。

远端 prefix 命中减少 Prefill 计算，却不一定减少当前请求的主要服务成本。没有远端 KV 恢复时，由 compute loop 集中推进流程简单而合理；高命中长 context 把瓶颈转向网络与 PCIe 后，可以分别让远端 DRAM→本地 DRAM、本地 DRAM→HBM 的 loading stage 自主推进。执行器只有在源块 ready 且目标空间已经分配时才搬运，低层 dispatcher 可以提前提出上层空间分配请求，让不同请求的传输与计算在依赖满足后重叠；提出请求本身不是成功分配或事务性 reservation。HBM 余量不足时退回 reactive allocation，KV 内容与 handoff 有效性仍由第55章的 owner 核验，而不是由优先级认证。<!-- source-family:SF-2026-ARXIV-2603-21257 -->

这还要求 service estimate 分别校准待加载 context 的传输成本与未缓存 query 的计算成本，再用于短作业或 deadline slack 排序；仅按 Prefill token 数排序可能错估高命中请求。[CALVO 的局部 Prefill 对照](https://arxiv.org/html/2603.21257v1)支持上述接口，但提前分配占用更多 HBM，多stage队列与profile漂移也付费。作者使用400Gbps RDMA、长context与Poisson到达、单request Prefill对照和相对无干扰TTFT定义的SLO，不证明一般多资源调度最优、正常Decode的TPOT或生产尾延迟。远端复用少、内存紧张或profile失准时，保留集中推进、reactive loading与保守队列，不把cache命中率当服务保证。<!-- source-family:SF-2026-ARXIV-2603-21257 -->

本人末注拟追加：

- `SF-2026-ARXIV-2603-21257` — Daily `2026-03-25`补03-24；[exact-v1](https://arxiv.org/html/2603.21257v1) §3.1～3.2、§4.1 footnote3、§4.2～4.3、§5。2+2+3=7，仅采用stage自治与ready/allocated前提、proactive allocation请求及context/query成本分估；80GB GPU/400Gbps、TTFT-only、baseline单request、Poisson/SLO定义与HBM回退保留，不采跨资源SJF/LSTF普遍最优或Decode收益。未核实现/复现；Source与具体owner差额经root非准备者有限接纳，具体正文PRE/实际POST状态以本日packet记录为准，非日级Gate。

## root必要Source、具体PRE与非writer实际POST

实际独读exact-v1§2.3–5/footnote2–3：两stage自治、source-ready/destination-allocated条件、提前allocation请求、HBM不足reactive、context/query二元profile成本与所测Prefill对照成立。SJF/LSTF引用不授多资源普遍最优；两项baseline优化、单request Prefill、随机倍数TTFT SLO、Poisson和未来Agent/routing工作均约束采用资格。具体Ch56差额与两PRE有限PASS后授作者窄锁，没有把权限申请当已成功分配。

写后root非writer实际完整Ch56 62–88：容量/margin→新78/80→完整MFS fabric两段，并读章末Helium/MFS/SARE/CALVO全部邻注。原两PRE逐字唯一各1、正文family标签2份、本人末注唯一1；流程状态未抄入静态注，其他family保留。cached/unstaged限定diffcheck0。自治loading／成本分估与stage-aware fabric是分层关系，KV有效性不越权；具体代价、回退和TTFT-only范围近文成立。一次有限actualPOST PASS，root接纳并释放Ch56本family锁，可计真实I，不授整日DAY、实验复现或无遗漏。
