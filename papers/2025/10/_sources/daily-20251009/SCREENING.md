# 2025-10-09 有限初筛

只处理本日窗口。API查询原值/范围/停止见fetch_manifest；四组start0/max30是查漏线索，不是263+11+65+190篇全文任务。相关官方标题补检cs.CL/2510 start0/show100返回失败；announced_date_first高级搜索（date-from 2025-10-08、to 2025-10-09、title language model、size50）web Cache miss。不能据这些失败宣称没有论文。

原API完整题摘读8家族（跨topic重复只计一次），身份以下列ID定位，但返回混最新版本，不作v1证据；本轮本日Seed恢复另读Function Tokens，合计9个潜力家族，不是确定落窗分母：

| 家族 | 原文具体潜力 | 当前处置/恢复位置 |
| --- | --- | --- |
| [Patterns behind Chaos 2510.05497](https://arxiv.org/abs/2510.05497) | 24k请求/四MoE模型的数据移动画像，prefill-aware expert placement可能改变路由/放置设计；架构模拟与现GPU分开 | 日期保留；原响应v5，不采其数字或当初版；恢复官方首次公告+v1 |
| [EARL 2510.05943](https://arxiv.org/abs/2510.05943) | 长上下文agentic RL不同stage的parallelism selector和layout-aware decentralized dispatcher，可能改变静态并行/中间batch布局 | 日期保留；只有submitted字段；定点官方公告检索未恢复public time |
| [lm-Meter 2510.06126](https://arxiv.org/abs/2510.06126) | on-device在线phase+kernel profiling可能区分优化瓶颈，不把单一吞吐宣传当增量 | 日期保留；提交不作公开，未读全论文/复现 |
| [CAM 2510.05520](https://arxiv.org/abs/2510.05520) | incremental overlapping clustering同时支持分层摘要与在线batch整合，可能改变固定摘要层次的更新策略 | 日期保留；不是因心理学命名/已有记忆主题排除 |
| [RLHF/DPO-COV 2510.05526](https://arxiv.org/abs/2510.05526) | 同时处理corrupted preference、overoptimization、verbosity的长度正则泛化界；需核假设而不是只看指标 | 日期保留；v2摘要不冒充v1，理论局部不自动排除 |
| [Critical attention scaling 2510.05554](https://arxiv.org/abs/2510.05554) | tractable model中β~log n临界scale，过小rank-collapse、过大identity，可能补长上下文scale边界 | 日期保留；简化模型并非普遍生产结论，v2不当v1 |
| [DS-CP 2510.05566](https://arxiv.org/abs/2510.05566) | prompt proximity重加权calibration以应对domain shift，需核覆盖validity条件；局部MMLU结果不自动排除 | 日期保留；v2不当v1，不把无时刻当无贡献 |
 | [InfoRMIA 2510.05582](https://arxiv.org/abs/2510.05582) | token-level membership定位泄漏，挑战sequence-level gold standard；安全测量增量需必要反侧 | 日期保留；v2与public time未恢复，不授安全保证 |

初筛不是Evidence Gate，未因日期保留而给0分。未读过所有API命中摘要，范围外标题不虚记逐项关闭。

## 本日普通恢复及新增日期线索

实际请求/时间见[recovery_manifest](recovery_manifest.json)。DeepSeek本日[news原件](deepseek_news.raw)独立研究索引10可见条目日期/标题读到05-14→10-21，停止可见段，不能以主页导航hold替代。Z.ai本日[ownbundle](zai_page_bundle.js)LoadMore明确page参数，实际[page2](zai_page2.raw)累计18条、末12-07、“没有更多”；恢复完成但10月目录历史缺段仍隔离。Google pubs修正category=2025/search=language model后1–15/37，首15标题浏览仍无first-public日级时间，不将年度库存变逐项队列。

Seed本日[ownbundle](seed_bundle.js)函数ce对article_type1实际指定x-tt-locale:US；真实2025/asc/count20/token0/20/40/60/80，末页has_more=false/next空，总量字段94，实际返回19/15/19/19/13=85条，未声称94题摘已审或目录无遗漏。日期浏览前4页仅作到目标段导航；末页09-22 MEF/ByteWrist→10-09 Function Tokens→10-21科学应用→10-22 Seed3D。Blog原type2终页结果不替pubs。

本日实际完整读取[官方列表末页](seed_locale_pub80.json)中的 **Memory Retrieval and Consolidation in Large Language Models through Function Tokens** 摘要，及[arXiv原abs](https://arxiv.org/abs/2510.08203)完整题摘/版本字段，真实web响应保存为[原响应](function_tokens_abs_web.json)。推理时function tokens激活上下文中most predictive features，预训练中其后content-token loss驱动特征学习；bipartite graph与case分析可能改变“知识内容仅由content tokens承担”的解释，不能当Agent记忆模块或成熟检索原则，也不因局部机制实验排除。

原Seed PublishDate1759939200000=UTC2025-10-08 16:00/BJT10-09 00:00，但目录显示日名不能当真实首公开午夜。arXiv精确v1提交字段为Thu,9 Oct2025 13:31:20 UTC，比本窗截止晚，仍不是互联网最早公开。两字段权限不同，不据其先后捏造first-public interval、自动判窗外或准入。潜力清楚，仅日期隔离、不评分/不授正面Evidence/不做Books，定点重开需官方历史公告或完全落窗公开bounds。

必要安全反侧补读：InfoRMIA精确v1 HTML已真实下载`informia_v1.html`，实际读§4.1、§6.2 pretrained-reference条件及§7。逐token分数与sequence聚合不是同一评价；MIMIR缺理想同分布OUT reference，使用Pythia-160M早期checkpoint是受限替代；低FPR下TPR与AUC排序可反转。精确正文恢复不解决first-public，仍不归本窗、不采数字或Books，不把date hold写成无安全增量。

代表排除：[HiBob](https://openai.com/index/hibob/)RSS10-08 08:00GMT落窗；完整官方core介绍应用采用、组织维护与业务KPI，没有新系统机制/对照/失效边界，不准入。搜索触发OpenAI community用户bug帖只发现身份，不替官方技术release。

补检实际查询：`site:arxiv.org "EARL" "2510.05943" October 2025`、`site:arxiv.org "Critical attention scaling" "October" "2025"`、`site:openai.com/index/hibob "October 8, 2025"`、`site:ai.meta.com OR site:qwen.ai OR site:deepseek.com "October 8, 2025" research`。前两未恢复first-public，后两返回HiBob及无关community线索；搜索结果不当原始证据。Google历史实际页1/2已经保存，page2同URL一次curl超时后urllib成功，不隐去失败。
