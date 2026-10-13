# Qwen3-Next必要标准审阅与Books差额

作者Meitner。精确材料为官方research item `qwen3-next`及其tokenLinks指向[正文JSON](https://docs.qwenlm.ai/research/qwen3-next/index.json)，不是搜索摘要。本日[API原件](SUP_QWEN_20261012.raw)、[正文原件](SUP_QWEN_NEXT_BODY_20261012.raw)与对应request支持身份/date/披露范围。官方ISO Sep10T20Z归属Sep11 BJT；拟分2+2+1=5，不改变旧候选或日期。

## 实际读层与采用

实际读Introduction、Key Features四项、Pretraining/Posttraining核心文字、Agentic Use、Develop with Qwen3中Transformers/SGLang/vLLM的文字说明和Note、Ultra-Long Texts、Summary。AST顶层198tokens，方法/评价核心10–104、部署文字105–166、长文本/结语167–197。图表仅metadata不冒充像素已读；外置代码、模型权重、engine实现及参考论文未核，不宣称artifact/复现/production验收。

纯linear attention有召回弱点而full attention有长序列成本。本版本75% Gated DeltaNet与25% gated attention（3:1）混合，后者SDPA输出门控，不把两种gate当同一memory update。head dimension由128到256、RoPE仅前25%维是具体配置，不是普适最优。Zero-Centered RMSNorm、对norm weights施weight decay及归一化router初始化处理训练波动/初始选择偏置；没有独立消融，不推出所有sink消失或最终路由公平。

MoE为512 experts，10 routed+1 shared，相比Qwen3的128/8提高稀疏容量；80B total/A3B的3.7% activated是模型事实，不等于memory/communication/端到端成本同比下降。native MTP增加multi-step训练以贴近推理，公开接受率目标不替full target verification或cache提交正确性证明。RL稳定性问题被官方声称解决，但独立算法/控制实验细节Not Disclosed，不采用解决一切hybrid+sparse RL的命题。

## 对照、成本与反侧

官方15T是Qwen3 36T的统一子集；9.3% Qwen3-32B训练compute及相对30B-A3B预算/性能是整体recipe结果，模型容量、数据量和架构共同变化，不能隔离单机制因果。4K prefill约7x/decode约4x、32K约10x只是官方报告，hardware、precision、batch、concurrency、SLO、重复运行/不确定性和完整端到端协议Not Disclosed。任务benchmark与RULER仅保留作者局部报告，不采榜单数字为普遍同质量或长检索保证。

明确反侧已实际读：官方说throughput高度依赖实现；Transformers并非一般可用MTP，SGLang/vLLM建议main支持不证明任意release已支持。默认256K若server无法启动建议减到32768，不把最大长度当给定硬件的容量保证。native262144、static YaRN扩长可影响短文本，固定factor不随请求适配，仅在必要长输入时考虑；不默认1M对所有任务无损。未读外置命令，因此只采用官方文字披露，不绑定未经核验的参数或版本。

## Books具体比较与处置提案

按ROADMAP实际定位并读具体正文：`MODEL-LONG-CONTEXT` [Ch22](../../../../../books/part-02-model/22-long-context.md)510–552已解释GDN的decay/方向重写、固定状态碰撞、chunk执行和attention互补；885–923已区分softmax output gate与memory gate、不能取消dense KV且可混合。`MODEL-MOE` [Ch21](../../../../../books/part-02-model/21-moe.md)112–140及655–704已解释activated compute不等runtime、均衡不保证语义公平、joint conditional population及初始化/校准分支。`INFER-SPECULATIVE-DECODING` [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)515–545已解释native MTP的架构绑定与full verification仍必要。

**仅报告提案，不称Qwen3-Next已被书稿覆盖。** 书中没有本版本3:1/512/10+1/Zero-Centered配置；它们是真实版本recipe，但本材料没有受控对照足以改变比例选择或norm/router处理的长期适用条件。现有上述论点承载可采用的稳定机制边界；新的版本参数与未披露RL细节留报告，不制造长期法则或用主题相似授已有覆盖。不缺owner，无已确认需写入的长期gap，当前无共享Books写请求。若独核发现明确新稳定条件，定点重开该差额并先root协调，而非把未读改外部hold。

评分/Evidence/Books均交Cicero实际审，不自授本日完成。
