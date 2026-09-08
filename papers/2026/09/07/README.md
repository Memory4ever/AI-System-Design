# Daily Research — 2026-09-07

**规范：** V3
**窗口：** 2026-09-06T09:00:00+08:00 ～ 2026-09-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T15:25:00+08:00

## 1. 结论

四个每日arXiv主类共537个去重身份：New254、仅Cross110、仅Replacement173。原始命中不是项目贡献数；题摘筛选及独立边界复核后保留41篇arXiv，加2项机构说明，共43个家族。普通修订、跨类出现与网站重列不重置日期，不因此启动版本对比。

43项均完成本次采用范围的作者审阅及非作者核验，普通待审与待独立为零。42项所需证据可作限定采用；RISE的保证推论仍有争议。七项必要增量已写入Ch17、24、30、39、56、76、78并通过写后复核，其余以具体已有论点承载，未把43项变成43条书稿新增。这些增量分别连接训练表示到部署身份、逻辑状态到实际执行、局部质量到整体计划、恢复许可到最终验收，不增加论文列表式正文。

浑元目录覆盖限制与RISE的JSD到reverse-KL保证争议均已隔离：前者不用于无遗漏断言，后者不用于正面证据或Books，并分别留下定点重开条件。本日没有普通研究待办。

## 2. 来源覆盖

原始入口与日期见机构记录、arXiv筛选依据及中国厂商共享核查。本轮不扫描每周源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI |官方研究正文及RSS精确字段确认Sep06两项；活动测量不是研发因果加速；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-ANTHROPIC |研究目录最新Sep04，已越过窗口起点；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-GOOGLE-AI |DeepMind研究列表、Research Blog及已定位出版身份；Sep04已观察到的两项无日期文章不移入本窗；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-META-AI |Sep06 Text-Audiobox卡片有Sep04 arXiv首次公告身份，去重；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-QWEN |官方双语API各37项重新取得，extra.date最大Sep03 10:00+08，未命中本窗；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-DEEPSEEK |官方updates最新Aug21，随后Aug13、Jul31，未把常驻模型入口算新事件；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-MOONSHOT |43个官方仓库release端点已重新取回：38空、5非空均越过本窗；具体停止日期见机构记录；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-ARXIV |cs.AI/cs.CL/cs.LG/cs.DC官方Sep07 New/Cross/Replacement；非主类只核具体候选的原primary公告，不全扫新类别；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-TENCENT-HUNYUAN |研究页下方“全部”九行截图最新Aug28；自动正文和浏览器失败，完整目录仍有缺口，不能据空响应判零；记录 | 受阻 | 完整目录及本窗条目未恢复 |
| SRC-ZAI |官方research日期序列Aug26→Aug14→Jun16→2025；未命中本窗；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-BYTEDANCE-SEED |官方Research/Blog/Publications已跨到Aug05/Jul06以下；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-BAIDU-ERNIE |官方博客May09→Apr30→Feb09，窗外；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-XIAOMI-MIMO |Paper/Blog及官方frontmatter恢复为六月或更早；独立代码release按实际事件日，不重计；记录 | 已检查 | 无；限所列入口和停止点 |
| SRC-MINIMAX |官方中英研究列表最新Aug13；技术目录Agent Team为May13，已恢复并排除窗外；记录 | 已检查 | 无；限所列入口和停止点 |


## 3. 候选与判断

arXiv时间由本日primary-new列表与官方公告时制组合推定：20:00 EDT对应北京时间08:00，不是submitted时间或RSS午夜批次标签。OpenAI沿官方RSS原始时刻。三项评分为Design Delta、System Reach、Durability；安全命题及实际新增Books的机制按采用范围深入审阅，不以分数6为由只读摘要。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/) | 2026-09-06T16:00:00+08:00 | 研发活动与完整研发结果分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [An Alien Mind](https://openai.com/index/an-alien-mind/) | 2026-09-06T17:00:00+08:00 | 监控风险披露不等于机制公开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Iris: Climbing to the Search Frontier](https://arxiv.org/html/2609.04304v1) | 2026-09-07T08:00:00+08:00 | partial rollout与context reset分责；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Rethinking Indirect Prompt Injection as a Test-Time Search Problem](https://arxiv.org/html/2609.04495v1) | 2026-09-07T08:00:00+08:00 | 注入成功率绑定搜索策略和预算；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs](https://arxiv.org/html/2609.04526v1) | 2026-09-07T08:00:00+08:00 | 量化adapter训练表示与导出身份一致；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation](https://arxiv.org/html/2609.04263v1) | 2026-09-07T08:00:00+08:00 | KV量化PPL恢复不等于检索恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/html/2609.04748v1) | 2026-09-07T08:00:00+08:00 | 缓存构造历史属于重放输入；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/html/2609.04518v1) | 2026-09-07T08:00:00+08:00 | credit分组改变参照人口；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/html/2609.04565v1) | 2026-09-07T08:00:00+08:00 | 稀疏loss不等于稀疏backbone；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Does the Selected Object Reach the Reader? Auditing Identity Handoffs in Grounded Language-Model Pipelines](https://arxiv.org/html/2609.04579v1) | 2026-09-07T08:00:00+08:00 | 已选对象需要显式身份交接；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Train What You Deploy:Token-Faithful Post-Training of a Production Coding](https://arxiv.org/html/2609.04678v1) | 2026-09-07T08:00:00+08:00 | 训练loss沿真实token与branch归属；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/html/2609.05019v1) | 2026-09-07T08:00:00+08:00 | 运行时只修尚未执行的后缀；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/html/2609.05198v1) | 2026-09-07T08:00:00+08:00 | 少prompt不等于少监督或计算；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference](https://arxiv.org/html/2609.05275v1) | 2026-09-07T08:00:00+08:00 | 结构mask只有实际跳算才省计算；3 + 2 + 2 = 7 | 深入完成 | 整合 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/html/2609.05279v1) | 2026-09-07T08:00:00+08:00 | 代理替换的成绩与协调成本分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/html/2609.04801v1) | 2026-09-07T08:00:00+08:00 | 记录真实、对象绑定和字段支持分开；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/html/2609.05295v1) | 2026-09-07T08:00:00+08:00 | 外推teacher机制与理论保证分开；2 + 2 + 2 = 6 | 争议 | 暂缓 — 保证未采用；窄机制已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/html/2609.05339v1) | 2026-09-07T08:00:00+08:00 | 记忆迁移保留方向和reader条件；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs](https://arxiv.org/html/2609.04281v1) | 2026-09-07T08:00:00+08:00 | 补问sensor不是人物或答案认证；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [Evidence Integration in Large Language Models](https://arxiv.org/html/2609.04290v1) | 2026-09-07T08:00:00+08:00 | 生成、检查和采用证据分层；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [When Load-Balancing Goes Too Far: Expert Pruning in Over-Dispersed Mixture-of-Experts Models](https://arxiv.org/html/2609.04453v1) | 2026-09-07T08:00:00+08:00 | 路由proxy与域切片任务分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Atlas: Optimizing Deployment of Compound AI Workflows on Heterogeneous Clusters](https://arxiv.org/html/2609.04513v1) | 2026-09-07T08:00:00+08:00 | 复合图传播条件质量而非独立相乘；3 + 2 + 2 = 7 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective](https://arxiv.org/html/2609.04489v1) | 2026-09-07T08:00:00+08:00 | mask pause target不删其条件作用；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [CIERA: Cross-Iteration Exponent Reuse for Lossless Allgather in Sharded MoE Training](https://arxiv.org/html/2609.04609v1) | 2026-09-07T08:00:00+08:00 | 跨步通信编码引入双方缓存状态；2 + 2 + 3 = 7 | 深入完成 | 整合 — `TRAIN-ZERO` [Ch39](../../../../books/part-04-training-system/39-zero.md) |
| [Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One](https://arxiv.org/html/2609.04531v1) | 2026-09-07T08:00:00+08:00 | 少步生成需训练少步映射；2 + 2 + 3 = 7 | 深入完成 | 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/html/2609.05401v1) | 2026-09-07T08:00:00+08:00 | 目标改写稳定性与准确性分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [From Answers to Interpretations: Rethinking Ambiguity-Induced Aleatoric Uncertainty Estimation in LLMs](https://arxiv.org/html/2609.04543v1) | 2026-09-07T08:00:00+08:00 | 解释歧义不等于答案多样性；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents](https://arxiv.org/html/2609.04629v1) | 2026-09-07T08:00:00+08:00 | 恢复准入与最终完成分权；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Large Language Models with At Most One Spike per Neuron](https://arxiv.org/html/2609.05151v1) | 2026-09-07T08:00:00+08:00 | spike代理不足以证明系统节能；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures](https://arxiv.org/html/2609.04819v1) | 2026-09-07T08:00:00+08:00 | PCA子空间混合不证明残差无信息；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models](https://arxiv.org/html/2609.04355v1) | 2026-09-07T08:00:00+08:00 | VLA经验引用与模型生效分别版本化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/html/2609.04575v1) | 2026-09-07T08:00:00+08:00 | 执行expert与归一化参考质量分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models](https://arxiv.org/html/2609.04582v1) | 2026-09-07T08:00:00+08:00 | probe、logit排序与阈值分三层；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Persistent Teacher Anchoring for Tool-Using Agents](https://arxiv.org/html/2609.04773v1) | 2026-09-07T08:00:00+08:00 | teacher验证前缀不能先执行工具；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/html/2609.04875v1) | 2026-09-07T08:00:00+08:00 | 删除源记录须处理派生执行状态；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing](https://arxiv.org/html/2609.05309v1) | 2026-09-07T08:00:00+08:00 | 多流支持度与功能必要性分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [What Attention Recalls and Recurrence Controls in Hybrid Language Models](https://arxiv.org/html/2609.04434v1) | 2026-09-07T08:00:00+08:00 | 恢复state后验证kernel确实消费；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/html/2609.04895v1) | 2026-09-07T08:00:00+08:00 | 缓存适配会改变router和trace；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Conformity Breaks Conformal Prediction](https://arxiv.org/html/2609.04445v1) | 2026-09-07T08:00:00+08:00 | peer transcript属于校准输入分布；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Optimizer Memory Schedules for Outscaling the Overtraining Axis](https://arxiv.org/html/2609.04577v1) | 2026-09-07T08:00:00+08:00 | optimizer记忆按updates和horizon比较；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU](https://arxiv.org/html/2609.04852v1) | 2026-09-07T08:00:00+08:00 | 持久KV工作区不等于当次attention容量；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys](https://arxiv.org/html/2609.04382v1) | 2026-09-07T08:00:00+08:00 | 训练隐私联合观察forward与gradient；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Tuning Collective Patterns to Alleviate Congestion in Shared AI Clusters](https://arxiv.org/html/2609.04417v1) | 2026-09-07T08:00:00+08:00 | collective语义与拥塞适配分层；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |

## 4. 证据与知识整合

每项只认证列明的采用范围，不称整篇所有附件或artifact复现均通过。详细模型、工作负载、测量条件及反证见31项作者证据与另12项作者证据；独立结果见31项核验及实际写后检查、12项核验。笔记早期“待独立/未写”属于交接记录，当前处置以本正文及后续实际核验为准。不采用未披露条件的跨模型性能倍数。

### [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)

官方内部观察中的成功样本排除、人工介入及资源增长不支持因果加速。Ch66目标到证据与Ch67自主性测量已承载，不新增公司案例。 当前落点：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [An Alien Mind](https://openai.com/index/an-alien-mind/)

官方未披露可复算的趋势评测方法，不采用RSI预测或CoT退化普遍结论。Ch72 policy-bound sensor已区分可控性、可监控性、faithfulness与outcome，sensor不拥有授权权。 当前落点：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Iris: Climbing to the Search Frontier](https://arxiv.org/html/2609.04304v1)

exact-v1 §3.2/4.1/4.3要求保存token、mask、logprob及policy版本，跨policy前缀需校正；context reset/retry还改变历史和成本。Ch33 Partial Rollout及Ch75语义策略/记账已有覆盖，不把无CM对照当纯模型能力。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Rethinking Indirect Prompt Injection as a Test-Time Search Problem](https://arxiv.org/html/2609.04495v1)

exact-v1 §2/3/G.2将搜索历史、白盒环境和utility/security双判定纳入协议。Ch72运行评价已有attacker、harness、预算与最终effect，不从此推出黑盒泛化或更多token必更危险。 当前落点：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs](https://arxiv.org/html/2609.04526v1)

exact-v1 §3/5.1/5.4仅在固定codes及相同scale grid、clamp、layout下保持合并表示。已补Ch30 merge与runtime adapter之间的分支；表示一致不证明与高精度LoRA同容量或质量，保留动态adapter替代。 当前落点：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation](https://arxiv.org/html/2609.04263v1)

exact-v1 §3/5区分packed codes与校准activations，低秩补偿不等于真实低bit kernel。主PPL多seed与部分RULER范围不同；Ch45量化目标与Ch30秩预算已承载，不采通用速度结论。 当前落点：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/html/2609.04748v1)

exact-v1 III/IV/VI还发现host prompt cache混杂，reset仅支持受控状态重放；driver/session不同不能混算。Ch45 Token Replay Identity已区分construction provenance与唯一根因，不把FP16缓存误称随权重量化。 当前落点：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/html/2609.04518v1)

exact-v1 §3–5/9显示同manifest仍可改变组内参照人口；held-out未显著不是算法等价。Ch33 Hierarchy of Groups已分state/history、membership、population与credit，不把结果推广为所有多harness无用。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/html/2609.04565v1)

exact-v1 §4/7/B.1的mask、完整长度归一化、gather-then-project分别影响监督和张量成本。失败family排除及表格命名冲突收窄能力/排行主张；Ch33 teacher归因与mask已有覆盖。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Does the Selected Object Reach the Reader? Auditing Identity Handoffs in Grounded Language-Model Pipelines](https://arxiv.org/html/2609.04579v1)

exact-v1 §2–4/6区分selection、selected-return与答案正确性。已补Ch76授权后的交接段：仅当合同要求且对象有权使用才预留slot；保留选错、预算占用与hash不能证明日志时刻的边界。 当前落点：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Train What You Deploy:Token-Faithful Post-Training of a Production Coding](https://arxiv.org/html/2609.04678v1)

exact-v1 §3–7的Clean/Realign/Fork按真实序列和来源划mask；同binary不保不同profile数值同一，观测路径不保所有prefix。Ch33 trajectory tree、shared-prefix一次梯度及reward归属已承载。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/html/2609.05019v1)

exact-v1 §3–4.3中route提案不是commit，插入后重验后继；计时不含离线构建，高edit率多为终态剪枝。Ch81条件transition和联合恢复已有已提交前缀/effect边界，不采普适加速。 当前落点：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/html/2609.05198v1)

exact-v1 §2–3.2/5反复rollout且筛选使用teacher/student采样，验证集还参与监控；词型变化不证明新推理机制。Ch33 teacher归因与Ch27分布选择已承载，不把数据量headline当效率保证。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference](https://arxiv.org/html/2609.05275v1)

exact-v1 mask、depth/time schedule与部署分支支持训练子深度暴露，但局部缩放不保整网等价。已补Ch17 Dropout段，区分有损early exit与完整target验证的self-speculation，不把CS-3结果外推GPU或所有规模。 当前落点：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/html/2609.05279v1)

exact-v1 §3–4/7的四swap pair才是相关比较单位，删notes同时删context。Ch82测量向量和Ch77迁移边界已承载；成绩恢复不意味着通信成本恢复，也非普遍人员类比。 当前落点：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/html/2609.04801v1)

exact-v1 §3–5/7中的P来自外部witness，模型只判E/S；视觉相似不能认证身份。收益多来自support，track-disjoint非video-disjoint；Ch77 typed provenance/identity owner和Ch72权限已有覆盖。 当前落点：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/html/2609.05295v1)

exact-v1 §3.1–3.3/4.1/4.3支持冻结历史位移teacher再蒸馏，复用rollout不免第二梯度阶段。Ch33监督来源/版本已覆盖窄机制；JSD小不能直接推出所需reverse-KL界，保证继承仍Disputed，不进入Books。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。仅窄机制对读通过，不计整篇Evidence通过。

### [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/html/2609.05339v1)

exact-v1 §2–4.4的双向平均可能掩盖反向损失，等维embedding不代表兼容，恢复成本条件于成功。两个模型/合成历史不支持格式普遍排名；Ch77迁移合同及Ch76索引版本已有覆盖。 当前落点：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs](https://arxiv.org/html/2609.04281v1)

exact-v1 §3–5/A.1.8中text位置也可能携带视觉信息，晚层patch不证明文字独立控制。有限模型与first-token proxy限定结果；Ch80 Answer/Clarify/Abstain及Ch72 sensor/authority已承载。 当前落点：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Evidence Integration in Large Language Models](https://arxiv.org/html/2609.04290v1)

exact-v1定义及§6.2 SAT对照只测无效样本拒绝率，不是完整checker能力；换prompt/parse/context也不能说同次forward故意用已知错误。Ch80 constraint→repair/discard已有覆盖，只采通用证据接口。 当前落点：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [When Load-Balancing Goes Too Far: Expert Pruning in Over-Dispersed Mixture-of-Experts Models](https://arxiv.org/html/2609.04453v1)

exact-v1 §3–4最差域routing mass只是greedy proxy；固定top-k减少resident pool不直接降active FLOPs，PPL与任务可分离。Ch21低频不等低贡献及domain validation已有覆盖，保留Mixtral反例。 当前落点：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Atlas: Optimizing Deployment of Compound AI Workflows on Heterogeneous Clusters](https://arxiv.org/html/2609.04513v1)

exact-v1 III–VI/VIII的variant-pair quality bucket减少profile需求，却损失长程/循环历史。已补Ch56 compound graph段，预测只服务计划搜索并保E2E确认；不采普遍最低regret或完整资源可行性/p99保证。 当前落点：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective](https://arxiv.org/html/2609.04489v1)

exact-v1 §2.1/3.3/4–6中pause仍参与forward和下游梯度，匹配pause预算非匹配无pause计算。局部线性化retention不保实际能力；Ch29模板/mask共同定义objective已覆盖。 当前落点：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [CIERA: Cross-Iteration Exponent Reuse for Lossless Allgather in Sharded MoE Training](https://arxiv.org/html/2609.04609v1)

exact-v1 §2–4以HashCache、ExpCache及changed bitmap重建参数，经验低碰撞不等于绝无碰撞。已补Ch39身份失效/full fallback设计边界；作者bitwise/loss实验不含故障恢复，16卡实测不混128卡模拟。 当前落点：`TRAIN-ZERO` [Ch39](../../../../books/part-04-training-system/39-zero.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One](https://arxiv.org/html/2609.04531v1)

exact-v1 §2.4/3.1/3.3/5/B.5中不同步数分别训练student，单步另用teacher配对。已补Ch24离线训练换在线工作分支，同时失去后续修正机会；steps、NFE、CFG、最终decode分账，不采精确分布保持。 当前落点：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/html/2609.05401v1)

exact-v1 §3/4固定trajectory后分reward crossing、reference flip、均值误差；改写机会数影响SCR，人工210样本不证全等价。Ch66等价prompt及双干预臂已覆盖；离线选择不证明在线训练因果或物理安全。 当前落点：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [From Answers to Interpretations: Rethinking Ambiguity-Induced Aleatoric Uncertainty Estimation in LLMs](https://arxiv.org/html/2609.04543v1)

exact-v1 §3–5/Limitations用澄清聚类及频次形成sensor，不是真实posterior，漏解释仍会偏移。共享clarification set才是主对照，AUROC不证校准；Ch80竞争belief与Ch66校准已有覆盖。 当前落点：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents](https://arxiv.org/html/2609.04629v1)

exact-v1 Method/Evaluation用可信shadow检查support及逐项severity，SAFE_PROGRESS不是terminal PASS，容差可允许增幅。已补Ch78 executor在commit前准入恢复路径；monitor不获授权，无可行路径须升级，不采物理安全保证。 当前落点：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)。新增段已实际写入，前后交接及写后独立检查通过。

### [Large Language Models with At Most One Spike per Neuron](https://arxiv.org/html/2609.05151v1)

exact-v1 §4–7仅在线性区映射部分算子，LayerNorm近似且含non-spiking readout，没有物理芯片。Ch49 Accelerator Readiness要求operator、访存、通信到E2E测量已承载，仿真分支不转成硬件收益。 当前落点：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures](https://arxiv.org/html/2609.04819v1)

exact-v1 §3/4/Limitations中残差probe可读仍非transfer因果，家族模型非独立样本。Ch5存在/可读/使用与解释faithfulness预算已有覆盖；不采CKA各向异性笼统解释或ILO为真值。 当前落点：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models](https://arxiv.org/html/2609.04355v1)

exact-v1 III-C/D、IV-C仅冻结prefix允许KV复用，context ID按objective取用；滑窗改变分布，锁内state替换不保跨进程故障原子性。Ch26版本循环、Ch45身份已覆盖，不采全ACoB推导或速度安全headline。 当前落点：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/html/2609.04575v1)

exact-v1 Setup/成本/限制中参考集合可只参与router、不执行expert，权重和可小于一，非原函数exact变换。同家族有限任务且未显著非无损；Ch21 selection/contribution共同版本已有覆盖。 当前落点：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models](https://arxiv.org/html/2609.04582v1)

exact-v1 Controlled Testbed/诊断/controls只在二选一合成任务支持阈值掩盖logit信息，不是所有幻觉机制。未检出probe不证无信息；Ch5证据阶梯与Ch66校准已覆盖，不能直接迁移开放prompt。 当前落点：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Persistent Teacher Anchoring for Tool-Using Agents](https://arxiv.org/html/2609.04773v1)

exact-v1 §3–4先存pending turn，完整committed才执行工具，仅监督assistant、observation仍作context。固定teacher不保student on-policy，纠偏不证明错误恢复；Ch33来源/credit和Ch78 effect gate已有覆盖。 当前落点：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/html/2609.04875v1)

exact-v1 transition/splicing及限制要求clean checkpoint、固定随机性和声明的counterfactual observations；外部effect不能撤回。重放下界仅限特定oracle；Ch77完整state/replay与Ch78补偿已覆盖。 当前落点：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing](https://arxiv.org/html/2609.05309v1)

exact-v1 §3–6的top-k干预保weight sum，mixer→identity改变交换非删除skip，局部低权重不等于可删全局stream。单checkpoint无matching训练对照；Ch17 state/mixer/writeback联合合同已有覆盖。 当前落点：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [What Attention Recalls and Recurrence Controls in Hybrid Language Models](https://arxiv.org/html/2609.04434v1)

exact-v1 §3–5/Appendix B中multi-token路径可能重置state，干预还改变position和状态分布。Ch17真实scan/kernel与Ch45 KV/recurrent构造消费已有覆盖，不把有限分工推广为事实/控制的唯一分离。 当前落点：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/html/2609.04895v1)

exact-v1 §3–5/限制区分post-access保留和pre-access加载，主动插入也计transfer，hit高可伴bytes增加。decode trace模拟不含prefill、非真实latency；Ch54 router-conditioned cache及Ch21版本已覆盖。 当前落点：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Conformity Breaks Conformal Prediction](https://arxiv.org/html/2609.04445v1)

exact-v1 §2–4/8中题目相同不保exchangeability，condition-aware校准可恢复却使集合更宽。finite quantile不沿用人口等式；Ch66 calibration/release联合版本及依赖失效已有覆盖，不说conformal理论失效。 当前落点：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Optimizer Memory Schedules for Outscaling the Overtraining Axis](https://arxiv.org/html/2609.04577v1)

exact-v1 §3/5/6/8及配置说明moments、decay、LR联合控制历史影响；小模型同validation选型/报告，token倍数非wallclock。Ch28轨迹及tokens/batch/steps区别已有覆盖，不采大模型scaling保证。 当前落点：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU](https://arxiv.org/html/2609.04852v1)

exact-v1 §4/6/7分repository与active view，rawK负责位置重建；re-RoPE不恢复缺失causal interactions。step内固定历史且保质量/fallback；Ch45 packet/position、Ch54 tiering与Ch75投影已覆盖。 当前落点：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys](https://arxiv.org/html/2609.04382v1)

exact-v1 §2/5/8中decoy不入loss导致返回gradient可辨分区，但不等于完整文本重建。有限probe/noise不保DP、罕见token或收敛；Ch72 observable channels及联合attacker已有覆盖。 当前落点：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。限定采用范围与实际章节对读通过，不强制新增文字。

### [Tuning Collective Patterns to Alleviate Congestion in Shared AI Clusters](https://arxiv.org/html/2609.04417v1)

exact-v1 §4/5.3/7/8只允许有限rank/chunk等价变换，bitvector不证任意浮点reduction逐bit等价。4/8节点实测与ns3分开且探索有成本；Ch36语义/physical map/ordering已有覆盖，不升级为全网最优。 当前落点：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。限定采用范围与实际章节对读通过，不强制新增文字。

## 5. 缺口与下一步

以下均为本窗终态保留项，不用于正面证据、Books或无遗漏断言；材料到达时只按表中身份和范围定点重开。

| 材料 | 缺少什么、为什么必要 | 可接受替代材料与续跑位置 |
| --- | --- | --- |
| [浑元Research全部列表](https://hunyuan.tencent.com/research) | 终态保留：截图九行最新Aug28，只支持可见行在窗外；正文、HTTP及再次浏览器打开失败，不能认证本窗完整目录无新项，也不据此作无遗漏断言 | 可展开完整日期列表的HTML、完整截图或本窗条目URL；只补本窗筛选。Sep01–07共享一个来源请求，不重复索要七份论文 |
| [RISE exact-v1](https://arxiv.org/html/2609.05295v1) §3.2 | 终态保留：JSD约束不直接保证所引用结果需要的reverse-KL界，缺有效附加条件或修正推导；该保证不作正面证据且不进入Books | 作者勘误或含support/分布假设的有效证明；只重审该保证，已有窄更新机制及其他家族不重跑 |

没有普通待审、待写或待独立项。未运行训练、kernel或机器人复现，不把未承诺的复现扩大为新阻塞；不扫描每周源、不扩修其他日期。

## 6. 复核

复核者：`/root/screen_sep01`核root作者31项；`/root`核`/root/screen_sep03_04`作者12项。
结论：通过

43项采用范围均有非作者主源与实际Books绑定，七项新增段均有写后验收。初筛36篇、两机构和高风险/分层排除已独立检查，恢复五项另由作者题摘裁决；没有继承旧完成标签。RISE争议和浑元来源限制已作为不采用、不写Books或不支撑无遗漏断言的终态保留项，并保存精确重开条件，因此本窗闭环通过。本轮V3格式、内部文件链接、候选逐项对应、跨日arXiv去重与scoped diff检查通过；这些检查不能替代上述语义审阅或消除真实证据边界。
