# 2026-09-23 — 官方公告日期恢复与有限贡献审阅

作者：原恢复 `apr02`，2026-09-30 续跑 `apr29_close`；恢复访问日期：2026-09-27／2026-09-30。当前状态：40家族必要证据/最终Books处置及35处实际整合写后已逐项非作者通过，只待§4.24全日独立复核；root已重新授权仅本日闭环，旧暂停指令不再作为停点。不是作者自签的独立日级Gate。

## 1. 窗口与日期依据

目标窗口严格为 `[2026-09-22T09:00:00+08:00, 2026-09-23T09:00:00+08:00)`。已亲读当前 AGENTS、统一 Prompt、Research/Report 合同、Sources 每日入口及12类路由、ROADMAP。官方 [availability/Announcement Schedule](https://info.arxiv.org/help/availability.html) 将 Tuesday20:00 Eastern 的常规公告对应 Wednesday00:00UTC；2026-09为EDT，故本次官方 recent **Wed,23Sep2026** 组对应 09/23约08:00BJT。这是官方组标签与时刻表联合的有据批次归属，不把 submitted/DOI-created 当 first-public，也不宣称逐篇成功上线秒级日志。标签解释另外复用 [09/22恢复笔记§1](../daily-20260922/arxiv-recovery-20260927.md)：当前 cs.CL/new Friday25 与 recent Friday25 的 New/Cross ID集合相同，而官方 Friday20:00没有常规公告。因此 recent标签不能再顺延一天。

本轮实际重新取十二类 recent 页面 `skip=0&show=2000` 的 Wed23组，所有组提取数与页面 showing一致；首遍解析因 href前后空格提取0，已定位修正，不能把解析失败当0更新。输出截断导致一次结构结果不可完整解析，仅用于失败诊断；最终按唯一身份压缩，原始类分组和去重身份在下方持久保存。

题摘首批30项中，只有Flux `2609.25949`在十二类为Cross-only。已定点重新取其官方abs primary=`cs.NI`与[cs.NI recent](https://arxiv.org/list/cs.NI/recent?skip=0&show=2000)：它位于`Wed,23 Sep2026 (showing22of22)`组，官方primary类别为cs.NI，不是凭cs.DC Cross擅定first-public。其余29在至少一个合同分类为New，或已有更早正式family（HBF）而去重；不从112个Cross-only库存推断全部首发属于本窗。

## 2. 来源停点与原身份检查

| 分类 | 该recent整页total | Wed23 New | Wed23 Cross | 官方组标题/停点 |
| --- | --- | --- | --- | --- |
| [cs.CL](https://arxiv.org/list/cs.CL/recent?skip=0&show=2000) | 659 | 80 | 28 | `Wed, 23 Sep 2026 (showing 108 of 108 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.LG](https://arxiv.org/list/cs.LG/recent?skip=0&show=2000) | 1230 | 118 | 98 | `Wed, 23 Sep 2026 (showing 216 of 216 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.DC](https://arxiv.org/list/cs.DC/recent?skip=0&show=2000) | 117 | 12 | 11 | `Wed, 23 Sep 2026 (showing 23 of 23 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.AI](https://arxiv.org/list/cs.AI/recent?skip=0&show=2000) | 1202 | 101 | 139 | `Wed, 23 Sep 2026 (showing 240 of 240 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.CV](https://arxiv.org/list/cs.CV/recent?skip=0&show=2000) | 784 | 108 | 35 | `Wed, 23 Sep 2026 (showing 143 of 143 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.RO](https://arxiv.org/list/cs.RO/recent?skip=0&show=2000) | 640 | 104 | 8 | `Wed, 23 Sep 2026 (showing 112 of 112 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.AR](https://arxiv.org/list/cs.AR/recent?skip=0&show=2000) | 64 | 8 | 2 | `Wed, 23 Sep 2026 (showing 10 of 10 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.PL](https://arxiv.org/list/cs.PL/recent?skip=0&show=2000) | 30 | 2 | 4 | `Wed, 23 Sep 2026 (showing 6 of 6 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.OS](https://arxiv.org/list/cs.OS/recent?skip=0&show=2000) | 7 | 1 | 1 | `Wed, 23 Sep 2026 (showing 2 of 2 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.PF](https://arxiv.org/list/cs.PF/recent?skip=0&show=2000) | 29 | 1 | 2 | `Wed, 23 Sep 2026 (showing 3 of 3 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.IR](https://arxiv.org/list/cs.IR/recent?skip=0&show=2000) | 117 | 11 | 4 | `Wed, 23 Sep 2026 (showing 15 of 15 entries )`；skip0/show2000，本组完整至下一日标题 |
| [cs.MA](https://arxiv.org/list/cs.MA/recent?skip=0&show=2000) | 89 | 8 | 7 | `Wed, 23 Sep 2026 (showing 15 of 15 entries )`；skip0/show2000，本组完整至下一日标题 |

跨类去重得到 **666** New/Cross身份：554在任一合同类为New，112仅在合同类cross。这是官方宽列表，不是贡献候选，不是666篇全文队列；cross-only也不自动全部拒绝，可能来自其他主分类的本批首次公开家族，仍需身份去重。

廉价检查正式09/23 §3的38个唯一arXiv ID：与真实Wed23集合只有 `2609.23640` 与 `2609.24194` 交集，均为cross-only；前者/后者在更早Tue22已公开，不能因为今日跨类出现重复计分。其余36不在Wed23组。[09/22恢复§4](../daily-20260922/arxiv-recovery-20260927.md)已核38/38在Tue22。旧机制/实验/实际Books写入不因此被否定，但旧本日日期/冻结/Complete不能直接继承。**路径纠正**：正式README的 `../../_sources` 实际解析到年级 `papers/2026/_sources/daily-20260923/`，原机构/证据附件有效存在；先前仅检查月级目录而称附件丢失不成立，现撤销该判断。有效证据继续复用，机构side不重复全扫。`/private/tmp/arxiv-20260923.json`及12份旧new HTML仍可见，页面日期全为Tuesday22September2026，只作为错配来源证据，不复制成Wed23。

历史Replacement原始批次尚未恢复；recent不含其完整历史清单。不能从本次New/Cross恢复推出没有重要修订。下一步仅对明确修订/撤回信号定点查官方归属，不制造全量版本diff任务。

已实际完整读取年级 [institution-screening.md](../../../_sources/daily-20260923/institution-screening.md)，不是只读旧README声明：OpenAI Sol/Luna与Prompt Caching、Qwen Code0.24.5、MiMo Code0.1.15、MiniMax Code0.5.2有原事件时间、核心说明与具体处置；旧CLI PR的较早owner仍保持。日期仅到日的Opus5.5/Card、Astra、MiMoV2.6、ZCode继续按原精确缺口隔离，不能因机构声明而强塞本窗。Hunyuan实际目录为9条：root已定点恢复第9条100116为[When Do Larger Batches Help Scale LLM Reinforcement Learning?](https://arxiv.org/abs/2608.29296)，官方v1 2026-08-29T14:32:09Z、当前只有v1，无September revision；09-22 display日/09-23 publicAt只是同family网页出现，不形成本窗首次公开/重要修订。纠正旧8条目录零事件措辞，不深审旧论文或挪动旧owner证据。Qwen动态Research等既有访问限制也不变成0更新；机构lane有效结果复用，本lane不重复全扫。

## 3. 有限贡献准入

先浏览666个官方题名，再对下表30个明确可能改变主线机制/评价边界的家族实际读取官方完整摘要和当前版本历史。这个定点集合不是全部待筛队列，也不是冻结分母；尚有安全、编译、协调等题名可能需第二批消歧。没有把所有分类命中都送全文。日期仍使用§1公告组；即便v1 submitted在9月6/7日或8月，也不据此否定本批首次公告。当前版本26513v2、26425v2已明确标出，不制造版本diff。

表中分数是已准入命题的三维初评`Design Delta + System Reach + Durability`，不是已经完成证据审阅。已准备好的独立单元见§4；其余普通待审不是外部受阻。29项通过本批初筛，1项较早同家族去重；29也不是本日最终冻结数量，须待独立准入口径和有限查漏完成。对原始标题明确无主线问题者，代表性范围关闭为`2609.26662`儿童近视治疗纵向血管研究、`2609.25697`特定地区青光眼筛查产品、`2609.25040`香蕉病害领域适配；它们仅按明确题名范围判断，未冒称摘要/全文已审。`2609.26502`晶体结构生成benchmark属于当前暂缓AIforScience，不凭含generative恢复；含评价隐私/可解释性机制的医疗题名不据学科标签自动拒绝。

| 家族/当前题摘版本 | 实际题摘中的具体贡献或去重理由 | 初评/后续 |
| --- | --- | --- |
| [2609.26796v1 Flash-dLLM](https://arxiv.org/abs/2609.26796v1) | dLLM cache刷新与同模型两视图验证共同放大HBM流量；融合KV写入和动态query/block计划改变实际执行分支，不以摘要加速倍数准入 | 2+2+2=6；已确认Ch49窄gap，深入单元§4.1 |
| [2609.26368v1 HySparse2](https://arxiv.org/abs/2609.26368v1) | 外层只桥接FA层的投影源、内层复用FA的KV/索引；recent窗口并入token选择，self-decoder后prefill退出改变state生成/消费边界 | 2+2+2=6；Ch22 gap深入，§4.2 |
| [2609.25611v1 Qwen3.8-Omni](https://arxiv.org/abs/2609.25611v1) | 原生多模态共训与LiveHarness/MMPlugins提出持续上下文、工具与实时Agent的具体设计线索；先核架构与训练责任，不把百万context/榜单当机制证据 | 2+2+2=6；必要技术报告待审，owner待Ch23/81具体比较 |
| [2609.25890v1 Length-aware speech training](https://arxiv.org/abs/2609.25890v1) | 匹配token exposure后顺序效应减弱，batch-mean与token-balanced weighting改变首epoch收益；需区分调度效率与真实优化作用 | 2+1+2=5；Ch28真实loss-weighting gap触发必要深入，§4.9 |
| [2609.25053v1 LatentPort](https://arxiv.org/abs/2609.25053v1) | hybrid兄弟模型迁移仅KV仍有缺口，GDN/conv持久态与小校正共同决定teacher-forced迁移；挑战cache可跨模型直接复用 | 2+2+2=6；Ch45窄gap深入单元§4.5，不采用16K/自由生成保证 |
| [2609.25048v1 OPD breadth/refresh](https://arxiv.org/abs/2609.25048v1) | 同轨迹与更新预算下prompt breadth收益取决于rollout refresh，换token预算排序又变；不是单调扩大提示集合的建议 | 2+1+2=5；标准完成，拟仅报告，§4.8 |
| [2609.26693v1 Serving-stack evaluation](https://arxiv.org/abs/2609.26693v1) | 推理前template拒绝被算失败、native vs uniform协议和pooled vs instance分母可改变排序；不是仅新增工具benchmark | 2+2+2=6；Ch66评价有效性窄gap必要深入，§4.10 |
| [2609.26621v1 Greedy precision](https://arxiv.org/abs/2609.26621v1) | 同硬件greedy仍受精度与head方向误差影响；FP32 head受batch/FP8 body限制，改变可复现执行合同 | 2+2+2=6；必要方法与Ch49数值执行owner待核 |
| [2609.26333v1 DisaggQuant](https://arxiv.org/abs/2609.26333v1) | Prefill低精度compute-native权重与decode weight-only可分别优化，但共享KV兼容仍是边界；不能从两阶段分拆推出任意格式可混用 | 2+2+2=6；Ch55真实阶段参数/缓存语义gap深入，§4.6 |
| [2609.26173v1 Attention quantization sensitivity](https://arxiv.org/abs/2609.26173v1) | 局部reconstruction并非component/layer任务敏感度的同一排序，activation weighting在V的效果不普遍；受控跨模型反证值得标准核验 | 2+1+2=5；Ch49实际量化正文比较待做 |
| [2609.25482v1 TSA](https://arxiv.org/abs/2609.25482v1) | 训练schedule与终态estimator共同定义优化结果，local-quadratic trajectory分析/受限迁移挑战把两者独立调参的选择 | 2+1+2=5；Ch28标准必要审阅待做 |
| [2609.25451v1 Dynamo recovery](https://arxiv.org/abs/2609.25451v1) | GPU模型分配生命周期脱离engine进程，pretraffic shadow与snapshot/replay分开；不是普通重启更快 | 2+3+2=7；深入单元§4.3 |
| [2609.25949v1 FluxOCS](https://arxiv.org/abs/2609.25949v1) | 面向整个workload复用circuit/摊销reconfiguration，不独立优化每个collective；需核network时间线及“最优”假设 | 2+2+2=6；Ch36必要来源/真实正文比较待做 |
| [2609.25869v1 Tessera](https://arxiv.org/abs/2609.25869v1) | 固定logical mask下物理retile与task组织分权，离线eligible portfolio让online只准备一份计划；plan最快不等request最快 | 2+2+2=6；Ch49 gap深入，§4.4 |
| [2609.25782v1 Hot/Cold HBF](https://arxiv.org/abs/2609.25782v1) | 已有更早同题IEEE LCA家族`10.1109/LCA.2026.3729099`，本lane重新取Crossref原字段published/print=2026-07；created=08-31不是首发 | —；较早家族身份去重，不把今日arXiv重公告重复计分；方法证据仍由真正较早owner复用 |
| [2609.26763v1 SARA](https://arxiv.org/abs/2609.26763v1) | P/D/KV传输用不同队列模型推尾分位成本/goodput配置；需判断假设下quantile目标是否区别已有phase/tail容量合同 | 2+1+2=5；Ch56标准必要审阅待做 |
| [2609.25442v1 WeightBridge](https://arxiv.org/abs/2609.25442v1) | trainer→rollout布局映射自动抽取并去冗余平衡，具体transfer plan不是“异步同步”重述；stall加速不能当训练E2E | 2+3+2=7；Ch36深入单元§4.7 |
| [2609.26467v1 RouteRLT](https://arxiv.org/abs/2609.26467v1) | generalist生成phase specialists，phase分类/稳定器/chunk边界切换共同拥有执行权；不是只加一层MoE | 2+2+2=6；Ch26窄分支待核 |
| [2609.26292v1 RoboTwin-Phys](https://arxiv.org/abs/2609.26292v1) | 连续物理属性轴把visual robustness与physical robustness分离；准入的是可复查评价边界而不是13属性/5k演示数量 | 2+1+2=5；Ch26/66具体采用边界待核 |
| [2609.26219v1 PatchKV](https://arxiv.org/abs/2609.26219v1) | prompt局部编辑后suffix因causal/RoPE漂移失效，离线repair区域与非局部稀疏attention联合；page precision标签不能省略 | 2+2+2=6；Ch45具体恢复partition gap必要深入，§4.11 |
| [2609.26086v1 CoVeR](https://arxiv.org/abs/2609.26086v1) | coverage margin只路由不替代最终verifier，head停止不等证据真值；具体成本/有效性分工值得核验 | 2+1+2=5；Ch76标准待审 |
| [2609.25853v1 MemoryAthena](https://arxiv.org/abs/2609.25853v1) | 直接Engram残差与两路生成表示分别提出内容，以未来token likelihood训练router并保留E残差回退；E不是事实真值 | 2+2+2=6；Ch22受限读取/表示职责gap必要深入，§4.12 |
| [2609.26779v1 Cliff compaction](https://arxiv.org/abs/2609.26779v1) | 只保留最近live窗口的verbatim fragments，并丢弃前次compaction而不是反复摘要；不从完整原始轨迹重新压缩，recall主动丢失 | 2+1+2=5；必要§2/3/6/8已读并纠正题摘解释；最终Ch75处置仍普通待办 |
| [2609.25130v1 Impact not invalidation](https://arxiv.org/abs/2609.25130v1) | dependency reachability/behavior变更不等claim不再成立，问法可改变同claim判决；需要区分缓存invalidator与claim有效性裁决 | 2+2+2=6；Ch77评价/有效性必要深入待审 |
| [2609.25052v1 Self-cleaning store](https://arxiv.org/abs/2609.25052v1) | append-only反馈与清理门槛可出现非单调保真区间；有限事实实验只支持局部机制，不以“自清理”名称认定长期可靠 | 2+1+2=5；标准最小机制消歧待做 |
| [2609.25770v1 Reading right, answering wrong](https://arxiv.org/abs/2609.25770v1) | 可读对输入而答错、resize配置改变表现；需核attention intervention是否证明依赖而非用提示救回当自主能力 | 2+1+2=5；Ch23标准待比较 |
| [2609.26425v2 Quantized world-model cache](https://arxiv.org/abs/2609.26425v2) | 2bit视频KV局部误差小/VBench相近仍可flicker，K的query-sensitivity与residual补偿区别均匀KV量化 | 2+2+2=6；当前v2必要审阅，Ch45 temporal边界待核，不做版本diff |
| [2609.25809v1 Two-thirds experts](https://arxiv.org/abs/2609.25809v1) | 保守预算静态专家基线与动态选择差距小，激进预算generation/多模态退步；重要的是控制比较后的适用边界 | 2+1+2=5；Ch21标准待比较 |
| [2609.26513v2 Virtual encoders](https://arxiv.org/abs/2609.26513v2) | decoder内部表征有encoder-like计算不等模块身份，需核causal干预能支持的功能范围；不以probe相似直接采用 | 2+1+2=5；当前v2标准，Ch23待对读 |
| [2609.26774v1 StableVQ](https://arxiv.org/abs/2609.26774v1) | STE encoder目标、区域codebook追踪与分离LR联合改变codebook/encoder耦合责任，不以ImageNet指标自动推广tokenizer | 2+2+2=6；Ch23必要机制/消融待核 |

本批题摘准入尚待非作者校准；必要审阅准备好的单元不等待其他项，后续不得把上表待审改名外部暂缓。

## 4. 必要证据与 Books queue

以下是实际原文与实际Books主线对读后的十二个有限单元；作者证据结论尚待root非作者审阅/采用及写后，不表示Books已整合。所有访问日期2026-09-27，公告归属采用§1，不将页头22Sep投稿日期改成本日首发时刻。当前没有复现实验或验证代码实现。

### 4.1 Flash-dLLM：更新状态路径与验证计划共同优化

来源：[exact-v1 HTML](https://arxiv.org/html/2609.26796v1)，已实际读§2.1–2.3/Alg1–2、§3.1/3.3、LimitationsA；6分，由实际Ch49缺口触发深入。QKV/RoPE/cache-write在SRAM融合后写最终KV；tracked+masked query读全cache，两视图相互隔离并逐位在首个不匹配处停止，未更新位置仍近似。收益不证明原联合采样分布或双向cache完全精确，同模型agreement也不是独立truth。§3.3有quality–throughput折衷及confidence-only峰值accuracy略高的反证；证据限单A10080GB、LLaDA1.5等受测masked模型、数学/代码、固定门槛和window，RTX3090局部kernel实验不是A100E2E，在线SLO未披露。

实际owner `INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“FlashAttention在这里的位置”及紧接batch packing已讲IO与membership，但未承载dLLM**刷新query集合+两视图验证**共同冻结执行计划的分支。拟在IO段内补“缓存省FLOPs却新增写回/验证流量→融合状态更新→保留近似质量预算”，不是追加论文摘要；Ch45保有cache freshness，Ch48保有采样/验证语义。静态/全量刷新在精确性、其他生成范式、门槛不稳时仍合理。**Queue：提案；未写Books；root需必要source/owner复核。**

### 4.2 HySparse2：桥接的不是所有层的同一个KV

来源：[exact-v1 HTML](https://arxiv.org/html/2609.26368v1)，实际§3.1–3.3及§4.1–4.5；6分、已确认Ch22窄gap深入。Outer只让self-decoder FA hidden作为cross-FA的K/V重新投影源，Q仍来自当前层；inner再把FA KV/索引复用到sparse层。token选择并入recent128，不另走SWA。这样prefill可在self-decoder退出，但依赖训练好的结构，不是现有checkpoint删层。80B-A3B及290B-A8B受限对照有DROP/BBH/GSM退步，FA-only源优于Mirror的解释仍是作者假说；百万context FLOPs/KV容量为资源计算，不是部署latency/SLO实测。

实际owner `MODEL-LONG-CONTEXT`，[Ch22](../../../../../books/part-02-model/22-long-context.md)“Sparse Attention还包含两个独立ownership轴”已讲full层刷新/后层复用，并非全新原则。真实窄增量是**outer FA-source→重投影的cross-cache**与**inner reuse**两个域，以及recent强制纳入选择如何移除独立local分支。拟在现两轴论证内补这组训练结构/早退出条件，不复制Ch45内存layout。full+window/dense在迁移风险、短context或精确回读时保留。**Queue：提案；未写Books；不采用全面质量保持或部署加速保证。**

### 4.3 Dynamo：模型分配存活不等请求状态已经恢复

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25451v1)，实际§2、§3.1–3.4、必要实现§4、§5.1–5.2；7分深入。GMS跨engine持有提交的只读weights和reader leases；pretraffic shadow另有context/communicator/graphs/private state，只共享权重，不保存旧请求KV。健康GMS/GPU允许promotion+freshKV+request replay，GPU reset/损坏则cold fallback；失败前未提交allocation不能发布。生产18周日志的device-preserving事后分类不等实时完整性oracle。SIGKILL受测8GPU B200、vLLM0.27.1/SGLang0.5.18、披露模型BF16/NVFP4/TP8等配置只支持相应恢复时钟；Table3中snapshot-only的DSV4-Pro慢于warm restart，而非‘snapshot比shadow快’；该错误由sep21对原表纠正。Shadow从failure injection计时、其他从container start，不能混同完整恢复clock，不证明所有失败、P99或外部effect exactly-once。

对读两个相邻职责后，推荐唯一owner `INFER-DYNAMO`，[Ch52](../../../../../books/part-05-inference-system/52-dynamo.md)“Failure与正确性”→“Wide-EP的部分Rank恢复”：现论证已有membership/expert coverage/graph同epoch，却没有**engine进程死亡与GPU模型allocation寿命分离，预流量shadow从未保存request-progress**。Ch56“MoE Failure Recovery必须拥有Request与Expert Generation”已拥有freeze/replay与策略，不应再完整解释runtime状态寿命；拟在Ch52现故障论证内加入保留只读model state→重建private execution state→请求replay的受限替代分支，旧full restart/healthy replica继续有效。Ch54接HBM额外预算，Ch35接durable checkpoint；不可改写成checkpoint原子性。**Queue：提案；未写Books；需要root来源/实际owner复核。**

### 4.4 Tessera：最快kernel与最小完整请求成本不是同一计划

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25869v1)，实际§2、§4.1–4.4、§5.1–5.2/Alg1–2、§6、§7.1–7.4；6分、Ch49具体gap深入。logical active interaction固定，Direct/Coarsened/Refined与task组织是两层物理选择；coarsen保留membership mask、refine保留online-softmax域。离线catalog/feature schema/regime table同版本，online先核dtype/layout/metadata/workspace等eligibility再准备一个plan；排名不是语义证明，miss保留eligible base fallback/no-plan。相同catalog的online穷举可改善kernel却让cold request更慢；4种GPU/2315视频mask与H100两模型50-step loop是不同指标，不冒称生产SLO。BF16输入/FP32累加、mask来源/独立profile split见§7；数值reference检查非bitwise等价保证。

实际owner `INFER-TENSORRT-LLM`，Ch49已有IO/heterogeneous packing但没有**保持mask不变的retile+离线eligible portfolio/online准备成本**具体分支。拟接IO-aware论证，用冷请求反证引出版本化regime与fallback；kernel更快不等请求更快，cache热重复也不等任意动态mask。简单native/base plan在shape少、短负载、表版本不匹配时保留；Ch48接编译/计划，Ch45接KV物理状态，不另堆“编译器新框架”。**Queue：提案；未写Books；root需非作者采用复核。**

### 4.5 LatentPort：混合模型的迁移对象不止KV

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25053v1)，实际§2、§3、§4.1–4.4、§7；6分，Ch45窄gap深入。Qwen3.5 Base4B→9B有同persistent geometry，但KV仍翻译，GDN矩阵/conv history可直接复用，metadata新建、fresh cache clone；形状相同不证明功能等价。KV-only对比加入GDN是**矩阵+conv+初始化语义的package**，不能全归因矩阵；低reconstruction error也未保证更好的续写。identity-anchored correction针对teacher-forced输出KL，不是整个handoff仅43万参数。4K/64 observed targets、单RTX5090、BF16+FP32 recurrent、64配对document/bootstrap支持受限行为损失改善；near-native三门槛均失败，16K未运行，自由生成/任务成功/生产E2E未证。

实际owner `INFER-KV-CACHE`，Ch45已有跨模型learned translator（约136–144行）及paired compatibility（约1230行），因此不能写“此前没有跨模型迁移”。真增量是**hybrid state manifest必须包含recurrent/conv/初始化，component-wise translation与copy在行为指标上分别裁决**。拟嵌入原handoff分支，保留paired质量gate和target重新prefill，不用NCR误写accuracy；Ch22解释GDN表达机制，Ch45拥有迁移状态。**Queue：窄提案，未实际写入，待非作者source/owner裁决。**

### 4.6 DisaggQuant：阶段参数对的兼容不等同token历史

来源：[exact-v1 HTML](https://arxiv.org/html/2609.26333v1)，实际§2.3–2.6、§3.1/3.3、§5；6分，Ch55已确认gap深入。format-only可仅decode关闭activation quant；full-disaggregation则共同训练不同P/D权重，prefill生成KV供decode消费，或冻结已有量化decoder只训练其prefiller。分离权重增加artifact/storage；本地ODP按block流式加载并暂借decode buffers后恢复，不适合直接推广稀疏MoE。单DGX Spark、batch1、披露Qwen/Gemma、NVFP4/LUT等format，训练100M Tülu3 tokens相同预算；误差条来自一run末5checkpoints而非独立训练seed。多轮未测：assistant token的decode-KV与后来用prefiller重建的KV可能不同，不能宣布context identity已经跨phase保持。

唯一owner推荐 `INFER-PD-DISAGGREGATION`，[Ch55](../../../../../books/part-05-inference-system/55-pd-disaggregation.md)现42–56行已有phase-specific precision→Decode-compatible layout，但未表达**学习后的prefiller/decoder参数pair及cache生成路径身份**；不能用layout相同授权同token history任意cache rebuild。拟在现precision policy分支补format-only vs learned pair及多轮未证边界；Ch49仍解释低精度kernel成本，Ch54接双artifact流式buffer预算。**Queue：窄提案；未写Books；不采用所有模型、batch、multi-turn加速/质量保证。**

### 4.7 WeightBridge：loader可提供映射，但不拥有publication保证

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25442v1)，实际§3.1–3.3、§4.1/4.2/4.6、§5；7分深入。以canonical checkpoint元素索引探测backend `load_weights`，通过diff2压缩slice/transpose source maps，再三阶段receive/external-exchange/internal-exchange去复制域冗余，轮式双buffer融合pack/assembly。依赖same-dtype value-preserving loader、匹配trainer/rollout参数精度及固定worker plan；下界只是egress/ingress traffic，在饱和带宽下可逼近，不消灭control/pipeline成本。SS/RS staging与同一步poll协调不等epoch原子提交/失败恢复。H10080GB、8GPU/node、NVLink+32×100Gb/s NIC、BF16/Megatron/SGLang/Miles四MoE配置证据的AGST和EWTT不同；较大规模距下界更远，AGST倍数不能代训练吞吐或新policy质量。

实际owner `TRAIN-DISTRIBUTED-TRAINING`，Ch36“通信对象从无类型字节演进为有版本训练状态”已讲canonical stream+receiver-native slicing/fusion以及partial-load poison，并非缺发布职责。真增量是**从loader自动抽取布局映射→按复制域去冗余的传输计划**，与后面的publication/poison contract并列，不能用优化plan替代后者。拟在canonical-loader论证中补该受限planning branch及固定拓扑/精度失配回退，Ch35接snapshot、Ch37接分片代数。**Queue：提案；未写Books，非作者复核未进行。**

### 4.8 OPD：扩大prompt集合不是独立于refresh的单调收益

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25048v1)，实际§3、§4、§5、§7；5分标准审阅。Qwen3-0.6B与两teacher，student top16上的reverse-KL/PPO surrogate；冻结轨迹仍重算teacher/student logprob，但prefix不随新student刷新。N=8/48/14080 prompt与M=1/10/110刷新快照的grid匹配14080轨迹、110更新，不匹配实现token数或训练时间。三数学数据集的143题×32次采样中，Frozen扩大breadth时平均accuracy下降，Fresh反向改善；该交互的question-paired CI仅针对固定训练出的模型，不代表training seed稳定性。两teacher复查中Qwen平均accuracy差的CI仍含0，JustRL正增益；parseability、平均accuracy与Pass32 coverage不是同一指标。

将已经生成的32K回答截断到16K再评价会改变赢家，但这不是重新执行两种native generation cap的matched训练/推理实验。Frozen在32K更高却耗用约1.8/1.7倍实现tokens；不能称同总compute下Frozen更好。局部gradient probe没有fresh–fresh参考，breadth、重复次数、prefix漂移的因果解释尚未识别。实际[Ch29](../../../../../books/part-04-training-system/29-sft.md)“Demonstration Schedule”及OPD紧邻段已经把repetition当sampling policy、将总token预算与held-out迁移/记忆分账，并要求rollout policy、teacher/tokenizer和refresh cadence绑定。新受控交互有信息价值，但本证据没有足够稳定机制或跨条件选择规则来更新该长期处置。**拟Disposition：仅报告，不称无贡献或仅主题相同；保留Frozen/Periodic/Fresh各自成立的成本与分布条件。待root非作者审阅该窄裁决。**

### 4.9 Length grouping：batch平均改变每token的objective权重

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25890v1)，实际§2–5；5分，由Ch28具体objective缺口触发必要深入。length grouping同时改变batch成员、batch顺序、token保留/容量利用率和每batch有效target数量，不能把四者都叫curriculum。batch-mean CE给每target系数`1/N_B`；固定参考常数Z的token-balanced diagnostic改成`1/Z`，这是一项objective-scale干预，不是AdamW参数更新幅度直接按`N_B/Z`缩放。固定batch membership/targets的12-epoch比较把order分离；首epochgrouping在Mimi有小PPL收益，但token-balanced干预使该收益消失。持续长短排序/持续grouping均有退步，另外两speech tokenizer没有同收益。12.6%→55.8%是固定容量利用率，不是true retained-token ratio。

受限证据为87M AR Transformer、LibriSpeech train-clean-100、257stored/256target chunks、batch64、AdamW、8配对初始化seed；main early stopping仅匹配max预算，实际执行updates不同，fixed-batch实验才全3324updates。`rho_pre`用stored长度，是diagnostic，不是训练时精确target系数，也不证明自然语言大模型存在同量级收益。已实际对读[Ch28](../../../../../books/part-04-training-system/28-pretraining.md)NTP/有效token定义与token-loss例、mean-CE诊断、training data contract：现正文尚未表达**variable valid-target batch下batch mean与全局token mean的权重不同，长度调度会改objective而不只是padding**。拟在loss聚合→PPL交接处补这一数学责任，再用grouping/ordering拆分实验作受限证据；Ch35负责分布式归一化实现，Ch27负责数据mix。固定token batch/明确accumulation语义时原平均CE仍正确，不能默认固定Z普遍更优。**Queue：窄提案，未写Books，需非作者source/actual-owner核验。**

### 4.10 Serving stack：未dispatch不能当作模型不会调用工具

来源：[exact-v1 HTML](https://arxiv.org/html/2609.26693v1)，实际§2–6；6分评价有效性深入。同`tools=`请求先由server检查template/capabilities，再render和parse；Ollama0.30.8的部分model tags在dispatch前HTTP400，而研究harness将结构化transport错误压成普通assistant error string，下游会误认模型non-call。native/native+固定hint/text-tools三条件分离channel与prompt，Llama的text-only退步又反证uniform协议不普遍公平。protocol fidelity只按实际produced turns，non-response另报；system task-success仍需固定task分母，不能用条件fidelity掩盖无交付。Qwen0.5B的一个41turn loop让pooled85%而episode平均34%，repeat valid call并不是进度。

实验仅固定两个coding任务及6道HumanEval sanity-check、小样本task-instance seeds，解码T1/top-p1且未固定RNG；CPU GGUF/Q4_K_M与vLLM T4、SGLang A800 upstream checkpoints不是完全同权重跨栈，后者只查两模型default行为。语法强制可让单步8/8valid却产生600–900turn不终止，未完成的agent condition不能当成功率。版本/launch flags会改gate名单，本文不证明全部模型或harness都有该bug。

实际[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Protocol adapter”已声明serialization/retry/stop改变subject，“Response Rate”已分条件质量/无条件交付，因此不新起一套原则。窄缺口是**请求before-dispatch rejection→transport/error identity保存→produced-turn protocol分母与task交付分母分开；pooled turn受loop长度权重扭曲**。拟接adapter论证，失败层保持typed reason，不能string error吞成model行为；Ch78负责parser/stop实际执行。**Queue：窄提案；未写Books；硬件/版本声明来自作者，未复现。**

### 4.11 PatchKV：先决定修复/复用集合，再量化剩余状态

来源：[exact-v1 HTML](https://arxiv.org/html/2609.26219v1)，实际§IV–VI；6分Ch45实际gap深入。针对两次context版本的aligned suffix，离线paired exact prefill校准length-conditioned high-quantile dirty window；stored attention只给dirty外非局部候选排序，二者union再block-round冻结repair set R。R精确重算，complement F恢复旧state；attention不是validity test，near-edit不允许被importance ranking漏掉。F各block已有冻结FP16/K8V8/K8V4 tag，fused restore只旋转shifted K，V不旋转，destination mapping必须覆盖位置/页改变。所谓精确重算R并不使整个F变成exact-equivalent cache。

实际PyTorch2.7/Transformers5.3/Accelerate1.14研究prototype，单server8×A800/CPU DRAM offload，Qwen3-32B/GLM4-9B/Llama3.3-70B、三edited QA、calibration分离。mean resume TTFT从repair execution开始，排除plan construction及think-time/profile/quant-store；省TTFT不能吞掉offline成本或外推并发tail/SLO。dirty-window收益CI含0；attention/precision较大不是单调质量更高，32token blocks对某些任务有成本与质量取舍。新context已summary丢证据时保留旧KV反而F1超过full-prefix reference，这不是对新token历史的状态等价证明。

实际[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“任意Chunk复用”已有position/conditioning seam、probe修复与fallback；窄增量是**invalidation/drift、importance与precision三种决定分权，先冻结R/F再对F做mixed precision transport**，不是把CacheBlend全当新发明。拟嵌该近似分支，保留full revised prefill在不可校准、变更模式漂移或高风险时成立；CPU/offload metadata和page placement成本由本owner接Ch54。**Queue：提案；未写Books，不采用全面无损、所有time尺度TTFT或生产收益。**

### 4.12 MemoryAthena：生成表示只能有条件修正直接读取

来源：[exact-v1 HTML](https://arxiv.org/html/2609.25853v1)，实际§3–5/Alg1/主要Table1–3。6分实际model读取职责gap深入。E为直接Engram memory残差，GE从检索cue生成latent，GH从memory-disabled causal backbone的另一次pass生成latent；不是三个独立语言模型。先学memory/interface，再冻结backbone、memory/generators/readers，只训练router对observed future-token loglikelihood相对E的增量；future target仅训练使用。推理current-state特征预测advantage/confidence，超过门槛选择一个生成候选，通过bounded interpolation修正E，拒绝仅在该injection site exact返回E残差，**不等事实真值或整model输出安全保证**。

主要Mistral7B及Llama2-7B接口迁移、五QA/六分类。shared checkpoint对照证明GE/GH并不一致胜E，ordinary soft fusion明显退步；from-scratch略优于pretrained memory，不能全因果归旧Engram知识。Yahoo特设tau1仍稍低于E，其余tau0，不是无调参统一rule；mixed F1+MC平均不是同单位truth。gold-label oracle优于部署router只是事后headroom，不可在线使用；router贡献weight不是独占route token比。定点补读Appendix B/C.3/M：每个endpoint全path强制同来源，future-advantage不能因果分摊某层；confidence的soft label来自advantage，不是校准correctness概率。GPT2四scale、单MI250X、BF16、338input/16output、1warmup/3measured的独立microbenchmark中E-only始终更快、reserved memory更小，不是Mistral下游QA的latency。小router参数数目也不代表完整167M reader/generator或多endpoint监督成本小；独立训练seed不确定性仍未据本次必要段确认，不能补造生产SLO。

实际[Ch22](../../../../../books/part-02-model/22-long-context.md)“容量必须同时声明计算、状态与读取合同”已有retrieval/状态读取的角色，但没有**addressable direct residual作明确reference，生成latent候选与router目标冻结分开、拒绝精确返回reference而非无条件soft fusion**这一model层条件分支。拟在读取机制解释内接到lookup memory/learned representation的共存，而不是Agent长期记忆Ch77或RAG文本证据store；Ch21只接条件计算选择，Ch45才拥有persistent cache。**Queue：窄提案；未写Books；目标likelihood不是correctness oracle，门槛/额外pass/任务迁移仍有代价。**

### 4.13 当前普通工作（替代旧暂停停点）

原29+新增5必要审阅与最终处置已完成，34为29实际整合/2已有覆盖/2仅报告/1争议；29处实际正文与邻接已由sep21非作者写后PASS。新增六New完整题摘已独立准入，root source→actual-owner及六处实写/邻接写后也全PASS；40冻结家族合计35I/2E/2Only/1D，只待§4.24日级独立Gate。TopoCross日期与ReDraftv3事件具体隔离已校准，不评分/采用，不扩scope。较早各§Queue/停点是过程，不覆盖本最新状态；普通待办不得改叫外部隔离。不启动下一日，不动共享索引/LearningState。

### 4.14 2026-09-30 三项已有证据的作者裁决

仅复用上述身份、精确版本、必要证据位置和反证均未变化的结果；本轮重新实读当前 owner 正文，尚待 root 非作者裁决，不自行签 Gate。

- **2609.26173v1：标准完成，拟已有覆盖，`INFER-TENSORRT-LLM`。** 当前 Ch49「二阶敏感度把 Output Gradient 带进量化 Artifact」实句已区分输入统计与输出损失敏感度，绑定 calibration objective／gradient／bit map；「输出分布也可以反过来指导离线精度分配」以单层扰动与 softmax reference 分配精度，并明确 logit SQNR 与分布距离非同对象、排序只是 proposal、最终行为与实际 kernel 各自验收。故本篇 reconstruction 排名与最终任务敏感度不一致的采用命题已有实际承载。其 V 常占主导的局部结果有报告价值，却没有全 mixed-bit 配置验证，不把 V+1 bit 变成新默认规则；不改书。当前锚点 Ch49:952–955、1059–1076；已读官方v1 §III–V的单projection RTN/GPTQ、九个1.3–8B模型、WikiText校准16K/test1K；未证明跨projection mixed-bit配置或V+1默认。后续sep21已核必要源与actual覆盖通过，维持已有覆盖。
- **2609.26779v1：标准完成，拟仅报告。** 当前 Ch75:302–308 已区分最近 live view 与可恢复原文，Ch75:368–373 的可寻址 eviction 与 Ch75:597–603 的 trace archive 又分别声明存储／回读代价。本文真实 flat-drop 不保旧 compaction，也不保证从 archive 召回；可作为低存储、可接受长期 recall 丢失的受限运行事实，不能借 tool rerun 恢复动态内容或外部 effect。SWE／KernelBench 的协议与成本排序不同、8K 有退步，没有形成可跨任务选择 flat-drop 的稳定门槛或新的 commit／恢复机制；因此不以主题相似判 Existing，也不为新名称增加书稿分支。保留其具体方法与负面结果，待将来出现同身份历史召回／动态 effect 的受控选择证据时定点重开。
- **2609.26086v1：标准必要证据已读，拟 Ch76 窄 gap 深入／整合，实际未写。** 当前 Ch76:1071–1077 由独立 sufficiency gate 决定继续／回答／abstain，却未解释 gate 自身昂贵时的单侧调用路由：便宜 coverage margin 只在明显未覆盖时暂缓 expensive decider、继续搜索；其余情形仍调用原 decider，不能从 embedding margin 直接授权停止。预算耗尽另报 budget exit，不冒充已证据充分。拟接现 Evidence Gap 成立条件之后两段，保留固定 top-k／直接每步 decider 的回退；增加 margin 训练、分布漂移、误暂缓造成冗余搜索等成本。采用只限角色分权与单侧 defer，不采用摘要倍率、全 Agent latency 或 truth 校准保证；因此不需为数字另开 §5.5／AppC。已读官方v1 §3/4/5.1–5.2/7：single-seed13、LODO代理agreement、固定topK、每步原decider成本与一goldpoint校准限制保留；后来已获独立source→owner及Ch76真实两段写后PASS；明确实际知识缺口后最低完成深度提升为受影响内容深入，评分仍 2+1+2=5，不倒推加分。

至此17普通项中3项完成作者单篇裁决，仍有14必要审阅；首批12与本3的非作者准入／采用、11原Books提案及 CoVeR 实写均仍是普通待办。有限题名查漏未结束，分母仍未冻结。旧38向09/22迁移由 `sep22_resume_v3` 独占协调，本日不重复改变其证据或 Books。

### 4.15 2026-09-30 安全／评价题名查漏第一组

本组仅沿已有库存中的五个具体题名线索回官方完整题摘和版本历史，不以正则或章节映射准入，不扩全666摘要。`25938`／`25808` 的 exact-v1 abs 网页缓存 miss 后用官方无版本 abs 恢复，当前均只 v1；访问失败不记无命中。五项均为原附录合同分类 New，公告日期沿用 §1 Wed23 联合依据；投稿字段本轮已见但不冒充公开时间。官方事件页未见撤回／纠错标记，仍须非作者准入校准。

| 精确身份与官方标题 | 具体增量与作者初裁 | 初评与下一步 |
| --- | --- | --- |
| [2609.26048v1 FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](https://arxiv.org/abs/2609.26048v1) | 能完成一次不等稳定交付→由 observed failure 注册 eligibility／runtime trigger／bounded instruction or denial，再以 timing-matched sham 和静默项拆开内容与打断的贡献→需要重验 harness 的交付规则，而非泛化“多反思更可靠” | 2+2+2=6；拟准入，§3–5必要方法／五臂设计已读；主要对照 p=.061、能力缺口与程序遵守不充分，不引用摘要普遍可靠保证；owner 待实际 Ch81／84 比较 |
| [2609.25938v1 Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL](https://arxiv.org/abs/2609.25938) | conformal 风险是校准label-relative→预注册替换执行数据库与专家盲核使风险／AUROC产生不同排序，suite也双向错→score构造oracle不得自己认证semantic truth | 2+2+2=6；拟准入，Ch66必要原方法／oracle反证待审，非仅SQL任务新benchmark |
| [2609.25808v1 Auditing Proxy-Based Validation Across Text Spans](https://arxiv.org/abs/2609.25808) | score与proxy共享文本span可能共用表面信号→改变边界／opening-template与matched-volume删除、off-span重读区分proxyagreement与construct→评估合同需要声明两者span与独立构念 | 2+2+2=6；拟准入，Ch66评价有效性必要审阅；不因63页遍历全部外部合同 |
| [2609.25721v1 Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages](https://arxiv.org/abs/2609.25721v1) | 单代数字蒸馏不能界定跨代遗留→固定Qwen三lineage×十代中系统prompt移除使关键词表达为0，而activation direction／base steering仍不同→停止可见表达不能独自认证trait清除 | 2+2+2=6；拟准入，可能与Ch29既有subliminal缓解依赖，必要probe／steering限制待审；不把probe直接叫内部trait真值 |
| [2609.26025v1 MICRO: Multi-Fidelity Active Search for Severe Error Discovery](https://arxiv.org/abs/2609.26025v1) | 高成本severity确认与低成本rating分离→joint conditional model+impact clustering+rollout将共享annotation预算投向confirmed severe errors→便宜rating只拥有acquisition而不是最终严重错误label | 2+1+2=5；拟准入，必要方法与WMT20回放成本／oracle边界待审；不把传统翻译任务局部结果外推foundation模型或线上风险率 |

此时拟准入为原29+新增5=34，分母仍未冻；新增五项仅题摘准入不等Evidence完成，FIRE已读局部也不自动Books通过。

### 4.16 三项新增必要审阅（作者裁决，未独立通过）

**[2609.25482v1 Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining](https://arxiv.org/html/2609.25482v1)**：原5分不变，实际 Ch28:648–663 有 schedule／base checkpoint×SFT update scale，但缺训练终态 estimator 与 terminal schedule 的联合选择，故受影响内容深入。已读 §3.1 定义／局部二次 risk 身份和 §4.1–4.5／Limitations；TSA只在训练结束把 raw final iterate 与 recent checkpoint mean 插值，不反向改变 live optimizer。局部 PSD quadratic 下 lag／noise协方差决定最佳插值，不能推为任意非凸训练定律。五个 paired data-order streams 的 schedule×estimator 比较含 pure AdamW 复查；depth22 三seed是 combined recipe，不能单独归因TSA，CORE只1/3达到qualification，训练时间差作者解释为allocation吞吐波动。额外 checkpoint memory、K／spacing／coefficient调参和权重组合验收不可省。拟 `TRAIN-PRETRAINING` 整合两窄段接 schedule 说明之后、SFT适配讨论之前：trajectory与returned weights分权→固定预算同时比较 cooldown×estimator，部署组合不等可原样resume训练，Ch35仍拥有恢复状态。保 raw endpoint／常规decay在预算紧、checkpoint不兼容或验证失败时成立；不采用record加速和统一最优alpha。

**[2609.26621v1 Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference](https://arxiv.org/pdf/2609.26621v1)**：6分，主官方PDF缓存miss／HTML404后从同一官方PDF直读内存成功，42页；仅实际读取pp2–8、11–15必要方法／配置／反证，不称全42页。native top-two logit margin触发head-only FP32重算，gating与scope分开，拓宽至RMSNorm／body可反退；unique-max directional flip代数条件可核，但RMS与Jacobian估计是经验heuristic，不把「head dominates」或「hidden相同 iff output相同」当全模型定理。FP32将低位存储cast不能恢复已截断权重；同一dtype内重复可一致，不代表跨dtype replay。主A10G、TinyLlama/GSM8K/HumanEval/MBPP、max256、greedy；不同架构／batch／kernel扩查不在同一共同统计分母。小batch门控成本、batch≥8和end-to-end FP8近无修复、Qwen跨硬件不同收益均限定该经验分支，prediction精度稳定性只是hypothesis。当前 Ch49:770–776 拥有output projection全词表／近似MIPS，Ch49:933–944 已拥有逐例一致性但没有**以小margin选择FP32 head、精度修复范围不单调**的执行机制。拟 `INFER-TENSORRT-LLM` 两窄段接output projection后／ExactTopK前，保完整既定precision plan或更高精度重新验收，不把margin写truth/safety门槛；Ch20仍拥有argmax／tie semantics。必要gap已明确，实际最低深度为受影响内容深入，尚未写Books。

**[2609.26763v1 SARA: SLO-Aware Resource Allocation for Disaggregated Agentic LLM Services](https://arxiv.org/html/2609.26763v1)**：5分，已实际读 §III-D/E／IV-A/B/C／VI-D／VII及AppendixB必要重尾近似。P、KV transfer、D各自建队列／容量模型，Kingman high-utilization、lognormal／exponential length、perfect overlap、moment matching均为条件；stage各达p不推出joint request达p，TTFT式只计prefill，另列transfer。末端allocation实数微分条件也不直接证明整数资源全局最优。**printed §VI-D “non-increasing therefore unique global optimum”推导争议需隔离**：单调非增不蕴含凸性或唯一性；甚至线性两阶段cost在固定总latency约束下可全线段同值，违反该理由的一般唯一结论。Eq58最多是满足光滑条件的驻点必要条件；不得作为普遍planning保证。VII SGLang/A100配本地量测和simulation，七日Azure replay／hourly重配不是原生产SLO；极限tail误差增加、紧预算175B colocation有胜例、exhaustive往往更高，作者未充分披露完整runtimeversion／并发identity，不补造。当前Ch56:894–921 已有versioned primitive+iteration/queue模型→PD两侧service rate与transfer→silicon validation/fallback，Ch56:120–124已有quantile与uncertainty policy。拟**暂缓中心最优保证**，保有限模型结果在报告，不据其一般唯一／joint-SLO宣传新增Books。重开仅需实际可行域／convexity与整数处理的证明或可比counterexample修正，不重扫网络／全部附录；由root裁决是否收窄为Only，而非作者自行用标签隐藏争议。

原29现在18个作者单篇裁决、11普通待必要证据；§4.15新增5仍待必要审阅，34分母未冻结。全体非作者采用／最终Gate及必要实际Books仍普通未完。

### 4.17 记忆失效、闭环写入与专家预算的有限作者裁决

- **25130v1 Impact Is Not Invalidation: Ask About the Claim, Not the Diff**：[exact-v1](https://arxiv.org/html/2609.25130v1)，6分。已读§II–VI及必要Appendix A问法身份；Ch77:1255–1278已有dependency tracing后独立support与选择性replay，缺的是**影响可达性/整份diff行为变化与某条claim不再成立是不同谓词**，不是泛化“独立验证”。§III恢复parent assertion在child执行，排除测试diff与无verdict，10次确定执行；CI-gated未改test的naive正类为空是该构造的范围条件，不推到所有仓库。§V同claim+diff但保持行为问法的A5C几乎不改善，改变问法才有差异；claim-relative仍漏失效，testmon更低陈旧但更多复验，两者无全面dominance。采用精确assertion/commit/环境身份与claim级复验proposal；保自然低base-rate后precision显著下降、Python小库/正例集中、post-cutoff仅22positive且repository混杂、prose反退、没有实际memory部署。正文§V-A的244/61与TableII604/151、§V-H paraphrase175与430/450等分母不一致，不采用这些争议数量或显著性为保证。拟Ch77选择性repair之后窄两段，原dependency tracing、全复验/人工fallback保留；知识缺口触发必要深入，待root source→actual owner与锁。

- **25052v1 Self-Cleaning and Captured Anyway: One Measured Primitive for Error in a Store an Agent Writes to Itself, and What a Falling Score Actually Measures**：[exact-v1](https://arxiv.org/html/2609.25052v1)，5分。实际§3 apparatus、§4.2/4.3、§5.2、AppK gate及AppQ自校正的必要边界。采用的是**同模型从自己append-only历史读取并写回时，只有与已取回多数一致才允许写入的gate，会拒绝纠正少数而固化已有false多数；低污染与高污染的方向不同**。Ch77:292–307已经讲读取entry多数≠independent evidence，542–546讲自判/摘要反馈污染，但没有该write-side admission的受限反例；拟在Entry Majority末补两段，不把读取聚合与写入过滤混成同机制。单topic、单数字corruption、k8/150step、五模型起初三seed是合成条件，AppK/重采样显示跨模型collapse不是五个独立确认；私有artifact不称独立重现。保强gate、多factor、typed-role并未被反证；均匀无放回检索（k8）/ranked retrieval边界和真实先验改变copy概率；二峰/早决时钟缺机制，1/n不能解释已观察时钟，不采用广泛吸引域/非单调全局理论、永久能力保持或普遍“更保守越坏”。append-only仍保存truth不等reader有能力正确使用，pass@8不能当部署可靠性。必要deep仅上述gate反例，其他未决不扩大附件；后来已按窄整合落实并通过非作者写后；不存在uniform-with-replacement采用。

- **25809v1 You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs**：[exact-v1](https://arxiv.org/html/2609.25809v1)，5分。已读§3–7与AppB对照缺陷；Ch21:553–575已有variable-k预算与层/token分配，但缺**先测固定降低k的质量曲线，再按不同预算区间（conservative/aggressive）判逐token动态分配额外价值，并区分likelihood QA与完整generation**这组实测选择边界。§3 shared experts不删、retained权重归一化；§5 threshold不是预算，QA/generation分别校准actual平均expert并允许10%overspend，best-of-four指四种动态规则（Naee relative-weight、DynRoute cumulative-mass、DiEP similarity、Ban calibratedlayer/token）由同suite均值择优，不叫严格完全compute match。§4/6九架构uniform sweep、四core动态规则，VL对照任务模态与判分也不同，不能把差异唯一归因于模态/规模/post-training；Table2固定k吞吐不属于动态方法，batch4/1024prompt/256output、硬件精度版本并未在必要正文披露，不采普遍加速倍率。AppB保留重复Fixed-K较低值会使dynamic相对优势更有利，其文字解释相反；因此不采用+0.06/+2.26精确优势或稳定显著性，只保局部预算曲线/质量反退与必须公平重测的机制边界。拟Ch21 variable-k受限评价后窄两段，固定native top-k与uniform reduced-k共存，知识缺口必要deep，此处原提案后来已按非作者纠正落实到Ch21，两段写后PASS；conservative/aggressive不是margin规则。

当前原29项作者必要审阅21，仍8项普通必要审阅；另§4.15五项准入/必要证据尚待独立校准，34工作池未冻结。以上均没有实际Books写入，不是独立通过；访问失败与未做普通项不改成外部隔离。

### 4.18 两项机器人必要审阅（作者裁决）

- **26467v1 RouteRLT: Learning When and Which RL Specialist Should Control a Vision–Language–Action Policy**：[exact-v1](https://arxiv.org/html/2609.26467v1)，6分。实际§III-A–E/Alg1、§IV-A/B、§V；Ch26:203–207已采用frozen VLA compact RL token+局部actor-critic与人工critical-phase handoff，真实缺口是**从训练期privileged phase label学causal latent selector，hysteresis/dwell稳定器独立于chunk horizon；切换立即废弃未执行suffix，以同一观测fresh VLA reference重提incoming specialist，仅executed action进入replay**。不是泛“MoE切换”，也不重新解释已提交动作可回滚。拟在原Online RL接口两段后补窄两段，低层安全controller仍保提交权。证据限SmolVLA、LIBERO三任务60heldout/三训练seed和Trossen一connector/port；真机仍operator alignment后开始insertion，30/30/20trials不能声称完全自主multi-specialist。privileged训/learned部署存在entry-state shift，phase单项success不能相乘得composedsuccess；router每步/五步query、额外latent/reference与replan成本，硬件精度与服务SLO Not Disclosed。不采普遍保能力、零handoff风险，fixed/manual handoff和frozen generalist共存。知识缺口必要深入完成，待root source→actual owner和窄锁。

- **26292v1 RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?**：[exact-v1](https://arxiv.org/html/2609.26292v1)，5分标准必要完成，作者拟**已有覆盖：MULTIMODAL-EMBODIED-VLA Ch26:522–532及574–586**。实际§2.1–2.4、§4.1–4.4、AppA/B范围，采用视觉/场景robustness不认证mass/friction/contact等物理轴、必须在任务可行条件中闭环验证；现正文明确这些不同domain-gap因素、未建模物理与独立sim/controller评价，RedVLA支路已经要求task-feasible risk配置和完整violation分母。不是仅按“机器人评价”主题判E。新增13参数/continuous range/每episode固定seed的suite与5k示教不单独改变长期解释；参数还包括camera/geometry并非纯不可见动力学，expert-planner成功过滤产生conditional feasible population，不证明覆盖全真实分布。§4 Clean/Official Random为引用既有public结果，Physical Random作者重跑且同时保visual随机；未披露匹配runtime/checkpoint/seed/不确定性，故不采用下降百分比为独立因果或“所有WAM/VLA不懂物理”的结论。保独立轴可实验的协议，不冒称该论文已做physics-only完整因子隔离；没有训练或真机修复对照，不新增Books diff。待root有限E终裁。

续跑停点：原29作者必要审阅23、余6：25611 Qwen3.8-Omni、25949 FluxOCS、25770 Reading Right Answering Wrong、26425v2 Quantized World-Model Cache、26513v2 Virtual Encoders、26774 StableVQ。新增5题摘准入仍待非作者校准，工作池34未冻；共享Books尚未写入。旧38证据已由09/22 owner实际迁入[真实日报](../../22/README.md)，保留年级旧附件供跨日复用，本日报随后移除错窗旧表/正文，不再等待迁移。

### 4.19 三项视觉表示必要审阅（作者提案，未写）

- **25770v1 Reading Right, Answering Wrong: How Visual Configuration Changes Affect Evidence Use in VLMs**：[exact-v1](https://arxiv.org/html/2609.25770v1)，5分。实际§3.1–3.3/§4.1–4.5；Ch23:63–65已经分可恢复/可访问/可表达，但尚没有**动态tile/grid的离散边界使相邻一像素改变完整visual configuration；同pixels变配置与同配置变pixels的成对控制，回答稳定不等accuracy改善**。拟在原三能力diagnostic两段后窄两段，采用preprocess配置身份和边界回归，不把resize现象唯一归因于encoder或数据内容。LLaVA-NeXT target-knockout减去同view相同数量non-target对照，支持这个模型的访问依赖改变，不证明所有model统一因果机制；Zc(I)固定后guided reading可恢复也不是原任务自主能力。七checkpoint四bench、greedy96token、source-cluster bootstrap但unadjusted多比较；InternVL样本小，fixedLow/High均让Qwenaccuracy略退。97.2%=173/178 readable且累计多条件/annotation-assisted record/excerpt选择，分母不是全部300、更不是单一部署procedure，引用cue不能替代用户未知target选择。增加tokens/标注/多次调用成本，原native preprocessing和完整原图/原文回读fallback保留。知识缺口必要deep，待root锁。

- **26513v2 Virtual Encoders in Multimodal Transformers**：[exact-v2](https://arxiv.org/html/2609.26513v2)，5分。当前版本§3、§4.1–4.4、§6；不为版本号做旧版diff。Ch23 native段87–92已有joint training而没有**没有专用continuous encoder并不意味着没有感知计算，它可在backbone内部形成；形成/被后续读取/跨模态路由要分别实测**。拟native训练分支之后窄两段，只采用functional regime，不创建新模块owner或声称某层完整encoder替代。31concept×40image/40audio、3:1probe split；meanpool+linearprobe/CKA只能诊断可读/几何，不直接真值。Gemma4/Chameleon单层modality residual Gaussian corruption、alive yes/no特定task和强度sweep支持局部necessary readout，未做activationpatching sufficiency，不能推出删token/停算安全；其他模型只有部分probe相似。PCA“language subspace”操作定义、未直接干预rotation，audio alignment/decodability只相关；边界不是所有多模态任务的共同层号。保dedicated encoder+projector资产复用、完整视觉读路径fallback；知识缺口必要deep，待root采用/窄锁。

- **26774v1 StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training**：[exact-v1](https://arxiv.org/html/2609.26774v1)，6分。§3.1/3.2、§4.1–4.4 Eq4–7、§5.1/5.2 Table1–4必要；Ch23“离散表示”130–135讲collapse/axis但未解释**encoder的STE reconstruction/commitment与codebook追踪是不同目标：相对assignment distance stopgrad缩STE、window-active FIFO后向near inactive传播targets、encoder/decoder warmup anneal与codebook constant高LR分别调度**。拟离散表示开头后窄两段，不按三技术名称堆砌；shared projection使inactive受间接影响≠每个原code独立梯度都非零，RegionVQ明确recent-active/unclaimed inactive self-target零loss，故不采用“每个code得到meaningfultarget/fullutil直接保证”。Eq4同code最匹配距离为零时分母/零权重边界未披露数值guard，也不当threshold-free全稳定实现证明。ImageNet256、256tokens VQGAN、linear/ViT projector与不同epochs/大型baseline非全预算match；Table3Region-only NaN、Dynamic-only低usage，组件必须条件组合而非各独立全解决；Table2生成Precision/IS也反退，100%usage不是语义quality或通用音频视频安全。pilotfreeze分开查机制，FIFO/nearestinactive search及分组优化成本需验收，代码未验证。保普通VQ/EMA-reset/continuous feature和统一optimizer简化分支，必要deep完成，printed广泛保证不采用，待root定点有限判。

### 4.20 原批次末三项必要审阅（作者提案，未写）

- **25611v1 Qwen3.8-Omni: Towards Native Omni-Modal Agents**：[exact-v1](https://arxiv.org/html/2609.25611v1)，6分。§2–5、§6.1.4/6.2、§7.1–7.4已必要读；原先精确匹配 `LiveHarness` 未找到不证明正文没有，官方§7.3明确为 `Qwen-Live-Harness`，现纠正。Ch84:554–568已有observation/action clock分离、918–938有后台event log，但未具体承载**spoken response/playback、foreground call与delegated task三种寿命分别取消：打断语音不自动取消已委派执行，结束实时call也不等任务终止；ack仅受理不是effect完成，异步结果须另回送**。拟在Observation Interface末后窄两段；仅采用公开生命周期分离，不补造durable/task权限继承、exactly-once或安全通知协议。独立监控session产生text事件、cooldown和连续positive suppression只是节流，不是真值/可靠探测。Table9仅10个有效响应/条件、一次warmup，6/12/20s预上传输入、VAD关、freshsession；TTFC从显式commit起排除上传/建连/playback，RTF还排除初始等待，不能称持续双向实时P99或完整用户延迟。Table10/11有VoiceBench/WildSpeech等反退；co-training与encoder阶段未隔离单一因果，S2约2.5T与分项合计2.6T不采用精确预算，多个benchmark使用不同harness不混并。FOA空间AuT是报告中的表示事实，但本次不借同篇再造第二owner diff；必要deep完成，待非作者actual-owner裁决。

- **25949v1 Flux: Optimal Scheduling of Optical Circuit Switches for LLM Training**：[exact-v1](https://arxiv.org/html/2609.25949v1)，6分。实际§3 Eq1–5、§4完整方法/评价/限制；Ch36:1630–1638已有TopologyRevision与互斥CP/EP光路复用，§训练DAG已有dependency windows，拟新增差异须被非作者核而不是同题自动入书。候选窄差异是**整个iteration的P2P+compute DAG联合定starttime/switch：同端点电路可延续、计算依赖允许隐藏重配；aggregate traffic丢失ready约束、最少重配次数不等最短makespan**。拟现可重构Fabric两段后窄两段，不采用任意训练最优/线上收益。Gurobi仅对所写atomic-message/knownduration/DAG约束模型最优，求解最坏指数与GPU/layer扩张成本；data-dependent MoE违背完整先验。ASTRA-sim/8GPU/两800Gbps链路/A100 roofline、假设无限片内NICbuffer为上界模拟，τ=1us–1ms不是实硬件，Rotor在低τ有竞争性。模型/profile漂移保静态/反应式collective；实际覆盖不足才写，待非作者校核。

- **26425v2 QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation**：[exact-v2](https://arxiv.org/html/2609.26425v2)，6分。§3、§4.1/4.2、§5.1–5.5必要读；Ch45:1239已有attention-aware量化、1430–1431已有anchor/residual分层，但未具体解释**过去query的secondmoment限制未来attention误差：query-weighted centroid/residual选择与储存K误差在query主子空间的logit补偿两种责任分开**。拟anchor/residual后窄两段，projection基U以BF16、C=EU实现INT8保存，不称所有残差精确修复或未来query必在过去子空间。diag近似、white/uniform residual假设、top8rank、统计/eigensolve/候选比较和额外低rank matmul成本；漂移时重校准/提高精度/FullKV。五video模型A80080GB、93frames480/720p；KIVI的recentBF16与group32和本法group64不同，非完全memory预算match。PSNR/SSIM/LPIPS对同模型BF16结果只测数值近似，VBench总分可漏局部flicker，也非闭环行动正确；K-only劣于V-only并非所有模型，HY aesthetic略退。Table5两组件消融仅HY；Table6 LingBot/HY latency反增约5–6%，LongCat反降，KV6.2×不等全系统memory/普适throughput或SLO。必要deep完成，待非作者actual-owner。

### 4.21 新增五项必要原文→实际owner的有限作者提案

以下五项均已获sep21完整题摘准入初核；本段实际必要审阅完成，不代表非作者采用/写后或日Gate。均因明确长期差额定点深入，分数不因投入而上调；尚未获新五项Books写锁。

- **26048v1 FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents**：[exact-v1](https://arxiv.org/html/2609.26048v1)，2+2+2=6。实际§3–6及Limitations。Policy把task eligibility、history触发、动作/否决、release和nudge limit分开；frozen panel同时保存risky state→firing→目标行为→独立verifier outcome。timing-matched sham帮助检验仅打断/提醒的效应，但deny条件的sham仍只有instruct、不真的deny，不能宣称所有action权完全匹配。14eligible/16silent任务、5arms×2attempt，silent更容易，interaction不作因果结论；real-vs-sham差额CI与p=.061不支持已确定普遍显著。行为分析排除4个枚举/token任务，12/22完成目标行为也不等获得原缺能力；失败必须分procedural slip与capability deficit。full-suite排除不可安装任务、tier不同portfolio不能混池，providerroute非checkpointhash；专家策略时间未计，广触发策略成本增加。实际Ch84:949–981已有版本化harness、success-preserving gate和counterfactual advantage，不重复这些原则；拟在自适应Harness末/下一Sandbox标题前窄两段，新增**eligibility→trigger→behavior→verified outcome分母链与同一触发时点sham控制**，不得把观察到行为遵循当发布批准或一般可靠性。静态workflow/独立outcome gate与人审fallback保留；非作者可判差额不足则Existing。

- **25938v1 Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL**：[exact-v1](https://arxiv.org/html/2609.25938v1)，2+2+2=6。实际§3.1–3.7、§7.1–7.3、§8及必要pilot限制。固定50候选池下分别替换score partition oracle和calibration label oracle，不能把二者同源对齐当正确性验证。formal certificate是含abstain=0 loss的marginal risk，不是已回答样本selective risk；question-exchangeable随机split的证明不自动覆盖schema-disjoint split。offline reference参与union-find/ORDERBY flag与gold-free control分账；严格suite refinement也不保证semantic wrong单调减少。两checkpoint/seed101的expert audit同时覆盖accepted/rejected侧，不只AI挑出的拒绝；自己的弱/suite风险约10%可与expert约17–20%并存。200重叠resplits不等独立CI，四checkpoint仅两Qwenlineages；AI-only taxonomy不能当人工gold，部分trace缺失/外部泛化pilot未过原预注册crosslineage条件。actual Ch66:585–590已写risk只涵盖定义label，故新差额不是泛label-relative原则；拟Structured Prediction Set末、RepeatConformal前两段：**partition/threshold-calibration/evaluation三个oracle角色分别冻结，cross-oracle score控制+接受和拒绝两侧独立审计**。不采用reference defect普遍率、部署semantic risk certificate或唯一机制因果；标签不可靠时保独立执行/人工/abstain。

- **25808v1 Auditing Proxy-Based Validation Across Text Spans**：[exact-v1](https://arxiv.org/html/2609.25808v1)，2+2+2=6。实际§3.1–3.4、§4.1–4.4、§5.1–5.4及关键限制。冻结score/construct/task/judge，只让proxy同规则在score span的严格补集重读；full-output仍含共享前缀，不能作为disjoint control。off-span关联与construct内分层permutation null比较，不机械以.5为null；残余gap可含proxy失配、spillover和粗label未捕获变化，不识别唯一containment比例/因果。Hotpot边界sweep支持共享开头表面信号，但80char等equivalence不足必须Unknown；ORBench虽proxy高、construct近chance仍因大量ties拒绝categorical verdict，20contracts中13 undecidable不能叫全audit通过。特征消融只对已生成文本删除开头、保持labels，非重新生成/线上router修复；XSTest construct也下降，不能说修复普遍保真。TFIDF50char是诊断而非生产routing，judge human κ低/稀少positives与合成漏检均保。actual Ch66:565–576只有无标签rubric/judge相关与target leakage及不确定性，未给**score-span identity、严格补集proxy和observed construct分层null**具体控制。拟无标签比较末、conformal interval前窄两段，不把共享span本身当缺陷；同span correctness也有NO FLAG。新control增加标签/重读/检验成本，不足时保Unknown/独立construct标签，不授权安全发布。

- **25721v1 Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages**：[exact-v1](https://arxiv.org/html/2609.25721v1)，2+2+2=6。实际Methods、Experimental Setup、Results、Discussion及结论；正式题名已重新对官方exact-v1 abs核对。每代从同Qwen2.5-7B base重启、attention rank16 QLoRA，用前代经数字/标点格式过滤（自动无words）的carrier训练，filtered N随retention变化；三条partly selected transmitting chains十代不是population decay/floor规律，gen1–7幂律外推不采用。默认context有行为，empty system下gen10 0/60但已知teacher displacement projection仍正；在base中施加student-base方向可诱导行为，不等从student移除/恢复trait，也不证明方向对实际传递必要。probe是已知方向对齐而非内部trait真值，decoy也可正；28层择峰和强dose能引起明显退化，不当安全无损steering。screen计owl mention而非全部preference，少量人工audit不能补造全FN界；dependent generations/filtered size、其他adapter与base影响未隔离。actualCh29:386–428已讲context行为入权重，1003–1011已讲activation probe相关而非机制，未承载**跨代carrier filtering×runtime context×行为/projection/干预分别复核，某上下文表达消失不认证lineage清除**。拟ContextDistillation代价段后、OnPolicy coverage前窄两段；不采用恶意trait、异构model、永久floor或continual无restart泛化。显式数据/模型lineage与独立行为审计、停止传播/已核demonstration fallback保留。

- **26025v1 MICRO: Multi-Fidelity Active Search for Severe Error Discovery**：[exact-v1](https://arxiv.org/html/2609.26025v1)，2+1+2=5。实际§2–4、§5.1–5.3。Joint Gaussian用cheap rating与strong loss annotation更新相关posterior，但只有strong annotation确认超过校准90th-percentile severe threshold；cheap query即时confirmation reward=0，且须留至少一次确认预算。impact向量一阶近似probability变化并固定variance，在impact空间cluster/represelection后M128 rollouts只模拟future annotation，不是全multi-fidelity最优动态规划。WMT20 En-De/LaBSE PCA32冻结且doc-disjoint；1024 paired pools/128segments、B16/32与假定ρ成本，不是实测人力秒/完整wallclock成本；ρ=1/8某配置tie，ρ高无改善。active search发现严重条目数不是无偏总体严重率，MQMseverity不是任意事实真值。actualCh66:283–318已讲信息量case选择与重复预算/selection bias，窄差额是**便宜观察和强确认拥有不同证据权限，在同一预算交错而非把rating当confirmed failure，并按posterior impact而非文本相似性分候选**。拟Evidence Budget现AgentAssay两段后/下一标题前窄两段；posterior失配、真实成本未知或高风险时保随机audit/确定确认，不用廉价分数自动裁定发布。

### 4.22 七个已具名标题的有限准入校准（不是新查询池）

2026-09-30继续仅在原666库存中已具名七个题名打开完整官方摘要/当前history；不新搜、不按owner或关键词自动retain。六个身份在附录合同类含New，复用§1 Wed23官方组+公告时刻的联合依据；部分v1 Submitted August不是更早公开的证据。Topo只Cross，额外定点主分类cs.NI；当前recent已滚动，不包含该ID，monthly仅证实本月identity、不能单独证明哪天。下表保存作者初评；sep21随后独立完整题摘校准通过六New，Topo潜在贡献通过但日期隔离。已有覆盖也要进入candidate后必要证据判断，不能为保持34预定数而前关。

| 精确v1/题名 | 原约束→实际题摘增量→会改变的选择 | 初评分/日期与下一步 |
| --- | --- | --- |
| [2609.26718v1 The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718v1) | distant失败惯常归distance→近端task-irrelevant background累积竞争并用t-distributed directional relevance matching保position→需分别验proximal干扰与distance、再选检索分布整形而不是仅扩窗口 | 2+1+2=5；合同cs.LG New本批；拟准入，Ch22实际gap/关键对照必要核；不采用普遍quality或唯一内部因果 |
| [2609.26708v1 Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](https://arxiv.org/abs/2609.26708v1) | fixed-corpus QAD虽保短QA但长生成loop→student通过实际部署quantized forward rollout、fullprecision teacher在studentprefix指导+taskverifier，在matched-budget继续QAD对照→优化state distribution须含量化引入的轨迹偏离 | 2+2+2=6；cs.LG New本批；拟准入，Ch49量化训练或Ch29 OPD实际owner定点；不能从广泛短能力保留claim推全部能力 |
| [2609.26487v1 When Recursive Models Finish Computing](https://arxiv.org/abs/2609.26487v1) | nominalbudget失败不足判断永久失败→延长recurrence、局部trajectory方向收缩但Jacobian另有expanding方向和跨步扰动命运→停止sensor不能把全谱contractivity或latent motion直接当correctness | 2+1+2=5；cs.LG New本批；拟准入，Ch17/18递归停止actual定点；小Sudoku/局部实证不是全网络收敛定理 |
| [2609.26300v1 CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](https://arxiv.org/abs/2609.26300v1) | attentionmass先select再补tail→依据遗漏后补偿残余error联合mass/withinblocklogitvariation来选block，并异步实现→selector应对下游补偿机制而非仅topmass负责 | 2+2+2=6；cs.LG New本批；拟准入，Ch45现tailcompensation实际差额必要核；不从operator倍率推全Serving |
| [2609.26249v1 PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models](https://arxiv.org/abs/2609.26249v1) | 固定block B绑lookahead与commit数→逐步closed-form confidencecliff saturation定horizon、独立threshold定commit→两控制变量分权并核saturatedyield假设 | 2+2+2=6；合同cs.CL New本批，v1 Submitted2026-08-13T05:12:09Z不替代firstpublic；拟准入，Ch24/49实际差额和理论条件必要核 |
| [2609.26182v1 Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation](https://arxiv.org/abs/2609.26182v1) | 新adapter可改旧embedding/索引→modalitypack只在自己的编码路径执行，未命中路径保持原计算图/pack隔离→保留旧资产要检查实际gate/graph而非仅冻结weights | 2+2+2=6；合同cs.CL/cs.CV New本批，v1 Submitted2026-08-10T01:48:14Z不是public；拟准入，Ch23 interface/Ch30 adapter实际owner定点，exactness条件须deep，不采任意输入自动识别保证 |
| [2609.26061v1 TopoCompress: Topology Aware Token Compression Algorithm for Distributed Edge MoE Inference](https://arxiv.org/abs/2609.26061v1) | rawtraffic placement与semantic compression独立→fastloop压低重要/高路由cost token并路由survivor，slowloop用postcompression traffic更新placement/replica/residency→容量规划应消费压缩后的真实负载 | 潜在2+2+2=6仅供校准，当前不正式评分/候选：合同Cross-only、primarycs.NI；[monthly identity](https://arxiv.org/list/cs.NI/2026-09?skip=0&show=2000)159号，recent未恢复Wed23primary组。v1 Submitted2026-08-01T10:38:20Z；v2 2026-09-23T05:12:59Z窗后且不采用。需要本窗primary公告或更早首public有效证据，不能仅Cross/提交字段入选；缺口仅此identity，不深审所有网络 |

另具名撤回事件[16639v2](https://arxiv.org/abs/2609.16639v2)官方仍明确withdrawn、comment为作者不同意；v2不入选不评分不Books。current abs指v3正文返回、v3submitted2026-09-22T05:52:45Z但无本窗Replacement公告恢复；exact-v3 abs缓存miss，current abs成功但只是currentstatus，recent无该ID，不从提交字段伪造公开时刻。不否定v3可能有效，更不从正文出现自动继承v1采用；隔离该v3事件日期/撤回后授权边界，待官方本批replacement与正式修订说明定点重开。09/22 owner已撤除v1单源Books，其他有效证据保留。

最新作者停点（取代此前过程计数）：原29+新增5必要source与处置均完成，34为29实际整合/2已有覆盖/2仅报告/1中央争议隔离；29处实际书稿及邻接全部获sep21非作者写后PASS。七具名题摘独立准入校准已通过六New，Topo潜在贡献通过但具体公开日期隔离、不正式评分或计候选；16639v2撤回及v3日期/恢复边界隔离通过。六New的必要source→owner、实际窄段/写后又获root独立PASS，最终40冻结为35I/2E/2Only/1D，只待§4.24非作者日级Gate；不是34配额截止。历史§Queue/计数只表当时进度，不代表当前状态；本轮仍进行中，未stage/commit/push。

### 4.23 六个已校准New的必要源文→实际owner提案

本组均经sep21完整exact-v1题摘独立准入PASS，日期复用§1/附录该ID所在官方Wed23 New而不是v1 Submitted。作者已读下列必要方法/关键评价/直接反证；实际知识差额确定后最低深度为受影响内容深入。下列保存源文/owner提案；root随后亲读必要原文和实际owner，六项source→owner均PASS并授对应两段窄锁，作者实际写入六处，root已逐处实读正文/邻接写后PASS；具体锚点与最终有限日Gate包见§4.24。不把该六项局部结果自行签为全日通过。

- **26718v1 Sirens/LYRA**：[官方v1](https://arxiv.org/html/2609.26718v1)，2+1+2=5。§2.1–2.3 Eq2–7、§3.1–3.3 Eq8–11、§4 Tables1–3、AppC/D必要。RoPE旋转保范数，不自动给所有content pair单调distance衰减；q=k且小相位展开只是例子。M个同分背景的简化式给证据质量1/(1+M exp(sB-sE))，说明位置/数量竞争分开。LYRA先对旋转后QK归一化再t映射，保RoPE/mask/value但不是原dot-product语义或一定改善：同温cosine基线的增益须(1-G)(cB-cE)>0，不能仅由单调映射推出所有背景被压低。Qwen3-8B仅末block整体193M参数一epochLongAlign/16K/seed42微调，外部方法比较未给相同微调控制，不归唯一QK变换因果；Table3 SQA/code/synthetic非全面最佳，κ16 overall低于原baseline。AppC额外FLOPs是分析估算不是实机延迟，KV和dense复杂度不变。实际Ch22:101–129已讲可访问/读取竞争、N-back表征干预，但缺**固定位置下近端背景logit干预与距离移动分开，以及背景数量×scoregap的归一竞争/有条件score整形**。拟`MODEL-LONG-CONTEXT`在N-back两段后、评估切片前两窄段，保持位置扩展/原QK/显式检索，不复制Ch13 RoPE推导。
- **26708v1 Quantized OPD**：[官方v1](https://arxiv.org/html/2609.26708v1)，2+2+2=6。§3–6 Eq1–3 Tables1–4及AppC/D/F必要。QAD先建立可采样低位policy；OPD以deployment quantized forward产生student prefix，冻结BF16 teacher评同prefix，sampled reverseKL+group-relative verifier奖励同时训练，BF16 master更新不是BF16 rollout。实际Ch49:877–903已分浮点probe/PTQ恢复与执行Gate，没有**恢复训练的state distribution须包含目标量化forward引发的自生成偏离**；Ch29:434后通用OPD prefix/token原则已成立，不重复拥有目标数学。拟`INFER-TENSORRT-LLM`浮点probe两段后/Post-quantization标题前两窄段。四0.6–4B模型、mixed1.58/4权重2.79/1.88effectivebit、INT8activation/INT4embeddinghead、math→codephase；0.6B借1.7Bteacher例外。matchedQAD对照同start/corpora/step/samples不是等FLOPs/墙钟，也未分离verifier与stateforcing各因果；GPUhour比的是追加OPD与QAD初始化，不是整个pipeline免费或同最终质量。AppC baseline部分generative BF16embedding/head及自实现Q-Palette、wholewidth上取，不称全budget/kernel匹配；Falcon code/个别QA仍可退步，teacher不是真值，termination/repetition下降不认证所有任务。未复现训练/低bit kernel，保普通QAD/PTQ/高精度与独立生成质量Gate。
- **26487v1 Recursive completion**：[官方v1](https://arxiv.org/html/2609.26487v1)，2+1+2=5。§2.1–2.3 Eq1–11、§3.1–3.6 Tables1/Figs1–5、§4/5必要。同weights/input/TRM继续16→512，用first exact solve作离线对齐，cumulative ever-correct不是endpoint或可部署未知答案stop。定义d为本步实际update归一方向，||Jd||<1不蕴含||J||<1，更不认证任务correct；maxexpansion的输出方向与下一步expanding输入方向低重叠，单步谱范数不能直接相乘推多步。attention扰动16步吸收、MLP仍>初幅，未来命运未证；875evercorrect中16暂时失解。150puzzles×5states Jacobian与更小扰动子集，1000同sourcehardSudoku、两attentioncheckpoint/一MLP，有限512不证persistent永不完成/无限收敛/自然语言通用sensor；Maze exactpath非唯一另外解释。实际Ch17:550–562已分DEQ停止proposal、执行次数/有效计算，尚缺**轨迹方向稳定与全空间扰动稳定分权；任务首次完成、更新停滞、停止授权三种观测不能相互代替**。拟`MODEL-TRANSFORMER-LAYER`Recursive Depth两段末、下一state-budget标题前两窄段；保固定depth、预算/外部taskgate，不把诊断改为自动停止算法。
- **26300v1 CompKV**：[官方v1](https://arxiv.org/html/2609.26300v1)，2+2+2=6。§3.1–3.2 Eq1–7、§4.1–4.3 Eq8–12、§5 Tables1–3、AppA.2/A.3及C/E必要。Mean tail下精确KL是logpartition残余；固定maxblocksize且所有withinlogitvariance趋零时二阶score为sum_g p_gb sigma²_gb，不是任意summary/大variance/fulloutput误差的全局最优。grouped keyvariance忽略跨coordinate covariance，以compactmean/variance估mass与residual；sink+recent算同exactbudget，fullBF16KV仍存CPU，不是整cache删除。两个stream最终等event合并一次归一，不能假设无依赖免费overlap。实际Ch45:580–611已有ResKV main/residual和TopKCompletion联合归一/减重，但仍mass selector与残余构建分开，缺**selector按实际tail补偿残余而不是只attentionmass排序**。拟`INFER-KV-CACHE`TopKCompletion两段后/二维budget标题前两段。H10080GB/batch1、16tokenblock、3models/RULER32K及LongBenchPro625English三round；mainAVG仍低于Full，某task更差，分组越细metadata/质量换；CPU-offload效率为单layerattentionstep，非全model/requesttail或与Quest+RESA实测等价（后者未测latency）。保fullKV/exactread提高/原massselector当低variation或不配套tail时合理。
- **26249v1 PACE-dLLM**：[官方v1](https://arxiv.org/html/2609.26249v1)，2+2+2=6。§4.1 Eq5–7、§4.2 Thm1–2、§5.1–5.3 Tables1–2及Limitations必要。cursor推进越过已提交及高confidence连续前缀，scatteredcommit不推进；每4pass从当前firstlowconfidence refitlogistic，horizonanchor cT与commit阈值τ分开，退化fit/flat按rail回退；可选boundarytightening任务路由仍存在。Theorems是monotone eligibility probability、iidshape、截断saturatedyield的oracle renewalrate；qT非rawconfidence cT，overshootingfixedB也可相等；不证明runtime拟合达oracle/全局latency/quality最优。actualCh24:598–603已有learnedblock-end/entropyproposal但不承载**不训练boundaryhead的当前cliff拟合、lookahead horizon和实际commit权限分开**；拟`MULTIMODAL-GENERATIVE-PARADIGMS`该分支末/DraftVerify标题前两段。LLaDA8B/Dream7B单H100batch1/L512、warmup排除半suite，FastdLLM KVdisabled隔离decoder不是最好全stack；Dream更慢、短长generation未测，sharerail不取消所有defaults，confidence非truth。保fixedblock/单token安全接口，runtimeSLO独立验。
- **26182v1 Modality-gated adapters**：[官方v1](https://arxiv.org/html/2609.26182v1)，2+2+2=6。§3.1–3.6 Prop1–2/Hook、§4.1–4.4 Tables2–4、§5 Table6、§8必要。冻结weights与zero-init不等旧graph永远不变；所有pack gate关闭时hook在adapter算术前返回，原图同weights/precision/kernel/order/batch才可bitwise，单gate开时其他pack不可见，多gate同forward未验证。尤其正文宣称inputkeyed不许可自动内容识别：thermal replicatedRGB字节相同，**encode入口声明gate**；audio guard存在、thermal依赖scope纪律，checkpoint backward recomputation也必须同gate。actualCh23:71–74已有continual projector混合/语言delta，280–282已有zero-initpromptcrossattn而非长期bypass，Ch30只有通用adapter训练/挂载；缺**新模态层内容量的pack执行scope和旧输入完全绕过证明**。拟`MULTIMODAL-REPRESENTATION`持续projector两段后/语音音素分支前两段。单Qwen3VL2B/audio+thermal两route，45K800step三seed控制没等trainparams，fullscale同时改loss/filter，gate-openthermalclassification94vsbase95退步不叫无退化；closedgate每modality一个input实测不认证全部concurrentrequest隔离或异kerneldeterminism。额外adapter驻留/训练和gate测试成本须验；保externalprojector或独立model，当多模态混合/入口scope不可靠回退。

当前普通停点：六项source→actual-owner与六处实际写后全部获root非作者PASS；与此前sep21的29处合计35处实际整合。40冻结家族为35I/2E/2Only/1D，候选必要审阅/Books/写后剩余0，最终日级非作者Gate尚待，报告保持进行中；Topo与ReDraftv3精确外部隔离不扩大scope。作者不以授权、实写或局部PASS自签全日。

### 4.24 最终日级有限复核包（作者汇总，非作者结论待填）

- **窗口/来源入口与停止范围**：正式[09/23报告§2](../../23/README.md)自包含14每日来源，各机构完整有界入口证据在年级[institution-screening.md](../../../_sources/daily-20260923/institution-screening.md)，Hunyuan旧8条记录由本笔记§2及正式报告纠正为9条/100116旧2608.29296v1且无revision；不沿旧publicAt单字段首公开。arXiv十二类actual New/Cross组/skip0/show2000/下一日stop在本笔记§1–2及附录A，666=554 New＋112 Cross-only是题名查漏库存，不是666完整题摘/正文或全学科召回。首30完整题摘中HBF较早家族去重，原29＋新增五（§4.21）＋七具名中六New（§4.22/23）经有限准入为最终40；不设34/40配额，不增新的查询池。
- **全部拟入选**：正式报告40行/40项§4，最终35整合、2已有覆盖（26173 Ch49 component敏感度；26292 Ch26 visual/physics与task-feasible评价）、2仅报告（25048 breadth/refresh条件；26779 live-window主动丢recall）、1中央争议（26763）。原34 source→actual-owner/最终处置与29actual由sep21逐批实际核并在正式§4引用对应本笔记必要证据；六New的exact-v1关键公式/方法/评价/反证由root另亲读并对actual owner核，两侧有效结果身份/版本/采用命题不变，不重读所有附件。
- **新增六处真实写后**：root已读actual正文及前后交接PASS：Sirens26718 Ch22:121–123；QuantizedOPD26708 Ch49:883–885；Recursive26487 Ch17:562–564；CompKV26300 Ch45:613–615；PACE26249 Ch24:604–606；MGDA26182 Ch23:75–77。所有窄段保原机制/成本/failure/fallback，未覆盖June09 BUDDY/OmniMem等共同章段；Flash等原29actual已获sep21逐处PASS。Flux仅Fabric局部机制落实，不称全章Refine。
- **纠错、安全、设计反证与重要事件**：SARA26763 printed VI-D Eq55–58/Fig8/VII已由sep21有限读核D，non-increasing不证明unique global optimum，不以此作Books正面采用；原有有界方法/实验不被全否定。26513v2/26425v2采用本窗精确版本必要机制/关键反证并已实际写后核，不按版本号推new贡献或复用未读正文。Topo26061与ReDraft16639v2/v3事件§4.22明确隔离，sep21完整题摘/当前原始status校准：v2 withdrawn永不候选/评分/Books；v3当前正文存在不证first-public/正式恢复，不能复活v1。Opus/card、Astra纠正/card、MiMoV2.6与ZCode四dateholds必须取得落窗时刻/可信公告才重开，不作为无遗漏或安全保证。
- **具名分层负侧最小范围**：本筆记§3记录26662儿童近视治疗/25697地区青光眼产品（领域应用）、25040香蕉病害适配（领域指标）、26502晶体结构生成benchmark（暂缓AIforScience）四个明确题名范围关闭，未称摘要/全文审；HBF25782按DOI/更早正式家族而非arXiv重公告去重。机构账本中KimiCLI1.52.0/MinimaxCode0.5.2是安装/打包而非新机制；QwenCode/MiMoCode的本窗release与较早PR首公区分，38旧论文已实际迁回09/22，由单一reconciliation owner处理；Sol/Luna未披露机制、prompt-cache已有具体机制覆盖的有限关闭结果可复用。以上是跨来源/范围/理由的具名样本，不把其余宽库存全部宣称排除全文核；非作者须在最终结论说明实际抽核身份/范围，而不是照抄作者已核。
- **终态保留与普通工作**：必要候选审阅/Books/实写/逐项写后剩余0；只待本节全日非作者复核。外部精确隔离为两项arXiv事件（Topo首公，ReDraftv3日期/恢复）、四机构日级DateHold与Google/Qwen/ZAI三目录限制，各在正式§5写了需要的官方公告/可读列表/API及定点重开范围。它们不支持正面采用、全网零新增或无遗漏，亦不因此新增无限恢复队列。机器V3/Markdown/引用/限定diff按实际运行结果同步，不能替代独立Gate。未stage/commit/push，共享索引/LEARNING_STATE由root维护。

机器预检：正式V3日报校验与本日报/六新增owner限定 `git diff --check` 均PASS；本次普通文档改动未复现实验、未验证低bit kernel或生产SLO。最终非作者结论由root在本节追加实际范围及判定；作者当前不自签。

**2026-09-30 root非作者最终日级结论：通过。** 实际核14源停止范围、十二类New/Cross日期依据、40正式行/40证据与35/2/2/1处置；复用sep21原34必要证据/29写后，自核新增六必要源与六处actual/邻接。负侧另取26662、25697、25040完整摘要和26502原始题摘，确认临床结果、领域适配和暂缓AI for Science的具体关闭理由；并核HBF、机构版本包装、撤回/修订/日期隔离。没有将宽库存称作全量全文复核。普通工作0，隔离项保留精确重开条件且不用于Books或无遗漏保证；正式§6同步本范围，完成仅指安全终态。

## 附录 A. 十二类 New/Cross 原始身份（去重前）

### cs.CL

New（80）：

```text
2609.26796 2609.26781 2609.26780 2609.26704 2609.26693 2609.26687 2609.26638 2609.26637 2609.26634 2609.26629 2609.26610 2609.26579 2609.26539 2609.26536 2609.26527 2609.26489 2609.26488 2609.26468 2609.26422 2609.26399 2609.26381 2609.26368 2609.26347 2609.26346 2609.26338 2609.26306 2609.26249 2609.26241 2609.26210 2609.26208 2609.26182 2609.26177 2609.26113 2609.26100 2609.26097 2609.26090 2609.26086 2609.26052 2609.26035 2609.26034 2609.25939 2609.25927 2609.25890 2609.25862 2609.25859 2609.25853 2609.25833 2609.25797 2609.25755 2609.25669 2609.25611 2609.25537 2609.25518 2609.25447 2609.25441 2609.25396 2609.25356 2609.25298 2609.25192 2609.25130 2609.25081 2609.25066 2609.25058 2609.25056 2609.25055 2609.25054 2609.25053 2609.25052 2609.25051 2609.25050 2609.25049 2609.25048 2609.25047 2609.25046 2609.25034 2609.25028 2609.25012 2609.25009 2609.25008 2609.25006
```

Cross（28）：

```text
2609.26658 2609.26481 2609.26388 2609.26237 2609.26218 2609.26204 2609.26185 2609.26121 2609.26061 2609.26048 2609.26025 2609.25948 2609.25938 2609.25808 2609.25802 2609.25721 2609.25686 2609.25645 2609.25602 2609.25498 2609.25405 2609.25237 2609.25186 2609.25176 2609.25021 2609.25010 2609.25007 2609.23640
```

### cs.LG

New（118）：

```text
2609.26751 2609.26718 2609.26708 2609.26679 2609.26667 2609.26631 2609.26621 2609.26603 2609.26537 2609.26508 2609.26487 2609.26460 2609.26435 2609.26426 2609.26402 2609.26392 2609.26389 2609.26384 2609.26377 2609.26355 2609.26342 2609.26333 2609.26310 2609.26300 2609.26288 2609.26280 2609.26275 2609.26272 2609.26257 2609.26242 2609.26231 2609.26217 2609.26216 2609.26214 2609.26199 2609.26173 2609.26167 2609.26165 2609.26147 2609.26146 2609.26112 2609.26094 2609.26081 2609.26077 2609.26067 2609.26063 2609.26037 2609.26025 2609.26021 2609.26018 2609.25987 2609.25980 2609.25963 2609.25962 2609.25938 2609.25916 2609.25914 2609.25876 2609.25874 2609.25839 2609.25836 2609.25827 2609.25814 2609.25811 2609.25809 2609.25808 2609.25802 2609.25788 2609.25781 2609.25777 2609.25757 2609.25745 2609.25735 2609.25728 2609.25722 2609.25721 2609.25701 2609.25692 2609.25675 2609.25659 2609.25657 2609.25655 2609.25645 2609.25634 2609.25623 2609.25602 2609.25582 2609.25569 2609.25542 2609.25541 2609.25510 2609.25501 2609.25484 2609.25482 2609.25471 2609.25444 2609.25438 2609.25433 2609.25430 2609.25397 2609.25373 2609.25340 2609.25334 2609.25326 2609.25310 2609.25297 2609.25237 2609.25179 2609.25166 2609.25163 2609.25152 2609.25149 2609.25146 2609.25143 2609.25134 2609.25131 2609.25082 2609.25021
```

Cross（98）：

```text
2609.26783 2609.26780 2609.26779 2609.26748 2609.26737 2609.26707 2609.26705 2609.26683 2609.26658 2609.26647 2609.26642 2609.26624 2609.26617 2609.26605 2609.26598 2609.26590 2609.26581 2609.26502 2609.26474 2609.26457 2609.26445 2609.26406 2609.26388 2609.26378 2609.26361 2609.26352 2609.26347 2609.26326 2609.26303 2609.26290 2609.26270 2609.26244 2609.26243 2609.26241 2609.26219 2609.26193 2609.26177 2609.26166 2609.26143 2609.26097 2609.26069 2609.26068 2609.26052 2609.26039 2609.26032 2609.25978 2609.25947 2609.25924 2609.25845 2609.25820 2609.25778 2609.25776 2609.25710 2609.25705 2609.25686 2609.25678 2609.25654 2609.25643 2609.25624 2609.25605 2609.25588 2609.25576 2609.25567 2609.25558 2609.25546 2609.25518 2609.25505 2609.25490 2609.25454 2609.25442 2609.25411 2609.25408 2609.25388 2609.25386 2609.25381 2609.25352 2609.25351 2609.25338 2609.25285 2609.25155 2609.25145 2609.25144 2609.25138 2609.25130 2609.25123 2609.25088 2609.25085 2609.25067 2609.25057 2609.25044 2609.25039 2609.25034 2609.25014 2609.25009 2609.25006 2609.24194 2609.23640 2609.22822
```

### cs.DC

New（12）：

```text
2609.26616 2609.26602 2609.26476 2609.26363 2609.26219 2609.26190 2609.25918 2609.25560 2609.25479 2609.25451 2609.25442 2609.25415
```

Cross（11）：

```text
2609.26788 2609.26763 2609.26080 2609.25949 2609.25817 2609.25463 2609.25443 2609.25437 2609.25082 2609.25043 2609.07204
```

### cs.AI

New（101）：

```text
2609.26779 2609.26777 2609.26760 2609.26758 2609.26642 2609.26565 2609.26556 2609.26550 2609.26532 2609.26461 2609.26457 2609.26428 2609.26419 2609.26293 2609.26279 2609.26268 2609.26261 2609.26244 2609.26243 2609.26213 2609.26207 2609.26193 2609.26187 2609.26175 2609.26160 2609.26157 2609.26145 2609.26144 2609.26135 2609.26126 2609.26125 2609.26124 2609.26123 2609.26121 2609.26106 2609.26105 2609.26095 2609.26087 2609.26076 2609.26069 2609.26060 2609.26059 2609.26048 2609.26046 2609.26029 2609.26015 2609.25960 2609.25873 2609.25852 2609.25848 2609.25806 2609.25804 2609.25769 2609.25766 2609.25760 2609.25738 2609.25715 2609.25712 2609.25686 2609.25678 2609.25677 2609.25647 2609.25643 2609.25620 2609.25618 2609.25607 2609.25591 2609.25588 2609.25581 2609.25575 2609.25572 2609.25570 2609.25555 2609.25508 2609.25496 2609.25491 2609.25474 2609.25469 2609.25467 2609.25466 2609.25463 2609.25443 2609.25408 2609.25405 2609.25400 2609.25366 2609.25337 2609.25303 2609.25299 2609.25286 2609.25285 2609.25284 2609.25272 2609.25254 2609.25199 2609.25187 2609.25165 2609.25088 2609.25036 2609.25013 2609.25010
```

Cross（139）：

```text
2609.26780 2609.26761 2609.26756 2609.26749 2609.26725 2609.26718 2609.26711 2609.26708 2609.26704 2609.26693 2609.26682 2609.26679 2609.26637 2609.26621 2609.26603 2609.26579 2609.26562 2609.26547 2609.26527 2609.26512 2609.26507 2609.26492 2609.26487 2609.26486 2609.26480 2609.26474 2609.26463 2609.26426 2609.26425 2609.26389 2609.26378 2609.26377 2609.26361 2609.26355 2609.26347 2609.26342 2609.26314 2609.26300 2609.26295 2609.26274 2609.26237 2609.26229 2609.26209 2609.26204 2609.26185 2609.26184 2609.26177 2609.26176 2609.26174 2609.26166 2609.26151 2609.26131 2609.26112 2609.26100 2609.26072 2609.26057 2609.26056 2609.26039 2609.26037 2609.26028 2609.26023 2609.26016 2609.26007 2609.26000 2609.25980 2609.25942 2609.25921 2609.25891 2609.25889 2609.25876 2609.25836 2609.25821 2609.25815 2609.25809 2609.25788 2609.25773 2609.25755 2609.25735 2609.25728 2609.25721 2609.25697 2609.25674 2609.25655 2609.25641 2609.25634 2609.25623 2609.25586 2609.25582 2609.25567 2609.25563 2609.25562 2609.25542 2609.25541 2609.25537 2609.25512 2609.25510 2609.25498 2609.25492 2609.25482 2609.25471 2609.25460 2609.25433 2609.25430 2609.25421 2609.25397 2609.25396 2609.25388 2609.25376 2609.25247 2609.25244 2609.25237 2609.25194 2609.25189 2609.25186 2609.25179 2609.25176 2609.25166 2609.25154 2609.25152 2609.25150 2609.25146 2609.25143 2609.25134 2609.25130 2609.25123 2609.25118 2609.25108 2609.25082 2609.25057 2609.25053 2609.25052 2609.25051 2609.25050 2609.25049 2609.25048 2609.25047 2609.25021 2609.25014 2306.02136
```

### cs.CV

New（108）：

```text
2609.26793 2609.26774 2609.26756 2609.26733 2609.26731 2609.26729 2609.26702 2609.26662 2609.26636 2609.26623 2609.26620 2609.26617 2609.26605 2609.26590 2609.26578 2609.26561 2609.26549 2609.26513 2609.26512 2609.26505 2609.26492 2609.26484 2609.26474 2609.26463 2609.26458 2609.26443 2609.26430 2609.26425 2609.26375 2609.26334 2609.26325 2609.26299 2609.26274 2609.26236 2609.26233 2609.26205 2609.26189 2609.26188 2609.26166 2609.26161 2609.26117 2609.26103 2609.26099 2609.26093 2609.26092 2609.26088 2609.26078 2609.26073 2609.26064 2609.26056 2609.26039 2609.25978 2609.25972 2609.25966 2609.25945 2609.25937 2609.25930 2609.25907 2609.25891 2609.25881 2609.25860 2609.25850 2609.25845 2609.25841 2609.25837 2609.25832 2609.25815 2609.25803 2609.25793 2609.25775 2609.25773 2609.25770 2609.25743 2609.25741 2609.25731 2609.25716 2609.25697 2609.25693 2609.25685 2609.25684 2609.25652 2609.25650 2609.25638 2609.25635 2609.25615 2609.25604 2609.25597 2609.25584 2609.25578 2609.25567 2609.25538 2609.25515 2609.25503 2609.25500 2609.25492 2609.25490 2609.25454 2609.25453 2609.25429 2609.25386 2609.25331 2609.25319 2609.25270 2609.25267 2609.25247 2609.25108 2609.25067 2609.25017
```

Cross（35）：

```text
2609.26795 2609.26792 2609.26648 2609.26638 2609.26631 2609.26567 2609.26537 2609.26420 2609.26378 2609.26182 2609.26168 2609.26151 2609.26105 2609.26097 2609.26095 2609.26081 2609.25884 2609.25864 2609.25831 2609.25746 2609.25654 2609.25633 2609.25627 2609.25611 2609.25511 2609.25444 2609.25375 2609.25334 2609.25271 2609.25138 2609.25123 2609.25058 2609.25051 2609.25040 2609.25022
```

### cs.RO

New（104）：

```text
2609.26795 2609.26792 2609.26766 2609.26753 2609.26672 2609.26618 2609.26580 2609.26567 2609.26564 2609.26520 2609.26499 2609.26490 2609.26467 2609.26423 2609.26420 2609.26408 2609.26378 2609.26360 2609.26315 2609.26314 2609.26313 2609.26304 2609.26292 2609.26267 2609.26256 2609.26238 2609.26184 2609.26155 2609.26131 2609.26130 2609.26118 2609.26085 2609.26084 2609.26083 2609.26071 2609.26051 2609.26007 2609.26004 2609.25994 2609.25969 2609.25961 2609.25942 2609.25932 2609.25917 2609.25905 2609.25900 2609.25898 2609.25887 2609.25831 2609.25820 2609.25813 2609.25785 2609.25756 2609.25754 2609.25750 2609.25746 2609.25725 2609.25724 2609.25709 2609.25696 2609.25695 2609.25689 2609.25688 2609.25687 2609.25674 2609.25668 2609.25666 2609.25658 2609.25654 2609.25653 2609.25649 2609.25642 2609.25639 2609.25636 2609.25631 2609.25630 2609.25627 2609.25625 2609.25619 2609.25614 2609.25606 2609.25577 2609.25562 2609.25558 2609.25527 2609.25511 2609.25506 2609.25486 2609.25470 2609.25450 2609.25417 2609.25398 2609.25376 2609.25375 2609.25374 2609.25369 2609.25363 2609.25351 2609.25338 2609.25322 2609.25274 2609.25271 2609.25264 2609.25031
```

Cross（8）：

```text
2609.26561 2609.26325 2609.26157 2609.26156 2609.26010 2609.25860 2609.25757 2609.25257
```

### cs.AR

New（8）：

```text
2609.26644 2609.26551 2609.26374 2609.25869 2609.25782 2609.25624 2609.25335 2609.25022
```

Cross（2）：

```text
2609.25873 2609.25637
```

### cs.PL

New（2）：

```text
2609.25427 2609.25421
```

Cross（4）：

```text
2609.26270 2609.26122 2609.25335 2609.25121
```

### cs.OS

New（1）：

```text
2609.25018
```

Cross（1）：

```text
2609.04043
```

### cs.PF

New（1）：

```text
2609.26763
```

Cross（2）：

```text
2609.26616 2609.26284
```

### cs.IR

New（11）：

```text
2609.26658 2609.26251 2609.26250 2609.26237 2609.26218 2609.26171 2609.26143 2609.25991 2609.25825 2609.25306 2609.25189
```

Cross（4）：

```text
2609.26780 2609.26086 2609.25833 2609.25408
```

### cs.MA

New（8）：

```text
2609.26481 2609.26080 2609.26010 2609.25959 2609.25956 2609.25913 2609.25432 2609.25194
```

Cross（7）：

```text
2609.26781 2609.26146 2609.26135 2609.26121 2609.26059 2609.25701 2609.25195
```

## 附录 B. 去重身份与实际官方题名（仅发现，不等于审阅）

- `2609.26796` [cs.CL；合同类含New] Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs
- `2609.26781` [cs.CL,cs.MA；合同类含New] Agensh: Scaling Organizational Intelligence to 1,024 Agents
- `2609.26780` [cs.CL,cs.LG,cs.AI,cs.IR；合同类含New] SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue
- `2609.26704` [cs.CL,cs.AI；合同类含New] Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning
- `2609.26693` [cs.CL,cs.AI；合同类含New] Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation
- `2609.26687` [cs.CL；合同类含New] Detecting GPT-Assisted Writing Using Interpretable Stylometric Features
- `2609.26638` [cs.CL,cs.CV；合同类含New] Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding
- `2609.26637` [cs.CL,cs.AI；合同类含New] Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models
- `2609.26634` [cs.CL；合同类含New] Knowledge Pull Requests for Continual Document Authoring
- `2609.26629` [cs.CL；合同类含New] PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation
- `2609.26610` [cs.CL；合同类含New] Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models
- `2609.26579` [cs.CL,cs.AI；合同类含New] Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models
- `2609.26539` [cs.CL；合同类含New] A retrospective analysis on the use of LLMs to study infant syntax learning
- `2609.26536` [cs.CL；合同类含New] Transcribe, Translate, and Optimize: Joint Reward Learning for Speech Translation
- `2609.26527` [cs.CL,cs.AI；合同类含New] A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation
- `2609.26489` [cs.CL；合同类含New] Calibration as a First-Class Criterion in LLM Evaluation
- `2609.26488` [cs.CL；合同类含New] Spoken Language Models that Think Aloud
- `2609.26468` [cs.CL；合同类含New] How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification
- `2609.26422` [cs.CL；合同类含New] Enriching Speech Emotion Representations with Conversational Context
- `2609.26399` [cs.CL；合同类含New] Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding
- `2609.26381` [cs.CL；合同类含New] Layout-Guided Masking for GROBID: Lightweight Structural Gains in Large-Scale Scientific PDF Ingestion
- `2609.26368` [cs.CL；合同类含New] HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing
- `2609.26347` [cs.CL,cs.LG,cs.AI；合同类含New] TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling
- `2609.26346` [cs.CL；合同类含New] Blaming Across the Aisle: Political Contrasting and Blame Attribution in the Danish Parliament
- `2609.26338` [cs.CL；合同类含New] Designing and Analysing Argument Mining Pipelines: Towards a Comprehensive Assessment
- `2609.26306` [cs.CL；合同类含New] CHiME-9 ECHI: A Machine Learning Challenge for Enhancing Conversations to Address Hearing Impairment
- `2609.26249` [cs.CL；合同类含New] PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models
- `2609.26241` [cs.CL,cs.LG；合同类含New] Damage Predicts Recovery: When Calibration Data Matters in Compressing Financial LLMs
- `2609.26210` [cs.CL；合同类含New] Same Chart, Different Story: Bias in Vision-Language Chart Interpretation
- `2609.26208` [cs.CL；合同类含New] Beyond Static Charts: Can Language and Vision Language Models Generate Interactive Data Visualization Interfaces?
- `2609.26182` [cs.CL,cs.CV；合同类含New] Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation
- `2609.26177` [cs.CL,cs.LG,cs.AI；合同类含New] Magnitude Profile Pruning: Calibration-Free Structured Attention Head Removal for Transformer Compression
- `2609.26113` [cs.CL；合同类含New] Differentiable Fuzzy Inference Layer: A Monotone, Compositional Ordinal Reasoning Head for Large Language Models
- `2609.26100` [cs.CL,cs.AI；合同类含New] TSS: Target-Side Sparsification for Speculative Decoding in Domain-Specific Large Language Models
- `2609.26097` [cs.CL,cs.LG,cs.CV；合同类含New] One Domain, Many Tongues: Composing Domain and Language LoRAs for Cross-Lingual Remote-Sensing MLLMs without Paired Data
- `2609.26090` [cs.CL；合同类含New] SpecialEduBench: Benchmarking Vision-Language Models on Knowledge, Skill, and Attitude in Language Intervention for Autistic Children
- `2609.26086` [cs.CL,cs.IR；合同类含New] CoVeR: Coverage-Based Routing of Verifier Calls in Agentic Retrieval
- `2609.26052` [cs.CL,cs.LG；合同类含New] Optimizing Denoising Trajectories in dLLMs: A Lightweight Evolutionary Heuristic Approach
- `2609.26035` [cs.CL；合同类含New] Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance
- `2609.26034` [cs.CL；合同类含New] Domain-Adaptive Pretraining Enhances Water Treatment Semantic Representation for Large-Scale Structured Literature Mining
- `2609.25939` [cs.CL；合同类含New] ClusterFewshot: Improving Few-shot Optimization for LLMs workflow
- `2609.25927` [cs.CL；合同类含New] Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models
- `2609.25890` [cs.CL；合同类含New] Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models
- `2609.25862` [cs.CL；合同类含New] Isolated Sign Language Recognition for Icelandic Sign Language: Experiments in a Low-resource Setting
- `2609.25859` [cs.CL；合同类含New] BELXTR: Biomedical Entity Linking via Contextualized Token Retrieval
- `2609.25853` [cs.CL；合同类含New] MemoryAthena: Adaptive Routing over Latent and Generated Memories
- `2609.25833` [cs.CL,cs.IR；合同类含New] ARAFA: An LLM-Generated Arabic Fact-Checking Dataset
- `2609.25797` [cs.CL；合同类含New] Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language
- `2609.25755` [cs.CL,cs.AI；合同类含New] Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation
- `2609.25669` [cs.CL；合同类含New] From Utterances to Networks: Modelling Slang Adoption and Diffusion Across Subreddits
- `2609.25611` [cs.CL,cs.CV；合同类含New] Qwen3.8-Omni: Towards Native Omni-Modal Agents
- `2609.25537` [cs.CL,cs.AI；合同类含New] Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference
- `2609.25518` [cs.CL,cs.LG；合同类含New] Matryoshka attribution: Learning to attribute language model outputs to representations and weights
- `2609.25447` [cs.CL；合同类含New] Conduct Under Pressure: What Sixty Language Models Do When a User Pushes
- `2609.25441` [cs.CL；合同类含New] Mining Legal Arguments in U.S. Corporate Case Law
- `2609.25396` [cs.CL,cs.AI；合同类含New] Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development
- `2609.25356` [cs.CL；合同类含New] TelecomGPT-R1: Unified Post-Training for Reasoning Across Heterogeneous Telecom Tasks
- `2609.25298` [cs.CL；合同类含New] FineWeb-CLaR: Culture, Language, and Region Annotations for Benchmark-Aligned Corpus Auditing
- `2609.25192` [cs.CL；合同类含New] FinFIRST: Benchmarking Search Agents for Financial Information Retrieval, Sourcing and Traceability
- `2609.25130` [cs.CL,cs.LG,cs.AI；合同类含New] Impact Is Not Invalidation: Ask About the Claim, Not the Diff
- `2609.25081` [cs.CL；合同类含New] ufakzeka-1: Building and Evaluating a 151M-Parameter Turkish Language Model from Scratch
- `2609.25066` [cs.CL；合同类含New] Understanding Reliability in LLM-based Human Behavior Simulation
- `2609.25058` [cs.CL,cs.CV；合同类含New] ChainDoRA: Tensor-Train Factorized Weight-Decomposed Low-Rank Adaptation for Parameter-Efficient LLM Fine-Tuning
- `2609.25056` [cs.CL；合同类含New] Graph-Based Inference for Feedback-Driven Word Deduction: A Scalable Framework for the Jotto Problem
- `2609.25055` [cs.CL；合同类含New] ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains
- `2609.25054` [cs.CL；合同类含New] MoM: Memory of Memory
- `2609.25053` [cs.CL,cs.AI；合同类含New] LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay
- `2609.25052` [cs.CL,cs.AI；合同类含New] Self-Cleaning and Captured Anyway: One Measured Primitive for Error in a Store an Agent Writes to Itself, and What a Falling Score Actually Measures
- `2609.25051` [cs.CL,cs.AI,cs.CV；合同类含New] LLM-Driven Training-free Location-Attribute Synergic Fusion: A Closed-Loop Paradigm for Dual-source Encrypted POIs and LULC Mapping
- `2609.25050` [cs.CL,cs.AI；合同类含New] FrontierMath Erdős
- `2609.25049` [cs.CL,cs.AI；合同类含New] Mitigating LLM Over-Refusal via Dynamic Semantic Routing Calibratione
- `2609.25048` [cs.CL,cs.AI；合同类含New] Prompt Breadth and Rollout Refresh Interact in On-Policy Distillation
- `2609.25047` [cs.CL,cs.AI；合同类含New] AIBuildAI-2.5: Efficient Autonomous AI Model Development Through LLM-Guided Tree Search
- `2609.25046` [cs.CL；合同类含New] Peerify: Benchmarking Peer-Review Claim Verification
- `2609.25034` [cs.CL,cs.LG；合同类含New] From Tone to Trajectory: Continuous Sentiment and the Shape of Monetary Policy Communication
- `2609.25028` [cs.CL；合同类含New] Retrieved-Span Training for Efficient Query-Focused Meeting Summarization on QMSum
- `2609.25012` [cs.CL；合同类含New] A Computational Approach to Measuring Semantic Change in Sanskrit Literature
- `2609.25009` [cs.CL,cs.LG；合同类含New] Same Quantity, Different Answer: Numerical Representation Invariance in Language Models
- `2609.25008` [cs.CL；合同类含New] Training a Language Model End-to-End in Rust: An Experience Report
- `2609.25006` [cs.CL,cs.LG；合同类含New] What Does 99% Accuracy Measure? A Reproducible Audit of Shortcut Learning in a Widely Used Fake News Corpus
- `2609.26658` [cs.CL,cs.LG,cs.IR；合同类含New] Discovery-Driven Integration of Disjoint Tables via Text
- `2609.26481` [cs.CL,cs.MA；合同类含New] Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies
- `2609.26388` [cs.CL,cs.LG；合同类Cross-only] On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality
- `2609.26237` [cs.CL,cs.AI,cs.IR；合同类含New] ABAI at COLIEE 2026 Task 1: Multi-Stage Retrieval with GraphRAG-Enhanced Meta-Learning, and a Post-Hoc Study of the Cross-Validation-to-Test Gap
- `2609.26218` [cs.CL,cs.IR；合同类含New] A Semantic Approach to the Academic Publishing Network: Document Vector Representations and Hybrid Structural-Semantic Fusion over OpenAlex Data
- `2609.26204` [cs.CL,cs.AI；合同类Cross-only] WatchPoint: Executable User Feedback for Real-World Agentic Web Development
- `2609.26185` [cs.CL,cs.AI；合同类Cross-only] Dynamic Deep Prompt Optimization for Defending Against Jailbreak Attacks on LLMs
- `2609.26121` [cs.CL,cs.AI,cs.MA；合同类含New] DTOC: Dynamic Tool Output Compression for Adaptive Context Management in AI Agents
- `2609.26061` [cs.CL；合同类Cross-only] TopoCompress: Topology Aware Token Compression Algorithm for Distributed Edge MoE Inference
- `2609.26048` [cs.CL,cs.AI；合同类含New] FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents
- `2609.26025` [cs.CL,cs.LG；合同类含New] MICRO: Multi-Fidelity Active Search for Severe Error Discovery
- `2609.25948` [cs.CL；合同类Cross-only] Challenges of Multi-Speaker Extraction for Real Conversational Speech Enhancement
- `2609.25938` [cs.CL,cs.LG；合同类含New] Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL
- `2609.25808` [cs.CL,cs.LG；合同类含New] Auditing Proxy-Based Validation Across Text Spans
- `2609.25802` [cs.CL,cs.LG；合同类含New] Latest Exact Match Attention
- `2609.25721` [cs.CL,cs.LG,cs.AI；合同类含New] Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages
- `2609.25686` [cs.CL,cs.LG,cs.AI；合同类含New] How Strongly Should Task State Influence an LLM Agent?
- `2609.25645` [cs.CL,cs.LG；合同类含New] Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices
- `2609.25602` [cs.CL,cs.LG；合同类含New] Rewired or Gated? How Instruction Tuning Shapes Knowledge-Conflict Circuits in LLMs
- `2609.25498` [cs.CL,cs.AI；合同类Cross-only] Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains
- `2609.25405` [cs.CL,cs.AI；合同类含New] Efficient Iterative Retrieval with Heterogeneous Batching
- `2609.25237` [cs.CL,cs.LG,cs.AI；合同类含New] Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers
- `2609.25186` [cs.CL,cs.AI；合同类Cross-only] From Pattern Recognizers to Personalized Companions: A Survey of Large Language Models in Mental Health
- `2609.25176` [cs.CL,cs.AI；合同类Cross-only] Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction
- `2609.25021` [cs.CL,cs.LG,cs.AI；合同类含New] "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It
- `2609.25010` [cs.CL,cs.AI；合同类含New] Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation
- `2609.25007` [cs.CL；合同类Cross-only] Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives
- `2609.23640` [cs.CL,cs.LG；合同类Cross-only] Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment
- `2609.26751` [cs.LG；合同类含New] EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations
- `2609.26718` [cs.LG,cs.AI；合同类含New] The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence
- `2609.26708` [cs.LG,cs.AI；合同类含New] Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning
- `2609.26679` [cs.LG,cs.AI；合同类含New] A Spectral Theory of Grokking: Weight Decay induces Feature Learning
- `2609.26667` [cs.LG；合同类含New] MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning
- `2609.26631` [cs.LG,cs.CV；合同类含New] Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD
- `2609.26621` [cs.LG,cs.AI；合同类含New] Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference
- `2609.26603` [cs.LG,cs.AI；合同类含New] Towards Hierarchical GNNs for multi-grid power flow: generalization across operating scenarios
- `2609.26537` [cs.LG,cs.CV；合同类含New] Notes on Fourier-Bessel wavelets
- `2609.26508` [cs.LG；合同类含New] Gap-Free Streaming PCA Beyond Rank-One Updates: Near-Optimal Rates and Applications to Differential Privacy
- `2609.26487` [cs.LG,cs.AI；合同类含New] When Recursive Models Finish Computing
- `2609.26460` [cs.LG；合同类含New] Can We Predict Anomaly Detection Performance from Embedding-Space Geometry?
- `2609.26435` [cs.LG；合同类含New] One-Step Generative Surrogate Models via Block-Triangular Joint Drifting
- `2609.26426` [cs.LG,cs.AI；合同类含New] DeepFEAv2: Deep Learning for Transient Finite Element Analysis Beyond Structured Meshes
- `2609.26402` [cs.LG；合同类含New] OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery
- `2609.26392` [cs.LG；合同类含New] Double Descent and Malign Overfitting in Diffusion Models
- `2609.26389` [cs.LG,cs.AI；合同类含New] TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series
- `2609.26384` [cs.LG；合同类含New] Learning to Defer with Guidance on Real World Medical Data
- `2609.26377` [cs.LG,cs.AI；合同类含New] FairMean: Promoting Fairness in Distributed Learning under Label Poisoning Attacks
- `2609.26355` [cs.LG,cs.AI；合同类含New] PACT: From Credit Assignment to Critic Alignment
- `2609.26342` [cs.LG,cs.AI；合同类含New] Geometry-Aware Hyperbolic Residual Quantization
- `2609.26333` [cs.LG；合同类含New] Disaggregated Quantization: Specializing LLM Prefill and Decode
- `2609.26310` [cs.LG；合同类含New] PreGS: A Parameter-Transfer-Based Multi-Expert Graph Neural Network for Node Classification
- `2609.26300` [cs.LG,cs.AI；合同类含New] CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference
- `2609.26288` [cs.LG；合同类含New] Quantifying Protocol-Induced Uncertainty in Comparative Predictive-Model Evaluation: Evidence from Large-Scale Daily PM10 Forecasting
- `2609.26280` [cs.LG；合同类含New] On the Effect of Bit-Level Parameter Perturbations in Machine Learning and Deep Learning Models
- `2609.26275` [cs.LG；合同类含New] JAMPR+/L2D: scalable neural heuristic for constrained vehicle routing problems in dynamic environment
- `2609.26272` [cs.LG；合同类含New] Mode Collapse Is Cheap to Detect: A Ground-Truth-Free Pre-Flight Check for Neural Samplers
- `2609.26257` [cs.LG；合同类含New] Information-Theoretic Decoupled Prompt Tuning for Continual Learning
- `2609.26242` [cs.LG；合同类含New] Can You Delete a Year of Market Data? Machine Unlearning Against Exact Retraining Oracles
- `2609.26231` [cs.LG；合同类含New] High-Order Liquid Evidence Modeling for Continuous and Subtle GNSS Spoofing Detection in Autonomous Driving
- `2609.26217` [cs.LG；合同类含New] MSA-CITE: A Co-Adapted LoRA Specialist Ecology for Fixed-Budget Small-Model Inference
- `2609.26216` [cs.LG；合同类含New] Beyond Imitation: Auditing the Recoverability of Reasoning in Distilled Models
- `2609.26214` [cs.LG；合同类含New] Bridging the Data Gap: Digital Twin as a New Paradigm for AI-based Radio Sensing
- `2609.26199` [cs.LG；合同类含New] Partially Observed Sparse Graphs: The Unknown Sampling Rate is a Tail Index
- `2609.26173` [cs.LG；合同类含New] Component Type, Not Reconstruction Error, Predicts Attention Quantization Sensitivity
- `2609.26167` [cs.LG；合同类含New] Activation-Energy Pruning for Spiking Neural Networks: Unsupervised Personalization via Spike-Count Saliency
- `2609.26165` [cs.LG；合同类含New] Spectral Tail Interventions in Decoder-Only Language Models: Reasoning-Sensitive Weight Structure from Controlled Surgery
- `2609.26147` [cs.LG；合同类含New] Block-Level Weight-Space Structure Persists Under Post-Training: An Empirical Study Across LLM Families
- `2609.26146` [cs.LG,cs.MA；合同类含New] From Risk Scoring to Risk Allocation: A Density-Driven Framework for Diverse Monitoring in Multi-Agent Systems
- `2609.26112` [cs.LG,cs.AI；合同类含New] Certified Mechanistic Interpretability: Lifting Single-Input Findings to Bounded Neighbourhoods
- `2609.26094` [cs.LG；合同类含New] CoEvo: Oracle-Grounded Self-Evolution of a Single Model for Multi-Step Causal Reasoning
- `2609.26081` [cs.LG,cs.CV；合同类含New] Margin-Drop Coordinates for Cross-Budget Robustness Evaluation
- `2609.26077` [cs.LG；合同类含New] Fast Matrix Multiplication in fp8: Certified Coefficient Optimization and Measured Error
- `2609.26067` [cs.LG；合同类含New] FuncCode: Compressing Kolmogorov--Arnold Networks in Function Space with Hardware-Aware Quantization
- `2609.26063` [cs.LG；合同类含New] Towards Adaptive Federated Graph Clustering: A Global Community-aware Contrastive Learning-based Approach
- `2609.26037` [cs.LG,cs.AI；合同类含New] xWhyL: Causal Interactive Learning
- `2609.26021` [cs.LG；合同类含New] BOBA: Dynamic Bayesian Optimization through Bayesian Active Inference
- `2609.26018` [cs.LG；合同类含New] The Dynamics of Quasiregular Neural Learning
- `2609.25987` [cs.LG；合同类含New] Theory for groupoid equivariant neural networks: an approach for steerable CNNs on bounded domains
- `2609.25980` [cs.LG,cs.AI；合同类含New] Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models
- `2609.25963` [cs.LG；合同类含New] GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression
- `2609.25962` [cs.LG；合同类含New] Exploring Solver-Level Warmstarting for Neural Network Verification
- `2609.25916` [cs.LG；合同类含New] Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement
- `2609.25914` [cs.LG；合同类含New] AURA: Angular Update Rate Adaptation for training complex-valued neural networks
- `2609.25876` [cs.LG,cs.AI；合同类含New] Evaluating the Effectiveness of SechKAN on 1D Data
- `2609.25874` [cs.LG；合同类含New] Neural Approximation by Function Composition: Rigidity and Doubly Exponential Convergence
- `2609.25839` [cs.LG；合同类含New] Gaussian Flow-Matching Schedules: Implications for Sampling and Training
- `2609.25836` [cs.LG,cs.AI；合同类含New] In-Context Guidance: Learning Inter-Task Synergies via Numerical Foundational Models for Few-Shot Multitask Optimization
- `2609.25827` [cs.LG；合同类含New] Protocol before progress: leakage-aware evaluation of AIS trajectory prediction
- `2609.25814` [cs.LG；合同类含New] CacheDyG: Decoupling Temporal Propagation for Efficient Dynamic Graph Learning
- `2609.25811` [cs.LG；合同类含New] Multi-View Fair Clustering Guided by Cross-View Sensitive Information Discrepancy
- `2609.25809` [cs.LG,cs.AI；合同类含New] You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs
- `2609.25788` [cs.LG,cs.AI；合同类含New] Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models
- `2609.25781` [cs.LG；合同类含New] A Lightweight Plastic-Memory Framework for Graph Few-Shot Class-Incremental Learning
- `2609.25777` [cs.LG；合同类含New] Disentangling Heterogeneous Traffic Dynamics for Multi-Step Traffic Forecasting via Adaptive Spectral Decomposition
- `2609.25757` [cs.LG,cs.RO；合同类含New] Minimal Recurrent Behavioral Memory for Imitation under Partial Observability
- `2609.25745` [cs.LG；合同类含New] Modular Norm RandOpt: Population-Efficient Ensembling through Architecture-Aware Perturbations
- `2609.25735` [cs.LG,cs.AI；合同类含New] Beyond Class Marginals: Bounding Rehearsal Gaps without Freezing Class Co-occurrence
- `2609.25728` [cs.LG,cs.AI；合同类含New] Self-Supervised Combinatorial Optimization with Constraints via Frank-Wolfe
- `2609.25722` [cs.LG；合同类含New] Signed Graph Pre-Training and Prompt Learning
- `2609.25701` [cs.LG,cs.MA；合同类含New] Fully Byzantine-Resilient Multi-Agent Reinforcement Learning
- `2609.25692` [cs.LG；合同类含New] Graph Domain Adaptation Does Not End with Representation Learning
- `2609.25675` [cs.LG；合同类含New] Marginal Log-Likelihood Increments under Dirichlet-Smoothed Markov Estimation
- `2609.25659` [cs.LG；合同类含New] When Riemann flows with Wasserstein: Generative Modeling of Probability Distributions on Manifolds
- `2609.25657` [cs.LG；合同类含New] Targeted Review for AI-Assisted Biodiversity Surveys: Active Continuous-Score Occupancy Modeling
- `2609.25655` [cs.LG,cs.AI；合同类含New] From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs
- `2609.25634` [cs.LG,cs.AI；合同类含New] An Exploratory Replica-Overlap Probe of the Grokking Transition
- `2609.25623` [cs.LG,cs.AI；合同类含New] What Should a Self-Teacher See? Privileged Context Design for On-Policy Self-Distillation
- `2609.25582` [cs.LG,cs.AI；合同类含New] EMGBlend: Heterogeneity-Aware Self-Supervised Pretraining for Gesture and Force Decoding
- `2609.25569` [cs.LG；合同类含New] SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling
- `2609.25542` [cs.LG,cs.AI；合同类含New] DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks
- `2609.25541` [cs.LG,cs.AI；合同类含New] A JEPA Recipe for Tabular Foundation Models
- `2609.25510` [cs.LG,cs.AI；合同类含New] Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training
- `2609.25501` [cs.LG；合同类含New] Continuous Optimization for p-adic Models
- `2609.25484` [cs.LG；合同类含New] Learning Defensive Policies against Diverse Inference Attacks for Smart Meter Privacy
- `2609.25482` [cs.LG,cs.AI；合同类含New] Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining
- `2609.25471` [cs.LG,cs.AI；合同类含New] A Practical Recipe for Semi-Supervised Federated ASR: Online Pseudo-Labels with Server Update Stabilization
- `2609.25444` [cs.LG,cs.CV；合同类含New] Mean Velocity Matching: Rethinking Generative Dynamics in Diffusion Models
- `2609.25438` [cs.LG；合同类含New] PermuFormer: Multi-Task Pretraining for Permutation Representation in Algebraic Combinatorics
- `2609.25433` [cs.LG,cs.AI；合同类含New] Lightweight Ranking Heads: Accelerating Multi-Task Experimentation in Production Recommender Systems
- `2609.25430` [cs.LG,cs.AI；合同类含New] Predictive Uncertainty for Neural CAE Surrogates
- `2609.25397` [cs.LG,cs.AI；合同类含New] Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing
- `2609.25373` [cs.LG；合同类含New] Extending FunctionGemma for Practical On-Device Mobile Function Calling
- `2609.25340` [cs.LG；合同类含New] Concept Drift from a Causal Perspective
- `2609.25334` [cs.LG,cs.CV；合同类含New] MT-ProtBERT: Multi-task Learning ProtBERT for Intrinsically Disordered Proteins Classification with Scarce Data
- `2609.25326` [cs.LG；合同类含New] Spatiotemporal Kronecker Covariance Neural Networks
- `2609.25310` [cs.LG；合同类含New] Topological Signal Processing With Unoriented Operators
- `2609.25297` [cs.LG；合同类含New] Correcting Within-Group Self-Selection Bias in Prioritized Replay
- `2609.25179` [cs.LG,cs.AI；合同类含New] Multi-Term Fourier Graph Neural Network with Sample Relationship Learning for Enhanced Remaining Useful Life Prediction
- `2609.25166` [cs.LG,cs.AI；合同类含New] Mitigating Sequential Reappearance in Diffusion Data-Point Unlearning
- `2609.25163` [cs.LG；合同类含New] Learning Neural Feedback Linearization for Data-driven Systems via Augmented Lagrangian
- `2609.25152` [cs.LG,cs.AI；合同类含New] Exposing Blind Spots in Deep Imbalanced Regression Evaluation
- `2609.25149` [cs.LG；合同类含New] Dual-GNN Multilevel Coarsening for Maximum Independent Set
- `2609.25146` [cs.LG,cs.AI；合同类含New] Brain-Inspired Hierarchical Modularity for General Continual Learning
- `2609.25143` [cs.LG,cs.AI；合同类含New] Stable Unsupervised Continual Chunking with Sheaf SyncMap
- `2609.25134` [cs.LG,cs.AI；合同类含New] The Probabilistic Structure of Large Language Models
- `2609.25131` [cs.LG；合同类含New] Entropy Can Flow, or It Can Guide. Be Entropy. LEDFlow: Introducing Entropy-guided Generation Order into Uniform Discrete Flow
- `2609.25082` [cs.LG,cs.DC,cs.AI；合同类含New] Federating Quantum and Classical Computing: A Privacy-Preserving Hybrid Approach
- `2609.26783` [cs.LG；合同类Cross-only] A Decentralized Partially Observable Team Decision Methodology with Delayed Information Sharing
- `2609.26779` [cs.LG,cs.AI；合同类含New] CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
- `2609.26748` [cs.LG；合同类Cross-only] Automatic depth-based local center clustering via $β$-integrated local depth and adaptive grouping
- `2609.26737` [cs.LG；合同类Cross-only] Diffusion-Induced Spatial Attention Overlapping Community Detection
- `2609.26707` [cs.LG；合同类Cross-only] Optimal Sequential Annotations for Off-Policy Evaluation
- `2609.26705` [cs.LG；合同类Cross-only] When are bosonic Gaussian states classical to learn?
- `2609.26683` [cs.LG；合同类Cross-only] PROSWIN: Probabilistic Solar Wind Speed Forecasting Using Deep Distributional Regression From Solar Images
- `2609.26647` [cs.LG；合同类Cross-only] Statistical Rates for Entropic Optimal Transport in the Discrete to SubGaussian Regime
- `2609.26642` [cs.LG,cs.AI；合同类含New] The Delegation Blind Spot: Auditing Product Decisions from Agent Choices
- `2609.26624` [cs.LG；合同类Cross-only] On Basis Function Selection for Sparse Gaussian Process Regression
- `2609.26617` [cs.LG,cs.CV；合同类含New] MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction
- `2609.26605` [cs.LG,cs.CV；合同类含New] Foundation model embeddings capture pre-diagnostic changes on screening mammograms
- `2609.26598` [cs.LG；合同类Cross-only] Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models
- `2609.26590` [cs.LG,cs.CV；合同类含New] GTR: Gated Token Recurrence for Efficient Dense Prediction
- `2609.26581` [cs.LG；合同类Cross-only] Polyak-Type Extragradient Methods for Monotone Root-Finding Problems
- `2609.26502` [cs.LG；合同类Cross-only] Deep Generative Crystal Structure Prediction: A Benchmark Study and a Controlled Test of Prototype Dependence
- `2609.26474` [cs.LG,cs.AI,cs.CV；合同类含New] PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices
- `2609.26457` [cs.LG,cs.AI；合同类含New] Recursive self-improvement of AI research agents
- `2609.26445` [cs.LG；合同类Cross-only] A Practical Guide on Graphical Model Validation
- `2609.26406` [cs.LG；合同类Cross-only] SuperPCA: subspace analysis and an efficient algorithm for high-dimensional PCA
- `2609.26378` [cs.LG,cs.AI,cs.CV,cs.RO；合同类含New] MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation
- `2609.26361` [cs.LG,cs.AI；合同类Cross-only] GitScholar: A Dataset for Predicting AI Research Impact from GitHub Engagement
- `2609.26352` [cs.LG；合同类Cross-only] HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning
- `2609.26326` [cs.LG；合同类Cross-only] Error Bounds for Statistical Estimators in BTL Model with Parametric Multivariate Utility Functions
- `2609.26303` [cs.LG；合同类Cross-only] Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target
- `2609.26290` [cs.LG；合同类Cross-only] Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining
- `2609.26270` [cs.LG,cs.PL；合同类Cross-only] Sample-Smooth Spaces: A Convenient Category for Differentiable Probabilistic Programming
- `2609.26244` [cs.LG,cs.AI；合同类含New] A Multi-Timestep LSTM Ensemble regressor for Enhanced Short-Term Runoff Prediction
- `2609.26243` [cs.LG,cs.AI；合同类含New] A Hybrid AI Framework for Academic Advising: Integrating Ensemble-Based Grade Prediction and a Rule-Based Expert System
- `2609.26219` [cs.LG,cs.DC；合同类含New] PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts
- `2609.26193` [cs.LG,cs.AI；合同类含New] Identifying Intelligent Processes via Online Sequential Testing
- `2609.26166` [cs.LG,cs.AI,cs.CV；合同类含New] MGRL-RSCC: Multi-Granularity Reward Reinforcement Learning for Fine-Grained Remote Sensing Change Captioning
- `2609.26143` [cs.LG,cs.IR；合同类含New] TailSpec-EASE: Knowledge-Graph-Regularized Linear Recommendation for Web Long-Tail Discovery
- `2609.26069` [cs.LG,cs.AI；合同类含New] RankCert: When Can Simulated Learners Safely Select an AI Tutor? Robust Decision Certification Under Structural Uncertainty
- `2609.26068` [cs.LG；合同类Cross-only] Differentiable Policy Transport over Multi-Layer Network Feasibility Geometry
- `2609.26039` [cs.LG,cs.AI,cs.CV；合同类含New] EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion
- `2609.26032` [cs.LG；合同类Cross-only] Hyperbolic Restricted Boltzmann Machine Neural Quantum State
- `2609.25978` [cs.LG,cs.CV；合同类含New] Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study
- `2609.25947` [cs.LG；合同类Cross-only] Bridge of $Ψ$'s: Quantum Circuit Optimization with Schrödinger Bridges
- `2609.25924` [cs.LG；合同类Cross-only] Conditional Tensor Diffusion: Distributional Counterfactual Learning and Inference
- `2609.25845` [cs.LG,cs.CV；合同类含New] Visual Jev: Accurate and Efficient Decisions from Shared Visual Context
- `2609.25820` [cs.LG,cs.RO；合同类含New] Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models
- `2609.25778` [cs.LG；合同类Cross-only] Statistical Gains from Looped Estimation under Parameter Budgets
- `2609.25776` [cs.LG；合同类Cross-only] Graded Representation Theory of Equivariant Neural Networks
- `2609.25710` [cs.LG；合同类Cross-only] Optimal Tradeoffs Between Network Size and Parameter Magnitude in Neural Approximation and Minimax Regression
- `2609.25705` [cs.LG；合同类Cross-only] On the Gradient Heterogeneity Dynamics of Adversarially Robust Federated Regression
- `2609.25678` [cs.LG,cs.AI；合同类含New] Toolcompass: Guiding Tool Trialing, Not Suppressing It
- `2609.25654` [cs.LG,cs.CV,cs.RO；合同类含New] CODA: Depth-Aligned Scene Completion and Object Decomposition from a Single RGB-D Image
- `2609.25643` [cs.LG,cs.AI；合同类含New] Ladders of Thought: A Self-Evolving Curriculum of Progressively Simplified Reasoning Traces
- `2609.25624` [cs.LG,cs.AR；合同类含New] Accelerating the Mitigation of LLM Inference Nondeterminism Across GPU Architectures
- `2609.25605` [cs.LG；合同类Cross-only] Generalized Deep Regression for Repeated Measurements
- `2609.25588` [cs.LG,cs.AI；合同类含New] Transformer Heads Looking for Order
- `2609.25576` [cs.LG；合同类Cross-only] Scalable Minimum-Volume Simplex Estimation with Non-asymptotic Analysis
- `2609.25567` [cs.LG,cs.AI,cs.CV；合同类含New] RootQuantV2: Adapting a Vision Foundation Model for Root-Trait Regression from Minirhizotron Imagery
- `2609.25558` [cs.LG,cs.RO；合同类含New] HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery
- `2609.25546` [cs.LG；合同类Cross-only] Synthesis and editing of multi-instrument audio mixtures using scalar-quantised latents with MIDI Span conditioning
- `2609.25505` [cs.LG；合同类Cross-only] FAST-ML: A Hybrid Physics-Machine Learning Framework for Tropical Cyclone Intensity Forecasting
- `2609.25490` [cs.LG,cs.CV；合同类含New] SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation
- `2609.25454` [cs.LG,cs.CV；合同类含New] MIND the Gap: A Geographic Implicit Neural Representation with Adjustable Spatial Scale
- `2609.25442` [cs.LG,cs.DC；合同类含New] WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning
- `2609.25411` [cs.LG；合同类Cross-only] Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis
- `2609.25408` [cs.LG,cs.AI,cs.IR；合同类含New] From Offline Proxies to Online Decisions: A Layered Engagement Evaluation Framework for Conversational AI
- `2609.25388` [cs.LG,cs.AI；合同类Cross-only] PICPIs: Prediction-Interval-Conditional Prediction Intervals
- `2609.25386` [cs.LG,cs.CV；合同类含New] Sex Estimation from Footwear Outsole Impressions Using CNN Transfer Learning and Interpretable Image Statistics
- `2609.25381` [cs.LG；合同类Cross-only] Penalized Nonreversible Langevin for Constrained Sampling
- `2609.25352` [cs.LG；合同类Cross-only] SSP-Bench: A Hybrid Data Generation Framework for Safety, Security, and Privacy Evaluation
- `2609.25351` [cs.LG,cs.RO；合同类含New] Learning from Humans for Proactive Assistance in Human-Robot Collaborative Transport
- `2609.25338` [cs.LG,cs.RO；合同类含New] GINIO: A Geometric SO(3)-Equivariant Interface for Neural Inertial Odometry
- `2609.25285` [cs.LG,cs.AI；合同类含New] Attention as a Routing Graph: Live Circuit Extraction from a Single Forward Pass
- `2609.25155` [cs.LG；合同类Cross-only] Empirical Auditing of Edge-Private Graph Generators
- `2609.25145` [cs.LG；合同类Cross-only] Variational objectives for amortized Bayesian inference in inverse problems: The role of posterior conditioning
- `2609.25144` [cs.LG；合同类Cross-only] The Informational Content in Lepto-Variance and Its Relation to Higher Moments
- `2609.25138` [cs.LG,cs.CV；合同类Cross-only] Calibration Count Reuse: Validity Does Not Determine Efficiency
- `2609.25123` [cs.LG,cs.AI,cs.CV；合同类Cross-only] WILSON - a pathology foundation model framework for patient-level analysis and diagnostic text generation
- `2609.25088` [cs.LG,cs.AI；合同类含New] An Accurate and Interpretable Hyper Graph Neural Network for GBM Survival Prediction
- `2609.25085` [cs.LG；合同类Cross-only] FREESIA: Covariance-Aware Posterior Transport for Expressive and Scalable Data Assimilation
- `2609.25067` [cs.LG,cs.CV；合同类含New] SPARC: SuperPixel-Aware Region Contrastive Learning for Self-Supervised Dense Prediction
- `2609.25057` [cs.LG,cs.AI；合同类Cross-only] Physics-guided deep metric learning with continuous time embeddings for open-world radar pulse de-interleaving
- `2609.25044` [cs.LG；合同类Cross-only] End-to-End Quantum Semantic Communication with Variational Quantum Neural Networks
- `2609.25039` [cs.LG；合同类Cross-only] What Does Chain-of-Thought Entropy Measure? A Channel Audit of Scaffolding, Routing, and Content
- `2609.25014` [cs.LG,cs.AI；合同类Cross-only] Not All 4-bit Quantizers Are Equal: Deployment-Time Mitigation of PII Leakage in Fine-Tuned Small Language Models
- `2609.24194` [cs.LG；合同类Cross-only] When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits
- `2609.22822` [cs.LG；合同类Cross-only] From IceCube to IT-Sphere: A Hybrid Quantum-Classical GNN for Banking IT Root Cause Analysis
- `2609.26616` [cs.DC,cs.PF；合同类含New] Seeking Cost-Optimal Infrastructure Size for Distributed Filesystems: A Ceph Case Study
- `2609.26602` [cs.DC；合同类含New] A Configurable Heuristic for the MLCS Problem
- `2609.26476` [cs.DC；合同类含New] Don't let your Memory defy you: Fragmentation-Aware Serverless Allocation with Elastic Memory Locality
- `2609.26363` [cs.DC；合同类含New] DHSched: Stateless Control for Stateful Real-Time Avatar Serving
- `2609.26190` [cs.DC；合同类含New] Distributed Near-Equitable Coloring in the LOCAL Model
- `2609.25918` [cs.DC；合同类含New] Hydrozoan: Latency-Adaptive DAG Consensus under Mixed Byzantine and Crash Faults
- `2609.25560` [cs.DC；合同类含New] Co-Fabric: Breaking Host-Domain Boundaries for Unified xPU Interconnection
- `2609.25479` [cs.DC；合同类含New] Adaptive and Cost-Efficient Joint Scheduling of UAV Routes and Analytics with Transit-Borne Fog
- `2609.25451` [cs.DC；合同类含New] Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo
- `2609.25415` [cs.DC；合同类含New] Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI
- `2609.26788` [cs.DC；合同类Cross-only] Quantum Advantage for Distributed Symmetry Breaking
- `2609.26763` [cs.DC,cs.PF；合同类含New] SARA: SLO-Aware Resource Allocation for Disaggregated Agentic LLM Services
- `2609.26080` [cs.DC,cs.MA；合同类含New] The Fleet Is the Model: Engineering Collective Intelligence with Fusion-MoA Pioneer R1
- `2609.25949` [cs.DC；合同类Cross-only] Flux: Optimal Scheduling of Optical Circuit Switches for LLM Training
- `2609.25817` [cs.DC；合同类Cross-only] Lizard: Bandwidth-Adaptive Real-Time Video Analytics through Content-Aware Packet Discarding at Last-Mile Edge Routers
- `2609.25463` [cs.DC,cs.AI；合同类含New] Rollout Efficiency in Reinforcement Learning for Reasoning Large Language Models: A Taxonomy and Future Directions
- `2609.25443` [cs.DC,cs.AI；合同类含New] ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes
- `2609.25437` [cs.DC；合同类Cross-only] Data center cooling choices shift water impacts across the grid: An integrated water-energy model for sustainable data center development
- `2609.25043` [cs.DC；合同类Cross-only] Encrypted Redundancy as a Diagnostic Resource: Relational Diagnosis in Quantum Encrypted Cloning
- `2609.07204` [cs.DC；合同类Cross-only] Agentic Algorithm Engineering: Improving Shared-Memory Exact Minimum Cuts
- `2609.26777` [cs.AI；合同类含New] SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving
- `2609.26760` [cs.AI；合同类含New] Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents
- `2609.26758` [cs.AI；合同类含New] Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It
- `2609.26565` [cs.AI；合同类含New] Quantum-Aided Active Device Detection in Energy-Harvesting Symbiotic Radio Networks
- `2609.26556` [cs.AI；合同类含New] Neutral-Atom-based Quantum Optimization for Resource Allocation in NOMA Networks
- `2609.26550` [cs.AI；合同类含New] JEV-as-a-Judge: Accept When Confident, Escalate When Unsure
- `2609.26532` [cs.AI；合同类含New] REFLEX with Jev for Efficient Selective Control in LLM Agents
- `2609.26461` [cs.AI；合同类含New] Reproducible AI Requires Reproducible Randomness
- `2609.26428` [cs.AI；合同类含New] The Source of Disturbance Matters: External, Internal, and Control-Generated Noise in Adaptive Regulation
- `2609.26419` [cs.AI；合同类含New] Reliability Theory for AI Control
- `2609.26293` [cs.AI；合同类含New] Dual-Frontier: When Can an Agent Trust Its World Model?
- `2609.26279` [cs.AI；合同类含New] FISSION: Label Augmentation for Bot Detection
- `2609.26268` [cs.AI；合同类含New] Decoupling Is Not Identification: Supervised Evidential Learning in Next-Token Prediction
- `2609.26261` [cs.AI；合同类含New] Coding Agents are Strong Prompt Optimizers
- `2609.26213` [cs.AI；合同类含New] Improved Multiplayer Bandit Algorithm for Bernoulli Rewards
- `2609.26207` [cs.AI；合同类含New] RCShift: Certifying When Partial Linkage Suffices for Finite-Sample Decisions
- `2609.26187` [cs.AI；合同类含New] TREND-10K: A Comprehensive Dataset for Next-Generation Video Quality Assessment Based on Preference-Driven Media
- `2609.26175` [cs.AI；合同类含New] EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models
- `2609.26160` [cs.AI；合同类含New] The Free-Recipe Limit: Every Recipe Effect Measures Which Premise of an Idealised Learner Broke
- `2609.26157` [cs.AI,cs.RO；合同类含New] Toward User-Mediated Self-Repair in Ubiquitous Robots Through Goal-Oriented Agentic AI
- `2609.26145` [cs.AI；合同类含New] Unanimity Without Persuasion: A Single Round of Debate Erases the Disagreement That Verification Needs
- `2609.26144` [cs.AI；合同类含New] When Verifiers Vote Backwards under Verdict Substitution: Signed Pivotal Value in Correlated Self-Consistency
- `2609.26135` [cs.AI,cs.MA；合同类含New] VACS: Value-Aligned Compositional Shielding for Multi-Agent Reasoning
- `2609.26126` [cs.AI；合同类含New] The Cost of Conservation: Coordination-Memory Laws for Exact-Support Generation
- `2609.26125` [cs.AI；合同类含New] When Big Data Becomes a Curse: Spatial Heterogeneity and the Limits of Learning from Passive Acoustic Monitoring Data
- `2609.26124` [cs.AI；合同类含New] MAC-RRG: Iterative Multi-Agent Collaboration for X-ray Radiology Report Generation
- `2609.26123` [cs.AI；合同类含New] FairMon: A Tool for Monitoring and Visualizing Algorithmic Fairness
- `2609.26106` [cs.AI；合同类含New] Early Prediction of Pathological Complete Response to Neoadjuvant Chemotherapy Using Temporal Deep Learning on DWI
- `2609.26105` [cs.AI,cs.CV；合同类含New] Neoadjuvant chemotherapy response prediction using pretreatment diffusion and contrast-enhanced magnetic resonance imaging with clinical variables
- `2609.26095` [cs.AI,cs.CV；合同类含New] FusionMMT: A Unified Multimodal and Multitask Learning Framework for Nuclear Fusion
- `2609.26087` [cs.AI；合同类含New] The Architect, the Adversary, and the Judge: Closed-Loop Generation of Standards-Aligned Assessment Items at Scale
- `2609.26076` [cs.AI；合同类含New] Selection-Invariant Communication Compilers for Privacy-Aware Multi-Agent LLM Workflows
- `2609.26060` [cs.AI；合同类含New] ChainUQ: Reasoning Consistency-Aware Uncertainty Quantification for Large Language Models
- `2609.26059` [cs.AI,cs.MA；合同类含New] Adversarial Course-of-Action Generation: Game-Theoretic Multi-Agent Algorithms for COA matching & COA generation
- `2609.26046` [cs.AI；合同类含New] Canonical locks that encode part-whole hierarchies
- `2609.26029` [cs.AI；合同类含New] CQ4OE: A benchmark for assessing LLM-assisted ontology generation from competency questions
- `2609.26015` [cs.AI；合同类含New] VideoX-Qwen: Data-Centric Instruction-Based Video Editing
- `2609.25960` [cs.AI；合同类含New] CausalLoss-Fin: Attributing Financial-Agent Loss to Decisions and Infrastructure Faults
- `2609.25873` [cs.AI,cs.AR；合同类含New] AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing
- `2609.25852` [cs.AI；合同类含New] Prediction Is Not Detection: Evaluating Pre-Recognition Claims in Longitudinal Clinical AI
- `2609.25848` [cs.AI；合同类含New] Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts
- `2609.25806` [cs.AI；合同类含New] When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention
- `2609.25804` [cs.AI；合同类含New] The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks
- `2609.25769` [cs.AI；合同类含New] Towards Omni-dimensional GUI Agent Navigation with Masked Trajectory Prediction
- `2609.25766` [cs.AI；合同类含New] Neurosymbolic Action Model Learning under Partial Observability
- `2609.25760` [cs.AI；合同类含New] The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance
- `2609.25738` [cs.AI；合同类含New] OmniFysics-Nano-V2 Technical Report: Understanding the Physical World Across Modalities
- `2609.25715` [cs.AI；合同类含New] LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data
- `2609.25712` [cs.AI；合同类含New] TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs
- `2609.25677` [cs.AI；合同类含New] Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing
- `2609.25647` [cs.AI；合同类含New] Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark
- `2609.25620` [cs.AI；合同类含New] ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research
- `2609.25618` [cs.AI；合同类含New] Reasoning-Preserving Fine-Tuning of Post-RL LLMs with Null-Basis LoRA
- `2609.25607` [cs.AI；合同类含New] ArticleMiner: Ontology-Guided Knowledge Graph Construction from Scientific Publications
- `2609.25591` [cs.AI；合同类含New] Evaluating Coding Agents on Kernel Exploit Generation
- `2609.25581` [cs.AI；合同类含New] Gaze responses to false-positive computer-aided detection prompts during colonoscopy: a paired-video and real-time eye-tracking study
- `2609.25575` [cs.AI；合同类含New] Direct Optimization of Generators for Search in Automated Theorem Proving
- `2609.25572` [cs.AI；合同类含New] A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators
- `2609.25570` [cs.AI；合同类含New] Recovering Agentic Sovereignty: Mitigating the Consensus Paradox via Contrastive Epistemic Decoding
- `2609.25555` [cs.AI；合同类含New] Weakly Supervised Quantum Error Mitigation
- `2609.25508` [cs.AI；合同类含New] SMTB: Fast Structure-Mapping with Tight Bounds
- `2609.25496` [cs.AI；合同类含New] Towards participatory speech dataset curation: A queer case study and conceptual framework
- `2609.25491` [cs.AI；合同类含New] Queer inclusion in speech datasets: An audit and taxonomy of practical tensions
- `2609.25474` [cs.AI；合同类含New] Spectra: A Rules-Driven LLM Pipeline for Automated KYC Document Processing
- `2609.25469` [cs.AI；合同类含New] RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation
- `2609.25467` [cs.AI；合同类含New] ShowTellArena: Evaluating Business Workflow Understanding from Demonstrations
- `2609.25466` [cs.AI；合同类含New] Real-Time Hand Gesture Recognition for OpenXR Using Transformer-Based Machine Learning
- `2609.25400` [cs.AI；合同类含New] Robust Failure, Conservative Repair: Textual Knowledge Distillation from Cross-Model Failures
- `2609.25366` [cs.AI；合同类含New] From Decorative to Load-Bearing: Task Difficulty Shapes the Causal Role of Chain-of-Thought
- `2609.25337` [cs.AI；合同类含New] Clarification Is Not Correction: LLMs Fail to Let Go
- `2609.25303` [cs.AI；合同类含New] Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing
- `2609.25299` [cs.AI；合同类含New] Making Agents More Consistent: Skills Should Form Habits for Repeat Tasks
- `2609.25286` [cs.AI；合同类含New] Learned Enterprise Data Comprehension: Compression and Routing for Data Agents
- `2609.25284` [cs.AI；合同类含New] When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning
- `2609.25272` [cs.AI；合同类含New] MedGate-Fusion: Integrating First-Encounter Semantic Narratives and Physiological Biomarkers for Prospective Stroke Risk Stratification
- `2609.25254` [cs.AI；合同类含New] The AI Neuroscientist: An Interactive Agentic Interface for Neuroimaging Analysis
- `2609.25199` [cs.AI；合同类含New] Lean Pool: An AI-Maintained Archive of Formalized Mathematics
- `2609.25187` [cs.AI；合同类含New] X-Planner: Event-Structured Task Planning for Embodied Intelligence
- `2609.25165` [cs.AI；合同类含New] Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings
- `2609.25036` [cs.AI；合同类含New] 4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting
- `2609.25013` [cs.AI；合同类含New] Do Existing Preconditioners Improve Biomedical Tabular Foundation Learning? An Empirical Study on TabPFN Optimization
- `2609.26761` [cs.AI；合同类Cross-only] A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem
- `2609.26756` [cs.AI,cs.CV；合同类含New] FleXray: Universal Clinical X-ray Segmentation
- `2609.26749` [cs.AI；合同类Cross-only] Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen
- `2609.26725` [cs.AI；合同类Cross-only] Does AI Save Time on Product Design? A Randomized Controlled Experiment of AI Prompt-to-Design Workflows
- `2609.26711` [cs.AI；合同类Cross-only] TraceVIC: Causal Reasoning over Code Evolution for Identifying Vulnerability-Inducing Commits
- `2609.26682` [cs.AI；合同类Cross-only] From Alignment to Access Control: A Framework for GenAI Policy Enforcement
- `2609.26562` [cs.AI；合同类Cross-only] The Disciplinary Language Transfer Problem: How Psychological Vocabulary Produces Governance Failures in AI Agent Deployment
- `2609.26547` [cs.AI；合同类Cross-only] Topology-Stratified Materials Discovery with A Flow-Based Generative Model
- `2609.26512` [cs.AI,cs.CV；合同类含New] Do Vision Model See Like the Brain? A Comparison Across EEG Encoding Model
- `2609.26507` [cs.AI；合同类Cross-only] The Ethics of Artificial Intelligence in Military Operations
- `2609.26492` [cs.AI,cs.CV；合同类含New] Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification
- `2609.26486` [cs.AI；合同类Cross-only] Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing
- `2609.26480` [cs.AI；合同类Cross-only] FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation
- `2609.26463` [cs.AI,cs.CV；合同类含New] Complementary Roles of Radiomics and Foundation Representations in Renal Cell Carcinoma Classification: A Comparative Study of 2D and 3D CT Encodings
- `2609.26425` [cs.AI,cs.CV；合同类含New] QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation
- `2609.26314` [cs.AI,cs.RO；合同类含New] TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models
- `2609.26295` [cs.AI；合同类Cross-only] On the security and privacy of LLMs in Mobility
- `2609.26274` [cs.AI,cs.CV；合同类含New] AIGC Video Detection based on the fusion of spatial-frequency-optical flow multimodal features
- `2609.26229` [cs.AI；合同类Cross-only] Reducing Hallucinations in Large Language Models Through Integrated Self-Verification and Retrieval-Augmented Generation
- `2609.26209` [cs.AI；合同类Cross-only] When Unpaired Sets Support Shared-Corruption Calibration: Moment Geometry and Two-Sample Precision
- `2609.26184` [cs.AI,cs.RO；合同类含New] Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems
- `2609.26176` [cs.AI；合同类Cross-only] Refusing Everything Looks Safe: Restoring the Benign Arm to Encoded-Prompt Evaluation
- `2609.26174` [cs.AI；合同类Cross-only] The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain
- `2609.26151` [cs.AI,cs.CV；合同类Cross-only] TTTIR: Unlocking Instance-Specific State Evolution via Test-Time Training for Image Restoration
- `2609.26131` [cs.AI,cs.RO；合同类含New] StepTrigger: Contact-State-Triggered Backdoor Attacks on VLM-Powered Legged Robots
- `2609.26072` [cs.AI；合同类Cross-only] Policy-Backed Selective Regeneration under Tainted Inter-Agent Communication
- `2609.26057` [cs.AI；合同类Cross-only] Observing the Conduct of Systematic Reviews with Generative AI Support: An Experience Report from a Graduate Software Engineering Course
- `2609.26056` [cs.AI,cs.CV；合同类含New] CricRAG: Retrieval Augmented Vision-Language Models for Personalized Cricket Coaching
- `2609.26028` [cs.AI；合同类Cross-only] REVE: Efficient Hallucination Correction for Large Audio-Language Models via Reused Encoder States
- `2609.26023` [cs.AI；合同类Cross-only] Reciprocal Collaboration: how lessons from convergence in GLAMs can enhance interdisciplinary AI research
- `2609.26016` [cs.AI；合同类Cross-only] Compiling Sufficient Governance Context from Declared Losses and Reachable States: Exact Observation-Contract Synthesis with Cardinality and Cost Objectives
- `2609.26007` [cs.AI,cs.RO；合同类含New] Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models
- `2609.26000` [cs.AI；合同类Cross-only] SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schrödinger Bridges
- `2609.25942` [cs.AI,cs.RO；合同类含New] Destination Support Restoration for Finite-Set Multimodal Trajectory Prediction
- `2609.25921` [cs.AI；合同类Cross-only] Toward Responsible AI-Augmented Cyber Defense: Pattern Recognition, Defense-in-Depth, and the Case for Human-AI Collaboration
- `2609.25891` [cs.AI,cs.CV；合同类含New] BAS-OPD: Budget-Aware Selective On-Policy Self-Distillation for Fine-Grained Multimodal Perception
- `2609.25889` [cs.AI；合同类Cross-only] Risk-Aware Online Conformal State Probing
- `2609.25821` [cs.AI；合同类Cross-only] CogenPVG: Cognitive-Enhanced Reflective Multi-Agent Framework for Persuasive Video Generation
- `2609.25815` [cs.AI,cs.CV；合同类含New] MorphoSHAP: Rethinking the Unit of Attribution in Explanation for Deep Visual Models
- `2609.25773` [cs.AI,cs.CV；合同类含New] Video-HopChain: Multi-Hop Questions and Confidence-Gated Exploration for Video Reasoning Models
- `2609.25697` [cs.AI,cs.CV；合同类含New] Interpretable AI plus Handheld, Portable Retinal Photographs: A Low-Cost Glaucoma Screening Solution for West Africa
- `2609.25674` [cs.AI,cs.RO；合同类含New] Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design on a Low-Cost Open Platform
- `2609.25641` [cs.AI；合同类Cross-only] When Quantum Meets AI: Quantum Methods for Machine Learning and Machine Learning Methods for Quantum Systems
- `2609.25586` [cs.AI；合同类Cross-only] Deflecting the Value Compass: Interacting with Large Language Models Temporarily Shifts Human Value Priorities Toward Personal Focus
- `2609.25563` [cs.AI；合同类Cross-only] AkasicMEM: Governed Enterprise Memory for Agents
- `2609.25562` [cs.AI,cs.RO；合同类含New] IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models
- `2609.25512` [cs.AI；合同类Cross-only] West-WRF AI 2-km: High-Resolution Prediction of Integrated Vapor Transport and Precipitation
- `2609.25492` [cs.AI,cs.CV；合同类含New] RGSQ: Riemannian Geometry-Sensitive Quantization for Large Vision-Language Models
- `2609.25460` [cs.AI；合同类Cross-only] Transformer-Informed Trajectory Optimization for Relative Motion in Cislunar Orbits
- `2609.25421` [cs.AI,cs.PL；合同类含New] Beyond Natural Language: An Agent-Native Language for Autonomous Science
- `2609.25376` [cs.AI,cs.RO；合同类含New] VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models
- `2609.25247` [cs.AI,cs.CV；合同类含New] Geometric and Semantic Coupling for Interaction Understanding in 3D Scenes
- `2609.25244` [cs.AI；合同类Cross-only] How Children Design and Reason about Trustworthy AI Chatbots
- `2609.25194` [cs.AI,cs.MA；合同类含New] Indirect tipping: a social attack surface in AI agent populations
- `2609.25189` [cs.AI,cs.IR；合同类含New] GroundedGEO: Auditing the Evidence Gap in Generative Search Rankings
- `2609.25154` [cs.AI；合同类Cross-only] Benchmarking Neural Defend ARCAS 1B: A Foundational Multimodal Deepfake Detection Model
- `2609.25150` [cs.AI；合同类Cross-only] Towards Sustainable Magnetic Resonance Imaging: Insights from long-term, high-resolution energy recordings across an entire scanner fleet
- `2609.25118` [cs.AI；合同类Cross-only] Rachel: A general-purpose language model directs and revises retrosynthetic routes
- `2609.25108` [cs.AI,cs.CV；合同类含New] You've Seen Enough: Quality-Constrained Image Coding for Machines
- `2306.02136` [cs.AI；合同类Cross-only] Financial sentiment analysis using FinBERT with application in predicting stock movement
- `2609.26793` [cs.CV；合同类含New] HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis
- `2609.26774` [cs.CV；合同类含New] StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training
- `2609.26733` [cs.CV；合同类含New] Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism
- `2609.26731` [cs.CV；合同类含New] ASTRA-SR: Atmospheric Seeing and Turbulence Restoration for Astronomical Image Super-Resolution
- `2609.26729` [cs.CV；合同类含New] GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation
- `2609.26702` [cs.CV；合同类含New] DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection
- `2609.26662` [cs.CV；合同类含New] Longitudinal Retinal Vascular Remodeling in Myopic Children Treated with Orthokeratology or Defocus Lenses: A Two-Year Comparative Study
- `2609.26636` [cs.CV；合同类含New] Laryngeal Structure Segmentation in High-Speed Videoendoscopy Using Deep Learning
- `2609.26623` [cs.CV；合同类含New] A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging
- `2609.26620` [cs.CV；合同类含New] GeoComposer: Geometry-Grounded Photographic Composition Instruction
- `2609.26578` [cs.CV；合同类含New] Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer
- `2609.26561` [cs.CV,cs.RO；合同类含New] Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation
- `2609.26549` [cs.CV；合同类含New] Latent Commonality Expectation-Maximisation for Box-supervised Tree Crown Instance Segmentation
- `2609.26513` [cs.CV；合同类含New] Virtual Encoders in Multimodal Transformers
- `2609.26505` [cs.CV；合同类含New] Semantically-Guided Domain Randomization for Industrial Object Detection in Low-Image-Budget Regimes
- `2609.26484` [cs.CV；合同类含New] From Token Importance to Conditional Removability: Rethinking Visual Token Pruning in Multimodal Large Language Models
- `2609.26458` [cs.CV；合同类含New] Code Plans, Diffusion Renders: Open-Ended Generative World Modeling
- `2609.26443` [cs.CV；合同类含New] Mammo-LIFE: Longitudinal Mammographic Imaging and Clinical Feature Enrichment for Post-Radiotherapy Outcome Prediction
- `2609.26430` [cs.CV；合同类含New] Latent Dataset Distillation for Human Motion Prediction
- `2609.26375` [cs.CV；合同类含New] KwaiMind Technical Report
- `2609.26334` [cs.CV；合同类含New] On the Role of the Projector in Contrastive Self-Supervised Learning: Last-Layer Rank Dynamics Drive Representation Quality
- `2609.26325` [cs.CV,cs.RO；合同类含New] Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping
- `2609.26299` [cs.CV；合同类含New] ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model
- `2609.26236` [cs.CV；合同类含New] COVER: Codec-Robust Video Watermarking with Generative Video Priors
- `2609.26233` [cs.CV；合同类含New] The Temporal Moderation Gap: Text-to-Video Safety Filters Are Blind to Harm in Motion
- `2609.26205` [cs.CV；合同类含New] LLaVA-Assessor: Building the Foundation LMM For Visual Quality Assessment
- `2609.26189` [cs.CV；合同类含New] Topology-Aware Parameter-Efficient Adaptation for Cross-Dataset Retinal Vessel Segmentation
- `2609.26188` [cs.CV；合同类含New] End-to-End Visual Odometry with RNNs and Attention
- `2609.26161` [cs.CV；合同类含New] Moving6DPoSe: A Multimodal Database for Monocular 6D Pose Estimation and Segmentation of Moving Objects
- `2609.26117` [cs.CV；合同类含New] Vorch-Human: Unified Multi-Task Human-Centric Generation via Long-Horizon Continuation
- `2609.26103` [cs.CV；合同类含New] MIAR: Medical Image Super-Resolution With Autoregressive Modeling
- `2609.26099` [cs.CV；合同类含New] Test-time Reinforcement Learning for Anomalous Video Understanding
- `2609.26093` [cs.CV；合同类含New] RECAP: Relation Evidence Calibration for Detecting Spatial Relation Hallucinations in Vision-Language Models
- `2609.26092` [cs.CV；合同类含New] Match One, Learn with Graph: One-to-Graph Query Collaboration with Backward Sharing for Object Detection
- `2609.26088` [cs.CV；合同类含New] BDSLI: A hybrid CNN-Transformer model for Bengali Sign Language interpretation
- `2609.26078` [cs.CV；合同类含New] ToW3D: Consistency-aware Interactive Point-based Mesh Editing on GANs
- `2609.26073` [cs.CV；合同类含New] Cellular-Communication-Level Interpretability for Pathology Foundation Models via Graph Distillation on Microenvironment
- `2609.26064` [cs.CV；合同类含New] SPEANet: Structural Prior Enhanced Attention Network for Parameter-Efficient Remote Sensing Object Detection
- `2609.25972` [cs.CV；合同类含New] NAWE: Digital Watermarking with Neural-Assisted Watermark Extraction
- `2609.25966` [cs.CV；合同类含New] GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration
- `2609.25945` [cs.CV；合同类含New] Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems
- `2609.25937` [cs.CV；合同类含New] Calibrating Retrieval Geometry: Reliability-Guided Training-Free Aggregation for Visual Place Recognition
- `2609.25930` [cs.CV；合同类含New] AT3D-AD: Anomaly Type-Aware 3D Anomaly Detection via Hierarchical Point-Language Alignment
- `2609.25907` [cs.CV；合同类含New] NaCR: Visual Localization via NeRF-aided Camera Ray Regression
- `2609.25881` [cs.CV；合同类含New] Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On
- `2609.25860` [cs.CV,cs.RO；合同类含New] MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving
- `2609.25850` [cs.CV；合同类含New] Less Is More in the Long Tail: Stage-Adaptive Sample Selection for Annotation-Efficient Dense Prediction
- `2609.25841` [cs.CV；合同类含New] Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes
- `2609.25837` [cs.CV；合同类含New] Identity-Centric Video Summarization via Hierarchical Fusion of Biometric, Appearance, and 3D Body Features
- `2609.25832` [cs.CV；合同类含New] PartLLM: A Unified Multimodal Foundation for 3D Part Segmentation
- `2609.25803` [cs.CV；合同类含New] LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction
- `2609.25793` [cs.CV；合同类含New] When Point Clouds Outperform Pixels: Rethinking Zero-Shot Multimodal Anomaly Detection
- `2609.25775` [cs.CV；合同类含New] TRACE: Trajectory Representation and Consistency Estimation for AI-Generated Video Detection
- `2609.25770` [cs.CV；合同类含New] Reading Right, Answering Wrong: How Visual Configuration Changes Affect Evidence Use in VLMs
- `2609.25743` [cs.CV；合同类含New] SAMI3D-DW: Interactive Segmentation of Any 3D Medical Images
- `2609.25741` [cs.CV；合同类含New] Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning
- `2609.25731` [cs.CV；合同类含New] Annual Earth-observation embeddings encode wildfire disturbance and support simplified burned area mapping
- `2609.25716` [cs.CV；合同类含New] FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance
- `2609.25693` [cs.CV；合同类含New] C2FXNet: Coarse-to-Fine Scene Expert for Unified Object Detection across Adverse Weather
- `2609.25685` [cs.CV；合同类含New] Initialization and Stopping Tolerance in CPU Dermoscopic Segmentation
- `2609.25684` [cs.CV；合同类含New] Real-Time Atomic-Resolution Electron Phase Imaging without Probe Calibration via Ptychography-Supervised Learning
- `2609.25652` [cs.CV；合同类含New] GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models
- `2609.25650` [cs.CV；合同类含New] Decoupling Disease, Covariates, and Individual Variability: A Unified Disentanglement Framework for Medical Image Classification
- `2609.25638` [cs.CV；合同类含New] What Drives Hierarchy-Aware Image Retrieval? Taxonomy Alignment, Objective Choice, and Geometry
- `2609.25635` [cs.CV；合同类含New] Shallow to Deep: Aligning Token Pruning with Stage-wise Roles in LVLMs
- `2609.25615` [cs.CV；合同类含New] Evidence-gated multimodal parsing and vectorization of architectural floor plans
- `2609.25604` [cs.CV；合同类含New] Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising
- `2609.25597` [cs.CV；合同类含New] Observer Choice and Threshold Selection in Retinal Vessel Segmentation: A Subject-Separated Evaluation
- `2609.25584` [cs.CV；合同类含New] Hi-OPD: Hierarchy-Aware Open-Prompt Detection for Remote Sensing Images
- `2609.25578` [cs.CV；合同类含New] Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction
- `2609.25538` [cs.CV；合同类含New] Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity
- `2609.25515` [cs.CV；合同类含New] Real-World Perception for Autonomous Driving in Adverse Weather: Enhancing Standard Detectors via Foundation-Guided Auto-Annotation
- `2609.25503` [cs.CV；合同类含New] SBMVTrack: Spike-Budgeted Multi-View Learning for Energy-Efficient UAV Tracking
- `2609.25500` [cs.CV；合同类含New] mbariml: a curation pipeline for turning deep-sea imagery and video into object-detection training data
- `2609.25453` [cs.CV；合同类含New] Combinatorial Network-Based Manifold Topological Deep Learning for Image Analysis
- `2609.25429` [cs.CV；合同类含New] Directional Total Variation-Regularized Implicit Neural Representations (DTV-INR) for Continuous Super-Resolution in Degraded Imaging Domains
- `2609.25331` [cs.CV；合同类含New] MirrorDistill: Illumination-Aware Latent Distillation for Efficient Low-Light Restoration
- `2609.25319` [cs.CV；合同类含New] Uncertainty-Aware 3D Residual Wavelet Diffusion for Ultra Low-Field MRI Super-Resolution
- `2609.25270` [cs.CV；合同类含New] RULER: Instance-aware Rubric Rewards for SVG Generation
- `2609.25267` [cs.CV；合同类含New] ImIR: Image-Instruction Tuning for All-in-One Image Restoration
- `2609.25017` [cs.CV；合同类含New] Deepfakes and Synthetic Media: Generation, Detection, and Governance
- `2609.26795` [cs.CV,cs.RO；合同类含New] ϕ-RIE: From Photorealistic Reconstruction to Interactive Environments
- `2609.26792` [cs.CV,cs.RO；合同类含New] DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving
- `2609.26648` [cs.CV；合同类Cross-only] ROAM-ASD: Robust Open-World Active Speaker Detection with Flexible Multimodal Fusion
- `2609.26567` [cs.CV,cs.RO；合同类含New] Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics
- `2609.26420` [cs.CV,cs.RO；合同类含New] Sample, Simulate, Select: Physics-in-the-Loop Text-to-Motion for Humanoids Without Training
- `2609.26168` [cs.CV；合同类Cross-only] TRACE: Transparent Retrieval for Abstract Concept Evaluation
- `2609.25884` [cs.CV；合同类Cross-only] LoRango: It Takes Two LoRAs to Unlock Hidden Behaviors in Diffusion Models
- `2609.25864` [cs.CV；合同类Cross-only] TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum
- `2609.25831` [cs.CV,cs.RO；合同类含New] Sometimes You Gotta Run Before You Can Walk: Run-then-Walk Scheduling Strategy for VLM Autonomous Driving
- `2609.25746` [cs.CV,cs.RO；合同类含New] Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking
- `2609.25633` [cs.CV；合同类Cross-only] Robust, Estimator-Agnostic Dynamic 3DGS Compression
- `2609.25627` [cs.CV,cs.RO；合同类含New] MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence
- `2609.25511` [cs.CV,cs.RO；合同类含New] A Deployment Study of Identity-Gated Drone Gesture Control
- `2609.25375` [cs.CV,cs.RO；合同类含New] PARTE: Plane-Assisted Robust Transformation Estimation for Point Cloud Registration
- `2609.25271` [cs.CV,cs.RO；合同类含New] Beyond the Flat Seafloor: A Closed-Form Two-View Constraint to Aid Sidescan Sonar Reconstruction
- `2609.25040` [cs.CV；合同类Cross-only] BananaVLM: A Domain-Adapted Vision Language Model for Banana Crop Disease Diagnosis
- `2609.25022` [cs.CV,cs.AR；合同类含New] NPLSD: Accelerating Line-Segment Detection on NPU Microcontrollers
- `2609.26766` [cs.RO；合同类含New] TM-APR: Thermal Temporal-Memory Localization via Analytic Online Adaptation
- `2609.26753` [cs.RO；合同类含New] Underwater Navigation in Unsteady Flows Using Measurement Histories from a Single Sensing Unit
- `2609.26672` [cs.RO；合同类含New] Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation
- `2609.26618` [cs.RO；合同类含New] NavSafe-$\infty$: Benchmarking Closed-Loop Driving Safety in Photorealistic Environments
- `2609.26580` [cs.RO；合同类含New] Wheel-loader V-Cycle Automation with Deep Koopman MPC
- `2609.26564` [cs.RO；合同类含New] Learning Air-Ground Motion Control with Temporal Mode Switching and Cross-Terrain Tracking
- `2609.26520` [cs.RO；合同类含New] MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection
- `2609.26499` [cs.RO；合同类含New] Generalizing Manipulation Skills with a Local Coding Agent
- `2609.26490` [cs.RO；合同类含New] Benchmarking Robots for Everyday Environments: From Lab Experiments to Real-World Operations
- `2609.26467` [cs.RO；合同类含New] RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy
- `2609.26423` [cs.RO；合同类含New] Dr-LiSA: Direct Radar-Lidar Scan Alignment for $SE(3)$ Localization
- `2609.26408` [cs.RO；合同类含New] SparseNav: Instruction-conditioned Sparse Semantic Perception for Training-Free Vision-Language Navigation
- `2609.26360` [cs.RO；合同类含New] Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering
- `2609.26315` [cs.RO；合同类含New] ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards
- `2609.26313` [cs.RO；合同类含New] SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation
- `2609.26304` [cs.RO；合同类含New] Shaft-Configuration-Adaptive Catheter Tip Position Estimation via Motor-History Conditioned Residual Learning
- `2609.26292` [cs.RO；合同类含New] RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?
- `2609.26267` [cs.RO；合同类含New] Multi-Axis Selective Decoupling Framework for Free-Floating Space Manipulators
- `2609.26256` [cs.RO；合同类含New] High-Bandwidth Biomimetic Finger for Tactile-Transparent Remote Texture Sensing
- `2609.26238` [cs.RO；合同类含New] Manipulation of Deformable Linear Objects Using Model Predictive Path Integral Control with Bidirectional Long Short-Term Memory Learning
- `2609.26155` [cs.RO；合同类含New] Toward Self-Repairing Ubiquitous Robots Using Goal-Oriented Agentic AI in Human-Robot Interactions
- `2609.26130` [cs.RO；合同类含New] Design and Implementation of an Ultra-Low-Cost Wall-Climbing Robot for Infrastructure Crack Detection
- `2609.26118` [cs.RO；合同类含New] GDLAM: Group-Disentangled Latent Action Model for Highly Disentangled Embodied Pretraining
- `2609.26085` [cs.RO；合同类含New] Acoustic Ellipses: Bio-Inspired Omnidirectional Echolocation in Cooperative Multi-Agent Systems using Frequency Sweeps
- `2609.26084` [cs.RO；合同类含New] Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments
- `2609.26083` [cs.RO；合同类含New] Situation Aware Locomotion for Dual Mobile Cobots in Shared Environments
- `2609.26071` [cs.RO；合同类含New] StrataVLA: Hierarchical and Efficient 3D Geometric Grounding for Vision-Language-Action Models
- `2609.26051` [cs.RO；合同类含New] Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations
- `2609.26004` [cs.RO；合同类含New] Manipulation with Stability Guarantees: Linear Deformable Objects with Non-negligible Physical Response Grasped at Multiple Location
- `2609.25994` [cs.RO；合同类含New] Safety-Constrained Model Predictive Control for an Omnidirectional Walking Assistive Robot Using Control Barrier Function
- `2609.25969` [cs.RO；合同类含New] Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance
- `2609.25961` [cs.RO；合同类含New] An Action Is Worth One Patch: Unified World-Action Modeling with PatchWAM
- `2609.25932` [cs.RO；合同类含New] Unsigned Distance Maps on 2D Point Cloud Registration
- `2609.25917` [cs.RO；合同类含New] Vision-based Underwater Formation Control With Input Saturations via Barrier Lyapunov Functions
- `2609.25905` [cs.RO；合同类含New] Control Barrier Functions for Safe Free-Flying Robotic Spacecraft Operations in Tumbling Target Capture
- `2609.25900` [cs.RO；合同类含New] You Should Be Properly Scoring Your Odometry
- `2609.25898` [cs.RO；合同类含New] Robust Active-Perception Control for Global-State-Free Aerial-Ground Cooperation
- `2609.25887` [cs.RO；合同类含New] What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation
- `2609.25813` [cs.RO；合同类含New] MOLA LiDAR-Inertial Odometry (MOLA-LIO) on the COMFORT Localization Benchmark
- `2609.25785` [cs.RO；合同类含New] VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation
- `2609.25756` [cs.RO；合同类含New] MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation
- `2609.25754` [cs.RO；合同类含New] PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning
- `2609.25750` [cs.RO；合同类含New] Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera
- `2609.25725` [cs.RO；合同类含New] AgriGen: Large-Scale Scene Generation Framework for Photorealistic Agricultural Robotics Simulation
- `2609.25724` [cs.RO；合同类含New] Designing an Efficient Excavator Bucket for Lunar ISRU: A Comparative Study with Vision-Based Fill and Displacement Analysis
- `2609.25709` [cs.RO；合同类含New] Zephyron: Integrated Design and Analytical Evaluation of a Solar-Assisted Mobile Manipulator for Multimodal Environmental Reconnaissance and Distributed Visual Inference
- `2609.25696` [cs.RO；合同类含New] The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers
- `2609.25695` [cs.RO；合同类含New] Induced Riemannian Metrics for Motion Planning with Constraints
- `2609.25689` [cs.RO；合同类含New] MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts
- `2609.25688` [cs.RO；合同类含New] MatcherCompass: A Deployment-Aware Benchmark to Guide Image Matcher Selection in the Wild
- `2609.25687` [cs.RO；合同类含New] SG-CPG: Severity-Gated Central Pattern Generators for Adaptive Quadruped Locomotion under Continuous Actuator Degradation
- `2609.25668` [cs.RO；合同类含New] CDKF-Track: Cluster-aware Data-Driven Kalman Filtering for Cooperative 3D Multi-Object Tracking
- `2609.25666` [cs.RO；合同类含New] Deploying Foundation Models for Embodied Navigation
- `2609.25658` [cs.RO；合同类含New] History-Conditioned Flow Matching for Probabilistic Dynamics of Tendon-Driven Continuum Robots
- `2609.25653` [cs.RO；合同类含New] PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation
- `2609.25649` [cs.RO；合同类含New] Skill Sequence Planning for Collaborative Multi-Robot Construction
- `2609.25642` [cs.RO；合同类含New] Contact-Stable Deformable Tissue Simulation Using Implicit Integration and Live-Pose Grasp Constraints for Laparoscopic Surgery Robot Policy Evaluation
- `2609.25639` [cs.RO；合同类含New] A Reconfigurable Bidirectional Cable-Driven Hip Exoskeleton with Swappable Bench/Backpack Dual-configuration Actuation
- `2609.25636` [cs.RO；合同类含New] RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents
- `2609.25631` [cs.RO；合同类含New] DynaForge: Planning-Guided Residual Learning for Dynamic Manipulation Demonstration Generation
- `2609.25630` [cs.RO；合同类含New] PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning
- `2609.25625` [cs.RO；合同类含New] From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations
- `2609.25619` [cs.RO；合同类含New] Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation
- `2609.25614` [cs.RO；合同类含New] A Deployable Four-Finger Payload for Teleoperated Free-Flying Manipulation with Astrobee
- `2609.25606` [cs.RO；合同类含New] CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing
- `2609.25577` [cs.RO；合同类含New] Recording Hand-Held Laparoscopic Instrument Motion in the Operating Room: Magnetometer-Free Fusion of Inertial, Range and Visual Sensing
- `2609.25527` [cs.RO；合同类含New] Digital Twin-Driven VR Teleoperation with Multi-View Spatial Perception for Surgical Robots
- `2609.25506` [cs.RO；合同类含New] RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation
- `2609.25486` [cs.RO；合同类含New] Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation
- `2609.25470` [cs.RO；合同类含New] A bioinspired internal model-based online estimator for planar pursuit
- `2609.25450` [cs.RO；合同类含New] REDACT: Robust Perceptive Locomotion under Unseen Visual Corruption
- `2609.25417` [cs.RO；合同类含New] Effects of Assistance Delay on Joint Mechanics and Energetics in Biological Torque Control of a Hip Exoskeleton
- `2609.25398` [cs.RO；合同类含New] Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture
- `2609.25374` [cs.RO；合同类含New] Angular momentum analysis on Karate roundhouse kicks: a longitudinal case study
- `2609.25369` [cs.RO；合同类含New] Capability-Aware Arbitration for Semantic Intent-Based Shared Control
- `2609.25363` [cs.RO；合同类含New] HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments
- `2609.25322` [cs.RO；合同类含New] JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation
- `2609.25274` [cs.RO；合同类含New] Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction
- `2609.25264` [cs.RO；合同类含New] Cosserat Modeling of Trimmed Helicoid Soft Arms with a Separated-Section Constitutive Law
- `2609.25031` [cs.RO；合同类含New] Towards Adaptive Interaction Strategies for Human Companion Robot via Deep Reinforcement Learning
- `2609.26156` [cs.RO；合同类Cross-only] Designing Task-Induced Arousal: A Multimodal Stress Induction Method for Interactive Experiments
- `2609.26010` [cs.RO,cs.MA；合同类含New] MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies
- `2609.25257` [cs.RO；合同类Cross-only] Higher-Order Approximation of Exit Functionals in Sampling-Based Stochastic Model Predictive Control
- `2609.26644` [cs.AR；合同类含New] Dynamic Slack-Aware Clocking for Near-Threshold Tensor Processing Units (TPUs)
- `2609.26551` [cs.AR；合同类含New] Toki: Profiling HBM Performance on FPGA Systems with RISC-V Soft Cores and PCIe Host DMA Traffic
- `2609.26374` [cs.AR；合同类含New] ESupNNet: An Error Supervising Neural Network architecture for error detection against soft errors in parameters
- `2609.25869` [cs.AR；合同类含New] Decoupling Logical Masks from GPU Execution for Dynamic Block-Sparse Attention
- `2609.25782` [cs.AR；合同类含New] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving
- `2609.25335` [cs.AR,cs.PL；合同类含New] GRADE-RTL: Evaluating LLM-Generated RTL Beyond Compilation
- `2609.25637` [cs.AR；合同类Cross-only] SLED-IFV: Solver-Validated LLM-Guided Decomposition for Scalable Hardware Information-Flow Verification
- `2609.25427` [cs.PL；合同类含New] Modular Composition of Inductive Types Using Lean Meta-programming
- `2609.26122` [cs.PL；合同类Cross-only] Why Do LLMs Fail at OCL Generation? A Graph Reasoning Perspective
- `2609.25121` [cs.PL；合同类Cross-only] TRACTOR Benchmark for Evaluating C to Rust Translators
- `2609.25018` [cs.OS；合同类含New] OSFoundry: Building and Evolving Operating Systems with Specification-Guided Agents
- `2609.04043` [cs.OS；合同类Cross-only] Extending concurrent separation logic to the hardware level to verify the xv6 OS kernel on RISC-V with AI agents
- `2609.26284` [cs.PF；合同类Cross-only] A Throughput-Oriented Analytical Model for Post-Quantum Security Protocols
- `2609.26251` [cs.IR；合同类含New] When Does Permutation Instability Generalize? Independent-View Validation for Listwise LLM Reranking
- `2609.26250` [cs.IR；合同类含New] Which Reranking Conclusions Survive the Answer Interface? A Prospective Finite-Orbit Audit
- `2609.26171` [cs.IR；合同类含New] When Concealed Links Cannot Be Recovered: A Structural Identifiability Bound and Evaluation Pitfalls in Offshore Leak Networks
- `2609.25991` [cs.IR；合同类含New] Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents
- `2609.25825` [cs.IR；合同类含New] Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search
- `2609.25306` [cs.IR；合同类含New] ReFilter: Bridging Embeddings and LLM Filtering for Similar Mobile App Retrieval
- `2609.25959` [cs.MA；合同类含New] Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents
- `2609.25956` [cs.MA；合同类含New] Governed AI-Agent Coordination for Dementia Care: Architecture, Safety Contracts, and Evidence-Derived Workflow Verification
- `2609.25913` [cs.MA；合同类含New] When Does Execution Provenance Help Agent Memory Retrieval?
- `2609.25432` [cs.MA；合同类含New] Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action
- `2609.25195` [cs.MA；合同类Cross-only] Qwen-Audio-Agent Technical Report
