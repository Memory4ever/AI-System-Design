# 04315：必要Source / actual-owner具体No Change提案

作者supp_20260605_author，2026-10-25；只Daily2026-06-05补Jun04。R33–36准入/精确v1联合日期有效复用，不第三AB/date。采用[Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline, exact-v1](https://arxiv.org/html/2606.04315v1)，官方HTML原件`SUP_2606.04315v1_20261025.html`303836bytes。实际读§3–6/T1–9/Alg1、Limitations、B/B.1、C、D backbone反侧及E/T13–14必要支持/反证。没有扩全baseline上游、全部prompt/实现或证明，未复现。支持与直接反侧已足，以下只采有限诊断/选型边界。

## 评分与最小采用命题

首次2+2+2=6；具体贡献：单场景memory排名会混构造保真、读取接口、actor能力和费用→同一跨场景protocol给store-answerability probe、无索引harness与主动读取/已有index组合→先查信息丢失层及query/复用条件，再决定是否预建schema或让Agent多步取证。6分标准必要审阅已达，针对active-interface与actor上限这类可能误采用命题定点核关键反侧；不借成熟memory taxonomy、机构或能映Ch77加分。

### 必要原证及未证明部分

- §3/T1–3八memory系统+搜索harness覆盖五task families；QA由Qwen3-32B judge、主构造/answer同Qwen3-32B，embedding Qwen3-Embedding-4B，ALFWorld改Qwen2.5-7B。不能把同一backbone多role当独立验证，跨domain的静态QA与环境SR/PS/c-sPS也不能合成同一效用单位。Gen是fractional rank、MemoryAgentBench四列先均权合一次；加入新method会改变原method rank，不是绝对能力比例。
- B固定deterministic子集：HotpotQA200题/9811corpus，LoCoMo200题，MAB200题，ALFWorld60、MemoryArena每scenario30；AMA原件此表仅写三个domain，别造满release计数。无所有seed/重复run/完整CI披露，T3 Variance只明称sampling-noise floor，不能变成严格显著/置信保证。
- §4.2/T4抽60个AMA题，由Codex/gpt-5.5 extra-high读complete store判断oracle answerability；含raw episodic时可用原trace，是受控上界probe，不是线上实际取回/actor利用或独立真值。Hippo entity schema可能丢step/action、PlugMem store可答而router未送达，支持分开construction/retrieval，不支持“主动读一定补齐”或所有index不可用。
- §4.3/T5长历史vswindow/实体直接命名/所采schema等probes各绑定population；换输入/任务也改变内容分布，不能从suite总体rank隔离“active control”唯一因果。§4.4 structural rate是在指定flat retrieval unit及grep/BM25/dense top5下“单unit不可答”的比例，不能等同必须依赖prebuilt index或所有可能retriever的信息论上界。N约2/32成本交点只属于所设amortization/token计数，不是普适wallclock盈亏点。
- §4.5/T7有限ALFWorld控制：原长context46.7%、golden procedural71.7%、GRPO86.7%，50stepcap；有规则仍失败只表明该actor/规则/任务尚有限制，不能证明文字永远不能编码state-dependent分支、非参数memory存在普适capacity ceiling或只有parametric update可越过。Golden/GRPO的额外专家与训练资源不可删；“all32cap”和“remaining17”不代分层完整因果实验。仅隔离这些泛化，不降分/删候选。
- §5/Alg1明确四action `{rg,read,dump,index_query}`，对raw/已有index取证；planner提出一个调用→executor→trace→同backbone judge判充分或给缺口hint→answerer。未列create/update/delete/write store动作，也未展示从online任务反馈持续学习write policy。因此初筛宽称active storage/read-write须收窄：本实现支持主动组织读取/查询、组合预建index，不据此认证主动写权限的独立收益。
- LightMem graph默认用SAID_BY/OF_TOPIC/FOLLOWS，PlugMem variant另tag/episodic/semantic；schema仍是预先选择，不是已实现的自动DSL/schema搜索。Judge sufficient会错；Kmax耗尽仍Answer(trace)，不是fail-closed授权门或证据完整保证。
- T8 LoCoMo67.3相对DCI45为+22.3pp/49.6%relative，不是跨所有任务49.6%；rank改善依赖suite和插入方法规则。Singlepass63.5是不同路径：禁dump、跳judge/replan，一次plan后rg/read/indexquery并行，不是同一loop只少一轮而所有接口不变；质量差不能唯一归judge。
- §5缓存layout在Qwen3-32B/vLLM局部把稳定prefix前置，cache hit5.4%→50%以上；singlepass省query tokens但仍支付LightMem build和planner等。未实现tier-router的2–3倍节省仅估算/建议，不采用“现报告cost必为upper bound”普遍保证。
- E/T13服务测量是Qwen3-32B/sglang/单B200，HotpotQA用2000corpus子集，而主任务9811；不能把这些wallclock/MFU或跨stack cache数据与主token表当统一等价净成本。平均在途约1、长prefill短decode与串行调用支持token≠latency的局部诊断；实现可改进与内生依赖的分类是作者分析，不等所有序列化可免费并行。具体软件版本/precision/并发/SLO/整链matched预算未充分披露，Not Disclosed。
- C两重要重建：AMA-Agent作者补足开源与原描述差额；MemoryArena原发布无simulated env，本篇自己实现approximation。因此不能把“真实Agent tasks”标成真实用户/原benchmark environment生产复现。D换Qwen3-4B后部分index更强、DCI的MAB退步，且动态三列约0被省略；不授frontier规模普遍active-harness胜出或能力threshold定律。
- Limitations judge protocol可改method排名；B.1固定reader只改answer prompt可改F1约34pp，说明评价接口会混淆排名，但LLM judge亦非不偏真值。现证据只支持受限bench诊断，不给安全/写入授权、实用户effect或生产SLO。

## actual owner：具体已有覆盖，不制造diff

已完整读当前ROADMAP/三Books上下文/仅2026路由及actual Ch77下列对应段，邻Ch76/78开头交接。唯一owner `AGENT-MEMORY` Ch77；不新建结构、不改共享Books。本次No Change针对**受限可采用命题**，不否定04315准入/贡献或按覆盖缩候选。

1. **丢在写时还是读时。** Ch77“先分开Construction与Retrieval Failure，再选择Memory结构”完整组：1046起明确construction未编入action/state与retrieval未找到已构造state；versioned trajectory→representation/provenance→fixed eligible query→causal/state evidence→sameContext budget。后续BabyAI的raw needle/constructed/完整路径，以及“用干预矩阵定位写入、检索与阅读失败”已有complete stored-vs-retrieved的明确诊断。对应本T4有限store probe；不再追加一份同义分类。
2. **读时组织raw与预建index的共存。** Ch77“从Write-time Summary转向Query-conditioned Late Construction”471起：write summary适合稳定分布/严格预算、不可恢复漏细节；保raw且按query高召回/有界window取证；同节sufficiency controller不足时沿source pointer回读raw，保controller/verifier可能错和新增token/延迟。对应AutoMEM plan/query→judge缺口→再读；本四action和图schema只是该分支的具体实例，不新增一种长期权限或真值接口。
3. **结构×workload与维护/摊销。** Ch77“先分解Memory组件，再判断Graph是否值得”当前1225起已逐列extraction/representation/index/maintenance/retrieval/answerer，说明raw exact fidelity/flat高QPS/router互有条件，不作全局排名；同组固定history/querypopulation和same model/budget。LateConstruction内写时fact extraction与cached fullhistory完整对照，明确query数/缓存/更新/维护决定交点。对应跨场景/结构需求和token摊销，不能再写成“flat或agentic永久优于index”。
4. **QA不是闭环effect，局部tokens不等净费。** Ch77“评估Memory”明确MemoryArena dependent episode的progress/success/latency、raw长历史与超窗负载不同，以及线上/静态分别验收、ingest/maintenance/retrieval/answer全部计费；same memory-on/off还验actual read/write exposure。对应本approx env/变化metric与成本限制，原有正文比本文泛上限更保守。

四项均有实际具体承载，并非只因标题相似或可映owner。拟**已有覆盖/NC，无正文或Review note改动、无PRE literal**；只保Report里的新bench实例与协议差异、不同baseline/harness/actor及尚未采用的泛化边界。表格排名、百分数和原vendor cache数字不是必须入书的长期机制。待本篇首次非writer必要Source/actual-owner/NC独核，不预NC验收/I/DAY；若发现一条未承载的长期差额，再只为该差额提最小PRE，而非按固定整合配额造diff。

## 当前准备态

本单篇6分必要Source/实际Ch77具体NC ready。04555已R57–58行政同步生效，累计新增I13＋旧Kimi合计14I；本04315不增加I。其余八04980/04708/04463/04306/04104/04896/04364/04485必要层及有限官方标题stop/最后DAY普通保持；本阶段交root即结束释放槽供首次独核，不因等待扩下一篇Methods。无State/index/他日/未经授权共享Books正文写入，未stage/commit/push。

## 当前R59–60已实际采用：具体已有覆盖生效

上节为首次独核前准备态。现已实际完整读回R59–60，6分必要Source/actual Ch77四组具体已有覆盖/NC通过，正式候选和证据保留；只行政同步README/本Source，不写Books/Review note、不另建PRE/POST，不第三技术。04315不增加I，既成新增I13＋旧Kimi合计14I；其余八及有限标题stop/DAY仍ordinary，未授DAY。
