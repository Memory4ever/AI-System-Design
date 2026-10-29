# 06-10 次批必要证据与实际 owner 差额

本日补Jun09；只保exact-v1。准入/日期独核在SUP_REVIEW§6；本文件不是已写Books或日级通过。作者已读Books上下文与下述实际owner完整直接相邻，reader已独立核必要域；root仍协调新增写入，不自行扩大共享写权限。

## 08105：同一sink图样的两种计算（5分）

必要原件 `SUP_2606.08105v1_20261025.html` §2–6，单head线性toy、DINOv2/OpenCLIP与LeJEPA三seed frozen-backbone dense probes。v1是gating+registers，不采用当前metadata后版position-free global pathway。近零sink value配合近零residual update支持NOP-like；非零value配合低stable-rank output支持broadcast-like，二者可在同一个pretrained ViT共存。Registers可同时承载两类功能，不等于消灭sink；gating+registers的dense分割probe改善而ImageNet classification几乎不变。

边界：理想perfect-sink近似与实际spectrum不可混用；rank-1 update是已假设单dominant sink后的诊断，并非唯一因果解释。Lemma4不采用“加公共向量严格降低variance”的强叙事：完全公共加量只平移均值，不能据此宣称LLM普遍oversmoothing定律。未读无关附录/实现、未复现，不把可视化或局部mIoU当生产收益。

actual owner `MODEL-SELF-ATTENTION` Ch14:298–332已有sink/null/gate和双轴诊断，真正差额是value/update norm与output-rank联合区分功能及register重新分工。拟在“Sink与Outlier…”两段之后、原semantic-body-binding之前插一段：

> 同一种竖条Attention图样还可对应不同计算：若sink的value范数和本头residual update都接近零，它可能帮助执行no-op；若value仍有内容尺度、跨query的output却近似低rank，它可能把共享信息广播到多处。两项诊断须一起读，不能把高权重或单个rank统计直接命名为功能。受限ViT对照中，register既可承载no-op也可承载broadcast，gating与register组合改善dense probe却几乎不改变全局分类，说明迁走sink位置不等消除其计算。[精确v1](https://arxiv.org/html/2606.08105v1#S3)仅支持这套条件诊断，不把理想single-sink推导推广全部LLM，也不由公共向量相加推出方差严格下降。逐层读出、干预与训练/探针费用仍在；诊断混合、任务或模型失配时，保原softmax/null/gate与更窄行为对照。<!-- source-family:SF-2026-ARXIV-2606-08105 -->

## 08292：恢复prompt轨迹不等迁移计算（5分）

必要原件§3–6：CSS选择、SVD/nearest-centroid、prompt-vs-answer full-trajectory restore及same-prompt/same-computation/same-answer controls；Qwen2.5-7B、Llama3-8B、Mistral7B五类单步计算。选择性必要、线性可解码、同prompt恢复可成立，而所测prompt-side rows仍未clean-transfer；广泛logprob变化可被same-answer/same-computation控制解释。负面结果不因没有新算法而排除。

边界：§5.1写18 cells但13+3+3=19，不采用该比例；只采用精确assay对象与局部失败，不能证明attention heads从不承载算法或不存在分布式可迁移状态。正控只证明部分patch敏感性，不认证所有prompt override对象都有足够检出力。未核代码/复现。

actual owner `WORLDVIEW-REPRESENTATION` Ch05“从可读出到机制”已有证据阶梯/跨context和训练checkpoint，邻接已有局部表征不能授完整机制；真正差额是恢复位置与三control分别隔离轨迹稳定、答案熟悉与计算选择。拟在阶梯后“更强的主张…完整机制”完整段后、训练checkpoint段前：

> 即使一次ablation可被恢复，还须问恢复的是prompt处理还是答案生成。先清零候选head，再分别恢复prompt positions与answer positions，可避免把答案logit的作用当成任务选择状态；随后把源prompt的状态patch到目标prompt时，还应比较同prompt、同计算但换表面形式、同答案但换计算三种控制。源答案概率提高而同计算/同答案控制也同幅移动，只支持广泛context或答案熟悉效应，不足以证明可迁移的计算。[受限三模型对照](https://arxiv.org/html/2606.08292v1#S4)中，必要、可解码与prompt-side恢复仍可和clean transfer失败共存；这不是证明所有head都没有算法。筛选、读出、完整restore与matched patch都付费，控制或行为检出力不足时保留局部因果判断与Unknown，不把可恢复升级为普遍mechanism identity。<!-- source-family:SF-2026-ARXIV-2606-08292 -->

## 08476：独立document的CP通信人口（6分）

作者实读exact-v1 §3–4；reader独立必要核§2–5。Document mask下不需要跨document attention；WholeDoc可免该doc跨worker KV，split doc只发送被其他query消费的prefix部分，合并连续buffer避免逐doc小拷贝。等token平衡FFN、max-attention-workload平衡二次attention是不同约束，长doc改PerDoc、短doc保WholeDoc的启发计划联合减少通信和小kernel。

反侧：全部实测单节点8H100 SXM80/NVLink，100K sampled packed sequences、16/32heads、128head-dim、CP4/8与64K–128K；非跨节点完整模型收敛训练。heuristic28%vsILP36% communication saving及imbalance1.04vs1.00不授全局最优；solver tens-of-minutes和heuristic规划、packing/copy/通信都计费。未核实现/像素/复现。

actual owner `TRAIN-DISTRIBUTED-TRAINING` Ch36 CP段已有固定/变长degree与headchunk buffer，缺独立docmask决定KV人口。拟在完整变长CP段后、“长序列切到多个rank后，跨边界对象也不一定是完整KV”前：

> Packed sequence中的document若彼此被mask隔开，CP也不必默认交换每个位置的完整KV。可先让短document尽量完整留在同一worker，只对被拆开的document发送其他query真正需要的prefix；再把这些片段压成连续buffer，避免逐doc小拷贝。划分同时满足每worker等token的非Attention成本与Attention最大负载，过长document仍用PerDoc切分，较短部分才走WholeDoc。它用doc边界、prefix metadata、packing与启发规划换较少通信，不改变原mask或反向梯度归属。[FlashCP受限对照](https://arxiv.org/html/2606.08476v1#S3)仅在单节点八H100与sampled packed序列/head配置中测时，heuristic仍落后ILP，不证明跨节点完整收敛或全局最优。无独立docmask、单doc占主导、计划来不及或净费用反退时，保普通PerDoc/Ring-CP与原同步/梯度验收。<!-- source-family:SF-2026-ARXIV-2606-08476 -->

## 09200：资源驻留与调度优先级不是免费overlap（6分）

作者实读exact-v1 §3–4，reader独立§2–5。§3.1通过GEMM tile大小改变per-block shared memory/驻留block数；不是对任意vendor kernel外加通用resource reservation。双stream与events保证本GEMM完成才启对应collective，随后迭代GEMM可与前collective重叠；higher-priority communication只在资源可用时推进，不抢占已驻留block。

四平台单节点A40/A100/H100各4GPU与MI250X8GPU、固定896MB collective、Llama派生GEMM microbench；不是完整训练step。过低occupancy虽TimeRatio约.3但GEMM本身非最优，高block-count MI250X priority可更慢，较大tile亦有局部反退；不能把作者跨iteration独立性搬进有optimizer依赖的真实训练。未核实现/像素/复现。

actual owner Ch36“Overlap不是免费隐藏”两段已有contention model/资源分配及step completion，但缺tile-residency knob与pending priority的实际资格。拟在原2602.20656 source-family后、频率/energy段前：

> 一个更窄的runtime控制是用GEMM tile改变每block的shared-memory需求和驻留数，为collective留下可共驻资源，再把communication stream设为较高priority；优先级只在资源可用时生效，不会抢占已驻留的compute block。Events仍须保证本次tensor先算出，再启动其通信；后续GEMM能否与前次collective并行，要由真实训练依赖证明，而不能照搬独立microbenchmark的跨iteration流水。[四平台有限对照](https://arxiv.org/html/2606.09200v1#S3)显示，压低occupancy可能改善overlap ratio却损失GEMM吞吐，MI250X高block-count下priority也可更慢。Tile/profile搜索、共享资源与同步成本全计费；依赖、共驻或完整step收益不合时，保普通stream/event、保守配额与顺序执行，不由局部重叠率批准训练提速。<!-- source-family:SF-2026-ARXIV-2606-09200 -->

## Fable 5 / Mythos 5：现有cascade责任链 + 发布约束（6分）

原件 `SUP_ANTHROPIC_FABLE_20261025.html` 307135字符、JSON-LD与article:published_time=2026-06-09T00:00:00.000Z，Jun09 BJT8:00；dateModified=Oct14。页面具名Jun12暂停/Jul1重部署，不把当日available写成当前状态。`SUP_FABLE_CARD_20261025.raw`为317页系统卡，只读p1–9日期/changelog/目录、p13–14§1.5、p57–58cyber机制、p65–68robustness直接反侧。

支持的必要链：target internalactivation probe筛流量，flagged项交trained LLM classifier并结合probe裁定；不要借其训练/scale未披露填实现。现card p14区分clients自动fallback+通知、Messages API默认block/structured category、可opt-in serverfallback及某些接口不可配。Changelog p2 Jun11更新的是frontier-LLM-development safeguards；与distillation是并列类别，不能把它混成“distillation规则Jun11才改”，也不能把整个currentcard都倒填Jun09原版。必要历史细节无法由当前卡精确归属时，只隔离该命题。

反侧：新闻cyber图在block模式且不含evasion，不是production fallback质量；AISI已有singleturn/部分多步jailbreak。bounty公共Opusproxy与Fable probe非完全同一、无API/rewind，1000小时无universal不证明不存在。30天retention/访问日志是厂商发布政策，不认证法遵、零保留或无泄漏；不将biology应用引回暂缓领域。

actual Ch72:1214–1222已明确probe只升级语义classifier、context exchange/prefix训练与部署状态、lateflag不追回及独立output/effect gate；Ch62:112–135/242已绑定解析后model revision、不可降级字段、fallback及receipt。拟本家族“已有覆盖”仅指该cascade责任链；具体provider配置/访问/retention/后续修订仅报告，不称所有发布技术已有覆盖，不新增通用重复段。待reader独立处置核查，不写新Books。
