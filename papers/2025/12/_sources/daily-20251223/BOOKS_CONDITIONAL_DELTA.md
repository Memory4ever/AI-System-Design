# 12/23 条件知识差额，不是本窗写入请求

Owner：`TRAIN-RLHF`，[Ch31](../../../../../books/part-04-training-system/31-rlhf.md)。已实际对读owner“Sequence reward 与 token updates 的错位”和相邻Ch30/32开头；当前Ch31承载proxy reward、checked span/完整行为区分，以及Numerical Execution Identity。现有scalar reward→token advantage段明确GRPO为同prompt组内reward，尚不承载**故意令生成与训练prompt不同而reward不变**的干预。既有代理评价原则是部分覆盖，不是整项新增训练干预已覆盖。

精确证据：[2512.19027v1](https://arxiv.org/html/2512.19027v1)，§3.1/3.2干预与ratio，§4.3无关prompt也有效及ratio-rescale对照，§E.2 off-policy/clipping分析，§5.1 instruction-follow回退与扩展限制。实际必要局部均读，三seed/Llama3.1-8B/lie-detector及模拟任务限制见[正文记录](NECESSARY_ADMISSION.md)。不是所有prompt语义变化都有效，更不是reward不变即可安全。

**日期仍隔离，不请求当前Books写入，不把此条件提案当整合待办或已整合。**若该精确事件官方firstpublic证明完全落窗，先请root准入/Evidence校准，再决定是否落到以下局部替换，不另建机制owner：

> 标准RL让rollout与training使用相同prompt，使policy ratio对应同一条件分布；这是避免off-policy偏移的合理默认。若一个固定但误设的reward持续强化不希望的行为，受限实验提出另一分支：在抑制该行为的prompt下生成输出，却在更宽松的prompt下训练同一输出，不修改reward。此时必须分别绑定generation/train prompt与logprob身份，不能沿用“同prompt on-policy”的解释。GRPO ratio与clipping对正负advantage可能产生不对称regularization；无关prompt也有效，说明收益不能全归于安全语义。增加prompt组合、独立行为/能力评价与指令遵循检查会增加成本，frontier/长上下文/真实风险尚未验证。效果或instruction-follow下降时，回退标准同prompt更新、可信reward修正和保守KL，而不把重上下文当安全保证。

拟位置：Ch31同prompt scalar→token更新段后、multi-agent credit段前。ratio/clipping算法细节仍由Ch32/33承载，Ch31只拥有训练目标/干预与边界，不复制算法教程。新原始日期或反证到达仅重开本项。
