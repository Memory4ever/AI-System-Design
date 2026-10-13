# 四项具体 owner 差额逐字提案（Source/PRE 待核，未获锁未写）

必要证据与反側为 SUP_EVIDENCE_SIX，reader Source独核之前不写。本轮已完整重读背景/哲学/写作、ROADMAP/LS；各具体owner/邻接比较实际材料位置在该notes。以下每项独立判，不因材料可映射owner强行造缺口；若实际现文已充分承载则收回新增并写已有覆盖。

## LMetric — INFER-SCHEDULING Ch56

置于465节中路由/placement/autoscale分权段之后、「全局Routing需要延迟模型」前。Ch55阶段匹配/goodput与Ch57平台开篇交接已读。

同质、Prefill/Decode 共驻的副本池中，路由还可用一个简单乘积把 prefix 复用与当前负载联动。令 `P` 为候选副本需要新算的 prompt tokens 加已排队的 Prefill tokens，`B` 为其等待和运行中的请求数，选择较小 `P×B`，使少算 Prefill 只有在 Decode 负担也合适时才成为优势。这是两个代理量的组合，不是精确新增请求延迟，也不替代 endpoint admission；异构模型、独立 P/D 池或形状差异明显时，下面的显式延迟模型仍有必要。

乘积仍会被热门 prefix 的小 `P` 吸向热点。若某类请求占比为 `x`，持有它的副本为 `M`，其余副本为 `Mbar`，`x/(1−x)>|M|/|Mbar|` 表示该类流量相对可承载副本过密；这只是简化流量模型的危险条件，不是稳定性定理。可先以短窗口发现高命中类，再在首警报后观察这些副本仍被连续选择且 multiplicative score 继续偏小，才将它们暂时排除，但新增窗口、门槛和指标延迟都要验收。[同质 co-located 对照](https://arxiv.org/html/2603.15202v1)中也有平均 TTFT 退步，故 proxy 漂移、热点未受控或 SLO 不达标时，应回退已校准的负载阈值或延迟预测策略，不能把少调权重写成无参数、无条件的最优路由。<!-- source-family:SF-2026-ARXIV-2603-15202 -->

## DOS — MULTIMODAL-GENERATIVE-PARADIGMS Ch24

置于当前519之前的attention列和影响两个段之后、positiontemperature段之前；实际465–519/691–706、Ch23和Ch25开篇交接已读。

影响排序还有一个不同的方向：不是问候选位置会影响多少其它位置，而是问该 masked query 的 attention 有多少流向**已经观测到的** token。对选定层的各 head 取平均，再对 observed columns 求 row mass，可优先揭示当前更依赖已知 context 的位置；content predictor 仍决定填什么，另一个熵约束可决定同轮提交几项。这只是可计算的依赖代理，不证明因果结构或精确 joint distribution。[受测解码对照](https://arxiv.org/html/2603.15340v1)仍有任务反退、按任务选择层的成本，以及更低 NFE 的其它基线；矩阵提取和排序也可能增加访存，不能由同一 forward 次数推出真实加速。代理、层选择或完整质量/费用不成立时，保留 confidence、固定小块或逐位置提交。<!-- source-family:SF-2026-ARXIV-2603-15340 -->

## DUET — INFER-PD-DISAGGREGATION Ch55

置于「两种阶段，两种节奏」Decode段之后、co-location干扰段前，Ch54 memory与Ch56 scheduling交接已读。

阶段拆分还可以深入计算数据流，而不只是把同样的 GPU 分成两池：Prefill 的大矩阵可使用 systolic array，包含 SSM 的模型还须安排局部 recurrent state 的保留与递推；小 batch Decode 则可能更适合 vector reduction、局部状态与更高内存带宽。这样用阶段专用计算换取更多硬件类型、封装和 KV/state handoff 耦合，不取消两池排队和资源匹配责任。[受限硬件设计](https://arxiv.org/html/2603.15530v1)的收益来自 RTL/周期仿真，计算峰值与内存配置也不等同 GPU 对照，并假设两池吞吐匹配而未模拟多请求调度；不能据此授生产 SLO 或将全部差距归给数据流。专用硬件不可得、handoff 或突发负载抵消收益时，同构 GPU 分池或原共驻路径仍是合理基线。<!-- source-family:SF-2026-ARXIV-2603-15530 -->

## LEXI — INFER-GPU-MEMORY Ch54

置于「减少Bytes」首句后，现703–709 losslessweights/GEMMtiling与Ch55 102–119 exponentKV transfer近邻实读；Ch53开篇/Ch55基础交接已读。仅运行期tensor wire编码/算术精度分离，不复制PDtransfer协议。

减少传输 bytes 也不必改变算术精度。对 BF16 tensor，可以原样保留 sign 与 mantissa，只对指数做 prefix-free 编码：固定权重可离线准备，运行中的 activation、KV 或 SSM state 则需按 layer 收集指数统计，随压缩流携带 codebook，并在计算前还原同一 BF16 数值。Bit-exact 描述解码后的数值身份，不表示 tensor 在每个内存层都采用相同物理格式，更不自动证明在线 codec 没有额外延迟。

在线编码把瓶颈移向启动、变长 packetization 和多 lane 解码。有限 codebook 对未见指数必须提供可恢复的 escape/raw 路径；稀有值变多时传输可能膨胀，短 payload 也难以摊薄 header 与统计成本。[指数编码原型](https://arxiv.org/html/2603.15589v1)的芯片面积来自 synthesis，端到端收益来自通信占主导的 chiplet 仿真，不是通用 GPU serving 测量。因此应绑定 dtype、codebook、escape、shape 和链路验收完整 encode/transfer/decode 成本；解码身份不符、entropy 变化或净收益不足时，回退未压缩 tensor，而不是把无损数值当作免费带宽。<!-- source-family:SF-2026-ARXIV-2603-15589 -->
