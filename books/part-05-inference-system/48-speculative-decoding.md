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

2026 年 DSpark 预印本用 semi-autoregressive drafter 与动态 verify length 展示了这条方向，
随后也出现 runtime integration；论文中的生产收益仍是作者在特定 DeepSeek workload 上的
实验，缺少完整 workload contract，故本章只吸收长期原则：**speculation policy 必须看到
全局 target capacity，而不能只最大化单请求 draft length。**

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

## Drafter 的演进：从辅助模型到受治理的 Serving Artifact

Draft path 也可以从 autoregressive model 演进为并行 refinement model。Diffusion/block draft 能一次提出多个 provisional tokens，减少 draft critical path；若再注入 target hidden features，可提高候选与目标分布的匹配。它没有改变 correctness owner：target 仍必须执行 exact verification，拒绝后只提交已验证 prefix。

```text
target feature snapshot
→ parallel block proposal
→ target exact verify
→ commit accepted prefix / rollback remainder
```

这条路线新增 target-feature interface、block denoising schedule、feature/cache compatibility 与专用 runtime；draft 更快也可能因接受率、verification batch 或并发机会成本而得不偿失。Autoregressive drafter 在实现成熟、target coupling 低或短 draft 足够时继续成立。

并行 draft 还要分别解决两个容易混淆的问题。第一是 **architecture dependency**：完全独立的 block proposals
延迟低，却忽略 block 内因果关系；轻量 causal encoder 或低秩 correction 可以在不恢复完整逐 token critical path
的前提下修正后续候选。第二是 **training distribution**：若 drafter 只在 target/SFT prefixes 上学习，部署时却连续
消费自己的错误 proposal，就会遇到 exposure mismatch；target-assisted rollout 与 verification-error replay 可以
把被拒状态重新纳入训练。

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

### Edge / Cloud 分离：Draft 复用把 Verify Depth 变成网络控制问题

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

## 什么时候有效

Speculative Decoding 的收益取决于几个条件。

第一，draft model 必须足够便宜。如果小模型生成候选的成本太高，就抵消了大模型少跑几次的收益。

第二，draft model 必须足够准。如果候选 token 很快被拒绝，大模型每次只接受一两个 token，收益有限。

第三，target model 的验证必须能高效并行。如果验证阶段本身开销很大，或者 batch / kernel / memory 状态让验证效率下降，收益也会变小。

第四，系统调度必须支持它。Speculative Decoding 改变了 Decode 的 token 产出形态：一个请求一次可能接受多个 token，也可能回退。这会影响 KV Cache 追加、batch scheduling、streaming 输出和 latency 统计。

## Trade-off

Speculative Decoding 的核心 trade-off 是：用额外的 draft computation 换取更少的 target model serial steps。

它适合 target model 很贵、draft model 很便宜、候选命中率高的场景。它不适合所有 workload。如果 prompt 分布复杂、draft model 和 target model 行为差异大，拒绝率高，收益会下降。

它也可能增加系统复杂度。服务端需要管理两个模型或一个带多 token prediction 能力的模型，需要处理候选 token 的 KV 状态，需要在验证后决定哪些 cache 可以保留、哪些需要回退。

此外，它和 batching 并不是天然独立的优化。一次请求接受多个 token，另一次请求只接受一个 token，会进一步增加 batch 内 token 进度差异。调度器需要能处理这种不均匀推进。

KV state 也必须事务化处理。Runtime 可以先把候选 K/V 写入临时 slots，验证后只提交 accepted prefix；也可以写入预留 blocks，再回滚被拒绝的 suffix。无论实现如何，block table、cached length 和 streamed tokens 必须在同一 accepted boundary 上一致。

## 和其他加速方法的关系

Speculative Decoding 解决的是 Decode 串行性问题。

它和 KV Cache 不冲突。KV Cache 仍然用于保存历史 K/V，只是 speculative verification 会让 cache 的追加和回退更复杂。

它和 Continuous Batching 也不冲突，但会让调度更复杂。不同请求在一次 iteration 中可能产出不同数量的 token。

它和量化、图优化、FlashAttention 属于不同层次。量化降低单次计算和带宽成本，图优化降低 kernel / memory overhead，Speculative Decoding 试图减少昂贵 target model serial step 的数量。

## 本章在知识树中的位置

```text
Decode
→ 自回归串行瓶颈
→ Speculative Decoding
→ KV Cache 状态管理
→ 推理调度
```

它是 Part V 中少数直接挑战 Decode 串行性的技术之一。

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

## 小结

Speculative Decoding 没有取消 autoregressive semantics，而是让便宜的 drafter 先提供已知候选，使 target model 能并行验证多个 positions。Exact acceptance 保护输出分布，系统收益则取决于 accepted progress 是否覆盖额外 draft、verification 和状态管理成本。放宽 verification 可以改变速度—质量 operating point，但那是新的 sampling contract，不再是语义透明的纯执行优化。

至此第46～48章分别从 batch membership、KV placement 和 serial target steps 三个正交方向优化 runtime。下一章开始把这些机制映射到实际 Serving stacks。

## Review notes

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
- DSpark: Dynamically Optimized Speculative Parallel Drafting for LLM Inference:
  https://arxiv.org/abs/2607.05147
- EAGLE-3: https://arxiv.org/abs/2503.01840
- SGLang Multiple Token Prediction: https://www.lmsys.org/blog/2025-07-17-mtp/
- SpecForge: https://www.lmsys.org/blog/2025-07-25-spec-forge/
- SpecBundle / SpecForge v0.2: https://www.lmsys.org/blog/2025-12-23-spec-bundle-phase-1/
- FlexSpec（Status: Experimental；edge/cloud reusable draft 与 network-aware verify control）:
  https://arxiv.org/abs/2601.00644
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

本轮 Review 补充了 greedy verification、distribution-preserving sampling 与 lossy
verification 的边界，并补入 EAGLE-3→MTP→SpecForge→SpecBundle 的 artifact evolution。
候选生成机制、verification contract 与 runtime scheduling 仍保持分层；2026 论文的 taxonomy、
动态 verify policy 与 benchmark 保持 `Status: Experimental`，只用于验证 matched-policy
baseline、capacity-aware verification 与 network-aware fallback 三项长期原则。

- Oilbird（verifier-state semantic draft retrieval；Status: Experimental）:
  https://arxiv.org/abs/2608.03839
