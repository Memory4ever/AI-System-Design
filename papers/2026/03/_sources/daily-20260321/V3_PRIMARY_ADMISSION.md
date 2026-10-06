# 03/21 首批准入与原字段

本窗03/20T09→03/21T09+08。此处保存本日公开目录实际相交的两项潜在信号，不继承旧候选。目录日期相交不代表当窗候选。

## FlexTrain

官方Seed API `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false`、x-tt-locale US，ID1661/ArticleID1782991128267，PublishDate原值1773936000000（Unix毫秒→BJT2026-03-20T00:00，日级目录字段，不是first-public）；UpdateTime1782991144000后续更新，不归本窗。外链 `https://openreview.net/pdf?id=h2yhNcbwSL`。

完整官方Title：
 FlexTrain: Scalable Hybrid-Parallel Training with Elastic Resource Utilization and Consistent Accuracy

完整官方Abstract：
Large language model (LLM) training has become a critical workload in shared GPU clusters. However, our observations reveal that these clusters suffer from significant underutilization. To address this inefficiency, various elastic training techniques have been developed to dynamically adjust GPU allocations to harness idle resources. Despite their potential, these methods have seen limited deployment in production environments due to three major challenges: accuracy inconsistency, excessive profiling overhead, and limited flexibility. In this paper, we propose FlexTrain, an elastic training system that achieves consistent model accuracy, high training efficiency, and effective resource utilization. FlexTrain prioritizes adjustments to the pipeline parallelism (PP) degree to preserve deterministic computation and maintain accuracy consistency, while also supporting data parallelism (DP) scaling to further enhance throughput under relaxed consistency requirements. It generates optimal PP schedules, predicts training performance under different configurations, and makes scaling decisions based on job submission intervals, scaling overhead, and expected throughput gains. Evaluation results show that FlexTrain can achieve up to 1.73× speedup for elastic jobs while preserving consistent accuracy, and up to 2.27× when accuracy consistency is relaxed, compared to conventional non-elastic scheduling strategy.

作者初步准入判断：GPU弹性不应被默认当作无损计算重排；原文明确PP-only保持deterministic computation，而DP缩放只在放宽accuracy consistency时采用，并按scaling overhead/interval/throughput决定执行。该替代设计/成立边界值得核验，可能改变elastic training并行轴的选择。尚未核保证、对照、bits/optimizer/RNG状态、性能配置，1.73x/2.27x不采用为本日证据。拟映射TRAIN-PIPELINE-PARALLEL / TRAIN-DISTRIBUTED-TRAINING，但日期未确认、不评分、不作Books判断；root已认可这一潜在准入增量，未授日期或实证通过。

必要日期恢复到此停止：forum原URL返回browser challenge；原pdf web不可读；public api2 notes同identity实际HTTP403。一次官方域title补检发现同identityattachment与hashedpdf，但搜索的5 months ago是索引字段不是原发证据；实际attachment仍challenge，api2 web亦Error，不绕验证码。SeedPublishDate相交日不充分落09窗口。请求同identity可公开原note/cdate/tcdate及正文first-public/version说明，或作者原始正文可靠首公开记录；恢复日期后只审PP/DP一致性与controller命题，不无限追附件。

## MixedDimKV — 日期线索补正

Seed同一type1有限slice，ID1407/ArticleID1776932180702，PublishDate1774022400000→BJT2026-03-21T00:00，是日级目录字段；UpdateTime1776932185000是后续更新。外链https://arxiv.org/pdf/2603.20616。先前“唯一相交信号FlexTrain”的记录漏掉03/21整天与本窗00–09的相交，现明确补正，不把漏项隐藏为窗外。

完整Title：Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression

完整官方Seed/精确[v1题摘](https://arxiv.org/abs/2603.20616v1)：

Key-value (KV) caching is widely used to accelerate transformer inference, but its memory cost grows linearly with input length, limiting long-context deployment. Existing token eviction methods reduce memory by discarding less important tokens, which can be viewed as a coarse form of dimensionality reduction that assigns each token either zero or full dimension. We propose MixedDimKV, a mixed-dimension KV cache compression method that allocates dimensions to tokens at a more granular level, and MixedDimKV-H, which further integrates head-level importance information. Experiments on long-context benchmarks show that MixedDimKV outperforms prior KV cache compression methods that do not rely on head-level importance profiling. When equipped with the same head-level importance information, MixedDimKV-H consistently outperforms HeadKV. Notably, our approach achieves comparable performance to full attention on LongBench with only 6.25% of the KV cache. Furthermore, in the Needle-in-a-Haystack test, our solution maintains 100% accuracy at a 50K context length while using as little as 0.26% of the cache.

准入层作者判断：token eviction的0/full-width二元容量选择→逐token维度预算和同head-importance条件下替代方案→需要重新考虑KV压缩粒度及质量/容量取舍。并非因新比例或长上下文关键词纳入；未读方法/实现或评价条件，摘要数字不作为Evidence。若日期证实，潜在owner INFER-KV-CACHE；当前不评分、不开Books比较。

实际官方abs header完整题摘及history：唯一v1原Submitted为“Sat, 21 Mar 2026 03:21:43 UTC”，即BJT11:21:43，已在本窗09右端后；arXiv v1公开不可能早于提交，因此该arXiv事件不属于本窗。header/history未见withdrawal/correction信号，不据此遍历全史。不能把Seed目录日级字段默认为零点首公开，也不能用arXiv提交替作者早先其他渠道公开定时。

一次exact-title+author/project+March2026有界搜索只得到arXiv及ResearchGate/CatalyzeX/alphaXiv等索引，没有可靠作者原文精确首公开；这些索引不是日期证据。到此停止。若恢复作者/Seed原文first-public可靠记录且范围完整落本窗，再核粒度预算与same-head对照必要证据；若只补arXiv公告则按真实窗外归属处理。不是将该潜在贡献关闭，也不为缺日期预读全文。
