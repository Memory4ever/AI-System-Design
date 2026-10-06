# 决定准入的最小追加原源读取

原源：https://arxiv.org/html/2602.17634v1 ，actual §4.3/Tables4–7与§5起始；以下是定位与判断摘要，不冒充原始全文。

Table4以8层/width128、较小训练集比较sequence mixers，参数2.0M–3.1M并不相同；DeltaNet long/short/overall MASE=.706/.792/.732，Conv+DeltaNet=.700/.786/.725，GatedDeltaNet=.708/.782/.730而Conv+GatedDeltaNet=.704/.784/.728（short反向）。Table5 decoder attention相对bilinear更好，但仅Gift-Eval相同尺寸的forecast结果。Table6 leave-one-augmentation-out几乎不变，去全部或synthetic更差。Table7 downsample改善long而short不变；flip-once/every overall四舍五入同.722。§5明确把LLM已成功hybrid组合迁移到univariate TSFM，跨channel仅future work。

拟贡献前EX理由：并非primitives成熟即排除；当前新增证据仍是固定forecast协议下recipe/Pareto，未给出改变通用hybrid机制选择的可比训练/执行预算条件、可推广的state-memory失效边界或新更新接口。以上局部短/长指标不能推Transformer或hybrid普遍必要性。只决定准入一次追加，不展开完整TS实验、附录或其他版本；待root独立校准。
