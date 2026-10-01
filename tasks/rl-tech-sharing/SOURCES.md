# 来源与论证边界

算法与框架来源核验日期：2026-09-21；S20、S21 于 2026-09-23 核验。迷宫制作时重新查阅 S03 论文摘要、S04 的 4.1 节与 S05 正文。来源编号对应 [逐页讲稿](./TALK.md)。论文支持机制解释，官方文档支持具体实现描述；两者不互相替代。迷宫、四路线简化与数值来自本材料的独立教学实验，不是论文 benchmark；代码省略的机制见 [实验说明](./EXAMPLES.md)。

2026-09-23 对照 Books Part IV 后，重新查阅 InstructGPT v1 的监督/评分器/策略三阶段、DAPO v1 的探索与长度处理、DPO v2 的相对目标，以及 GAE 原论文摘要。新加的路线回报、聚合权重与偏好概率反例为本材料独立计算；Books 章节链接用于继续学习，不替代 primary source。未重新核验框架动态版本，也不扩大此前框架支持范围的声明。

同日核对过 DAPO v1 §3.1～3.4 和 §4.1；为收紧主讲范围，相关动画现已移除，研究机制只保留为附录参考。当前评分器动画只训练一个长度特征权重，DPO 概率变化是数学反例，均不构成真实 LLM 实验。

同日随后为“两道题、各四条回答”的框架对照，重新打开 S11～S15 的官方入口及 S22 的流程文档。补充的是角色交接、分组与 batch 计数、同步/异步的区别；没有核验全部模型支持矩阵、锁定源码 commit 或运行三框架。两组奖励、优势与一次更新的设定由本材料独立构造，不视为框架默认输出。

第 15 页的问题与机制补充另核对 S23，以及 Miles v0.1 §2.2～2.5 和异步文档的 Metrics 部分。0.20/0.12 是概率差异的假设例子；排查步骤是工程建议，不是框架自动诊断能力或性能结论。

2026-09-24 制作第 15 页分步动画时，再核对 S23 的策略比较模式、S13 §2.4～2.5 的 TITO/R3，以及 S22 中 Miles Fully Async 的完整组 buffer、生成槽释放、版本与过滤规则。动画只展示这些机制的受限案例，不扩大为框架功能独占或加速排名；未运行真实框架。异步图固定两批数据：第 1 批 Q1/Q2 各四答，第 2 批 Q3/Q4 各四答；每批完整且符合规则才更新。接受后用于 v8→v9 与拒绝后重采是预设教学结局，不是运行框架算出的质量判定。

## 基础与算法

| 编号 | Primary source | 本材料使用位置与边界 |
| --- | --- | --- |
| S01 | Williams, [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://link.springer.com/article/10.1007/BF00992696), 1992 | REINFORCE 与 likelihood-ratio 思路；核验出版信息及摘要，材料提供可独立复算的有限动作推导，不声称复现论文实验 |
| S02 | [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), 2022 | SFT、偏好 Reward Model、PPO 的典型 RLHF 链；不是所有 RLHF 必须使用的固定流程 |
| S03 | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347), 2017 | clipped surrogate；不把 clipping 解释成硬性信赖域保证 |
| S04 | [DeepSeekMath](https://arxiv.org/html/2402.03300v3), v3 | GRPO、outcome supervision 与组内优势；本材料不采用模型性能数字 |
| S05 | [Direct Preference Optimization](https://arxiv.org/html/2305.18290v2), v2 | 偏好损失、KL 正则目标的重参数化；理论联系不代表与在线 PPO 具有相同训练轨迹 |
| S06 | [Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs](https://arxiv.org/html/2402.14740v2), v2 | RLOO 的 leave-one-out baseline；不是“GRPO 的下一代” |
| S07 | [DAPO](https://arxiv.org/html/2503.14476v1), v1 | 动态采样、clip-higher、token-level loss 与超长奖励处理；具体 recipe 不自动适用于开放任务 |
| S08 | [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/html/2503.20783v1), v1 | Dr. GRPO 对长度与难度相关归一化偏差的讨论；不推出所有归一化都应删除 |
| S09 | [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760), 2022 | 代理奖励过度优化；材料中的错误奖励实验独立设计 |
| S17 | [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438), 2015 | TD residual 与 GAE；语言模型映射和两 token 数值例子为教学整理 |
| S18 | [Group Sequence Policy Optimization](https://arxiv.org/html/2507.18071v2), v2 | sequence-level ratio 与 clipping；长度归一化后的 ratio 不能等同于未经改动的精确 importance weight |
| S19 | [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242), 2026 | 多奖励标准化的扩展阅读；这里只使用摘要层面的动机，不作完整目标推导或 Pareto 保证 |
| S20 | [GSM8K 数据仓库](https://github.com/openai/grade-school-math)、[Training Verifiers to Solve Math Word Problems](https://arxiv.org/html/2110.14168v2), 2021 | 区分数学题作为微调与验证器研究数据、原实验中的计算器标注；不能描述为该论文执行了在线 RL；用于可选 LLM 扩展实验的背景，不是迷宫实验来源 |
| S21 | [PRM800K 数据仓库](https://github.com/openai/prm800k)、[Let's Verify Step by Step](https://arxiv.org/abs/2305.20050), 2023 | 步骤级正确性标签与过程监督；不将其称为计算器工具调用数据或本分享已运行的训练 |

## 框架与系统

| 编号 | 官方入口 | 本材料使用位置与边界 |
| --- | --- | --- |
| S10 | [HybridFlow: A Flexible and Efficient RLHF Framework](https://arxiv.org/abs/2409.19256) | 理解 verl 的控制流与计算流分离；历史论文不是当前全部实现的说明书 |
| S11 | [verl HybridFlow 指南](https://verl.readthedocs.io/en/latest/hybrid_flow.html)、[官方仓库](https://github.com/verl-project/verl) | 控制器、WorkerGroup、数据交接；`latest` 与默认分支可变化，未固定运行版本 |
| S12 | [miles 官方仓库](https://github.com/radixark/miles) | 项目归属、slime 演进关系、实现入口；不是只依赖一条历史宣传介绍 |
| S13 | [Miles v0.1: Production-Level Post-Training](https://arxiv.org/html/2609.08368v1), 2026-09-08 | rollout、训练后端、权重同步、异步和一致性设计；没有复现论文性能结果 |
| S14 | [SkyRL 官方仓库](https://github.com/NovaSky-AI/SkyRL) | 当前统一 `skyrl` 与 Agent/Gym 组件关系；旧目录仍存在不等于旧教程就是当前入口 |
| S15 | [SkyRL 文档](https://docs.skyrl.ai/docs)、[Agent Integration](https://docs.skyrl.ai/docs/tutorials/agent-integration) | 模块化生成/环境接口；集成页标为 WIP，应和当前仓库一起读，不承诺历史类名跨版本兼容 |
| S16 | [SkyRL-Agent](https://arxiv.org/abs/2511.16108) | 多轮、长轨迹 Agent 训练背景；不作为全部 SkyRL 功能的唯一来源 |
| S22 | [verl GRPO](https://verl.readthedocs.io/en/latest/algo/grpo.html)、[Miles Core Concepts](https://miles.radixark.com/docs/user-guide/concepts)、[Miles Fully Async](https://miles.radixark.com/docs/user-guide/fully-async)、[SkyRL System Overview](https://docs.skyrl.ai/docs/getting-started/overview)、[SkyRL Quickstart](https://docs.skyrl.ai/docs/getting-started/quickstart)、[SkyRL One-Step Off-Policy](https://docs.skyrl.ai/docs/tutorials/one_step_off_async) | 2026-09-23 查阅；两题八回答的执行映射、采样与训练 batch 区别、buffer / 批次流水线及权重交接。教学按同步一次更新统一比较；异步示例不等于默认执行方式，字段不可跨版本照抄 |
| S23 | [verl Rollout Correction](https://verl.readthedocs.io/en/latest/algo/rollout_corr.html) | 2026-09-23 查阅；区分策略差异诊断、重要性加权和拒绝采样，以及有效样本量/过滤比例；具体概率比较对象取决于模式，不把校正等同于 reference KL、无偏保证或奖励修复 |
| S24 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023 | 2026-09-24 查阅；非连续 KV blocks 与动态内存管理支持第 14～15 页的生成侧解释；不引入脱离 workload 的倍数，不把分页称为所有碎片归零 |
| S25 | [vLLM Weight Transfer](https://docs.vllm.ai/en/v0.21.0/training/weight_transfer/), v0.21.0 | 2026-09-24 查阅；初始化、开始、传输、结束协议，NCCL / IPC 场景及 pause/resume 接口。动画的版本交接是概念流程，不声称此版本自动提供整个 RL 数据一致性协议 |
| S26 | [vLLM Async Reinforcement Learning](https://docs.vllm.ai/en/v0.19.0/training/async_rl/), v0.19.0 | 2026-09-24 查阅；暂停模式、在途请求、换权重后的 KV 清理与跨版本续写。保留 token 不等于保留旧 KV；接口为此版本的证据，不跨版本照抄配置 |
| S27 | [verl V1 Async Trainer](https://verl.readthedocs.io/en/latest/advance/v1_async_trainer.html), latest | 2026-09-24 查阅；共置/分离模式、partial rollout 保留 token/logprob 并重建 KV、版本滞后及组接受规则；动态文档，不把所有异步模式画成同一执行拓扑 |

## 视频参考及核验范围

2026-09-24 查看 [rollout 是 RL 训练的瓶颈：vLLM 加速与异步训练详解](https://www.bilibili.com/video/BV1N1b76qEif/) 的公开简介和登录后关键画面，包括耗时分解、推理引擎、异步时间线、框架与权重交接。没有取得完整音轨或逐字字幕，因此不记录为完整逐字审阅，也不将未听到的解释归给作者。

吸收的是“先定位瓶颈，再优化采样，随后处理重叠带来的新问题”的表达顺序；机制依据仍是 S24～S27 及框架原始材料。视频中的固定占比、加速数字缺少本材料可核验的完整实验条件，不移入幻灯片。画面中的零碎片、持续满载或权重共享表述也不作为技术保证：分页不消除所有浪费，Actor/Critic 不能默认是同一套参数，同设备执行不等于零成本同步。未保存或嵌入视频画面，动画为独立教学设计。

## 如何解释“已核验”

这里的核验指实际打开论文/官方页面，核对材料使用的机制或项目描述，不表示运行过其中的代码。S01 为出版页，S19 为摘要级扩展，其余算法的核心推导与框架主要机制对应论文正文或官方架构说明。动态文档未保存整站副本，也没有声称锁定源码 commit。

演进图中的箭头表示“回应什么压力”或“依赖什么机制”，不是作者间的必然继承关系。所有框架优势都需按任务、模型、硬件、采样与 loss 设置验证；本材料不提供脱离这些条件的速度排名。
