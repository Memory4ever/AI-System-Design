# Jun04 Batch2：先就绪两篇必要证据/actual owner提案

作者supp_20260605_author，2026-10-24。恢复重读当前AGENTS、研究/Report合同、Prompt、来源每日/arXiv及ROADMAP；实际读回reader R13–15并采用。五项准入及Jun04联合日期已通过，不第三核；04056跨日hold不评分/正式候选。前三I及DistIL双争议复用，不第三审。只对本两已就绪项先交接，不等其余三Methods完成。

两完整官方exact-v1 HTML实存`SUP_2606.05037v1_20261024.html`与`SUP_2606.05014v1_20261024.html`，未运行代码/复现。Books公共三上下文已读，actual owner和相邻章节入口已实际核。reader R16–18必要Source/actualowner/PRE及root两新窄授已实际采用；下列两处四段及各本人H2注已实际保存reader R19唯一actualPOST已通过，累计新增I5，窄位释放。

## B2-S1 Self-Reflective APIs 2606.05037v1

评分2+2+2=6：server-owned语义修复值进入typed consumer的跨API/Agent边界是新增，格式化JSON或借用validation本身不计分。标准以上按owner具体知识缺口深入必要§3–6：Schema v0.1、实验接口/runner、leak audit、三模型pilot、负侧/外推和billing replication限制；不全扫其引用或代码。

原文suggestions每项含registered action type及literal parameters。消费者知道词表，可合并到深拷贝后的下一请求，再调用LLM继续，最多5次尝试；HTTP200 body success=false是semantic失败，不能按HTTP状态计成功。Intent disambiguation亦有接口，confidence signaling未测。普通schema只约束类型/字段，server validator知道跨字段、外部状态及私有规则，修复建议与business validator分模块但同源。

关键归因限制已正面采用reader：Verbose保per-rule diagnosis却去掉literal fix；Reflective把同诊断加action+真实fix values。因此**不支持“等信息量仅换结构”因果**；作者的structure独占收益修辞不采用。两leak审计分别检查validator error message和task.description/success_criteria，不等全面语义泄漏检测（已知substring/手列paraphrases只覆盖枚举）。提供答案给受限consumer的好处仍可描述，不因此撤回typed repair接口本身。

Recipe作者自建10任务×3runs=每model/mode30；haiku4.5/sonnet4.6和gpt4o-mini，Fisher两侧与tokens-per-success CI只限各cell，重复任务不是30个独立不同任务。gpt4o-mini核心gap不显著(p.435)、某数值任务Verbose更好/概念已足时平手，实际有效流量通常无需repair，所以per-failure提升不等平均per-call收益。Billing也是作者规则+答案式payload的fictitious API、Stripe sandbox，100%不是外部API独立验证。billed tokens不等latency，原文明确未测latency；hardware/precision/concurrency/SLO不适用本API试验或Not Disclosed，不能作生产延迟/安全证据。低重试成本也不替代反馈制备、API验证/调用费用及维护成本。

Actual owner `AGENT-TOOL-CALLING`，Ch78“Schema 可以拒绝缺字段…”完整段后→“同一调用跨 adapter…”完整段前。现段只说semantic validation与principal，不承载service-owned repair参数到retry consumer；同章SMT规则修复和tool文档学习是不同producer/校验接口。已读邻Ch77/79开头，分别持有memory/planning，不新增并列owner。

最小literal两段（只提案）：

> 语义拒绝之后，服务端还可以把自己掌握的修复知识交给重试消费者，而不只返回错误名称：用有限action词表和literal parameters描述下一请求可作的修改，客户端再解析并重新提交。这个接口适合私有跨字段规则或当前业务状态，不能让模型从通用先验猜出它本来不知道的值。建议只是待验参数，不自动继承原调用的授权；重新提交仍经过schema、业务规则与真实principal检查。这是从接口分责推出的运行要求，不是原实验已证明的安全协议。
>
> Self-Reflective APIs的有限对照还要求分清“增加修复信息”与“只换结构”：Reflective含具体fix值而Verbose不含，不能把收益唯一归于JSON形式。错误返回与任务prompt都可能提前泄露这些值，已知字符串审计不认证完整无泄漏。作者自建小样本中有模型不显著、任务退步与诊断已足的分支；只在失败请求上的恢复率和billed tokens也不是全流量延迟或工具effect保证。反馈构造、全部重试与验证费用均付费，规则/词表漂移或修复意图不明时，保留明确拒绝、人工澄清和原验证路径，不因建议可解析就自动扩大权限。<!-- source-family:SF-2026-ARXIV-2606-05037 -->

## B2-S2 Depth-Attention 2606.05014v1

评分2+1+2=5：新增同token跨depth的原KV槽递归mixed Value接口，单组件层级但可复用；不把普通attention或无参数本身加分。标准以上因owner的跨层状态成本缺口深入§3–5、A模型/FP16设置、B理论成本和实测说明及对应消融，不读无关baseline引用。

Eq2深度权重读当前层q及同token的当前/前层k；Eq3当前层贡献raw v、前层贡献其**已经mixed的v**，不是所有历史raw v直接平均。然后保原q/k/causal mask做序列attention，在标准V-cache槽保存同shape mixed V，后续token/更深层消费该槽，不能拿旧checkpoint的raw KV当兼容新状态。GQA按group平均q，固定stride限制source set；更密source增加training activation及PP跨stage取K/V通信，半深stride在有限消融最好而非通用常数。保causal mask不等bitwise等价原网络，是另行训练的新架构。

Qwen3-style1.5B/3B从头Pile32B同data/schedule/hyperparams，cross-layer baselines均reference PyTorch无custom kernels，基座一致不等每种机制已充分调优或生产kernel等价。Table1逐任务有反退，uniform mixing已有部分收益、value-only较key/key-value好，更多来源不单调。FP16；额外FLOPs理论0.004%却训练wallclock+9.1/11.2%，3B batch64、prefill2048、decode2048总generation526.6→532.8s而非加速，prefill峰值30.6GB未变；无额外persistent inference state不等无temporary activation/IO/PP通信。128K额外内存为理论估计非真实128K SLO。本文必要域未找到硬件型号/重复训练/运行CI，Not Disclosed；不能由较小算术量授hardware或实际分布式吞吐保证。规模只360M–3B/32Btokens，较大模型及data尚未证。未实现/复现fused kernel，作者预期不作事实。

Actual owner `MODEL-TRANSFORMER-LAYER`，Ch17现ExoFormer及IADA两组完整段后→“## Normalization 控制什么”前。现IADA按pooled hidden读历史/gate，与用本身q/k及mixed V原槽是不同接口；Ch16/18开头已读，各自拥有FFN与生成objective，不接管该depth状态语义。

最小literal两段（只提案）：

> 跨层选择也可以放进attention内部，而不另存一组hidden history：对同一token，用当前层query读取当前及前面选定层的keys，混合当前raw Value和那些层已经混合过的Value，再让普通causal attention读取这个结果。Depth-Attention的受限分支把mixed Value原位写入标准V-cache槽，保留原Q/K和mask，因此不扩大持久KV的shape；它却改变了Value内容与后续消费语义，并不是对旧checkpoint或raw KV的无损替换。GQA可在组级读深度，稀疏stride又限制跨层source数，不能把固定半深stride视为普适最优。
>
> 同shape状态复用省去了额外持久buffer，但训练activation、depth读取以及pipeline跨stage通信仍付费。有限1.5B/3B同训练条件的比较有逐任务反退，算术FLOPs很小也不等墙钟为零：未融合PyTorch路径中训练和推理均有开销，更密source并不总更好。128K内存估算不是实际长Context服务证据，fused kernel和更大规模收益尚未验证。质量、cache构造身份或跨设备成本不合时，保留普通residual、原attention与独立hidden路由基线，不因无新增参数或持久槽就承诺速度与SLO。<!-- source-family:SF-2026-ARXIV-2606-05014 -->

## 交接与剩余

R17另核B6 inference明确一次warmup＋两次测量run，修正初笔记可能造成的“未披露运行重复”理解；独立训练重复、运行CI和硬件型号仍未披露，本次不以此授生产稳定性。此为必要证据行政精确化，不重做有效Source。

上述两项实际必要Source/owner/PRE已由reader R16–R18通过，root明确新授后Ch78/Ch17两处各两段与本人true-H2注已真实保存并完整新增/完整直接两侧/本人注自读，限定diff-check通过；reader R19唯一非writer actualPOST已通过，本项整合生效且窄位释放。05158/04193/04945三项已评分但必要Source尚普通，未默认已读全文。机构差额/其余题摘仍ordinary。新增生效I已5、DistIL争议1，不授DAY/FINAL。未stage/commit/push。
