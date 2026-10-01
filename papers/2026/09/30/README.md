# Daily Research — 2026-09-30

**规范：** V3
**窗口：** 2026-09-29T09:00:00+08:00 ～ 2026-09-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T15:45:00+08:00

## 1. 结论

本窗冻结 **42 个唯一材料家族**：37 项完成针对采用命题的深入审阅与实际 Books 整合，3 项标准审阅后确认具体已有覆盖，2 项标准审阅后仅保留新增对照证据。实际新增机制进入21个现有章节；没有新增章节，也不把框架/论文名称当成论证主线。正式报告和实际写回已通过非作者验收，普通可执行待办为0；完成指本窗安全终态，不表示八项隔离材料的Coverage/Evidence已通过。

重要变化集中于三条系统关系：

- 状态复用不是一个“cache hit”指标：原生selector决定正确读取，consumer适配、近似跨迭代cache、recurrent writeback与layout handoff各有不同authority和代价。
- 学习信号必须分开“谁选位置”“谁估贡献”“哪些token受监督”：teacher suffix、segment续跑、advice敏感性和memory增量不等于同一种credit。
- 高共识、高agreement或新排行榜不能直接变成真实能力保证：分组与sensor耦合、人工抽样、共享答案池的任务变化都需独立解释。

原始列表是有界发现入口，不是每日有数百篇长期贡献的断言：实际浏览cs.CL本期145个新标题、cs.DC的24个new/cross标题，另以限定主线题名查询浏览首80条（该查询总命中187，未声称187条全部语义关闭）。它们重叠，**不相加为raw唯一身份或完整摘要数**。42项均实际读完整题摘并取得精确正文/必要证据；首批准入及后续审阅分批独立核查。ER-JEPA被抽检反证后从拟关闭重开为候选，没有为降低工作量删去该证据。

八处来源/日期缺口已穷尽本次可用定点恢复路径并隔离，见§5：不支持候选、Books或“无遗漏”断言。来源受限不等于论文被验证；本次没有实验复现或生产性能认证。

## 2. 来源覆盖

检查在2026-09-30北京时间09:00后进行，覆盖始终固定于上述窗口，实际首次检查及后续定点恢复截至本次检查时间。以下按每日来源顺序；没有常规扫描每周来源。原始阶段停点及审阅定位见[本日来源材料](../_sources/daily-20260930/PROGRESS.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)最新日期向旧项停止；09/29 GPT-6.1 Sol文章/card定点取正文；[RSS](https://openai.com/news/rss.xml)恢复返回403 | 受阻 | Sep29只有日期/时区不明，不能确定落窗；G1 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)最新两篇09/29；survey按范围关闭，GLM cyber原文已读核心说明，定点元数据恢复失败 | 受阻 | cyber文章日期只有Sep29，时区/时刻不足；G2 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)最新所见Sep1，止于窗前；[Google Research](https://research.google/pubs/)首15/11563目录按年/题名，含2027to-appear；09/29 Diffusion Controller blog链接2603.06981v1旧正文 | 受阻 | 年份不是首次公开时钟；没有逐读50篇旧论文；目录新事件日期G3 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空内容；[Blog](https://ai.meta.com/blog/)最新所见07/27，链接publication定点恢复超时 | 受阻 | 空目录不证明零命中，G4 |
| SRC-QWEN | [官方blog](https://qwen.ai/blog)动态空响应，浏览器30秒超时；辅助官方检索仅得09/18旧LiveTranslate | 受阻 | 搜索旧项不能替代完整动态目录，G5 |
| SRC-DEEPSEEK | [官方入口](https://www.deepseek.com/)所见最新V4.1 Flash 09/10，止于窗前 | 已检查 | 本次可见入口未发现本窗相关披露；不保证全网零遗漏 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)可见最新2025/11；[GitHub org](https://github.com/MoonshotAI)10/42只作项目发现，updated不当release；[kimi-code release API](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=3)最新三项09/24、09/23、09/19均窗外，停止 | 已检查 | 不以commit更新重启无关代码审阅；只覆盖列明入口 |
| SRC-TENCENT-HUNYUAN | [Research全部列表](https://hunyuan.tencent.com/research)两次HTTP恢复及浏览器30秒超时；[官方org](https://github.com/Tencent-Hunyuan)替代查项目不能还原全部目录 | 受阻 | “全部”列表本窗材料/日期G6 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)最新08/26→08/14→2025，有序止于窗前 | 已检查 | 本次可见目录未发现本窗项 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)第1/13页20项08/18→05/14，止于窗前；SeedRealtime作者Blog正文日期恢复为08/05，非本窗新项 | 已检查 | 不用后续索引日重评分旧全文 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)第1/2页最新05/09→2025/11，止于窗前 | 已检查 | 本次可见入口未见本窗项 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/)Papers最新06/29 MOPD，止于窗前；Blogs15个undated按钮无href，原HTML未得对应技术正文链接 | 受阻 | Blog身份/公开日期G7；Papers与Blogs分开，不宣称全站零命中 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)最新08/13→07/31→06/09，止于窗前 | 已检查 | 范围是列明技术入口，不宣称全网穷尽 |
| SRC-ARXIV | [cs.CL/new](https://arxiv.org/list/cs.CL/new?show=2000)页头09/30：326项=145new+83cross+98replacement；[cs.DC/new](https://arxiv.org/list/cs.DC/new)36=15new+9cross+12replacement。CL145new与DC24new/cross题名有界浏览；LG/AI/CV/RO/AR/PL/OS/PF/IR/MA按主线题名补检，API首80/187（submitted范围仅发现，不定归属），保留项逐一官方公告定位 | 已检查 | 原始列表/检索不等全量摘要队列；Environment Steering的更早正文线索不能唯一核日期，G8。没有把replacement数称新增论文数 |

arXiv主题查询为 `ti:"language model" OR ti:LLM OR ti:MoE OR ti:"world model" OR ti:VLA OR ti:"KV cache" OR ti:pretraining OR ti:transformer`，`submittedDate:[202609281800 TO 202609291800]`，start=0/max_results=80；早期四个主题query各max40只作补检线索，不宣称其余结果全关闭。搜索不能支持技术结论，采用依据均回到原文。

## 3. 候选与判断

下列“09/30公告08:00推定”指[官方本期new/cross列表](https://arxiv.org/list/cs.CL/new?show=2000)及[availability日程](https://info.arxiv.org/help/availability.html)对应的 `2026-09-30T08:00:00+08:00`，并非实际秒级观测或全网首发保证。官方Submitted字段为提交UTC原值，不替代公开。各家族身份和提交原值保留于下列证据笔记；更早作者正文会优先校正。SYNTH单列本期新增证据事件，旧机制不重评。当前官方事件页未见撤回信号，不为此遍历全部版本史。

三维评分顺序：Design Delta + System Reach + Durability。5～6分的实际整合项因§4列出的具体机制缺口/设计修正补足深入审阅，未升分来配合Books。最多三条演进摘要不限制逐项审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention — 2609.35794v1](https://arxiv.org/html/2609.35794v1) | 2026-09-30T08:00:00+08:00 | 检索缺证据与存在证据却受干扰需要不同补救；生成前gate提供条件性路由。 2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [When Successful Memories Mislead Embodied Agents: Memory Adaption For Task-Conditioned Execution — 2609.35808v1](https://arxiv.org/html/2609.35808v1) | 2026-09-30T08:00:00+08:00 | 成功轨迹的旧动作schema仍能误导；将接口兼容收益与压缩收益分开。 3+1+2=6 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1) | 2026-09-30T08:00:00+08:00 | 高judge agreement不保证区间/检验校准；人工配对抽样和估计不确定性改变发布判断。 3+2+3=8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Less Uniform Discrete Diffusion is More Powerful and Scalable — 2609.35817v1](https://arxiv.org/html/2609.35817v1) | 2026-09-30T08:00:00+08:00 | uniform reverse目标的平滑与corruption身份耦合；清洁目标和per-token time改变训练解释。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1) | 2026-09-30T08:00:00+08:00 | 修正错误与引入新错必须分账，revision前gate和后验acceptance预算不同。 2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-REFLECTION` / [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models — 2609.35860v1](https://arxiv.org/html/2609.35860v1) | 2026-09-30T08:00:00+08:00 | 用同一统计量定义难组再测detectability会自造gap；冻结partition后须换signal检验。 3+1+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Mnemon: Raw Records, Fast Judgments, Slow Thoughts — 2609.36059v1](https://arxiv.org/html/2609.36059v1) | 2026-09-30T08:00:00+08:00 | raw authority已覆盖；新增判定器替换条件及waves、总判断、lifecycle cost的不同预算。 2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning — 2609.36178v1](https://arxiv.org/html/2609.36178v1) | 2026-09-30T08:00:00+08:00 | judge选址不等数值credit；恢复两端状态，用固定current policy续跑估局部贡献。 2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Learning from Teacher Continuations at Student States — 2609.36246v1](https://arxiv.org/html/2609.36246v1) | 2026-09-30T08:00:00+08:00 | teacher文本continuation免logit接口，但其后续状态及CE监督边界不同于逐token纠错。 2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Reliable Parallel Decoding in Masked Diffusion Language Models — 2609.36452v1](https://arxiv.org/html/2609.36452v1) | 2026-09-30T08:00:00+08:00 | 同pass高confidence不足以joint commit；final-layer稳定性与未解决上游熵约束承诺集合。 2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching — 2609.36522v1](https://arxiv.org/html/2609.36522v1) | 2026-09-30T08:00:00+08:00 | 并行迭代反复访问同timestep可缓存输出，但命中检查及通信可能吃掉NFE收益。 2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SEED: Self-Speculative Decoding via Implicit Encoder-Decoder — 2609.36590v1](https://arxiv.org/html/2609.36590v1) | 2026-09-30T08:00:00+08:00 | verifier刷新deep KV，再由薄末层读raw embedding起草，形成自推测的另一条件分支。 2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference — 2609.36654v1](https://arxiv.org/html/2609.36654v1) | 2026-09-30T08:00:00+08:00 | 未来列可补偿时当前误差应条件化；scale候选需私有回放真实顺序量化轨迹。 2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1) | 2026-09-30T08:00:00+08:00 | 独立artifact KV丢跨artifact条件；冻结cache producer并训练query consumer，不将位置修复当充分条件。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators — 2609.36899v1](https://arxiv.org/html/2609.36899v1) | 2026-09-30T08:00:00+08:00 | 暂停长轨迹可改善resident组成；depart/destination分离改变异构rollout调度。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation — 2609.36903v1](https://arxiv.org/html/2609.36903v1) | 2026-09-30T08:00:00+08:00 | 长多方双语评价及固定架构data对照限制由短dyadic效果外推的能力判断。 2+2+2=6 | 标准完成 | 仅报告：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；新增证据不改长期机制，旧机制不重评 |
| [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation — 2609.36931v1](https://arxiv.org/html/2609.36931v1) | 2026-09-30T08:00:00+08:00 | system date是确定性输入干预，隐藏默认值可改变比较而非随机采样噪声。 2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage — 2609.36938v1](https://arxiv.org/html/2609.36938v1) | 2026-09-30T08:00:00+08:00 | 预测层间selector可预取，但target native selector及缺失补读仍决定Attention可见状态。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models — 2609.36952v1](https://arxiv.org/html/2609.36952v1) | 2026-09-30T08:00:00+08:00 | 匹配compute/token/current-batch对照仍显示历史内容作用；初筛关闭理由因此被独立反证。 2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Purlin: Separating Orchestration from the Datapath of Collectives — 2609.36954v1](https://arxiv.org/html/2609.36954v1) | 2026-09-30T08:00:00+08:00 | layout/copy-reduce语义和coordination可复用，但hardware datapath及数值policy不等价。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Cobalt: Leveraging Expert Co-activation for Efficient Distributed MoE Training — 2609.36959v1](https://arxiv.org/html/2609.36959v1) | 2026-09-30T08:00:00+08:00 | 单token多expert的destination-node union不同于各expert负载和，改变布局目标。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Learning from Think-Mode Advantage via On-Policy Distillation — 2609.37044v1](https://arxiv.org/html/2609.37044v1) | 2026-09-30T08:00:00+08:00 | teacher优势与trace对兄弟response的可转移性分离，用group路由权重而非一律强模仿。 2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains — 2609.37062v1](https://arxiv.org/html/2609.37062v1) | 2026-09-30T08:00:00+08:00 | 内部skip仍需本层KV投影和route元数据；policy省层不自动成为引擎收益。 3+2+2=7 | 深入完成 | 整合：`INFER-SGLANG` / [Ch51](../../../../books/part-05-inference-system/51-sglang.md) |
| [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents — 2609.37196v1](https://arxiv.org/html/2609.37196v1) | 2026-09-30T08:00:00+08:00 | capability shape grant与当前具体值provenance分离；缓存授权不能缓存证据真值。 3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Compiling Learning Problems into Adaptation Programs for Language Models — 2609.37371v1](https://arxiv.org/html/2609.37371v1) | 2026-09-30T08:00:00+08:00 | episode geometry可摊销选择adaptation program；未知family仍需default与适配成本预算。 2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling — 2609.37494v1](https://arxiv.org/html/2609.37494v1) | 2026-09-30T08:00:00+08:00 | 共享答案池把单题分类变耦合assignment；chance和干扰控制变化须与原任务分开。 2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification — 2609.37532v1](https://arxiv.org/html/2609.37532v1) | 2026-09-30T08:00:00+08:00 | 保完整草稿而限ragged verification共享预算；图固定地址不意味着commit边界固定。 2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models — 2609.37533v1](https://arxiv.org/html/2609.37533v1) | 2026-09-30T08:00:00+08:00 | 离散router latent可让parallel reverse采样相关；clean/noisy router匹配决定训练推理接口。 2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision — 2609.37624v1](https://arxiv.org/html/2609.37624v1) | 2026-09-30T08:00:00+08:00 | 删除坏监督移除该输入的训练机会，纠正则尝试供正面目标；两种intervention不可混同。 2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving — 2609.37626v1](https://arxiv.org/html/2609.37626v1) | 2026-09-30T08:00:00+08:00 | projection/KV ownership解耦后，live-layout切换需稳态+暂态容量及共同handoff。 3+2+2=7 | 深入完成 | 整合：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Honeycomb: Constant-Size Scene Memory Representation for Video World Models — 2609.37690v1](https://arxiv.org/html/2609.37690v1) | 2026-09-30T08:00:00+08:00 | 固定planes在expanding bounds下warp/coarsen；存储恒定不等信息精度恒定。 2+2+3=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs — 2609.37852v1](https://arxiv.org/html/2609.37852v1) | 2026-09-30T08:00:00+08:00 | 量化dP使saved delta失配，重算匹配contraction恢复softmax梯度零行和。 3+2+3=8 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Retrieval Capacity of Self-Attention Under Competition — 2609.37879v1](https://arxiv.org/html/2609.37879v1) | 2026-09-30T08:00:00+08:00 | 权重不等独立知识贡献；V方向及delete/renormalize不同干预改变诊断解释。 2+1+3=6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs — 2609.37891v1](https://arxiv.org/html/2609.37891v1) | 2026-09-30T08:00:00+08:00 | 旧synthetic pipeline不重算；本窗同600M/data trace ablation和seed外反证限制效率归因。 2+1+2=5 | 标准完成 | 仅报告：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；新增证据不改长期机制，旧机制不重评 |
| [Scaling Zero-Order Pretraining through Model Sharding — 2609.37899v1](https://arxiv.org/html/2609.37899v1) | 2026-09-30T08:00:00+08:00 | 可分目标移除跨expert SPSA噪声，以表征耦合换独立更新，非通用通信分片。 2+2+3=7 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Learning What to Remember: Long-horizon Counterfactual Memory Optimization — 2609.37930v1](https://arxiv.org/html/2609.37930v1) | 2026-09-30T08:00:00+08:00 | rewrite总效用含继承收益；相邻状态对同future targets的增量才接近本次write credit。 2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [How Local Mixing Encodes Relative Position in Global NoPE Attention — 2609.38109v1](https://arxiv.org/html/2609.38109v1) | 2026-09-30T08:00:00+08:00 | 局部mixing及Q/K对齐能读implicit recency，修正必须显式PE的绝对句。 2+1+3=6 | 深入完成 | 整合：`MODEL-POSITION-ENCODING` / [Ch13](../../../../books/part-02-model/13-position-encoding.md) |
| [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms — 2609.38121v1](https://arxiv.org/html/2609.38121v1) | 2026-09-30T08:00:00+08:00 | K/query与V/output需要不同consumer metric，post-RoPE变换折叠及在线代价不同。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [HelixWorld: A Real-time Interactive Audio-Visual World Model — 2609.38123v1](https://arxiv.org/html/2609.38123v1) | 2026-09-30T08:00:00+08:00 | camera/world state联合条件视听，在student自身轨迹纠偏streaming而非只换音轨。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation — 2609.38142v1](https://arxiv.org/html/2609.38142v1) | 2026-09-30T08:00:00+08:00 | advisor对recorded response的预测敏感性可选择监督，但不是executor反事实因果。 2+2+3=7 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Rho: A Foundation for Efficiently Adaptable VLA Models — 2609.38164v1](https://arxiv.org/html/2609.38164v1) | 2026-09-30T08:00:00+08:00 | embodiment midtraining→任务更新→冻结action generator的latent repair分开适配authority。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization — 2609.38169v1](https://arxiv.org/html/2609.38169v1) | 2026-09-30T08:00:00+08:00 | state误差随transition传播；readout时序与temporal/spatial敏感度影响量化生命周期。 2+2+3=7 | 深入完成 | 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |

## 4. 证据与知识整合

精确版本均为表中的v1；HTML优先，Self-Correction与ATTUNER采用同版PDF，Mnemon读取无版本HTML并确认页头v1。以下逐项定位采用命题、关键对照/限制和实际正文，不以“已吸收语义增量”替代细节。未复现实验、未审全部artifact；性能结论只限作者配置，具体配置与未披露字段在关联笔记，不将算子/孤立计时当serving SLO。

### [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention — 2609.35794v1](https://arxiv.org/html/2609.35794v1)

生成前区分 distraction/missing 的 gate 段；离线标签依赖 reference/NLI，主噪声模拟、专家域仍需校准；classifier不是证据真值，更保守拒答会牺牲coverage。 最终整合位置：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [When Successful Memories Mislead Embodied Agents: Memory Adaption For Task-Conditioned Execution — 2609.35808v1](https://arxiv.org/html/2609.35808v1)

lossless source/derived memory 段补历史action normalization。§3–4因子对照：冻结exact-match map，未匹配不猜；紧凑表示并非总优于normalized全文，fresh规划保留full fallback。 最终整合位置：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1)

Judge Ranking后补统计推断合同。§2–6/9.6/B1要求MCAR同item人工配对，λ估计/收缩付power代价；小样本bootstrap CI警告不等禁止所有resampling，模拟不证明所有tool接口有效。 最终整合位置：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [Less Uniform Discrete Diffusion is More Powerful and Scalable — 2609.35817v1](https://arxiv.org/html/2609.35817v1)

生成objective段补目标/条件身份。§3–4/ablation只支持特定初始化、mask及训练配置；per-token时间不是corruption oracle，token/step不是latency；大UDLM从零预训练未验证。 最终整合位置：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1)

已有覆盖：正文已推导(1−A)ECR−A EIR，并区分verify-first与预算。PDF§3–4/6读29模型三数据集；仅两组GSM8K初答/修订文件可回溯，gate汇总缺对应paired records、冻结配置和不相交IDs，收益只作descriptive，不写成验证过的无偏优势。 最终已有覆盖位置：`AGENT-REFLECTION` / [Ch80](../../../../books/part-07-agent/80-reflection.md)。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models — 2609.35860v1](https://arxiv.org/html/2609.35860v1)

高共识错误段补非循环证据阶梯。§2–7分组是operational不是latent真理；换signal仍共享响应；单轨迹diffusion检测只在LLaDA三任务/Dream PopQA显著，困难组不是不可检测。 最终整合位置：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Mnemon: Raw Records, Fast Judgments, Slow Thoughts — 2609.36059v1](https://arxiv.org/html/2609.36059v1)

lossless/lazy段补decision/rank contract及成本边界。§4–7单调替换还须固定阈值；少量answer context可能以广扫描换来，ECI不含read/write，历史增长仍增搜索；不同grader榜单不合并。 最终整合位置：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning — 2609.36178v1](https://arxiv.org/html/2609.36178v1)

语义Segment段中旧milestone限制之后。§3–5无偏解释有确定段执行/无中间reward/gamma1前提；positive-only bonus不继承训练无偏，续跑不进训练batch、额外时间与不可回滚fallback保留。 最终整合位置：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Learning from Teacher Continuations at Student States — 2609.36246v1](https://arxiv.org/html/2609.36246v1)

Teacher Text Continuation段。§2–5只在student新prefix后采teacher自身suffix，student/env内容mask出loss；跨tokenizer靠文本；滞后/不可恢复prefix及teacher成本保留，top16 KL不是exact对照。 最终整合位置：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [Reliable Parallel Decoding in Masked Diffusion Language Models — 2609.36452v1](https://arxiv.org/html/2609.36452v1)

并行承诺段补同pass跨层稳定/entropy budget。§2–4不是跨denoising-step收敛，也不证明joint correctness；空集fallback保活性，full/block质量吞吐条件不同，NFE少可能更慢。 最终整合位置：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching — 2609.36522v1](https://arxiv.org/html/2609.36522v1)

跨迭代同Timestep近似cache独立段。§2–4/Algo1–2缓存(xhat,epshat)，τcache≠solverτ，状态不同使轨迹近似；SD1.5 matched 8GPU对照与1vs8资源比较分开，小τ少NFE仍更慢。 最终整合位置：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [SEED: Self-Speculative Decoding via Implicit Encoder-Decoder — 2609.36590v1](https://arxiv.org/html/2609.36590v1)

MTP/full-target段后。§4–5不新增独立cross-attention，联合训练后target才是verifier authority，非原checkpoint分布保证；task-specific SFT/greedy单卡不能外推生产goodput，空代码库不称复现。 最终整合位置：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference — 2609.36654v1](https://arxiv.org/html/2609.36654v1)

未来补偿与舍入代价段。§4/Eq12–14/§5/AppendixD：Schur连续松弛不是离散全局最优；候选同起点独立回放，winner才commit；15,461题七任务限定W4A4结果，搜索更宽不总更好。 最终整合位置：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1)

固定Producer/适配Consumer段。PDF§3–5/D/E只训query LoRA，artifact KV不变但online hidden/KV变化；warm TTFT不含离线构造，跨域可退步，oracle只是条件性诊断不是values无误差证明。 最终整合位置：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators — 2609.36899v1](https://arxiv.org/html/2609.36899v1)

rollout/version段补resident/pending pools。§4–6迁移保policy identity，兼容才KV fan-in否则re-prefill；in-flight credit不硬限轨迹年龄，硬件affinity与迁移/吞吐-tail成本保留。 最终整合位置：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation — 2609.36903v1](https://arxiv.org/html/2609.36903v1)

仅报告：新贡献主要是长场景/数据控制证据，既有全双工表示和评价边界可承载，不新增通用机制。§2–3多数训练小时为synthetic非真实；混合非target speakers不等逐人建模，协议结果不证明任意长会话。 最终仅报告位置：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation — 2609.36931v1](https://arxiv.org/html/2609.36931v1)

已有覆盖：run identity、完整system prompt、cohort/render及resolved-model receipt已有具体要求。§3–4九模型六数据集控制日期（§5.5仅precision/batch受限对照）；proprietary一周调用仍有漂移，不能声称所有日期效应总大于其他因素。 最终已有覆盖位置：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage — 2609.36938v1](https://arxiv.org/html/2609.36938v1)

KV demand paging后补Janus分支。§4–5早层预测仅优化物理访问，target selector精确barrier不变；8H200/受限DRAM/低到达率trace支持条件收益，写packing需CPU，排队和读写积压仍在。 最终整合位置：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models — 2609.36952v1](https://arxiv.org/html/2609.36952v1)

已有覆盖：latent alignment不替代heldout行为、acquisition/retention连续checkpoint、replay配方与双域holdout三段实际存在。§2–5当前模型重算旧raw views；五seed局部控制不能外推任意模型，推理移除路径不等训练免费。 最终已有覆盖位置：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [Purlin: Separating Orchestration from the Datapath of Collectives — 2609.36954v1](https://arxiv.org/html/2609.36954v1)

一侧通信后补语义/协调/数据面分层。§3–5 ready与consumer ACK分离，兼容layout才composition；确定rank reduction与opt-in switch不是同保证，单节点结果/扩展方案及反输配置保留。 最终整合位置：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [Cobalt: Leveraging Expert Co-activation for Efficient Distributed MoE Training — 2609.36959v1](https://arxiv.org/html/2609.36959v1)

replica分支补co-activation/capacity联合目标。§3–4保router top-k，EMA是surrogate；global重排暂停/副本梯度同步有成本，traffic不含全部通信，指数节点cover复杂度不能外推大EP节点数。 最终整合位置：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [Learning from Think-Mode Advantage via On-Policy Distillation — 2609.37044v1](https://arxiv.org/html/2609.37044v1)

Teacher Think Advantage段。§3–4/干预共享bank/rollout控制支持局部路由；TRD是compatibility proxy非真实推理因果，stop-gradient response权重不改token KL，trace生成与滞后不免费。 最终整合位置：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains — 2609.37062v1](https://arxiv.org/html/2609.37062v1)

piecewise graph后补RUN/ProjectOnly行带。§3–4当前cohort maps/graph兼容，至多一次dense→routed promotion；matched长度不等自然停止，always-route可变慢，checkpoint本身质量损失不由engine抹去。 最终整合位置：`INFER-SGLANG` / [Ch51](../../../../books/part-05-inference-system/51-sglang.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents — 2609.37196v1](https://arxiv.org/html/2609.37196v1)

Permission Graph/deterministic authorizer后。§3–4前置blueprint+monitor再核当前绑定，tracing启发式/judge非安全oracle；合法候选内恶意选择仍可通过，保留utility损失/误拒与人工升级。 最终整合位置：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Compiling Learning Problems into Adaptation Programs for Language Models — 2609.37371v1](https://arxiv.org/html/2609.37371v1)

Episode Geometry段。§4/AppendixG.1早中晚指depth区域rank16，full-stack指全层rank4 LoRA，非训练阶段/full-rank；训练selector与未知任务失配不免费，保固定LoRA分支。 最终整合位置：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling — 2609.37494v1](https://arxiv.org/html/2609.37494v1)

MCQ接口后补coupled diagnostic。§3–5要求每题唯一有效且各题gold不共用pool option；同大小无关池控制部分混杂但长context仍在，joint chance不是原k^-N，不将新排行冒充原benchmark真值。 最终整合位置：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification — 2609.37532v1](https://arxiv.org/html/2609.37532v1)

Verify Length后补固定图ragged metadata。§III–IV token/position/KV/acceptance同边界，predictor需训练、target verifier仍authority；对照backend不同，预算保留与重分配混合，不声称本轮认证全部分布证明。 最终整合位置：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models — 2609.37533v1](https://arxiv.org/html/2609.37533v1)

非factorized reverse分支。方法/对照只支持该route mixture条件，不把借用MoE称新通用expert runtime；不认证所有渐近定理或宣称diffusion替代AR，保fallback和路由成本。 最终整合位置：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision — 2609.37624v1](https://arxiv.org/html/2609.37624v1)

删除→纠正监督段。§3–5 paired raw/delete/rewrite/paraphrase/clean canary，nested poison/LoRA三seed；EM以coherent输出为分母，对照不全显著，不将inconclusive当等效或声称纠正普遍更安全。 最终整合位置：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving — 2609.37626v1](https://arxiv.org/html/2609.37626v1)

batch phase switch后补manifest差集及hysteresis。§3–5跨rank boundary/下一层迁移覆盖；DOP非总优，切换比例分母是特定prefill而非decode，目标内存不可行就拒绝切换。 最终整合位置：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)。

### [Honeycomb: Constant-Size Scene Memory Representation for Video World Models — 2609.37690v1](https://arxiv.org/html/2609.37690v1)

persistent world state固定planes段。§3–4只更新最新chunk，feature storage不是系统总内存；pose/depth误差和空间时间分辨率下降保留，revisit指标不证明物理世界状态。 最终整合位置：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs — 2609.37852v1](https://arxiv.org/html/2609.37852v1)

attention backward不变量段。§3–4/Eq2/4需归一P/相同V等条件；恢复的是再量化前FP32不变量，不消除全部FP8误差/保证optimizer收敛，kernel时间不等全训练。 最终整合位置：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Retrieval Capacity of Self-Attention Under Competition — 2609.37879v1](https://arxiv.org/html/2609.37879v1)

路由权重不等独立知识贡献段。§2–4保原weights比较相对NLL，删除与renorm有不同误差；先dense后筛不证明加速，有限上下文capacity不是存储事实数。 最终整合位置：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs — 2609.37891v1](https://arxiv.org/html/2609.37891v1)

仅报告：2025-11-10/2026-04-29作者正文已公开主机制。本期§4.2/5.1新增同架构tokenizer预算对照，保数据形状/知识覆盖/总成本分账；不足以改现有数据/训练结论，不新增项目简介。 最终仅报告位置：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [Scaling Zero-Order Pretraining through Model Sharding — 2609.37899v1](https://arxiv.org/html/2609.37899v1)

零阶更新后补separability分支。§3–9/Eq3–4理论限固定C3可分loss等假设，byte-LSTM matched controls支持局部；shared decoder含exact delta-rule，未验证大型Transformer，不称全模型纯ZO。 最终整合位置：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Learning What to Remember: Long-horizon Counterfactual Memory Optimization — 2609.37930v1](https://arxiv.org/html/2609.37930v1)

Memory Rewrite总效用/新增贡献段。方法中potential/control-variate关系限定估计；未来查询采样、重复评估成本与proxy泄漏仍需控制，不把后续总reward直接归当前更新。 最终整合位置：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)。

### [How Local Mixing Encodes Relative Position in Global NoPE Attention — 2609.38109v1](https://arxiv.org/html/2609.38109v1)

开篇绝对句及mask/implicit位置段。§III–VI/A的lag moment依赖投影alignment，零均值独立Q/K不自动产生期望recency；有限120M/350M实验不保证无限长，保RoPE/ALiBi可控性。 最终整合位置：`MODEL-POSITION-ENCODING` / [Ch13](../../../../books/part-02-model/13-position-encoding.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

### [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms — 2609.38121v1](https://arxiv.org/html/2609.38121v1)

transform/bit-allocation后。§4–5/AppD QuEST条件证明不直接覆盖实际affine quantizer，local L2不预测decode质量，长context可退步；无生产吞吐/SLO不写2-bit无损加速。 最终整合位置：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [HelixWorld: A Real-time Interactive Audio-Visual World Model — 2609.38123v1](https://arxiv.org/html/2609.38123v1)

可控camera model后补联合视听与student-state蒸馏。§2–5/D.7空间声cue非完整声学物理，RTF非first-response/concurrency SLO；未全项胜teacher，不称普遍drift-free。 最终整合位置：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation — 2609.38142v1](https://arxiv.org/html/2609.38142v1)

Advice预测敏感性段。§4–7/E只在reflection gate后加self-distillation，原GRPO advantage保留；matched-count控制不等同batch因果干预，changing-teacher收敛未证，跨executor可弱于专训。 最终整合位置：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [Rho: A Foundation for Efficiently Adaptable VLA Models — 2609.38164v1](https://arxiv.org/html/2609.38164v1)

多源对齐后midtraining/latent repair段。§6–7冻结backbone/generator只学latent initialization，已知难配置少纠正不证明任意机器人OOD；FlowDAgger为复用非首创，支持域限制保留。 最终整合位置：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)。

### [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization — 2609.38169v1](https://arxiv.org/html/2609.38169v1)

减少Bytes/recurrent state段。§2–5/F/H仅相同inputs/gates下误差递推，本步浮点readout先于packed writeback；codes/scales/pivots共同ready，4bit退化与双缓冲代价保留，update速度非tokens/s。 最终整合位置：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。实际正文已有对应source-family，位于主Review notes之前；旧方案/失效条件未被替换。 [必要原文位置、评价条件与反证](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

## 5. 缺口与下一步

普通可执行工作：无。正式报告最终独立复核及机器校验已完成。以下G1～G8为**本窗终态保留项**，不进入42个候选，不评分，不用于正面证据、Books或无遗漏断言，不支持覆盖通过。本次已定点尝试官方入口/动态浏览或同材料替代；材料到达后按下表条件定点重开对应事件，不扩到其他日期或整月。

| 身份/入口 | 缺少材料、必要性与当前边界 | 可接受替代与定点重开 |
| --- | --- | --- |
| G1 [GPT-6.1 Sol原文](https://openai.com/index/introducing-gpt-6-1-sol/) / [safety card](https://deploymentsafety.openai.com/gpt-6-1-sol) | Sep29原始published字段含时区/时刻；仅日期与窗口部分相交，不能先采用 | 官方RSS条目、含datePublished/时区的HTML或官方精确发布记录；确认落窗才做贡献/必要机制审阅 |
| G2 [GLM-5.3 cyber原文](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) | 原始09/29时间/时区；正文已可读但不能冒称本窗新事件 | 作者feed、meta发布时间或官方带时区记录；只恢复本事件准入，不重新扫survey |
| G3 [Google Research publications](https://research.google/pubs/) | 可定位本窗first-public的新事件列表；排序year/to-appear不提供公开时钟 | 官方dated research feed、单篇精确body发布时间/作者原始链接；只筛已定位的本窗主线项 |
| G4 [Meta Research](https://ai.meta.com/research/) | Research可读目录及本窗日期；空响应不能证明零项 | 官方research export/feed或本窗原文列表；只恢复该入口/窗口 |
| G5 [Qwen Blog](https://qwen.ai/blog) | 动态技术列表的本窗条目与日期；搜索到旧页不证明目录完整 | 可保存HTML/官方feed/带日期原文链接；只恢复本窗，不遍历旧论文 |
| G6 [Hunyuan Research全部](https://hunyuan.tencent.com/research) | 可读“全部”列表及本窗条目；GitHub替代不等于目录闭合 | 页面导出/官方列表数据或本窗具体原文链接；只核本窗身份/日期/贡献 |
| G7 [MiMo Blogs](https://mimo.xiaomi.com/) | 15个无日期按钮对应原文身份与发布时间 | 官方Blog列表导出或具体原文及带时区发布时间；不重审窗前Papers |
| G8 [Environment Steering 2609.35807v1](https://arxiv.org/abs/2609.35807v1) | 早期NOVAS展示线索未能证明全文首公开；不能断言旧事件也不能采用本日 | 作者原始全文/精确OpenReview ID及首次公开记录；仅恢复该family日期再决定准入，不能用摘要/展示日替代正文日期 |

窗外恢复线索不属于本窗：MoK [作者全文08/04](https://cursor.com/blog/mixture-of-kittens)已有同机制/结果；Alignment Forecasting [四作者09/25正文](https://www.lesswrong.com/posts/f7r9QCmjoYFG9ReyF/alignment-forecasting-predicting-misalignment-from-training)早于本窗（未披露时区，不补造精确owner时刻）；Google Diffusion Controller链接[2603.06981v1](https://arxiv.org/abs/2603.06981v1)为旧正文；SeedRealtime作者正文08/05已恢复。都未重新计本日分数或改其他Daily。prompt-perturbation Springer正文first-online2025/06/24，不能把会议/后收录当本期新研究。

## 6. 复核

复核者：`sep30_independent`、`sep30_evidence_check`、`sep30_complement_review`（相对Daily作者root）；Books写入者和复核者分离，root对三代理写的27项作非作者实际写后验收，root写的10项由代理分工实际验收。
结论：通过

正式报告最终非作者核查已完成；八项外部保留不签Coverage/Evidence通过，不妨碍本窗安全终态。

已执行：全部42候选的日期/具体准入与限定证据分批非作者审阅，37项实际Books写后及前后衔接分别非作者复核；5项标准候选对照具体正文或新证据。否定侧按来源/理由定点抽检MoK、Alignment、Environment、范围外invoice OCR、generic WQG-ADMM/Byzantine以及ER-JEPA误关闭，后者恢复matched-budget反证并重开；未声称全部宽列表逐摘要排除审核。纠正了NoPE绝对句、compiler层区域/LoRA rank身份、ProVer插入后旧指代、AnswerPool不同题gold唯一前提、Schur题数，以及NFE/算子速度对端到端收益的外推。

独立记录：[准入/基础设施及root三项](../_sources/daily-20260930/INDEPENDENT_ADMISSION_CALIBRATION.md)、[证据与root两项](../_sources/daily-20260930/INDEPENDENT_EVIDENCE_CHECK.md)、[主题补检/root其他项](../_sources/daily-20260930/INDEPENDENT_COMPLEMENT_REVIEW.md)、[root对27项非作者写后与根证据](../_sources/daily-20260930/ROOT_EVIDENCE_NOTES.md)。

机械校验：本正式报告V3字段/日期/评分校验通过；42表项与42证据标题一一对应，Stable Node/路径可由ROADMAP解析，本地链接和Markdown围栏检查通过，37实际机制均在各章主Review notes之前。未暂存`git diff --check`通过。运行前已有约1206行git状态且大量暂存内容，保留；本次未stage/commit/push。已有cached whitespace告警位于其他April/Sep22/Sep25/tasks文件，不以修本日为名覆盖。本日星期三，无Weekly；日常流程结束后仅继续Learning State指向的04/23单篇独立历史checkpoint，其结果不改变本日候选或日期。
