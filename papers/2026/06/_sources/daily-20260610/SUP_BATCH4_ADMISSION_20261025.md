# Jun09 已见模型/系统题摘收束（第4批）

只处理前轮已见且完整读过题摘的具名增量，不扩大宽目录。作者本轮已逐项重读下面12项exact-v1完整AB/history，原件`SUP_ABS_2606.<ID>v1_20261025.html`、精确DOI完整字段`SUP_EXACT_2606.<ID>_20261025.json`都已存。无撤回/具名勘误标记；有版本号不自动全版diff，下面保已见会影响采用的变化信号。首次公开推断仍只arXiv公告，不认证全球首次或逐字历史。

除07665外，11项v1 Submitted与registered/findable/arxiv.content联合：最早Jun09 00:00Z，不晚于同日registered，整体BJTJun09。表保真实原字段，Created未充上界。脚本条件复算与history唯一v1均已逐项核；待reader一次日期/准入校准。

| ID | Submitted v1 UTC | registered UTC | 原有约束→具体增量→改变的判断；拟评分 |
| --- | --- | --- | --- |
| 09563 PRISM | Jun08 14:37:46 | Jun09 03:53:18 | 单输出/单标签监测不能恢复同时instructions/constraints/subgoals→activation-conditioned set interpreter按覆盖/unsupported用judge-GRPO训练→内部读出须按多指令覆盖/幻增另校准，不预授faithfulness；2+2+2=6 |
| 09338 Multi-Hop Knowledge Composition | Jun08 11:05:17 | Jun09 03:48:12 | 单事实记住不保证implicit composition→固定individual暴露/未暴露与九data格式对照仍有97%单hop/组合缺口→重考虑pretrain composition人口而非只补知识；2+2+2=6 |
| 09079 FlashMemory-DS-V4 | Jun08 06:25:54 | Jun09 03:42:34 | 在线learned KV indexer训练可能需要大backbone→backbone-free dualencoder+lookahead KV chunk预测→训练摊销与未来读取分布校准成为独立约束；2+2+2=6 |
| 08048 PoE-Bridge | Jun06 08:21:06 | Jun09 03:20:00 | DLM proposal直接IS到AR有大distribution gap→中间PoE、并行draft/rejection再IS，混温/elasticwindow→target fidelity/particle/verification预算须联合比较；2+2+2=6 |
| 08327 CHIAR-Former | Jun06 20:38:42 | Jun09 03:26:10 | 每token全attention未必需要动态混合→v1四层DCT/RBF/attention entropy routing发现RBF collapse及不同任务胜负→重考虑spectralmixing边界，不能只因小模型排除；2+1+2=5 |
| 09287 Trajectory Geometry | Jun08 09:54:07 | Jun09 03:47:07 | 静态probe不描述层间路径→五ambient geometry统计与shuffle/random controls对promptfamily变化→可核表示诊断的测量身份/非因果边界，不预授complexity或universal phase；2+1+2=5 |
| 09514 BUDDY | Jun08 14:06:35 | Jun09 03:52:14 | 静态depth route不随decode history变/单budget→定额topk中间层+first-layer KV pool作globalcontext+optionalbudgetpredictor→层预算与动态KV身份/质量代价要分开；2+2+2=6 |
| 08411 AsyncLane | Jun07 02:24:11 | Jun09 03:27:59 | 完成本block才advance令尾残token阻塞→delimiter fork refine/generate、prefix仍可编辑、lane tree/sharedprefixbatch/refresh→依赖与commit/净调用费变化；2+2+2=6 |
| 09551 FuseFSS | Jun08 14:30:00 | Jun09 03:53:02 | 非线性fixedpoint逐operator协议→interval/polynomial/predicate spec编译成packedcomparison+vectorlookup两FSS→安全假设/精度与preprocessing/online费用须联合验收；2+2+2=6 |
| 09061 ChunkedPrefill Scheduling | Jun08 05:55:50 | Jun09 03:42:11 | 静态token预算+FCFS可能饥饿/jitter→age+remainingwork，LPRS时间预算与APC并发控制→空间结构和时间目标是不同旋钮；2+2+2=6 |
| 08382 STAR-KV | Jun07 00:24:02 | Jun09 03:27:21 | 低rank固定/启发选择→differentiable softthreshold按head/block调rank，K/V敏感度异分解+混精度→rank producer/校准费与执行净收益需分账；2+2+2=6 |

三项后版摘要信号需保：09563当前metadata改active→present，不能把v1“active”直接当causaltruth；09338后版camera-ready不借为当窗实证；09079v1只500K/13.5%KV，当前metadata的1M、8H20、2.8×throughput/2.7×concurrency是后版新增，不倒填。08327v1四层与PPL36.54vs66.62，不采用当前后版400M/MetaRouter和小corpus反向结论；这是明确重要修订信号，只核影响拟采用的v1边界，不扩整版史。09287 Jun10v2不凭版本号扩比较。

07665 AgentCompile v1（日期未决，非本窗确定候选）：SubmittedJun04 03:49:56Z→registeredJun09 03:11:34Z跨BJT多日。v1仅bounded advisory metadata→compiler templates/interface+hardware check/empirical validation/fallback，PyTorcheager三小模型；不借Augv2“直接生成五类kernel/vLLM对照”倒填。潜在贡献清楚但日期尚可执行定点恢复，暂不读全文/owner、不以登记日进候选；需原始公告/作者datedfirstpublic或其他合法界收窄。并非因小模型排除。

独立校准已完成：10项准入/日期通过，评分沿表5/6；09287经双方只点读§3.3–3.5/4.2/4.4/5.2/6后关闭贡献、不评分、不进owner。理由为150短prompt分类间描述几何、未独立控制length/pooling/复杂度，C1–C4只排部分替代，§6选层/干预/difficulty是待验假设，未修正具体机制或设计结论；不是小模型或‘观测一律无价值’。07665仍潜贡献日期未决，不入本窗确定候选。

上述为本批准入刚结束时历史停点。当前10项必要/actualowner与I/E/H均已完成独核，普通0，具体见SUP_BATCH4_SOURCE_OWNER及README；07665单篇潜贡献日期未决见BATCH6末节恢复，不扩Methods。后续已见Agent/多模态具名题摘亦已收束，剩余B6落实不因Books可能已有覆盖删池。
