# Live 2026-10-09：两项 DC 必要证据作者笔记

作者：review_mar11_continue。独立 ownership 为本文件；正式日报由 supplement_20260312 维护，root 独立复核两篇作者Source/PRE及实际POST。窗口为 2026-10-08 北京时间自然日；准入/日期复用 root 官方 DC Oct8 组与完整 AB 校准，不以 Submitted Oct7 搬移归属。作者证据只处理 2610.09424 / 2610.09372；初始不写Books，随后仅root逐项认可PRE/授窄锁的一段与本人注落实，不写State、不自授Source/PRE/POST/DAY。后续另获本日发现/准入独立复核，范围独立记录在末节，不把两篇作者证据当自验。

## CoMoE — 2610.09424v1

- 原证：[精确 v1 HTML](https://arxiv.org/html/2610.09424v1)。当前官方 v1/无撤回信号复用本日有效 AB；事件日期 2026-10-08。实际必要阅读：§2/Table1 与 §2.3（HTML79–119），完整 §3.1–3.3（126–175），完整 §4.1–4.3/Table2–3（176–249），§5.2/Conclusion（256–263）；Fig3–17只读 caption 与正文讨论，未读取像素，不声称完整曲线重建。原件署名作者支持其机制与配置实验，未读代码/复现/独立硬件验收。
- 准入链：弱 PCIe、无相应 GPU P2P 路径的 EP 推理下，重复发送同 token 和粗粒度 combine 等待放大通信成本 → host 单份 token 供多目标拉取，以及 token 贡献完成驱动的 combine → 重选通信路径与同步粒度，而非改变 router/expert。正式评分 **2+2+2=6**：重要通信替代机制、跨 GPU/host/NUMA 边界、可复用的带宽与完成条件；标准必要阅读完成，具体 Books gap 则深入其受影响范围，不因 gap 改分。
- 机制：§3.1 的均匀无放回 expert 选择只是 fanout 分析假设，不授实际 router 均匀。按 target 的索引加一份源 GPU→host payload，接收 GPU 各自拉取；省 source egress 副本，不省全部接收流量，瓶颈转向共享 PCIe/DRAM。§3.2 ready flags+每 token outstanding counter，最后贡献触发 accumulation；仍须等齐该 token 的 authoritative contributions。NUMA placement 将 buffer 放接收端 local domain；tiles 与 batched commit 摊薄信号。§3.3 pinned/mapped host buffer，由 GPU loads/stores 推进，非 CPU 路由/复制线程；作者称 SGLang backend 替换，model/scheduler 未变。
- 关键评价与直接反侧：同 8×RTX5090、BF16、SGLang0.5.9、四模型（DeepSeekV2Lite/GPTOSS20B/Qwen3 30BA3B/GLM4.7Flash）对默认 NCCL；ShareGPT 每 model/backend/request-rate 1000 prompts 的均值，文中 throughput 改善范围1.24–1.46×；这是作者受限结果，不授 tail SLO。1024 token routing trace replay 支持 dispatch 对照；CoMoE-Sync人为加全局 barrier，支持该障碍的局部归因，不代表穷尽最优 NCCL 调度。combine 分解消融为 DeepSeek hidden2048/top6 的随机1–256token请求。跨 A800 对照同时换 CPU/内存/GPU/互联，不能作单硬件因果；Table1 BF16 5090仅A800的0.67，而非同 FLOPs。高 request rate 队列稀释相对收益；Agent工具调用同样稀释，未报告成功率/答案质量对照，不授质量或隐私。
- 成本/未证：Qwen staging 512MiB/GPU、总4GiB；24/170 SM 被通信占用。无 CPU computation 不等零 host 成本；pinning/DRAM/PCIe/readiness/NUMA/SM/metadata 全计，硬件 CapEx 不是 TCO，分数节点线性 overprovision 不是实际 scale-out。重复运行/CI、请求长度分布/并发、完整 SLO、功率/整机费用与数值一致性/故障恢复 = Not Disclosed；原文方法不补内存 fence/epoch/abort 实现。只采用受限路径提案与成本转移，不授所有消费卡兼容/无 straggler/production guarantee。
- Actual owner：`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 已实际读125–165、225–249：161–163有按层通信SM/chunk与重复remote token复用，225–238有 signal/completion≠全局fence，240–244有跨节点/节点内collective分解。`MODEL-MOE` Ch21实际155–250有 weighted combine/恢复token身份，并明确kernel/通信映射交Ch49；Ch54容量/offload不另建第二owner。具体 gap 仅 host共享multicast+接收端NUMA token-completion路径，不把已有细粒度原则包装为新知识。

### 最小拟文 PRE（待 root 实际独核/授权，不是已写）

建议在 Ch49 原 MixServe 两完整段/source 注之后、device-initiated 小节之前接一段：

在缺少可用 GPU P2P、必须经 host 的 PCIe 节点内，重复 token 还可以由共享 host buffer 承载：源 GPU 只写一份 payload 与目标索引，各目标 GPU 分别拉取；减少的是 source egress，接收流量与共享 PCIe/DRAM 压力仍在。Combine 可由接收端 NUMA-local stash、ready flags 和每 token 贡献计数驱动，只有该 token 所需贡献齐全才放行 accumulation，不等待无关 token，也不能把可见地址当完成。[CoMoE 的受限对照](https://arxiv.org/html/2610.09424v1)以 GPU 读写 mapped host memory 实现这条分支，CPU 不在路由 data path，却仍支付 pinned buffers、NUMA、metadata、信号和通信 SM；人工 barrier 消融与单节点 BF16 结果不授所有拓扑、数值或故障恢复。共享链路饱和、可见性/完成无法验收或质量回归时，保留普通库 collective/固定通信计划；GPU 价格估算不替完整服务成本与 SLO。

当前状态：root已实际独立核必要Source/Ch49完整局部并认可PRE；作者依窄锁已写Ch49新246单段+本人2326注，实际写后225–257/本人注回读与限定diffcheck通过。root非writer实际新增正文、完整局部邻接与自身末注POST通过、Ch49窄锁释放；按授权仅同步自己的末注状态。可计本家族实际整合，不授DAY。

## Expert Coupling — 2610.09372v1

- 原证：[精确 v1 HTML](https://arxiv.org/html/2610.09372v1)。事件日期2026-10-08/current v1无撤回信号复用本日root官方列表/AB；没有拿HTML头部Submitted Oct7当公开日。实际必要范围：§I准入/并行限制75–102，§II/III104–157含TableI（offline routing held-out），完整§V162–194（185–194输出缺口已补），完整§VI/VII195–242（197设置补核），必要A-A/TableII267–312与A-B315–322直接routing反侧。Fig只caption+正文，不读像素、参考文献或完整算法/每步库存；未读代码/复现。
- 正式评分 **2+2+2=6**：不改router/expert的重要placement/通信替代，横跨EP与attention TP/SP ownership，稳定的布局/总流量vs拥塞边界；标准必要Source作者完成。已有共同激活主题不降低评分；具体训练token-owner接口gap深入，不扩大其他附件。
- 原约束→增量→选择：固定专家布局+规范sequence shard让同token仍跨多个expert目的地；作者先按共选图做等量专家的节点/GPU层级局部交换，并对(token,destination rank)去重；在TP/EP为同一组GPU且启用SP的布局，再用前两层route affinity预测当前MoE owner，按confidence和严格T/EP quota分配，把token与其residual的置换融合进attention后reduce-scatter，all-gather恢复canonical顺序。规划不改最终router，错预测仍走真实dispatch；没有新增collective不等没有permute/lookup/等待。等数量专家不保证token/链路均衡；权重依globalexpertID加载，不授迁移/故障/逐bit合同。
- 对照/范围：一套12层、width4096、128experts/width1024（13.6B总、top2/6），FineWeb-Edu、序8192、batch128、2000steps约2.1Btokens、BF16+FP32router/optimizer。MI300X每node8卡xGMI全连，跨节点每GPU100GbRoCE；EP8–64，shuffle仅TP8EP8/TP16EP16。对同step2000 checkpoint/同语料heldout；B原contiguous Megatron A2A→D去重→P合置→Sshuffle分拆。一次14cleansteps和一次14instrumentedsteps各去4warmup后10步中位数，不是两套独立训练seed/两次clean重复；未报告CI。TableI是记录route离线模拟，不是dispatcher时间；VI才有运行计时。
- 直接反侧：VI-C top6单node shuffle A2A倍率1.46低于placement-only1.48；集中owner增加最忙pair流量，总bytes减少不必减少xGMI时间。两fusedpermutes耗数ms，planner原成本约forwardA2A的1/3，侧stream后主stream仍约1ms等待；不能用Conclusion“almost no overhead”略掉。top2完整step仅1.01–1.06×，1.41×最高来自EP16 top6 P路线，不能挪成shuffle通用收益。三router A-B支持本模型幅度依co-selection，balance/skew仍影响净收益；长程每1000步重fit是作者expectation，不是实测稳定周期。未评inference、CP或任意TP/EP组、跨模型普遍性。离线trace/图分区/搬权重及计划/置换/同步与最终step质量均计费，实测短同checkpoint步时不代表从scratch动态部署全成本或长期能力不损。
- Actual owner：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)实际700–807：700–717已有冻结router/tokenidentity→dispatcher/逆置换/step责任，780–783 Cobalt已有coactivation+nodeunion/副本布局且明确集中负载/迁移与梯度费，793后owner-oriented是参数梯度目的地，不是tokenowner。Ch40实际167–194仅SP/CP与EP/TP兼容交接；Ch37目录与251附近作用域仅SP激活切分，故不再另建第二owner。已有合置原则不新写；具体gap是利用已存在attention collective的目的索引改变MoE tokenowner并恢复顺序，不是预测expert权重prefetch或optimizerowner改变。

### 最小拟文 PRE（待 root 实际独核与锁，不是已写）

建议接 Ch36 Cobalt完整两段/source END之后、跨站点federation之前一段：

合置 experts 仍不决定哪个 rank 持有 token：在 TP 与 EP 为同一组 GPU、且启用 sequence parallel 的受限布局中，可以用先前层的 route affinity 提议下一 MoE 层的 token owner，按每 rank 固定 token 配额分配，再把 token 与 residual 的置换融入 attention 后已有的 reduce-scatter；后续 all-gather 恢复 canonical 顺序。预测只改变执行位置，当前 router 决定仍须完整 dispatch，不因预测而跳过 expert；checkpoint 权重也仍按 global expert identity 对应。[Expert Coupling 的训练对照](https://arxiv.org/html/2610.09372v1)提供此分支，但少发总 bytes 可能把流量集中到最忙链路，shuffle 也不保证比仅合置更快。Trace 拟合、等量 expert 分区、权重布局、quota planner、双置换与等待均计费；无新增 collective 不等零开销，短 checkpoint 计时不证明长期能力或任意并行布局等价。Affinity 漂移、组不一致、canonical/residual/梯度身份无法验收或净收益不足时，恢复规范 sequence shard、静态 EP 与已验证的 dispatcher，不以locality替完整step验收。

当前状态：root实际独读V-A/B、VI及必要A-A配置与Ch36 Cobalt完整局部，Source/PRE通过后授窄锁。作者已按接纳逐字PRE在Cobalt END后/federation前写新785单段及本人1852 Review note；旧两段与下一federation保留，作者已顺读完整局部/本人注及Ch35/37开篇交接。root非writer actual新785/775–798完整局部及本人1852注POST通过，Ch36窄锁释放；按授权仅同步本人注状态。可计本家族实际整合，不授DAY；无自验。

## 独立发现/准入局部 scope（后续授权，与上面作者证据分开）

复核者：review_mar11_continue；发现/筛选作者：supplement_20260311。实际完整阅读本日 [arxiv-screening.md](arxiv-screening.md) 当前查询、停止位置和范围判断。两篇本人作者 Source 不在本节独核；四DC完整AB准入复用root有效首批校准，不重审。最新读取文件尚无后续新分页/AB关闭结果，不能因笔记存在而授Coverage。

1. 查询边界：四主题查询使用14日提交元数据仅作发现上界，三有效50条标题/身份读取与模型超时分开；244/770/1390未去重14日总量不称本日分母。系统首50到Oct5；多模态/Agent首50仍Oct7，其start50为普通可执行分页。CL仅标题到#173；DC本日#13–34标题停止窗前。查询成功/标题浏览不授完整题摘或Evidence完成；Submitted不能代替Oct8公开公告。此执行记录/停止语义通过，未重新执行四API或声称验证全返回XML。
2. 代表标题EX：实际官方 [DC recent](https://arxiv.org/list/cs.DC/recent)定点find两完整原题及Oct8日期组132：#17/2610.09713，172行“Rendezvous under Variable Disorientation:The Algorithmic Power of Fixed Unit Distance”；#18/2610.09659，181行“Communication-Aware Qubit Placement and Automatic Node-Count Allocation for Distributed State-Vector Simulation”。前者明确非模型驱动Agent/模型训练推理执行、后者量子state-vector，不由通信术语授foundation贡献。仅此2项title级范围EX通过，不称AB全文、所有EX或整类召回。
3. 未关闭判断保留正确：09512 ADMM、10487 LOCAA、10148 cloud carbon、09786 HPC及7具名CL相关标题仍待完整AB/具体增量判断，不依关键词关闭/准入。不扩抓列表或把未完成材料称外部hold，无共同错误需扩查已判集合。后续仅核作者实际完成的新分页/拟入选与分层代表排除，当前局部范围不能替日级完成。

局部结论：通过上述真实scope与2项代表EX；Coverage/后续AB/全部候选Evidence仍未验收。root允许本节保存，不修改其independent-review.md。

### 后续实际增量发现复核

上面的查询/待AB记录是旧停点，不作当前未完成宣称。本轮actual读arxiv-screening.md15–26与新增54–57：三主题已分页到Oct6边界（system index16/09111；MM start50首09217；Agent start50 index40/09237，前一09240），model同query下界收窄Oct7有限重试101项、start100末09274已读。承认其**作者执行记录与停止语义**，没有重新跑API/独读全部XML，不将244/770/1390作本日分母，也不授本窗完整公开召回。Submitted/public仍分离；两篇当前评价作者证据不在本节自验。

新增四项完整AB排除独立实际读：09512/10487/10148精确官方abs v1经web cache miss后curl官方HTML提取完整title/blockquote；09786精确官方abs v1 web16–18。仅准入级，不读全文/代码/所有领域实验：

- [09512 DAP-ADMM](https://arxiv.org/abs/2610.09512v1)：连接/非平衡mass的graphOT求解、邻居通信、projection/penalty与残差收敛；AB的泛称ML应用未给模型能力/训练执行关系。与RESEARCH_CONTRACT42–44边界一致，具体范围EX，不因理论/ADMM排除。
- [10487 LOCAA](https://arxiv.org/abs/2610.10487v1)：确有tool-integrated LLM、compressor-aware guidance、persistentmemory及闭环试验；因此不能说没有Agent。但摘要实际新增是将这些已有接口用于科学模拟compressor EB多约束调参，并报告同field时步记忆少试验，未陈述新的Agent执行机制、可迁移失效/可靠性条件；按暂缓AIforScience与合同65具体增量门槛接纳范围EX。不把数字下降授有效通用机制，也不因应用名或标题关键词关闭其他Agent研究。
- [10148 rSCI](https://arxiv.org/abs/2610.10148v1)：bottomup/总量报告残差问责愿景，具可信reconciliation当前不足的自限；无基础模型/训练/推理workload关系。范围EX，不贬低通用云碳会计。
- [09786 HPC-MQBench](https://arxiv.org/abs/2610.09786v1)：Slurm配置与Kafka单brokerqualification/auditable选择，AB明确阶段相关、allocation非因果与future multi-broker；通用测量类比而非模型系统增量。范围EX；不以负面结果或小规模作排除理由。

四项EX与author11语义校准一致，无共同误判需扩大已判集合。新增09778/10508/10455/10170完整AB准入继续复用root已有效独核，本文不重审；新增model四potential及其公开日期/后续AB仍普通待办，不由标题、下载或本节授Coverage/DAY。实际范围仅本日当前记录、上述四原AB和两早先titleEX。

### 新增13项完整AB非作者准入校准

该段替换上段model/后续AB的旧停点，不撤有效四EX。实际逐份读取13个精确v1官方abs完整标题、blockquote摘要/subjects；10179摘要泛称不足时，仅定点实际HTML intro91–102补足机制，即停止，不读全文队列。作者supplement_20260311；本人不是这些13项的发现/AB作者。本节仅准入，不是正式评分、必要Source或Books完成。

| ID | 非作者裁决及可辨识原始增量 |
| --- | --- |
| [10395](https://arxiv.org/abs/2610.10395v1) | PASS；固定权重linear-attention block执行连续graph update与multiplier状态，算法执行误差和因果结构恢复分测，训练学得executor仍开放。 |
| [10381](https://arxiv.org/abs/2610.10381v1) | PASS；loop共享weights不等KV共享尺度，以末loop reference与低bit residual重构，重选缓存表示与恢复。 |
| [09346](https://arxiv.org/abs/2610.09346v1) | PASS；fixed completion遗漏quantized student访问prefix，blockwise初始化后冻结FPteacher在线reverse-KL恢复，重选恢复人口。 |
| [09877](https://arxiv.org/abs/2610.09877v1) | PASS；校准扰动下local与propagated error分账及separable mixedbit allocation，不以科学应用或未经核保证排除/采用。 |
| [09876](https://arxiv.org/abs/2610.09876v1) | PASS；每denoise内recursive latent thinker引导frozen painter，不依symbolic target，错误注入/修复是后续可核边界。 |
| [09679](https://arxiv.org/abs/2610.09679v1) | PASS；concave prompt-exposure surrogate/Fenchel slope与shared price控制全horizon admission/revisit，代理不等真实学习收益。 |
| [09493](https://arxiv.org/abs/2610.09493v1) | PASS；match文本不等实际依赖，paired-state magnitude诊断与signed equal-norm控制分责、曝光不显著不等不存在。 |
| [09757](https://arxiv.org/abs/2610.09757v1) | PASS；midprefill集中不认证删context，sink-isolated GQA/discarded-mass包络与条件observer反例，理论无实测不自动EX。 |
| [10533](https://arxiv.org/abs/2610.10533v1) | PASS；多表达激活不同/共享memory造成编辑旁损，joint representation update与reuse-frequency penalty重选表达覆盖/locality。 |
| [10426](https://arxiv.org/abs/2610.10426v1) | PASS；harness搜索轨迹与runtime相关，component promotion、verified harness-matched SFT与fresh online RL分清执行/数据人口。 |
| [10332](https://arxiv.org/abs/2610.10332v1) | PASS；compact stage/action蒸馏及admissible joint scoring，示教预算增加后stage收益消失的直接反侧值得核验。 |
| [10232](https://arxiv.org/abs/2610.10232v1) | PASS；同模型共享设置九种评价rank弱一致，ability与willingness/任务人口分测，不授refusal唯一因果。 |
| [10179](https://arxiv.org/abs/2610.10179v1) | PASS；完整AB后实际intro91–102核到Cov/CovDep/AM×whole-trajectory scalar/local-query-token credit及preserved-action-alignment控制，信号身份与credit支持集有具体选择差额。 |

日期按root允许复用的有效定点证据：12项为author11实际官方LG/CL/AI Oct8组；09757复用root独立实际availability175/183及DataCite原始身份/registered夹证，下界公告ID、上界已公开ID均Oct8，不拿Submitted/metadata单值当公开日，保留官方列表目标未见局限。本轮web的LG recent回旧July缓存不作日期证据，不重追有效日期。13逐项PASS，四model与四多模态/训练/诊断/memory子包已即时交作者；25完整AB=8既有准入+13新准入+4具体EX，2标题EX单列。未重跑所有query/读取全XML，不授全分类召回或DAY；之后Source只能按具体任务ownership推进，本人作者证据另由root独核。
