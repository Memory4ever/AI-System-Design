# 第48章 Speculative Decoding

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-SPECULATIVE-DECODING`
**Legacy Chapter:** Ch44
**Status:** Draft

**Roadmap Intent:** 用小模型猜测，大模型验证，缓解自回归串行瓶颈。

## 本章要回答的问题

自回归 Decode 每次只能生成一个 token，这是 LLM 推理延迟的根本瓶颈之一。Speculative Decoding 为什么能让大模型“看起来一次生成多个 token”？它为什么不是简单地用小模型替代大模型？它在什么条件下才真正有效？

Speculative Decoding 的直觉可以概括为一句话：**小模型先写草稿，大模型批量审稿。**

本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**

## 从 Decode 串行瓶颈开始

普通 Decode 的流程是：

```text
大模型生成 token 1
→ 把 token 1 接回上下文
→ 大模型生成 token 2
→ 把 token 2 接回上下文
→ 大模型生成 token 3
...
```

生成 `K` 个 token，就要运行 `K` 次大模型 forward。这个串行依赖无法简单通过扩大 batch 消除，因为同一个请求内部下一个 token 依赖上一个 token。

这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？

## 草稿模型和目标模型

Speculative Decoding 通常有两个模型角色：

- `Draft model`：较小、较快，负责快速生成候选 token。
- `Target model`：原本要服务的较大模型，负责验证候选 token，并保证最终输出仍然符合目标模型的分布。

可以把流程拆成五步：

```text
1. 传统 baseline:
   target model 生成 4 个 token，需要 4 次计算。

2. 投机:
   draft model 快速生成 5 个候选 token。

3. 验证:
   target model 通过一次 forward 并行验证这些候选 token。

4. 接受 / 拒绝:
   连续通过的前缀 token 被接受。
   第一个不通过的位置之后全部丢弃。

5. 回退:
   target model 生成正确 token，进入下一轮。
```

如果 draft model 猜得足够准，那么大模型一次验证就能接受多个 token。这样，单位大模型 forward 产出的有效 token 数增加，Decode 吞吐和 latency 都可能改善。

## 为什么验证可以并行

自回归生成慢，是因为“生成下一个 token”依赖前一个 token 的结果。但如果 draft model 已经给出一串候选 token，大模型就可以把这串候选当作已知序列，计算每个位置上目标模型会给出的分布。

也就是说，大模型不需要一步一步“发现”这些 token，而是在一次前向中检查：

```text
如果上下文是 prefix，
draft token 1 是否可接受？
如果上下文是 prefix + draft token 1，
draft token 2 是否可接受？
...
```

这利用了 Transformer 在一个序列内部并行计算多个位置表示的能力。生成是串行的，但验证一段给定序列可以并行。

## 它不是近似替代

### 当 Draft 可能优于 Target，系统进入效用仲裁分支

经典 speculative decoding 的正确性前提是 target 拥有最终分布，draft 只是 proposal，因此 rejection sampling 必须保持 target exactness。若某些输入上 draft 本身质量更高，选择 draft 输出就不再是 exact acceleration，而是新的 model-routing 决策；仲裁器必须显式拥有 utility、风险和成本契约，并与 lossless verification 分开。收益是可能避免“更大 target 覆盖更好 draft”，代价是失去单一分布保证、需要独立校准和回滚。要求严格复现 target 时，经典接受规则仍是唯一合理路径。当前证据只支持特定评测中的相对质量现象，不证明 draft 普遍优于 target。

<!-- source-family:SF-2026-ARXIV-2605-24793 -->

一个常见误解是：Speculative Decoding 就是用小模型替代大模型生成。

不是。小模型只负责提出候选，大模型仍然决定哪些 token 被接受。经典 speculative decoding / speculative sampling 的目标是在加速的同时保持目标模型原有输出分布。也就是说，系统希望加速的是采样过程，而不是换成另一个模型的行为。

这点很重要。否则它就只是模型压缩或蒸馏，而不是 speculative decoding。

## 接受规则为什么不能只是“两个模型输出相同”

在 greedy decoding 中，可以直观地比较 draft token 是否与 target 的选择一致。但在 sampling 中，如果只接受两个模型恰好采到相同 token，会改变目标分布或浪费大量候选。

经典 speculative sampling 根据 draft distribution `q` 与 target distribution `p` 计算接受概率；拒绝时再从经过校正的 residual distribution 采样。它的关键性质是：最终样本仍服从 target model 的分布，而不是仅仅“多数时候看起来一样”。

因此“target model 生成正确 token”只是一种直觉说法。严格系统实现必须区分 greedy verification 与 distribution-preserving sampling。

## Exact Acceptance 机制

设 draft distribution 为 `q(x)`，target distribution 为 `p(x)`。对 draft 采样出的 token `x`，经典 acceptance probability 是：

```text
a(x) = min(1, p(x) / q(x))
```

若接受，则继续验证下一 draft token；若拒绝，则从校正后的 residual distribution 采样：

```text
p_residual(x)
= normalize(max(0, p(x) - q(x)))
```

这组规则保证每个最终 token 的边缘分布仍来自 target model。工程实现还需处理 floating-point、zero probability、batch mask 和第一个 rejection 后的 KV rollback，但不能把规则简化成“概率更大就接受”。

## Lossless Verification 是分布契约

Exact acceptance 不只是一个实现细节，而是 speculative decoding 的语义边界：

```text
lossless verification:
execution path changes
target sampling distribution stays unchanged

lossy verification:
acceptance rule changes
output distribution also changes
```

一旦系统为提高 accepted progress 而放宽 acceptance rule，它就不再只是 runtime
optimization，而是在引入新的 decoding policy。此时必须同时说明质量目标、允许的
distribution shift、适用 workload 和 rollback 条件，不能只用 acceptance rate、
block efficiency 或 tokens/s 宣称“更快”。

这也反向约束 drafter training objective。Forward KL 在 drafter 容量足够时与 perfect acceptance 共享全局最优，
且 early training 梯度平滑，因此仍是合理基线；但在 capacity-limited 可达区域，更低 KL 不保证更大的
distribution overlap。单 token exact acceptance 满足 `alpha = sum_x min(p(x), q(x)) = 1 - TV(p,q)`，因此可用
KL 到 TV 的自适应 hybrid，或对 `-log(alpha)` 优化，让训练信号更接近 runtime 实际消费的 overlap。

直接对齐 acceptance 会增加 target、temperature、domain、draft architecture 与 verification rule 的 coupling；
低 overlap 还可能放大 gradient，必须做数值保护。它改善 proposal quality 也不等于 goodput，因为 verification
shape、batching 和 scheduler cost 仍存在。LK Losses 为这条 objective-to-runtime alignment 提供了实验性证据，
不证明其固定 mix、head weighting 或作者吞吐结果可跨 workload 外推。

这个边界也改变 benchmark baseline。若 verification 只接受 `min-p`、`eta` 等
truncation policy 所允许的候选，比较对象应是 target model 在**相同 truncation
policy** 下的 sampling。拿它与未截断 target baseline 比较，会把 truncation 自身的
行为变化和 verification 的效果混在一起。

因此，一个可审计的实验至少要固定：

```text
target / draft model revision
+ tokenizer
+ temperature and truncation policy
+ verification rule
+ draft length / tree shape
+ precision and hardware
+ workload, concurrency and SLO
```

2026 年一项预印本把现有 lossy verification 归纳为 truncation-based 与
collaborative 两类，并报告 draft probability overshoot 是后者的重要 failure mode。
该 taxonomy 和经验结论仍属 `Status: Experimental`；本章只吸收更稳定的原则：
**放宽 exact verification 就是在修改 sampling contract，必须用 matched-policy
baseline 同时评估速度与质量。**

## 接受长度小例子

Draft 一次提出 4 个 tokens。若前 3 个依次通过，第 4 个拒绝，则本轮 target verification 至少推进 3 个 accepted positions，并在拒绝位置按 target-corrected distribution 产生 replacement token；第 4 个以后依赖错误 prefix 的候选全部作废。

衡量收益时应记录：

```text
accepted_tokens_per_target_step
draft_cost
verification_cost
rollback / scheduling overhead
```

Acceptance rate 高不等于端到端加速一定高。若 draft 自身昂贵、verification shape 低效或 target batch 被打散，节省的 serial steps 可能被额外 work 抵消。

一个粗略的判断框架是：

```text
benefit exists when
cost(draft + one verification)
< cost(replaced target serial steps)
```

它是测量框架而非通用 speedup 公式；真实结果必须绑定模型、draft length、batch、hardware 和 workload。

## Verify Length 不是孤立的固定超参数

一次提出更多 draft tokens，不代表应该全部进入 target verification。越靠后的候选需要前面
所有 tokens 都被接受才有价值，其 expected prefix survival 往往逐步下降；与此同时，
verification positions 会占用 target batch 的 token budget。高并发时，把低存活概率的
suffix 塞进 batch，可能挤掉其他请求更确定的 Decode progress。

因此 verify depth 更适合被理解为容量决策：

```text
choose verify depth to balance
expected accepted progress
- draft and verification cost
- opportunity cost of target batch capacity
```

这不是说某一种动态算法天然最优。在线策略需要估计 prefix survival，并结合当前 engine
在不同 verification shapes、batch composition 和硬件上的 throughput profile。若
confidence calibration、traffic mix 或 scheduler 行为变化，旧 profile 就可能失效。

### 接受率损失要分成 Information Floor 与 Model Gap

Block drafter 在一次 proposal 中并不知道 target 将实际提交的前序 token，因此后位置缺少 realized prefix information；
这部分是接口带来的 information floor。除此之外，drafter 对已知条件的建模误差才是可训练的 model gap。只观察平均
accepted length 会把二者混在一起，进而错误地把所有拒绝都归因于 drafter 太弱。

可用一个只补充已实现前序 token 的诊断 probe 估计 floor，再与当前 block drafter 比较；但 probe 不是新的 serving
方案，也不能绕过 target verification。这个分解帮助判断应该改 model、改变 block interface，还是接受不可偿还的串行依赖；
代价是额外诊断执行与更细的 workload slicing。若单 token drafting 已经满足 SLO，或 block 内依赖弱，原来的 aggregate
acceptance/cost profile 仍是足够的工程指标。

2026 年 DSpark 预印本用 semi-autoregressive drafter 与动态 verify length 展示了这条方向，
随后也出现 runtime integration；论文中的生产收益仍是作者在特定 DeepSeek workload 上的
实验，缺少完整 workload contract，故本章只吸收长期原则：**speculation policy 必须看到
全局 target capacity，而不能只最大化单请求 draft length。**

### 从全局 Verify Length 到输入自适应 Block Policy

全局动态 depth 让 runtime 根据 acceptance profile 和 batch capacity 调整本轮预算，但同一 workload 内的输入
也可能拥有不同可预测性。固定长度在分布稳定、controller 不可校准或 batch 形态简单时仍最容易复算；当最优
长度集中在训练 block 附近的小范围内，可以把选择改写成受约束分类，而不是无界搜索：

```text
current hidden-state snapshot
→ predict one block size from a bounded local set
→ draft that many provisional tokens
→ target exact verification
→ commit accepted prefix / rollback suffix
```

这里 predictor 只拥有 proposal budget，不拥有 correctness。Target 的 verification、sampling policy 和 rollback
语义保持不变；因此 controller 预测错时应退化为额外 draft/verify work，而不能静默改变输出分布。相应 identity
至少绑定 target/drafter revision、hidden-state interface、candidate set、sampling contract 与 runtime profile。

输入自适应获得更细的 acceptance/cost 匹配，却新增离线 label search、controller training、distribution drift 和
batch fragmentation。BlockPilot v1 的受限实验还显示 label construction 会随模型和候选数增长；它没有证明
controller 可跨硬件、并发或 SLO 直接迁移。若 acceptance 差异小、label 成本高或 scheduler 已能用更便宜的
online statistic 调整 depth，全局固定或 runtime-level policy 仍更合理。

两级 draft/full verification 也不是唯一 ownership 结构。当中等置信候选很多时，把所有 rejection
直接升级到完整 target 会浪费算力；可以在两者之间插入共享 embedding/output head 的 routed slim
verifier：drafter 提案后，中间层分别选择接受、局部重写或升级到 full verifier，最早重写位置拥有
rollback boundary，其后的 speculative suffix 全部失效。控制流由 binary fallback 演进为：

```text
draft proposal
→ intermediate verifier: accept / rewrite / escalate
→ full verifier for unresolved suffix
→ commit one verified prefix / rollback the rest
```

层级越深不代表越快。每一层都新增 model/KV state、threshold calibration、offline mask search、batch
fragmentation 与 rollback coordination；更多层在作者受限实验中反而可能因 routing cost 变慢。传统两级
方案在 drafter acceptance 已高、输出短或 backend 无法高效承载 routed submodel 时仍更简单。VIA-SD
只为其模型、任务与 threshold contract 提供实验性证据，不证明生产多租户与 tail SLO。

### Verification 可以稀疏化，但 Exactness 不能稀疏化

逐 token 验证最直接且易证明；长 draft block 下，先定位可能分歧的位置再集中 target compute 可减少验证工作，但 acceptance owner 仍须覆盖所有概率质量并保留 exact commit boundary。收益是降低 verify cost，代价是索引/稀疏 kernel 开销和漏检风险；无法证明等价时回退 dense verification。<!-- source-family:SF-2026-ARXIV-2605-19893 --> exact-v1 §3–5 支持论文的 sparse verification，§6 不证明任意模型或硬件都更快。

## Drafter 的演进：从辅助模型到受治理的 Serving Artifact

Draft path 也可以从 autoregressive model 演进为并行 refinement model。Diffusion/block draft 能一次提出多个 provisional tokens，减少 draft critical path；若再注入 target hidden features，可提高候选与目标分布的匹配。它没有改变 correctness owner：target 仍必须执行 exact verification，拒绝后只提交已验证 prefix。

```text
target feature snapshot
→ parallel block proposal
→ target exact verify
→ commit accepted prefix / rollback remainder
```

这条路线新增 target-feature interface、block denoising schedule、feature/cache compatibility 与专用 runtime；draft 更快也可能因接受率、verification batch 或并发机会成本而得不偿失。Autoregressive drafter 在实现成熟、target coupling 低或短 draft 足够时继续成立。

Hybrid backbone 的 self-speculation 还取决于 **component composition topology**，不能从“模型包含 local attention、SSM 或 recurrent block”直接推出某一层可以成为 drafter。可用的 proposal path 必须保留目标函数所需的信息流，并为被跳过组件定义可重放的 provisional state；target 拒绝候选时，KV、recurrent state、SSM state 与 token frontier 要回到同一 commit point。

```text
component graph + committed state frontier
→ choose one topology-valid proposal subpath
→ produce tokens and provisional component states
→ target verifies under the full path
→ atomically commit all states or roll back all states
```

较短 subpath 以更低 draft cost 换 representation gap、跨组件 state conversion 和更复杂 rollback。组件顺序改变、state interface 不稳定或 acceptance 不能覆盖转换成本时，独立 AR drafter 或不做 speculation 更合理；component presence 只用于发现候选，不是 admission evidence。

<!-- source-family:SF-COMPONENT-AWARE-SELF-SPECULATION -->

并行 draft 还要分别解决两个容易混淆的问题。第一是 **architecture dependency**：完全独立的 block proposals
延迟低，却忽略 block 内因果关系；轻量 causal encoder 或低秩 correction 可以在不恢复完整逐 token critical path
的前提下修正后续候选。第二是 **training distribution**：若 drafter 只在 target/SFT prefixes 上学习，部署时却连续
消费自己的错误 proposal，就会遇到 exposure mismatch；target-assisted rollout 与 verification-error replay 可以
把被拒状态重新纳入训练。

### Attention 转换必须保持 Draft Function，而不只是压缩 KV

把已有 MHA/GQA checkpoint 转换成 MLA，可以缩小 draft model 的 cache；若只优化 weight reconstruction、低秩误差或 standalone perplexity，转换后的模型仍可能作为普通生成器工作，却因 proposal ranking 与 target 偏离而显著降低 speculative acceptance。这里约束已经改变：draft 的成功标准不是独立生成质量，而是单位 draft/verify 成本下的 target agreement。

因此转换可以增加一个 training-time-only 的 functional reconstruction 阶段：冻结原 attention block，以真实 calibration hidden states 为输入，优化转换后模块的 query/KV projections，使其在 output projection 之后逼近原模块响应；随后再用 target acceptance 和端到端 output-token throughput 验证，而不是只看重建误差。

```text
MHA/GQA checkpoint
→ MLA structural conversion
→ reconstruct post-projection attention function
→ measure draft-target acceptance under exact verifier
→ deploy unchanged MLA cache and inference graph
```

这个机制保持 target 为唯一 correctness owner，也不需要读取 verifier logits 作为训练监督；代价是额外 calibration data、转换训练、artifact lineage 和 backend-specific 验证。功能逼近并不保证所有任务都改善，draft size、converter、backend 与模型 family 仍会交互。若 drafter 不需要架构转换、转换后的 acceptance 已足够，或维护额外训练 artifact 的成本高于 cache 收益，原始 draft model 继续成立。

```text
parallel proposal backbone
→ cheap intra-block causal correction
→ drafter-owned rollout states
→ target verification-error replay
→ exact target commit
```

两条改进可以组合，却不互相证明：架构修正不能自动解决 on-policy drift，on-policy data 也不能保证 runtime
kernel 更快。Domino 与 Draft-OPD 分别为这两条分支提供受限实验；其结果绑定作者的 Qwen、A100、Transformers/
SGLang、低并发和训练合同，不能外推为通用倍数。经典独立 AR drafter 在实现简单、数据有限或可独立升级时仍合理。

当 drafter 与 verifier 为了独立扩缩容、异构并行或 failure isolation 被拆成不同进程，原本同进程隐含的
committed prefix、future branch 和 rollback state 必须升级成协议。Verifier 应是唯一 commit/client-stream owner，
Drafter 只能发布带 base-version 的 provisional buffer：

```text
verifier committed length / epoch
→ drafter builds versioned future-token buffer
→ verifier accepts only matching buffer
→ commit accepted prefix or fall back to one-token verify
→ close / cancel / retry idempotently
```

One-round-ahead enumeration 可以移除 per-token host reconciliation，却增加 speculative compute、buffer memory、
fanout、staleness、late message 与 liveness state。Colocated path 在单机和低隔离需求下更简单；response-based
协调在吞吐压力低、协议可读性优先时仍可用。SGLang issue #27462 只证明 current roadmap 的 ownership 与
fallback design，尚未完成的 checklist、无 benchmark/SLO 和持续修订意味着它不是事件日实现或 production guarantee。

### 从 Lexical Reuse 到 Verifier-state Semantic Retrieval

训练独立 drafter 能覆盖语义变化，却增加训练、部署和兼容生命周期；suffix/table drafter 无训练成本，
但通常只能复用 lexical overlap。介于两者之间的分支，是复用 verifier 已产生的 hidden state 作为 semantic key，
从跨请求 store 取回 draft candidates，再与 suffix 或 rejected-branch candidates 合并成 verification tree：

```text
verifier-owned hidden key
→ tenant- and revision-scoped retrieval store
→ semantic + lexical candidate merge
→ target verification tree
→ verifier commits exact prefix or rejects branch
```

Correctness owner 没有改变：retrieval 只提案，target verifier 逐 token 决定 commit。代价是大 key、index/eviction、
tenant privacy、store drift、retrieval latency 与 cross-request poisoning；batch 增大后 verification capacity 还可能
抵消单请求收益。Oilbird 的 greedy、指定 Llama/Qwen 与 batch sensitivity 实验只说明该分支可行，不证明高并发
production goodput。独立 drafter 在接受率稳定时更通用，lexical drafter 在低成本与隔离优先时仍更简单。

Classical speculative sampling 把 drafter 看作一个独立小模型。它语义清晰、可替换，却可能
因为与 target 的分布差距而很快拒绝。后续演进没有取消 verification contract，而是在不断
提高“便宜候选与 target 一致”的能力：

```text
independent small LM
→ EAGLE: reuse target top-layer features, feature-level autoregression
→ EAGLE-2: context-aware dynamic draft tree
→ EAGLE-3: direct token prediction + multi-layer feature fusion + training-time test
→ model-native MTP head
→ SpecForge training pipeline
→ versioned draft checkpoint / SpecBundle
```

EAGLE 利用 target hidden features 降低近似难度，但 feature regression 也限制了 draft model
随数据扩展。EAGLE-3 去掉 feature prediction loss，融合 target 的低、中、高层 features，并在
训练时把 drafter 自己的多步输出重新喂回模型，以暴露 inference 时的 error accumulation。
这解决了 train/inference input mismatch，却让 drafter 更依赖 target architecture、selected
layers、LM head、tokenizer 和训练数据分布。

MTP 把候选预测头放进目标模型训练或 checkpoint，省去寻找另一套小模型并提高架构一致性；
旧的独立 drafter 仍适合没有原生 MTP head、需要独立更新或跨 runtime 复用的 target。两者都
必须由 full target verification 决定 accepted prefix，不能因为 drafter “来自 target”就绕过
sampling correctness。

候选来源还可以更轻：不训练独立 drafter，也不新增原生 MTP head，而是从 target model 的 hidden
state 在 embedding space 探测未来 token，再交给 target exact verification。它把 proposal-source
演进补成三条并列分支：

```text
independent draft checkpoint
| target-coupled learned MTP head
| training-free latent / embedding probe
→ exact target verification
```

Training-free 不等于 free：tree construction、nearest-token search、额外 hidden-state access 和较低
acceptance 都可能抵消收益；公开实现、TP、并发与 stochastic sampling 语义若未验证，就只能保持
Experimental。独立 drafter 在 artifact 可治理和接受率更高时继续合理；原生 MTP 在训练链可控制时更
紧密；latent probe 适合不能重训 target、又能接受受限候选质量的场景。

当 EAGLE-3 进入工程系统，问题继续从算法迁移到 artifact lifecycle。SpecForge 的 online
mode 在训练时运行 target、减少磁盘但需要更多 GPU；offline mode 预先物化 hidden states，
降低同时驻留的算力需求，却增加 TB 级数据、target-version coupling 与再生成成本。SpecBundle
进一步把 draft weights 发布成面向特定 target 的版本化产物。这条演进的长期结论是：

```text
draft artifact identity
= target revision + tokenizer/template + feature contract
+ training data/generator + draft architecture + verification runtime
```

Target weights、chat template、domain mix 或 runtime kernel 改变后，acceptance length 可能
漂移而 correctness tests 仍通过。平台因此要同时做 compatibility gate、acceptance/SLO
canary、rollback 和 provenance。作者报告的 speedup 只在其模型、数据、硬件、batch 和
参数条件内成立；不能把某个 draft bundle 当成可跨 target 通用的加速插件。

### 一个 Target 可以对应多个 Workload-specific Proposal Artifacts

#### 同一 AR Backbone 也可以承担 Masked Multi-token Proposal

独立 drafter 与 auxiliary MTP head 都不是唯一分支。若训练时保持 causal attention 和 clean AR loss，同时让同一
backbone 在额外 masked positions 上产生多 token candidates，runtime 可以省去第二模型/head artifact；但 proposal
仍不等于 exact acceptance：confidence threshold、left-to-right commit、target distribution 和 block KV lifecycle
必须共同定义。

```text
AR state
→ masked multi-position proposal from same backbone
→ confidence / acceptance policy
→ ordered commit + block KV update
```

训练序列/compute 增加，proposal signal 可能随 block size 衰减；低 threshold 会改变输出分布，block batching 又会
让快请求等待最慢请求。独立 drafter 在 target 不可重训、可独立伸缩或 workload specialization 明确时仍合理；
single-token AR 保留最简单 exactness。MARS 的证据仅覆盖其训练与 one-token benchmark contract，不是严格
lossless speculative decoding 的证明。

单一 generic drafter 的 residency、缓存和回滚最简单；当 chat、math 或 code 的 proposal distribution 明显
不同后，只有 target/tokenizer compatible 仍不足以保证高 acceptance。可以训练多个 domain specialists，
再选择三种组合分支：离线混合数据训练一个 drafter、对 aligned weights 做受验证的 merge，或在运行时让
多个 drafter 从同一 prefix 产生候选 tree，再执行 confidence selection / merged-tree verification。

Merged tree 要保持每个 subtree 的 ancestor mask、depth position 与 token identity，并屏蔽 cross-subtree
attention；最终仍由 target exact verification 和 KV commit boundary 决定输出。它保护 sampling semantics，
不保护 goodput：多份 weights、双 tree generation、更大的 verify shape、router calibration、batch
fragmentation 和 cache rollback 都是新增成本。流量同质、显存紧或 SLO 稳定性优先时，generic/mixed drafter
仍更合理；未经 matched cost 的 acceptance length 不能当作端到端加速。

多 proposal artifact 还会把 verify depth 从单请求超参数变成 batch-level shared budget。Scheduler 需要结合
request confidence、expected accepted work、在线负载与硬件 cost profile，在一批请求之间分配验证深度；
target model 仍执行 exact acceptance。这个分支用更高潜在吞吐换来 artifact multiplication、routing drift、
难请求饥饿与 fairness 风险。Homogeneous workload 或强公平 SLO 下，固定 drafter 与固定验证预算仍可能更稳定。

### Edge / Cloud 分离：Draft 复用把 Verify Depth 变成网络控制问题

<!-- semantic-body-binding:SF-PIPESD-AN-EFFICIENT-CLOUD-EDGE-COLLABORATIVE-PIPELINE-INFERENCE-FRAMEWOR:start -->
Edge drafter 与 cloud target 若严格串行，会把网络 RTT 加到每个 verify cycle。Pipeline 可以让下一段 draft 与上一段 cloud verification 重叠，但每个 proposal 必须携带 prefix/target revision、sequence number 和 rollback frontier，网络乱序或拒绝时只提交连续已验证前缀。收益是隐藏 RTT，代价是 speculative state、带宽浪费和断连恢复；网络稳定、设备足够或隐私不允许上传时，本地 target/普通 speculative 仍更简单。作者结果只属于其 edge/cloud 拓扑与 workload。
<!-- semantic-body-binding:SF-PIPESD-AN-EFFICIENT-CLOUD-EDGE-COLLABORATIVE-PIPELINE-INFERENCE-FRAMEWOR:end -->

当 drafter 位于 edge、target 位于 cloud，独立小模型方案仍然最直接：target 稳定、网络良好且 edge
容量足够时，它拥有清晰的 artifact identity。困难出现在 target 持续 fine-tune，而 edge 不能随每个版本
同步新 draft；此时可以冻结一份与 target family 共享的 anchor，让 drafter 跨多个受约束 target revisions
复用，再由在线 controller 选择本轮提出多少 tokens：

```text
target-family compatibility
+ observed prefix acceptance
+ edge draft latency
+ uplink/downlink condition
+ cloud verification profile
→ verify depth K or direct-cloud fallback
```

这里 `K` 不再只是 model confidence 的函数。提得太少，无法摊薄 network round trip；提得太多，低存活
suffix 会占用带宽和 target batch，并在 mismatch 后产生 rollback traffic。Controller 因而拥有一份随 channel、
acceptance 与 cloud load 变化的 policy state；需要 calibration version、hysteresis、safe fallback 与 per-request
KV commit boundary。Tokenizer、architecture 或 target behavior 越过 anchor 的兼容域时，继续复用旧 draft
不是 graceful degradation，而是 artifact mismatch。

FlexSpec 在受限 edge/cloud 设备、模型与部分模拟网络条件下展示了这条设计分支，但没有覆盖真实蜂窝 tail、
multi-tenant cloud 或任意 target drift。正文吸收的是“artifact reuse + network-aware verify control”的机制，
不是其作者 speedup。低 acceptance、低带宽或 target 跨 family 变化时，直接 cloud decoding；target 稳定且
同机时，经典 speculative decoding 仍更简单。

### Hybrid Recurrent State 不能只移动 KV Pointer 回滚

纯 Attention runtime 的 speculative branch 通常把候选 K/V 写入临时 slots；拒绝 suffix 后，移动
`cached length`、回收对应 blocks，再提交 accepted prefix。这种做法成立，是因为 KV Cache 是按 token
追加、可以按位置截断的 exact state。Hybrid attention/recurrent model 还包含另一类状态：例如 gated
linear recurrence 已把整段 suffix 压入一个 lossy matrix state。它不是 token 列表，推进到候选末端后无法
靠缩短一个 pointer 恢复到任意 accepted boundary。

最直接的旧方案是为 tree 中每个候选节点保存完整 recurrent-state snapshot。它正确、易审计，在 tree 很小或
state 很小时仍合理；但 snapshot 数量随候选节点增长，兄弟分支也不能像 KV blocks 那样自然共享。另一条分支
是延迟 recurrent update，等 target 确认后再串行重算 accepted tokens；它节省临时状态，却会重新引入本来想
消除的串行路径。

Tree-structured WY update 展示了一个中间设计：先把 branch-local gated updates 保持成可组合的 compact
representation，用 tree dependency 和 triangular solve 并行完成 target verification，只在 accepted path
确定后重建其 recurrent state：

```text
committed recurrent state
+ branch-local gated deltas over a draft tree
→ algebra-aware parallel verification
→ reconstruct accepted-path recurrent state
→ atomic commit with KV / output frontier
```

关键不是某个 kernel 名称，而是 **rollback protocol 必须理解 state algebra**。Verifier 仍是唯一 commit owner；
KV blocks、recurrent state、accepted length 与 streamed output 必须跨过同一个 frontier。否则 token 已被拒绝，
recurrent state 却可能已经吸收它，后续输出就从不可见的错误历史继续。

这条证据目前只覆盖论文给出的 Qwen3.5 hybrid variants、matched correctness points 和相应硬件/shape；作者报告的
收益主要出现在 recurrent-state memory pressure 占主导的区域，非 memory-bound 区域可能付出额外开销。更宽的
draft tree 也不自动等于更高 goodput，因为 verify shape、acceptance、batch interaction 与 state reconstruction
仍共同决定成本。小 tree、低并发或状态很小的系统继续使用 snapshot；短 chain 且 target verification 已是瓶颈时，
deferred update 也可能更简单。

### Agent Workflow 让 Proposal Budget 与 Residual State 都变成动态对象

经典 speculative decoding 假定 token stream 结构近似稳定，可以用统一 draft budget 提出连续候选。Agent workload 会在 reasoning、tool schema、JSON/action 与 observation 等语义块之间切换；重复模式和可接受长度随阶段变化，固定 budget 容易在结构边界产生低接受率，也会让一批异质 Agent 请求互相拖累。

一种演进分支是由 Agent runtime 暴露非权限性的 block hint，serving scheduler 仍拥有 proposal budget：

```text
workflow phase / semantic block hint
→ isolate drafting context by block
→ allocate draft budget from observed redundancy
→ target verifies under the original sampling contract
→ commit accepted tokens or rollback temporary state
```

hint 只改变 proposal policy，不能改变 target authority；缺少显式 metadata 时应退化到普通 speculation。它用 Agent–serving interface、per-block statistics 与更多调度状态换取潜在接受率，结构少、batch 小或 workload 漂移大时，统一 drafter 仍更简单。

### 从 Token Draft 到 Read-only Tool Speculation

Token-level speculative decoding 只提前产生候选 token，外部工具仍在完整 action 生成后启动。对长 reasoning
与慢 read tool 的 Agent turn，可以增加一层 action speculation：main stream 产生首 token 后复用同一 prefix
KV fork 当前模型，以 forced tool-call prefix 探测下一 action；只有 probe confidence 达到门限才并发执行被
manifest 标为 read-only 的工具。Main stream 完成后，最终 tool name 与 canonical arguments 完全匹配，
precomputed observation 才能进入会话；不匹配则丢弃结果并走 serial fallback。被拒 probe 的已验证 token
prefix 可以继续作为普通 speculative draft，但仍由 target verification 决定提交。

这里存在两个不同 frontier：tool execution 可以提前，conversation/effect commit 不能交给 probe。Exact
action match 只保护会话采用哪个结果，不会撤销已经消耗的查询、quota、隐私暴露或远端可见副作用，也不能让
非确定网络结果与稍后 serial call 相同。因此 write/non-idempotent tools 继续串行，除非另有 sandbox、
checkpoint、transaction 或 compensation。收益只在剩余 decode/tool latency 覆盖 probe overhead、tool
schema 稳定、prefix cache/logprobs 可用且 serving 有 spare capacity 时成立；短工具、no-think、格式漂移或
heavy batching 下，serial execution 更合理。

Proposal artifact 也不一定是独立小模型。目标 Agent 可以在 partial trajectory 上切换到受限 speculator mode，
复用 prefix KV，并用自身 rollout 产生下一次 tool call 的训练目标。这减少 draft/target 行为漂移，却让
speculator quality 与 Agent policy revision 更紧密耦合。无论预测命中率多高，它仍只拥有 proposal 权限：
canonical Agent 输出匹配后才能提交副作用；不可逆工具最多预取输入，或在隔离且可丢弃的事务里执行。

多候选验证还暴露另一个边界：一次拒绝后用于 correction 的 residual distribution 不能沿用已被候选集合消耗的概率质量。Residual shaping 可以重新分配剩余质量并在证明条件下保持 target distribution，但增加 shaping loss、numerical path、candidate interaction 与验证成本。它与 workflow-aware drafting 是正交分支：前者修正拒绝后的采样语义，后者改善候选生成；两者都必须以 empirical distribution test 验证 exactness，不能用吞吐提升代替分布契约。

### Asynchronous Drafting 需要有界 Staleness 与可取消 Proposal

同步 drafter 让状态最清楚；target 与 drafter 速度失配时，异步生成可隐藏等待，但 proposal 必须绑定 prefix/version、允许取消，并在 commit 前重新验证。收益是提高 overlap，代价是浪费 draft、队列状态和 stale proposal；低并发或 acceptance 低时同步路径更稳。<!-- source-family:SF-2026-ARXIV-2605-20022 --> exact-v1 §3–5 只证明其 flexible async 设计，§6 不保证所有 workload 的尾延迟收益。

## 什么时候有效

### Edge 场景先管理 Draft Residency，再谈 Acceptance

多个 draft model 理论上可以按阶段选择最佳 proposal，但 edge device 的主要代价可能是把 draft 从存储搬进内存。把“哪个 draft 可能有效”和“哪个 draft 当前 resident”分离后，scheduler 可以根据预测维护一个有界 working set，并把加载与 target execution 重叠：

```text
phase signal → draft-effect prediction
→ memory-feasible resident set
→ prefetch / evict
→ propose, verify and update prediction
```

它用 predictor、驻留抖动和预取带宽换更少 reactive load。Draft pool 小、内存足够或预测不稳定时，固定单 draft 更简单；切换成本必须计入 acceptance gain，不能只比较被接受 token 数。

#### MoE verification 还要结算 target-expert expansion

Edge MoE 的 speculative cost 不能只看 draft acceptance。若 target experts 从 CPU 或 Flash 按需搬运，多 token block 的 verification 会激活各 token expert 的 union；更长 proposal 可能减少 target steps，却触发更多 weight loading。一个受限分支使用固定驻留的 draft expert 产生候选，再由 confidence 与预计 expert expansion 共同截断 block，并预取 target experts；最终 token 与 KV 仍只由 target verification 提交。

它用额外 draft training、router-agreement state 和误预取带宽换更少 reactive load。模型已全驻留、batch 足以摊销 loading、预测漂移或 draft artifact 不可治理时，普通 target-only offload 或现有 speculative path 仍更简单。Acceptance、expert union、residency 与 transfer 必须进入同一个 workload contract，不能用接受率代替端到端 latency。

Speculative Decoding 的收益取决于几个条件。

第一，draft model 必须足够便宜。如果小模型生成候选的成本太高，就抵消了大模型少跑几次的收益。

第二，draft model 必须足够准。如果候选 token 很快被拒绝，大模型每次只接受一两个 token，收益有限。

第三，target model 的验证必须能高效并行。如果验证阶段本身开销很大，或者 batch / kernel / memory 状态让验证效率下降，收益也会变小。

第四，系统调度必须支持它。Speculative Decoding 改变了 Decode 的 token 产出形态：一个请求一次可能接受多个 token，也可能回退。这会影响 KV Cache 追加、batch scheduling、streaming 输出和 latency 统计。

## Trade-off

### Acceptance 不是独立常数，在线决策必须结算系统状态

固定 proposal 长度在负载稳定、draft/target 成本可预测时最容易实现；进入共享 serving runtime 后，同一请求的收益会随队列、形成中的 batch、draft 与 verification 成本以及 acceptance 分布一起变化。在线策略因此应比较“继续串行 target decode”与“本轮 proposal + verify”的条件期望，而不是只追逐接受率：

```text
request state + live load + emergent batch
+ draft / verify cost + acceptance estimate
→ speculate | shorten | bypass
→ observe latency and accepted boundary
```

这把 speculation 从静态模型属性提升为 runtime policy，却引入估计误差、控制开销和策略抖动。负载较小、draft 极便宜或估计器尚未校准时，固定长度乃至关闭 speculation 仍是更可预测的基线；评估必须同时报告端到端 latency、goodput、拒绝回滚和额外算力，而不能用 acceptance 单独替代系统收益。

<!-- source-family:SF-2026-ARXIV-2605-15051 -->

Speculative Decoding 的核心 trade-off 是：用额外的 draft computation 换取更少的 target model serial steps。

它适合 target model 很贵、draft model 很便宜、候选命中率高的场景。它不适合所有 workload。如果 prompt 分布复杂、draft model 和 target model 行为差异大，拒绝率高，收益会下降。

它也可能增加系统复杂度。服务端需要管理两个模型或一个带多 token prediction 能力的模型，需要处理候选 token 的 KV 状态，需要在验证后决定哪些 cache 可以保留、哪些需要回退。

此外，它和 batching 并不是天然独立的优化。一次请求接受多个 token，另一次请求只接受一个 token，会进一步增加 batch 内 token 进度差异。调度器需要能处理这种不均匀推进。

KV state 也必须事务化处理。Runtime 可以先把候选 K/V 写入临时 slots，验证后只提交 accepted prefix；也可以写入预留 blocks，再回滚被拒绝的 suffix。无论实现如何，block table、cached length 和 streamed tokens 必须在同一 accepted boundary 上一致。

### Flash-resident Target 改写 Draft/Verify 成本模型

模型都驻留 DRAM/GPU memory 时，speculation 主要比较 draft compute 与 target verification；在手机等受限设备上，大 target 可能每轮都从 flash 流式读取权重，而小 draft 常驻 DRAM。此时多 token verification 的主要收益是摊薄 target weight IO，state placement 本身进入决策。

它用 draft memory、候选回滚和额外控制换更少 target loading；acceptance 低、flash bandwidth 足够、target 已驻留或 thermal/power 约束改变时，普通 decode 仍可能更快。手机实验必须绑定设备、模型、量化、长度、温控和 batch，不能把 flash-backed 收益外推到 server GPU。

<!-- source-family:SF-2026-ARXIV-2605-16786 -->

## 和其他加速方法的关系

Speculative Decoding 解决的是 Decode 串行性问题。

它和 KV Cache 不冲突。KV Cache 仍然用于保存历史 K/V，只是 speculative verification 会让 cache 的追加和回退更复杂。

它和 Continuous Batching 也不冲突，但会让调度更复杂。不同请求在一次 iteration 中可能产出不同数量的 token。

它和量化、图优化、FlashAttention 属于不同层次。量化降低单次计算和带宽成本，图优化降低 kernel / memory overhead，Speculative Decoding 试图减少昂贵 target model serial step 的数量。

### Semantic Draft 仍需要唯一 Commit Boundary

Token-exact speculative decoding 的验证边界清楚：目标模型接受多少 token，就提交多少 token。语义 draft 可以一次提出多个 prefix 并并行验证，扩大 proposal 空间，却不能把“意思相近”直接当作可提交状态；runtime 仍需选择一个 maximal valid prefix，明确 reject、rollback 和 residual state。收益是降低串行验证深度，代价是 verifier 成本、语义误判和更复杂的缓存回滚；不能证明 verifier 与目标分布兼容时，应回退 token-exact 路径。[受限证据：arXiv:2605.04263v1]

<!-- source-family:SF-2026-ARXIV-2605-04263 -->

### Edge–Cloud Draft Length 是通信条件下的 Optimal Stopping

在本地 draft、云端 target 的路径中，固定候选长度容易实现，但网络 RTT/带宽、acceptance 与本地 compute 会共同改变“再生成一个 draft token”是否值得。Controller 可在每步比较预期接受收益与新增本地计算/上行/等待成本，选择发送或继续。

在线停止减少部分通信空洞，却依赖网络和 acceptance 估计，误差会造成过长 draft 或频繁小请求。网络稳定、估计器未校准或高 tail-risk 时，固定短 draft 是更可预测的 fallback；评估必须绑定设备、链路、模型、长度与 SLO。

<!-- source-family:SF-2026-ARXIV-2606-20591 -->

## 本章在知识树中的位置

```text
Decode
→ 自回归串行瓶颈
→ Speculative Decoding
→ KV Cache 状态管理
→ 推理调度
```

它是 Part V 中少数直接挑战 Decode 串行性的技术之一。

### Context Asymmetry 是质量—成本分支，不是免费 Exactness

经典 speculation 让小 drafter 提议、完整 target verifier 读取同一条件并执行 exact acceptance。长 Agent context
使 verifier 成本占主导后，可以让 drafter 保留完整输入，而让 verifier 只读取压缩条件，再用少量融合或
divergence signal 调节接受：

```text
full context → drafter proposal
compressed context → verifier score
fusion / divergence gate → accept, correct or fallback
```

因此该路线属于 bounded quality–latency alternative，不能沿用经典 speculative decoding 的 target-distribution
exactness 结论。压缩器、融合参数与 divergence threshold 都成为版本化 artifact；低置信、Context 冲突或
高风险请求必须回到 full-context verifier。完整 Context 仍是正确性基线；只有 matched quality、batch、长度、
硬件与 SLO 证明节省覆盖压缩和 fallback 成本时，asymmetric verifier 才成立。

## 从机制演进到系统设计

经典 speculative decoding 以共享条件和 exact acceptance 保持 target distribution；当 verifier、网络或长 Context 成本上升后，分支扩展到 response-level cascade、稀疏 target attention、edge-cloud offload 和 asymmetric context。此时 proposal、verification 与 commit 的接口仍相同，但不一定继续拥有 exactness。

降低 verifier 成本可以增加 accepted progress，却引入 router error、稀疏读取遗漏、WAN RTT、Context mismatch 和新的质量阈值。只有 target-aligned matched arm 能区分算法差异与 dtype/framework 噪声；低 acceptance、schema-critical request 或 invariance screen 失败时，应回到 dense target 或普通 autoregressive decode。

## 自检问题

1. Speculative Decoding 为什么需要 draft model 和 target model？
2. 为什么生成是串行的，但验证候选 token 可以并行？
3. 为什么它不是简单的小模型替代？
4. acceptance rate 对加速效果有什么影响？
5. `min(1,p/q)` 与 residual sampling 怎样保持 target distribution？
6. 为什么 acceptance rate 高仍不保证端到端加速？
7. Speculative Decoding 会给 KV Cache 和 batching 带来哪些额外复杂度？
8. 为什么 lossy verification 不能只被描述为 runtime optimization？
9. 含 truncation policy 的 verification 为什么必须使用 matched-policy baseline？
10. 为什么 draft checkpoint 必须与 target revision、tokenizer 和 runtime 一起版本化？
11. Edge/cloud speculation 中，为什么 verify depth 必须同时看到网络状态与 target capacity？
12. 为什么 hybrid attention/recurrent model 的 speculative rollback 不能只移动 KV cached-length pointer？

## 小结

Speculative Decoding 没有取消 autoregressive semantics，而是让便宜的 drafter 先提供已知候选，使 target model 能并行验证多个 positions。Exact acceptance 保护输出分布，系统收益则取决于 accepted progress 是否覆盖额外 draft、verification 和状态管理成本。放宽 verification 可以改变速度—质量 operating point，但那是新的 sampling contract，不再是语义透明的纯执行优化。

至此第46～48章分别从 batch membership、KV placement 和 serial target steps 三个正交方向优化 runtime。下一章开始把这些机制映射到实际 Serving stacks。

## Review notes

- Block Drafting Information Floor（realized-prefix information 与 model gap 分解；Status: Experimental）：
  https://arxiv.org/abs/2608.27339v1
  - 证据边界：论文给出特定 target/domain/draft interface 下的分析与实验；information floor 不构成跨模型接受率
    常数，单 token probe 也不等于端到端更快。

- AsymSpec（full-context drafter + compressed-context verifier；Status: Experimental）：
  https://arxiv.org/abs/2608.26004v1
  - 证据边界：论文结果绑定所披露的 Qwen3-32B、vLLM、任务与确定性设置；该路线改变 verifier
    条件，不能被描述为经典 exact speculative decoding 的无损替代。

- DraftExpert（MoE target-expert expansion-aware drafting 与 prefetch；Status: Experimental）：https://arxiv.org/html/2607.24434v1

- Functional Reconstruction for MLA Draft Models（转换后的 draft 以 target acceptance 对齐功能，而不只做 KV/weight reconstruction；Status: Experimental）:
  https://arxiv.org/abs/2607.27269v1

- MemSpec（edge draft residency 与 adaptive scheduling；Status: Experimental）: https://arxiv.org/abs/2608.10362

- SGLang parallel speculative decoding roadmap（revision-sensitive design evidence）:
  https://github.com/sgl-project/sglang/issues/27462

- Domino（parallel proposal 的 causal correction；Status: Experimental）: https://arxiv.org/abs/2605.29707
- DARTree（depth-wise causal correction + deferred tree pruning；No Change / Experimental evidence）:
  https://arxiv.org/abs/2608.13524
- Draft-OPD（drafter on-policy distribution；Status: Experimental）: https://arxiv.org/abs/2605.29343

- MARS（same-backbone masked multi-token proposal；Status: Experimental）: https://arxiv.org/abs/2604.07023

Primary-source 校验入口：

- Fast Inference from Transformers via Speculative Decoding: https://arxiv.org/abs/2211.17192
- Accelerating Large Language Model Decoding with Speculative Sampling: https://arxiv.org/abs/2302.01318
- Revisiting Lossy Verification in Speculative Decoding:
  https://arxiv.org/abs/2607.26627
- DSpark: Dynamically Optimized Speculative Parallel Drafting for LLM Inference: https://arxiv.org/abs/2607.05147v1
- SPORK（read-only action speculation；Status: Experimental；write/non-idempotent tools 不在证据边界内）: https://arxiv.org/abs/2607.03333v1
- EAGLE-3: https://arxiv.org/abs/2503.01840
- SGLang Multiple Token Prediction: https://www.lmsys.org/blog/2025-07-17-mtp/
- SpecForge: https://www.lmsys.org/blog/2025-07-25-spec-forge/
- SpecBundle / SpecForge v0.2: https://www.lmsys.org/blog/2025-12-23-spec-bundle-phase-1/
- FlexSpec（Status: Experimental；edge/cloud reusable draft 与 network-aware verify control）:
  https://arxiv.org/abs/2601.00644
- TreeWY（GDN accepted-state reconstruction；Status: Experimental）:
  https://arxiv.org/abs/2608.20961
- DFlash（target-conditioned diffusion drafter + exact verification；Status: Experimental）: https://arxiv.org/abs/2602.06036
- LK Losses（acceptance-aligned drafter objective；Status: Experimental）:
  https://arxiv.org/abs/2602.23881
- Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing（Status: Experimental）:
  https://arxiv.org/abs/2603.17942
- TAPS（Status: Experimental；workload-specific proposal artifacts 与 lossless tree composition）:
  https://arxiv.org/abs/2603.27027
- VIA-SD（Status: Experimental；routed intermediate verifier ownership）:
  https://arxiv.org/abs/2606.12243
- Bebop / MTP with Rejection Sampling（Status: Experimental；distribution-aligned MTP proposal）:
  https://arxiv.org/abs/2606.12370
- Self-speculative tool prediction（dual-mode Agent、shared prefix state；Status: Experimental）:
  https://arxiv.org/abs/2607.25816v1
- AngelSpec（workload-specific proposal artifacts 与 batch-level verification budget；Status: Experimental）:
  https://arxiv.org/abs/2607.25852v1

本轮 Review 补充了 greedy verification、distribution-preserving sampling 与 lossy
verification 的边界，并补入 EAGLE-3→MTP→SpecForge→SpecBundle 的 artifact evolution。
候选生成机制、verification contract 与 runtime scheduling 仍保持分层；2026 论文的 taxonomy、
动态 verify policy 与 benchmark 保持 `Status: Experimental`，只用于验证 matched-policy
baseline、capacity-aware verification 与 network-aware fallback 三项长期原则。

- Oilbird（verifier-state semantic draft retrieval；Status: Experimental）:
  https://arxiv.org/abs/2608.03839

### Daily integration evidence trace

- `2026-05-02 / SF-COMPONENT-AWARE-SELF-SPECULATION` — exact-v1 `arXiv:2605.01106v1`；正文只吸收 component topology 与多状态原子 rollback 的设计约束，不把组件存在写成可用 draft path 的充分条件。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22840` — primary `arXiv:2606.22840v1`; Method=`arXiv:2606.22840v1 — §2.2 LLM Cascade and Routing; §3 System Design; §3.1 Architecture Overview`; Evaluation=`arXiv:2606.22840v1 — §4 Evaluation; §4.6 Extended Engineering Benchmark; §4.7 Case Study: Cost Inversion on mteb-retrieve`; non-proof=`arXiv:2606.22840v1 — §6 Discussion; §6.4 Cross-Provider Failure Modes; §7 Conclusion`; fallback=该 family 的 failure pressure 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 披露的 evaluation signal 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24957: `arXiv:2606.24957v1`; exact-v1 URL=`https://arxiv.org/html/2606.24957v1`; Method=`https://arxiv.org/html/2606.24957v1 — §3 Observation; 4 Dustin Sparse Verification`; Evaluation=`https://arxiv.org/html/2606.24957v1 — §5 Experiment; Accuracy and End-to-End Decode Throughput`; Non-proof=`静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25091: `arXiv:2606.25091v1`; exact-v1 URL=`https://arxiv.org/html/2606.25091v1`; Method=`https://arxiv.org/html/2606.25091v1 — §II Background and Setting; III Gain Window`; Evaluation=`https://arxiv.org/html/2606.25091v1 — §III-A/B/C comparisons; IV Pipelining`; Non-proof=`这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25097: `arXiv:2606.25097v1`; exact-v1 URL=`https://arxiv.org/html/2606.25097v1`; Method=`https://arxiv.org/html/2606.25097v1 — §3 Methods; Serving-stack Configuration; TAIS Screen`; Evaluation=`https://arxiv.org/html/2606.25097v1 — §4 Results; E0/E1/E2/E5; B Reproducibility`; Non-proof=`证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

### Source-family integration record

<!-- recovered-daily-20260623:INFER-SPECULATIVE-DECODING:start -->
### 2026-06-23 evidence integration — INFER-SPECULATIVE-DECODING

相邻章 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22840**：RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving 的 exact-v1 机制为：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 因此 把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收。 该 family 的 failure pressure 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 披露的 evaluation signal 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:INFER-SPECULATIVE-DECODING:end -->

<!-- recovered-daily-20260624:INFER-SPECULATIVE-DECODING:start -->
### 2026-06-24 evidence integration — INFER-SPECULATIVE-DECODING

相邻章 `books/part-05-inference-system/49-tensorrt-llm.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24957**：speculative verification 的 target KV 不再全读；Dustin 混合历史 attention 与 draft lookahead，semantic retrieval heads 在线估计关键 token，只对稀疏 KV 做 target verification。 静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。
- **SF-2026-ARXIV-2606-25091**：edge-cloud speculative decoding 的准入由 RTT、edge draft time、acceptance 与 target verification time 共同决定；single-request latency 不再是唯一目标，饱和 server 的 multi-tenant capacity 才可能 justify offload。 这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。
- **SF-2026-ARXIV-2606-25097**：speculative decoding 上线前增加 target-aligned invariance screen：byte identity、McNemar、TOST 与 matched target-only arm 分离算法安全差异和 dtype/framework 噪声。 证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。

<!-- recovered-daily-20260624:INFER-SPECULATIVE-DECODING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-DFLARE-DIFFUSION-SPECULATION:start -->
- `SF-DFLARE-DIFFUSION-SPECULATION` — Daily `2026-06-02`；primary `arXiv:2606.02091v1`；Books review `books-review:SF-DFLARE-DIFFUSION-SPECULATION`。

  **已吸收的语义增量：** 增加 per-draft-layer target-feature fusion 作为扩大 draft capacity 的机制与成本。
<!-- daily-books-trace:SF-DFLARE-DIFFUSION-SPECULATION:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18967:start -->
- `SF-2026-ARXIV-2606-18967` — Daily `2026-06-18`；primary `arXiv:2606.18967v1`；Books review `books-review:SF-2026-ARXIV-2606-18967`。

  **已吸收的语义增量：** RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18967:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19755:start -->
- `SF-2026-ARXIV-2606-19755` — Daily `2026-06-19`；primary `arXiv:2606.19755v1`；Books review `books-review:SF-2026-ARXIV-2606-19755`。

  **已吸收的语义增量：** `SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling` 路由到 `INFER-SPECULATIVE-DECODING`：SafeSpec 将安全 head 并入 target verification 的同一次前向：draft token 通过语义与风险联合门，风险触发 rollback 和 safety-guided multi-sampling，而非在 speculative path 外串联 guard。target verifier 持有 accept/rollback 控制；外部 guard 仍作为未知攻击与 head 故障 fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19755:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-31315:start -->
- `SF-2026-ARXIV-2606-31315` — Daily `2026-07-01`；primary `arXiv:2606.31315v1`；Books review `books-review:SF-2026-ARXIV-2606-31315`。

  **已吸收的语义增量：** 新增证据边界：固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L215`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2606-31315:end -->

<!-- daily-books-trace:SF-2026-AGENTSPEC:start -->
- `SF-2026-AGENTSPEC` — Daily `2026-08-26`；primary `arXiv:2608.24004v1`；Books review `books-review:SF-2026-AGENTSPEC`。

  **已吸收的语义增量：** 新增 workflow block hint 与 dynamic proposal budget，并明确 target authority 和无 hint fallback。
<!-- daily-books-trace:SF-2026-AGENTSPEC:end -->

<!-- daily-books-trace:SF-2026-RESISPEC:start -->
- `SF-2026-RESISPEC` — Daily `2026-08-26`；primary `arXiv:2608.24411v1`；Books review `books-review:SF-2026-RESISPEC`。

  **已吸收的语义增量：** 新增 residual shaping 的分布契约、数值代价及与 workflow drafting 的正交关系。
<!-- daily-books-trace:SF-2026-RESISPEC:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-03333:start -->
- `SF-2026-ARXIV-2607-03333` — Daily `2026-07-04`；primary `arXiv:2607.03333v1`；Books review `books-review:SF-2026-ARXIV-2607-03333`。

  **已吸收的语义增量：** 新增证据边界：Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L510`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-03333:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24434:start -->
- `SF-2026-ARXIV-2607-24434` — Daily `2026-07-28`；primary `arXiv:2607.24434v1`；Books review `books-review:SF-2026-ARXIV-2607-24434`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: self-speculation optimized for acceptance -> include target-expert expansion/residency cost -> fixed-footprint draft expert + expansion-aware truncation -> exact target verification and token/KV commit. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L548`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24434:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25816:start -->
- `SF-2026-ARXIV-2607.25816` — Daily `2026-07-29`；primary `arXiv:2607.25816v1`；Books review `books-review:SF-2026-ARXIV-2607.25816`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: separate tool-call predictor -> same-model speculative mode -> self-rollout targets -> joint agent/speculator optimization with canonical commit. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25816:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25852:start -->
- `SF-2026-ARXIV-2607.25852` — Daily `2026-07-29`；primary `arXiv:2607.25852v1`；Books review `books-review:SF-2026-ARXIV-2607.25852`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25852:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27269:start -->
- `SF-2026-ARXIV-2607.27269` — Daily `2026-07-30`；primary `arXiv:2607.27269v1`；Books review `books-review:SF-2026-ARXIV-2607.27269`。

  **已吸收的语义增量：** 新增证据边界：Functional reconstruction trains an MLA-compatible draft path to preserve target-relevant behavior rather than merely reconstruct KV tensors. Better functional alignment can raise accepted progress, but still requires exact target verification and adds target-specific coupling. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27269:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-10362:start -->
- `SF-2026-ARXIV-2608-10362` — Daily `2026-08-12`；primary `arXiv:2608.10362v1`；Books review `books-review:SF-2026-ARXIV-2608-10362`。

  **已吸收的语义增量：** MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。
<!-- daily-books-trace:SF-2026-ARXIV-2608-10362:end -->

<!-- daily-books-trace:SF-2026-ASYMSPEC:start -->
- `SF-2026-ASYMSPEC` — Daily `2026-08-27`；primary `arXiv:2608.26004v1`；Books review `books-review:SF-2026-ASYMSPEC`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：让轻量 drafter 读 full context、large verifier 读 compressed view，以 contrastive delta-fusion 和 divergence-aware acceptance gate 传递被压缩信号；并保留边界：只在特定确定性设置验证；不是 token-exact 的普通 SD 等价保证，压缩器与 verifier drift 仍可能失效。 相邻章节对读：books/part-05-inference-system/47-pagedattention.md#L119;books/part-05-inference-system/49-tensorrt-llm.md#L735。PagedAttention 拥有 KV storage，Execution Engine 拥有 compiled runtime；draft/verify acceptance semantics 属于 Speculative Decoding。
<!-- daily-books-trace:SF-2026-ASYMSPEC:end -->

<!-- daily-books-trace:SF-2026-BLOCK-DRAFTING-FLOOR:start -->
- `SF-2026-BLOCK-DRAFTING-FLOOR` — Daily `2026-08-28`；primary `arXiv:2608.27339v1`；Books review `books-review:SF-2026-BLOCK-DRAFTING-FLOOR`。

  **已吸收的语义增量：** 补足 information floor 与 model gap 的诊断分解。
<!-- daily-books-trace:SF-2026-BLOCK-DRAFTING-FLOOR:end -->
