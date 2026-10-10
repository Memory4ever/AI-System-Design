# 03-10增量首批准入校准

旧1家族IH与原评分/日期/连续§4被冻结。以下只用精确v1完整题摘判断潜力，尚未证首次公开日，不是确定候选，也未评分或深审。

| v1身份 | 原约束→原文实际增量→潜在选择 | 状态 |
| --- | --- | --- |
| [2603.07416 DualSpec](https://arxiv.org/abs/2603.07416v1) | 统一action speculation+严格action匹配→Search/Visit不同entropy与capacity需求、confidence semantic verifier→按动作类型选推测和验证；性能可信度另核 | 日期潜力 |
| [2603.07887 Reject Resample Repeat](https://arxiv.org/abs/2603.07887v1) | 多轨迹采样正确率/成本缺解释→SMC非渐近条件/下界及sampling error不预测最终accuracy→不能把目标分布贴近当解题提升 | 日期潜力，理论/负面不关闭 |
| [2603.08412 Aligning to Illusions](https://arxiv.org/abs/2603.08412v1) | 偏好标签/成对accuracy默认稳定有效→人工choice blindness、judge匹配依赖和label corruption下pairwise不变但BoN退化→偏好信号构造/评估需拆开 | 日期潜力，安全/设计反证 |
| [2603.07482 Stream Independence](https://arxiv.org/abs/2603.07482v1) | token/semantics早混合使head干预纠缠→两独立stream到output才融合及干预/过约束collapse→architecture解释/表达代价；不凭小模型关闭 | 日期潜力 |
| [2603.08068 ICRL](https://arxiv.org/abs/2603.08068v1) | tool coldstart依赖SFT→RL rollout fewshot辅助后逐减至zero→可替代coldstart；需核训练budget/对照，不把recipe先授普遍性 | 日期潜力 |
| [2603.07540 UniLongGen](https://arxiv.org/abs/2603.07540v1) | 长interleaved生成失效仅当token长度问题→visual event污染与internal relevance剪历史→按事件保safe conditioning而非全历史 | 日期潜力 |
| [2603.08391 Adaptive Loops Memory](https://arxiv.org/abs/2603.08391v1) | 重复层参数节省牺牲storage→learned halting+gated memory分账math/common sense、iso-FLOP对照→compute depth/storage分离 | 日期潜力，后续v3仅轻量状态线索 |
| [2603.07169 CUDAMaster](https://arxiv.org/abs/2603.07169v1) | ML-only kernel评测外推→multi-scenario FP32/BF16 benchmark、hardware/profile toolchain→潜在评价负载与优化决策变化，若只是组合需定点core核准入 | 日期/准入含糊，非因预算不明关闭 |
| [2603.07810 Temperature Scheduling](https://arxiv.org/abs/2603.07810v1) | location-independent cooling效率→temperature-aware energy/carbon/TTFT/water共优化→跨地负载选择，贡献不是仅ADMM术语 | 日期潜力；需核本模型及可执行约束 |
| [2603.07770 ArcLight](https://arxiv.org/abs/2603.07770v1) | CPU框架忽略NUMA远端access→细粒TP/内存thread schedule→NUMA分区执行选择 | 日期潜力，具体机制可信度待证 |
| [2603.08026 DyLLM](https://arxiv.org/abs/2603.08026v1) | dLLM每步全序列重复算→相邻attention context余弦判saliency及partial attention/FFN复用→不同于仅step减少 | 日期潜力 |
| [2603.08343 Hadamard Output](https://arxiv.org/abs/2603.08343v1) | dense output quadratic→fixed orthogonal crosshead混合+affine→learnable dense mixer与resource取舍 | 日期潜力 |
| [2603.07700 TDM-R1](https://arxiv.org/abs/2603.07700v1) | fewstep deterministic生成依赖diff reward→surrogate learning与generator拆开/per-stepreward→non-diff监督可行边界 | 日期潜力 |
| [2603.08706 ACT](https://arxiv.org/abs/2603.08706v1) | imitation reflection无法自行判断action质量→correct comparative judgment RL→critical判断和后训练组成，非只reflection文本 | 日期潜力 |
| [2603.08761 Formal Limits v1](https://arxiv.org/abs/2603.08761v1) | cert sound/generic/tractable并存→声称复杂性/行为不可辨识/有限证据三barrier→potential受限认证；理论正确性不在题摘层认证 | 日期潜力，理论安全约束深入需确认后再触发 |

代表EX先复用本日有效独立core：IH同事件重复；New ways to learn math and science仅交互概念/早期反馈无model机制；AbstractionFallacy意识本体论未给模型形成/系统选择可验证增量；CHMv2暂缓科学应用、不以DINO owner绕回。
新题摘的明确范围EX（API full abstract已读）：08593 GPU-accelerated DECam astronomy pipeline、07764 GANRA非线性NRA solver，机制服务天文/SMT领域而未建立foundation训练/推理机制，前者按AIforScience暂缓，后者仅LLM+GPU求解应用。07764的SMT执行新算法本身有价值，不用title标签贬低或推它没有算法。

这些不是候选总数或全文审阅数，后续只对本次实际有贡献潜力/含糊题摘补必要日期；未处理同query分页继续。
