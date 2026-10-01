# PolicyBank / LACE：最小 source→owner 采用提案

作者apr20_resume；未独立通过、未共享Books写入。必要源的实际位置、对照、反证及未证明内容见[v3-reopen-notes“随后四项”](./v3-reopen-notes.md)。两项均2+2+3=7，深入必要内容而非全附件；不因可讲多层故事泛收。

## 15505 PolicyBank → AGENT-MEMORY / Ch77

[v1 §3–7](https://arxiv.org/html/2604.15505v1)。实际Ch77 `从原始轨迹到派生策略`已有advisory / source / supersession并在“即使一条derived strategy…”明确memory不自改workflow policy；后续Failure Trace→Rule有正例误拒淘汰。缺口不是没有可改规则，而是**失败有执行偏离与规范/解释本身不完整两个诊断入口**，检索更多正确原文也可能稳定复制规范误解。拟在该advisory段后、archive回退段前嵌入下述两段，不取代平台policy authority：

> 失败经验还要先区分“没有遵从当前规范”和“遵从了不完整或误写的规范”。前者可以修检索与执行步骤，后者即使忠实重放也会复现错误；只有来自被授权开发者、明确适用域的校验反馈，才可用来提出规范解释的修订候选。派生 entry 可记录 capability、trigger、precondition、eligibility、action 与反例，同时保留原规范及 supersession；Memory 提供可检索的解释，不拥有批准改变业务 policy 的权力。
>
> 这种诊断支付额外校验、版本维护与反例回归成本，稀疏二值结果也可能无法辨认究竟错在哪条资格条件。[PolicyBank](https://arxiv.org/html/2604.15505v1)的受限实验用 benchmark annotation 作为所需行为依据、用解释性反馈修订 entry，曾先过度放宽取消条件再修正；这些标签不自动成为真实组织的授权事实，紧接原任务的 sister 测试也不等远期独立部署验证。反馈不可信、规则冲突或适用域变化时，应保留原 policy 与原始轨迹，交 Workflow/Security owner 核准，不能让更高任务分覆盖权限。

作者source边界：21airline/9retail原任务的三类sister、五order seeds、两API model；pass^k是所有k一致成功，不是pass@k。baseline检索触发输入不完全matched，解释反馈与scalar差异、humanoracle及retail原任务逆序保留；82%为normalized gapclosure非实际成功率。拟采用该诊断/权限分责差异，不采用benchmark policy修补已证明真实治理、未来恶意反馈安全或私有字段实施保证。

## 15529 LACE → MODEL-SELF-ATTENTION / Ch14

[v1 §3–4及E.1/F.1](https://arxiv.org/html/2604.15529v1)。实际Ch14 content-dependent Q/K/V、`Mask定义哪些边可以存在`及数值/实现边界讲单序列，batch默认独立；目前没有同一请求内多个推理thread的显式横向hidden-state路由。拟紧接mask/单序列路由的主线补两段，不新建多Agent workflow、也不拿thread名字为跨tenant通道：

> 多条独立采样能覆盖不同路径，却要等答案完成后才由选择器整合；若同一请求的推理分支需要在生成中交换中间表示，可以在原有序列 Attention 旁增设低维 cross-thread Q/K/V 路径，再以 gate 与原输出融合。thread identity、token position 与可见前缀共同定义连接域：共享请求内的分支才是候选，batch或tenant identity不能因为flatten成一个矩阵就消失。原causal backbone保留，也不自动证明新增横向边没有读取未来位置，必须单独明确其时间mask与缓存生命周期。
>
> 这条分支增加联合训练、分支相关性、共享错误与同步/访存成本，更多thread不再等于独立样本。[LACE](https://arxiv.org/html/2604.15529v1)用低维支路、gate及thread-group训练提供受限机制证据，但本文flattened SDPA公式未明示横向时间mask，不能据其宣称已验证无泄漏实现；它的短微基准虽增加不足1.3% FLOPs，四thread step latency仍增加约31～38%，TPS反而下降。横向信息没有提升独立质量/选择验收、mask语义不清或同步成本不能摊销时，保留独立采样及完成后的voting/selection更透明。

必要反证：Qwen3 1.7/4B、4threads、LACE独有CPT+SFT+RL不与“sameRLsteps”当全budgetmatched；best@4/选择格式与pass@1非同estimand，gate强度不是semantic causal证明。E.1 RTXPRO6000Blackwell97GB/bf16/context50/gen100：4B N4 ms27.6→36.2(+31.2%)、TPS144.8→110.6；N128step+96.4%，不是线上concurrency/p99。F.1只训练细节不补lateralmask；拟采用**横向routing设计与未证明实现边界**，不称当前论文所有因果保证/全算法正确。若独立核判断该限定下不应入Books，可保Only并保原证据；不为消除未决扩所有附录或全复现。

两项书稿拟段都在Review notes前、名称删除后有问题/条件/机制/代价/回退链。还须非作者实际必要source→owner与root窄写锁；没有把提案算I。

## root有限独立采用复核

root非作者实际打开15505v1 §3/5/7与15529v1 §3/E.1，并对读真实Ch77 advisory→权重更新交接、Ch14 causal/padding mask→support分支。复用未变化的作者其余必要对照阅读，不声称复现实验或全附件复核。

- **15505窄采用PASS**：规范不完整与执行偏离的诊断在现有advisory边界内补足，而非授予memory改policy的authority。原文feedback来自trusted developer/benchmark所需行为，binary与解释反馈差异及过度放宽后反例修订均可定位；拟稿保留额外校验、任务近邻与真实组织授权的区别，不采用Gap→空集为已证收敛。所需行为标签不能取代实际权限，两个拟段可写Ch77指定位置。
- **15529窄采用PASS**：实际Eq1–6给低维cross-thread QKV/flattened SDPA/gate，却未在该式提供新增路径的完整时间mask；拟稿只解释条件性横向交换设计与需验mask/缓存身份，不宣称实现无泄漏。E.1单RTX PRO6000 Blackwell、BF16、context50/gen100的<1.3% FLOPs与N4 step约31～38%增加/TPS下降是不同量，正文须在数字附近保留这些条件，不把microbenchmark当服务concurrency/p99；独立采样仍是透明回退。两个拟段可写Ch14指定位置。

以上仅源→实际owner的窄采用，不计实际整合或日级Gate；实际书稿写后仍需作者外检查。

## root实际写后复核

root非作者实际顺读Ch77 advisory之后的15505两段及其权重更新交接、Ch14 causal/padding mask之后的15529两段及后续support分支。两处**实际写后PASS**：PolicyBank将规范解释错误与执行偏离拆开且仍由Workflow/Security核准，不以更高任务分改变授权；LACE将同请求thread表示交换与跨tenant/batch分离，横向时间mask未证边界、同步/共享偏差与独立采样回退保留，实测成本附近包含单RTX PRO6000 Blackwell/BF16/context50/gen100，不外推p99。采用命题与先前必要来源一致，章末notes只同步写后状态；可计本日实际整合10，不等日Gate。未复现实验或验证生产部署。
