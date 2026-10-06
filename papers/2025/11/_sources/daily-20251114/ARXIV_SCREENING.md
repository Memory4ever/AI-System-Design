# 11/14 arXiv 有界筛选与停点

只记录本日实际选择，不将宽响应或月列表变成全量队列。四组主题查询的60/1/16/12为跨组命中；收窄model-training后36/36。查询、分类、submitted发现区间、start0/max100/停止start100见 [helper](arxiv_discovery.py) 与原始request。官方CL月表只浏览08700–09599这56条标题，边界见 [bounded_titles](bounded_titles.py)；没有读取全月1527项题摘。该表不能认证Thu13首次公开。

## 19个已选择信号

完整题名、完整摘要和原submitted/updated字段分别实际读于 [首批11 XML](raw-arxiv-first-exact-v1.xml)、[有界补检8 XML](raw-arxiv-bounded-exact-v1.xml)，不在这里截短摘要代替原件。前3个SAGE/SSR/WMPO已交 [新方向校准包](ARXIV_FIRST_CALIBRATION_READY.md)；以下其余增量也保留，不因日期或深审成本关闭。

| 精确v1身份 | 具体潜在增量与未证边界 |
| --- | --- |
| 2511.08798 SAGE | tool-argument联合不确定性和EVPI/问题成本；模拟用户收益不能直接推广真实用户。 |
| 2511.08854 Decomposition of Small Transformer Models | SPD因果重要度与loss适配序列，并给toy induction和GPT2组件定位；不是完整语言模型唯一机制。 |
| 2511.08877 Hallucinate or Memorize? | 100条/20域GPT4.1引用观察与citation frequency proxy；潜在知识记忆失效证据，但citation count不是已核训练频次，不能因相关性授1000阈值或记忆干扰因果。当前v2题名不同，不覆盖v1命题。 |
| 2511.08968 Bayesian Mixture of Experts | 原专家second linear layer上structured Laplace / curvature近似，而非新增adapter；校准改善、近似和开销待核，不是增加参数的通用Bayesian口号。 |
| 2511.08972 SSR | transport map同时产生选择/权重并有限使用平衡路由；需核梯度、训练推理分工和预算。 |
| 2511.09148 LoopTool | 探测具体失败、judge纠正标签、失败驱动扩展接入data-training闭环；需要隔离额外数据/轮数/judge与评测污染。 |
| 2511.09158 Efficient Reasoning via Reward Model | outcome依赖的conciseness reward回应length/training collapse；准确率和token变化需绑定baseline及奖励/理论假设。 |
| 2511.09381 Self-Correcting LLMs: Generation vs. Multiple Choice | 输出空间与任务格式改变self-correction收益/失败；局部反证可准入，不因不是新算法关闭，任务/模型条件待核。 |
| 2511.09385 AMaPO | instance-wise margin重分配正确/错误排名样本的梯度；需要核normalization与rank/对齐对照，不照录普遍稳定保证。 |
| 2511.09515 WMPO | pixel imagined轨迹承接VLA视觉接口并做on-policy GRPO；真实数据、world-model误差、contact失败与总预算保留。 |
| 2511.09516 MAP-VLA | demonstration stage memory经soft prompt调优、trajectory匹配注入冻结VLA；冻结base不等无训练，记忆检索/阶段混淆和真实长期任务条件待核。 |
| 2511.08821 BayesQ | posterior expected loss下whitening/codebook与mixed-bit预算分配；RN50/BERT局部不自动推广LLM或端到端cost。 |
| 2511.08914 SPEED-Q | vision/language量化敏感度差异下分阶段处理与蒸馏稳定低bit训练；2bit相对倍数不是绝对质量/同总预算保证。 |
| 2511.08923 TiDAR | 同一模型structured attention masks内diffusion draft与AR采样/验证及exact KV；吞吐和AR质量需核协议/hardware/预算，不从题摘授4.71–5.91倍普遍收益。 |
| 2511.08983 SpiralThinker | iterative latent更新与progressive alignment/text-latent交错，iteration/latent budget各任务不同最优；未生成文本token不等免费计算。 |
| 2511.09030 Solving a Million-Step LLM Task with Zero Errors / MAKER | 极细分任务与逐步voting纠错组合延长依赖链；Hanoi局部任务的可拆/可验证性、错误相关性和成本需要核，不推广组织级无错。 |
| 2511.09057 PAN | AR latent dynamics消费history/language action，diffusion decoder出视频；动作可控、长程一致性与物理真实性须分验，v1 Interactable与当前Actionable题名保留。 |
| 2511.09146 DoPE | truncated matrix entropy定位frequency outlier并training-free重参数化RoPE；需要核假设/原生长度/检索与推理反侧，不授普遍sink起因。 |
| 2511.09345 Seer Self-Consistency | 先用快速answer entropy估计预算，再并行System2采样；预测开销、质量口径和与顺序adaptive SC的可比性仍需核。 |

上述19个唯一家族是潜力信号而不是已确认当窗候选；未用题摘缺少实验细节作为关闭理由。当前不展开19份全文，必要首公开下界不能由submitted/一般schedule/DataCite注册独立给出。三个官方v1页、真实日期路径400和官方日列表搜索空的有限恢复见 [日期包](ARXIV_FIRST_CALIBRATION_READY.md)。其余信号共用失效的是同一个历史日列表入口，而不是机械给每项重复空路径；已保留各自精确v1原日期，原件若到达只重开对应ID。

## 当前修订/撤回信号

对19个已选ID做一次官方API identity/comment检查，见 [current signals](raw-arxiv-selected-current-signals.xml) 及request，start0/max19且返回19。没有看到撤回/纠错标记；这是当前字段轻量检查，不是没有所有修订的证明。SPD/SAGE/SSR/LoopTool/AMaPO/Spiral/Seer/DoPE有v2，PANv4，08877改题/会议版本；不因版本号或会议comment就称本日重要事件，不读晚版全文来补历史v1。

## 关闭与未扩队列

Parkinson叙述分类与GIS政治persona流程两个完整题摘理由见 [校准包](ARXIV_FIRST_CALIBRATION_READY.md)，后者明确请求抽核。标题明确的医学sleep/microaneurysm、traffic场景、spacecraft定位/运动及声学fleet属领域应用，未见主线机制或纠错信号，标题范围关闭；不称这些领域无学术价值。宽响应中的late编号/2026条目只作日期身份异常线索，不称本日论文，也不生成其他月份处理队列。

CL相关标题补检用于发现新命名机制（如TiDAR/DoPE/MAKER），不是为每个主线标题额外建立关闭单。没有称术语/标题检查全学科召回。剩余普通事项是独立准入/日期隔离核验；日期未恢复的家族不进入正面证据或Books，精确重开需要真实官方历史公告/list身份或作者原始精确发布字段，而不是更多摘要或新的搜索排名。

## 后续有限作者日期恢复

只定点恢复TiDAR/MAKER，不扩大19家族。实际三query：`site:research.nvidia.com "TiDAR" "November"`、`site:github.com/NVlabs/TiDAR "2025" "11"`、`site:starsterminal.com "MAKER" "November 13"`，见 [raw23](raw-web-23.json)；返回主要为不匹配身份，未将其他NVIDIA项目/月份纳入池。再用精确题名两query：`"TiDAR: Think in Diffusion, Talk in Autoregression" site:research.nvidia.com` 和 `"Solving a Million-Step LLM Task with Zero Errors" "November 13"`，见 [raw24](raw-web-24.json)。仅MAKER恢复了作者官方[Cognizant Blog](https://www.cognizant.com/us/en/ai-lab/blog/maker)。

该Blog实际 [GET200](raw-maker-author-blog.html.request.json)，核心见 [raw25](raw-web-25.json)；日期只显示November13,2025，无可核原生发布时间/时区。HTML中 `repo:modifyDate=2025-11-13T07:06:35Z/40Z/43Z` 属三个image/png资源，不是文章首公开。未把资源时间、作者官网日粒度或第三方当天转帖赋为完全落窗的论文首公开。Stop当前路径；若官方精确文章首发字段到达，只重开MAKER日期。

原源核心更清楚地区分atomic step、first-to-ahead-k voting、red-flag/resample和已知Hanoi计划执行，尚不支持creative planning或一般组织无错。仅记录同家族初筛增量与反侧，不用这次日期恢复偷偷完成未经校准的深入审阅，也不拿它扩为其他来源全文队列。
