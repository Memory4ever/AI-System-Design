# 11896 Think While Watching：必要Source与具体已有覆盖提案

当前结果：root actual Eq8–12/三阶段/完整Tables5–6/队列C及Ch23/77具体NC通过，formal53已含1+2+2=5标准/已有覆盖Books0。以下“待独核”是准备历史，不授DAY。

mar14_supplement，本提案待非Source作者实际独核。第六题摘准入P/官方arxiv事件Mar13日级夹证已独核，不等本Source。官方exact-v1 HTML GET200/563011B/2026-10-10T01:07:57.501367Z，SUP_NECESSARY_11896.raw/txt。本人实际读完整署名/题摘、§3.1–3.3/Eq1–7、§4.1–4.4/Eq8–12、§5.1–5.5/full Tables2–6、A未来工作、B完整implementation、C完整流式backlog条件和G错误分析；未全prompt/data appendix E、代码、像素case或复现，支持与关键反证足够即停。

## 原增量、评分与必要方法

逐segment读入时decode阻塞且多轮历史衰减→一输入unit对应一派生memory/回答unit的可见前缀与独立position序列→检验派生视频state如何复用、保持因果可见性并降低串行耦合。dual KV和parallel模式本身明确引用已有工作，不给借用成熟并行/队列/摘要原理分。新增且有验证的命题是streaming-aligned监督/显式mask与segment memory在该多轮输入接口下的质量—成本条件，**1+2+2=5**，标准必要审阅完成提案；跨表示/缓存消费边界而非仅指标提升。不授重要新通用并发保证。

§3/4：received R_u是segment或question，generated C_u是相应m_t或rationale/answer，one-to-one同序。m_t=Mem_theta[S_t]保存〈segmentID,note〉；式10从已有notes+dialogue生成answer，非原始视频无损存储。训练把完整R前缀放在C后缀前，Eq11按unit arrival限制C_u只读R_≤u与C_≤u，R不读C；必须连同C内部token causal mask使用，不能只靠序列拼接宣称未来不可见。Eq12源位置只依赖已收到R span，输出位置只依赖已生成C长度，从而不需预知本次完整输出长度。独立双KV是common pattern，adaptive attention在q_len=k_len/1时用FA，否则显式streaming mask；未核kernel/并发一致性，不补造实际snapshot/lock实现。

## 评价与直接反侧

§4.3/B：三阶段5,160单轮、2,752多轮/8,513rounds、1,500长视频/6,000rounds，GPT5.2依据原QA合成CoT/memory，阶段三同时增加长时/不确定性/干扰数据；8×RTXA6000 48GB、bf16、full SFT、batch128，不把联合treatment拆唯一mask或memory因果。真实输入还可有早期identity被过压缩、未足证就commit、近期干扰覆盖旧证（G），Stage3不认证全memory长期保真。

Table2/3：Qwen3VL4B StreamingBenchmultiS3 57.40低于offlineThinking58.52，OVO2Bmulti47.15低于47.74；token/AvgFrames的single/multi人口不同，56.10%少tokens不等全计算或等原证曝光。Table5 notes57.40 vs无notes52.35支持该消融局部差额，120/60segments55.33比60/30的57.40低，而30/15 segments57.20但tokens380.50更高。attention远距质量只是关联，不是实际使用每个note的因果证明。Table6 TTFT明确单位为首次answer token前处理的tokens，TWW与interleaved同2304.28，非wallclock/并发deadline；不采用92.6%真实延迟保证。

AppendixC常率λ/μ、μ>λ且interleaved decode完全停止ingest时，backlog λT_dec，catchup=ρ/(1−ρ)T_dec；理想full overlap近0只是假设，原文明确scheduling/sync/cacheoverhead可剩backlog，不能授真实双KV零等待或处理率不受decoder竞争。线上到达/共享GPUprofile、full pipeline tail/concurrency/SLO、重复seed/CI未认证；FutureWork仍待联合accuracy/latency/resource协议。支持仅受测Qwen3VL/StreamingBench/OVO等、非任意全双工服务。

## 具体NC（非主题映射）

实际顺读Ch23『Streaming Multimodal Identity』1057–1093完整上下游：1076–1078已经直接承载两逻辑前缀/各自position axis、output可见到达prefix、decode段观察revision、buffer同步/commit仍属runtime，以及缓存/编码/同步成本、口径不明TTFT不得替端到端和serial退路；1081–1083直接保存derived evidence/时间来源、压缩漏证/错trigger/保守回退。另1060附近已分训练顺序与实际读取历史并留cache失配/原历史退路。Ch77 68–106具体model-generated summary须derived/原证权威、验证来源与revise/pending写入，归通用memory owner，不重复到Ch23。Ch22与Ch24入口分别保sequence容量和生成采样职责，无需让memory note接管world或sampling。

本稿实际新增只是该现有因果可见前缀与派生state的受限validation，未支持新commit/snapshot/provenance不变量；式11/12与one-unit格式是此实现的具体序列化配方，不据精细公式强写新稳定知识段。**拟标准完成/已有覆盖：MULTIMODAL-REPRESENTATION Ch23上述完整具体局部，Books0**。有限数字/配置与负侧留报告，不把已有覆盖用作减分或取消候选。待root实际必要方法/关键反侧与完整指定owner独核；不授全附件/代码或本日报DAY。
