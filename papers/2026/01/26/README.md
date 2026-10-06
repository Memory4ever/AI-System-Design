# Daily Research — 2026-01-26

**规范：** V3
**窗口：** 2026-01-25T09:00:00+08:00 ～ 2026-01-26T09:00:00+08:00
**补充窗口：** 2026-01-25 ～ 2026-01-25
**窗口说明：** 用户授权已有 Daily 来源遗漏补查；原窗口、候选日期与有效审阅保留，新增仅按 Jan25 北京时间自然日，不继承原09:00筛选边界。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T07:16:11+08:00

## 1. 结论

原轮有限原源重建后，确定当窗候选为 **0 个家族**，不是“零发布”或“全来源无遗漏”。6 个相关家族读完完整题摘或官方核心：MCTS-Reasoning、Context Length Crunch、Kimi CLI 0.87 和 Indeed 访谈贡献关闭；Qwen3-Max-Thinking 与 Infinigram 存在值得核验的机制，但必要日期/精确版本或机制解释不能成立为当窗采用依据，分别隔离，不列确定候选、不评分。

Qwen 的多轮经验累积把并行预算转向反思与历史摘要，有潜在长期价值；官网列表与正文的日期冲突，不能任选窗内字段。Infinigram 的共享 byte 索引接口也不能仅因使用成熟算法而排除；当前 byte-prefix 概率却不足以证明任意 tokenizer 的精确 token 分布，且报告页头与作者站更早发布日期不一致。

原轮 Books 判断为 **No Change**，实际写入 0；没有声称两个隔离机制已被具体 Existing 覆盖。原轮 root 非作者日级复核有效保留。[原查询、停止与具体排除理由](../_sources/daily-20260126/SCREENING.md)及[本轮前快照](../_sources/daily-20260126/supplement-original-20261008.md)保留原始依据。

本轮补充仅处理 Jan25 自然日。新增10个相关家族：8份完整题摘、1份官方核心与1份不完整原源；新增确定候选 **1个家族 SOAR**，已深入核验 grounded curriculum 机制并在 TRAIN-DATA 整合两段，root非写入者actual POST通过，root独立日级DAY通过，普通待办0。LLM42、TensorLens 与 Structure 的具体增量成立但必要公开日期未恢复，终态隔离；MaskedDepth、LiMo 与 EfficientAgents 贡献关闭，StepDeepResearch 与 LanguageVAE 为更早已公开事件，MDPI96 的完整题摘/日期原件受阻隔离。原6家族不重排；库存、submission buffer和三方收录不变为候选分母。[本轮实际入口、分页与停止](../_sources/daily-20260126/supplement-native-stops-20261008.md)可复查，本轮root独立日级验收通过；外部保留项不授正面Coverage/Evidence或无遗漏。

## 2. 来源覆盖

只扫描每日来源及下列实际触发的表外原源，不扫描每周组。当前网页目录反映执行时状态；年度存量与混合搜索命中没有被当作本日新论文分母。

表中原窗口记录保留；本轮14入口逐项重新检查或复用同身份有效原件，具体 fresh 返回和停止见[补充停止记录](../_sources/daily-20260126/supplement-native-stops-20261008.md)。重要变化：Seed 原生 ascending 2026 API type1 第一页 Jan20→Jan22→Jan27，type2 首项 Feb12，均跨补充日后停止，不翻 next20 或审242库存；ZAI fresh15条、Baidu首10条与MiniMax English12条有日期邻接，未见Jan25；其余历史缺段不因失败称零发布。arXiv BJT Jan25 无普通公告批次，但此规则不证明具体家族公开日；只用四条本窗主题发现与指定潜力项有限日期恢复。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原 Research 页后读[官方 RSS 日期邻接](../_sources/daily-20260126/jan26_openai_rss.txt)：1245 项 feed 最早 Dec2015，只抽 Jan20～29；Indeed Jan26 00:00 GMT 落窗，读完整官方访谈后贡献关闭；Jan23 Codex loop 窗外 | 已检查 | 本次 feed/可读原文无未处理条目；不声称全部官方原始出版渠道无遗漏 |
| SRC-ANTHROPIC | Research 原页 Publications 最新 10 条仅 Sep～Oct2026；窗口日期/主题补查没有恢复 Jan25～26 原始历史片段；[原返回](../_sources/daily-20260126/jan26_native1.txt)、[有限补查](../_sources/daily-20260126/jan26_search1.txt) | 受阻 | 缺可核的当窗目录；搜索返回现代内容不能证明无命中 |
| SRC-GOOGLE-AI | DeepMind 原 Research + [RSS 100 项](../_sources/daily-20260126/jan26_deepmind_rss.txt)覆盖到 Nov2025，Jan16 D4RT 与 Jan29 Genie 邻接未含窗内条目；Google Research pubs 2026 年列表只作定位，不将 385 年度存量送题摘队列 | 受阻 | DeepMind feed 切片已检查；Google Research 缺日级发布日期/历史切片，不授整个来源覆盖保证 |
| SRC-META-AI | Research 空返回、publication fallback 失败后，检索恢复[官方 publication page=3](../_sources/daily-20260126/jan26_meta_archive.txt)：Feb27→Feb10→Jan2 后混入更早年份；停止该页，不扩历年队列 | 受阻 | 已见邻接列表没有 Jan25～26，但混合排序不足确定完整窗口 |
| SRC-QWEN | 旧 github.io 目录到 Sep2025、动态 blog shell 不能作历史证明；具体原 blog 完整核心 + [同 ID 官方 article API](../_sources/daily-20260126/jan26_qwen_identity_dates.txt)已核 | 受阻 | extra.date Jan26 04:00+08 与 content datePublished Jan23 04:00+08 冲突，blog Jan25 无 TZ，首公开/版本未明 |
| SRC-DEEPSEEK | 官网当前模型卡片、官方 API news / docs 恢复失败与窗口有限日期查询；停止可用入口；[原页与尝试](../_sources/daily-20260126/jan26_native2.txt)、[补查](../_sources/daily-20260126/jan26_recovery1.txt) | 受阻 | 缺 Jan25～26 原始历史目录；无搜索结果非零发布 |
| SRC-MOONSHOT | Platform Blog 26 条最新 Nov7,2025；官方 org 与具体 CLI release 恢复。0.87 [原 published_at](../_sources/daily-20260126/jan26_kimi_release_fields.txt) Jan25 09:48:17Z 落窗，读 release 与 PR701/702 实际代码；0.88 窗外 | 受阻 | CLI 窗内事件已贡献关闭；模型/研究历史 blog 切片仍不完整，不因 CLI 代替全部模型来源 |
| SRC-TENCENT-HUNYUAN | 首查 Research 空返回，实际浏览器开页/重取 tab 后导航与 accessibility 再失败；原官方 GitHub 组织入口没有恢复该日期研究切片；[原返回](../_sources/daily-20260126/jan26_native3.txt)，尝试停止见 SCREENING | 受阻 | 缺“全部”历史目录/可读取日期条目；不是未存在或零命中 |
| SRC-ZAI | 原 Research 13 个带日期条目，窗口邻接 Feb2 GLM-OCR / Jan19 GLM-4.7-Flash / Jan13 GLM-Image；[全返回](../_sources/daily-20260126/jan26_native3.txt)到 Dec2025，原 release-notes 辅助入口已查。本轮 text超时后直接GET恢复15个原生日期条目，同邻接跨过Jan25后停 | 已检查 | 两轮可读研究列表均未见对应窗口条目；不扩旧库存或授全站无遗漏 |
| SRC-BYTEDANCE-SEED | 原 Research Jan27 Post-LayerNorm / Dec2 GR-RL 窗外；public_papers第1页20/242、13页只定位。补充本轮[官方API实值](../_sources/daily-20260126/supplement-native-final-20261008.txt)：ascending2026/page_token0/count30，papers type1 returned20/total82、next20、has_more true，Jan20→Jan22→Jan27；blog type2 returned9/total23、next20、has_more true，首项Feb12。两者跨补充日后均停止，不读next | 受阻 | 原宽目录历史受阻记录保留；本轮指定native API日段未见Jan25，其他公开渠道/完整source未授覆盖，库存不成为候选队列 |
| SRC-BAIDU-ERNIE | Blog 第1页日期从 May2026 到 Nov2025，Jan29 PaddleOCR1.5 / Jan15 / Jan8 与 Dec2025 跨过目标日期；分页2页，第1页已经越过本窗下界，[原列表](../_sources/daily-20260126/jan26_native3.txt) | 已检查 | 该博客日期列表没有本窗条目；不授另行未发布正文保证 |
| SRC-XIAOMI-MIMO | Paper 8 项带日期：Feb3 HySparse / Jan8 MiMo-V2-Flash 为邻接，读原首页；Blog 15 标题无日期 + More，原 org 未恢复历史切片；[原列表](../_sources/daily-20260126/jan26_native4.txt) | 受阻 | Paper 日期切片已检查，Blog 的历史时间/更多列表受限 |
| SRC-MINIMAX | English Blog 12 个日期卡片 Jan27 M2-her / Dec23 M2.1 跨过窗；中文 blog 重定向空 shell，Agent Tech Blog 只有 shell；[原入口返回](../_sources/daily-20260126/jan26_native4.txt) | 受阻 | English 列表已检查；中文/Agent 历史条目不可恢复，不合并为零事件 |
| SRC-ARXIV | [官方 availability](https://info.arxiv.org/help/availability.html)的 Sunday–Thursday 20:00 ET 公告规则；Jan25 Sunday 公告换算为 Jan26 09:00 BJT，恰在排除端点；[原规则](../_sources/daily-20260126/jan26_native2.txt)，按四条模型/多模态/GPU/world-model 主题补查作者早公开线索 | 已检查 | 本窗没有常规公告批次；Submitted 不作公开日期，非标准作者早公开只做有限查漏，不承诺全分类/全网召回 |
| 表外：[Alex Towell 作者站](https://metafunctor.com/) | 仅 Infinigram 与 MCTS 原完整题摘/必要方法，以及这两个家族 archive 日期邻接；没有全站历史研究扫描 | 受阻 | MCTS 贡献关闭；Infinigram 首公开/精确 Jan25 版本及 token law 必要解释隔离 |
| 表外：[Context Length Crunch 作者上传稿](https://www.researchgate.net/publication/400058348_The_Context_Length_Crunch_Bottlenecks_in_Multimodal_Deep_Research_Agents) | 完整题摘 + §4；原上传稿讨论建议性多模态 token 缓解组合 | 已检查 | 贡献关闭；未核精确时刻，不为不影响处置的日期扩查 |
| 补检：[有限主题/日期查询](https://www.google.com/) | 四条当日模型/多模态/GPU/world-model 查询，机构限定日期补查与两个家族必要身份恢复；[原命中](../_sources/daily-20260126/jan26_topics.txt)、实际查询/停止见 SCREENING | 已检查 | 搜索仅发现和恢复身份，不证明首公开或全覆盖；窗口外线索不扩本日 |
| 表外：[SOAR 作者页](https://ssundaram21.github.io/soar/) | 原生 January25,2026 事件、完整核心；仅定点核 arXiv2601.18778v1 必要机制和关键评价，root必要源/PRE已通过 | 已检查 | v1 HTML body August24 与 PDF首页 January27不同，HTML Jan25版本权限隔离；不得投射当前blog/后版数字，后来PDF只核必要机制 |
| 表外：[MDPI Algorithms19(2)96](https://www.mdpi.com/1999-4893/19/2/96) | 具名身份、局部原文；HTML429、GET403、XML失败和PDF403后有限恢复停止 | 受阻 | 缺完整题摘、官方公开日及必要核心，终态隔离，不因访问失败贡献关闭 |

## 3. 候选与判断

原窗口确定候选 **0 个家族**，原评分与处置不变。Qwen 与 Infinigram 必要条件尚未成立，只在 §5 保留，不将相交日期先列入确定候选；另外4个贡献关闭项保留在原始资料中。本轮新增确定候选 **1个家族**，作者Jan25 blog为本次公开事件；其他9个新相关家族均已具名结束有限筛选或必要恢复，不靠主题映射、访问状态或实验大小改变门槛。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability（SOAR）](https://ssundaram21.github.io/soar/) | 2026-01-25 | 难题稀疏奖励使固定pool selection难以解锁学习→teacher以inner student在真实难题训练奖励集上的实际进步生成课程→需重新考虑generator目标而非仅调learnability；2+2+3=7 | 深入完成 | 整合：`TRAIN-DATA` [Ch27在线数据控制环](../../../../books/part-04-training-system/27-data.md#post-training-data-selection-是当前-policy-的在线控制环)两段；root actual POST通过 |

## 4. 证据与知识整合

以下两段为原轮有效判断逐字保留；其“本次”指原轮，新增采用另见下方补充。

没有确定当窗候选的证据采用，Books **No Change**，不是本次不做 Books。已加载 Books 背景、学习/写作指南，并定点对照 `MODEL-SAMPLING` 的单/多轨迹预算与 coverage/selection（[Ch20](../../../../books/part-02-model/20-sampling.md)及邻接）、`AGENT-CONTEXT` 的工作集/压缩损失（[Ch75](../../../../books/part-07-agent/75-context.md)及邻接）、`AGENT-REFLECTION` 的反馈来源与停止条件（[Ch80](../../../../books/part-07-agent/80-reflection.md)及邻接）。

现有章节承载基本约束，不足以自动关闭所有新验证/接口。Qwen 的机制可能改变历史表示与预算分配；Infinigram 的 tokenizer-independent 查询可能有长期差额。两者因必要日期/精确版本和直接反证隔离，本日不采用其机制/数字、不称 Existing，不创建结构候选或配方笔记。其余关闭项没有原始贡献达到改变长期知识的门槛。无需共享 Books 写锁，未修改书稿、ROADMAP 或 Learning State。

### [Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability（SOAR）](https://ssundaram21.github.io/soar/)

稀疏难题的直接 RL 缺少成功轨迹时，仅按当前可解率选择题目不一定产生通向真实难题的课程。[SOAR 作者页](https://ssundaram21.github.io/soar/)原生 January25,2026 事件提出：teacher 生成 question/answer，inner student 在这批合成题上短程更新，teacher 的奖励来自 student 在 hard reward set 相对 baseline 的实际正确率进步，而不是生成题的约50%可解率。潜在差额是把 generator 的训练目标接到真实学习进展，不只是对既有 sample pool 做难度排序。

HTML-first 打开[精确v1 HTML](https://arxiv.org/html/2601.18778v1)后，正文 printed August24,2026 与页头 v1Jan26 有实际版本一致性信号，故不授该 HTML Jan25 原件权限。必要回退的[精确v1 PDF](https://arxiv.org/pdf/2601.18778v1)首页 printed January27,2026；§3.2 的 `R(X)=Acc(after,Q_R)-Acc(baseline,Q_R)`、§3.3 的 inner reset/promotion 与作者 blog 的核心机制一致。本轮只核该必要命题，不追完整版本史；PDF 的后来正文日期不改写作者 Jan25 事件，也不把 current blog/HTML 的数值投射回Jan25。[必要PDF摘录](../_sources/daily-20260126/supplement-soar-v1-pdf-20261008.txt)留原件位置。

关键评价只作精确PDF的证据约束：Llama3.2-3B-Instruct、MATH/HARP 的 fail@128 split、未见难题作测试，Table4 的 MATH pass@32 PQ18.9±5.3 对 HardOnly9.6±2.6、g12812.4±7.4和 Intrinsic14.1±7.5；Table5 的 HARP PQ12.3±2.0 对 HardOnly8.2±1.0。表注/B.8明确重复student seeds的均值与SD，而非当前博客数字。不同课程日程、教师训练和inner repeats均付费；B.9单次metaRL为4×8 H200/H100约48–60小时，扩大hard-only group并不构成端到端等预算优势证明。单3B数学试验不授任意模型/领域普遍结论，错误伪答案、题目结构与多样性共变也不证明错误答案本身有益。B.8/Table3 的teacher/student训练batch为2/8、max generated tokens为512/1024、temperature为1；这是训练配置，不宣称最终evaluation全部采用相同batch。Evaluation报告pass@k及student seed均值/SD，HardOnly与PQ至少6个student seeds；输入长度、precision、concurrency与SLO为Not Disclosed，不据此给serving保证。本轮未核artifact或复现。

已加载 Books 背景并实际读 `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)的 synthetic trajectory reweighting 与 online checkpoint-coupled selector、Ch26/28相关交接。现有正文拥有固定池的权重/选择，未直接承载 grounded teacher 生成课程的差额。root独立实际读作者Jan25核心、精确PDF必要方法/Table4/B.8/B.9与actual owner PRE后授权窄锁；本轮已在Ch27的2605-05227分支后、optimizer-aware OPUS前整合两段及自身末注（当前1109/1111、1606）。明确`Q_R`来自`D_train`而非heldout/test，teacher奖励是学生相对baseline的实际进步，inner reset与阈值promotion分别拥有阶段状态，最终独立heldout才验收。作者写后完整邻接顺读、限定diff检查通过；root actual POST通过，不据source/PRE自授日级验收。旧正文及其他并发修改未重排，不改ROADMAP或Learning State。

## 5. 缺口与下一步

原轮普通可执行待办0及 root 非作者日级复核保留；本轮普通可执行待办0，root独立最终日级复核通过，不以旧完成标签替代本轮验收。下列原外部限制及新增限制均为对应窗口终态保留项，不用于正面证据，不支持正面 Coverage / Evidence、Books 或无遗漏断言：

1. [Qwen3-Max-Thinking](https://qwen.ai/blog?id=qwen3-max-thinking)：同 ID 官方正文已核，列表 `extra.date=2026-01-26T04:00:00+08:00` 落窗，但正文 `datePublished/dateModified=2026-01-23T04:00:00+08:00` 窗外；blog `2026/01/25` 无时区。不能用模型名日期、转载日或任选字段确认首公开。已读实际 TTS 增量，不评分、不采用数字、不进 Books；重开只需官方首公开公告、可信公开存档或明确修订/版本说明，先判断事件是否完全落窗，再核 take-experience/预算对照所需机制与条件。跨日仅复用必要日期 reconciliation，实际同 ID / 正文重新核验，未继承旧候选。
2. [Infinigram](https://metafunctor.com/latex/infinigram/)：PDF printed Jan25 无时区；原 landing published_time Dec3,2025 UTC 与 March16,2026 modified，archive 有 Dec3 论文/博客，无法证明 Jan25 是首次公开或重要修订。Eq5 的 byte-prefix chain product 不足以证明 arbitrary-tokenizer 精确分布；可变长 tokens 的 boundary/互斥与归一化未解释，top-k 截取也非完整 token law。性能表是 Target、示例 artifact 占位。重开只需该家族可辨识 Jan25 版本/公开证据，以及作者对 tokenization boundary law、归一化与覆盖范围的必要澄清或实际可核 artifact；不为此遍历新证明/全年版本。
3. 历史目录缺段：Anthropic Publications、Google Research 日级论文切片、Meta mixed page=3 完整性、DeepSeek history、Moonshot 模型/blog、Hunyuan“全部”目录、Seed Jan2026分页、MiMo Blog、MiniMax 中文/Agent Blog。已原入口、有限恢复与必要浏览器尝试而未得所需字段。重开须可读原目录/RSS/官方日期条目或可信窗口存档，只核 Jan25 09～Jan26 09；失败/未命中不写零论文，不把旧宽列表变为题摘/全文队列。
4. arXiv 作者非标准早公开召回：常规公告窗口规则已核，但有限补检不证明不存在作者稿。新线索须给具体标题/家族和原作者公开时间；只恢复受影响项，不重扫所有分类或月份。

本轮新增终态保留项：

- [LLM42 /2601.17768v1](https://arxiv.org/abs/2601.17768v1)、[TensorLens /2601.17958v1](https://arxiv.org/abs/2601.17958v1)、[Structure /2601.17869v1](https://arxiv.org/abs/2601.17869v1)：完整题摘经 root 准入校准具有具体机制/负面证据潜力，但 submission 是发现buffer，有限官方公告/作者页恢复未得Jan25 public依据，repo registration也不证明正文公开。不确定候选、不评分、不为日期未解深审；重开只需该具名家族官方原公告或可核作者Jan25正文事件，不追时分秒、不扩月库存。
- [MDPI96](https://www.mdpi.com/1999-4893/19/2/96)：题目身份和局部正文可核，完整摘要、原生公开日与必要方法/评价不可得；有限恢复已停止，不把三方Jan25推荐作public，不以403关闭贡献。重开只需具名原摘要和官方公开事件/必要核心。
- 本轮历史目录缺口仍为 Anthropic、Google pubs、Meta mixed list、DeepSeek、Moonshot模型/blog、Hunyuan“全部”、MiMo blog、MiniMax中文/Agent。Seed仅本次指定原生API日段恢复，原窗口行的旧分页受阻记录不擦除；不授其他channel全覆盖。补充恢复仅核Jan25自然日，不继承上面原轮09:00边界。

MaskedDepth、LiMo、EfficientAgents 的具体贡献关闭及 StepDeepResearch/LanguageVAE 更早事件身份见[完整题摘与校准记录](../_sources/daily-20260126/supplement-native-stops-20261008.md#完整题摘与贡献校准)；没有把它们因日期未核或小实验一概排除。相关关闭项未见实际撤回/勘误信号，不为无关日期继续扩查。

窗外恢复线索，不属本窗也不阻塞完成：Kimi CLI 0.88 官方 `published_at=2026-01-26T13:10:05Z`（Jan26 21:10:05 BJT）属于 Jan27 默认窗口，留待该日独立检查。hgpu Jan25 收录 SynPerf 链接 arXiv:2601.14910，v1 Submitted Jan21 11:47:56 UTC 不是公开；常规公告按规则推定 Jan22 09:00 BJT，当前 v2 名称 PipeWeave/Apr28 不能当原稿。未发现本窗事件，留待真实归属日必要身份/版本核验，未冒称已审重复项。

## 6. 复核

复核者：root（原轮独立于作者 jan26_independent；本轮独立于作者 supp_jan26）
结论：通过

已完成首批有限准入校准：root 实际原源核 MCTS 完整题摘/scope、ContextCrunch 完整题摘/§4、Kimi 0.87 release / PR702，三项具体关闭通过；Infinigram 初始笼统“成熟组合”理由被纠正，实际共享接口潜在差额、日期归属和 Eq5 直接反证现已隔离并保留重开条件。Qwen 日期定点核验采用相同官方 ID 原字段，不拿别日结论替代本日处置。

root 完成本日六部分顺读：实际核 Indeed 完整访谈核心/末段与原 RSS Jan26 00:00 GMT，应用 case 不具可归因设计增量，关闭通过；实际核 Qwen same ID/date 字段与 Infinigram published/modified 原字段，必要日期及机制条件继续隔离。全部 6 个本日相关家族均由非作者检查，首批未变化的具体关闭与必要反侧有效复用。14 个每日来源的有限范围/停止、外部缺口、arXiv 端点排除、窗外 0.88 不扩窗、0 确定候选 / Books No Change 均一致。范围外搜索标题仅定点分层抽检，未将其称为全网或全部搜索条目验证。无改书，因此无写后整合 claim。

机器校验：完成态 V3 格式/一致性通过，21 个本地引用实际存在；限定 Git diff 检查与两份新建 Markdown 的逐文件空白检查通过。静态结果不替代上述 root 独立语义验收。未 stage、commit、push，未删除证据或修改共享 Books / 索引。

本轮首批 root 实际完整题摘/作者核心校准已纠正 MaskedDepth、LiMo 的初始潜力判断并具体关闭，LLM42、TensorLens和受限Structure反证潜力保留但日期终态隔离；SOAR的 Jan25 原生作者事件不因 Jan26 submission/后加ICML badge排除。root发现精确HTML正文August24异常后，作者仅回退精确v1PDF首页/核心奖励/关键评价，保留两种原件及采用权限差异。root实际必要源与Ch27 actual PRE通过；作者已完成两段/自身末注窄写及完整邻接顺读，root actual POST已通过并释放窄锁，root完整六部分及native-stops日级DAY顺读通过；另外实际打开PDF Table5核HARP对照，要求补齐性能合同条件后完成，不继承上述旧通过或自授独立验收。

本轮实际机器检查：完成态V3格式/一致性通过；28个本地引用（21唯一）实际存在；原窗口与原§4连续两段逐字包含于补充报告，原0候选及有效审阅未迁移。限定README/_sources/授权Ch27的unstaged diff-check通过，限定cached为空；19份新source文件保留发现/必要原件，不称全部已作证据采用。静态检查不替代root日级DAY。未stage、commit、push，未改共享State/索引或别日。
