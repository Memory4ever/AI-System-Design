# Weekly Research — 2026-W37

**规范：** V3  
**窗口：** 2026-09-06T09:00:00+08:00 ～ 2026-09-13T09:00:00+08:00  
**状态：** 完成  
**Books：** 纳入本次  
**检查时间：** 2026-09-14T10:53:06+08:00

## 1. 结论

本周复用 09-07 至 09-13 七份 Daily 的 111 个唯一材料家族，并只对 29 个每周来源及实际触发的按需来源做新增扫描；跨日与周级新增去重后，候选分母为 119。所有候选都已有证据处置和 Books 判断；七份 Daily、Weekly 作者自审与非作者 fresh-context 复核均已完成，Weekly Gate 已闭合。

新增周级材料把本周的系统主线收敛为三个状态边界：

1. **Runtime artifact 不能只声明“模型可加载”。** Runner capability、静态 plan、逐请求状态、量化 operand/output 格式和 fallback 共同定义实际执行语义。
2. **Checkpoint / weight transfer 的正确性取决于 canonical state 与完成证据。** Global layout 可以消除冗余 metadata collective，但低精度恢复仍要区分数值、编码与 optimizer continuation；异步 buffer 只有在消费者完成后才能复用。
3. **Serving control plane 的发布对象是带 readiness 的流量状态机。** DRA、canary、HTTPRoute 分流和 scale-to-zero 不能作为互不相干的功能开关。

Books 复用本周 Daily 已落实的章节改动，并新增一处 `TRAIN-CHECKPOINT` 正文：把 FP32 main parameter 定义为低精度训练的 canonical update state，明确 weights-only artifact 无法自动承诺量化编码可复现。其余七项周级候选均由现有具体论点承载，没有为制造 diff 重写章节。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 复用 [07](../../09/07/README.md)、[08](../../09/08/README.md)、[09](../../09/09/README.md)、[10](../../09/10/README.md)、[11](../../09/11/README.md)、[12](../../09/12/README.md)、[13](../../09/13/README.md) Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-ANTHROPIC | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-GOOGLE-AI | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-META-AI | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 受阻 | 09-08～09-13 的公开目录为空壳或无法稳定枚举；不支持本周绝对零事件断言 |
| SRC-QWEN | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-DEEPSEEK | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-MOONSHOT | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 受阻 | 09-12～09-13 的 Blog 已查；仓库补充入口受公共访问限额影响，不据此断言零 release |
| SRC-TENCENT-HUNYUAN | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-ZAI | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 受阻 | 09-08～09-13 的 Blog 卡片缺稳定日级时间，不能据此证明本周为零 |
| SRC-MINIMAX | 复用 09-07～09-13 七份 Daily 的该来源覆盖与证据 | 已检查 | 无 |
| SRC-ARXIV | 复用 09-07～09-13 七份 Daily 的当窗列表、筛选与证据；Weekly 未重扫 | 已检查 | 无 |
| SRC-MISTRAL | 官方 News 的本窗条目；逐项排除融资、合作及产品案例 | 已检查 | 无 |
| SRC-AI2 | 官方 Papers 首屏及本窗身份检索 | 受阻 | 目录缺稳定日级时间，未唯一定位到新的当窗材料家族；不支持“无遗漏”断言 |
| SRC-BLACK-FOREST-LABS | 官方 Research 本窗列表 | 已检查 | 无 |
| SRC-PHYSICAL-INTELLIGENCE | 官方研究/更新入口本窗列表 | 已检查 | 无 |
| SRC-WORLD-LABS | 官方 Research & Insights 本窗列表 | 已检查 | 无 |
| SRC-SSI | 官方 Updates 本窗列表 | 已检查 | 无 |
| SRC-REFLECTION-AI | 官方 Blog 与 News 的本窗技术条目 | 受阻 | 页面提取缺稳定日期；未将无日期条目冒充本周事件 |
| SRC-AMI-LABS | 官方 Updates 本窗列表 | 已检查 | 无 |
| SRC-THINKING-MACHINES | Connectionism 本窗文章列表 | 已检查 | 无 |
| SRC-PRIME-INTELLECT | 官方 Blog / Research 本窗列表 | 已检查 | 无 |
| SRC-SAKANA-AI | 09-10～09-12 官方 Blog：合作、Fugu 版本/产品说明与 World Model 综述逐项筛选 | 已检查 | Fugu 指向 2026-06 的既有报告，综述未提供新的 Sakana 原始机制；均在候选前关闭 |
| SRC-RECURSIVE | 官方 Recent Stories 本窗列表 | 已检查 | 无 |
| SRC-MIND-LAB | 官方 Publications / Updates 本窗列表 | 已检查 | 无 |
| SRC-SAND-AI | 官方组织仓库、release 与研究入口的本窗更新 | 已检查 | 仓库活跃但未发现本窗 release、RFC 或新研究正文；普通 commit 不作候选 |
| SRC-EVERMIND | 官方论文/更新入口的本窗技术条目 | 受阻 | 页面缺稳定日级日期；未取得可唯一归属本周的新材料 |
| SRC-METR | 官方 Research 本窗列表 | 已检查 | 无 |
| SRC-PYTORCH | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-MEGATRON-LM | 官方仓库按本窗 merged PR 查询；62 个事件逐项题目/说明筛选，保留 #6214、#6666 | 已检查 | 后续 API 额度耗尽不影响已保存的本窗查询结果 |
| SRC-DEEPSPEED | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-VERL | 官方仓库按本窗 merged PR 查询；19 个事件逐项题目/说明筛选，保留 #7764 | 已检查 | 无 |
| SRC-VLLM | 官方 Releases；v0.29.0 的 release notes 与关联变更定点审阅 | 已检查 | 无 |
| SRC-SGLANG | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-TRITON-LANGUAGE | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-FLASHINFER | 官方仓库按本窗 merged PR 查询；98 个事件逐项题目/说明筛选，保留 #4829、#4952 | 已检查 | 无 |
| SRC-NCCL | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-HF-TRANSFORMERS | 官方 Releases；v5.17.0 的 HYV4 runtime 能力说明定点审阅 | 已检查 | 无 |
| SRC-KSERVE | 官方 Releases；v0.21.0-rc0 的 DRA、canary 与 scaling 变更定点审阅 | 已检查 | 这是 pre-release，不外推为稳定版生产保证 |
| SRC-RAY | 官方 Releases 的本窗发布 | 已检查 | 无 |
| SRC-MCP | 官方 Releases 的本窗发布 | 已检查 | 无 |

## 3. 候选与判断

日级候选保持原报告的评分与 Books 处置；每行末尾链接其逐项证据。跨日以材料家族和原始身份复核，111 个日级候选的首个 primary URL 均唯一，未发现需要合并而重复计数的家族。周级来源新增 8 个家族，因此本表共 119 项。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/) | 2026-09-06T16:00:00+08:00 | 研发活动与完整研发结果分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [An Alien Mind](https://openai.com/index/an-alien-mind/) | 2026-09-06T17:00:00+08:00 | 监控风险披露不等于机制公开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Iris: Climbing to the Search Frontier](https://arxiv.org/html/2609.04304v1) | 2026-09-07T08:00:00+08:00 | partial rollout与context reset分责；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Rethinking Indirect Prompt Injection as a Test-Time Search Problem](https://arxiv.org/html/2609.04495v1) | 2026-09-07T08:00:00+08:00 | 注入成功率绑定搜索策略和预算；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs](https://arxiv.org/html/2609.04526v1) | 2026-09-07T08:00:00+08:00 | 量化adapter训练表示与导出身份一致；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation](https://arxiv.org/html/2609.04263v1) | 2026-09-07T08:00:00+08:00 | KV量化PPL恢复不等于检索恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/html/2609.04748v1) | 2026-09-07T08:00:00+08:00 | 缓存构造历史属于重放输入；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/html/2609.04518v1) | 2026-09-07T08:00:00+08:00 | credit分组改变参照人口；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/html/2609.04565v1) | 2026-09-07T08:00:00+08:00 | 稀疏loss不等于稀疏backbone；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Does the Selected Object Reach the Reader? Auditing Identity Handoffs in Grounded Language-Model Pipelines](https://arxiv.org/html/2609.04579v1) | 2026-09-07T08:00:00+08:00 | 已选对象需要显式身份交接；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Train What You Deploy:Token-Faithful Post-Training of a Production Coding](https://arxiv.org/html/2609.04678v1) | 2026-09-07T08:00:00+08:00 | 训练loss沿真实token与branch归属；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/html/2609.05019v1) | 2026-09-07T08:00:00+08:00 | 运行时只修尚未执行的后缀；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/html/2609.05198v1) | 2026-09-07T08:00:00+08:00 | 少prompt不等于少监督或计算；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference](https://arxiv.org/html/2609.05275v1) | 2026-09-07T08:00:00+08:00 | 结构mask只有实际跳算才省计算；3 + 2 + 2 = 7 | 深入完成 | 整合 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/html/2609.05279v1) | 2026-09-07T08:00:00+08:00 | 代理替换的成绩与协调成本分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/html/2609.04801v1) | 2026-09-07T08:00:00+08:00 | 记录真实、对象绑定和字段支持分开；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/html/2609.05295v1) | 2026-09-07T08:00:00+08:00 | 外推teacher机制与理论保证分开；2 + 2 + 2 = 6 | 争议 | 暂缓 — 保证未采用；窄机制已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/html/2609.05339v1) | 2026-09-07T08:00:00+08:00 | 记忆迁移保留方向和reader条件；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs](https://arxiv.org/html/2609.04281v1) | 2026-09-07T08:00:00+08:00 | 补问sensor不是人物或答案认证；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Evidence Integration in Large Language Models](https://arxiv.org/html/2609.04290v1) | 2026-09-07T08:00:00+08:00 | 生成、检查和采用证据分层；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [When Load-Balancing Goes Too Far: Expert Pruning in Over-Dispersed Mixture-of-Experts Models](https://arxiv.org/html/2609.04453v1) | 2026-09-07T08:00:00+08:00 | 路由proxy与域切片任务分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Atlas: Optimizing Deployment of Compound AI Workflows on Heterogeneous Clusters](https://arxiv.org/html/2609.04513v1) | 2026-09-07T08:00:00+08:00 | 复合图传播条件质量而非独立相乘；3 + 2 + 2 = 7 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective](https://arxiv.org/html/2609.04489v1) | 2026-09-07T08:00:00+08:00 | mask pause target不删其条件作用；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [CIERA: Cross-Iteration Exponent Reuse for Lossless Allgather in Sharded MoE Training](https://arxiv.org/html/2609.04609v1) | 2026-09-07T08:00:00+08:00 | 跨步通信编码引入双方缓存状态；2 + 2 + 3 = 7 | 深入完成 | 整合 — `TRAIN-ZERO` [Ch39](../../../../books/part-04-training-system/39-zero.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One](https://arxiv.org/html/2609.04531v1) | 2026-09-07T08:00:00+08:00 | 少步生成需训练少步映射；2 + 2 + 3 = 7 | 深入完成 | 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/html/2609.05401v1) | 2026-09-07T08:00:00+08:00 | 目标改写稳定性与准确性分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [From Answers to Interpretations: Rethinking Ambiguity-Induced Aleatoric Uncertainty Estimation in LLMs](https://arxiv.org/html/2609.04543v1) | 2026-09-07T08:00:00+08:00 | 解释歧义不等于答案多样性；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents](https://arxiv.org/html/2609.04629v1) | 2026-09-07T08:00:00+08:00 | 恢复准入与最终完成分权；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Large Language Models with At Most One Spike per Neuron](https://arxiv.org/html/2609.05151v1) | 2026-09-07T08:00:00+08:00 | spike代理不足以证明系统节能；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures](https://arxiv.org/html/2609.04819v1) | 2026-09-07T08:00:00+08:00 | PCA子空间混合不证明残差无信息；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models](https://arxiv.org/html/2609.04355v1) | 2026-09-07T08:00:00+08:00 | VLA经验引用与模型生效分别版本化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/html/2609.04575v1) | 2026-09-07T08:00:00+08:00 | 执行expert与归一化参考质量分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models](https://arxiv.org/html/2609.04582v1) | 2026-09-07T08:00:00+08:00 | probe、logit排序与阈值分三层；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Persistent Teacher Anchoring for Tool-Using Agents](https://arxiv.org/html/2609.04773v1) | 2026-09-07T08:00:00+08:00 | teacher验证前缀不能先执行工具；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/html/2609.04875v1) | 2026-09-07T08:00:00+08:00 | 删除源记录须处理派生执行状态；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing](https://arxiv.org/html/2609.05309v1) | 2026-09-07T08:00:00+08:00 | 多流支持度与功能必要性分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [What Attention Recalls and Recurrence Controls in Hybrid Language Models](https://arxiv.org/html/2609.04434v1) | 2026-09-07T08:00:00+08:00 | 恢复state后验证kernel确实消费；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/html/2609.04895v1) | 2026-09-07T08:00:00+08:00 | 缓存适配会改变router和trace；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Conformity Breaks Conformal Prediction](https://arxiv.org/html/2609.04445v1) | 2026-09-07T08:00:00+08:00 | peer transcript属于校准输入分布；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Optimizer Memory Schedules for Outscaling the Overtraining Axis](https://arxiv.org/html/2609.04577v1) | 2026-09-07T08:00:00+08:00 | optimizer记忆按updates和horizon比较；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU](https://arxiv.org/html/2609.04852v1) | 2026-09-07T08:00:00+08:00 | 持久KV工作区不等于当次attention容量；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys](https://arxiv.org/html/2609.04382v1) | 2026-09-07T08:00:00+08:00 | 训练隐私联合观察forward与gradient；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [Tuning Collective Patterns to Alleviate Congestion in Shared AI Clusters](https://arxiv.org/html/2609.04417v1) | 2026-09-07T08:00:00+08:00 | collective语义与拥塞适配分层；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/07/README.md#4-证据与知识整合) |
| [ChatGPT Images 2.5 与 System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations) | 2026-09-08T19:30:00+08:00 | 多模态生成发布把输入/输出 guard、结果指标与 provenance 绑定到同一 release；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)、`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [UniRL #377：EP expert-layout policy 离开 generic transport](https://github.com/Tencent-Hunyuan/UniRL/pull/377) | 2026-09-08T11:04:32+08:00 | model/backend layout policy 与通用权重传输分责；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)、`TRAIN-TENSOR-PARALLEL` [Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [UniRL #258：rank error fail-fast](https://github.com/Tencent-Hunyuan/UniRL/pull/258) | 2026-09-09T00:21:33+08:00 | completion-order error exposure 与 poisoned pool 阻断二次 RPC；3 + 3 + 2 = 8 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [VeOmni #1159：preserve shared gather gradients](https://github.com/ByteDance-Seed/VeOmni/pull/1159) | 2026-09-08T20:39:37+08:00 | distributed autograd borrowed/owned gradient buffer correctness；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [VeOmni #1158：Wan Ulysses SP attention correctness](https://github.com/ByteDance-Seed/VeOmni/pull/1158) | 2026-09-08T18:26:39+08:00 | sequence/head ownership 与 padding semantics 共同决定 SP 等价性；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [VeOmni #1162：await pending async save at train end](https://github.com/ByteDance-Seed/VeOmni/pull/1162) | 2026-09-08T10:50:15+08:00 | job terminal status 必须消费 checkpoint future 与异常；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [Kimi Code #3626：停止 child teardown 误取消 sibling tools](https://github.com/MoonshotAI/kimi-code/pull/3626) | 2026-09-08T10:26:13+08:00 | cancellation ownership 从 actor teardown 回到 spawn scope；3 + 2 + 2 = 7 | 深入完成 | 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [Kimi Code #3645：large file read 可恢复分页](https://github.com/MoonshotAI/kimi-code/pull/3645) | 2026-09-08T19:47:28+08:00 | observation cursor、Unicode 边界与 source-drift 检查；2 + 2 + 2 = 6 | 深入完成 | 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [Kimi Code #3492：reasoning_details round trip](https://github.com/MoonshotAI/kimi-code/pull/3492) | 2026-09-08T19:54:02+08:00 | summary 与 opaque continuation state 的身份、顺序和中断提交边界；2 + 2 + 2 = 6 | 深入完成 | 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [Kimi Code #3654：保留 structured tool results](https://github.com/MoonshotAI/kimi-code/pull/3654) | 2026-09-08T21:40:30+08:00 | human-readable 与 typed payload 的非等价性和 spill 完整性；3 + 2 + 2 = 7 | 深入完成 | 整合 — `AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [MiniMax Provider Verifier #60：M3 image scaling contract](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier/pull/60) | 2026-09-08T22:32:25+08:00 | provider 输入边界需要缩小、放大、像素上限与 orientation 的可执行矩阵；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/09/README.md#4-证据与知识整合) |
| [An alignment assessment of recent cybersecurity incidents](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) | 2026-09-09T21:34:27+08:00 | 研究型 cyber eval 暴露 pre-release scan、monitor view 与 action authority 的系统边界；3 + 3 + 3 = 9 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Kimi Code #3662/#3678/#3691：single producer → remove shadow view → event-source state store](https://github.com/MoonshotAI/kimi-code/pull/3691) | 2026-09-09T15:24:02+08:00 | event journal、fold、snapshot、reset/fork 与 ID 只由一条状态链提交；3 + 3 + 3 = 9 | 深入完成 | 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [UniRL #208：per-sample deterministic seed](https://github.com/Tencent-Hunyuan/UniRL/pull/208) | 2026-09-09T18:47:00+08:00 | `n>1` rollout 的 sample identity、探索与重排复现合同；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [UniRL #426：恢复 import 泄漏的 backend state](https://github.com/Tencent-Hunyuan/UniRL/pull/426) | 2026-09-09T18:52:50+08:00 | colocated runtime 的进程级 execution policy 不能由 import 静默改写；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [VeOmni #1164/#1172：local staging → global fail-closed commit](https://github.com/ByteDance-Seed/VeOmni/pull/1172) | 2026-09-09T11:49:51+08:00 | node-leader promotion、全局失败归约与 metadata-last 共同构成 checkpoint transaction；3 + 3 + 3 = 9 | 深入完成 | 整合 — `TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [VeOmni #1165：保留 video sampling identity](https://github.com/ByteDance-Seed/VeOmni/pull/1165) | 2026-09-09T14:07:00+08:00 | source FPS/frame count/selected indices 防止第二次采样改变训练输入；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)、`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability](https://arxiv.org/html/2609.07162v1) | 2026-09-10T08:00:00+08:00 | 一条 trace 无法判定需要跨执行比较的 safety hyperproperty；3 + 3 + 3 = 9 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Conduit: A Unified Residual-Stream Restoration Framework for KV Cache Reuse in Vision-Language Models](https://arxiv.org/html/2609.05821v1) | 2026-09-10T08:00:00+08:00 | shifted-prefix 多模态请求的 query-conditioned selective KV refresh；虽总分 6，因确认的 KV reuse 知识缺口强制深入；2 + 2 + 2 = 6 | 深入完成 | 整合 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Deadline-Aware Adaptive Prefill Chunking for Efficient Large Language Model Serving](https://arxiv.org/html/2609.07883v1) | 2026-09-10T08:00:00+08:00 | Prefill chunk 选择由 active Decode 的最早 deadline 约束；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Are Verifier Errors Independent Within a GRPO Group? Evidence from Qwen2.5 Rollouts](https://arxiv.org/html/2609.06386v1) | 2026-09-10T08:00:00+08:00 | 组内 verifier error 相关性改变 GRPO 有效样本量与评估合同；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Hyperparameter Scaling Laws Across MoE Sparsity](https://arxiv.org/html/2609.08690v1) | 2026-09-10T08:00:00+08:00 | activation ratio 是 MoE recipe identity 的独立坐标；3 + 2 + 3 = 8 | 深入完成 | 整合 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](https://arxiv.org/html/2609.08279v1) | 2026-09-10T08:00:00+08:00 | restore counterfactual 分离 eviction destruction、retrieval miss 与 reader residual；3 + 2 + 3 = 8 | 深入完成 | 整合 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training](https://arxiv.org/html/2609.07108v1) | 2026-09-10T08:00:00+08:00 | evolving policy 下 draft co-training 需要 branch-aware CP 与 PP side-channel；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)、`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Parallelism Strategy Chaining for Fast Training Convergence](https://arxiv.org/html/2609.07236v1) | 2026-09-10T08:00:00+08:00 | 并行策略选择从最短 step time 提升为训练阶段相关的 time-to-quality；3 + 3 + 2 = 8 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Measurement-Driven Diagnosis and Mitigation of Host-CPU Co-location Interference in Single-GPU LLM Serving on a Multi-GPU Server](https://arxiv.org/html/2609.05425v1) | 2026-09-10T08:00:00+08:00 | host co-tenant 干扰需从服务阶段 tail 诊断，不能由 GPU counter 直接归因；3 + 3 + 2 = 8 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Analytical Resource Management for Fine-grained MoE Computation-Communication Overlap](https://arxiv.org/html/2609.07536v1) | 2026-09-10T08:00:00+08:00 | readiness DAG 与 CTA residency 共同约束 compute/communication overlap；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)、`INFER-EXECUTION` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) ；[日级证据](../../09/10/README.md#4-证据与知识整合) |
| [Compass](https://arxiv.org/html/2609.10549v1) | 2026-09-11T08:00:00+08:00 | TP overlap 需按 topology 与 decomposition overhead 选择；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) / `TRAIN-TENSOR-PARALLEL` [Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Data-Efficient Language Modeling](https://arxiv.org/html/2609.10702v1) | 2026-09-11T08:00:00+08:00 | 有限 exposure 下须分离可见线索、监督目标与功能保持；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) / `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [HuRo](https://arxiv.org/html/2609.10706v1) | 2026-09-11T08:00:00+08:00 | 人类视频转 VLA 监督必须同时对齐 observation、action 与缺失信号；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [NCP-ArchPreview](https://arxiv.org/pdf/2609.10715v1) | 2026-09-11T08:00:00+08:00 | next-token objective 叠加离散 concept state，并反馈 token generation；3 + 3 + 3 = 9 | 深入完成 | 整合 — `MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [The Truth Was Never Gone](https://arxiv.org/html/2609.10739v1) | 2026-09-11T08:00:00+08:00 | probe label 与目标语义可 perfect alias，要求 rival-context identification；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [When Synthetic Data Hurts](https://arxiv.org/html/2609.10750v1) | 2026-09-11T08:00:00+08:00 | skill router 的 synthetic ID gain 可与真实/OOD forgetting 并存；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) / `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Composable CXL Memory](https://arxiv.org/html/2609.10790v1) | 2026-09-11T08:00:00+08:00 | DRA/CDI 把共享 CXL region 提升为可调度 KV resource；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [REACH](https://arxiv.org/html/2609.10861v1) | 2026-09-11T08:00:00+08:00 | inner correction + exceptional outer recovery 改写 HBM reliability fast path；3 + 3 + 2 = 8 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [When Validation Stops Learning](https://arxiv.org/html/2609.10873v1) | 2026-09-11T08:00:00+08:00 | update gate 要同时度量错误控制与丢失学习机会；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Rethinking Verbalized Confidence](https://arxiv.org/html/2609.10996v1) | 2026-09-11T08:00:00+08:00 | judge soft-score channel 随 model generation 改变，需重新校准而非沿用惯例；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [The Agent Incident Registry](https://arxiv.org/html/2609.11030v1) | 2026-09-11T08:00:00+08:00 | incident taxonomy 必须分 causal role、disclosure 与 realized outcome；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [T1](https://arxiv.org/html/2609.11042v1) | 2026-09-11T08:00:00+08:00 | 长轨迹 MoE RL 同时要求 token fidelity 与 routing fidelity；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Grounding Agent Memory](https://arxiv.org/html/2609.11060v1) | 2026-09-11T08:00:00+08:00 | memory write 从 trajectory summary 演进为 propose-probe-commit；3 + 3 + 3 = 9 | 深入完成 | 整合 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Benchmark Radar](https://arxiv.org/html/2609.11115v1) | 2026-09-11T08:00:00+08:00 | benchmark catalog 将 identity、artifact、adoption 与 score history 分层；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Phase-Decoupled Power Control](https://arxiv.org/html/2609.11133v1) | 2026-09-11T08:00:00+08:00 | P/D lane 使用不同 actuator，并由 stack fingerprint 与 tail SLO 校准；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Quantifying the Memorization-to-Generalization Transition](https://arxiv.org/html/2609.10657v1) | 2026-09-11T08:00:00+08:00 | grokking onset 是 data、width、learning rate 与 weight decay 的条件 phase boundary；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [GEOSTEER](https://arxiv.org/html/2609.10658v1) | 2026-09-11T08:00:00+08:00 | activation steering 从固定方向改为保持范数的自适应 geodesic optimization；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [AcFlow](https://arxiv.org/html/2609.10723v1) | 2026-09-11T08:00:00+08:00 | 冻结 DiT 时以 concept-conditioned activation flow 建立连续、token-dependent 控制接口；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [ExaServe](https://arxiv.org/html/2609.10812v1) | 2026-09-11T08:00:00+08:00 | 3072 replicas 下暴露 centralized proxy 与 Ray control-plane 的扩展失效；2 + 3 + 2 = 7 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Detectable Only Where It Is Confounded](https://arxiv.org/html/2609.10830v1) | 2026-09-11T08:00:00+08:00 | duplication count 反证常用 membership-evidence 构造的可识别性；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Flow Duality and Source Geometry](https://arxiv.org/html/2609.10863v1) | 2026-09-11T08:00:00+08:00 | continuous/discrete flow matching 的条件 duality 将 source geometry 变为 transition timing 变量；2 + 1 + 3 = 6 | 深入完成 | 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Story Imprinting](https://arxiv.org/html/2609.10883v1) | 2026-09-11T08:00:00+08:00 | story-only fine-tuning 可把角色偏好与条件性有害行为 imprint 到 Assistant；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [ReactHuman](https://arxiv.org/html/2609.10895v1) | 2026-09-11T08:00:00+08:00 | 用真实 action consequences 区分合理、安全与物理 grounding；3 + 2 + 3 = 8 | 深入完成 | 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [SearchAtlas](https://arxiv.org/html/2609.10901v1) | 2026-09-11T08:00:00+08:00 | evidential query graph 暴露 search evidence propagation 与 constraint loss；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [IMLE-VLA](https://arxiv.org/html/2609.10915v1) | 2026-09-11T08:00:00+08:00 | single-step cIMLE action head 改变 VLA latency 与 multimodal coverage 取舍；3 + 2 + 2 = 7 | 深入完成 | 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Measuring the Value of World-Model Updates](https://arxiv.org/html/2609.10954v1) | 2026-09-11T08:00:00+08:00 | fork ledger 让单次 world-model update 的反事实效用可观测；3 + 2 + 3 = 8 | 深入完成 | 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Decoupling Readiness from Release](https://arxiv.org/html/2609.10964v1) | 2026-09-11T08:00:00+08:00 | 以 CVaR 与 released-work budget 控制 Agent workflow contention tail；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Fengshui](https://arxiv.org/html/2609.10970v1) | 2026-09-11T08:00:00+08:00 | 联合选择 chiplet ecosystem、accelerator、memory、fusion 与 parallelism；3 + 3 + 2 = 8 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Phases in Associative Memories via Hidden Neurons](https://arxiv.org/html/2609.10976v1) | 2026-09-11T08:00:00+08:00 | 统一 polynomial/exponential associative-memory regimes 并分离 visible stability 与 hidden storage；2 + 1 + 3 = 6 | 标准完成 | 仅报告 — Explanatory Analogy；不改 Books ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Demystifying the Privacy-Utility Trade-off](https://arxiv.org/html/2609.10992v1) | 2026-09-11T08:00:00+08:00 | context privacy 清洗须联合 intent、factual integrity、coherence 与属性组合；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Distribution-aware Language Neuron Identification](https://arxiv.org/html/2609.10993v1) | 2026-09-11T08:00:00+08:00 | neuron identification 从 sign entropy 改为 distribution overlap 并以干预验证 specificity；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [K/V-Cache Interventions Dissociate Representation Alignment](https://arxiv.org/html/2609.11020v1) | 2026-09-11T08:00:00+08:00 | KV trajectory transplantation 分离 representation alignment 与 persona expression；3 + 1 + 3 = 7 | 深入完成 | 整合 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [EMMI](https://arxiv.org/html/2609.11058v1) | 2026-09-11T08:00:00+08:00 | edge/server split 改为 fused、compressed、fixed-size multimodal representation；2 + 3 + 2 = 7 | 深入完成 | 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Belief-Shift Branching](https://arxiv.org/html/2609.11061v1) | 2026-09-11T08:00:00+08:00 | Tree RL 用 value-curve pivot 决定 fork，改变有限 rollout 的 credit assignment；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [The Information Geometry of Large Language Models](https://arxiv.org/html/2609.11063v1) | 2026-09-11T08:00:00+08:00 | Fisher-Rao output geometry 提供跨架构比较与 minimum-disturbance intervention；3 + 3 + 3 = 9 | 深入完成 | 整合 — `MODEL-POSITION-ENCODING` [Ch13](../../../../books/part-02-model/13-position-encoding.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [MOSAIC](https://arxiv.org/html/2609.11065v1) | 2026-09-11T08:00:00+08:00 | GraphRAG retrieval 改为 query-specific seed、traversal、stop 与 evidence policy；3 + 2 + 3 = 8 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [When Noise Fabricates Bias](https://arxiv.org/html/2609.11067v1) | 2026-09-11T08:00:00+08:00 | 文本噪声会非对称制造 judge bias，修正 bias measurement validity；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Beyond Solver Verdicts](https://arxiv.org/html/2609.11085v1) | 2026-09-11T08:00:00+08:00 | solver verdict 正确不能证明 formal translation faithful；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [KuaiRP Series](https://arxiv.org/html/2609.11127v1) | 2026-09-11T08:00:00+08:00 | 以 domain teacher 与原 base student 恢复领域注入后的通用能力；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) / `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [The Oligarch Barely Steers Model Collapse](https://arxiv.org/html/2609.11146v1) | 2026-09-11T08:00:00+08:00 | 多模型递归训练中 concentration/head identity 影响较弱，composition、human fraction 与 susceptibility 更能解释速度；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) ；[日级证据](../../09/11/README.md#4-证据与知识整合) |
| [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one/) | 2026-09-11T18:00:00+08:00 | 平台控制权从嵌入式 client policy 迁移为集中服务，并揭示集中化后的运行时反馈环；3 + 3 + 3 = 9 | 深入完成 | 整合 — `PLATFORM-FOUNDATIONS` [Ch57](../../../../books/part-06-ai-infrastructure/57-what-is-ai-platform.md) ；[日级证据](../../09/12/README.md#4-证据与知识整合) |
| [vLLM v0.29.0](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) | 2026-09-09T16:54:49+08:00 | 默认 Runner 迁移把 capability fallback、KV sizing 与采样内存纳入同一 runtime contract；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Transformers v5.17.0](https://github.com/huggingface/transformers/releases/tag/v5.17.0) | 2026-09-09T23:42:45+08:00 | 能加载含 MTP 权重的 checkpoint 不等于当前 runtime 会执行 MTP；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [KServe v0.21.0-rc0](https://github.com/kserve/kserve/releases/tag/v0.21.0-rc0) | 2026-09-11T01:44:50+08:00 | 推理服务发布把 DRA、canary readiness、HTTPRoute 流量与 scale-to-zero 连成控制面状态机；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-PRODUCTION` [Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [Megatron-LM #6214：由参数布局推导 MFSDP v2 checkpoint chunk metadata](https://github.com/NVIDIA/Megatron-LM/pull/6214) | 2026-09-09 | global layout 已拥有 shard identity 时，可用局部算术替代逐 DTensor 的 metadata collective；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [Megatron-LM #6666：从 FP32 main parameter 重建量化参数](https://github.com/NVIDIA/Megatron-LM/pull/6666) | 2026-09-10 | 恢复合同必须区分数值等价、量化编码等价与 optimizer update continuity；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [verl #7764：权重传输返回前消费 completion markers](https://github.com/volcengine/verl/pull/7764) | 2026-09-09 | 可复用通信 buffer 的生命周期必须由远端完成证据而非 barrier 或本地 enqueue 结束；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [FlashInfer #4829：统一 PrimTS plan/run 与 page-table contract](https://github.com/flashinfer-ai/flashinfer/pull/4829) | 2026-09-09 | 静态 execution profile 与逐请求 launch state 分权，才能安全复用 plan 与 CUDA Graph；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [FlashInfer #4952：量化合同拆成 weight/activation/output axes](https://github.com/flashinfer-ai/flashinfer/pull/4952) | 2026-09-09 | 单一 variant 名无法表达 operand、输出格式与 runner capability 的组合边界；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |

## 4. 证据与知识整合

### 日级 111 项候选：复用已完成的逐项证据

Weekly 不重新抓取或无差别重读每日来源。候选表已经为每个日级家族链接原 Daily 的逐项原始材料、证据边界与 Books 比较；本次只复核跨日身份与处置是否冲突。结果如下：

- [09-07](../../09/07/README.md#4-证据与知识整合)：43 项；无跨日重复或处置冲突。
- [09-08](../../09/08/README.md#4-证据与知识整合)：0 项；零候选结论保留。
- [09-09](../../09/09/README.md#4-证据与知识整合)：11 项；无跨日重复或处置冲突。
- [09-10](../../09/10/README.md#4-证据与知识整合)：16 项；无跨日重复或处置冲突。
- [09-11](../../09/11/README.md#4-证据与知识整合)：40 项；无跨日重复或处置冲突。
- [09-12](../../09/12/README.md#4-证据与知识整合)：1 项；OpenAI 在线存储平台的集中控制与反馈环已写入 `PLATFORM-FOUNDATIONS`，独立复核已通过。
- [09-13](../../09/13/README.md#4-证据与知识整合)：0 项；零候选结论经独立复核通过。

### [Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [An Alien Mind](https://openai.com/index/an-alien-mind/)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Iris: Climbing to the Search Frontier](https://arxiv.org/html/2609.04304v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Rethinking Indirect Prompt Injection as a Test-Time Search Problem](https://arxiv.org/html/2609.04495v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs](https://arxiv.org/html/2609.04526v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation](https://arxiv.org/html/2609.04263v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/html/2609.04748v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/html/2609.04518v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/html/2609.04565v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Does the Selected Object Reach the Reader? Auditing Identity Handoffs in Grounded Language-Model Pipelines](https://arxiv.org/html/2609.04579v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Train What You Deploy:Token-Faithful Post-Training of a Production Coding](https://arxiv.org/html/2609.04678v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/html/2609.05019v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/html/2609.05198v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference](https://arxiv.org/html/2609.05275v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/html/2609.05279v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/html/2609.04801v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/html/2609.05295v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/html/2609.05339v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs](https://arxiv.org/html/2609.04281v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Evidence Integration in Large Language Models](https://arxiv.org/html/2609.04290v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Load-Balancing Goes Too Far: Expert Pruning in Over-Dispersed Mixture-of-Experts Models](https://arxiv.org/html/2609.04453v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Atlas: Optimizing Deployment of Compound AI Workflows on Heterogeneous Clusters](https://arxiv.org/html/2609.04513v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective](https://arxiv.org/html/2609.04489v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [CIERA: Cross-Iteration Exponent Reuse for Lossless Allgather in Sharded MoE Training](https://arxiv.org/html/2609.04609v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One](https://arxiv.org/html/2609.04531v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models](https://arxiv.org/html/2609.05401v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [From Answers to Interpretations: Rethinking Ambiguity-Induced Aleatoric Uncertainty Estimation in LLMs](https://arxiv.org/html/2609.04543v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents](https://arxiv.org/html/2609.04629v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Large Language Models with At Most One Spike per Neuron](https://arxiv.org/html/2609.05151v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures](https://arxiv.org/html/2609.04819v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models](https://arxiv.org/html/2609.04355v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/html/2609.04575v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models](https://arxiv.org/html/2609.04582v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Persistent Teacher Anchoring for Tool-Using Agents](https://arxiv.org/html/2609.04773v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/html/2609.04875v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing](https://arxiv.org/html/2609.05309v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [What Attention Recalls and Recurrence Controls in Hybrid Language Models](https://arxiv.org/html/2609.04434v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/html/2609.04895v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Conformity Breaks Conformal Prediction](https://arxiv.org/html/2609.04445v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Optimizer Memory Schedules for Outscaling the Overtraining Axis](https://arxiv.org/html/2609.04577v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU](https://arxiv.org/html/2609.04852v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the Decoys](https://arxiv.org/html/2609.04382v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Tuning Collective Patterns to Alleviate Congestion in Shared AI Clusters](https://arxiv.org/html/2609.04417v1)

复用 [09-07 Daily 的逐项证据与 Books 判断](../../09/07/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [ChatGPT Images 2.5 与 System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [UniRL #377：EP expert-layout policy 离开 generic transport](https://github.com/Tencent-Hunyuan/UniRL/pull/377)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [UniRL #258：rank error fail-fast](https://github.com/Tencent-Hunyuan/UniRL/pull/258)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VeOmni #1159：preserve shared gather gradients](https://github.com/ByteDance-Seed/VeOmni/pull/1159)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VeOmni #1158：Wan Ulysses SP attention correctness](https://github.com/ByteDance-Seed/VeOmni/pull/1158)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VeOmni #1162：await pending async save at train end](https://github.com/ByteDance-Seed/VeOmni/pull/1162)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Kimi Code #3626：停止 child teardown 误取消 sibling tools](https://github.com/MoonshotAI/kimi-code/pull/3626)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Kimi Code #3645：large file read 可恢复分页](https://github.com/MoonshotAI/kimi-code/pull/3645)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Kimi Code #3492：reasoning_details round trip](https://github.com/MoonshotAI/kimi-code/pull/3492)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Kimi Code #3654：保留 structured tool results](https://github.com/MoonshotAI/kimi-code/pull/3654)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [MiniMax Provider Verifier #60：M3 image scaling contract](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier/pull/60)

复用 [09-09 Daily 的逐项证据与 Books 判断](../../09/09/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [An alignment assessment of recent cybersecurity incidents](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Kimi Code #3662/#3678/#3691：single producer → remove shadow view → event-source state store](https://github.com/MoonshotAI/kimi-code/pull/3691)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [UniRL #208：per-sample deterministic seed](https://github.com/Tencent-Hunyuan/UniRL/pull/208)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [UniRL #426：恢复 import 泄漏的 backend state](https://github.com/Tencent-Hunyuan/UniRL/pull/426)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VeOmni #1164/#1172：local staging → global fail-closed commit](https://github.com/ByteDance-Seed/VeOmni/pull/1172)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [VeOmni #1165：保留 video sampling identity](https://github.com/ByteDance-Seed/VeOmni/pull/1165)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability](https://arxiv.org/html/2609.07162v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Conduit: A Unified Residual-Stream Restoration Framework for KV Cache Reuse in Vision-Language Models](https://arxiv.org/html/2609.05821v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Deadline-Aware Adaptive Prefill Chunking for Efficient Large Language Model Serving](https://arxiv.org/html/2609.07883v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Are Verifier Errors Independent Within a GRPO Group? Evidence from Qwen2.5 Rollouts](https://arxiv.org/html/2609.06386v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Hyperparameter Scaling Laws Across MoE Sparsity](https://arxiv.org/html/2609.08690v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](https://arxiv.org/html/2609.08279v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training](https://arxiv.org/html/2609.07108v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Parallelism Strategy Chaining for Fast Training Convergence](https://arxiv.org/html/2609.07236v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Measurement-Driven Diagnosis and Mitigation of Host-CPU Co-location Interference in Single-GPU LLM Serving on a Multi-GPU Server](https://arxiv.org/html/2609.05425v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Analytical Resource Management for Fine-grained MoE Computation-Communication Overlap](https://arxiv.org/html/2609.07536v1)

复用 [09-10 Daily 的逐项证据与 Books 判断](../../09/10/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Compass](https://arxiv.org/html/2609.10549v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Data-Efficient Language Modeling](https://arxiv.org/html/2609.10702v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [HuRo](https://arxiv.org/html/2609.10706v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [NCP-ArchPreview](https://arxiv.org/pdf/2609.10715v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [The Truth Was Never Gone](https://arxiv.org/html/2609.10739v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Synthetic Data Hurts](https://arxiv.org/html/2609.10750v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Composable CXL Memory](https://arxiv.org/html/2609.10790v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [REACH](https://arxiv.org/html/2609.10861v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Validation Stops Learning](https://arxiv.org/html/2609.10873v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Rethinking Verbalized Confidence](https://arxiv.org/html/2609.10996v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [The Agent Incident Registry](https://arxiv.org/html/2609.11030v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [T1](https://arxiv.org/html/2609.11042v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Grounding Agent Memory](https://arxiv.org/html/2609.11060v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Benchmark Radar](https://arxiv.org/html/2609.11115v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Phase-Decoupled Power Control](https://arxiv.org/html/2609.11133v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Quantifying the Memorization-to-Generalization Transition](https://arxiv.org/html/2609.10657v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [GEOSTEER](https://arxiv.org/html/2609.10658v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [AcFlow](https://arxiv.org/html/2609.10723v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [ExaServe](https://arxiv.org/html/2609.10812v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Detectable Only Where It Is Confounded](https://arxiv.org/html/2609.10830v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Flow Duality and Source Geometry](https://arxiv.org/html/2609.10863v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Story Imprinting](https://arxiv.org/html/2609.10883v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [ReactHuman](https://arxiv.org/html/2609.10895v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [SearchAtlas](https://arxiv.org/html/2609.10901v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [IMLE-VLA](https://arxiv.org/html/2609.10915v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Measuring the Value of World-Model Updates](https://arxiv.org/html/2609.10954v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Decoupling Readiness from Release](https://arxiv.org/html/2609.10964v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Fengshui](https://arxiv.org/html/2609.10970v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Phases in Associative Memories via Hidden Neurons](https://arxiv.org/html/2609.10976v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Demystifying the Privacy-Utility Trade-off](https://arxiv.org/html/2609.10992v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Distribution-aware Language Neuron Identification](https://arxiv.org/html/2609.10993v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [K/V-Cache Interventions Dissociate Representation Alignment](https://arxiv.org/html/2609.11020v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [EMMI](https://arxiv.org/html/2609.11058v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Belief-Shift Branching](https://arxiv.org/html/2609.11061v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [The Information Geometry of Large Language Models](https://arxiv.org/html/2609.11063v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [MOSAIC](https://arxiv.org/html/2609.11065v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [When Noise Fabricates Bias](https://arxiv.org/html/2609.11067v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Beyond Solver Verdicts](https://arxiv.org/html/2609.11085v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [KuaiRP Series](https://arxiv.org/html/2609.11127v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [The Oligarch Barely Steers Model Collapse](https://arxiv.org/html/2609.11146v1)

复用 [09-11 Daily 的逐项证据与 Books 判断](../../09/11/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。

### [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one/)

复用 [09-12 Daily 的逐项证据与 Books 判断](../../09/12/README.md#4-证据与知识整合)。本周身份去重与新增周级证据未改变该处置。


### [vLLM v0.29.0](https://github.com/vllm-project/vllm/releases/tag/v0.29.0)

精确采用 v0.29.0 release。Model Runner V2 成为默认路径，同时对尚未支持的 sequence parallelism、dual-batch overlap、elastic expert parallelism、custom logits processor 和部分 speculative decoding 保留 MRV1 fallback。CUDA Graph memory profiling 用于 KV auto-sizing，batch-sharded sampling 将每步 logits memory 按 TP 分片；这些是作者 release 的实现主张，不是跨硬件性能保证。

本项目采用的是“默认 backend 仍须以 capability matrix 和 fallback 解释实际路径”。Ch49 已经把 model revision、precision、KV layout、kernel/backend capability、plan revision 和 fallback 定义为 execution artifact identity，因此不新增正文。594 commits 是 release 规模，不等于 594 个独立候选。

### [Transformers v5.17.0](https://github.com/huggingface/transformers/releases/tag/v5.17.0)

精确采用 v5.17.0 release。HYV4 loader 支持模型结构，但 release 明确说明当前实现不执行 MTP layers：发布 checkpoint 保留这些 weights 供其他 runtime speculative decoding 使用，加载时则忽略它们。

该事实否定“checkpoint 字段存在且 load 成功就意味着能力已执行”。Ch49 已要求 deployment artifact 同时绑定 architecture、module mapping、graph rewrite、runtime/backend capability 与实际执行证据，已经完整承载此结论；它只证明当前 Transformers 版本的行为，不证明 HYV4/MTP 的模型质量或其他 runtime 行为。

### [KServe v0.21.0-rc0](https://github.com/kserve/kserve/releases/tag/v0.21.0-rc0)

精确采用 v0.21.0-rc0 pre-release。release 把 ServingRuntime DRA `resourceClaims`、RawDeployment HTTPRoute canary traffic split、`CanaryPredictorReady` gating 与 direct KEDA scaling 带入同一版本；其中 readiness gating 用来避免 canary 未准备好时的暂态 503。

稳定结论不是“KServe 已经保证生产可靠”，而是资源取得、revision readiness、traffic commit 与缩容条件必须由同一发布状态机协调。Ch73 已按 readiness gate、progressive delivery、rollback 与 SLO evidence 组织这条链，现有覆盖充分。pre-release、未运行本仓库环境的 e2e、未披露具体模型/硬件/并发/SLO，使它不能支撑性能或稳定版兼容承诺。

### [Megatron-LM #6214：由参数布局推导 MFSDP v2 checkpoint chunk metadata](https://github.com/NVIDIA/Megatron-LM/pull/6214)

精确采用 merged PR #6214。旧 generic helper 为每个 DTensor 通过 `all_gather_object` 恢复 shard offset；MFSDP v2 的 `GlobalLayout` 已保存参数 global element offset，`DBuffer` 又保存本 rank owned range，因而 chunk metadata 可以用两者交集的局部算术推导。PR 的测试检查 byte-identical checkpoint 并阻断相关 collectives。

这证明的是“已有权威 layout 时 metadata 不必再次协商”，不是所有 checkpoint collective 都可移除。Ch35 已要求 global tensor identity、local shard offsets、dtype/shape 与 layout metadata，并把 resharding 建立在 global coordinates 上；现有论点正好拥有该机制。Experimental MFSDP v2、测试规模和未披露的模型级端到端保存时间限制性能外推。

### [Megatron-LM #6666：从 FP32 main parameter 重建量化参数](https://github.com/NVIDIA/Megatron-LM/pull/6666)

精确采用 merged PR #6666。使用 `--fp8-param-gather` 时，checkpoint 保存反量化 BF16 weight 而不保存 block scales；`MXFP8 → BF16 → MXFP8` 不是编码幂等，但 PR 测得反量化数值与 GEMM 不变。Optimizer 的 FP32 main parameter 能精确 round-trip，model parameter 又是它的派生函数，因此修复在 optimizer load 后经训练时相同路径重新量化、同步并强制 parameter all-gather。

这是新的长期不变量：恢复测试必须声明比较的是 represented value、quantization encoding 还是 update state；有 canonical FP32 main state 时可以重建派生副本，没有 optimizer state 的 weights-only / finetune / release path 则需要保存 scale/format 或降低合同。该增量已写入 [Ch35](../../../../books/part-04-training-system/35-checkpoint.md)“低精度参数恢复要区分数值、编码与更新状态”。公开证据限于特定 MXFP8 路径、4 张 GB300、TP=2；约 5 ms 是 unit-test model 的 warm load，不作模型规模成本结论。

### [verl #7764：权重传输返回前消费 completion markers](https://github.com/volcengine/verl/pull/7764)

精确采用 merged PR #7764。可复用传输 buffer 的旧路径可能在下一轮覆盖前只完成本地 enqueue；即使存在 barrier，上一轮的远端 read/completion marker 仍可能占据 slot。修复要求 sender 与中间 forwarding rank 在 weight update 返回前消费 outstanding completion，才把 buffer generation 交给下一轮。

本项目采用的是 completion ownership：enqueue、barrier 和 remote consumption 是不同事件，复用内存必须等待真正拥有读取责任的一方提交完成。Ch36 已把通信对象定义为版本化训练状态，并把 buffer generation、completion 和 rollout/update weight version 放在同一状态迁移中，因此已有覆盖。PR 的 component test 不等于完整 Agentic RL workload、不同互连或生产压力下的证明。

### [FlashInfer #4829：统一 PrimTS plan/run 与 page-table contract](https://github.com/flashinfer-ai/flashinfer/pull/4829)

精确采用 merged PR #4829，范围是 experimental PrimTS。新合同让 `plan()` 拥有 device、batch/capacity 上界、head/page geometry、dtype、query storage 和 mask/window specialization；`run()` 接收 query/KV tensors、page tables、lengths、offsets、window bounds、scales 与 output 等逐请求状态。失败的 re-plan 不覆盖最后一个完整 plan，成功 re-plan 则使旧 CUDA Graph capture 失效。

该机制把“可安全缓存的静态 execution profile”与“每次 launch 必须更新的动态状态”分开。Ch49 已要求 plan revision、shape/KV layout、workspace/capture lifetime、safe commit 和 fallback 共同构成 execution plan identity，现有覆盖充分。该 PR 修改 public experimental API，且未提供端到端 serving benchmark；不能据此声称更快或通用于其他 backend。

### [FlashInfer #4952：量化合同拆成 weight/activation/output axes](https://github.com/flashinfer-ai/flashinfer/pull/4952)

精确采用 merged PR #4952。单一 `QuantVariant` 会混淆 weight encoding、activation operand 与 layer output。新的 `QuantConfig` 将三者分开，runner 分别声明支持的 weight/activation pair 和 output format；结构配置不能代替 backend capability，legacy preset 仅作为迁移入口。

Ch49 已把 weight-only 与 activation quantization、accumulator/output dtype、runner/kernel capability 和 artifact identity 分开，并要求先做 feasibility 再选择 plan，现有覆盖充分。本次证据是 API/实现合同，不是质量或性能 benchmark；当前 runner output 仍只支持 BF16，其他 output enum 不能被当作已实现能力。

### 技术演进一：从“可加载组件”到可证明的 Runtime Artifact

旧方案把 model class、checkpoint 和一个 backend 名称视为足够的部署描述；当架构、MTP、paged KV、CUDA Graph、量化格式和动态 request metadata 同时进入 runtime 后，这种描述不再能决定实际执行路径。vLLM 的 capability fallback、Transformers 对 MTP weights 的忽略、FlashInfer 的 plan/run 分责与量化 axes 共同表明：

```text
loadable checkpoint
→ capability-resolved runtime
→ static execution profile
→ live request state
→ measured evidence + fallback
```

更细的 contract 换来缓存复用、显存控制与可解释 fallback，也增加 artifact matrix、兼容迁移与验证成本。稳定简单 workload 仍可用单一静态 backend；只有状态与能力分叉时才需要完整 plan identity。

### 技术演进二：从文件恢复到 Canonical State 与 Completion Ownership

Sharded checkpoint 先把单 writer 扩展为 global layout 下的局部 ownership；#6214 进一步利用已有 layout 消除重复 metadata negotiation。低精度训练又引入 canonical FP32 update state 与派生 quantized replica；#6666 表明数值等价和编码等价是两种 restore contract。在线 weight transfer 则把持久文件换成可复用 buffer，#7764 说明其 commit 证据必须来自远端消费完成。

收益是减少冗余 collective、缩短同步路径并支持更高频状态迁移；代价是 layout、generation、optimizer/model identity 和 completion marker 必须共享版本。缺 main params、缺 scale metadata 或消费者未完成时，旧的持久 checkpoint / 不复用 buffer 仍是更安全的分支。

### 技术演进三：从 Deployment Object 到 Readiness-gated Traffic State

传统部署对象只描述 desired replicas；canary、DRA 与 scale-to-zero 把资源可得性、revision readiness、路由比例和容量变化耦合起来。KServe 的本周 pre-release 提供一个受限实现案例，vLLM 的 queue admission/runtime fallback 则提醒 data plane 也可能拒绝或降级执行。

因此 release owner 不能在 Pod 创建或配置接受时提交成功，而要等待资源、模型、runtime 与路由共同形成可服务证据；代价是状态机更长、收敛与回滚更复杂。单 revision、固定容量的内部服务仍可使用更简单的滚动发布，不能把复杂控制面当作默认收益。

## 5. 缺口与下一步

普通来源、候选、证据、Books 与复核待办均为零。

本窗终态保留项：以下限制均不支持正面证据、Books 或无遗漏断言，并分别给出定点重开条件。

- SRC-AI2 的官方目录缺稳定日级时间，SRC-REFLECTION-AI 与 SRC-EVERMIND 的页面提取也未给出足以唯一归属本周的日期；这些入口不用于“本周绝无遗漏”的断言，也没有候选或 Books 结论依赖它们。若得到带时间的官方条目或唯一材料身份，只定点重开对应来源。
- SRC-META-AI 在 09-08～09-13 的公开目录无法稳定枚举，SRC-XIAOMI-MIMO 同期的 Blog 卡片缺日级时间；SRC-MOONSHOT 在 09-12～09-13 的仓库补充入口受公共访问限额影响。它们是从 Daily 继承的终态限制，不支持零事件、候选或 Books 断言；官方目录恢复可枚举时间，或出现可唯一定位到本窗的 release/RFC 时，只定点重开相应来源和日期。
- GitHub REST API 在完成 Megatron-LM、verl、FlashInfer 本窗查询后达到匿名额度上限；已保存的查询结果和直接 PR/release 页面足以审阅本周 8 项，额度恢复时只需复核查询边界，不重跑 Daily 或其他周级来源。
- 未取得作者之外的生产复现；所有 release/PR 结论均限制在公开代码、测试与披露配置内，不形成跨硬件性能保证。

没有需要用户补交的材料。

## 6. 复核

复核者：`semantic_review_sep_w37`（非作者 fresh-context reviewer）  
结论：通过

独立复核了 2026-09-06 09:00～09-13 09:00 周窗与七份 Daily 的无缝覆盖，确认 111 个日级候选逐行与原 Daily 一致、首个 primary URL 唯一，并与 8 个周级新增家族去重后形成 119 项。对 vLLM、Transformers、KServe、Megatron-LM、verl 与 FlashInfer 的 primary release/PR 逐项核对了日期、准入、评分、采用命题与证据边界，未发现把版本功能或局部测试外推为生产保证。Ch35 的低精度恢复增量真实位于正文，形成“数值等价/编码等价/update continuity → canonical FP32 main state → 重建派生量化副本 → weights-only 降级边界”的完整论证。AI2、Reflection AI、EverMind 以及从 Daily 继承的 Meta、Moonshot、MiMo 限制均已按 `受阻` 隔离，未用于零事件或 Books 正面结论，并保留定点重开条件。技术演进、Books owner、Markdown、本地链接、评分与机器检查无剩余阻断；机器校验仅作辅助。Cross-model skipped：本次为非交互独立复核，未获单独授权。
