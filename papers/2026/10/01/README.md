# Daily Research — 2026-10-01

**规范：** V3
**窗口：** 2026-09-30T09:00:00+08:00 ～ 2026-10-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T15:06:01+08:00

## 1. 结论

本窗冻结 **21个唯一家族**：2项机构事件与19项arXiv首公开。20项深入、1项标准必要证据审阅；19项长期差额已实际整合到13个owner章节，2项具体已有覆盖。所有必要实际写后复核及最终非作者日级验收通过，普通待办为0。原始分类目录的数百条库存不是候选或全文队列，不报告无法支持的全来源raw总数。

重要增量沿既有论证归入：跨身份reasoning消费与monitor反馈权限；Agent真实推测执行、memory变异与session恢复；共享KV身份/lifetime、逻辑/物理搜索工作量及数值prefix合同；异构MoE计划、host-only通信与训练proxy/视觉蒸馏；world-model规划视野、VLA观测新鲜度及solver质量取舍。没有把厂商公告变成完整安全证明，也没有把模拟硬件、局部无错或减NFE变成生产保证。保留原机制及fallback，不新增节点。来源四个子入口仍有具名外部材料限制，见§5；今日周四，不生成Weekly。

## 2. 来源覆盖

执行时间与原始依据见[机构有限检查](../_sources/daily-20261001/INSTITUTIONS.md)及[arXiv 本日记录](../_sources/daily-20261001/ARXIV.md)。下表自包含实际入口/停止边界；未声称互联网或全机构零遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/news/research/)及[RSS](https://openai.com/news/rss.xml)首8项至09/28；09/30两事件读核心，保留安全披露、排除小企业培训支持 | 已检查 | RSS web失败后原XML可读；不以Research子栏代表全部事件 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)最新09/30→29→25；读唯一09/30机器人职业估计核心 | 已检查 | 增量是职业暴露/成本估算，不新增VLA/系统机制，贡献前关闭 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)首页30项最新09/16；[Research Blog](https://research.google/blog/)最新09/29→24；[DeepMind Blog](https://deepmind.google/blog/)顶部Argon回原文 | 已检查 | [pubs](https://research.google/pubs/)年份目录无可靠日排序，仅辅助，不把全年目录称当日论文 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空页后查[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)最新前缀09/24→07→06→08/04；[Blog](https://ai.meta.com/blog/)首页最新可见07/27、旧置顶混排 | 已检查 | 有限公开前缀，不由空页/混排证明全机构无遗漏 |
| SRC-QWEN | [Research](https://qwen.ai/research)、[Blog](https://qwen.ai/blog)及旧主页跳转，fresh原页/公开首页脚本仍是共享应用壳；浏览器建tab超时 | 受阻 | 带日期研究目录本窗隔离；脚本08/10开屏下架不是论文日期，不记零命中 |
| SRC-DEEPSEEK | [News/Research](https://www.deepseek.com/news/)可见News5项最新09/10、Research10项最新06/24 | 已检查 | Show All后续不可提取；结论限可见最新前缀 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26项最新2025/11；[kimi-cli release](https://github.com/MoonshotAI/kimi-cli/releases)最新09/22，09/23 archive | 已检查 | 沿明确研究/Agent入口停止，不枚举全org普通commit |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)公开JS恢复[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，page1/size30/renderType0：total11/返回11，取完全部 | 已检查 | publicAt/publishedAt/display时间/updated均早于窗，不用createdAt冒充公开日期 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)fresh原页最新08/26→14→06/16；[release notes](https://docs.z.ai/release-notes/new-released)最新08/26→18 | 已检查 | web旧缓存另由当前原HTML核，不重审旧论文 |
| SRC-BYTEDANCE-SEED | [papers](https://seed.bytedance.com/en/public_papers)newest首页20/242、1/13页最新08/18→12→06→07月，越窗停止；[Research](https://seed.bytedance.com/en/research)最新07/06 | 已检查 | [Blog](https://seed.bytedance.com/en/blog)无可提取目录单独保留；不用papers替它证明零 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)首页最新05/09→04/30→15→02月 | 已检查 | 仅当前最新边界，不扫旧模型 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/)Paper8项最新06/29，Blog15卡片无时刻；公开JS恢复首卡[原文](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)日期09/27 | 已检查 | 首卡窗外、其余Blog无钟终态隔离；不由首卡推断15项全部零 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)/[CN Blog](https://www.minimax.cn/blog)最新08/13→07/31→06/09；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)空响应，[llms index](https://agent.minimax.io/docs/llms.txt)定位techblog.md后打开失败 | 已检查 | Agent子目录文章/日期隔离，不由主目录推断零 |
| SRC-ARXIV | [cs.CL new](https://arxiv.org/list/cs.CL/new)/[recent](https://arxiv.org/list/cs.CL/recent)、[cs.LG recent](https://arxiv.org/list/cs.LG/recent)的Thursday1Oct主题标题；DC/OS/PF/AR/PL系统查漏、CV/RO/AI/IR/MA多模态定点线索，相关题名才读完整题摘；19唯一家族冻结，9具名Replacement当前说明有限检查，停止依据见原记录§1/5/6/8/9 | 已检查 | 首次过宽查询/截断未读部分不冒充检查，全分类完整召回未验证；未建立宽列表逐条义务。官方[公告规则](https://info.arxiv.org/help/availability.html#announcement-schedule)对应10/01 08:00BJT，Submitted不用作公开时刻 |

## 3. 候选与判断

冻结21唯一家族，均为本窗首次公开事件，无重复计分；必要精确版本访问2026-10-01。分数仍评材料增量，不因最终整合而上调。已确认的长期缺口与设计反证仅加深受影响内容，未遍历无关附件。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Disrupting a coordinated model distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) | 2026-09-30T18:30:00+08:00 | 密文隐藏不等消费授权，跨身份/model-family重放需与release gate分层。3+2+3=8 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST通过 |
| [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | 2026-10-01T04:00:00+08:00 | 风险监测与训练反馈权限分账，不能优化低monitor score代替安全。3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，仅反馈分工增量，实际POST通过 |
| [TomasuLLM](https://arxiv.org/html/2609.38201v1) | 2026-10-01T08:00:00+08:00 | 真实工具推测执行需要区分operand就绪、当前提交与预测观测的后继有效性。3+2+2=7 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，COW搜索与Live Fork之间，实际POST通过 |
| [The System Prompt Illusion](https://arxiv.org/html/2609.38205v1) | 2026-10-01T08:00:00+08:00 | probe可读、表征几何相似、局部patch因果证据不能互换；设计反证加深。2+1+2=5 | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，仅readout/局部因果分账 |
| [Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2609.38222v1) | 2026-10-01T08:00:00+08:00 | 全回答支持率含空输出，不等于非空回答的条件支持率；verifier标签不是语义真值。2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，仅分母及oracle权限边界 |
| [SpecScale](https://arxiv.org/html/2609.39334v1) | 2026-10-01T08:00:00+08:00 | 逻辑候选数不等实际forward数，独立draw与PRM排队分别控制；长期机制缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-CONTINUOUS-BATCHING` / [Ch46](../../../../books/part-05-inference-system/46-continuous-batching.md)，iteration工作单元后，实际POST通过 |
| [Preserving Provenance in Shared KV Caches](https://arxiv.org/html/2609.38706v1) | 2026-10-01T08:00:00+08:00 | local key正确不保证connector保留计算等价和sharing权限，跨worker/lookup-store身份须一致。3+2+2=7 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Prefix reuse，实际POST通过 |
| [Vosti](https://arxiv.org/html/2609.38981v1) | 2026-10-01T08:00:00+08:00 | 单kernel确定性不足wholeengine；canonical KV与relational kernel合同须组合。3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值验收，实际POST通过 |
| [KVTether](https://arxiv.org/html/2609.39819v1) | 2026-10-01T08:00:00+08:00 | message变异须传播prefix版本失效，跨context引用和waiting age分账；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Agent语义区域后，实际POST通过 |
| [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/html/2609.39131v1) | 2026-10-01T08:00:00+08:00 | flash层容量不免费，write endurance、缓存锁定与admission压力联合规划；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，扩展层级，实际POST通过 |
| [The Planning Limits of Latent World Models](https://arxiv.org/html/2609.39235v1) | 2026-10-01T08:00:00+08:00 | 精确transition仍会因目标评分短视失败，prediction质量与planning range不同。3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Imagined rollout，实际POST通过 |
| [U-Fuzz](https://arxiv.org/html/2609.38275v1) | 2026-10-01T08:00:00+08:00 | 正确memory不保证正确消费，query/state变异、探索与判错需分权；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)，Recall/Use之后，实际POST通过 |
| [StateFork](https://arxiv.org/html/2609.38648v1) | 2026-10-01T08:00:00+08:00 | 文件恢复不等session后续观察等价，逻辑分支与checkpoint物理化分权；恢复合同深入。2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，联合恢复之后，实际POST通过 |
| [Blackout and Freeze](https://arxiv.org/html/2609.39145v1) | 2026-10-01T08:00:00+08:00 | 缺帧与陈旧帧不同，恢复任务成功不认证物理风险；安全设计反证。3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Safety envelope，实际POST通过 |
| [Two-step Flow VLA](https://arxiv.org/html/2609.39822v1) | 2026-10-01T08:00:00+08:00 | 近action区间可另学平均velocity，NFE减少与控制质量必须分账；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，solver分支，实际POST通过 |
| [Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/html/2609.39816v1) | 2026-10-01T08:00:00+08:00 | batch形状确定性不保证早先token不受未来影响，低精度累加需条件化prefix不变性。3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值合同，实际POST通过 |
| [HAPMoE](https://arxiv.org/html/2609.39350v1) | 2026-10-01T08:00:00+08:00 | 异构stage不能事后固定同构EP/TPE，需要device-aware联合容量/通信/分区计划；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`TRAIN-PIPELINE-PARALLEL` / [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)，Stage Balance，实际POST通过 |
| [ThunderEP](https://arxiv.org/html/2609.40093v1) | 2026-10-01T08:00:00+08:00 | host-only通信的relay traffic与依赖链收益不同，prefill DMA不能直接移植captured decode；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，多路径分支，实际POST通过 |
| [Gradient-Conflict Audit](https://arxiv.org/html/2609.38465v1) | 2026-10-01T08:00:00+08:00 | 降冲突proxy不等改善任务，诊断有效性须区分预测/同期、干预/结果与population；设计反证加深。3+1+2=6 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，多模态方差冲突后，实际POST通过 |
| [CW-OPD](https://arxiv.org/html/2609.38777v1) | 2026-10-01T08:00:00+08:00 | 单world端点匹配不约束跨视觉响应，共同logit变化消项仅限transition；长期缺口加深。2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，teacher对照分支，实际POST通过 |
| [S-OPD](https://arxiv.org/html/2609.39120v1) | 2026-10-01T08:00:00+08:00 | teacher只选学生视觉contrast位置，mask敏感与noise稳定是不同辅助目标；长期缺口加深。2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，视觉选择分支，实际POST通过 |

## 4. 证据与知识整合

### [Disrupting a coordinated model distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/)

采用09/30官方说明“About the attack / Responding”及尝试数量脚注，访问2026-10-01。RSS原值 `Wed, 30 Sep 2026 10:30:00 GMT`，不是列表发现日。厂商报告的是reasoning artifact重放与边界强化，不是密码破解或独立复现；数量不能当成功率。关联旧arXiv只作背景，不在本窗重新入选。

Ch72 `Hidden Reasoning Trace 不是 Secrecy Boundary`已有隐藏界面与opaque handle读取授权，但未具体承载可重放reasoning对象的跨身份/model-family消费权限。新增段落位于SecureClaw读取边界之后、context-membership之前：区分artifact admission与output release，保留迁移便利、延迟/缓冲/误拒及answer-only回退；这些工程取舍不冒充厂商实现。实际family标记 `SF-2026-OPENAI-DISTILLATION-CAMPAIGN`，非作者来源/owner PRE及实际邻接POST通过。

### [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

采用当次发布原文受限访问与monitor/sandbox说明，访问2026-10-01。JSON-LD `datePublished=2026-09-30T20:00:00+00:00`；modified字段不是首次公开。它是厂商公开事实，不提供反馈分离的可比消融、安全充分证明或完整性能contract，不采用裸benchmark。

Ch72已具体承载sensor不是authority、runtime暂停身份及sandbox；不重复整套release recipe。窄增量只把monitor证据、incident处置与训练目标lineage分账，插在runtime身份之后、attempt opportunity之前，保留审查/修复延迟与未知谱系暂停自动回灌。`SF-2026-GOOGLE-GEMINI4-ARGON`实际正文已写；“谨慎避免反馈”不扩大成已证明零回灌。非作者PRE及实际邻接POST通过。

### [TomasuLLM](https://arxiv.org/html/2609.38201v1)

采用精确v1 §3.1–3.8、§4、§5.1–5.4及直接相关A.3–A.5，访问2026-10-01。本窗arXiv首公开按Thursday 1 October官方列表和公告规则确定：09/30 20:00 EDT即10/01 08:00北京时间；Submitted不是公开时刻。以下arXiv v1均沿此依据，未见当前官方撤回说明。

隔离状态分支可以提前真实执行工具，但文件已写与进程已加载的operand readiness不同；提交时分别验证canonical action、当前依赖/loaded version、wrapper观测与effect可晋升性。预测观测不同可只使后继失效，不抹掉已经验证的当前真实结果。局部process-tree trace不覆盖所有daemon、remote、network和随机输入，未捕获或不可逆effect须barrier。4,010抽样审计之外另有390 barrier；20故障注入和所测wrapper无false acceptance不是普遍安全认证。实验三次fresh paired，额外drafter/GPU、分支准备与CPU成本存在；超时任务按matched progress，不冒称全部完成，未复现或核代码。

Ch81原有learned transition、COW与live-log晋升，但缺真实工具operand和四类frontier validation的交接；正文在COW分支之后补这个差额，保留短工具/吞吐优先时串行基线，`SF-2026-ARXIV-2609-38201`实际写后独立通过。实验配置及反证见[必要证据§4.1](../_sources/daily-20261001/ARXIV.md#41-tomasullm-38201必要源实际owner-ready拟窄i)，不将作者局部加速泛化为生产SLO。

### [The System Prompt Illusion](https://arxiv.org/html/2609.38205v1)

采用v1 §3、§4、§5.5–5.8、§6。差向量probe预测prompt类别、CKA描述几何、十个coding query的code-fraction patch分别对应可读、相关和局部介入；安全/permissive profile相近不证明相同安全circuit，也没有controlled jailbreak支撑普遍安全因果结论。原文null均值/标准差与“300标准差”量级不一致，不采用该认证；英语、模型规模、模板与prompt长度混杂、单forward及局部patch反例保留。17模型、20prompt×100query、greedy/seed42/max200、BF16 inference/FP32 CKA等仅是白盒测量协议，不是部署性能结论。

Ch5的correlation→prediction→causation及readout→局部intervention→跨context检验，实际承载拟采用的分账命题（约208–232行）；独立源和具体正文复核通过，故不重复改书。CKA阈值配方、未核完整数学证明及安全机制强解读没有被“已有覆盖”标签吸收。[具体证据§4.3](../_sources/daily-20261001/ARXIV.md#43-system-prompt-illusion-38205必要源具体窄e-ready)。

### [Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2609.38222v1)

采用v1 §3.2、§4.1–4.6、§5.1–5.3、§6 Table2、§7–8。评价事件是所有保留claims被verifier标为支持，空输出可使marginal Full Support成功；95%目标不自动保证已回答条件下的95%支持。每dataset60题、30/30校准测试、100 seeded resplits复用同generated artifacts，非100独立生成；同backbone及reference verifier仍有共享错误、标签与真值边界。Table2的GPT-4o-mini在95%目标下，HotpotQA/NQ的nonempty为10.80%/9.70%，条件FS仅78.48%/71.72%，不能只报高marginal FS。最多3hop、k10、阈值0.3；硬件、precision、concurrency、SLO和端到端成本Not Disclosed，不由此推多hop普遍更优。

Ch66已有abstention-inclusive marginal risk≠answered selective risk以及oracle≠semantic truth，另有exchangeability/recalibration（约608、624–626行）；独立实际正文确认这几个窄命题，故已有覆盖。多hoprecipe、全部数值或自动verifier正确性不宣称已进入Books。[具体证据§4.2](../_sources/daily-20261001/ARXIV.md#42-multi-hop-conformal-38222标准必要源具体窄e-ready)。

### [SpecScale](https://arxiv.org/html/2609.39334v1)

采用v1 §3.2、§4.1–4.3、§5.1–5.6。一个distinct prefix forward后按logical multiplicity独立抽样，不是共享随机draw；PRM跨请求flush由profile token规模、sibling完成与defer计数触发。step-top-k剪枝不是搜索最优证明，满分早停会改tie选择；较大batch可降吞吐、部分质量切片退步，FastTTS仅重实现部分机制。A10080GB/Xeon6326、Qwen2.5-3/7B或Llama3-3/8B及PRM7/8B、temperature0.8、max40steps、width4、主实验最多32并发；precision/跨run误差Not Disclosed，normalized latency不是P99 ITL/SLO。Ch46 iteration工作单元之后补logical/physical work分离和PRM三类排队责任，独立必要证据与实际邻接POST通过；未把sampling law等价当作浮点路径逐位一致或lossless search。详见[必要证据§7.1](../_sources/daily-20261001/ARXIV.md)。

### [Preserving Provenance in Shared KV Caches](https://arxiv.org/html/2609.38706v1)

采用v1 §3、§4.1–4.3、§5.1–5.4、§6.3–6.5、§7，访问2026-10-01。计算provenance与sharing permission是不同不变量；request adapter/salt和worker resolveddtype/weights/KV representation需用稳定、规范descriptor贯穿lookup/store，进程handle或路径不足。有限registry与hash/key转换假设不认证未声明维度，差分checker看KV变化也不能独自发现授权错误。所测connector/release反例有具体版本边界，SGLang0.5.20已绑定salt，不称所有当前实现都同样失效；跨精度输出变化不自动等于accuracy退步。单host配置不是多host fleet；identity fingerprint和固定预算下的存储/eviction代价未消失，无可分辨延迟差不等于零成本。未核公开代码或复现实验。

Ch45原Prefix reuse已列模型/adapter等身份，但缺local→shared等价类如何保留和双端绑定；新增该具体桥接及反证/fallback，独立PRE与实际邻接POST通过。与Ch52路由只作分工，不在两章重复机制。`SF-2026-ARXIV-2609-38706`。

### [Vosti](https://arxiv.org/html/2609.38981v1)

采用v1 §2.2–2.3、§3、§4.1–4.3、§5.1/5.3、§6.1–6.2、§7，访问2026-10-01。固定模型、dtype、部署和sampler初态的per-request trace前缀可比较，靠canonical cold-prefix KV、逻辑/物理映射、写隔离、lookup-before-publish与kernel relational合同组合；masked额外tile需精确identity transition，不借浮点重结合证明。engine证明依赖kernel合同，translator/solver/编译GPU可信，finite-input假设未运行时检查，功能正确性与liveness不在该性质内。7模型H200 BF16有限cases不能推生产全输入、多GPU或跨编译器；固定特化可能利Decode而损Prefill。未审代码或复现，不采用脱离warmup/batch/上下文配置的性能保证。

Ch49原特定epilogue确定性之后新增wholeengine组合合同，再交接近似恢复分支；独立PRE与实际邻接POST通过。它不是把原容差验收改成“通用零误差”，`SF-2026-ARXIV-2609-38981`。

### [KVTether](https://arxiv.org/html/2609.39819v1)

采用v1 §4–7及§8.1/8.3–8.5。Harness按程序顺序维护message版本，replace/remove使下游prefix-dependent KV失效；fork后context lifetime独立，物理page取所有live引用最高priority，在途消费结束且无有效引用才回收。Suspended内MRU借等待顺序作启发式，不是全局最优或永久pin；无lifetime消融可退步。三工作负载每个400任务、5RPS，但在线trace与两离线重建不同；实际GLM4.7/SGLang0.5.8、三节点12 GB200使用匹配长度的随机prompt和记录的tool等待，非真实任务语义闭环。Precision/SLO Not Disclosed；256K mapping约350ms未包含在primitive或通知小数字中，费用按另模型价格估算不等实际账单，未核实现。

Ch45已有typed region和policy hint，但缺ordered mutation→prefix invalidation及跨context回收fence；在其后补这个实际差额和有限MRU，非作者PRE与实际邻接POST通过。[源包§7.2](../_sources/daily-20261001/ARXIV.md)，`SF-2026-ARXIV-2609-39819`。

### [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/html/2609.39131v1)

采用v1 §3.2–3.3、§4.2–4.3 Eq7、§5.1–5.5 Eq8/Table1/3/4。模拟器分别跟踪HBM/HBF/host tiers，hit减少计算/迁移而仍锁完整prefix容量；buffer限制admission压力，不是固定物理partition，也不禁止后续decode增长。写寿命基于均匀wear、单位write amplification与100k P/E等假设外推，非商品设备实测保证。B200计算模型、16-bit weight/cache存储、FP8 index timingproxy，H100/B200 kernel calibration不等HBF controller实测；LMCache multi-turn session复制不是独立轨迹，初请求同时到达，后续按原gap，无外部到达率或latency SLO，mean TPOT可能与吞吐相反。能耗模型不计static package power，轻负载能耗可反升，未核代码/复现。

Ch54原层级容量/搬运缺flash write-endurance与headroom耦合；在扩展层级初句后补锁定容量、写入压力和模拟边界，再交接不同远端访问接口。独立必要证据、actual owner与真实两段邻接POST通过，`SF-2026-ARXIV-2609-39131`；不把作者模拟速度或寿命写成普遍硬件规格。

### [The Planning Limits of Latent World Models](https://arxiv.org/html/2609.39235v1)

采用v1 §3 Eq1、§4–6.3、直接相关AppB/C、D.1/Table4、E/Table5。K为想象长度、L为goal lookahead；perfect simulator和true-state距离也出现短视目标评分失败，不能只归因transition误差。P*为有限tested L诊断，不保证单调、0不等于零成功；扩大predictor或训练展开也不自动补score视野。增加K、近subgoal和MPC分别改变不同选择；等展开预算是candidates×steps×iterations（连elite数也变），不是同wallclock/FLOPs，部分任务仍退步。专家同episode subgoal有privileged信息，Bridge仅offline、控制步时不同，硬件/precision/concurrency/SLO Not Disclosed，未核代码。

Ch25原Imagined rollout解释累积误差/uncertainty课程，但缺精确预测仍短视的goal-ranking边界；在课程之后、Computer-use前新增K/L/训练深度分账及各补救成本。独立PRE与actual邻接POST通过，`SF-2026-ARXIV-2609-39235`。

### [U-Fuzz](https://arxiv.org/html/2609.38275v1)

精确v1 §3–6与Appendix A必要范围：同checkpoint两个隔离副本每次只改query或memory state；变异器的descriptor与判错reference分权，检索未找到不能证明无支持。探索以有限义务及behavior novelty扩展，failure label不参与本分支的保留/排序；coverage非稳健性证明。四backend三run、同有效执行预算只提供受限互补证据，不等相同总生成/验证费用；output-only子集不能诊断内部原因。硬件、precision、完整费用及SLO未披露，未核实现。详见[源包§7.3](../_sources/daily-20261001/ARXIV.md)。Ch77原Recall/Use分账之后补checkpoint变异与oracle/探索分权，两段实际PRE/POST由非作者通过，`SF-2026-ARXIV-2609-38275`。

### [StateFork](https://arxiv.org/html/2609.38648v1)

v1 §2–6/AppA.1：固定context下future-action observation equivalence是恢复合同，不是全host bitwise证明；persistent shell/PTY、process image、filesystem lineage和mount须组合恢复。逻辑分支可即时checkpoint或从最近物理节点重放suffix，但时间/remote API不自动可回放。受控本地session含单run宏实验，大resident memory可能失去优势、组合restore比bare CRIU贵；不认证恶意tenant、分布式snapshot或生产tail，precision/API细配置Not Disclosed。[源包§7.4](../_sources/daily-20261001/ARXIV.md)。Ch81联合恢复后补session组成和logical/physical materialization，非作者实际邻接POST通过，`SF-2026-ARXIV-2609-38648`。

### [Blackout and Freeze](https://arxiv.org/html/2609.39145v1)

采用v1必要方法、phase/length消融及物理反侧：zero-black缺帧与重复陈旧帧不同，恢复success也可能伴更高contact/drop。模拟及真实controller/频率、step与episode分母分开；WidowX有限实机含operator/deadman与early stop，不授普遍安全。单seed及有限重复不能变成稳定性保证，训练BF16不补造推理GPU/precision/concurrency/SLO。Ch26 Safety envelope开头补感知新鲜度与安全/成功分账，保留override与旧基线；实际PRE/POST通过，`SF-2026-ARXIV-2609-39145`。未核代码/复现。

### [Two-step Flow VLA](https://arxiv.org/html/2609.39822v1)

采用v1方法、evaluation及solver反侧：同expert先走粗区间，再学近action区间平均velocity；candidate/two-halfstep teacher target stopgradient，但共享参数仍更新，不是两套冻结expert。选定τ的profile不是全field最优证明。π0.5/Piper/JAX/4090D有限任务中减少NFE伴success及continuity反退，排首次JIT的solver计时不等端到端5倍；离线第一action误差不认证整chunk闭环，camera/state/publication时钟必须分开。Precision/concurrency/SLO Not Disclosed，未核代码。Ch26原solver分支之后补区间目标及控制质量验收，actual PRE/POST通过，`SF-2026-ARXIV-2609-39822`。

### [Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/html/2609.39816v1)

采用v1 §2.2–2.3、3.1–3.3、4.1–4.4、5及Appendix A.1.3 Proposition1直接证明。固定batch形状的repeat determinism不保证早先输出不受未来token影响；row-local量化/scale group与累加路径须保持prefix不变性。混合整数消项的exactness要求block code bound、全部partial sum及转换满足精确表示范围，不自动延伸完整误差界或BF16等价。小code range损质量、扩大range需correction额外乘积，H20实际kernel反更慢，算术量节省非wallclock收益。Ch49 wholeengine合同后补该条件化numerical分支，非作者实际PRE/POST通过，`SF-2026-ARXIV-2609-39816`；未核实现或复现。

### [HAPMoE](https://arxiv.org/html/2609.39350v1)

v1 §3–5、Limitations/AppA–B：profile后联合PP/TP/DP/EP/TPE/CP、非均匀layers/device及recompute，区分已重叠与暴露dispatch/combine。Pruning与受限cost模型不授全空间最优；warmup-before-training离线计划，不支持动态重配置。BF16/top2/seq4096等各comparison保globalbatch，跨cluster不合并；作者adapted baselines及整栈结果不能隔离单维因果。正文收益区间与Table3不一致、dense硬件名单冲突，均不采用相应数字；短search time不含完整profile成本，未核代码/长程收敛/生产tail。Ch38原L/p估算后补EP/TPE不能固定带入异构stage与联合materialization，实际非作者PRE/POST通过，`SF-2026-ARXIV-2609-39350`。具体条件与反证见[§7.5](../_sources/daily-20261001/ARXIV.md)。

### [ThunderEP](https://arxiv.org/html/2609.40093v1)

v1 §2.1–2.2、4–5：host-only shared medium减少dispatch重复relay，GPU combine主要减少依赖链而非bytes；payload/flag分离且最后receiver credit才reuse。Prefill双向DMA/SM分工，decode为captured graph保留SM搬运；routing-aware小DMA与CPU reduction负收益保留。两单NUMA六consumerGPU/noP2P、vLLM/NCCL、BF16与native MXFP4各自比较，120B转BF16 OOM不构同precision胜出；五run平均TTFT/TPOT不是tail/SLO/数值等价。N=2无traffic优势，大combine接近原bandwidth，未核代码/训练反向。Ch36多路径之后补host-only替代分支及phase限制，非作者实际PRE/POST通过，`SF-2026-ARXIV-2609-40093`。[配置与关键消融§7.6](../_sources/daily-20261001/ARXIV.md)。

### [Gradient-Conflict Audit](https://arxiv.org/html/2609.38465v1)

采用v1 §3–5及直接相关Appendix C–E：早期proxy预测最终任务与同期checkpoint相关分开，cluster bootstrap保留同run依赖。63base runs的252checkpoint加其他人口共93runs/372checkpoint，不视为372独立重复。α投影降低干预后方向冲突，改变norm且raw梯度会适应；有限seed噪声及CI不证明所有功能interference或gradient surgery无用。Generation失败切片改变normratio含义，自洽也可能坍缩；method简化不能用来否定原optimizer。M4Max/MPS/float32合成小decoder不授生产UMM结论。Ch28旧projection proposal/heldout gate之后补proxy构造有效性，非作者实际PRE/POST通过，`SF-2026-ARXIV-2609-38465`。[必要协议与反证§7.7](../_sources/daily-20261001/ARXIV.md)。

### [CW-OPD](https://arxiv.org/html/2609.38777v1)

v1 §3–5与A/B/C/E直接相关段：固定A rollout prefix在原图/编辑图各匹配endpoint，另蒸馏归一log-prob变化。共同加性logit不影响transition target，不使endpoint或整体loss免疫错误；B非独立on-policy trajectory，opposite错误的直接反例保留。VLM验编辑不是严格单变量证书，低fliprate可能两边同错；同预算λ=0支持局部分工，不认证真实视觉因果。主EMA teacher γ=.05与frozen扰动人口分开；主文4GPU/AppE2GPU不合成总cost，precision及一致完整CW计时Not Disclosed。Ch33原privileged-context区间之后新增endpoint/transition两target及fallback，独立PRE与实际邻接POST通过，`SF-2026-ARXIV-2609-38777`。[源包§7.8](../_sources/daily-20261001/ARXIV.md)。

### [S-OPD](https://arxiv.org/html/2609.39120v1)

v1 §3–5/A1/A3/B1/B3/B6：teacher原图对遮挡图概率下降只提供位置gate/权重，学生mask contrast与noise agreement形成辅助目标；masked/noisy支路每update stopgradient，sampled-token surrogate非真值。Count-matched random及全token反侧限定“更广更好”；text oracle改变输入，4B oracle准确率自身降低，gap变小不独证感知改善。四A10080G的time/step含额外16%/28.6%，排初始化/保存/validation；无新增部署module不等训练免费，precision/跨train seed及SLO未披露。Ch33承接CW后补teacher选择与学生双目标的不同分工，独立PRE与实际邻接POST通过，`SF-2026-ARXIV-2609-39120`。[源包§7.9](../_sources/daily-20261001/ARXIV.md)。

## 5. 缺口与下一步

普通待办：无。非作者日级汇总复核已通过。

外部终态保留项（有限原始替代已用完，只恢复本窗对应入口，不扩大旧研究；均不用于正面证据、Books或无遗漏保证）：

- [Qwen Research/Blog](https://qwen.ai/research)：fresh原HTML/公开脚本仍为应用壳，浏览器替代超时；缺可确定本窗公开时间的研究目录。可接受官方带日期列表或具体文章/论文链接，重开SRC-QWEN未覆盖入口。
- [Seed Blog](https://seed.bytedance.com/en/blog)：无可提取文章目录；papers/research最新前缀已检查但不能替Blog。可接受官方带日期Blog列表/单文，重开SRC-BYTEDANCE-SEED的Blog子入口。
- [MiMo Blog](https://mimo.xiaomi.com/)：15卡片无时刻，首文已核09/27窗外，余项缺可靠日期；公开JS不能由首卡推全列表零。可接受其余卡片原文的公开日期/官方说明，重开SRC-XIAOMI-MIMO Blog未核日期项。
- [MiniMax Agent Tech Blog](https://agent.minimax.io/docs/techblog)：原页为空，官方llms索引定位techblog.md仍打开失败；缺本窗带日期目录与具体正文。可接受官方MD/HTML文章或带日期目录，重开SRC-MINIMAX Agent子入口。

Meta混排、Google pubs年份目录与DeepSeek ShowAll另限制相应辅助/后续入口；已检查的最新前缀不代表全机构零遗漏。性能、理论或安全结论的未披露条件和冲突数字已在§4收窄/不采用；这些不是新增无身份全文请求。旧版本比较不作为常规队列，九个具名Replacement只限当前说明与已完成的定点核对。

## 6. 复核

复核者：`sep22_resume_v3`（最终非作者日级Gate，2026-10-01T15:06:01+08:00）；`apr29_close`参与独立分批来源/实际写后核。复核者均未写本报告或本日Books。

结论：通过

最终实际复读六部分、两份源包的停止范围/冻结记录；核14来源到安全终态、日期/版本/准入、21唯一家族及19采用标记。全部候选的必要证据与具体owner PRE、实际两段及邻接POST按未变身份/命题有效复用：sep22亲核机构2与arXiv13（含2窄已有覆盖），apr29独立核其余6。既有覆盖只对应Ch5读出/因果分账和Ch66弃答分母/oracle权限，不称整配方已有。

排除抽检为机构2个核心说明（小企业支持、机器人职业估计），arXiv2个完整题摘（38203临床ASR、38219语料workflow）；代表来源/主题/理由，不是全部negative全文验证。风险检查核9具名当前Replacement说明及已完成的5个定点摘要比较，TensorHub收窄与现有owner一致；未将摘要相同当正文未变，未继续版本全量比较。没有验证所有分类/Revision、未读标题或互联网零遗漏；四外部子入口保留隔离，不作为Coverage或Evidence正面通过。

正式V3格式/一致性、21行与21证据节、本地链接/六标题/围栏、Stable ID及19采用标记唯一性检查通过；两源包和13个实际Books的限定`git diff --check`通过。全仓未暂存`git diff --check`通过；暂存区仍有本轮前的空白告警，未修改。保护既有staged/unstaged，未stage、commit或push。脚本通过不替代上述语义验收，未声称核代码或复现实验。
