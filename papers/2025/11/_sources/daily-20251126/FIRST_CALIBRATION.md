# Nov26 首批准入校准

作者Aristotle。窗口BJT[2025-11-25 09:00,2025-11-26 09:00)，UTC[Nov25 01Z,Nov26 01Z)。fresh已实际重读AGENTS、研究/Report合同、来源使用说明/Daily及按需/arxiv、Prompt、ROADMAP、最新11月checkpoint4/30；没有读其他日候选或旧Weekly。以下原源均本日新取得，不从25覆盖反推。

## 已准备好的拟入选

[Estimating AI productivity gains from Claude conversations](https://www.anthropic.com/research/estimating-productivity-gains)：本日GET productivity.html/receipt，published_time与JSON-LD datePublished均2025-11-25T11:05:00.000Z，即BJT19:05落窗；当前dateModified=2026-08-25T16:13:14Z，不称历史逐字冻结。正文Nov25；Bibtex却date=2025-11-05，原字段冲突保留，不能用citation自动当首公开，也不静默删除它。请root核日期权限及是否需定点恢复这个冲突。

完整官方核心/Validation/Limitations已实际读，raw-core-and-boundaries1.json、raw-screening-core2.json、raw-first-calibration-core3.json保留原请求/响应。文章经济外推不纳入本项目；仅拟采用其中评价proxy的具体反证：同模型在1800对话中对prompt变体的自一致性高，但1000 JIRA tasks的外部实际工时对照显著不同，估计压缩短/长任务差异且缺失chat后验证工作。新局部证据意味着自一致不能代外部校准，也不能把chat内估计节省当已验证端到端收益。原有“同意/稳定估计可代表完成成本”判断→文中实际外部对照与few-shot排序退化→应分别记录模型估计、外部elapsed/校验成本和适用人口。不是借成熟可观测性原则收经济预测。

拟2+1+2=5，标准审阅；只支持该任务人口/模型估计，不采用80%时间节省或1.8%宏观增速为实测系统收益。十示例少样本校准改善log相关却降低Spearman，不能写成全面更准。人类拥有代码库背景而模型只有ticket title/description，这个对照不是等信息条件的模型vs人类排名。未运行估算/重验dataset，不扩论文/宏观经济/RCT全附件。初筛主体及必要反侧已足够校准；如准入通过，Books再实际比PLATFORM-EVALUATION-SYSTEM的time-horizon/proxy论点，不因本文名称缺位造diff。

## 代表性排除待独立校准

[Expanding data residency access to business customers worldwide](https://openai.com/index/expanding-data-residency-access-to-business-customers-worldwide/)本日独立RSS1245项，窗口过滤仅此项，pubDate=Tue25Nov2025 22:00GMT。实际核心L29～45描述区域可用性、in-region at-rest storage与eligible customer/新workspace/APIproject；不能从at-rest扩成全推理路径或数据主权安全保证。暂拟贡献关闭：地区扩展本身没有披露新的存储/隔离机制或可归因设计成立条件，只是服务可用范围；若root判版本约束本身形成实际安全/兼容变化，应只重开此核心，不借成熟regional-policy原则收录。尚需补读API段尾部后最终关闭，不把“无算法名”作为理由。

## 来源停点

14每日入口均已实际首查，raw-native-0.json；各来源有限历史切片/分页仍普通待办，不称完成。OpenAI RSS、Anthropic native、Seed type1/2 p0、Hunyuan publicList、DeepSeek updates及四组arxiv窄主题已本日独立请求，receipt保存。arxiv提交发现区间Nov21 19Z～Nov24 19Z只是有界恢复候选，非实际public；74+10+82+34=200返回，169身份线索，不是本窗169新论文/全题摘队列。发现agent/领域条目较多，后续先收窄机制主题；只选与主线有关的具名精确v1补完整题摘，不遍历宽月表。cs.DC recent返回的是当前近月列表，不作2025历史覆盖；本日有界历史公告补检仍待。

请root现在独立校准本单项与代表性负侧，无需等来源全部完成。作者继续无关入口与窄主题初筛，Books仍root独占，不stage/commit/push。

## 负侧补读与八项 exact-v1 追加（2026-10-04T16:45:00+08:00）

Data residency原页API段L39～51已实际补读（raw-exactv1-gate4.json）：批准advanced-data-controls的enterprise customer新建regional Project，requests handled in-region且不存request/response at rest。保留API与workspace不同语义，不能把本文概括成“只有at-rest”。最终作者仍贡献关闭：此次公开是更多地区可用、既有控制使用说明与eligibility，未建立新的执行/隔离机制或原设计失效条件；不是说这些兼容事实没有价值，也不是因缺算法名关闭。不扩读当前2026条款来补2025新机制。

从本日独立原始窄主题标题定点8项，全部exact-v1完整题摘已实际读，raw-exactv1-gate4.json和raw-exactv1-fullabstract5.json。以下是潜在增量而非日期已确认候选，不因未给摘要实验细节关闭：

- An Online Fragmentation-Aware GPU Scheduler for Multi-Tenant MIG-based Clouds，2511.18906v1：固定MIG合法布局使连续arrival/departure碎片化，作者定义metric驱动greedy避免增量碎片；需核是否真正改变placement而非只另一分数，10%不作通用保证。submitted Nov24 09:10:35Z非public。
- VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking，2511.18692v1：activation-only neuron选择忽略flash连续访问开销→contiguous chunk按importance/estimated-latency筛选→同稀疏度不等同I/O执行成本；实际局部条件有潜在贡献，4.65/5.76只作者平台。submitted Nov24 02:27:19Z。
- Pier: Efficient Large Language Model pretraining with Relaxed Global Communication，2511.17849v1：DiLoCo outer optimizer的momentum warmup/decay与DP/TP执行相配，潜在优化/通信取舍；只摘要还不能认定无损与任意global通信都可稀释，需相同tokens/outer频率/收敛预算。submitted Nov22 00:29:04Z，v2 Nov26 21Z在本窗终点后，不借latest-v2。
- Nemotron-Flash: Towards Latency-Optimal Hybrid Small Language Models，2511.18890v1：同parameter deep-thin质量与real-device latency frontier分离，depth/width影响small batch、operator影响large batch；hybrid search与weight normalization具名机制需必要归因，不因小模型关闭或照录倍率。submitted Nov24 08:46:36Z。
- Equivalence of Context and Parameter Updates in Modern Transformer Blocks，2511.17864v1：token-dependent rank1/RMSNorm patch、input/output controllability的构造条件可能改变“prompt等同统一weight更新”的理解；必须核是否仅固定token/上下文、层级patch及可逆条件，不把精确表示扩成全函数/训练等价。submitted Nov22 01:17:15Z。
- Transformers with RL or SFT Provably Learn Sparse Boolean Functions, But Differently，2511.17852v1：单层Transformer、可分解fixed2-sparse函数及中间监督下，RL整链和SFT逐步学的不同学习动态；理论/小模型直接可支撑主线，不因简化关闭，需充分条件边界，不外推任意LLM。submitted Nov22 00:38:43Z。
- No Free Lunch in Language Model Bias Mitigation? Targeted Bias Reduction Can Exacerbate Unmitigated LLM Biases，2511.18635v1：4techniques/10models/7families在StereoSet多个axis的局部退化，潜在设计反证是单轴改善不能签发未目标轴/Coherence；不因既有多维安全原则就关闭新负证据。submitted Nov23 22:21:18Z，2026 journal reference不改归属。
- General Agentic Memory Via Deep Research，2511.18423v1：offline轻mem+complete page-store，online researcher按请求构造context，保留原信息而延后检索；不是JIT类比本身贡献，需必要对照区分更大context/test-time预算与实际二阶段收益。submitted Nov23 12:29:33Z。

各原页当前未列相关撤回标记；没有遍历版本史。上述初筛待root局部校准，普通下一步是有限首公开恢复/关键条件，而不是169条全题摘。之后相关新主题补检亦保持有界。
