# 2603.10335v1 Fuel Gauge：必要 Source / actual owner / PRE

窗2026-03-12 BJT。第二包完整题摘/本arxiv事件日级日期有效复用，不重开。`SUP_CORE_10335.raw` GET200，2026-10-09T13:18:01Z，精确v1；作者实际读§4全部（两假设、Alg1、Eq2/3、训练）、§5全部、§6全部 Tables1–4、Appendix A完整训练设置、D完整开销。只读B/C相关开头/标题不授全附件。官方精确v1 PDF已直接打开核页6/7图注/表字段，截图两种入口都cache/internal失败，未声称视觉读图；以下采用表和文字机制，不采用图像精确点值。

## 方法、实现与反侧

训练标签是已结束trace的归一化位置 `1-i/N`，200个MMLU/MMMU问题，单层最近8步hidden→depthwise/pointwise conv→2层MLP；累积估计读数，固定intercept1拟合斜率，`Nhat=-1/k`。因此是**生成进行中的监督进度proxy**，不是只看prompt已知这次随机采样N，更不是证明存在原生能量变量。HypothesisII中 `i>j` 又写 `r_i>r_j` 与递减叙述反向；单调本身也不推出线性。主文“jointly训练”与AppA“both independently”口径未闭合，窗口描述8与 `h_{i-8:i}` 索引资格也保留；不认证精确复现recipe。

§5.1只描述按预测长度预分配、不够时更新再扩；没有完整paged allocator/block-map、过度预留、回收或多租户admission接口。不能把PagedAttention的非连续物理页逻辑称为需要大连续区域的一般碎片问题；保留原按实际页增长的合理基线。

§5.2 Eq4是到目标fuel读数的绝对误差J，Eq5沿正/负归一化∂J更新；正eta一定增fuel不由公式普遍推出（∂J含sign(f-r_target)），稿中未给统一r_target执行配置。因此PRE不采用这个确定方向的steering recipe，也不将干预读数/长度变化证明原生fuel或sample-independent N。

## 关键评价/系统资格

- 单A6000、PyTorch2.8，text Transformers4.53.2 vs多模态4.57.0；Qwen3-4/8B、Qwen3VL2/4B，首200 MMLU/MMMU训练，GPQA/MathVision/LongVideoBench外任务。主实验5seed、AIME10seed，未以无重复否定结果。
- Table1 GPQA8B rMAE .2732 vsDirect .5795，video .4527等支持该数据/模型的进度预测；Eq6跨**全部步骤**的ratio不是初始几个token或尾部分位准确率。未提供underprediction尾概率/可行容量签证，不能据全程均值授开头准确reserve。
- Table3 #Allocs GPQA8B HF533→39.87（13.37×），image4B544→59.10，video4B60s43.62→27.81（1.569×）；基线作者指定HF16-token增长。它测调用次数，不测真实fragmentation bytes/OOM、峰值reservation、并发throughput或端到端SLO，不能搬成通用vLLM收益。
- Table4是**绝对Pearson** .95–.99；有限eta/model/task扫描关联不是跨任务统一正方向或任意target accuracy可控。不把图注linearity作普遍保证。
- TableS7独立predictor batch1 792.7token/s、batch32 11217.3 vsbase22.4，82.24k参数；不含实机hook/fit同步、KV重分配、backprop modulation联合路径。不能直接以独立吞吐比认证端到端零开销。

## 唯一 owner 与实际差额

ROADMAP `INFER-SCHEDULING` [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) 为唯一owner：此处不是减少KV字节，而是新进度估计信号怎样成为forecast/实况的接口。作者实际读当前Ch56 100–175完整“当前能放下/分布预测/Future-state Reservation”及246–265 hidden quality scorer完整分支；Ch54开头/容量与fragmentation接口、Ch55开头PD消费边界也实际读。

现Ch56 105–116已约束预测/未来增长/校准margin，124–128为per-class reservation，259–261以hidden-state **最终正确弱标签**取消并行trace。这些不含最近hidden→已完成trace进度标签→在线外推的**长度sensor**，不能把质量scorer当长度sensor。差额是信号身份与预测是否足以支付物理reservation的具体交接；成熟回退/margin原则本身不另计贡献。Ch54只handoff实际页/bytes，不再另写owner。

影响2 + 冲击1 + 长期2 = 5。必要系统/理论边界深入已读完；提案仅整合下列受限估计接口，不采用原生fuel、通用碎片/13.37×端到端或确定steering保证。待独核PRE及root裁，不先formal候选/Books。

## 逐字两段 PRE（建议插Ch56点估计/分布SJF段之后、树式decode之前）

入队时的长度预测还可在 Decode 进行中由进度信号更新：对已有完整轨迹用归一化token位置训练轻量hidden-state读数，再从当前读数序列外推结束位置，给出带request、model/layer、训练人口与生成策略身份的长度proposal。它使用已经生成的状态，不是只看prompt就知道这次随机采样的终点；监督为线性进度也不证明模型内部有原生“fuel”。调度器可据更新后的proposal调整未来KV reservation，但实际已占页、扩容/回收与硬cap仍由runtime确认；斜率不稳定、读数越界、生成策略或模型改变时，应停止外推，回到实际页增长、保守reserve与既有抢占/拒绝路径。

[Fuel Gauge的有限方法与评价](https://arxiv.org/html/2603.10335v1)支持这个在线长度sensor分支，但其跨全部生成步骤的平均预测误差和HF小块基线的allocation次数，不等初始时刻的尾部校准、真实碎片/OOM、并发容量或生产SLO。较大reservation可能减少重分配却挤占其他请求，hidden读取、拟合、同步与扩容也都有费用，应在同一allocator和质量/并发人口上验收预测与实况、浪费与underprediction。稿中另一个隐藏态steering分支改变生成过程，不能与被预测的原轨迹混作同一收益分母；方向/目标及联合开销尚未闭合时，保留不干预生成、普通paged增长的基线，不以独立predictor吞吐宣称端到端免费。

若owner认为实际已有该长度sensor资格或差额不重要，应明确No Change并回对具体正文，不为5分自动写书；当前PRE只是作者提案。
