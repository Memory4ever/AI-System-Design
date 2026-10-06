# 2025-09-03 第四批窄主题精确v1题摘

## 1. 实际范围

作者完整读以下15份官方精确v1 title+abstract/comments/版本栏，初次组合输出截断的00996/00997/01016随后定点完整回读；原件abs-2509.<ID>v1.raw与请求及[完整题摘](supplement-20261011/SUP_EXACT_20261011.json)在supplement-20261011。11P/1C/3U仅准入判断，全部公开自然日未证，不评分/Evidence/Books。Seed的Robix Sep01目录不是完整论文公开日期，不据此关闭01106。三U只读决定事实，不将整池或全文变队列。

| 精确身份与完整题名 | 暂判 | 具体理由/限制 |
| --- | --- | --- |
| [00996](https://arxiv.org/abs/2509.00996v1) MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper | P | rigid PEFT参数→多prompt expert动态激活适配非平稳分布→激活容量/路由取舍；不由manifold图授因果，EMNLP2025先稿门。 |
| [00997](https://arxiv.org/abs/2509.00997v1) Supporting Our AI Overlords: Redesigning Data Systems to be Agent-First | U | agentic speculation的scale/heterogeneity/redundancy/steerability是具名约束，但需必要core判query/memory方案是否仅research opportunities，非“agent-first”准入。 |
| [01016](https://arxiv.org/abs/2509.01016v1) Analysis of Error Sources in LLM-based Hypothesis Search for Few-Shot Rule Induction | U，反侧 | 规则假设搜索优于直接program生成，AB未说明具体bottleneck；必要core判失败条件是否修正search/verification选择，不因未给全部实验细节关闭。 |
| [01028](https://arxiv.org/abs/2509.01028v1) CompSlider: Compositional Slider for Disentangled Multiple-Attribute Image Generation | P | 多属性纠缠→conditional-prior latent与结构约束slider→无需重训foundation的control接口；不授完全disentangle，ICCV2025先稿门。 |
| [01052](https://arxiv.org/abs/2509.01052v1) FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games | P，评价 | 观测/动作分离的长故事状态与CUAjudge/COASTmemory→交互planning评价，不由游戏领域或ranking准入；judge非oracle，EMNLP2025先稿门。 |
| [01055](https://arxiv.org/abs/2509.01055v1) VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use | P | 多模态tool状态/rollout straggler→统一工具环境与异步rollout→RL采样/工具执行接口；不授全部2×或可复现。 |
| [01081](https://arxiv.org/abs/2509.01081v1) Assessing Large Language Models on Islamic Legal Reasoning: Evidence from Inheritance Law Evaluation | U，反侧 | 当前AB仅法域MCQ排名与context/rule/knowledge三类一般错误；必要core判是否具体structured reasoning评价盲区，不按宗教/法律领域直接排除。 |
| [01082](https://arxiv.org/abs/2509.01082v1) REFINESTAT: Efficient Exploration for Probabilistic Program Synthesis | P | 统计程序可执行不等成立→统计约束与诊断指导prior/likelihood重采样→程序验证对象扩大；不授所有统计假设真值。 |
| [01083](https://arxiv.org/abs/2509.01083v1) DSDE: Dynamic Speculative Decoding with KLD Stability for Real-World Serving | P | low-acceptance/straggler→KLD/variance估质量并控制draft长度→接受率与并行尾延迟联动；不授全硬件或所有分布稳健。 |
| [01088](https://arxiv.org/abs/2509.01088v1) Privacy-Preserving Reasoning with Knowledge-Distilled Parametric Retrieval Augmented Generation | P，安全 | document到LoRA generator及hidden/logit distill→检索表征/原文存储边界；原文移除不等参数隐私或无泄漏，需安全独核。 |
| [01092](https://arxiv.org/abs/2509.01092v1) REFRAG: Rethinking RAG based Decoding | P | retrieved token block-diagonal/压缩-感知-展开→RAG上下文计算与容量选择；AB倍率转写符号不全，不照录端到端性能。 |
| [01106](https://arxiv.org/abs/2509.01106v1) Robix: A Unified Model for Robot Interaction, Reasoning and Planning | P | 原子动作/语言统一序列、主动对话和interrupt+consistency RL→机器人交互控制接口；SeedSep01列表不证正文首公开，不授闭环安全。 |
| [01142](https://arxiv.org/abs/2509.01142v1) Dream-Coder 7B: An Open Diffusion Language Model for Code | P | coding任意order、padding penalty和random truncation SFT/RL→离散生成监督与并行解码选择；未证AR预算公平、emergence因果。 |
| [01167](https://arxiv.org/abs/2509.01167v1) Do Video Language Models Really Know Where to Look? Diagnosing Attention Failures in Video Language Models | P，反侧 | 精确v1不是新版TempCore；keyframe encoder选不准任务相关帧→视频输入选择与reasoning能力分开，不授所有VLM失效。 |
| [01185](https://arxiv.org/abs/2509.01185v1) Modular Techniques for Synthetic Long-Context Data Generation in Language Model Training and Evaluation | C | 完整AB四种模板生成、SFT/DPO/GRPO与metadata/model-agnostic组合，未指出新验证机制/具体成立条件或修正现有判断的反侧；不因无实验细节或日期关闭。 |

root可先核11P/安全反侧与代表C；三U作者继续定点决定段。第三批六U已另追加为5P/1C，第三批首30现28P/2C；前三批73=67P/6C（独核只授实际已签前43，不提前授第三批）。

## 2. 三U关闭为3P，第四批14P/1C

- [00997v1](https://arxiv.org/html/2509.00997v1)：实际完整§2/3/4，BIRD50个parallel attempts的distinct subplan仅总量10–20%，两backend22task×2 traces探索/solution阶段重叠，人工hint改变query数。P不是尚未实现agent-first DB架构：是query独立执行假设与Agent speculative workload冗余/grounding控制的局部证据；brief/querypriority/approximation/sleeperagents仍proposal，不授新系统已实现或20%全收益。
- [01016v1](https://arxiv.org/html/2509.01016v1)：实际完整§4，64hypotheses→8摘要丢26%正确假设，但implementor在上游双fail仍可救部分test，correctness由另LLM按规则文字评而非唯program-test。P为compression选择与downstream可执行效标错位，不采人类等价/17×因果或全面模块消融；无需读附录C–E全部。
- [01081v1](https://arxiv.org/html/2509.01081v1)：实际完整§5及Table7（§4混排局部不计全读），40个答对case人工核仍有遗漏/造heir、虚构citation/错误份额解释，accuracy遮掩解释错误。P只LLM答案/依据效标分开，非法律领域指标准入，不授法律规则或训练语料已知；47%等百分比只该小样本/本文口径。

原件分别core-2509.<ID>v1.raw。三U普通决定工作0，但独核/公开日门未授完成。第四批14P/1C，前三四批88题摘作者81P/7C，不混正式候选。

root独核§9随后实际读本批15完整精确v1 AB/comments/history及以上三个core决定范围，准入14P/1C通过；00997 proposal/局部冗余、01016摘要丢真解/implementor恢复、01081正确答案下错误依据边界保留。只准入校准，不授公开日、正式Evidence或最终DAY。00629先稿门另见第三批后补差额，不推倒本批有效结论。
