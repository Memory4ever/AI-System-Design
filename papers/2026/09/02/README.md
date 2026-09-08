# Daily Research — 2026-09-02

**规范：** V3
**窗口：** 2026-09-01T09:00:00+08:00 ～ 2026-09-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T16:43:01+08:00

## 1. 结论

本日报沿用户认可的题摘初筛继续，不重扩原始池、不继承旧完成标签。实际书稿增量围绕量化与缓存的状态边界、生成/诊断代理与真实行为的区别，以及Agent累计风险与独立授权。

四个arXiv主类官方公开批次共有521个去重原始身份：368项读完整题摘，153项标题已明确范围外。初筛拟留128项经独立核验移出3项、漏检抽查恢复2项，机构定点触发另恢复Qwen-Drive；加3项机构/工程材料得到131个工作身份。00002和00351存在日期身份冲突，移入缺口后，**本窗确定候选129个家族（126个arXiv + 3个机构/工程）**。这是审查对象，不是129项稳定长期贡献。

普通作者待审为0；126项完成当前采用命题所需证据审阅，另2项中心证据争议、1项必要artifact缺失。Books决定为**整合11项、已有覆盖76项、仅报告39项、暂缓3项**。11项实际增量落入10章，Ch11输出监督粒度和Ch54 UMA容量/恢复边界也已写后独立通过。普通作者与独立审阅、逐ID整稿检查均已结束；来源/日期限制、两项中心争议和一项artifact缺口已经隔离，不用于候选正面结论或Books写入，作为本窗终态保留项定点重开。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Path to Astra 的核心说明与官方 RSS Sep01 13:00Z；本窗北京时间21:00；Sep03 overview 为后续事件，不混入  原始检查 | 已检查 | 无 |
| SRC-ANTHROPIC | 复用官方 Research 相邻日期 Sep04→Aug28/Aug26 的定点检查  原始检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | Agentic Video首发JSON-LD Sep01 17:00Z恢复在窗；另复用共享日期检查，不重扫年级目录 | 受阻 | 1项贡献候选；另两项研究页只标2026不能分配日窗 |
| SRC-META-AI | Muse Spark1.3 Sep02 08BJ首发及evaluation methodology已有核心审查；新卡另按arXiv首次公开去重  原始检查 | 已检查 | Muse只能力/版本与非匹配排名，未披露新机制，贡献排除，不作零命中 |
| SRC-QWEN | 中英文发布API定点日期与Qwen-Drive触发的官方cs.CV Wed2公开批次  原始检查 | 已检查 | 论文00111恢复本窗；Sep03 Blog是后续重复，不按提交日改归属 |
| SRC-DEEPSEEK | 官方API Updates日期边界Aug21→Aug13已跨过本窗  原始检查 | 已检查 | 无 |
| SRC-MOONSHOT | FlashKDA精确commit及GitHub事件时刻；Kimi0.40属于下一窗口，迁移提示不入选  原始检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 共同中国来源检查；用户Research目录截图可见最新Aug28 | 受阻 | 尚缺完整可读取目录与原文链接，不能将截图扩大为完整覆盖 |
| SRC-ZAI | 同一共同记录；官方研究目录时间排序，Aug26→Aug14→Jun16已越过窗口  原始检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research/Blog/Publication定点日期检查，最新已早于窗口  原始检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方博客最新May09，下一页为更旧内容  原始检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 共同记录已恢复原始route/frontmatter/iframe；Blog日期Jun10/Jun8/May30及更旧，Paper区亦早于本窗  原始检查 | 已检查 | 无 |
| SRC-MINIMAX | 中英文研究列表最新Aug13；官方llms→techblog.md恢复May13 AgentTeam目录  原始检查 | 已检查 | 无 |
| SRC-ARXIV | 官方Wed2 cs.AI/LG/CL/DC批次，521身份的当前初筛见逐项记录 | 受阻 | 初筛521项及126项arXiv候选作者审阅完成；00002/00351日期身份冲突单列，不纳入确定本窗分母 |

本轮只使用每日分组与具体触发，不加载每周来源。来源实际检查的限制不因没有拟留候选而消失。
原始列表与题摘路径、日期依据及补检范围见初筛预览。

## 3. 候选与判断

评分按 Design Delta + System Reach + Durability，各0–3分。标准/深入完成只表示采用命题得到相应审阅，不认证全文所有结论或附件。三项暂缓不计证据完成；各项Books决定的具体理由在下一节。

arXiv时间采用官方Wed2公开批次对应北京时间Sep02 08:00，不使用submitted日期代替；本轮映射核验已明确不再加一天。机构时间分别来自原RSS、JSON-LD和精确commit事件。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [OpenAI — Path to Astra](https://openai.com/index/path-to-astra/) | 2026-09-01T21:00:00+08:00 | 3 + 3 + 3 = 9；贡献问题：能力阈值触发暂停、受限访问与独立控制，检验发布责任而非从外部行为猜测内部机制 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Google Agentic Video（机构窗口恢复）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) | 2026-09-02T01:00:00+08:00 | 2 + 1 + 3 = 6；贡献问题：问题驱动视频时段、帧率和模态读取，补全表示节到推理取证循环的交接 | 深入完成 | 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [trajectory-judge 2609.00038](https://arxiv.org/html/2609.00038v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：观察面控制、clean/silent/loud与定位分母 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [REAL-Q: E2E LLM Quantization via Dynamic Gradient Descent](https://arxiv.org/html/2609.00049v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：冻结Hessian的逐层PTQ近似可能误估后续损失，动态块校正改变误差反馈路径 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling](https://arxiv.org/html/2609.00051v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：拒绝被分解为检测头、安全神经元和输出头的可干预路径，而非单一拒绝方向 | 深入完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes](https://arxiv.org/html/2609.00052v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：Agent接口移除文本后，工具动作仍可构成模型身份指纹，包装变化和模型替换需分开识别 | 深入完成 | 已有覆盖 — `PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/html/2609.00060v1) | 2026-09-02T08:00:00+08:00 | 3 + 3 + 2 = 8；贡献问题：跨授权、凭据、支付和履约阶段的绑定漏洞可绕过各阶段局部校验 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration](https://arxiv.org/html/2609.00061v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：训练塌缩可能压低概率而非删除能力，基座与策略的反事实组合提供修复分支 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [RePro: Proof-Verified Benchmark Rewriting for Reliable Evaluation of LLM Mathematical Problem Solving](https://arxiv.org/html/2609.00062v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：防污染改写也可能破坏题意，形式证明把改写有效性与答案校验分开 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Attention Sensitivity Is Not Enough: Dissociating Attention-Level and Behavioural In-Context Learning under Fine-Tuning](https://arxiv.org/html/2609.00064v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：直接提高attention解释代理不一定提高行为ICL，给代理目标训练提供受控反证 | 深入完成 | 整合 — `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization](https://arxiv.org/html/2609.00066v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：NVFP4共享scale让离群通道损害陪伴通道，通道配组成为硬件约束下的新误差控制量 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://arxiv.org/html/2609.00067v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：先看文本可能污染视觉证据，context-blind witness把观察与仲裁分离 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/html/2609.00069v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：自改harness可改动授权或评价器而伪造任务收益，改变自改系统允许修改的边界 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops](https://arxiv.org/html/2609.00077v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：程序编辑表面多样却算法语义收敛，in-loop与blind评价揭示自改研究的模式塌缩 | 深入完成 | 已有覆盖 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [RW-LoRA: Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks](https://arxiv.org/html/2609.00078v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：模型状态随机游走替代多副本gossip聚合，通信减少以更新串行化为代价 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Commit-first LLM judging inherits the judge's own errors](https://arxiv.org/html/2609.00088v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：judge先承诺答案可把可操控锚点移入judge自身，防操纵策略依赖judge先验正确性 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Safin-1: Safety from Within through Memory-Native State Evolution](https://arxiv.org/html/2609.00092v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：共享backbone之外引入结构化路由持久状态，原生状态适配与权重适配分工不同 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding](https://arxiv.org/html/2609.00097v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：低比特候选扫描与attention计算融合，去掉选择阶段全局同步和外置元数据 | 深入完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](https://arxiv.org/html/2609.00103v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：记忆正确率受上下文可压缩性与误差成本影响，单一长度不能表达有效容量 | 标准完成 | 已有覆盖 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Qwen-Drive-1.0（机构触发恢复）](https://arxiv.org/html/2609.00111v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 3 = 6；贡献问题：辅助训练latent与可执行行动解耦，检验共享表示、梯度权与部署控制的边界 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Lingua Franca or Probing Artifact? Rethinking Latent Language in Multilingual LLMs](https://arxiv.org/html/2609.00155v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：隐状态几何和输出可解码性对内部语言给出不同判断，限制英语中介推断 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](https://arxiv.org/html/2609.00161v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：平均去噪损失弱化稀疏交互区域，局部误差信号重分配可改变动作结果监督 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [WHALE: A Simple Recipe for Joint Harness-Weight Optimization](https://arxiv.org/html/2609.00196v1) | 2026-09-02T08:00:00+08:00 | 3 + 3 + 2 = 8；贡献问题：固定harness优化权重与固定权重优化harness可能彼此失配，需研究交替优化的耦合 | 深入完成 | 已有覆盖 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation](https://arxiv.org/html/2609.00206v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：视频时间片段与音画跨模态局部无害内容可组合成危害，单片审查不覆盖组合语义；并非多轮对话 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning](https://arxiv.org/html/2609.00213v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：固定多奖励投影可把不同奖励画像混叠，产生聚合本身诱发的reward hacking | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Invalidation Contracts for Cross-Episode Agent Memory](https://arxiv.org/html/2609.00243v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：服务端有效性戳与planner遵守失效协议是两件事，缓存正确性不能由版本戳独自保证 | 标准完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems](https://arxiv.org/html/2609.00275v1) | 2026-09-02T08:00:00+08:00 | 3 + 3 + 2 = 8；贡献问题：逐动作权限成立仍可在共同触发下透支整个fleet风险，需要累计剩余损失预算 | 深入完成 | 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Exact Global MCMC with Denoising Diffusion](https://arxiv.org/html/2609.00279v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：以扩散路径密度构造MH校正，允许不完美denoiser作为精确采样proposal | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](https://arxiv.org/html/2609.00293v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：视觉与文本冲突时证据权重可能不对称，模态对齐不等于知识冲突可仲裁 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Workload Identification with Physical Side Channels for AI Governance](https://arxiv.org/html/2609.00309v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：物理GPU侧信号可独立于软件自报核验训练/推理活动，但受任务与对抗扰动影响 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Two locked tests of phase-structure features for transition prediction](https://arxiv.org/html/2609.00335v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：以null控制重新检验RoPE相位解释，避免把相位几何相关性当成机制 | 受阻 | 暂缓 — 见§5 |
| [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/html/2609.00355v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：融合视觉状态被一次块draft复用，grounded低熵任务可优于逐token草稿，开放文本仍有链式优势 | 深入完成 | 已有覆盖 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Deterministic LLM Inference Across GPU Kernels: Power-of-Two INT8 Quantization Scales and the Limits of Tolerance-Based Conformance](https://arxiv.org/html/2609.00363v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：INT8近似容差可能掩盖epilogue错误并虚增性能，bitwise核验改变正确性门槛 | 深入完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference](https://arxiv.org/html/2609.00407v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：异构NPU/NDP执行把expert复用、放置和代价建模耦合，而非单纯按参数均分 | 标准完成 | 已有覆盖 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [How Temporal Correlations Shape Memory in Linear Recurrent Neural Networks](https://arxiv.org/html/2609.00420v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：线性循环网络的记忆学习受输入时间相关性约束，不仅由状态维度决定 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [(V)LMs generalize beyond surface co-occurrence: Evidence from cross-modal number agreement](https://arxiv.org/html/2609.00443v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：跨模态新词与数关系的受控干预可区分抽象规则迁移和共现记忆 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Group Adaptive Clipping Policy Optimization](https://arxiv.org/html/2609.00444v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：由advantage调整importance-ratio clipping以改变更新有效性；不是组内投影 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference](https://arxiv.org/html/2609.00450v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 1 = 5；贡献问题：大block硬件效率与量化精度冲突，误差补偿需在真实执行分块下成立 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Towards a Belief-Based World Model for LLM Agents](https://arxiv.org/html/2609.00455v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：世界模型不仅生成未来画面，还可供belief查询，改变状态可询问性的评价对象 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Toppling the Hierarchy in Byte-level Language Modeling](https://arxiv.org/html/2609.00463v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：字节层级下采样可能损害字符信息，提供压缩表示与语言能力的受控反证 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Exploring Collaboration between a language and a non-language agent](https://arxiv.org/html/2609.00474v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：内部决策能力与对外语言沟通能力可不匹配，影响异构Agent协作的能力估计 | 深入完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [The Privacy-Hallucination Tradeoff in Differentially Private Language Models](https://arxiv.org/html/2609.00492v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：差分隐私与训练事实频率共同改变输出错误形态，隐私保证不等于事实可靠性 | 争议 | 暂缓 — 见§5 |
| [Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models](https://arxiv.org/html/2609.00495v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：扩散拒绝涉及多位置迭代commit而非AR开头拒绝，安全控制位置需要重定 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Validity-Aware Jailbreak Evaluation 2609.00498](https://arxiv.org/html/2609.00498v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：独立validity oracle、retrieval依据和比较配置 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space](https://arxiv.org/html/2609.00515v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：跨语言因果迁移证据可检验共同语义中介，不能仅凭输出英语推断内部语言 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents](https://arxiv.org/html/2609.00549v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：技能使用的选择偏差会让总体收益与同任务实际使用效应异号 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](https://arxiv.org/html/2609.00550v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：同一证据转为图像或文字可改变参数知识与上下文的优先级 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](https://arxiv.org/html/2609.00575v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：压缩误差按expert整体输出而非独立投影最小化，需考虑MLP内部误差耦合 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning](https://arxiv.org/html/2609.00605v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：forget样本与实际已学知识不对齐可能使unlearning梯度改错对象 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows](https://arxiv.org/html/2609.00643v1) | 2026-09-02T08:00:00+08:00 | 3 + 3 + 2 = 8；贡献问题：新证据到来时依赖图选择性撤销工作，区别于整段重跑或无条件保留旧结果 | 深入完成 | 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Patterning in Practice: Debiasing Reward Models with Susceptibilities](https://arxiv.org/html/2609.00699v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：局部posterior响应指导偏好数据重权；粗去偏目标可能误伤合理拒答/回应切片 | 深入完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](https://arxiv.org/html/2609.00727v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：音频风格信息可被encoder保留却不被decoder使用，识别瓶颈不能只看表征可读性 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Online Self-Weighted Fine-Tuning](https://arxiv.org/html/2609.00734v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：按在线成功rollout加权但保持专家梯度的SFT形成不同于RL的优化分支 | 标准完成 | 已有覆盖 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis](https://arxiv.org/html/2609.00746v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：视觉适配可能削弱既有attention sink，相关诊断与因果损伤需区分，后插归一化不等于原生QK norm | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [How Do Language Models Choose Between Context and Memory?](https://arxiv.org/html/2609.00753v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：可读或可steer的上下文方向不一定被模型自然复用，因果使用量不同于探针准确率 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [A Unified Mechanistic Analysis of Knowledge- and Safety-Based Refusals](https://arxiv.org/html/2609.00760v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：知识不足与安全拒绝共享方向但迁移不对称，上层再区分拒绝理由，不能把两种拒答视为同一能力 | 深入完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Frozen Cores Need Task Signal: Fisher-Whitened Cross-Covariance for Low-Resource LLM Adaptation](https://arxiv.org/html/2609.00762v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：冻结子空间内优化坐标改变LoRA可训练参数尺度，子空间选择影响误差 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Instella-MoE Technical Report](https://arxiv.org/html/2609.00791v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：Gated MLA、稀疏层执行与AMD训练配合形成可检查的开放MoE设计分支 | 深入完成 | 整合 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [SFAD: Speculative Factuality-Aware Decoding](https://arxiv.org/html/2609.00796v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：事实目标直接steer target logits，不能称对原target分布无损的speculation | 标准完成 | 已有覆盖 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Characterizing the Scalability and Performance of Large-Scale AI Training Under Multi-Tenancy](https://arxiv.org/html/2609.00817v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：大规模多租户训练的通信争用证据可能改变独占集群下的并行选择 | 标准完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents](https://arxiv.org/html/2609.00823v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：后续压力能改变Agent已作出的停止决定，需核对计划承诺何时真正约束行为 | 标准完成 | 已有覆盖 — `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [Visual Attention Faithfulness in Vision-Language Models is Heterogeneous](https://arxiv.org/html/2609.00830v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：视觉attention的必要性和充分性并不相同，干预可校正热图解释 | 标准完成 | 已有覆盖 — `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [Probabilistic Model Checking of Autoregressive Neural Sequence Models](https://arxiv.org/html/2609.00838v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：对自回归输出做概率模型检查与保守反例细化，提供不靠采样估计的验证分支 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Does Fault Localization Beat a Fresh Attempt? A Placebo-Controlled Study of Test-Guided Code Repair](https://arxiv.org/html/2609.00854v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：定位故障的反馈可能不如盲重采样，placebo控制限制反思收益归因 | 深入完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [MemoryWalker: Stop Training Agents on Contexts They Never Saw](https://arxiv.org/html/2609.00865v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：淘汰上下文后的分支轨迹不是原始线性序列，错误linearization可改变训练梯度 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Visual Insensitivity Gap: Diagnosing When Vision-Language Models Fail to Use Visual Evidence](https://arxiv.org/html/2609.00868v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：视觉信息在encoder可用却未被语言输出消费，需要分开衡量提取与使用 | 争议 | 暂缓 — 见§5 |
| [Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry](https://arxiv.org/html/2609.00873v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：扩散语言模型的记忆泄漏在token位置上可能不同于AR，影响隐私攻击评价 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [CacheBridge: Efficient Cross-Model KV Cache Transfer](https://arxiv.org/html/2609.00891v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：跨模型KV复用需要可校准的头/表示映射，不能把缓存视为模型无关文本前缀 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [In-Context Neurofeedback: Can LLMs Control Their Internal Representations through Privileged Access?](https://arxiv.org/html/2609.00904v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：模型获知内部反馈不等于能控制自身表征，针对内省能力主张的反证 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference Voting](https://arxiv.org/html/2609.00905v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：只用成对偏好构造MH接受准则，提供无显式奖励密度的采样分支 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO](https://arxiv.org/html/2609.00925v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：不同后训练目标对已有grounding电路的影响不同，不能把收益统称为学会推理 | 标准完成 | 已有覆盖 — `TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling](https://arxiv.org/html/2609.00949v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：总体任务准确率可掩盖动作类别校准差异，状态grader不能替代动作风险检查 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CoBRA: Learning Tool-Use Boundaries via Counterfactual Margins](https://arxiv.org/html/2609.00967v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：工具调用的反事实边际收益可用于训练，而非把调用本身当作成功信号 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](https://arxiv.org/html/2609.00993v1) | 2026-09-02T08:00:00+08:00 | 3 + 3 + 2 = 8；贡献问题：DeepEP共享协议状态与collective顺序使原地PD切换受跨rank约束 | 深入完成 | 已有覆盖 — `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/html/2609.01004v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：高范数视觉sink与内容重要性不等价，影响visual token pruning依据 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](https://arxiv.org/html/2609.01024v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：条件执行单位下沉到expert内部组合路径，改变专家作为最小调度单元的假设 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [The Multiple Timescales of Gradient Descent on the Edge of Stability: A Perturbative Derivation of the Central Flow](https://arxiv.org/html/2609.01034v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：edge-of-stability训练用多时间尺度中心流解释，区别于静态局部曲率直觉 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](https://arxiv.org/html/2609.01035v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：递归子Agent授权的风险须按组合证书控制，局部安全不能直接推出整体界 | 深入完成 | 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [From Truncation to Commitment: Persistent Context in Uniform Discrete Diffusion](https://arxiv.org/html/2609.01043v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：持续保留选中token与逐步截断是不同扩散过程，影响迭代纠错的状态寿命 | 深入完成 | 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Lagged Coupling: Internal Representations Become Readable Before They Become Causal](https://arxiv.org/html/2609.01048v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：训练中表征先可读取、后才产生行为因果作用，限制探针作为能力里程碑 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://arxiv.org/html/2609.01068v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：复用speculative draft轨迹预测输出长度，减少独立长度预测器成本 | 标准完成 | 已有覆盖 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](https://arxiv.org/html/2609.01091v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：蒸馏可能传递未显式监督的行为特征，需区分知识转移与隐性trait传播 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts](https://arxiv.org/html/2609.01100v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：路由共同模态漂移会影响专家分工，以EMA分离公共项的路由机制值得核验 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP](https://arxiv.org/html/2609.01103v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：缩小CLIP模态间隙可能加重hubness并降低预测，否定距离越近越好的代理 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Replicating TRACE: A Practitioner's Guide to Its Threshold and Particle Budget](https://arxiv.org/html/2609.01108v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：对既有TRACE主张的复现显示效果受lag与估计器底噪约束，需收窄因果解释 | 深入完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs](https://arxiv.org/html/2609.01117v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：冻结LM上递归latent状态增加计算深度，能力变化不等于增加参数知识 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Scaled Idempotence in Transformer Attention: Paired OV Geometry and Shared-Value Algebras](https://arxiv.org/html/2609.01129v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：OV投影的代数结构限定头如何读写表示，补全attention权重之外的机制 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Does task decomposition improve automatic NLG evaluation?](https://arxiv.org/html/2609.01139v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：judge分解的收益可能来自人工标签而非分解本身，需控制监督来源 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [On the Design Fundamentals of Pixel Text Representation Learning](https://arxiv.org/html/2609.01147v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：原生分辨率、渲染和训练目标共同影响像素语言模型，不可把变化归给单一输入形式 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](https://arxiv.org/html/2609.01161v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：不同层级版权防御可在泄漏与退化间产生不同边界，不能只按拒答率选择 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training](https://arxiv.org/html/2609.01170v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：预先划分模块与训练后形成模块可能承担不同因果作用，挑战仅从最终结构推断学习过程 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://arxiv.org/html/2609.01215v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：VLA策略重构为可执行技能库需保持rollout等价与回报，压缩不是任意代码替换 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Prompt-Robust Language Models: Which Training Strategies Work?](https://arxiv.org/html/2609.01217v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：prompt鲁棒训练的改进可能被复现条件和梯度冲突解释，简单模板基线不可漏掉 | 深入完成 | 已有覆盖 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Multi-Head Self Attention is a Parameter Identification Mechanism](https://arxiv.org/html/2609.01231v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：多头参数的gauge不唯一影响机制识别，应区分可识别函数与参数坐标 | 深入完成 | 已有覆盖 — `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [Position Matters: Feature Inversion Attacks in ViT Split Inference with Token Reduction and Shuffling](https://arxiv.org/html/2609.01232v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：split ViT的位置打乱可被逆向恢复，位置变换不是可靠隐私屏障 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](https://arxiv.org/html/2609.01235v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：可变记忆的canonical/trust epoch更新协议改变旧值与修订值的可用性 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Post-Training Science for Supervised Fine-Tuning](https://arxiv.org/html/2609.01244v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 3 = 7；贡献问题：跨模型SFT的学习率与损失代理缩放研究可能改变小模型调参向大模型迁移方式 | 深入完成 | 已有覆盖 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](https://arxiv.org/html/2609.01245v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：仅终局回报下稀少探索信号与KL约束耦合，需区分无信号与更新失败 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](https://arxiv.org/html/2609.01249v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：重建路径可洗去水印，改变水印验证面对变换攻击时的保证 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [From Base Rollouts to RL Reasoning: A Budgeted Search Perspective](https://arxiv.org/html/2609.01274v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：RL后的搜索收益曲线不能直接证明基础能力新增，需与基座搜索恢复比较 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models](https://arxiv.org/html/2609.01277v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：音视频联合latent局部时间重映射提供时序控制，不依赖整体重新生成 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives](https://arxiv.org/html/2609.01282v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：解释传播规则跨算子必须守恒，operator覆盖不足会影响归因正确性 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reliability Challenges in Diffusion Vision-Language Models](https://arxiv.org/html/2609.01318v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：dLVLM首步长度先验与晚commit可能造成AR不同的可靠性失效 | 标准完成 | 已有覆盖 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [mzCache: On-Device LLM Memory Management under Multitasking](https://arxiv.org/html/2609.01338v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：移动多任务内存压力下细粒度共享缓冲支持GPU推理与CPU恢复并行 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Probing Factual Knowledge Transfer with Training Data Interventions](https://arxiv.org/html/2609.01341v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：训练数据定点移除显示跨语事实迁移可能被共现残留和简单负例高估 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](https://arxiv.org/html/2609.01343v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：循环MoE在FLOPs、参数和KV同时匹配后仍可能有收益，排除额外计算混杂 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades](https://arxiv.org/html/2609.01345v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：cascade用自身verifier计算质量可在真实错误上升时显示改进，闭环指标存在结构性盲点 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR](https://arxiv.org/html/2609.01354v1) | 2026-09-02T08:00:00+08:00 | 3 + 2 + 2 = 7；贡献问题：RLVR验证器对等价答案和数值容差发生可证明错误，直接污染奖励与排名 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs](https://arxiv.org/html/2609.01356v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：翻译的目标语序形成和表层语言实现可分离，细化内部语言生产机制 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA](https://arxiv.org/html/2609.01361v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：truth probe跨语体相对稳定却跨语料失效，数据结构可伪装成真实性方向 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Behaviorally Effective LoRA Writes Are Sparse and Structured](https://arxiv.org/html/2609.01374v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：同一checkpoint换写入子空间会改变后续行为，有效LoRA写入比原rank更集中 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [When Tokenization is Secretly Output Supervision](https://arxiv.org/html/2609.01386v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：输入与输出tokenization解耦显示监督粒度而非仅输入表达改变数值学习 | 深入完成 | 整合 — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching](https://arxiv.org/html/2609.01404v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：导航成功却无法正确终止任务，视觉能力不能证明动作协议完整性 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search](https://arxiv.org/html/2609.01431v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：调参实验目标从单点最优转为缩放规律的不确定性，改变小规模实验预算分配 | 标准完成 | 已有覆盖 — `WORLDVIEW-SCALING-LAW` [Ch7](../../../../books/part-01-worldview/07-scaling-law.md) |
| [Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning](https://arxiv.org/html/2609.01449v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：带持久状态且无timestep的迭代器可在推理不去噪，扩散可能只提供训练curriculum | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning](https://arxiv.org/html/2609.01455v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：良性微调破坏拒绝可能来自低秩输出路由锐化而非泛化的梯度冲突 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices](https://arxiv.org/html/2609.01457v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：权重绑定使服务端可直接监督hidden state，split微调可去掉逐步双向通信 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers](https://arxiv.org/html/2609.01466v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：trace fold的正确率收益可由简单scratchpad解释，剩余价值是审计而非更强推理 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](https://arxiv.org/html/2609.01491v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：效率压力和事后约定可能形成不可人读通信，新协议的创造与学习条件不同 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall](https://arxiv.org/html/2609.01532v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：forward KD在mid-training可伤害事实学习却保留推理收益，阶段变化影响目标选择 | 标准完成 | 已有覆盖 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](https://arxiv.org/html/2609.01549v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：竞争环境中分散世界模型面临可识别性障碍，集中动力学与策略影响需分开 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories](https://arxiv.org/html/2609.01556v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：结构近邻已在top-k却被表面词形压低，lexical reranker在不同域可反向作用 | 标准完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [H3-World: Turning Language Understanding into World Control](https://arxiv.org/html/2609.01560v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：语言动作对齐时间latent并限制attention区间，可把粗生成控制转为时段控制 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs](https://arxiv.org/html/2609.01573v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：SFT/RL标注预算的近最优区域可跨模型规模迁移，不必追单一最优比例 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally](https://arxiv.org/html/2609.01587v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：因果恢复精度显示损伤信号不等于可修复层，统一细粒度量化可优于局部补bit | 标准完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Mechanism Design for Alignment and Control](https://arxiv.org/html/2609.01595v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：能力可隐藏而不可伪造的假设下，诚实与服从需联合激励，监督保证有形式边界 | 标准完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |
| [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](https://arxiv.org/html/2609.01596v1) | 2026-09-02T08:00:00+08:00 | 2 + 2 + 2 = 6；贡献问题：联合动作与接触力预测把相似进度但不同接触后果分开评价和训练 | 深入完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation](https://arxiv.org/html/2609.01604v1) | 2026-09-02T08:00:00+08:00 | 2 + 1 + 2 = 5；贡献问题：judge的误差比较、汇聚和输出可由干预定位，微调雕刻已有通路而非全新评价器 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Moonshot — FlashKDA 数值纠错](https://github.com/MoonshotAI/FlashKDA/commit/7afb9f454f160a6c4bbc0999beca0a8c40a38934) | 2026-09-01T16:16:56+08:00 | 3 + 2 + 2 = 7；贡献问题：分块三角求解的混合精度纠错，区分精确代数、实际dtype与误差/资源合同 | 深入完成 | 仅报告 — 受限机制/反证保留，具体未整合理由见下文 |

## 4. 证据与知识整合

每项说明当前采用的精确版本和知识判断；完整配置、反证与未采用的headline留在原始证据笔记。以下不是把摘要重写成全文审阅。

### [OpenAI — Path to Astra](https://openai.com/index/path-to-astra/)

厂商能力阈值使development/release可以延迟、受限access和额外containment成为release条件；malicious user与模型自主未授权行为是不同威胁路径。20个近期V8内部样本及expert-hardened环境是厂商证据，不是所有系统的能力认证；Blue权限不同默认生产，首发仍计划soon availability。

当前Books已读Ch72风险框架/独立control及CoT monitor接口段，mitigation validation→residual-risk decision+owner已提供决策责任，Ch73 release gate承接。root判断足以承载阈值后hold原则，No Change — Existing Coverage；不因厂商首发版本事实再追加泛化阈值句，更不从外部行为推断内部模型机制。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [Google Agentic Video（机构窗口恢复）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

固定帧率全量输入改为query-conditioned acquisition：问题驱动时间段、frame rate、视觉/音频/transcript选择，内部tool读入后继续推理；不是仅codec tokenization或视频生成。首发benchmark缺可复算的全prompt/版本/预算合同，不采用通用88/66/7%收益，也不将token节省当端到端时延。

当前guide仅解释读取历史/续轮上下文、动态推理与工具往返计账边界，不作本窗新release或复现证明。实际Ch23 codec-aware末段原只有输入表示稀疏，欠推理中的读取控制分支；root核采用证据后授权，现已补极小段及Review notes并由root实际顺读上下文，Integrate — 独立写后复核通过。 当前owner：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。精确证据与边界。

### [trajectory-judge 2609.00038](https://arxiv.org/html/2609.00038v1)

初筛曾按“过程≠结果已知”排除；root完整题摘指出按outcome survives分层和final-reply观察盲区是具体新反证，恢复准入。当前评分3 / 2 / 2 = 7，深入采用命题证据复用；[HTML](https://arxiv.org/html/2609.00038v1)§3–9原独立审阅有效。

实际Books：Ch66“从Final Answer到Artifact、Process与Environment Evolution”已有完整silent/loud/clean、定位分母、最终回复支持和fault frequency边界。No Change — Existing Coverage；恢复候选不意味着重复插入书稿。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [REAL-Q: E2E LLM Quantization via Dynamic Gradient Descent](https://arxiv.org/html/2609.00049v1)

固定曲率近似的解析补偿未必跟得上已量化列造成的当前残差：v1 §4保留GPTQ式补偿，每个128列block后以当前输出损失梯度更新尚未量化权重。这里改变离线校准的状态与计算，不把新增反向/Adam成本藏进Serving收益；§6–7与Appendix D的条件和反证详见笔记。

Books比较：`INFER-TENSORRT-LLM` Ch49“二阶敏感度把Output Gradient带进量化Artifact”已有曲率/成本，但未区分冻结曲率近似与当前残差的顺序梯度补偿。root已独立核原文/邻段并授权；原节内已补该分支，保留静态补偿旧方案，章末来源已同步。Integrate — 已写入；root实际顺读原节与相邻交接后，写后复核通过。 当前owner：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。精确证据与边界。

### [From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling](https://arxiv.org/html/2609.00051v1)

v1 §3.1–3.2、§4.1–4.4通过最小差分、matched随机对照、双向patch及永久编辑后的重新验收，区分有害检测、残差中介与拒答输出。它支持受控电路验证链，不证明放大几个权重就获得普遍安全；OR-Bench和能力代价边界不能被单一安全率覆盖。

Books比较：实际读取Ch17“Layer冗余取决于干预协议”及前后residual机制；该段已完整写入minimal-pair→matched-random→双向patch→永久edit后adaptive/utility/副作用，且章末有本family精确来源。No Change — Existing Coverage；非复用旧标签，系当前正文真实存在。Ch16提供readout/causal-use前提，Ch72负责部署安全，不复制同一电路叙述。 当前owner：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。精确证据与边界。

### [AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes](https://arxiv.org/html/2609.00052v1)

当前准入：独立前64批次1放行，重点纠正“识别backbone”的强表述。重新读[HTML §3–4](https://arxiv.org/html/2609.00052v1)，旧note中的预算/对照与当前机制一致。

实際Books：Ch59“Identity必须覆盖模型行为”已写structured-action指纹、schema/prompt/sampling/budget/reference/calibration identity，以及重验证而非权重/provider证书；章末有本source。No Change — Existing Coverage。Ch58/60承担数据/运行对象，Ch72权限与攻击边界不重复。 当前owner：`PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md)。精确证据与边界。

### [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/html/2609.00060v1)

source-pinned x402/MPP/ACP/AP2模型把授权、请求、付款与履约关系分开，反例找missing binding→最小strengthening→复验，合法交易可达不能被deny-all替代。lost-response下entitlement可恢复、计费/去重原子一致，REST/MCP不能仅一侧要求幂等。

实际Books：Ch72 canonical action到异步结算段已包含entitlement、atomic replay protection、跨接口一致与证据分层。No Change — Existing Coverage；Ch78 action/Ch84平台权限承接而不重复支付模型。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration](https://arxiv.org/html/2609.00061v1)

来源：[精确 HTML](https://arxiv.org/html/2609.00061v1)，§4、§5、Appendix A训练协议；当前abs身份一致。

Books比较：Ch33已有correct-mode diversity、verifier与跨prompt区别，以及reference-regularized repair与adapter residual credit；当前collapsed策略与冻结base配对是该训练信号原则的一种实现，未证明必须改变长期设计结论。root复核同意 No Change — Existing Coverage；受reward约束的图像修复实例与反证留Daily，不把图像机制推广文本RL或另加方法段落。 当前owner：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。精确证据与边界。

### [RePro: Proof-Verified Benchmark Rewriting for Reliable Evaluation of LLM Mathematical Problem Solving](https://arxiv.org/html/2609.00062v1)

当前准入：独立前64批次1放行受限评测有效性命题；不是数学科学应用。重新读[HTML §3–6](https://arxiv.org/html/2609.00062v1)核实方法、分母、选择效应与重写敏感度。

Books比较：实际对读Ch66正式正文“Dataset是受治理的评估资产”（sampling/slice、provenance、contamination）、autoformalization的kernel/semantic gate，以及“Miscoverage要拆成Sampling Failure与Selection Failure”/“Adaptive Evaluation”中的尝试与选择记录。它们不是RePro-specific实现，但已能约束把retained correctness外推全量可靠率。No Change — Existing Coverage；具体generated/retained与题目难度选择留Daily，不用Review notes后历史残块充当正文，也不新增孤立论文节。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Attention Sensitivity Is Not Enough: Dissociating Attention-Level and Behavioural In-Context Learning under Fine-Tuning](https://arxiv.org/html/2609.00064v1)

来源：[精确 HTML](https://arxiv.org/html/2609.00064v1)，§3、§4、§5、Appendix B；当前abs身份一致。

Books比较：Ch15当前“可视化不是head唯一语义”覆盖静态解释警告，但缺代理作为训练目标后的变化。root独立读§3–5与实际邻段后授权窄补；已在同一论证后加入诊断→优化目标→独立行为验收的短连接，章末绑定精确来源。Integrate — 已写入；root实际顺读前例、新段、head分化与Review notes后通过写后复核；不复制整套ICS方法或通用evaluation章节。 当前owner：`MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md)。精确证据与边界。

### [OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization](https://arxiv.org/html/2609.00066v1)

来源：[精确 HTML](https://arxiv.org/html/2609.00066v1)，§3、§4、§5 limits；当前abs标题/版本/Comments已复核，未显示撤回。

Books比较：Ch49已有rotation/group/layout共版本化，缺共享scale“受牵连误差”的推导；root已独立核原文/邻段并授权，原节内已补误差单位→paired permutation→weight repair→融合执行短链。Integrate — 已写入；root实际顺读原节与相邻交接后，写后复核通过。 当前owner：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。精确证据与边界。

### [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://arxiv.org/html/2609.00067v1)

同一image/question先生成context-blind witness，再在arbiter引入text；leaky witness保持两次调用/提示但提前暴露text，才是隔离效应近似matched control。Witness-only到arbiter还混合描述压成answer与reconciliation，不单独证明后者作用。

实际Books：Ch66“Model Self-report不能拥有输入来源真值”已把provenance、matched cue与self-report分权；相邻EvalSpec完整对象与下游独立oracle要求使读者不能用视觉优先或单一judge自证。blind/leaky/staged是该原则的一组受限实验控制，并未证明必须采用新的生产路由。No Change — Existing Coverage；具体generator反转留Daily，不以缺论文术语为新增正文理由。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/html/2609.00069v1)

完整current diff和exact pre-change文件构成一个实际mutation；按functional role与七种obligation识别破坏。把tampered/benign改动植入同一位置追求相同表面功能，缓解只认生成风格，但按构造标签不等于现实风险真值。

当前Ch66“从Snapshot到Feedback-conditioned Policy”中harness可修改两段已真实写入diff/prechange、作用面、protected/provenance/completeness、lineage与falsepositive；邻段把生成evaluator交独立准入。No Change — Existing Coverage（作者定点复核，旧独立窄命题证据可复用。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops](https://arxiv.org/html/2609.00077v1)

Diff字符距离、描述embedding clusters、冻结mechanism taxonomy是不同sensor。DAPS用类别频率改变proposal选择、近200条描述去重，另用每10轮audit退回faithful checkpoint；只有gate读取audit，读后即validation不是blind。

当前Ch81 evaluator-driven search在production checklist拥有duplicate/lineage/独立评审，其后已要求component ablation确认真实机制、未参与搜索和蒸馏的finalholdout，并明确反馈过的test不再独立。论文taxonomy/embedding是可误分的sensor实现，不改变这些设计责任。No Change — Existing Coverage；代码表面多样性反例和matched-audit对照留Daily，不因新的组合方法而追加章节。 当前owner：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)。精确证据与边界。

### [RW-LoRA: Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks](https://arxiv.org/html/2609.00078v1)

一个mobile `(A,B)` token串行访问节点，在每站K步更新后按Metropolis–Hastings转移；不平均不同A/B，故不引入因子均值相乘的交叉项。target stationary distribution属于目标权重，不是任意图上天然公平；定理要求固定连通图/mixing、光滑/无偏/有界梯度及全过程factor norm有界，不能当故障恢复保证。

Books：Ch36已有目标权重与参与频率、网络/同步语义，Ch30给factor参数化。论文具体单token轨迹可作为后续去中心训练分支，但当前只证明固定拓扑/IID下通信账目，未建立本项目平台可采用的并发/恢复边界。仅报告 — 受限实验替代路线，不声称现有正文已逐项描述RW，也不强行追加通用故障协议来替论文补证据。 精确证据与边界。

### [Commit-first LLM judging inherits the judge's own errors](https://arxiv.org/html/2609.00088v1)

DeepEval G-Eval4.1.5、Opus4.8judge、Sonnet5generator、四个Python小函数、12×8候选best-of-N。selector只读visible tests及judge score；heldout在每batch固定后执行但不反馈。

当前Ch66“Scorer不是绝对真相”明确固定judge/prompt/sampling/rubric，用人工或可执行verifier校准关键slice；相邻reward-feedback段又禁止judge独占reward与releaseauthority。commit-first的反向案例强化该结论，不证明新生产门槛；仅冻结judge自解答案当然不满足现有独立oracle要求。No Change — Existing Coverage。保存committed answer及reachable checks是实验复现要点，留Daily；三次求解不设通用阈值。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Safin-1: Safety from Within through Memory-Native State Evolution](https://arxiv.org/html/2609.00092v1)

recurrent state不断演进，anchor checkpoint是累积前缀而非分段重置；共享anchor embedding读取本层snapshot，经前层生成state-aware key。token同时softmax选择历史anchor、持久可学习state和零payload null，readout加到当前state path。

当前Ch22 recurrence、WRITE/READ和state continuity已区分固定有损state、显式历史访问、临时state与Agent durable memory；本文addressable state-bank是值得保存的实验实现分支，但尚不推翻其取舍。仅报告 — architecture exploration，不因‘安全state’名称修改安全治理章节，不把具体持久bank等同现有全部机制。 精确证据与边界。

### [Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding](https://arxiv.org/html/2609.00097v1)

Key拆2bitthumbnail与8bitresidual，Query全扫thumbnail，sink/local pseudo-max设delta阈值，selected blocks补residual和值。pseudo-max低估只相对同一评分的理想阈值保守，不消灭量化false negative；未选项仍删除，重建也只是nearFP16，不能叫dense lossless。

Ch45“固定Top-k到Top-p”已要求score estimator误差、selected精算、线性扫描/metadata成本及FullKV回退；Ch49拥有融合和graph执行。delta降低global reduction是局部可用实现选择，不改变‘近似选择须按质量与完整成本验收’的已有结论。No Change — Existing Coverage；不说现有Ch45已讲top-delta公式，具体算法留Daily。 当前owner：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。精确证据与边界。

### [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](https://arxiv.org/html/2609.00103v1)

synthetic16symbol、候选3–6长的精确membership、每stream16query，低熵LZ约0.7与4bit对照；自然video密度是heuristic，labelprior也不同，不能把其全部差值叫压缩能力。九VLM及RAG-like比较，FLOPs由shape解析且假定一query/stream，不是profile、物理显存或多query摊销性能。

当前Ch22“先拆四种能力”与“Effective utilization”已分接收长度/有效使用/物理容量及拒答/成本；Ch66拥有分布/校准/完整对象验收。此处entropy控制是这些原则的重要实验化，而非把FLOPs提升为唯一效率尺度。No Change — Existing Coverage；synthetic容量和payoff反例保留在Daily，不重构全书memory taxonomy。 当前owner：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)。精确证据与边界。

### [Qwen-Drive-1.0（机构触发恢复）](https://arxiv.org/html/2609.00111v1)

v1的辅助视觉未来状态用于训练共享表示，不能把训练期latent当成部署时可执行控制或持久world state。采用命题的精确方法/评价记录区分数据、梯度所有权与运行接口；本项由Qwen机构线索触发恢复，不重扫整个cs.CV。

实际Books：Ch26“Action-facing Representation也是Gradient Authority Boundary”至“Training-only Foresight不是Persistent World State”已有共享表示/训练权、辅助监督、部署接口和causal/control边界，Ch5拥有可读与实际使用差异。No Change — Existing Coverage；同一长期原则不因driving/BEV命名再追加。 当前owner：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。精确证据与边界。

### [Lingua Franca or Probing Artifact? Rethinking Latent Language in Multilingual LLMs](https://arxiv.org/html/2609.00155v1)

同hidden state经language-conditionedGMM与raw/tunedlogitlens后语言分类给出不同分布。前者测geometry后者测finalunembedding可读性；raw偏English、tuned向最终输出语言移动，不能由任何一种断言唯一内部语言。

当前Ch5“可读三层”与最后mechanism诊断段已明确信息存在、reader解码、行为因果使用及freshprobe/observereffect；邻接Ch4函数机制、Ch6计算图不需复制语言实例。No Change — Existing Coverage；本paper受控反例提高已有警告的证据，不要求每种probe有单独正文。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](https://arxiv.org/html/2609.00161v1)

全局像素均方误差会把大量权重分给静态背景。方法用冻结Qwen2.5-0.5B抽取被操纵物体词，以其cross-attention作区域prior，再以detached local prediction error在8个采样候选区域间分配权重，归一化加权denoising loss，背景仍保留单位权重。

实际Books：Ch25“从重建Observation到预测可推进Representation”已有reconstruction容量分配、task-relevant supervision与action-conditioned outcome边界；Ch15刚补训练解释代理仍需行为验收。本方法的区域采样与gradient routing是受限实现，不足以要求统一world-model loss改用它。No Change — Existing Coverage，主文复合指标的反向子项保留在报告。 当前owner：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。精确证据与边界。

### [WHALE: A Simple Recipe for Joint Harness-Weight Optimization](https://arxiv.org/html/2609.00196v1)

model theta与executable harness h构成trajectory policy：固定h做verifier-accepted RSFT，再固定更新后的theta搜索tool/schema/parser/context/termination。D_weight与D_harness分开，fixed/patience切换；不是同时梯度，也无joint optimum保证。

实际Ch81 evaluator-driven artifact搜索段及后续holdout段绑定artifact/evaluator/budget/lineage，Ch59 identity/组合绑定覆盖权重与wrapper，Ch33/29拥有weight-update信号。No Change — Existing Coverage：当前具体alternation策略留报告；原counterpart上的最好结果不能授权新pair，是现有identity/revalidation原则，不因新增配对名词扩章。 当前owner：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)。精确证据与边界。

### [Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation](https://arxiv.org/html/2609.00206v1)

研究单位是视频时间段与音画重组，不是多轮对话。各部分无害而组合有害，full vs shuffled isolated人评构成具体控制；20人/144视频能支持该构造的组合效应，但不认证任意viewer一致语义。

实际Ch72 pre-guard检查窗口段已有chunk overlap、模型可见范围和丢跨块组合语义的风险；Ch23时空对齐/provenance段拥有模态、时间轴和读取identity。No Change — Existing Coverage：本证据将既有组合检查原则落到视频受控反例，不要求为每种媒体复制一套gate。具体评价分母/正反例留报告。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning](https://arxiv.org/html/2609.00213v1)

固定scalar聚合会把不同reward profile合并并偏向容易维度。以EMA shortfall/volatility/progress乘积动态调权，和DRBO、删信号、additive/prior以及GRPO/GDPO/PPO对照保持data/prompt/rollout其余超参；受测static scalar升而accuracy降是聚合失真的具体反例，不是所有固定权重必然失败。

当前Ch33“Verifiable Reward优势与边界”明确格式压正确性、多组件scale改排序及独立heldout/adversarial检查，phase-specific/typed credit后续承接控制。仅报告：动态调权是可验证替代分支，暂未改变全书已有reward contract；不把自适应参数法升格为通用推荐。 精确证据与边界。

### [Invalidation Contracts for Cross-Episode Agent Memory](https://arxiv.org/html/2609.00243v1)

机制：server拥有table/key版本与依赖，client缓存recovery suggestion；table-wide清除会误删未变化row，rowdiff只删受影响项并restamp其余。依赖传播需走pre-reload旧图，因旧边可能被新值删除。

实际Books：Ch77“先分解Memory组件”（write/freshness/answer use分开）与“派生结论”到PlanFence的正式正文已说明当前source版本、依赖失效、送达≠重新推导、细粒度依赖成本以及缺依赖/恶意owner边界；Ch78/81拥有effect-time执行。No Change — Existing Coverage。pre-reload snapshot和规则hash是该原则的实现案例，不为每种API字段另补正文。 当前owner：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)。精确证据与边界。

### [The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems](https://arxiv.org/html/2609.00275v1)

per-call权限正确不等fleet累计风险可控；trusted registry按tool/spec/schema/receipt归类effect，外部pricer用补偿后的残余损失quantile定价，agent不能自定风险。沿agent→workflow→tenant所有ledger原子reserve，再confirm/cancel，例外由authority另开审计allocation，不能悄悄扩普通budget。

实际Ch84 scheduling段原只有run/tenant预算与resource/providerquota，欠宣告风险计量与真实损失的两层保证。root独立读exact§3–6和Ch84/81/72后批准极小补，现已在原预算段后写入层级预留、可信身份/定价与loss边界；root实际顺读上下调度/AgentRM过渡及Reviewnotes后写后PASS，Integrate已验收。不把概念资源模型当部署完成的AgentOS。 当前owner：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)。精确证据与边界。

### [Exact Global MCMC with Denoising Diffusion](https://arxiv.org/html/2609.00279v1)

不是“denoiser准确所以sample精确”：固定共享top-noise状态，对原forward path与新reverse path作MH，接受率包含两条路径的Gaussian概率和目标未归一化density，未知常数抵消；可计算目标density与正variance/fullsupport是条件，不能直接把同算法用于未知真实图像分布。与局部MALA复合保持同一stationary分布，差denoiser可令global move几乎冻结，理论不等有限时间有效混合。

实际Ch24 Draft/Verify/Correct及distributional correctness段已区分proposal、target accept/reject与质量，Ch48拥有自回归speculation。这里是 Principle Reuse，不是diffusion替代AR或把MCMC稳定分布等同单次token无损。仅报告：保留通用生成/采样机制证据，但当前采用不要求把连续density的完整MCMC算法混进自回归commit节；未提出新结构owner。 精确证据与边界。

### [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](https://arxiv.org/html/2609.00293v1)

固定context→entity→query顺序，context仍为文字反事实，entity为名字或照片；先筛能认出照片且两种模态都能正确回忆事实的model-specific集合，Llama3-8B同时筛选与判答案。故不是共同固定全集准确率，也不是图像渲染相同passage的00550设置。

Ch23语义/时空/行动对齐和Ch5受控干预/读出/行为的分权已经要求不能由相似或输出偏好认定因果使用；本paper进一步给出实体解析时序的受限解释，但不能据此规定通用输入排序或backpatch策略。仅报告 — 机制案例；不谎称现有Books已写该layer-specific链，也不把每个机制案例追加为新生产结论。 精确证据与边界。

### [Workload Identification with Physical Side Channels for AI Governance](https://arxiv.org/html/2609.00309v1)

一张H200 NVL，外部Rogowski交流电流探头包围PCIe辅助供电正线；10MHz采样、5秒窗口、30个主要频谱特征与两阶段random forest。探头无DC响应，测的是动态纹理不是直接总能耗。

实际Ch72“Hardware Attestation也必须声明Adversary Tier”已要求测量对象、硬件/firmware、证据链、验证者与对手假设，并保留现场/独立审计回退；其后片上边界不将物理sensor当证明。本方法是该合同下独立sensor的一种实验实现，不改变校准、误报与信任责任。No Change — Existing Coverage；特征/阈值及受控反证保留Daily，不给安全章追加分类器配方。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [Two locked tests of phase-structure features for transition prediction](https://arxiv.org/html/2609.00335v1)

Study1封存比较1136eligible/175positive，99%BCa区间跨零且增量未达预先0.05；1063replication只检方向不救primarygate。Study2在b0–b4的1415transition/480group上20×5groupfold，15层/池化treatment的规则要求平均增量、至少4/5block同向与block均值均成立，所有失败，b5/b6未打开。

暂缓 — 仅记录作者声明的null，机制/复算证据仍Partial。Ch13当前只采用RoPE旋转与相对位置机制，未绑定旧理论2607.25507；不据此修改数学结论，也不把这一弱可复算案例升级成普遍治理实验。P2材料请求：作者Study1pipeline/result与Study2Artifact4/5原始或可读导出、模型/数据身份、PC/基线特征定义及评估配置；可接受官方仓库或作者原附件。无需未授权b5/b6数据，不追另一篇理论来代填实验披露。 精确证据与边界。

### [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/html/2609.00355v1)

冻结Qwen3-VL8B，5层1.05B blockhead读取五层已融合hidden states，而非重新视觉编码；一次输出offset marginals，product score仅排序候选，ancestor-mask target逐节点持有真正conditional并提交最长正确greedy路径。Marginal product不等联合分布，开放文本后缀依赖强时链式draft更可靠；固定head tree-vs-chain说明width贡献，但不证明head大小完全无关。

实际Ch48“parallel refinement draft”及相邻architecture/statisticaldependency、targetverify、拒绝prefixcommit已经区分同类机制；cost章节要求accepted progress覆盖draft/verify及状态成本。GLANCE是多模态条件下的具体实现和适用性案例，未要求更换canonical机制。No Change — Existing Coverage；融合视觉是条件信息复用而非视觉必然提高速度，跨attentionfusion的排序反转留Daily，不给正文追加新的熵普遍定律。 当前owner：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。精确证据与边界。

### [Deterministic LLM Inference Across GPU Kernels: Power-of-Two INT8 Quantization Scales and the Limits of Tolerance-Based Conformance](https://arxiv.org/html/2609.00363v1)

采用：合法epilogue运算自由与错误舍入都可落在一个BF16 spacing内，因此容差验收不等kernel可互换。Qwen3-1.7B九类故障/三severity/两scale的8232cells支持此盲区；预测矩阵经smoke与事后纠正，不能称完全预注册无调整。

实际Books：Ch49“量化acceptance contract”及下一量化分布段，现有两段完整包含verifier故障检测力、条件性逐位一致、requantization与dtype/identity共同冻结。No Change — Existing Coverage；原单篇独立证据有效，当前正文绑定已作者回读。 当前owner：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。精确证据与边界。

### [DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference](https://arxiv.org/html/2609.00407v1)

Router先确定激活expert，host按各expert token量、NPU/NDP算力、resident缓存令PMove为零及共享PCIe/CXL成本排序，再扫描排序prefix选择NPU子集。只是限定排序空间的最佳split，不是任意assignment全局最优证明。

实际Ch54 expert residency/miss下界段已区分按路由缓存、prefetch overlap、大expertbatch摊薄与低并发搬参压力；推理调度接手工作量/资源选择。DynaNDE给出特定NPU/NDP限制下的实现选择，未推翻已有数据移动判断。No Change — Existing Coverage；三阶段共享link合同与有限prefix搜索留Daily，不把模拟排序法升为必须采用的平台scheduler。 当前owner：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。精确证据与边界。

### [How Temporal Correlations Shape Memory in Linear Recurrent Neural Networks](https://arxiv.org/html/2609.00420v1)

同singularvectors、时点内whitened、跨时协方差为Cij乘identity、alignedinitialization使线性RNN平方损失在任务mode解耦，gradientflow保留该子空间。每mode输出增益g乘时间向量v(b)，损失中的输出平方项变为g²vᵀCv/2；时间相关性不等跨mode相关性。

Ch4/5现有数据/目标/架构共同决定学习、Ch22容量与有效利用分离足以防止“状态维数独自决定实际记忆”的设计误用。仅报告 — 理论解释案例；不将上述线性条件推到现代LLM，更不新增“相关性总是免费memory”的无条件正文。 精确证据与边界。

### [(V)LMs generalize beyond surface co-occurrence: Evidence from cross-modal number agreement](https://arxiv.org/html/2609.00443v1)

Qwen3-VL2B/4B冻结模型，仅训练两个新token的tied embedding/unembedding；视觉组以单/多生物图与不泄露数的caption训练，语言组有agreement线索。30样本、50初始化seed，2800最小对测试及0–3干扰词。

仅英语、一个家族两小模型、受控新增embedding；预训练本就包含语言抽象，不证明凭几张图从零学会语法。H100/RTX6000Ada，其他不采用性能数值；不推广为所有VLM无词频依赖。实际Ch5“记忆与泛化不是简单对立”及因果证据阶梯明确允许共享计算与局部记忆共存，并要求干预/跨context确认。No Change — Existing Coverage；该反例增加窄证据，不需要把新词实验完整复制进正文。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [Group Adaptive Clipping Policy Optimization](https://arxiv.org/html/2609.00444v1)

Binary reward、组内中心化但不std归一化，正确样本advantage=(k-c)/k；upper clip随该advantage放宽，下界固定，loss使用GSPO长度几何平均ratio。只改clip headroom，不是重新投影组内梯度，也不直接补采成功样本。

Ch33 DAPO Clip-Higher、DrGRPO统计单位、GSPO约束单位和后文conditional band已清楚说明clip控制更新而不创造reward真值，并要求ratio/normalization/预算匹配。No Change — Existing Coverage：本例改变clip分配规则而非这些长期设计责任；具体稀有成功slice、同checkpoint干预及理论落差保留报告，不再增加一组算法清单。 当前owner：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。精确证据与边界。

### [HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference](https://arxiv.org/html/2609.00450v1)

大L1 block摊薄FP scale/accumulator，内层2bit SIG微块scale恢复局部动态范围；W离线逐block择SIG2/3，A/KV用SIG1，W4A5、L1=128、微块8或32。微块内fixedpoint归约后再L1dequant，scale metadata与额外L2逻辑不能算零；psum每次从MXINT8恢复FP16累加再压回，近似并非数学无损。

逐步消融区分A5、L1变大、SIG补偿与psum量化：SIG恢复质量也增加能耗，最终收益来自组合。HBQ-E reasoning质量低于接近等精度的HBQ-A/对照，故不能使用E最快数字同时宣称A质量。仅报告 — 特定ASIC的可检查实现分支；Ch49量化/scale/layout/accumulation及tile成本已有长期责任，不新增GPU支持或宣称通用最佳bitwidth。 精确证据与边界。

### [Towards a Belief-Based World Model for LLM Agents](https://arxiv.org/html/2609.00455v1)

Policy可不提供假设action直接查询当前belief，与simulate(action)分开。这里belief是手写准确状态空间和更新：已知全部receptacle、由gameengineplacement规则给uniform支持、看见/未看见就collapse/renormalize；没有unknown-location类别。

实际Ch25核心区分observed/latentbelief/imaginedstate，后文belief-state/inference validation独立于transition，Ch77外部memory拥有来源/修订而非把推断当事实。No Change — Existing Coverage；这里是暴露当前不确定性的具体接口证据，不需要新建worldmodel owner或把手写oracle当通用学习方案。 当前owner：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。精确证据与边界。

### [Toppling the Hierarchy in Byte-level Language Modeling](https://arxiv.org/html/2609.00463v1)

固定byte IO下改变character/word层数量、位置及attention/FFN作用粒度；whitespace取样、residual保留原位，首尾full-character。100M/400M、12/24层、1B/4Bword，单H100/BF16、2048长度。

Ch11已有byte fallback只是开放覆盖、字符/byte/token不等、跨tokenizer预算按稳定信息单位核算；Ch15拥有attention的信息访问。仅报告 — 条件架构反证：保留压缩计算影响字符能力这一实验路线，而非宣称现有章已有全部层级模型机制，亦不因缺某布局名称而新增正文。 精确证据与边界。

### [Exploring Collaboration between a language and a non-language agent](https://arxiv.org/html/2609.00474v1)

Frozen Lc0penultstate→3layerMLP→32continuousinputtokens，get_policy文本摘要仍给两组，LLAMIA额外latent。先5Mstatepolicy对只训projector，再DAPO联合LLM/projector；injectedtokens不属于采样actionloss但梯度穿过projector。

平均calls减少抵消每call32tokens只是作者负载，训练4B/14B接近6%但8B 16.8vs15GPUh已约12%，不重复“每种规模均6%”；表中token/query主要工具输出计量，不当完整reasoning成本。No Change — Existing Coverage：实际Ch82latent通信节已明确序列化损失、对齐/版本/回退、不可读embedding只作proposal，并保留可审计text；这里是固定specialistpair的训练型受限实例，不因“非语言agent”另造协议保证。 当前owner：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md)。精确证据与边界。

### [The Privacy-Hallucination Tradeoff in Differentially Private Language Models](https://arxiv.org/html/2609.00492v1)

GPT-J6B按已知预训练cutoff选后2020Wiki文章，20K背景+355专题；FactScore用Llama3.1-8B拆claim/检索原Wiki/裁决并CORE去冗余。5人分层30article复核但不是全量独立truth，pretraining事实与article日期也不是同一概念。

暂缓 — 独立复核后仍为中心证据争议。可以保存经限定的隐私/事实可靠性反证，但sequence/document单位未闭合，不能靠收窄文字将family标为通过。Ch72隐私信任边界、Ch66独立事实verifier已不将低perplexity或privacyclaim当正确性；本次不向Books写有争议的unit保证、固定频率阈值或“DP必然使所有模型幻觉增加”。 精确证据与边界。

### [Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models](https://arxiv.org/html/2609.00495v1)

LLaDA8B/Dream7B Base/Instruct，prefill拒绝或顺从序列的128response位置控制，以及单token不同stepcommit说明早期计算步与文本前部位置不是同一变量。拒绝token在unsafe轨迹也常出现，predict/top1不等真正commit；这不证明一个“拒绝神经元”控制所有安全。

仅报告 — 受限decoder安全替代路线。Ch24已有provisional/committed、跨step稳定不等正确与完整输出验证，Ch72保留独立安全边界；本例具体词表控制和前8步启发式不升为默认生产机制。token未committed与已对外发布又是两种承诺，不把内部freeze直接叫执行授权。 精确证据与边界。

### [Validity-Aware Jailbreak Evaluation 2609.00498](https://arxiv.org/html/2609.00498v1)

方法：保留原句抽取step，先分类sequential/unordered/single；step内容/relevance由检索辅助judge，顺序依赖先打乱再推graph，另call检查原顺序，解析失败仅回退位置检查。最终由LLM按rubric合成actionability，不是独立确定性真值，也不以各step概率相乘。

可长期采用：non-refusal/policy violation与可执行有害能力是不同评价轴，后者需要内容、依赖及完整性；错误内容也可能已违反refusal policy，不能判“安全”。Books对读Ch72 residual-risk段原有有害帮助≠实际损害，但未明确这两个轴；root授权后，已在该段后补两句并加章末精确证据边界。Integrate — 已写入，root实际顺读上下文后写后复核通过；不添加SEAV方法流程或性能headline。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space](https://arxiv.org/html/2609.00515v1)

Llama3.1-8B/Aya23-8B的18语言行为分解显示source/target能力可解释所测翻译变化；加入一个bilinear项没有改进，不排除任意pair-specific机制。MultiBLiMP每语言200例且接近饱和，BLEU与GlobalMMLU也不能等同完整语言能力。

No Change — WORLDVIEW-REPRESENTATION / Ch5。实际对读“从可读出到机制”及“信息存在、可读与被使用”相邻段，已明确行为分解、一阶归因、局部干预和跨环境复验不能混为完整机制。此处受限跨语言案例留Daily，不以新名词追加第二套解释理论。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents](https://arxiv.org/html/2609.00549v1)

固定task/seed/decoding比较skill-enabled与disabled，OAE对所有配对任务计helpful−harmful；RAE只在enabled实际返回skill的子集上作同任务差值。未配对的“调用 vs 未调用”lift混入题目难度；但RAE仍条件于处理后的调用选择，不是无需假设的总体因果效应，也不能隔离toolprompt、搜索、context变化与真实skill内容使用。

No Change — PLATFORM-EVALUATION-SYSTEM / Ch66。实际对读“Skill必须在真实Control Path中评估”的noSkill→oracle→selection→productionretrieval链及前后受控intervention/版本化EvalSpec；已有设计要求是不以工具出现或强制正确上下文当实际收益。RAE的条件分母和失配contentcontrol作为本报告测量边界保存，不把它推荐为通用无偏估计器或向Books追加论文指标清单。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](https://arxiv.org/html/2609.00550v1)

13VLM先按各自closed-book五次一致答案筛选，随后将冲突证据作为text或renderedimage，并在multi-evidence中交换模态/顺序。这个model-specific“parametricknowledge”分母不等groundtruth；EFR要求三次均追随外证，追随counterfactual证据不等事实正确。

No Change — MULTIMODAL-REPRESENTATION / Ch23，handoff Ch66。已对读Ch23 fusion后truthauthority与“任务贡献/当前可靠性不能共用Gate”，Ch66输入来源真值与matchedcue干预。现有正文不把modality或selfreport当truth；具体gap和渲染策略留本报告，不改成统一图像优先/文本优先设计。 当前owner：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。精确证据与边界。

### [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](https://arxiv.org/html/2609.00575v1)

每expert三投影分解为sharedbase与expertresidual。压缩某hidden维时删gate/up残差对应行和down残差对应列，该维仍由base贡献，不是整个神经元归零；以原expert输出与base-only替换的单维贡献差平方估计importance，而非分别最小化三矩阵Frobenius误差。

仅报告 — INFER-TENSORRT-LLM / Ch49。已对读数值执行/二阶output-sensitive校准及其runtime边界；其长期原则已具备，本例sharedbase替换和单维局部近似是受限压缩分支，不为方法差异新开正文。没有把压缩率当实际GPUmemory，也没有把离线时间摊薄当每次部署都免费。 精确证据与边界。

### [Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning](https://arxiv.org/html/2609.00605v1)

TOFU受控20目标每人15QA分为已注入且要求忘、已注入未要求、未注入但要求各5；Llama2-7BChat只注入前两组。单步GA的一阶梯度内积预测各set损失变化，重复计算不是完整优化轨迹定理；扣retain损失后，所测遗忘不自动扩散到同entity漏列事实，未注入目标的梯度又可增加utility损害。

No Change — PLATFORM-SECURITY / Ch72。实际对读“Unlearning必须分开参数擦除与推理拒答”及前后retainedutility、backflow和部署artifact段；已有不以一次probe未命中/拒答证明擦除的长期结论。当前以本例明确说明题集遗漏与多余目标的不同失败，并保留selfconsistency不能确定真实知识边界；不把CONFS写成权威知识清单或生产删除完成器。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows](https://arxiv.org/html/2609.00643v1)

每attempt读immutable snapshot，记录data/controlselector、parentattempt与journal起点；结构迭代另记collection membership。revision typedpatch生成delta，与reads相交再遍历受影响后代，分别cancel/avoid/recompute或暂时continue/reuse。

Integrate — AGENT-WORKFLOW / Ch81，独立证据及写后复核通过。root实际核验§3、§4.1与Appendix A.6，并对读原有恢复段后授权；现L520三句将aligned suffix恢复连接到最终read certificate/journal重验的分支复用，保留unknown扩重算及进程内锁的边界。root已实际顺读新增段、两侧交接及Review notes并通过；没有将运行计数写成全部独立adversarial试验或生产保证。 当前owner：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)。精确证据与边界。

### [Patterning in Practice: Debiasing Reward Models with Susceptibilities](https://arxiv.org/html/2609.00699v1)

Gemma2-9B在Skywork训练RM，SGLD局部posterior上的RM-Bench splitloss与训练pairloss协方差估计susceptibility，再对期望observable变化作未正则pseudo-inverse，得到数据重权并从头重训。理论为局部线性posterior响应，不是实际AdamW重训路径保证；有限SGLD偏差、inverse估计不稳与实验order-one coupling均由作者说明。

No Change — TRAIN-RLHF / Ch31，handoff PLATFORM-EVALUATION-SYSTEM / Ch66。实际对读Ch31 Bradley–Terry差值、preference数据的length/style/分布偏差与Ch66目标/holdout分离；已有“奖励代理必须独立验收且跨切片回归”的设计结论。局部susceptibility重权仅为昂贵实验分支，不追加为标准去偏recipe。 当前owner：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。精确证据与边界。

### [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](https://arxiv.org/html/2609.00727v1)

Expresso四speaker七style、同text同speaker跨style，meanpoolhidden/CKA与LOSO线性probe，再与开放toneprompt映射输出比较。Qwen2Audio/Qwen2.5Omni/Chroma等不是只改变单一训练目标的matched模型；Whisper仅使用encoder作ASR基线，不宣称Whisper模型本身没有decoder。

No Change — MULTIMODAL-REPRESENTATION / Ch23，handoff WORLDVIEW-REPRESENTATION / Ch5。实际对读encoder/projector与alignment目标边界，Ch5证据阶梯已完整区分信息存在、probe可读、行为使用。将模型比较和GRL有限失败留Daily，不把相关架构差异写成唯一机制。 当前owner：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。精确证据与边界。

### [Online Self-Weighted Fine-Tuning](https://arxiv.org/html/2609.00734v1)

每batch从专家题解取监督方向，当前policy作K次rollout估binarysuccess，stopgradient权重1−p_hat后做weightedSFT。它不是只训练成功rollout，也不是原expectedreward policygradient的代数恒等式；替换成功条件分布为一条oracle并丢负分支是surrogate设计。

No Change — TRAIN-SFT / Ch29。实际对读“从平均拟合转向覆盖尚未学会的序列”及末段选择器/监督allocation边界，已保留uniformSFT、tail筛选与能力回归。在线successweight作为替代实例留Daily，不因读者未见方法名就追加正文，也不称优于一般RL。 当前owner：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)。精确证据与边界。

### [Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis](https://arxiv.org/html/2609.00746v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00746v1) §3–5、Limits、Appendix B.1–B.3/F.3；未审Appendix A完整证明，不将理论保证计为已验证。

当前Ch14 sink/no-op与Ch17 normalization/intervention边界足以防止把相关诊断当通用因果机制。仅报告 — 受限适配诊断；保留‘适配可能削弱既有sink’而非‘视觉引入sink’，不强制所有模型采用新归一化。 精确证据与边界。

### [How Do Language Models Choose Between Context and Memory?](https://arxiv.org/html/2609.00753v1)

2 / 2 / 2 = 6，标准审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00753v1) §2–6及Appendix A/B/C；abs v1 Sep01 05:35:36Z，无撤回说明。

实际Ch5已有‘可读信息→reader解码→行为因果使用’与独立干预验证链，邻接模型计算图不需要新增authority方向术语。No Change — Existing Coverage。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [A Unified Mechanistic Analysis of Knowledge- and Safety-Based Refusals](https://arxiv.org/html/2609.00760v1)

2 / 2 / 2 = 6；因采用拒答机制边界，深入审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00760v1) §3–5、Limits、Appendix A.4–A.6/C/D.2；abs v1 Sep01 05:43:04Z，无撤回说明。

实际Ch17最小差分→matched random→双向patch→永久编辑后新checkpoint验收已包含这些必要责任，Ch72承担真实授权。No Change — Existing Coverage；不为具体两类拒答再建一套机制正文。 当前owner：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。精确证据与边界。

### [Frozen Cores Need Task Signal: Fisher-Whitened Cross-Covariance for Low-Resource LLM Adaptation](https://arxiv.org/html/2609.00762v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00762v1) §3–6、Limits、Appendix A.4/B.3–B.5/G.5/H.2；未将未读A.2证明当已验证。

实际Ch30 rank/targetmodule与trainable/base/activation/artifact分账已承载采用结论。仅报告 — 受限冻结子空间替代分支；保留坐标和span的具体控制，不将短任务结果变成通用LoRA替代建议，也不声称Ch30已有完整FCCA。 精确证据与边界。

### [Instella-MoE Technical Report](https://arxiv.org/html/2609.00791v1)

3 / 2 / 2 = 7，深入采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00791v1) §2.1–2.3、2.8–2.9、3.3–3.4及Appendix A；未采用未完整审阅的数据混合/预训练recipe细节。

已实际对读Ch21 dispatch/overlap到runtime handoff及Ch36分布式数学不变量：现有等价执行优化不足以代替‘为重叠主动改变模型依赖’的区别。Integrate — Owner MODEL-MOE / Ch21：独立reviewer实际重读§2.1.3/Eq2–3、§3.3.1/Table13、§3.4/Appendix A后放行，root授权文件锁；L310窄连接及Reviewnote已写，独立reviewer实际顺读上下handoff后PASS，锁释放。不在多章重复recipe。 当前owner：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)。精确证据与边界。

### [SFAD: Speculative Factuality-Aware Decoding](https://arxiv.org/html/2609.00796v1)

2 / 2 / 2 = 6，标准采用命题审阅完成；性能/理论保证不采用。实际读[精确v1 HTML](https://arxiv.org/html/2609.00796v1) §3–5、6.2/6.4/6.6、Limitations与Algorithm；abs v1 Sep01 06:46:54Z，v2 Sep03在窗外，不替代v1；无撤回说明。

实际Ch48‘draft优于target则进入效用仲裁’与exactacceptance/residual规则已清楚分离分布保持和质量改变。No Change — Existing Coverage（仅采用目标改变的可核机制）；未证明性能与事实保证留为报告局限，不把争议headline写Books。 当前owner：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。精确证据与边界。

### [Characterizing the Scalability and Performance of Large-Scale AI Training Under Multi-Tenancy](https://arxiv.org/html/2609.00817v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[精确v1](https://arxiv.org/html/2609.00817v1) §II、IV、V-C、VII及V中的对应边界；v1 Sep01 07:17:17Z，Sep03 v2在窗外，无撤回。

实际Ch36通信原语、payload/topology/runtime版本与profile要求足以承载所采用的系统判断。No Change — Existing Coverage；有价值的是通信模拟与实训分界/噪声反例，不把synthetic吞吐作为平台设计默认阈值。 当前owner：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。精确证据与边界。

### [Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents](https://arxiv.org/html/2609.00823v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00823v1) §3–7主要机制/对照、Limits、Appendix A.2/A.4/B.1/B.3；v1 Sep01 07:24:53Z，无撤回。

当前Ch79cumulativeconstraintledger、verificationreserve、termination≠correctness，Ch81commitowner已有完整边界。No Change — Existing Coverage；probe可提议继续/组织，不能代替环境证据授权Complete。 当前owner：`AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md)。精确证据与边界。

### [Visual Attention Faithfulness in Vision-Language Models is Heterogeneous](https://arxiv.org/html/2609.00830v1)

2 / 1 / 2 = 5，标准采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00830v1) §3–4、Limits、Appendix A/C；v1 Sep01 07:32:01Z，无撤回。

已对读Ch15热图解释后‘独立行为干预不能由attention proxy取代’及新00064限定，足够承载采用原则。No Change — Existing Coverage；不为一次小样本模式聚类新增解释taxonomy。 当前owner：`MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md)。精确证据与边界。

### [Probabilistic Model Checking of Autoregressive Neural Sequence Models](https://arxiv.org/html/2609.00838v1)

2 / 2 / 2 = 6，标准机制与界限审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00838v1) §3–5，包括所采用mass-preservation证明草图；v1 Sep01 07:37:55Z，无撤回。

仅报告 — 有限生成空间的形式化验证分支，Owner PLATFORM-EVALUATION-SYSTEM。当前Ch66真实外部oracle/EvalSpec及Ch20sampling可衔接，但尚未证明该指数展开方法适用于目标大模型生产规模；不强制增加模型检查小节，也不把未探索质量判safe。 精确证据与边界。

### [Does Fault Localization Beat a Fresh Attempt? A Placebo-Controlled Study of Test-Guided Code Repair](https://arxiv.org/html/2609.00854v1)

3 / 2 / 2 = 7，深入采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00854v1) §3–5、Appendix D–F；v1 Sep01 07:48:51Z，无撤回。

计划是内部pre-specified非外部preregistered；publictest盲区、processhash旧span须checkpoint恢复、解析/timeout旧缺陷均明确保留。实际Ch80局部诊断/repair与Evaluation的成本、选择偏差、回归，加Ch66matchedintervention已足够承载采用的反证。No Change — Existing Coverage；不把oracle强信号的反结果写成普遍禁用reflection。 当前owner：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)。精确证据与边界。

### [MemoryWalker: Stop Training Agents on Contexts They Never Saw](https://arxiv.org/html/2609.00865v1)

3 / 2 / 2 = 7，深入采用命题审阅完成。实际读[精确HTML](https://arxiv.org/html/2609.00865v1) §3–6机制与主要实验、Appendix E.1/F.3/F.4/G；未认证全部variational/convergence推导。

实际Ch33‘opaqueharness→exactcall evidence→trajectorytree→sharedtoken一次’及后续mask/position/kernel责任已覆盖采用的训练输入身份原则。No Change — Existing Coverage；具体SDCC近似与可疑physicalunion简化留Daily，不向书稿引入未经证明的高阶等价结论。 当前owner：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。精确证据与边界。

### [The Visual Insensitivity Gap: Diagnosing When Vision-Language Models Fail to Use Visual Evidence](https://arxiv.org/html/2609.00868v1)

Family: Disputed。独立审阅确认主文全分布KL与Appendix top50实现之间未闭合的定义冲突；以下诊断边界可以有限采用，不代表该family Evidence Passed，也不把不采用冲突数字等同解决冲突。

BF16/A10080GB，7B单卡/32B两卡，greedy、binary8/open64 tokens；不把32 GPU小时或单例时间当生产SLO。仅报告 — 诊断方法及其信息目标/解析分母边界，Owner WORLDVIEW-REPRESENTATION / PLATFORM-EVALUATION-SYSTEM。Ch5已有可读信息与因果使用区别；本例尚未证明新的encoder-to-decoder因果损失，不为名称新增Books机制。 精确证据与边界。

### [Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry](https://arxiv.org/html/2609.00873v1)

3 / 2 / 2 = 7，隐私采用命题深入审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00873v1) §3–5、Limitations、Appendix D.1–D.2；未认证Appendix A完整理论证明。

仅报告 — diffusion攻击面与受限统计替代，Owner PLATFORM-SECURITY。实际Ch72已把观察面、参考信息、query budget及经验攻击≠数学隐私保证分开，Ch66拥有matched/selection测量责任；本轮不把具体Q-Skew统计当安全默认，也不虚称Books已有其专门算法。 精确证据与边界。

### [CacheBridge: Efficient Cross-Model KV Cache Transfer](https://arxiv.org/html/2609.00891v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00891v1) §2–4全部采用的推导/方法/实验与§6；abs v1 Sep01 08:20:35Z，无撤回。

No Change — Existing Coverage，Owner INFER-KV-CACHE：实际Ch45 Prefixreuse已有directionaltranslator artifact与translation+transfer+assembly/质量fallback，后续重构proxy≠未来utility及gather/codec成本亦明确。具体局部head先验与ridge校准是该实验分支，不需为每种mapper再增书稿小节；。 当前owner：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。精确证据与边界。

### [In-Context Neurofeedback: Can LLMs Control Their Internal Representations through Privileged Access?](https://arxiv.org/html/2609.00904v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00904v1) §2/3.3/4/5/6.1/6.3、Limitations及Appendix D/F/J；abs v1 Sep01 08:36Z，无撤回。

No Change — Existing Coverage，Owner WORLDVIEW-REPRESENTATION。实际Ch5可读/被用/因果阶梯与外部groundtruth/freshprobe已足以承载所采用的受限反证；不能把反馈指标或自报变成系统安全权限。具体神经反馈task保留Daily。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference Voting](https://arxiv.org/html/2609.00905v1)

3 / 2 / 2 = 7，采用命题深入审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00905v1) §2–3/4.1–4.2/5、Appendix C.2/C.6/D.1/D.3/D.5.1；D.5其余optimality推导仅边界读取，不采用通用最优保证。

仅报告 — 条件化生成的受限MCMC分支，Owner MODEL-SAMPLING。当前Ch20一般解码与Ch48验证不能被该定理替代；本轮保留精确性类型和judge假设，不把多步昂贵采样推荐为生产默认，不强行新增一套MCMC教科书正文。 精确证据与边界。

### [Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO](https://arxiv.org/html/2609.00925v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00925v1) §3–9/Limitations、Appendix A/C.1–C.2/F.1–F.4；abs v1 Sep01 08:49:01Z，无撤回。

No Change — Existing Coverage，Owner TRAIN-DPO / WORLDVIEW-REPRESENTATION。Ch34离线pair与onlinecoverage分支、Ch5因果证据阶梯、Ch66分母/selection已经承载采用解释。保留recipe而非loss排名与有限复用反证，不将个别方向命名为全模型grounding电路。 当前owner：`TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md)。精确证据与边界。

### [Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling](https://arxiv.org/html/2609.00949v1)

3 / 2 / 2 = 7，评价有效性采用命题深入审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00949v1) §3–4/Limitations、Appendix C.2/D/E/F.2；abs v1 Sep01 09:08:15Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-EVALUATION-SYSTEM。实际Ch66真实tool/effect过程检查与outcome分开、合法替代路径/false reject边界，以及Ch72effect授权已有采用结论。细分类/诊断控制留报告，不把goldoracle改造成生产控制器。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [CoBRA: Learning Tool-Use Boundaries via Counterfactual Margins](https://arxiv.org/html/2609.00967v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。实际读[exact HTML](https://arxiv.org/html/2609.00967v1) §3/4.1–4.4/Limitations、Appendix A/C/E/F；abs v1 Sep01 09:24:11Z，无撤回。

仅报告 — 受限tool-routing训练分支，Owner AGENT-TOOL-CALLING，TRAIN-GRPO handoff。不将未知正确性转给router，Books中tool提议/授权/执行责任保持；本轮保留pairedutility与分组baseline具体实验，不为一套retrievalrecipe扩写多个章节。 精确证据与边界。

### [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](https://arxiv.org/html/2609.00993v1)

共享weights/KV省handoff，但P AllReduce与D分组AllGather顺序不一致可形成等待；rank-aligned turnstile/一致enqueue和允许边界交错使不冲突计算重叠。buffer/counter/workspace/QP等按phase分开，取消后不能立刻复用半完成状态。

实际Books：Ch55“Break-even思维”与下一PDAF段真实两段已含相交组例子、顺序、共享/phase状态、成本及串行/分池共存。No Change — Existing Coverage；不追加框架名称或性能表。 当前owner：`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。精确证据与边界。

### [SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/html/2609.01004v1)

2 / 1 / 2 = 5，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01004v1) §3.2–3.3/4.1–4.3、Appendix B/D.1–D.5；abs v1 Sep01 09:52:10Z，无撤回。

仅报告 — 视觉token预算的受限设计分支，Owner MULTIMODAL-REPRESENTATION。保留aggregation、分层预算与索取attention权重的执行成本，不把局部裁剪方法提升为通用token重要性定律，不新增Books机制。 精确证据与边界。

### [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](https://arxiv.org/html/2609.01024v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01024v1) §3.1–3.2/4.1–4.3/5.1–5.3及Limitations；abs v1 Sep01 10:21:10Z，无撤回。

仅报告 — 重新组合条件函数的受限分支，Owner MODEL-MOE。实际Ch21已有细粒度激活/物理group分账及新架构依赖≠原函数执行重排，当前采用的设计边界已承载；不为SwiGLU特定组合扩写第二套owner。 精确证据与边界。

### [The Multiple Timescales of Gradient Descent on the Edge of Stability: A Perturbative Derivation of the Central Flow](https://arxiv.org/html/2609.01034v1)

2 / 1 / 2 = 5，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01034v1) §2/3/4.1–4.3/8及Result4.1推导；未认证Appendix A–D或全部高余维/高阶公式。

仅报告 — 训练动力学的受限解释，Owner TRAIN-PRETRAINING。不把形式多尺度近似变成训练默认调参或严格收敛结论，不新增Books定理。 精确证据与边界。

### [Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](https://arxiv.org/html/2609.01035v1)

3 / 2 / 2 = 7，采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01035v1) §3/4.1–4.2/5–7、Appendix A.1–A.2/B；不采用未完整复核的branching临界律/occupancy最优规则。

No Change — Existing Coverage，Owner AGENT-PLATFORM / AGENT-MULTI-AGENT。实际Ch84累计风险账本≠真实损失上界、可信pricing/identity及授权不可余额替代，加Ch66 selection/部署校准已有采用边界。本报告保存条件证书的精确前提，不把形式输入变成平台已经能给出的安全保证。 当前owner：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)。精确证据与边界。

### [From Truncation to Commitment: Persistent Context in Uniform Discrete Diffusion](https://arxiv.org/html/2609.01043v1)

2 / 2 / 2 = 6，采用命题标准审阅；关键恒等式另深入核验。已读[exact HTML](https://arxiv.org/html/2609.01043v1) §3–5/6、Appendix A/B.1/C.1–C.2/D.2/D.5–D.7；abs v1 Sep01 10:43:24Z，无撤回。

Integrate — 已写入并独立写后通过，Owner MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 L117–119在provisional/committed区分后补持久denoiser条件副本与底层mutable state、最终重新读出的边界，保留错误条件持续影响的代价；Review notes记录exact来源而非新论文正文节。root独立实际读§4.1–4.3/5.1–5.3/6及原Ch24后批准，2026-09-07再次顺读实际新增段/两侧交接/notes并通过，写锁已释放。该PASS仅限此采用命题，不扩为所有oracle理论或性能认证。 当前owner：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。精确证据与边界。

### [Lagged Coupling: Internal Representations Become Readable Before They Become Causal](https://arxiv.org/html/2609.01048v1)

2 / 1 / 2 = 5，标准采用命题审阅完成。HTML404、webPDF缓存失败后直接取得[exact PDF](https://arxiv.org/pdf/2609.01048v1)，共15页，实际读§3–7、Appendix B/C及A尾部；不采用未完整读的外部checkpoint损坏归因。

仅报告 — 可读性与操控性分离的受限证据，Owner WORLDVIEW-REPRESENTATION。实际Ch5既有可读/被用/因果阶梯承载所需警告；本轮不采用缺artifact的数值与安全普遍推论，不据此强写新Books结论。 精确证据与边界。

### [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://arxiv.org/html/2609.01068v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01068v1) §3–4/5.1–5.3、Limitations、Appendix B.1/B.3/C.1–C.3/D.1/D.4；采用双head与静态调度，不采用未展开的动态迁移机制。

No Change — Existing Coverage，Owner INFER-SCHEDULING。实际Ch56已有prediction/calibration、真实remainingwork、机会成本、fairness与轻载fallback，Ch48拥有speculativework；此处sharedbackbone是受限signal供给实现，不改authority或新增调度owner。 当前owner：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。精确证据与边界。

### [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](https://arxiv.org/html/2609.01091v1)

3 / 2 / 2 = 7，安全采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01091v1) §3–5、Appendix A.2–A.3/B.1/C.1–C.3/E.2/E.4–E.5；不认证未读的全部projection/跨模型优化轨迹附件。

仅报告 — 已知trait的受限SFT监测/约束分支，Owner TRAIN-SFT / PLATFORM-SECURITY。不把已知probe保护扩成隐性行为完全消除；保留可见数据清洗不足与observer被优化后的独立行为验收，不为固定corridor配方新增Books机制。 精确证据与边界。

### [Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts](https://arxiv.org/html/2609.01100v1)

2 / 1 / 2 = 5，标准采用命题审阅完成，额外理论主张不采用。已读[exact HTML](https://arxiv.org/html/2609.01100v1) §3–6/Limitations/Appendix D；abs v1 Sep01 11:43:41Z，无撤回。

仅报告 — 显式reference state的路由分支，Owner MODEL-MOE。保留state更新/投影/负载代价，不采用过强的语义分解与稳定保证，不追加Books默认设计。 精确证据与边界。

### [When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP](https://arxiv.org/html/2609.01103v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01103v1) §3–5/Limitations、Appendix A.3/A.7/D.3–D.4；abs v1 Sep01 11:46:56Z，无撤回。

No Change — Existing Coverage，Owner MULTIMODAL-REPRESENTATION。实际Ch23‘对齐不是把向量拉近’已区分目标及下游有效性，Ch66拥有校准/分布与比较协议；保留此受限反证而非新增统一hubness校正算法。 当前owner：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。精确证据与边界。

### [Replicating TRACE: A Practitioner's Guide to Its Threshold and Particle Budget](https://arxiv.org/html/2609.01108v1)

3 / 2 / 2 = 7，评价反证采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01108v1) §3–11与Reproducibility；abs v1 Sep01 11:48:16Z，无撤回。

No Change — Existing Coverage，Owner WORLDVIEW-REPRESENTATION / PLATFORM-EVALUATION-SYSTEM。实际Ch5因果使用条件与Ch66分层coverage/阈值/独立校准足以承载本次反证；具体TRACE估计器留报告，不扩成通用因果发现章节。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs](https://arxiv.org/html/2609.01117v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01117v1) §3.1–3.5/4.1–4.2/4.4–4.6、Limitations及Appendix A/C/G/I；abs v1 Sep01 11:56:17Z，无撤回。

仅报告 — 受训潜在工作状态的循环分支，Owner WORLDVIEW-LLM-INTELLIGENCE。保留模型参数冻结与可训练proposer/refiner、软约束与真实状态保证的区别；不将有限任务配方上升为所有推理必须沿该latent轨迹的设计结论。 精确证据与边界。

### [Scaled Idempotence in Transformer Attention: Paired OV Geometry and Shared-Value Algebras](https://arxiv.org/html/2609.01129v1)

2 / 2 / 2 = 6，结构命题标准审阅，采用恒等式定点深核。已读[exact HTML](https://arxiv.org/html/2609.01129v1) §3.1–3.3/4.1–4.7/5.1–5.4/5.6/6.1–6.2；abs v1 Sep01 12:05:11Z，无撤回。

仅报告 — 权重几何的受限诊断，Owner MODEL-MULTI-HEAD-ATTENTION。实际Ch15参数换基、GQA共享约束及可解释性与真实功能/执行成本分开已承载本次边界；不把新代数关系变成heads可删/可重复执行的默认设计。 精确证据与边界。

### [Does task decomposition improve automatic NLG evaluation?](https://arxiv.org/html/2609.01139v1)

3 / 2 / 2 = 7，评价反证采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01139v1) §2–6/Limitations、Appendix C/D.1–D.4；abs v1 Sep01 12:15:53Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-EVALUATION-SYSTEM。实际Ch66 tie-awaremetrics、冻结scorer/aggregation/selection身份、独立校准及atomicclaim与结论不同estimand已覆盖。保留‘分解需与同label/calibration预算直接基线比较’的受限反证，不为通用禁用分解写新规则。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [On the Design Fundamentals of Pixel Text Representation Learning](https://arxiv.org/html/2609.01147v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01147v1) §2.1–3.5/4–5/Limitations及Appendix B.1–B.2/C；abs v1 Sep01 12:20:19Z，无撤回。

仅报告 — pixeltext表示与视觉预算的受限训练分支，Owner MULTIMODAL-REPRESENTATION / TRAIN-DATA。不把局部recipe提升为必须多模态grounding的普遍定律，也不因以图代词能缩token就承诺Serving效率；保留真实输入/任务合同。 精确证据与边界。

### [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](https://arxiv.org/html/2609.01161v1)

3 / 2 / 2 = 7，安全评价采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01161v1) §3–6/Limitations；abs v1 Sep01 12:43:02Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-SECURITY / PLATFORM-EVALUATION-SYSTEM。实际Ch72合法路径必须可达、不能拒绝全部交易获得空洞安全及Ch66可用性/选择条件/独立judge合同，已承载本次有限对照。实验控制保留日报，不加入版权法律推论。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training](https://arxiv.org/html/2609.01170v1)

2 / 1 / 2 = 5，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01170v1) §3–6/Limitations；abs v1 Sep01 12:47:09Z，无撤回。

仅报告 — 早期训练归因与有效更新区分，Owner TRAIN-PRETRAINING / WORLDVIEW-REPRESENTATION。保留测量对象/模板/优化器控制，不把有限动态观察变成训练架构或逐层学习率默认策略。 精确证据与边界。

### [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://arxiv.org/html/2609.01215v1)

2 / 2 / 2 = 6，标准采用命题审阅完成，形式保证不采用。已读[exact HTML](https://arxiv.org/html/2609.01215v1) §3.1–3.4/4.1/4.4/4.6–4.8/5；abs v1 Sep01 13:19:05Z，无撤回。

仅报告 — worldmodel辅助技能归并的受限分支，Owner MULTIMODAL-WORLD-MODELS / MULTIMODAL-EMBODIED-VLA。保留featurepartition、typedlibrary与realenvironmentreturn分开；未生效的gate和未通过motor结果不能写成Books稳定机制。 精确证据与边界。

### [Prompt-Robust Language Models: Which Training Strategies Work?](https://arxiv.org/html/2609.01217v1)

3 / 2 / 2 = 7，训练代理反证采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01217v1) §3–4/Limitations、Appendix C/G/H；abs v1 Sep01 13:21:32Z，无撤回。

No Change — Existing Coverage，Owner TRAIN-SFT / PLATFORM-EVALUATION-SYSTEM。实际Ch29 L538–550 promptphrasing与validation模板漂移、Ch66 promptvariants/冻结metric及Ch15训练proxy≠行为验收承载该反证。单任务模板配方保留报告，不添加默认逐模板batch规范。 当前owner：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)。精确证据与边界。

### [Multi-Head Self Attention is a Parameter Identification Mechanism](https://arxiv.org/html/2609.01231v1)

采用：同一head内QK因子可逆换基不改乘积；OV有配对变换，故参数坐标不唯一。共享KV需组内兼容，RoPE限制可交换结构。

实际Books：本轮已读Ch15 head分化后两段与Ch14/16承接，明确投影块而非全head矩阵、配对恒等式、共享/位置条件和执行收益非目标。原独立写后复核已验同一段。No Change — Existing Coverage；不因本轮又读一次重复增加参数识别章节。 当前owner：`MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md)。精确证据与边界。

### [Position Matters: Feature Inversion Attacks in ViT Split Inference with Token Reduction and Shuffling](https://arxiv.org/html/2609.01232v1)

3 / 2 / 2 = 7，安全采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01232v1) §2.1–2.3/3.2/4/5.1/5.3/7；abs v1 Sep01 13:32:30Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-SECURITY。实际Ch72 L223–229已否定hiddenstate天然privacy/utility中间地带，要求攻击者知识/下游能力及不发布分支；本次新攻击是该边界的受限证据，不为每种shuffle重建增加独立章节。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](https://arxiv.org/html/2609.01235v1)

canonical JSON、domain/length-separated commitment把单对象扩成整组成员/顺序验证；request、authority、epoch/revocation与terminal结果同时绑定。trust anchor必须在证据包之外，两个verifier不自动构成独立实验团队复现。

实际Books：Ch77“Memory Transaction Boundary”到“恢复记录不等于恢复未来计算”的正式正文已包含整组校验、外部anchor、代价与非目标；与Ch78副作用交接不冲突。No Change — Existing Coverage。 当前owner：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)。精确证据与边界。

### [Post-Training Science for Supervised Fine-Tuning](https://arxiv.org/html/2609.01244v1)

核心是受控recipe选择，不是通用最优超参。数据由同一任务judge迭代生成并接受，task-score与testNLL同200行相关不是独立validation选择保证。

实际Ch29“Evaluation应分开能力与行为”及Distribution-drift段、Ch30相邻adapter责任已覆盖loss拟合局限、模板偏差、task/安全/通用回归与anchor边界。root同意 No Change — Existing Coverage；这些证据要求按同一recipe校准而非跨模型盲排NLL，但不必为每个参数条件再加书稿规则。 当前owner：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)。精确证据与边界。

### [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](https://arxiv.org/html/2609.01245v1)

3 / 2 / 2 = 7，训练系统采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01245v1) §3.1–4.1/4.3–4.4、Appendix A–D/F/G/I/J；abs v1 Sep01 13:44:40Z，无撤回。

No Change — Existing Coverage，Owner TRAIN-GRPO。实际Ch33 L218–275 mixedsignal/组统计依赖与prompt选择，L337–355 admission/lossdenominator/policyratio/verifier identity已有主线。该recipe强化系统合同与故障归因边界，不改变现有默认设计，也不为未量化quarantine新增已认证实现。 当前owner：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。精确证据与边界。

### [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](https://arxiv.org/html/2609.01249v1)

3 / 2 / 2 = 7，安全采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01249v1) §2威胁设定、§3–6；abs v1 Sep01 13:46:31Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-SECURITY。实际Ch72 L509–522已有metadata/signal/verifier分层、变换与falsepositive/negative边界，negative不证明非AI生成。该攻击补实验上下文，不改变现有设计，也不将未验签metadata写为认证链。 当前owner：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。精确证据与边界。

### [From Base Rollouts to RL Reasoning: A Budgeted Search Perspective](https://arxiv.org/html/2609.01274v1)

3 / 2 / 2 = 7，能力比较采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01274v1) §3–6/Limitations；abs v1 Sep01 14:08:39Z，无撤回。

No Change — Existing Coverage，Owner TRAIN-GRPO / PLATFORM-EVALUATION-SYSTEM。Ch33既有policy/采样预算/组信号分工与Ch66 controller、selector、metric和成本合同足以承载公平比较；本项保留受限行为解释，不增加默认用搜索替代RL的结论。 当前owner：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。精确证据与边界。

### [TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models](https://arxiv.org/html/2609.01277v1)

2 / 2 / 2 = 6，标准采用命题审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01277v1) 问题/方法/benchmark/mainresults/ablation、Appendix Algorithm1、gap推导与reproducibility；abs v1 Sep01 14:12:57Z，无撤回。

仅报告 — MULTIMODAL-GENERATIVE-PARADIGMS。作为预测cleanstate上的时间控制分支保留，当前实验不足以把特定跨模态readmap变成通用生成默认设计；不另扩Books实现细节。 精确证据与边界。

### [HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives](https://arxiv.org/html/2609.01282v1)

3 / 2 / 2 = 7，评价采用命题深入审阅完成。已读[exact HTML](https://arxiv.org/html/2609.01282v1) §3.1–3.7、§4.1–4.2、§5.4–5.5/§6；abs v1 Sep01 14:16:08Z，无撤回。

No Change — Existing Coverage，Owner PLATFORM-EVALUATION-SYSTEM / MODEL-MULTI-HEAD-ATTENTION。实际Ch66 L1873–1885 attributioncontract/测量路径及Ch15 attentionproxy≠behavior已承载独立observer与有效性分开；数学守恒可作诊断但不替代受控行为证据，不为每种归因算子另加Books正文。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Reliability Challenges in Diffusion Vision-Language Models](https://arxiv.org/html/2609.01318v1)

2 / 2 / 2 = 6，标准采用命题已审。实际重开[精确HTML](https://arxiv.org/html/2609.01318v1) §3、§4.1、§4.3；采用生成顺序/预算与可靠性指标分开，不采用全部人口属性评价或范式优劣排名。

实际Ch24“Editable tokens与commit boundary”及成本/quality验收，已将可改state、提交与质量独立；Ch66负责完整测量对象。No Change — Existing Coverage，MULTIMODAL-GENERATIVE-PARADIGMS；不为受限诊断新增通用幻觉控制器。 当前owner：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。精确证据与边界。

### [mzCache: On-Device LLM Memory Management under Multitasking](https://arxiv.org/html/2609.01338v1)

3 / 2 / 2 = 7，采用命题深入已审。实际读[精确HTML](https://arxiv.org/html/2609.01338v1) §2.3–4.4、§5、§6.1–6.5。

Integrate — INFER-GPU-MEMORY：已在Ch54“扩展层级”补UMA物理容量与restorecriticalpath两段，保留压缩减占用、resident/simple分支及外压/热约束；independent_sep02实际顺读前后与新增段后通过，证据记录见独立notes。Review notes保留精确primary和限制。 当前owner：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。精确证据与边界。

### [Probing Factual Knowledge Transfer with Training Data Interventions](https://arxiv.org/html/2609.01341v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01341v1) §3–5/Limitations。

实际Ch5“从可读出到机制”要求局部干预、混杂控制和跨context复验，Ch27拥有训练provenance；本研究为已有证据阶梯提供受限反证，不改变owner。No Change — Existing Coverage，WORLDVIEW-REPRESENTATION；不采paper中的全因果强表述。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](https://arxiv.org/html/2609.01343v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01343v1) §3.1–3.5/§4.1及§5.2；只采用近匹配预算下循环MoE的设计分支，不认证全部scaling拟合。

实际Ch21“MoE Capacity必须在同一Budget下比较”已分total/active/通信与质量，持久容量和执行path分别验收；循环复用是受限组合证据。No Change — Existing Coverage，MODEL-MOE，不将两次循环写成默认配方。 当前owner：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)。精确证据与边界。

### [Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades](https://arxiv.org/html/2609.01345v1)

同verifier选择纠错tail又生成dashboard，使accepted-wrong无法进入直接纠错且不在内部曲线上暴露；必须独立采样accepted/rejected并保留teacher-error。真实Qwen2.5/GSM8K/MATH单seed回路退化，不是持续改善的floor验证；two-population推论依赖improving-loop，合成20seed只是控制机制，不外推真实量级。

实际Books：Ch66“Scorer不是绝对真相”后两段明确独立audit、接受/拒绝分母、开放域可判断边界，以及真实未改善不能证明普遍floor。No Change — Existing Coverage；仅采用dashboard盲区，不引入收敛定律。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR](https://arxiv.org/html/2609.01354v1)

误拒、execution/no-verdict与错误接受是不同故障；relative tolerance到大整数可接受差一。未承诺extraction格式不能混为实现错误，judged subset正确率也不能代替覆盖率。

实际Books：Ch66“Transformation Stability”后规则verifier段已含双向扰动、适用域、异常覆盖和magnitude-conditioned tolerance，与下一可执行证据交接通顺。No Change — Existing Coverage。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs](https://arxiv.org/html/2609.01356v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01356v1) §3.4、§4.1–4.3。

Ch5的可读/局部干预/行为使用阶梯实际承载该边界，Ch15的head混合不允许单头语义贴标签。No Change — Existing Coverage，WORLDVIEW-REPRESENTATION；保留新局部机制证据，不把旧“无跨系统责任所以排除”理由继续使用。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA](https://arxiv.org/html/2609.01361v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01361v1) §2.3–3.4、§4.3–4.6。

实际Ch5独立reader与跨context复验、Ch66测量/选择/校准合同已覆盖。No Change — Existing Coverage，WORLDVIEW-REPRESENTATION；仅采用probe有效性反证，不开展医学应用路线或给临床建议。 当前owner：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。精确证据与边界。

### [Behaviorally Effective LoRA Writes Are Sparse and Structured](https://arxiv.org/html/2609.01374v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01374v1) §3/§4及§5的同状态与投影实验。

仅报告 — TRAIN-LORA。Ch30已有rank与适配位置依赖任务、预算及激活子空间；本文保留训练后写空间的受限探针和条件分支，不把相同rank等同相同能力，也不为少量benchmark新增普遍adapter收缩配方。 精确证据与边界。

### [When Tokenization is Secretly Output Supervision](https://arxiv.org/html/2609.01386v1)

2 / 2 / 2 = 6，因当前Books缺口深入采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01386v1) §2.1/§3.1–3.4。

Integrate — MODEL-TOKENIZER：Ch11已在V/T取舍后补输出监督粒度、条件化路径与预算两段及精确Review note；independent_sep02已实读前后正文确认必要增量及写后PASS，不改变owner。 当前owner：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)。精确证据与边界。

### [Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching](https://arxiv.org/html/2609.01404v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01404v1) §3.1–3.2、§4.3–4.6。

实际Ch26 stateownership将proposal/controller/environment outcome分权，Ch66过程与结果分开。No Change — Existing Coverage，MULTIMODAL-EMBODIED-VLA；无须把benchmark的重复声明规则当生产成功提交协议。 当前owner：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。精确证据与边界。

### [Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search](https://arxiv.org/html/2609.01431v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01431v1) §4–5.6：GP拟合loss surface，再采样各规模的最优超参，用log-power系数posterior的熵减少除以成本幂选择实验。

实际Ch7“实验预算”“Scaling适用边界”与联合留出尺度验证已拥有实验规划/代理失配责任。No Change — Existing Coverage，WORLDVIEW-SCALING-LAW；entropy acquisition保留可选实现，不把代理模型自信写成已找到规律。 当前owner：`WORLDVIEW-SCALING-LAW` [Ch7](../../../../books/part-01-worldview/07-scaling-law.md)。精确证据与边界。

### [Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning](https://arxiv.org/html/2609.01449v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01449v1) §2–3及结论：共享block循环并保持隐藏状态，已知clue锁定；训练时随机长度rollout、重新注噪、每段截断反传，推理可用固定最大噪声和稳定输出停止。

仅报告 — MULTIMODAL-GENERATIVE-PARADIGMS：保留“训练curriculum与推理生成范式可解耦”分支，当前特定任务/架构不改写Ch24既有可变state/commit论证，也不归入环境worldmodel。 精确证据与边界。

### [When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning](https://arxiv.org/html/2609.01455v1)

2 / 2 / 2 = 6，安全命题深入已审。实际读[精确HTML](https://arxiv.org/html/2609.01455v1) §3.2–3.3、4.1–4.5：100输入block empirical Fisher、top64归一化谱只是局部梯度几何；logitlens的拒绝/服从首token最大值与patch的margin不是完整有害回答概率。

仅报告 — TRAIN-SFT：已有SFT回归/遗忘与安全独立验收不被改变；保留路由几何的解释性候选，但不以局部margin实验建立普遍“浅层拒绝修好即可”的长期机制。无需为采用不到的强因果结论追加无限证明审查。 精确证据与边界。

### [Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices](https://arxiv.org/html/2609.01457v1)

2 / 2 / 2 = 6，接口/隐私采用命题深入已审。实际读[精确HTML](https://arxiv.org/html/2609.01457v1) §3–4/5.1–5.3/6.1–6.2。

仅报告 — TRAIN-DISTRIBUTED-TRAINING：公开机制是有条件改变优化边界的工程分支；实际训练与隐私等价不足以写成Books默认splitrecipe。保留finitecache/冻结/威胁模型限制，不因通信数字高就升级。 精确证据与边界。

### [Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers](https://arxiv.org/html/2609.01466v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01466v1) §3–5.4。

仅报告 — PLATFORM-TRACE：采用原始事件/派生投影/消费者的责任分界作为受限工程案例；没有证据证明完整fold优于更小的任务状态，故不以新框架扩充长期Books主线或增加全局报告规则。 精确证据与边界。

### [GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](https://arxiv.org/html/2609.01491v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01491v1) §3/4.1、4.3–4.5。

仅报告 — AGENT-MULTI-AGENT：保留有预算时协议创造/使用/传递不同的受限案例；单虚构任务不足以写成平台应使用不可读语言或替代typedtool协议。 精确证据与边界。

### [Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall](https://arxiv.org/html/2609.01532v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01532v1) §2.2–6.2/6.4/Discussion。

实际Ch28“Distillation要分开PrefixProvenance与KLDirection”已将teacher版本、prefix、entropy-gated curriculum和accuracy/diversity/cost作为条件分支。No Change — Existing Coverage，TRAIN-PRETRAINING；本研究增加固定corpus的阶段性反证，未形成替代所有NTP或始终按entropy路由的结论。 当前owner：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。精确证据与边界。

### [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](https://arxiv.org/html/2609.01549v1)

2 / 2 / 2 = 6，标准采用命题已审，形式收敛保证不采用。实际读[精确HTML](https://arxiv.org/html/2609.01549v1) §3–5.2：centralMARSSM训练消费jointaction/observation，playerinfoset只见本方历史；imaginedrollout从root重启，decoder观测参与policy更新，critic与actor信息分权。

仅报告 — MULTIMODAL-WORLD-MODELS：保留prediction/inputinformation/strategyownership分支，不将理想固定isomorphicmodel+精确RNaD收敛外推并行学习。该游戏特殊结构不足以把集中模型设为通用worldmodel必选架构。 精确证据与边界。

### [Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories](https://arxiv.org/html/2609.01556v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01556v1) §3/5–10。

实际Ch76 querygenerator/index/reranker/packing/contextuse分别冻结且source recall与finaloutcome分开。No Change — Existing Coverage，AGENT-RAG；该反证支持现有分层验收，不写默认lexical或LLMrerank总是更好。 当前owner：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)。精确证据与边界。

### [H3-World: Turning Language Understanding into World Control](https://arxiv.org/html/2609.01560v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01560v1) §3–5。

仅报告 — MULTIMODAL-WORLD-MODELS：保留由textcondition到时间绑定的生成分支；当前无persistentstate、在线闭环、planning或policytraining，不能按名称把它写成完整worldmodel或物理控制器。 精确证据与边界。

### [Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs](https://arxiv.org/html/2609.01573v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01573v1) §2.1–3.5。

仅报告 — TRAIN-RLHF：保留用可接受性能区域而非噪声点最优做预算试验的受限策略；不固定通用SFT/RL比例或把样本数当总成本，当前不改写Books后训练分支。 精确证据与边界。

### [The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally](https://arxiv.org/html/2609.01587v1)

2 / 2 / 2 = 6，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01587v1) §3–6。

No Change — Existing Coverage，INFER-TENSORRT-LLM：Ch49量化质量/粒度/执行plan联合验收已有责任边界；保留局部proxy不能代替行为恢复的反证，不据受限RTN损伤把mixedprecision或salience保护淘汰。 当前owner：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。精确证据与边界。

### [Mechanism Design for Alignment and Control](https://arxiv.org/html/2609.01595v1)

2 / 1 / 2 = 5，标准概念命题已审，不采用完整最优机制定理。实际读[精确HTML](https://arxiv.org/html/2609.01595v1) §2.1–2.3的环境/评估序/机制与jointIC：已知finiteactionuniverse、agent知道type、私有signal、designer能承诺reward，报告可隐匿不可伪造能力证书。

仅报告 — AGENT-MULTI-AGENT：用作evaluation与executioncontrol不能互相替代的理论背景；尚无映射到实际LLMcontroller的验证，不修改Books为已实现防护。 精确证据与边界。

### [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](https://arxiv.org/html/2609.01596v1)

2 / 2 / 2 = 6，物理责任采用命题深入已审。实际读[精确HTML](https://arxiv.org/html/2609.01596v1) §4–6.5/7。

No Change — Existing Coverage，MULTIMODAL-EMBODIED-VLA：实际Ch26的proposal、controller、environmentoutcome和反馈/安全所有权已承载本项；jointwrench是此接口的受限实现，不把预测值写成forcecommand或替代校准/限幅。 当前owner：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。精确证据与边界。

### [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation](https://arxiv.org/html/2609.01604v1)

2 / 1 / 2 = 5，标准采用命题已审。实际读[精确HTML](https://arxiv.org/html/2609.01604v1) §3–7。

No Change — Existing Coverage，PLATFORM-EVALUATION-SYSTEM：Ch66归因干预/选择分母/测量路径与真实有效性分开，Ch5probe证据阶梯已覆盖；只作局部机制解释，不把可解释评分路线当“judge不是捷径”的全面证明。 当前owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确证据与边界。

### [Moonshot — FlashKDA 数值纠错](https://github.com/MoonshotAI/FlashKDA/commit/7afb9f454f160a6c4bbc0999beca0a8c40a38934)

fp16 Neumann中间幂在near-collinear keys情形产生大值和抵消；新路径seed与diagonal solve保FP32，8×8forward substitution后在BF16 HMMA输入处量化，FP32累加、BF16最终写回。不是把整个算法都升级FP32，也不是数学恒等式保证有限精度完全相同。

实际Ch49数值验收与recurrent lowering段已有reference differential、适用slice、dtype/artifact和条件回退，具体分块求逆留作受限实现。拟 仅报告：重要实现纠错必须审，但未证应更改全书既有数值设计结论，也不把kernel名称升级canonical owner。 精确证据与边界。

## 5. 缺口与下一步

本窗普通作者审阅、独立复核及整稿验收均已做完，可执行待办为0。以下均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；外部材料到达时按所列身份定点重开，不靠重复阅读同一页面解决，也不授权扩展本窗：

| 材料 | 缺少什么、为何必要 | 可接受替代材料与续跑位置 |
| --- | --- | --- |
| [Locked Phase 2609.00335v1](https://arxiv.org/abs/2609.00335v1) | PDF7页已读，但Study1 pipeline/result、Study2 Artifact4/5只有声明或hash，缺模型/数据身份、PC与基线特征、配置及输出；不能验证机制或复算null。 | 作者官方仓库/原附件或可读导出；只补这组实验，不追未授权b5/b6或另一理论代填。建议2609.00335v1-study1-study2-artifacts.zip。 |
| [2609.00492v1](https://arxiv.org/abs/2609.00492v1) | sequence/document隐私单位关系未闭合，中心保证仍Disputed；不靠删争议数字把family标Passed。 | 作者邻接关系、采样/裁剪/会计单位说明及exact artifact或勘误；建议2609.00492v1-privacy-unit-clarification.md。 |
| [2609.00868v1](https://arxiv.org/abs/2609.00868v1) | 主文全词表KL与Appendix top50实现定义冲突，影响中心gap指标。 | 对应版本代码、支持集/归一化/尾部处理和配置，或勘误；建议2609.00868v1-kl-definition.md。 |
| [腾讯浑元完整Research目录](https://hunyuan.tencent.com/research) | 截图最新Aug28不证明完整目录覆盖本窗；空壳/失败响应不算零命中。 | 完整列表和日期/文章链接HTML或官方列表接口响应；只筛本窗；建议hunyuan-research-list-20260902.html。 |
| Google：multi-agent hardening、enterprise graph RAG | 正文仅年份2026，无法确认日窗；具体URL及已试路径见共享检查与日期材料请求。 | 官方RSS/JSON-LD、存档或作者可核首次公开时间；只定点归属，不重扫全年目录。 |
| [HyperWorld 2609.00002](https://arxiv.org/abs/2609.00002)、[Activation-Matched 2609.00351](https://arxiv.org/abs/2609.00351) | 当前abs分别显示Jun12、May29，与缓存Sep02 new公告身份冲突；并非确定落窗，保留证据但不进入当窗评分表。 | 官方first-announcement、版本历史或纠错说明；恢复真实owner后定点接手，不扩为整月回填。 |

未对上述3个证据未决家族写入新机制。11项已整合不依赖这些争议；“已有覆盖”来自实际正文比较，不只是ROADMAP映射。

## 6. 复核

复核者：independent_sep02、root（独立于作者finish_sep02）。
结论：通过

准入完成128项拟留逐项复核和排除风险抽查，恢复漏检、移出3项一般方法；日期Hold不伪落窗。采用命题复核见独立记录、root前8项、root后8项以及root七项写入与三机构复核。11项必要Books写入均实际顺读前后交接与章末证据；普通独立审阅与逐ID整稿对账均已结束。§3/§4各129唯一材料URL、双向差集为0；126个arXiv中123项采用范围通过、2项中心争议、1项Partial，另3机构通过。11/76/39/3的Books处置与60项深入、66项标准、2争议、1受阻一致。

`python3 scripts/validate_research.py --report papers/2026/09/02/README.md` 通过；标题、围栏、129项评分合计、候选/证据一一对应、本地路径和heading anchor检查通过。相关Books、报告及作者笔记的 `git diff --check` 通过；root同时完成相关 staged/unstaged 范围检查。本轮未stage、commit或push，修改保留待人工Review。来源日期、材料和中心证据争议均以不采用、不写Books和精确重开条件隔离；它们没有冒充Evidence通过，但不再留下本窗可执行工作，因此整体复核通过。
