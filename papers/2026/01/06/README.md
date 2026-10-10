# Daily Research — 2026-01-06

**规范：** V3
**窗口：** 2026-01-05T09:00:00+08:00 ～ 2026-01-06T09:00:00+08:00
**补充窗口：** 2026-01-05 ～ 2026-01-05
**窗口说明：** 用户授权保留已有候选、日期、评分与有效审阅，只补遗漏；旧09点窗口与旧材料原样保留，新增按前一完整北京时间自然日检查，不搬移归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T14:13:06+08:00

## 1. 结论

2026-10-07增量补查已处理14个每日源的Jan05自然日切片；新增确定落窗候选0，新增评分/证据审阅/Books修改均0。独立复核重取arXiv四主题156条重叠发现metadata，身份新增0，四组补窗old-update虽返回0，但字段被API改写为互斥submittedDate，不能支持零修订；不重开原55家族或扩大Submitted池。机构有限目录已核，Qwen60条完整日期、Hunyuan9条完整日期、AgentTech本页May13已获得有限处置，不要求历史无删除证明。14个每日源12已检查、2受阻（Google/Meta），另1辅助标题补检入口检索受限；必要具名RIMRULE/CSSBench修订日期保持终态请求。普通待办0，补查独立复核通过，完成表示安全终态，不表示互联网无遗漏或外部缺口消失。

本日候选清单冻结为55个唯一材料家族：15项实际整合、11项具体已有覆盖、21项仅报告/关闭、8项中心争议安全隔离。root负侧抽检重开00129后，实际原核心确认本次综合未披露新增可采用机制或对照边界，贡献前关闭通过；原55项结果不变，日级独立验收通过，普通待办0。四个arXiv主题查询156条含重叠metadata仅作发现；实际定点读72份完整v1题摘，不等于72候选或72证据审阅。55家族均已得到必要处置；宽metadata列表不是默认逐项审阅队列，贡献前关闭及窗外/归属未定线索留在本日原始记录，不计候选。

十五处受限长期增量已实际进入Ch12组合embedding、Ch21参数几何与功能分离、Ch49 kernel验收、Ch77保护开启条件、Ch69字段exposure、Ch72角色投影与guard身份、Ch27混语类型×任务敏感度、Ch28梯度代理、Ch66固定anchor独立fit、Ch17 rank-one carry/write、Ch24部署activation patch与单目合成退化训练接口、Ch36联邦MoE参与集合、Ch51 constraint调度/合法性分责与Ch78 scope/目标对象；root必要原源与实际写后通过。十一项具体已有覆盖、局部recipe关闭与八项中心争议分别归档；八项中心争议不作为正面证据或Books依据。机构历史切片、arXiv titlebackstop/public revision与mirror精确限制不支持无遗漏或性能/安全保证。

## 2. 来源覆盖

原始查询/执行时刻/停止依据见[本日查询与筛选](../_sources/daily-20260106/queries-and-screening.md)、[官方日期字段](../_sources/daily-20260106/official-date-slices.jsonl)、[arXiv原查询](../_sources/daily-20260106/arxiv-discovery-metadata.jsonl)。均仅本日窗口与当前主线主题；不扫描Weekly来源。

本次自然日实际重扫入口、查询/分页/停止与响应见[2026-10-07增量记录](../_sources/daily-20260106/supplement-20261007.md)。下表保留旧窗口依据，并分别标明补窗结果；没有新增按需触发，不扫描每周来源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 旧Research+RSS1243日期metadata，Jan2T10Z→Jan7T00Z；补窗fresh RSS1251日期metadata同邻接、Jan05自然日0，未读全年正文 | 已检查 | 有限公开入口不覆盖所有作者镜像 |
| SRC-ANTHROPIC | 旧Research HTML174 publishedOn，Dec19T19:45Z→Jan8T00Z；补窗fresh HTML139唯一日期同邻接、Jan05自然日0 | 已检查 | 有限Research目录，不等全机构事件 |
| SRC-GOOGLE-AI | 旧与补窗DeepMind第1页30/265、9页，Jan9→Dec3跨窗后停；fresh Google首15/11592为year目录，日期筛选URL不可读 | 受阻 | Jan05 first-public历史切片未恢复，不用年标签归属 |
| SRC-META-AI | 旧与fresh Research不可提取正文；补窗Jan05官方域窄搜索0后停 | 受阻 | Jan05事件日期列表不可恢复，搜索0不证明无事件 |
| SRC-QWEN | 独立恢复官方api/page_config?code=research.research-list，完整无序60条date全部读完，最大2025Dec23，Jan05条目0；旧站及新Blog壳失败保留 | 已检查 | 仅该完整返回目录，不据旧网页壳失败请求无具名线索的历史快照或无删除证明 |
| SRC-DEEPSEEK | 保留原news10日期；独立重开官方/news/，研究索引10条Jan12→Dec31、动态Apr24→Dec1均跨Jan05；可见列表处停 | 已检查 | 有限news切片，不要求查看更多或所有镜像的历史无删除证明 |
| SRC-MOONSHOT | 补窗Platform完整可见26条止Nov7；fresh releases100读到Oct24、Jan05 published_at0，changelog Jan4→Jan9；独立核Blog停点 | 已检查 | 有限官方Blog/release切片；没有具体Jan05遗漏线索，不请求全机构研究/修订档案 |
| SRC-TENCENT-HUNYUAN | Research网页/浏览器失败保留；official POST code0/total9/list9，完整publishedAt/displayPublishTime/publicAt日期读完，最早Feb3，Jan05条目0 | 已检查 | 有限9条官方目录；无具名Jan05遗漏/字段矛盾，不请求当期全历史快照或无删除证明，不称浏览器核查成功 |
| SRC-ZAI | 独立重开Research时间排序首15条，Jan13→Dec10/9已跨Jan05，在查看更多处停；release Jan14→Dec22 | 已检查 | 目标窗口已跨越，不因更早分页未取而请求Jan05目录；仅授有限切片 |
| SRC-BYTEDANCE-SEED | 补窗type1/2的2026ASC page0/count20，最早Jan19T16Z/Feb11T16Z均在Jan05之后；2025旧有效Dec14/Dec23切片保留。独立重取2025paper仍total94/has_more/next20但缺sub_article_list | 已检查 | 缺2025列表不是Jan05日期的必要缺口，不算空命中；不扩全年或授全机构无遗漏 |
| SRC-BAIDU-ERNIE | 旧与fresh Blog第一页Jan8→Dec23跨窗后停，无Jan05条 | 已检查 | 有限Blog目录 |
| SRC-XIAOMI-MIMO | Paper8条Jan8→Oct21保留；独立取官网路由数据16个EN Blog，逐个恢复正文/显式iframe：15个日期或月标签均窗外，blog1完整core仅泛能力描述、不准入 | 已检查 | frontmatter与HSS/Safety正文日期不同但均窗外，分别保留；不请求无贡献页日期或全历史档案 |
| SRC-MINIMAX | 独立重开EN/CN Blog，Jan27/28→Dec23跨Jan05后停；AgentTech原HTML恢复唯一2026May13日期及agent-team链接，本页读完 | 已检查 | 仅该有限目录；无具名Jan05线索，不因唯一晚页日期请求历史无删除/全站档案 |
| SRC-ARXIV | 旧72份定点v1题摘及55家族处置保留；补窗fresh四原主题Submitted缓冲start0/max100仍72/3/33/48，身份新增0；自然日old-update四组返回0但过滤被API改写为互斥submittedDate，旧稿修订发现不获阴性权限 | 已检查 | 原具名RIMRULE/CSSBench修订公开日期另保留，不由metadata反推；辅助标题入口受限另列，不请求全量公开批次 |
| 补检：[arXiv相关标题backstop](https://arxiv.org/list/cs.CL/2601?skip=0&show=25) | Jan05 cs.CL catchup与CL月首25定点恢复，未扩整月逐项筛选 | 检索受限 | catchup HTTP400、月首25Cache miss；只是辅助检索不可用，不请求全量批次或无删除证明 |

## 3. 候选与判断

本次补充窗口新增确定落窗家族0，不新增评分或候选行；以下55家族旧日期字段与原评分保留，未按本次自然日规则搬移。

下列区间起点统一为`2026-01-05T01:00:00Z`；upper加原日期字段与排程合取支持，本次不把registered伪装成公开时刻。详见原始[first-public](../_sources/daily-20260106/first-public-fields.jsonl)与[v1日期字段](../_sources/daily-20260106/date-fields-screened.jsonl)、[补充日期字段](../_sources/daily-20260106/date-fields-screened-02.jsonl)。无具体更早正文线索的普通首次announcement按官方假期与不可advance规则限定；若恢复相反公开事件，仅重开相关家族。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [The Trojan in the Vocabulary](https://arxiv.org/abs/2601.00065v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:19:31Z | donor系数跨base几何复用会改变组合风险，donor信任不自动继承；3+2+2=7 | 深入完成 | 整合：MODEL-EMBEDDING，[Ch12行几何](../../../../books/part-02-model/12-embedding.md#向量关系从训练目标中形成) |
| [Revati](https://arxiv.org/abs/2601.00397v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:27:18Z | 真实serving控制逻辑与虚拟时间/执行分责，需协调及值语义界限；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1332–1372 |
| [FlexSpec](https://arxiv.org/abs/2601.00644v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:33:02Z | frozen draft适配受限PEFT target family并调通信stride；2+2+2=6 | 争议 | 暂缓：随机exactness/stride中心目标缺口；Ch48已有受限anchor与通信边界未授争议保证 |
| [FlashInfer-Bench](https://arxiv.org/abs/2601.00227v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:18Z | 新增随机/确定性kernel不同测试对象与context生命周期；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49 learned-kernel admission](../../../../books/part-05-inference-system/49-tensorrt-llm.md#learned-kernel-只是-candidate-producercompiler-与-verifier-仍拥有-admission) |
| [Geometric Regularization in MoEs](https://arxiv.org/abs/2601.00457v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:28:43Z | weight proxy与routed activation不等价的受限反证；3+1+2=6 | 深入完成 | 整合：MODEL-MOE，[Ch21专家化边界](../../../../books/part-02-model/21-moe.md#专家化模块化与更新边界) |
| [CPPO](https://arxiv.org/abs/2601.00501v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:29:43Z | 熵差top-k与positive-advantage局部contrastive训练recipe；1+1+2=4 | 已关闭 | 仅报告：局部recipe不增加已解释的sensor/view/budget约束，不授per-token因果或通用收益 |
| [Belief Poisoning Attacks](https://arxiv.org/abs/2601.00240v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:36Z | 可写profile/memory会改变identity-dependent保护开启条件；3+2+2=7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 1136/1138：可信identity anchor与derived belief分权 |
| [FwPKM](https://arxiv.org/abs/2601.00671v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:33:39Z | static PKM到chunk-local可写容量与runtime-state边界；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) 630–660 |
| [Probabilistic Guarantees for Avoiding Hallucinations](https://arxiv.org/abs/2601.00641v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:32:58Z | 独立生成/固定oracle与judge错误条件下的重复选择保证；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-SAMPLING，[Ch20](../../../../books/part-02-model/20-sampling.md) 331–358/388–407；不采用任意低幻觉泛化 |
| [Online Finetuning Decision Transformers with Pure RL Gradients](https://arxiv.org/abs/2601.00167v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:21:53Z | 事后改return conditioning会使行为denominator失配；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 118–152/1988–1999；reset/Q局部recipe仅报告 |
| [Noise Optimization](https://arxiv.org/abs/2601.00090v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:20:05Z | 冻结生成器下联合quality/diversity初始noise局部recipe；1+1+2=4 | 已关闭 | 仅报告：不授Gaussian边际、等预算优势或生产SLO，未改变长期机制 |
| [Sigmoid Head](https://arxiv.org/abs/2601.00680v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:33:51Z | 冻结generator的独立sigmoid QE头与避dominant负采样配方；1+1+2=4 | 已关闭 | 仅报告：局部QE实现，不授校准概率或改变生成分布 |
| [Hierarchical LoRA-MoE for CTC Multilingual ASR](https://arxiv.org/abs/2601.00557v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:01Z | shared/lang-specific LoRA与LIDposterior驱动单pass局部routing；1+1+2=4 | 已关闭 | 仅报告：不把无预给language ID外推无训练language labels或通用解码优势 |
| [QSLM](https://arxiv.org/abs/2601.00679v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:33:50Z | spike-language模型的层敏感度tiered quantization搜索配方；1+1+2=4 | 已关闭 | 仅报告：局部量化配方，不采用通用power/memory/quality数字 |
| [MAESTRO](https://arxiv.org/abs/2601.00481v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:29:16Z | schema统一不等usage字段跨provider/transport/framework实际暴露；2+2+2=6 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69 LLM阶段](../../../../books/part-06-ai-infrastructure/69-trace.md#llm-trace-的阶段设计) |
| [Defensive M2S](https://arxiv.org/abs/2601.00454v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:28:39Z | user-only角色投影/template/guard联合验收有不同召回与遗漏边界；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72 observer边界](../../../../books/part-06-ai-infrastructure/72-security.md#从输入窗口到中间激活与权重observer-state-决定隐私边界) |
| [JourneyBench](https://arxiv.org/abs/2601.00596v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:55Z | workflow adherence、tool/参数和模拟用户错误分账的protocol；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) 880–938；Ch66 363–376 oracle边界 |
| [Right for the Wrong Reasons](https://arxiv.org/abs/2601.00513v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:30:00Z | outcome与显式reasoning-trace不一致的评价反证；2+2+2=6 | 争议 | 暂缓：judge/label/sampling/network/run identity中心冲突，不授内部faithfulness或10B阈值 |
| [Mixed-Language Pretraining](https://arxiv.org/abs/2601.00364v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:26:30Z | 真实web混语类型对翻译/理解任务敏感度不同的反证；3+1+2=6 | 深入完成 | 整合：TRAIN-DATA，[Ch27双语分支](../../../../books/part-04-training-system/27-data.md#双语词汇干预是可版本化的数据控制分支)，root写后通过 |
| [ReDGE](https://arxiv.org/abs/2601.00781v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:36:10Z | 解析categorical后验与有限transport/梯度proxy条件分账；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28梯度接口](../../../../books/part-04-training-system/28-pretraining.md#梯度不存在时训练必须改写更新接口)，root写后通过 |
| [JP-TL-Bench](https://arxiv.org/abs/2601.00223v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:12Z | 冻结anchor图、逐candidate独立fit隔离候选池耦合；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 judge ranking](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#judge-ranking-要同时校准局部比较与全局区间)，root写后通过 |
| [Deep Delta Learning](https://arxiv.org/abs/2601.00417v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:27:45Z | rank-one carry与同步write的条件性跨层替代分支；2+1+2=5 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17 depth routing](../../../../books/part-02-model/17-transformer-layer.md#residual-stream-从单一累加状态走向-depth-wise-routing)，root写后通过 |
| [ActErase](https://arxiv.org/abs/2601.00267v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:24:14Z | 冻结source activation/mask部署干预及多concept组合失效；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 1141/1143，root写后通过 |
| [CSSBench](https://arxiv.org/abs/2601.00588v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:44Z | 中文clean/semantic扰动paired安全协议；2+1+2=5 | 争议 | 暂缓：ORR的refusal与safe-answer标签冲突，未采用ORR/CER与总体排名 |
| [Trajectory Guard](https://arxiv.org/abs/2601.00516v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:30:04Z | task/trajectory双loss局部anomaly sensor；1+1+2=4 | 已关闭 | 仅报告：不替代policy gate，外部全anomaly集不授FPR或生产coverage |
| [ECR](https://arxiv.org/abs/2601.00543v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:30:41Z | offline teacher语义anchor与small projection局部配方；1+1+2=4 | 已关闭 | 仅报告：未增加模型系统的长期设计条件，不采用headline性能 |
| [FaithSCAN](https://arxiv.org/abs/2601.00269v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:24:17Z | uncertainty/visual/alignment三branch局部VQA detector配方；1+1+2=4 | 已关闭 | 仅报告：pseudo-supervision与diagnostic信号不证明内部因果或完备安全 |
| [From Sight to Insight](https://arxiv.org/abs/2601.00215v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:01Z | 图像→结构文本介入限定视觉与推理故障的分段诊断；3+1+2=6 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 58–65；不授encoder唯一因果 |
| [MetaJuLS](https://arxiv.org/abs/2601.00095v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:20:12Z | learned dirty-constraint priority与合法mask/closure不同责任；2+2+2=6 | 深入完成 | 整合：INFER-SGLANG，[Ch51](../../../../books/part-05-inference-system/51-sglang.md#structured-generation-也是-runtime-state) 130/132，root写后通过 |
| [CoRename](https://arxiv.org/abs/2601.00482v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:29:17Z | seed反馈推得scope、valid AST目标与用户批准分账；2+2+2=6 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md#安全执行需要-preventive-gate-与-evidential-gate) 549，root写后通过 |
| [WildAGTEval](https://arxiv.org/abs/2601.00268v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:24:15Z | spec/execution扰动与isolated/cumulative历史分账；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1295–1320，root具体通过 |
| [MalOptBench](https://arxiv.org/abs/2601.00213v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:22:59Z | 合法优化形式不排除有害目标组合的安全评价盲区；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 542–615，root具体通过 |
| [YapBench](https://arxiv.org/abs/2601.00624v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:32:34Z | minimal baseline/可见字符/类内median的冗长度量合同；2+1+2=5 | 标准完成 | 仅报告：没有correctness gate，不改变质量/成本联合验收原则，root必要通过 |

| [AEGIS](https://arxiv.org/abs/2601.00561v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:06Z | atomic checklist拆分有限多模态生成评价协议；2+1+2=5 | 标准完成 | 仅报告：有限judge×task协议不证明确定输出或knowledge因果，不重复Ch66一般测量原则 |

| [Compositional Diffusion with Guided Search for Long-Horizon Planning](https://arxiv.org/abs/2601.00126v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:20:56Z | overlap local-mode composition下population pruning/resampling；2+2+2=6 | 争议 | 暂缓：J与sorting方向中心冲突，受影响保证不入Books |
| [RMAAT: Astrocyte-Inspired Memory Compression and Replay for Efficient Long-Context Transformers](https://arxiv.org/abs/2601.00426v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:27:58Z | segment memory/recomputation替代与retention/backprop语义；2+2+2=6 | 争议 | 暂缓：retention→VJP与graph生命周期未决，受影响保证不入Books |
| [Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning](https://arxiv.org/abs/2601.00791v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:36:25Z | attention谱sensor与compiler validity标签的实质反证；3+1+2=6 | 争议 | 暂缓：sensor选中纠错gold不足独立校准，受影响保证不入Books |
| [Imitation from Observations with Trajectory-Level Generative Embeddings](https://arxiv.org/abs/2601.00452v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:28:36Z | trajectory diffusion embedding与近邻expert kernel reward替代；2+1+2=5 | 争议 | 暂缓：Eq2/Alg1/A2 reward接口冲突，受影响保证不入Books |
| [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://arxiv.org/abs/2601.00664v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:33:29Z | block diffusion forcing/rollingKV与交互条件分支；2+2+2=6 | 争议 | 暂缓：frame/block及future-condition availability身份未决，受影响保证不入Books |

| [GRIT -- Geometry-Aware PEFT with K-FAC Preconditioning, Fisher-Guided Reprojection, and Dynamic Rank Adaptation](https://arxiv.org/abs/2601.00231v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:24Z | factor-space KFAC/PA/PG动态rank局部优化配方；1+1+2=4 | 已关闭 | 仅报告：不借成熟Fisher/rank原则抬分，不授原显示公式的exact natural-gradient保证 |
| [Talk Less, Verify More: Improving LLM Assistants with Semantic Checks and Execution Feedback](https://arxiv.org/abs/2601.00224v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:23:14Z | reverse-code→intent Q*与反馈执行的局部配方；1+1+2=4 | 已关闭 | 仅报告：有限generator/discriminator配方，不采headline性能或企业级trust保证 |

| [Constructing a Neuro-Symbolic Mathematician from First Principles](https://arxiv.org/abs/2601.00125v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:20:54Z | ordered hypergraph scope与continuous witness/离散proof架构蓝图；2+1+2=5 | 标准完成 | 仅报告：faithfulness为公理，未量化verified prover，不改变当前正式证明authority链 |
| [The Reasoning-Creativity Trade-off: Toward Creativity-Driven Problem Solving](https://arxiv.org/abs/2601.00747v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:35:23Z | correctness双侧gate的PSD kernel语义冗余理论；2+1+2=5 | 标准完成 | 仅报告：finite simplex/interior理论不等现实SGD必保多样性 |
| [Memory Bank Compression for Continual Adaptation of Large Language Models](https://arxiv.org/abs/2601.00756v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:35:34Z | VQ index bank/fixed codebook与query KVLoRA调制接口；2+1+2=5 | 标准完成 | 仅报告：局部codec recipe，训练reset不冒充runtime换码本 |
| [InfoSynth: Information-Guided Benchmark Synthesis for LLMs](https://arxiv.org/abs/2601.00575v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:26Z | UMAP/kNN信息指标与生成反馈的benchmark surrogate；2+1+2=5 | 标准完成 | 仅报告：有限构建/筛选协议，不授semantic coverage或独立gold |
| [In Line with Context: Repository-Level Code Generation via Context Inlining](https://arxiv.org/abs/2601.00376v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:26:47Z | caller inlining/AST+LLM retrieval构造派生context view；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 72–97/307–319/440–465 |
| [RIMRULE: Improving Tool-Using Language Agents via MDL-Guided Rule Learning](https://arxiv.org/abs/2601.00086v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:19:59Z | failure trace规则抽取与MDL压缩/符号检索；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 957–980 |
| [Spatial4D-Bench: A Versatile 4D Spatial Intelligence Benchmark](https://arxiv.org/abs/2601.00092v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:20:08Z | modality/可见帧与空间题gold支持证据的有条件反证；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 575–584 |
| [Can Large Language Models Still Explain Themselves? Investigating the Impact of Quantization on Self-Explanations](https://arxiv.org/abs/2601.00282v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:24:36Z | 量化task accuracy不能代理self-explanation各评价对象；2+1+2=5 | 深入完成 | 仅报告：受限评价反证，不授内部faithfulness或参数信任保证 |

| [Robust Uncertainty Quantification for Factual Generation of Large Language Models](https://arxiv.org/abs/2601.00348v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:26:08Z | fake/multi-fact分型后组合外部signal的局部uncertainty recipe；1+1+2=4 | 已关闭 | 仅报告：有限fake/multi-fact场景，不把AUROC当intrinsic校准真值 |
| [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:29:54Z | RAG与compiler/CodeQL/KLEE多反馈的局部secure-code配方；1+1+2=4 | 已关闭 | 仅报告：未新增checker有效域或安全contract，不授完备安全 |
| [Rectifying Adversarial Examples Using Their Vulnerabilities](https://arxiv.org/abs/2601.00270v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:24:18Z | re-attack跨classifier边界的局部adversarial rectification；1+1+2=4 | 已关闭 | 仅报告：不采用任意attack或physical deployment安全保证 |
| [FreeText: Training-Free Text Rendering in Diffusion Transformers via Attention Localization and Spectral Glyph Injection](https://arxiv.org/abs/2601.00535v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:30:30Z | attention sink定位与glyphVAE/LogGabor条件注入生成分支；2+1+2=5 | 标准完成 | 仅报告：有限artifact recipe；deployment Y来源/定位正确保证隔离 |

| [NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos](https://arxiv.org/abs/2601.00393v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:27:11Z | 单目合成退化配对训练frozen video条件消费接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 1169，root实际写后通过 |
| [HFedMoE: Resource-aware Heterogeneous Federated Learning with Mixture-of-Experts](https://arxiv.org/abs/2601.00583v1) | 2026-01-05T01:00:00Z ～ 2026-01-05T02:31:37Z | sample forward/batch backward/usage upload三参与集合分责；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 399，root实际写后通过 |

## 4. 证据与知识整合

增量补查没有新增准入家族，故新增标准/深入审阅与Books修改均0；本次只复用原身份未变化的有效处置，不把摘要、metadata或目录零命中称新的证据审阅。原逐项证据如下。

### [The Trojan in the Vocabulary](https://arxiv.org/abs/2601.00065v1)

已读§3–4.3、§5.1–5.3/B；donor shared-row系数复用于base不是几何或行为等价。20小模型组合的SER仅target token emission，不等harm；LoRA后恢复还额外改norm。实际Ch12两段与首源注通过root写后；[完整必要证据与owner差异](../_sources/daily-20260106/tokenforge-source-owner-proposal.md)。

### [Revati](https://arxiv.org/abs/2601.00397v1)

§3.2–3.3/4.1–4.4/6.1–6.3/8支持真实控制路径+virtual compute/timekeeper；固定输出长度忽略EOS值依赖，jitter、collective与硬件predictor需单独核。有限H200实验不证明真实质量或通用误差界。Ch66所列局部已承载该命题，root原源与正文对读通过；[证据记录](../_sources/daily-20260106/first-three-evidence.md)。

### [FlexSpec](https://arxiv.org/abs/2601.00644v1)

§IV-A/B/C Algorithm2、§V-A/B。ID-only draft==target argmax verifier不足证明T1/top-p0.9随机分布等价；固定γ的线性分式目标不证明内点最佳stride。保反证、不降分删候选；Ch48只已有受限artifact/通信条件，未写这些保证，故不制造纠错diff。root必要原源/当前正文独立核通过；采用隔离与重开见§5。

### [FlashInfer-Bench](https://arxiv.org/abs/2601.00227v1)

§3.3/4.5的确定性容差、低精度匹配比例、sampling empirical TVD+mask rejection与isolated/persistent context分责是采用增量；有限频率不证明exact，harness开销不等SLO。2025Oct21 Blog已trace/apply/fallback，不重复计首次机制；正文不采用生成kernel优于native的矛盾数字。Ch49两段及首源注root实际POST通过；[必要原源](../_sources/daily-20260106/first-three-evidence.md)。

### [Geometric Regularization in MoEs](https://arxiv.org/abs/2601.00457v1)

§2/3.1–3.4/4/Limitations。Frobenius trace约束不保证固定输入quadratic form为零，正文修正原文“所有元素之和”；NanoGPT约130M、8/top2、6层，所测penalty的weight MSO反升、activation仍高，WikiText有局部小改善而PTB高方差。不采用p>.05=独立或所有正则化失效。Ch21两段及首源注root实际POST通过，未复现实验。

### [CPPO](https://arxiv.org/abs/2601.00501v1)

实际深入§3.2/4.1–4.4/6/8/10：entropy-change选位+双view InfoNCE及positive-advantage gate。view perturbation不是已验证的语义保留干预；Eq9/Algorithm1 normalization不同，MI界含假设，不证明token因果。Qwen2.5VL3/7B、ViRL39K、G5、2epochs对照，额外forward使作者训练时间增加约39%，相同epoch非compute-matched；hardware/precision=Not Disclosed。Ch33现1044–1048已有view、sensor非真值及budget取舍；新局部recipe仅报告，评分校准由root通过，非把成熟InfoNCE/GRPO算原创。

### [Belief Poisoning Attacks](https://arxiv.org/abs/2601.00240v1)

实际读§3/4/5/6、A2.1/A2.4的必要范围：角色可修改profile/memory并在reflection中重复消费，不是模型权重攻击。64个gpt4o-mini/AgentScope模拟agent；human仅framing，belief probe与人类规范解释不等内部因果识别或真人harm。A1 payoff方向与主文冲突，不采用方向性数字；prototype gate不证明完备防御。Ch77两段及首源注已通过root原源→owner与actual POST，不扩大权限；[必要证据及当前owner](../_sources/daily-20260106/fw-guarantee-belief-evidence.md)。

### [FwPKM](https://arxiv.org/abs/2601.00671v1)

实际§2/3/4/6及A/B必要范围支持chunk-local sparse fast weights及同row aggregation/lookahead。NIAH更改chunk并读1–4遍，不是单遍无损128K；参数增加与FLOPs相近不等吞吐不降。Ch22具体训练M0/runtime Mt、session ownership与回退已经承载，root实际source/current body复核通过；不采用Eq20未决符号或理论收敛保证。[必要证据](../_sources/daily-20260106/fw-guarantee-belief-evidence.md)。

### [Probabilistic Guarantees for Avoiding Hallucinations](https://arxiv.org/abs/2601.00641v1)

实际§2/3.1–3.4/Algorithm1/4的i.i.d generation、固定input/oracle与qTP/qFP是前提，不由fresh context自动保证；Qwen3-4B短提取与独立synthetic label-flip judge只支持受控实验。空judged-positive事件不是所有输出真错，偶数K strict-majority边界不照录。Ch20具体候选coverage、相关误差、独立selector信号与完整预算已经承载，root实际源→owner通过；不授真实LLM judge独立或通用任意低幻觉。[必要证据](../_sources/daily-20260106/fw-guarantee-belief-evidence.md)。

### [Online Finetuning Decision Transformers with Pure RL Gradients](https://arxiv.org/abs/2601.00167v1)

实际§3.1–3.3/4.1/4.3：按g_online采样后改用g_actual训练不能继续把旧policy(g_actual)当原行为denominator。监督hindsight仍有适用域，不否定所有relabeling。共同reset、L_eval环境步与不可reset的Q模型分别有成本，outer iteration不等compute matched。Ch33同condition ratio及on-policy source不等state一致已有具体承载，root实际原段与局部正文通过；[证据停点](../_sources/daily-20260106/necessary-evidence-02.md)。

### [Noise Optimization](https://arxiv.org/abs/2601.00090v1)

实际§3/4/A2/B：联合四noise、quality/diversity/prior-radius优化是局部recipe；pink FFT renormalization非Gaussian边际证明。64取4与100优化步不等预算，HPS有负侧；单A10080GB每步时间不等请求SLO，precision=Not Disclosed。身份与区间原字段已核，新增recipe评分4关闭；Ch24 213–215已有coupling保边际与优化改边际边界，本次不进一步采用。评分对象不是成熟tradeoff，也不是因Books已有降分。[必要证据](../_sources/daily-20260106/necessary-evidence-02.md)。

### [Sigmoid Head](https://arxiv.org/abs/2601.00680v1)

实际§2–5/Limitations后新增命题只取额外sigmoid头、十负样本避dominant的局部实现，不把成熟likelihood≠truth原则算原创。冻结generator、skipnegative不自动标correct，head分数不等生成分布或真实校准概率。EvalSelf XCOMET/Qwen72B伪gold、small-model最佳NS与大模型代理选配、部分Boosted负侧都限制收益。精确身份/date与仅报告理由已核；[原源边界](../_sources/daily-20260106/model-training-evidence.md)，未复现。

### [Hierarchical LoRA-MoE for CTC Multilingual ASR](https://arxiv.org/abs/2601.00557v1)

完整v1题摘和本日身份/原日期字段已核：CTC mHuBERT的shared/lang-specific LoRA与LIDposterior驱动routing是局部新配方，保候选并评分4关闭，不因声学实验范围外排除。推理不要求预给language ID不等训练未使用语言身份；单pass效率口号不当已核端到端性能。没有安全/纠错/重要修订实际信号，不为该局部配方另做全benchmark深入；仅报告，不改变长期机制。

### [QSLM](https://arxiv.org/abs/2601.00679v1)

完整v1题摘、精确身份/date已核：新增只有spike-language模型的global/block/module级敏感度search，借用的预算/Pareto取舍不算新贡献分。候选评分4关闭，并未排除所有小模型/编译优化研究。原文的86.5%memory与20%power为待核作者结果，本次不采用任何通用性能结论；没有实际安全/纠错/重要修订信号，局部recipe仅报告。

### [MAESTRO](https://arxiv.org/abs/2601.00481v1)

实际§3.1.1/3.1.2/4.1/4.3/5.1/A2.2：字段可能在provider响应、stream transport或framework hook丢失，统一OTEL schema不保证exposure。12 predefined instances、有限运行、Jaccard/LCS不等生产可移植性或因果归因，hardware/precision=Not Disclosed。Ch69两段及首注已由root实际源→owner/POST通过；[必要原源及scope](../_sources/daily-20260106/security-and-evaluation-evidence.md)。

### [Defensive M2S](https://arxiv.org/abs/2601.00454v1)

实际§3/4/5/Limitations/C2：压缩只取user角色，删assistant状态；模板对不同guard有明显负侧。93×含不同token构造/取消回复生成，不是同协议walltime；p=.12不证明等效，Longturn单seedFPR不混成SafeDial。Ch72两段+首注root原源→owner/POST通过，不保证完备防御；[必要原源](../_sources/daily-20260106/security-and-evaluation-evidence.md)。

### [JourneyBench](https://arxiv.org/abs/2601.00596v1)

实际§2/3/4/7/K：三SOP/703 datapoints/41tools、predetermined blackbox responses；UJCS序列任何missing/extra/order错误先归0，DPA改变节点prompt与tool exposure，不唯一归因大小。simulator生成缺失输入/提前终止不全归Agent失败，不认证所有合法异步路径或真实effect。Ch81 880–938与Ch66 363–376具体已有覆盖，root源/current body复核通过；[原源边界](../_sources/daily-20260106/security-and-evaluation-evidence.md)。

### [Right for the Wrong Reasons](https://arxiv.org/abs/2601.00513v1)

主文与A/B/C有judge身份、binary/ternary标签、T0/default0.7–1、391-input/5layer与512–256–128–1网络不一致；self-critique单prompt追加不当两阶段同预算。RIS测显式trace与judge标签，不识别内部反思机制，10,734 traces/三小模型不定义所有10B以下capacity阈值。root必要原文核通过中心争议暂缓，不制造现Ch66没有错误的纠正正文；恢复只需唯一run config、label校准与对应结果。[必要证据](../_sources/daily-20260106/security-and-evaluation-evidence.md)。

### [Mixed-Language Pretraining](https://arxiv.org/abs/2601.00364v1)

Mixed-Language v1实际§3–5/7显示parallel/code-switch任务敏感度反证；Latin语言对/1.35B、同step/token而非unique/domain全匹配、QA非全无影响。Ch27两段与首注root必要源→owner及actual POST通过；评分对象固定3+1+2=6，不把成熟跨语桥接加分。[完整必要证据](../_sources/daily-20260106/model-training-evidence.md)。

### [ReDGE](https://arxiv.org/abs/2601.00781v1)

ReDGE v1实际§3.2–3.4/4.1/Runtime/AppendixA.1中A1–2假设：posterior closedform不等finiteDDIM精确transport或无偏梯度，小时刻退化依赖schedule/固定其余grid/轨迹避开boundary。single f evaluation，sampler是f-independent additive成本；§4 schedule与§3/Fig1方向冲突不采配方。Ch28两段与首注root实际写后通过。[原必要证据](../_sources/daily-20260106/model-training-evidence.md)。

### [JP-TL-Bench](https://arxiv.org/abs/2601.00223v1)

JP-TL v1实际§3.2/4.1/4.3–4.7/5.2/5.3.1：freeze的是anchor graph/output/judge/aggregation身份而非每fit全部anchor参数；candidate-inclusive centering/refusal exclusion分别影响尺度/分母。结构可比不授未来endpoint或人类真值，70items/20anchors代价与人工支持边界保留。Ch66两段与首注root实际写后通过。[原必要证据](../_sources/daily-20260106/necessary-evidence-02.md)、[实际cache](../_sources/daily-20260106/core-2601.00223v1-selected.json)。

### [Deep Delta Learning](https://arxiv.org/abs/2601.00417v1)

实际§2.1–2.2/Eqs3–7、§3.1–3.3、§4.1–4.2。unit k/epsilon→0/fixed-input的carry谱范数界不授权input-dependent full Jacobian；同β gate作用carry erasure和write。论文无实验节，未采稳定训练或性能口号。Ch17两段与首注root必要原源→owner及actual POST通过；[必要证据](../_sources/daily-20260106/necessary-evidence-02.md)。

### [ActErase](https://arxiv.org/abs/2601.00267v1)

实际§3.1–3.3/4.1–4.2/4.5/A1–A3/C：source/target准备后冻结FFN source均值与mask，新路径patch非weight/data删除。OR/overlap平均的十concept退化与准备成本保留；50/30step冲突隔离，不采生产SLO或安全保证。Ch24两段+首注root必要原源→owner与actual POST通过；[证据停点](../_sources/daily-20260106/safety-necessary-evidence-02.md)。

### [CSSBench](https://arxiv.org/abs/2601.00588v1)

实际§3.1–3.4/4.1/4.3/Limitations；clean与pinyin/homophone/symbol/zero-width有限paired测试有增量，但§3.4把ORR定义refusal、§4.1实际judge标safe-answer，安全回答不能直接当拒答。root实际原段已核中心冲突；保5分安全必要审阅，不判整篇无效，不采用ORR/CER或整体排名。所测10个≤8B模型、greedy/有限格式不外推全部中文安全；[必要证据](../_sources/daily-20260106/evaluation-necessary-evidence-03.md)。

### [Trajectory Guard](https://arxiv.org/abs/2601.00516v1)

局部dual-loss recipe4但已实际深入安全必要Methodology/Architecture/HybridLoss/Dataset/Splits/Metrics/Latency/Limitations；外部RAS/WhoWhen全为anomaly，仅recall不能证明FPR或生产coverage。长valid轨迹误报、异构latency与11+step退化保留；sensor不获得authorization/commit权，未形成替代policy gate条件。root完整题摘准入/评分关闭校准通过；[证据](../_sources/daily-20260106/safety-necessary-evidence-02.md)。

### [ECR](https://arxiv.org/abs/2601.00543v1)

完整v1题摘与精确身份/date已核；新增只有offline teacher semantic anchors与small projection的compact-model局部训练配方，不把成熟distillation/geometry原则计入评分。效率/privacy应用口号没有具体安全约束变化，未采用100K corpus收益或无需运行成本保证。root完整题摘局部recipe4评分对象通过，不因小模型范围外排除。

### [FaithSCAN](https://arxiv.org/abs/2601.00269v1)

完整v1题摘与精确身份/date已核；内部uncertainty、visual和cross-modal三branch加attention与pseudo-supervision是局部detector配方，未证明内部电路因果。safety-critical是应用目标，不是实际部署安全约束变化；未采全面效率/可靠性保证，不自动扩大为全附件安全审阅。root完整题摘局部recipe4评分对象通过。

### [From Sight to Insight](https://arxiv.org/abs/2601.00215v1)

actual v1 §3/4.1–4.2/5.1–5.4/Limits与Table7，图像改结构文本同时改变可访问的信息与表示难度，不唯一隔离encoder。九类选取与Claude部分task退步、训练identity/表格冲突不支持所有任务或统一SFT/RL结论。Ch23 58–65具体recoverable/access/output分段诊断已承载，root实际selected必要段与owner复核通过；不称root读过Table7全部字段。[证据](../_sources/daily-20260106/formal-and-control-evidence-04.md)。

### [MetaJuLS](https://arxiv.org/abs/2601.00095v1)

actual v1 §2.1–2.2/3.1–3.3/4.2–4.5/6，GAT决定dirty propagator工作次序、domain-reduction/operation proxy反馈不拥有合法性与真实walltime认证权。十语言与mixed3task设置分别保留，纠正English-only猜测；fallback entropy不是全部难例/错误检测器。Ch51 130/132已融入固定顺序→学习调度→合法mask提交责任→语义prefix两种保证；工程closure要求明确为推导，非作者已实现能力。root必要source→owner及actual POST通过。[证据](../_sources/daily-20260106/formal-and-control-evidence-04.md)。

### [CoRename](https://arxiv.org/abs/2601.00482v1)

actual完整HTML题摘及§3/4.1.1–4.1.2/5.3–5.5/7，seed/feedback所得scope是候选匹配，不批准全scope；closestline可能找到valid但wrong AST，comments另走findreplace。oracle模拟accept不证明真实human判断，baseline失败排除/Java单commit及人工IDE成本限制不采用通用F1或安全保证。Ch78 549唯一窄段已融入unique-anchor/expectedold，root必要source→owner通过，actual POST通过。[证据](../_sources/daily-20260106/formal-and-control-evidence-04.md)。

### [WildAGTEval](https://arxiv.org/abs/2601.00268v1)

actual v1 §3–5/Limits/AppB，300conversations/86APIs/60scenarios是构建、50stratified实际评价，coreAPI set exact不认证所有合法顺序、ordinal judge不是真实effect。spec与execution复杂度分相、gold-prefix孤立与predicted-prefix累积测试已被Ch66 1295–1320具体承载；root必要source与actual owner核通过，无新Books。[证据](../_sources/daily-20260106/evaluation-necessary-evidence-03.md)。

### [MalOptBench](https://arxiv.org/abs/2601.00213v1)

actual §3/4/5.1必要部分/5.2/5.3/Limits，四task60改写、ASR any3与成功sample harm不能当真实执行/事故率，token删除importance不证明Attention因果。合法算法形式与goal/effect授权不同，Ch72 542–615实际承载dual-use与组合目标边界，root必要source/current body核通过具体已有覆盖。[证据](../_sources/daily-20260106/safety-necessary-evidence-02.md)。

### [YapBench](https://arxiv.org/abs/2601.00624v1)

actual §3/4/5必要指标与7限制，304英语/76endpoint、可见字符排reasoning/markdown，YapScore=max(0,L−B)没有correctness gate。0分不证明充分，YapTax token均值与字符median不是同一成本对象；仅报告有界可复查测量协议，不复制现Ch66长度偏置/质量成本原则。root actual必要source→owner核通过5分标准完成。[证据](../_sources/daily-20260106/evaluation-necessary-evidence-03.md)。

### [AEGIS](https://arxiv.org/abs/2601.00561v1)

actual v1 §3.3/4.5必要评价核；Gemini atomic yes/no checklist经人工去冗余，有限judge×task的一致度不证明deterministic输出或知识因果。人工仅10%题，interleaved83.9与总体90.7分账；GPT5 Editing agreement54.8也不授跨task通用judge。root actual必要source及Ch66 rubric/label、judge任务与agreement论点核通过5分标准仅报告，不新增Books。[证据](../_sources/daily-20260106/evaluation-necessary-evidence-03.md)。

### [Compositional Diffusion with Guided Search for Long-Horizon Planning](https://arxiv.org/abs/2601.00126v1)

v1 §3.1 Eq5的g↑而J=prod exp(−g)↓，与Alg1 minJ/文字lowquality highJ方向冲突；Bethe/local conditional近似不是全局正确。Table1借baseline/100trials5seeds与Table2 privileged PDDL条件不合并。root实际§3.1决定性原段核通过终态暂缓，不采用pruning可靠性或统一性能，不把一般composition事实判无效。[必要证据](../_sources/daily-20260106/generation-and-memory-evidence.md)。

### [RMAAT: Astrocyte-Inspired Memory Compression and Replay for Efficient Long-Context Transformers](https://arxiv.org/abs/2601.00426v1)

v1 §3.3/3.4/4.1–4.2及AppD；retention仅缩放固定M×d状态，消融memory仍3.4GB。AppD line10重算m'未在line13显式重建retention scale却称AD隐式含它；line12先backward释放graph，随后line13 retain身份不明。root actualAppD核通过隔离，不称代码执行失败或所有梯度错，不能采用exact-equivalence/性能归因。[必要证据](../_sources/daily-20260106/representation-sensors-evidence-06.md)。

### [Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning](https://arxiv.org/abs/2601.00791v1)

v1 §3.1–3.4、4.7、5.2–5.4、D.1；heldout/nested结果不等全data最优。§5.3按spectral-vs-Lean disagreement manual correction并出现每model不同gold，无法当独立盲标；mass s_h=N的标准情形退化uniform，Table19差异仅作者记录未获root实际核，不作为新增被确认断言。root actual5.3/D.1及aggregation原段核通过中心暂缓，不授有效proof classifier或attention因果。[必要证据](../_sources/daily-20260106/representation-sensors-evidence-06.md)。

### [Imitation from Observations with Trajectory-Level Generative Embeddings](https://arxiv.org/abs/2601.00452v1)

v1 §4.1–4.3及A2；mu已含200/30expert轨迹，不把DE=1说成全部支持独立。Eq2 mean f(d/σ)、Alg1 f(−d/σ)符号不同，A2又logsumexp kernel；非线性reward变换不自动保同一最优策略。root actual三个决定性原段核通过终态隔离，不采用统一reward/performance recipe，有限trajectory表示不因此作废。[必要证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://arxiv.org/abs/2601.00664v1)

v1 InteractiveMotion/TrainingInference/5.2及必要4.2/5.5；Eq5 floorblock+l却l标frames，§5.2 B还代表blockcount。future noisy state与部署真实future条件未精确定义，root actual决定性段核通过隔离strict-causal/availability保证。H10010NFE25fps计时预提audio仅motion生成，非E2E500ms；synthetic DPO loser另训onlyaudio，不将所有一般block生成判错。[必要证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [GRIT -- Geometry-Aware PEFT with K-FAC Preconditioning, Fisher-Guided Reprojection, and Dynamic Rank Adaptation](https://arxiv.org/abs/2601.00231v1)

actual v1 §2.1–2.4与§3 Table1；拟新增仅factor-space KFAC及PA/PG动态rank的局部recipe，不把Fisher/有效rank成熟原则计原创。原显示r×r矩阵与deltaW梯度维度身份冲突保留，不能授exact natural gradient；已有Ch30 optimizer/rank约束不作为降分理由。root实际局部recipe4关闭校准通过；未采用runtime/A8保证，不为关项遍历全部附录。[证据](../_sources/daily-20260106/necessary-evidence-02.md)。

### [Talk Less, Verify More: Improving LLM Assistants with Semantic Checks and Execution Feedback](https://arxiv.org/abs/2601.00224v1)

完整v1题摘的Q* reverse code→intent match与Feedback+execution局部配方身份/date已核，root局部recipe4关闭认可。不将成熟独立validation或测试原则当新增机制，不采用performance headline/企业trust；一次HTML404不是贡献关闭理由，也不伪称全文不可恢复。[证据](../_sources/daily-20260106/benchmark-and-generation-evidence-05.md)。

### [Constructing a Neuro-Symbolic Mathematician from First Principles](https://arxiv.org/abs/2601.00125v1)

actual v1 §2.1/3.1/3.2–3.4/A1–A2；faithful/nonnegative/smooth是前提，zero energy iff truth不是engine自动保证。连续witness搜索与离散proof action是受限蓝图，§7 preliminary没有统一量化对照，既不因缺artifact排除，也不采verified prover/miniF2F加速。root actual2.1/3.1/A1/A2核；5标准仅报告，不将特定数学solver机械归工具schema owner。[证据](../_sources/daily-20260106/formal-and-control-evidence-04.md)。

### [The Reasoning-Creativity Trade-off: Toward Creativity-Driven Problem Solving](https://arxiv.org/abs/2601.00747v1)

actual v1 §3.2–3.4/4.1–4.4/5.3/6.4/7.1；bounded utility、PSD kernel、interior entropy barrier的Shahshahani flow不等现实parametric SGD，O(B²)及verifier/semantic kernel有成本。没有LLM训练实测，未采用SGD-realization保证，故该未采层不构成本窗普通待办。root actual3.2/3.3/6.4/7.1及Ch33 1415–1442核通过5标准仅报告，不重复correct-mode/reference校准原则。[证据](../_sources/daily-20260106/model-training-evidence.md)。

### [Memory Bank Compression for Continual Adaptation of Large Language Models](https://arxiv.org/abs/2601.00756v1)

actual v1 §3.3/3.4/3.6/4.2–4.4；online codebook reset属于训练，runtime仅forward编码/量化追加indices，不反向更换码本。bank footprint不含整个model/encoder/workspace，retention相对200document基线非永久无损。root实际训练reset/线上fixed-codebook append及KVLoRA、Ch22 915–941核通过5仅报告，不重复model-bound压缩schema/provenance/refresh与raw evidence回退。[证据](../_sources/daily-20260106/generation-and-memory-evidence.md)。

### [InfoSynth: Information-Guided Benchmark Synthesis for LLMs](https://arxiv.org/abs/2601.00575v1)

actual v1 §3.1/3.2.1–3.2.2/4.1/5.4等；negativeKL估计、matched N entropy及UMAP随机性不能认证原空间semantic覆盖。co-generated solution/test执行只证局部一致，statement修改和困难题filter改变评价身份/分母。root实际KL负值、匹配N与filter困难项核通过5标准仅报告，不把成熟truth/contamination原则计为新贡献或写入配方段。[证据](../_sources/daily-20260106/benchmark-and-generation-evidence-05.md)。

### [In Line with Context: Repository-Level Code Generation via Context Inlining](https://arxiv.org/abs/2601.00376v1)

actual v1 §3.3.1–3.3.2/3.4/4.2/4.4；naive参数/return替换不保证capture/earlyreturn/effects语义，context重写不是实际执行。Qwen1.5B辅助PPL的40/40/20quantile非生成正确校准，EM/ES/ID.F1明确无Pass@k。root实际retrieval/metrics及Ch75 72–97/307–319/440–465核通过5具体Existing：dependency充分、原source与派生view、gold/span/下游结果分账；不授upstream等价。[证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [RIMRULE: Improving Tool-Using Language Agents via MDL-Guided Rule Learning](https://arxiv.org/abs/2601.00086v1)

actual v1 §2.1–2.3/3及4必要；fixed fields先filter可用tool后排序，只提供advisory。MDL plug-in entropy全对/全错均0，不直接奖励更多正确；α在failure集选择不是独立heldout，greedy非全局。ToolHop跨model58.1→57.4负侧保留。root实际MDL/α/greedy与Ch77 scope/version/advisory/原episode回退核通过6标准具体Existing，不采用原错误的熵单调说明；v2 public未定另隔离。[证据](../_sources/daily-20260106/necessary-evidence-02.md)。

### [Spatial4D-Bench: A Versatile 4D Spatial Intelligence Benchmark](https://arxiv.org/abs/2601.00092v1)

actual v1 DataUnification/QA/EvaluationProtocol及两ablation；40K数据非直接human基线，MCA zero-shot与NA MRA不合并。64frames/单帧/blind有部分盲侧较强，不唯一归因language prior；5/10/30min对应不同subset，不授时长因果。root actualdataunification/QA/zero-shotMCA/MRA及Ch66 modal necessity、visible-frame gold slice核通过5具体Existing，未冒充所有deep ablation已由root核。[证据](../_sources/daily-20260106/benchmark-and-generation-evidence-05.md)。

### [Can Large Language Models Still Explain Themselves? Investigating the Impact of Quantization on Self-Explanations](https://arxiv.org/abs/2601.00282v1)

actual v1 §3.3/3.4/4.1.1/4.2/4.3.2/5.2–5.3及C；weights-only PTQ六7–72B的NLE/CFE是不同proxy，自我一致/CC-SHAP不认证内部reasoning。48nativeEnglish人/30indices、排14B与judge agreement≠human correlation限制保留，不采统一退化/量化confidence唯一因果。root实际ranking/user-study/judge相关及Ch49 1032–1045三层验收核通过5受限反证，仅报告；未授所有模型或未来endpoint可靠性。[证据](../_sources/daily-20260106/evaluation-necessary-evidence-03.md)。

### [Robust Uncertainty Quantification for Factual Generation of Large Language Models](https://arxiv.org/abs/2601.00348v1)

actual v1 III-A/III-C、IV-A/IV-B1–2；NLI拒答/BM25 Wikidata/外judge的FR/FT/FF分类进入局部logit公式，不是纯模型内部概率。77fake+50real、四model/五sample部分退步；保fake/multi-fact这一适用场景，不将平均AUROC推广为calibratedtruth或跨场景无外部成本。root实际完整AB、局部recipe及有限对照校准通过4关闭；未采headline性能。[证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509v1)

完整exact-v1题摘新增RAG repair与compiler/CodeQL/KLEE多工具feedback局部组合，未披露改变checker有效域/安全contract或原设计结论的反证，不把安全标题自动升级全附件深入。root actual完整AB及具体recipe4关闭认可；不采用漏洞降低数字、真实deployment或semantic/security完备。新增date-fields-safec保raw Submitted Jan1T23:34Z/registered Jan5T02:29:54Z，仍与官方延迟公告/identifier规则合取，不把registration伪装public瞬时。[证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [Rectifying Adversarial Examples Using Their Vulnerabilities](https://arxiv.org/abs/2601.00270v1)

完整exact-v1题摘新增利用adversarial sample脆弱性再attack、跨decision boundary的局部rectification，不是已实测physical部署安全contract变化；autonomous-driving应用举例不授真实控制安全。root actual完整AB、局部recipe/有限对照边界核通过4关闭，不采任意attack保证或performance headline。[证据](../_sources/daily-20260106/context-reward-evidence-07.md)。

### [FreeText: Training-Free Text Rendering in Diffusion Transformers via Attention Localization and Spectral Glyph Injection](https://arxiv.org/abs/2601.00535v1)

actual exact-v1 §3.1.2/3.2.1–3.2.3/4.4/4.5必要；reference Y IoU选timelayer，未明部署Y来源/heldout calibration，不能猜intrinsic localization或attention因果。glyphVAE/noisealigned/LogGabor与annealed masked guidance是公开局部条件分支，不因一层保证未知冻结全部事实。Flux fullAes5.342低base5.365，不授全质量保持；A6000/bf16/928²50step仅有限artifact成本。root实际referenceY/noisealigned glyph及ablation必要核通过5标准OnlyReport，不写Book或SLO保证。[证据](../_sources/daily-20260106/benchmark-and-generation-evidence-05.md)。

### [NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos](https://arxiv.org/abs/2601.00393v1)

actual v1 bidirectional motion/sparse keyframe/degradation/conditioning/generation及必要反证。新相机visibility cull/depth-average退化后render回原view，以原video为target训练frozenbackbone的control branch，缺novel-view配对truth时改变训练选择；短邻域近线性插值与遮挡/二维/文字失败限制保留，不把hallucinated细节当3Dtruth、action cause或普遍speedup。root实际核心与Ch24/25差异核授权，Ch24 1169单段+1491首注已通过actual POST及camera/motion前后，锁释放。[证据](../_sources/daily-20260106/generation-and-memory-evidence.md)。

### [HFedMoE: Resource-aware Heterogeneous Federated Learning with Mixture-of-Experts](https://arxiv.org/abs/2601.00583v1)

actual v1 III-D2/III-E1–2及必要IV/V-C条件。sample forward路由、资源budget backwardmask和usage-threshold upload三集合不同，更新参与身份是工程要求，不由usage补出weightnormalization或完整作者实现。Eq17/20/21符号/聚合争议及模拟设备caps保留，不授IB最优、variance必降、forward峰值降低或production可行。root实际D2/E1、ownerfed段核授权，Ch36 399单段+1745首注经actual POST及前后核通过，锁释放。[证据](../_sources/daily-20260106/generation-and-memory-evidence.md)。

## 5. 缺口与下一步

本轮可执行补查与独立复核已结束，普通待办0。必要外部保留限于Google Jan05 first-public、Meta日级日期入口，以及原具名RIMRULE v2/CSSBench v2公开日期；arXiv辅助标题入口只记检索受限，不索全量批次。具体原因、官方日期/具名事件替代及定点重开见[增量记录](../_sources/daily-20260106/supplement-20261007.md#独立补查复核与终态)。Qwen/Hunyuan完整有限返回、AgentTech单May13、Seed2025缺响应、ZAI更早页与MiMo无贡献无日页面均不产生泛化历史请求；不要求全机构无删除证明。外部保留不支持正面候选、Books、无遗漏或Coverage通过。以下旧终态争议及具名材料请求保持原样。

普通待办：0。00129定点重开与修正后的贡献前关闭已获root实际原核心独立复核；原55家族必要审阅、Books处置及15项实际写后均通过，root日级Gate通过。下列仍为本窗终态保留项，材料恢复后仅定点重开，不扩新库存。

外部来源保留以本轮上段及§2为准，旧八组泛化请求已由有限目录证据收窄；不删除原日期未定家族及RIMRULE/CSSBench具名修订请求。catchup/月目录title backstop仅检索受限，query0/holiday不授全量召回，也不因此请求全量公开批次/全部作者镜像/历史版本证明。恢复具体入口或具名事件后仅重开相应source/window/family，不支持无遗漏。

FlexSpec中心争议：需精确随机verifier（概率/残差重采样或等价证明）、accepted-length模型及同quality/通信约束下stride目标材料；现不将exactness/内点最优作为正面证据或Books结论。原必要HTML可读，不误写访问受阻。只重开00644受影响命题。

RWR中心争议：请求精确judge identity、binary/ternary标签映射、sampling温度、network输入层配置与run对应表，以解决主文/Appendix A–C所披露配置冲突；可接受作者勘误或精确artifact/config与结果映射。现不采用内部faithfulness、10B阈值、两阶段同预算或RIS/F1因果，只重开00513受影响评价命题，不把正文可读误写访问故障。

日期未定线索及RIMRULE v2公开事件：保原字段，需实际public announcement/作者first-public证据使区间完全落窗；不能由Submitted/Updated或后继metadata反推。late009xx/02404/11580的upper在窗外，不扩本窗或另开日期。具体身份/raw字段已留在本日原始日期记录；归属未确定部分只作精确终态保留，不作全部revision/mirror归属完成声明。

CSSBench v1中心标签争议：只请求ORR refusal/safe-answer的精确parser和映射、与human refusal标签校准及其对应CER结果；不能由二者混名授安全提升。v2 Submitted Jan5T04:37:42Z/Updated Jan6T01:58:45Z不足证明v2落窗，恢复实际公开批次后仅审影响该命题的精确修订，不继承v1或扩大窗口。

[Compositional Diffusion with Guided Search for Long-Horizon Planning](https://arxiv.org/abs/2601.00126v1)中心争议终态保留：需唯一ranking score/排序方向及匹配实现/config或作者勘误，重开00126受影响pruning命题；必要HTML可读但中心接口不唯一，不作为正面证据/Books或性能保证。

[RMAAT: Astrocyte-Inspired Memory Compression and Replay for Efficient Long-Context Transformers](https://arxiv.org/abs/2601.00426v1)中心争议终态保留：需精确可执行实现或勘误，给detached state、retention乘法、两个VJP及gradient累积/graph保留次序的run映射，重开00426相关梯度命题；必要HTML可读但中心接口不唯一，不作为正面证据/Books或性能保证。

[Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning](https://arxiv.org/abs/2601.00791v1)中心争议终态保留：需独立blind统一proof-adjudication、parser/version及exact scorer/aggregation/config，解释指标与标签身份，重开00791有效性评价命题；必要HTML可读但中心接口不唯一，不作为正面证据/Books或性能保证。

[Imitation from Observations with Trajectory-Level Generative Embeddings](https://arxiv.org/abs/2601.00452v1)中心争议终态保留：需精确actualreward code/config或勘误、state-only/state-action encoder映射与run对应表，重开00452相关reward/性能命题；必要HTML可读但中心接口不唯一，不作为正面证据/Books或性能保证。

[Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://arxiv.org/abs/2601.00664v1)中心争议终态保留：需exact mask/index、frame/block单位、在线可得condition window与对应latency配置或勘误，重开00664严格因果/延迟命题；必要HTML可读但中心接口不唯一，不作为正面证据/Books或性能保证。

[FreeText](https://arxiv.org/abs/2601.00535v1)定位保证终态保留：若要采用完全intrinsic部署定位或正确性，需reference Y来源、t/layer选择的calibration/heldout分离与精确artifact配置或勘误。当前有限公开glyph生成分支仅报告，不将此保证作正面证据/Books，也不因该未知冻结整项。

[HFedMoE](https://arxiv.org/abs/2601.00583v1)聚合保证终态保留：如要采用原algorithm的归一平均、IB最优或variance/performance主张，需Eq17/20/21唯一score/weight定义、usage-vs-actualupdate规则及精确config/run对应，或作者勘误；当前仅采用工程三账分责，不静默修正公式或为该未采用保证卡住已支持机制。

## 6. 复核

2026-10-07增量补查复核者：audit_supp_jan06（独立于作者supp_jan06）。结论：通过。实际核14源本轮入口/主题/停止与原记录；独立重开Google、Meta、Qwen、DeepSeek、Kimi、Hunyuan、ZAI、Seed、MiMo、MiniMax目录及arXiv补检，重取八条arXiv API查询（四incoming identity新增0，四old-update均0）。MiMo16个EN路由15项窗外、一项完整core贡献前关闭；不把无日泛能力页作候选或材料请求。纠正有限目录被泛化受阻及全机构档案请求；14:13定点读取Qwen官方60条无序完整date、AgentTech唯一May13，并复核Hunyuan完整9条日期，无具名Jan05线索，不建立历史无删除请求。最终14每日源12已检查、Google/Meta2受阻，另arXiv辅助标题入口1检索受限；仅原具名RIM/CSS等必要日期请求保留，外部hold不作覆盖通过。全部新增拟入选0，无新增标准/深入审阅或Books写入；原55行候选日期/评分及§4证据原样保留、有效旧复核复用，未无差别重读原55或附件。机器校验另附，不代替该有限语义验收。以下保留旧窗口实际复核记录。 后续独立核API返回的查询标题确认lastUpdatedDate未按请求生效，而被改写成与另一submittedDate互斥的过滤；上述0响应只保留请求事实，不支持旧稿零更新/零公开修订。

本轮机器检查：V3单日报告结构/一致性校验通过；本日两文件局部链接无缺失、限定diff检查通过；§3候选与§4证据合并内容在独立复核写回前后完全一致（55候选行）。这些检查不证明无遗漏或原实验复现。

复核者：root

结论：通过

root已实际首批准入校准及定点必要源→owner复核：Tokenforge/FlashInfer/MoE/BPA/MAESTRO/M2S/MixedLanguage/ReDGE/JP-TL/DDL/ActErase/MetaJuLS/CoRename/NeoVerse/HFedMoE十五处实际正文与前后、首注写后通过；Revati/FwPKM/00641/OnlineDT/Journey/FromSight/Wild/MalOpt/Inline/RIM/Spatial十一项具体已有覆盖通过；Yap/AEGIS/Mathesis/DCR/MBC/InfoSynth/FreeText标准仅报告与00282受限反证深入必要核通过；RU/SAFE-C/Rectify完整AB局部recipe4关闭通过；FlexSpec/RWR/CSS/CDGS/RMAAT/Geometry/TGE/Avatar八项争议必要命题核通过；CPPO/Sigmoid/HLoRA/QSLM/TG/ECR/FaithSCAN评分对象校准通过，Noise/GRIT/TalkLess具体局部recipe4关闭已校准。全部55拟入选的必要命题和具体Books处置已分批核；8争议项为受影响保证的安全终态而非正面Evidence通过。

来源/主题/关闭理由分层负侧实际样本为00081/00097、MotionPhysics/RGBIR/Omni/Sphere六项既已核、00202/00245/00444/00553四份完整v1题摘新增抽核，以及00129一项完整题摘后重开§2.1–2.3/3.1–3.3/4与对应引用的必要核心。00129原标签关闭不足已纠正，具体dynamic/ADC/co-sparse/P&R机制对应已引工作，本次综合/方向未披露新可采用机制或对照边界；不按photonic或综述标签关闭。其他普通负侧未全量独立核，不称全部156metadata、所有附件或全互联网验证。root同时核14来源有限历史切片/原查询停止、日期区间、六部分一致性与终态隔离，正式日级Gate通过。外部来源/公开revision-mirror/titlebackstop限制仍不授正面Coverage/Evidence、Books或无遗漏。完成态格式校验与限定diffcheck仅是接口检查，不替代上述语义验收。
