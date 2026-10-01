# 2026-04-24 四项执行与策略候选的有限非作者核

复核者 root。以下只核四个官方 exact-v1 的必要原文、当前 owner 和处置边界；正式报告仍未通过整日来源、日期、否定侧及其余候选 Gate。arXiv submitted 不单独证明本窗公开。

## `2604.20930v1` SafeRedirect：仅报告

[官方 §3–4、Limitations](https://arxiv.org/html/2604.20930v1)给“validator 要求有害字段才算完成”的任务明确失败许可、固定拒答与保留 placeholder。这是模型收到的 system prompt 替代行动，不是执行器 hard stop 或外部 policy。三类 AI/ML 工具任务、七模型、单轮试验中，unsafe 仅指成功抽取且被一个 judge 判最高有害的输出；剩余输出并未全部获得安全证明，部分模型仍有失效。第72章 `PLATFORM-SECURITY` 已把 prompt 意图和强制执行/残余风险分开，未见必须改写的长期机制。维持 2+2+2=6、深入审阅、仅报告；若应用把 prompt 直接当授权门，另以真实 runtime gate 验收，不能引用本试验签发。

## `2604.21026v1` MCAP：受限排序证据，仅报告

[官方 §3.1–3.5、§4.8、Limitations](https://arxiv.org/html/2604.21026v1)以 Q/V 与 FFN activation norm 对 layer 排序，供部署时精度和驻留决策；给定 iid/sub-Gaussian 等假设的 top-k 恢复界只涉及排序。它不保证量化或跳层后的任务质量。论文的全层 paging 与 hot-only skip 不是同质量策略，1/3/8B Llama、T4/A10G、单 GPU batch1、W4A8/W4A16 的吞吐不能外推并发或任意边缘设备。第49章 `INFER-EXECUTION` 与第54章内存约束已有 artifact/精度/容量分账；该具体评分器尚不改变原则，维持 2+1+2=5、标准审阅、仅报告。若真实 workload 上提供独立质量与端到端 SLO 对照，再重判准入价值。

## `2604.20932v1` Adaptive RAG Defense：动态控制不等通用安全

[官方 §4–6](https://arxiv.org/html/2604.20932v1)让 sentinel 观察 query/retrieval，再由 strategist 选 pre/post 检测 hook；作者对一个小型 RAG 管线测多种攻击。其 membership 指标是 exact mask-fill，不能等同推断优势；content leakage 未做同等实证，静态/动态评估协议也不完全同构。第72章已有安全策略 owner、剩余风险与 false-refusal/utility 的交接，动态 hook 只是一种受限方案，不提供普遍优于静态策略或开放世界零 ASR。维持 2+2+2=6、深入审阅、仅报告；实际部署需同攻击、同工作负载和 controller 成本的独立回归。

## `2604.20917v1` DexBench：联合分数不是因果理解证书

[官方 §3–4、Limitations](https://arxiv.org/html/2604.20917v1)把给定输入的 exact statement coverage 预测，与为未覆盖 branch 生成 mutant 输入配成两项可执行测试；联合成功是两个 pass@k 事件的交，不要求同一次模型内部持有共同的因果表示。数据来自有限 Python 基准，代码污染与 branch 选择仍可能影响难度。第66章 `PLATFORM-EVALUATION-SYSTEM` 已有执行 oracle 与语义配对的长期责任；本配对提供新受限 evaluation slice，但不改变“可执行结果不独证内部理解”。维持 2+1+2=5、标准审阅、仅报告。

四项均未写 Books；本文不改变日级状态。
