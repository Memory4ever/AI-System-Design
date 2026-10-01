# Daily Research — 2026-04-13

**规范：** V3
**窗口：** 2026-04-12T09:00:00+08:00 ～ 2026-04-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T22:28:28+08:00

## 1. 结论

按当前V3完成来源/贡献/证据、Books与非作者日级验收：504条宽库存只用于标题查漏和定点题摘，不是504篇当窗新论文或全文队列。有限30项重判为11项具体前分母关闭、19项准入；正式清单67个唯一家族，37深入完成、28标准完成、1原版材料受阻、1中心安全争议。33项已实际整合并通过root或apr03必要原文/真实正文/相邻链路独立复核，19已有覆盖、13仅报告、SEA原版受阻及CORA争议各1项暂缓。普通可执行工作为0；版本、日期与来源保留项按§5隔离，不支持正面采用或零遗漏断言。旧稿无损保留于[过程档案](../_sources/daily-20260413/v2.1-report-before-v3.md)，不继承旧DOI-created owner或Complete。

## 2. 来源覆盖

14个每日来源按本窗核对。未变化机构目录复用[Apr11真实读取记录](../_sources/daily-20260411/v3-reopen-notes.md)实际跨过本窗的停点；本次新增读取Google Vantage、Seed目录/精确外链版本及KimiCLI相邻正式release，不把复用写成全部二次抓取。arXiv正常公告槽为本日08:00北京时间，逐family归属仍需批次、精确版本与例外结合，不能将DOI创建或Updated字段单独当首发。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml)1230项，04-10T00Z→04-13T06Z，后者晚于本窗；Research Index现行9项/Load more、Research52和Publication200项sitemap已作身份查漏 | 受阻 | News无本窗条目，历史Research分页未恢复；lastmod不作公开日期 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)170个publishedOn，04-09T16:34Z→04-14T13:01Z | 已检查 | 该官方目录无本窗条目，不含未列作者稿 |
| SRC-GOOGLE-AI | [April Blog](https://research.google/blog/2026/04/)9条，Apr13 Vantage核心原文已读；DeepMind selected264项首屏跨04-22→03-22 | 受阻 | Vantage按人类教育技能任务具体关闭；Google Publications日级历史停点未恢复 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)返回0可读行 | 受阻 | 缺历史Research/Publications日期目录；不是零命中 |
| SRC-QWEN | [动态40项](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)+[静态60项](https://qwen.ai/api/page_config?code=research.research-list)，04-02T04+08→04-15T10+08，静态早于2026 | 已检查 | 官网合并列表无本窗条目，不等于所有作者稿无更新 |
| SRC-DEEPSEEK | [可见研究/动态](https://www.deepseek.com/news/)，研究06-24→02-25、动态04-24→2025-12-01 | 已检查 | 结论限可见目录，不扩张到未列作者稿 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)最晚2025-11-07；[KimiCLI1.31.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.31.0)04-10T14:45:26Z、[1.32.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.32.0)04-13T11:39:51Z，均窗外；K2.5 release空 | 受阻 | 两相邻已知release不在窗；完整April Blog/CLI分页仍未恢复，不查普通commit |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)publicList page1/size100/renderType0，total9/list9，04-30/23→02-13 | 已检查 | “全部”可见目录无本窗条目，不保证未列作者稿 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)04-29→04-07→04-01 | 已检查 | 已跨本窗；不用CMS createdAt作首发 |
| SRC-BYTEDANCE-SEED | [Papers](https://seed.bytedance.com/en/public_papers)API type1/US，242项，页0/20/40停到窗下；Blog type2/95项页0实际15、页20实际18，04-22T16Z→04-08T16Z→03-31T16Z | 已检查 | Continuous Adversarial Flow Models目录Apr12T16Z与外链v1版本时点未协调，精确隔离；不是0命中或全242全文 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)04-15→02-06→2025；ERNIE release仅2025-06-30 | 已检查 | 已查Blog/release无本窗条目，不代替全部百度作者稿 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper06-29→03-13→02-03，三个模型release空 | 受阻 | Paper/release无本窗；Blog缺历史日期 |
| SRC-MINIMAX | [EN Blog](https://www.minimax.io/blog)05-26→03-18、CN04-27→03-18；CLI26release，04-10v1.0.7→04-16v1.0.8；M2/M2.5 release空 | 受阻 | 已查列表无本窗；Agent TechBlog无历史日戳，单独隔离 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)Sun04-12 20:00EDT→04-13 08:00北京；504宽库存08549～09547/OAI/精确v1/邻界联合查漏，题摘语义及受影响有限30项已处理为11关闭/19保留 | 已检查 | 67贡献候选已整理；49个晚Updated身份与2Seed版本日期缺口精确隔离，不以字段单独定首发或机械迁日，整日仍待独立Gate |

## 3. 候选与判断

本窗67个唯一贡献家族，33整合/19已有覆盖/13仅报告/1SEA受阻暂缓/1CORA争议暂缓；37深入完成、28标准完成、1受阻、1争议安全终态。每项按必要机制/关键反证审阅，不以已有owner或局部负结果自动拒绝；有限30队列另11个具体关闭保留在过程档案。下表时段是官方公告槽、连续ID/OAI批次及早v1元数据联合支持的有界推断，不是逐篇成功日志或Updated等于首发；晚字段和机构目录版本冲突在§5隔离。来源、清单整理与单篇审阅不等整日报已过独立Gate。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Dynamic sparsity in tree-structured feed-forward layers at scale — 2604.08565v1](https://arxiv.org/html/2604.08565v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | hard routing/梯度与prune改变条件容量实现选择；2+2+2=6，必要机制缺口深入 | 深入完成 | 整合 `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)，root采用通过 |
| [CSAttention — 2604.08584v1](https://arxiv.org/html/2604.08584v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | scan→离线query-centroid短表，摊销/失配改变retrieval选择；2+2+2=6，必要机制缺口深入 | 深入完成 | 整合 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，root采用通过 |
| [QCFuse — 2604.08585v1](https://arxiv.org/html/2604.08585v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | context-aware selector→layerwise recompute/prefetch的近似缓存分支；2+2+2=6，必要机制缺口深入 | 深入完成 | 整合 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，root采用通过 |
| [Uncertainty-Aware Transformers — 2604.08885v1](https://arxiv.org/html/2604.08885v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 少数类undercoverage反证要求marginal/切片分账；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root采用通过 |
| [EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context — 2604.08556v1](https://arxiv.org/html/2604.08556v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 固定递推状态的结构/内容任务压力需区分；1+2+2=5 | 标准完成 | 已有覆盖 `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)，root采用通过 |
| [Re-Mask and Redirect: Exploiting Denoising Irreversibility in Diffusion Language Models — 2604.08557v1](https://arxiv.org/html/2604.08557v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 外部修改accepted-state provenance可重开生成轨迹；2+2+2=6、安全深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root写后独立复核通过 |
| [Efficient RL Training for LLMs with Experience Replay — 2604.08706v1](https://arxiv.org/html/2604.08706v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | buffer horizon、reuse与生成价格分别约束训练选择；2+2+2=6、机制缺口深入 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)，root写后独立复核通过 |
| [Demystifying the Silence of Correctness Bugs in PyTorch Compiler — 2604.08720v1](https://arxiv.org/html/2604.08720v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 单调用oracle遗漏cache/context跨调用错误；2+2+2=6、机制缺口深入 | 深入完成 | 整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root写后独立复核通过 |
| [HiFloat4 Format for Language Model Pre-training on Ascend NPUs — 2604.08826v1](https://arxiv.org/html/2604.08826v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 格式与tensor-role联合决定SR/RHT保护条件；1+2+2=5 | 标准完成 | 已有覆盖 `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，root采用通过 |
| [SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks — 2604.08865v1](https://arxiv.org/html/2604.08865v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | prompt scalar baseline用critic校准交换group rollout；2+1+2=5 | 标准完成 | 已有覆盖 `TRAIN-PPO` [Ch32](../../../../books/part-04-training-system/32-ppo.md)，root采用通过 |
| [Semantic Intent Fragmentation: A Single-Shot Compositional Attack on Multi-Agent AI Pipelines — 2604.08608v1](https://arxiv.org/html/2604.08608v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 局部goal-alignment不替代scope×destination授权；2+2+2=6、安全深入 | 深入完成 | 整合 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，root写后独立复核通过 |
| [TensorHub: Scalable and Elastic Weight Transfer for LLM RL Training — 2604.09107v1](https://arxiv.org/html/2604.09107v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | reference-only数据源用mutability/retention管理副本生命周期；3+3+2=8 | 深入完成 | 整合 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，root写后独立复核通过 |
| [Act or Escalate? Evaluating Escalation Behavior in Automation with Language Models — 2604.08588v1](https://arxiv.org/html/2604.08588v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 外部成功信号与风险成本阈值不等于模型自知正确性；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EXAONE 4.5 Technical Report LG’s First Open-Weight Vision-Language Model for Industrial Intelligence — 2604.08644v1](https://arxiv.org/html/2604.08644v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | vision GQA/no-KV与视觉token预算的公开架构分支；限版本事实，无受控组件归因；2+1+2=5 | 标准完成 | 仅报告 |
| [Decomposing the Delta: What Do Models Actually Learn from Preference Pairs? — 2604.08723v1](https://arxiv.org/html/2604.08723v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | generator gap、sample judge gap与正确性标签需分拆，不以teacher强弱替代pair选择；2+1+2=5，长期机制缺口深入 | 深入完成 | 整合 `TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need — 2604.08749v1](https://arxiv.org/html/2604.08749v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 冻结随机scaffold与预训练LoRA具有不同初始化/质量/显存成本；2+1+2=5，长期机制缺口深入 | 深入完成 | 整合 `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [StaRPO: Stability-Augmented Reinforcement Policy Optimization — 2604.08905v1](https://arxiv.org/html/2604.08905v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | embedding几何加入reward是可检验局部分支，不是推理真值与因果信用；2+1+2=5 | 标准完成 | 仅报告 |
| [Dissecting Bug Triggers and Failure Modes in Modern Agentic Frameworks: An Empirical Study — 2604.08906v1](https://arxiv.org/html/2604.08906v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | backend×model ID、重复执行与序列化暴露interaction failure，历史bug样本不成生产失败率；2+2+2=6 | 标准完成 | 仅报告 |
| [Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning — 2604.08926v1](https://arxiv.org/html/2604.08926v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | Hard/Mid/Easy分支把teacher bias、on-policy pair与group collapse分别处理；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models — 2604.08964v1](https://arxiv.org/html/2604.08964v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 历史KL相对current anchor用于提前解锁未来block，不是单步confidence；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Confident in a Confidence Score: Investigating the Sensitivity of Confidence Scores to Supervised Fine-Tuning — 2604.08974v1](https://arxiv.org/html/2604.08974v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | SFT×metric×task决定confidence排序变化，模型更新需要校准身份刷新；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Quantisation Reshapes the MetacognitiveGeometry of Language Models — 2604.08976v1](https://arxiv.org/html/2604.08976v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | quantization×metric与训练/测试format变化必须分账；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment — 2604.08988v1](https://arxiv.org/pdf/2604.08988v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 顺序episode的跨任务记忆评价是拟核贡献，原版必要证据当前不可复核，不据此采用收益；2+1+2=5 | 受阻 | 暂缓：见§5原版材料缺口 |
| [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory — 2604.08995v1](https://arxiv.org/html/2604.08995v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | memory/history噪声与student-own-rollout训练对齐部署状态分布；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding — 2604.09000v1](https://arxiv.org/html/2604.09000v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | isolated/connected memory node按信息角色压缩，TMR收益须与压缩独立分账；2+1+2=5 | 标准完成 | 仅报告 |
| [Regime-Conditional Retrieval:Theory and a Transferable Router for Two-Hop QA — 2604.09019v1](https://arxiv.org/html/2604.09019v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | Q/Union二元选择后冻结混合权重，连续自适应权重是需独立验收的消融；2+1+2=5，长期机制缺口深入 | 深入完成 | 整合 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Watt Counts: Energy-Aware Benchmark for Sustainable LLM Inference on Heterogeneous GPU Architectures — 2604.09048v1](https://arxiv.org/html/2604.09048v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | finite查询与在线Poisson负载的idle账本改变硬件排序，GPU-only不等全服务能耗；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [DRIFT: Harnessing Inherent Fault Tolerance for Efficient and Reliable Diffusion Model Inference — 2604.09073v1](https://arxiv.org/html/2604.09073v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | checksum定位后用旧activation近似恢复是质量/故障预算分支，不是exact rollback；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [EdgeFlow: Fast Cold Starts for LLMs on Mobile Devices — 2604.09083v1](https://arxiv.org/html/2604.09083v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | weightlet解包与CPU/NPU拓扑调度改变coldstart critical path，而非resident decode普遍更快；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation — 2604.09155v1](https://arxiv.org/html/2604.09155v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | joint harmful-execution risk不能直接转成执行条件harm rate；精确争议见§5；2+2+2=6，安全深入 | 争议 | 暂缓 |
| [Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG — 2604.09174v1](https://arxiv.org/html/2604.09174v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | facet级证据缺失/冲突/读者忽略应分账，NLI分数不自动是真值概率；1+2+2=5 | 标准完成 | 已有覆盖 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Generalization and Scaling Laws for Mixture-of-Experts Transformers — 2604.09175v1](https://arxiv.org/html/2604.09175v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | hard Top-K统计容量的条件理论参考，不直接给开放LM路由规模recipe；2+1+2=5 | 标准完成 | 仅报告 |
| [SAGE: A Service Agent Graph-guided Evaluation Benchmark — 2604.09285v1](https://arxiv.org/html/2604.09285v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | SOP规则链与chat judge区分过程/结果，set-overlap不等有序合法轨迹；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [OASIS: Online Activation Subspace Learning for Memory-Efficient Training — 2604.09406v1](https://arxiv.org/html/2604.09406v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | online activation basis更新需运输optimizer moments，二阶近似不保full covariance；2+2+2=6，长期机制缺口深入 | 深入完成 | 整合 `TRAIN-ZERO` [Ch39](../../../../books/part-04-training-system/39-zero.md) |
| [Many-Tier Instruction Hierarchy in LLM Agents — 2604.09443v1](https://arxiv.org/html/2604.09443v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | instruction标签与保序数值扰动反证prompt hierarchy不等执行授权；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Attention-Based Sampler for Diffusion Language Models — 2604.08564v1](https://arxiv.org/html/2604.08564v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | confidence与影响列和分离，近似排序和动态阈值改变unmask选择；2+2+2=6，真实gap深入 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)已实际落笔且root写后独立复核通过 |
| [Skip-Connected Policy Optimization for Implicit Advantage — 2604.08690v1](https://arxiv.org/html/2604.08690v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 单prefix条件MC与双信用坐标不同于每token结果广播；2+2+2=6，真实gap深入 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)已实际落笔且root写后独立复核通过 |
| [p1: Better Prompt Optimization with Fewer Prompts — 2604.08801v1](https://arxiv.org/html/2604.08801v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 候选system-prompt真signal与response noise分解改变优化预算；2+1+2=5，真实gap深入 | 深入完成 | 整合：`AGENT-PROMPT` [Ch74](../../../../books/part-07-agent/74-prompt.md)已实际落笔且root写后独立复核通过 |
| [Spectral Geometry of LoRA Adapters Encodes Training Objective and Predicts Harmful Compliance — 2604.08844v1](https://arxiv.org/html/2604.08844v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 跨制造方法monitor反转与退化生成judge假阳性改变adapter验收；2+1+2=5，真实gap深入与安全反证 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已实际落笔且root写后独立复核通过 |
| [Revisiting the Capacity Gap in Chain-of-Thought Distillation from a Practical Perspective — 2604.08880v1](https://arxiv.org/html/2604.08880v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | prestudent baseline与数据选择estimand改变teacher比较有效性；2+1+2=5，真实gap深入 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)已实际落笔且root写后独立复核通过 |
| [Drift and selection in LLM text ecosystems — 2604.08554v1](https://arxiv.org/html/2604.08554v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 受限递归n-gram的稳定固定点仍可能丢失长程结构；2+1+2=5 | 标准完成 | 仅报告：受限recursive n-gram理论不据此采用真实LLM语料稳定过滤规则 |
| [Multi-User Large Language Model Agents — 2604.08567v1](https://arxiv.org/html/2604.08567v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 多用户selection/execution与privacy/utility需分开验收；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Distributionally Robust Token Optimization in RLHF — 2604.08577v1](https://arxiv.org/html/2604.08577v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 完整trajectory minibatch-DRO边界而非任意OOD；2+1+2=5 | 标准完成 | 仅报告：有限minibatch trajectory-DRO；原公式误读已撤销 |
| [On the Spectral Geometry of Cross-Modal Representations: A Functional Map Diagnostic for Multimodal Alignment — 2604.08579v1](https://arxiv.org/html/2604.08579v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 谱复杂度相似≠basis可用的受控反证；1+2+2=5 | 标准完成 | 已有覆盖 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Adjoint Matching through the Lens of the Stochastic Maximum Principle in Optimal Control — 2604.08580v1](https://arxiv.org/html/2604.08580v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 控制依赖噪声决定一阶/二阶adjoint与lean-AM的条件边界；2+1+2=5 | 标准完成 | 仅报告：σ条件下理论未验证训练生成器迁移或部署收益；root必要原文独立核通过 |
| [Unified Multimodal Uncertain Inference — 2604.08701v1](https://arxiv.org/html/2604.08701v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 人类scalar target可用离散分布拟合，但MSE不等事实概率；2+1+2=5 | 标准完成 | 仅报告：人类scalar target拟合不形成事实正确性或risk calibration保证；root必要原文独立核通过 |
| [Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition — 2604.08708v1](https://arxiv.org/html/2604.08708v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | ragged多run轨迹重构残差提供排序proxy，非风险校准；2+1+2=5 | 标准完成 | 仅报告：ragged重构代理尚不作为校准risk或通信因果归因 |
| [Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics — 2604.08764v1](https://arxiv.org/html/2604.08764v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | activation-PCA方向与gradient能量的局部关联不证明语义或训练因果；2+1+2=5 | 标准完成 | 仅报告：局部proxy机制观察不直接采用优化或普遍泛化结论 |
| [ELT: Elastic Looped Transformers for Visual Generation — 2604.09168v1](https://arxiv.org/html/2604.09168v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 同图prefix监督使有限loop深度成为训练过的输出配置，不保证无限容量；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root写后独立复核通过 |
| [Decoupling Vector Data and Index Storage for Space Efficiency — 2604.09173v1](https://arxiv.org/html/2604.09173v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 图邻接与完整向量分离改变压缩、导航I/O、重排及GC映射合同；2+2+2=6，真实gap深入 | 深入完成 | 整合 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)，root写后独立复核通过 |
| [MixFlow: Mixed Source Distributions Improve Rectified Flows — 2604.09181v1](https://arxiv.org/html/2604.09181v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 条件Gaussian参数插值共同训练，使缺κ部署具有已训练的标准Gaussian回退；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root写后独立复核通过 |

| [Advantage-Guided Diffusion for Model-Based Reinforcement Learning — 2604.09035v1](https://arxiv.org/html/2604.09035v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 短horizon的sigmoid/指数advantage倾斜补value窗口；理想true advantage与learned value须分开；2+1+2=5 | 标准完成 | 仅报告 |
| [Tora3: Trajectory-Guided Audio-Video Generation with Physical Coherence — 2604.09057v1](https://arxiv.org/html/2604.09057v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 共享2D运动状态经video endpoint与audio conditioning两个接口，不由同步性推出物理真值；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md), apr03实际写后独立通过 |
| [Hierarchical Alignment: Enforcing Hierarchical Instruction-Following in LLMs through Logical Consistency — 2604.09075v1](https://arxiv.org/html/2604.09075v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | MaxSMT一致子集与parser/NLI信号不等认证权限，需分开policy sensor与enforcement；1+2+2=5 | 标准完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过 |
| [DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation — 2604.09089v1](https://arxiv.org/html/2604.09089v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 多层安全signal/一次prompt bias不同于生成中守卫，cadence与功能安全代价需独立验收；2+2+2=6，必要安全/边界深入 | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过 |
| [CLIP-Inspector: Model-Level Backdoor Detection for Prompt-Tuned CLIP via OOD Trigger Inversion — 2604.09101v1](https://arxiv.org/html/2604.09101v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 冻结backbone仍可由prompt/meta-network带后门，候选类覆盖与repair标签是检测边界；2+1+2=5，必要安全/边界深入 | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过 |
| [Truncated Rectified Flow Policy for Reinforcement Learning with One-Step Sampling — 2604.09159v1](https://arxiv.org/pdf/2604.09159v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | deterministic prefix/stochastic tail分开RL与蒸馏；joint surrogate与真实terminal entropy不同；2+1+2=5 | 标准完成 | 仅报告 |
| [GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking — 2604.09222v1](https://arxiv.org/html/2604.09222v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | audio band威胁预算与task utility非单调，matched benign/attack需两条账；2+1+2=5，必要安全/边界深入 | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过 |
| [Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models — 2604.09227v1](https://arxiv.org/html/2604.09227v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | LR preview筛seed/prompt后HR重跑；D–velocity commutator和局部修正不是HR等价续算；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md), apr03实际写后独立通过 |
| [2D or 3D: Who Governs Salience in VLA Models? -- Tri-Stage Token Pruning Framework with Modality Salience Awareness — 2604.09244v1](https://arxiv.org/html/2604.09244v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 时间salience平滑不能替代语义保护，组合消融暴露误剪跨步延续边界；2+1+2=5，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过 |
| [VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis — 2604.09330v1](https://arxiv.org/html/2604.09330v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 同步video/action flow仍是clean-video→action单向条件，不证明action-conditioned环境因果；2+2+2=6，必要安全/边界深入 | 深入完成 | 已有覆盖 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md), apr03具体owner独立通过 |
| [Phonemes vs. Projectors: An Investigation of Speech-Language Interfaces for LLM-based ASR — 2604.09332v1](https://arxiv.org/html/2604.09332v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | 有限配对监督下explicit phone/wordboundary与continuous projector不同；encoder已见语言和token成本需分账；2+1+2=5，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过 |
| [Mind the Gap Between Spatial Reasoning and Acting! Step-by-Step Evaluation of Agents With Spatial-Gym — 2604.09338v1](https://arxiv.org/pdf/2604.09338v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | step/backtrack增加completion不等success，强模型反收益要求planning协议分账；2+1+2=5 | 标准完成 | 已有覆盖 `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md), apr03具体owner独立通过 |
| [Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts — 2604.09364v1](https://arxiv.org/html/2604.09364v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | last-position patch阴性不排除full-sequence分布式视觉仲裁，干预单位影响因果范围；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过 |
| [Do Vision Language Models Need to Process Image Tokens? — 2604.09425v1](https://arxiv.org/html/2604.09425v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | representation/substitution稳定不等删除安全，single-token答案/multi-token VQA/caption协议须分开；2+1+2=5，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过 |
| [Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories — 2604.09429v1](https://arxiv.org/html/2604.09429v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | canonical raxel接口使camera由sidecar变可生成状态，shared codec与joint真实学习不能等同；2+2+2=6，真实gap深入 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过 |
| [E3-TIR: Enhanced Experience Exploitation for Tool-Integrated Reasoning — 2604.09455v1](https://arxiv.org/html/2604.09455v1) | 2026-04-13T08:00:00+08:00 ～ 2026-04-13T09:00:00+08:00 | expert分叉负adv停shared-prefix梯度但保留suffix/self池，mixed ratio不证明真实知识边界；2+2+2=6，真实gap深入 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md), apr03实际写后独立通过 |

## 4. 证据与知识整合

以上为可验收工作小批次，不代表分母冻结。真实实验均未在本地复现。

### [Dynamic sparsity in tree-structured feed-forward layers at scale — 2604.08565v1](https://arxiv.org/html/2604.08565v1)

[exact-v1](https://arxiv.org/html/2604.08565v1) §3、§5–8：节点线性响应同时负责hard binary routing与输出，路径stop-gradient；GELU放置影响梯度偏斜，平衡利用率不保证质量提升，统计prune将动态树转为静态路径。125M三seed与OPT1.3B/26B scratch对照支持条件分支但不全面优于Dense；FT复用已有Attention不是同预算从零训练。§7表格称单A100 layer runtime而§8限定理论/模拟潜力，故不采用加速数。实际[Ch21](../../../../books/part-02-model/21-moe.md)已将此机制嵌入granularity→loadbalance之间，root非作者原文/正文复核通过，不改“条件计算必须核执行收益”的既有结论。

### [CSAttention — 2604.08584v1](https://arxiv.org/html/2604.08584v1)

[exact-v1](https://arxiv.org/html/2604.08584v1) §3–4：Prefill按Query子空间构造centroid→Key Top-L表，Decode近邻centroid短表合并+recent window，新Key更新表；完整KV仍线性增长。受测三7B/8B模型、dualEPYC7513/1TiB/1或4A100，Table3 step2 score50.81 vs Full52.41反驳所有差距≤0.6表述；CPU–GPU预建索引8K/16K相对H2O0.88×/0.97×，不能省略反收益。Ch45原binary-key estimator与通用recall未承载Query-side离线摊销；实际机制正文已写，root非作者原文/正文采用通过，不以机器校验代替判断。线上并发/SLO等未披露，不使用通用吞吐数字。

### [QCFuse — 2604.08585v1](https://arxiv.org/html/2604.08585v1)

[exact-v1](https://arxiv.org/html/2604.08585v1) §3–5：CPU anchors先为Query提供文档上下文，critical-layer K选择重算token，第i层recompute与i+1层prefetch重叠；radix chunk identity和causal mask不保证未重算KV语义exact。单A10080GB、Llama3.1-8B/Qwen3-8B/Mistral7B、多跳QA、平均ROUGE/TTFT及0.1～0.5比例是作者contract，40%质量结论不普遍；QCAll/QCLast为emulated variants。Ch45现chunk position/seam论证无此selector→recompute分支，实际机制正文已写并通过root非作者原文/正文采用；线上长度/并发/精度/SLO未建立，保留Full Prefill回退。

### [Uncertainty-Aware Transformers — 2604.08885v1](https://arxiv.org/html/2604.08885v1)

[exact-v1](https://arxiv.org/html/2604.08885v1) §4、§5.4–5.7/§6：中间层正负kNN距离比产生nonconformity；reference可只保留正确训练点，calibration不能按正确性过滤。CLS/flattened与PCA是表示/成本分支，BERT/RoBERTa GLUE/SuperGLUE的少数类undercoverage与aggregate coverage应分账；类别不平衡本身不自动证明exchangeability失败。Ch66现“同步Calibration State”、marginal/切片限制与shortlist coverage已承载主要长期边界，故当前No Change而非因encoder标签拒绝。没有把分类结果外推开放generation，root已独立单篇核对通过。

### [EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context — 2604.08556v1](https://arxiv.org/html/2604.08556v1)

[exact-v1](https://arxiv.org/html/2604.08556v1) §5–9区分结构可行与内容记忆；130M/FineWeb8B/bf16/H200及短结构任务不证明通用语言质量，小模型attention消融不可直接归因130M主模型。DPI需要实际信息丢失，不是任意固定递推都不可能记忆的证明。[Ch22](../../../../books/part-02-model/22-long-context.md)固定容量/recall与GDN输入依赖更新、hybrid边界已承载本命题，保持已有覆盖而非照搬标题否定EMA。

### [Re-Mask and Redirect: Exploiting Denoising Irreversibility in Diffusion Language Models — 2604.08557v1](https://arxiv.org/html/2604.08557v1)

[exact-v1](https://arxiv.org/html/2604.08557v1) §3、§4.1–4.3、§6/Limitations：攻击者可直接修改denoising state，remask或prefix各自单独无效，组合才使轨迹重开。它不只是普通用户prompt攻击；两7B/8B模型、greedy线性schedule、单judge不能外推整个范式不安全。实际Ch24 Editable tokens与commit boundary增加accepted-state外部改写provenance与isolated audit分支，root已独立核来源/正文；未验证防线与本地实验未复现保持不变。

### [Efficient RL Training for LLMs with Experience Replay — 2604.08706v1](https://arxiv.org/html/2604.08706v1)

[exact-v1](https://arxiv.org/html/2604.08706v1) §3–5.5、假设4.1–4.3：N/R horizon、B/R reuse、W/T生成成本分别改变选择，importance correction不能消除样本与历史iterate的所有条件依赖。受测Qwen0.6B/7B、OpenR1/MATH、至少4seeds和LR匹配支持有条件replay，active GPU compute不等wall-clock；高reuse、冷暖buffer、late崩溃保留为边界。实际Ch33 Replay小节把成本与分布代价纳入原训练主干，root写后独立复核通过，不把降低采样成本当收敛保证。

### [Demystifying the Silence of Correctness Bugs in PyTorch Compiler — 2604.08720v1](https://arxiv.org/html/2604.08720v1)

[exact-v1](https://arxiv.org/html/2604.08720v1) §4.2–4.5/§5：77是公开release可复现patch的限定集合，26被5个fuzzer找到、15graph问题都漏检，不能外推部署错误率。跨调用状态/cache/context、alias/view/in-place等需要比单算子更多的oracle。实际Ch49 staged differential之后补相同artifact跨输入/context执行；LLM仅生成mutation，assertion与triage拥有correctness判定。root必要来源和实际正文独立复核通过，没有宣称本地复現或所有编译错误已覆盖。

### [HiFloat4 Format for Language Model Pre-training on Ascend NPUs — 2604.08826v1](https://arxiv.org/html/2604.08826v1)

[exact-v1](https://arxiv.org/html/2604.08826v1) §3–6：HiFloat4格式、tensor-role分工及dW SR/RHT保护应联合比较，forward NR并不随SR普遍获益；相同正交旋转只在full precision乘积上等价，量化后不保证。三架构50B-token训练/25B ablation支持受限loss认识，不建立下游质量、真实能耗或任意模型等价。all-linear FP4与§5.1高精度保护、8/120与6.25%的内部口径不照录为事实。Ch28 mixed precision已明确格式×角色、SR不通用、RHT成本与高精度回退；无需新增产品格式摘要，root已独立核已有覆盖通过。

### [SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks — 2604.08865v1](https://arxiv.org/html/2604.08865v1)

[exact-v1](https://arxiv.org/html/2604.08865v1) §3–5：prompt-only BCE critic估计当前policy solvability，A=R−V广播给整条response，仍用token ratio/clipping；不是识别哪个token造成正确。DeepSeek-R1-Distill-Qwen1.5B/7B、4A100/4H100、DeepScaleR/DAPO17K、batch256/512、KL0、GRPO组8与Avg@16为主比较条件；token+BCE消融在500steps崩溃后停止，相关0.642不证明calibration，控制环境也不等同LLM。Ch32 Baseline Granularity正文实际解释该机制及critic刷新/过期、GRPO与token-critic共存，判已有覆盖，root已独立核对通过。

### [Semantic Intent Fragmentation: A Single-Shot Compositional Attack on Multi-Agent AI Pipelines — 2604.08608v1](https://arxiv.org/html/2604.08608v1)

[exact-v1](https://arxiv.org/html/2604.08608v1) Threat Model、Formal Model、Measurement Pipeline、Table5–7、Limitations提供单次请求自动组合越权plan的窄反证；旧LG7b/Koala逐步过滤漏检，但新LG3可标出8/87，pure-SIF为0/14，故不能采用“任何单步语义防线必然失效”。CIV参与成功定义与防线评价，10/10不是独立检测率；8个benign还排除2个plan失败，0/8不证明生产0FPR。Ch72原跨会话风险没有完整承载scope×destination的单请求组合，实际已将此判断整合进authority→stepguard主干；root已独立核exact-v1 Table5–7、Mechanistic/Limitations及实际正文，通过写后采用，本地实验仍未复现。

### [TensorHub: Scalable and Elastic Weight Transfer for LLM RL Training — 2604.09107v1](https://arxiv.org/html/2604.09107v1)

[exact-v1](https://arxiv.org/html/2604.09107v1) §3、§4.3–4.6、§5.1–5.4：ROS只持GPU副本reference；unpublish使新读不可见并等待在途传输drain，retain最后copy用CPU offload保底；group事务固定shard view、prefix复制与crossDC seed各有独立语义。最后non-spot副本丢失可unavailable，server重建softrefs不是持久Checkpoint。作者Hopper/RDMA/200Gbps跨站、veRL的NCCL/UCX全局阶段baseline、1T重复权重压力模型与省略loss细节限制外推；不将总GPU stall减少直接当训练质量/普遍生产保证。Ch36原versioned tensor/UniRL与delta/lease无此reference-only生命周期分支，实际已嵌入同主干；root已独立核exact-v1 §3.1–3.3/§4.3.3–4.5/§5.2及实际正文，写后采用通过。

### [Act or Escalate? Evaluating Escalation Behavior in Automation with Language Models — 2604.08588v1](https://arxiv.org/html/2604.08588v1)

1+2+2=5标准完成：§2–6成本阈值基于外部tree的条件成功信号，8models/250samples（thinking50）及人类记录决定任务；不是让模型获得真值自知。Table1Qwen成本措辞增益小而GPT5mini有增益，不能照录cost无效；Qwen9B SFT模板外部p，heldoutMovieLens特定boundary全对，NoSignal幻造p不能作开放能力保证。Ch66外部校准与Ch56风险×成本policy已有具体正文，canonical Ch66已有覆盖。

### [EXAONE 4.5 Technical Report LG’s First Open-Weight Vision-Language Model for Industrial Intelligence — 2604.08644v1](https://arxiv.org/html/2604.08644v1)

2+1+2=5标准完成/仅报告：§2–5公开1.2Bvisionencoder+32BLLM，visionGQA即无KV也选择减attention复杂度，resolution/tokenbudget、2D/1DRoPE、MTP与contextparallel构成明确受限架构分支，不因缺消融直接拒绝。§3vision温度1.0/文档.6、top-p.95/presence1.5、32k/128k输出且MTP关闭；对照混合官方报告与内测，不能将排行榜归因visionGQA/MTP或称生产吞吐。只记录版本/作者配置事实，Ch23/49稳定机制不因此改变，hardware/precision/batch/concurrency/SLO未在此采用证据披露。

### [Decomposing the Delta: What Do Models Actually Learn from Preference Pairs? — 2604.08723v1](https://arxiv.org/html/2604.08723v1)

§2–5/AppendixD分开generator能力差、sample judge差与正确性pair；同3500prompts四种正确/错误方向都有小幅收益，但正确→错误最好，不能取消正确性。Nemotron-8B/OpenR1、固定s1-3B rejected，GPT-OSS120B medium/temperature.6/五评分，DPO LR5e-8/beta.2；AMC/AIME avg@16与其他pass@1分开，top5k和全集16.5k并非等预算。Ch34 DPO难题中第三‘相对质量’后已实际加入两种delta，root独立核原文/相邻正文通过；未证单维因果或普遍效率，硬件/precision/SLO未披露。

### [A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need — 2604.08749v1](https://arxiv.org/html/2604.08749v1)

§3/5.1–5.3/5.6/6/8：固定随机scaffold只训练低秩adapter、尺度β及embedding/head，需要PRNG/architecture/init身份；不是预训练LoRA等价替代。WikiText103同架构预算所有scale较full训练差，900Mloss3.95>3.156；H200/bf16/batch32/128tokens Table9大模型吞吐不更快。Ch30初始化→显存之间实际写入随机scaffold条件分支，root必要原文/正文通过；低trainablestate仍有forward/input-gradient成本，ASIC猜测不采用。

### [StaRPO: Stability-Augmented Reinforcement Policy Optimization — 2604.08905v1](https://arxiv.org/html/2604.08905v1)

2+1+2=5标准完成/仅报告：§4.1–4.3、§5setup/相关/组件消融，adjacentembedding方向ACF与netdisplacement/pathlength PE加入outcome reward；两代理不是token真值因果信用，若干MW p=.1363/.2158不显著。正文3σ与15.87%尾概率口径矛盾不采用；受测Qwen/Math/Game24与GPT4omini标签的几何operating point不能成通用faithfulness选择。

### [Dissecting Bug Triggers and Failure Modes in Modern Agentic Frameworks: An Empirical Study — 2604.08906v1](https://arxiv.org/html/2604.08906v1)

2+2+2=6标准完成/仅报告：exact-v1题名Dissecting Bug Triggers and Failure Modes，§3/8/9/11：截至2025-08-11取820→501→409fixedbugs；只有273有repro/config可分析，modelBackend×ID、ConsecutiveExec和ExportComponent提供具体interaction failure。35选择sourcebugs中16transfer，11reports仅1fixed/6communityack/4designboundary；47%是bugfix附test inclusion非测试覆盖率/生产失败率。Ch81 847–859确定性transition与agent scenario分测及verifiedstate版本绑定已承载大方向；不把historical样本当全框架通用oracle，保留受限触发模板证据。

### [Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning — 2604.08926v1](https://arxiv.org/html/2604.08926v1)

§3 Eq4/14–16、§4.1–4.5/Table3/7：Hard走multi-teacher SFT，Mid走GRPO+on-policy pair GAL，Easy跳过；两个梯度估计独立的理论不能推共享rollout的variance必降。Qwen7B/4B、16A80080GB/bf16/G8/max8192，AMC动态grading退步，teachercost须计入。Ch33 collapsed group后的条件分流已实际整合并通过root复核，不把DPO/PPO/GRPO写作线性淘汰；线上并发/SLO不适用，未复现实验。

### [Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models — 2604.08964v1](https://arxiv.org/html/2604.08964v1)

§3.3 Eq4–7/§4/AppD/E：current distribution作anchor、历史加权KL衰减，解锁futureblock；不是单步confidence或每个block历史相等。LLaDA8B/1.5 gen256/block32/H6/default.01，最佳阈值与history非普遍；Wildvoice有退步。Ch24 commit/history→parallelstate的现有主干已补此分支并通过root核验；理论过去均值不证明未来真值，hardware/precision/concurrency/SLO未披露。

### [Confident in a Confidence Score: Investigating the Sensitivity of Confidence Scores to Supervised Fine-Tuning — 2604.08974v1](https://arxiv.org/html/2604.08974v1)

1+2+2=5标准完成：§3–6，BART/FlanT5/Llama3.1-8B/Gemma2-2B×translation/SQuAD/GSM8K×12metrics，144config/3seeds。SFT后48/144下降中仅2项显著、96/144上升中8项显著（Holm/ANOVA），不是普遍恶化；817TruthfulQA/Claude3.5Sonnet judge、23/48AUROC下降另列。作者testset minmax缩放不等概率校准，采用验证集属于平台规则。Ch66 calibration跟随model/task/metric version与独立quality sensor的真实正文承载，已有覆盖，未复现实验。

### [Quantisation Reshapes the MetacognitiveGeometry of Language Models — 2604.08976v1](https://arxiv.org/html/2604.08976v1)

1+2+2=5标准完成：§3–6 Tables3–7，Llama3-8B-Instruct、3000TriviaQA/4domains，Q5_K_M vsf16、7900GRE/Vulkan/llama.cpp。AUROC2与meta-d′/d′排序不同只在四域；LoRA因Q5merge不可用使用f16训练/评价，不当量化后直接恢复。seed42、10kbootstrap与宽CI不证明等价，低d′使M-ratio不稳定。Ch66 artifact/metric identity和切片校准已承载此受限边界，已有覆盖；不宣布某指标对量化普遍不变。

### [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment — 2604.08988v1](https://arxiv.org/pdf/2604.08988v1)

2+1+2=5，受阻/暂缓：官方HTML当前返回后发EvolutionaryFlywheel内容，不能替代SEA-Eval原版。原作者实际§4–5读取笔记保留于过程档案，包括120/90任务口径、两Claude harness及memory/token归因限制，但未保存可供当前独立核对的完整原版。apr03尝试两条官方PDF入口均截断，作者追加有界下载45秒及一次240秒续传仍只得到6,102,037/10,828,779字节、缺EOF且无法解析；停止重复下载，不用笔记充当新独立证据。本次不采用任务数量、收益或memory机制结论，也不以其支持Books已有覆盖；恢复可绑定SEA-Eval v1的必要正文后仅重开本项标准审阅/Books决定。

### [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory — 2604.08995v1](https://arxiv.org/html/2604.08995v1)

§3.1–3.5/5.1–5.2：history/memory/current noisy latent分责；errorbuffer corrupt、600stepclean单段→2400step student-own多段rollout并online更新memory，最后DMD。5B/28B的viewrevisit以定性为主，不证明每component归因、物理可执行transition或通用FPS。Ch25‘取回memory不证明使用’前实际补训练/部署上下文一致性并通过root核；不把generated frames提交成环境真值。

### [StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding — 2604.09000v1](https://arxiv.org/html/2604.09000v1)

2+1+2=5标准完成/仅报告：§4–5，isolatedtext sphericalclustering/diversity与entity-connected degree/redundancy分别压缩，temporalretrieval含recency权重/segment预算；不是同一节点均匀topK。Table2固定M3Agent其余组件、30%压缩robot30.7>30.3/web47.0<47.9，70%+TMR不可归因compression单独。2A10080G/3次均值、GPT4o judge与固定memorygraphs，更多retrievalcalls可抵消压缩收益；仅保留受限压缩/读路径实验，不承诺开放长期memory保持或整体服务SLO。

### [Regime-Conditional Retrieval:Theory and a Transferable Router for Two-Hop QA — 2604.09019v1](https://arxiv.org/html/2604.09019v1)

§5.1–6.6/Alg1主部署先二元Q/Union，再冻结α=.25；881五折/100sentence标注、NVEmbedv2/BGE/e5mistral/fixedpool且仅hop1correct，Table2MuSiQue303 +5.3pp p=.002、Hotpot570 +1.1pp p=.143。§6.5 P-weighted消融+2.6pp(ns)/−.2pp与主配置分开。Ch76 Dense/Hybrid后实际补第二跳关系query owner与保守混合；作者侧初稿连续路由错误已纠正，root修后重新核原文/正文通过。Gaussian假设与这些正均值不成开放no-regret或finalanswer/SLO保证。

### [Watt Counts: Energy-Aware Benchmark for Sustainable LLM Inference on Heterogeneous GPU Architectures — 2604.09048v1](https://arxiv.org/html/2604.09048v1)

root已经独立核§3.2/5.3并对读Ch70 121–145，finite1000query与5minPoissonλ口径、NVMLboard边界与idle改变排序；已有覆盖通过，不采用TDP代实际能耗。

### [DRIFT: Harnessing Inherent Fault Tolerance for Efficient and Reliable Diffusion Model Inference — 2604.09073v1](https://arxiv.org/html/2604.09073v1)

§3–6：memoryread errorfree、random bitflip，INT8/INT32；checksum定位大误差后由较早activation覆盖是近似恢复，paired cancellation可漏检；10step offload/layoutrepack仍需等待。14nm synthesis/HBM2/SCALE-Sim非真实GPU，能耗与加速不同DVFS点。Ch49数值correctness→近似faultrecovery主干已补并通过root核；平均LPIPS不证明每图quality或部署收益。

### [EdgeFlow: Fast Cold Starts for LLMs on Mobile Devices — 2604.09083v1](https://arxiv.org/html/2604.09083v1)

§4.1–4.3/5.1–5.5：channel-greedy压缩、bit-weightlet解包INT8、topologypriority+CPUsteal阈值改变coldstart criticalpath。Xiaomi15Pro/Snapdragon8Elite16GB/512GB，Llama/Mistral/Phi/Qwen平均4–7bit，5bit有quality代价；512/512 CPUdecode不总更快，QNN逆向格式兼容限制。Ch49图优化后的coldstart/resident分支已实写并通过root核，不用局部TTFT代完整servingSLO。

### [CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation — 2604.09155v1](https://arxiv.org/html/2604.09155v1)

2+2+2=6安全深入/争议暂缓：§3.4Eq3–5控制joint risk，未给conditional executed-risk相同界；AppD Eq10 HR=Σeh/T所有proposal、Eq11mHR=Σeh/Σe执行条件率、Eq12GAR=executioncoverage非task-goal成功。coverage<1时joint≤α不足以推出“自主执行最多1% harmful”，需除coverage。root必要原文独立核同意隔离此采用保证，不否定jointCRC本身。恢复需作者补条件分母证明/明确收窄宣称；不写Books安全保证。

### [Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG — 2604.09174v1](https://arxiv.org/html/2604.09174v1)

1+2+2=5标准完成：§3–6，Hotpot3000/medical1500、24039/11007facets，goldsupport仅Hotpot，BGEbase/300chunk/50overlap/K5、RoBERTaMNLI entail−contradict不是校准概率。StrictEvidence/SoftRAG/LLMonly和resynthesis使用同facet而每case单run；strict失败与soft约30%退化不等内部先验因果定位。Ch76 301–337relevance/sufficiency/faithfulness及counterfactual evidence段已具体承载，已有覆盖。

### [Generalization and Scaling Laws for Mixture-of-Experts Transformers — 2604.09175v1](https://arxiv.org/html/2604.09175v1)

2+1+2=5标准完成/仅报告：§3Theorems3.2/3.4/3.7、§5–6，boundedhardTopK/Cβ/compactC1manifold/iid squaredloss下worstcase路由组合容量项；不是任意LM loss或learnedrouter优化的通用scaling recipe。TinyStories/WikiText/OpenWeb少预算拟合、估计intrinsicdimension和β与moderateM/k实验非单调，保留理论对象/假设差异，不据此修改Ch21工程路由结论。

### [SAGE: A Service Agent Graph-guided Evaluation Benchmark — 2604.09285v1](https://arxiv.org/html/2604.09285v1)

1+2+2=5标准完成：§3–4，SOP graph state→path→action与chat三judge分开，path是setoverlap非完整顺序合法性，judge labels输入rule仍非deterministic truth。27models/6scenarios、turn1/5/10/15/final，不称所有turn覆盖；不同Qwenjudges严格度构成反证。Ch66 process/outcome与judgecompetence/bias具体正文已承载，已有覆盖。

### [OASIS: Online Activation Subspace Learning for Memory-Efficient Training — 2604.09406v1](https://arxiv.org/html/2604.09406v1)

§3 Eq1–5/Alg1/3.2/§4–5：forward fullX、save XU投影backward/fullweights，onlineOjabasis/reorthogonalize；basis overlap运firstmoment，diagonal secondmoment近似而非fullcovariance。130M loss3.28>Adam3.21，1B rank32GSM8K23.78<27.09；rank/drift/orthogonalize增加成本。Ch39 lowbitstate后实际补坐标identity与momenttransport，root核通过，不称精确梯度、LoRA或所有scale无损。

### [Many-Tier Instruction Hierarchy in LLM Agents — 2604.09443v1](https://arxiv.org/html/2604.09443v1)

1+2+2=5标准完成：§4–6，853=427code+426IF、46agent contexts、10models/40k/temp0，多层增加同时改变冲突数量，无法只归因层数。ordinal/scalar表示与保序数值扰动也改变服从说明prompt labels不等authority。Ch72 InstructionHierarchy authenticated provenance/policyengine段已承载，已有覆盖；不把有限bootstrap当全模型保障。

### [Attention-Based Sampler for Diffusion Language Models — 2604.08564v1](https://arxiv.org/html/2604.08564v1)

§3.1–3.2/Alg1–2、§4与Table1/§5.1–5.5：单层Softmax、块内固定attention及平均代表性假设下，column-sum降序优化的是近似目标，不是任意多层全序列likelihood。动态阈值来自低置信组最大影响，sub-block提取绕开融合kernel不materialize attention的问题；理论FLOPs÷A100峰值不是实测开销。Fast-dLLMv2-1.5B/7B与LLaDA1.5-8B、单A6000、GSM8K/MATH/HumanEval/MBPP；1.5B Parallel MATH31.02<Confidence32.24，7B Parallel MATH51.88<Entropy51.92，不能称每项最优。采用证据中precision、输入输出长度、batch、并发/SLO未披露。Ch24 masked generation原confidence schedule与00375探索熵分支后已实际补影响排序/成本条件，root已完成必要原文与实际正文/相邻链路的独立采用复核；未复现实验。

### [Skip-Connected Policy Optimization for Implicit Advantage — 2604.08690v1](https://arxiv.org/html/2604.08690v1)

§3.1–3.2/Eq1–6、Table2/§4.1–4.3、AppendixC/D：上游早停段与原题重排[s,q]后，G个下游结果均值作prefix reward；单上游使用KL衰减历史SPO baseline，下游GRPO不能反向借作其空间baseline。vLLM同batch暂停，median mean-NLL选段、KV指针重定向并重算重排prefix；不保证无discard工作。Qwen2.5-Math7B/Llama3.2-3B、dapo-math-17k、500steps、128prompt/G8、bf16、1024/3072长度；训练GPU型号/生产SLO未披露。Table2组件移除均低于原方法，但GPT5-nano只分析correct轨迹且instruction continuation不是真rawprefix或learner因果信用。Ch33 token-credit原段后已实际补此分支，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [p1: Better Prompt Optimization with Fewer Prompts — 2604.08801v1](https://arxiv.org/html/2604.08801v1)

§3.2–3.3/Eq4–5、§4–5、§7：二元reward/iid response的总variance拆为response sampling与真实prompt差异，selector扣噪声而不用不稳SNR；每轮KNM成本及子集穷举不能遗漏。Qwen3-4B prompt generator、4B/1.7B frozen response、4H100三日预算、K×M约固定，数学Ktop1过拟合、IFBench全量仍更好；跨Qwen家族迁移未证明开放任务普适。precision/生产并发SLO未披露。Ch74生命周期中实际插入‘自动Prompt优化还要区分设计信号与采样噪声’，不把teacher训练或Prompt增加authority混写，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [Spectral Geometry of LoRA Adapters Encodes Training Objective and Predicts Harmful Compliance — 2604.08844v1](https://arxiv.org/html/2604.08844v1)

§3.1–3.6、§5.2–5.8/§7：Llama3.2-3B r8、q/v_proj、38adapter含4legacy，70/30小split。DPO训练sensor在steering上AUC0而非普适指纹；steering使生成collapse，Guard判unsafe而GPT4o对300条判0harmful，不能把artifact当真实攻击成功。ρ.72只来自24非steered且主要healthy/drift分群，PCA14/18文字冲突不采用定量全域分离。hardware/完整precision长度并发SLO未披露。Ch66 subject identity后、harness小节前已补跨method holdout与行为测量分支，安全反证及真实gap深入，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [Revisiting the Capacity Gap in Chain-of-Thought Distillation from a Practical Perspective — 2604.08880v1](https://arxiv.org/html/2604.08880v1)

§3.1–3.3、§4.1–4.3、AppendixA/B/C：Qwen2.5各尺寸与QwQ32B、MATH/15预选BBH、4A10080GB、单run。同题共同正确交集合法隔离rationale；单teacher全部正确集考察部署效用，却一起改变数量/难度/质量，不证明capacitygap不存在。原mix有效batch20而standard2造成10倍update差，对齐后原优势不稳定；BBH3:2split与>30pp ICLgap预选限定外推，1.3比例不成普适阈值。Ch29多teacher debate前已补基线与两种estimand；precision/线上并发SLO未披露，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [Drift and selection in LLM text ecosystems — 2604.08554v1](https://arxiv.org/html/2604.08554v1)

§4.5 Theorem2、§5.2–5.5：有限字母表、variable-order n-gram与soft normative publication下，描述性固定点是n-shallow，外部规范要求超出n阶可产生非零project–lift KL/L1稳态。matched exact recursion仅5符号、n3/r5、同seed、80/20贡献、α1，区分‘收敛’与‘保留长程结构’；不是实际训练LLM。Ch27递归synthetic语料段已拆supplier/parameter/corpus与human-anchor约束，但本项对真实tokenizer、learned conditional与过滤器没有可验证的对应或通用阈值。保留这个理论对象的新边界，不据toy equilibrium配置修改生产recipe；hardware/precision/length/batch/concurrency/SLO为理论不适用，未运行script。

审阅：标准完成，评分2+1+2=5；仅报告：受限recursive n-gram理论不据此采用真实LLM语料稳定过滤规则。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Multi-User Large Language Model Agents — 2604.08567v1](https://arxiv.org/html/2604.08567v1)

§4.1–4.2、§5.1–5.3：共享上下文同时观察多用户消息，Ci默认私有、persona/global constraint串在单user-role；Says/Colon/XML并非认证authority。题目把instruction selection F1与execution Acc、privacy与authorized utility、partial-disclosure协调分开。温度/top-p均1，受测模型在selection高时执行仍低，隐私高时效用可低，conflict/aligned条件和轮数另有对照；不外推真实ACL。Ch72‘Agent Privacy必须对整条Trajectory记账’与‘隐私检测是Policy-bound Sensor’已要求独立收件人/任务效用评测和sensor≠access-control，Instruction Hierarchy区分prompt标签与真实authority，实际承载这个判断。保留新多用户反证，而不是因已有主题拒绝；hardware、精度、输出长度/batch/并发/服务SLO未披露，不采用数字保证。

审阅：标准完成，评分1+2+2=5；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Distributionally Robust Token Optimization in RLHF — 2604.08577v1](https://arxiv.org/html/2604.08577v1)

exact-v1 §3.1–3.2/Alg2–3/§4/AppendixA.1：RTO用DPO-derived token reward，DRO重加权minibatch的完整trajectory，不是每span新增reward。作者与apr03重新核HTML MathML和PDF-v1 Eq8均为Ψη+ρ/η，与Alg2及ν=1/η一致；旧纯文本提取丢失fraction导致ρη误读，撤销原公式争议，不等待不存在的勘误。χ² mean/std上界仅满足非负权重条件时tight，不直接成为任意deployment OOD保证。Llama3-8B/OpenMath10k/五数学bench只支持披露目标分支；保留这个受限轨迹鲁棒目标于报告，不把minibatch半径升级为Ch32开放分布不变性。hardware/precision/完整长度/batch/concurrency/SLO未披露不补造，未运行代码或复现实验；apr03必要原文独立裁决为5分标准、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：受限minibatch trajectory-DRO不等任意OOD保证，原KL公式争议已按官方原式撤销。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [On the Spectral Geometry of Cross-Modal Representations: A Functional Map Diagnostic for Multimodal Alignment — 2604.08579v1](https://arxiv.org/html/2604.08579v1)

§4.1、§4.4–4.6、§5：DINOv2-B14 768维/MiniLM-L6 384维，Flickr30k1000图各5caption均值，graph kNN15、basis50–100、单seed。谱距离相近但functional-map basis不对齐，低监督composition弱，受测retrieval低于Procrustes/relative；image-level caption-equivalence使i2tR1=R5，与标准CLIP协议不可直接拼榜。graph采样本身可能影响几何诊断，不能推出所有encoder缺共享语义。Ch23‘统一架构不等于双向可用的统一语义空间’及随后的几何噪声反证，已明确相关几何≠可操纵/可用语义，实际承载本项采用命题；保留受控新负结果，但不据此替换跨模态alignment机制。hardware/precision/batch/concurrency/SLO未披露。

审阅：标准完成，评分1+2+2=5；已有覆盖 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Adjoint Matching through the Lens of the Stochastic Maximum Principle in Optimal Control — 2604.08580v1](https://arxiv.org/html/2604.08580v1)

§3/Table1、§5 Theorem4/Remark5、§6：general drift/control-dependent diffusion的Hamiltonian BAM涉及一阶/二阶adjoint；仅σ(t)的专门条件可lean AM避免二阶quantity。Lemma9 verification/regularity承接critical point与optimal control，不等有限神经参数训练全局收敛；SMP BSDE的q未知，lean-adjoint给Hamiltonian方向的无偏估计，在此连续控制对象下解释MSA。trust-region稳定保证属于future work。exact-v1没有实际生成器数值性能对比，不能沿缓存后发‘已数值证明必要性’；理论不适用硬件/precision/length/batch/concurrency/SLO。本项解释的是指定连续控制对象下的噪声/adjoint依赖，尚无训练生成器的数值迁移证据；保留这个理论增量于报告，不把它改写为Ch24已验证的采样器或训练保证。root必要来源独立裁决为标准完成、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：σ条件下理论未验证训练生成器迁移或部署收益；root必要原文独立核通过。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Unified Multimodal Uncertain Inference — 2604.08701v1](https://arxiv.org/html/2604.08701v1)

§2–3.3、§4 Tables3–4：WikiVideo10主题的人类scalar premise/hypothesis判断分别标audio/video/AV；teacher5次推理均值不是独立真值，CLUE-D 100confidence bins、σ.05 Gaussian target、KL训练，输出期望替代直接生成标量。token-vs-distribution/pos:neg比例改变MSE，audio切片token分支可更好；1:1选ratio不能普适且改变training prior。modality-specific batch减少padding/gradient imbalance，不由总结果证明其全部因果作用。受测3B模型与human/MSE目标不证明世界事实概率或deployment risk校准；precision/hardware/完整长度/batch/concurrency/SLO本次必要位置未披露。分布化输出是拟合人类scalar target的可检验接口分支，但MSE不能证明事实正确性或风险校准；不据此改变Ch66的事实/部署calibration contract。root必要来源独立裁决为标准完成、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：人类scalar target拟合不形成事实正确性或risk calibration保证；root必要原文独立核通过。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition — 2604.08708v1](https://arxiv.org/html/2604.08708v1)

§4.1–4.3、§5.1–5.7：10条独立run×不同agent/不同轨迹长度的embedding建ragged集合，PARAFAC2低秩重构残差量化整段结构变化而非只final-answer agreement。Qwen3-embedding-.6B/dim256，GPT4o/Qwen2.5-7B/Llama3.1-8B、Camel/AutoGen/AnyMac、MATH/MoreHopQA/MMLU/HumanEval，temperature.9、单A10080GB或API；GPT5给final correctness标签，AUROC/AUARC为ranking，不是频率校准。工具结果也字符串化，低残差可以共享同源错误；tensor轴不能仅凭名称取得topology/communication因果解释。新增多run成本、rank/embedding选择和judge版本影响测量，未给独立真实risk保证；Ch66已有trajectory evidence、correlated-error与calibrated sensor主干，本次只保留受限新proxy，不将它当稳定production Gate替换。precision/完整长度/batch/服务并发SLO未披露。

审阅：标准完成，评分2+1+2=5；仅报告：ragged重构代理尚不作为校准risk或通信因果归因。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics — 2604.08764v1](https://arxiv.org/html/2604.08764v1)

§2–3、Table1、§5：10encoder/decoder模型210M–1.7B，同合并C4/Wiki/FineWeb/arxiv/Frenchwiki语料，以早30%activation拟一次固定PCA QT，再测早/晚gradient matrix在其与matched-rank normal方向的能量；20random normal null令p最小1/21。QT只是activation-derived tangent proxy，不是真实概念/流形；去QT改善IsoScore*与early gradient集中支持局部几何解释，却不证明isotropy改进必然提升语义或泛化。晚期一些切片退步、encoder更弱、proxy未跟随late变换均保留。论文明确没有新optimizer/architecture或干预训练结果，故保留形成机制与测量反证，不把相关性写成新训练recipe。hardware/precision/length/batch/concurrency/SLO未用于本次采用数字，未披露不补造。

必要理论反查§2.4 Eq9/10/11：tangent与normal两个梯度上界不能直接相除得到比率上界，尚缺tangent非退化下界。局部抛物线x=(u,u²)、对称小u、W=0平方损失y=−1时g=1，tangent期望E[u]=0而normal E[u²]>0；这是本次独立反例，不是作者实验。故不采用Prop2.3的普遍ratio或自强化因果保证；固定PCA proxy/匹配秩的有限测量不随之作废。局部实验仅报告，理论保证单独隔离于§5；重开须补适用的梯度下界或修正定理。apr03必要原文及具体反证独立核通过。

审阅：标准完成，评分2+1+2=5；仅报告：保留固定PCA局部测量，不采用缺少下界的梯度ratio保证或普遍泛化结论。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [ELT: Elastic Looped Transformers for Visual Generation — 2604.09168v1](https://arxiv.org/html/2604.09168v1)

exact-v1 §3 ILSD/Eq1–2、§4.1–4.2/Figure8及Limitations：full-depth teacher与随机严格prefix student在同一图共享θ，target停止梯度但共享参数仍由两支更新，groundtruth监督λ由1降至0。它补充的是中间深度输出合同，不是implicit fixed-point或免费adaptive depth。ImageNet256/UCF16×128×128、MaskGIT/MAGVIT codebook1024/270epochs；DiT SD1.4VAE、batch512/500k、512DDPM/CFG3。N1×L32 FID10.30与超训练Lmax退步限制无限深度/容量推断；硬件、precision、生产并发/SLO Not Disclosed。Ch24 equilibrium后已实际整合有限loop分支，root核必要原文、正文及前后衔接通过，未复现实验。

### [Decoupling Vector Data and Index Storage for Space Efficiency — 2604.09173v1](https://arxiv.org/html/2604.09173v1)

exact-v1 §3.1–3.5/§4.1–4.2/§5.1–5.2.2，不沿用库存后发COMPASS标题。邻接与向量分开编码/存储；导航优先图I/O，内存PQ候选稳定后批量预取向量重排，batch graph merge/repair与vector append/GC通过ID-location协调。无损编码不等于exact ANN，early-stop仍近似。双32core Xeon8336C/512GB/PM9A3 NVMe、64搜索线程、109M proprietary/100M–1.4B公开向量、recall@10配QPS/P99；8bit向量delta不改善，低Ls和部分billion低recall吞吐可更差，不采用生产freshness/SLO保证。Ch76 filtered ANN与index update之间已实际写入layout/I/O/维护分支；root必要来源、实际正文及相邻论证独立通过，未复现实验。

### [MixFlow: Mixed Source Distributions Improve Rectified Flows — 2604.09181v1](https://arxiv.org/html/2604.09181v1)

exact-v1 §3–4/Alg1–2/§5–6：对κ-conditioned Gaussian与标准Gaussian的μ/Σ作连续参数插值，共同训练velocity，非Bernoulli抽选两个source。κ=x1只训练可见时，部署由已训练的标准端点采样，不需要条件source预测器。额外网络与联合训练、KL/插值权重是代价；CIFAR10/FFHQ/AFHQ64、作者FID/NFE中，低β可在高NFE退步，FFHQ4NFE不全面更好。Eq5与Alg1 KL对象不同，不采用exact objective统一或NFE即wall-clock/SLO；硬件、precision、生产并发/SLO Not Disclosed。Ch24 source identity后已实际整合训练覆盖与缺κ回退条件，root必要原文、正文和相邻论证独立通过，未复现实验。

### [Advantage-Guided Diffusion for Model-Based Reinforcement Learning — 2604.09035v1](https://arxiv.org/html/2604.09035v1)

exact-v1 §IV–VII：窗口reward会遗漏长期价值，SAG以有界sigmoid、EAG以指数advantage倾斜trajectory diffusion，state-dependent normalizer不可省略；生成轨迹再进入actor/critic buffer。真实advantage、均值零与单调权重条件下的理论改善不等学得value/world时每次policy单调。四MuJoCo/1.5M真实env steps，Hopper低于PolyGRAD，SAG/EAG对value误差的敏感度不同。保留这一理论与目标分支，仅报告，不把Ch25想象轨迹升级为长期return保证；hardware/precision/生产SLO Not Disclosed。apr03必要原文独立核通过，未复现实验。

审阅：标准完成，评分2+1+2=5；仅报告。

### [Tora3: Trajectory-Guided Audio-Video Generation with Physical Coherence — 2604.09057v1](https://arxiv.org/html/2604.09057v1)

exact-v1 Methods、Tables2–5/AppendixF–G：首帧latent依2D轨迹搬运作局部flow endpoint，外部区域Gaussian；audio消费8D position/velocity/acceleration。soft mask和区域均衡loss避免稀疏运动区被背景稀释，初始audio gate减少干扰。Ovi720×720/5s、32A100/bf16、batch32/30ksteps、50代表视频；video-only与audio-only各有指标优势，joint不全面最好，tracking/音频相关不是物体质量、接触或空间声学真值。Ch24 guidance/prior后已实写共享状态与两接口分支，apr03必要源/真实正文/相邻衔接独立通过；未披露生产并发/SLO，不用同步指标批准World Model。

审阅：深入完成，评分2+2+2=6；整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md), apr03实际写后独立通过。

### [Hierarchical Alignment: Enforcing Hierarchical Instruction-Following in LLMs through Logical Consistency — 2604.09075v1](https://arxiv.org/html/2604.09075v1)

exact-v1 §4.1–4.2：parser按来源atomize指令，pair-NLI估计冲突，lexicographic MaxSMT选一致子集，再把偏好蒸馏到policy；43,380条训练及strong-language测试仍有失败。可满足性不等开放语言安全，parser/NLI可能漏上下文与传递冲突。Ch72 Policy-as-Data现已分开versioned policy artifact、模型sensor与确定enforcement/fallback，实际承载该采用命题；已有覆盖，不以solver结果替代ACL。apr03必要源和当前正文独立核通过，保留受限新反证而非按安全主题拒绝。

审阅：标准完成，评分1+2+2=5；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过。

### [DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation — 2604.09089v1](https://arxiv.org/html/2604.09089v1)

exact-v1 方法及Tables3–4：attention聚合训练token analyzer，LoRA联合secure CE/margin/KL；一次prompt分数调vocab bias，后续不随每个token持续判断。QwenCoder3/7B、DeepSeekCoder1.3/6.7B、SeedCoder8B；joint secure-pass不同于conditional security，删安全目标后仍用未训analyzer steering会伤功能，无KL也有功能退步。Table4受限300token下k64检查wall-clock +38.7%，更频繁代价陡增，不外推完整SLO。Ch72 Learned Security Sensor已有一次检查/持续风险/频率/执行authority分工与fallback，判已有覆盖；apr03必要原文及真实正文核通过，不将固定bias称校准risk。

审阅：深入完成，评分2+2+2=6；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过。

### [CLIP-Inspector: Model-Level Backdoor Detection for Prompt-Tuned CLIP via OOD Trigger Inversion — 2604.09101v1](https://arxiv.org/html/2604.09101v1)

exact-v1 §3–5.3/Limitations：白盒trigger inversion在1000无标签OOD图与候选class中查异常ASR/loss，冻结CLIP并不消除learnable prompt/meta-network供应链风险。ViT-B16/CoCoOp、10datasets/4attacks、最多50候选且必须含target；47/50检出仍有三fine-grained失败，100图pool明显弱，repair另需clean labels，k2阈值不是risk校准。Ch72可组合Prompt的identity/versioned supply-chain与trigger-neighborhood测试真实覆盖拟采用命题，判已有覆盖。apr03必要源/实际owner独立通过，不采用任意攻击检出或clean-free修复保证。

审阅：深入完成，评分2+1+2=5；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过。

### [Truncated Rectified Flow Policy for Reinforcement Learning with One-Step Sampling — 2604.09159v1](https://arxiv.org/pdf/2604.09159v1)

exact-v1以官方PDF为准（HTML页头为后期编译），§4.1–4.5：deterministic prefix加Gaussian tail，RL梯度限tail，prefix用off-policy endpoint MSE自蒸馏。采用的是受限截断设计，不采用真实terminal marginal entropy保证：augmented joint surrogate省略prefix volume correction，沿路径对time恒定也不推出对state的divergence为零。评价可省tail但仍用N候选Q选择，one-step不等完整decision只有一次计算。apr03必要PDF独立核通过，仅报告；中心entropy/全局改进保证隔离于§5，不否定全部实验，也不新写Books精确entropy承诺。

审阅：标准完成，评分2+1+2=5；仅报告。

### [GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking — 2604.09222v1](https://arxiv.org/html/2604.09222v1)

exact-v1 §3.1–3.3/§4.3–4.4：attack和ASR utility的双梯度选稀疏Mel bands；同48-band随机控制与full-band反例说明更多频带不必更强攻击，而可更损utility。四7B/10B ALLM共享Whisper-large-v3；AdvBench520音频80/20、Libri500/AIR800、4090/bf16/100epochs/T3000，由LlamaGuard3/DeepSeekV3判断。有限结果不证明人耳无感、全encoder外推或实际risk校准。Ch72 Sensor Robustness不能删除Task-critical Semantics现有benign countertask与attacked outcome双分支真实承载，已有覆盖；apr03源/owner独立核通过，不增攻击教程。

审阅：深入完成，评分2+1+2=5；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md), apr03具体owner独立通过。

### [Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models — 2604.09227v1](https://arxiv.org/html/2604.09227v1)

exact-v1 §3 Eq4–11/Alg1/§4–5：选择downsampler D，估计其与velocity的commutator，用短窗口stored HR velocity校正LR preview，选seed/prompt后重新运行标准HR生成，不是上采样同一轨迹继续。Flux1-dev/SD3.5L、A100、PixArt30K随机5000prompts（2–1885chars），500轨迹/5step相似结果仅受限近似；selector、早期HR和缓存漂移成本不为零，预览速度不等最终交付SLO。Ch24跨尺度draft后已实写preview选择分支与直接HR回退，apr03必要源/正文/相邻链路写后通过，未复现实验。

审阅：深入完成，评分2+2+2=6；整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md), apr03实际写后独立通过。

### [2D or 3D: Who Governs Salience in VLA Models? -- Tri-Stage Token Pruning Framework with Modality Salience Awareness — 2604.09244v1](https://arxiv.org/html/2604.09244v1)

exact-v1 §4.3–4.4/§5.1–5.3/Table3：首步dense，窗口/EMA先平滑模态及区域salience，再按阈值形成独立候选并融合；不写成EMA调整固定阈值。冻结MLA/RLBench四任务、A100-PCIE40GB/Xeon6348，Table3 S1+S3 62.2<baseline70，S2+S3 71.5，是受限交互反证；另Table2 50%配置47.5<不剪48.8，不能混为无损宣称。norm/attention只是代理，不是动作因果重要性。Ch23时间区间合并之后实写平滑/语义保护分工与静态、不复用、dense回退，apr03必要源/实际正文及邻接通过；precision/batch/生产控制SLO Not Disclosed，未复现实验。

审阅：深入完成，评分2+1+2=5；整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过。

### [VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis — 2604.09330v1](https://arxiv.org/html/2604.09330v1)

exact-v1 §3.2–3.3/§4.2–4.4/Limitations：clean video detach/global pooling后重复供action序列，生成video不受action影响；同步flow time不是双向闭环。CosmosPredict2-2B、480P10Hz93frames/432×768/35NFE、8H20/40k/batch1每GPU，AgiBot1794/200、LIBERO400/50。Table2各维error<.2的SR与Table3 replay task success不同，真实20trials11vs7还改变synthetic-pretrain预算。Ch25 environment/agent/joint channel与counterfactual action support已具体承载拟采用边界，已有覆盖；apr03必要源/当前正文独立通过，不写rigorous alignment或物理安全保证。

审阅：深入完成，评分2+2+2=6；已有覆盖 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md), apr03具体owner独立通过。

### [Phonemes vs. Projectors: An Investigation of Speech-Language Interfaces for LLM-based ASR — 2604.09332v1](https://arxiv.org/html/2604.09332v1)

exact-v1 §3–5.3/Tables1/4/5/7：冻结Whistle encoder、20h Tatar配对适配比较连续projector与phoneme/wordboundary接口；预训练已含Tatar，不称未见语言泛化。英语encoder recipe不同，音素BPE113→125tokens反而更长，词表扩大也会退步，显式接口优势不等减token或完整声学保真。Qwen3-1.7/8B、Libri960、披露8A800训练recipe不作推理时延。Ch23 encoder/projector→共享token交接已实写监督约束与接口共存分支，apr03必要源/真实正文/相邻核通过；5分真实缺口深入，未复现实验。

审阅：深入完成，评分2+1+2=5；整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过。

### [Mind the Gap Between Spatial Reasoning and Acting! Step-by-Step Evaluation of Agents With Spatial-Gym — 2604.09338v1](https://arxiv.org/pdf/2604.09338v1)

官方PDF-v1 §3–4.2/AppendixA：八模型500同puzzles、4A10080未量化baseline/Gym，one-shot与step/backtrack改变调用、历史与legal-action接口，grid仍可见；weak改善而strong stepwise −5.6/−5.8，backtrack completion提升不等solve。不能仅归因训练激励或contamination，更不是compute-matched能力榜。Ch79 Search-based Planning真实解释搜索/回溯收益非单调与预算回退，Ch66 protocol与outcome分账相邻支撑，唯一owner Ch79已有覆盖。apr03必要PDF及具体正文独立核通过，不采用普遍空间能力保证。

审阅：标准完成，评分2+1+2=5；已有覆盖 `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md), apr03具体owner独立通过。

### [Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts — 2604.09364v1](https://arxiv.org/html/2604.09364v1)

exact-v1 §5–7/Limitations：full-sequence与last-position matched patch不同，九模型各100合成反事实，三7B～8B局部SAE steering。probe可读不等答案采用，MAC首稳定logit crossover只是定位heuristic，steering有退步；自然图像、开放truth和生产SLO未验。float16/bfloat16、至多4H200/device_map auto只绑定披露设置。Ch23 Object Hallucination Circuit Probe→VQ交接实写干预位置/sequence范围及外部grounding回退，apr03必要源/实际正文/相邻独立通过，未复现实验。

审阅：深入完成，评分2+2+2=6；整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过。

### [Do Vision Language Models Need to Process Image Tokens? — 2604.09425v1](https://arxiv.org/html/2604.09425v1)

exact-v1 §3–7：六VLM跨层state替换仍保留visual read，实际删tokens则改变访问合同并须同步mask/positions/KV；single-token答案也可退步，不能把multi-token VQA与caption差异泛称所有reasoning难度。LoRA/distillation有额外训练、teacher依赖，caption teacher相似不是人类真值。Ch23阶段压缩后实写稳定性≠可删除及协议验收，apr03纠正输出术语后写后最终通过；hardware/precision/生产并发SLO本次必要证据 Not Disclosed，未复现实验，5分真实缺口深入。

审阅：深入完成，评分2+1+2=5；整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过。

### [Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories — 2604.09429v1](https://arxiv.org/html/2604.09429v1)

exact-v1 §3.2–3.5/§4/Limitations：canonical frame中raxel=d+o三通道、coarse H/2×W/2复用video VAE、modality与grid身份供video/camera双向去噪；chain-rule和同shape不是joint正确证明。Wan2.1T2V14B+6B camera branch、RealEstate10K/DL3DV metric-scale、480×832/12FPS，Procrustes解pose、focal假设principal point居中；Plücker对照同时换codec，cycle不是外部3D真值，动态/内参偏离须验。Ch23 camera/provenance→3D state交接实际写入与独立pose回退，apr03必要源/正文/相邻独立通过；hardware/precision/生产SLO Not Disclosed。

审阅：深入完成，评分2+2+2=6；整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md), apr03实际写后独立通过。

### [E3-TIR: Enhanced Experience Exploitation for Tool-Integrated Reasoning — 2604.09455v1](https://arxiv.org/html/2604.09455v1)

exact-v1 §4.1–4.2/§5.1–5.3/Tables3–4/AppC：self池保留，高entropy anchor分expert suffix，best expert优于self才纳混合组；negative expert branch停共享prefix梯度，suffix继续更新，prefix混合ratio不等完整无偏IS。8A100，SFT bf16/4096/batch128/3epochs；RL warm-up n8+m8/k3/50steps、post n16+m0/250steps，batch128/mini16/response8192/obs512/max4tools。tree-adv部分退步，文字降幅与表不一致不照录，不证明同总预算优势或model knowledge truth。Ch33 teacher/prefix信用交接实写分流与self/离线回退，apr03必要源/实际正文/相邻独立通过，未复现实验。

审阅：深入完成，评分2+2+2=6；整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md), apr03实际写后独立通过。


## 5. 缺口与下一步

普通可执行工作：无。33实际增量均完成写后非作者复核；原12项中11项必要原文/实际owner已由apr03复核，SEA已按可用材料边界精确隔离。最终日级来源/日期/集合与处置独立复核通过；未变化的有效PASS复用，不重扫504或无差别全文。以下是安全终态保留项，不是声称缺失证据已经通过。

已隔离的来源保留项：

- [SEA-Eval 2604.08988v1](https://arxiv.org/pdf/2604.08988v1)：缺可绑定此原版题名和版本的完整§4–5。HTML呈现后版内容，官方PDF有界尝试均截断、无有效EOF/解析结果；旧作者笔记不能替代当前独立材料。它不支持正面实验结论、Books或完整证据断言，处置受阻/暂缓。可接受官方完整v1 PDF，或明确绑定该原版的作者稿及必要方法/评价页；届时只重开本项及依赖结论，不重扫全日。未提出私有artifact或全部版本史请求。

- OpenAI：News RSS已跨窗口，Research Index的历史Load-more未恢复；Research/Publication sitemap只用于身份发现，lastmod不证明首发。Google：April Blog/DeepMind selected目录已读，但Publications日级历史停点不可取。Meta：Research返回不可读内容，缺历史Research/Publications日期列表。三者须恢复官方日期目录/当窗artifact或可复核历史快照后定点重开，不支持全机构零遗漏或未读研究的正面结论。
- Moonshot：已核KimiCLI相邻正式release窗外，Blog只读到2025-11历史；完整April Blog/CLI分页仍缺。Xiaomi MiMo：Paper跨窗、模型release空，但Blog历史日期入口缺失。MiniMax：EN/CN Blog及CLI26release跨窗，但Agent TechBlog历史日戳缺失。恢复相应官方目录/分页或当窗原文日期后仅补相关入口；不把普通commit或模型名字当发布事件。
- Seed：[Continuous Adversarial Flow Models](https://arxiv.org/abs/2604.11521v1)官网目录PublishDate `2026-04-12T16:00:00Z`，而外链exact-v1 submitted `2026-04-13T14:23:31Z`；目录日期与该版本正文尚无法建立同一首次公开事件。[Nexus](https://arxiv.org/abs/2604.09258v1)目录日期 `2026-04-09T16:00:00Z`更早，但本文版本/公告批次与目录正文是否同版未证。两项不作为本窗候选、不进入Books；恢复当时官方正文/版本及公开时点证据后分别定位真实owner，submitted单独也不是首发证明。

日期保留项：[原始身份与原字段](../_sources/arxiv-owner-replay-20260903/20260413/arxiv-owner-receipt.json)中49项v1 Updated字段不早于本窗截止，另有后期更新混入，不能使用前段的早字段推断为整批授权。保留各ID/原值供定点恢复，本窗不采用其方法/评分，也不把它们机械迁至下一天；需官方公告/精确版本/可支持本窗的联合证据。前段已经过联合校准的家族不因这些例外全量重审，Updated、DOI-created和submitted任一字段都不能单独改名首发。

中心采用限制：[CORA](https://arxiv.org/html/2604.09155v1)的joint harmful-execution risk上界不能直接成为条件执行harm rate；HR全proposal、mHR条件执行、GAR执行coverage必须分开，单项暂缓，需作者收窄或补分母证明才重开其安全保证。[08764](https://arxiv.org/html/2604.08764v1)两个梯度上界缺tangent非退化下界，不能推出普遍ratio保证；保留固定PCA局部测量，仅报告，补下界/修正定理后只重开理论采用。[09159](https://arxiv.org/pdf/2604.09159v1)保留截断设计，仅报告；joint surrogate与terminal marginal entropy不同，沿路径time恒定不能推出state divergence为零，需完整volume/边缘熵推导才能采用该保证。三处不支撑Books强保证，不否定各自全部有效实验。DRTO08577旧公式争议已按官方MathML/PDF-v1 ρ/η撤销，不能继续请求不存在的勘误。

## 6. 复核

复核者：apr03（非作者日级、有限必要原文与新增8项写后复核）；root（未变25项实际增量及其他5项必要证据结果）
结论：通过

日级复核实际核对14个来源的入口、主题与具名停点，67行/67唯一家族及对应证据，日期联合推定与49晚字段、2个Seed例外的隔离；没有把宽库存误作全文队列。33项实际Books增量已由root（25项）或apr03（8项）核必要exact-v1、真实正文和相邻链路；有限恢复组的22项、原12项及新增6个否定侧抽样见[非作者增量与日级核验](../_sources/daily-20260413/V3_INDEPENDENT_INCREMENT_AUDIT.md)，另5项未变root结果复用。08577纯文本误读已撤销、08764比率保证单独隔离、09425协议术语和09244 EMA→候选→fusion顺序已修正。SEA隔离处置通过，不是原版证据通过；普通待办为0。范围未覆盖504全文或全外部目录，未运行论文实验。当前V3结构/一致性校验与本次文件范围diff检查通过；仓库全局cached检查仍有运行前已有09/22与个人任务文件的行尾空白，未为本任务修改或stage它们。机器检查不替代上述语义复核。
