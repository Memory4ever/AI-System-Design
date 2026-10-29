# 2025-10-07 第二批精确v1准入

作者Ptolemy；本日新增窗口Oct06完整BJT自然日，非作者root待核。下列23份完整title/AB/comments/current history已实际读，全部本日精确v1原响应HTTP200/exit0，见[supplement](supplement-20261012/)中`abs-2510.<ID>v1.raw/request.json`。16P4C3N初判，P未核first-public不评分/formal/Evidence/Books；N是普通决定工作，不隔离外部。

| v1身份 | 提案 | 原约束 → 原文增量 → 可能改变的判断与限制 |
| --- | --- | --- |
| [04532 DriveMind](https://arxiv.org/abs/2510.04532v1) | P | 自然语言CoT被假定中介driving规划 → 去ego/nav prior强降、去CoT弱变及无训练扰动probe → 解释trace与action使用需分开。attention/perturbation不直接证明全模型因果；accepted后公开数据只是计划。 |
| [04568 COSMIR](https://arxiv.org/abs/2510.04568v1) | N | CoA free-form消息丢细节 → structured memory及Extract/Infer/Refine微循环 → 需定点核结构/受控信息损失是否改变context选择，非仅成熟prompt组合。 |
| [04584 Audio MCQA](https://arxiv.org/abs/2510.04584v1) | P | 单accuracy不显选择顺序/措辞依赖 → 三bench四model同时扰动question/choices → 稳健性评价协议改变，不由单次分数比较音频能力。ICASSP2026提交不是先稿公开证。 |
| [04641 Demographic Bias Detection](https://arxiv.org/abs/2510.04641v1) | P | 单轴/单内容评价掩盖联合人口偏差 → 十二dataset多标签与跨轴/多demographic持续缺口 → 训练数据审计gate需覆盖联合而非榜单。fine-tuned小模型承诺不授可扩展可靠认证。 |
| [04678 MATPO](https://arxiv.org/abs/2510.04678v1) | P | 单agent长context/noisy工具、多model角色内存昂贵 → 单LLM以role prompt并按planner/worker rollout credit assignment RL → 角色训练与部署分离可改变选择。18.38%摘要比率非同预算普胜。 |
| [04764 BabyLM Grice](https://arxiv.org/abs/2510.04764v1) | C | 新五maxim benchmark比较10M/100M/3T与儿童，摘要只更多数据总体更好及维度差异；未给可改变主线的控制条件或评价反侧，非因小模型/传统语言主题关闭。 |
| [06274 Complexity OoD](https://arxiv.org/abs/2510.06274v1) | N | 推理能力缺统一定义 → minimal solution/Kolmogorov proxy区分complexity/length/composition → 需核实际定义/条件是否新可用评价边界，还是perspective重命名；不采“scaling data cannot”无前提泛化。 |
| [04819 Visual Reps inside LM](https://arxiv.org/abs/2510.04819v1) | P | 感知信息可解码被混成output可用 → visual value/key与encoder比较、prefix干预及存在不输出反例 → representation/consumer能力分开。COLM2025仅具名先稿身份门，不自动O。 |
| [04850 Distillation Detection](https://arxiv.org/abs/2510.04850v1) | P | 蒸馏数据部分可见难查污染 → generated token probability deviation → 检测signal/低FPR选择可能改变。AUC/TPR非污染存在性证明，calibration/普通难度替代解释保留。 |
| [04871 TRM](https://arxiv.org/abs/2510.04871v1) | P | HRM双频双网递归结构未清楚 → 单2层7M递归网络对照 → 深度/共享递归选择可变。ARC数字非与大LLM统一训练/推理预算普胜。 |
| [04919 SQL Data Alignment](https://arxiv.org/abs/2510.04919v1) | P | SFT被假定总能提升target → SQL structural分布匹配高/低时增益与无增益 → data选择条件可变，非因text-SQL域关。相关预测非已证因果或所有task结构距离有效。 |
| [04980 Hanabi](https://arxiv.org/abs/2510.04980v1) | P | 更高阶ToM被视作更有用 → first-order意图与success相关强于second-order → 多agent rationale评价优先级可变。相关不证ToM导致success；Wordplay2025只先稿线索。 |
| [05003 Medical QLoRA](https://arxiv.org/abs/2510.05003v1) | C | 既有LoRA/QLoRA用于medical CoT、60%内存比full tuning是成熟取舍/领域指标，无新机制或质量资源成立边界；非因medical关键词关。coherence/factuality不授临床安全。 |
| [05038 GQR](https://arxiv.org/abs/2510.05038v1) | P | rank/score融合不能利用双repr空间 → 用text retriever score指导visual query embedding test-time优化 → multimodal retrieval表示/quality-cost选择可变。14x/54x摘要结果不授端到端等质量成本因果。 |
| [05046 COLE](https://arxiv.org/abs/2510.05046v1) | C | 23French task/94models与open/closed差距及难项，摘要只扩benchmark/榜单与领域前沿，未给可修正具体主线判断的控制条件；French/规模不决定排除。 |
| [04767 ParallelBench](https://arxiv.org/abs/2510.04767v1) | P | dLLM parallel被当免费提速 → token依赖理论与analytic list操作、任务难度和并行粒度不适配 → quality/speed评价及commit并行选择改变。非所有diffusion必失败。 |
| [04816 ESCIM CVR](https://arxiv.org/abs/2510.04816v1) | C | SCM造nonclicked conversion labels+多task用于广告CVR，具体推荐应用反事实框架与A/B指标未建立模型主线新机制或通用学习条件；不是因为没有LLM词关闭。ICDMaccepted不授日期。 |
| [04465 Autonomy Matters exact-v1](https://arxiv.org/abs/2510.04465v1) | P | personalization越好被当越受信 → 3×3/N450中间autonomy非单调调节privacy concerns → agent action/user control选择可变。是用户感知/信任不是实测泄露或模型alignment安全，v1不用latest标题。 |
| [04488 MACI](https://arxiv.org/abs/2510.04488v1) | P | 固定对抗/聚合/heuristic停浪费预算 → information/behavior双dial和dispersion/termination条件、judge高能力依赖 → debate控制/stop可靠性选择可变。termination不证正确或clinical安全。 |
| [05188 Dramaturge](https://arxiv.org/abs/2510.05188v1) | N | 局部修改破坏长文global一致 → coarse/fine多agent协调循环 → 需核协调冲突/成立条件而非成熟self-refine流程+domain质量。 |
| [04520 Aria](https://arxiv.org/abs/2510.04520v1) | P | compilation被混成statement语义 → 依赖图分解/grounded definitions及term checker → formalization验证路径可变。编译91.6与正确68.5分开，研究数学task不借通用Agent引入科学应用；这里只核模型形式化/语义验证机制。 |
| [04550 TRAJECT](https://arxiv.org/abs/2510.04550v1) | P | final答案掩盖tool selection/args/order → 可执行API及并行宽度/依赖深度诊断，short→mid瓶颈 → tool轨迹评价可变，不授production可靠性。 |
| [04560 ContextNav](https://arxiv.org/abs/2510.04560v1) | P | similarity检索context可能噪声/结构不一致 → retrieval+structural alignment及downstream反馈Operational Grammar Graph优化 → ICL上下文策略可变。SOTA单数字不采，未核效益归因。 |

三N只恢复决定方法/局部对照；04465必要privacy威胁角色定点核，不扩全部P core。有限身份门只对应具名COLM/Wordplay或其他实际comments线索，不扫会议全集。

## 2. 三N与隐私反侧实际收束

以下四本日exact-v1 HTML均HTTP200/exit0完整响应；实际只读取指定必要段，不授全文/Evidence。第二批最终提案**18P5C/N0**，root待核；原16P4C3N保留为历史。

- **04568 COSMIR：窄P。** [v1](https://arxiv.org/html/2510.04568v1)、[core](supplement-20261012/core-2510.04568v1.raw)实际完整§4–7。structured memory区分unresolved questions/gathered facts/inferred facts，gathered受k-fraction budget且删最旧事实，inferred并未同样明示bound；不是无损长期记忆。CoA/COSMIR同chunk64k、summary/memory8k、相同model温度/max-token，但COSMIR三倍调用，非同预算增益。Table2只将Extract换Qwen时InfBench-MC65.50低于all-Qwen65.93，强planner/manager无法修复弱extract；这一瓶颈/成本条件足以改变阶段模型分配，非仅mature combo提高榜单。missed fact无再出现就不可恢复，fixed-order/chunk与长QA范围限定；未做独立schema/微循环因果消融。
- **06274 Complexity OoD：C。** [v1](https://arxiv.org/html/2510.06274v1)、[core](supplement-20261012/core-2510.06274v1.raw)实际完整§2.2–2.3/3.2。沿既有Kolmogorov input/conditional description长度和object/relation/step proxy提出perspective，必要段未给新定理、可执行proxy验证或修正具体设计的反证。K(y|x)是最短描述长度，不直接等运行时间/推理步骤，oracle/primitive假设和不可计算限制不能靠例子消除；不采“更大K必更深计算/任意复杂度泛化/scaling data cannot”的泛断言。C不因无LLM实验，也不因日期未知。
- **05188 Dramaturge：窄P。** [v1](https://arxiv.org/html/2510.05188v1)、[core](supplement-20261012/core-2510.05188v1.raw)实际完整HCR、Iterative Improvement with Quality Control与Ablation/Iterative Improvement Analysis。两phase在无≥1.0评分增益时停全局storyline编辑，再局部编辑，N次无增益停；提出全局可变状态与局部修复相互破坏的控制边界。单Appendix E示例6轮/基线1–2轮后降仅局部，Table3加模块同时增调用，不证同预算因果/一般收敛。P针对这个锁定/失败条件，不因剧本质量指标倒推机制新颖或可靠性。
- **04465 Autonomy Matters：P保留，隐私感知不等安全。** [v1](https://arxiv.org/html/2510.04465v1)、[core](supplement-20261012/core-2510.04465v1.raw)实际完整§4.2、4.3.3、4.4.1、4.5、5.3–5.4。两脚本化场景/真实个人数据、GPT-4o敏感judge，三autonomy由always approval/auto/flag才approval构造。privacy-aware是输入直接删敏感信息的理想条件，非模型学会privacy alignment；所有条件都检查/通知，仅中间条件改变发送行为。538响应筛88后450/九格50，dependent是Likert concern/trust/willingness；中间autonomy相对no对trust/concern有差，而willingness未显著不同。敏感内容/通知暴露数量不保证一致，posthoc至少一次也不控制总量，不授泄露率或跨场景可靠认证。

首批和第二批累计作者新完整题摘35，提案28P7C/N0；论文公开日仍未确认，不能混AgentKit新已关闭formal或原两Evidence家族。以上“root待核”为当时过程，当前已实际获root SUP_INDEPENDENT§5通过，不再普通待办。
