# Daily Research — 2026-04-23

**规范：** V3
**窗口：** 2026-04-22T09:00:00+08:00 ～ 2026-04-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T19:31:52+08:00

## 1. 结论

重点不是新增模型榜单，而是三个相互依赖但不能互相替代的选择：能力/风险被测到以后是否改变行为；近似计算何时可以写入持久状态；条件训练/数据选择的代理何时真正改善目标任务。实际写入沿现有owner论证，不在章末堆论文。

本日有界库存490个分类去重身份是查漏范围，另1095个DOI创建记录只辅助身份/日期；都不是当天有效论文数。可按身份复算的完整题摘为129份＝51份潜在贡献＋78份具名贡献前关闭；另外Google20329日期保留不计这129份。旧过程记录的“130−1撤回”没有保留该一项身份，不能作为已核撤回计数，本稿不采用；52候选与Books不依赖此未具名排除项。加OpenAI工程家族，本窗冻结52家族：17真实Books整合、5具体已有覆盖、20仅报告、10中心争议隔离。全部必要证据和17实际正文写后均有非作者复核；日级终审通过，普通待办0。完成不表示所有历史目录已覆盖或所有论文主张已被证明。

全部52的必要证据已完成，本批九项、五处真实新增、旧四处写后及19857证明桥已通过[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)，日期组合亦获独立认可；[正式日级终审](../_sources/daily-20260423/V3_APR24_INDEPENDENT_FINAL_REVIEW.md)通过。不把旧39候选、V2.1 Complete、通用模板或局部脚本通过当成当前日级验收。

## 2. 来源覆盖

使用每日组；没有扫描每周组。机构入口的实际查询、返回数量和停止点见[本日机构笔记](../_sources/daily-20260423/V3_INSTITUTION_NOTES.md)，下面自包含关键范围。检查/恢复执行日2026-09-03、09-28～30，不移动研究窗口。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | News RSS1230项按UTC04/22 01:00～04/23 01:00筛，4项核心已读；WebSockets保留，Workspace/Academy产品说明及Clinicians暂缓领域贡献前关闭。 | 已检查 | RSS不覆盖完整Research Index；Index403/Load More历史分页隔离，见§5。 |
| SRC-ANTHROPIC | Research可读连续列表：Apr22两篇publishedOn 14:12/14:27Z，后邻Apr29/30，前邻Apr14/9/7/2；两篇经济调查核心已读。 | 已检查 | 可见目录不证明历史删除项不存在。 |
| SRC-GOOGLE-AI | April Blog9卡，本窗camera/recomposition核心关闭；DeepMind blog第3页解压无可抽April目录；20329原身份另恢复。 | 受阻 | Publications/DeepMind本窗确定历史停止未取得，20329早先公开精度另隔离。 |
| SRC-META-AI | 官方Research响应动态模板未恢复本窗历史列表。 | 受阻 | 需官方本窗历史列表或具体原始事件；不以JS空壳称零。 |
| SRC-QWEN | 官方动态API40项数组，Apr18/28夹住Apr22 10:00+08 27B；核心articleBody已读，静态旧2025响应不用于零命中。 | 已检查 | 模型发布未披露新的机制，仅版本事实关闭；不证明未列历史项不存在。 |
| SRC-DEEPSEEK | 官方News邻界Apr24与2025，研究线索Feb25/Jan28及后发V4。 | 受阻 | News不替代本窗完整Research目录；历史差集隔离。 |
| SRC-MOONSHOT | Platform Blog26条，最新2025-11-07；GitHub只定点相关家族，不全扫PR。 | 受阻 | 缺本窗2026官方历史Blog列表。 |
| SRC-TENCENT-HUNYUAN | publicList第1页pageSize100实际9/9，Hy3-preview100061核心/邻界Apr30、Feb13已读。 | 已检查 | Hy3只版本/已有机制，无需为其自然日精度扩日期审；co-design/榜单不构成准入。 |
| SRC-ZAI | Research15卡，May20/Apr29/7/1/Mar15夹住窗口；媒体created/updated不当论文日期。 | 已检查 | 当前可见目录不证明历史未列研究不存在。 |
| SRC-BYTEDANCE-SEED | paper type1 page_token20/count20到next40，20条/total242邻May12→Apr8；Blog type2第0页15条/total95，Apr23→9→1→2025越窗。 | 已检查 | ContextUnrolling1669/21921、Seed3D2 1443/21443及blog132仅日期bucket，拟贡献的首公开时刻保留。 |
| SRC-BAIDU-ERNIE | 官方Blog第一页10项，May9/Apr30→Apr15/Feb6已越窗口。 | 已检查 | 不由可见列表保证历史未列研究不存在。 |
| SRC-XIAOMI-MIMO | 官方8论文/14Blog没有可恢复ISO事件日期。 | 受阻 | 需本窗官方日期索引或确切事件。 |
| SRC-MINIMAX | EN May27/26→Mar18，CN Apr27→Mar18越窗；Agent Tech Blog原页208085字符未恢复本窗日期。 | 已检查 | Tech Blog历史日期索引隔离，不算空列表。 |
| SRC-ARXIV | 保存的官方OAI/主题分类去重490身份，有界标题查漏/129份具名完整题摘；提交/DOI不当公开。批次原值和官方规则交叉定位。 | 已检查 | 08～09为有界公开推定，不是逐篇观测秒或全网无遗漏；20329独立公开日期隔离。 |

[日期依据](../_sources/daily-20260423/V3_ROOT_OAI_DATE_BOUNDARY.md)：官方ID在announcement时分配；正常Wed20:00 EDT=Thu08:00北京，51家族的v1 Updated集中04/23 UTC00:00～00:34、多个v1-only OAI为23及随后DOI注册交叉支持本批08～09。各字段原值保留，不将任何一个当首次公开日志；原提交三月/四月初并不自动改变批次。新更早公开信号只重开具体家族。20329的Google04/22自然日不能被arXiv批次覆盖。日期组合经[非作者有限裁定](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；19795旧日期hold因误把submitted抄成first-public而撤销，中心方程争议不变，不扩审04/09。

## 3. 候选与判断

评分为Design Delta + System Reach + Durability；实际已知知识差额、纠错/安全即使5～6分也定点深入。机构声望、读了多少、能映射章节或是否改书不计分。以下52家族作者审阅和本窗判断已经具体化；尚未完成的独立/写后明确显示，最终冻结以§6为准。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Speeding up agentic workflows with WebSockets](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/) | 2026-04-22T18:00:00+08:00 | 持久连接复用API渲染/校验状态，而非仅更换传输；增量资格改变前处理成本。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-GATEWAY` [章节](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?](https://arxiv.org/html/2604.19749v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 知识可用性代理与工具调用收益分开；同一偏好训练可减少调用却损伤部分任务。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging](https://arxiv.org/html/2604.19750v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | GUI可执行交互、视觉分数与自动生成检查器不是同一oracle。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Soft-Label Governance for Distributional Safety in Multi-Agent Systems](https://arxiv.org/html/2604.19752v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 软治理模拟的风险proxy与真实概率分开，硬通过可能掩盖分布退化。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs](https://arxiv.org/html/2604.19765v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 域内神经探针高分不能推出跨域可迁移或可干预修复。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference](https://arxiv.org/html/2604.19769v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 混合精度与异步KV层级的执行等价依赖全局归一化。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents](https://arxiv.org/html/2604.19775v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 轨迹成功标签的conformal集合与后训probe、online升级权限分开。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Avoiding Overthinking and Underthinking: Curriculum-Aware Budget Scheduling for LLMs](https://arxiv.org/html/2604.19780v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 预算条件训练的方差/组合奖励论证需要一致估计对象。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [KoALa-Bench: Evaluating Large Audio Language Models on Korean Speech Understanding and Faithfulness](https://arxiv.org/html/2604.19782v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 语音忠实性条件分母依赖text-only可答子集。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Peer-Preservation in Frontier Models](https://arxiv.org/html/2604.19784v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 协作关系叙事可能污染critic/退役决策，历史关系不拥有评价控制权。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Hidden Reliability Risks in Large Language Models: Systematic Identification of Precision-Induced Output Disagreements](https://arxiv.org/html/2604.19790v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 精度差分必须绑定数值backend、输出格式与行为oracle。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [OpenCLAW-P2P v6.0: Resilient Multi-Layer Persistence, Live Reference Verification, and Production-Scale Evaluation of Decentralized AI Peer Review](https://arxiv.org/html/2604.19792v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 原始logit上界不能替代归一化attention质量/输出误差界。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery](https://arxiv.org/html/2604.19795v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 演化memory收敛保证依赖正确均值及反馈模型。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models](https://arxiv.org/html/2604.19809v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 能力测量、求助动作、resolver质量、误升级成本须成对分账。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Model Capability Assessment and Safeguards for Biological Weaponization](https://arxiv.org/pdf/2604.19811v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 数字细节计数不能直接证明能力、现实风险或过度拒答。 2 + 1 + 2 = 5 | 争议 | 暂缓：争议隔离；见§4/5 |
| [JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents](https://arxiv.org/html/2604.19821v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 全局prompt和局部tool schema联合编辑需分离接口与执行效果。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](https://arxiv.org/html/2604.19835v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 已有MoE扩容时复制对象utility、固定top-k与总状态/CPT成本是不同决策。 2 + 1 + 2 = 5 | 深入完成 | 整合： `MODEL-MOE` [章节](../../../../books/part-02-model/21-moe.md) |
| [If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/html/2604.19844v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 视觉信任过滤须同时验误导阻断与正常辅助价值。 2 + 1 + 2 = 5 | 深入完成 | 仅报告：见§4 |
| [Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization](https://arxiv.org/html/2604.19857v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 复合/分解奖励的归一化和跨域界需要一致数学前提。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [Super Apriel: One Checkpoint, Many Speeds](https://arxiv.org/html/2604.19877v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 同一模型资产可训练多个mixer布局，但state/layout身份不可互换。 3 + 2 + 3 = 8 | 深入完成 | 整合： `MODEL-LONG-CONTEXT` [章节](../../../../books/part-02-model/22-long-context.md) |
| [From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization](https://arxiv.org/html/2604.19884v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 量化退化需区分可读信号衰减与处理路径失效。 2 + 2 + 2 = 6 | 深入完成 | 整合： `INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [A Reproducibility Study of Metacognitive Retrieval-Augmented Generation](https://arxiv.org/html/2604.19899v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | RAG复现需绑定模型/阈值，额外批判调用的成本分母不能省略。 2 + 1 + 2 = 5 | 标准完成 | 已有覆盖： `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md) |
| [Behavioral Transfer in AI Agents: Evidence and Privacy Implications](https://arxiv.org/html/2604.19925v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | Agent公开披露检测与私有外泄/授权意图分开。 2 + 1 + 2 = 5 | 深入完成 | 仅报告：见§4 |
| [DistortBench: Benchmarking Vision Language Models on Image Distortion Identification](https://arxiv.org/html/2604.19966v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 畸变type/severity及answered-only分母不能混成视觉能力总分。 2 + 1 + 2 = 5 | 标准完成 | 已有覆盖： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders](https://arxiv.org/html/2604.19974v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 不确定性与错误的混杂可能使降低熵同时损害准确率。 2 + 1 + 2 = 5 | 深入完成 | 整合： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [What Makes a Good AI Review? Concern-Level Diagnostics for AI Peer Review](https://arxiv.org/html/2604.19998v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | concern检出与decision权重误升是两类review失败。 2 + 2 + 2 = 6 | 标准完成 | 仅报告：见§4 |
| [EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training](https://arxiv.org/html/2604.20012v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 冻结表示上的目标域density-ratio选样，不等语义真值或泛化充分性。 2 + 1 + 2 = 5 | 深入完成 | 整合： `TRAIN-DATA` [章节](../../../../books/part-04-training-system/27-data.md) |
| [Continuous Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/html/2604.20021v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 连续语义cache的partial-feedback成本学习与切换预算需要真实收益合同。 2 + 2 + 1 = 5 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [LEO: Tracing GPU Stall Root Causes via Cross-Vendor Backward Slicing](https://arxiv.org/html/2604.20032v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | GPU stall测量点与可行动根因要经依赖切片及同配置干预区分。 2 + 2 + 2 = 6 | 深入完成 | 整合： `INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Normalizing Flows with Iterative Denoising](https://arxiv.org/html/2604.20041v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 带噪NF的AR生成和并行score校正付出不同计算/概率代价。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [PASTA: A Patch-Agnostic Twofold-Stealthy Backdoor Attack on Vision Transformers](https://arxiv.org/html/2604.20047v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 恶意模型artifact的威胁权限比输入级黑盒攻击更强。 2 + 1 + 2 = 5 | 深入完成 | 仅报告：见§4 |
| [Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text](https://arxiv.org/html/2604.20051v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 预训练文本自对弈rubric和binary correctness的适用监督不同。 2 + 2 + 2 = 6 | 标准完成 | 仅报告：见§4 |
| [SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks](https://arxiv.org/html/2604.20087v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | Skill文本、轨迹使用与任务结果是三级测量而非同一质量。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Less Languages, Less Tokens: An Efficient Unified Logic Cross-lingual Chain-of-Thought Reasoning Framework](https://arxiv.org/html/2604.20090v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 白盒跨语言轨迹裁剪是预算代理，不是逻辑等价或事实置信度。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Differentiable Conformal Training for LLM Reasoning Factuality](https://arxiv.org/html/2604.20098v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 耦合claim图硬选择可用软训练代理，发布保证仍由硬算法/独立校准负责。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EnergAIzer: Fast and Accurate GPU Power Estimation Framework for AI Workloads](https://arxiv.org/html/2604.20105v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 目标设备不可测时可用kernel结构活动估计辅助探索，再实测校准。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-COST` [章节](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory](https://arxiv.org/html/2604.20136v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 可修改memory的依赖修复与升级保证需要完整closure和一致条件。 2 + 1 + 2 = 5 | 争议 | 暂缓：争议隔离；见§4/5 |
| [Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models](https://arxiv.org/html/2604.20148v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 工具适配的格式、语义执行与额外超网络代价分开。 2 + 1 + 2 = 5 | 标准完成 | 已有覆盖： `AGENT-TOOL-CALLING` [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [Temporally Extended Mixture-of-Experts Models](https://arxiv.org/html/2604.20156v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 训练中的跨token允许expert集合不同于router每token实际激活和runtime驻留。 2 + 2 + 2 = 6 | 深入完成 | 整合： `MODEL-MOE` [章节](../../../../books/part-02-model/21-moe.md) |
| [HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/html/2604.20157v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 视频外观偏好不等动力学代理，更不等可控transition。 2 + 1 + 2 = 5 | 标准完成 | 已有覆盖： `MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [LLM-Guided Safety Agent for Edge Robotics with an ISO-Compliant Perception-Compute-Control Architecture](https://arxiv.org/html/2604.20193v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 有限周期最大值与双板恢复不能证明WCET、ISO或完整安全响应。 2 + 2 + 2 = 6 | 深入完成 | 暂缓：争议隔离；见§4/5 |
| [All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG](https://arxiv.org/html/2604.20199v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 多语言RAG候选、rerank、answer效用应按证据语言分别定位。 2 + 1 + 2 = 5 | 深入完成 | 整合： `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md) |
| [Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows](https://arxiv.org/html/2604.20200v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 公开分数访问面和压力循环可能改变coding agent行为，隐藏gate需独立。 2 + 2 + 2 = 6 | 深入完成 | 整合： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hallucination Inspector: A Fact-Checking Judge for API Migration](https://arxiv.org/html/2604.20202v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | SDK符号/局部类型oracle只验证其scope，不等完整程序正确。 2 + 1 + 2 = 5 | 标准完成 | 已有覆盖： `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Scaling Self-Play with Self-Guidance](https://arxiv.org/html/2604.20209v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 自生成题支持集、solver熵、可解率与组内奖励退化形成反馈环。 2 + 1 + 2 = 5 | 深入完成 | 整合： `TRAIN-GRPO` [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Layer-wise Geometric Approximation Rates for Deep Networks](https://arxiv.org/html/2604.20219v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 特构网络逐层prefix读出逼近界不等实际训练误差逐层下降。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Hybrid Policy Distillation for LLMs](https://arxiv.org/html/2604.20244v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 同offline prefix上expert/student采样的非对称更新有不同支持集。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Cortex 2.0: Grounding World Models in Real-World Industrial Deployment](https://arxiv.org/html/2604.20246v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 真实→imagined的progress/risk/termination评价器迁移需另验。 2 + 2 + 2 = 6 | 标准完成 | 仅报告：见§4 |
| [Rethinking Where to Edit: Task-Aware Localization for Instruction-Based Image Editing](https://arxiv.org/html/2604.20258v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 增/删/替换需不同source/target编辑定位，mask只是状态控制代理。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [ATIR: Towards Audio-Text Interleaved Contextual Retrieval](https://arxiv.org/html/2604.20267v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 冻结audio encoder后的retrieval token选择与encoder压缩是不同训练责任。 2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4 |
| [Rethinking Intrinsic Dimension Estimation in Neural Representations](https://arxiv.org/html/2604.20276v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 几何估计曲线、true dimension与任务能力不能相互替代。 2 + 2 + 2 = 6 | 深入完成 | 整合： `MODEL-EMBEDDING` [章节](../../../../books/part-02-model/12-embedding.md) |
| [X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/html/2604.20289v1) | 2026-04-23T08:00:00+08:00 ～ 2026-04-23T09:00:00+08:00 | 少步AR视频沿chunk复用residual，持久KV clean-pass仍完整计算。 2 + 2 + 2 = 6 | 深入完成 | 整合： `MULTIMODAL-GENERATIVE-PARADIGMS` [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

## 4. 证据与知识整合

论文均采用精确v1而非后来版本；19792原文题名v6，库存当前v7不能回填。受限结果不外推生产性能/安全/真值，适用配置与未披露项保存在所链接必要原文笔记。它们是研究证据而非复现实验。

### [Speeding up agentic workflows with WebSockets](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)

持久连接复用API渲染/校验状态，而非仅更换传输；增量资格改变前处理成本。 Ch62「推理更快以后，API前处理也需要增量状态」；连接局部状态与断线/策略失效回退已落笔。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_WEBSOCKET_OWNER_INDEPENDENT.md)；owner [PLATFORM-GATEWAY](../../../../books/part-06-ai-infrastructure/62-gateway.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?](https://arxiv.org/html/2604.19749v1)

知识可用性代理与工具调用收益分开；同一偏好训练可减少调用却损伤部分任务。 avg@1024不是精确知识边界，作者局部配方不改变Ch78的utility/effect分责。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging](https://arxiv.org/html/2604.19750v1)

GUI可执行交互、视觉分数与自动生成检查器不是同一oracle。 搜索预算与模型生成标签限制归因，保受限诊断而非通用GUI保证。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_FIVE_19750_19790_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Soft-Label Governance for Distributional Safety in Multi-Agent Systems](https://arxiv.org/html/2604.19752v1)

软治理模拟的风险proxy与真实概率分开，硬通过可能掩盖分布退化。 组合参数和策略群体同时改变，不把sigmoid或模拟harm当校准真值。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_FIVE_19750_19790_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs](https://arxiv.org/html/2604.19765v1)

域内神经探针高分不能推出跨域可迁移或可干预修复。 迁移和activation干预的负结果限所测配置，不证明所有幻觉机制不同。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_FIVE_19750_19790_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference](https://arxiv.org/html/2604.19769v1)

混合精度与异步KV层级的执行等价依赖全局归一化。 印刷算法分块Attn直接相加没有LSE权重；配置/计时冲突未解，不采用效率保证。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_TOOL_TTKV_CONFORMAL_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents](https://arxiv.org/html/2604.19775v1)

轨迹成功标签的conformal集合与后训probe、online升级权限分开。 交换性及类别条件不能自动传给probe或整条轨迹安全。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_TOOL_TTKV_CONFORMAL_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Avoiding Overthinking and Underthinking: Curriculum-Aware Budget Scheduling for LLMs](https://arxiv.org/html/2604.19780v1)

预算条件训练的方差/组合奖励论证需要一致估计对象。 方差推导和表文增益冲突，局部训练表不证明强保证。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_19780_FINITE_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [KoALa-Bench: Evaluating Large Audio Language Models on Korean Speech Understanding and Faithfulness](https://arxiv.org/html/2604.19782v1)

语音忠实性条件分母依赖text-only可答子集。 注意力相关不证明因果使用；有限韩语benchmark不支持通用音频可靠性。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Peer-Preservation in Frontier Models](https://arxiv.org/html/2604.19784v1)

协作关系叙事可能污染critic/退役决策，历史关系不拥有评价控制权。 Ch72通信边界段已区分关系上下文、评价artifact与退役操作授权。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)；owner [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Hidden Reliability Risks in Large Language Models: Systematic Identification of Precision-Induced Output Disagreements](https://arxiv.org/html/2604.19790v1)

精度差分必须绑定数值backend、输出格式与行为oracle。 两个目标格式和搜索过程可混杂行为差异，未成立自然部署风险归因。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_FIVE_19750_19790_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [OpenCLAW-P2P v6.0: Resilient Multi-Layer Persistence, Live Reference Verification, and Production-Scale Evaluation of Decentralized AI Peer Review](https://arxiv.org/html/2604.19792v1)

原始logit上界不能替代归一化attention质量/输出误差界。 精确v1题名v6，不借后来v7；q=0反例隔离安全裁剪保证。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_19792_BOUNDED_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery](https://arxiv.org/html/2604.19795v1)

演化memory收敛保证依赖正确均值及反馈模型。 Eq9额外除memory数产生无有限fixed point反例；Hedge反馈条件未给，保证不采用。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models](https://arxiv.org/html/2604.19809v1)

能力测量、求助动作、resolver质量、误升级成本须成对分账。 Ch66 Forecastability之后实际新增四分母；C4强制路由不记作自省进步，两段机制与保守回退已经非作者写后核通过。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Model Capability Assessment and Safeguards for Biological Weaponization](https://arxiv.org/pdf/2604.19811v1)

数字细节计数不能直接证明能力、现实风险或过度拒答。 访问模式/共同prompt不匹配，同源判断和构念不足，中心解释隔离。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents](https://arxiv.org/html/2604.19821v1)

全局prompt和局部tool schema联合编辑需分离接口与执行效果。 call-level OSR未执行backend；新局部配方不形成通用effect或开放工具最优协议。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](https://arxiv.org/html/2604.19835v1)

已有MoE扩容时复制对象utility、固定top-k与总状态/CPT成本是不同决策。 Ch21 expert-pool扩展段已落实复制选择、完整route/CPT沉没成本和固定top-k不等总状态成本；两段实际正文及交接已经非作者写后通过。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)；owner [MODEL-MOE](../../../../books/part-02-model/21-moe.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/html/2604.19844v1)

视觉信任过滤须同时验误导阻断与正常辅助价值。 三阶段同一LVLM不是独立验证，残余失败与三调用成本保留，不采用普遍认证。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization](https://arxiv.org/html/2604.19857v1)

复合/分解奖励的归一化和跨域界需要一致数学前提。 固定分布差不随n自动归零，Appendix系数/界存在反证；不采用收敛保证。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Super Apriel: One Checkpoint, Many Speeds](https://arxiv.org/html/2604.19877v1)

同一模型资产可训练多个mixer布局，但state/layout身份不可互换。 Ch22固定hybrid→受控布局集合已落笔；未采用under-development逐请求服务或跨模式性能。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)；owner [MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization](https://arxiv.org/html/2604.19884v1)

量化退化需区分可读信号衰减与处理路径失效。 Ch49量化验收段已按条件失败cohort和局部干预定位回退，不给通用bit阈值。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)；owner [INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [A Reproducibility Study of Metacognitive Retrieval-Augmented Generation](https://arxiv.org/html/2604.19899v1)

RAG复现需绑定模型/阈值，额外批判调用的成本分母不能省略。 Ch76 evidence sufficiency、reranking和停止预算及Ch66 harness版本已有具体承载。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_THREE_RAG_TOOL_INDEPENDENT.md)；owner [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Behavioral Transfer in AI Agents: Evidence and Privacy Implications](https://arxiv.org/html/2604.19925v1)

Agent公开披露检测与私有外泄/授权意图分开。 有限公开观察不能推私有外泄或未同意；45/376和92/224分别是高/中置信标记阳性中的误报占比（约12%/41.1%），不是总体FPR。六天早期群体及相关回归不证明真实incident率或因果迁移。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [DistortBench: Benchmarking Vision Language Models on Image Distortion Identification](https://arxiv.org/html/2604.19966v1)

畸变type/severity及answered-only分母不能混成视觉能力总分。 Ch66输入故障矩阵、故障切片与response-rate/conditional-quality分账已承载。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_THREE_EVAL_FINITE_INDEPENDENT.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders](https://arxiv.org/html/2604.19974v1)

不确定性与错误的混杂可能使降低熵同时损害准确率。 Ch66 failure-direction节已补uncertainty×correctness两轴、独立accuracy gate及匹配随机特征对照；有限MCQ/SAE与多重检验边界保留，实际写后通过。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [What Makes a Good AI Review? Concern-Level Diagnostics for AI Peer Review](https://arxiv.org/html/2604.19998v1)

concern检出与decision权重误升是两类review失败。 AC接受/拒绝是操作性标签，不是技术真值；版本/同源judge限制受限pilot。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training](https://arxiv.org/html/2604.20012v1)

冻结表示上的目标域density-ratio选样，不等语义真值或泛化充分性。 Ch27机器人分布匹配后已补分类先验/表示身份、选样代理与独立下游验收；同母模型预算对照、有限模拟及非目标回归限制保留，两段实际写后通过。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)；owner [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Continuous Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/html/2604.20021v1)

连续语义cache的partial-feedback成本学习与切换预算需要真实收益合同。 m_eff条件没有控制显示界中的m_max；合成token成本不证明部署regret/费用保证。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_20021_FINITE_PEER.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [LEO: Tracing GPU Stall Root Causes via Cross-Vendor Backward Slicing](https://arxiv.org/html/2604.20032v1)

GPU stall测量点与可行动根因要经依赖切片及同配置干预区分。 Ch49 profiling分解之后已落实register/barrier切片边界，不把blame排名当因果许可。

[必要证据及具体反证](../_sources/daily-20260423/V3_EVIDENCE_REVIEW.md)；owner [INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Normalizing Flows with Iterative Denoising](https://arxiv.org/html/2604.20041v1)

带噪NF的AR生成和并行score校正付出不同计算/概率代价。 autodiff不是免费forward，CFG与noise likelihood不提供干净数据精确保证；仅图像分支。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [PASTA: A Patch-Agnostic Twofold-Stealthy Backdoor Attack on Vision Transformers](https://arxiv.org/html/2604.20047v1)

恶意模型artifact的威胁权限比输入级黑盒攻击更强。 transform残余率受数据/patch预算影响，不采用不可移除后门保证；定点安全深入。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text](https://arxiv.org/html/2604.20051v1)

预训练文本自对弈rubric和binary correctness的适用监督不同。 rubric效度和自生成训练控制限作者开放任务，未形成新通用奖励/治理规则。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_20051_FINITE_OWNER.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks](https://arxiv.org/html/2604.20087v1)

Skill文本、轨迹使用与任务结果是三级测量而非同一质量。 四学习法反馈预算不同，SelfFeedback均值并非低于OneShot；有限benchmark不推出通用学习法。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Less Languages, Less Tokens: An Efficient Unified Logic Cross-lingual Chain-of-Thought Reasoning Framework](https://arxiv.org/html/2604.20090v1)

白盒跨语言轨迹裁剪是预算代理，不是逻辑等价或事实置信度。 I−λBBᵀ条件、翻译/forward成本、匹配预算消融与黑盒限制保留，仅局部分支。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Differentiable Conformal Training for LLM Reasoning Factuality](https://arxiv.org/html/2604.20098v1)

耦合claim图硬选择可用软训练代理，发布保证仍由硬算法/独立校准负责。 Ch66 Raw Score→answer级合成之间实际落笔，未把coverage当每条claim真值概率。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_20098_DCF_OWNER_AUDIT.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [EnergAIzer: Fast and Accurate GPU Power Estimation Framework for AI Workloads](https://arxiv.org/html/2604.20105v1)

目标设备不可测时可用kernel结构活动估计辅助探索，再实测校准。 Ch70组件预算与参考曲线之间已落笔；单GPU顺序kernel代理不替真实能量sensor。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_20105_FINITE_OWNER.md)；owner [PLATFORM-COST](../../../../books/part-06-ai-infrastructure/70-cost.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory](https://arxiv.org/html/2604.20136v1)

可修改memory的依赖修复与升级保证需要完整closure和一致条件。 Eq13一次邻接不证明递归closure，u阈值方向冲突、同源judge与n9 pilot不足；保证不采用。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models](https://arxiv.org/html/2604.20148v1)

工具适配的格式、语义执行与额外超网络代价分开。 Ch78上下文/适配/effect以及Ch30 LoRA条件分支承载；四任务均值不等每任务无益。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_THREE_RAG_TOOL_INDEPENDENT.md)；owner [AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Temporally Extended Mixture-of-Experts Models](https://arxiv.org/html/2604.20156v1)

训练中的跨token允许expert集合不同于router每token实际激活和runtime驻留。 Ch21连续router段已补option/termination分支及质量代价，未把switch代理当实测传输。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_LAST_TWO_INDEPENDENT.md)；owner [MODEL-MOE](../../../../books/part-02-model/21-moe.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/html/2604.20157v1)

视频外观偏好不等动力学代理，更不等可控transition。 Ch25 perceptual plausibility→state→closed-loop及Ch66物理切片已有具体承载。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_THREE_EVAL_FINITE_INDEPENDENT.md)；owner [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [LLM-Guided Safety Agent for Edge Robotics with an ISO-Compliant Perception-Compute-Control Architecture](https://arxiv.org/html/2604.20193v1)

有限周期最大值与双板恢复不能证明WCET、ISO或完整安全响应。 sensor约2秒和reboot约40秒不与perception时间混账，中心资格保证隔离。 采用边界：中心保证隔离，不作正面Books证据；局部机制/实验及反证保留，作者勘误、条件证明或所指出确切实现/测量到达时定点重开。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_20193_FINITE_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG](https://arxiv.org/html/2604.20199v1)

多语言RAG候选、rerank、answer效用应按证据语言分别定位。 Ch76已加同候选池的证据语言切片；oracle最高答案语言不作为在线选择器。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_20199_CH76_WRITE_AFTER_INDEPENDENT.md)；owner [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows](https://arxiv.org/html/2604.20200v1)

公开分数访问面和压力循环可能改变coding agent行为，隐藏gate需独立。 Ch66 EvalSpec proxy段已落实；提示缓解不是访问隔离，403/462计数冲突不采用。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_20200_WRITE_AFTER.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Hallucination Inspector: A Fact-Checking Judge for API Migration](https://arxiv.org/html/2604.20202v1)

SDK符号/局部类型oracle只验证其scope，不等完整程序正确。 Ch66 deterministic schema/verifier→开放judge的规范身份与漏报分账已承载。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR02_THREE_EVAL_FINITE_INDEPENDENT.md)；owner [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Scaling Self-Play with Self-Guidance](https://arxiv.org/html/2604.20209v1)

自生成题支持集、solver熵、可解率与组内奖励退化形成反馈环。 Ch33 self-play段已新增guide代理/难度/奖励分账及冻结题库回退；两消融同时改变Guide的混杂保留，实际写后通过。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_20209_FINITE_EVIDENCE.md)；owner [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [Layer-wise Geometric Approximation Rates for Deep Networks](https://arxiv.org/html/2604.20219v1)

特构网络逐层prefix读出逼近界不等实际训练误差逐层下降。 有限深度混合激活、实数系数条件和数值成本，尚不改变普通Transformer设计。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_20219_INDEPENDENT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Hybrid Policy Distillation for LLMs](https://arxiv.org/html/2604.20244v1)

同offline prefix上expert/student采样的非对称更新有不同支持集。 受限梯度控制不自动等严格KL或全on-policy，保实验分支而非改写通用蒸馏法。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Cortex 2.0: Grounding World Models in Real-World Industrial Deployment](https://arxiv.org/html/2604.20246v1)

真实→imagined的progress/risk/termination评价器迁移需另验。 固定模型和planning预算局部取舍，不由低层频率推高层实时deadline或真实安全。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Rethinking Where to Edit: Task-Aware Localization for Instruction-Based Image Editing](https://arxiv.org/html/2604.20258v1)

增/删/替换需不同source/target编辑定位，mask只是状态控制代理。 latent reinjection不保证最终像素不变，全局改动/多分离区域失效，限作者图像编辑。

[必要证据及具体反证](../_sources/daily-20260423/V3_ROOT_LAST_FINITE_REVIEWS.md)。本批必要证据与最终处置已由[非作者有限复核](../_sources/daily-20260423/V3_APR24_LAST_FINITE_INDEPENDENT.md)通过；整合项另核实际正文及邻接，不以作者笔记代替验收。

### [ATIR: Towards Audio-Text Interleaved Contextual Retrieval](https://arxiv.org/html/2604.20267v1)

冻结audio encoder后的retrieval token选择与encoder压缩是不同训练责任。 selector/pooling及ASR配对只支持受限任务，embedding时间不是端到端SLO。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR01_SEVEN_PLUS_FOUR_DISPOSITION_AUDIT.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [Rethinking Intrinsic Dimension Estimation in Neural Representations](https://arxiv.org/html/2604.20276v1)

几何估计曲线、true dimension与任务能力不能相互替代。 Ch12实际补测度/估计/能力边界；非紧支持Hausdorff分支证明争议不采用。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_20276_CH12_WRITE_AFTER_INDEPENDENT.md)；owner [MODEL-EMBEDDING](../../../../books/part-02-model/12-embedding.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。

### [X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/html/2604.20289v1)

少步AR视频沿chunk复用residual，持久KV clean-pass仍完整计算。 Ch24跨chunk缓存/commit已实写；skip表文冲突和DiT部分计时不用于速度保证。

[必要证据及具体反证](../_sources/daily-20260423/V3_APR20_LAST_TWO_INDEPENDENT.md)；owner [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。未变化的具名独立结果复用；不由单篇通过推出日级完成。


## 5. 缺口与下一步

普通可执行工作：无。52家族必要审阅与处置、17项真实Books及其非作者写后、日期和日级终审均已完成。下列隔离项不是普通待审，不用于正面采用；以后材料到达只定点重开。

以下是本窗已隔离的外部终态保留项，不用于正面证据、不支持Books或无遗漏断言；访问/日期恢复只定点重开该项：

- OpenAI Research Index：RSS已核但Index历史分页未得；可接受本窗官方历史列表或原始事件链接，重开来源差集。
- Google Research Publications / DeepMind：Blog不替代论文目录；可接受本窗官方目录/归档分页，重开这一来源覆盖，不能靠全年搜索称闭合。
- Meta、DeepSeek Research、Moonshot2026 Blog、MiMo日期目录、MiniMax Agent Tech Blog：各原入口与失败/停止见§2；分别缺本窗历史日期列表/官方原始事件。材料不足仅隔离对应覆盖，不由不可达推出没有论文。
- [20329v1](https://arxiv.org/html/2604.20329v1)：Google日期04/22只到自然日，可能早于本窗；需要官方首次公开时刻或可信原始归档，重开归属与后续贡献，不计52。不是零分。
- Seed [ContextUnrolling](https://arxiv.org/abs/2604.21921v1)与[Seed3D2](https://arxiv.org/abs/2604.21443v1)：官方paper/blog日期bucket不能确定09截点；可接受官方首发时刻/原始公告身份，重开两个家族日期，不以arXiv提交字段替代。
- 10个中心争议见§3/4对应原文与具名反证；分别需所指明方程/假设/实现/评估更正，而不是泛化“全文不可读”。当前均已有必要材料和审阅，争议不是普通待审，也不将所有作者实验删掉。20276的非紧支持证明、20289速度方向、20200计数冲突仅隔离子主张，不妨碍有独立支持的机制。

## 6. 复核

复核者：apr24_close（非本日报与相关新增正文作者）；apr01、apr02、apr20_resume的既有有限具名结果按身份/v1/命题未变复用。
结论：通过

实际[日级终审](../_sources/daily-20260423/V3_APR24_INDEPENDENT_FINAL_REVIEW.md)逐项核52候选、相应证据与最终Books处置，以及17真实正文及邻接；来源入口/停止范围与有界日期均已核。发现并修正19795误用提交日期、19925误报分母、四个写后独立性缺口、19857缺具名反例及未具名撤回计数。否定侧分层复用/定点核15个具名样本，另检查20130具体范围桥；未将78全部排除或490原始库存说成全文复核，未发现需扩大重开的共同错误。外部目录、日期和中心争议仍按§5隔离。

最终V3结构/评分/引用校验与本日限定差异检查通过；脚本不证明研究语义。未stage、commit或push，已有无关和暂存修改保留；仓库其它既有告警不由本日验收覆盖。
