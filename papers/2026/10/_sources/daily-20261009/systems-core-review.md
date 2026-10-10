# Live 2026-10-09 系统必要证据

作者：supplement_20260311。日级笔记仅本文件ownership；正式六部分由supplement_20260312写，不写State/索引。Books仅按root逐篇窄锁执行，非写入者root完成actual POST。窗口2026-10-08北京时间自然日。四项AB的root准入校准复用[发现记录](arxiv-screening.md)；本文件逐篇记录本人实际必要证据、评分和owner差额，不自授非作者Source/PRE/POST或DAY。

## MemFerry — 2610.09657v1

[精确v1 HTML](https://arxiv.org/html/2610.09657v1)。官方DC 10-08组#19公开归属已核，不把页首07 Oct Submitted改作公开日；当前仅v1未见撤回。评分 **2+2+2=6**：层级计算/驻留与梯度直写是机制替代，跨host—accelerator及optimizer边界，可复用容量/时间取舍；不按1.68×宣传评分。标准必要Source已完成；实际owner确认长期gap，拟采用内容深入到必要算法/实现和评价，不扩大全文/代码复现。

实际本人读范围：HTML III-A–C（103–172）；IV-A–E（173–380，含Alg1/2、GO递推与双路径式）；V（381–387、442–444）；VI-A–E（445–510）；VII只用于DHA已有先例关系（512–517）。图只读caption及所需正文，未做所有pixels、代码或重现实验。

采用的最小链：传统offload把host当存储后搬到HBM→按profile为层选GFGB、DHA或DFGB，DFGB前向直读后趁链路空隙搬到HBM用于反向，shadow model将logical tensor与host/HBM storage分离→计算位置、参数驻留和反向梯度位置须分别选择，而不能从“offload比例”推断整步时间。GO分支可将选定梯度直接写mapped host，省去HBM梯度buffer但仍支付链路写入。ScaleUp的辅助NPU转发只是另一路；配额取决于启动延迟、带宽和host/fabric争用，不是免费链路。

直接反侧与采用边界：DHA是GPU读取注册host，不是CPU做forward；CPU optimizer继续拥有更新。V在消费前加同步，storage切换亦不能替代版本/生命周期责任。Alg1 `base/baseline`、`T_trans`和Alg2排序对象记号未统一，本文只采有限profile-planning接口，不照录成已核可执行算法或全局最优；GO按加性profile和空间预算的DP也不授真实争用下的最优/精确容量保障。VI-C全梯度DHA在V100可慢于baseline，模型增大收益减弱；VI-A承认DeepSpeed梯度buffer析构/重建差异，另给native baseline，不能把全部收益归因DHA。未给loss/收敛或恢复对照，不授训练质量等价。

评价身份：A100实验128CPUcores/8×80GB A100、V100实验12CPUcores/32GB，PCIe3.0，PyTorch1.9.0/Python3.6/CUDA11.7；BERT/Roberta/GPT2-medium及手配TransformerXL 0.7–6.7B、sequence378–4096。局部V100容量实验batch1；4.3B固定globalbatch的DataParallel至8GPU，6.7B batch sweep另计。ScaleUp为4训练NPU+4辅助NPU、13B TransformerXL、batch32–256，不当成只付4卡。精确DeepSpeed revision、precision、总训练步/数据、重复方差与planner/profile摊销：Not Disclosed；服务concurrency/SLO非训练实验适用。有限iteration-time/peak-memory结果不外推现代软件栈、全部模型或总费用。

**owner/PRE实际依据（随后获root授权并写后通过，见末段）：** `TRAIN-ZERO` Ch39。本人实际顺读253–309 Offload/TRANSIT/full-host-cache/CPU-authoritative stream，邻章Ch38/40开篇。273–275已有phase zero-copy且299–305有buffer生命周期，但没有per-layer GFGB/DHA/DFGB前向—反向分开选择及梯度直写的明确接口。在TRANSIT完整限制段275之后/Full Host Cache标题前整合一段有限分支；不新建Ch49第二owner。现书已有全费用/旧路径原则，仅新这一差额。

可供独立审阅的精确止点：III-B/C；IV-B/C/D与V同步/存储；VI-A baseline差异、VI-C慢写反侧、VI-D规模限制、VI-E辅助资源。支持这些有限命题已足够，不继续无关references或所有图。没有必要外部材料请求；代码不可得不阻塞此论文范围。

root已actual必要Source独核通过，并actual Ch39局部确认owner/PRE；下文逐字正文随后已写并通过非写入者POST（275完整TRANSIT限制段后、Full Host Cache前）：

直接读取host还可以由层的前向与反向需要分别决定，而不是只按一个phase切换所有page：一层可先搬到HBM再计算、全程由GPU读取mapped host，或前向直读host后趁链路空隙搬到HBM用于反向。Logical tensor与底层storage分离，让后一模式切换访问位置；选定梯度也可直接写host，省去HBM梯度buffer但仍支付链路写入。[MemFerry的有限对照](https://arxiv.org/html/2610.09657v1)支持这种逐层计算/驻留/写址分工，不保证profile规划全局最优、autograd兼容或训练质量等价。消费前同步、storage寿命和CPU更新版本仍须分别验收；V100低带宽下全梯度直写反而更慢，DeepSpeed梯度buffer的重建差异也不能归入DHA本身。Profile、注册host、所有搬运与CPU更新、额外辅助设备及恢复/质量回归都计费；链路、计划或状态身份失配时回显式HBM搬入、普通offload或原scale-out，不由更低显存签发整步性能与训练正确性。<!-- source-family:SF-2026-ARXIV-2610-09657 -->

## vLLM-Omni — 2610.09307v1

[精确v1 HTML](https://arxiv.org/html/2610.09307v1)，官方DC Oct8组#22确认。当前仅v1无撤回。评分 **2+2+2=6**：异构stage控制/数据/会话分离改变runtime接口、跨engine与transport边界、有稳定状态约束；不按支持模型名单和吞吐数字评分。本人必要Source完成；actual owner确认gap后采用内容深入，root非作者Source/PRE与写后POST均通过，具体位置见末段。

actual读：§1核心约束/旧系统关系140–169；§2.1–2.6完整172–296（含request final-output集合、async_chunk、StagePool、typedpayload/KV与session）；§4.2.1有关turn API467–468、§4.2.5–6 498–512；§5.1–5.3 513–613（T3–8必要行）；§5.6/结论655–686。其他模型/平台全库存、所有pixels、代码/PR与完整nightly artifacts未核，不称系统复现。

采用链：单engine token frontier不足以表示异构音频/codec/diffusion输出→orchestrator只拥有admission/sticky routing、跨stage推进与client progress，engine保token/KV或denoise控制，connector搬重payload；async_chunk预提交下游placeholder并从data-plane收chunk，避免每chunk重复control-forward；完成须final-output stage集合全部drain→stage完成、client增量和整请求完成必须分开。StagePool replica独立，不是池内collective；single-request streaming和跨调用session另有身份，typedlatent状态与engine KV分责。未把具体类/API或session设为所有pipeline默认。

直接反侧：§2.6明示session/AR–diffusion能力仍evolving，§7 broader session、闭环robot及跨硬件评价future；§4.2.1 turn realtime无resume/playbackack/overlap，不等full-duplex。§5.2MRv2需one-line startup guard才测，text-only C32有32/128请求失败；更多replica在C32 RTF反升，非单调扩容。§5.6 opt-in turn-mode无法可靠停止、出现无关追加音频，未计正面结果；其duplex仅单个四turn fixture，不测barge-in/admission正确性。这些是性能/安全release限制，不因支持矩阵擦除。没有独立完整端到端output-quality或faultrecovery保证，不授物理动作安全。

评价身份：H200 Qwen3Omni表commit ee8fdab1d、Fixed-Len2500/900和Random-MM synthetic输入；C1/4/8/16/32或openloop0.1/0.5/1req/s分开，T3–5是three-repetition median of mean metrics；T6/7另用H100 Jul5–11nightly平均，不能混成同硬件/commit因果。TTS H200 Seed-TTS、default2GPU vsQwen fused1GPU，同runner但warm reference cache使冷启动TTFP不同；有限Whisper WER不是完整speech quality，本文不采用具体gain。硬件profile、generator/runtime/connector、chunk/replica与cachewarm身份、生成输出长度和完整费用须绑定。未披露条目的精确precision/全recipeSHA、tailP95/P99及failurebudget写Not Disclosed，不从“nightly”推服务SLO。架构有限实验已足支持上述分工，停止无关平台/图表扩读。

owner/PRE提案：唯一`INFER-VLLM` Ch50。本人actual1–105/255–310（异步PP→restore→failure），相邻Ch49/51开篇，Ch42 250–294 pipelinefusion、Ch52 70–100 state/dataedge。现书已有PP token-frontier/connector完成和stateedge，却没有异构client-emitting与final-output集合及chunk-control suppression完整接口。建议Ch50现274 PP完整结尾后/restore标题前一段，不在Ch42/52另增机制。拟逐字最小文：

异构生成stage也不能仅按最后一个token stage判断请求完成：AR、codec与diffusion各保自己的调度和state，外层orchestrator只拥有admission、stage推进、sticky replica、abort及client progress，重payload由connector搬运。下游可先接placeholder，再随upstream chunk经data-plane计算，而不为每chunk重复control-forward；client-emitting结果与下游输入分开，只有声明的final-output stage集合全部drain才结束请求。长期session再增加独立身份、retention与fence，不把latent buffer混进engine KV。[vLLM-Omni的有限对照](https://arxiv.org/html/2610.09307v1)支持这条异构runtime分工，不认证全部pipeline默认或取消/会话安全；MRv2仍有启动guard和高并发失败，更多音频replica亦会使高负载RTF退步。Warm-cache语音、不同硬件/recipe与one-session health不可当完整质量或tail SLO，input/output、所有engines、connector、session驻留与全部冷/热成本须分别计价。状态、chunk或质量失配时回full-payload handoff、较窄已验收pipeline和独立输出/控制gate，不由统一runtime签发物理effect或普遍加速。<!-- source-family:SF-2026-ARXIV-2610-09307 -->

两项没有新的必要外部材料请求。root随后分别actual必要Source/PRE，授Ch39/50单段＋自身note窄锁，本作者已逐字落实；root非写入者actual POST均通过并释放。MemFerry实际Ch39新增277/本人412注（完整250–312）；vLLM-Omni实际Ch50新增276/本人416注（完整253–316）。两家族实际整合至TRAIN-ZERO/INFER-VLLM，不是只提案；原6分不改，不授本日完成。上文记录当时提案和必要源范围供追溯，以本段最终状态为准。限定diffcheck通过，未stage/commit/push，旧并发正文保留。
