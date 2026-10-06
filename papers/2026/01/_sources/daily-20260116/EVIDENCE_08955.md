# 2601.08955v1 — adaptive lookahead is a learned control object

[Exact HTML](https://arxiv.org/html/2601.08955v1)，必要原段PRIMARY_08955_NECESSARY.md（§3.1–3.3、4.1、4.3–4.4、Limitations与B.2）。拟2+2+2=6：固定horizon/单步策略→state-conditioned K head与frozen world-model rollout/行动policy联合目标→重新选择规划计算分配；Reach只给policy↔imagined-state生成的实际handoff，不借物理安全泛原则。标准必要源已读，可能具体长期gap则对差额深入，待root实际复核。

World model用expert+真实policy rollout的next-state NLL；初policy先SFT。训练分支ITP_R用teacher-forced expert action在frozen WM中想象，按expert-action log likelihood−λ_K k构造K伪标签，再joint action/K-head warmup；随后A2C joint log p(K)+logπ(a|imagined states)，奖励env−λ_K K−λ_step。伪标签的“optimal”是给定模型/专家路径proxy，不是实际环境最优horizon。ITP_I是冻结policy/WM的prompt选择/反思分支，不能把两分支统一当无训练。Imagined state不是环境事实，模型质量/状态误差可反馈到K选择。

§4.3比较固定K及随机K；固定中等K峰值后下降为局部反侧。NB按policy+WM整个episode token相对K0/Kmax归一化，不是latency、money或训练预算。140 ALFWorld tasks/14fold均值点不是14独立重训seed；ITP_I vs ReAct random、ITP_R vs SFT random仍包含不同controller/训练，不将总收益唯一归因K头。§4.4固定Qwen3 policy换WM，DeepSeekV3.2未接受WM训练，ITP_R政策训练可补偿；不能用此归因模型规模/更差backbone普遍无效。

配置：文本模拟ALFWorld、ScienceWorld的行动机制，不采用科学领域应用结果/真实物理安全。Qwen2.5 7B/Qwen3 8B/Llama8B，正文与table的Llama3/3.1标签不一致，不采用对应精确排行榜。B.2披露fp16 true/bf16 false、LoRA r8/α16/drop.05、global batch16、3epochs、temp.7/topP.9，Kmax5/8及WM输出上限；这些属于该配置不是通用recipe。hardware、完整matched训练/推理总成本及独立重训CI于必要core Not Disclosed；Limitations明确text-only、真实复杂环境/机器人/实时开销未证。

Books准备判断：实际Ch79:68–72 transition只作proposal与384–390预算/horizon一般压力已承载事实边界，但未讲把horizon本身作为学习目标及teacher-forced伪标签→online联合控制。拟唯一owner AGENT-PLANNING，在“学习到的Transition只能验证候选”两段后/Decomposition前加两短段：固定K的合理基线→proxy teacher-label K head/联合动作预算→stale/误差放大与token≠latency/无真实安全保证。不是双ownerCh25；Ch25只handoff。待root必要source/具体gap批准窄锁，无写入，不授当前已有覆盖。未运行代码/实验。

最终收据：root实际§3.1/3.3.1–2、4.3–4.4/limits与当前Ch79 owner/邻接核通过，6分对知识缺口深入；实际Ch79 L75/77两段及L512末注写入，root非作者实际顺读两段/transition前文/Decomposition交接与末注POST通过，窄锁释放。正文仅受限文本模拟分支，不授物理/OOD安全。日级仍进行中。
