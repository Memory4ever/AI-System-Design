# 第47章 PagedAttention

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-PAGED-ATTENTION`
**Legacy Chapter:** Ch43
**Status:** Draft

**Roadmap Intent:** 像操作系统管理内存一样管理 KV Cache。

## 本章要回答的问题

为什么 KV Cache 不能简单地为每个请求预留一大段连续显存？PagedAttention 为什么会借鉴操作系统的 paging 思想？它解决的是 attention 公式本身的问题，还是 KV Cache 的内存管理问题？

本章的核心判断是：**PagedAttention 不改变 Attention 数学语义，而是用 block table 将逻辑连续的 KV positions 映射到离散物理 blocks。**它把按最大长度预留的问题改写为按需分配，并将浪费约束到 block 粒度附近。

## KV Cache 为什么会碎片化

在 LLM Serving 中，每个请求的 KV Cache 都会随着生成不断增长。问题是，系统事先不知道一个请求最终会生成多少 token。

如果为每个请求提前预留最大长度的 KV Cache，短请求会浪费大量显存。如果按实际长度动态分配连续显存，又会遇到外部碎片：请求不断进入、完成、释放，不同长度的 cache 块在 GPU memory 中留下空洞。

这很像操作系统管理进程内存的问题。程序逻辑上希望自己看到连续地址，但物理内存可以是不连续的。操作系统用页表把逻辑页映射到物理页，从而降低连续分配压力。

PagedAttention 把这个思想迁移到 KV Cache。

分页并不会消灭所有浪费。最后一个 block 可能没有被 token 填满，形成 bounded internal fragmentation；它解决的是大块预留和连续分配造成的浪费，将最坏浪费限制到 block 粒度附近。

## 逻辑连续，物理离散

在 PagedAttention 里，一个请求的 KV Cache 被切成固定大小的 block。模型逻辑上仍然认为自己在访问连续的历史 token，但底层物理显存可以是不连续的。

可以理解为：

```text
Logical KV blocks for request A:
  A0 → A1 → A2 → A3

Physical GPU blocks:
  #7 contains A0
  #2 contains A1
  #13 contains A2
  #4 contains A3

Block table:
  logical A0 -> physical #7
  logical A1 -> physical #2
  logical A2 -> physical #13
  logical A3 -> physical #4
```

这里的重点是：逻辑上连续的 token 序列，在物理显存中可以被打散存放。只要 block table 能正确映射，attention kernel 就能找到对应的 K/V block。

## 它到底优化了什么

PagedAttention 主要优化 KV Cache memory utilization。

它带来的收益来自几个方面。

第一，按需分配。请求生成到哪里，就分配到哪里，不需要为最大输出长度提前预留完整空间。

第二，减少碎片。固定大小 block 更容易复用，系统不需要寻找一整段连续显存。

第三，支持共享。某些请求可能共享 prompt prefix，或者在 beam search、parallel sampling 中共享早期 token。block 级管理使 KV Cache 共享和 copy-on-write 更容易实现。

第四，提高 batch 上限。当 KV memory 浪费减少，同一张 GPU 可以容纳更多并发请求，continuous batching 的空间也更大。

这也是 vLLM 论文把 PagedAttention 放在 serving throughput 问题中的原因：吞吐不是只由 compute 决定，也受 KV memory 是否能高效装下更多请求影响。

注意这是一条间接路径。PagedAttention 本身不会减少模型权重 FLOPs，也不会消除自回归依赖；它通过提高可用 KV capacity，让 scheduler 有机会维持更大的有效 batch。

## Block 数量与内部碎片

设 block 可容纳 `S_b` 个 tokens，请求当前长度为 `T_r`，则需要：

```text
N_blocks,r = ceil(T_r / S_b)
```

最后一个 block 的未使用 slots 为：

```text
waste_r = N_blocks,r * S_b - T_r
0 <= waste_r < S_b
```

相比按最大长度 `T_max` 预留，paging 将单请求末尾浪费限制在一个 block 内；实际 memory 仍包含 block metadata、alignment 和 allocator reserve。

例如 `S_b=4`、`T_r=10` 时需要 3 个 blocks，最后 block 浪费 2 个 token slots。若 block size 改成 16，只需 1 个 block-table entry，却浪费 6 个 slots。Block size 因此是 metadata/kernel efficiency 与内部碎片之间的权衡。

一个token位置在不同head中不再保留同样长度时，页的内部碎片还会沿head维度返回：只要所有head共用同一长度的分配，短head删掉KV也可能仍被最长head锁住物理容量。一条[受限非均匀缓存分支](https://arxiv.org/html/2606.06302v1#S4)先从离线profile固定每层各head的保留预算，再按相近预算分组，为每组维护独立页表，并复用按该shape准备的kernel分割计划。这里固定的是容量形状，不是每次选中的token；减小group能少留空洞，却增加页表、host维护和kernel接线费用，仍需保持原head身份与位置映射。

静态预算也不能直接当作请求峰值显存证书：KV双份、组内最大值、页对齐和metadata之外，还须另计压缩前的Prefill瞬时空间、后续增长与reserve。少量pilot上的预算稳定不保证新domain同样成立，固定split也不批准完美balance、零在线成本或质量无损；本地vLLM/A100对照不替完整服务SLO。Profile、token选择、页表/分割产物和实际kernel应绑定同一模型/布局版本并计全部费用；预算、质量或真实峰值失配时，回退较保守保留、普通统一页与动态规划，而不由逻辑压缩率放行更多请求。<!-- source-family:SF-2026-ARXIV-2606-06302 -->

模型共置时，固定token数的block不一定占相同字节；各engine独立预留KV pool虽简单，却不能把空闲容量直接借给另一种布局。一个物理分配分支先预分配共享tensor，以参与模型KV block字节数的公倍数作统一slab，一slab只容一种block-size class，manager记录FREE/PARTIAL/FULL与块占用，返回slab及局部block ID；各engine再按本类每slab块数形成自己的block编号与tensor view。[这种共享slab接口](https://arxiv.org/html/2509.06261v1)借的是物理空间，不是跨模型复用KV内容，也不由相同字节数认证model/TP/KVdtype/量化scale与layout兼容。仅全空slab才能回pool并重格式化给另一类，尚有live block时不能直接转借；视图/映射更新、GPU读取与回收同步仍须真实实现验收，不能把分配登记当完成。公倍数膨胀、未满slab、class偏斜、reserve/alignment/metadata及manager都付费，不采零碎片或零开销。原对照中的Prism重实现已使用slab，不能把主吞吐差全归allocator；另有排序、placement和局部队列共同变化，单模型FP16消融也不证混精度争用已解。低bit cohort没有对齐质量回归，平均profile与decode tokens/s不替峰值容量、全部到达/丢弃请求的TTFT/TPOT或端到端SLO。量化/装载/profile、共享表与views/同步、调度预测及全部质量和失败回归均计费；真实布局、同步、容量或质量未验时，保独立已测pool、普通分页/静态partition与保守余量和队列，不能以共享容量批准状态混用。

<!-- source-family:SF-2025-ARXIV-2509-06261 -->

### 当 Token 已被淘汰，Block 仍可能无法回收

PagedAttention 将连续大块预留改成固定 block allocation，但它的回收接口仍以 block 为单位。只要请求保留
完整历史，除最后一个 block 外通常没有空洞，这个粒度既简单又高效；问题出现在 H2O、Scissorhands 等
token-level KV eviction policy 开始删除 block 中间的 tokens 时。逻辑上已经死亡的 slots 若散落在多个
blocks，allocator 仍不能释放任何一个含 live token 的 block，内部碎片便以新的形式返回。

更细粒度的演进不是让 eviction policy 直接操作 allocator，而是在两者之间增加 token liveness 与物理
placement 的解耦层：

```text
eviction policy owns logical live / dead decisions
→ token table maps logical token identity to block + offset
→ reclamation planner packs live tokens when net blocks can decrease
→ asynchronous copies update physical placement
→ mutable slot map becomes visible before the next attention read
```

这里必须分开两个 commit。Eviction 决定哪些语义状态可以丢弃；reclamation 只把同一组 retained K/V 搬到
更少 blocks。后台搬运要保持 token conservation、unique mapping 与 pre-attention visibility，并在复制期间预留
bounded headroom；否则“回收显存”可能先耗尽显存，或让 kernel 读取尚未完成的 destination。CUDA Graph 也不应
因每次 relocation 重捕获，稳定 tensor 与 graph input 可以保留，只在 replay 前更新 slot mapping 并通过 event
建立依赖。

这条分支获得可回收的 token-level holes，却新增 planner work、copy/decode contention、mapping version、共享
prefix 的 Copy-on-Write 边界和 distributed shard coordination。Native full-retention path 在显存压力不高、质量
要求禁止 token eviction 或 relocation 收益不足时仍是优先基线；token virtualization 只在 eviction 已经成立且
预计释放的 blocks 足以覆盖迁移成本时启用。它扩展 paging 的回收粒度，不取代 block allocator。

## Prefix Sharing 与 Copy-on-Write

两个请求拥有相同 8-token prefix、block size 为 4 时，可以让前两个 logical blocks 指向同一组 physical blocks：

```text
request A table: [#7, #2, #11]
request B table: [#7, #2, #19]
```

共享 prefix blocks 应保持不可变。请求进入不同生成分支时，为各自的新 logical block 分配独立 physical block；若共享的最后 block 尚未填满且需要追加，则必须 Copy-on-Write，不能直接修改其他请求仍引用的数据。

Memory manager 因此需要引用计数或等价 ownership 机制。释放 request A 时，`#7` 和 `#2` 只有在 B 等其他引用也结束后才能回收。

软件上的不可变还不等于物理字节完整。共享prefix的同一份KV若在驻留期间受到内存故障，后续命中的key、block table和refcount都可能仍合法，却反复读取损坏状态；影响范围是实际引用该块的请求，不必扩散到其它prefix。可以在整块计算完成后封存tensor内容摘要，并在复用前按同一布局验核，失配时使块失效、从可信模型重算。这增加的是materialization-ready、sealed与reuse-check状态，不能把登记进hash map的时刻当GPU写入已完成，也不让内容仍流畅替代字节完整性。<!-- source-family:SF-2026-ARXIV-2604-17249 -->

[共享KV的有限故障注入](https://arxiv.org/html/2604.17249v1#S6)只支持理想目标、单bit/BF16与所测驻留窗口，不证明真实租户已能实施定向硬件攻击。CPU调度时验核仍有检查到GPU读取之间的窗口，新块延迟封存也须处理，因此“一批内的损害界”依赖具体同步和失效语义，不是零错误保证；单batch、统一内存的微小吞吐差又不能外推独立GPU与并发命中。摘要保存、搬运、验核和失配后的prefill均计费，硬件ECC、salt隔离与TTL重算仍各有用途；完整性或费用前提不齐时，保留私有缓存、缩短复用期或重新计算，不由高命中率批准长期共享。<!-- source-family:SF-2026-ARXIV-2604-17249 -->

## Kernel 怎样保持语义

Attention kernel 对每个 logical token position 计算其 block index 与 block offset：

```text
logical_block = floor(position / S_b)
offset        = position mod S_b
physical      = block_table[logical_block]
```

随后从对应 physical block 读取 K/V。间接寻址改变 memory access path，却不能改变 position 顺序、causal visibility 或 numerical contract。

分页对象还可以进入多个可组合算子，而不只由一个attention kernel读取。一个[受限分页tensor分支](https://arxiv.org/html/2606.06453v1#S4)让每个对象携带sequence边界与page-index映射，逐请求应用算子后，再传播输出shape和新分配或复用的页；长短不同的中间结果可保持ragged布局，不必先拼成矩形再拆回。这个接口仍要求请求之间独立、非序列维相容，算子不能通过变换batch维偷偷跨请求混合；真实token位置与causal可见性也不能由逻辑连续view重写。

Query-independent的块摘要与query-dependent的累计统计又有不同身份：共用KV的allocator或page机制，不使统计自动取得跨prefix/分支共享资格。Namedcache的声明、更新/重置时点与请求映射须另验；layout传播合法也不证明稀疏选择等同full attention，随机早停的近似TopK还需独立质量预算和exact回退。Metadata、auxiliary驻留、选择与转换都计费；布局、统计身份、支持的backend或质量不合时，回到原已验paged kernel、重建请求局部统计或full attention，而不因算子可组合批准无损与服务SLO。<!-- source-family:SF-2026-ARXIV-2606-06453 -->

正确性测试应在相同模型与 deterministic decoding 下比较 contiguous/paged、shared/unshared 和 allocate/free/reuse 路径。Block table 错一项可能产生合法数值但错误的输出。

## 和普通 attention 的关系

PagedAttention 容易被误解成一种新的模型结构。更准确地说，它是在保持 attention 语义的前提下，改变 KV Cache 的存储和访问方式。

标准 attention 关心的是：

```text
当前 Query 如何与历史 Key 计算权重，
再用这些权重聚合历史 Value。
```

PagedAttention 关心的是：

```text
历史 Key / Value 不连续存放时，
attention kernel 如何通过 block table 找到它们。
```

所以它属于模型机制和系统实现之间的交界：数学语义仍是 causal attention，但运行时 memory layout 被重新组织。

## Trade-off

PagedAttention 不是免费优化。

首先，它需要 attention kernel 支持 block table 间接访问。连续 tensor 访问很简单，分页后的非连续 block 访问会增加实现复杂度。

其次，block size 是一个权衡。block 太大，内部浪费增加；block 太小，metadata 和调度开销增加，kernel 访问也可能更复杂。

再次，PagedAttention 解决的是 KV Cache memory allocation 和 fragmentation 问题，不直接解决 decode 串行性。它能提高 batch 上限和显存利用率，但生成仍然是逐 token 的。

最后，它也不是唯一可能路径。后续一些工作尝试通过 CUDA virtual memory 等方式保留虚拟地址连续性，同时延迟物理分配。这说明 PagedAttention 是一个重要设计点，但不是最终答案。

## 和 vLLM 的关系

vLLM 把 PagedAttention 作为核心设计之一，用它支撑高吞吐 LLM Serving。更完整地看，vLLM 不只是 PagedAttention，还包括请求调度、continuous batching、KV block 管理、并发请求生命周期等系统能力。

因此在知识树里，本章只讲 PagedAttention 的内存管理思想；第 50 章的 LLM Serving Engine 案例会进一步讨论 vLLM 如何把这个机制和 scheduler、API、distributed inference 组合起来。

### Shared Prefix 与 Private Suffix 可以使用不同页粒度

统一小页降低 suffix 内部碎片，却增加共享 prefix 的 block table、refcount 与 kernel metadata；统一大页便于连续读取，又会浪费短而频繁变化的 private suffix。Allocator 可让高复用共享 prefix 使用连续大粒度 HOT region，让请求私有 suffix 使用 token/small-page COLD region，并在生命周期变化时受控迁移。它改善 locality 与 metadata，却引入双 allocator、迁移、边界碎片和 CoW 复杂度；长度和复用均匀时统一粒度仍更稳。`arXiv:2608.15584v1` 的 GraniKV 结果只覆盖作者 runtime/workload，不证明所有 prefix 分布或 kernels 都适合该切分。

<!-- source-family:SF-2026-ARXIV-2608-15584 -->

## 同一请求内部也可能需要不同分配粒度

统一 page size 简化 allocator 和 attention kernel，但长共享 prefix 与短 private suffix 的复用、碎片和访问模式不同。高复用 prefix 可以放入 contiguous hot pool，suffix 保持 token-granular cold pages，再由 dispatcher 在两个 backend 间组合读取。这避免为了 suffix 灵活性切碎 prefix，也避免为了 prefix 连续性浪费 suffix 容量。

双 allocator 会增加 metadata、迁移和 kernel dispatch 复杂度；共享 prefix 短、复用低或请求同质时，统一分页依旧更可靠。是否启用必须同时核算存储节省、cascade attention、调度开销和 fallback，而不是只看 cache hit。

## 本章在知识树中的位置

```text
KV Cache
→ KV memory fragmentation
→ PagedAttention
→ conditional token-level reclamation
→ vLLM
→ GPU Memory
→ 推理调度
```

PagedAttention 是从 KV Cache 进入 LLM runtime 内存管理的关键节点。

## 从机制演进到系统设计

PagedAttention 从解决连续 KV 分配碎片，演进到 prefix sharing、copy-on-write 与可编程 sparse index 后，page table 成为请求可见性的状态边界。Agent workload 可以通过索引选择减少读取，但 kernel 只能执行已声明的 sparse pattern，不能证明被跳过的信息不重要。

更灵活的分页和稀疏读取降低 HBM 浪费，却增加 metadata、index drift、共享隔离和数值验证成本。pattern 未校准、请求高风险或 page identity 不一致时，应回到 dense attention 或私有 KV；分页优化继续保持模型语义不变这一基本合同。

## 自检问题

1. 为什么为每个请求预留最大 KV Cache 会浪费显存？
2. PagedAttention 中 logical block 和 physical block 分别是什么？
3. 为什么操作系统 paging 的思想能迁移到 KV Cache？
4. PagedAttention 提高吞吐的间接路径是什么？
5. `ceil(T_r/S_b)` 为什么能限制末尾内部碎片？
6. Prefix sharing 为什么需要 Copy-on-Write 或不可变 block？
7. PagedAttention 的 trade-off 是什么？
8. Token eviction 后为什么会重新出现内部碎片？Liveness decision 与 physical reclamation 为什么应由不同 owner 负责？

低秩 KV page 的 canonical 机制由 [Ch45](./45-why-kv-cache-speeds-up.md) 负责；本章只补充执行交接：allocator 必须把 rank、factor layout 与重构 kernel 版本视为 page metadata，迁移或复用时不能只复制逻辑 page ID。

## 小结

PagedAttention 把 request 的逻辑 token 序列与 physical KV placement 解耦。Block table 支持按需增长、固定粒度回收、prefix sharing 和 Copy-on-Write，使 Continuous Batching 能在变长请求下维持更高有效并发。当上层进一步采用 token eviction 时，第二层 token table 可以在不改变 retained KV 的前提下把逻辑空洞重新压回可释放 blocks，但必须支付 relocation、versioning 与可见性同步成本。

它解决的是 state placement，不是 autoregressive serial dependency。下一章转向时间维度，讨论怎样减少昂贵 target model serial steps。

## Review notes

- `SF-2026-ARXIV-2606-06453` — jun06_continue接替supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 §3–5/6.3–6.4/Limitations/8–9/11.2–11.3/13必要，保原3+3+2=8/唯一Ch47。只paged对象sequence/page metadata跨算子与auxstat身份，compiler优化归Ch49不重复。保batch/shape支持、approxTopK有损/阈值反侧、质量预算、channel表文矛盾与全fee，不授prefixstat自动共享/无损或SLO。旧有效摘要复用/错genericNC不沿，旧归属不搬。未核图像素/代码/复现；R11首次必要/PRE通过，root本轮fresh窄授后已实际SAVE/完整自读，R12唯一actualPOST通过，实际I5生效、窄位释放；仅行政同步既成结果，不授DAY。

- `SF-2026-ARXIV-2606-06302` — supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 §2.2/3–5/7与Alg1必要，保原2+2+2=6/唯一实际Ch47。仅headgroup物理回收/shape与peak分责，保profile漂移、组表fee、原容量式/CTA分配不闭和受限runtime；不采zerooverhead、精确recipe/峰值/质量或SLO保证。旧Jun05日期/候选不搬，旧机制摘要复用而错NC不沿；未看图像素/代码/实验复现。R7首次必要/原两段PRE/root本轮fresh新窄授后已逐字真SAVE并完整新增/直接两侧/本人注自读，R8唯一actual完整新增/直接两完整侧/本人注POST通过，实际I3生效与窄位释放；只行政同步，不第三研究或授DAY。

Primary-source 校验入口：

- Efficient Memory Management for Large Language Model Serving with PagedAttention: https://arxiv.org/abs/2309.06180
- vToken（token-level liveness 与 block-level reclamation；Status: Experimental；single H100 / single-GPU
  decoding scope）: https://arxiv.org/abs/2608.13263

本轮 Review 补充了 internal/external fragmentation 的边界，并明确 PagedAttention 通过 KV capacity 间接影响吞吐。论文中的设计与当前 vLLM 实现不能视为完全同一版本；本章保留机制不变量，具体 block manager 与 kernel 行为应以目标版本文档和代码为准。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-06453:start -->
- `SF-2026-ARXIV-2606-06453` — Daily `2026-06-05`；primary `arXiv:2606.06453v1`；Books review `books-review:SF-2026-ARXIV-2606-06453`。

  **已吸收的语义增量：** Programmable sparse-attention indexes and kernels change request-level serving state and execution for Agent workloads.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06453:end -->

- `SF-2026-ARXIV-2604-17249` — Daily2026-04-22补Apr21，supp_apr22_author_fresh；[exact-v1](https://arxiv.org/html/2604.17249v1) §3/4、§5.2–5.4/T5、§6/7，2+2+2=6，安全受影响内容深入。只采共享物理块ready/seal/reuse-check生命周期与条件性失效重算；理想SFI非真实租户攻击、TCR非harm、同步窗口和统一内存/单batch成本限制近文。root必要Source/实际owner/A18逐字PRE通过，作者限定保存两段与本人注，root非writer实际完整COW/refcount→新两段→Kernel及本人注POST通过，窄lease释放；作者仅同步已发生行政状态。日期资格另核，不授零错误、实现/复现或日级。

- `SF-2025-ARXIV-2509-06261` — Darwin继任Godel，Daily2025-09-10补Sep9；作者96/Bacon134实际[FineServe exact-v1](https://arxiv.org/html/2509.06261v1)§3–7/式1–3/Alg1–2/T1–4必要域，原2+2+2=6/日期/P复用，唯一Ch47跨model/precision物理slab/class/localID/view与全空回收差额通过；Ch45量化身份/Ch56调度仅既有交接。保物理共享非内容复用、公倍数与partial/reserve成本/真实同步资格、Prism*已slab/局部单FP16及多协议/drop分母、µ/平均F/贪心/算法分支未闭和量化质量/全费。未核像素/code/runtime/实机或质量复现，不补scheduler最优/零碎片或完整实现保证，不回填v2；逐字PRE/root新位/实际POST仅后到事实，不预DAY。
