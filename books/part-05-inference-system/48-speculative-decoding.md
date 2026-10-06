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

保持 target 分布之外，带 key 的采样还需要让 drafter 只决定推进长度，不决定 watermark 可见的 token。一个条件分支按完整 context 索引共享 Poisson clocks，将同一底层过程分别映射到 target 与 draft 分布；target 的第一个 winner 始终提交，只有它也在 draft 的多候选集合内时才沿树继续，否则提交该 target token 后结束本轮。候选可重复，合并后的 context 还须保留 multiplicity。理想的跨 context 独立 clocks 下，固定 target、keyed randomness 与初始 prefix，已到达的输出链由 target 侧决定，drafter 影响 stopping time；这比用接受来源决定 key 更清楚，也不同于把一个普通随机 seed 按不同执行顺序消耗。

精确性相对于所声明的 processed target law，并以独立 clocks 和完整 context 身份为条件；key 的伪随机实现与浮点行为还需另外验收。有限 support 可为每 token 生成 B 次 arrival 再选最早 B 个，支付约 support×B 的 clocks、树验证与水印 bookkeeping；单 context 的 acceptance 下界不证明总体吞吐。Unbiased watermark 是对随机 key/source 的边缘性质，不是每个固定 key 都等同无水印输出，也不证明任意改写攻击或法律归属。受限摘要/解释任务的检测与 drafter 替换对照不认证所有模型，实际输出一致性也未达到逐字全等；论文承认耦合记账开销。支持、key/context 复现或端到端收益不成立时保留普通 rejection sampler/target-only，安全审计另按第72章的 observation contract 验收。 [必要机制与反证](https://arxiv.org/html/2609.21858v1)。<!-- source-family:SF-2026-ARXIV-2609-21858 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18810:start -->
单 token overlap 也不足以指导 parallel block drafter。固定的 head/position loss weight 在 acceptance bottleneck
长期停在同一位置时简单且可重放；但早位逐渐变准后，限制 accepted prefix 的位置会向后迁移。此时可把 expected
accepted length 写成可微 surrogate，再按每个位置对 prefix survival 与 continuation value 的边际贡献分配 CE credit。
这只改变 drafter training owner 的 loss weight；target verifier 仍独占 accept/commit，drafter architecture 与
inference procedure 也不随之改变。

动态 credit 更接近 runtime 真正消费的 accepted progress，却把训练目标与 target-generated token、draft
confidence、block size、temperature 和 acceptance surrogate 耦合；累计 survival probability 还会让后位权重消失，
需要不对称平滑和数值保护。相关性下降、低置信度不稳、训练开销超过收益，或 target/temperature 漂移时，应回退
固定衰减 CE、普通 Forward-KL/CE，或重新标定后再启用。现有证据只覆盖 exact-v1 披露的 DFlash 单轨迹 parallel
drafter、有限模型与 benchmark，以及指定 H200 训练和 L40S serving 配置；不能外推到 tree/autoregressive drafter、
其他 verifier、batch/concurrency 或生产 SLO。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18810:end -->

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

这里的 workload 不能只固定输入输出长度。随机 token、重复文本与真实请求即使 shape 相同，也可能让 target 产生不同可预测性的续写，改变 drafter 的接受长度和最优 draft depth；padding、position 协议与并发还会改变实际执行成本。因此应在相同模型、采样合同与长度切片下保留真实语义流量，并同时测 accepted progress、draft/verify 开销和端到端吞吐。高 batch 下较短 draft 可能更合适，不能从单请求 acceptance 较好就推出 fleet 收益。<!-- source-family:SF-2026-ARXIV-2604-09557 -->

词表剪枝是另一条降低 proposal 成本的分支，却可能削弱跨语言、稀有 token 的长尾覆盖，使草稿更常被拒绝；在 exact target verification 仍成立时，这不等于最终 target 输出必然更差。需要分别验收 proposal 的接受效率与目标输出的 sampling/质量合同，而不是把两者混成一个准确率。作者 SPEED-Bench 的有限模型、B200及部分多卡配置还受 temperature、padding 与客户端并发实现影响，不支持通用合成流量偏差或生产 SLO 常数；语义分布变化、长尾 miss 或 draft 成本抵消收益时，完整词表、短 draft 和 target-only 仍是合理回退。

2026 年一项预印本把现有 lossy verification 归纳为 truncation-based 与
collaborative 两类，并报告 draft probability overshoot 是后者的重要 failure mode。
该 taxonomy 和经验结论仍属 `Status: Experimental`；本章只吸收更稳定的原则：
**放宽 exact verification 就是在修改 sampling contract，必须用 matched-policy
baseline 同时评估速度与质量。**

受 grammar 约束时，当前位置合法也不保证剩余前缀存在任何可完成后缀。若 verifier 只有局部 mask，它可能保持逐 token 合法却采到最终死路，得到的是 projected law 而不是目标 grammar-conditional law。更强的分支用 future-validity function 对局部 transition 做 Doob transform，再执行 exact acceptance：grammar owner 定义语言，validity evaluator 判断可完成性，target verifier 仍独占 commit。<!-- semantic-body-binding:SF-2026-ARXIV-2605-07698 -->

它以未来可完成性换取计算复杂度；一般 CFG 的 exact validity 存在 #P-hard 边界。只能近似时必须显式报告分布误差，或回退可枚举 grammar、普通 constrained decode 与明确的 projected-law 语义。exact-v1 对 Dyck、有限 JSON 等语法给出的理论、TV bound 与实验不证明一般 grammar 可廉价保持目标条件分布。

## 接受长度小例子

Draft 一次提出 4 个 tokens。若前 3 个依次通过，第 4 个拒绝，则本轮 target verification 至少推进 3 个 accepted positions，并在拒绝位置按 target-corrected distribution 产生 replacement token；第 4 个以后依赖错误 prefix 的候选全部作废。

这里作废的是提交资格及对应错误 prefix 的 KV，不意味着已经计算的辅助 hidden feature 永远不能作为下一轮 proposal 的条件；这种跨轮复用仍须从更正后的 prefix 生成并重新验证，不能把辅助 feature 冒充正确前缀的 target KV。它用额外特征对齐、有限生命周期与 reset 管理换取较好的下一轮草稿；当失效状态难以隔离或收益不足时，丢弃并重算仍是更简单可靠的路径。

把下一轮 draft 与当前 verify 重叠后，还要区分检索 proposal、target-verified guidance 与 committed chain。目标侧可以对检索候选做验证，用更正后的前缀刷新下一轮 draft 的条件；但“来自 target”或使用 causal mask 本身不证明整条 guidance 已符合 greedy 路径。只有在同一更正路径上已逐位置验证的 guidance 才能延伸提交；随机解码发生拒绝时，residual sampling 的 replacement 可能不同于预计算路径，后续 guidance 必须失效，不能绕过重新验证。[受限双侧检索方案](https://arxiv.org/html/2601.05524v1)支持这种状态与权限分层，但其 EM accuracy 不是 token-law 证明，本文不继承全局 lossless 宣称。检索、跨模型同步与状态刷新都增加成本；没有同路径验证依据、过期草稿难以隔离或 overlap 收益不足时，普通 rollback、短 draft 和 target-only 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2601-05524 -->

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

旧 block 的接受长度统计还受自身上限截断：接受到顶只说明后续没有被这次测量观察到，不等于下一位置已被拒绝；频繁到顶可提示需要另测更长 block，但不能直接把缺失尾部当成可兑现收益。尤其双向 block drafter 扩大 horizon 后，原有位置的 proposal 分布也可能改变，因此必须重新测量完整接受长度、EOS处理和实际验证成本，不能把旧 histogram 无条件外推成更长 block 的吞吐承诺。

把线性 draft 扩成树，还需要区分“这个 token 的边缘概率”和“它在已接受父路径下的概率”。一次 block backbone 前向可以共用，但后续节点用低秩 parent-conditioned head 修正分支分布；用于预算的边接受率则应在所有祖先已接受的条件人口上校准，而非混入祖先已拒绝、实际不可达的边。各边估计的乘积提供 path-survival 预算信号，不是未经检查的独立性证明。负载控制器再把这个信号与同 engine、硬件、batch 和温度的验证成本配对，以边际价格裁树；收益不成立时回到代码相同的 chain，必要时关闭 speculation。它增加条件头、校准与部署 profile 成本，不能由更高接受长度推出更高端到端吞吐。

随机解码下，树的选形与验证还须共享同一个抽样合同：先决定是否接纳下一 slot，再看该 slot 抽到的 token；兄弟节点从排除已有抽样的 proposal 依次无放回抽取，target 按同一 draw order 重构对应 proposal、执行接受比与正部残余更新，不能按 token 值事后丢弃或重排兄弟。否则确定性 top-k 树即使看似高概率，也可能改变输出分布。[受限树状研究](https://arxiv.org/html/2609.22098v1)保留了这一偏差反例，以及 greedy-match 校准标签到 sampling 拒绝率仍未单独隔离的差异；其 H200/BF16 matched research harness、A100 动态引擎和排除 drafter/prefill 争用的模拟不是同一生产吞吐证据。校准漂移、draw-order 重构或实际成本验收失败时，保留原 chain/target-only 路径，不将预算估计当作 exactness 保证。<!-- source-family:SF-2026-ARXIV-2609-22098 -->

树形选择并非只能在确定性 top-k 与完全随机扩展之间二选一。一个受限混合分支先保留 top-m，再从归一化 tail 抽一个 token，最后补不重复的高概率候选；供树排序的 proxy 与用于 target 验证的真实 proposal 必须分开。对 m≥1，取 proxy=min(q_m,tail mass)，既不依赖抽到的身份，又不小于最高 fill 概率，使 sampled slot 固定在 fill 前。按 path proxy 裁树还须保持祖先闭合与明确 tie order；单说 proxy 与 token 独立不够，低于 fill 的 proxy 仍会让是否保留取决于抽中谁。验证先按真实 tail 执行接受/正部残余，再处理确定性点，不能拿排序分数冒充抽样概率。

这条受条件构造的 lossless 论证不授予任意事后剪枝。正文 m=0 的 q_1+ε 与附录基例的 z=1 未统一，不继承该分支的全域保证；树排序用原概率、抽样/验证经温度处理时也必须保存各自身份。受限 A6000、三个 target、六项任务的三 seed 结果支持小幅 accepted-length 与速度收益，但低温下收益收窄，更多 deterministic slots 会剪掉随机探针。稀疏概率实现又牺牲 tail 覆盖，完整词表 PyTorch 对照未作同等优化；排序、采样、真实 proposal 重构与 KV commit 都有成本。边界或测量无法核实、温度/模型改变或收益不足时回到原 chain/top-k/target-only，不以理论精确性认证任务真值或生产 SLO。 [必要机制与反证](https://arxiv.org/html/2609.21827v1)。<!-- source-family:SF-2026-ARXIV-2609-21827 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-37532:start -->
预算决策还必须能落到 executor 的 shape。Block-diffusion drafter 保留全长候选最容易复用已训练资产，但每请求等宽验证会把低存活 suffix 和 padding 一起付费；统一裁短又会丢掉长可接受前缀。一个受限实现保留 full draft，以独立 predictor 给 prefix 打分，在同一 batch 的较小验证容量内分配不等长窗口，再把这些窗口紧凑打包。固定地址、固定 shape 的 workspace 将变化的 offsets/lengths 当作数据传递，使 token、position、KV reference 与 acceptance row 对齐同一请求边界，而不是每步由 host 重切 tensor 或重新捕获图。

Controller 只选择验证工作；target 仍拥有 acceptance、successor sampling 与 accepted-prefix/KV commit，长度选择不得依赖本轮接受随机数。Predictor 仍需按 target–drafter pair 监督训练与版本绑定，图兼容也不证明输出分布或质量已验收。[DScale v1 §III–IV](https://arxiv.org/html/2609.37532v1)的主证据限两种 Qwen targets、数学/代码、A100 和 closed-loop 并发；accepted-token retention 对照同时扩大了预算，不能归因于纯重分配。低并发、预测漂移或边界/packed layout 无法一致提交时，固定窗口与普通 draft–verify 继续成立；tile/kernel 实现属于第49章，这里的 owner 仍是验证容量与提交语义。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-37532:end -->

若先从同一个 drafter 独立抽多条完整 path，再按 target 相关的规则选其中一条，验证面对的已不是原始单 path proposal：选择改变了中选路径的分布，必须重构该 selection-induced distribution，再校正接受与残余抽样。[多路径 block verification 的受限构造](https://arxiv.org/html/2602.16961v1)用 q^Γ 表达这个分布，并在“接受一个 prefix、再补一个 correction token”的算法类中分析最优接受长度；其 greedy 多路径实现不继承全局最优。排序还必须有一致严格全序：原文 injective 排序定义与可能相等的 p/q 打分未统一，直接用严格小于公式处理 ties 会漏概率质量，因而不能把未澄清 recipe 当作所有输入均 exact 的已验证实现。更多候选也增加 draft、选路和验证费用：有限 OPT 对照中 K=4 的接受进度增加而 walltime 更差，较大模型在温度1时连每次调用进度也可能下降，低温又可改变取舍。只有 selection distribution、支持域、tie policy 和实际成本均可核验时才采用该分支；否则原 block verifier、chain 或 target-only 继续合理，接受长度不替代端到端 SLO。<!-- source-family:SF-2026-ARXIV-2602-16961 -->

分支预算还可以改变fork发生的位置，而不只是选择多少条完整path。先生成一段共享trunk，再在其已实现prefix下独立展开多条suffix，能复用共同草稿工作；代价是减少早处分叉的覆盖，并把trunk长度、suffix长度和宽度耦合到同一验证成本。[延迟树展开的受限实现](https://arxiv.org/html/2602.16994v1)让selector从有限三元组中选择，但selector的输入必须是当时可取得的状态：上一token的target/draft特征可复用，当前root的target特征缺一行KV，读取它要另付target forward；原接口只额外取当前draft特征。共享prefix下的proposal仍须按相同条件验证，selector不拥有acceptance或commit权，也不能沿用任意事后选路的原proposal。离线多次验证标签、warmup硬件曲线和MLP推理都要计价，forward延迟和accepted progress的surrogate不是生产并发/SLO实测；有限对照中某些模型的每次进度或tokens/sec反退，NDE也不在所有模型上提高速度。feature时点、采样合同或成本校准失配时，固定tree、较早fork与普通chain仍合理，不把dataset级oracle最优形状当作线上免费信息。<!-- source-family:SF-2026-ARXIV-2602-16994 -->

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

预算选择还包含两个互相耦合的问题：树要继续生长多深，以及已经生成的节点中要交给 target 验证多少个。只训练前者而固定后者，会让控制器适应一个上线后不再成立的验证成本；只训练后者也可能依赖固定深度形成的候选分布。一条受限分支先分别训练“继续/停止”的 depth policy 与 verification-size policy，再交替冻结其中一个、更新另一个，使二者适应彼此改变后的候选和成本。奖励采用本轮接受 token 数除以 draft 与 verification 时间，而不是单独最大化 acceptance length；它只调整 proposal 和验证工作量，target 的接受、采样与提交合同不能交给控制器。

联合适应新增策略训练、硬件成本校准与分布漂移风险，局部每轮吞吐也不等于多请求公平性、尾延迟或 fleet goodput。[受限实现](https://arxiv.org/html/2603.01639v1)的组件消融并未显示每个组件在每种模型上都单调增益，且采用 HumanEval 训练后在指定任务上测试；没有证明策略可跨硬件、并发和 SLO 无校准迁移。运行时应另计决策开销并保留正确性回归，成本分布稳定或学习成本无法摊销时，固定 tree、单一在线 depth policy 仍是合理选择。<!-- source-family:SF-2026-ARXIV-2603-01639 -->

请求之间的最优 draft length 也可能同时不同并随轮次变化。把整个 batch 锁在同一 draft/verify barrier 上，虽然实现简单，却会让短 draft 请求等待长 draft 请求；异步分支允许同一次 mixed forward 中部分请求继续 draft、部分请求执行 target verification，并依据在线 acceptance/cost 为每个请求更新计划。它改变的是 per-request control state 与 batch composition，不改变 target 对 accept/commit 的最终所有权。代价是更复杂的 KV refresh、混合 kernel、饥饿与调度公平性；作者的 1.70–4.58 倍结果绑定三模型、五类 workload 和披露 GPU，低并发、短输出或 mixed forward 效率不足时仍应回退同步 batch。

<!-- source-family:arxiv:2609.17943v1 -->

更细的请求预算也不要求在每个 draft depth 都运行一个停止判据。若深度间的置信信号并非同样有用，可在离线校准后只保留少数有区分度的 depth gates，并为这些深度分别设阈值；在线把有限的共享节点预算优先分给更有希望继续延伸的请求，没有合适的深度延伸时再考虑局部加宽。这是 proposal-tree 形状与请求间分配的替代分支，不是赋予置信模型提交权；target 的验证与回滚仍决定哪些 token 能进入正式历史。

稀疏 gate 减少控制开销，却可能错过请求可预测性突变，优先分配还增加校准漂移、公平性与 ragged-tree 执行成本。尤其“剩余预算大于零”不等于还能放下下一次整组扩展：runtime 必须按实际将分配的节点做 admission，不能把启发式伪代码当成严格容量或最优性证明。ECHO v1 的高低负载配置同时改变 depth、width 和节点预算，接受长度或平均深度也不是节点利用率，不能据此分离每个控制组件的收益或承诺通用 SLO。置信不足、负载稳定或展开成本不能摊销时，固定 tree 和更简单的 depth policy 仍应保留。<!-- source-family:SF-2026-ARXIV-2604-09603 -->

### Routed Slim Verifier 只接管中等成本分支

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


### Memory-limited Speculation 要联合规划树与驻留状态

固定 draft depth 或只最大化 acceptance，在 draft/target state 都能常驻设备时容易实现；内存受限后，扩大候选树会同时增加 KV、intermediate state 与 verification batch 占用。级联自适应树把候选扩展顺序、存活概率和 memory budget 放进同一 plan，scheduler 拥有分配与裁剪权，draft 只提出候选，target verification 仍拥有 commit authority。

联合规划可能提高单位内存的有效接受长度，却带来在线估计、树管理和不规则 kernel 开销；预测偏差会让高价值分支被过早裁掉。短输出、低并发或显存宽裕时，固定 verify length 仍更稳定。`arXiv:2605.11186v1` 的 §4–§6 只支持作者模型、显存和 workload 下的级联树结果，不证明 production serving 的端到端 SLO 必然改善。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11186 -->

内存预算不只决定候选树，也决定验证如何读取历史。显存不足时，整层历史 KV 搬回后再验证最容易复用成熟 attention，却把完整传输停顿放到关键路径。另一分支将 target 已提交的旧 prefix 复制到 CPU：用 H 表示已完成迁移的历史边界、C 表示 committed 边界、L 表示候选 frontier，维持 H≤C≤L；只有 copy 完成并确认可用才推进 H，释放对应 GPU 历史。近期 committed tail 与未验证 frontier 留在 GPU，拒绝只撤销 frontier，不回滚 CPU history。每个流入的 history chunk 服务本轮所有 verification queries，但每个 query/head 分别维护 running maximum、按新最大值重标定的分母与加权和，最后各自归一化；候选区域仍保留各 query 的 causal mask。分块的实数 full-attention 等价，不代表浮点逐 token 重放相同。

传输窗口还可在同 GPU 推进 drafter，但只有估计的 target 延迟增量和剩余窗口同时允许时，才准入一个完整 token forward；收到完成 ACK 后再考虑下一步。过期 round 不启动，已启动工作则等结束后退回 target 独占。TPC 限制不隔离 L2 或带宽，draft 越快也可能越妨碍目标。[SpecStream v1 §4–5](https://arxiv.org/html/2609.33184v1)的有限 A800 配置中，acceptance 增长仍可能吞吐下降，长历史 offload 仍慢于全 GPU 路径，drafter KV 也继续增长。离线调参、copy、共享资源和完整请求成本均需核算；窗口不稳、容量足够或收益不足时，串行 draft–verify、完整恢复和普通 AR 继续成立。<!-- source-family:SF-2026-ARXIV-2609-33184 -->

## Drafter 的演进：从辅助模型到受治理的 Serving Artifact

Draft path 也可以从 autoregressive model 演进为并行 refinement model。Diffusion/block draft 能一次提出多个 provisional tokens，减少 draft critical path；若再注入 target hidden features，可提高候选与目标分布的匹配。它没有改变 correctness owner：target 仍必须执行 exact verification，拒绝后只提交已验证 prefix。

```text
target feature snapshot
→ parallel block proposal
→ target exact verify
→ commit accepted prefix / rollback remainder
```

这条路线新增 target-feature interface、block denoising schedule、feature/cache compatibility 与专用 runtime；draft 更快也可能因接受率、verification batch 或并发机会成本而得不偿失。Autoregressive drafter 在实现成熟、target coupling 低或短 draft 足够时继续成立。

若 block-diffusion 模型在 block size 收缩为 1 时本身退化成 autoregressive factorization，同一组权重还可以在两个执行模式间切换：正常 block decoding 负责并行 proposal，block-size-1 路径负责逐 token verification。它避免维护独立 verifier 或再蒸馏一个模型，但没有消除额外 forward；因此轻量 router 只能根据当前状态决定“本轮验证是否可能回本”，而不能改变 acceptance 与 commit 规则。

这种 self-speculation 把风险从 model-version mismatch 转成 mode-switch correctness、router calibration、两种 cache/state layout 的一致性和失败后的重算。接受率低、block 很短或 router 开销接近节省时，直接 diffusion decode 仍更合理；需要严格 target-distribution 等价时，仍必须证明 block-size-1 路径就是 authoritative verifier。`arXiv:2603.25702v1` 只在 §4.1–§4.4 的 same-model block-size-one verifier、routing policy 与 fallback，以及 §5–§6 所披露的模型、任务和实验边界内支持该分支，不证明其他 diffusion 架构或 serving workload 获得相同收益。<!-- source-family:SF-2026-ARXIV-2603-25702 -->

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

对于重复使用同一组权重的 **looped LM**，浅递归深度已经能产生 draft，完整深度才是 target。朴素的“先 draft 一段、再整段验证”容易实现和回滚，却把两个阶段串行隔开；当不同 token 分别处于不同递归深度时，可以将它们组成同一批次，令新位置继续浅层提议、旧位置同时向完整验证推进。这里摊薄的是重复读取共享权重所需的串行调用，不是减少每个已提交 token 必经的目标计算。拒绝时只清空未确认前缀之后的在途位置，完整深度输出仍拥有唯一 commit 权。

这个波前调度用更宽的在途状态与跨深度 KV 访问换取更少的串行间隙：上下文变长或请求批量增大时，KV 流量和计算会吃掉收益。即使不共享跨深度 KV，重排 batch 与 reduction 后也不能保证 BF16 逐 token 重放等同普通 AR；跨递归深度共享 KV 虽可缓解流量，却可能进一步改变原模型读到的状态，必须另作为近似分支评估，不能沿用 exact self-speculation 的保证。它是 looped 架构的条件性选择，普通固定深度模型、KV 流量占主导或浅层 draft 命中率低时，分阶段验证或直接 decode 仍可能更合适。<!-- source-family:SF-2026-ARXIV-2609-23033 -->

并行 draft 还要分别解决两个容易混淆的问题。第一是 **architecture dependency**：完全独立的 block proposals
延迟低，却忽略 block 内因果关系；轻量 causal encoder 或低秩 correction 可以在不恢复完整逐 token critical path
的前提下修正后续候选。第二是 **training distribution**：若 drafter 只在 target/SFT prefixes 上学习，部署时却连续
消费自己的错误 proposal，就会遇到 exposure mismatch；target-assisted rollout 与 verification-error replay 可以
把被拒状态重新纳入训练。

### Chain Depth 会累积 Attention Drift

把 drafter 误差只归因于参数量差距，在短 proposal 中常够用；chain depth 增长后，hidden norm 与自生成 token 的 attention share 可能逐步偏移，使候选在进入 verifier 前已经离开 target 的高概率路径。Runtime 可按深度观测漂移，在 calibration 支持的阈值处执行 normalization、缩短 draft 或提前终止，但 target-only acceptance 始终保留唯一 correctness 与 commit authority。

更细的深度监控和归一化会增加统计状态、训练校准与控制分支，阈值漂移也可能过早终止有价值的 proposal。短 draft、接受率稳定或监控成本高时，原有固定策略仍成立；观测失配时应回退短链或关闭 speculation。exact-v1 只支持论文披露的模型、训练和 benchmark，不证明生产尾延迟的普适改善。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09992 -->

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

并行 drafter 的另一个独立压力是随 prefix 与并发增长的 **drafter-side KV**。为每个历史位置从 target hidden state 投影一套 draft KV，条件信息丰富，接口也容易训练，却复制了随请求长度增长的驻留状态；直接读取 target KV 可省掉副本，但可能失去最后位置 hidden state 已汇聚的上下文摘要，并让较远的 draft token 更难命中。一种条件性分支让 drafter 只读 target 已提交前缀的既有 KV，以最后位置 hidden state 初始化有界 recurrent state，再生成并行 proposal；这不阻止 target 在接受后继续写自己的 KV，target 仍单独验证和提交。它把额外 KV 容量换成 target/drafter 层维度与位置编码兼容、混合 backbone 计算和版本耦合。短输入、低并发或接口不兼容时，独立 KV 的旧方案仍较简单且可能更快；因此验收应同时量接受长度、实际 KV 占用和并发吞吐，而非只看单请求 draft 质量。<!-- source-family:SF-2026-ARXIV-2609-24197 -->

### Drafter 更新从离线训练演进为受 Gate 的在线状态循环

离线训练并冻结 drafter 的做法并没有错：当 target revision、请求分布与接受率长期稳定时，它把训练故障隔离在
Serving 之外，也让 rollback 只需切换一个经过验证的 artifact。约束在流量持续漂移时改变——drafter 训练时看到的
prefix 与线上 target 真正访问的状态逐渐分离，固定 artifact 的 proposal cost 仍在，却不再稳定换来 accepted progress。

第一步演进可以复用 target 在正常服务中已经产生的 hidden states，作为 drafter 的训练信号，而不重新加载 target
或为训练重复 target forward。Serving runtime 只拥有请求执行与 hidden-state capture；独立 trainer 拥有 gradient、
optimizer 与 candidate draft revision；控制器根据观测到的接受率、训练开销和 GPU 机会成本决定是否启用 speculation
及训练。target verifier 仍是 correctness owner，线上信号不能越权成为 acceptance authority。

```text
committed target serving state
→ bounded hidden-state capture
→ decoupled draft training
→ candidate revision evaluation
→ gated promotion or rollback
```

这样可以降低重复 target compute，却新增 signal retention、privacy、训练资源争用和 revision lineage。训练信号若偏向
高频租户，还会把少数 workload 的 drafter 质量掩盖在平均接受率里；预期节省不能覆盖训练与同步成本时，应关闭在线
训练并继续使用离线 drafter。<!-- source-family:SF-2026-ARXIV-2602-05145 -->

第二步演进把更新变成持续的 on-policy loop：专用异步 training server 消费 serving traces，生成新 draft revision，
再经版本化同步送往 inference workers。异步化避免训练直接进入 Decode critical path，但也使 serving 中可能同时存在
多个 draft revision；因此同步频率、promotion epoch、worker pinning 与 rollback point 必须成为显式状态。训练服务器
只能提出 revision，Evaluation/acceptance telemetry 才能授权发布，request 一旦开始则应绑定已提交版本，不能在中途
静默换权重。

这条路线用对 domain shift 的更快适应，换来 stale-gradient、短期过拟合、跨 worker 版本偏斜和同步流量。线上轨迹
并不天然代表未来分布，错误 proposal 也可能形成自我强化；无独立 holdout、接受率校准或稳定 rollback 时，周期性离线
刷新仍更容易审计。`arXiv:2602.06932v1` 只支持作者披露的异步 on-policy 架构与控制关系；本轮 exact-v1 packet
没有独立 Evaluation locator，因此不吸收性能 headline。<!-- source-family:SF-2026-ARXIV-2602-06932 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36590:start -->
同模型复用还有一条不同于 early exit 或新增 MTP head 的分支：完整 verification 已为前缀产生深层 KV，下一轮只让末端薄层读取这份 cache，并把最新 token 的 raw embedding 直接送入薄层起草，避免重新执行大多数前层。SEED 在所测模型中使用最后两层；这里的“cross-attention”只是标准 self-attention 读取缓存的描述，不是新加的 encoder–decoder 模块。浅输入起草态仍属 provisional，完整 verifier 只提交 accepted prefix 对应的深层状态，拒绝后的候选及 cache 不能进入下一轮 committed prefix。

这也不是 training-free 跳层：AR cross-entropy 与 block-causal speculative loss 联合训练，才让薄层适应“已验证深前缀 + 当前浅输入”。Verification authority 因而是重新训练后的 target，不保证保持原 checkpoint 分布。薄层加深能改善候选却增加 draft 成本；深表征 probe 是动机而非因果证明。Qwen3-1.7B/4B-Base、逐任务 SFT、greedy、单 A6000 的实验不证明大模型或生产并发收益，代码未复现；无法重训、兼容身份变化或收益不足时，仍选独立 drafter、原生 MTP 或普通 target decoding。[exact-v1 §4.1–4.3、§5、AppA](https://arxiv.org/html/2609.36590v1)
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36590:end -->

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

### 历史 Logits 与 N-gram Cache 只能提出候选

独立 drafter、原生 MTP 和 latent probe 都在试图给未来 token 提供更好的 proposal；上下文重复模式充分时，另一条不重训模型的分支是保留已验证位置的 target logits 与 n-gram。最近一次相同 token 之后的 logits 可作为未来分布的 surrogate，而不是未来真分布；检索结构则通过触碰祖先更新近期性、只淘汰 LRU leaf 来限制状态容量，再将检索树与 logit 树合并交给 target 验证。状态维护和 failure-link 重建影响能找出哪些候选，不获得 token 输出或 KV commit 的权限。

这条路径省下 drafter 训练，却增加 logit 存储、模式查找、树构造及重建成本；相同 token 的语义上下文改变时，旧 logits 可能完全不适合新的 continuation，候选 budget 也会挤占验证计算。`arXiv:2604.14885v1` 的 RACER 证据限于 greedy、batch 1、FP16、RTX 4090/A800 与最多 1,024 output tokens；其中 Llama-3.1 的 SpecBench speedup 2.41 低于 EAGLE-3 的 2.51，不支持通用胜出、并发 SLO 或随机采样 exactness。重复模式稀少或维护成本过高时，应回退普通 target decoding 或已有 drafter；acceptance 与 commit 的合同仍由 target verifier 维持。

<!-- source-family:SF-2026-ARXIV-2604-14885 -->

固定离线文档 draft 也可以沿已接受 prefix 做窗口匹配和树状 realignment，但局部 crop 的并行校正不能直接拥有整页输出。一个分层分支先对 crop 提出并校正候选，再交给 full-page target 在整页语境下最终验证；global 阶段仍循环推进，不等于一次 forward 验完。[HSD 的受限机制](https://arxiv.org/html/2602.12957v1)中，τ=1 只在同 processed greedy 与 tie 约定下维持该验证，较低阈值容忍非 argmax，是近似质量分支而非随机采样 exactness；target confidence 也不认证 OCR 真值。仅 crop 路径会失去语境、部分文档仍慢于原 decoding，筛去重复或超长输出后的 timing 人口不能代替全部文档。Draft、crop/full-page 编码、trie 与验证循环的成本都需保留；draft 不准、页级质量退步或视觉 prefill 主导时，回退整页 target decoding 或已验收 drafter，不从区域接受率宣告全流程加速。 <!-- source-family:SF-2026-ARXIV-2602-12957 -->

### 动态候选树必须编译为 Accelerator-safe Commit Plan

在 GPU 上逐层扩展候选树、动态裁枝并回滚 KV，控制流灵活且容易根据 acceptance 调整；专用加速器若要求静态 shape、规则 batch 和预先规划的 memory layout，同一算法会被 host orchestration、动态分支与不可表达的回滚吞掉。此时不能取消 target verification，而应把候选树编译成静态批结构，并显式分开 provisional candidates、verification result、accepted prefix 与 KV commit frontier：

```text
dynamic candidate tree
→ flatten with ancestor / position identity
→ static accelerator batch
→ target verification
→ ordered acceptance
→ atomic KV and output commit
```

Tree builder 仍只拥有 proposal；target verifier 拥有 acceptance，runtime 拥有 KV/output commit。静态化降低动态控制开销，却可能计算更多无效候选、限制树形自适应，并把 mask、position 与 rollback correctness 写进 execution plan；接受率低或静态批浪费较大时，普通 Decode 或较小固定 proposal 仍更稳健。`arXiv:2603.08088v1` 的 §3.1–§3.3 支持 branchable KV、tree flattening/mask/position 语义与 fused teacher 机制，§4.5 只定义 timing methodology，§5.1–§5.2 才构成所测 Ascend NPU 的实验边界；Limitations 之外不证明其他 draft/target、加速器或生产 SLO 获得相同收益。<!-- source-family:SF-2026-ARXIV-2603-08088 -->

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

若选择不经 target verifier 的 standalone 块输出，训练时还要处理块内前缀归谁所有。一个受限分支让 student 一次给出整块 argmax tokens，再让冻结 AR teacher 依次读取这些 student tokens，对块内条件概率评分；不同块之前仍使用真实训练前缀。这不是逐位置独立对齐 gold token，也不保证并行 marginal 恢复 teacher 的 joint distribution，原式标为 KL 不授完整 KL 期望等价。部署用置信度决定块长并直接提交，因而接受的是质量—并行度取舍，而非 lossless acceptance；训练 teacher forward、mask/KV 更新、模板与较长训练均须计费。作者有限 Qwen 设置约三倍 chunk factor伴随准确率退步，也不等 wall-clock 三倍。质量回归或块内依赖不满足时，逐 token AR 或保留 target verifier 的 proposal 分支仍成立。<!-- source-family:SF-2026-ARXIV-2602-06019 -->

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

对工具调用文本，block hint 还可以细化成 **schema 状态决定 draft 来源**。有限状态机区分 tool name、parameter name、parameter value 与普通文本：前两类从已知 schema 提出结构候选，开放值则利用 token recycling 和历史成功调用的 hidden-state/suffix 检索。这样将结构冗余与内容复用分开，所有分支仍由原 target 验证，并没有把 target 约束成只会生成 schema 中的候选。Schema 合法、历史调用成功也不等于当前业务或权限合法；这一层只改变 token proposal，不能越过第 78 章的工具执行授权。<!-- source-family:SF-2026-ARXIV-2604-13519 -->

状态解析、schema revision 和历史检索增加维护、隐私与检索成本，开放值与结构边界判断错误还可能压低接受率；格式不稳定、复用弱或大 batch 下应回退统一 drafter/普通 target 生成。作者 Qwen/Llama、API-Bank/ToolAlpaca/BFCLv2/ToolBench 的 batch-1 实验支持这个条件分支，不证明高并发 SLO 或任意精度下分布完全相同；训练型 drafter 的准备成本也不能从单请求加速中消失。下一层的 read-only tool speculation 则真正提前发起外部调用，它另有 effect frontier，不能与本节的 token 草稿混为一件事。

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

Proposal artifact 还可以来自同一 RL prompt 的历史 rollout，而不再训练一个小 drafter。[受限的复用分支](https://arxiv.org/html/2601.09083v1)把历史 response 的 substring 组织成计数树，用当前 suffix 匹配后提出频繁 continuation；没有可用匹配时继续普通 decode。历史文本只提出 token，不拥有 learner trajectory：仍由当前 policy 验证后决定实际接受的轨迹，不能把旧 rollout 直接当作当前 on-policy sample。同一 group 正在生成的文本可以更新候选树；空闲时为未来 prompt 做 runahead 也可以补充草稿，但这些预生成轨迹本身丢弃，不成为训练 target。<!-- source-family:SF-2026-ARXIV-2601-09083 -->

这用检索、树维护与缓存容量换 draft-model 训练和执行成本，也新增 prompt/policy identity、历史文本泄露与过时草稿问题。受测实现支持局部 rollout 加速，未完整披露随机采样下的 rejection/residual 验证细节，不能据此认证 target distribution；runahead 的接受率模拟也不是端到端训练收益。验收需分别记录 rollout、完整 step、被丢弃工作与缓存开销；复用弱、内存紧或验证语义不清时，回退普通当前-policy decode 或已验证的 drafter。

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

还可以不另训练 draft model，而直接借用 target 的非 expert 参数和 GPU 中驻留的少量 hot experts 生成 proposal。draft阶段不换入CPU专家；缺失expert只在proposal路径由驻留子集或离线affinity替代，完整target验证仍按真实路由取权重并裁决输出，再按本轮激活热度更新下一轮驻留集合。这改变的是 draft artifact 与 residency 的关系，不是允许替代 expert 的结果直接提交；验证中的 expert union、换入字节与 accepted progress 必须共同结算。

它省去独立 draft 训练，却增加 affinity校准、热集替换、缓存抖动与额外验证工作；更多驻留draft专家提高接受率，也可能因compute增加而更慢。作者的NLLB/WMT greedy精确匹配与Mixtral/Scout的sampling配置是不同验证合同，借用同一target权重本身不证明任意采样exactness。Xeon、H100/PCIe5与有限batch结果中，小batch缓存可优于speculation；模型已全驻留、hotness漂移或替换成本超过收益时，应回退target-only decode、静态cache或已有draft。运行时仍须先核自己的正确性与负载，而不是采用一个最大吞吐倍率。

<!-- source-family:SF-2026-ARXIV-2604-10152 -->

这些路径共用一个判断：Speculative Decoding 的收益取决于几个条件。

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

### Device–Edge Offload 是受约束的 Proposal Placement

固定在设备端生成相同长度的 draft，适合网络和电量稳定的场景；移动环境中，每个 token 的 entropy、剩余 energy/latency debt 与链路状态都会改变继续本地生成是否值得。Controller 可以据此在线决定继续 draft 或发送到 edge target，但该 action 只改变 proposal placement，不能越过 target verifier 的唯一 commit boundary。

在线控制以额外估计器、网络观测和策略抖动换取资源适应性；模拟中的平均收益不能代表真实无线尾延迟。估计失准、链路剧烈变化或安全预算不足时，应回退固定短 draft、直接 target inference 或保守 offload。exact-v1 证据只覆盖其模拟拓扑、draft/target pair 与资源 envelope。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10124 -->

## Stochastic Target 改变了 Block Drafter 的 Factorization

在 greedy target 下，block drafter 可把未来位置近似为较稳定的单一路径；sampling entropy 升高后，各位置存在相关的多模态 continuation，独立预测会组合出 target 几乎不会采样的 block。更合适的 drafter 应显式建模跨位置依赖，并以 expected verified progress 而非逐 token likelihood 作为训练目标。

exact target 仍拥有最终验证与 commit 权，因此该变化提高的是 proposal quality，不改变 correctness owner。它会增加 drafter 复杂度，且收益依赖 target entropy、batch 和验证成本；低熵或短 block 场景仍可使用简单独立 draft。
<!-- source-family: arxiv:2608.05448v1; daily: 2026-08-07; semantic-body-binding: stochastic-block-draft-factorization -->

### Draft 结构必须同时优化 Coverage 与 Verification Waste

固定宽度 tree draft 易实现，却会在不确定分支上生成大量最终被拒 token；只走一条 greedy draft 成本低，又可能错过高概率替代路径。渐进 tree 分支根据局部置信与剩余验证预算逐层扩展，controller 拥有 expansion policy，target model 仍拥有 acceptance 与最终 token commit。它用额外 tree state 和不规则 kernel 换取更好的 coverage/waste 平衡，短输出或 acceptance 已高时线性 draft 仍更简单。

当一棵树混用不同来源的候选时，局部置信还不够：上下文匹配的连续片段与历史 logit 转移候选可能具有不同接受率。若仍按来源无关的概率分配验证节点，就会把深度浪费在低接受率路径上。一个有条件的分支是在固定节点预算内，让高接受率来源形成深 spine、低接受率来源在各层提供较宽 fallback；target 仍统一验证，只提交通过的前缀。这样优化的是每次验证的预期 accepted progress，代价是来源级接受率估计、随 workload 漂移的树形选择和不规则验证布局。相关理论依赖候选接受事件的近似独立与来源异质性；作者五个模型、五个数据集、greedy batch-1 的结果不证明 sampling、并发或生产尾延迟普遍受益。来源差异不稳定或估计开销过高时，原来的单源链/固定树仍是更稳的基线。<!-- source-family:SF-2026-ARXIV-2604-02047 -->

MoE target 还暴露第二个成本轴：draft 的 token acceptance 高，不代表验证便宜；若候选触发大量分散 Experts，weight movement 与 All-to-All 会吞掉收益。drafter selection 因而需要联合估计 acceptance、verification FLOPs、Expert-set overlap 与通信，并在预测失准时回退普通 Decode。作者实验只覆盖其 MoE、draft 与硬件，不能把某个 Expert 阈值当成通用配置。

<!-- source-family:SF-2026-ARXIV-2607-10661 -->
<!-- source-family:SF-2026-ARXIV-2607-12696 -->

### Diffusion proposal 与 AR verifier 必须对齐同一个 Prefix 条件分布

masked diffusion 一次给出多个位置的 marginal，AR target 却按已接受 prefix 逐 token factorize。直接按 diffusion marginal 排序候选，会把彼此不一致的未来 token 组合交给 verifier，造成 acceptance 浪费。proposal adapter 应把候选重新条件化到当前 committed prefix，或只提交能够被 target 顺序验证的结构。

对齐增加 proposal 计算和实现复杂度，也不能保证高 acceptance；特定模型与任务结果不能外推。target verifier 始终拥有 exact commit，factorization mismatch 或预算超界时回退普通 AR decode。

<!-- source-family:SF-2026-ARXIV-2607-22634 -->

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

严格 acceptance 会截断被拒绝的 draft；允许质量—成本取舍时，也可以显式放松接受函数，并随 draft 位置衰减放松量，将更大的偏离预算放在较早位置。拒绝后的 residual 必须随该接受函数一起定义，不能只调 acceptance 而继续沿用原纠正分布。[受限图像 speculation 的理论](https://arxiv.org/html/2601.09212v1)中，给定接受函数后的正部 residual 最小化的是固定长度、包含虚拟 target 续写的混合分布误差上界，不是任意完整生成序列的全局最优 law，更不是图像语义保证；只有接受函数逐点不低于经典规则等条件成立时，特定 residual 等价关系才可使用。位置衰减的平均归一化 schedule 可能让后段系数低于一，不能自动沿用这一条件。

这种放松属于有损替代分支，而不是更高效的 exact verification。小扰动、特定区域质量平衡与每个 prefix 的分布距离条件，不能由有限样本平均距离替代；接受长度改善也不能替代最终质量和端到端时间的验收。受限图像模型的质量指标已有退步 slice，draft 训练、验证树、lookup、调参和额外采样的完整预算仍须计入。需要严格 target law、质量回归或误差条件无法校准时，回退经典 acceptance/residual 或普通自回归，而不把经验退火配置提升为通用无损配方。<!-- source-family:SF-2026-ARXIV-2601-09212 -->

有损分支还要分清“按某个draft token选择的目标分布”和最终算法的混合输出分布。可以在单步divergence预算内提高当前proposal的接受概率，但这一目标随抽到的token变化；把各条件路径及拒绝后的recover sampling混合后，最终law的偏离并不直接等于局部预算δ。[Cactus的理论](https://arxiv.org/html/2604.04987v1)给出另一隐式控制函数Γ(δ)，并非可直接套用的同一δ上界；实用KL求解还有Taylor近似。

因此接受长度增加必须与最终输出law、任务质量及实际wall time一起验收，不能把单步分布界升级为整序列事实正确率。调参、求解、额外采样和质量回归是接受率收益的代价；需要严格target-distribution合同或近似边界无法校准时，仍回退经典exact acceptance，不能把有损路径更名为无损。<!-- source-family:SF-2026-ARXIV-2604-04987 -->

另一条有损分支不再遇到首个拒绝就停止当前 draft，而是维护多条尚未提交的粒子轨迹。每个粒子先生成一段，target 批量计算该段的 likelihood ratio，以 importance weight 修正 proposal；有效样本数不足时重采高权重祖先，再继续推进，最后从归一权重中选出一条完整输出。这里的权重、祖先和 KV 引用是候选状态，不是已经验证可提交的 exact prefix；重采复制的 metadata/refcount 必须与真正共享的 KV 区分，内部一步推进更多 token 也不等于用户同时收到多条序列。要求严格 target law 的请求仍用经典 acceptance；允许近似的请求则必须验收最终混合分布和任务质量，不能沿用 verifier 的逐 token 无损合同。

单轮重要性采样的一致性也不是整轮重采历史的有限误差保证。受限 [SMC v1](https://arxiv.org/html/2604.15672v1) 的定理要求 iid proposal、目标绝对连续和有限四阶权重矩，完整多轮误差仍未证明；有限粒子不能称 exact。并行粒子只在权重搬运主导、总验证 token 满足 `BN(K+1)≤R` 的 roofline 条件下便宜，输出仍只有一条，不能把粒子数直接乘进交付吞吐。Paged/Radix 的祖先元数据复用减少 KV tensor 复制，却仍有随序列长增长的元数据和重采成本；其单 H100、Llama/Qwen 结果还须保不同 draft 容量、质量容差以及额外 GPU 基线的分母，不能外推同质量、同预算或生产 SLO。权重退化、长轨迹相关或质量回归无法校准时，保留普通自回归与经典 speculation 回退。<!-- source-family:SF-2026-ARXIV-2604-15672 -->

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

## MoE Verifier 的 Expert Budget 应对齐真实提交概率

树验证会同时展开多个位置的 expert demand，原本稀疏的单 token 路由也可能形成很大的 expert union。若必须保持原 target 的输出分布，完整路由、缩短 draft tree 或减少并行分支仍是合理选择。允许质量近似时，另一条分支是逐层等权累加整棵树的 router mass，只保留固定预算的 top-B experts；名单外的 expert 可以被截断为零，也可以由名单内的 expert 替换并重算组合权重。这是在改变 verifier 的 target routing，不只是裁剪 draft：经典 acceptance rule 即使实现正确，也只对应修改后的 target，任务分数接近不能证明保留原 target 的分布。

[MoE-Spec 的受限实验](https://arxiv.org/html/2602.16052v1)支持这种质量与专家流量的局部取舍，而不是通用无损加速：作者用三种 MoE、五类任务、每类 80 个样本，在 FP16、A100 和 single-request 条件下按质量容忍度选择预算；温度 1 的结果含五次运行，但所沿用 EAGLE tree 的 q=1 实现本身有分布偏差，不能用两者共享的偏差证明 exactness。选择器还付出作者所报 2–3% 开销与部署预算校准，长尾质量、小树和高 batch 下的专家共用可能抵消收益；执行全部专家后才选择的 oracle 也不能当作可部署加速。严格正确性或质量回归时应回退完整路由与较简单的 proposal，而不是把放宽质量合同悄悄写成原模型等价。<!-- source-family:SF-2026-ARXIV-2602-16052 -->

MoE target 验证一个 draft block 时，各位置到达最终输出的概率不同；把每个 draft token 的 router mass 等权相加并固定 expert 数，会为很可能被前序拒绝截断的位置搬运无效权重。更合理的 verifier selector 以离线估计的 position commitment probability 加权 expert demand，用需求分布有效秩自适应决定集合大小，再在不移除 root token 自然 top-k 的前提下按 residency 裁剪。收益是减少 verifier expert traffic，代价是提交概率漂移、额外统计和 rerouting 风险；校准失效或正确性预算紧时回退完整路由。`arXiv:2608.02989v1` 只在 12 个 model-task pair 上验证该机制。<!-- source-family:SF-2026-ARXIV-2608-02989 -->

## 云边 Speculation 把网络消息纳入 Exact Verification

draft 位于边缘、target 位于云端时，经典 acceptance 之外还多了一条非对称通信路径。常见接受路径可以只上传 acceptance-sufficient 信息；拒绝时再由下行逐级补充 correction，只有 total-variation certificate 证明有限 top-k 足以恢复 residual distribution 时才允许提交，否则升级到更完整表示。调度器只在 confirmed-prefix frontier 上跨请求流水，不执行依赖尚未确认前缀的同请求 runahead。收益是隐藏受限上行链路，代价是证书计算、多轮纠正和复杂恢复；网络稳定或同机验证时经典协议更简单。`arXiv:2608.04974v1` 的 2.82–28.03× 仅属于三组模型 pair、两类 workload 和三个网络 profile。<!-- source-family:SF-2026-ARXIV-2608-04974 -->

### 多模态 Drafter 应按状态取证，而不是固定携带视觉预算

不同任务和 decode 阶段需要的视觉证据并不相同：固定少量 token 会削弱 grounding，固定大量 token 又会拖慢 drafter 并降低接受率。可复用视觉 memory 配合有界、state-conditioned retrieval，把视觉读出作为 hidden-state correction 而不是反复插入自回归上下文，可以改善 cache 复用。它仍需在目标模型、视觉任务和质量门槛下校准；动态取证错误必须能退回完整视觉条件。
<!-- source-family: arxiv:2608.22883v1; semantic-body-binding: state-conditioned-visual-speculation -->

视觉取证还可以在训练与推理之间分离。直接让小 drafter 读取完整 visual KV，条件最直接，在容量足够时仍合理；长视觉序列却可能稀释 attention 并压低接受长度。一条替代分支在训练时用 target 中层 visual state bridge 和递归 multi-token prediction 适配 drafter，推理时只消费 target 已融合视觉的 text hidden states 与有界 text window，把完整视觉计算留给 target。它不是从整个系统删除视觉，也不把 draft 的窄视图授为完整 evidence；target 继续拥有 verification、输出分布责任与 accepted-prefix commit。

Bridge、hidden-state interface 和训练分布新增耦合，不能由训练用过视觉推断任意任务在推理时都能少读视觉。[受限实验](https://arxiv.org/html/2602.15318v1)中，25k visual tokens 的平均接受长度可由1.21恢复到4.37，但短序列消融也有3.82→3.79的小幅退步；LLaVA-OneVision7B/L20、temp0的平均 decode speedup 为2.82，而包含 prefill 的 end-to-end speedup 为1.93。Prefill 仍付费，训练与接口成本也未被这两个比率消除；受测任务不证明全部质量、并发或 SLO，更不等于本书已核验 lossless 实现。接口漂移、接受率或独立质量回归时，退回完整视觉条件、较简单 draft 或普通 target decode，不让局部长序列收益覆盖这些旧分支。<!-- source-family:SF-2026-ARXIV-2602-15318 -->

### 多个 Drafter 可以非破坏地嫁接到共享 Speculation Tree

不同 drafter 的调用成本和命中区域不同，若每次都重建候选树，就会重复支付 target state 与验证开销。把新分支非破坏地 graft 到共享 tree，并依据在线接受状态决定 call、skip 或切换更强 drafter，可以把成本集中在最可能被提交的路径。代价是 tree ownership、节点去重和 verifier commit 必须保持一致，错误分支不能污染已经验证的前缀。
<!-- source-family: arxiv:2608.26112v1; semantic-body-binding: multi-drafter-shared-speculation-tree -->

共享树是同时组织多个候选来源；另一条alternative branch每轮只调用一个drafter，用当前block的target/draft分布距离形成alignment反馈，再以UCB等策略兼顾探索与利用。每个新query重新估计任务匹配，与同一query内通过discount/window追踪漂移，是两种不同更新范围。Selector只决定proposal来自谁，不取得target验证或committed-prefix权。

在线选择可适应异质输入，却增加驻留weights、未跟上当前prefix的drafter KV补齐、探索和切换成本。[Multi-Drafter的stationary/i.i.d.及随机停止时间分析](https://arxiv.org/html/2604.05417v1)不直接保证wall-time收益；对齐距离也不是业务质量分数。切换贵时可先探索再固定，但误淘汰最优drafter与query内漂移仍会失败。任务同质、pool过大或显存/反馈预算不足时，固定单drafter继续更合适，严格target commit不随选择器改变。<!-- source-family:SF-2026-ARXIV-2604-05417 -->

## Diffusion Draft 需要重新建立可验证前缀

### Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority

独立小 drafter 成本低，却可能因容量不足产生低 acceptance；直接放大 drafter 又会吞掉 speculation 的收益。对于
block-diffusion drafter，可以把 target 的只读 hidden feature 按 draft layer 注入，使较宽的并行 proposal 更接近 target，
同时把 `target revision + feature interface + draft layer + denoising schedule` 固化为 proposal artifact。它改变候选质量，
不改变 target verification、accepted-prefix commit 与 rejected-suffix rollback。

更多 target feature 会增加内存、带宽和 drafter critical path，并可能在 interface 漂移后产生表面高 acceptance 的错误
状态。收益必须以 accepted progress 减去 feature extraction、draft 与 verify 总成本衡量；低 acceptance、feature 不兼容
或 batch 无法摊薄开销时，回退较小 drafter 或普通 target decode。作者证据只覆盖所测模型、任务和实现。

<!-- source-family:SF-DFLARE-DIFFUSION-SPECULATION -->

### 双向 Mask Context 必须先改写成 Temporal-causal Verification Layout

AR target 天然把已确认 prefix 与未来位置分开；diffusion LM 的 mask slots 可以双向交互，若直接套用 token-level
verification，同一次 forward 中的候选可能互相泄漏未来信息。可验证分支把 reference/data token 与 prediction slot 分开，
按 denoising temporal order 构造 causal mask，并让 RoPE position 与该顺序一致；draft 只收集候选，target 仍在单次
forward 后决定可提交集合。mask、position 或 block identity 不一致时，整块候选失效。

这条布局恢复了受限的 verification boundary，却可能降低 diffusion 并行度，并引入额外 KV/layout 与不同 temporal factor
的质量—吞吐选择。无法证明目标分布保持、tokenizer/position contract 漂移或质量 gate 失败时，应回退原始 blockwise
denoising，而不是把更快的近似路径标成 exact speculative decoding。

<!-- source-family:SF-2026-ARXIV-2606-02544 -->

## 小结

Speculative Decoding 没有取消 autoregressive semantics，而是让便宜的 drafter 先提供已知候选，使 target model 能并行验证多个 positions。Exact acceptance 保护输出分布，系统收益则取决于 accepted progress 是否覆盖额外 draft、verification 和状态管理成本。放宽 verification 可以改变速度—质量 operating point，但那是新的 sampling contract，不再是语义透明的纯执行优化。

至此第46～48章分别从 batch membership、KV placement 和 serial target steps 三个正交方向优化 runtime。下一章开始把这些机制映射到实际 Serving stacks。

### AR 与 Diffusion 可以组成双视图 Proposal/Verification

AR 保留精确左到右 factorization，diffusion 则能并行提出多个 token；双视图架构让 diffusion 负责 proposal，AR owner 负责验证和最终 commit，从而把并行机会与输出语义分开。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12825 -->

收益来自更长的可接受 proposal，代价是同时维护两套模型状态、额外内存和一致性协议。所测模型与吞吐结果不能证明所有 workload 都加速；接受率低、状态同步出错或内存超限时，应回退普通 AR decoding 或更小的 draft model。

### Lossless 要区分分布、有限精度轨迹与任务结果

理论上的 distribution equivalence 不等于 BF16/FP32、不同 reduction 或 kernel path 下逐 token trajectory 完全相同，更不等于 downstream benchmark 不变。Speculative artifact 应分别声明算法分布保证、有限精度 replay 身份和任务质量 gate；strict replay 失败时，唯一精确 fallback 是关闭 speculation、运行 target-only decode。<!-- source-family:SF-2026-ARXIV-2609-15504 -->

被 verifier 拒绝的 hidden state 也并非必然无用：它可以作为下一轮只读 proposal state，减少 drafter 重算，但不得越过 target commit frontier。reuse drift、ancestry/bookkeeping 不完整或额外状态抵消收益时，应丢弃临时状态并恢复普通 drafting。<!-- source-family:SF-2026-ARXIV-2609-14717 -->

另一条重叠分支预先计算多个可能验证结果对应的下一轮 draft：cache key 不是只有接受长度，还包含拒绝后 sampled bonus token；真实结果到达后仅选命中分支，否则执行 backup drafting。Verifier 仍按普通 acceptance/residual 规则提交，且不必把整个 draft cache 交给 target 验证。[Saguaro 的受限机制](https://arxiv.org/html/2603.03251v1#S4)还揭示 acceptance 与 cache hit 不是同一目标：压低 cached top-token 的 draft 概率会让 residual 更易命中缓存，却可能降低 draft 接受率。若改变 proposal 分布 q，就必须以相同 q 计算 acceptance 与 correction，不能一边用偏置 draft，一边沿用旧 residual 来声称 target-law 不变。

batch 越大，至少一请求 cache miss 导致整批等待的机会越高；低延迟但低质量的 backup 因而可能胜过高质量 just-in-time draft。这个转折依赖 batch barrier、命中率与两种 draft 的实际成本，不是随机 backup 普遍最优。它还要支付额外 draft device、分支 mask、fragmented KV 整理和每轮通信；作者配置用 target TP4 H100 加独立一张 H100，计时排除 Prefill，不能把 decode 改善当成同 GPU 预算的全请求或生产 SLO 保证。命中率低、分支太贵或吞吐已 compute-bound 时，同步 draft–verify 或 target-only 路径仍成立。<!-- source-family:SF-2026-ARXIV-2603-03251 -->

进一步并行化时，下一轮 draft 通常依赖本轮 verifier 的接受长度与 bonus token；若提前猜测这两个结果，猜错就必须退回串行路径，batch 越大越容易有请求触发回退。一条条件性替代方案是把昂贵的 draft backbone 与轻量 token correction head 分开：验证尚未结束时，backbone 对每个可能的接受边界预计算互不污染的 proposal 表示；verifier 给出真实接受前缀与 bonus 后，只选择对应分支并运行短 head。target 始终拥有 token/KV 的最终提交权，这消除了**猜错验证结果导致的 backbone 串行回退**，但不消除 head、同步屏障与分支预计算的成本。分支数、显存和 draft GPU 预算可能抵消收益；backbone 赶不上 verification、batch 小或旧 drafter 已足够便宜时，顺序 draft–verify 仍更简单。DPara 的作者证据限于 Qwen3-8B/14B、所列数学/代码/聊天任务及 H800/GB200/A10 配置，不能外推为任意采样、并发与 SLO 的普遍加速。<!-- source-family:SF-2026-ARXIV-2609-27396 -->

## Review notes

- `SF-2026-ARXIV-2602-16994` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16994v1) §4–6/T4–7、AppendixE Eq8–12/footnote4；2+2+2=6，共享trunk后fork与selector可取状态差额深入。采用current-target-root须额外forward的接口边界，不授oracle免费、全模型收益或surrogate生产SLO；有限反侧/额外成本/旧tree共存近正文。root必要原源/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-06019` — Daily `2026-02-07`；[MTP with Student Forcing exact-v1](https://arxiv.org/html/2602.06019v1) §3–4/§5.1–5.5与A1。2+2+2=6，具体standalone块内student-prefix训练缺口深入；跨块真实prefix，Eq3非完整KL期望，4GH200/100Ksteps与Qwen模板配置/质量牺牲保留，不采chunkfactor=walltime或lossless。root必要源/owner写前通过，正文/邻接与末注root实际非作者POST通过，未复现。

- `SF-2026-ARXIV-2601-05524` — Daily `2026-01-13`；[Double exact-v1](https://arxiv.org/html/2601.05524v1) §2.2/4.2–4.3/D.2。只采用双侧检索与overlap下proposal、同路径已验证guidance和commit分层；随机拒绝使suffix失效。causal mask宣称及EM accuracy不单独证明token-law，不继承全局lossless；未运行代码。root必要原源/当前owner写前通过，root实际新增正文/前后邻接及末注写后复核通过。

- `SF-2026-ARXIV-2603-03251`：[exact-v1](https://arxiv.org/html/2603.03251v1) §3/Alg1/Theorem7、§4.1–4.3/Theorems12/15/17、§5–6、Appendix B.1–B.3；采用 accepted-length+bonus cache、changed-q residual 及 batch-miss backup 成本边界。geometric fan-out 推导有 acceptance/power-law 假设，backup 阈值以整批等待和两种 draft 成本为条件，不是所有 scheduler 的最优保证。BF16、单机 H100、target TP4/SSD 另1 draft GPU；Llama70B/1B和Qwen32B/0.6B，四数据集各128 prompts、512 decode tokens，默认 greedy/batch1，计时排除 Prefill。高 batch 多 draft GPU 图为预测而非实测扩规模；mask/fragmented KV extend 位于 critical path，性能重复/不确定性及生产 SLO 未完整披露。作者必要正文审阅完成；root 已实际对读必要原文、两段与邻接，非作者 POST 通过，未本地复现或实现复验。

- `SF-2026-ARXIV-2604-09557`（Experimental）：[SPEED-Bench v1](https://arxiv.org/html/2604.09557v1) §6–8.4/Table1及配置。采用语义流量→proposal可预测性→接受长度/容量的测量边界；词表剪枝损害draft覆盖不等exact target输出质量下降。不同模型、B200/多卡、采样例外、padding和client成本不合并外推。apr01必要源→实际owner采用通过；真实正文及相邻衔接已由apr01非作者实际写后通过，未复现实验。

- `SF-2026-ARXIV-2604-10152`，Experimental：[exact-v1](https://arxiv.org/html/2604.10152v1) §III–VI。采用self-borrow resident target experts、proposal-only affinity及verification hot-set更新；保留expert-union/loading成本、greedy/sampling配置区分、更多N与小batch反例，不推免费驻留或任意sampling exactness。apr02必要来源→实际owner及真实正文/相邻衔接写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-14885` — [RACER v1](https://arxiv.org/html/2604.14885v1)，Daily `2026-04-17`。采用 §3.1–3.3 与 Table 1 的历史 logits / 有界 n-gram proposal 状态分支；保留 target verification 权限、容量/重建成本及 greedy batch-1 反例边界。单篇必要原文/owner 独立 PASS 复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §4；root已重开必要v1/实际正文及两侧交接写后独立PASS，真实整合；Ch48锁释放。

- `SF-2026-ARXIV-2604-13519`（Status: Experimental）：官方 exact-v1 §4.1–4.3/§5/§6.1/AppB.2；schema FSM 与 free-value 检索均只产生 target 验证的 draft。2×A100-PCIE40GB/PyTorch2.5.1/CUDA12.4、batch1与 fp16 质量边界不能外推 concurrency/SLO 或实测全分布等价；实际两段置于 Agent block-hint→read-only tool speculation 之间，待非作者写后核。https://arxiv.org/html/2604.13519v1

- [2604.04987v1](https://arxiv.org/html/2604.04987v1)，Theoretical / Experimental；§2–3、Theorem3。条件h与最终h_alg不同，Γ无闭式、实用KL Taylor近似；acceptance length不等于wall-time或事实质量，保留严格target-law分支。
- `SF-2026-ARXIV-2604-15672`（Theoretical / Experimental）：[exact-v1](https://arxiv.org/html/2604.15672v1) §3 Algorithm 1、§3.1–3.3、§4。采用多粒子未提交祖先状态→target 批量评分/重采→终点单输出的近似 law 分支；Theorem 3.1 仅 iid proposal、`p≪q`、四阶矩下的单轮界，`BN(K+1)≤R` roofline、metadata 成本及 3pp/10pp/15% 不同质量容差保留。单 H100/Llama/Qwen、draft 不 matched 及 SSD 多一张 GPU，不能推同预算普遍 SLO；root 写前及真实正文/相邻交接的非作者写后核验通过，未复现实验。
- [2604.05417v1](https://arxiv.org/html/2604.05417v1)，Theoretical / Experimental；§2.3、§3–4、H.1–H.2。采用每round单drafter及alignment-feedback边界；stationary/i.i.d. regret不能外推生产SLO，switch成本含missing-KV重算，query间reset与query内漂移处理分开。

- `SF-2026-ARXIV-2609-27396`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.27396v1) §3.1–3.3 给出 multi-anchor backbone、独立 acceptance-boundary 分支、verifier 后 bonus-conditioned AR head；§4 与附录 A–D 给出 Qwen3-8B/14B、H800 主实验、batch/采样/异构设备条件与 fallback 分解。它只消除因预猜验证结果错误而产生的 backbone fallback，不保证分支预计算免费、所有 batch/SLO 加速或实现已由第三方复现。

- `SF-2026-ARXIV-2605-07698`（Status: Theoretical / Experimental）：[exact-v1](https://arxiv.org/html/2605.07698v1) 支持 future-validity、Doob transform、TV bound 与受限 grammar 实验；一般 CFG 的 exact validity 为 #P-hard，近似函数不自动保持目标条件分布。

- **Ceiling-Clipped Acceptance Histograms — Experimental**：[exact-v1](https://arxiv.org/html/2608.30427v1)§3、§4.1、§5.5、§7.2仅支持接受长度的上限删失、双向horizon改变与重测职责。anchor和proposal计数、EOS过滤、近似相同均值与浮点tie须分开；正文不采用附录A6的普遍保证、硬件条件不明的加速或无条件exactness。

- ReTrace（Status: Experimental）：[exact-v1 PDF](https://arxiv.org/pdf/2608.29748v1)第3–6页支持上一轮verification辅助特征参与下一轮draft、位置对齐与有限轮次状态的设计；正文只吸收proposal条件与target提交状态分离。Dense/low-rank实验不互相替代，不据此主张可以复用错误prefix KV或任意并发下都加速。

- `SF-2026-ARXIV-2602-05145`（TIDE；Status: Experimental）：exact-v1 的 §3.1 定义从 target serving
  hidden states 复用训练信号、解耦 inference/training 及 runtime activation gate；§A.4 披露 heterogeneous GPU
  evaluation configuration；§6 不证明线上训练在任意 workload、隐私边界或 GPU 配置下都值得启用。
  https://arxiv.org/html/2602.05145v1
- `SF-2026-ARXIV-2602-06932`（Aurora；Status: Experimental）：exact-v1 的 §3.1 定义 dedicated
  asynchronous training server、on-policy serving traces、GPU-aware RPC 与 draft synchronization；Evaluation=
  `Not Disclosed — exact-v1 packet 未提供独立 Evaluation locator`；§7 不证明持续更新可避免 domain shift、
  revision staleness 或生产 rollback 风险。https://arxiv.org/html/2602.06932v1

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

- `2026-05-05 / SF-COMPONENT-AWARE-SELF-SPECULATION` — exact-v1 `arXiv:2605.01106v1`；正文只吸收 component topology 与多状态原子 rollback 的设计约束，不把组件存在写成可用 draft path 的充分条件。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22840` — primary `arXiv:2606.22840v1`; Method=`arXiv:2606.22840v1 — §2.2 LLM Cascade and Routing; §3 System Design; §3.1 Architecture Overview`; Evaluation=`arXiv:2606.22840v1 — §4 Evaluation; §4.6 Extended Engineering Benchmark; §4.7 Case Study: Cost Inversion on mteb-retrieve`; non-proof=`arXiv:2606.22840v1 — §6 Discussion; §6.4 Cross-Provider Failure Modes; §7 Conclusion`; fallback=该 family 的 failure pressure 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 披露的 evaluation signal 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24957: `arXiv:2606.24957v1`; exact-v1 URL=`https://arxiv.org/html/2606.24957v1`; Method=`https://arxiv.org/html/2606.24957v1 — §3 Observation; 4 Dustin Sparse Verification`; Evaluation=`https://arxiv.org/html/2606.24957v1 — §5 Experiment; Accuracy and End-to-End Decode Throughput`; Non-proof=`静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25091: `arXiv:2606.25091v1`; exact-v1 URL=`https://arxiv.org/html/2606.25091v1`; Method=`https://arxiv.org/html/2606.25091v1 — §II Background and Setting; III Gain Window`; Evaluation=`https://arxiv.org/html/2606.25091v1 — §III-A/B/C comparisons; IV Pipelining`; Non-proof=`这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25097: `arXiv:2606.25097v1`; exact-v1 URL=`https://arxiv.org/html/2606.25097v1`; Method=`https://arxiv.org/html/2606.25097v1 — §3 Methods; Serving-stack Configuration; TAIS Screen`; Evaluation=`https://arxiv.org/html/2606.25097v1 — §4 Results; E0/E1/E2/E5; B Reproducibility`; Non-proof=`证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

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
- `SF-2026-ARXIV-2607-03333` — Daily `2026-07-07`；primary `arXiv:2607.03333v1`；Books review `books-review:SF-2026-ARXIV-2607-03333`。

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
- `SF-2026-ARXIV-2607.27269` — Daily `2026-07-31`；primary `arXiv:2607.27269v1`；Books review `books-review:SF-2026-ARXIV-2607.27269`。

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

- `SF-2026-ARXIV-2601-09083` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09083v1)，必要原段见本日PRIMARY/EVIDENCE。6分历史RL substring-tree/current-policy verification具体gap深入；同group更新与idle runahead discarded分开。§4.1实际配置不含runahead，4.2模拟非E2E；随机acceptance/residual实现未完整披露，不授distribution guarantee，成本与普通decode退路相邻。root必要源/owner写前通过，root actual正文/邻接与末注POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2601-09212` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09212v1)。6分 position-decaying relaxed acceptance/residual 具体差额深入；Theorem2/Proposition1 与 Appendix F 条件、COCO/config/质量反侧已由 root 必要原源与 owner 写前复核通过。固定接受函数下的上界最小化不授整序列全局最优，平均 TV 不授 every-prefix 条件，late ω<1 不自动满足经典规则下界。正文两段保留有损合同、完整成本与 exact fallback；root 非作者实际正文/邻接与末注 POST 通过，窄锁释放，未运行实现或复现。

- `SF-2026-ARXIV-2602-15318` — Daily `2026-02-19`；[Sparrow exact-v1](https://arxiv.org/html/2602.15318v1) §2–4/Table2/5/6、§6。2+2+2=6，训练visual bridge/递归MTP与推理text-hidden分离差额深入；Table6 Qwen2.5VL7B/A800长序列恢复不授全部长度胜出，短3.82→3.79反侧保留。Table2 LLaVA7B/L20四video任务temp0 DSR2.82/ESR1.93，prefill与feature接口成本近正文，不授lossless实现已核、全任务质量/并发SLO。root必要源/实际48及47/49邻接PRE通过并授窄锁；root已实际核两段正文、完整邻接及末注，非作者POST通过，窄锁释放；未核代码或复现，未授日级Gate。

- `SF-2026-ARXIV-2602-16052` — Daily `2026-02-20`；[MoE-Spec exact-v1](https://arxiv.org/html/2602.16052v1) §3.1–3.3、§4、§6 与 Appendix A–C 必要预算/实现反侧。正文区分等权 tree-wide budget 的 truncation/substitution 与原 target exactness，并与已有 position-weighted selector 连续比较；质量容忍度、q=1 偏差、选择成本和 oracle 非部署性保留。root 非作者 PRE 与实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，不授日级完成。

- `SF-2026-ARXIV-2602-12957` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12957v1) 必要方法、关键评价与直接限制；2+1+2=5，实际 owner 差额定点深入。只采用正文条件机制与明确有限适用范围，不授随机采样 exactness、全页质量或全流程加速保证；root 必要原源/actual owner PRE 通过并授窄锁，作者正文/完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16961` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16961v1) §3–6、AppendixC/D必要证明与Eq27–29；2+2+2=6，选中IID路径分布差额/中心tie反側深入；不授greedy全局最优、ties未统一全域exact recipe或更长接受必更快；反侧、额外成本与原方案回退近正文。root必要原源/actual owner PRE通过；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及末注POST通过，窄锁释放；未核实现/复现，非日级验收。
