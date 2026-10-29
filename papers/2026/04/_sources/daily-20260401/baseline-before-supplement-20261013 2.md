# Daily Research — 2026-04-01

**规范：** V3
**窗口：** 2026-03-31T09:00:00+08:00 ～ 2026-04-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T02:07:56+08:00

## 1. 结论

本次重审不能沿用旧日报的 `V2.1 Complete`。旧报告以 DataCite 创建日代理 arXiv 公告、仅列 arXiv 来源，并把 34 篇全部当候选；其中部分题摘是后续版本而非 v1。旧版原文完整保存在[当日来源存档](../_sources/daily-20260401/LEGACY_V21_REPORT.md)，本次校正的查询、题摘与单篇审阅见[当日 V3 checkpoint](../_sources/daily-20260401/V3_REVIEW_CHECKPOINT.md)。

本轮对旧 516 条 arXiv identity 做主题标题筛选，对拟入选、强信号排除项和分层抽样排除项读题摘；旧 34 项与关闭侧均经定点反向核查。进一步读正文后，OccSim、VecAttention、DIAL、SkillReducer、ASI-Evolve 的具体命题已由现有章节覆盖，低分且已有完整机制承载的 StepCache 降为前分母关闭；从旧关闭侧恢复的 SLVMEval 带出长视频生成 evaluator 准入的新增命题。经本次独立复核，冻结为 **20 个唯一 Source Family**；这不等于 516 项均经全文或逐篇精确公告分钟审计。PolarQuant、APEX-EM、ConSelf、Xuanwu 等强信号排除项均有具体原因，见来源审阅。OpenAI Research 分页和 Meta Research 经有界尝试仍缺可靠停点，均被隔离；不能声称“当天无遗漏”。

已独立对照书稿，CRAFT、OptiMer、单向量检索、Video-Oasis、SLVMEval、语义 memory pipeline、kernel 物理下界、SysOM、BenchScope、DUME、Concept Training、ShapE-GRPO 与 FlexMem 的有条件命题已由主任务写入对应章节，并核对了其余候选的已有覆盖判断。具体来源与边界见下文；隔离来源和争议论文均未作为正面证据。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [Research](https://openai.com/research/) 与 [Research index](https://openai.com/research/index/) 可见首屏，止于 2026-08-18；[News RSS](https://openai.com/news/rss.xml) 在本窗有融资/算力公司声明、无技术研究条目。 | 受阻 | Research index `Load more` 历史页未取得，直接 HTML/文本入口也只显示首屏。News 不可替代 Research；本项不支撑零命中断言。恢复条件：可读的官方历史分页或本窗完整官方研究目录。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) HTML 的 `publishedOn` 序列，窗内 2026-03-31T22:17Z 的 [澳大利亚采用率分析](https://www.anthropic.com/research/how-australia-uses-claude)。 | 已检查 | 该项是采用/经济分析，不是本项目模型系统机制；无正面候选。 |
| `SRC-GOOGLE-AI` | [Google Research 2026-03 归档](https://research.google/blog/2026/03/)及 [DeepMind Publications](https://deepmind.google/research/publications/) 可见跨窗日期。 | 已检查 | 精选论文目录不能证明未列作者稿全部缺席；本窗 arXiv 主题扫描补其公开稿。 |
| `SRC-META-AI` | [Meta Research](https://ai.meta.com/research/) 抽取文本为空、直接页面请求超时；[Meta Blog](https://ai.meta.com/blog/) 可见 2026-04-08→03-26。 | 受阻 | Blog 无本窗条目，但 Research 无可读停点；本项不支撑零命中断言。恢复条件：可读的官方 Research 历史目录或当窗官方公告存档。 |
| `SRC-QWEN` | [新 Research](https://qwen.ai/research) 前端合并[旧研究配置](https://qwen.ai/api/page_config?code=research.research-list) 60 项和[新文章接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 40 项；新接口 `extra.date` 在邻域由 03-30T04:00+08 跳到 04-02T04:00+08，旧项均早于 2026。 | 已检查 | 官网此列表无本窗条目；作者单独 arXiv 稿由论文源查，不从该目录推断全部研究不存在。 |
| `SRC-DEEPSEEK` | [官方研究与动态](https://www.deepseek.com/news/)：研究 2026-06-24→02-25，动态 04-24→2025-12-01，均跨本窗。 | 已检查 | 结论只针对官网可见目录。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog) 当前最新 2025-11-07；[kimi-cli Releases](https://github.com/MoonshotAI/kimi-cli/releases) 1.28.0 为 03-30T15:15Z，1.29.0 为 04-01T14:06Z，夹住本窗。官方仓库 UTC 03-31～04-01 邻域提交检索有 17 条，集中于 CLI 探索、会话和兼容性局部修订。 | 已检查 | 邻域提交不能直接视为本窗发布事件；这些局部修订也不是独立研究家族，论文由 arXiv 路由。 |
| `SRC-TENCENT-HUNYUAN` | [官方 Research](https://hunyuan.tencent.com/research) 前端 `publicList` 公开接口以 `pageNum=1,pageSize=100,renderType=0` 返回 9/9；日期 04-23→02-13。 | 已检查 | “全部”目录本窗无条目；不代表全部作者论文无命中。 |
| `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research) 04-01 16:00 的 [GLM-5V-Turbo](https://www.zhipuai.cn/zh/research/156) 已过本窗 09:00，上一条 03-15。 | 已检查 | 04-01 16:00 线索归 04-02，不计本窗。 |
| `SRC-BYTEDANCE-SEED` | [官方论文目录](https://seed.bytedance.com/en/public_papers)分页总 242 项，页 40 的邻域 04-07→03-31 20:00 北京时间→03-25；窗内目录项 [TDDFT 分子计算](https://arxiv.org/abs/2603.29257v1) 属暂缓的 AI for Science。另查 [Blog 五类](https://seed.bytedance.com/en/research)：Foundation Jun23→Feb16、Visual Apr23→Feb13、Audio Apr9→2025Jul、[AI Infra](https://seed.bytedance.com/en/blog_list/ai-infra) 2025Aug→Mar、[Frontier](https://seed.bytedance.com/en/blog_list/frontier-research) Jul7→2025Dec，均跨窗。 | 已检查 | 官网页/博客范围已闭合；[官方仓库](https://github.com/ByteDance-Seed)窗内有 VeOmni CI、token-zero guard 等局部提交，不以提交日代替发布事件或把局部修复硬升候选。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 04-15→02-06；[Publication](https://ernie.baidu.com/blog/zh/publication/)现存条目无本窗新稿；[ERNIE Releases](https://github.com/PaddlePaddle/ERNIE/releases) 唯一可见正式发布为 2025-06-30 `ernie-4.5`，本窗指定仓库 commit 检索为 0。 | 已检查 | 仅限这些公开目录，不代表百度作者在别处无论文；论文源另查。 |
| `SRC-XIAOMI-MIMO` | [官网 Paper 栏](https://mimo.xiaomi.com/) 06-29→03-13；[官方仓库](https://github.com/XiaomiMiMo)当窗及相邻日 commit 检索无命中。 | 已检查 | Blog 栏不提供可靠单篇日期，不拿无日期条目作本窗新论文；该栏目日期仍是受限范围，作者论文由 arXiv 查。 |
| `SRC-MINIMAX` | [英文 Research Blog](https://www.minimax.io/blog) 05-26→03-18；注册的[中文博客](https://www.minimaxi.com/blog)跳转 minimax.cn，目录 04-27→03-18；[Agent 技术页](https://agent.minimax.io/docs/techblog) 索引只列 04-27 Agent Team；[CLI Releases](https://github.com/MiniMax-AI/cli/releases) 最早邻近 04-01T09:03Z，已晚于本窗 04-01T01:00Z 截点。 | 已检查 | 仓库窗内有 CLI/skills 小修，但缺改变长期系统机制的独立研究；不把 commit author date 当公开事件。 |
| `SRC-ARXIV` | 旧 [516 项 DOI-created owner inventory](../_sources/arxiv-owner-replay-20260903/20260401/arxiv-owner-receipt.json) 已标题筛选；拟入选与强信号/分层抽样排除项核 exact-v1 题摘。官方 [公告规则](https://info.arxiv.org/help/availability.html)、相邻 ID 的 OAI 日期与 DOI 批次交叉界定 03-31 20:00 ET / 04-01 08:00 北京时间公告。 | 已检查 | 旧 513 项按 v1 *Submitted* 建表无效；516 项未逐篇核精确公开分钟。独立抽查范围见 §6，不把 DOI created 冒充单篇公开时刻。 |

## 3. 候选与判断

下表是本次处理的 **20 项冻结候选**。所有 arXiv 行的 04-01 08:00～09:00 为官方常规公告、相邻 OAI/ID 与 DOI 批次共同支持的**有界归属推定**，不是单篇精确上线分秒；元数据及不确定性见[当日 checkpoint](../_sources/daily-20260401/V3_REVIEW_CHECKPOINT.md)。评分对应本次受限命题的 Design Delta + System Reach + Durability，不继承旧表 8/30 等分值。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [CRAFT `2603.28768v1`](https://arxiv.org/html/2603.28768v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 按层专家副本的边际收益必须与最小设备 KV 并发共同预算；3+3+2=8。 | 深入完成 | 整合：MODEL-MOE — [章节](../../../../books/part-02-model/21-moe.md)。
| [GPU Fail Quietly `2603.28781v1`](https://arxiv.org/html/2603.28781v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 观测通道消失与硬件数值异常分账；1+2+2=5。 | 标准完成 | 已有覆盖：PLATFORM-MONITORING — [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。
| [Time is Not Compute `2603.28823v1`](https://arxiv.org/html/2603.28823v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | wall-clock/unique-data 约束下 FLOPs 最优点不普适；1+2+2=5。 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md)。
| [OptiMer `2603.28858v1`](https://arxiv.org/html/2603.28858v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | CPT 数据混合从训练前搜索改为后验模型向量组合，仍有专家训练/holdout 成本；3+2+2=7。 | 深入完成 | 整合：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md)。
| [LLM Memory Pipeline `2603.29002v1`](https://arxiv.org/html/2603.29002v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 长上下文语义 memory 分段与异构放置须按阶段验收；3+2+2=7。 | 深入完成 | 整合：INFER-TENSORRT-LLM — [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。
| [GPU Kernel Agent `2603.29010v1`](https://arxiv.org/html/2603.29010v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | kernel 物理下界作为搜索预算/anti-gaming 诊断而非正确性证明；2+2+2=6。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。
| [Web Agent Benchmark `2603.29020v1`](https://arxiv.org/html/2603.29020v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 实例化/失败处理和标注口径决定 Web Agent 跨次比较是否有效；2+2+1=5。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [SLVMEval `2603.29186v1`](https://arxiv.org/pdf/2603.29186v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 长视频生成 evaluator 须按时长与可感知退化类型通过成对正反例准入；2+2+2=6。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [Concept Training `2603.29123v1`](https://arxiv.org/html/2603.29123v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | NTP 单标签→上下文等价 token-set 的受限目标分支；2+2+2=6。 | 深入完成 | 整合：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md)。
| [Long-Task Reliability `2603.29231v1`](https://arxiv.org/html/2603.29231v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 重复长任务须按任务域/时长测可靠性，不能用短任务 pass@1 替代；2+2+2=6。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [SysOM `2603.29235v1`](https://arxiv.org/html/2603.29235v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | rank→CPU/GPU/OS 差分与符号 provenance 形成诊断链；3+3+2=8。 | 深入完成 | 整合：PLATFORM-MONITORING — [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。
| [FlexMem `2603.29252v1`](https://arxiv.org/html/2603.29252v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 压缩视觉 KV 经可检索 memory bank 条件读回，不等于精确 KV 复用；2+2+2=6。 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION — [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。 |
| [BenchScope `2603.29357v1`](https://arxiv.org/html/2603.29357v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 评估 suite 的有效维度依赖模型群体/结果矩阵，非能力真值；2+2+2=6。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。
| [ELT-Bench-Verified `2603.29399v1`](https://arxiv.org/html/2603.29399v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | benchmark 误拒/歧义/错误 GT 修正同一 Agent 能力结论；2+2+2=6。 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。
| [Single-Vector Retrieval `2603.29519v1`](https://arxiv.org/html/2603.29519v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | domain shift、relevance proxy 与大库淹没比维度不足更具解释力；2+2+2=6。 | 深入完成 | 整合：AGENT-RAG — [章节](../../../../books/part-07-agent/76-rag.md)。
| [Video-Oasis `2603.29616v1`](https://arxiv.org/html/2603.29616v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 视频评价应测视觉/时序必要性，避免语言 shortcut；2+2+2=6。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。
| [Near-Miss `2603.29665v1`](https://arxiv.org/html/2603.29665v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | final outcome 正确不证明 action 前读过授权状态；2+2+2=6。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING — [章节](../../../../books/part-07-agent/78-tool-calling.md)。
| [VCC `2603.29678v1`](https://arxiv.org/html/2603.29678v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | lossless 原始轨迹与 task-filtered view 分离，派生 memory 可回指；2+2+2=6。 | 标准完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)。
| [DUME `2603.29765v1`](https://arxiv.org/html/2603.29765v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 兼容 dense experts 可后验拟合路由器组合；3+2+2=7。 | 深入完成 | 整合：MODEL-MOE — [章节](../../../../books/part-02-model/21-moe.md)。
| [ShapE-GRPO `2603.29871v1`](https://arxiv.org/html/2603.29871v1) | 2026-04-01T08:00:00+08:00 ～ 2026-04-01T09:00:00+08:00 | 单回答候选集合的效用须做候选级 marginal credit；2+2+2=6。 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)。

## 4. 证据与知识整合

### [CRAFT `2603.28768v1`](https://arxiv.org/html/2603.28768v1)

原文 §4.1–5.3 按层记录增加专家副本的边际平衡收益，以固定 expert memory 预算规划副本，并把同 DP rank 的最小 KV 容量计入并发上限；不是仅优化 expert load。作者在 A100/BF16、两种 MoE、输入≤4096/输出 256 的设置观察到受限 goodput 收益，未证明动态画像漂移时同样成立。Ch21 已把「按层收益→显存/KV→并发」接入原放置主线；均匀副本在稳定负载、显存宽裕时仍合理。

### [GPU Fail Quietly `2603.28781v1`](https://arxiv.org/html/2603.28781v1)

原文事故集有 69 个 GPU 类事件却仅 15 个 telemetry 完整，脱附子集只有 5 个可处理；joint GPU/monitoring/OS plane 能识别 scrape payload collapse，但弱代理标签与事故发现时间不等于前瞻性故障预测。Ch67 已把指标缺失与零值分开，仍要求 OS 日志交叉验证；本项未改变该判断，故已有覆盖。

### [Time is Not Compute `2603.28823v1`](https://arxiv.org/html/2603.28823v1)

作者以 8 个 4090 单卡配置、48M unique tokens 和有限 wall-clock 比较预训练选点；重复语料与实际时间令 FLOPs-optimal 不自动等于工程最优。Ch28 已明确 unique data/repetition、compute/time 和硬件执行条件分账。论文的受限拟合不能提供普遍的最优幂律，因此无新书稿结论。

### [OptiMer `2603.28858v1`](https://arxiv.org/html/2603.28858v1)

§3–5 先从同一 base 为各域单独 CPT，得到参数增量，再在 development set 搜索合成权重；选择时点从训练前数据比例移到训练后向量组合，但没有消除各域训练、模型存储或独立 holdout 费用。Gemma-3-27B/BF16/8×H200 的 15–35× 只比较搜索成本。Ch28 已将这条条件分支并入预训练预算论证。

### [LLM Memory Pipeline `2603.29002v1`](https://arxiv.org/html/2603.29002v1)

原文把长上下文处理区分为写入、索引/压缩、检索和消费四个阶段，分别评估注意力、RAG 与压缩 memory 在不同设备上的压力。Ch49 已写成异构 execution/placement 分支；它不改变 KV 的精确身份，也不把特定 FPGA/实验结果外推为通用吞吐。

### [GPU Kernel Agent `2603.29010v1`](https://arxiv.org/html/2603.29010v1)

§3–5 的 kernel 搜索用硬件物理下界限制无意义搜索，并以独立正确性检查阻止只按 benchmark 排序；下界是搜索预算诊断，不是程序正确性证明。Ch66 已把这层 anti-gaming 证据接入既有 evaluator 主线，性能结论不超出作者 kernel、硬件和测量范围。

### [Web Agent Benchmark `2603.29020v1`](https://arxiv.org/html/2603.29020v1)

原文 §3–5 逐题审 643 个 WebVoyager 任务，发现网站边界不强制、硬编码日期和实时地域差异、CAPTCHA/限流重试及不可能任务的排除规则不一致；修订为 535 题、运行时实例化相对日期、指定网站和人工 success rubric。两名审阅者的 95.9% 一致率只说明该标注协议在所测题上的一致性，不证明任务真值无误。Operator 的 68.6% 与另一协议所报 87% 不能作为同条件模型退化比较。Ch66 已要求冻结 task/harness/environment/evaluator revision 和跨次可比条件；此稿给 Web 场景的受限实例，未新增 owner。

### [SLVMEval `2603.29186v1`](https://arxiv.org/pdf/2603.29186v1)

PDF v1 §3–4 将长视频生成 evaluator 本身作为被评估对象：从带密集字幕的原始视频造 10 类质量/文图一致性退化配对，由五名标注者确认退化确实可感知后，才用正反例检验自动评分器是否把较好视频排在前面。§6 按退化类型、视频时长比较 VLM judge、CLIPScore 与 VideoScore；人工在 10 类的配对正确率为 84.7%–96.8%，受测自动系统在其中 9 类弱于人工，且多数系统随时长增加而退化。长期命题不是某个模型排名，而是把**任务长度与可辨识正反例**放进 evaluator admission：短视频指标和对视频理解模型的输入消融不能单独证明一个 judge 可评价长视频生成质量。代价是合成退化的 construct validity、人工过滤和时长切片成本；Appendix K 明确合成错误分布不代表未来真实生成失败，降质强度本身也是实验参数。Ch66 已有一般性的 known positive/negative controls，却未承载长视频生成的长度迁移和退化类型这条具体交接；主任务已将其紧接 Video-Oasis 的视频理解消融段整合，仍保留两类评价对象之别。

### [Concept Training `2603.29123v1`](https://arxiv.org/html/2603.29123v1)

§3 的 concept loss 对同义候选概率求和取负对数，再与 NTP 插值；集合由教师模型生成，限英语完整单 token 名/动/形容词。§4–5 的 1B/3B/8B 短继续训练改善所测词汇语义和 content-word PPL，同时 global PPL 略变差，未测试指令/系统任务。Ch28 已将「单标签目标→等价集合监督」作为有代价的实验性训练分支，不覆盖标准 NTP 的精确生成边界。

### [Long-Task Reliability `2603.29231v1`](https://arxiv.org/html/2603.29231v1)

原文 §3–5 将同一任务重复运行的 pass^k、按时长/领域切分的可靠性衰减、部分完成质量与工具调用分布异常分别量化。396 题按软件工程、网页研究、文档处理及四个人类预估时长分层；10 个经 OpenRouter 路由的模型、温度 0.7、每题 k=3、两种 scaffold，计划 23,760 episode，完成 23,392。剩余 episode、路由漂移和以人类时间代理 Agent 难度均限制跨场景推断；tool entropy 的 meltdown 阈值在小规模 pilot 的人工标注上校准，不是普适早停器，其恢复收益仍属未来工作。Ch66 已有 Pass@k/Pass^k、任务 horizon、重复运行与环境身份分账，本文不改变现有结论。

### [SysOM `2603.29235v1`](https://arxiv.org/html/2603.29235v1)

§3–5 用跨 rank CPU waterline 和 GPU/OS 差分找慢 rank，再用 eBPF 栈、Build-ID 与后置符号化追根因；观测/符号质量也是诊断可信度一部分。论文报告的 0.33% overhead 是 2×A100、指定 Llama/PyTorch/NCCL/采样条件，不是 80k GPU fleet 全域 SLO。Ch67 已纳入这条分层诊断链。

### [FlexMem `2603.29252v1`](https://arxiv.org/html/2603.29252v1)

§3–5 将长视频逐 clip visual KV 压为近期上下文 `C` 和可检索长期 bank `M`，查询时按需取回；这属于模型外层的派生视觉状态，不是原始 KV 的精确跨请求复用。“无限长度”是流式接口而非无损无限记忆；单 RTX 3090、两种 LLaVA 系模型、五类长视频和一类流视频任务没有生产并发/尾延迟证据。Ch23 已在原长视频表示主线中补足“逐片段写入压缩状态→按问题回读→保留原 clip/时间身份与失效回退”；短视频可直接编码时仍以直接输入为简单基线。

### [BenchScope `2603.29357v1`](https://arxiv.org/html/2603.29357v1)

§2–5 从 item×model 结果矩阵计算谱有效维度，并用相关性/leave-one-out 检查 benchmark 冗余；它依赖所选模型群体和二值/连续结果编码，不是“真实能力维度”。Ch66 已吸收这种 suite 容量诊断，并保留构念、版本和低样本的边界。

### [ELT-Bench-Verified `2603.29399v1`](https://arxiv.org/html/2603.29399v1)

§3–5 从失败任务的 660 个 mismatch 列区分 Agent 错误、评价误拒、歧义和错误 GT；同一 Agent/模型在修正评价后 pass 由 46/203 到 66/203。218/660 benchmark-attributable 不能误写为所有任务或 Agent 成功。Ch66 已要求先核 scorer/reference artifact 再发布能力结论，故此文是受限实例而非新判断。

### [Single-Vector Retrieval `2603.29519v1`](https://arxiv.org/html/2603.29519v1)

理论构造说明低维并非唯一瓶颈，实验以 LIMIT/MSMARCO 显示域迁移、余弦 proxy 与真实 relevance 的错位、大库噪声邻近均可使单向量检索失败；具体模型、微调条件不能外推所有语料。Ch76 已把这条成因链接入单/多向量成本—质量取舍。

### [Video-Oasis `2603.29616v1`](https://arxiv.org/html/2603.29616v1)

§3–5 用视觉/时间遮蔽、消融与机会水平对照检查视频 QA 是否真的需要所给模态；v1 的 54% 是其特定基准中可由 shortcut 解决的样本，非通用模型失效率。Ch66 已要求在发布多模态指标前测模态必要性，保留原完整输入 benchmark 作为另一证据轴。

### [Near-Miss `2603.29665v1`](https://arxiv.org/html/2603.29665v1)

§3–4 检查 mutating tool call 前是否实际读取 policy 要求的只读状态，即使最终数据库状态正确也可能漏掉前置证据；50 个改造后的航空任务和模型轨迹的 8–17% 是特定 mutating 子集，非生产事故率。Ch78 已规定 effect 前提读集与提交复核，Ch66 分账 trace 与终态，故已有覆盖。

### [VCC `2603.29678v1`](https://arxiv.org/html/2603.29678v1)

§2–3 将原始 JSONL 编译为可回指 full view、用户可见 UI view 和任务过滤 adaptive view，避免摘要把关键证据抹掉；AppWorld 的 token/成功率比较也受不同格式基线和 memory 合并步骤影响。Ch77 已拥有 lossless 原轨迹 locator、derived memory 与任务证据支持集，故不额外写同一机制。

### [DUME `2603.29765v1`](https://arxiv.org/html/2603.29765v1)

§2–3 的闭式 ridge router 把共享 seed/架构/tokenizer 的独立 dense experts 后验接成 MoE；“training-free”仅指组合时无需反传，不包括先前专家训练与特征前向。小模型/3B 领域和推理任务支持受限可行性，不证明异构专家无损组合或生产路由均衡。Ch21 已把该条件分支接入 MoE 演化主线。

### [ShapE-GRPO `2603.29871v1`](https://arxiv.org/html/2603.29871v1)

§3–4 针对**单条回答内**多候选的 set-level max utility，以 Shapley marginal contribution 分配候选级 credit；只有 max 结构才有作者的 `O(K²)` exact 计算，等长候选是无额外重加权 bias 的假设。Qwen3-8B/2×GH200 的摘要、代码建议与 Netflix 模拟推荐结果未证明真实点击奖励或任意集合函数。Ch33 已把它作为与普通 GRPO 组内完整回答不同的条件分支。

本窗值得长期保留的主线是：模型训练端，语义等价标签与后验 CPT 向量组合改变 objective/mixture 的选择时点，但同时增加教师标签、各域训练和 holdout 费用；模型部署端，MoE 副本不是独立的负载均衡开关，因为按层收益会挤占最小 rank 的 KV 并发；推理执行端，语义 memory 与 sparse/KV 路径须分别计模型状态、外层状态和异构设备 placement；平台证据端，kernel 搜索物理上界、benchmark 有效维度、视频模态必要性以及跨 rank 因果诊断都只能作为明确条件下的判断，不能用漂亮总分代替 evaluator 和 provenance。

以上命题的原始 exact-v1 方法、对照、硬件/输入长度/精度/并发/SLO 披露与未证明范围逐项记录在[本日 V3 来源审阅](../_sources/daily-20260401/V3_REVIEW_CHECKPOINT.md)。特别注意：CRAFT 的 goodput 仅适用于作者两种 MoE、A100/特定长度和并行拓扑；Video-Oasis 的 v1 摘要是 54%，不可用后版 55%；ShapE-GRPO 的多项式计算只针对 max-set utility；概念训练的改善仅是英语词汇语义和 content-word PPL，global PPL 反而小幅退化。机构公告、DOI 日期与作者实验的证据权限互不替代。没有任何作者 benchmark 被写成无条件生产收益。

Books 对照的旧论点、新增命题及实际段落由主任务分别落实于 Ch21、Ch23、Ch28、Ch33、Ch49、Ch66、Ch67、Ch76。其余候选不是遗漏：`No Change` 已核对应具体章节（见工作表）。

## 5. 缺口与下一步

1. `SRC-OPENAI` Research 历史分页与 `SRC-META-AI` Research 经本轮有界尝试仍缺官方可读停点，已作为来源保留项隔离；不以 News/Blog 替代，也不据此作零命中断言。可用官方历史目录恢复时，只重开受影响来源和材料。Qwen 官方研究列表及其他机构已检查的入口见上表，不重复扫全年。
2. [Measuring the metacognition of AI `2603.29693v1`](https://arxiv.org/pdf/2603.29693v1) 有明确的待核方法贡献：比较 confidence discrimination 时应与主任务能力分账。但官方 [arXiv 历史](https://arxiv.org/abs/2603.29693) 记 v1 于 2026-03-31 提交、v2 于 04-16、v3 于 07-08；v1 PDF 参考文献 [12] 却写 `Accessed: 9 Septembre 2026`，晚于这三个版本。这可能只是作者年份笔误，不能据一处错误推断正文不实；本轮仍将其作为版本/出处 `Disputed` 隔离，不评分、不写 Books、不支撑本窗正面命题。可接受的重开材料是作者勘误或可核的版本来源解释，届时只重审该家族。
3. 独立语义复核和 Books 段落对账已完成，范围与剩余证据边界见 §6。外部目录或作者解释恢复时，仅重开对应来源或家族；不重跑已验证的其他候选。

终态保留项：目前没有需要用户提供的 exact-v1 PDF。OpenAI/Meta 的来源目录已达到本轮可执行入口的停止点，分别等官方可读历史目录；`2603.29693` 等可核作者勘误或版本解释。三项均不用于正面证据、Books 或无遗漏断言，也不以无界重试拖住其他候选。定点重开条件分别为官方可读的 OpenAI/Meta 当窗研究目录，或该论文可核的作者勘误/版本解释。

## 6. 复核

复核者：主任务（非本日报作者）。
结论：通过
范围与结果：独立逐项对读 20 项候选的 §3/§4 贡献、证据边界与 Books 决定；核对 13 项实际整合的 source-family 标记与目标章节，并检查其余已有覆盖项指向具体旧论点。排除侧按旧 516 条身份顺序作 10 个等距分层题摘样本（`2603.28770`、`2603.28919`、`2603.29050`、`2603.29152`、`2603.29261`、`2603.29391`、`2603.29520`、`2603.29664`、`2603.29801`、`2603.29928`），并复查强信号误排；样本中未发现须新增的长期 AI System 命题，但它不能证明未抽到的每篇都正确关闭。反向检查实际找回 SLVMEval 并整合 Ch66；`2603.29693v1` 因版本出处争议隔离。OpenAI/Meta Research 缺可读历史停点，均不用于零命中或无遗漏断言。20 项按当窗公告批次有界归属，不冒充单篇精确分钟。结构校验和 `git diff --check` 通过，但两者只证明格式，不替代以上语义判断。
