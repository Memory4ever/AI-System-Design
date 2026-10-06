# Daily Research — 2026-01-10

**规范：** V3
**窗口：** 2026-01-09T09:00:00+08:00 ～ 2026-01-10T09:00:00+08:00
**窗口说明：** 用户明确要求已有Daily只增量补遗漏，保留原窗口、候选日期及有效证据，不搬原候选；新增材料按前一完整自然日检查。
**补充窗口：** 2026-01-09 ～ 2026-01-09
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T02:13:19+08:00
**补充检查时间：** 2026-10-07T17:40:32+08:00

## 1. 结论

2026-10-07本轮增量检查Jan09完整自然日已独立验收通过，原17家族及其评分、公开归属、有效审阅/Books写后验收均保留。实际14源切片、有界主题发现与有限停止见[增量记录](../_sources/daily-20260110/supplement-20261007.md)。本轮41份完整精确v1题摘经独立准入校准：36新增论文家族、3论文贡献前关闭、2必要日期保留；另Datadog官方核心贡献前关闭。36新项必要审阅与实际owner处置完成，33项新增Books实际整合及非写入者POST通过、3项已独立决定仅报告；扫描、筛选、审阅、Books与复核的普通可执行待办为0，完整增量DAY通过见[非报告作者验收§8](../_sources/daily-20260110/post-audit-20261007.md#8-01-10-增量日级非报告作者验收)。Kimi0.73作为原版本家族补充事件深入完成、仅报告，旧3分不变；原17＋新36=53正式家族，不把两个日期保留先纳入。完成只表示本次安全终态，日期、中心争议及具名历史来源限制仍隔离，不授正面Coverage/Evidence或无遗漏保证；以下原轮结论只授其原范围。

本日从当前原始来源独立重建，不采用旧 Daily/Weekly 候选、评分或完成标签。14来源已作本窗有限入口检查，原始主题查询、历史字段和停止点均保留；不是全机构、全分类或全互联网无遗漏。本日21份唯一完整新题摘分为16正式论文家族、4贡献前关闭及1日期保留；另Kimi两release经接口核心定点重开，作为1正式版本家族，合计17正式。SB Energy官方核心负侧与MiMo/TRecViT旧body身份另检，不把收录或版本号单独计新事件。

17项逐项必要处置已完成：8实际Books整合并非作者POST通过（CC++、LaST、CounterVid、GDPO、RoboVIP、rank-one编辑反证、GenProve、RelayLLM），1具体已有覆盖，7仅报告，1中心争议终态隔离。GDPO原已有覆盖提案经具体owner核纠正后落实窄差额，Kimi原功能名关闭也经实际patch检查纠正为受影响兼容契约的深入版本审阅，均保留改判依据。STDD日期下界未知不进正式分母；机构历史目录与公开revision/mirror限制安全保留。root已完成最终来源、日期、具名负侧及六部分独立日级验收，普通可执行待办为0；这些保留项不算正面Coverage/Evidence或无遗漏保证。

## 2. 来源覆盖

原始查询及停止位置保留在[本日记录](../_sources/daily-20260110/DISCOVERY.md)、[原生字段](../_sources/daily-20260110/PRIMARY_META_RAW.json)、[历史API](../_sources/daily-20260110/HISTORY_API_RAW.json)。只检查指定主题和日期邻接段，不把宽目录变为逐项题摘队列。

下表原检查事实保留。本轮Jan09自然日fresh切片补充如下（精确入口/参数见[增量记录§1–2](../_sources/daily-20260110/supplement-20261007.md)）：OpenAI RSS1251items仅日期过滤，Datadog新事件核心关闭；Anthropic SSR CC++官方BJTJan10窗外不搬原arXiv；Google月目录9项Jan28→Jan12末、DeepMind page3 Feb05→Jan09旧TRecViT→Dec03停止，pubs仍受限；Meta0可读+两窄域查询不授0研究；Qwen配置60项末Dec23；DeepSeek更新Apr24→Dec01；Moonshot release page1/100跨本窗，0.73自然日事件已纠正/深入，仅报告。Hunyuan publicList page1/size100/render0实际9项末Feb03；ZAI page1/2到hasMorefalse，Jan13→Dec21；Seed升序2026 paper/blog首20/9，最早Jan20/Feb12故停止更晚页，不继承旧77/82差额。ERNIE首10 Jan15→Jan08→Dec23止；MiMo8Paper与16具名Blog路由/6inline+10iframe实际恢复，Jan08旧Flash身份及一无日期同body去重，没有可核Jan09新Blog；MiniMax中英Jan27/28→Dec23，TechBlog.md实际页末唯一May13事件，当前正文访问故障已恢复，但历史删除索引仍隔离。arXiv四主题model123/123、runtime70、multimodal34、agent90=317跨组原始重复命中，仅作有界标题发现，追加完整题摘总41，不授317语义关闭；lastUpdated被改写Submitted不授revision阴性，必要公开日采用首次ID公告下界＋findable上界联合核日，不用注册直接授公开。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原RSS/SB核心有效记录保留；本轮RSS1251 items只按Jan09邻接过滤，SB Jan09T11Z复用、Datadog Jan09T00Z＝BJT08:00的新自然日事件实际读核心后独立贡献前关闭；Jan08两项停止 | 已检查 | 当前feed不保证删除/未索引历史；宽items非逐项语义队列 |
| SRC-ANTHROPIC | 原CC++ exact-v1有效证据保留；本轮Research SSR publishedOn Jan09T17:17Z→Jan08相邻段，官方CC++实为BJTJan10，不移原arXiv事件；更晚Jan14停止 | 已检查 | 目录未索引历史与公开镜像不作全量保证 |
| SRC-GOOGLE-AI | 本轮Google Research Jan2026月目录9标题Jan28→Jan12到页末无next；DeepMind page3 Feb05→Jan09 TRecViT→Dec03/Nov21停止，旧body身份去重；pubs year2026未取到 | 已检查 | 月/选取目录非全部Google事件；pubs访问受限，收录日期不是新正文 |
| SRC-META-AI | 本轮Research实际0可读行；官方域两查询January 9, 2026 research、Jan 9, 2026 LLM agent inference均empty，有限恢复停止 | 受阻 | 目标窗可验证历史索引未恢复，不由empty推0研究；本窗终态隔离 |
| SRC-QWEN | 本轮官方page_config research-list60卡，完整date字段最大2025Dec23T05:08:30Z；有限配置读取停止 | 已检查 | 2026删除/未索引历史未恢复，配置不授本窗完整性；60卡非题摘队列 |
| SRC-DEEPSEEK | 本轮首页和Change Log日期桥接Apr24_2026→Dec1_2025，止相邻段；原有效记录保留 | 已检查 | Changelog不是全部研究公开事件 |
| SRC-MOONSHOT | 本轮Kimi Blog最近2025Nov07；release page1/per_page100从Sep22_2026至Oct24_2025跨窗停止；0.74/0.75原证复用，0.73 Jan08T16:54:15Z＝BJTJan09新增事件，完整body与PR575/576/568/584/585/587必要patch独核深入，仅报告 | 已检查 | 只到page1及具名接口变更；不遍历全release/PR，不授运行/认证安全 |
| SRC-TENCENT-HUNYUAN | 原size1000记录保留；本轮Research骨架后publicList page1/size100/render0，code0/total9/list9到页末、最早publicAt Feb03 | 已检查 | 当前9项不能恢复Jan09删除/未索引历史，publication/display/update不混用 |
| SRC-ZAI | 本轮官方Research正确page1/2，page2 hasMorefalse到末；publication Jan13→Dec21/Dec10–07跨界停止 | 已检查 | 未索引/删除历史不获覆盖；CMS created/updated Jan07–08不等公開 |
| SRC-BYTEDANCE-SEED | 原分页77/82及blog14/19事实保留；本轮article_type1/2/year2026/count20/token0/order_desc=false，论文20/82、Blog9/23，首公开Jan20/Feb12已晚于上界故停止更晚页 | 已检查 | 本轮有限升序切片不认证隐藏/删除历史；不继承原差额作本轮命中或队列 |
| SRC-BAIDU-ERNIE | 本轮中文Blog首10条，Jan15→Jan08→Dec23跨界、next page2/2，止本日期段；原有限记录保留 | 已检查 | Jan08 date-label无时区，不补秒，当前切片非全部历史事件 |
| SRC-XIAOMI-MIMO | 本轮Paper8项Jan08 Flash邻接Feb03/Oct21；frontend恢复16具名Blog route，6inline+10iframe实际读取日期/body，无可核Jan09新Blog；一无日期Flash同body去重 | 已检查 | 无日期body不补公開事件，Updated/v2号不证明重要修订，删除/改写历史不授阴性 |
| SRC-MINIMAX | 本轮中英Blog Jan27/28→Dec23跨界；Agent TechBlog.md正文已恢复，唯一May13_2026条目到页末；原正文失败不再当当前访问障碍 | 已检查 | Jan09删除/未索引历史仍隔离，当前文档/IPO报道不代替历史研究队列 |
| SRC-ARXIV | 原8主题失败/100元标题有限记录保留；本轮4主题Submitted缓冲Jan07T19Z→Jan08T19Z，model123/123、runtime70、multimodal34、agent90，317跨组重复题名仅发现；41完整exact-v1题摘分36准入/3关闭/2日期保留 | 已检查 | Submitted非公开；lastUpdated被改写不授revision阴性。首次ID公告下界+findable上界仅核具名日，公开revision/镜像与延期ID日期限制隔离，不称317逐项关闭 |

## 3. 候选与判断

原17家族（16论文+1Kimi版本家族）的逐项处置、8实际POST及原轮日级验收仍保留。本轮新增36论文均已核Jan09自然日归属、通过准入并准备必要证据，接入下方同一连续表，总53家族；其中33项新增Books实际POST已通过、3项仅报告已独立决定，36项Books处置均实际落实且必要非作者POST通过，无普通Books待办，不把提案当整合。另STDD、MoEBlaze和SPINAL的必要首公开界只在§5保留，不混入本表。Kimi0.73是同一家族补充事件，不增加分母；宽元标题、关闭项及受阻日期不计正式候选。

原候选arXiv区间为有条件的首次公告范围：官方排程及ID首次announcement才分配且不能提前，与原Submitted均在Jan7T19Z之后、Jan8T19Z之前及注册可访问upper共同约束。不是Submitted或registered=public；原字段保留在[首次三项](../_sources/daily-20260110/PRIMARY_META_RAW.json)及[其余字段](../_sources/daily-20260110/BACKSTOP_DATES_RAW.json)。BJT起点均Jan9T09，终点保守写到原upper之后一秒，均完全落原窗；原有效日期字段不移。新增36项只填已核公开日2026-01-09，联合公告下界/已findable上界的实际逐ID值见[增量记录§2](../_sources/daily-20260110/supplement-20261007.md#2-有界arxiv发现与首批准入)，不补造精确公开时刻。原项目定点查漏见[恢复边界](../_sources/daily-20260110/PROJECT_DATE_BOUNDARY_RAW.md)，未取得更早可核首公开事件，不等于证明作者镜像/修订不存在。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GDPO](https://arxiv.org/html/2601.05242v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T11:02:39+08:00 | 各reward单独归一再组合改变多奖励objective；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [LaST](https://arxiv.org/html/2601.05248v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T11:02:47+08:00 | slow latent cache与fast fresh observation双时钟及mixed-ratio训练；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [CounterVid](https://arxiv.org/html/2601.04778v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:52:22+08:00 | 视频输入对与答案输出对定义不同偏好条件；2+1+2=5 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [CC++](https://arxiv.org/html/2601.04603v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:48:33+08:00 | exchange关联与廉价probe升级级联安全检查；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [RoboVIP](https://arxiv.org/html/2601.05241v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T11:02:38+08:00 | 保留动作轨迹的多view inpaint与视觉exemplar训练接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MiJaBench](https://arxiv.org/html/2601.04389v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:43:52+08:00 | 总体安全可掩盖target群体条件差异；3+1+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Merging Triggers, Breaking Backdoors](https://arxiv.org/html/2601.04448v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:45:09+08:00 | defender poison引入trigger interference再clean recovery；2+2+2=6 | 深入完成 | 仅报告：受限修复recipe未给可迁移trigger选择或repair contract |
| [On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions](https://arxiv.org/html/2601.04600v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:48:29+08:00 | edit recall与two-hop可用性分离，跨层冗余有locality代价；3+1+2=6 | 深入完成 | 整合：MODEL-FFN [Ch16](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [When More Words Say Less](https://arxiv.org/html/2601.04609v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:48:40+08:00 | 固定长度下contrast-set specificity区别于verbosity；2+1+2=5 | 标准完成 | 仅报告：局部图像描述测法不新增真实性或task utility合同 |
| [Prior-Informed Zeroth-Order Optimization](https://arxiv.org/html/2601.04710v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:50:53+08:00 | elite/bottom perturbation ranking改变局部ZO方向；2+1+2=5 | 标准完成 | 仅报告：未有可信跨配置alignment/全成本成立规则 |
| [AM3Safety](https://arxiv.org/html/2601.04736v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:51:27+08:00 | turn risk variance及低mean penalty改变reward权重；2+1+2=5 | 标准完成 | 仅报告：阶段/judge人口内recipe，未给可迁移turn-importance准则 |
| [Judge Decoding via Distributional Divergence](https://arxiv.org/html/2601.04766v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:52:07+08:00 | KL阈值决定draft/target切换，代价是非exact分布；2+1+2=5 | 标准完成 | 仅报告：局部judge selector，理论强保证隔离 |
| [Token Maturation](https://arxiv.org/html/2601.04854v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:54:03+08:00 | 连续token buffer逐步更新与commit替代离散采样；2+2+2=6 | 争议 | 暂缓：α corruption/commit/loss身份见§5 |
| [GenProve](https://arxiv.org/html/2601.04932v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:55:45+08:00 | 联合生成claim及typed provenance，而匹配不等entailment；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Compositional Steering with Steering Tokens](https://arxiv.org/html/2601.05062v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T10:58:36+08:00 | 冻结单行为tokens后只学习composition token；2+1+2=5 | 标准完成 | 仅报告：局部参数权限recipe未形成跨语义/高阶controller合同 |
| [RelayLLM](https://arxiv.org/html/2601.05167v1) | 2026-01-09T09:00:00+08:00 ～ 2026-01-09T11:00:55+08:00 | learned token-span handoff使两模型消费不同rendered history；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Kimi CLI 0.74/0.75](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.74) | 2026-01-09T21:23:56+08:00 ～ 2026-01-09T22:47:54+08:00 | ACP model/thinking持久化与ReadFile typed-media返回改变版本兼容契约；1+1+1=3 | 深入完成 | 仅报告：局部版本调用/配置接口，不授新通用安全或可靠性保证 |
| [MuLo-SD](https://arxiv.org/html/2601.05149v1) | 2026-01-09 | lowresolution draft/learned映射与二维local rejection expansion改变纠正边界；2+1+2=5 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Not All Steps are Informative: On the Linearity of LLMs’ RLVR Training](https://arxiv.org/html/2601.04537v1) | 2026-01-09 | checkpoint差向量外推与真实RL校正形成替代更新分支；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Learning Dynamics in RL Post-Training for Language Models](https://arxiv.org/html/2601.04670v1) | 2026-01-09 | classifier-first→fullRL分阶段参数权限；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [On the Hidden Objective Biases of Group-based Reinforcement Learning](https://arxiv.org/html/2601.05002v1) | 2026-01-09 | prefix消项依赖effectiveweights，clip后moments仍可更新；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers](https://arxiv.org/html/2601.04890v1) | 2026-01-09 | noise–WD矩阵norm与effective scale分责，gauge/sharedclip边界；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Nalar: An agent serving framework](https://arxiv.org/html/2601.05109v1) | 2026-01-09 | dynamic future发现依赖，immutable value与mutable placement/两级policy分责；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [DR-LoRA: Dynamic Rank LoRA for Mixture-of-Experts Adaptation](https://arxiv.org/html/2601.04823v1) | 2026-01-09 | baseMoE按saliency增长active rank，allocated/终态预算分账；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [ReHyAt: Recurrent Hybrid Attention for Video Diffusion Transformers](https://arxiv.org/html/2601.04342v1) | 2026-01-09 | 局部softmax/远历史kernel共同归一化及双阶段因果适配；2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [PackCache](https://arxiv.org/html/2601.04359v1) | 2026-01-09 | condition quota/temporal预算与3D位置分责；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [AgentOCR](https://arxiv.org/html/2601.04786v1) | 2026-01-09 | episode segment-render cache与下一视图density控制分责；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [CompassMem](https://arxiv.org/html/2601.04726v1) | 2026-01-09 | topicdiverse起点与unsatisfied-subgoal共享queue；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Robust Reasoning as a Symmetry-Protected Topological Phase](https://arxiv.org/html/2601.05240v1) | 2026-01-09 | 离散input选择正交operator的有限保序替代及isometry权限反侧；2+1+2=5 | 深入完成 | 仅报告：拓扑强结论未支持比现有isometry更具体且可核的设计边界 |
| [Plenoptic Video Generation](https://arxiv.org/html/2601.05239v1) | 2026-01-09 | frustum-mean整视频检索支持multi-in/single-out顺次重绘；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [ResMAS](https://arxiv.org/html/2601.04694v1) | 2026-01-09 | 受扰性能面积目标先选图再优化邻接纠错prompt；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Mechanisms of Prompt-Induced Hallucination in Vision-Language Models](https://arxiv.org/html/2601.05201v1) | 2026-01-09 | baseline-correct计数人口的prompt冲突、head均值干预和format/content分责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Reinforced Efficient Reasoning via Semantically Diverse Exploration / ROSE](https://arxiv.org/html/2601.05053v1) | 2026-01-09 | embedding启发分叉、epsilon root重启及符号敏感长度信用；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Orchestrating Intelligence / OI-MAS](https://arxiv.org/html/2601.04861v1) | 2026-01-09 | 逐轮role→model重调度，生成后logprob只调训练成本权重；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/html/2601.05214v1) | 2026-01-09 | 同生成trace的三域tool字段probe与effect前提案接口；2+1+2=5 | 深入完成 | 仅报告：三字段提案未绑定完整训练/评测序列的可比结果 |
| [Precision over Diversity](https://arxiv.org/html/2601.04954v1) | 2026-01-09 | pilot-ever-positive筛选和单soft约束改变可靠性/支持人口取舍；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Learning Latent Action World Models In The Wild](https://arxiv.org/html/2601.05230v1) | 2026-01-09 | 连续容量约束相对VQ的条件替代及camera-relative动作/controller桥接；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Milestones over Outcome / SGVR](https://arxiv.org/html/2601.05073v1) | 2026-01-09 | formal参考→numeric slots→SR汇总sequence reward，不等segment信用；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SemPA](https://arxiv.org/html/2601.05075v1) | 2026-01-09 | 生成policy语义偏好训练→固定prompt末hidden句向量读出；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Addressing Overthinking via Gated Perception-Reasoning Optimization / GPRO](https://arxiv.org/html/2601.04442v1) | 2026-01-09 | fast FFN、visual revisit和reasoning三种operator分开extra compute；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop](https://arxiv.org/html/2601.05184v1) | 2026-01-09 | future query人口独立于synthetic corpus和继承checkpoint；3+1+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [VerseCrafter](https://arxiv.org/html/2601.05138v1) | 2026-01-09 | 静态BG点云与对象mu/fullSigma轨迹作为不同控制载荷；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [BackdoorAgent](https://arxiv.org/html/2601.04566v1) | 2026-01-09 | stage-hook跨step传播及single-turn tokenprob sensor迁移反侧；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Concept Tokens](https://arxiv.org/html/2601.04465v1) | 2026-01-09 | definition CE只训special input embedding，控制与事实/校准分责；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [GRACE](https://arxiv.org/html/2601.04525v1) | 2026-01-09 | support swap/remove保难负例的训练人口与format/path/content gate；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Vision-Language Introspection](https://arxiv.org/html/2601.05159v1) | 2026-01-09 | head校准anchor/context双counterfactual hidden差向量纠正；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Forge-and-Quench](https://arxiv.org/html/2601.04706v1) | 2026-01-09 | native enhancedtext＋forged视觉feature双路径及近似误差敏感性；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [UniDrive-WM](https://arxiv.org/html/2601.04453v1) | 2026-01-09 | plan-first未来图像conditioning与联合head的选择压力；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [HyperAlign](https://arxiv.org/html/2601.04614v1) | 2026-01-09 | MOS监督cone geometry primitives调制已有Euclidean scorer；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgentDevel](https://arxiv.org/html/2601.04620v1) | 2026-01-09 | blueprint对critic解释泄漏与总分/paired-flip晋级人口反侧；3+1+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Token-Level LLM Collaboration via FusionRoute](https://arxiv.org/html/2601.05106v1) | 2026-01-09 | expert selection与complement logits的不同authority及双forward接口；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Prototypicality Bias Reveals Blindspots in Multimodal Evaluation Metrics](https://arxiv.org/html/2601.04946v1) | 2026-01-09 | wrong-prototypical/right-atypical固定prompt反向pair诊断；3+1+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DVD: Detecting Variant Contamination](https://arxiv.org/html/2601.04895v1) | 2026-01-09 | 多次生成的low-prob token难度variance作为受控变体污染探针；2+1+2=5 | 标准完成 | 仅报告：variance探针未给可迁移可识别membership条件或阈值 |

## 4. 证据与知识整合

以下新增25项的必要证据按研究合同§7复用身份/精确版本/采用命题未变的本日已读记录；22项实际整合且非作者POST通过，Holonomic/InternalTool/DVD已独立决定仅报告。连同下方先前11项新增整合，本轮36项处置全部落实。每项明确具体已有论点、候选差额和实际写后依据，不把owner路由、PRE或“Experimental”标签当写入验收；仍待完整独立增量DAY。

### [Robust Reasoning as a Symmetry-Protected Topological Phase](https://arxiv.org/html/2601.05240v1)

exact-v1 Methods Eq9–12、Results Figs1–4及noise/geometric定义，详见[必要证据/owner提案§4.5](../_sources/daily-20260110/admission-extra-20261007.md#45-holonomic-network--260105240v12026-10-07-bjt)。离散input选择由Exp(M−Mᵀ)构造的正交operator，S10 swap/float64测试L50→5000仅支持有限替代；初态Jacobian范数1或orbit点距不认证操作同态、逻辑读出或Gaussian多步噪声的拓扑保护。root独立决定仅报告：拓扑结论没有支撑比现有isometry/norm权限更具体且可核的长期设计条件，不把该论文精确机制冒称已有覆盖；有限operator实验仍保留，不改准入/评分。不采无限causal horizon、通用hallucination理论或Transformer不能处理次序的强主张，不写Books。

### [Plenoptic Video Generation](https://arxiv.org/html/2601.05239v1)

exact-v1 §3.1–3.3/Eq6–10/Alg1–2、§4.1–4.4/Tables1–4见[必要证据§4.3](../_sources/daily-20260110/admission-extra-20261007.md#43-plenopticdreamer--260105239v12026-10-07-bjt)。跨帧frustum包含比例均值选top-k整视频作为multi-in/single-out串行重绘条件；不是无遮挡真实co-visibility，已有Ch25跨view memory/self-conditioning主原则不另计增量。窄差额是该检索/输出接口及容量取舍：context>6同步退、translation .54>.52；Algo2的m/k/l字面流程不授任意容量压缩或终止保证。32H100/context parallel8、缓存/串行生成和训练费用保留，一致幻觉不等真实几何。 实际整合Ch25:642–644及末注1633，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [ResMAS](https://arxiv.org/html/2601.04694v1)

exact-v1 Def1–3/Eq3–6、Tables1–2/Figs5–7及必要配置见[必要证据§4.1](../_sources/daily-20260110/admission-extra-20261007.md#41-resmas--260104694v12026-10-07-bjt)。以F(0)归一的受扰面积先选graph，再用邻接纠错样例优化prompt，是现Ch82图预算/coordination tax之外的具体目标分支。面积高不保证F(0)高，预测p≤.8与面积p1未桥、0.86 tuple accuracy不证明未见图泛化；独立随机回复不覆盖相关故障/攻击。8A100×12h及重优化费用计价，保固定小图和直接扰动曲线退路。 实际整合Ch82:178–180及末注1076，root非写入者已实际核必要原证、完整局部邻接与自身末注，POST通过，见[独立记录§7](../_sources/daily-20260110/post-audit-20261007.md#7-最后五项实际-books-非作者-post)。不授日级Gate、实现或复现。

### [Mechanisms of Prompt-Induced Hallucination in Vision-Language Models](https://arxiv.org/html/2601.05201v1)

exact-v1 §3–6/8、Tables1–4/Fig5、AppA/D见[必要证据§4.2](../_sources/daily-20260110/admission-extra-20261007.md#42-pih--260105201v12026-10-07-bjt)。baseline本已正确计数的条件人口再加误导prompt，按纠正率选head并将各token输出替为其均值，分开format与content copying；这不是现Ch23已有write/read或OCR-head机制的同义改写。Janus正常计数略退、Qwen format copying反增、model-specific image-reliance和层号口径有反侧，不授所有copying下降、唯一电路或一般能力无损；均值亦不数学保magnitude。head/m选择独立人口未明确、200–300RTX3090 GPUh与在线干预计费。 实际整合Ch23:1121–1123及末注1465，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [Reinforced Efficient Reasoning via Semantically Diverse Exploration / ROSE](https://arxiv.org/html/2601.05053v1)

exact-v1 §3/Eq1–10、§4–5/Tables1–4、AppA2见[必要证据§4.4](../_sources/daily-20260110/admission-extra-20261007.md#44-rose--260105053v12026-10-07-bjt)。全路径后的embedding启发分叉、epsilon root重启及正确兄弟路径分歧后的符号敏感长度校准，是Ch33已有tree/segment预算之外的具体Experimental替代。Eq2全双和SD≤0，Eq3非标准非负semantic entropy；top20/static embedding不作语义oracle，自适应共享叶子非iid、不能授无偏policy-gradient。正A缩小与负A按2−ratio^α放大分开，信用消融同时换loss、MATH500/pass@8及α反侧和8A800全预算保留。 实际整合Ch33:237–239及末注2493，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [Orchestrating Intelligence / OI-MAS](https://arxiv.org/html/2601.04861v1)

exact-v1 §3.1–3.3/Eq2–5、§4–5/Tables1–3/AppB–C见[必要证据§5.1](../_sources/daily-20260110/admission-extra-20261007.md#51-oi-mas--260104861v1)。每轮role概率累计选子集/EarlyStop，再按role选model；生成后logprob调整只调训练cost penalty，不是线上正确性签名。现Ch82离线role profile/fleet confidence已有，但未承载此逐轮配置/训练权重接口。归一插值未完整参数化、成本组件有accuracy反退、本地GPU用API价格proxy及3B估价，不能授79.78%实测GPU节约；硬turn预算/verifier与固定小池退路是自己的要求。 实际整合Ch82:264–266及末注1077，root非写入者已实际核必要原证、完整局部邻接与自身末注，POST通过，见[独立记录§7](../_sources/daily-20260110/post-audit-20261007.md#7-最后五项实际-books-非作者-post)。不授日级Gate、实现或复现。

### [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/html/2601.05214v1)

exact-v1 Method Eq1–3/Inference Protocol、Tables1–3/Feature Extraction见[必要证据§5.2](../_sources/daily-20260110/admission-extra-20261007.md#52-internaltool--260105214v1)。完整AR call后取function首subtoken、argument均值和closing delimiter三域提probe；reference规范化一致不是外部真实性或授权。Table1 headline实际weighted average，错误类recall为.53/.61等；3d三字段、d训练输入及whole-sequence mean评测未绑定，support/test人口亦未桥，missing/bypass与effect-time代价无保证。root独立决定仅报告：具体三字段提案未与完整训练/评测序列头条绑定在可比条件，不能支持新的字段定位收益/执行前可靠性条件；不是因为Ch78有sensor主题而声称精确已有覆盖。保留局部提案和纠错，不写Books。

### [Precision over Diversity](https://arxiv.org/html/2601.04954v1)

exact-v1 §2–5/Tables1–4、Eq1/Limitations与必要AppD–F见[必要证据§5.3](../_sources/daily-20260110/admission-extra-20261007.md#53-precision-over-diversity--260104954v1)。pilot-ever-positive样本筛选和单soft约束作为有偏代理，联动IF奖励可靠性与约束支持；Ch31已有confusion profile×budget和verifier非完整覆盖，不复述成新增。pilot零正例不等逻辑不可满足，单向false-accept噪声不等对称/真实相关噪声，hard-only在CFBench/FollowBench/32B并非全面胜mixed。judges/200人工、OOD文字冲突、pilot/curriculum偏差及每步费用非总净成本保留。 实际整合Ch31:807–809及末注1169，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [Learning Latent Action World Models In The Wild](https://arxiv.org/html/2601.05230v1)

exact-v1 §3–9/Tables1–2/Figs4–12、正则定义及必要AppA见[必要证据§5.4](../_sources/daily-20260110/admission-extra-20261007.md#54-learning-latent-action-world-models-in-the-wild--260105230v1)。冻结frame-causal encoder，inverse→continuous容量正则/VQ的条件替代，再借有真实action的历史状态adapter控制；预测误差、cycle一致和控制不能同指标选最优。Ch25已覆盖不可唯一恢复/动作≠control，窄差额是无共同embodiment的continuous容量与camera-relative locality及state-conditioned adapter。负βKL符号不授可执行loss，simple动作VQ仍合理、planning不全胜；大batch联合网络/decoder/CEM和标签付费。 实际整合Ch25:282–284及末注1629，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [Milestones over Outcome / SGVR](https://arxiv.org/html/2601.05073v1)

exact-v1 §2–4/Eq1–5/Tables1–4、Limitations与AppD–F见[必要证据§5.5](../_sources/daily-20260110/admission-extra-20261007.md#55-sgvr--260105073v1)。formal参考skeleton映numeric slots，SR汇总为一个sequence reward/advantage，不是现Ch33语义segment信用。SR、SC、FA分人口；正确数字不认证生成文字derivability，部分predicate映射不保全逻辑。AppF有GPT-5-nano equivalence/regex/人工争议而非零错deterministic checker；SR87.7伴SC15.2、其他任务/配置反侧、8H100/BF16训练与合成/checker成本保留。 实际整合Ch33:748–750及末注2494，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [SemPA](https://arxiv.org/html/2601.05075v1)

exact-v1 §3–6/Eq1–6/Tables2–6、Limitations/AppA见[必要证据§5.6](../_sources/daily-20260110/admission-extra-20261007.md#56-sempa--260105075v1)。NLI偏好proxy做sequence DPO更新policy，再由固定PromptEOL末hidden读句向量，是现Ch76专用contrastive encoder之外的条件替代；owner不是Ch12 token lookup或另造DPO理论。PL softmax形式相似不等梯度/几何/能力等价，单向entailment非双向改写，STS提升只授encoder候选而非RAG召回。GSM8K/DROP/MMLU反退、over-alignment、4RTX5090/LoRA与模板/索引重编码成本保留。 实际整合Ch76:266及末注1284，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [Addressing Overthinking via Gated Perception-Reasoning Optimization / GPRO](https://arxiv.org/html/2601.04442v1)

exact-v1 §3.1–3.3/Eq1–6、§4.1–4.3/Tables2–3见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。alternate FFN中按hidden/entropy/imagefeatures选择原fast FFN、visual-revisit crossattention和reasoning MetaTrans，区分视觉重读与语言推理两种extra compute；Ch23原producer/consumer接口未承载该operator分工。GPT4归因非内部因果，raw entropy→1−U不授校准；7B MathVerse/MMVet和MM-Vet response-length切片反侧、teacher/controller/8H100约600GPUh不由token比例证明E2E便宜。 实际整合Ch23:119–121及末注1461，root非写入者实际正文/完整局部邻接/自身末注POST通过；GPRO长度依POST已限定MM-Vet切片，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop](https://arxiv.org/html/2601.05184v1)

exact-v1 §3/Alg1–2、§4–5.4/Tables1–3/Figs2–6/Limitations/C2见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。future query-group人口是不同于synthetic corpus与继承checkpoint的闭环控制轴，Ch27原corpus/parameter recursion并未具体承载；reset/incremental/accumulation对照支持受控诊断。预设线性人口非真实用户响应，dynamic新prompt/nondynamic重用混杂；小模型Math反侧、news proxy测试prompt选择和质量/similarity重采样可能引bias。2A100/五代局部实验不授必然collapse或无偏纠偏。 实际整合Ch27:408–410及末注1312，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [VerseCrafter](https://arxiv.org/html/2601.05138v1)

exact-v1 §3.1–3.2/Eq1–5、§4–5.4/Tables1–3见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。shared world frame静态BG点云与对象mu/fullSigma轨迹分别render条件；covariance承载extent/orientation而非只center，是Ch25持久位置/轨迹之外的具体载荷分工。camera/object编辑不等像素独立或物理因果，同annotation pipeline测控制、ObjMC不验covariance/遮挡真值；static aesthetic反退和Wan14B/16×96GB/380h付费保留。 实际整合Ch25:396–398及末注1631，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [BackdoorAgent](https://arxiv.org/html/2601.04566v1)

exact-v1 §3–4/stagehooks、§5.1–5.4/Tables1–5/Figs3–4见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。跨stage state传播、clean≠safe已由Ch72承载，不为taxonomy再写；窄反证是single-turn tokenprob sensor在多step target/nontarget trace中差异小且不一致，不能原样迁移成workflow detector。有限同实例预算、utility提升伴ASR不授安全，qwenCode退与channel标签矛盾保留，不推所有概率sensor无效。root决定只补sensor作用域/迁移反侧或仅报告；必要安全深入完成但非实现/生产保证。 实际整合Ch72:72及末注3190，root非写入者已实际核必要原证、完整局部邻接与自身末注，POST通过，见[独立记录§7](../_sources/daily-20260110/post-audit-20261007.md#7-最后五项实际-books-非作者-post)。不授日级Gate、实现或复现。

### [Concept Tokens](https://arxiv.org/html/2601.04465v1)

exact-v1 §3/§4/Tables1–3/AppC见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。definition corpus将concept名替special token，普通LM CE仅训input embedding、冻结其余模型；不同于Ch29原response masked CE权限。assert/negate是控制接口不授新事实，negation主要增abstention且correct17.6<25.1/precision44.56<46.65；单定义lossless/最佳embedding捕获concept未证，平均近似非逐例等价。4bit Llama8B/Hotpot1k/Gemini judge与人工κ、200epochs完整forward/backward和definition provenance均计费。 实际整合Ch29:90及末注1195，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [GRACE](https://arxiv.org/html/2601.04525v1)

exact-v1 §3/Eq1–5、§4/Table1、AppA Alg1/B1/C1 Table5/C2–3见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。support swap/remove保顺序与难负例构当前context支持人口，再format→path→content gate；Ch76已有sufficiency/abstain接口不复述，差额是干预人口与训练奖励权限。ROUGE/citation非entailment，best-effort路径不给content事实权；continuous reward不保证group variance，retriever换分布有反退。Qwen4B/Llama8B、400steps/8rollouts/4A800×8h与baseline异预算保留。 实际整合Ch76:574–576及末注1285，非写入者jan10_books_audit实际正文/完整局部邻接/自身末注POST通过，见[独立记录§5](../_sources/daily-20260110/post-audit-20261007.md#5-root-七项-trainingrag-实际-post非写入者)。不授日级Gate、实现或复现。

### [Vision-Language Introspection](https://arxiv.org/html/2601.05159v1)

exact-v1 §3.1–3.2/Eq1–14、§4/Tables1–2/Limitations、AppA1–3/E见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。GT-region校准head定位anchor，inpaint anchor/context视图后hidden差加回，与Ch23已有knockout/two-pass不同。JS不作hallucination/事实truth；非作者fresh复核已纠正旧理论摘要：A.1 Eq15显式假设分量正交，Prop1/2仅在该正交/加性/理想inpainting及相应alpha条件下成立，尚未证明真实非线性网络满足这些条件。温度式不授最大熵/事实校准，abstract/不集中head限制和α≥.7退保留。serial17.730s/parallel7.823s对原3.130s、约3streams内存及未披露hardware/precision/SLO不作免费修复；7项PRE见[独立记录§3](../_sources/daily-20260110/post-audit-20261007.md#3-ch23ch25-七项必要证据与实际差额-pre)，实际写后另验的原停点已由下述POST取代。 实际整合Ch23:107–109及末注1463，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [Forge-and-Quench](https://arxiv.org/html/2601.04706v1)

exact-v1 §3.1–3.2/Eq2–6、§4/Tables1–5、AppA1/Table6/A3见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。保native enhancedtext并额外用flow bridge锻造SigLIP空间feature、Injection adapter给T2I，区别替换text或真实reference；Ch24已有typed generation接口不等此双路径。更强target重构不保近似forged feature稳定，noise cosine只是proxy；FLUX/MeiGen局部GenEval/DPG退和理解保持未全面证明。2B bridge+1B injection、200M/13M训练及0.49s局部非E2E保留。 实际整合Ch24:1019–1021及末注1786，root非写入者已实际核必要原证、完整局部邻接与自身末注，POST通过，见[独立记录§7](../_sources/daily-20260110/post-audit-20261007.md#7-最后五项实际-books-非作者-post)。不授日级Gate、实现或复现。

### [UniDrive-WM](https://arxiv.org/html/2601.04453v1)

exact-v1 §2.3–2.4/§3.1–3.7/Table4及Eq11见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。plan tokens先于future image，联合visual监督通过共享参数辅助planner，不是已实现的推理时图像回送、多action causal rollout。Ch25原action-conditioned/辅助head原则已有，具体差额是plan-first conditioning及joint head选择压力。AR192×128与continuous256×256异分辨率不授纯decoder因果，Eq11口径不授唯一literal loss，mASE退、8H200/Bench2Drive有限closed-loop与L2/boxcollision分开。 实际整合Ch25:171及末注1627，root非写入者实际正文/完整局部邻接/自身末注POST通过，记录见[实际写后交接](../_sources/daily-20260110/supplement-20261007.md#七项实际写入及非作者post)。不授日级Gate、实现或复现。

### [HyperAlign](https://arxiv.org/html/2601.04614v1)

exact-v1 §3.2–3.4/Eq5–9/Alg1、§4.1–4.5/Tables1–2/Fig4见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。MOS监督cone aperture，geometry primitives经MLP调已有Euclidean cosine，是现Ch66 reference geometry/proxy之外的条件替代，不自签entailment/hierarchy。六消融未全隔离MLP容量/训练，跨数据库AGI→AIG .6309/.6244低于CIA .6506/.7443，不授普遍robust；CLIP/4090/十次prompt-group split/earlystop与完整部署预算限制保留。 实际整合Ch66:129及末注4563，root非写入者已实际核必要原证、完整局部邻接与自身末注，POST通过，见[独立记录§7](../_sources/daily-20260110/post-audit-20261007.md#7-最后五项实际-books-非作者-post)。不授日级Gate、实现或复现。

### [AgentDevel](https://arxiv.org/html/2601.04620v1)

exact-v1 §2.2–2.4/Eq1–19、§3.1–3.4/Tables1–3见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。Table3同b0/split/budget的critic看blueprint→Train增/Test退及P2F更高，去flipgate总分提高伴P2F恶化，构成解释泄漏与promotion人口分账的具体反证；此前成熟release组合关闭已撤，不因现Ch66 heldout/Ch80归因原则已有再次关池。promoted/evaluated RC和35.5/34.2口径不授唯一累计flip或普遍因果；blind同model不等独立truth，Sonnet/ClaudeCode预算未全披露。只提Ch66 regression窄差额，不复制成熟reflection链；实际融入Ch66:410–412（原POST时408–410，因HyperAlign插入顺移）两段及末注4562，非写入者jan10_books_audit已顺读393–443完整邻接/原受控对照，POST通过，见[独立记录§2.1](../_sources/daily-20260110/post-audit-20261007.md#21-三项实际-postfresh-非写入者)。不授DAY、零回归或实现复现。

### [Token-Level LLM Collaboration via FusionRoute](https://arxiv.org/html/2601.05106v1)

exact-v1 §2–4/Eq1–7/Alg1/Assumption4.1、§5–6/Tables1–2见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。router既选expert又加complement logits，selection和生成authority及共同prefix两forward/KV重建不同于Ch56原handoff。Eq1 log/log、Eq2 missing normalizer与Eq7 prefix logZ缺项不静默修成严格CDPO或一般最优保证；局部greedy组合机制与global理论分离。GSM/HumanEval/MATH反侧、训练额外阶段和state/前缀重建成本保留，实际融入Ch56:290–292两段及末注1564，非写入者jan10_books_audit已顺读277–321完整邻接并核原机制/反侧，POST通过，见[独立记录§2.1](../_sources/daily-20260110/post-audit-20261007.md#21-三项实际-postfresh-非写入者)。不授DAY或实现复现。

### [Prototypicality Bias Reveals Blindspots in Multimodal Evaluation Metrics](https://arxiv.org/html/2601.04946v1)

exact-v1 §3/Eq1–5、§4/filter/human、§5/Tables1–2/§6见[必要证据及实际owner](../_sources/daily-20260110/supplement-20261007.md)。固定prompt的wrong-but-prototypical/right-but-atypical反向pair是现Ch66 hubness/semantic object之外的具体诊断，不把一般similarity非truth当新增。近似生成/筛选非真正argmin/max，19467 image/pair人口未清、Qwen过滤与300人工非全标签真值，ProtoScore非全best/跨域校准。FLUX/GRPO附加模型成本和不同评价分母保留，实际融入Ch66:131（原POST时129，因HyperAlign插入顺移）窄段及末注4561，非写入者jan10_books_audit已顺读104–138完整邻接/原证反侧，POST通过，见[独立记录§2.1](../_sources/daily-20260110/post-audit-20261007.md#21-三项实际-postfresh-非写入者)。不授DAY或新scorer真值。

### [DVD: Detecting Variant Contamination](https://arxiv.org/html/2601.04895v1)

exact-v1 §3–5/Eq6–9/Tables2–3、AppA1–2见[必要证据及具体owner](../_sources/daily-20260110/supplement-20261007.md)。固定prompt多次生成low-prob token难度variance是controlled注入的变体污染检测分支，仍不由mixture variance恒等式识别真实membership；完整记忆也可低variance、未污染亦可多峰。Eq6索引/tail-count口径、阈值和production FPR未闭合，AUC不等私有预训练污染率或纠正benchmark。root独立决定仅报告：尚无可迁移可识别membership条件/阈值，controlled局部AUC不能成为新长期污染admission机制；不是以Ch66有contamination主题冒称exact已有覆盖。保N50生成费用、MinK++反侧和GPT4o变体语义proxy，不写Books。

### [AgentOCR](https://arxiv.org/html/2601.04786v1)

exact-v1 §4.1–4.3/Eq3–8、§5/Table1–4、§7与AppA/B2–4必要条件，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。normalized segment episodecache仅省重复render，完整Stack/resize、encode/decoder及缓存增长仍计费；compressiontool改下一视图，不删除source。K1成功率45.3低于K5的78.2，successgated奖励不保证保真，正文trainingiterations与Alg envstep频率未桥。Qwen2.5-VL3/7B、ALFWorld/Search、2/4H100，text基线部分更强，caps不同、168.77ms render非E2E。6分具体接口差额深入，root写[Ch75:199](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-07-agent/75-context.md:199)两段及668注；本作者实读180–217完整POINTS/softtoken邻接、本注并重开§4原机制，非写入者POST通过，不授增量DAY。

### [CompassMem](https://arxiv.org/html/2601.04726v1)

exact-v1 §4.2–4.3/Eq4–11、§5、B2–3/C1，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。topicdiverse起点、Skip/Expand/Answer及sharedvisited/evidence，queue按未满足subgoal排序；LLM typededges/满足标签不授事实或因果权。§4.3.3 literalstop要求全满足，C1仅594/1540满足却均回答；AvgMaxRounds2.4与B2一次追加未桥，不授完整终止/生产保证。LoCoMo、Narrative298题有限样本、Qwen14B/vLLM/GPT4omini/BGEM3，平均20.87/max65.38s及更多tokens不是tailSLO。6分具体搜索差额深入，root写[Ch77:278](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-07-agent/77-memory.md:278)两段及1748注；本作者实读255–294 RippleMem/FactState完整邻接、本注及重开§4.3原operator，非写入者POST通过，不授增量DAY。

### [ReHyAt: Recurrent Hybrid Attention for Video Diffusion Transformers](https://arxiv.org/html/2601.04342v1)

exact-v1 §3.2–3.4/Eq5–19、§4/5，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。chunk-local/overlap softmax与远历史kernel共同归一化、逐block featuremap蒸馏后全DiT flowmatching适配。Eq13全远历史又在17/18加入累计状态，字面不支持递归等价；15/20/25 of30转换仍保fullattention，不授全模型定内存。Wan1.3B、500paired/50prompts、160H100h适配及物理控制/人偏好反侧保留，mobile block不是端到端SLO。6分具体差额深入，root写[Ch22:477](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-02-model/22-long-context.md:477)两段及1162注；本作者非写入者实读449–505完整因果kernel/SSM邻接、本注，并重开v1采用命题，POST通过，不授中心强保证或增量DAY。

### [PackCache](https://arxiv.org/html/2601.04359v1)

exact-v1 §3.1–3.4/Eq4–9、§4.1–4.4/Table1–3，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。condition固定quota不入temporal decay，masked物理删除、多帧预算与3D时间rebase保空间身份；位置变换须作用于实际Key，不只改metadata。Eq6/7分配和quota3/W、FIFO触发口径不足以唯一执行。Lumos1-3B/672×384/160VBenchI2V、A40/H200，24帧部分质量退步、48帧FullKV OOM拟合不是实测速率。6分具体差额深入，root写[Ch45:402](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-05-inference-system/45-why-kv-cache-speeds-up.md:402)小节两段及1698注；本作者非写入者实读390–421 selector/recompute及workload eviction完整邻接、本注并重开v1采用命题，POST通过，不授无损、唯一FIFO实现或增量DAY。

### [Nalar: An agent serving framework](https://arxiv.org/html/2601.05109v1)

exact-v1 §3.1–3.4/§4.1–4.3/Table1–3/§6.1–6.3/Table4，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。dynamic future创建/登记consumer/取值发现依赖，immutable output与mutable placement metadata分责，global周期policy/local事件enforcement及迁移dependency/sessionstate次序。不是external effect exactly-once或故障原子迁移；2nodes各4A10080GB/100GbE/vLLM LLaMA8B与64CPU profileemulation分开，SRTF/LPT JCT/makespan收益伴P95+3.3%/+2.6%，precision/完整length/质量等价未披露。6分具体runtime执行差额深入，root独立源/owner核后写[Ch84:90](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-07-agent/84-agent-platform.md:90)两段与1151注，本作者非写入者实际顺读52–113完整邻接/正文/本注POST通过；不授增量DAY。

### [DR-LoRA: Dynamic Rank LoRA for Mixture-of-Experts Adaptation](https://arxiv.org/html/2601.04823v1)

exact-v1 §3.2–3.3/Eq5–12/Alg1、§4.1/§5.1–5.3/Limitations及A.1–A.3，见[必要证据/POST](../_sources/daily-20260110/supplement-20261007.md)。routingweight EMA×gradient–weight rank importance提出baseMoE每expert rank growth，rmax预分配只改变active而非allocated memory；router warmup/后联合训、wholeexpert消融限制归因。ceil quota/event数和expert/module N口径未闭合，不授literal精确同终态预算。OLMoE/Phi、1epoch/4L40S48GB/ZeRO2/bf16/3runs，MMLU/ARC反侧、43.2/32.7h长于普通LoRA39.7/30.2h，不授医疗split独立泛化或全任务收益。5分具体Ch30差额深入，root实际源/owner核后写[Ch30:300](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/30-lora.md:300)两段与798注，本作者非写入者实际顺读278–346邻接/正文/本注POST通过；不授增量DAY。

### [Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers](https://arxiv.org/html/2601.04890v1)

exact-v1 §2–4.4、§5/Table1–2与必要A/B/C详见[必要证据与实际POST](../_sources/daily-20260110/supplement-20261007.md)。noise–WD矩阵norm与learned effective scale分责，不授所有矩阵scale锁死或μP普遍失效；既有attention/SSM缩放、gauge低精度失稳、轻decay和共享clip norm排除的权限边界保留。Falcon-H1-0.5B/30与240GT、逐配置LR搜索、LMhead及Muon MMLU反侧，不授全任务改善、fold后总成本为零；hardware/总wallclock未充分披露。6分具体parameterization差额深入，root独立原源/owner核后写[Ch28:379](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/28-pretraining.md:379)两段与1583末注，本作者非写入者实际完整邻接359–425/正文/本注POST通过；不授本日增量日级完成。

### [Not All Steps are Informative: On the Linearity of LLMs’ RLVR Training](https://arxiv.org/html/2601.04537v1)

exact-v1 §3.1–3.3/§4.1–4.3、A.1/Table1–3、A.2关键反侧详见[必要证据](../_sources/daily-20260110/theory-review-20261007.md)。fixed-prefix/sampleweight诊断不授所有新trajectory线性；两checkpoint差外推是proposal，交替真实RL提供reward-grounded校正，Fig5半径有限。LCB200/1200步 `.2619/.2762`低于基线`.2714/.2857`；6.1倍仅AIME24 matched quality实际RL步数，不是GPU总预算/墙钟。DeepSeekR1DistillQwen1.5B/DeepScaleR无KLentropy配置、optimizer moments/I/O/调参费用未全披露。6分具体差额深入，root实际source→owner独核后写[Ch33:1237](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/33-grpo.md:1237) recipe后两段与末注；非写入者audit_supp_jan06实际完整邻接/正文/末注POST于2026-10-07T15:42:04+08:00通过（见同一证据文件），不授增量DAY。

### [Learning Dynamics in RL Post-Training for Language Models](https://arxiv.org/html/2601.04670v1)

exact-v1 §3–5、A.1/A.2、B.1–B.3及PDFp14详见[必要证据](../_sources/daily-20260110/theory-review-20261007.md)。新增为额外classifier-only1epoch→fullRL6epochs，不是head-only取代全程。局部reward-only NTK解释可保留，一般KL定理因§3.2、Eq23 log/log与后续logratio求导冲突不采用；zero innerproduct不支持unique argmax或所有实际更新熵必降。Pythia2.8B/AlpacaFarm/UltraFeedback/ArmoRM三runs、GraceHopperH100/512tokens，ArmoRM非人类真值，额外阶段不授净成本降低。5分因受影响理论/具体owner深入，root必要源/成本邻接独核后实际写[Ch31:648](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/31-rlhf.md:648)两段与1165注，非写入者audit_supp_jan06实际POST于2026-10-07T15:42:04+08:00通过（见同一证据文件），不授增量DAY。

### [On the Hidden Objective Biases of Group-based Reinforcement Learning](https://arxiv.org/html/2601.05002v1)

exact-v1 §3–6、B/C/D必要推导详见[必要证据](../_sources/daily-20260110/theory-review-20261007.md)。共享prefix只在完整group/identical effectiveweights条件消项，子集/lengthweight/activeclip不自动成立；Adam全历史同正scale、moments一致缩放与epsilon可忽略才支持局部尺度不变性，独立KL/组间变化破坏前提。advantage梯度clip为零后旧moment tail仍有有限更新，不授硬trust-region、ratio普遍单向越界或删除clip。正文与canonicalAdam附录符号口径不作为可执行recipe。6分具体group estimator→loss reduction→optimizerstate接口深入，root实际source/owner独核后写Ch33 LossReduction尾两段及RelativeAdvantage尾一段（[实际moment段:2363](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/33-grpo.md:2363)、[尺度条件:2463](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/33-grpo.md:2463)）与末注；非写入者audit_supp_jan06实际POST于2026-10-07T15:42:04+08:00通过（见同一证据文件），不授增量DAY。

### [MuLo-SD](https://arxiv.org/html/2601.05149v1)

exact-v1 §3.2–3.3/Eq5–7、§4.1/Table1/§4.3与Appendix Alg1/Implementation/Latency：低分辨率起草、learned rowcausal up/down映射、target概率pool阈值、拒绝位置向二维邻域扩展并顺序重采，同时保留远端accepted。不是经典acceptance/residual或target joint分布等价，不能移用LANTERN的δ界。Tar1.5B/AR-DTok、A100 batch1、512p/1024p，CUDA-event decoding计时；额外4A100训练模块150ksteps（4x另150k）、τ扫选对齐LANTERN GenEval，不授无损/通用1.7倍/生产SLO。local-only不改周边context反侧、部分quality退步、更快ZipAR和lowresdrafter瓶颈均保留。原5分标准投入后因Ch48具体空间纠正差额定点深入，root实际原源/owner独核，root写入[Ch48:835](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-05-inference-system/48-speculative-decoding.md:835)两段及Reviewnote1027；本作者非写入者实际全文邻接825–850、两段与本注/必要原证POST通过，不授增量日级完成。

### [CC++](https://arxiv.org/html/2601.04603v1)

采用exact-v1 §4、§5.1–5.3与Jan9官方核心：交换关联检查有别于单独输出检查，廉价activation probe flag触发付费ensemble升级，不获得独立refusal权限。全exchange标签是prefix弱监督；训练窗口平滑与部署EMA状态须分别校准，later flag不能追回已泄漏内容。static-anyflag评估、testset调α和不同模型流量合同不支持普遍安全或统一成本保证。深入完成，实际整合 `PLATFORM-SECURITY` [Ch72](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-06-ai-infrastructure/72-security.md:834)两段与末注；root实际必要源、正文邻接与POST通过。

### [LaST](https://arxiv.org/html/2601.05248v1)

采用exact-v1 III-D/E、IV-B：slow latent KV和fast fresh observation是两个观测时钟；mixed-ratio训练改变cache age分布，不是免费换执行频率。保κ枚举不一致与1:8单比率反侧，不采用15.4倍普遍收益。深入完成，实际整合 `MULTIMODAL-EMBODIED-VLA` [Ch26](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:339)窄段及末注，root实际POST通过。

### [CounterVid](https://arxiv.org/html/2601.04778v1)

采用exact-v1 Eq3–8、§4.1/4.2与heldout244：固定视频比较答案和固定答案比较视频是不同pair条件；同场景anchor不证明只改动作的纯因果，λ=1不证明gradient balance。68% good pairs、text preference反侧与生成成本分别保留，不采用统一全面优势。深入完成，实际整合 `TRAIN-DPO` [Ch34](/Users/apple/Documents/Work/PycharmProject/AI-System-Design/books/part-04-training-system/34-dpo.md:279)两段和末注，root实际POST通过。

### [GDPO](https://arxiv.org/html/2601.05242v1)

原分2+1+2=5，必要方法、tool/math/code评价与末批advantage归一化消融支持percriterion归一→weightedcombine→batch中心/尺度两个不同authority；不是所有reward目标无冲突或零方差数值实现已被保证。root实际原§2/3.1 Eq4–6/3.2和4.1五run、Ch33:1397–1408发现旧即时/未来段不完整承载该接口，原SpecificExisting提案纠正为缺口深入。实际Ch33:1406新增criterion population与batch scale分责，保旧immediate/future/turn顺序分支；feb01_v3实际1395–1417正文邻接和2265注POST通过，深入完成。

### [RoboVIP](https://arxiv.org/html/2601.05241v1)

必要exact-v1 §3.2–4.4/5及[原段](../_sources/daily-20260110/ROBO_EVAL_RAW.md)：动作/gripper帮助分割，stitch多view输入video inpaint与视觉exemplar复用原action轨迹；这是训练观察接口改变，不等新真实动作安全控制。§4.2明示各方法均不能生成一致multiview，图像feature matching不是world truth；SimplerEnv只有单view，不能单独证明multiview收益。π0 ID平均低于text、Octo相反，real100 vs200轨迹也不是同数据预算。root必要原源与具体Ch26 derived-label差额通过，actual Ch26:545新增appearance edit与mask/scene/view/time/action身份分责，保生成/分割成本、真实示教BC和闭环fallback；不采一致性/普适成功保证。jan02_v3实际529–554正文/邻接及1784末注POST通过，深入完成。

### [MiJaBench](https://arxiv.org/html/2601.04389v1)

exact-v1 §3–6/限制（[原核心](../_sources/daily-20260110/BOUNDARY_CORE_RAW.md)）支持aggregate安全掩盖不同target人口。English与Portuguese native seeds/群体不相同，不授language/group纯因果；2112人工子集经Qwen初次一pass一fail选择，majority judge不成为独立真值，也未测positive prompt FPR。root实际§4/5的528k/2112选择人口与native/positive-prompt限制，以及Ch66:3242–3250 Average-only保存per-example/slices/uncertainty、长度/证据budget、相关样本及独立judge控制，确认具体已有覆盖；非MiJa精确算法已写。原6标准完成，不另写Books。

### [Merging Triggers, Breaking Backdoors](https://arxiv.org/html/2601.04448v1)

exact-v1 §3–5.4（[方法](../_sources/daily-20260110/BOUNDARY_METHOD_RAW.md)、[反侧](../_sources/daily-20260110/BOUNDARY_EVAL_RAW.md)）的defender poison四trigger与128clean recovery只在受控malicious SFT/模型切片验收。cross-trigger输出唤起不识别唯一共同latent或head因果，六trigger对照和正常能力退步保留，GPT4o toxic/refusal judge不等真实执行harm。root实际§3.1/3.2 Eq1–3、§4评价与§5.2–5.4六trigger直接反侧，通过原6必要安全深入与OnlyReport：额外poison修复case未给可迁移trigger selection或通用repair contract，clean/attack复核原则不算原创新贡献；不写Books。

### [On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions](https://arxiv.org/html/2601.04600v1)

exact-v1 §5–7.2与[关键对照](../_sources/daily-20260110/04600_METHOD_EVAL_RAW.md)：GPT-J6B的受限MQuAKE/CounterFact里edit recall和two-hop access是不同人口，冗余跨层copy改善two-hop同时明显损伤specificity/fluency。greedy直接回答不独立定位内部reasoning成因，不推所有ROME失效。实际融入Ch16:255 knowledgeDB→recall/composition→MLP表示分工，工程验收/回退显式为推断。root必要原源/具体owner通过，jan02_v3实际244–267正文邻接及333注POST通过，深入完成。

### [When More Words Say Less](https://arxiv.org/html/2601.04609v1)

exact-v1 §3.1–4.4/限制（[原文](../_sources/daily-20260110/AM3_SPECIFICITY_CORE_1_RAW.md)）固定length并比较target与4999个contrast images的CLIP相似度rank；有助区分verbosity与有限语料中的specificity，不提供语义真实性/task sufficiency。5000 COCO、CLIP77token排除长描述及30人偏好都是测量人口。root实际§3.1–4.4及限制151–154通过原5标准OnlyReport：局部图像描述测法不改当前Ch66冻结测量身份、长度/证据budget和相对排序候选集的长期合同，非声称该精确recipe已有覆盖，不写Books。

### [Prior-Informed Zeroth-Order Optimization](https://arxiv.org/html/2601.04710v1)

exact-v1 §III算法1–4、IV及V-C–H（[core](../_sources/daily-20260110/04710_CORE_RAW.md)、[eval](../_sources/daily-20260110/04710_EVAL_RAW.md)）用M个方向评价构造elite/bottom guide再付对称差分，不能只报两forward总成本。20k baseline40kforward与M2/10k或M4/5k不能统一说identical cost，V-E时间与Table10不合不采用。Lemma1的k<d covariance近I operator guarantee有rank障碍，Lemma4归一的s/s²及算法/理论选择人口需隔离，不否定OPT1.3B/SST2BoolQ有限alignment。jan02_v3实际方法/理论/必要eval及Ch28:304–310非作者通过，标准完成，仅报告：局部loss-sorting替代未提供可信跨配置alignment/全成本成立规则，不冒称elite recipe已有覆盖。

### [AM3Safety](https://arxiv.org/html/2601.04736v1)

exact-v1 §3.2 Eq1–9/4.1–4.5（[method](../_sources/daily-20260110/AM3_SPECIFICITY_CORE_0_RAW.md)、[eval](../_sources/daily-20260110/AM3_SPECIFICITY_CORE_1_RAW.md)）：N=8 rollout的turn safety variance加低mean penalty，经softmax权重进入helpful/safe reward。这是局部新recipe，不将成熟GRPO计分；InternVL3-78B T0只是judge proxy，固定reward不证明安全约束满足。8H800/7000 dialogues/500 coldstart与不同baseline人口，Table2/3有helpful退步；阶段整体对照不唯一辨turnweight因果。原5标准完成，仅报告：未披露可迁移的turn-importance选择准则。feb01_v3实际完整AB、必要方法/eval和直接反侧非作者通过，不写Books。

### [Judge Decoding via Distributional Divergence](https://arxiv.org/html/2601.04766v1)

exact-v1 §4/5、AppA1.1–1.5（[main](../_sources/daily-20260110/KL_MAIN_RAW.md)、[proof](../_sources/daily-20260110/KL_PROOF_RAW.md)）target||draft KL阈值与top1>.9回退是非exact切换策略。accepted prefix不自动给局部second-order expansion所需δ小，V≫d不推出head差向量满rank，近似式不能无remainder升为普遍lowerbound；共享primitive坐标不证明线性/二次边界等价或内部logic pivot。root实际§4/5与AppA局部展开/下界/overcomplete论证通过原5标准OnlyReport：只隔离理论强保证，保留有限accuracy/accepted tokens/8V100 wallclock不同测量，不判有限实验无效，不写Books。

### [Token Maturation](https://arxiv.org/html/2601.04854v1)

exact-v1 §3.3/3.4/Alg1/4.1及5/6（[原文](../_sources/daily-20260110/04854_CORE_RAW.md)）中α的noise/maturity方向与(1−α) loss权重解释不一致；Alg1按K-buffer front进度commit，未给sufficient convergence检验。24层/10BT/600Ksteps有限entropy和qualitative观测保留，不判结果伪；CFG双forward不授低端到端开销。原6中心终态暂缓，feb01_v3实际完整AB及必要原段非作者通过。§5精确重开；中心未决命题不进入Books或正面Evidence。

### [GenProve](https://arxiv.org/html/2601.04932v1)

exact-v1 §3–5/限制（[core](../_sources/daily-20260110/04932_CORE_RAW.md)、[eval](../_sources/daily-20260110/GEN_EVAL_RAW.md)）联合生成claim及doc/sent/type关系；Quotation/Compression/Inference taxonomy借TROVE，不计为本次原创。reference匹配threshold/F1不等entailment或实际source使用，noSim F1更高而内容轴退步，model-level human correlation不当逐claim正确率。Qwen3-8B SFT+GRPO及额外tags/retrieval有成本、硬件Not Disclosed。深入完成，实际Ch76:819 supportspan后新增typed relation与独立entailment分权；root必要source-owner通过，jan02_v3实际798–831正文邻接和1175注POST通过。

### [Compositional Steering with Steering Tokens](https://arxiv.org/html/2601.05062v1)

exact-v1 §3/4、§5/限制（[methods](../_sources/daily-20260110/STEER_RELAY_METHOD_RAW.md)、[eval](../_sources/daily-20260110/05062_EVAL_RAW.md)）冻结base/subword embedding和独立behavior tokens后只训练composition token，额外输入embedding tokens不是noise。质量只在约束成功人口评价，unseen/反序与Llama长度任务会退步；每行为50k teacher generation及>1M evaluations付费，不从2→3-property组合推任意semantic约束或所有model scale。zero-init orthogonal penalty数值约定未披露不自动判代码失败。jan02_v3实际必要原文及Ch29:430–449/Ch30:118–132/Ch66:58非作者通过，标准完成，仅报告：固定语言/长度/格式局部参数权限recipe未形成跨语义/高阶或独立质量人口的新controller合同，不宣称exact已有覆盖。

### [RelayLLM](https://arxiv.org/html/2601.05167v1)

exact-v1 §2/3、§4/5.2–5.5（[methods](../_sources/daily-20260110/STEER_RELAY_METHOD_RAW.md)、[eval](../_sources/daily-20260110/05167_EVAL_RAW.md)）SLM保留call command history，teacher消费去command的context并返回n-token span；handoff不是target验收。warmup/filter人口、teacher identity与fixed-n重训练预算单列，call ratio不等总prefill/网络wallclock，换14B teacher和n500也有取舍。root实际原源及Ch56:250–289差额通过，实际288新增不同rendered-view与return-lineage身份而非KV兼容。feb01_v3实际276–295正文邻接与1512注POST通过，深入完成。

### [Kimi CLI 0.74/0.75](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.74)

原release `published_at`分别为Jan9T13:23:56Z及14:47:53Z，两个事件合并为一个版本家族；表内范围仅包围这两个已核时刻，不把PR merge当release公开。完整body与[必要原patch](../_sources/daily-20260110/KIMI_REQUIRED_CHANGE_CORE.md)纠正原功能名关闭：PR591加入terminal-auth setup描述、session model/thinking选择，并持久化default config及thinking metadata，不只是临时session切换；authenticate自身仍NotImplemented，不授认证安全。PR596改后缀排除为header/type分派，返回base64的ImageURLPart/VideoURLPart；text100KiB和media80MiB不同限额及empty/oversize拒绝是实际消费者兼容条件，不证明恶意媒体处理安全。PR595官方docs→local source→确认clone只是成熟help-routing方案，关闭。原新增命题1+1+1=3，但兼容/调用契约确变，按合同深入受影响两patch；root实际core及准入/评分/深入处置通过，不运行代码、不遍历全PR。OnlyReport：保存本版本客户端/配置适配事实，未建立新通用可靠性或授权机制，不改Books。

原Kimi家族补充事件：[0.73](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.73) `published_at` Jan08 16:54:15Z＝BJTJan09 00:54:15，原窗前而补充自然日内，不搬原0.74/0.75日期或改旧3分。实际完整release及PR575/576/568/584/585/587必要patch：stdio100MiB仅transport frame限额；await MCP初始化后loop/cleanup的task兼容；params=None接受不授取消成功；YOLO off恢复未来审批不撤既有effect；Ralph maxsteps仅每turn、原prompt重复与STOP非独立完成证明；default-provider refresh失败保留旧配置，不给用户secret新权限。SDK reexport不等行为改变。root独立实际重开必要diff通过受影响接口深入审阅，OnlyReport：未形成新长期机制差额，不写Books；runtime未复现，不追加family。完整证据见[增量记录§3](../_sources/daily-20260110/supplement-20261007.md)。

## 5. 缺口与下一步

本轮普通可执行待办为0：36新论文必要审阅、actual owner对照与正式行/§4同步完成，33项实际整合及必要非作者POST通过、3项独立决定仅报告；最后五项实际POST见post-audit§7，完整六部分独立增量DAY已由root验收通过，见post-audit§8。以下外部日期、中心和历史来源保留只在对应材料恢复时单项重开，不混为普通工作、正面Coverage/Evidence或无遗漏保证。原17项处置/8实际POST仍有效。

本轮外部日期终态保留：[MoEBlaze2601.05296v1](https://arxiv.org/abs/2601.05296v1)目前必要公开日界为Jan09–Jan12；[SPINAL2601.06238v1](https://arxiv.org/abs/2601.06238v1)为Jan09–Jan13。各首次Submitted落本批缓冲而findable上界晚，不能用晚Updated或Submitted反推公开日；不评分、不深入方法、不进正式36或Books。只接受本ID可验证first-public日/官方announcement切片的同一个具名请求，重开日期后再处理受影响单篇，不索全站或完整历史。

外部终态保留：上述历史队列/删除或未索引内容、arXiv公开revision和作者镜像召回不用于正面覆盖或无遗漏断言；恢复目标窗原公开列表/可验证官方first-public后只重开对应来源日期。STDD2601.04205虽有Jan9注册，但Submitted Dec7，缺完全落窗的实际first-public下界，不能只凭Jan ID或注册列为本窗正式候选；接受官方具体announcement或作者可验证首公开事件，不继续方法审阅来替代日期。

中心终态保留：[Token Maturation](https://arxiv.org/html/2601.04854v1)需实际α corruption/embedding/update/loss/commit配置与其结果的明确绑定，才能重开受影响中心命题；当前不采用该保证、不写Books、不支持正面Evidence或无遗漏。无需遍历后版、代码或全附件来延长本窗。

## 6. 复核

复核者：root（非报告作者，完整增量DAY；具名非写入者批次记录于本日post-audit）

结论：通过

本轮增量复核者：root（非报告作者）及具名非写入者批次；当前结论：通过。完整独立DAY原证见[post-audit§8](../_sources/daily-20260110/post-audit-20261007.md#8-01-10-增量日级非报告作者验收)：实际核14源有限查询/日期邻接/分页停点、六部分、41完整题摘分区与Datadog/04719/05111/05191具体负侧，未将317跨组题名命中或宽目录当逐项语义关闭。原17候选逐字保留，53唯一家族、36新增必要审阅/actual owner处置及33实际Books整合的各批非作者POST均通过；Holonomic/InternalTool/DVD仅报告及Kimi0.73同家族事件由root独立决定。VLI正交假设纠偏与GPRO的MM-Vet长度切片已进入实际正文；training/RAG七项及最后五项实际POST分别见§5/§7。145本地文件链接、围栏、V3与限定unstaged/cached diff-check实际通过，但机械检查不替代语义审阅。上文与增量记录的阶段性“待DAY/准备”仅为当时停点，本段及§8是现行终态；扫描、筛选、审阅、Books和复核普通待办0。日期、中心争议、具名历史索引/revision限制均保留，不授正面Coverage/Evidence或无遗漏；未核模型实现、复现或生产SLO。下文原轮复核仍只授原17家族范围。

原轮复核者：root（非报告作者，首批准入、必要证据/实际POST及原17家族日级验收）；jan02_v3与feb01_v3参与具名证据和写后批次。

原轮结论：通过；不代替本轮增量验收。

root已实际读首四完整题摘及SB Energy官方核心、CC++官方/论文核心，必要source/owner及首3POST；GDPO/rankedit/GenProve/Relay/RoboVIP原源与owner通过，实际POST分别为jan02_v3的rankedit/GenProve/RoboVIP与feb01_v3的GDPO/Relay。root实际核MiJa§4/5与Ch66:3242–3250具体Existing、MB§3–5.4必要安全反侧、Specificity§3.1–4.4/限制、KL§4/5/AppA受限理论处置。feb01_v3实际核AM3Safety/Maturation完整AB、必要方法/评价与直接反侧；jan02_v3实际核PriorZO/Steering原core/eval、具体owner与OnlyReport理由。root实际TourPlanner Eq4/Hindsight完整AB/ToolGate决定core及MiMo v2有限标记通过关闭；Kimi两必要patch揭示原功能名关闭不足，已纠正为原3分接口变更深入OnlyReport，root准入/评分/受影响证据通过。最终复核实际对照14来源有限停止、首次三项与其余14原日期字段、官方ID/公开排程条件和可见项目日期信号，核17家族归并、各项处置及正文实际位置；六部分日级验收通过，普通待办0。完成态V3与限定diff检查另行机械验证，不能替代语义核验。负侧范围不等100元标题全量或全附件验证，外部和中心保留项不授正面Coverage/Evidence或无遗漏。未stage、commit或push。
