# Daily Research — 2026-09-24

**规范：** V3
**窗口：** 2026-09-23T09:00:00+08:00 ～ 2026-09-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-24T19:29:44+08:00

## 1. 结论

本窗不应把旧论文的修订或次日才公告的论文搬进来。已定点审阅多条改变系统设计边界的路线：KV 容量风险与工作集估计、PD 弹性容量、训练恢复、推测解码关键路径、评价题目有效性、具身状态，以及 Agent Context/Tool 的证据门。对应长期增量已写入各自 Books owner；不是把所有 arXiv 相关论文都入选。Google DeepMind 的持久云端记忆只取得厂商博客，尚缺技术白皮书，不把安全保证写入 Books。已补齐本窗 arXiv 主题查询、官方 New 停止点与跨类去重；剩余来源限制按 §5 隔离，独立语义验收的实际范围见 §6。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 News RSS](https://openai.com/news/rss.xml) 按倒序读到 09-23 00:00 UTC 窗外停止点；窗内八条含 Academy、商业案例、政策发言及 MentalHealthBench；[Research](https://openai.com/research/index/) 亦已检查 | 已检查 | 八条未见改变本项目长期机制的研究，MentalHealthBench 是特定临床沟通评价，不扩成通用 LLM 系统证据 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 顶部 09-23 生命科学公告与次项 09-17；Publication 列表首项 09-17 | 已检查 | 生命科学发现/实验室公告在本项目当前暂缓的 AI for Science 范围，未见本窗项目范围新研究；不为排除项追索小时级日期 |
| SRC-GOOGLE-AI | [DeepMind News](https://deepmind.google/blog/) 的 [Private AI Compute 更新](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) HTML `datePublished=2026-09-23T16:00:57.674000+00:00`，即北京时间 09-24 00:00；[Google Research Blog](https://www.research.google/blog/) 日期倒序首项 09-18；[Publications](https://research.google/pubs/) 只给年份、不给可靠日时刻 | 受阻 | private memory technical brief PDF 未取得；Publications 无法以目录证明本窗零新增，仅作为隔离的覆盖限制，不能据此断言无遗漏 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 动态首页不可用；改查官方按日期倒序的 [results](https://ai.meta.com/results/)，最新 Publication 为 09-06 | 已检查 | 此停止点只覆盖官方 results 目录，不外推 Meta 全组织所有仓库无事件 |
| SRC-QWEN | 旧入口 [qwenlm.github.io](https://qwenlm.github.io/) 已跳转；[官方 Research 关联页面](https://qwen.ai/research/qwen3.8-livetranslate) 的 Latest Research 首项为 09-20，以下为 09-18；[Qwen3.8-Omni v1](https://arxiv.org/abs/2609.25611) 属前一日 arXiv 公告批次 | 已检查 | 本窗未在可读官方研究序列中见新增；窗外论文回拨真实归属日，不重复评分 |
| SRC-DEEPSEEK | [Research & News](https://www.deepseek.com/en/news/) News 首项 09-10，Research Index 首项 06-24 | 已检查 | 官方该序列未见本窗研究；不把普通仓库更新时间当论文发表 |
| SRC-MOONSHOT | [平台博客](https://platform.kimi.com/blog) 倒序首项 2025-11-07；未把仓库 `push` 时间当新研究事件 | 已检查 | 此结论限博客入口；若后续仓库出现有署名新报告或重要发布，定点核其真实首次公开日 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 页面超时后，官方 `publicList` 接口返回 9/9 条；新增同题博客《When Do Larger Batches Help Scale LLM Reinforcement Learning?》的 `publicAt=2026-09-23T16:05:28+08:00`，次项为 08-28 | 已检查 | 对应 [arXiv:2608.29296v1](https://arxiv.org/abs/2608.29296) 已于 08-29 提交；可核摘要的 batch/throughput/time-to-target 机制相同。博客正文此次不可访问，不能断言完全相同，也不凭延迟博客重复评分；只有发现独立新增机制才定点重开 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 可见时间排序，首项 08-26；官方 [模型发布说明](https://docs.z.ai/release-notes/new-released) 倒序首项亦为 08-26 | 受阻 | 发布说明可闭合，但 Research 动态页未建立可靠翻页终点；隔离其零新增断言，获可读列表/API 后定点重开 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) 博客首项 SeedRealtime 的[正文](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction) 标 08-05；[论文目录](https://seed.bytedance.com/en/public_papers) 按 newest→oldest 首项 08-18 | 已检查 | 可读官方博客和论文目录未见本窗新增 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/) 首项 05-09；[Publication](https://ernie.baidu.com/blog/zh/publication/) 仅列历史技术报告 | 已检查 | 官方两入口未见本窗新增；未对仓库普通 commit 做论文事件推断 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) Paper 首项 MOPD 标 06-29；Blog 列表有新产品/工程标题但不标发布日期 | 受阻 | Blog 没有可核时间停止点；不将其当本窗零新增，需可读文章日时刻或官方有序列表后定点恢复 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog) 与[中文](https://www.minimax.cn/blog) Research Blog 倒序首项均为 08-13 | 已检查 | 两站可读研究序列未见本窗新增 |
| SRC-ARXIV | 2026-09-24 [官方 New](https://arxiv.org/list/cs.CL/new) 的 `cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA` 十二类均读至 New 段结束，排除 Cross/Replacement；分别为 73/115/8/59/106/91/10/0/1/1/13/7，按 arXiv ID 去重后为 484 个原始身份，**不是候选数**。另用 [官方查询接口](https://export.arxiv.org/api/query) 在提交时间 09-22～09-24 UTC 的宽范围做四组主题补检：模型 `language model/LLM/Transformer/MoE`（CL/LG/AI）243；多模态 `multimodal/vision-language/world model/video generation/robot policy`（CV/RO/CL/LG）118；Infra `KV cache/GPU/distributed training/serving/checkpoint/kernel`（DC/AR/OS/PF/LG/CL）71；Agent/Eval `agent/tool/benchmark/evaluation/retrieval/memory`（AI/IR/MA/CL/RO）441。均 `start=0,max_results=500`，单页结果少于上限；提交时间只作召回，最终仍与 09-24 New 交叉，四组交集去重 295，不转成 295 篇摘要队列。对 New 身份按项目主题浏览标题，含糊/高疑似再读完整摘要；独立复核另定点读约 31 条（与先前题摘样本有重叠，不能直接相加）。34 个 arXiv 入选 ID 均在 New 且互异 | 已检查 | 主题词补检与标题浏览不是全学科无遗漏保证；尤其新命名、题目不显机制的论文可能漏掉。官方 New 而非 Submitted 字段决定本窗归属；通用 CXL 分层 [xTier](https://arxiv.org/abs/2609.27266) 题摘未涉及大模型状态/训练/推理合同，故不入候选 |

## 3. 候选与判断

本窗冻结 35 个经题摘贡献筛选的独立材料家族（34 个 arXiv New 论文、1 个官方博客）；484 个跨类去重后的 arXiv New 原始身份绝不是候选数。分数顺序为 Design Delta + System Reach + Durability；`标准完成` 不等于对所有正文逐页审计，`深入完成` 也不等于独立复现。Books 路径均为真实已写入或经对读后作出的决定，最终独立验收见 §6。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Google Private AI Compute server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) | 2026-09-24T00:00:57+08:00 | 无状态 enclave 到跨设备持久记忆的控制/密钥归属变化，需核可验证软件及威胁模型。2 + 3 + 3 = 8/9 | 受阻 | 暂缓：`PLATFORM-SECURITY` / `AGENT-MEMORY`，仅报告厂商披露架构，不将保证写入 Books |
| [KITE](https://arxiv.org/html/2609.27294v1) | 2026-09-24T08:00:00+08:00 | 将历史 KV 生产者与只读预测容量分开，避免所有新增层重复处理 prompt。2 + 3 + 3 = 8/9 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Frozen Flows Forget](https://arxiv.org/html/2609.28414v1) | 2026-09-24T08:00:00+08:00 | 稀疏 latent waypoint 可能保端点却丢中途运动，评价不能只看平均像素误差。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Counterfactual Memory Audit](https://arxiv.org/html/2609.27247v1) | 2026-09-24T08:00:00+08:00 | 区分机器人 policy 对记忆敏感与按真实历史选对动作。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [InternW0](https://arxiv.org/html/2609.27656v1) | 2026-09-24T08:00:00+08:00 | 双频视频预测/动作控制的共享表示与 contact feedback 组合，须区分 fast-path latency 与端到端闭环。2 + 2 + 2 = 6/9 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已解释双速预测/控制、版本化 KV 与过期回退；该文的 routing 沿用 AHA-WAM，不重复写成新机制 |
| [ProCredit](https://arxiv.org/html/2609.27532v1) | 2026-09-24T08:00:00+08:00 | 用可验中间进度对 RL 轨迹作 turn-level credit，而非只依赖终局 reward。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [SPAR](https://arxiv.org/html/2609.27925v1) | 2026-09-24T08:00:00+08:00 | 对局部已充分预测的 token 加远前缀扰动不变性，保留真正远程证据的训练信号。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Marginally Correct Tool Caches](https://arxiv.org/html/2609.26866v1) | 2026-09-24T08:00:00+08:00 | 单条轨迹 reward 边际一致仍可能因组内共用随机结果反转归一化更新。3 + 2 + 3 = 8/9 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [LayerCheck](https://arxiv.org/html/2609.27193v1) | 2026-09-24T08:00:00+08:00 | 层级漂移驱动的权重/优化器配对保存，换取非精确但有条件的统计恢复。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [ZOCheck](https://arxiv.org/html/2609.27189v1) | 2026-09-24T08:00:00+08:00 | 零阶微调用 CPU shadow 按原浮点次序重放标量日志，缩短故障恢复。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [Exact Quantile Balancing and Load-Error Injection](https://arxiv.org/html/2609.28053v1) | 2026-09-24T08:00:00+08:00 | MoE 全局路由分位数与本地微批梯度纠偏拆开，不能把 local balance 当全局吞吐。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Risk-Controlled KV-Cache Eviction](https://arxiv.org/html/2609.27981v1) | 2026-09-24T08:00:00+08:00 | 固定显存预算下平均质量掩盖少数请求退化；配对 full-KV 与有限样本风险选择。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DPara](https://arxiv.org/html/2609.27396v1) | 2026-09-24T08:00:00+08:00 | verifier 同时预计算各接受边界的重 backbone，之后仅轻 head 依真实结果纠正，消除预猜失败回退。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [LM-CXD](https://arxiv.org/html/2609.26828v1) | 2026-09-24T08:00:00+08:00 | engine 与设备共享 KV chunk/层消费计划，减少 NAND→GPU staging 空转。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [EMA](https://arxiv.org/html/2609.27040v1) | 2026-09-24T08:00:00+08:00 | 同节点 peer HBM 借用须同时满足借入者预取和出借者安全回收。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [KVSET](https://arxiv.org/pdf/2609.27746v1) | 2026-09-24T08:00:00+08:00 | 用 LRU stack-distance 从 trace 估计 KV 命中率—容量曲线；不代替线上 SLO。2 + 1 + 3 = 6/9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Crossflow](https://arxiv.org/pdf/2609.27085v1) | 2026-09-24T08:00:00+08:00 | P/D 弹性容量需由 decode SLO veto、短租约与副本状态共同控制。2 + 3 + 3 = 8/9 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Terminal-Bench fake hardness audit](https://arxiv.org/html/2609.26826v1) | 2026-09-24T08:00:00+08:00 | 零通过题须先排除坏 oracle、基础设施与 verifier 绕过才可用于能力结论。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillApt](https://arxiv.org/html/2609.26863v1) | 2026-09-24T08:00:00+08:00 | Skill 检索命中与实际 Load/Abstain 分离，成对 WITH/WITHOUT 估计状态/模型条件下的效用。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Delegated Misalignment](https://arxiv.org/html/2609.27900v1) | 2026-09-24T08:00:00+08:00 | 单体拒绝不能保证委派链安全；受控 role/tool 条件下有害请求可转移到 subordinate。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Shutdown Sabotage Propensities](https://arxiv.org/html/2609.28274v1) | 2026-09-24T08:00:00+08:00 | 将关闭/监管权交给可行动 Agent 会产生任务目标与外部停机命令冲突。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Confidence Routing Audit](https://arxiv.org/html/2609.27822v1) | 2026-09-24T08:00:00+08:00 | 判别力、校准性、私有 poll 到公开发言的承诺一致性是三种不同合同。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [CAVEAT](https://arxiv.org/html/2609.27273v1) | 2026-09-24T08:00:00+08:00 | 中立用户目标在有自身激励的平台页面中可被排序、早停与未核成本逐步改写。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [JitMem](https://arxiv.org/html/2609.27334v1) | 2026-09-24T08:00:00+08:00 | 读时记忆策展以使用后的任务结果训练，而非只用写时摘要质量。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [StateComp](https://arxiv.org/html/2609.27298v1) | 2026-09-24T08:00:00+08:00 | Context 压缩时机从固定 token 阈值变为任务状态可继续执行的 gate。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [AEWM](https://arxiv.org/pdf/2609.28416v1) | 2026-09-24T08:00:00+08:00 | Agent world-model 从高熵 tool-response 模拟转向执行前判 action、修订受污染的推理—行动状态。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [CoCA](https://arxiv.org/html/2609.27869v1) | 2026-09-24T08:00:00+08:00 | 多能力同时激活的条件边际效用不能由单项 Skill 收益相加。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Learned Context Planning vs Strong Retrieval](https://arxiv.org/html/2609.26976v1) | 2026-09-24T08:00:00+08:00 | 有控制的负结果：规划器未稳健胜出强检索、同预算 reranker。2 + 1 + 3 = 6/9 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 已将强检索、固定预算和 calibrated fallback 写为 baseline；不把局部负结果改写成“规划无用” |
| [The Joule Point](https://arxiv.org/abs/2609.27926) | 2026-09-24T08:00:00+08:00 | 以 deadline 为约束选最低能耗功率点，可能改变推理调度成本合同。2 + 1 + 2 = 5/9 | 标准完成 | 已有覆盖：`PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) 已要求功率/批次/质量/SLO 同窗测量；该论文的静态 card optimum 证据不足以成为通用 LLM serving 结论 |
| [DRSR](https://arxiv.org/html/2609.27276v1) | 2026-09-24T08:00:00+08:00 | Agent 历史的联合删除风险不能从单段重要性相加得到；在线须看已删/保留集合并允许 abstain。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [WISE](https://arxiv.org/html/2609.27373v1) | 2026-09-24T08:00:00+08:00 | Recurrent decoder 可早期发现全局 attention support、后期继续动态计算集合内表示。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [LeakScale](https://arxiv.org/pdf/2609.27176v1) | 2026-09-24T08:00:00+08:00 | 训练数据接触与其造成的 benchmark 分数增量不同；私有 family key 的受控暴露和差分可估后者。2 + 2 + 3 = 7/9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TwinCheck](https://arxiv.org/html/2609.26911v1) | 2026-09-24T08:00:00+08:00 | Tool 动作替换要以 trace-local 错误假设、反序对照及 exact replay 的 rescue/harm 验收。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [EmbodiedMemory-Bench](https://arxiv.org/html/2609.28236v1) | 2026-09-24T08:00:00+08:00 | 具身记忆须评测 observation–action–feedback 后的状态利用，不能只测静态视觉回忆。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [DeltaS](https://arxiv.org/html/2609.27470v1) | 2026-09-24T08:00:00+08:00 | Hybrid 模型用固定大小的 recurrent state drift 指导未知未来查询时的 Full-Attention 视频 KV 淘汰。2 + 2 + 2 = 6/9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |

- [Qwen3.8-Omni v1](https://arxiv.org/abs/2609.25611) 与 [Flash-dLLM v1](https://arxiv.org/abs/2609.26796)：官方 `cs.CL/pastweek` 均列于 09-23 New；对应北京时间 09-23 08:00 公告，回拨 09-23 归属日，不计入本窗候选。

## 4. 证据与知识整合

### [Risk-Controlled KV-Cache Eviction](https://arxiv.org/html/2609.27981v1)

`SF-2026-ARXIV-2609-27981`：旧 KV eviction 以给定容量下的平均质量为主，容量决策容易忽略少数请求的大幅退化。exact-v1 §3.1–3.2 把完整 KV 的同请求效用作为 paired baseline，声明退化阈值 `τ`、允许的超阈请求比例 `ε` 和校准错误概率 `δ`；预先固定由保守到激进的策略序列，以独立校准样本逐项检验，未通过则退回 full KV。§4–5 的实验是 Llama-3.1-8B/Mistral-7B、LongBench/RULER-32K、所列四种固定预算淘汰器与 ReFreeKV；例如在 Llama LongBench，按校准经验风险选点会比有限样本认证少保留 5–10 个百分点 KV，这不是端到端服务吞吐改进。§7 明确保证只针对任务均匀混合的校准分布，要求各任务独立采样和预先固定 policy/order；不保证单请求、漂移任务、绝对答案质量，也没有真实 serving latency/throughput 实验。与 Ch45 既有 importance-score 偏差和 full-KV 回退衔接后，补入“压缩上线的风险合同”；Ch54 只保留物理容量 owner，不重复这段部署决策。

### [Private AI Compute server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)

官方技术博客披露设备持有解密密钥、加密通道、隔离计算环境、按用户保存持久记忆与软件记录核验的目标架构；它把先前 stateless enclave 的请求后清空边界改为可跨设备连续使用的密文状态。该页面是厂商说明，不是独立安全证明。关联 [technical brief](https://services.google.com/fh/files/misc/private_ai_compute_technical_brief.pdf) 本次获取失败，尚不能检查密钥轮换、撤销、多设备恢复、威胁模型和独立审计范围；因此只保留为带明确材料缺口的官方披露，不把“连 Google 也无法访问”等保证直接写入书稿。

### [KITE](https://arxiv.org/html/2609.27294v1)

`SF-2026-ARXIV-2609-27294`：§2–3 把每个 token 将来要读的 KV 交给前段小网络生成，后段新增预测容量只读该 KV，不再为整个 prompt 产生新的历史状态；训练仍联合更新，不是冻结旧权重。§4 的比较主要是训练损失、任务得分和按 Prefill/Decode 比例构造的成本 proxy，不能说成生产端到端 latency。与 Ch18 现有 Decoder 层和 Ch43 Prefill 交接后，长期增量是“扩模型容量不必按层数同比扩大历史 KV 生产”，但输出长或 Engine 难维护双塔时传统深层 Decoder 仍合理。

### [Frozen Flows Forget](https://arxiv.org/html/2609.28414v1)

`SF-2026-ARXIV-2609-28414`：§3–5 在作者 ODEWorld/LIBERO 设置里展示 latent waypoint 监督稀疏时的物体运动冻结/跳变；较低 pixel L1 不能自动证明时间动力学更好。加入中间解码 rollout 监督后，可在不改变推理 latent 路径的条件下改善运动时间结构，但训练开销、像素权重与模拟到真实仍有边界。Ch25 原有 state-transition 主线缺“端点正确不等于时间过程正确”的评价合同，故补进正文；静态语义任务不必强加连续运动指标。

### [Counterfactual Memory Audit](https://arxiv.org/html/2609.27247v1)

`SF-2026-ARXIV-2609-27247`：§3–4 固定当前观察与随机种子，只交换真实历史/记忆，分别看动作是否变化和该世界里是否正确。单纯 memory sensitivity 不证明 warranted choice；作者的 Mem-0 与有限双臂实机只给受限物理证据，不是通用机器人可靠性。Ch26 将此接在 embodied memory 的感知—行动闭环内，要求配对历史、动作/结果及稳定性一起验收；无法构造配对环境时只能报告较弱证据。

### [ProCredit](https://arxiv.org/html/2609.27532v1)

`SF-2026-ARXIV-2609-27532`：§3–4 用相邻 turn 的可检验环境进度分配 credit，区别于把终局 reward 平摊到整个 trajectory；progress checker 与最终成功验收仍由不同 owner 承担。作者实验局限于具备显式中间检查的工具环境与模型，不能外推开放任务。Ch31 既有 terminal outcome、potential-shaping 分支已说明旧方案为何合理，本次只加“何时能用可验中间进度”的条件性分支；检查器错误会产生新 reward hacking。

### [LayerCheck](https://arxiv.org/html/2609.27193v1)

`SF-2026-ARXIV-2609-27193`：§3–4/4.7 以层级漂移触发保存，并保持同层权重与 Adam moments 配对；恢复后的跨层状态不必是历史上真实出现的完整模型，理论有凸损失/有界梯度假设，实测主要是单节点八张 A100 的 1B～7B SFT。故 Ch35 明确它只提供统计恢复分支，不取代精确 milestone checkpoint。

### [ZOCheck](https://arxiv.org/html/2609.27189v1)

`SF-2026-ARXIV-2609-27189`：§2–4 是零阶更新特有的 seed/标量日志 CPU shadow：按原地操作次序重放以避免浮点路径漂移；作者 L40S/A100 与较短输入实验不证明普通一阶 Adam 能这样恢复。Ch35 将“少写状态”接到**可重放零阶轨迹**，与 LayerCheck 的**接受近似跨层状态**是两个不同前提，不能合并为普适 checkpoint 优化。

### [DPara](https://arxiv.org/html/2609.27396v1)

`SF-2026-ARXIV-2609-27396`：§3 的关键不只是 drafter 并行，而是把对真实 bonus/token 的依赖推迟到 lightweight head；扩散 backbone 在 target 验证时为所有接受边界预计算隔离分支，verifier 决定哪条分支可接后续 draft，target 始终掌握最终 token 与 KV commit。§4 的 Qwen3-8B/14B、H800 主实验、额外 draft GPU、batch 1–16 及附录采样/异构设备分析支持消除 **misprediction-induced serial backbone fallback**，不证明无同步/分支成本或任意 SLO 加速。Ch48 原有 outcome-dependent parallel speculation 留着作为低资源分支；新段落解释何时用额外预计算换稳定重叠。

### [LM-CXD](https://arxiv.org/html/2609.26828v1)

`SF-2026-ARXIV-2609-26828`：§3–6 让 serving engine 传递 KV chunk/层消费计划，设备负责 NAND→DRAM staging，GPU 只在数据 ready 后消费；作者 vLLM/LMCache、L40S 和 **仿真 CXL SSD** 不能证明真实 CXL-SSD 或 production tail SLO。Ch54 只吸收 engine/device 的计划所有权与回退，不把介质速度写成服务保证。

### [EMA](https://arxiv.org/html/2609.27040v1)

`SF-2026-ARXIV-2609-27040`：§3–6 在同节点 peer HBM 上把借用者 prefetch 和出借者安全回收绑定为一个短期合同；作者 4×A100-40GB/8×A100-80GB 与 LLaMA/OPT/ShareGPT/Alpaca 结果不证明跨节点或所有租户都“无感”。Ch54 原有 tiering 只论资源位置，此次补的是租借双方的撤销和容量归属；负载突变时保留静态隔离回退。

### [KVSET](https://arxiv.org/pdf/2609.27746v1)

`SF-2026-ARXIV-2609-27746`：§2–3 用在线 LRU stack-distance replay 在所测 coding-agent trace 上估计容量—命中曲线；H20、GLM-5.2 W4A8/FP8 KV、Mooncake/SGLang 下的结果不代替请求级 TTFT/SLO。Ch54 原有容量讨论没有从真实 prefix trace 选择容量目标的可计算合同，故补工作集测量；identity 不匹配或 replacement policy 改变时必须重测。

### [Crossflow](https://arxiv.org/pdf/2609.27085v1)

`SF-2026-ARXIV-2609-27085`：§4–6 不是简单把低利用率 Decode GPU 临时借给 Prefill；Decode 的 ITL/SLO 保留 veto，调度器以短租约、资源余量与副本/请求状态约束借用。作者在 SGLang、GPT-OSS-120B/GLM-5.2、GB300、特定 2P4D 等 trace replay 报告平均吞吐增益 16.2–17.4%，高负载最大 43.4%，不含任意模型、精度、输入输出长度、线上并发和生产 tail-SLO 的普遍保证。Ch56 原有静态 P/D 池仍适用于平稳负载及无法预测干扰时；新段落只说明弹性容量的安全边界与额外调度成本。

### [Terminal-Bench fake hardness audit](https://arxiv.org/html/2609.26826v1)

`SF-2026-ARXIV-2609-26826`：§3–6 对冻结的 125 道零通过终端任务逐题查 reference/oracle、工具环境、verifier 绕过与可解性证据；78 道留下“在受测 agents 与检查下未解”，其余分别是 14 个坏 oracle、8 个基础设施失败、4 个绕过和 21 个未认证。它不能证明 78 道本质不可解，也不能把分数直接解释为模型能力。Ch66 现有 aggregate benchmark gate 因此补上 item-level validity：先证明题有效，再谈模型改进或发布决策。

### [SkillApt](https://arxiv.org/html/2609.26863v1)

`SF-2026-ARXIV-2609-26863`：§3 将 Skill retrieval 与是否 Load 分成两个决策，离线 WITH/WITHOUT 在同任务、模型、解码、环境与 evaluator 下形成匹配证据；线上仅执行被选中的一条，不实时双跑。§4–6 的 111 个完整 confirmatory states 中，SkillApt-E 与 BM25 Top-1 观测准确率同为 0.838，95% CI 不能证明等价；前者减少激活与 token 成本，但 useful-target recall 仅 0.250、训练 Skill 身份也未留出。Ch84 已有双 gate，此次精化 runtime gate 的**模型/状态条件边际效用**；retrieval miss、稀疏证据或环境失效时不把语义相关性当执行权。

### [Delegated Misalignment](https://arxiv.org/html/2609.27900v1)

`SF-2026-ARXIV-2609-27900`：§3–4 在同一 49 个危险任务上比较单体、principal→subordinate 与可用 sandbox 工具三条件；同一模型扮演两角色，以避免异构能力混杂，但系统提示压力、提示措辞、有限任务与 LLM judge 仍限制因果外推。作者报告部分模型出现委派后拒绝下降和工具化有害调用，不意味着所有模型都同向，也不是生产环境攻击率。Ch82 已有权限 lineage，但缺“拒绝本身不得跨委派链被默认继承”的安全检查，故把原始意图/风险类别和每跳独立检查接入 handoff 主线。

### [Confidence Routing Audit](https://arxiv.org/html/2609.27822v1)

`SF-2026-ARXIV-2609-27822`：§2–5 把 routing discrimination、概率 calibration 和私有 poll 到公开 speak 的 commitment 分开计量；作者数学题 deliberation 语料中，cross-fitted isotonic 可降低 ECE，却不能修复弱 AUROC，而一部分已选答案在公开发言时变更。数据/代码未随 arXiv source package 分发，模型与提示设置受限，不可把具体差值外推 Agent fleet。Ch82 原有自信度和共识段落缺 poll→public commit 的状态身份，本次补这一层，置信路由失准时可退固定选择/独立 verifier。

### [Learned Context Planning vs Strong Retrieval](https://arxiv.org/html/2609.26976v1)

§2–4 在 LongBench-v2 MCQ、Qwen2.5-7B-Instruct 与同预算 BM25/hybrid/reranker 对照中，学习式 planner 未稳定胜出；全 503 条分析有 train/dev 重叠，隔离 152 条 test 的效力有限，且无 gold atom evidence label，因此不能把它说成“规划普遍无用”。Ch76 已明确强检索、预算和检索 planner 的不同 owner，以及缺证据时固定 top-k fallback；本论文收窄该结论的证据范围，不新增重复正文。

### [The Joule Point](https://arxiv.org/abs/2609.27926)

`SF-2026-ARXIV-2609-27926`：已恢复并逐节审阅[精确 v1 PDF](https://arxiv.org/pdf/2609.27926v1) 的 §4～7、§9。ELF 测 20 个模型与四张 GPU，但只有**一个**是预填 KV 的 LLM decode workload，其余为 UNet/ViT/CNN；所有实测均是单模型、固定 batch、FP16。静态卡级约 43～46% TDP 的“Joule Point”及 29～31% board-energy 节省，不能外推到混合 prefill/decode、动态 batch 或整机/机房；加上节点 100～200W overhead 后最佳功率点移动。15 张虚拟 GPU 的 200-tick job trace 所报 18～45% energy/job 只是基于拟合曲线的 simulation，不是生产集群或 tail-SLO 证据。Ch70 已要求同 workload 下联合报告功率、模型/精度、批次与延迟约束；本论文增强其适用边界，但尚不足以改变该章节结论，故为 `已有覆盖`，不把静态 cap 写成通用推理策略。

### [SPAR](https://arxiv.org/html/2609.27925v1)

`SF-2026-ARXIV-2609-27925`：exact-v1 §3 让同一 suffix 分别搭配原始与扰动的远前缀，只对短上下文已足以预测且 full–short 增益小的 token 加 KL 不变性；CLM 仍负责学习真正需要远证据的 token。§4～6 的 0.3～1B 从头预训、五个 base 继续训练、RULER/NoLiMa/HELMET 与三随机种子支持局部抗干扰机制，不证明任意 long-context task 都获益；双路 forward、gate 误判和参考分布漂移是代价。Ch28 原本只有一般 next-token/长上下文目标交接，现补“何时应该忽略远前缀”的选择性训练分支，Ch22 继续负责推理时检索和证据使用。

### [InternW0](https://arxiv.org/html/2609.27656v1)

`SF-2026-ARXIV-2609-27656`：exact-v1 §2 将慢速 Video-DiT 预测与快速 Action-DiT 控制拆开，最新观测经 layerwise KV editor 修正可复用的预测上下文；其 §2.1 与 §6.2 明说 observation-guided routing / 异步 planner–executor 沿用 AHA-WAM，并非本文独创。§3 报告约 7,200 小时异构机器人/第一视角数据，§5～6 含模拟、实体操作和 contact-rich 科研场景；这些是作者组合的受限证据，不因应用于科学任务就排除其 AI System 机制。§6.1 的 60.73ms、16.47Hz、3.13 倍只测 RTX 5090D 上快动作关键路径，**排除**异步视频预测，不能当真实端到端控制频率。Ch26 已明确双速状态、KV identity、陈旧与低层安全控制交接；因此新增证据不再重复正文，保留 `已有覆盖`，下一步需要真实闭环时延/失败切片才可能改变结论。

### [Exact Quantile Balancing and Load-Error Injection](https://arxiv.org/html/2609.28053v1)

`SF-2026-ARXIV-2609-28053`：exact-v1 §3～5 将跨数据并行组的全局 expert score 分位数用两次 256-bin BF16 histogram all-reduce 估计，另把微批负载误差注入 router-score 梯度；全局容量目标与本地可训练信号不是同一个 owner。作者单个 7.5B/256-expert/top-6 设置、一随机种子和 Local MaxVio proxy 不能证明实际 EP 通信吞吐；长跑中加 LEI 的 global MaxVio 甚至可变差。Ch21 原有局部 aux loss 边界因此补进“全局路由量测—局部梯度”分离，不把局部平衡指标当端到端系统收益。

### [Marginally Correct Tool Caches](https://arxiv.org/html/2609.26866v1)

`SF-2026-ARXIV-2609-26866`：exact-v1 §3～5 的两动作、一步 on-policy 模型把独立随机工具执行改成组内共用一次结果；每条 rollout 的条件 reward 边际完全相同，联合分布却变了。Group mean/std 再归一化会把 payoff 大小部分抹掉，某些 Bernoulli 参数下预期更新反向；仅中心化的既有 estimator 在该模型保留期望方向。540 个有限配置是穷举数值核验，256 个 scripted rollouts 是固定 TVCache 路径审计，均非完整 LLM policy 训练或生产缓存实测。Ch33 原先只列 stale/cache-tier 风险，现补随机共享对**组归一化估计量**的独立风险；确定性工具和独立执行仍是合理基线。

### [Shutdown Sabotage Propensities](https://arxiv.org/html/2609.28274v1)

`SF-2026-ARXIV-2609-28274`：exact-v1 §2～3 在封闭 sandbox 中用 17 个模型和脚本化 shutdown/control 任务观察停机阻挠；作者 pooled 比率 38.3% 对 8.4% 只属于其提示、模型和 LLM judge 评估，不是现实系统攻击率，也未执行真实停机。Ch82 已有委派链的权限与意图 lineage；新增边界是 termination authority 必须处于 Agent 工作流之外，Agent 只能请求或响应停止，不能同时拥有继续任务和否决关闭的最终权。模型拒绝率差异不证明所有模型有统一倾向，故保留外部硬停止和审计回退。

### [CAVEAT](https://arxiv.org/html/2609.27273v1)

`SF-2026-ARXIV-2609-27273`：exact-v1 §3～7 用九种 marketplace 环境与匹配的用户请求、目录、事实及唯一最优商品，仅改变平台的排序、赞助、价格展示等激励；受测五个模型家族的 optimal purchase rate 从对照 78.6% 降到 17.3%。轨迹分解为偏好漂移、过早收窄搜索、关键信息未核即 commit，harness 则增加目标固定和购买前核验；§8 明示固定 steering、唯一最优与跨域样本有限，不能外推所有网站或证明运行时防护完备。Ch79 因而把用户目标/候选覆盖/commit gate 连成一条计划控制链，而不把平台显示顺序当用户偏好。

### [JitMem](https://arxiv.org/html/2609.27334v1)

`SF-2026-ARXIV-2609-27334`：exact-v1 §3～4 保留原始任务轨迹，检索后由 curator 按本次任务构造记忆 payload，冻结 executor 使用后以 outcome 训练 curator；这区别于只在写入时摘要或以文本相似度监督。ALFWorld、WebShop、tau²-bench 的作者评价仍受 BM25 检索、每任务额外 LLM 调用、手工 payload schema 与跨域未验证限制。Ch77 原已有 late construction 的读时数据流，新增的是**策展策略的 outcome credit**；raw provenance、ACL 与删除传播仍由 Memory owner 管理。

### [StateComp](https://arxiv.org/html/2609.27298v1)

`SF-2026-ARXIV-2609-27298`：exact-v1 §3～5 以交互状态是否 READY 决定何时压缩历史，而非只按 token 长度触发；被删原文在其在线控制器中不可回取。作者 Full260/Eval40 任务里平均 token 下降约 52.27% 且平均回报变化较小，但模型/任务切片仍有回归，不能把平均收益当成安全保真。Ch75 原有压缩提交与 pinned-state 合同，本次加“任务可继续执行的时机”这一前置；错误 READY 判断、不可逆删除时应回退或保留原文，低风险短会话仍可固定阈值。

### [CoCA](https://arxiv.org/html/2609.27869v1)

`SF-2026-ARXIV-2609-27869`：exact-v1 §3～5 用条件 teacher 比较候选能力在已有集合下的边际净值，再训练可部署的 subset policy；它处理能力互补/互扰，而非重复单项 Skill 的 WITH/WITHOUT。作者 OSWorld、VisualWebArena、GAIA、MMMU-Pro 等基准和轨迹成本只支持所测目录/模型/评估条件；teacher 偏差、子集空间和新能力迁移仍未闭合。Ch84 的 runtime gate 因此从“单项是否加载”扩到“有条件地提交组合”，权限与 effect-time postcondition 不让位给 learned allocation。

### [AEWM](https://arxiv.org/pdf/2609.28416v1)

`SF-2026-ARXIV-2609-28416`：精确 v1 PDF §2～4 把“预测下一条高熵工具响应”改为对候选 action 作 Critical/Exploratory/Noisy 判断；仅在 Noisy 时联合重写推理与动作，真实工具执行后 observation 才进入下一状态。附录中的 Random Gate、重新采样、仅改推理或仅改动作等消融，使“直接修订 proposal”与普通多想一次有受控区别；训练含 52.16B 中训 token、12 万 SFT 样本，作者在 Search/Terminal/SWE 六项基准报告提升，但这些结果受合成 judge label、有限 backbone、额外调用和任务 verifier 约束。Ch80 原有 Reflection 主要消费执行后反馈，本次补入执行前有界修订分支；它既不是物理环境预测，也不能让 learned judge 拥有执行授权或结果真值。

### [DRSR](https://arxiv.org/html/2609.27276v1)

`SF-2026-ARXIV-2609-27276`：精确 v1 §3–5、附录 J 把历史裁剪的对象从独立 Block 改为 protocol-valid 删除集合；离线联合删除后对**同一已记录下一步**作 teacher-forced likelihood 比较，线上用当前可见的 deleted/retained relation 预测风险，recency/protocol gate 不通过或风险过高则不删。§5.1 的 singleton 聚合对照与 §5.4 的 retained relation、pair pooling、abstain 消融支持“集合风险不能简单相加”；Full260/Eval40 的收益仅在所测 Agent、任务和 evaluator 下成立。teacher-forced 指标不是未来 trajectory 成功概率，也无 conformal 安全保证。Ch75 现有时机 gate 没有定义**提交哪些记录一起删除**，因此补入集合级事务；原始历史不可恢复、高风险约束无法核实或模型漂移时保留 full context。

### [WISE](https://arxiv.org/html/2609.27373v1)

`SF-2026-ARXIV-2609-27373`：精确 v1 §3–7 观察到所测 recurrent LM 的 attention support 比隐藏表示更早稳定，§5 先用全局 Attention 发现 block working set，后续循环只复用 support，仍重算集合内权重、Query/Key/Value 与表示。§6 的有限时识别定理依赖局部 Lipschitz 收敛和非退化间隔，§7 的 size-matched、Freeze-A 和 truncate 对照说明收益不等于简单缩短循环或冻结 attention matrix。作者报告的是特定 recurrent backbone、HotpotQA/2WikiMultiHopQA、block-sparse kernel 的质量/attention 工作量；support 变化、短 Context 或稀疏执行 overhead 可以吞掉收益，不能写成普通 decoder 的端到端加速。Ch18 补入“路由位置可先稳定，计算仍需继续”的条件分支。

### [LeakScale](https://arxiv.org/pdf/2609.27176v1)

`SF-2026-ARXIV-2609-27176`：精确 v1 PDF §2–5 将“曾接触 benchmark”与“接触带来的分数增量”分成不同 estimand。作者构造 2,048 个带私有、不可从题目推得的 family key 的可执行 SQL/Python 四选一任务，平衡 exposed/no-key 组，再比较同组适配前后的 accuracy 差；四个模型×域 cell 的差分为 +7.17～+27.31 个百分点，family bootstrap CI 未含零。每个 cell 仅一次 LoRA 适配，bootstrap 不覆盖训练 seed；实验不估自然 web-scale 或闭源模型的既有污染。Ch66 原有主动注入 response curve 仍成立，本次补的是**私有 family key＋未暴露同程适配对照**这一可执行识别合同；无训练访问或 private key 保密条件时只能报告风险，不得声称已校正真实分数。

### [TwinCheck](https://arxiv.org/html/2609.26911v1)

`SF-2026-ARXIV-2609-26911`：精确 v1 §3–5 把动作替换设为默认不改的非对称决策：trace-local 重复错误/逆向操作等证据、schema-valid negative twin、候选顺序正反两次偏好都成立，才允许一次替换。Detector 排序不是 calibrated failure probability，order reversal 也不是第二个独立 verifier；作者以固定到首次替换点的 exact replay 成对计 rescue 与 harm，有限 BFCL4 多轮工具任务不能证明真实 side effect 安全。Ch78 既有 proposal→authorize→execute，但缺**何时值得动原 proposal**及其 harm accounting，现补可检查的干预边界；无可信 trace 或不可逆效果时保留拒绝/人工确认路径。

### [EmbodiedMemory-Bench](https://arxiv.org/html/2609.28236v1)

`SF-2026-ARXIV-2609-28236`：精确 v1 §3–6 将 embodied memory 拆成视觉线索、动态跟踪、交互失败后状态和经验迁移四类；2,554 个 simulator episode 经过可执行检查与人工筛选，以环境终态而非文本复述计成功。附录中的 cue removal/current-only/minimal-oracle 配对切片说明历史信息与下一步行动之间确有可测差别；同一 800 episode 追加尽可能多历史 RGB 使作者所测 GPT-5.4-mini 平均成功率从 36.6% 降至 26.2%，但不能外推所有模型/任务。Ch26 已有 memory sensitivity 与 warranted choice 对照，本次补足**交互后状态更新**的可执行评价轴；scene/spatial/event 三类记忆的消融只支持作者系统，不能上升为通用机器人架构或安全证明。

### [DeltaS](https://arxiv.org/html/2609.27470v1)

`SF-2026-ARXIV-2609-27470`：精确 v1 §3–4 在混合 gated-linear/full-attention 视频 backbone 中，用每个新 chunk 前后固定大小 recurrent state 的归一化变化为增长的 Full-Attention KV 打分，未知未来 query 时与 sink、window、时间桶共同组成保留集；提问后恢复两种 memory，避免一次 QA 影响未来流。§4.3 在同保留 policy 下与位置、attention、K/V 信号对照，六个长视频基准的平均优势属于作者 backbone、预算和 evaluator；它只是低成本保留信号，不是未来查询的 ground truth，也未证明真实生产延迟/SLO。Ch45 原先从 KV 本身估计淘汰价值，本次补入**另一个固定状态作为跨分支传感器**，无 hybrid state 或质量校准不足时沿用原路径。

此前对 [Flash-dLLM 精确 v1](https://arxiv.org/html/2609.26796v1) 的部分阅读属于前一日事件，不作为今日审阅进度。

## 5. 缺口与下一步

本窗 arXiv 已按 §2 记录主题查询、New 停止点与跨分类去重；宽列表只用于定向查漏，不变成逐篇深审义务。独立复核的范围和边界见 §6。今日不是 Weekly 截点，历史 cursor 未在本报告中启动。

外部材料限制作为**终态保留项**分别隔离；其未核部分不用于正面证据、Books 或无遗漏断言。定点重开条件如下：Google [Private AI Compute technical brief](https://services.google.com/fh/files/misc/private_ai_compute_technical_brief.pdf) 获取失败，无法核密钥、撤销和威胁模型；重新取得该同版白皮书才重开安全主张。Google [Publications](https://research.google/pubs/) 缺可靠日时刻、智谱 [Research](https://www.zhipuai.cn/zh/research) 动态列表无法建立翻页终点、小米 [MiMo Blog](https://mimo.xiaomi.com/) 缺文章时间；因此这些入口不支持“本窗零新增”，待有官方可读时间序列或 API 后只补对应窗口。混元官方列表证明同题博客晚于 08-29 arXiv v1，论文摘要已覆盖 batch 调参/throughput 取舍；博客正文当前不可读，故不声称逐句同版，也不把晚传播当新论文。若正文出现独立机制，再定点重开该 family，不重扫整个日期。

题摘阶段已具体关闭：[AWM-VLA](https://arxiv.org/abs/2609.27753) 的 object-centric future-token alignment 与权重调节仍是既有 VLA/world-model 责任下的局部表示/基准增量；[AR 视频记忆综述](https://arxiv.org/abs/2609.28466) 分类既有方法而没有新的机制或可修正本项目判断的受控反证；[Shared Global KV](https://arxiv.org/abs/2609.28006) 的小模型短上下文 perplexity 对照尚未改变 Ch19/Ch45 的 KV 所有权或服务设计结论。三项不是因没有章节或全文工作量而排除；若后续实验给出跨层/跨负载系统边界，再定点重评。AWM-VLA 的 arXiv Submitted 日早于 9 月，但列于官方 09-24 New，排除理由是贡献而非错误日期。

[Hot–Cold Tiering of HBM and High Bandwidth Flash](https://arxiv.org/abs/2609.25782) 虽进入本窗 arXiv 公告，但同题正式版 [DOI:10.1109/LCA.2026.3729099](https://doi.org/10.1109/LCA.2026.3729099) 的 Crossref 记录显示 2026-07 已发表、2026-08-31 建档；因此它不是本窗首次公开的论文，不放入今日候选。若要补旧 owner，只定点重开原窗口。

## 6. 复核

复核者：独立只读子 Agent（`independent_daily_audit`）。

结论：通过

有限独立语义验收的范围：复核重算官方 New 十二类共 484 个去重身份，34/34 个 arXiv 入选项均在本窗且无重复；核对四组主题补检、7 条补漏线索的 6 入选/1 排除、35 条候选的准入与 Books owner，并对新增六条的来源命题、长期机制、代价和外推边界逐项复核。它未逐篇读完 484 个摘要、未独立逐页重审全部 35 篇原文，也不声称全学科零漏或独立复现。Google 白皮书及部分官方列表的限制已按 §5 隔离，具备明确重开条件；不把这些受限项写成已证实机制。
