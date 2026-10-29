# LazyAttention 04302：首次必要 / 6分 / actual Ch45最小PRE

最新行政事实：reader R94–95已实际完整采用，唯一actualPOST通过，指定Ch45窄位释放；新增I19＋旧Kimi1合20。本文待PRE/SAVE/POST为过程时态，不第三必要证据或正文，未授DAY。

作者supp_20260605_author，只补2026-06-05的Jun04自然日。启动重读AGENTS/当前研究与Report合同/Prompt、来源使用/Daily/arxiv/恢复、ROADMAP/Books三公共上下文、仅2026路由与本日最新停点，已实际完整采用R89–91八项收窄准入/精确v1联合日证。不第三abs/DOI，当前notice无撤回信号有效复用。

## 精确原件与读取停止

https://arxiv.org/html/2606.04302v1 GET200/495864bytes，原件`SUP_2606.04302v1_20261025.html`，SHA256 `797dfa88264ffc52bbee31ae14c228a3df5f19e67e1f91da711f5a33adc9549f`。实际首次必要读§1–4全文/Eq1–7/Fact3.2、T1–2、A相关机制比较、B baseline实现、C.4/T6–7、C.5–6/T8–9、C.8–9/T11–12。C.1–3/C.7仅必要上下文和定义，不称全表图像/全附录已审；未核代码、未运行或复现。不读上游/全历史。

精确family检索Books无04302/LazyAttention条目，不等无同机制；本日原件中只有初筛AB/date与本Source，未发现可直接复用的同事件必要/owner有效链。随后实际比较现文（下节），不以marker有无代I/NC。原有cache研究有效层不重做。

## 机制：位置重对齐不修复上下文依赖

§3.1/Fact3.2利用RoPE `(R_m q)^T(R_n k)=q^T R_(n-m) k`；共享文档cache使用固定局部位置/文档offset metadata。不同请求读同一物理cache时，在attention tile内临时完成目标位置的旋转，不在HBM为每个目标offset物化修改后的副本；避免原地旋转共享块的race。不是删掉位置，不把早层hidden/V改成任意新上下文的full-prefill状态。数学相等只对给定兼容cache和相同attention/mask语义的重对齐；原文采用block-attention微调模型/独立文档复用，不能由此签普通causal模型任意文档拼接无损。

§3.2 Prefill长Q tile/短K tile时单次旋转K而非先归零再转两遍，按文档offset table读cos/sin；Decode单Q时遇文档offset变化才在register旋转Q，metadata将block_id/offset/mask打包64-bit，必要时即时算sin/cos以省内环全局访存。这里有额外算量、表/metadata与kernel维护，zero-copy不是零成本；§3.3仍普通dense attention的二次算量和线性KV，不是新的cache policy或任意稀疏算法。

§3.2–3.4 tile理想模型Prefill增量3/(4M)、Decode平均3/(4BN)，不授实测延迟恒等/常数开销；1600-token例的r≤1%与文中不同N/B默认不直接拼成通用数值recipe。Roofline B项把element读数写bytes，实际dtype/metadata和总运行预算须补，本文不照公式给SLO。§3.5只在位置效应可注入score时扩展RoPE/ALiBi；linear attention明确scope外，任意绝对位置相加/hidden位置依赖不能自动纳入。

A承认RoPE-decoupling/MEPIC等已有方向，本次增量是按文档共同offset与phase-specific kernel实现消除物化，不称位置解耦全球首创。C.9 MEPIC-like为作者重实现，非官方artifact，不能把其47.19ms或16%与Lazy40.84/.67%差额泛化为所有MEPIC。B中的BlockAttention-vLLM遇refcount0可原位旋转、否则copy再旋转，对照更具体而非所有baseline永远copy。

## 对照人口 / 关键反侧 / 成本

§4基于vLLM0.8.5.post1 V1、PyTorch2.7/CUDA12.4、Tulu3-Block-FT（8B、Block-Attention微调），主机120GB RAM/GH200 H10096GB；四QA数据集，默认五doc/请求。作者称相同batching/paging/budget，未全披露dtype、所有arrival/seed/CI或productiontrace。C.1有70B TP4/H100，C.2 A10040GB/A4048GB只作局部扩展，不将单点扩大fleet/SLO保证。

T1明确**全部格为trace-driven simulation**：100k doc pool、K10、Zipf alpha1.1/1.5/2.1，非真实VRAM全量实测；§4.1请求是五doc而非同K，不能合成单一end-to-end归因。No-limit仍GPU0.9利用率约66GB可用，非无限内存。Zipf前C与C/D理论例依赖每doc占位模式，不是所有LRU/workload严格命中界。C.8受限16doc×8k/10GB pool/shuffled orders的实测与T1分开。

T2 EM：Lazy69.2平均对Block-vLLM69.3、Full71.8；2Wiki70.7对71.4/Full73.6，Narrative59.7对61.0/Full62.2等反退保留。作者将差异归tokenization/finite precision，但没有完整same-token逐步输出隔离，不能自签精确生成序列/全部质量不变。前提为给定cache的attention恒等，非全文doc依赖修复。

§4.3五doc4096tokens/64query、2048chunk budget、三hot-doc DRAM；同scheduler/batching/paging/launch仅改rotation路径，保受限.13%Decode观测。C.9另一100请求/最多5并发为.67%，两个数不统一成常数；额外每步开销也不由“曲线看似常差”证明永不累积。C.4文字称128k logits max diff低于1e−5，但T7实际max abs=3.7457e−5、relative=5.4829e−7，不能照录前者阈值或补改表；正文不采用硬数值稳定证书。C.6短256token M64优于M128/256，未证单tile普适最优。额外metadata、kernel调优、统计/索引、预计算/搬运、缓存失效和完整请求质量验收都计费；热点/位置复用不足和原生kernel更合适时保普通prefix/recompute。

## 6分 / actual owner具体缺口

Design Delta2＋System Reach2＋Durability2＝6：文档统一offset的prefill/decode算子与物理共享/缓存引用边界联合设计，跨cache manager/attention kernel，稳定的身份与算存取舍；不把RoPE成熟恒等式、机构、性能数字或能映owner计分。因实际长期缺口深入必要条件和反侧，非自动全文配额。

`INFER-KV-CACHE` Ch45；实际读136–166 prefix identity/connector/COW，225–239 chunk因果repair/FrameBlend/wrapper、1768–1778 interleaved位置/conditioning seam和物理copy反侧，1826–1840跨adapter近似/低秩cache tile内重构与位置旋转；邻Ch44/46真实开篇交接。现文已有位置身份不等上下文、原位改共享块需COW、tile内旋转和跨adapter近似分责；但未具体承载同文档跨logical-offset共享一个物理copy、prefill旋转K/decode旋转Q及文档级offset何时切换的执行分支。ForkKV tile旋转服务于base/residual近似分解，不足以代本document reuse/共享引用场景，故有小gap而非无条件NC，不移Ch13重复RoPE主推导。

拟Ch45现227完整causal repair成本/回退段后、FrameBlend完整段前。完整上锚：

> 这种方法节省的不是任意 Prefill，而是被判定为无需修复的部分；代价包括 selection error、额外估计开销和 optimized kernel 难以高效执行的 irregular causal mask。未选 token 仍可能影响答案，作者实验也不能证明选择器跨模型、任务和长度分布保持充分。因此高风险请求、依赖稠密、短 Context 或选择置信不足时，应回退 full-context Prefill；只有模型、chunking、position、selection rule 与 KV layout identity 全部兼容时，局部重算结果才可复用。

完整下锚：

> 持续视频还可把 contextualization 的预算从 idle time 部分移到 query time：先以短窗口写 KV，问题到达后用各层检索的共同 token 候选，一次按时间顺序重预填这些视觉 tokens，只替换原读取集合中的对应 rows。[FrameBlend 的受限对照](https://arxiv.org/html/2610.29229v1)不是恢复完整历史的 exact KV，而是用查询相关重算换较少日常预填；原视觉 tokens 仍保在 CPU，跨层位置与替换身份也须一致。总处理费下降可伴 TTFT 明显增加，部分问答切片反退；存储、传输、选择、重算与窗口调优全计费。新query依赖、质量或响应deadline不合时，扩大原窗口、保留完整重算/读取与独立答案验收，不由少FLOPs或训练免费签发无损与交互SLO。<!-- source-family:SF-2026-ARXIV-2610-29229 -->

## R92修句后批准原两段（root新窄授后已SAVE，待唯一POST）

即便已允许复用文档内部的状态，位置重对齐仍不必先在HBM造一份新cache。可以保留一份共享文档KV，把每个请求的文档起点偏移留作metadata，直到attention tile被读取时才临时施加相对位置变换。[一个受限kernel分支](https://arxiv.org/html/2606.04302v1)在Prefill的长Query/短Key tile中旋转Key，在Decode的单Query路径中仅遇到文档偏移改变才旋转Query，并打包block/offset/mask元数据；这避免修改别的请求正在读取的共享块，也避免为每个目标位置物化副本。它保留位置关系而不是取消RoPE，改变的是给定兼容cache的读法；独立文档缺失的跨文档hidden/Value依赖不会因此补回，普通causal模型的任意拼接仍须重算或另验近似。

这种物理共享与上面的因果修复是两份责任：前者可减少位置副本和搬运，后者决定旧状态是否适合当前组合。需要绑定model、tokens、文档局部位置、目标offset、mask、共享域与kernel配置，不能只按文本相同命中。原文Table 1的命中率全为特定Zipf轨迹模拟，另有受限16文档实测；block-attention微调模型的QA质量仍有反退。MEPIC-like对照也只是作者重实现，不授全部backend或普通模型无损。Tile内变换仍增加计算、metadata、调优、预计算和完整质量验收费用，zero-copy不等零开销；热点/位置复用不足、位置或上下文身份失配、净收益不合时，保留普通prefix cache、已验物化重编码或full-context Prefill，不让较高命中率取代质量与端到端成本。<!-- source-family:SF-2026-ARXIV-2606-04302 -->

## 停止与交接

### 当前R92–93已采用 / root新窄授后真实SAVE

已实际完整读回R92–93：首次必要/正式6分/actual Ch45具体gap与Table1范围修句后原两段PRE通过，不第三原证/AB/date。root本轮fresh实际完整双锚和唯一trueH2 Review notes后新窄授，作者仅将上列修后原两段SAVE于causal repair完整成本/回退段后、FrameBlend完整段前，加本人true-H2注。修句按root完整替句以“反退。”结束，随后原MEPIC-like内容保留；不把所有命中率表冒模拟。完整新增、直接完整上下段及本人整注已实际自读，物理位置复用与context repair分责/全部反侧保留。

写前快照`/private/tmp/lazyattn-0605-save.6SgZbr/ch45-before.md`，SHA256 `2534bf782dc315b7e36c94200d2210aa305c9eaf8bdaaf839205915fdf2b7094`；最终写后SHA256 `822f0a1027d8491b8ecf358befc9fd864eb1e3f7ef3a67e86e7c0916cb660e7b`。只逆除本两段和本人注后整个Ch45字节等于写前，正文family marker/本人注各1，注最近前置真H2为Review notes；原两侧、所有他注和并发差额完整保护。范围核不代reader实际语义POST。

当前仅待唯一非writer actualPOST，I19不提前变I20；真实SAVE/selfread阶段ready即交root释放作者槽，后七必要及三cue校准/有限stop仍ordinary，不因等待扩Methods或NAV。下文首次准备态为本SAVE前过程，不是当前待办。State/index/他日不改，无stage/commit/push。

支持与关键反侧足，首次必要/6分/actual Ch45具体gap及原两段PRE ready即交root/reader，不等Batch4余七Methods；当前未Book授权/SAVE/本人注/POST/I。I19保持；其余八已过AB/date不自动深入完成，三具名title cue另有完整AB原件，待单独初筛，不扩全月/73/706。State/index未改，未stage/commit/push。
